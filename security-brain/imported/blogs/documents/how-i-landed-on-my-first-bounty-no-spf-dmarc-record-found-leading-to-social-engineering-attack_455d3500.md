---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-18_how-i-landed-on-my-first-bounty-no-spf-dmarc-record-found-leading-to-social-engi.md
original_filename: 2020-07-18_how-i-landed-on-my-first-bounty-no-spf-dmarc-record-found-leading-to-social-engi.md
title: 'How I landed on my first bounty : No SPF / DMARC Record Found leading to Social
  Engineering Attack'
category: documents
detected_topics:
- command-injection
- supply-chain
tags:
- imported
- documents
- command-injection
- supply-chain
language: en
raw_sha256: 455d35007b680d5dcc764f275c186400ef81e775d635e8a0296396ff06efe700
text_sha256: fe9eacd44d101ee64de48ddb3671bfac12dd4ec2cb6572eedd8b71813539adde
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# How I landed on my first bounty : No SPF / DMARC Record Found leading to Social Engineering Attack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-18_how-i-landed-on-my-first-bounty-no-spf-dmarc-record-found-leading-to-social-engi.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `455d35007b680d5dcc764f275c186400ef81e775d635e8a0296396ff06efe700`
- Text SHA256: `fe9eacd44d101ee64de48ddb3671bfac12dd4ec2cb6572eedd8b71813539adde`


## Content

---
title: "How I landed on my first bounty : No SPF / DMARC Record Found leading to Social Engineering Attack"
url: "https://medium.com/@fardeenahmed410/how-i-landed-on-my-first-bounty-no-spf-dmarc-record-found-2fdfea64cf52"
authors: ["Fardeen Ahmed"]
programs: ["Lululemon"]
bugs: ["No valid SPF records", "No DMARC records"]
bounty: "250"
publication_date: "2020-07-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4399
scraped_via: "browseros"
---

# How I landed on my first bounty : No SPF / DMARC Record Found leading to Social Engineering Attack

How I landed on my first bounty : No SPF / DMARC Record Found leading to Social Engineering Attack
Fardeen A.
Follow
2 min read
·
Jul 18, 2020

116

7

Hey there. Today i will be sharing you about how i was able to earn a bounty of €250 for demonstrating how a user can be social engineered at www.lululemon.com. So let’s start.

I went through the bug-bounty program of lululemon, a European Web-store. I checked through its gateways, and found nothing to be present. So i went up. Eventually, I thought of finding logical bug and if possible escalating to next level (only if it was possible), so checked DMARC, DNS and SPF Record through these sites respectively :-

MX Lookup Tool - Check your DNS MX Records online - MxToolbox
Javascript is disabled. Javascript is required for this site. This test will list MX records for a domain in priority…

mxtoolbox.com

SPF Query Tool
These tools are meant to help you deploy SPF records for your domain. They use an actual RFC 7208 compliant library…

www.kitterman.com

I found the webstore without SPF Record, and without DMARC Record. For knowing more about SPF, DMARC ad expired DNS Record, please visit here :

SmarterTools Incorporated
In our last post, Understanding Spam in the New SmarterMail, we mentioned some of the changes to the antispam settings…

www.smartertools.com

Now, as it doesn’t contain a proper or well-configured SPF/DMARC Record as well as no DNS configuration found, i tried to send email through fake mailer (a.k.a shwoing how a social engineering attack can take place) it with emkei.cz fake mailer. And this time, it happened. BINGO!!!!!!

Get Fardeen A.’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I reported it with a valid POC, demonstrated about how it can be used using a video POC. They at first said it’s not qualifiable for P3 vulnerability, then again i showed and gave valid proofs with a new POC

TIP : Many a time they won’t “Triage” your report and tell it as P5. You don’t have to get mad or feel sad. Again send them a message about your finding and to what extent you can escalate vulnerability to. They will surely give the reply back with positive response.

After 4–5 days of intrusive search and inspection, they responded with the bounty of €250, and it came to me.

So, many said for this write-up, and i gave you all the easiest way possible. Hope it works for you. Thank you and keep rocking…!!!!! And just don’t stop.

Follow up my Instagram : fardeenchenzhen

/////////////////####Happy Hacking####\\\\\\\\\\\\\\\\\\\\\
