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
    "Amazon EBS is zonal - meaning that you can only attach volumes to EC2 instances in the same availability zone",
    "EBS provides SSD (high IOPS options) and HDD (data archiving, backups) options",
    "General purpose SSD EBS and HDD EBS can only be attached to a single ec2 instance",
    "HDD EBS is throughput optimized",
    "SSD EBS can be used as a boot volume for ec2, whereas HDD EBS cannot",
    "SSD EBS is faster than S3 or EFS",
    "S3 is a highly durable and scalabe object storage service",
    "The multiple types of S3 object storage are: Standard, Intelligent tiering, Standard Infrequent Access, One Zone I-A, S3 Glacier / Glacier archive",
    "S3 Standard storage is mainly used for frequently accessed data",
    "S3 Intelligent tiering storage is used for changing or unknown access patterns",
    "S3 Standard IA or S3 One-zone IA is used for storing long-lived, yet less frequently accessed data",
    "S3 Glacier and Glacier archive is used for low-cost, long-term storage and data archiving",
    "S3 Access Controls Lists secure access to your S3 buckets and objects",
    "s3 Bucket policies control external access to your S3 bucket",
    "AWS EFS is a scalable shared file storage service that can be accessed by many EC2s in different AZs",
    "AWS EFS only supports linux servers",
    "AWS FXS - Amazon FSX for Lustre has everything that EFS has + a parallel filesystem used for large-scale cluster computing. Use cases: machine learning or high performance computing",
    "FSX for Windows is a fully managed Microsoft Windows file server service",
    "AWS Backup is a fully managed service to backup your servers and databases",
    "The different relational databases in AWS are: RDS, Aurora and Redshift",
    "Amazon RDS is a relational database service that supports MySQL, Postgres, etc",
    "Amazon Aurora is a fully managed service that's better than RDS. It automatically grows or scales as needed. It uses a database cluster. Use cases: online transactions apps",
    "Redshift is a fully managed warehouse solution. Use cases: online analytical processing apps, data reporting and analytics",
    "Some non-relational DBs are DynamoDB, DocumentDB",
    "Dynamo db stores data in an item - attributes structure",
    "DocumentDB is a MongoDB compatible DB that stores JSON docs. A table is a collection, a row is called a document and a column a field",
    "Elasticache is an open source in memory database like memchached & redis. It is faster than disk databases. Use cases: real-time analytics, distributed session management, geospacial services",
    "Memcached database does not have a data replication feature unlike Redis",
    "AWS Keyspaces is an Apache Cassandra wide colum database that can handle large amounts of data",
    "AWS Neptune is a graph database service for apps that need access to many datasets",
    "AWS Timestream is a serverless time series databse for IoT and operational apps. Use cases: stock prices, weather changes",
    "AWS Ledger is an immutable transaction log database that tracks each application data change",
    "Cloudwatch is a suiote of monitoring services that can be used on AWS or on your on-premises data centers",
    "Cloudwatch collects data from AWS services as well as custom metrics"
    "Cloudwatch metrics can get metrics from apps",
    "Cloudwatch logs can monitor, store and analyze log files",
    "Cloudwatch alarms can be used to set alarms on a threshold",
    "Cloudwatch events - now called EvenBridge events, respond to system events like the status change of an instance",
    "Cloudwatch dashboards are customizable dashbaords where you can see different metrics at once",
    "AWS service health dashboard is a public dashboard that shows the status of AWS services across all regions",
    "AWS personal health dashboard shows the status of the AWS resources that you are using",
    "Health API provides programmatic information to the data in your personal health dasboard. It is only available to business or enterprise accounts",
    "AWS cloudtrail is used for IT audits. It tracks user activity and API usage. You can store management events or data events",
    "Cloudtrail management events provide information about the management operations such as attaching IAM roles, creating new VPCs and creting subnets",
    "Cloudtrail data events share information about the resource operations performent ON or IN your resources. Such as S3 object-level API activities or Invoking Lambda functions",
    "AWS Artifact is an on-demand security and compliance reports service",
    "Security hub: Helps you comply with your company's specific standards",
    "AWS VPC stands for Virtual Private cloud. Logical isolation of your resources within AWS",
    "Virtual Private Gateway: Connect to an external data center or to an external network",
    "VPC peering: Connect to another VPC within the same AWS account or in another AWS account",
    "VPC Outpost: Rack of EC2 instances than can help you exten your VPC",
    "VPC Endpoint: Private connection between your VPC and other AWS services that doesn't traverse the internet",
    "Elastic Load Balancer (ELB): Distribute traffic to underlying servers",
    "There are 4 types of ELBs: Application Load Balancer, Network Load Balancer, Gateway Load Balancer and Classic Load Balancer",
    "Application Load Balancer (ALB) uses HTTP and HTTPS protocols and is used for web apps microservices and containers",
    "Network Load Balancer (NLB) uses TCP/UDP, TLC procotols and is used to transfer data between apps. It also provides low-latency",
    "Gateway Load Balancer (GLB) uses IP protocol and is used to run and scale virtual appliances",
    "Classic Load Balancer (CLB) uses HTTP/HTTPS, TCP, SSL and TLS protocls and is used for old ec2 networks (legacy)",
    "Route 53 is a Domain Name System service (DNS)",
    "Global Accelerator: Provides a set of static anycast IP addresses that work as a single fixed entry points for the ELBs",
    "Cloudfront: Content Delivery network for static objects or streaming",
    "Private link: Private connection to your aws services that doesn't traverse the internet. Now called VPC endpoint",
    "AWS VPN: Securely connect your on-premises network to AWS.  Site-so-site vpn: Tunnel between your network and AWS VPC. Client-VPN: Allows your users to connect to AWS or to your on-premises resources",
    "AWS Direct Connect: Dedicated network connection from your On-premises data centers to AWS. Better connection than regular VPN. It doesn't traverse public internet, unlike VPN",
    "Transit Gateway: Connect VPC, Direct Connect Gateway, VPN and On-premises to a single gateway. It is used in large organization with 100+ VPCs",
    "API Gateway: Restful API services",
    "App Mesh: Application-level networking to containersized apps",
    "Cloud Map: Cloud resource discovery service for apps with changing resources",
    "SQS: Simple queue service that offers Standard and First-in-first-out (FIFO) queues. FIFO messages can only be processed once",
    "SNS: Simple Notification Service. Messaging and notification service. Applications write to a topic that users can subscribe to",
    "Step functions: Service used to orchestrate lambdas",
    "AWS MQ: Apache MQ (Message Queue) managed message broker. Supports more messaging protocl types than SQS (JMS, NMS, AMQP, MQTT)"
    "EventBridge: Serverless event buss to connect data from other applications"
    "Appsync: It uses GraphQL for apps to get the data they need. Doesn't query the entire dataset, only what you want. Combine data for 1 or more datasources",
    "Appflow: Transfer data between SaaS to AWS like Salesforce -> AWS",






]

question_of_the_day = random.choice(questions)

payload = {'content': question_of_the_day}
files = []
headers = {}

response = requests.request(
    "POST", url, headers=headers, data=payload, files=files)

print(response.text)
