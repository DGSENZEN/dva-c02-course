# test_lab1.py
import pytest
import boto3
import json
import os
import logging
import time

# --- Configuration ---
LAMBDA_FUNCTION_NAME = "InventoryStatusChecker"
AWS_ENDPOINT_URL = os.environ.get("AWS_ENDPOINT_URL", "http://localhost:4566")
KNOWN_LOW_STOCK_PART_ID = "abc-123"
KNOWN_NORMAL_STOCK_PART_ID = "xyz-789"
KNOWN_UNKNOWN_PART_ID = "unknown-part-001" 
EXPECTED_LOW_STOCK_THRESHOLD = 10 
DEFAULT_STOCK_LEVEL = 25 

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# --- Fixtures ---
@pytest.fixture(scope="module")
def lambda_client():
    """Creates a Boto3 client configured for LocalStack."""
    logger.info(f"Creating Boto3 client for Lambda targeting {AWS_ENDPOINT_URL}")
    try:
        client = boto3.client(
            "lambda",
            endpoint_url=AWS_ENDPOINT_URL,
            region_name="us-east-1",
            aws_access_key_id="test",
            aws_secret_access_key="test",
        )
        # Basic check to see if LocalStack is reachable
        client.list_functions(MaxItems=1)
        logger.info("Boto3 client created successfully.")
        return client
    except Exception as e:
        logger.error(
            f"Failed to create Boto3 client or connect to LocalStack: {e}",
            exc_info=True,
        )
        pytest.fail(
            f"Could not connect to LocalStack Lambda at {AWS_ENDPOINT_URL}. "
            f"Is LocalStack running with lambda service? Error: {e}"
        )


# --- Helper Function ---
def invoke_lambda(lambda_client, payload):
    """Invokes the Lambda function and returns the parsed response."""
    logger.info(f"Invoking {LAMBDA_FUNCTION_NAME} with payload: {json.dumps(payload)}")
    try:
        response = lambda_client.invoke(
            FunctionName=LAMBDA_FUNCTION_NAME,
            InvocationType="RequestResponse",
            Payload=json.dumps(payload).encode("utf-8"),
        )
        logger.info(f"Raw Lambda response status code: {response.get('StatusCode')}")

        response_payload_bytes = response["Payload"].read()
        response_payload_str = response_payload_bytes.decode("utf-8")
        logger.info(f"Raw Lambda response payload: {response_payload_str}")

        # Check for function errors reported by Lambda itself (e.g., unhandled exceptions)
        if response.get("FunctionError"):
            error_info = {
                "error_type": response["FunctionError"],
                "payload": response_payload_str,
            }
            logger.error(f"Lambda function execution reported an error: {error_info}")
            pytest.fail(f"Lambda function execution failed: {error_info}")

        # Parse the JSON string returned by our function's code
        parsed_response = json.loads(response_payload_str)
        logger.info(f"Parsed Lambda response payload: {parsed_response}")
        return parsed_response

    except json.JSONDecodeError as e:
        logger.error(
            f"Failed to decode JSON response from Lambda: {response_payload_str}",
            exc_info=True,
        )
        pytest.fail(f"Lambda response was not valid JSON: {e}")
    except Exception as e:
        logger.error(
            f"Failed to invoke Lambda function '{LAMBDA_FUNCTION_NAME}': {e}",
            exc_info=True,
        )
        pytest.fail(f"Failed to invoke Lambda function '{LAMBDA_FUNCTION_NAME}': {e}")


# --- Test Functions ---


@pytest.mark.main_objective(1)
def test_lambda_function_exists(lambda_client):
    """Objective 1: Verifies the Lambda function was created."""
    logger.info(f"Checking existence of Lambda function: {LAMBDA_FUNCTION_NAME}")
    try:
        lambda_client.get_function(FunctionName=LAMBDA_FUNCTION_NAME)
        logger.info(f"Lambda function '{LAMBDA_FUNCTION_NAME}' found.")
    except lambda_client.exceptions.ResourceNotFoundException:
        logger.error(f"Lambda function '{LAMBDA_FUNCTION_NAME}' not found.")
        pytest.fail(f"Lambda function '{LAMBDA_FUNCTION_NAME}' not found.")
    except Exception as e:
        logger.error(f"Error checking for Lambda function: {e}", exc_info=True)
        pytest.fail(f"Error checking for Lambda function: {e}")


