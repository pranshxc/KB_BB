---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-06-23_yahoo-small-business-luminate-and-the-not-so-secret-keys.md
original_filename: 2017-06-23_yahoo-small-business-luminate-and-the-not-so-secret-keys.md
title: Yahoo Small Business (Luminate) and the Not-So-Secret Keys
category: documents
detected_topics:
- ssrf
- cloud-security
- xss
- command-injection
tags:
- imported
- documents
- ssrf
- cloud-security
- xss
- command-injection
language: en
raw_sha256: 1a890946cbb7e14ef0dee62841e584a124936491c40cb0ee74ae9603c6e6d6ff
text_sha256: 00fbec626aed0ea8848b058f957064d77f2d93abbd7da916aa9af4077118e84d
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Yahoo Small Business (Luminate) and the Not-So-Secret Keys

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-06-23_yahoo-small-business-luminate-and-the-not-so-secret-keys.md
- Source Type: markdown
- Detected Topics: ssrf, cloud-security, xss, command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `1a890946cbb7e14ef0dee62841e584a124936491c40cb0ee74ae9603c6e6d6ff`
- Text SHA256: `00fbec626aed0ea8848b058f957064d77f2d93abbd7da916aa9af4077118e84d`


## Content

---
title: "Yahoo Small Business (Luminate) and the Not-So-Secret Keys"
page_title: "Yahoo Small Business (Luminate) and the Not-So-Secret Keys —  DOS"
url: "https://dos.sh/blog/2017/6/21/yahoo-small-business-luminate-and-the-not-so-secret-keys"
final_url: "https://dos.sh/blog/2017/6/21/yahoo-small-business-luminate-and-the-not-so-secret-keys"
authors: ["Tommy DeVoss / dawgyg (@thedawgyg)"]
programs: ["Yahoo! / Verizon Media"]
bugs: ["Blind SSRF"]
bounty: "9,000"
publication_date: "2017-06-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6174
---

[Tommy DeVoss](/blog?author=594aaf96b11be11541865d30)

[June 23, 2017](/blog/2017/6/21/yahoo-small-business-luminate-and-the-not-so-secret-keys)

[hacking](/blog/category/hacking), [bounty](/blog/category/bounty)

#  [Yahoo Small Business (Luminate) and the Not-So-Secret Keys](/blog/2017/6/21/yahoo-small-business-luminate-and-the-not-so-secret-keys)

[Tommy DeVoss](/blog?author=594aaf96b11be11541865d30)

[June 23, 2017](/blog/2017/6/21/yahoo-small-business-luminate-and-the-not-so-secret-keys)

[hacking](/blog/category/hacking), [bounty](/blog/category/bounty)

It's been awhile since I have written up any of the bugs I have found during my normal bug hunting, and this will be my first post for our company’s new blog. For those that do not know me, my name is Tommy, and I go by the alias “dawgyg”. I am a Unix System Admin, DevOps, and Hacker for Development Operations Security located in Richmond, Virginia. I am also a Bug Bounty Hunter in my free time. 

