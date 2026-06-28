---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-04-15_fixing-typos-and-breaching-microsofts-perimeter.md
original_filename: 2024-04-15_fixing-typos-and-breaching-microsofts-perimeter.md
title: Fixing Typos And Breaching Microsoft’s Perimeter
category: documents
detected_topics:
- command-injection
- supply-chain
- sso
- ssrf
- otp
- api-security
tags:
- imported
- documents
- command-injection
- supply-chain
- sso
- ssrf
- otp
- api-security
language: en
raw_sha256: b59bce8f046143ae7912658d8f435a61604759665594d9aae51405d7a2bdeaf8
text_sha256: eb84fd41b033d451ced53c27d8fdd211f95f58695feccd27bb8306aad15f613b
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# Fixing Typos And Breaching Microsoft’s Perimeter

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-04-15_fixing-typos-and-breaching-microsofts-perimeter.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, sso, ssrf, otp, api-security
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `b59bce8f046143ae7912658d8f435a61604759665594d9aae51405d7a2bdeaf8`
- Text SHA256: `eb84fd41b033d451ced53c27d8fdd211f95f58695feccd27bb8306aad15f613b`


## Content

---
title: "Fixing Typos And Breaching Microsoft’s Perimeter"
page_title: "Fixing Typos and Breaching Microsoft’s Perimeter  – John Stawinski IV"
url: "https://johnstawinski.com/2024/04/15/fixing-typos-and-breaching-microsofts-perimeter/"
final_url: "https://johnstawinski.com/2024/04/15/fixing-typos-and-breaching-microsofts-perimeter/"
authors: ["John Stawinski", "Adnan Khan (@adnanthekhan)"]
programs: ["Microsoft"]
bugs: ["RCE", "CI/CD", "Supply chain attack"]
publication_date: "2024-04-15"
added_date: "2024-05-13"
source: "pentester.land/writeups.json"
original_index: 338
---

April 15, 2024

# Fixing Typos and Breaching Microsoft’s Perimeter 

Progressing through certifications, developing as a red teamer, breaking into Bug Bounty — many steps along my security journey have been difficult.

#### **One of the easiest things I’ve done was breach Microsoft’s perimeter.**

