resource "aws_vpc" "jessica-vpc" {
  cidr_block           = var.cidr_block
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "${var.myname}-vpc"
  }
}

resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.jessica-vpc.id
  count                   = length(var.subnet_cidr["public"])
  cidr_block              = var.subnet_cidr["public"][count.index]
  map_public_ip_on_launch = true
  availability_zone = var.az_list[count.index]

  tags = {
    Name = "${var.myname}-public_subnet-${count.index + 1}"
  }
}

resource "aws_subnet" "private" {
  vpc_id            = aws_vpc.jessica-vpc.id
  count             = length(var.subnet_cidr["private"])
  cidr_block        = var.subnet_cidr["private"][count.index]
  map_public_ip_on_launch = false
  availability_zone = var.az_list[count.index]

  tags = {
    Name = "${var.myname}-private_subnet-${count.index + 1}"
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.jessica-vpc.id

  tags = {
    Name = "${var.myname}-Internet_gateway"
  }
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.jessica-vpc.id
  
  route {
    cidr_block = var.rt_cidr
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "${var.myname}-public route table"
  }
}

resource "aws_route_table" "private" {
  vpc_id = aws_vpc.jessica-vpc.id

  tags = {
    Name = "${var.myname}-private route table"
  }
}

resource "aws_route_table_association" "public" {
  count          = length(var.subnet_cidr["public"])
  subnet_id      = aws_subnet.public[count.index].id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "private" {
  count          = length(var.subnet_cidr["private"])
  subnet_id      = aws_subnet.private[count.index].id
  route_table_id = aws_route_table.private.id
}