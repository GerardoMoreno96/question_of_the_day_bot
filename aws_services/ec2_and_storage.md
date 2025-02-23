### **EC2 and Storage:**
- There are 3 types of storage integrations in AWS: Block storage, object storage, and file storage.
- Amazon EC2 instance store provides temporary or ephemeral low-latency block storage for your EC2 instance.
- Amazon EC2 instance store uses the local disk or storage volumes physically attached to the underlying host computer of the EC2 instance.
- Amazon EC2 instance store loses data when stopped or terminated.
- Amazon EBS is a persistent block-level storage for EC2 instances.
- Amazon EBS is zonal, meaning that you can only attach volumes to EC2 instances in the same availability zone.
- EBS provides SSD (high IOPS options) and HDD (data archiving, backups) options.
- General-purpose SSD EBS and HDD EBS can only be attached to a single EC2 instance.
- HDD EBS is throughput-optimized.
- SSD EBS can be used as a boot volume for EC2, whereas HDD EBS cannot.
- SSD EBS is faster than S3 or EFS.