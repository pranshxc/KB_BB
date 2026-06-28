---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-17_1000-ssrf-in-slack.md
original_filename: 2019-02-17_1000-ssrf-in-slack.md
title: $1.000 SSRF in Slack
category: documents
detected_topics:
- ssrf
- command-injection
- mobile-security
tags:
- imported
- documents
- ssrf
- command-injection
- mobile-security
language: en
raw_sha256: 44eff91c47ea25c5ebfb867ea20dddc5a208e1a194bebf404e135daf4b3270b7
text_sha256: 0861258d1a2e61ec9d22fa029708c9167e2d95e37106bff0de6ac88c14d1eb27
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# $1.000 SSRF in Slack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-17_1000-ssrf-in-slack.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, mobile-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `44eff91c47ea25c5ebfb867ea20dddc5a208e1a194bebf404e135daf4b3270b7`
- Text SHA256: `0861258d1a2e61ec9d22fa029708c9167e2d95e37106bff0de6ac88c14d1eb27`


## Content

---
title: "$1.000 SSRF in Slack"
url: "https://medium.com/@elberandre/1-000-ssrf-in-slack-7737935d3884"
authors: ["Elber Andre (@Elber333)"]
programs: ["Slack"]
bugs: ["SSRF"]
bounty: "1,000"
publication_date: "2019-02-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5406
scraped_via: "browseros"
---

# $1.000 SSRF in Slack

$1.000 SSRF in Slack
Elber Andre
Follow
4 min read
·
Feb 17, 2019

436

1

Before I start, I have two important tips for anyone starting in the world of BugBounty.

1: Always check previous reports, you may know some bypass that may work in that situation, or you can learn something new.

2: If you like content about Bug Bounty or other hacking related stuff, sign up for my channel and follow the new posts.

Elber Tavares
BugBounty, CTF, Writeups e outros temas aleatórios.

www.youtube.com

SLACK AND SSRF:
Press enter or click to view image in full size

Slack is the collaboration hub that brings the right people, information, and tools together to get work done. From Fortune 100 companies to corner markets, millions of people around the world use Slack to connect their teams, unify their systems, and drive their business forward.

Slash Commands;

“SSRF in api.slack.com, using slash commands and bypassing the protections.”

You can learn more about Slash Commands Here:

“Some Slack features like “Integrations / Phabricator” and “Integration / Slash Commands” allow users to submit URL that will be accessed by the backend servers. A blacklist tries to forbid access to internal resources (loopback, 10.0.0.0/8, 192.168.0.0/24, …). This blacklist can be bypassed using “[::]” as the hostname. Only services binding all the interfaces and supporting IPv6 can be reached using that vector.” Said user agarri_fr for the slack.

Press enter or click to view image in full size

Slack has disabled the option to register IPV6 addresses in your Slash Commands.

slacka: ‘I created a new issue for the ipv6 blocking and escalated the case with our engineers. I’ll let you know when we have an update.’

~Fixed~

For them, a fix, for me, a bypass.

To bypass this new protection, I used a redirect with the ‘Location’ header in PHP.

in your own domain: index.php

<?php
header("location: http://[::]:22/");
?>

location: http://[::]:22/

And save.

Go to your Slack and type /youslash

Try with my server http://hackerserver[.]com/

Results:

:22

:25

Jul 13th — First response
Jul 18th — Triaged
Jan 23 — Slack rewarded elber with a $500 bounty.

After I found this bypass, I looked for more vulnerabilities in Slack, and I found the Event Subscriptions parameter.

Get Elber Andre’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

“Bypass of the SSRF protection in Event Subscriptions parameter.”

The vulnerability is present in the “Event Subscriptions” parameter where:
“Your app can subscribe to be notified of events in Slack (for example, when a user adds a reaction or creates a file) at a URL you choose. ".
URL:
https://api.slack.com/apps/YOUAPPCODE/event-subscriptions?

When we add a site that does not meet API standards, we receive the following message:

Press enter or click to view image in full size

Your request URL gave us a 500 error. Update your URL to receive a new request and challenge value.

Bypass using an IPV6 vector [::].

On my host, x.php has:

<?php
header("location: ".$_GET['u']);
?>

PoC:

http://hacker.site/x.php/?u=http://%5B::%5D:22/

Response:
SSH [::]:22

SMTP [::]:25

This report Slack selected as a duplicate of another SSRF, I insisted that they put me as a participant in the other report.

I saw that the other report was different from mine, so I told the team that they could have been wrong.

Press enter or click to view image in full size

Jul 24th — Duplicated
Sep 2nd — Triaged
Jan 23 — Slack rewarded elber with a $500 bounty.

References:

https://hackerone.com/reports/61312

(The reports will be publicly disclosed on Hackerone on 02/22)

https://hackerone.com/reports/381129

https://hackerone.com/reports/386292
