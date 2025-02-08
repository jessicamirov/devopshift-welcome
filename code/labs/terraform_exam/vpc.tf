provider "aws" {
  region = var.region
}

variable "region" {
  type    = string
  default = "us-east-1"
}

variable "az_list" {
  type    = list(string)
  default = ["us-east-1a", "us-east-1b"]
}

variable "myname" {
  type    = string
  default = "jessica"
}

resource "aws_vpc" "jessica-vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "${var.myname}-vpc"
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.jessica-vpc.id

  tags = {
    Name = "${var.myname}-Internet_gateway"
  }
}

resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.jessica-vpc.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone       = var.az_list[0]

  tags = {
    Name = "${var.myname}-public_subnet"
  }
}

resource "aws_subnet" "private" {
  vpc_id            = aws_vpc.jessica-vpc.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = var.az_list[1]

  tags = {
    Name = "${var.myname}-private_subnet"
  }
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.jessica-vpc.id
  
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "${var.myname}-public route table"
  }
}

resource "aws_route_table" "private" {
  vpc_id = aws_vpc.jessica-vpc.id

  tags = {
    Name = "${var.myname}-private route table"
  }
}

resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "private" {
  subnet_id      = aws_subnet.private.id
  route_table_id = aws_route_table.private.id
}

# OUTPUTS
output "public_subnet_id" {  
  value       = aws_subnet.public.id
  description = "Public subnet ID"
}

output "vpc_id" {  
  value       = aws_vpc.jessica-vpc.id
  description = "VPC ID"
}