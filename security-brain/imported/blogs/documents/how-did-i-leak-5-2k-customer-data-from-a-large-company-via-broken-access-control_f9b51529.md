---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-11_how-did-i-leak-52k-customer-data-from-a-large-company-via-broken-access-control.md
original_filename: 2022-03-11_how-did-i-leak-52k-customer-data-from-a-large-company-via-broken-access-control.md
title: How Did I Leak 5.2k Customer Data From a Large Company? (via Broken Access
  Control)
category: documents
detected_topics:
- access-control
- command-injection
- file-upload
- automation-abuse
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- file-upload
- automation-abuse
- api-security
language: en
raw_sha256: f9b51529517f4ff2ce763999123982d6b4257a44af5aa4f69bbdead042bd2fe7
text_sha256: 5ae169894213de9b0fb3ba26b9307f56000e66f670208cc2522d3e08a785c5d5
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# How Did I Leak 5.2k Customer Data From a Large Company? (via Broken Access Control)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-11_how-did-i-leak-52k-customer-data-from-a-large-company-via-broken-access-control.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, file-upload, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `f9b51529517f4ff2ce763999123982d6b4257a44af5aa4f69bbdead042bd2fe7`
- Text SHA256: `5ae169894213de9b0fb3ba26b9307f56000e66f670208cc2522d3e08a785c5d5`


## Content

---
title: "How Did I Leak 5.2k Customer Data From a Large Company? (via Broken Access Control)"
url: "https://canmustdie.medium.com/how-did-i-leak-5-2k-customer-data-from-a-large-company-via-broken-access-control-709eb4027409"
authors: ["can1337 (@canmustdie)"]
bugs: ["Broken Access Control"]
publication_date: "2022-03-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2833
scraped_via: "browseros"
---

# How Did I Leak 5.2k Customer Data From a Large Company? (via Broken Access Control)

Top highlight

How Did I Leak 5.2k Customer Data From a Large Company? (via Broken Access Control)
can1337
Follow
3 min read
·
Mar 12, 2022

550

1

Hello everyone!

Today we’re going to talk about the vulnerability I found a few months ago. The vulnerability targeted customers and suppliers directly in the company, also was a subdomain of a large skincare company. (This report has been resolved but I can’t provide information about the company because it runs a private program) I will try to explain this vulnerability to you briefly. I hope I can contribute to the development of your know-how. So let’s get started.

Recon is not dead!

First, I was on crt.sh and after several unsuccessful hacking attempts to other subdomains I found this subdomain. The subdomain was just an employee panel and no other features. It only covered the login panel.

Press enter or click to view image in full size
(It looks pretty straight.)

I ran LinkFinder on that panel and found a few JS files from the app. One of the JS files won my priority because the filename contained the word “login”.

Press enter or click to view image in full size

The href part is interesting. If we had a successful login it would redirect us to ‘App/Index/#!/Dashboard’. But does it really control? Here’s the time to test the Broken Access Control.

Get can1337’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I went directly to the href address without logging in and was successfully able to access the app’s dashboard! No need to login.

Press enter or click to view image in full size

But that is not all. Because there was something wrong. The application dashboard didn’t return any data. I could only see the interface. Everything was zero.

More recon get results & It’s hacktime!

Here is the exciting part. I needed more endpoints because that JS file didn’t contain any other endpoints. I went back to Linkfinder and started inspecting all the JS files I found. Before long, I reached the following endpoints.

Press enter or click to view image in full size

I’ve tried a few endpoints and all, and I had some results as “Inbound” and “Outbound”. (These meant customers and suppliers.)

Press enter or click to view image in full size

I came across such a tab and the file upload function was ineffective. However, the ‘Customer’ button in the ‘Download Templates’ tab was working. (Likewise the ‘Suppliers’ button in Inbound) BINGO!

I got all (5200-odd) the customers and suppliers’ PII information in the app. (Both csv files contain customer_code, name, address, phone.)

Press enter or click to view image in full size
Press enter or click to view image in full size

I had to download and search to check if the data was genuine. I did NOT go further than this step.

This report is rated high severity and fixed several months ago. And here is my tweet:

https://twitter.com/canmustdie/status/1471101658679681024

That’s all for now. Thanks for reading. See you in another write up!

You can follow me on twitter: https://twitter.com/canmustdie
