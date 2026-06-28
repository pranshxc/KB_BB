---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-16_edmodo-bug-bounty-writeup.md
original_filename: 2021-05-16_edmodo-bug-bounty-writeup.md
title: Edmodo Bug Bounty Writeup
category: blogs
detected_topics:
- xss
- command-injection
tags:
- imported
- blogs
- xss
- command-injection
language: en
raw_sha256: 69a6ff458fe218ace406e01159fd912679402121bf435dc2bb0cb7abe10dd263
text_sha256: 1dd08915519388b1753525f1079c2f46c12faa15e1545dbb5100c6c152a75135
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Edmodo Bug Bounty Writeup

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-16_edmodo-bug-bounty-writeup.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `69a6ff458fe218ace406e01159fd912679402121bf435dc2bb0cb7abe10dd263`
- Text SHA256: `1dd08915519388b1753525f1079c2f46c12faa15e1545dbb5100c6c152a75135`


## Content

---
title: "Edmodo Bug Bounty Writeup"
page_title: "Edmodo Bug Bounty Writeup - Pethuraj's Blog"
url: "https://www.pethuraj.com/blog/edmodo-bug-bounty-writeup/"
final_url: "https://www.pethuraj.com/blog/edmodo-bug-bounty-writeup/"
authors: ["Pethuraj (@Pethuraj)"]
programs: ["Edmodo"]
bugs: ["XSS"]
publication_date: "2021-05-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3652
---

![Edmodo Bug Bounty writeup](https://www.pethuraj.com/blog/wp-content/uploads/2021/05/Edmodo-Bug-Bounty.png)

[XSS](https://www.pethuraj.com/blog/category/xss/)

# Edmodo Bug Bounty Writeup

[16/05/202125/05/2021](https://www.pethuraj.com/blog/edmodo-bug-bounty-writeup/) by [admin](https://www.pethuraj.com/blog/author/admin/)

I found XSS vulnerability on one of Edmodo asset and it was found to be duplicate.

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/05/edmodo1-1024x196.png)

After my report got duplicated, I decided to bypass the XSS fix and started on the same target https://snapshot.edmodo.com.

The page looked like this and it has some input fields just like a form creation website.

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/05/edmodo2-1024x620.png)

I tried the same payload which I reported earlier just to check if it’s fixed. And it is!

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/05/edmodo3-1024x123.png)

There is no popup and also I noticed the basic XSS payloads are being stripped off.

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/05/edmodo4-1024x296.png)

As you can see above screenshot, the payload didn’t execute. So I tried to understand the fix and decided to use encoded XSS payloads.

This time I used a base64 payload inside <embed> tag and it is a XSS. 

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/05/edmodo5-1024x697.png)

The payload executed and popped an XSS.

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/05/edmodo6-1024x587.png)

This payload is limited only to Firefox browser as by OWASP.

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/05/edmodo7.png)Refer to the OWASP’s XSS Filter Evasion cheatsheet for this payload – https://owasp.org/www-community/xss-filter-evasion-cheatsheet

For reporting this vulnerability, Edmodo rewarded me for this vulnerability with exciting goodies.

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/05/edmodo-mail-1024x367.png)

And after few days I received the swag pack!

![](https://www.pethuraj.com/blog/wp-content/uploads/2021/05/edmodo-swag-986x1024.jpg)

**Get in touch with me –**

<https://twitter.com/Pethuraj>  
<https://www.linkedin.com/in/pethu/>

[![](https://www.pethuraj.com/blog/wp-content/uploads/2025/01/Use-Burp-Suite-like-a-PRO-Part-2-300x150.png)](https://www.pethuraj.com/blog/how-to-use-burp-suite-like-a-pro-part-2/)

#### [How to use Burp Suite Like a PRO? PART – 2](https://www.pethuraj.com/blog/how-to-use-burp-suite-like-a-pro-part-2/)

Ready to level up your Burp Suite skills? In part 2, I've compiled some awesome tips and tricks to help ...  

[Read More](https://www.pethuraj.com/blog/how-to-use-burp-suite-like-a-pro-part-2/)

[![burp suite advanced tutorials](https://www.pethuraj.com/blog/wp-content/uploads/2022/07/Mastering-Burp-suite-300x150.png)](https://www.pethuraj.com/blog/use-burpsuite-like-a-pro-part-1/)

#### [How to use Burp Suite Like a PRO? PART – 1](https://www.pethuraj.com/blog/use-burpsuite-like-a-pro-part-1/)

This blog series is an advanced tutorial of the popular web application security and penetration testing tool Burp Suite, to help ...  

[Read More](https://www.pethuraj.com/blog/use-burpsuite-like-a-pro-part-1/)

Share on Social Media

[x](https://x.com/share?url=https://www.pethuraj.com/blog/edmodo-bug-bounty-writeup/&text=Edmodo+Bug+Bounty+Writeup)[facebook](https://www.facebook.com/sharer.php?u=https://www.pethuraj.com/blog/edmodo-bug-bounty-writeup/)[linkedin](https://www.linkedin.com/shareArticle?url=https://www.pethuraj.com/blog/edmodo-bug-bounty-writeup/&title=Edmodo+Bug+Bounty+Writeup)[email](mailto:?subject=Edmodo+Bug+Bounty+Writeup&body=https://www.pethuraj.com/blog/edmodo-bug-bounty-writeup/)[whatsapp](https://api.whatsapp.com/send?text=Edmodo+Bug+Bounty+Writeup%20https://www.pethuraj.com/blog/edmodo-bug-bounty-writeup/)

## Post navigation

[How I made to Paypal Bug Bounty $750](https://www.pethuraj.com/blog/paypal-bug-bounty-writeup/)

[Escalating XSS to Arbitrary File Read](https://www.pethuraj.com/blog/escalating-xss-to-arbitrary-file-read/)
