---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-21_taking-over-google-cloud-shell-by-utilizing-capabilities-and-kubelet.md
original_filename: 2023-02-21_taking-over-google-cloud-shell-by-utilizing-capabilities-and-kubelet.md
title: Taking over “Google Cloud Shell” by utilizing capabilities and Kubelet
category: documents
detected_topics:
- automation-abuse
- access-control
- command-injection
- otp
- cloud-security
tags:
- imported
- documents
- automation-abuse
- access-control
- command-injection
- otp
- cloud-security
language: en
raw_sha256: e20719698dd87af1ba6391e50b707d92e080b379e8bfa022d0ed3a34f0a2ca29
text_sha256: e22304086f2c3549357ef0de63d2dc01357e7aa00fb91574a833bf663695c927
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Taking over “Google Cloud Shell” by utilizing capabilities and Kubelet

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-21_taking-over-google-cloud-shell-by-utilizing-capabilities-and-kubelet.md
- Source Type: markdown
- Detected Topics: automation-abuse, access-control, command-injection, otp, cloud-security
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `e20719698dd87af1ba6391e50b707d92e080b379e8bfa022d0ed3a34f0a2ca29`
- Text SHA256: `e22304086f2c3549357ef0de63d2dc01357e7aa00fb91574a833bf663695c927`


## Content

---
title: "Taking over “Google Cloud Shell” by utilizing capabilities and Kubelet"
url: "https://medium.com/@chenshiri/taking-over-google-cloud-shell-by-utilizing-capabilities-and-kubelet-fd5e2417f286"
authors: ["Chen Shiri (@ChenShiri73)"]
bugs: ["Container escape", "RCE", "Kubernetes"]
publication_date: "2023-02-21"
added_date: "2023-05-15"
source: "pentester.land/writeups.json"
original_index: 1497
scraped_via: "browseros"
---

# Taking over “Google Cloud Shell” by utilizing capabilities and Kubelet

Taking over “Google Cloud Shell” by utilizing capabilities and Kubelet
Chen Shiri
Follow
8 min read
·
Feb 21, 2023

134

1

Press enter or click to view image in full size

The research performed on the boundaries of Google Bughunters

Note: All information is for ethical purposes only.

Table of Contents

1. What is google cloud shell? and what’s the problem?
2. Environment details
3. Hack 1-Breaking out of the Container and Getting read/write access
4. Hack 2- Gaining execution on the host
5. Kubelet Key on the Node
6. Causes & Mitigations

What is google cloud shell? and what’s the problem?

“Google Cloud Shell is a free interactive shell for running projects and testing within your web browser”

Link- https://shell.cloud.google.com/

You don’t need to be registered to GCP for having a shell, just a standard Google account.

That is not the regular cloud shell for GCP Accounts (requiring a sign up to the cloud)

The Google cloud shell allows you to run your projects online and to collaborate and share it with others.

Press enter or click to view image in full size
Figure 1- Using Google Cloud Shell to run existing code

I read about a few bug bounties for this platform, among them was about “docker.sock” a container escape, which has already been fixed!

Press enter or click to view image in full size

https://threatpost.com/100k-google-cloud-shell-root-compromise/153665/

https://cisomag.com/dutch-researcher-claims-google-bug-bounty/

This article will detail about my research into google cloud shell, the vulnerabilities result on secrets and other containers data exposed, tokens etc.

This attack vector could allow malicious actors in environments to read and modify the data that stored and accessible from other containers and services.

2. Environment details

After observing the environment, I’ve noticed that every time that I’m running a code he is running in a new container

There are 4 main websites in our attack chain, and we need to pay attention to these as we follow the twists and turns of this attack:

Press enter or click to view image in full size
Figure2: main websites

Now I wanted to know what kind of system I’ve access to.

As we can see the container’s control group

Cat /proc/1/cgroup
Press enter or click to view image in full size
Figure3- the container runs in Kubernetes orchestration

The container IP is 172.17.0.4 and from this we can assume that the host’s IP is the default IP of 172.17.0.1

Press enter or click to view image in full size
Figure 4: the container’s and the node IP below

3. Hack 1-Breaking out of the Container and Getting read/write access node of Google’s Infrastructure-

Linux capabilities provide a subset of the available root privileges to a process.

This effectively breaks up root privileges into smaller and distinctive units.

Each of these units can then be independently be granted to processes.

I checked the capabilities of the containers, as you can see, the container has CAP_MKNOD and CAP_SYS_ADMIN capabilities that considered as insecure capabilities for running containers.

$ Capsh — print
Press enter or click to view image in full size
Figure 4: the container is running with insecure capabilities

First, I attempted to access into the host using a number of commonly used techniques that utilize “sys_admin”, but they were protected (hardening, profiles)

I noticed that most the commands for devices information lsuch as “fdisk -l” are not working, but “df -h is” permitted

As we can see on figure 5 “/dev/sda1” device (of the host) has “/root” directory mounted on.

So we can understand that “dev/sda1” is the host filesystem.

Also, As we can see the container has just about 4.5 GB of storage, while the host has more than 60 GB.

To test whether the container has access to the host, I tried to create a temporary file system (tmpfs) and mount it to /mnt:

And the system created.

$ Mount -t tmpfs none /dst
Press enter or click to view image in full size
Figure 5: “dev/sda1 host device and mounting permissions

Now I used “CAP_MK_NOD” permissions to access the node instance.

By that we can gain Read/Write permissions on the node

