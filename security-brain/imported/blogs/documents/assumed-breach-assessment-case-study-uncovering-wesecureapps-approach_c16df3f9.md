---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-14_assumed-breach-assessment-case-study-uncovering-wesecureapps-approach.md
original_filename: 2023-02-14_assumed-breach-assessment-case-study-uncovering-wesecureapps-approach.md
title: 'Assumed Breach Assessment Case Study: Uncovering WeSecureApp’s Approach'
category: documents
detected_topics:
- cloud-security
- oauth
- idor
- access-control
- ssrf
- command-injection
tags:
- imported
- documents
- cloud-security
- oauth
- idor
- access-control
- ssrf
- command-injection
language: en
raw_sha256: c16df3f912c47d52ac11fdcfbc6b6eca462d78597f88716ca56827a91a6677bb
text_sha256: 0004d52fdedabe205c446d556c07fa8db868436862082fae235c5e141fb76178
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Assumed Breach Assessment Case Study: Uncovering WeSecureApp’s Approach

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-14_assumed-breach-assessment-case-study-uncovering-wesecureapps-approach.md
- Source Type: markdown
- Detected Topics: cloud-security, oauth, idor, access-control, ssrf, command-injection
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `c16df3f912c47d52ac11fdcfbc6b6eca462d78597f88716ca56827a91a6677bb`
- Text SHA256: `0004d52fdedabe205c446d556c07fa8db868436862082fae235c5e141fb76178`


## Content

---
title: "Assumed Breach Assessment Case Study: Uncovering WeSecureApp’s Approach"
url: "https://wesecureapp-smm.medium.com/assumed-breach-assessment-case-study-uncovering-wesecureapps-approach-45a512c0bd63"
authors: ["WeSecureApp (@wesecureapp)"]
bugs: ["Internal pentest", "Missing authentication", "Hardcoded credentials", "Cloud"]
publication_date: "2023-02-14"
added_date: "2023-03-08"
source: "pentester.land/writeups.json"
original_index: 1528
scraped_via: "browseros"
---

# Assumed Breach Assessment Case Study: Uncovering WeSecureApp’s Approach

Assumed Breach Assessment Case Study: Uncovering WeSecureApp’s Approach
WeSecureApp
Follow
7 min read
·
Feb 14, 2023

1

This blog post focuses on the Assumed Breach Assessment approach with an assessment case study performed by the WSA team. But first,

What is an Assumed Breach Assessment?

As the name suggests, an Assumed Breach Assessment is performed by assuming that the threat already possesses a particular level of access. The assessment is performed to learn what an attacker could achieve with that particular level of access. Basically, as a pentester, you would be provided with access to one or more of the following:

Internal network through a jump server
VPN connection to the internal network
On-site system access
Access to machines from different segments of the network

The above-mentioned can be provided with a list of goals that are expected to be achieved by the Red Team, these goals can be as follows:

Getting access to PCI-DSS-related sensitive data.
Getting access to sensitive data which may include keys, credentials, etc.
Command execution on internal apps
Lateral movement to cloud infra.
Unauthenticated access or password resets

To summarize, an assumed breach assessment comes with a particular level of access to achieve a particular list of goals. Next, let’s have a look at one of our successful assumed breach projects to better understand the approach and goals.

Since we were given only VPN access for this particular assumed breach project, we planned to first enumerate all the routes that would be passing through the VPN to have an attack surface to work on. Then we’ll perform live host discovery and network enumeration on each of the IP ranges to find vulnerabilities. We’ll then try getting a foothold or some sensitive information that would help us in the lateral movement to their cloud infra, which was our ultimate goal. Now, let’s dig deeper.

An Assessment Case Study Performed by the Team

The WeSecureApp team was engaged with a client to perform an assumed breach red team assessment. The team was provided with the following set of goals:

During the assessment, the team was given an OpenVPN connection and a google account “wesecureapp@company.com”. We were asked to perform the activity as an internal employee. When we connected to the OpenVPN connection which lands us inside the client network, we found some internal IP ranges going through the VPN.

Moving forward, to find the live IPs from the ranges we used the AngryIP Scanner tool. On further network enumeration using Nmap, we found various kinds of services running on those subnets. Following are some of the critical findings we found by performing manual pentest on the subnets:

We were able to access different service dashboards without authentication. Some of these services were Aerospike, Prometheus, Kibana, Cerebro, Sonar, and neo4j.
We found multiple service dashboards like RabbitMQ with default credentials enabled.
A Grafana instance was misconfigured which allowed users to create accounts on the instance. We used the email id provided to us wesecureapp@company.com to register on this instance. We were then able to log in successfully on the portal and view various sensitive statistics of COMPANY infrastructure like AWS Billing dashboard, EBS usage, etc.
Press enter or click to view image in full size

