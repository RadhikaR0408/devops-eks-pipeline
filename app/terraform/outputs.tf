output "cluster_name" {
  value = aws_eks_cluster.eks.name
}

output "region" {
  value = "us-east-1"
}
