import json


def lambda_handler(event, context):
    print('Entering lambda excution.. printing event and context')
    print(context)
    print('--*20')
    print(event)

    return {

        "statusCode": 200,
        "body": json.dumps({"message": "Running python script on lambda using Terraform"}),

    }
