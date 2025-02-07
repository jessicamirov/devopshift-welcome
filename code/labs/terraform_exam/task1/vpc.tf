provider "aws" {
  region = "us-east-1"
}

variable "az1" {
  default = "us-east-1a"
}

variable "az2" {
  default = "us-east-1b"
}

variable "myname" {
  type = string
  default = "jessica"
}

resource "aws_vpc" "jessica-vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "${var.myname}-vpc"
  }
}

resource "aws_subnet" "public_ip" {
  vpc_id     = aws_vpc.jessica-vpc.id
  cidr_block = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone = var.az1
  tags = {
    Name = "${var.myname}-public"
  }
}

resource "aws_subnet" "private_ip" {
  vpc_id     = aws_vpc.jessica-vpc.id
  cidr_block = "10.0.2.0/24"
  availability_zone = var.az2
  tags = {
    Name = "${var.myname}-private"
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.jessica-vpc.id
  tags = {
    Name = "Internet_gateway"
  }
}

resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.jessica-vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }
  tags = {
    Name = "public route table"
  }
}

resource "aws_route_table_association" "public_rt" {
  subnet_id      = aws_subnet.public_ip.id
  route_table_id = aws_route_table.public_rt.id
}

resource "aws_route_table" "private_rt" {
  vpc_id = aws_vpc.jessica-vpc.id
 
  tags = {
    Name = "private route table"
  }
}

resource "aws_route_table_association" "private_rt" {
  subnet_id      = aws_subnet.private_ip.id
  route_table_id = aws_route_table.private_rt.id
}