@pytest.mark.main_objective(2)
def test_low_stock_part_id(lambda_client):
    """Objective 2: Tests invocation with a known low stock part ID."""
    payload = {"part_id": KNOWN_LOW_STOCK_PART_ID}
    response = invoke_lambda(lambda_client, payload)

    assert response.get("statusCode") == 200, "Response statusCode should be 200"
    assert "body" in response, "Response missing 'body'"
    body = json.loads(response["body"])  # Body is a JSON string

    assert "partId" in body, "Response body missing 'partId'"
    assert "isLowStock" in body, "Response body missing 'isLowStock'"
    assert body["partId"] == KNOWN_LOW_STOCK_PART_ID, f"Response body 'partId' mismatch"
    assert isinstance(body["isLowStock"], bool), "'isLowStock' should be a boolean"
    assert (
        body["isLowStock"] is True
    ), f"Part ID '{KNOWN_LOW_STOCK_PART_ID}' should be low stock (True)"
    logger.info("Low stock part ID test passed.")


@pytest.mark.main_objective(3)
def test_normal_stock_part_id(lambda_client):
    """Objective 3: Tests invocation with a known normal stock part ID."""
    payload = {"part_id": KNOWN_NORMAL_STOCK_PART_ID}
    response = invoke_lambda(lambda_client, payload)

    assert response.get("statusCode") == 200, "Response statusCode should be 200"
    assert "body" in response, "Response missing 'body'"
    body = json.loads(response["body"])

    assert "partId" in body, "Response body missing 'partId'"
    assert "isLowStock" in body, "Response body missing 'isLowStock'"
    assert (
        body["partId"] == KNOWN_NORMAL_STOCK_PART_ID
    ), f"Response body 'partId' mismatch"
    assert isinstance(body["isLowStock"], bool), "'isLowStock' should be a boolean"
    assert (
        body["isLowStock"] is False
    ), f"Part ID '{KNOWN_NORMAL_STOCK_PART_ID}' should NOT be low stock (False)"
    logger.info("Normal stock part ID test passed.")


@pytest.mark.main_objective(4)
def test_missing_part_id_error(lambda_client):
    """Objective 4: Tests invocation with missing 'part_id' key."""
    payload = {"some_other_key": "some_value"}  # Missing part_id
    response = invoke_lambda(lambda_client, payload)

    assert (
        response.get("statusCode") == 400
    ), "Response statusCode should be 400 for missing part_id"
    assert "body" in response, "Response missing 'body'"
    body = json.loads(response["body"])

    assert (
        "error" in body
    ), "Response body should contain an 'error' key for bad requests"
    assert (
        "Missing 'part_id'" in body["error"]
    ), "Error message should indicate missing part_id"
    logger.info("Missing part ID error test passed.")


# Optional Test
def test_unknown_part_id_default_stock(lambda_client):
    """Tests invocation with an unknown part ID, expecting default stock level."""
    payload = {"part_id": KNOWN_UNKNOWN_PART_ID}
    response = invoke_lambda(lambda_client, payload)

    assert response.get("statusCode") == 200, "Response statusCode should be 200"
    assert "body" in response, "Response missing 'body'"
    body = json.loads(response["body"])

    assert "partId" in body, "Response body missing 'partId'"
    assert "isLowStock" in body, "Response body missing 'isLowStock'"
    assert "currentStock" in body, "Response body missing 'currentStock'"
    assert body["partId"] == KNOWN_UNKNOWN_PART_ID, f"Response body 'partId' mismatch"
    assert (
        body["currentStock"] == DEFAULT_STOCK_LEVEL
    ), f"Stock for unknown part should be default ({DEFAULT_STOCK_LEVEL})"
    # Check if default stock is low or not based on threshold
    expected_low_stock = DEFAULT_STOCK_LEVEL < EXPECTED_LOW_STOCK_THRESHOLD
    assert (
        body["isLowStock"] is expected_low_stock
    ), f"isLowStock mismatch for default stock level"
    logger.info("Unknown part ID test passed.")
