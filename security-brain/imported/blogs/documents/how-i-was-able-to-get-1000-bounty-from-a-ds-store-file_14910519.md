---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-21_how-i-was-able-to-get-1000-bounty-from-a-ds-store-file.md
original_filename: 2021-08-21_how-i-was-able-to-get-1000-bounty-from-a-ds-store-file.md
title: How I was able to get 1000$ bounty from a ds-store file?
category: documents
detected_topics:
- idor
- command-injection
- information-disclosure
tags:
- imported
- documents
- idor
- command-injection
- information-disclosure
language: en
raw_sha256: 149105193c4709907b84988e51c13aec15a303d7b57762eb68d11fce6d0d9a2d
text_sha256: 3661ab6d15cd98f5845aa079b6fd4c7af2f9a39bbeb47ced5020fba066604c4a
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to get 1000$ bounty from a ds-store file?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-21_how-i-was-able-to-get-1000-bounty-from-a-ds-store-file.md
- Source Type: markdown
- Detected Topics: idor, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `149105193c4709907b84988e51c13aec15a303d7b57762eb68d11fce6d0d9a2d`
- Text SHA256: `3661ab6d15cd98f5845aa079b6fd4c7af2f9a39bbeb47ced5020fba066604c4a`


## Content

---
title: "How I was able to get 1000$ bounty from a ds-store file?"
url: "https://xelkomy.medium.com/how-i-was-able-to-get-1000-bounty-from-a-ds-store-file-dc2b7175e92c"
authors: ["Khaled Mohamed (@0xElkomy)"]
bugs: ["Information disclosure", "Debugging enabled"]
bounty: "1,000"
publication_date: "2021-08-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3402
scraped_via: "browseros"
---

# How I was able to get 1000$ bounty from a ds-store file?

How I was able to get 1000$ bounty from a ds-store file?
Khaled Mohamed
Follow
3 min read
·
Aug 21, 2021

533

5

Press enter or click to view image in full size
Photo by Florian Olivo on Unsplash
Go!

Hello, gents and ladies :), In this blog, we will talk about one bug I was found before and to know I did not get this bug in just 5 minutes to know It needs experience with some patience to get some bug that was I mean, you need to learn more to be able to get a lot of bugs it’s not a superpower but it’s called a continuity pursuit.

The Starter?

I will teach you how to get bounty from ds-store-file in 5 minutes [I Just kidding]. Let’s start with the starter pack. In the first, I was just collect some information about the subdomains and the ASNs numbers and check the Public CVEs with some tools I will mention below. When I was collecting the information I found the /.DS_Store I available I knew there is a tool easiest to dump this file with the terminal I will mention there in the exploit section, I think to here we were talking about noting important let's go to the exploit section.

Tools used in the Exploit
1 — Subfinder
2 — Httpx
3 — Nuclei
4 — ds_store_exp

Shout out to @projectdiscovery

Exploit

Hello again, In the first, I was run a subfinder with httpx and got about 100 subdomains is alive and send this output to the nuclei public templates not a private. And after this, I will still wait to finish those tools but with the owasp zap proxy I was doing some manual searching about bugs with this proxy, and still nothing Important but after the Nuclei finished I found a subdomain with Info severity file called /.DS_Store after this, I clone the ds_store_exp tool and use it to dump the file after dump I found a directory with a debug error from a Laravel Framework called Symfony to watch the image below..

Press enter or click to view image in full size
Symfony Profiler Search Bar

But before that, I just saw a big error I can’t understand anything about it but after some clicks, I got the image above. let’s continue

Get Khaled Mohamed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But after that, I report the bug as just debug enabled but one from the trigger team told me it’s not a bug what is the impact you can get from it, In the first reaction from me it was I can’t get anything but after some minutes about one hour, I click on the latest button on the left and found cookies and IP it’s not formed me it was for one from the trigger team in the program and I try to use that cookie on the main site It was the exciting thing I take over the account with just a debug mode enabled just need one click from the user to go to the error page and I can just steal his cookies.

I think it is a high impact now but the team considers it as a medium, I don’t understand why.

Conclusion

The Conclusion is how the ds-store file is important and can make you get bugs from it, you just need to focus more on what you got from your recon, and God willing you will get a bounty rewarded.

TimeLine

1 — Submit the Report on Aug 14th — 2021.

2 — More information at Aug 14th — 2021.

3 — Send new information on Aug 14th — 2021.

4 — Triged on Aug 14th — 2021.

5 — Receive a bounty on Aug 19th — 2021 It was a 500$ bounty and 500$ bonus.

Please don’t forget to follow me on the Twitter to watch new blogs from me on @0xELkomy and if you have any comment also send to me thanks. Feel free to connect with me if you have anything.

Thank you to read the full blog

Regards,

xElkomy

Checkout more blogs on @cyberar:

Understanding IDOR Vulnerabilities: Protecting Sensitive Event Data (cyberar.io)
