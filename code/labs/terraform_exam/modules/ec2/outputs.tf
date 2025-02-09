output "vm_public_ip" {
  value       = aws_instance.jessica-ec2.public_ip
  description = "Public IP address"
}