We then increased our attack surface by DNS brute forcing to find any internal subdomains of company.com . We used the Dnsenum tool to accomplish this. We were unable to find any such application with which we can get a foothold on the company’s network.

We then found that Zeppelin, an online notebook service was running without any authentication. This had two notebooks available. One of the notebooks had some code snippets which contained sensitive details like S3 buckets, Access Keys, and Secret Keys. This is where the fun begins.

Press enter or click to view image in full size

The before-found secret keys gave us access to the S3 bucket and we were able to dump a huge amount of data stored in the buckets. We explored multiple S3 buckets and found that the AWS keys which belonged to the user “research team” had access to a lot of sensitive information which included access to the latest GitLab backups, old HR data, financial data, etc.

We found that the app-config.properties file from the GitLab backup had hardcoded TSRTC FTP credentials. We tried these credentials on an FTP server running on one of the IPs which was publicly accessible. We were able to successfully log in to this FTP server which had data belonging to TSRTC. Hence, we didn’t move further to exploit this service. We also found multiple hardcoded credentials in the backup files.

Press enter or click to view image in full size

Upon further enumeration, we found that the privileges of this AWS Account belonged to “Research Team” and also found that this user had permission to create and terminate instances as well. Then we created a T2 Micro instance from this account and tried terminating it.

Press enter or click to view image in full size

We found that the SQL DB backup had hardcoded credentials to various internal MySQL database instances, however, many DBs were not accessible to us via the OpenVPN service provided to us by the client team so we were not able to test the validity of these credentials. We also got embedded QA/Test credentials to some of the 3rd party integrations like Spicejet, Razorpay, juspay, etc.

Get WeSecureApp’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Upon further investigation, we found that there was an access key and secret key to one of the accounts in clear text in the SQL DB file itself. We tried utilizing these keys on our local machine using AWS CLI and found that these keys were valid and these keys belonged to the systems user. To enumerate the rights of this account, we used an AWS post-exploitation toolkit called PACU.

Upon further enumeration, we found that the owner of this account is the Co-Founder of the company, which indicated that the account could be a high-privilege user. We used a module in the PACU toolkit named “console” which uses the GetFederationToken privilege in AWS to fetch a temporary Federation URL that could be used to access the console of this particular user. We found that the user has been misconfigured and the GetFederationToken policy was assigned to this account.

Since this account had admin privileges on the AWS environment. We could have performed activities such as the following:

Creating/Deleting ec2 instances.
Deleting S3 buckets.
Terminating existing running ec2 instances.
Adding our SSH Keys to KMS and attaching them to EC2 instances leading us to gain RCE on any instance.
Viewing and modifying guard duty logs, CloudTrail logs and traffic rules, VPC groups and perform actions on many such critical services in use.
Get access to KMS Service.
Create new users and generate new access keys.
Access To GCP Management Console — Over Permissive Permissions Enabled

We were also able to gain access to the GCP Management Console with overly permissive permissions enabled. When performing enumeration on permissions, it is noticed that the given user contains overly permissive permissions enabled as the user wesecureapp@company.com has persistent access to the GCP platform of the Company. Although there is not much data or information in-store at the GCP level it is still a flash point for an internal threat actor to abuse these overly permissive permissions to create services and perform GCP operations. When enumerating the services, it is found that the user has the right to create projects and apply for an OAuth consent form.

In this scenario, we were able to dump the email addresses of 1600 users in the company.com organization. Since the use of GCP is very limited in the Company’s infrastructure, we were not able to laterally move in GCP.

Conclusion

The Assumed Breach Assessment performed by the WeSecureApp team highlights the importance of securing sensitive data and the consequences of leaving systems misconfigured or vulnerable. The team was able to identify multiple vulnerabilities, including unauthenticated access to dashboards, hardcoded credentials, and sensitive data stored in plaintext. These findings underscore the need for organizations to implement proper security controls and regularly assess their systems for vulnerabilities. By following the recommendations provided, organizations can improve the security of their systems and reduce the risk of data breaches.

Here are some recommendations:
Enable proper authentication mechanisms for all web-based services, particularly those containing sensitive data.
Disable debug mode in all Django instances and ensure sensitive information is not leaked through it.
Enable proper access controls and restrict access to sensitive data, including dashboard credentials and AWS keys.
Enable proper encryption for sensitive information and ensure it is properly stored and secured.
Ensure AWS credentials are not hardcoded in GitLab backup files or any other locations.
Regularly review and monitor the permissions granted to AWS users.
Regularly perform security assessments to identify and remediate potential vulnerabilities.
Recommended Reading

Automation and Scalability in Red Team Assessments

The Five Stages of the Red Team Methodology

7+ Major Reasons to Hire a Red Team to Harden Your App Sec

Originally published at https://wesecureapp.com on February 14, 2023.
