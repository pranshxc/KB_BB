---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-01_stored-xss-with-password-recovery-page.md
original_filename: 2020-07-01_stored-xss-with-password-recovery-page.md
title: Stored XSS with Password Recovery Page
category: documents
detected_topics:
- xss
- command-injection
- cors
tags:
- imported
- documents
- xss
- command-injection
- cors
language: en
raw_sha256: 45dccf803105967cc3d14ff47b2c9e607ededf977504859d140472ecef739ed6
text_sha256: 13f4613b8cf3992cb8ecbf13c2c45962f7a342c690c56c57266907b38b9e3993
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS with Password Recovery Page

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-01_stored-xss-with-password-recovery-page.md
- Source Type: markdown
- Detected Topics: xss, command-injection, cors
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `45dccf803105967cc3d14ff47b2c9e607ededf977504859d140472ecef739ed6`
- Text SHA256: `13f4613b8cf3992cb8ecbf13c2c45962f7a342c690c56c57266907b38b9e3993`


## Content

---
title: "Stored XSS with Password Recovery Page"
page_title: "EN | Stored XSS with Password Recovery Page > Lütfü Mert Ceylan"
url: "https://lutfumertceylan.com.tr/posts/stored-xss-with-password-recovery-page/"
final_url: "https://lutfumertceylan.com.tr/posts/stored-xss-with-password-recovery-page/"
authors: ["Lütfü Mert Ceylan (@lutfumertceylan)"]
bugs: ["Stored XSS"]
publication_date: "2020-07-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4458
---

# EN | Stored XSS with Password Recovery Page

June 01, 2020

![](/images/cross-site-scripting.svg)  

In April of this year, I found a Stored Xss vulnerability at University of Utwente. However, I later realized that there was a vendor of the vulnerable system, and I contacted them. Then they fixed this vuln. and rewarded me with a $$$ bounty. Also this was my first bounty. I don’t say the company that produced the system because they want to remain confidential.

### Recon

I discovered XSS with a simple payload execution in the “First Name” input. But I thought this vuln was a Self XSS. Because all pages were private for every user (except for one page). Then I saw that the password recovery page also contains user First Name value.

### First Try

I type a payload in the “first_name” input  
![](/images/payl.png)

but the system always encodes the payloads on Profile Page.  
![](/images/payl2.png)

Profile Page was not public anyway. Not bad luck!

### Catch You!!

I believed XSS was no longer possible. But there is one last place, “Password Recovery Page”, Moreover, it reflects the user’s “first_name” value to the page.

I just created the page with the request to create a Password Recovery Page. The system not encode the payload on this page. So payload was executed!

### The end :

9 April 2020 - Report sent  
10 April 2020 - Scenario requested  
13 April 2020 - Report’s scenario sent  
14 April 2020 - I was awarded a $$$ bounty  

**__Tags:** [Bug Bounty](https://lutfumertceylan.com.tr/tags/#bug-bounty),  [bugbounty](https://lutfumertceylan.com.tr/tags/#bugbounty),  [hack](https://lutfumertceylan.com.tr/tags/#hack),  [poc](https://lutfumertceylan.com.tr/tags/#poc),  [stored xss](https://lutfumertceylan.com.tr/tags/#stored-xss),  [write-up](https://lutfumertceylan.com.tr/tags/#write-up),  [xss in password recovery](https://lutfumertceylan.com.tr/tags/#xss-in-password-recovery)

#### Share on

[ __Twitter](https://twitter.com/intent/tweet?text=https://lutfumertceylan.com.tr/posts/stored-xss-with-password-recovery-page/ "Share on Twitter") [__Facebook](https://www.facebook.com/sharer/sharer.php?u=https://lutfumertceylan.com.tr/posts/stored-xss-with-password-recovery-page/ "Share on Facebook") [__LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https://lutfumertceylan.com.tr/posts/stored-xss-with-password-recovery-page/ "Share on LinkedIn") Previous [Next](https://lutfumertceylan.com.tr/posts/ato-and-data-leakage-via-cors-misc0/ "EN | Account Takeover and Sensitive Data Leakage via CORS Misconfiguration ")
