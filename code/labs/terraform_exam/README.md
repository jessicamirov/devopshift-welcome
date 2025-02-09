Jessica Mosheev - AWS Infrastructure with Terraform

This project implements a complete AWS infrastructure using Terraform, including VPC, EC2 instances, and Application Load Balancer with Auto Scaling.

Features:
VPC Module: Creates a VPC with public and private subnets across multiple availability zones
EC2 Module: Deploys EC2 instances with appropriate security groups
ALB Module: Sets up Application Load Balancer with auto-scaling capabilities

Prerequisites:
AWS CLI configured with appropriate credentials
Terraform v1.0.0 or newer
An AWS account with necessary permissions

Resource Configuration:
VPC Configuration-

CIDR Block: 10.0.0.0/16
Public Subnets: 10.0.1.0/24, 10.0.2.0/24
Private Subnets: 10.0.3.0/24, 10.0.4.0/24
Internet Gateway for public internet access
Separate route tables for public and private subnets

EC2 Configuration-

AMI: Ubuntu 22.04 (ami-0e1bed4f06a3b463d)
Instance Type: t2.micro
Public IP address enabled
Security Group: Allows SSH (22) and HTTP (80)

ALB Configuration-

Application Load Balancer in public subnets
Target Group with health checks
Auto Scaling Group (min: 1, max: 3)
Launch Template with user data for web server setup

Usage:
Initialize Terraform:
    terraform init

Review the execution plan:
    terraform plan

Apply the configuration:
    terraform apply

To destroy the infrastructure:
    terraform destroy

Module Variables:
VPC Module-
module "vpc" {
  source = "./modules/vpc"
  subnet_count = 2
  subnet_cidr = {
    public  = ["10.0.1.0/24", "10.0.2.0/24"]
    private = ["10.0.3.0/24", "10.0.4.0/24"]
  }
}

EC2 Module-
module "ec2" {
  source = "./modules/ec2"
  vpc_id = module.vpc.vpc_id
  subnet_id = module.vpc.public_subnet_id[0]
  instance_type = "t2.micro"
  ami = "ami-0e1bed4f06a3b463d"
  assigen_public_ip = true
}

ALB Module-
module "alb" {
  source = "./modules/alb"
  vpc_id = module.vpc.vpc_id
  subnets = module.vpc.public_subnet_id
  instance_type = "t2.micro"
  ami = "ami-0e1bed4f06a3b463d"
}

Outputs:
VPC ID
Public and Private Subnet IDs
EC2 Instance Public IP
ALB DNS Name

Security Considerations:
1.All security groups are configured with minimum required access
2.Private subnets are isolated from direct internet access
3.Public access is limited to necessary ports (80, 22)
4.Auto Scaling ensures high availability

Contributing:
1.Fork the repository
2.Create your feature branch
3.Commit your changes
4.Push to the branch
5.Create a new Pull Request