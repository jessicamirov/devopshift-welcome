provider "aws" {
  region = var.region
}

variable "region" {
  default = "us-east-1"
}

data "aws_instances" "yaniv-vm" {
  filter {
    name   = "tag:Name"
    values = ["yaniv-vm"]
  }
}

data "instance_ids" "yaniv-vm" {
    instance_id="i-09df7e0ed385f871b"
}

output "instance_ids" {
  value = data.aws_instances.yaniv-vm.id
}
