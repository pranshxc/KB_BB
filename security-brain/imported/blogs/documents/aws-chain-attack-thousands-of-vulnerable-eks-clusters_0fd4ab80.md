---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-04_aws-chain-attack-thousands-of-vulnerable-eks-clusters.md
original_filename: 2023-06-04_aws-chain-attack-thousands-of-vulnerable-eks-clusters.md
title: AWS Chain Attack- Thousands of Vulnerable EKS Clusters
category: documents
detected_topics:
- cloud-security
- sso
- access-control
- command-injection
- otp
- api-security
tags:
- imported
- documents
- cloud-security
- sso
- access-control
- command-injection
- otp
- api-security
language: en
raw_sha256: 0fd4ab8029ad772714c270dbe7c6741da5bf177e50a7638bd3d73e99ae75da55
text_sha256: 42dcad93b920347953a47c63a7b91029b3a7b9cd881dc38e0e7e976cce90f259
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# AWS Chain Attack- Thousands of Vulnerable EKS Clusters

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-04_aws-chain-attack-thousands-of-vulnerable-eks-clusters.md
- Source Type: markdown
- Detected Topics: cloud-security, sso, access-control, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `0fd4ab8029ad772714c270dbe7c6741da5bf177e50a7638bd3d73e99ae75da55`
- Text SHA256: `42dcad93b920347953a47c63a7b91029b3a7b9cd881dc38e0e7e976cce90f259`


## Content

---
title: "AWS Chain Attack- Thousands of Vulnerable EKS Clusters"
url: "https://medium.com/@chenshiri/aws-chain-attack-thousands-of-vulnerable-eks-clusters-701cbd963907"
authors: ["Chen Shiri (@ChenShiri73)"]
bugs: ["AWS Kubernetes", "EKS", "Container escape", "Security misconfiguration"]
publication_date: "2023-06-04"
added_date: "2023-06-05"
source: "pentester.land/writeups.json"
original_index: 1088
scraped_via: "browseros"
---

# AWS Chain Attack- Thousands of Vulnerable EKS Clusters

AWS Chain Attack- Thousands of Vulnerable EKS Clusters
Chen Shiri
Follow
10 min read
·
Jun 4, 2023

133

5

Press enter or click to view image in full size

The research performed on the boundaries of bug bounty

In this article, I will discuss my research on the Elastic Kubernetes Service (EKS) and the attack methodology I have developed for this service.

I will discuss about two zero day vulnerabilities that I found that break the pod isolation mechanism.

My research focuses on a chain attack that exploits vulnerabilities in the Kubernetes orchestration of AWS cloud, specifically in EKS.

AWS Kubernetes environments without thirdparty security products are vulnerable by default

Table of Contents

1. Background about the problem
2. EKS architecture
3. Proof of Concept Video
4. Understanding the attack
5. Attack 1-using the metadata of the host
6. Attack 2-Generating a new Kube-Config
7. The risk
8. Access to the Kubernetes manifest
9. How I accessed pods? accessing other namespaces
10. Getting the session
11. Recap: A Systemic Failure
12. How to remediate?

1. Background about the problem

The attack vector I have identified allows attackers with limited access (i.e., non-root) to a secured pod to move laterally and gain access to privileged KubeAPI in Kubernetes environments without third-party security products.

This attack vector has serious implications as it could allow malicious actors in customer environments to read and modify data stored and accessible from other containers and services, also the takeover of the cluster enables access to data from all containers, including those that should be inaccessible such as secrets and storage, thereby compromising other security mechanisms of the cluster.

The discovery of the vulnerabilities in AWS Kubernetes service mechanism poses a critical security problem as it allows unauthorized access to sensitive customer data stored in containers. This not only compromises the privacy of the data but also puts many customers at risk of non-compliance with regulations that govern the handling of such data. Essentially, the vulnerability allows an attacker to gain access to other containers, which can lead to the exposure of confidential information, including personally identifiable information (PII), financial information, and other sensitive data. This could result in severe consequences, such as financial loss, legal penalties, and reputational damage for the affected organizations. It’s crucial to address this security flaws immediately to prevent further unauthorized access to the cluster and mitigate the risks associated with the compromised data.

To execute this attack, I leveraged a combination of Kubernetes capabilities such as host communication and API along with AWS mechanisms to gain access to the entire cluster and cloud components. The attack vector is based on two vulnerabilities:

The EC2 VM Role (i.e., the role of the node) is accessible from the containers.
In Kubernetes environment, the role has privileges to generate new kubeconfig. in addition, it has permissions to all cluster with a bypass.
2. EKS architecture