$ Mkdir -p /mnt/host
$ Mount <hostfilesystem> /mnt/host
$ Ls /mnt/host
Press enter or click to view image in full size
Figure 6: Utilizing the host device for gaining access to the host (Node) from the container
I had access to 60+ GB of storage per session.
Access every container on the node- DNS, frontend & backend Containers.
I had access to critical files of Google’s shell mechanism- authorization, credentials and tokens, images and container registry.
Access to different shell sessions on the same account — some of the sessions are being shared with others.
I had access to the instance information on google cloud, details about the instance and about the deployment of all the containers on the node.
Access to/var/lib/kubelet/pods: This directory contains the configuration and data for the containers running on the node. Each subdirectory represents a pod, and within each pod directory, there are subdirectories for each container in the pod.
Access to /var/log/containers: This directory contains the log files for the containers running on the node. The log files are named after the container’s ID and can be useful for troubleshooting issues with containers.

Once I looked at the hosts partition files, I identified files that contained information about authentication and environment, including “Environment.json.”

Get Chen Shiri’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The “Environment.json” file, which provides details about the instance and authentication, is used to configure the environment.

Press enter or click to view image in full size
Figures 7: examining “environment.json” deployment.

“devops.cloud.google.com” website is Google’s official documentation and resource hub for DevOps on Google Cloud

Press enter or click to view image in full size
Figures 8: examining “environment.json” deployment.
Press enter or click to view image in full size
Figures 9: examining “environment.json” deployment.

I had access to every container on the node.

Press enter or click to view image in full size
Figure 10: accessing the environment pods and container config.

4. Hack 2- Gaining execution on the host and getting root on the node

I exploited “cap_sys_admin” to get execution on the host.

To trigger this attack i needed a cgroup where we can create a release_agent file and trigger release_agent invocation by killing all processes in the cgroup, this way I mounted a cgroup controller and created a child cgroup.

To do that, I created a “/tmp/cgrp” directory, mounted the RDMA cgroup controller and created a child cgroup

Next, I enabled cgroup notifications on release of the “x” cgroup by writing a 1 to its notify_on_release file. I also set the RDMA cgroup release agent to execute a “/cmd” script, which I will create later in the container by writing the /cmd script path on the host to the release_agent file.

I got the container’s path on the host from the “/etc/mtab” file.

The files i add or modify in the container are present on the host, and it is possible to modify them from both worlds: the path in the container and their path on the host.

Now I have created the “/cmd” script such that it will execute the “ps aux” command and save its output into “/output” on the container by specifying the full path of the output file on the host.

Now I have executed the attack by spawning a process that immediately ends inside the “x” child cgroup.

Press enter or click to view image in full size
Figure 11: The full attack

By creating a “/bin/sh” process and writing its PID to the “cgroup.procs” file in “x” child cgroup directory, the script on the host will execute after “/bin/sh” exits.

The output of “ps aux” performed on the host is then saved to the “/output” file inside the container.

As you can see, know commands are executed on the host

Press enter or click to view image in full size
Figure 12: Verifying the host IP
Press enter or click to view image in full size

Shell on the node

Press enter or click to view image in full size
Figure 13 — Running the execution automation

I had full access to all the pods in the environment on the Node

Docker access on other pods:

Press enter or click to view image in full size
Figure 14: Able to execute regular “kubectl” commands on the node

I sent the article to the google issue tracker — issue 192165360

And the marked it as intended behavior

So I continued my research 👨🏻‍💻👾.

What can you use this issue? you can have free machines with high memory and storage, gmail and drive are limited to 15 gb of storage, with this you can have a storage of 60+

Unfortunately, after sending my vulnerability, the execution was fixed!

5. Kubelet Key on the Node

I accessed “kubelet.key” and “kublet.crt” on the node

The kubelet.key file used by the Kubernetes kubelet component for secure communication with the Kubernetes API server.

The kubelet is an essential component of a Kubernetes cluster that runs on each node and is responsible for managing and maintaining the containers running on that node.

When the kubelet starts up, it generates a certificate signing request (CSR) and sends it to the API server. The API server then signs the CSR with the cluster’s CA (Certificate Authority) to generate a certificate that the kubelet uses to authenticate itself with the API server.

The kubelet.key file contains the private key corresponding to the kubelet’s certificate, which is used to establish a secure connection between the kubelet and the API server. This ensures that all communication between the kubelet and the API server is encrypted and cannot be intercepted or tampered with by unauthorized parties.

In summary, the kubelet.key file is an essential component of a Kubernetes cluster’s security infrastructure, allowing the kubelet to securely communicate with the API

server and ensuring the confidentiality and integrity of cluster communication.

Using the key I could intercept the communication of the API Server, which can be used for listing other customer’s nodes etc.

But I stopped here due to customer information

Press enter or click to view image in full size
Figure 16: “kubelet.key” and “kublet.crt” on the node
Press enter or click to view image in full size
Figure 17: Accessing “kubelet.key” and “kublet.crt” on the node

After sending these other findings, i got the the same response.

6. Causes & Mitigations

By default, containers are not isolated from the host and can reach the file system of the host.
Block network connection between containers and nodes. That can be done through IP tables https://docs.docker.com/network/iptables/.
When a container is built without any additional capabilities, “CAP MKNOD” is present. remove any unnecessary capabilities.
Further security measures, such as Secomp profile, can protect it- https://docs.docker.com/engine/security/seccomp/
When installing Docker on a host, it creates a new network interface with the IP address 172.17.0.1. Someone with even a basic understanding of Docker containers could readily guess that this is the IP address of the node. using a different IP address for the node instead the default address of 172.17.0.1.

If you like the research please like and subscribe for more articles.⬇️

Twitter- https://twitter.com/ChenShiri73