Over the last few weeks I have been doing the bug bounty thing with @zlz (<https://twitter.com/samwcyo>), and we have been targeting Yahoo and their various entities/properties/acquisitions. Tonight (Monday June 12th) was no exception. This ended up bringing us to their Luminate Small Business section, which allows for users to list local businesses, create websites (and host them on Yahoo servers), create stores/shops, and purchase various things such as domains etc. After spending some time looking at the 'Free' portions of the sites, we decided that it would be best if we purchased accounts to get access to more functionality to test, which we hoped would lead us to finding more issues. 

I started out by creating an account to sell things online, while @zlz decided to sign up for an account that included web hosting for us. During his checkout process, @zlz happened to notice an image being loaded on one of his pages, which seemed to be just a picture of one of the Luminate pages we had already been seeing/testing a bit. He quickly grabbed the link to the image, pasted it into our private chat on the Bug Bounty Forum Slack, and mentioned what it was doing. At this time, I had been fighting another Blind Server Side Request Forgery issue I had found with the help of @jobert (<https://twitter.com/jobertabma>) and was having no luck finding a way to exploit it in a meaningful way (Note: the blog post for that issue will be posted in the coming weeks, after it is patched and permission has been given to blog about it). 

After having no luck at the time with that SSRF, @zlz asked me to look at the endpoint he had found, as he was unable to figure out a useful way to exploit what we saw as flawed functionality. The endpoint found was: https://webshots.luminate.com/tools/site/snapshot/desktop and it contained just a single param: “url”. Upon navigating to this page, it would respond with content type of an jpeg image. But what caught our attention was the fact that the url provided in the url param would be the image 'featured' in the image. We started playing around with this for the next hour or two trying to get it to load various local IP addresses, all of which seemed to be blocked, including localhost. We also attempted to load remote svg images for potential XSS, all to no avail. After inspecting the requests that would be sent to the remote server included in the “url” param, we decided that this was making a simple GET request to the url provided, and seemed to just take a screenshot of the webpage. Stumped, we decided to call it a night, as he had to work the next morning, and I had to head to Washington DC for the annual AWS Public Sector Summit. 

Fast forward a few hours. I made it to DC for the AWS Summit, and the first talk I decided to sit in on was one titled “Securing Your AWS Account”. Now, I personally don’t really like the talks at conferences, so I generally don’t pay attention to them, and this one was no different. But, for some reason, I started listening for a couple of minutes after the introduction was done. During the opening of his talk, the speaker mentioned the AWS Meta Data IP address, which EC2 instances have access to. Then the IP address of this server flashed on the big screen. It looked familiar to me. I went back to the private chat with @jobert from the night before (he had been trying to help me find a meaningful way to exploit the Blind SSRF), and noticed that the IP address that was up on the screen in the talk was the same address that Jobert had been helping me test on. On a whim, I decided to plug in the IP and part of a path “http://169.254.169.254/latest/meta-data/" and was surprised when I was greeted with the following image:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5886dcdb03596ecad25f7563/1498065462741-4DVQT3DYA4U6ZGHAV6SU/image-asset.png)

After seeing this, I quickly changed the URL to: “http://169.254.169.254/latest/meta-data/iam/security-credentials/" and it showed that an IAM Role existed called “Ec2LeastPrivileged”, changing the path one more time to “http://169.254.169.254/latest/meta-data/iam/security-credentials/Ec2LeastPrivileged”, and I was greeted with the following:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5886dcdb03596ecad25f7563/1498226138569-KH77S14RWSU6LFSYFPG2/image-asset.png)

Game over. After discovering this, I promptly ended all testing, and filed the report to Yahoo via their Bug Bounty Program on HackerOne. The response from Yahoo was even better than expected. They had the issue triaged within an hour of reporting, had the end point taken down and the compromised Secret Keys revoked less than an hour later. Such a quick response and fix, in my opinion, shows how serious Yahoo is taking security these days, and I would like to give a huge shout out to @junot and @ftsqrl from the Yahoo Paranoids for getting this problem taken care of so quickly. I would also like to give a shout out to @jobert for his assistance in trying to exploit the Blind SSRF that ended up helping me learn enough to exploit this one fully. His blog post at <https://www.hackerone.com/blog-How-To-Server-Side-Request-Forgery-SSRF>  
is definitely a must read for anyone who wants to get more information on Server Side Request Forgery issues. 

**Timeline:**  
_06-12-2017:_ Initial discovery by @zlz, unable to exploit  
 _06-13-2017 1:30pm Eastern Time:_ Successful exploitation, compromising the IAM Secret Keys  
 _06-13-2017 1:44pm Eastern Time:_ Report submitted to Yahoo! via HackerOne  
 _06-13-2017 2:47pm Eastern Time:_ Endpoint taken down, keys rotated, HackerOne report marked as Resolved.  
_06-29-2017:_ Yahoo Awards bounty of: $9,000 

Tagged: [Bounty](/blog/tag/Bounty), [SSRF](/blog/tag/SSRF), [Privesc](/blog/tag/Privesc), [AWS](/blog/tag/AWS)
