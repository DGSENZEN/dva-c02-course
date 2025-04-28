# inventory_status_lambda.py - STARTER CODE
import json
import logging

# Configure basic logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# --- Constants (Use these in your logic) ---
LOW_STOCK_THRESHOLD = 10
KNOWN_PART_STOCK = {
    "abc-123": 5,  # Example low stock item
    "xyz-789": 50,  # Example normal stock item
    "def-456": 8,  # Another low stock item
}
DEFAULT_STOCK_LEVEL = 25  # Stock level for unknown parts


# --- Helper Functions (Implement these) ---


def get_inventory_level(part_id):
    """
    Implement this function:
    - It should take a 'part_id' string.
    - Look up the part_id in the KNOWN_PART_STOCK dictionary.
    - If found, return the corresponding stock level (int).
    - If not found, return the DEFAULT_STOCK_LEVEL.
    - Add a logger.info message indicating the part_id and the stock level returned.
    """
    logger.info(f"TODO: Implement get_inventory_level for part ID '{part_id}'")
    # --- Your Code Here ---
    stock_level = DEFAULT_STOCK_LEVEL  # Replace this placeholder logic
    # --- End Your Code ---
    return stock_level


def is_low_stock(stock_level):
    """
    Implement this function:
    - It should take a 'stock_level' integer.
    - Compare it against the LOW_STOCK_THRESHOLD constant.
    - Return True if stock_level is less than the threshold, False otherwise.
    """
    logger.info("TODO: Implement is_low_stock")
    # --- Your Code Here ---
    result = False  # Replace this placeholder logic
    # --- End Your Code ---
    return result


# --- Main Lambda Handler (Implement the core logic) ---


def lambda_handler(event, context):
    """
    Implement the main logic for this handler:
    1. Log the received event.
    2. Extract the 'part_id' from the 'event' dictionary safely (handle missing key).
       - If 'part_id' is missing, log an error and return a 400 Bad Request response:
         {'statusCode': 400, 'body': json.dumps({'error': "Missing 'part_id' in request body"})}
    3. Call the 'get_inventory_level' helper function with the extracted part_id.
    4. Call the 'is_low_stock' helper function with the stock level obtained from step 3.
    5. Construct the success response body dictionary containing:
       - 'partId': The requested part_id.
       - 'currentStock': The stock level obtained from step 3.
       - 'isLowStock': The boolean result from step 4.
    6. Log the final result (e.g., part ID and low stock status).
    7. Return a 200 OK success response containing the response body (JSON stringified):
       {'statusCode': 200, 'body': json.dumps(response_body)}
    8. (Optional but Recommended) Add a basic try/except block around the core logic (steps 3-7)
       to catch unexpected errors and return a 500 Internal Server Error response.
    """
    logger.info(f"Received event: {json.dumps(event)}")
    logger.info("TODO: Implement lambda_handler logic")

    response_body = {}
    status_code = 501  # Not Implemented (default)

    # --- Your Code Here ---
    # Hint: Use event.get('part_id') for safe extraction.
    # Remember to handle the case where part_id is None or empty.
    # Call your helper functions.
    # Build the response_body dictionary.
    # Set the correct status_code (200 for success, 400 for missing part_id).
    # --- End Your Code ---

    # Return the final HTTP response object
    return {"statusCode": status_code, "body": json.dumps(response_body)}