To successfully execute this attack, there are four main websites in the attack chain that require attention. These sites are critical to understanding the twists and turns of the attack chain.

AWS Cloud < <EKS Architecture-> node-> container -> app users>

3. Proof of Concept Video

If you like the video please like and subscribe for more articles.

Twitter- https://twitter.com/ChenShiri73

4. Understanding the attack

Instance metadata is data about your instance that you can use to configure or manage the running instance. The IMDS is divided into categories, for example, host name, events, and security groups and it’s considered as powerful attack vector.

While assessing AWS Elastic Kubernetes Services cluster mechanisms, I found several cloud services of the node-instance accessible from the container- using API-Token creation can lead to lateral movement.

From the AKS container, you can gain detailed information on the context of running by using the instance metadata endpoint.

From this you can find the ARN, labels, networking and details about the instance.

As you an see in this attack vector we have access to non-root user , with limited permissions in on of the containers without access to the cloud or k8s.

PoC- For the PoC we’ve backend and frontend namespaces- in this scenario have access to the frontend container.

Press enter or click to view image in full size
Attack Flow
5. Attack 1-using the metadata of the host

Now we will request a token from the frontend container.

Figure 1- Request to the metadata server to get a temporary token from the frontend

Accessing information about the Cloud environment

Figure 2- Using the token to get information about the node

I have developed a script that utilizes metadata queries to obtain network information about node instances in a cluster, without having to perform a network scan.

The script works by first retrieving the mac addresses of the nodes-instances, and then generating a request for information based on the mac address. This enables the script to retrieve information on the relevant subnets and security groups, node names, cluster names, cluster host names, and other relevant details.

With this script, it is possible to obtain valuable network information about node instances in a cluster quickly and efficiently, without resorting to time-consuming and potentially intrusive scanning methods.

Figure 3 : Executing the script, as we can see it shows information about the cluster and other namespaces using the security groups (utilizes the mac address and metadata)

The EC2 Instance Role grants an instance access to a specific set of IAM credentials and, depending on the policies associated with the role, may also allow access to various AWS services.

To retrieve the EC2 role of a node, you can send a request to the metadata service. By adding the token to the request, you can obtain the privileged role of the instance.

Without the token, we will usually get an unprivileged role

Figure 4- The EC2 host role cloud profile info
Figure 5-: Generating a request to retrieve the EC2 role (Node)using the temporary token

After accessing the role we can use an open source tool called “Pacu” to access the AWS UI using the credentials, it was very limited so I continued to research for a vector:

Figure 6- AWS Cloud UI account access using the role

In the default configuration, most listing permissions are restricted, which means that users do not have access to detailed information about instances or databases unless explicitly granted permission.

In my attempts to obtain details about instances and databases, I found that I did not have the necessary permissions. Specifically, I was unable to access any detailed information on instances or databases, indicating that the default restrictions were in place.

Despite the default restrictions on listing permissions, I was able to find a way to bypass these limitations by utilizing the “Describe-tags” functionality. This allowed me to list the tags of all the resources in the cloud environment, including details such as the cluster name, namespaces (using security groups default tags), cloud components, and more.

With this bypass, I was able to obtain valuable information about almost all the components in the environment, despite the default role permissions and restrictions.

We will need this information later.

Figure 7: Listing tags from all environments- we can see resource ID, Type and even names of every cloud component in the cluster.
6. Attack 2-Generating a new Kube-Config

Despite my default role permissions not including write or list permissions for components or access to cloud components, I was able to discover that the role did have permissions to generate a new “kubeconfig” file. This file could be generated using the cluster name that I had previously identified.

Kubernetes uses a YAML file known as kube-config to store cluster authentication information for kubectl. This file can be used to authenticate with the cluster kubeAPI either by sending a custom post request or by using the “kubectl” binary.

I was able to use the “update-kubeconfig” command to generate a kube-config file by specifying the role and cluster name.

Figure 8- Generating a new kube-config to the target cluster.
Figure 9- Although the user lacks permission to list namespaces directly, we can utilize “get services” to identify

Typically, in real-world environments, most namespaces have at least one service configured, but this is not the case here.

Get Chen Shiri’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Since the API did not have sufficient RBAC permissions to list namespaces, I had to find a workaround. To obtain the names of each namespace, I utilized the “list services” command with the “ — all-namespaces” flag along with the security group tags.

Figure 10: Now we can see all the services on the cluster and open ports (without active scan), and the namespaces names on the left.

I had access to list the names of the cluster’s namespaces.

Now I could retrieve information about the pods of and config files of the those namespaces

Figure 11 : listing pods of the backend containers.
7. The RIsks

