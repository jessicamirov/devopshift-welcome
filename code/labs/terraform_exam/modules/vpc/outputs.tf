output "public_subnet_id" {  
  value       = [for subnet in aws_subnet.public : subnet.id]
  description = "Public subnet IDs"
}

output "private_subnet_id" {  
  value       = [for subnet in aws_subnet.private : subnet.id]
  description = "Private subnet IDs"
}

output "vpc_id" {  
  value       = aws_vpc.jessica-vpc.id
  description = "VPC ID"
}