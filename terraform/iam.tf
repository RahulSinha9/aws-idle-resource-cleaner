resource "aws_iam_policy" "scanner" {
  name = "aws-idle-resource-cleaner-readonly"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = [
        "ec2:DescribeInstances",
        "ec2:DescribeVolumes",
        "ec2:DescribeAddresses",
        "elasticloadbalancing:DescribeLoadBalancers"
      ]
      Resource = "*"
    }]
  })
}
