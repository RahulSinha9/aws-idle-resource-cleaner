# 🧹 AWS Idle Resource Cleaner

> **Find wasted AWS capacity before it becomes a wasted AWS bill.**

AWS environments accumulate forgotten resources: unattached EBS volumes, unused Elastic IPs, underutilized EC2 instances, and load balancers receiving little or no traffic.

**AWS Idle Resource Cleaner** is a **read-only AWS FinOps scanner** that discovers these resources, evaluates utilization, ranks cleanup opportunities, and estimates potential monthly savings — without making destructive changes.

---

## 🚀 Why This Project?

Cloud cost optimization is not only about finding the biggest AWS bill.

It is about answering:

```text
What is running?
        ↓
Is it actually being used?
        ↓
How much could it cost?
        ↓
Should we investigate or remove it?
```

This project turns that process into an automated workflow.

### Example

```text
EC2 i-0123456789
CPU Utilization: 3.2%
Network Traffic: Low
Status: IDLE
Estimated Waste: $47/month
Confidence: HIGH
```

Instead of manually checking dozens of AWS resources, the scanner produces a prioritized cleanup report.

---

## ✨ Features

| Capability | Description |
|---|---|
| 🔍 EC2 Analysis | Detect potentially underutilized EC2 instances |
| 💾 EBS Detection | Find unattached EBS volumes |
| 🌐 Elastic IP Audit | Identify unused Elastic IP addresses |
| ⚖️ Load Balancer Analysis | Detect potentially idle load balancers |
| 📊 Utilization Analysis | Evaluate CloudWatch utilization metrics |
| 💰 Savings Estimation | Estimate potential monthly savings |
| 🎯 Confidence Scoring | Rank cleanup recommendations by confidence |
| 🛡️ Read-Only by Design | No automatic resource deletion |
| 📄 Reporting | Generate structured cleanup recommendations |
| ☁️ Terraform IAM | Deploy least-privilege AWS permissions |
| 🔄 CI Automation | Automated testing through GitHub Actions |

---

# 🧠 How It Works

```text
                   AWS Account
                       │
                       ▼
              ┌─────────────────┐
              │ Resource Scanner │
              └────────┬────────┘
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
       EC2            EBS           EIP
         │             │             │
         └─────────────┼─────────────┘
                       ▼
                CloudWatch Metrics
                       │
                       ▼
              Utilization Analysis
                       │
                       ▼
              Cost Estimation Engine
                       │
                       ▼
               Confidence Scoring
                       │
                       ▼
              Cleanup Recommendations
```

The scanner focuses on **evidence-based recommendations**, rather than blindly deleting resources.

---

# 🔎 Detection Examples

## EC2

Potentially idle instances can be identified using utilization signals such as:

```text
Average CPU:        2.8%
Network Activity:   Low
Instance Status:    Running

Recommendation:
Investigate instance for potential termination or rightsizing.

Confidence:
HIGH
```

## EBS

Example:

```text
Volume: vol-0abc123
State: available
Attached: No

Recommendation:
Review and remove unattached volume.

Estimated Savings:
$8.00/month
```

## Elastic IP

Example:

```text
Elastic IP: 18.xxx.xxx.xxx
Association: None

Recommendation:
Release unused Elastic IP after validation.
```

## Load Balancers

Traffic and utilization signals can be used to identify load balancers that may no longer serve active workloads.

---

# 💰 FinOps Output

The scanner is designed to produce recommendations that can be prioritized.

Example:

```text
┌──────────────────────────────────────────┐
│ AWS COST OPTIMIZATION REPORT             │
├──────────────────────────────────────────┤
│ Potential Monthly Savings:    $182.40    │
│ Resources Investigated:       47         │
│ Cleanup Candidates:             9        │
│ High Confidence:                6        │
│ Medium Confidence:              3        │
└──────────────────────────────────────────┘
```

A future deployment can feed this output into:

```text
AWS Cost Dashboard
        ↓
Slack / Email
        ↓
FinOps Review
        ↓
Approved Cleanup
```

---

# 🛡️ Safety First

This project intentionally follows a **read-only discovery model**.

It does **not automatically terminate EC2 instances, delete EBS volumes, release Elastic IPs, or remove load balancers**.

This makes it suitable for environments where cleanup requires:

```text
Detection
   ↓
Human Review
   ↓
Approval
   ↓
Controlled Remediation
```

That separation is useful for production AWS environments.

---

# 🏗️ Project Structure

