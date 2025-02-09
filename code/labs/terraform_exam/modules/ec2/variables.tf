variable "myname" {
  type    = string
  default = "jessica"
}

variable "vpc_id" {
  type        = string
  description = "VPC ID where the EC2 instance will be created"
}

variable "subnet_id" {
  type        = string
  description = "Subnet ID where the EC2 instance will be created"
}

variable "ami" {
  type        = string
  description = "AMI ID for the EC2 instance"
}

variable "instance_type" {
  type        = string
  description = "Instance type for the EC2"
}

variable "assigen_public_ip" {
  type        = bool
  description = "Whether to assign a public IP to the instance"
  default     = true
}