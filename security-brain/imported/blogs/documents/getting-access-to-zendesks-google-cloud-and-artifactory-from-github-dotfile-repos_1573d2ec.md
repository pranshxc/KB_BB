---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-23_getting-access-to-zendesks-google-cloud-and-artifactory-from-github-dotfile-repo.md
original_filename: 2019-04-23_getting-access-to-zendesks-google-cloud-and-artifactory-from-github-dotfile-repo.md
title: Getting access to Zendesk’s Google Cloud and Artifactory from GitHub dotfile
  repos
category: documents
detected_topics:
- command-injection
- otp
- automation-abuse
- information-disclosure
- cloud-security
- supply-chain
tags:
- imported
- documents
- command-injection
- otp
- automation-abuse
- information-disclosure
- cloud-security
- supply-chain
language: en
raw_sha256: 1573d2ecdb6a6a86a410f0d8e1700e50abb924e6c7b280e7e7ed38789b997223
text_sha256: 1f3204278e324dbae1bdedd488f93f1f925c56447fac079575b440d6a78ee054
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: true
---

# Getting access to Zendesk’s Google Cloud and Artifactory from GitHub dotfile repos

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-23_getting-access-to-zendesks-google-cloud-and-artifactory-from-github-dotfile-repo.md
- Source Type: markdown
- Detected Topics: command-injection, otp, automation-abuse, information-disclosure, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: True
- Raw SHA256: `1573d2ecdb6a6a86a410f0d8e1700e50abb924e6c7b280e7e7ed38789b997223`
- Text SHA256: `1f3204278e324dbae1bdedd488f93f1f925c56447fac079575b440d6a78ee054`


## Content

---
title: "Getting access to Zendesk’s Google Cloud and Artifactory from GitHub dotfile repos"
url: "https://blog.assetnote.io/bug-bounty/2019/04/23/getting-access-zendesk-gcp/"
final_url: "https://www.assetnote.io/resources/research/getting-access-to-zendesks-google-cloud-and-artifactory-from-github-dotfile-repos"
authors: ["Ruby Nealon (@_ruby)"]
programs: ["Zendesk"]
bugs: ["Information disclosure"]
bounty: "3,000"
publication_date: "2019-04-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5292
---

[Research Notes](/resources/research)

Security Research

April 22, 2019

# Getting access to Zendesk’s Google Cloud and Artifactory from GitHub dotfile repos

No items found.

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/653795bb35bc995a6f921d3f_citrixbleed.svg)

Creative Commons license

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a3a26e1e476a7b1dc65cc9_tppefinal.png)

  

At Assetnote, we’re a small team and all of us come from an InfoSec background and part of our product development is our team actively monitoring trends in the causation of organizational exposures and breaches. One common pattern we’ve identified is employees and contractors of organizations accidentally leaking their sensitive data such as credentials, source code and even raw customer PII on third-party platform sites like GitHub, PasteBin and Trello.

In this article we’re going to talk specifically about exposures on GitHub - these are typically made by employees/contractors of a technical discipline and are more likely to contain credentials with access to infrastructure. Git can be tricky to get right, and while a lot of the cases we’ve disclosed via vulnerability disclosure programs are due to credentials being left in a historical commit (some even labelled “Remove credentials”), in some cases credentials are even left in the HEAD of the master branch.

Today we’re announcing our Third-Party Platform Exposure module, which will be available for the Assetnote continuous security (CS) platform later this year, and disclosing some of the most critical findings we’ve found benchmarking against public bug bounty targets.

### Zendesk’s Google Cloud and Artifactory

On February 15th, after launching for a beta test, our TPPE monitor detected two public repositories containing Zendesk employee dotfiles, a repository typically used by a developer for easy portability of their CLI and SDK settings.

Looking at the first repository, our TPPE monitor reported to us that two common formats of credentials were present in the repository, an artifactory token for a repository hosted with JFrog and a GCloud “legacy-credentials” folder.

