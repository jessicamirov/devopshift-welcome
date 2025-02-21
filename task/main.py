from terraform_template import terraform_jinja2

def get_user_choose():
    ami_options = {
        "ubuntu": "ami-0dee1ac7107ae9f8c",
        "amazon-linux": "ami-0f1a6835595fb9246"
    }
    instance_types = {"small": "t3.small", "medium": "t3.medium"}

    ami = input("Choose AMI: Ubuntu / Amazon Linux ")
    instance_type = input("Choose INSTANCE TYPE: small / medium ")
    region = input("choose REGION: us-east-1 ")
    alb = input("choose LOAD BALANCER Name ")

    if region != "us-east-1":
        print("Invalid region, defaulting to us-east-1")
        region = "us-east-1"

    return {
        "ami": ami_options.get(ami),
        "instance_type": instance_types.get(instance_type),
        "region": region,
        "alb": alb,
        "availability_zone": "us-east-1a"
    }

def main():
    print("Cloud Deployment Configuration")
    user_choose = get_user_choose()
    terraform_jinja2(user_choose)

if __name__ == "__main__":
    main()