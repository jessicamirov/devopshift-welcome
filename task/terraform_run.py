import os
from python_terraform import Terraform

def run_terraform() -> str:
    terraform = Terraform(working_dir=os.getcwd())
    terraform.init()
    terraform.plan()
    try:
        return_code, stdout, stderr = terraform.apply(skip_plan=True, capture_output=True)
        if return_code == 0:
            return stdout
        else:
            raise Exception(stderr)   
    except Exception as e:
        print("Error running Terraform:", {e})
        print("Terraform Apply Failed:", stderr)
        exit(1)
        