Upon inspection by our team, we determined that these credentials were valid. We were able to confirm the Artifactory token by making a request to the hostname in the environment variables with the username and token listed:
  
  
  export ARTIFACTORY_KEY="<REDACTED>”;  # For HTTP repository access
  export ARTIFACTORY_USERNAME="<REDACTED>";
  curl u $ARTIFACTORY_USERNAME:$ARTIFACTORY_KEY https://<REDACTED>/artifactory/api/build
  Response:
  {
  "uri": "http://<REDACTED>/artifactory/api/build"
  ...
  
  

[view raw](https://gist.github.com/rubyroobs/6c3c8e21cc122f66bcb0e4317136a4b6/raw/12192f33fbe5c17abaf8f2cd7ffa548c6aad0466/zendesk_artifactory_1.sh)[zendesk_artifactory_1.sh ](https://gist.github.com/rubyroobs/6c3c8e21cc122f66bcb0e4317136a4b6#file-zendesk_artifactory_1-sh)hosted with ❤ by [GitHub](https://github.com/)

We also validated the Google Cloud credentials. It’s not particularly straightforward to make an authenticated request to the Google Cloud API by cURL with the legacy credentials format, but we found by simply using the gcloud configuration folder in the repository in our local shell, it meant we could use the gcloud CLI as if we were the user.
  
  
  ruby@nippon:~|⇒  cp <REDACTED>/.config/gcoud ~/.config/gcloud
  ruby@nippon:~|⇒  gcloud projects list
  PROJECT_ID  NAME  PROJECT_NUMBER
  ...
  <REDACTED>  Bime development  <REDACTED>
  <REDACTED>  Bime preproduction  <REDACTED>
  <REDACTED>  Bime production  <REDACTED>
  …
  <REDACTED>  Zendesk Authentication  <REDACTED>
  …
  <REDACTED>  Voice Production  <REDACTED>
  …
  <REDACTED>  Zendesk Billing  <REDACTED>
  ...
  
  

[view raw](https://gist.github.com/rubyroobs/040a4d3f7361eb4f92c35f69ce3a1dda/raw/b61b44cdca372a4c59ea99b7b491334f118a6b3b/zendesk_gcloud_1.sh)[zendesk_gcloud_1.sh ](https://gist.github.com/rubyroobs/040a4d3f7361eb4f92c35f69ce3a1dda#file-zendesk_gcloud_1-sh)hosted with ❤ by [GitHub](https://github.com/)

These are some of the 150~ projects that the users credentials had access to. The project names have been slightly altered but are in essence what the projects were.

For those unfamiliar with Google Cloud, it makes management of SSH access really easy by removing the necessity to add all authorised users SSH keys to boxes, and instead allows you to SSH to instances using
  
  
  gcloud compute ssh <instance>
  
  

[view raw](https://gist.github.com/rubyroobs/e18b3c3946497790cdbb04f7316d5a45/raw/2222e747011ece26d5a1a1792574e72f628504ec/zendesk_gcloud_2.sh)[zendesk_gcloud_2.sh ](https://gist.github.com/rubyroobs/e18b3c3946497790cdbb04f7316d5a45#file-zendesk_gcloud_2-sh)hosted with ❤ by [GitHub](https://github.com/)

Although we did not test this upon discovery of the bug, investigation after showed this would have been possible for externally reachable instances using the command.

In the second repository, our TPPE monitor highlighted similar looking artifactory credentials with a different type of token. Using an updated proof of concept, we were able to prove that these were valid also:
  
  
  export ARTIFACTORY_USERNAME="<REDACTED>"
  export ARTIFACTORY_API_KEY=***REDACTED***
  curl -i -u $ARTIFACTORY_USERNAME:$ARTIFACTORY_API_KEY https://<REDACTED>/<REDACTED>/artifactory/api/
  
  {
  ...
  
  

[view raw](https://gist.github.com/rubyroobs/73e6cb72182bcab91812419502453e1d/raw/9dac15b29ba6ddf89a36f0308bc512980bd4dd3d/zendesk_artifactory_2.sh)[zendesk_artifactory_2.sh ](https://gist.github.com/rubyroobs/73e6cb72182bcab91812419502453e1d#file-zendesk_artifactory_2-sh)hosted with ❤ by [GitHub](https://github.com/)

Zendesk immediately revoked all tokens and had both repositories removed within around 12 hours and acknowledged after doing so. They generously paid their maximum bounty ($3000) per repository due to the critical nature of this vulnerability, and clarified they’ve taken measures to prevent similar issues in the future. For a clearer timeline, the HackerOne reports are disclosed and can be read here:

  * [#496414 - Leaked artifactory_key, artifactory_api_key, and gcloud refresh_token via GitHub](https://hackerone.com/reports/496414)
  * [#496925 - Leaked artifactory_api_key via GitHub](https://hackerone.com/reports/496925)

### Takeaways

Both of these GitHub repositories were leaked accidentally, and it’s not the first time something like this has happened. As you saw in the header, we’ve reported similar bugs before with a variety of impacts organization to organization, and bug bounty hunters are also on the hunt too (see this report where [$15,000 was paid for a GitHub Enterprise API token](https://hackerone.com/reports/396467)).

We recognise that it’s impossible to ensure issues like these never occur, and believe the best approach is continuous monitoring to identify such potential leaks as they occur. Our solution, Third-Party Platform Monitoring, will launch later this year and tackle this issue directly by using our asset discovery techniques to identify what to monitor and show exposures with a high degree of confidence using both pattern detection and human augmentation.

For bug bounty hunters, public tools like [michenriksen/gitrob](https://github.com/michenriksen/gitrob) are really cool and a great addition to your toolchain if you want to start looking for issues like these. Credentials aside, looking at what a target makes public on GitHub intentionally or not can be very valuable to your research.

For organizations, we recommend asking your employees to be careful what they make public. In our experience the majority of leaks have been in repositories that were intended to be public, but had credentials in due to a slip up, a bad .gitignore or even in a plainsight “Removing secrets” commit due to a misunderstanding of how git and GitHub work.

Written by:

Ruby Nealon

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
