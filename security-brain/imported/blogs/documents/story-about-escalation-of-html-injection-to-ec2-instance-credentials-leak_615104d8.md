---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-14_story-about-escalation-of-html-injection-to-ec2-instance-credentials-leak.md
original_filename: 2022-10-14_story-about-escalation-of-html-injection-to-ec2-instance-credentials-leak.md
title: Story about Escalation of HTML Injection to EC2 Instance credentials leak
category: documents
detected_topics:
- ssrf
- cloud-security
- xss
- command-injection
- otp
tags:
- imported
- documents
- ssrf
- cloud-security
- xss
- command-injection
- otp
language: en
raw_sha256: 615104d85d8ba56104bd74da5a654e37039aa68f9e1e47a92654cf1c0646522a
text_sha256: 3fe02291dca074fa736eba66ed0ee6c84d25308b1bc6020eac5c9a70e8fb2dc8
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Story about Escalation of HTML Injection to EC2 Instance credentials leak

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-14_story-about-escalation-of-html-injection-to-ec2-instance-credentials-leak.md
- Source Type: markdown
- Detected Topics: ssrf, cloud-security, xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `615104d85d8ba56104bd74da5a654e37039aa68f9e1e47a92654cf1c0646522a`
- Text SHA256: `3fe02291dca074fa736eba66ed0ee6c84d25308b1bc6020eac5c9a70e8fb2dc8`


## Content

---
title: "Story about Escalation of HTML Injection to EC2 Instance credentials leak"
url: "https://medium.com/@Cybervenom/story-about-escalation-of-html-injection-to-ec2-instance-credentials-leak-e2cbd7343a83"
authors: ["Harsh Tandel (@H4r5h_T4nd37)"]
bugs: ["SSRF", "HTML injection"]
publication_date: "2022-10-14"
added_date: "2022-10-17"
source: "pentester.land/writeups.json"
original_index: 2040
scraped_via: "browseros"
---

# Story about Escalation of HTML Injection to EC2 Instance credentials leak

Story about Escalation of HTML Injection to EC2 Instance credentials leak
Harsh Tandel
Follow
2 min read
·
Oct 14, 2022

108

Hello all, Thank for the overwhelming response here I am with my new finding tale.

So here in the web app there was functionality for generating invoices. There was blacklist-based filtering and input is allowed to limited numbers. There was a company address textbox that allowed HTML attributes a has capacity of more characters then any other fields.

To validate HTMLI i used payload “<h1>TEST</h1><b>test</b>” and then selected data range and generated invoice.It executed in invoice PDF.So i decided to escalate it.I used iframe with aws metadata url http://169.254.169.254/latest/meta-data/ .But as i clicked on save it blocked request.So I need to escalate it with bypassing the filter.

So firstly i need to figure out what is blacklisted i tried to bypass using redirection but it ended up with error cause it was not following redirect.So i decide to do encoding and converting to decimal. Finally I converted “169.254.169.254” into decimal which is “2852039166”. This converted version bypassed blacklist filter and data saved successfully.

Press enter or click to view image in full size

So I generated invoice and clicked on download.Yes I got metadata page printed in a address text box.So it was successfully exploited.But as i tried “http://2852039166/latest/meta-data/iam/security-credentials” it again blocked me. So i can show metadata but it was not that enough.

Get Harsh Tandel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now i Reviewed metadata and i got endpoint “identity-credentials”. I repeated procedure to see what’s in it. At last i come to “identity-credentials/ec2/security-credentials/ec2-instance” which was retrieving ec2 instance accesskey,secret key and token.

So our final url is “http://2852039166/latest/meta-data/identity -credentials/ec2/security-credentials/ec2-instance” and payload is “ <iframe src = “http://2852039166/latest/meta-data/identity -credentials/ec2/security-credentials/ec2-instance” width =“800” height = “800”></iframe> ”

I placed payload in address field and hit save and it saved successfully.Now generated invoice and downloaded boom ec2 credentials are leaked.

I could use and get into ec2 but it was out of our engagement scope.So here i stopped.

Thank You Peace out.
