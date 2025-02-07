provider "aws" {
  region = var.region
}

variable "region" {
  default = "us-east-1"
}

variable "ami" {
  default = "ami-0e1bed4f06a3b463d"
}

variable "instance_type" {
  default = "t2.micro"
}

resource "aws_instance" "jessica-ec2" {
  
  ami           = var.ami
  instance_type = var.instance_type

  vpc_security_group_ids = [aws_security_group.sg.id]

  tags = {
    Name = "jessica-ec2"
  }
}

resource "aws_security_group" "sg" {
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

output "vm_public_ip" {
  value       = aws_instance.jessica-ec2.public_ip
  description = "Public IP address"
}
