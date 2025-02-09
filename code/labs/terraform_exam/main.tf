provider "aws" {
  region = var.region
}

variable "region" {
  type    = string
  default = "us-east-1"
}

module "vpc" {
  source = "./modules/vpc"
  subnet_count      = 2
  subnet_cidr = {
    public  = ["10.0.1.0/24", "10.0.2.0/24"]
    private = ["10.0.3.0/24", "10.0.4.0/24"]
  }
}

module "ec2" {
  source            = "./modules/ec2"
  vpc_id            = module.vpc.vpc_id
  subnet_id         = module.vpc.public_subnet_id[0]
  instance_type     = "t2.micro"
  ami               = "ami-0e1bed4f06a3b463d"
  assigen_public_ip = true
}

output "vpc_output" {
  value       = module.vpc
  description = "outputs of the module"
}

output "ec2_output" {
  value       = module.ec2
  description = "outputs of the module"
}

module "alb" {
  source        = "./modules/alb"
  vpc_id        = module.vpc.vpc_id
  subnets       = module.vpc.public_subnet_id
  instance_type = "t2.micro"
  ami           = "ami-0e1bed4f06a3b463d"
}

output "alb_output" {
  value = module.alb
}