```text
aws-idle-resource-cleaner/
│
├── src/
│   └── scanner.py
│
├── tests/
│   └── test_scanner.py
│
├── terraform/
│   └── iam.tf
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── pyproject.toml
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Tech Stack

```text
Python
AWS SDK (boto3)
Amazon CloudWatch
Amazon EC2
Amazon EBS
Elastic IP
Elastic Load Balancing
Terraform
GitHub Actions
Pytest
FinOps
```

---

# 🚀 Getting Started

## 1. Clone

```bash
git clone https://github.com/RahulSinha9/aws-idle-resource-cleaner.git
cd aws-idle-resource-cleaner
```

## 2. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure AWS

Make sure your AWS credentials are available through one of the standard AWS credential mechanisms.

Verify access:

```bash
aws sts get-caller-identity
```

## 5. Run Tests

```bash
pytest -q
```

---

# 🔐 IAM Permissions

The Terraform configuration provides a foundation for read-only access to the AWS services required by the scanner.

Typical permissions include:

```text
ec2:DescribeInstances
ec2:DescribeVolumes
ec2:DescribeAddresses
elasticloadbalancing:DescribeLoadBalancers
cloudwatch:GetMetricStatistics
```

The goal is to follow the principle of:

> **Minimum permissions required to discover cost optimization opportunities.**

---

# 🧪 Testing

Run:

```bash
pytest
```

The project includes automated tests covering scanning logic and recommendation behavior.

CI automatically validates the project through GitHub Actions.

---

# 📈 Roadmap

### Phase 1 — Current

- EC2 idle detection
- EBS orphan detection
- Elastic IP detection
- Load balancer analysis
- Savings estimation
- Confidence scoring
- Terraform IAM
- Automated testing

### Phase 2

- AWS Cost Explorer integration
- CSV/JSON reports
- Slack notifications
- Email notifications
- CloudWatch dashboards

### Phase 3

- Multi-account scanning
- AWS Organizations support
- Scheduled EventBridge scans
- Historical cost tracking
- FinOps dashboard

### Phase 4 — AI FinOps

```text
AWS Metrics
     ↓
Cost Data
     ↓
AI Analysis
     ↓
Optimization Explanation
     ↓
Recommended Action
     ↓
Human Approval
```

The AI layer could answer questions such as:

> "Why did this resource become expensive?"

> "Which resources should we investigate first?"

> "What is the safest way to reduce this month's AWS spend?"

---

# 🎯 Real-World Use Cases

### DevOps Teams

Automatically discover infrastructure that may no longer be required.

### FinOps Teams

Identify potential waste and prioritize optimization opportunities.

### Platform Engineering

Run the scanner on a schedule across cloud environments.

### Startups

Reduce unnecessary AWS spend without introducing automatic destructive actions.

### Learning / Portfolio

Demonstrates practical knowledge of:

```text
AWS
+
Python
+
CloudWatch
+
Terraform
+
FinOps
+
CI/CD
+
Cloud Cost Optimization
```

---

# 🌟 What Makes This Different?

Most cleanup scripts follow a simple pattern:

```text
Find resource → Delete resource
```

This project follows:

```text
Find resource
      ↓
Measure utilization
      ↓
Estimate cost
      ↓
Calculate confidence
      ↓
Recommend action
      ↓
Human approval
```

That makes the project closer to a **production FinOps workflow** than a basic AWS cleanup script.

---

# 📊 Example Recommendation

```json
{
  "resource_type": "ec2",
  "resource_id": "i-0123456789",
  "status": "idle",
  "average_cpu_percent": 3.2,
  "estimated_monthly_savings": 47.00,
  "confidence": "high",
  "recommendation": "Investigate for termination or rightsizing"
}
```

---

# 🤝 Contributing

Contributions are welcome.

A typical workflow:

```bash
git checkout -b feature/new-detector
```

Make your changes, add tests, and open a pull request.

---

# 📜 License

This project is intended for educational, engineering, and FinOps experimentation purposes.

---

## 👨‍💻 Author

**Rahul Sinha**

DevOps Engineer | AWS | Kubernetes | Terraform | CI/CD | DevSecOps | AI + Cloud Automation

GitHub:  
https://github.com/RahulSinha9

---

## ⭐ Support the Project

Found this project useful?

⭐ Star the repository  
🍴 Fork it  
🐛 Report an issue  
💡 Suggest an optimization idea

---

> **Don't wait for the AWS bill to tell you something is wrong. Find the waste first.**
