### **VPC and Networking:**
- AWS VPC stands for Virtual Private Cloud. Logical isolation of your resources within AWS.
- Virtual Private Gateway: Connect to an external data center or to an external network.
- VPC peering: Connect to another VPC within the same AWS account or in another AWS account.
- VPC Outpost: Rack of EC2 instances that can help you extend your VPC.
- VPC Endpoint: Private connection between your VPC and other AWS services that doesn't traverse the internet.
- Elastic Load Balancer (ELB): Distribute traffic to underlying servers.
- There are 4 types of ELBs: Application Load Balancer, Network Load Balancer, Gateway Load Balancer, and Classic Load Balancer.
- Application Load Balancer (ALB) uses HTTP and HTTPS protocols and is used for web apps, microservices, and containers.
- Network Load Balancer (NLB) uses TCP/UDP, TLC protocols and is used to transfer data between apps. It also provides low-latency.
- Gateway Load Balancer (GLB) uses IP protocol and is used to run and scale virtual appliances.
- Classic Load Balancer (CLB) uses HTTP/HTTPS, TCP, SSL, and TLS protocols and is used for old EC2 networks (legacy).
- Route 53 is a Domain Name System service (DNS).
- Global Accelerator: Provides a set of static anycast IP addresses that work as a single fixed entry point for the ELBs.
- CloudFront: Content Delivery network for static objects or streaming.
- Private Link: Private connection to your AWS services that doesn't traverse the internet. Now called VPC endpoint.
- AWS VPN: Securely connect your on-premises network to AWS. Site-to-site VPN: Tunnel between your network and AWS VPC. Client-VPN: Allows your users to connect to AWS or to your on-premises resources.
- AWS Direct Connect: Dedicated network connection from your On-premises data centers to AWS. Better connection than regular VPN. It doesn't traverse the public internet, unlike VPN.
- Transit Gateway: Connect VPC, Direct Connect Gateway, VPN, and On-premises to a single gateway. It is used in large organizations with 100+ VPCs.
