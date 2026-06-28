---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-15_we-discovered-major-vulnerabilities-in-control-web-panel-heres-how-we-found-them.md
original_filename: 2022-08-15_we-discovered-major-vulnerabilities-in-control-web-panel-heres-how-we-found-them.md
title: We discovered major vulnerabilities in Control Web Panel. Here’s how we found
  them.
category: documents
detected_topics:
- command-injection
- path-traversal
- password-reset
- xss
- otp
- automation-abuse
tags:
- imported
- documents
- command-injection
- path-traversal
- password-reset
- xss
- otp
- automation-abuse
language: en
raw_sha256: 2b756d7b48660c9e5dff0b95b1596ca7b020683b9eb13d9e1b6229535cd85d91
text_sha256: b0df0c357b07625b326c37019d2153512d95b36261e63a427044790522eeae1c
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# We discovered major vulnerabilities in Control Web Panel. Here’s how we found them.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-15_we-discovered-major-vulnerabilities-in-control-web-panel-heres-how-we-found-them.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, password-reset, xss, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `2b756d7b48660c9e5dff0b95b1596ca7b020683b9eb13d9e1b6229535cd85d91`
- Text SHA256: `b0df0c357b07625b326c37019d2153512d95b36261e63a427044790522eeae1c`


## Content

---
title: "We discovered major vulnerabilities in Control Web Panel. Here’s how we found them."
url: "https://www.immersivelabs.com/blog/we-discovered-major-vulnerabilities-in-control-web-panel-heres-how-we-found-them/"
final_url: "https://www.immersivelabs.com/resources/c7-blog/we-discovered-major-vulnerabilities-in-control-web-panel-heres-how-we-found-them"
authors: ["Immersive Labs (@immersivelabs)"]
programs: ["Centos Web Panel (CWP)"]
bugs: ["Path traversal", "RCE", "Weak crypto", "Password reset", "Account takeover"]
publication_date: "2022-08-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2305
---

[All Blogs](/container7)

[Responsible Disclosures](/c7/responsible-disclosures)

August 15, 2022

# We discovered major vulnerabilities in Control Web Panel. Here’s how we found them.

Request A Demo

CVE's

Ultimate Windows Security

