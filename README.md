# DVA-C02 Course: Cloud Developer Accelerator

**An approximate 5-week, 20-hour blended course designed for developers to master AWS Developer Associate concepts through hands-on Katas & Labs, real-world case studies, and targeted readings. Students will leave with both the credential and the practical skills necessary to excel as cloud developers.**


## 📋 Table of Contents
1.  [Course Overview](#course-overview)
2.  [Learning Competencies](#learning-competencies)
3.  [Prerequisites](#prerequisites)
4.  [Course Structure](#course-structure)
5.  [Week-by-Week Outline](#week-by-week-outline)
6.  [Lab Environment & Tools](#lab-environment--tools)
7.  [Mandatory Readings](#mandatory-readings)
8.  [Optional Readings](#optional-readings)
9.  [Repository Structure](#repository-structure)


## Course Overview
*   **Duration:** 5 weeks (approx. 20 hours total: 10h live + 10h self-study/labs)
*   **Format:** Blended micro-learning + live sessions + self-paced Katas & Labs + capstone
*   **Delivery:** Twice-weekly 1-hour live sessions; ~2 hours of self-study/labs per week
*   **Goal:** Pass AWS Certified Developer – Associate (DVA‑C02) and gain hands-on cloud development skills using Python, LocalStack, and AWS services.


## Learning Competencies
By the end of this course, students will be able to:

*   **Implement & Refactor** code using Clean Code principles in an AWS context.
*   **Design & Implement** serverless CRUD APIs and data handling patterns (Lambda, API Gateway, DynamoDB).
*   **Apply** event-driven patterns using SNS, SQS, considering idempotency and error handling (DLQs).
*   **Enforce** security best practices: IAM least-privilege roles, secure secret management (Secrets Manager), and encryption concepts (KMS).
*   **Automate** deployments using Infrastructure as Code (AWS SAM) and basic CI/CD concepts.
*   **Implement** safe deployment strategies (Lambda Aliases, Blue/Green, Canary).
*   **Instrument** applications for observability using CloudWatch (Logs, Metrics, Alarms) and AWS X-Ray.
*   **Apply** stability patterns and basic optimization techniques (Circuit Breaker concept, Lambda tuning).
*   **Architect** solutions drawing analogies from real-world case studies (e.g., Parts Unlimited, Netflix, Amazon).
*   **Collaborate** via GitHub and test code using automated test suites (`pytest`).

---

## Prerequisites
*   Basic programming experience (Python required for labs).
*   Git & GitHub fundamentals.
*   Docker installed locally for LocalStack labs.
*   Python 3, `pip`, `boto3`, and `pytest` installed locally.



## Course Structure

| Week | Live Sessions (2x 1h) | Topics                                       | Lab / Self-Study (~2h)                                       |
| :--- | :-------------------- | :------------------------------------------- | :----------------------------------------------------------- |
| 0    | Onboarding            | Course Intro, Clean Code, DevOps 3 Ways      | Env Setup (Docker, LocalStack, Python tools), Kata 1, Lab 1 (Clean Lambda) |
| 1    | Module 1A & 1B        | Data Models, DynamoDB CRUD, Event Patterns   | Kata 2 (DynamoDB), Lab 2 (Event Handling: SNS/SQS)           |
| 2    | Module 2A & 2B        | Security: IAM, Secrets, Encryption Concepts  | Kata 3 (Secrets), Lab 3 (IAM Role & Secrets Integration)     |
| 3    | Module 3A & 3B        | Deployment: IaC (SAM), CI/CD, Safe Deploys   | Lab 4 (SAM Template), Kata 4 (Alias Deploy), Lab 5 (Canary)  |
| 4    | Module 4A & 4B        | Observability, Optimization, Stability       | Kata 5 (Logging), Lab 6 (Metrics, Alarms, X-Ray, Stability) |
| 5    | Capstone & Review     | Project Showcase, Final Mock Exam, 3rd Way | Capstone Project Implementation & Course Retrospective       |



## Week-by-Week Outline

### Week 0: Onboarding & Foundations
*   **Live (1 h):**
    *   Course logistics, GitHub repo.
    *   **Guided Exercise:** Walkthrough/Demo of Kata 1 (Clean Code Refactoring).
*   **Lab / Self-Study (~2 h):**
    *   **Environment Setup:** Install Docker, Python 3, `pip`, `boto3`, `pytest`. Clone repo. Set up `awslocal` alias. Start LocalStack via `docker compose`.
    *   **Kata 1:** Complete the Clean Code refactoring exercise (if not done live).
    *   **Lab 1:** Implement the "Inventory Status" Lambda function (`inventory_status_lambda.py` starter code), deploy to LocalStack, and verify using the provided `pytest` suite (`test_lab1.py`).
    *   **Case Study Context:** Think of this initial work as improving legacy code and basic deployment flow at "Parts Unlimited" (*The Phoenix Project*).
    *   Baseline quiz on AWS fundamentals (optional).

### Week 1: Module 1 – Development with AWS Services
*   **Session 1A (1 h live):**
    *   **Pre-work:** Kleppmann Ch 1 (Reliable, Scalable, Maintainable) & Ch 2 (Data Models).
    *   **Topics:** Data Modeling (SQL vs NoSQL), DynamoDB Core Concepts (Tables, Items, Keys, Attributes), CRUD Operations.
    *   **Case Study:** Netflix Click-Stream Ingestion (High-volume writes/reads, schema flexibility needs).
*   **Lab / Self-Study (~1 h):**
    *   **Kata 2:** Implement DynamoDB `put-item` and `get-item` operations for "Parts Unlimited" orders (`order_manager.py` starter code).
    *   *(Optional Extension):* Add `update-item` functionality to Kata 2.
*   **Session 1B (1 h live):**
    *   **Pre-work:** Newman Ch 4 (Integration Patterns). Review AWS Docs: SNS Overview, SQS Overview, Lambda Event Source Mapping.
    *   **Topics:** Event-Driven Architectures, Decoupling (SQS), Fan-out (SNS), Idempotency, Retries, Dead-Letter Queues (DLQs).
    *   **Case Study:** Amazon Order Processing (Order placement triggers decoupled inventory, shipping, notification events via SNS/SQS).
*   **Lab / Self-Study (~1 h):**
    *   **Lab 2:** Create an SQS queue and SNS topic in LocalStack. Modify Lab 1's Lambda (or create a new one) to publish a message to SNS upon successful processing. Create a second Lambda triggered by SQS (subscribed to the SNS topic) to log the message. Test the flow.
    *   Quiz: Scenario-based questions on event patterns.

### Week 2: Module 2 – Security
*   **Session 2A (1 h live):**
    *   **Pre-work:** AWS Well-Architected Framework, Security Pillar
    *   **Topics:** IAM Principles (Least Privilege), Roles vs Users, Policies, Secure Configuration & Secrets Management (Secrets Manager vs Parameter Store).
    *   **Case Study:** Protecting Financial Service Credentials (e.g., storing/rotating Stripe API keys securely).
*   **Lab / Self-Study (~1 h):**
    *   **Kata 3:** Implement fetching a secret from LocalStack Secrets Manager (`shipping_client.py` starter code).
    *   **Lab 3:** Define an IAM policy JSON granting specific DynamoDB access (e.g., `PutItem`, `GetItem` on the `Orders` table). Create an IAM role using `awslocal` and attach the policy. Modify the Lambda deployment (Lab 1 or 2) to use this role ARN. Verify access (conceptual in LocalStack, focus on resource definition).
*   **Session 2B (1 h live):**
    *   **Pre-work:** Newman Ch 9 (Securing Services). Review AWS Docs: KMS Concepts, ACM Overview.
    *   **Topics:** Encryption in Transit (HTTPS/TLS, ACM with API Gateway/ALB), Encryption at Rest (Server-Side Encryption), Envelope Encryption (KMS).
    *   **Case Study:** Securing Healthcare Data (Meeting HIPAA compliance via encryption).
*   **Lab / Self-Study (~1 h):**
    *   **Demo/Conceptual Lab:** Use `awslocal kms create-key`. Discuss how the KMS Key ARN is used in other services (e.g., S3 bucket policy, DynamoDB SSE). Briefly demo creating an API Gateway endpoint for a Lambda function (manual setup via `awslocal`). Discuss where ACM would fit.
    *   Quiz: Questions on authentication, authorization, and encryption patterns.

### Week 3: Module 3 – Deployment
*   **Session 3A (1 h live):**
    *   **Pre-work:** Review AWS Docs: SAM Introduction. *DevOps Handbook* Part III (CI Practices).
    *   **Topics:** Infrastructure as Code (IaC) benefits, AWS SAM (`template.yaml`, `sam build`, `sam deploy`), Basic CI/CD pipeline stages.
    *   **Case Study:** Automating E-commerce Platform Updates (e.g., Etsy's deployment pipeline enabling frequent, reliable releases).
*   **Lab / Self-Study (~1 h):**
    *   **Lab 4:** Create a `template.yaml` file defining the Lab 1 Lambda function and the Kata 2 `Orders` DynamoDB table. Use `sam build` and `sam deploy --guided` (or `awslocal cloudformation deploy`) to deploy the stack to LocalStack. Verify resources are created.
*   **Session 3B (1 h live):**
    *   **Pre-work:** *Accelerate* Ch 4 (CI/CD) & Ch 5 (Architecture for CD).
    *   **Topics:** Deployment Strategies (All-at-once, Rolling, Blue/Green, Canary), Lambda Versions & Aliases, Traffic Shifting.
    *   **Case Study:** Rolling out Mobile App Backend Features Safely (e.g., Facebook app updates using canary releases).
*   **Lab / Self-Study (~1 h):**
    *   **Kata 4:** Manually practice Lambda deployment steps: `update-function-code`, `publish-version`, `update-alias`.
    *   **Lab 5:** Extend Kata 4. Use `awslocal lambda update-alias --routing-config` to perform a weighted canary deployment (e.g., 10% traffic to new version). Simulate invoking the alias multiple times to see traffic distribution (conceptual). Discuss rollback.
    *   Quiz: Scenario questions on deployment strategies, rollback & versioning.

### Week 4: Module 4 – Troubleshooting & Optimization
*   **Session 4A (1 h live):**
    *   **Pre-work:** SRE Ch 4 (SLOs) & Ch 6 (Monitoring). Review AWS Docs: CloudWatch & X-Ray Overviews.
    *   **Topics:** Observability Pillars (Logs, Metrics, Traces), SLIs/SLOs, CloudWatch Logs (Structured Logging), Metrics (Standard vs Custom), Alarms, AWS X-Ray basics.
    *   **Case Study:** Debugging Performance in a Ride-Sharing App (e.g., Uber/Lyft - tracing requests across microservices to find bottlenecks).
*   **Lab / Self-Study (~1 h):**
    *   **Kata 5:** Modify the Lab 1 Lambda to output structured JSON logs.
    *   **Lab 6 (Part 1 - Observability):** Add a custom CloudWatch metric (`put_metric_data`) for "Orders Processed" to a relevant Lambda. Create a CloudWatch Alarm (`put_metric_alarm`) that triggers if Lambda errors (standard metric) exceed a threshold. (Optional: Add basic X-Ray SDK instrumentation to the Lambda). View logs, metrics (conceptual graph), and alarm state via `awslocal`.
*   **Session 4B (1 h live):**
    *   **Pre-work:** *Release It!* Ch 2 (Stability Patterns). Review AWS Lambda Performance Tuning guides.
    *   **Topics:** Lambda Performance (Cold Starts, Memory Tuning), Provisioned Concurrency, Stability Patterns (Circuit Breaker concept), Caching Strategies (briefly), Dev/Prod Parity importance.
    *   **Case Study:** Handling Black Friday Traffic Spikes (e.g., Amazon retail - scaling, caching, preventing cascading failures).
*   **Lab / Self-Study (~1 h):**
    *   **Lab 6 (Part 2 - Stability/Optimization):** Write a Python code snippet demonstrating the core logic of a Circuit Breaker state machine (no AWS integration needed). Analyze Lambda logs/metrics from previous steps to discuss cold starts. Use `awslocal lambda put-provisioned-concurrency-config` to apply PC to a function and discuss its impact. Discuss where caching could improve the lab architecture.
    *   Quiz: Questions on metrics, SLIs/SLOs, stability patterns, performance tuning.

### Week 5: Capstone & Review
*   **Live (3 h total):**
    *   **Capstone Showcase (1.5 h):** Teams briefly present their capstone project implementation.
    *   **Final Mock Exam (1 h):** DVA-C02 style questions.
    *   **Debrief & Retrospective (0.5 h):** Review mock exam answers. Discuss the Third Way (Culture of Experimentation - *DevOps Handbook* Part V, *Accelerate* Ch 10). Course retrospective & next steps.
*   **Lab / Self-Study (Deliverable):**
    *   **Capstone Project:** Implement a small, defined microservice application combining elements from previous labs (e.g., API Gateway -> Lambda (CRUD) -> DynamoDB, with another Lambda triggered by DynamoDB Streams or SQS, deployed via SAM, including basic security and logging). Submit GitHub repo link.

---

## Lab Environment & Tools
*   **Docker Compose** with LocalStack services (Lambda, API Gateway, DynamoDB, SNS, SQS, IAM, CloudWatch, Secrets Manager, CloudFormation, STS, SSM)
*   **`awslocal`** CLI wrapper for AWS CLI commands
*   **Python 3** with **Boto3** SDK
*   **AWS SAM CLI** for Infrastructure as Code
*   **`pytest`** for running automated lab checks
*   **Git & GitHub** for version control and collaboration


## Mandatory Readings

*(Specific page ranges or sections may be assigned weekly)*

| Resource                                     | Relevant Weeks (Primary Focus) |
| :------------------------------------------- | :----------------------------- |
| Martin, *Clean Code*                         | 0                              |
| Kim et al., *The Phoenix Project*            | 0, 3                           |
| Kleppmann, *Designing Data‑Intensive Apps*   | 1                              |
| Newman, *Building Microservices*             | 1, 2                           |
| AWS Well-Architected Framework               | 2                              |
| Wiggins, *The Twelve-Factor App*             | 2, 4                           |
| *The DevOps Handbook*                        | 3, 5                           |
| Forsgren et al., *Accelerate*                | 3, 5                           |
| SRE (Google), *Site Reliability Engineering* | 4                              |
| Nygard, *Release It!*                        | 4                              | 


## Optional Readings
*   Humble & Farley, *Continuous Delivery* – Pipeline & automation details
*   Fowler, *Patterns of Enterprise Application Architecture* – Data access patterns
*   Google SRE Team, *Site Reliability Workbook* – Exercises on SLOs & monitoring
*   DORA State of DevOps Reports – Key capabilities & metrics

