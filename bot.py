import requests
import random
import os

url = os.getenv("DISCORD_WEBHOOK_URL")

questions = [
    "There are 3 types of storage integrations in AWS: Block storage, object storage and file storage",
    "Amazon EC2 instance store provides a temporary or ephemeral low-latency block storage for your EC2 instance",
    "Amazon EC2 instance store uses the local disk or storage volumes physically attached to the underlying host computer of the ec2 instance",
    "Amazon EC2 instance store loses data when stopped or terminated",
    "Amazon EBS is a persisten block-level storage for EC2 instances",
    "Amazon EBS has is zonal - meaning that you can only attach volumes to EC2 instances in teh same availability zone",
    "EBS provides SSD (high IOPS options) and HDD (data archiving, backups) options"
]

question_of_the_day = random.choice(questions)

payload = {'content': question_of_the_day}
files = []
headers = {}

response = requests.request(
    "POST", url, headers=headers, data=payload, files=files)

print(response.text)
