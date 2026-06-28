---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-14_how-i-bypassed-incapsula-waf-by-imperva.md
original_filename: 2021-12-14_how-i-bypassed-incapsula-waf-by-imperva.md
title: How I Bypassed Incapsula WAF By Imperva
category: documents
detected_topics:
- sqli
- api-security
- command-injection
tags:
- imported
- documents
- sqli
- api-security
- command-injection
language: en
raw_sha256: ca18452d941a7da656e4098fe3df786721682ada44a2520ac66d601e79d50592
text_sha256: 2eb2977fac2e6bfb2df1637ba8adc4e79d5d6cb914fb16435910a811efa40b9e
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# How I Bypassed Incapsula WAF By Imperva

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-14_how-i-bypassed-incapsula-waf-by-imperva.md
- Source Type: markdown
- Detected Topics: sqli, api-security, command-injection
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `ca18452d941a7da656e4098fe3df786721682ada44a2520ac66d601e79d50592`
- Text SHA256: `2eb2977fac2e6bfb2df1637ba8adc4e79d5d6cb914fb16435910a811efa40b9e`


## Content

---
title: "How I Bypassed Incapsula WAF By Imperva"
url: "https://medium.com/@daudmalik06/how-i-bypassed-incapsula-waf-db0498b3a021"
authors: ["Dawood Ikhlaq"]
bugs: ["SQL injection"]
publication_date: "2021-12-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3089
scraped_via: "browseros"
---

# How I Bypassed Incapsula WAF By Imperva

How I Bypassed Incapsula WAF By Imperva
Vulert
Follow
3 min read
·
Dec 14, 2021

73

About Myself

Hi All, I’m Dawood, having more than 7 years of experience in cyber security, especially in web application security, a passionate developer and always a learner.

Listed in the hall of fame of many big companies for responsible vulnerability disclosure including Google, Facebook etc.

Test Scenario

Please Note: In this write-up, for privacy reasons I have replaced the target name, username and passwords with “redacted”.

I was testing the rest API of a web application https://redacted.com/ for security vulnerabilities. There was an endpoint that caught my attention, this endpoint was used to add or update items within the cart.

Vulnerability

Actually, as can be seen from the screenshot below: the endpoint was not validating an input called (courses) and while testing against different vulnerabilities i found that the endpoint was vulnerable to SQL Injection. During differet test i found that the application was using Incapsula WAF by Imperva to protect itself from cyber attacks, and was making the testing difficult.

Press enter or click to view image in full size

How I bypassed Incapsula WAF

Som I decided to bypass the installed WAF, the WAF was blocking almost all of the complex queries including all of the SQL special keywords like (insert, update, sleep, onto, etc.)

Press enter or click to view image in full size

As can be seen from the above screenshot the WAF was completely blocking the special keywords including the keyword sleep,

I tried different ways like sleep(1+1), sleep (5), sleep(/**/2), etc.. and none of them was working, all requests were being blocked by WAFof.

Why did I decide to use a sleep statement? I was using a sleep statement to demonstrate the SQL injection vulnerability without harming the database or without accessing any confidential data.

Then I decided to use partial url encoding sle%25p(5) which is equivalent to sleep(5), and even this was blocked then I decided to put some random hex value within the parenthesis with URL encoding and I was amazed to see that the payload sle%25p%28'0x12'%2b1) bypassed the Famous WAF .

Get Vulert’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

If you decode the payload using url decoding the payload is simply sleep(‘0x12’+1), which is a completely valid sql statement and this bypasses the expensive WAF.

Exploit

By using Boolean based SQLI, i was able to fetch the current user of the database ( for the sake of simplicity and security i am using the word redacted instead of real username value ).

Payload

I have used the following payload

‘%2b12%2bif(user()+like+redacted%’,2,sle%45p%28'0x12'%2b1))+ — +s

This payload tells MySql if the current user is redacted then returns 2 and rest of query will be executed.

Press enter or click to view image in full size

otherwise it will cause the mysql to sleep and it seems it was sleeping for 4–5 seconds,

Press enter or click to view image in full size

Conclusion

Though it’s good to use web application firewalls and it helps avoiding security incidents in the beginning but they never guarantee the security of the application, the application security should be handled at application end.

And once again by this article We’ve proved that we should never rely on someone else i.e WAF but we should conduct manual security testing (Penetration Testing) ourselves.

For any clarification please don’t hesitate to ask me.

Best Regards

Dawood Ikhlaq

daudmalik06@gmail.com

Visit https://devnack.com for free consultation about your application security
