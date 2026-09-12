# AWS Idle Resource Cleaner

Read-only FinOps scanner that identifies likely idle AWS resources and estimates avoidable spend.

## Detects
- Unattached EBS volumes
- Unused Elastic IPs
- EC2 instances with low utilization
- Idle load balancers
- Candidate cleanup actions with confidence scores

The default mode is **report-only**. No AWS resource is deleted by this project.
