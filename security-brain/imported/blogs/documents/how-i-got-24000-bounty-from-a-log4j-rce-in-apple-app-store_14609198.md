---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-25_how-i-got-24000-bounty-from-a-log4j-rce-in-apple-app-store.md
original_filename: 2024-08-25_how-i-got-24000-bounty-from-a-log4j-rce-in-apple-app-store.md
title: How I got $24000 Bounty from a Log4j RCE in Apple App Store.
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
raw_sha256: 14609198ff709a34ec5ca1b75a6892aa4164a434dc222ff19ee0155d056cb6aa
text_sha256: 2ec7949b8acb4f33fa46e49cd961fd19bec7a01cd187a00c075c1c8a09625740
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# How I got $24000 Bounty from a Log4j RCE in Apple App Store.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-25_how-i-got-24000-bounty-from-a-log4j-rce-in-apple-app-store.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `14609198ff709a34ec5ca1b75a6892aa4164a434dc222ff19ee0155d056cb6aa`
- Text SHA256: `2ec7949b8acb4f33fa46e49cd961fd19bec7a01cd187a00c075c1c8a09625740`


## Content

---
title: "How I got $24000 Bounty from a Log4j RCE in Apple App Store."
url: "https://medium.com/@meharhuzaifa777/exploiting-log4j-rce-in-apple-app-store-ca99a549de1f"
authors: ["Mehar huzaifa (@Hunter_Huzaifa_)"]
programs: ["Apple"]
bugs: ["RCE", "Components with known vulnerabilities"]
bounty: "24,000"
publication_date: "2024-08-25"
added_date: "2024-08-26"
source: "pentester.land/writeups.json"
original_index: 44
scraped_via: "browseros"
---

# How I got $24000 Bounty from a Log4j RCE in Apple App Store.

Mehar huzaifa
 highlighted

How I got $24000 Bounty from a Log4j RCE in Apple App Store.
Mehar huzaifa
Follow
3 min read
·
Aug 26, 2024

212

3

Press enter or click to view image in full size
Summary.

Log4j is a popular Java-based logging library used by many organizations to log activity on their servers. The Log4j RCE vulnerability was disclosed in December 2021, which allows attackers to execute arbitrary code on a server running the vulnerable version of Log4j by sending a specially crafted string.

When this vulnerability surfaced, it quickly became a significant concern across the industry due to its simplicity of exploitation and the widespread use of Log4j.

Description.

My name is Huzaifa, and I am a cybersecurity researcher and bug hunter. this is my 1st writeup.

Lets Start.

In April 2022, I discovered a critical Remote Code Execution (RCE) vulnerability in the Apple App Store, stemming from the infamous Log4j vulnerability (CVE-2021–44228). This vulnerability, commonly known as “Log4Shell,” had widespread impacts globally, and its presence in a platform like the Apple App Store could have led to severe security breaches affecting millions of users.

It was a routine day, and I picked up my iPhone to change my region settings. While doing so, I noticed an input field for the city name. Given my background in security research and the ongoing concerns around Log4j, I decided to test whether the Apple App Store might still be vulnerable. I entered a Log4j payload in the city input field and proceeded to change my region. Initially, nothing seemed to happen 😟 , and I didn’t receive any indication that the payload had triggered.

Later that evening, I went to the App Store to download a game. As the game began downloading, I unexpectedly received an email notification from my server indicating that the Log4j payload had been triggered 🙂.

Intriguingly, the email also revealed the hostname of the App Store server. After that, I modified the payload to execute commands such as sys:os.name and sys:os.version, and to my surprise, these commands executed successfully, providing me with detailed information about the operating system running on the App Store's server.

Get Mehar huzaifa’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This confirmed that the input I provided earlier in the city field had been logged and subsequently executed, highlighting a severe vulnerability in the App Store’s backend systems. I promptly reported the vulnerability and at the end of our 1-month process, I received an e-mail like the one below and I was rewarded with $24000 Bounty! critical nature of the issue.

Press enter or click to view image in full size

Additionally, I received formal acknowledgment from Apple’s Product Security team for my contribution.

https://support.apple.com/en-us/102812 ( April 2022) .

Timeline:
April 05, 2022 — Initial Report.
April 14, 2022 — Triaged.
April 19, 2022 — Fixed.
April 29, 2022 — Bounty awarded.

Thank you for taking the time to read this article. I look forward to sharing more insights in future publications!

Good By!

Twitter & Linkdin
