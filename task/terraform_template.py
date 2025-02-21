from Jinja2 import Template

def terraform_jinja2(user_config):
  
  # Map user inputs to jinja2 template variables
  ami = user_config.get("ami")
  instance_type  = user_config.get("instance_type")
  region =  user_config.get("region")
  alb = user_config.get("alb")
  availability_zone = user_config.get("availability_zone")

  terraform_template = """
  provider "aws" {
   region = "{{ region }}"
  }

  resource "aws_instance" "web_server" {
   ami = "{{ ami }}"
   instance_type = "{{ instance_type }}"
   availability_zone = "{{ availability_zone }}"

   tags = {
     Name = "WebServer"
   }
  }

  resource "aws_lb" "application_lb" {
   name = "{{ load_balancer_name }}"
   internal = false
   load_balancer_type = "application"
   security_groups = [aws_security_group.lb_sg.id]
   subnets = aws_subnet.public[*].id
  }

  resource "aws_security_group" "lb_sg" {
   name        = "lb_security_group"
   description = "Allow HTTP inbound traffic"

   ingress {
     from_port   = 80
     to_port     = 80
     protocol    = "tcp"
     cidr_blocks = ["0.0.0.0/0"]
   }
  }

  resource "aws_lb_listener" "http_listener" {
   load_balancer_arn = aws_lb.application_lb.arn
   port              = 80
   protocol          = "HTTP"

   default_action {
     type             = "forward"
     target_group_arn = aws_lb_target_group.web_target_group.arn
   }
  }

  resource "aws_lb_target_group" "web_target_group" {
   name     = "web-target-group"
   port     = 80
   protocol = "HTTP"
   vpc_id   = aws_vpc.main.id
  }

  resource "aws_lb_target_group_attachment" "web_instance_attachment" {
   target_group_arn = aws_lb_target_group.web_target_group.arn
   target_id        = aws_instance.web_server.id
  }

  resource "aws_subnet" "public" {
   count = 2
   vpc_id = aws_vpc.main.id
   cidr_block = "10.0.${count.index}.0/24"
   availability_zone = element(["us-east-1a", "us-east-1b"], count.index)
  }

  resource "aws_vpc" "main" {
   cidr_block = "10.0.0.0/16"
  }
  """

  template = Template(terraform_template)
  terr_jinja_template = template.render(
    region=region, 
    ami=ami, 
    instance_type=instance_type, 
    availability_zone=availability_zone, 
    load_balancer_name=alb
)

  with open("main.tf", "w") as f:
      f.write(terr_jinja_template)
    
  print("Terraform configuration generated successfully in main.tf")