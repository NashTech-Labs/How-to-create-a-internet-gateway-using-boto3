import time
import boto3
from botocore.exceptions import ClientError
import json
import logging


# taking the input from user where want to create internet gateway 
REGION= input("Please, Enter the region name where you want to Delete this NACL:-")
client = boto3.client("ec2", region_name=REGION)

# setup the logger config
logger_info = logging.getLogger()
logging.basicConfig(level=logging.INFO,format=' %(message)s')

# taking input from user for the internet gateway's key name
key_name=input("Please, Enter the key name for the internet gateway:-")
# taking input from user for the internet gateway's key value
key_value= input("Please, Enter the key vlaue for the key name for internet gateway:-")


# function to create a internet gateway
def create_gateway():

    try:
        response = client.create_internet_gateway(TagSpecifications=[
            {
                'ResourceType': 'internet-gateway',
                'Tags': [{'Key': key_name,'Value': key_value},]
            },
        ])

    except ClientError:
        logger_info.exception('Sorry, Not able to create the internet gateway in given VPC')
        raise
    else:
        return response


if __name__ == '__main__':

    logger_info.info('Creating an internet gateway...')
    logger_info.info(f'Please wait ......  \n We are creating your internet gateway...\U0001F570')
    time.sleep(5)    
    internet_gateway = create_gateway()
    
    logger_info.info(f'\nHurry, Your Internet gateway has been created with: {json.dumps(internet_gateway, indent=4)}')