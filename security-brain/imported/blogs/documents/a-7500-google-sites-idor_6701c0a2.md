---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-24_a-7500-google-sites-idor.md
original_filename: 2021-10-24_a-7500-google-sites-idor.md
title: A 7500$ Google sites IDOR
category: documents
detected_topics:
- idor
- access-control
- command-injection
- mfa
tags:
- imported
- documents
- idor
- access-control
- command-injection
- mfa
language: en
raw_sha256: 6701c0a24348e6f0a73ee4bb60aa9758015f440ee54e34ea3fc0304191cae030
text_sha256: 238050a3f945cd2e8520270d51c52050daf75245534a0a1be4dd4b7cdf3954d4
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# A 7500$ Google sites IDOR

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-24_a-7500-google-sites-idor.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, mfa
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `6701c0a24348e6f0a73ee4bb60aa9758015f440ee54e34ea3fc0304191cae030`
- Text SHA256: `238050a3f945cd2e8520270d51c52050daf75245534a0a1be4dd4b7cdf3954d4`


## Content

---
title: "A 7500$ Google sites IDOR"
page_title: "A 7500$ Google sites IDOR – Jal | r0ckin's blog"
url: "https://r0ckinxj3.wordpress.com/2021/10/24/a-7500-google-sites-idor/"
final_url: "https://r0ckinxj3.wordpress.com/2021/10/24/a-7500-google-sites-idor/"
authors: ["Jalal (@r0ckin_)"]
programs: ["Google"]
bugs: ["IDOR"]
bounty: "7,500"
publication_date: "2021-10-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3217
---

#  A 7500$ Google sites IDOR

Posted by[r0ckinxj3](https://r0ckinxj3.wordpress.com/author/r0ckinxj3/)[24 October 202114 July 2024](https://r0ckinxj3.wordpress.com/2021/10/24/a-7500-google-sites-idor/)Posted in[Non classé](https://r0ckinxj3.wordpress.com/category/non-classe/)

Hi, 

My name is **Jalal** aka **r0ckin** and this is my first blog post and it is about a vulnerability that I’ve discovered on Google sites.

##### What is Insecure Direct Object Reference(IDOR):

According to OWASP, An Idor vulnerability can permit you to view or edit someone else’s account by providing its unique identifier and it is an access control bug.

[**Broken Access Control**](https://owasp.org/Top10/A01_2021-Broken_Access_Control/) has taken the first rank on OWASP top-10-2021.

[![](https://owasp.org/www-project-top-ten/assets/images/mapping.png)](https://owasp.org/www-project-top-ten/assets/images/mapping.png)

now let’s move straightforward on how did I found this bug.

_**Mapping the application**_

So the first that I’ve done is to map the application: 

After configuring my browser with my favorite intercepting proxy burp suite, I configured the scope under the proxy tap to include “sites.google.com” and I started mapping out the application, This was done by first exploring visible content and then browsing the entire application, visiting every link and submitting every form. 

**Analyzing the application**

So after reviewing the sitemap i found this request

![](https://imgur.com/28yidz5.png)

After few tries on fuzzing for other bugs with no success, I decided to hunt for idors, So i created a second account that is identified by **tomasideasontesting** , And from the site map I replaced every **catherinerecipespersonal** by **tomasideasontesting** and I reviewed the response to see if it succeeded or not.

**Results**

So after trying to find idors, the other requests had no success because access controls measures had been taken. But on the **service=ListScripts** i got an 200 ok response with a private identifer for **tomasideasontesting** scripts! 

![](https://imgur.com/UJX28qK.png)

[](https://imgur.com/UJX28qK.png)

**Final thoughts**

I think that endpoint was vulnerable because it was connected with other google service(**script.google.com)** so the developers did not pay attention to it.

**Video**

[](https://imgur.com/28yidz5.png)

Thanks for reading 

To: r0ckin <r0ckinxj3@hotmail.com>

<https://twitter.com/r0ckin_>[](https://twitter.com/share?url=https%3a%2f%2fportswigger.net%2fweb-security%2faccess-control%2fidor&text=Insecure+direct+object+references+\(IDOR\)+%7c+Web+Security+Academy%0A)

### Share this:

  * [ Share on X (Opens in new window) X ](https://r0ckinxj3.wordpress.com/2021/10/24/a-7500-google-sites-idor/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://r0ckinxj3.wordpress.com/2021/10/24/a-7500-google-sites-idor/?share=facebook)
  * 

Like Loading...

### _Related_

Posted by[r0ckinxj3](https://r0ckinxj3.wordpress.com/author/r0ckinxj3/)[24 October 202114 July 2024](https://r0ckinxj3.wordpress.com/2021/10/24/a-7500-google-sites-idor/)Posted in[Non classé](https://r0ckinxj3.wordpress.com/category/non-classe/)
