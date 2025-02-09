# provider "aws" {
#   region = var.region
# }

# variable "region" {
#   type    = string
#   default = "us-east-1"
# }

variable "az_list" {
  type = list(string)
  default = ["us-east-1a", "us-east-1b", "us-east-1c", "us-east-1d"]
  description = "available availability zones from us-east-1 region" 
}

variable "myname" {
  type    = string
  default = "jessica"
}

variable "cidr_block" {
  default = "10.0.0.0/16"
}

# variable "public_subnet_cidr" {
#   type        = list(string)
#   default     = ["10.0.1.0/24"]
#   description = "public subnet cidr block"
# }

# variable "private_subnet_cidr" {
#   type        = list(string)
#   default     = ["10.0.2.0/24"]
#   description = "private subnet cidr block"
# }

variable "subnet_cidr" {
  type = map(list(string))
  description = "public and private subnets to cidr blocks"
}

variable "subnet_count" {
  type        = number
  description = "Number of subnets to create per type (public/private)"
  default     = 2
}

variable "rt_cidr" {
  default = "0.0.0.0/0"
  description = "the public subnet for route table"
}