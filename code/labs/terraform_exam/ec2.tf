variable "ami" {
  description = "Ubuntu 22.04 AMI ID"
  type        = string
  default     = "ami-0e1bed4f06a3b463d"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

resource "aws_security_group" "sg" {
  description = "Allow SSH (port 22) and HTTP (port 80)"
  vpc_id      = aws_vpc.jessica-vpc.id  

  ingress {
    description = "SSH from anywhere"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTP from anywhere"
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

  tags = {
    Name = "${var.myname}-secuirty-group"
  }
}

resource "aws_instance" "jessica-ec2" {
  ami           = var.ami
  instance_type = var.instance_type
  subnet_id     = aws_subnet.public.id
  associate_public_ip_address = true

  vpc_security_group_ids = [aws_security_group.sg.id] 

  tags = {
    Name = "${var.myname}-ec2"
  }
}

output "vm_public_ip" {
  value       = aws_instance.jessica-ec2.public_ip
  description = "Public IP address"
}