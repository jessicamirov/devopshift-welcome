module "ec2" {
  source = "./modules/ec2"
  ami = "ami-0c02fb55956c7d316"
  machine_type = "t2.micro"
  name = "Jessica-vm"
}

output "printingmpduleinfo" {
    value = module.ec2
}