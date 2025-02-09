resource "aws_security_group" "sg" {
  vpc_id = var.vpc_id
  name_prefix = "${var.myname}-ec2-sg"
  description = "Allow SSH (port 22) and HTTP (port 80)"

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
    Name = "${var.myname}-ec2-secuirty-group"
  }
}

resource "aws_instance" "jessica-ec2" {
  ami           = var.ami
  instance_type = var.instance_type
  associate_public_ip_address = var.assigen_public_ip
  vpc_security_group_ids = [aws_security_group.sg.id] 
  subnet_id  =  var.subnet_id
  tags = {
    Name = "${var.myname}-ec2"
  }
}