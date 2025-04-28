# Lab 1: Building & Deploying a Simple "Inventory Status" Lambda

**Objective:** Apply clean code principles to **create** a simple AWS Lambda function from requirements, deploy it to a local AWS environment (LocalStack), test its invocation manually, and understand how code clarity impacts the development workflow (Flow).

**Time Estimate:** 45-60 minutes

---

## Prerequisites

Before starting this lab, ensure you have the following installed and configured:

1. **Docker & Docker Compose:** Required to run LocalStack. Download from [Docker's website](https://www.docker.com/products/docker-desktop/). Ensure the Docker daemon is running. Use `docker compose` (with a space) command.
2. **Python 3:** Required for writing the Lambda function. Download from [python.org](https://www.python.org/). `pip` should also be available.
3. **AWS CLI:** Required for interacting with LocalStack's AWS simulation. Install instructions [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
4. **`awslocal` Alias (Highly Recommended):** To avoid typing `--endpoint-url=http://localhost:4566` for every command, set up a shell alias. Add this line to your shell profile (`~/.bashrc`, `~/.zshrc`, `~/.bash_profile`, etc.):

   ```bash
   alias awslocal='aws --endpoint-url=http://localhost:4566'
   ```

   _Remember to restart your terminal or run `source ~/.your_profile_file` after adding the alias._ If you don't set this up, you **must** add `--endpoint-url=http://localhost:4566` to every `aws` command targeting LocalStack.

---

## Setting up the Local AWS Environment (LocalStack)

1. **Create Lab Directory:** Create a new directory for this lab work.

   ```bash
   mkdir aws-dev-lab1
   cd aws-dev-lab1
   ```

2. **Create `docker-compose.yml`:** Inside the `aws-dev-lab1-impl` directory, create a file named `docker-compose.yml` and paste the following content into it:

   ```yaml
   # docker-compose.yml
   version: "3.8"
   services:
     localstack:
       container_name: localstack_main
       image: localstack/localstack:latest
       ports:
         - "127.0.0.1:4566:4566"
       environment:
         - SERVICES=lambda,iam,dynamodb,sqs,sns,s3,secretsmanager,cloudwatch,sts,apigateway,ssm
         - DOCKER_HOST=unix:///var/run/docker.sock
         - PERSISTENCE=1
       volumes:
         - "./localstack_data:/var/lib/localstack"
         - "/var/run/docker.sock:/var/run/docker.sock"
   ```

3. **Start LocalStack:** Make sure you are inside the `aws-dev-lab1` directory in your terminal and run:

   ```bash
   docker compose up -d
   ```

4. **Verify LocalStack:** Wait about 30-60 seconds for initialization. Check if the container is running:

   ```bash
   docker ps
   # You should see 'localstack_main' listed.
   curl http://localhost:4566/_localstack/health
   # Should return JSON showing running services.
   ```

---

## Lab Steps

### Step 1: Create the Lambda Function Code

1. Inside your `aws-dev-lab1` directory, create a new file named `inventory_status_lambda.py`.
2. **Your Task:** Write the Python code for the Lambda function in this file. The function must meet the following requirements:
   - **Import necessary libraries** (`json`, `logging`).
   - **Configure basic logging.**
   - **Define Constants:**
     - `LOW_STOCK_THRESHOLD = 10`
     - `KNOWN_PART_STOCK = {"abc-123": 5, "xyz-789": 50, "def-456": 8}` (A dictionary simulating known stock levels)
     - `DEFAULT_STOCK_LEVEL = 25` (Stock level for parts not in the dictionary)
   - **Implement Helper Function `get_inventory_level(part_id)`:**
     - Takes a `part_id` string as input.
     - Looks up the `part_id` in the `KNOWN_PART_STOCK` dictionary.
     - Returns the corresponding stock level if found, otherwise returns `DEFAULT_STOCK_LEVEL`.
     - Logs the part ID and the stock level being returned.
   - **Implement Helper Function `is_low_stock(stock_level)`:**
     - Takes a `stock_level` integer as input.
     - Returns `True` if `stock_level` is less than `LOW_STOCK_THRESHOLD`, otherwise returns `False`.
   - **Implement Main Handler Function `lambda_handler(event, context)`:**
     - Logs the received `event`.
     - Safely extracts the `part_id` from the `event` dictionary (e.g., using `event.get('part_id')`).
     - **Error Handling:** If `part_id` is missing or empty, log an error and return an HTTP 400 response: `{'statusCode': 400, 'body': json.dumps({'error': "Missing 'part_id' in request body"})}`.
     - If `part_id` is present, call `get_inventory_level` to get the stock.
     - Call `is_low_stock` with the obtained stock level.
     - Construct a success response body dictionary containing `partId`, `currentStock`, and `isLowStock` keys with their respective values.
     - Log the result (e.g., part ID and low stock status).
     - Return an HTTP 200 response: `{'statusCode': 200, 'body': json.dumps(response_body)}`.
     - _(Optional but recommended: Wrap the main logic in a `try...except` block for robustness)._
   - **Clean Code:** Use meaningful variable names and ensure your code is well-commented or self-explanatory.

### Step 2: Prepare Deployment Package

1. Once you have written the code in `inventory_status_lambda.py`, create a zip file containing it:

   ```bash
   zip inventory_status_deployment.zip inventory_status_lambda.py
   ```

### Step 3: Define Dummy IAM Role ARN

1. Define the dummy role ARN in your terminal (use the correct syntax for your OS - Bash/Zsh shown):

   ```bash
   ROLE_ARN="arn:aws:iam::000000000000:role/lambda-dummy-role"
   ```

### Step 4: Deploy to LocalStack

1. Use the `awslocal` command to create the Lambda function using your code:

   ```bash
   # Try creating first:
   awslocal lambda create-function \
     --function-name InventoryStatusChecker \
     --runtime python3.9 \
     --role $ROLE_ARN \
     --handler inventory_status_lambda.lambda_handler \
     --zip-file fileb://inventory_status_deployment.zip

   # If create failed with ResourceConflictException, update the code:
   # awslocal lambda update-function-code \
   #  --function-name InventoryStatusChecker \
   #  --zip-file fileb://inventory_status_deployment.zip
   ```

2. Wait a few seconds for the deployment.

### Step 5: Manual Testing & Verification

You **must** test your deployed function to ensure it works correctly.

1. **Low Stock Case:**

   - Create an `event.json` file: `echo '{"part_id": "abc-123"}' > event.json`
   - Invoke: `awslocal lambda invoke --function-name InventoryStatusChecker --payload file://event.json output.json`
   - Verify `output.json`: `cat output.json`
   - **Expected Output:** `{"statusCode": 200, "body": "{\"partId\": \"abc-123\", \"currentStock\": 5, \"isLowStock\": true}"}`

2. **Normal Stock Case:**

   - Update `event.json`: `echo '{"part_id": "xyz-789"}' > event.json`
   - Invoke: `awslocal lambda invoke --function-name InventoryStatusChecker --payload file://event.json output.json`
   - Verify `output.json`: `cat output.json`
   - **Expected Output:** `{"statusCode": 200, "body": "{\"partId\": \"xyz-789\", \"currentStock\": 50, \"isLowStock\": false}"}`

3. **Missing Part ID Case:**

   - Update `event.json`: `echo '{"other_key": "value"}' > event.json`
   - Invoke: `awslocal lambda invoke --function-name InventoryStatusChecker --payload file://event.json output.json`
   - Verify `output.json`: `cat output.json`
   - **Expected Output:** `{"statusCode": 400, "body": "{\"error\": \"Missing 'part_id' in request body\"}"}`

4. **Troubleshooting:** If your output does not match the expected output, review your Python code in `inventory_status_lambda.py`, fix any issues, re-zip the file (Step 2), update the function code (`awslocal lambda update-function-code ...`), and repeat the manual tests. You can also check the Lambda logs using `awslocal logs ...` commands (see previous lab versions for examples) to help debug.

---

## Reflection

Consider these questions based on the lab and the course readings:

1. How did breaking the required logic into smaller, well-named functions (`get_inventory_level`, `is_low_stock`) help you structure your code for the main `lambda_handler`? (_Clean Code_)
2. Imagine this Lambda function was much more complex. How would writing unclear code (poor names, long functions, magic numbers) slow down development and debugging? How does this relate to "Flow"? (_The Phoenix Project_)
3. How does the repeatable deployment process (zip, `awslocal lambda create/update-function`) contribute to improving Flow compared to manual deployment steps?

---

## Cleanup

When you are finished, stop and remove the LocalStack container:

1. Navigate back to the `aws-dev-lab1-impl` directory in your terminal.
2. Run:

   ```bash
   docker compose down
   ```
