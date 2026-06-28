---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-06_part-2-the-two-privescs.md
original_filename: 2022-05-06_part-2-the-two-privescs.md
title: 'Part 2: The two privescs'
category: documents
detected_topics:
- access-control
- command-injection
- automation-abuse
- cloud-security
- supply-chain
- otp
tags:
- imported
- documents
- access-control
- command-injection
- automation-abuse
- cloud-security
- supply-chain
- otp
language: en
raw_sha256: b2af0f43747b117768cd4a023c98ccf0a476e1e06962445d25f5b4c839cee8a2
text_sha256: 4003948064ae53d5f81f8a9dace3e2601a0c67d0bfd30f2f492c871f66112dce
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Part 2: The two privescs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-06_part-2-the-two-privescs.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, automation-abuse, cloud-security, supply-chain, otp
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `b2af0f43747b117768cd4a023c98ccf0a476e1e06962445d25f5b4c839cee8a2`
- Text SHA256: `4003948064ae53d5f81f8a9dace3e2601a0c67d0bfd30f2f492c871f66112dce`


## Content

---
title: "Part 2: The two privescs"
page_title: "Cloudflare Pages, part 2: The two privescs"
url: "https://www.assetnote.io/resources/research/cloudflare-pages-part-2-the-two-privescs"
final_url: "https://www.assetnote.io/resources/research/cloudflare-pages-part-2-the-two-privescs"
authors: ["Sean Yeoh (@seanyeoh)", "James Hebden (@devec0)"]
programs: ["Cloudflare"]
bugs: ["Command injection", "Container escape", "Bash Path injection", "RCE", "Local Privilege Escalation", "Information disclosure"]
publication_date: "2022-05-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2658
---

[Research Notes](/resources/research)

Security Research

May 6, 2022

# Cloudflare Pages, part 2: The two privescs

No items found.

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/653795bb35bc995a6f921d3f_citrixbleed.svg)

Creative Commons license

