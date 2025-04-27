# DVA-C02 Course

An approximate 5-week, 20-hour blended course designed for anyone to master AWS Developer Associate concepts through hands-on labs, real-world case studies, and targeted readings. Students will leave with both the credential and the practical skills necessary to excel as cloud developers.

---

## 📋 Table of Contents
1. [Course Overview](#course-overview)
2. [Learning Competencies](#learning-competencies)
3. [Prerequisites](#prerequisites)
4. [Course Structure](#course-structure)
5. [Week-by-Week Outline](#week-by-week-outline)
6. [Lab Environment & Tools](#lab-environment--tools)
7. [Mandatory Readings](#mandatory-readings)
8. [Optional Readings](#optional-readings)
9. [Repository Structure](#repository-structure)

---

## Course Overview
- **Duration:** 5 weeks (20 hours total approx.)
- **Format:** Blended micro-learning + live sessions + self-paced labs + capstone
- **Delivery:** Twice-weekly 1-hour live sessions; 1–2 hours of self-study/labs (approximately)
- **Goal:** Pass AWS Certified Developer – Associate (DVA‑C02) and gain hands-on cloud skills

---

## Learning Competencies
By the end of this course, students will be able to:

- **Design & Implement** serverless applications (Lambda, API Gateway, DynamoDB)
- **Apply** event-driven patterns (SNS, SQS, Kinesis) with idempotency and dead-letter queues
- **Enforce** security best practices (IAM least-privilege, Secrets Manager, KMS)
- **Automate** deployments via Infrastructure as Code and CI/CD pipelines (SAM, CloudFormation, CodePipeline)
- **Instrument** applications for observability (CloudWatch Logs, Metrics, X‑Ray)
- **Optimize** performance and cost (Lambda tuning, DynamoDB capacity, caching)
- **Architect** data-intensive microservices using real-world analogies and case studies
- **Collaborate** through GitHub, code reviews, and peer instruction workflows

---

## Prerequisites
- Basic programming experience (preferably in Python or JavaScript)
- Git & GitHub fundamentals
- Docker installed locally for LocalStack labs

---

## Course Structure

| Week | Live Sessions       | Topics                                    | Lab / Self-Study                        |
|------|---------------------|-------------------------------------------|-----------------------------------------|
| 0    | Onboarding (1.5 h)  | Course intro, Clean Code & DevOps theory  | Environment setup & baseline quiz       |
| 1    | Module 1A & 1B (2.5 h) | Serverless CRUD & Event-Driven Patterns   | LocalStack CRUD + SNS/SQS exercises     |
| 2    | Module 2A & 2B (2.5 h) | Security: IAM, Secrets, Encryption        | IAM role lab + Secrets Manager demo     |
| 3    | Module 3A & 3B (2.5 h) | Deployment: IaC & CI/CD, Canary Releases  | CodePipeline & blue/green strategies    |
| 4    | Module 4A & 4B (2.5 h) | Observability & Optimization              | CloudWatch Logs, X‑Ray, performance tuning |
| 5    | Capstone & Review (3 h) | Project presentations & Final Mock Exam   | Capstone deliverable & remediation plan |

---

## Week-by-Week Outline

### Week 0: Onboarding
- **Live (1.5 h)**
  - Course logistics, GitHub repo walkthrough, Slack channel
  - Clean Code essentials (Martin—pp 34–56; 57–81)
  - DevOps “Three Ways” (Phoenix Project—pp 1–48)
- **Lab**
  - Docker & LocalStack CLI install
  - GitHub Classroom activation
  - Baseline quiz on AWS fundamentals

### Week 1: Module 1 – Development with AWS Services
- **Session 1A (1 h live + 1 h lab)**
  - Pre-work: Kleppmann Ch 1 (pp 26–71) & Ch 2 (pp 72–116)
  - Case Study: Netflix click-stream ingestion
  - Lab: LocalStack CRUD API (Lambda + DynamoDB)
- **Session 1B (1 h live + 0.5 h quiz)**
  - Pre-work: Kleppmann Ch 5 (pp 198–230) & Ch 6 (pp 231–263)
  - Concepts: idempotency, retries, DLQs (SNS vs. Kinesis)
  - Quiz: 5 scenario-based questions

### Week 2: Module 2 – Security
- **Session 2A (1 h live + 1 h lab)**
  - Pre-work: AWS Well-Architected Framework, Security Pillar (pp 1–8; 15–17)
  - Hands-on: IAM least-privilege role for Lambda–DynamoDB
  - Lab: Store & rotate secrets with LocalStack Secrets Manager
- **Session 2B (1 h live + 0.5 h quiz)**
  - Pre-work: Newman Ch 9 (pp 211–240)
  - Topics: envelope encryption (KMS), ACM with API Gateway
  - Quiz: 5 questions on auth & encryption patterns

### Week 3: Module 3 – Deployment
- **Session 3A (1 h live + 1 h lab)**
  - Pre-work: Phoenix Project Ch 4–7 (pp 49–114)
  - Build: SAM template & LocalStack CodePipeline
- **Session 3B (1 h live + 0.5 h quiz)**
  - Pre-work: Accelerate Ch 4–5 (pp 89–152)
  - Workshop: canary & blue/green via Lambda aliases
  - Quiz: scenario questions on rollback & versioning

### Week 4: Module 4 – Troubleshooting & Optimization
- **Session 4A (1 h live + 1 h lab)**
  - Pre-work: SRE Ch 4 & 6 (pp 83–112; 147–176)
  - Lab: Tail CloudWatch logs & instrument X‑Ray in LocalStack
- **Session 4B (1 h live + 0.5 h quiz)**
  - Pre-work: Release It! Ch 2 (pp 45–75)
  - Exercise: Lambda cold-start profiling & caching strategies
  - Quiz: metrics, SLIs/SLOs, cost alerts

### Week 5: Capstone & Review
- **Live (3 h)**
  - Team presentations: end-to-end data-intensive microservice
  - Final mock exam (1 hr) + debrief
  - Course retrospective & next steps

---
## Lab Environment & Tools
- **Docker Compose** with LocalStack services (Lambda, API Gateway, DynamoDB, SNS, SQS, IAM, CloudWatch)
- **awslocal** CLI wrapper for AWS CLI commands
- **GitHub Classroom** assignments & GitHub Actions for CI
---

## Mandatory Readings

Note: Some of these are just gross chapter coverings, just to make sure no info is extra or less, within the week we'll have specific page ranges to read from.


| Resource                           | Chapters / Sections                | Pages       |
|------------------------------------|------------------------------------|-------------|
| Kleppmann, *Designing Data‑Intensive Applications* | Ch 1 & 2, Ch 5 & 6                   | 26–116, 198–263 |
| Martin, *Clean Code*               | Ch 1–2                              | 34–81       |
| Kim et al., *The Phoenix Project*  | Ch 1–3 & Ch 2’s First Way concepts  | 1–48        |
| AWS Well-Architected Framework     | Security Pillar Intro & Principles  | 1–8; 15–17  |
| Newman, *Building Microservices*   | Ch 1 & Ch 4                         | 1–26; 85–115|
| Google SRE, *Site Reliability Engineering* | Ch 4 & Ch 6                          | 83–112; 147–176 |
| Forsgren et al., *Accelerate*      | Ch 4 & Ch 5                         | 89–152      |
| Kim et al., *The DevOps Handbook*  | Part III & IV                       | 167–237     |
| Nygard, *Release It!*              | Ch 2                                | 45–75       |
| Wiggins, *The Twelve-Factor App*   | Factor 3 & 4 (PDF sections)         | Config & Backing Services |

---

## Optional Readings
- Humble & Farley, *Continuous Delivery* – Pipeline & automation (select chapters)
- Fowler, *Patterns of Enterprise Application Architecture* – Data access patterns
- Google SRE Team, *Site Reliability Workbook* – Exercises on SLOs & monitoring
- DORA State of DevOps Reports – Key capabilities & metrics

---

## Repository Structure
```plaintext
├── README.md           # (this file)
├── labs/               # LocalStack lab instructions & code
│   ├── lab1-crud/      # Serverless CRUD API
│   ├── lab2-events/    # SNS → SQS → Lambda
│   ├── lab3-security/  # IAM & Secrets Manager
│   └── lab4-observability/ # CloudWatch & X-Ray
├── readings/           # PDFs & links for mandatory & optional readings
├── slides/             # Slide decks (per session)
├── quizzes/            # Weekly quiz files
├── capstone/           # Capstone project template
└── .github/
    └── workflows/      # CI for labs & quizzes
```