![Person typing on a laptop and calculator with digital business analytics and charts overlay.](https://cdn.prod.website-files.com/678a13476d0a697e355dec29/679e35321b8a79e83942e484_66fd19525782517ab997c582_66be1e419868b697610076d8_stock-laptop-typing-charts.webp)

Contributors

[![Blue geometric shape resembling a stylized tilted square with rounded edges on a black background.](https://cdn.prod.website-files.com/678a13476d0a697e355dec29/679a01ba01a698790b22ce7f_Immersive%20Author%20Photo.avif)](/author/immersive)[![](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/679d09ee1fbc8d8d39c51b3f_679a01ba01a698790b22ce7f_Immersive%20Author%20Photo.webp)](/author/immersive)

[Immersive](/author/immersive)[](https://www.linkedin.com/company/immersive-labs-limited/)

Content Team

Immersive

Share 

[ ](https://www.linkedin.com/shareArticle?mini=true&url=https://www.immersivelabs.com//resources/c7-blog/we-discovered-major-vulnerabilities-in-control-web-panel-heres-how-we-found-them)

[ ](https://twitter.com/intent/tweet?text=https://www.immersivelabs.com//resources/c7-blog/we-discovered-major-vulnerabilities-in-control-web-panel-heres-how-we-found-them)

[ ](https://www.facebook.com/sharer/sharer.php?u=https://www.immersivelabs.com//resources/c7-blog/we-discovered-major-vulnerabilities-in-control-web-panel-heres-how-we-found-them)

## Overview

Earlier this year, researchers at Immersive Labs responsibly disclosed several vulnerabilities in Centos Web Panel, which was recently rebranded as Control Web Panel (CWP).The vulnerabilities we found allowed malicious actors to take over accounts and run commands as root on vulnerable servers. There were hundreds of thousands of them online – millions of websites could have been affected.Fully patched and totally safe now, MITRE assigned the following CVEs for the vulnerabilities we reported:

  * CVE-2022-25046: Path traversal vulnerability leading to remote code execution (RCE)
  * CVE-2022-25047: Account hijack via the password reset token
  * CVE-2022-25048: As a standard user execute commands in the context of root

### What is CWP?

CWP is a shared hosting platform built to run on CentOS servers. It’s shared hosting services mean that even a single web server running CWP can host many websites.The server operator creates standard user accounts for each new customer – effectively giving them their own slice of the resources on the shared server.As with most things, there are pros and cons to this sort of setup. The positive aspect is the financial benefit; monthly running costs for both the operator and the customer are low because a single server is capable of running thousands of websites.The downsides are that if the single host goes down, so too does every website it hosts. Even more concerning however, is that if the main host gets compromised, so will every account that’s provisioned on the server.

### Impact

Shodan shows there are approximately 185,000 active CWP servers on the internet. Each one likely runs between 10 and 100 websites, meaning any vulnerability on the underlying server software could impact millions of individual websites.

![](https://cdn.prod.website-files.com/678a13476d0a697e355dec29/693fe0c948d11b64d3555849_679e35311b8a79e83942e458_66fd19525782517ab997c40f_66be1e429868b697610076ec_impact.avif)

CWP caters to personal and small business accounts rather than large enterprises. But a wide “watering hole” attack would still have a fairly large potential threat surface.Attackers exploiting these vulnerabilities at scale could infect millions of websites with credential harvesting malware or target payment portals to intercept or modify banking details.

### Mitigation

At the time of writing, all the reported vulnerabilities have been patched by the team at CWP.In its default configuration, CWP is able to automatically apply updates at regular frequencies, meaning that all CWP instances should be fully patched unless updates have been forcibly disabled.To check your installed version, SSH onto the target server and run the following command:`cat / path to version.php`

### How we found them

The next few paragraphs will go into a bit more technical detail about how we found the vulnerabilities, as well as how they work.

#### CVE-2022-25046: _Path traversal vulnerability leading to remote code execution_

Back in January, [Octagon published a blog post](https://octagon.net/blog/2022/01/22/cve-2021-45467-cwp-centos-web-panel-preauth-rce/) discussing a CVE that chained two old vulnerabilities together to achieve pre-authenticated RCE. When we took a closer look at the way the vulnerabilities worked, we realized they only affected an older version of the application. In fact, most of the functions mentioned no longer existed.So we looked deeper at the mitigations on the Octagon post. We spotted that the code on the latest version had been further modified, with the addition of `htmlspecialchars` and `strip_tags`. These functions are designed to stop XSS attacks by filtering and removing HTML tags that are frequently used for them.However, the unintended side effect of this extra security means that we now have a new (and trivial) method to bypass the directory traversal filtering.

![](https://cdn.prod.website-files.com/678a13476d0a697e355dec29/693fe0c948d11b64d355584c_679e35311b8a79e83942e455_66fd19525782517ab997c40c_66be1e429868b697610076f0_getsecurity.avif)

In this function, the first check is for a string comparison that looks for `..`, and checks to see if the null byte trick is being used – as reported by Octagon.From here, the function removes any whitespace from the ends, replaces any null bytes, then filters an HTML.Then comes the issue. If you send a string like `variable=../`, the first check is fine as `..` isn’t present. But after the final strip tags, you’re left with `variable=../../`.With a way to bypass the checks, you can now perform a standard directory traversal attack.We searched for existing functions that could be used to run OS commands, and actually found a command injection vulnerability that we chained together with the filter bypass to gain code execution.PoC scripts can be found on the [Immersive Labs GitHub](https://github.com/Immersive-Labs-Sec/CentOS-WebPanel), and you can see the full exploit at work in the video clip below.

![](https://cdn.prod.website-files.com/678a13476d0a697e355dec29/693fe0c948d11b64d3555852_679e35311b8a79e83942e45b_66fd19515782517ab997c406_66be1e429868b6976100770e_y65Qn6vBACb2bZUsBsaChv.avif)

#### CVE-2022-25047: _Account hijack via the password reset token_

When reviewing the authentication flows used by CWP, we noticed that the password reset token generation didn’t include any elements that were secret or random. In fact, every element of the password reset token could be calculated if you had the email address and username of any given user, which is just as unfortunate as it sounds.To exploit this vulnerability, all an attacker needs to do is trigger a valid password reset for a known account and intercept the response. The server response will contain the date and time that that password reset was requested. The date returned by the server will match within a few milliseconds the date that was used to generate the reset token.This reset token can now be used to set a new password for the account without needing access to the target's email account.[Check out our PoC script here](https://github.com/Immersive-Labs-Sec/CentOS-WebPanel) and watch the video below to see this in action.

![Terminal showing Python script help for hijacking Centos web panel user accounts with password reset command.](https://cdn.prod.website-files.com/678a13476d0a697e355dec29/693fe0c948d11b64d355584f_679e35311b8a79e83942e45e_66fd19525782517ab997c412_66be1e429868b69761007711_Z68m9zWYLP81X3K5hGwSRW.avif)

It’s worth noting that this attack won’t work for the root account, instead generating and sending a password reset email to the user account. Although, as with most password resets, it does say you can ignore this email if you didn’t initiate the reset.

#### CVE-2022-25048: _As a standard user execute commands in the context of root_

Because CWP is a shared hosting platform, there are many site administrators that are given access to manage their part of the server. They should only be able to interact with the files and configuration of their domains and not anyone else’s.During our research, we were able to identify several instances of command injection vulnerabilities that would allow any standard user account to run commands as root and therefore gain access to the full system.In each example the cause is the same: input data from the user is used to create a shell command that’s then executed in the context of the root account.

### Disclosure

We reported the vulnerabilities to the CWP team as soon as we confirmed our findings were valid. The developers were quick to respond and worked with us to patch and test all the fixes that were released.CWP has an aggressive automatic update process that includes forced expiry of instances that aren’t kept up to date. The forced expiry date for all vulnerable versions has now passed, which is why we chose to publish these details in full now, and not sooner.CWP offered us a bounty for disclosing the vulnerabilities responsibly. Instead, we asked it to make a donation to Save the Children in support of Ukraine – and it did.

### Immersive Labs

If you’re an Immersive Labs customer, we’ve released a series of labs that take a closer look at these vulnerabilities from the perspective of offensive and defensive teams as well as application security, looking at how to identify and patch these types of vulnerabilities.If you want to learn more about Immersive Labs, [book a demo here. ](https://www.immersivelabs.com/demo/)

![](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/67ea6e4dc7d9e7940a86668e_a856caea8f872a304f4893861f684706_HSBC.svg)

![](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/67ea6e4dbfe2611885cc5300_34e740291918ffa8c942c66c7cd9f423_GoldmanSachs.svg)

![](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/67ea6e4d6dc61041edb8eeb4_bd2af39a845b5517a7cd02523c12c212_NationaGrid.svg)

![](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/69d8fe0bff9362a993632cdc_Daimler_Truck_Logo%201%20\(1\).svg)

![](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/67ea6e4dc778551f18383852_5e31e30ad7f50d874358a99a85dab399_Citi.svg)

![](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/67ea6e4dc7d9e7940a86668e_a856caea8f872a304f4893861f684706_HSBC.svg)

![](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/67ea6e4dbfe2611885cc5300_34e740291918ffa8c942c66c7cd9f423_GoldmanSachs.svg)

![](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/67ea6e4d6dc61041edb8eeb4_bd2af39a845b5517a7cd02523c12c212_NationaGrid.svg)

![](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/69d8fe0bff9362a993632cdc_Daimler_Truck_Logo%201%20\(1\).svg)

![](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/67ea6e4dc778551f18383852_5e31e30ad7f50d874358a99a85dab399_Citi.svg)

![](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/67ea6e4dc7d9e7940a86668e_a856caea8f872a304f4893861f684706_HSBC.svg)

![](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/67ea6e4dbfe2611885cc5300_34e740291918ffa8c942c66c7cd9f423_GoldmanSachs.svg)

![](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/67ea6e4d6dc61041edb8eeb4_bd2af39a845b5517a7cd02523c12c212_NationaGrid.svg)

![](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/69d8fe0bff9362a993632cdc_Daimler_Truck_Logo%201%20\(1\).svg)

![](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/67ea6e4dc778551f18383852_5e31e30ad7f50d874358a99a85dab399_Citi.svg)

customer insights

![HSBC logo with red hexagon and white triangles with text HSBC in black.](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/68cd2d07a3bef530ce2bce68_hsbc-logo-testimonials.webp)

"The speed at which Immersive produces technical content is hugely impressive, and this turnaround has helped get our teams ahead of the curve, giving them hands-on experience with serious vulnerabilities, in a secure environment, as soon as they emerge."

![](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/6735fba9a631272fb45132b3_placeholder-image.svg)

TJ Campana

Head of Global Cybersecurity Operations, HSBC

![Kroll company logo with a green arc above the letter R on a white background.](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/68cd2d07bce12671fa38ad42_kroll-logo-testimonials.webp)

"Realistic simulation of current threats is the only way to test and improve response readiness, and to ensure that the impact of a real attack is minimized. Immersive’s innovative platform, combined with Kroll’s extensive experience, provides the closest thing to replication of a real incident — all within a safe virtual environment."

![](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/6735fba9a631272fb45132b3_placeholder-image.svg)

Paul Jackson

Regional Managing Director, APAC Cyber Risk, Kroll

![Specsavers logo with white text on a green dual-oval background.](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/68cd2d07e44bb7ea48cbb9bf_specsavers-logo-testimonials.webp)

"Exploring cybersecurity can feel like a huge challenge with so many skills to master, but Immersive has made the journey so much easier for me over the past five years. This practical, interactive approach hasn’t just improved my technical abilities—it’s given me a real sense of confidence. I truly recommend Immersive!"

![](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/6735fba9a631272fb45132b3_placeholder-image.svg)

Paul Blance

Specsavers

![Mercedes-Benz brand logo.](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/68cd2d07bc8ceb9b5b1e16b7_merc-logo-testimonials.webp)

"I recently got the chance to try out Immersive, and it was an enlightening experience! The gamified learning made absorbing new information quite enjoyable. The community is welcoming, adding to the overall positive atmosphere. It would be fantastic to see more active users, which could enhance collaboration and discussions. Overall, a solid platform!"

![](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/6735fba9a631272fb45132b3_placeholder-image.svg)

Atakan Bal

Mercedes Benz

## Ready to Get Started?  
Get a Live Demo.

Simply complete the form to schedule time with an expert that works best for your calendar.

Subscribe for the latest news, thought leadership and product updates

By subscribing you agree to with our [Privacy Notice.](https://www.immersivelabs.com/legal-documents/end-user-privacy-notice)

[![](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/6759b61c2c4a5793d96bfb2d_WhiteOutLogo.svg)](/)

Platform

[Immersive One](/products/platform)[Prove Resilience](/platform/prove)[Improving Readiness](/platform/improve)[Reporting Readiness](/platform/report)[Programs](/platform/programs)

Capabilities

[Hands-On Labs](/products/labs)[Application Security](/products/application-security-training)[Crisis Simulation](/products/crisis-sim)[Cyber Range Exercise](/products/cyber-range-exercising)[Cyber Drills](/products/cyber-drills)[Cyber Ranges](/products/cyber-range-training)[Workforce Exercises](/products/workforce-exercising)[Dynamic Threat Range](/lp/dynamic-threat-range)

Solutions

[Operational Technology](/solutions/operational-technology)[Secure Your SDLC](/solutions/secure-sdlc-training)[Financial Services](/solutions/financial-services)[Red Team Training](/products/red-team-training)[Blue Team Training](/products/blue-team-training)[AI Hands-On Labs](/ai/ai-hands-on-labs)[For All Employees](/solutions/for-employees)[For Developers](/products/application-security-training)[Compliance](/compliance)[Upskilling Teams](/products/upskilling-teams)[AI Hub](/ai)[Tech Partners & Integrations](/tech-partners)

Resources

[Blogs](/resources/blog)[What’s New](/resources/whats-new)[Container 7](/container7)[Webinars](/resources/webinars)[eBooks & Reports](/resources/ebooks)[The Resilience Room](/resources/the-resilience-room)[Battle Threat Cards](/container7/threat-card-hub)[Partnerships](/partners)[Glossary ](/cybersecurity-glossary)[Cybersecurity Essentials](/resources/cybersecurity-essentials)[Community ](https://community.immersivelabs.com/)[All Resources](/resources)

Company

[Our Story](/company/our-story)[Leadership & Investors](/company/leadership)[Careers](/company/careers)[Awards & Accolades](/company/awards-and-accolades)[Cyber Million](/resources/cybermillion)[Legal](/legal)[Security & Privacy](/company/legal/security-and-privacy)[Accessibility Statement](/company/legal/accessibility-statement)[Modern Slavery Statement](https://info.immersivelabs.com/hubfs/Website%20Documents/Legal%20Documents/Immersive%20Modern%20Slavery%20Statement%20-%20November%202025.pdf)[Covenant](/covenant)[Contact Us](/company/contact)[Request a Demo](/company/contact)

[](https://www.facebook.com/immersivelabsuk/?locale=en_GB)[](https://x.com/immersivelabs)[](https://www.linkedin.com/company/immersive-labs-limited/?originalSubdomain=uk)[](https://www.youtube.com/channel/UCBHsoN0R2YtWYptg2fvrT2w)

© 2026 Immersive. All rights reserved.

![](https://cdn.prod.website-files.com/6735fba9a631272fb4513263/69a84b3fd21f6d4531b8b837_Immersive%20Logo%20-%20crop.svg)