![Bart Simpson sliding down a staircase, before falling off the railing and hitting each stair on the way down. bart is labelled with the words 'cloudflare pages' and the steps are labeled with various security issues.](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/659feb72bf22b29b278079d0_bart-slide.png)

  * [Introduction](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt2/#introduction)
  * [OrangeRa1n Jailbreak](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt2/#orangera1n-jailbreak)
  * [Conclusion](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt2/#conclusion)
  * [Part 3](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt2/#part-3)

### Introduction

Following on from our 1st story, we’ll be continuing the epic tale of our research into Cloudflare pages in this second installment. If you haven’t read part 1, you can read it [here](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt1/).

We pick up where we left off, after harvesting a bunch of secrets from the Cloudflare pages build system, and getting our reverse shell running as the <span class="code_single-line">AzDevOps+</span> user, which gave us <span class="code_single-line">root</span> in the container.

### OrangeRa1n Jailbreak

As we reported the previous vulnerabilities to Cloudflare, they systemically applied fixes to the code orchestrating the builds, which locked us back out. We had to find a new way back in each time. While we still had access though, we wanted to try and find further injection bugs. Having exhausted the low hanging fruit for escaping the <span class="code_single-line">buildbot</span> user, we now wanted to get a root shell in the Cloudflare Pages CI hosts. You may remember us talking a big game about containers, privilege escalation, and container escape earlier in this post. In any CD system you are looking at, these can often lead to some really good findings if you can achieve them - this is because the container is often improperly treated as a security boundary by application developers. In the case of Cloudflare pages, this was the case.

In the previous post in thise series, we talked about the <span class="code_single-line">buildbot</span> user, and the <span class="code_single-line">AzDevOps+</span> user, and the fact that our build scripts were running in the context of this user as part of the build process, potentially inside a container. The previous two findings were all performed in the context of this <span class="code_single-line">buildbot</span> user, and eventually <span class="code_single-line">AzDevOps+</span> \- which gave us <span class="code_single-line">root</span> in the container, but we wanted to try a little harder and see if we could execute code as <span class="code_single-line">root</span> on the host, and then potentially escape the container. First let’s look for some other ways we can get back into the <span class="code_single-line">AzDevOps+</span> user, should we get locked out - given we currently have access and the build tooling source code.

Referring again to the screenshot from the first set of findings, of the process tree -

![a screenshot of a process tree from within a reverse shell, showing our process is running as the AzDevOps+ user we mentioned previously](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/659fec426624e587105674ce_pstree-azdevops.png)

You can see here that we have processes in the tree running as root, and as <span class="code_single-line">AzDevops+</span>. Interestingly, this process tree tells us quite a lot about the execution environment

  * The node process running as root, has a PID of 1. Normally, PID 1 is the initialisation system under Linux (either SysV init or systemd), and the fact that PID 1 is showing as node is a strong indicator that we are in fact running inside a container, and this node process is our container entrypoint.
  * The build script is running as buildbot, but further up the process tree, we can see the sudo to the buildbot user, running as root. Given the parent process of sudo is running as AzureDevOps - this tells us that the AzureDevOps user has root access via sudo.
  * The fact that the sudo is happening as part of a bash script strongly suggests that AzureDevOps has passwordless sudo. When automating sudo calls, entering a password into sudo programmatically via a script requires good secrets management, and significant extra engineering effort - mostly, folks do not bother with this and just grant passwordless sudo to the user running the automation (or build script, in our case).
  * We can see that there are a mixture of node processes and bash scripts running from the __w directory, but also from /opt/pages. The /opt/pages folder strongly suggests this part of the process tree is part of the pages build, and we can potentially influence it with our build.

Given the above factors, compromising the integrity of any of the scripts in the process tree prior to the sudo have a high chance of giving us passwordless root, inside a container. And having root in a container gives us a strong chance of escaping the container. With that in mind, we dug into the scripts in question.

We focused first on the page build script, <span class="code_single-line">/opt/pages/build_tool/build.sh</span>. Sadly, this looked fairly simple and didn’t present a lot of opportunity for command injection. We moved further up the process tree.

Looking at the .js scripts in the <span class="code_single-line">__w</span> directory, it became apparent pretty quickly that these were part of the Microsoft Azure DevOps Pipelines agent. We’d like to quickly take a moment to thank Microsoft for their transparency and recent commitment to Open Source - because the entire build agent was available to us on GitHub.

Reading the documentation for Pipelines, you are [very quickly](https://docs.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline?view=azure-devops) introduced to the format and purpose of the .azure-pipelines.yml file. The Azure DevOps Pipelines agent operates on a .yaml configuration file, which we briefly mentioned earlier in this post. Essentially, it is a workflow file and details the steps which will be executed by the agent inside of an Azure VM when the pipeline is executed in Azure DevOps. We didn’t actually have to dig too deep into the agent code to work out how this all works due to the extensive documentation.

Reading over the documentation, looking for ways we might be able to run our own code under the Pipelines agent, Sean noticed [this documentation section](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/variables?view=azure-devops&tabs=yaml%2Cbatch#set-a-job-scoped-variable-from-a-script) on Azure DevOps Pipelines variables, specifically that that can be interpolated inside the YAML. Normally, you would assume that if Cloudflare pages was generating an Azure DevOps Pipeline file to run our builds, they would be sanitising variables for the interpolation patterns detailed in the document.

To test this assumption, which is a key part of finding good bugs - we tried to insert some interpolated Azure DevOps Pipeline variables into our build settings, to see if we could use them to interpolate strings we controlled into the build steps we should not be able to control. Keeping In mind the commands in the Pipeline configuration would be running as the AzureDevOps user, which we strongly suspect has passwordless sudo, we went looking for a useful variable to set.

We found the below command which uses the <span class="code_single-line">account_env</span> variable to generate the command used to run the build script. If we can control <span class="code_single-line">account_env</span>, we can likely run an arbitrary command before the <span class="code_single-line">sudo</span> happens, as <span class="code_single-line">$()</span> substitutions happen prior to execution of a command in bash, in a subshell, which runs in the context of the user running the command. In our case, the contents of account_env would be evaluated (and executed!) as the AzureDevops user prior to the <span class="code_single-line">sudo</span> to buildbot, which is exactly the outcome we want.

![a screenshot of the post-status-update part of the build tooling pipeline used by azure devops, where $\(account_env\) is present in the commandline](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/659fec6ddcfcc68597f40ed0_account-env-pipeline.png)

With this target input in mind, we added the following to the “build command” in our Cloudflare pages project -

echo ok shell please

echo '##vso[task.setvariable variable=account_env];bash /tmp/shell.sh;echo '

This would tell Azure DevOps Pipelines (hopefully) to set the <span class="code_single-line">account_env</span> variable in the Pipelines configuration to the string ‘;bash /tmp/shell.sh; echo’. <span class="code_single-line">/tmp/shell.sh</span> is unsurprisingly, a reverse shell - and is part of our Git repository. If the variable injection works, and we can inject this command, the reverse shell should be checked out in time for the evaluation of <span class="code_single-line">$(account_env)</span> to happen, which would trigger our reverse shell as the AzureDevOps user.

Running the job, we receive -

![a screenshot of a reverse shell session, with the whois command showing the user as AzDevOps_azpcontainer](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/659fec7f093bb2734968fb08_azdevops-shell.png)

…a shell, as <span class="code_single-line">AzureDevops_azpcontainer</span> \- the full, non-truncated username running the Pipelines again. The username also strongly supports the fact that we are in a container, as well as the UUID hostname, which is commonly seen with Docker containers. We’ve now got a second way back to this user, and another report to file.

Now that we’ve got a few ways in, it’s time to really break out the privilege escalation and go for a full container escape. Firstly, in our new context, we poke around the filesystem. One of the easiest ways to break out of containers (and a bit of a cardinal sin) is if the Docker socket is bind-mounted or accessible via TCP without TLS from inside the container. As luck would have it, there was indeed a <span class="code_single-line">/var/run/docker.sock</span> present in the environment. It was owned by root. Testing our theory that the <span class="code_single-line">root</span> in the container we could access via <span class="code_single-line">sudo</span> would still be able to access the socket, despite the user namespace remapping which occurs by default with <span class="code_single-line">docker</span>, meaning the UID of <span class="code_single-line">root</span> in the container maps to an ineffective user ID in the host kernel. Naturally, we attempted to check what was at the other end of the docker socket.

![a screenshot of the reverse shell after running sudo to gain root access in the container, and installing the docker package](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/659fec8a3466e6efb277a265_sudo-su-docker-install.png)

So, we installed docker inside our container. Executing <span class="code_single-line">mount</span> showed the presence of <span class="code_single-line">overlayfs</span> and a series of bind mounts for files like <span class="code_single-line">/etc/resolv.conf</span>, confirming we are indeed inside of a docker container, so an escape would be worthwhile if we could pull it off.

Let’s break out!

At this point, we had <span class="code_single-line">docker</span> installed, and <span class="code_single-line">root</span> access inside the container. The container escape with this access is actually really easy. We knew at this point we were trapped inside -

  * A process namespace, which would be limiting the processes and environment variables we could see
  * A network namespace, limiting what kind of networks we had access to
  * A user namespace, meaning our root account wasn’t the “real” root user on the host
  * And other, less problematic namespaces and cgroups

We simply ran the below command, to create a “super privileged container” -
  
  
  sudo docker run -ti --privileged --net=host -v /:/host -v /dev:/dev -v /run:/run ubuntu:latest
  
  

Let’s dig into those arguments a little -

  * <span class="code_single-line">-ti</span> attaches a PTY and runs the command interactively, given us an interactive shell

  * <span class="code_single-line">\--net=host</span> disabled network namespace creation. This means our network namespace is the “root” or host network namespace, we are not confined in this regard. We can access all network interfaces, firewall rules (iptables) and network sockets on the host.

  * <span class="code_single-line">\--uts=host</span> disabled UTS namespace creation. This means our hostname information will be the same as the actual host. Not essential, but cool to demonstrate impact.

  * <span class="code_single-line">\--ipc=host</span> disabled IPC namespace creation. We have full access to host IPC.

  * <span class="code_single-line">\--pid=host</span> disabled process namespace creation. This means our PID namespace is the “root” or host namespace, we can see all processes.

  * <span class="code_single-line">-v /:/rootfs</span> mounts the host server’s filesystem inside the directory /rootfs inside our container. Whilst this doesn’t disable the mount namespace (we still have our own filesystem for the container) it does allow access to all files on the host.

  * <span class="code_single-line">\--privileged</span> is going to be very useful for us in proving impact on this issue, as it allows us to operate inside the same user namespace as the actual server (our root account is the “real” root account) and also allows full access to the host’s /proc filesystem

Boom.

![a screenshot showing the above docker command being run and the result being a root shell on the host machine with access to the host filesystem, showing the hostname of the host system](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/659feca28231a3d939ad2562_super-privileged-container.png)

Googling, we realised that these were in fact tokens which the instance used for authenticating with Azure Devops itself. Interesting! Similar to instance AWS tokens obtainable via the cloud instance metadata APIs. Using these we could say a friendly Windows Hello to Cloudflare’s Azure Devops Organisation.
  
  
  curl https://cloudflarepages@dev.azure.com/cloudflarepages/_apis/teams?api-version=6.0-preview.3 -H "Authorization: Bearer $SECRET_SYSTEM_ACCESSTOKEN" | jq`
  curl https://cloudflarepages@dev.azure.com/cloudflarepages/_apis/projects/<uuid>/teams/<uuid>/members?api-version=6.0 -H "Authorization: Bearer $SECRET_SYSTEM_ACCESSTOKEN" | jq
  
  

With this, we were able to list all of Cloudflare’s users within this project:

![a screenshot of the API call response for listing the users in the Cloudflare org we had access to, via the API, showing a list of Cloudflare employees who has access to Cloudflare's org used for pages](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/659fecc18e5fda447cfcf452_cloudflare-users.png)

We were also be able to access all Cloudflare pages build history for all users on Cloudflare pages -
  
  
  curl https://cloudflarepages@dev.azure.com/cloudflarepages/Pages/_apis/pipelines/2/runs?api-version=6.0-preview.1 -H "Authorization: Bearer $SECRET_SYSTEM_ACCESSTOKEN" | jq
  
  

![a screenshot showing the build history in DevOps pipelines for the cloudflare pages project, including our builds](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/659fecd3b920cb7184a0d335_cloudflare-builds.png)

### Conclusion

We had achieved our goal of stealing Github and Cloudflare tokens from the platform, but we had also managed privilege escalation to root in the container, escaping the confinement of the container we were in to get a root shell on the host, and ultimately getting access to the Azure Devops Organisation for Cloudflare.

In remediating this issue, there’s multiple points of defense in depth that could be utilized to prevent this from occurring:

  * The initial vector was caused by a subtle feature of Azure Devops Pipelines. As recommended only in the security section of their documentation, they suggest adding a restriction on logging commands to prevent this kind of exposure (<https://docs.microsoft.com/en-us/azure/devops/pipelines/security/templates?view=azure-devops#agent-logging-command-restrictions>); We point to Felix Wilhelm’s work at Google Project Zero that similarly addressed these concerns [https://bugs.chromium.org/p/project-zero/issues/detail?id=2070&can=2&q=&colspec=ID%20Type%20Status%20Priority%20Milestone%20Owner%20Summary&cells=ids](https://bugs.chromium.org/p/project-zero/issues/detail?id=2070&can=2&q=&colspec=ID%20Type%20Status%20Priority%20Milestone%20Owner%20Summary&cells=ids)
  * Providing passwordless sudo as the azure devops user resulted in us being able to privilege escalate to root within the container. Creating a password or heavily restricting the permissions of passwordless sudo to only specific necessary binaries may have mitigated this risk partially
  * Mounting the docker.sock socket into the container allowed us to escape out of the container. By not mounting this file at all, or restricting permissions to read and write from this socket file may have mitigated this risk if we weren’t able to escalate to root.
  * Limiting possible syscalls using technologies like SELinux, AppArmor, or emulating syscalls using technology such as gVisor prevent the use of inappropriate syscalls which indicate compromise. In our case, our builds had no business calling syscalls such as mount, chroot, clone - but here we were spawning containers and mounting filesystems.
  * Directly executing the commands with interpolated variables with a high privilege user resulted in this vulnerability, so sanitizing the environment variables and dropping privileges before executing the operation would have also prevented this risk.

At this point, we submitted all our bugs to Cloudflare, and they very quickly triaged and began attempting to remediate the issues. We asked to disclose initially, however very reasonably their response was to request we stop testing until they had mitigated the vulnerabilities.

### Part 3

After assessing their options, Cloudflare decided to pursue different architectures for Cloudflare Pages not based on Azure Pipelines. They also requested that we not disclose until they had finished their rearchitecture. It’s not every day you get to say you hacked a platform to the point where it had to be totally rearchitected - but here we are. You might think that would have been enough, but join us in [The return of the secrets: part 3](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt3/) for the final part of our research, where we look at the re-architected platform. Or, head back to [part 1](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt1).

Written by:

James Hebden

Sean Yeoh

Your subscription could not be saved. Please try again. 

Your subscription has been successful. 

Get updates on our research

Subscribe to our newsletter and stay updated on the newest research, security advisories, and more!

Enter your email address to subscribe

Provide your email address to subscribe. For e.g abc@xyz.com 

SUBSCRIBE 

### More Like This

[Security ResearchNew!Doing the Due Diligence: Analyzing the Next.js Middleware Bypass (CVE-2025-29927)Read moreRead on ASN Blog](/resources/research/doing-the-due-diligence-analyzing-the-next-js-middleware-bypass-cve-2025-29927)

[Security ResearchNew!How an obscure PHP footgun led to RCE in Craft CMSRead moreRead on ASN Blog](/resources/research/how-an-obscure-php-footgun-led-to-rce-in-craft-cms)

[Security ResearchNew!Citrix Denial of Service: Analysis of CVE-2024-8534Read moreRead on ASN Blog](/resources/research/citrix-denial-of-service-analysis-of-cve-2024-8534)

[Security ResearchNew!Nginx/Apache Path Confusion to Auth Bypass in PAN-OS (CVE-2025-0108)Read moreRead on ASN Blog](/resources/research/nginx-apache-path-confusion-to-auth-bypass-in-pan-os)

[Security ResearchNew!Leveraging An Order of Operations Bug to Achieve RCE in Sitecore 8.x - 10.xRead moreRead on ASN Blog](/resources/research/leveraging-an-order-of-operations-bug-to-achieve-rce-in-sitecore-8-x---10-x)

[Security ResearchNew!Insecurity through Censorship: Vulnerabilities Caused by The Great FirewallRead moreRead on ASN Blog](/resources/research/insecurity-through-censorship-vulnerabilities-caused-by-the-great-firewall)

[Back to All](/resources/research)

### Ready to get started?

Get on a call with our team and learn how Assetnote can change the way you secure your attack surface. We'll set you up with a trial instance so you can see the impact for yourself.

[Request a Demo](/demo)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/64241df2676aeba82706ffe8_assetnote-logo.svg)

Address:  
Level 10, 12 Creek Street, Brisbane QLD, 4000  
‍  
Contact:  
[contact@assetnote.io  
  
](mailto:contact@assetnote.io)Press Inquiries:[  
](mailto:contact@assetnote.io)[press@assetnote.io](mailto:press@assetnote.io)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/661f041240ed96ed7a03fe6f_61dc1beb212a1202fc512a76_SOC%202-03-p-500.png)

[](https://twitter.com/assetnote)[](https://www.linkedin.com/company/assetnote/)

Platform Features

[Continuous Asset Discovery](/platform/asset-discovery)

[Deep Asset Enrichment](/platform/asset-enrichment)

[Assetnote Exposure Engine](/platform/assetnote-exposure-engine)

[Expert Security Research](/platform/expert-security-research)

[Collaborative Workflows](/platform/collaborative-workflows)

[Customization](/platform/customization)

Use Cases

[Continuous Asset Discovery and Inventory](/use-cases/continuous-asset-discovery-and-inventory)

[Real-Time Exposure Monitoring](/use-cases/continuous-security-monitoring)

[Attack Surface Reduction](/use-cases/attack-surface-reduction)

[Mergers & Acquisitions](/use-cases/mergers-and-acquisitions)

[Bug Bounty Readiness](/use-cases/bug-bounty-readiness)

© 2026 Assetnote. All rights reserved.

[Privacy Policy](https://assetnote.io/policies/privacy-policy)
