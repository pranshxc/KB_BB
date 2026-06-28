---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-09_my-first-bug-a-unique-500-xss.md
original_filename: 2023-06-09_my-first-bug-a-unique-500-xss.md
title: 'My First Bug: A Unique $500 XSS.'
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: 346513e9f8e95277e7ec5c821b40390f70ee42b0874f97e99bc7d492ef6f612b
text_sha256: 17d8673dd2dcd787e9c1b4cbf881eaa8f90b1f95e94f637067f85bcdc74b7979
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# My First Bug: A Unique $500 XSS.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-09_my-first-bug-a-unique-500-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `346513e9f8e95277e7ec5c821b40390f70ee42b0874f97e99bc7d492ef6f612b`
- Text SHA256: `17d8673dd2dcd787e9c1b4cbf881eaa8f90b1f95e94f637067f85bcdc74b7979`


## Content

---
title: "My First Bug: A Unique $500 XSS."
url: "https://medium.com/@f3tch/my-first-bug-a-unique-500-xss-eb5caccb628f"
authors: ["f3tch"]
bugs: ["XSS"]
bounty: "$750"
publication_date: "2023-06-09"
added_date: "2023-06-12"
source: "pentester.land/writeups.json"
original_index: 1064
scraped_via: "browseros"
---

# My First Bug: A Unique $500 XSS.

f3tch
 highlighted

f3tch
 highlighted

f3tch
 highlighted

My First Bug: A Unique $500 XSS.
f3tch
Follow
4 min read
·
Jun 8, 2023

747

9

whoami

Hi, my name is ### ###. I am 14 years old and started bug bounty when I was 13. My brother is a bugbounty hunter for almost 5 years on bugcrowd, he is my motivation and taught me everything security researching or bugbounty, After 7 months of hard work and dedication, I have finally gotten my first bug paid too, on a private program on a collaboration with my brother. Hope you will enjoy reading my finding.

Press enter or click to view image in full size
Photo by Arget on Unsplash
cat vulnerability

One evening after taking a shower, I thought let’s try to find a bug for real now. I opened BurpSuite, turned on some music, and opened a private program’s main domain, which we will call www.target.com. I logged into my testing account, clicked just one button, “Add to Cart”, and intercepted the request using Burp Proxy. I checked Burp history, and before the Add to Cart actual request, there was another POST request that was being made through api.target.com. I sent the request to the repeater and inspected it, there was some URL Encoded JSON data inside a parameter named param. Basically, the request was bringing some known data about the product that I was adding to the cart. I noticed some data was reflected in the response. The response was in JSON, but the Content-Type was set to HTML!!! As I’m pretty dumb, I thought the JSON data was inside a script tag, which it wasn’t. I tried exiting the JSON data in response which did not work. Later when I finally realized, that the JSON data was printed straight to HTML document without any tags, I tried adding <h1> tag, and to my surprise, it worked!!!

The <h1> tag was reflected in the response body just as expected, after running it in the browser it was confirmed that an XSS was possible. But this XSS wasn’t as simple. I noticed api.target.com is only accessible if the referer header is set to any subdomain/domain of target.com, plus, because of it being POST-Based Reflected XSS, I had to send a request to that endpoint using a website owned by me, but Origin header would have blocked any request from other domains. This seemed like a big problem, but I had a trick up my sleeve. I had an idea, I first checked if I could change the POST request to GET request, and thankfully it worked! Even with GET request, the <h1> tag was reflected! Now I went to https://account.target.com/login?redirect=https://account.target.com/home and put the vulnerable link in the redirect parameter! The link looked like something like https://account.target.com/login?redirect=https://api.target.com/file?param={"data":"<h1>"} Now, once I logged in to my account, account.target.com would redirect me to https://api.target.com/file?param={"data":"<h1>"} with the referer header and origin header both set to account.target.com, allowing the victim to enter the vulnerable link!

Get f3tch’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

cat WAF_Bypass

Entering a <script> tag would be blocked by the WAF, so I tried bypassing the WAF in order to achieve a full-blown Reflected XSS. After about 6 hours of bypassing, I came up with a payload <input+type=text+onbeforeinput=location=’https://asd.com'><!-- which, I don’t think would ever have been triaged if I reported that. Once the HTML code loads, the victim would have to enter any data in a form, and they would have been redirected to https://asd.com.

I could not find a WAF and asked my real brother for collaboration (he is a much better hacker than me, top 500 in the world and top 50 in my country), and he accepted to collaborate. I sent all the details and information I had gathered yet, and BOOM! Within 2 hours he found the bypass!!! The payload looked like <%s%v%g+%on%l%oad%=c%o%nf%i%rm%(1%)><!--! I had achieved a valid XSS most likely to be triaged because of all the bypasses. The final link looked like: https://account.target.com/login?redirect=https://api.target.com/file?param={"data":"<%s%v%g+%on%l%oad%=c%o%nf%i%rm%(1%)><!--"}.

exit

After the report was done, in just a day, the report got triaged, and the bounty was rewarded after about 5 days of it being triaged. This was my first bug and after so much hard work I had finally achieved something in my life! The total payment was $750, and with division between me and my brother, I was awarded $500.

Press enter or click to view image in full size

Thanks for reading till the end! I hope you learned something.
