---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-15_the-effectiveness-of-employing-bchecks-to-uncover-significant-secrets.md
original_filename: 2024-02-15_the-effectiveness-of-employing-bchecks-to-uncover-significant-secrets.md
title: The effectiveness of employing BChecks to uncover significant secrets
category: documents
detected_topics:
- supply-chain
- sso
- access-control
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- supply-chain
- sso
- access-control
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: b6997c10f29453fb74da34275e064e5e8bb7519218ecbc0e768d6547438e35c1
text_sha256: 6f455d6ca872ffe8562a02dacc2df6b718422be01228af6edadde93d37ec22eb
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: false
---

# The effectiveness of employing BChecks to uncover significant secrets

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-15_the-effectiveness-of-employing-bchecks-to-uncover-significant-secrets.md
- Source Type: markdown
- Detected Topics: supply-chain, sso, access-control, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: False
- Raw SHA256: `b6997c10f29453fb74da34275e064e5e8bb7519218ecbc0e768d6547438e35c1`
- Text SHA256: `6f455d6ca872ffe8562a02dacc2df6b718422be01228af6edadde93d37ec22eb`


## Content

---
title: "The effectiveness of employing BChecks to uncover significant secrets"
url: "https://xelkomy.medium.com/the-effectiveness-of-employing-bchecks-to-uncover-significant-secrets-788e15a8a952"
authors: ["Khaled Mohamed (@0xElkomy)"]
bugs: ["Hardcoded credentials"]
publication_date: "2024-02-15"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 429
scraped_via: "browseros"
---

# The effectiveness of employing BChecks to uncover significant secrets

The effectiveness of employing BChecks to uncover significant secrets
Khaled Mohamed
Follow
4 min read
·
Feb 16, 2024

14

Opening

During my recent penetration testing engagement for a company, a critical bug surfaced that posed a significant threat to the entire website. This discovery led to the exposure of the developers’ secrets, revealing a GitHub token, an npm token, and even more sensitive information, including a private SSH key. Strangely, all these credentials were laid bare within a single JavaScript file.

Press enter or click to view image in full size
Let’s do it
Scenario

The context of this article suggests that the method I employed to uncover this issue is accessible to anyone. I utilized tools such as Burp Suite, along with the Burp BCheck templates during the discovery process, the monster of this blog is the BCheks it was a great to use by built custom bchecks to find for us the secrets into the JS files and the whole site with passive scan while you test the target you are working on and using the burp proxy and make a passive scan enabled at the burp dashboard like:

The Default Tasks when you open the burp suite

The custom BChecks we employed are now public, making them accessible to anyone with a Burp Suite Pro license. Users can easily download and import these BCheck templates into their Burp Suite, allowing seamless utilization. Simply visit the following links:

Information Disclosure Secret Finder — certain: Certain-leaks-checker.bcheck
Information Disclosure Secret Finder — tentative: Tentative-leaks-checker.bcheck

These BCheck templates proved effective in uncovering numerous secrets, including the GitHub secret key and NPM token for the company.

Press enter or click to view image in full size
The Finding I have got by the templates into the burp suite
The Exploitation Phase:

GitHub:
Upon discovering these keys, I pondered how I could maximize their impact. Armed with the acquired secrets, I created a GitHub repository named KeyHacks. Scouring the page for the term “github,” I stumbled upon a Proof of Concept (PoC) command that allowed me to ascertain the permissions associated with the GitHub secret key:

Press enter or click to view image in full size
GitHub Validation Command

Executing the aforementioned command empowered me to perform various actions on the target, including downloading deployment information, halting the running server, and accessing private GitHub repositories, but as penetration testers on black box engagement, we can’t do it.

Get Khaled Mohamed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

NPM:
Furthermore, upon validating the exposed npm token, insights into potential exploitations surfaced. The validated token revealed a project published on npmjs. Reflecting on a trend from two years ago involving confused dependencies, where attackers added a backdoor to a package and published it, we contemplated a similar scenario. The idea was to update the package with our backdoor. However, it’s crucial to emphasize that, as penetration testers, we refrain from such actions without the explicit permission of the victim, especially when dealing with secrets present in a production site rather than a testing environment.

Press enter or click to view image in full size
NPM Validation Command for the token

The examples above served solely as proof of concept for the identified findings. However, it’s crucial to emphasize that actual exploitation cannot be pursued without explicit permission from the target. As a responsible penetration tester, it is imperative to seek authorization from the client before proceeding with any actions. While the excitement of exploiting vulnerabilities may be tempting, unauthorized actions could lead to severe consequences, including termination from your company and irreparable damage to its reputation. Always prioritize ethical and responsible conduct in the realm of penetration testing.

Those finding was while engagement with a client on my work with 
BugSwagger LLC
.

Please don't hesitate to reach out to me anytime on X, also known as Twitter.

I trust that this write-up proves helpful to you in any way.

Don’t Miss Our Company Cyber AR:
CyberAR | Penetration testing | Cyber Security
