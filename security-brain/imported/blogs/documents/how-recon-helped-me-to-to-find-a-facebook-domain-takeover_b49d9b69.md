---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-17_how-recon-helped-me-to-to-find-a-facebook-domain-takeover.md
original_filename: 2019-07-17_how-recon-helped-me-to-to-find-a-facebook-domain-takeover.md
title: How Recon helped me to to find a Facebook domain takeover
category: documents
detected_topics:
- command-injection
- automation-abuse
tags:
- imported
- documents
- command-injection
- automation-abuse
language: en
raw_sha256: b49d9b69469b5b57d5e991c388b50e7571fc9deb2562e8009467cb000d33212e
text_sha256: c913a52122dde4b817b89d5382bde3001f81c92b9b41509b3c934590adcc7f2f
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# How Recon helped me to to find a Facebook domain takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-17_how-recon-helped-me-to-to-find-a-facebook-domain-takeover.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `b49d9b69469b5b57d5e991c388b50e7571fc9deb2562e8009467cb000d33212e`
- Text SHA256: `c913a52122dde4b817b89d5382bde3001f81c92b9b41509b3c934590adcc7f2f`


## Content

---
title: "How Recon helped me to to find a Facebook domain takeover"
url: "https://medium.com/@sudhanshur705/how-recon-helped-me-to-to-find-a-facebook-domain-takeover-58163de0e7d5"
authors: ["Sudhanshu Rajbhar (@sudhanshur705)"]
programs: ["Meta / Facebook"]
bugs: ["Subdomain takeover"]
bounty: "500"
publication_date: "2019-07-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5141
scraped_via: "browseros"
---

# How Recon helped me to to find a Facebook domain takeover

How Recon helped me to to find a Facebook domain takeover
Sudhanshu Rajbhar
Follow
4 min read
·
Jul 17, 2019

1.4K

5

Heyy Everyoneee,

Hope you all are doing good.In this writeup I am going to tell you how I was able to takeover a domain which was owned by Facebook.

Short Story

After my final exams got over,I setup some goals in which fb hof was one of them.Had to go through some N/As and informative reports.But finally I did it.

Here we Go ,

So if you go to https://www.facebook.com/whitehat/info/ you will find that their acquisitions ,partnerships are also inscope of their program.You can say that everything which they own is in scope excluding few domains only.So without wasting time I started collecting the domains which are owned by Facebook.

What’s the best way to find all the domains which are owned by a particular company ?

@0xpatrik has already written an article about it https://0xpatrik.com/asset-discovery/

Before you move ahead I recommend you to read his article.

Horizontal domain correlation:

Let’s start by checking the whois result of facebook.com

whois facebook.com

Look at the Registrant email it’s domain@fb.com you can use this email to find all the other sites which have the same registrant email as facebook.com

For reverse WHOIS I found this site https://tools.whoisxmlapi.com/reverse-whois-search really helpful. Or else you can use https://viewdns.info but there the results are limited and also tools like domlink or amass can be used for horizontal domain correlation as mentioned by @0xpatrik in his article.

Just go to https://tools.whoisxmlapi.com/reverse-whois-search and in the search field,enter the email.

Press enter or click to view image in full size
https://tools.whoisxmlapi.com/reverse-whois-search (domain@fb.com)

We got around 2,756 unique domains which all have “domain@fb.com” in their whois scan result.

Now just don’t get stop here, we can still get some more domains last time we used the Registrant email , now this time we will use the Registrant Name and let’s see the difference now.

Press enter or click to view image in full size
https://tools.whoisxmlapi.com/reverse-whois-search (Facebook, Inc)

Cool this time we get more domains than before around 3,441.

Get Sudhanshu Rajbhar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now let’s remove the duplicate ones.Save all this in one file.Then

sort filename | uniq |tee outputFileName

Press enter or click to view image in full size

So finally we have around 4k unique domains, which have either Facebook Inc or domain@fb.com in their whois scan result.You can still get some more domains use something else this time other than registrant email or name which you found common in the already collected domains.

After I collected all the domains , I used filter-resolved tool by @tomnomnom, to resolve all the domains.

cat fb2.txt | ~/tools/filter-resolved |tee live-domains.txt

Then I used subfinder, to find all the subdomains of the domains which were in live-domains.txt file.

subfinder -dL live-domains.txt -o subdomains.txt

Repeating the same process again, use filter-resolved for resolving all the subdomains which we found using subfinder.

Moving towards the last step, I used webscreenshot for taking screenshots of the subdomains.

And while going through the screenshots I found this domain www.buckbuild.com

Press enter or click to view image in full size

Followed this article : https://0xpatrik.com/takeover-proofs/

Then I uploaded something to verify the takeover was successful or not.And yeah!! here we go ,found my first subdomain takeover.

Press enter or click to view image in full size

POC time:

Press enter or click to view image in full size

Timeline:
July. 08— Initial Report
July 11— Report Triaged
July 12 — Fixed
July. 17— Bounty awarded $500

Press enter or click to view image in full size

Thankyou for reading it till the end.I hope you enjoyed reading it.

Well one thing which I want to share is after the screenshot part was done, I didn’t bother to look at them as they were all looking same ,I was like there’s no point in going through them other hunters might have already looked at those domains, so I left it.Then after a 2–3days again I looked at it and you all know what happened next.

Guys believe in yourself don’t feel like you will not find anything just because others are also looking at the same thing so your chance is less of finding something there.

Sya Everyoneeeee