Two weeks before compromising a domain-joined Microsoft server, former coworker Adnan Khan discovered a critical supply chain vulnerability in [GitHub’s Runner Images](https://adnanthekhan.com/2023/12/20/one-supply-chain-attack-to-rule-them-all/). Inspired by this attack and CI/CD research we’d performed during Red Team engagements, we teamed up to see who else was vulnerable.

Microsoft DeepSpeed was our first joint target, and my first time ever performing public vulnerability research. 

During our attack on DeepSpeed, we compromised a server **joined to Microsoft’s largest Active Directory domain with the privileges of a Microsoft Senior Developer.**

This is the story of how we breached Microsoft, kick-started a partnership that would change the landscape of self-hosted GitHub CI/CD security, and the growing pains we experienced along the way.

# What is DeepSpeed?

[Microsoft DeepSpeed](https://github.com/microsoft/DeepSpeed) is an open-source deep-learning optimization library. “Open-source” means that anyone can see the application’s code on the public internet. If you don’t understand ML, don’t worry – it is mostly irrelevant to this vulnerability. **What’s more important is the fact that Microsoft uses GitHub to store DeepSpeed’s source code.**

If you’ve been following [the research we’ve released so far](https://johnstawinski.com/2024/01/05/worse-than-solarwinds-three-steps-to-hack-blockchains-github-and-ml-through-github-actions/), you probably suspect that the Microsoft DeepSpeed repository uses self-hosted runners. You’re correct. 

If you haven’t been following and are unfamiliar with self-hosted runners, here’s the TL;DR.

# Self-hosted Runner Background

GitHub allows organizations to attach machines (computers) to repositories called “self-hosted runners”. These runners execute code specified within workflows as part of the GitHub Actions CI/CD process.

For example, let’s say Microsoft wants to run a set of tests when a GitHub user wants to contribute their own code by submitting a pull request. Microsoft can define these tests in a YAML workflow file used by GitHub Actions and configure the workflow to run on the pull_request trigger. **Now, whenever a user submits a pull request, the tests will execute on a runner.** This way, repository maintainers don’t need to manually test everyone’s code before merging.

**GitHub recommends against using self-hosted runners on a public repository** , as misconfigurations could allow external attackers to compromise the runners and gain a foothold in the organization’s infrastructure or tamper with subsequent builds. Instead, GitHub recommends using GitHub-hosted runners, which are available for free (up to a limit) to all GitHub repositories.

It is possible for an organization to securely use self-hosted runners on a public repository**if the runners are ephemeral, isolated, and permissions are locked down**.

# Where did Microsoft Go Wrong?

Microsoft violated all of the guidelines I just laid out. They used a **domain-joined workstation** as a non-ephemeral, self-hosted runner on the public DeepSpeed repository. Essentially, an employee took one of their computers and offered it up to everyone on the internet.

Many of our other attacks, like [our attack on PyTorch](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/), required implantation, reconnaissance, crazy token pivots, and secret stealing to prove impact. **With DeepSpeed, all we had to do was get RCE and we had breached one of the largest organizations in the world.**

By default, when a self-hosted runner is attached to a repository, any of that repository’s workflows can use that runner. This setting also applies to **workflows from fork pull requests.** The result of these settings is that, by default, any repository contributor can execute code on the self-hosted runner by submitting a malicious PR.

_Note: A “contributor” to a GitHub repository is anyone who has added code to the repository. Typically, someone becomes a contributor by submitting a pull request that then gets merged into the default branch. More on this later._

# Finding Typos

It didn’t take long to identify DeepSpeed as a target. We didn’t have any of our advanced search and scanning infrastructure yet, but a simple GitHub search for “self-hosted” brought up DeepSpeed in the Fall of 2023, with its 32,000 stars, as one of the first results. The repository had enough traffic that we could identify workflows from contributors that ran without approval. 

**Step one was becoming a contributor.** To do this, we had to submit a pull request that got accepted and merged by a DeepSpeed maintainer. Typically, engineers will submit PRs for bug fixes or feature additions, but we didn’t want to spend the time doing that. Instead, we decided to try submitting a typo fix – finding a typo in their documentation and submitting a PR that fixes that typo.

We fired up Grammarly and got to work.

![](https://lh7-us.googleusercontent.com/2cdKOZ5vwQx7ynUOEnJaw4xaopqKaFpzHDD77fyBj-dDqT-GQKjTBo4dDcbsL5a4mh9y6HqBjBCtiStUzaIeugC4YAXPavNqkW5-fl4cwAiro9ZcL2mBtdQOOltgvhlTK-RMsQDgSRDDDeTw0feFxnM)

_This pic is officially a staple of all my CI/CD blog posts._

Quickly we discovered a sentence in SECURITY.md that had an additional word. The sentence read “…please download it from the the Microsoft’s Security Response Center…”. We removed the extra “the” and submitted our PR.

![](https://lh7-us.googleusercontent.com/n2jUunpr9PxhneTWFxl-Nnz4-zXKw5MupHxtKSERy45w8UMAfcCqD5eu5iyG-xNiQRSJsz4O7RYy1aDpWvqXq8DhbrmXJpOJ7bTe5tsLfLVMUmSZXB7mLqhv1DSyKkmyHuxjY6Dz12xliHNSMh5wkWU)

_After finding a typo in SECURITY.md, we submitted a pull request. Once Microsoft merged the PR, we were now a “Contributor” to the DeepSpeed repository._

Microsoft merged our PR within days. We hadn’t identified any accessible repository secrets, and the self-hosted runner workflows had limited GITHUB_TOKEN permissions, so to prove impact we’d need to get on the runner and search for secrets on the filesystem. At the time, we knew very little about the runner aside from architecture data in workflow logs.

# 3,2,1, Launch

I was confident we could execute code on DeepSpeed’s self-hosted runners, but that didn’t stop nerves from setting in as I prepared for my first attempt at public vulnerability research. As you’ll see shortly, CI/CD attacks can always surprise you.

Now that we had contributor status, we created a new workflow in our repository fork and configured the workflow to run on one of DeepSpeed’s self-hosted runners (an example workflow is shown further down).

Given that we didn’t need to persist on the runner, we opted not to use our “Runner-on-Runner” C2 payload and instead get a more traditional reverse shell. If you’re unfamiliar with Runner-on-Runner, Adnan explains it well during his walkthrough of a [critical GitHub vulnerability he found](https://adnanthekhan.com/2023/12/20/one-supply-chain-attack-to-rule-them-all/#preparing-the-payload). 

What we didn’t know is that the self-hosted runner we were targeting was a **REDMON domain-joined machine** (REDMON is Microsoft’s largest domain, created in 1999), and because of that, it had full EDR and firewall restrictions. Unsurprisingly, it did not play nice when we tried to manipulate SSH keys.

![](https://johnstawinski.com/wp-content/uploads/2024/04/image.png?w=1024)

_During this attempt, we learned the employee couldn’t modify their own `authorized_keys` file._

_Note: Installing C2 or getting reverse shells may be considered out-of-scope for bug bounty programs and could be treated as unnecessary malicious activity by the organization. During these operations, we felt our actions were justified due to the fact that post-exploitation was critical to determining impact. Bug bounty programs we have submitted to agree with this sentiment._

In hindsight, we should have installed RoR right away, as it would have saved a lot of time battling file system and egress restrictions. After several failed attempts to get shell access, we decided to run a simple `ls` command on the user’s home directory so we could learn more about the system. We pushed a workflow that looked like this:
  
  
  name: nv-h100
  
  on:
  
   pull_request
  
  jobs:
  
   unit-tests:
  
     runs-on: [self-hosted, nvidia, h100]
  
     steps:
  
       - uses: actions/checkout@v3
  
       - name: unit-tests
  
         continue-on-error: true
  
         run: |
  
           whoami
  
           pwd
  
           ls

_This workflow runs the `whoami`, `pwd`, and `ls` commands on the self-hosted runner._

The output revealed the self-hosted runner was actually the server of a Microsoft employee and was joined to the REDMOND domain.

![](https://lh7-us.googleusercontent.com/6C4e0rox5P-IZ4MiOSFLY5Mg_7HtjBiwHbjgljRWDzwKWiowV2HWKcR_A2Q29X0Olxpz2C3tfBHJoGCqtFRanFEI2kJH_SAG5kcv-Ug-FzomXu4jRl3dtreTy7MBA1C_DA2D9pgPB1d7g3SQqruAkR0)

_We’ve blurred the employee’s name to preserve their anonymity. Regardless of who was responsible, Microsoft should have technical controls and review requirements in place that prevent these mistakes._

Upon seeing that command output, the operation shifted from a curious foray into CI/CD security to “**Holy Sh** we just breached Microsoft** ”.

A heavy feeling followed the initial shock of this discovery. If we were able to discover and exploit this vulnerability during my first-ever bug bounty attack, surely nation-states could as well.

At this point, we stopped the operation and wrote our report. We never expected Microsoft would use a domain-joined machine as a self-hosted runner – most likely, there were secrets to be discovered on the machine, but given the significance of this vulnerability, we wanted to submit our report as soon as possible.

# How bad could it have been?

An advanced threat actor discovering this vulnerability in the wild would start by installing Command-and-Control (C2) on the machine. If they were sophisticated, this C2 would evade detection. **Then they would look for lateral movement within the domain.**

Personally, I don’t know the state of Microsoft’s Active Directory security posture. Considering that Microsoft invented Active Directory, you’d hope they know how to lock it down, but we’ve seen [firsthand examples of organizations not using their own software securely](http://adnanthekhan.com/2023/12/20/one-supply-chain-attack-to-rule-them-all/). 

Regardless of their Active Directory hygiene, the compromised runner was running in the context of a user who was a **Senior Developer working at Microsoft**. This means that anyone who compromised the runner would have that user’s privileges in the REDMOND domain. Again, I can’t comment on Microsoft’s posture, but let’s just say that an Active Directory foothold as a Senior Developer is very, very attractive to an attacker. 

In the worst-case scenario, they could escalate their privileges to the domain administrator and compromise every server, database, and application in the domain. In the best-case scenario, Microsoft’s IR team would have detected their activities quickly and evicted them from the network. All we can do is hope we found this vulnerability before the bad guys.

# Lessons Learned

This attack prompted us to be more thorough in future operations, developing stable RoR C2 that works across several architectures. We also started making exhaustive game plans prior to launching any attack.

Personally, this attack prompted me to embrace how serious these vulnerabilities could be. Hacking can feel fun, like an exciting game or a challenge, and it’s easy to lose track of the impact you can have on individuals and corporations. This attack brought home the fact that these things matter.

#### I remember wondering if our future attacks would reach this level of impact. 

# Who Else is Vulnerable?

Since hacking Microsoft, we’ve leveraged similar attack paths to [discover critical supply chain vulnerabilities in PyTorch, TensorFlow, GitHub, Crypto wallets, Web3 blockchains, and more](https://johnstawinski.com/2024/01/05/worse-than-solarwinds-three-steps-to-hack-blockchains-github-and-ml-through-github-actions/), earning hundreds of thousands of dollars in bug bounties along the way. In part due to the lessons learned during DeepSpeed, these future attacks were more sophisticated, orchestrated, and smooth. Several of these exploits could have led to a supply chain attack similar to SolarWinds or the recent XZ compromise had they been discovered by a malicious attacker. 

As we’ve slowly released our research, we’ve seen many organizations take steps to secure their self-hosted CI/CD security. Outlets like [SecurityWeek](https://www.securityweek.com/major-it-crypto-firms-exposed-to-supply-chain-compromise-via-new-class-of-ci-cd-attack/), [The Hacker News](https://thehackernews.com/2024/01/tensorflow-cicd-flaw-exposed-supply.html), [YCombinator HN](https://news.ycombinator.com/item?id=38969533), [CSOOnline](https://www.csoonline.com/article/1290656/researchers-demo-new-ci-cd-attack-techniques-in-pytorch-supply-chain-attack.html), and others have covered our research and helped spread the word. However, this vulnerability class is far from closed, as we see new repositories weekly that are susceptible to self-hosted runner takeover.

This attack set the stage for Adnan and I’s collaboration, propelling us to push the limits of CI/CD security in future operations. Hopefully, we’ll be able to dive into the full breadth of our research at a certain hacking conference that takes place every August. 

# Remediation

Microsoft took very quick action to remediate the issue. At the time, Microsoft had a **lot** more repositories with self-hosted runners that were likely vulnerable to similar attacks.

After we submitted our report, they remediated the issue in less than three days by enforcing workflow approval requirements to the entire Microsoft organization, removing the domain-joined self-hosted runner, and switching to mostly ephemeral runners. 

# A Whopping Zero Dollars

Microsoft Security Response Center (MSRC) does not have the best reputation in vulnerability research. I was hopeful they would reward us due to the critical nature of the vulnerability, but they stayed true to their reputation.

Three months after receiving our report, they determined our submission was “not eligible for a bounty”. Microsoft has **very** specific categories for determining what products and services are eligible for rewards, and DeepSpeed was not one of them (even though the vulnerability impacted their Active Directory environment). 

Yes, DeepSpeed didn’t fall under an explicit category that was eligible for a bounty, but more reputable programs will typically grant rewards in scenarios where a critical vulnerability like this is discovered. By refusing to bend their categorization, MSRC is telling bounty hunters everywhere that they won’t be rewarded for disclosing these types of vulnerabilities. That’s not a message an organization like Microsoft should send, given how prominent of a target they are for real attackers.

Just look at the [CISA report](https://www.cisa.gov/sites/default/files/2024-04/CSRB_Review_of_the_Summer_2023_MEO_Intrusion_Final_508c.pdf) of the Microsoft Exchange hack that occurred in the summer of 2023, which allowed the nation-state group Storm-0558 to access the email accounts “of 22 enterprise organizations, including government agencies and three think tanks.” Microsoft has been targeted by nation-states before, and probably will be again. They need to do everything in their power to secure their perimeter, including encouraging good-faith vulnerability research.

At the very least, breaching Microsoft should not be this easy. Typically, significant CI/CD knowledge around GitHub Actions is required to execute these attacks. 

#### But with DeepSpeed,**** the only thing standing between the public internet and Microsoft’s internal network was a single typo and some shell commands.

_Want to hear more? Subscribe to the[official John IV newsletter](https://johnstawinski.ck.page/2034b623ad)_  _to receive live, monthly updates of my interests and passions._

### Share this:

  * [ Share on X (Opens in new window) X ](https://johnstawinski.com/2024/04/15/fixing-typos-and-breaching-microsofts-perimeter/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://johnstawinski.com/2024/04/15/fixing-typos-and-breaching-microsofts-perimeter/?share=facebook)
  * 

Like Loading…

Categories:

[Uncategorized](https://johnstawinski.com/category/uncategorized/)

· Tagged:

[azure](https://johnstawinski.com/tag/azure/), [cybersecurity](https://johnstawinski.com/tag/cybersecurity/), [devops](https://johnstawinski.com/tag/devops/), [github](https://johnstawinski.com/tag/github/), [security](https://johnstawinski.com/tag/security/)

* * *

[Previous Post](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/)

* * *

[Next Post](https://johnstawinski.com/2024/07/30/black-hat-and-def-con-preview-grand-theft-actions-or-continuous-integration-continuous-destruction/)

## 2 responses to “Fixing Typos and Breaching Microsoft’s Perimeter ”

  1. [Worse than SolarWinds: Three Steps to Hack Blockchains, GitHub, and ML through GitHub Actions – John Stawinski IV](https://johnstawinski.com/2024/01/05/worse-than-solarwinds-three-steps-to-hack-blockchains-github-and-ml-through-github-actions/)

[July 20, 2024](https://johnstawinski.com/2024/04/15/fixing-typos-and-breaching-microsofts-perimeter/comment-page-1/#comment-522)

[…] Gaining remote code execution on a domain-joined Microsoft machine by exploiting Microsoft Deepspeed (update – walkthrough now available in Fixing Typos and Breaching Microsoft’s Perimeter ) […]

[Like](https://johnstawinski.com/2024/04/15/fixing-typos-and-breaching-microsofts-perimeter/?like_comment=522&_wpnonce=b62e0eeeb2)Like

[Reply](https://johnstawinski.com/2024/04/15/fixing-typos-and-breaching-microsofts-perimeter/comment-page-1/?replytocom=522#respond)

  2. [Black Hat and DEF CON Preview: “Grand Theft Actions” or “Continuous Integration, Continuous Destruction”? – John Stawinski IV](https://johnstawinski.com/2024/07/30/black-hat-and-def-con-preview-grand-theft-actions-or-continuous-integration-continuous-destruction/)

[July 30, 2024](https://johnstawinski.com/2024/04/15/fixing-typos-and-breaching-microsofts-perimeter/comment-page-1/#comment-526)

[…] Fixing Typos and Breaching Microsoft’s Perimeter […]

[Like](https://johnstawinski.com/2024/04/15/fixing-typos-and-breaching-microsofts-perimeter/?like_comment=526&_wpnonce=97801b6527)Like

[Reply](https://johnstawinski.com/2024/04/15/fixing-typos-and-breaching-microsofts-perimeter/comment-page-1/?replytocom=526#respond)

### Leave a comment [Cancel reply](/2024/04/15/fixing-typos-and-breaching-microsofts-perimeter/#respond)

Δ
