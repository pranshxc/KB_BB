---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-23_microsoft-bug-reports-lead-to-ranking-on-microsoft-msrc-quarterly-leaderboard-q3.md
original_filename: 2022-12-23_microsoft-bug-reports-lead-to-ranking-on-microsoft-msrc-quarterly-leaderboard-q3.md
title: Microsoft bug reports lead to ranking on Microsoft MSRC Quarterly Leaderboard
  (Q3 2022)
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: a833f1b83c6d43ee443b7bd0a7506325a8f9ae9f2f6947263517669c9f5dce8f
text_sha256: 43e9fec53616773bb54b46ef5b51ca504587e3671ca309c58801bbc1b0743c47
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Microsoft bug reports lead to ranking on Microsoft MSRC Quarterly Leaderboard (Q3 2022)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-23_microsoft-bug-reports-lead-to-ranking-on-microsoft-msrc-quarterly-leaderboard-q3.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `a833f1b83c6d43ee443b7bd0a7506325a8f9ae9f2f6947263517669c9f5dce8f`
- Text SHA256: `43e9fec53616773bb54b46ef5b51ca504587e3671ca309c58801bbc1b0743c47`


## Content

---
title: "Microsoft bug reports lead to ranking on Microsoft MSRC Quarterly Leaderboard (Q3 2022)"
url: "https://medium.com/supakiad-s-m3ez/microsoft-bug-reports-lead-to-ranking-on-microsoft-msrc-quarterly-leaderboard-q3-2022-c6c9f70e2ccd"
authors: ["Supakiad S. (@Supakiad_Mee)"]
programs: ["Microsoft"]
bugs: ["XSS"]
publication_date: "2022-12-23"
added_date: "2023-01-02"
source: "pentester.land/writeups.json"
original_index: 1740
scraped_via: "browseros"
---

# Microsoft bug reports lead to ranking on Microsoft MSRC Quarterly Leaderboard (Q3 2022)

Supakiad S. (m3ez)
 highlighted

Microsoft bug reports lead to ranking on Microsoft MSRC Quarterly Leaderboard (Q3 2022)
Microsoft MSRC Quarterly Leaderboard from my security bug reports submitted.
Supakiad S. (m3ez)
Follow
5 min read
·
Dec 23, 2022

171

7

Press enter or click to view image in full size
Table of Contents

— Part 0 — Whoami?
— Part 1 — Selecting a program
— Part 2 — Let the hunt begin!
— Part 3 — Reporting
— Part 4 — Claims the Rewards
— Disclosure Timelines

Part 0 — Whoami?

Hello, I am Supakiad Satuwan, a Security Consultant from Thailand. In this article, I will go through the story of my first valid bug found on Microsoft bug bounty program. This has given me an opportunity to be ranked in MSRC 2022 Q3 Security Researcher Leaderboard. Let’s get started!

What is MSRC?

The Microsoft Security Response Center(MSRC) is part of the microsoft defender community and on the front line of microsoft security response evolution. This platform engaged with security researchers working to protect Microsoft’s customers and the broader ecosystem. For more details: Microsoft Security Response Center

Part 1 — Selecting a program
Before starting my bug bounty hunting journey, I navigated to Microsoft Bounty Programs | MSRC for a list of in-scope and ongoing programs. After going through the list, I decided to work on Microsoft Dynamics 365 and Power Platform Program.
Press enter or click to view image in full size
Microsoft Dynamics 365 and Power Platform
Part 2 —Let the hunt begin!
Analyzing the target
I started the hunt on Power Apps Platform.
While analyzing the Power Apps Platform and the applications on it, I noticed that an application sent requests to https://apps.powerapps.com
It caught my attention. Therefore, I navigated to the following URL:
https://apps.powerapps.com/authflow/authframe?telemetryLocation=global
Press enter or click to view image in full size
This page displayed nothing. However, after viewing the HTML code, I noticed that the value of telemetryLocation parameter was reflected to the page.
Press enter or click to view image in full size
I modified the value of telemetryLocation parameter from global to m3ez. The result proved that I could control telemetryLocation value.
Press enter or click to view image in full size
Exploit start!
After analyzing this page, I performed Cross-site Scripting (XSS) testing by injecting the following JavaScript payload:
</script>
As a result, I discovered that the page reflected the payload without input validation or sanitization mechanism.
Press enter or click to view image in full size
I injected the following XSS payload into telemetryLocation parameter:
</script><body/onload=alert(`m3ez`)>
The final URL was
https://apps.powerapps.com/authflow/authframe?telemetryLocation=</script><body/onload=alert(`m3ez`)>
After opening the link, the XSS payload was executed as shown in the image below.
Press enter or click to view image in full size

PoC

Get Supakiad S. (m3ez)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Part 3 — Reporting

After discovering and confirming that the target was vulnerable to Cross-site Scripting (XSS), I immediately began the reporting process through MSRC portal. This consists of the following steps:

Navigated to Report a Vulnerability | MSRC Researcher Portal
Entered vulnerability details, including Impact, PoC, and Evidence. Then, submitted the form.
Press enter or click to view image in full size
MSRC Researcher Portal (microsoft.com)
Press enter or click to view image in full size
After 4 days, MSRC team replied and confirmed my report. ^_^
Press enter or click to view image in full size
Within the same day, Microsoft bounty team replied that they were reviewing a possible bounty award for my vulnerability report.
Press enter or click to view image in full size
After a few hours, I received great news from the MSRC team ^_^
Press enter or click to view image in full size
Part 4 — Claims the Rewards
After Microsoft bounty team confirming my report eligibility for bounty rewards, they inquired about payment providers selection for bounty awards delivery.
Press enter or click to view image in full size

Note: Currently, Microsoft only supports awards delivery through either Bugcrowd or Microsoft Payment Central in order to receive bounty award payments.

A few weeks later, I received an email from Bugcrowd which contains a submission claiming link from Microsoft Bug Bounty Program.
Press enter or click to view image in full size
After claiming, I received my first reward from Microsoft Bug Bounty Program.
Press enter or click to view image in full size
A few months later, my name has been ranked on 2022 Q3 Leaderboard | MSRC Researcher Portal (microsoft.com)
Press enter or click to view image in full size
And I have been recognized on the recent quarterly leaderboard for Microsoft MSRC and will be receiving some MSRC magic swag as a reward for my achievements!
Press enter or click to view image in full size
Disclosure Timelines
Sep 23, 2022 — Vulnerability Discovered and Reported through MSRC portal.
Sep 27, 2022 — MSRC team confirmed. MSRC ticket was moved to Review/Repro.
Sep 27, 2022 — MSRC status was changed from Review / Repro to Develop
Dec 1, 2022 — MSRC status was changed to Pre-Release and Complete.
Dec 23, 2022 — Public release of the security advisory.

This is my first bug bounty writeup and a part of my valid bugs found on the Microsoft bounty program. I hope you enjoy the story. Thank you for reading.

Special thanks to Suphitcha Worasing for reviewing the content and grammar.

Any comments and suggestions will be appreciated ^_^

I appreciate your feedback and would love to hear your thoughts on my blog. If you have any comments or suggestions, please feel free to reach out to me on LinkedIn or Twitter.

LinkedIn: Supakiad S.

Twitter: (@Supakiad_Mee)

Thank you for your support!
