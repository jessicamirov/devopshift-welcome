variable "region" {
  type    = string
  default = "us-east-1"
}

variable "myname" {
  type    = string
  default = "jessica"
}

variable "subnets" {
    description = "List of subnets"
    type        = list(string)
}

variable "desired_capacity" {
  type = number
  default = 1
}

variable "max_size" {
  type = number
  default = 3
}

variable "min_size" {
  type = number
  default = 1
}

variable "ami" {
  description = "AMI ID for EC2 instances"
  type        = string
}

variable "instance_type" {
  description =  "Instance type for EC2 instances"
  type        = string
  default     = "t2.micro"
}

variable "vpc_id" {
  description = "Vpc_id"
  type        = string
}