From here we’ve several options, those risks don’t exist in any official Kubernetes or major cloud Kubernetes (GKS & AKS, etc.) because those particular attack vectors were the result of non-standard, insecure implementations , and without the flaws, the k8s capabilities wouldn’t be a security risk.

Exposure of K8’s namespace manifest, which contains details about its integration with services, databases, environment variables, etc.
Exec to pods — Due to integrated systems that very common and essential, such as monitoring and backup systems like Prisma, it is common to grant the role permission to exec, which results in the takeover of every namespace in the pod.
Takeover via vulnerable pod deployment- depends on the RBAC.
8. Access to the Kubernetes manifest

I got access to all the informations of the pods, including the container internal specification of commands and environment variables using the Kubernetes manifest.

Press enter or click to view image in full size
Figure 12: listing the information & configurations of relevant components in the Kubernetes orchestration

Attackers can use the permissions and bypass methods to view configurations and access pods. The attacker can access the Kubernetes manifest of all the pods, which allows access to the environment variables that usually contain secrets and information about services and sensitive systems.

In addition to the container data, we’ve got the risk of accessing the pods.

It was a challenge, since I didn’t have permissions to exec (connect) into pods.

But I’ve found a bypass for that.

9. How I accessed pods? accessing other namespaces

I achieved connection to the pods using the YAML below since the role has permissions to create pods.

In most environments the role is has exec priviliged for monitoring and log collection services such as prisma, but in a case of an hardened RBAC to the role we will only have access to create mirror pods- special pods created by Kubernetes itself for internal purposes, a potential bypass for this case is to the pods in this case. So we will create a new pod.

By setting the “mirror” field in the pod’s annotations to “true. This allow us to gain access to the target node and ultimately the pods.

10. Creating a vulnerable container

I built using a docker file an image with SSH configured The docker file will copy a public key from the host for SSH login.

The local vulnerable image is located in a local registry- at the attacker endpoint computer

run a local Docker registry using the command docker run -d -p 5000:5000 — restart=always — name registry registry:2.

Pod Specs: i created the deployment “vulnv3.yaml”

The new privileged pod has port 22 open, the deployment downloads my image

The node of the deployment, is the node of the target namespace!

The vulnerable pod:

apiVersion: v1
kind: Pod
metadata:
  name: vulnerable-mirror-pod
  namespace: ui-systems
spec:
  nodeName: 7931b048-dfa4-40f7-80f1-e4761226a673
  nodeSelector:
  kubernetes.io/hostname: ip-192-168-28-94.ec2.internal
  containers:
  - name: vulnerable-mirror-pod
  image: localhost:5000/vulnpod:v2
  volumeMounts:
  - name: docker-sock
  mountPath: /var/run/docker.sock
  securityContext:
  privileged: true
  ports:
  - containerPort: 22
  env:
  - name: MY_ENV_VAR
  value: "my_value"
  volumes:
  - name: docker-sock
  hostPath:
  path: /var/run/docker.sock

After this the ssh step we can breakout to the node with the following commands

df -h
Copy /dev/<host device>
chroot /hostsys /bin/bash
I made a deployment of a container to the target node.
I added SYS_Admin capability, which makes the container vulnerable to a breakout.

Now I connected to the pods exploited the container breakout vulnerability and had access to the node

Now I successfully gained the access to pods of every namespace in the node.

You can exec into pods using regular docker commands

Now we have access to all container’s informations: stored data, secrets & database authentication (if secret manager not in use, and if in use usually can connect him with the pod access)

11. Recap: A Systemic Failure

To review, the attack chain was comprised of the following steps:

First vulnerability:

Utilizing the metadata service to generate a token.
Generate an API requests with the token to get access to the EC2 Role.

Second vulnerability- roles generating kubeconfig

Using calls that available on the minimal role to communicate to get information about the target cluster/cloud components.
Using the information and “kubeconfig” command of AWS CLI to generate a new config.
Communicating with the “Kube API” using the config.
Using the API capabilities to get information about the target nodes, and deploy a new container is SSH configured.
SSH to the vulnerable container and escape into the host — the target node.
Lateral movement by utilizing the secrets & data on all all containers
12. How to remediate?

The service is vulnerable to the chain attack by default, Unfortunately it’s not possible to remove some permissions of the ec2 role.

But it’s possible to limit the access to retrieve it using IP rules from the containers.

To protect your environment, you’ll to implement the following practices:

Implement Ip rules from the containers, block insecure metadata services the instance from the containers.
Change the EC2 instance IAM role permissions, the minimal permissions are vulnerable
Consider third party protection service secure your environment.

If you like the research please like and subscribe for more articles.⬇️

Twitter- https://twitter.com/ChenShiri73
