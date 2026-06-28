---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-30_how-to-find-access-admin-panel-by-digging-into-js-files.md
original_filename: 2022-05-30_how-to-find-access-admin-panel-by-digging-into-js-files.md
title: How to find & access Admin Panel by digging into JS files…🥰
category: documents
detected_topics:
- xss
- command-injection
- rate-limit
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- rate-limit
- automation-abuse
language: en
raw_sha256: b45fe6cfd70ae29def1ad29945316273b66b4926bdda52645794b77e03c915c0
text_sha256: c3dd01899c1668a0a8838892ca60fcf08f4881b37d8417af0e93c49f69766066
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# How to find & access Admin Panel by digging into JS files…🥰

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-30_how-to-find-access-admin-panel-by-digging-into-js-files.md
- Source Type: markdown
- Detected Topics: xss, command-injection, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `b45fe6cfd70ae29def1ad29945316273b66b4926bdda52645794b77e03c915c0`
- Text SHA256: `c3dd01899c1668a0a8838892ca60fcf08f4881b37d8417af0e93c49f69766066`


## Content

---
title: "How to find & access Admin Panel by digging into JS files…🥰"
url: "https://medium.com/@ratnadip1998/how-to-find-access-admin-panel-by-digging-into-js-files-282d89391a2d"
authors: ["Ratnadip Gajbhiye (@scspcommunity)"]
bugs: ["Weak credentials", "WAF bypass"]
publication_date: "2022-05-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2595
scraped_via: "browseros"
---

# How to find & access Admin Panel by digging into JS files…🥰

Top highlight

How to find & access Admin Panel by digging into JS files…🥰
Ratnadip Gajbhiye
Follow
3 min read
·
May 30, 2022

803

11

Hello All,🙂

I’m back again with a new write-up…Again this article is about Admin Panel Access…( This is my 5th write-up on Admin Access more on the way…)😄

Few days ago I got an invite on hackerone for a private program.🤔

Consider the company name as “target.com”.

I checked the resolved reports of the program and noticed that 100+ reports have been resolved till now.🙁

Then I decided to not test for common issues like XSS, CRLF, Header Injection etc.😌

I ran wayback urls, gau, & OTX on “target.com” and grabbed all the JS URLs..
I found thousands of URLs, the main thing is to filter live URLs.

I used the “fff” tool for filtering live URLs (Available on Github).😍

Command I used :
cat jslist.txt | fff | grep 200 | cut -d “ “ -f1 | tee livejs.txt

It will give you only a live URL.
After filtering the live URL, I have a total 300+ live JS URLs.

There are 300+ URLs, not all the URLs are useful.

I again filter the URLs using grep method :
cat livejs.txt | grep dev
cat livejs.txt | grep app
cat livejs.txt | grep static
etc.

Using the above cmnd you’ll get only those URLs which contain “dev”,”app” & “static” etc. words in the url path.
Eg. In my case vulnerable URL was : https://target.com/static/js/main.235e6842.chunk.js. 🤨

Again I used a tool called “Nemesis” (https://github.com/machinexa2/Nemesis).♥️
Nemesis is a good tool for recon, vulnerabilities, secrets and more! .♥️

Command I used.
nemesis -u https://target.com/static/js/main.235e6842.chunk.js -e

It will give me results bunch of information and some HTTPS & HTTP URLs.

I manually open all the URLs on the browser and one URL has a login page. (https://stagging-dev.target.com)🤨

I tried all the things: redirect bypass, force browsing, SQL bypass, default credentials brute-force etc. but nothing worked.😀

Get Ratnadip Gajbhiye’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When I try to brute-force the admin panel my IP gets blocked by cloud-flare.😂

Then I copied that URL and pasted it into my notepad. After some time later my IP gets unblocked.🤪

I tried to find the origin IP behind cloud-flare. I started Shodan search, Censys search etc after that I got the IP address for a particular website. (20.xxx.xxx.x8)😎

Still I’m not sure that IP address belongs to same organization then I open https://20.xxx.xxx.x8 in browser and it gives me error :

Websites prove their identity via certificates. Firefox does not trust this site because it uses a certificate that is not valid for 20.xxx.xxx.x8. The certificate is only valid for the following names: *.target.com, target.com. 🥳

The above error confirms that the IP address belongs to the same organization.😋

I opened https://20.xxx.xxx.x8 on Firefox and clicked on the “Accept the risk and continue” button.

The IP address redirects me to Admin Panel but this time it was “Barracuda system Panel”😉

https://20.xxx.xxx.x8/cgi-mod/index.cgi?locale=en_US

I entered “admin” in both fields and clicked on the login button.😂

I get access to the admin panel. 😎♥️

Press enter or click to view image in full size

In the meantime I didn’t dig more into the panel.

I make a video POC and submit it to the program. The hackerone team triaged the report and updated the severity High 8.3 within an hour.🔥

Reported > Fixed within days > Points…🤩

Always dig more and Never lose your hope..🙂 Make every effort to bypass the login panel..🔥

I hope you enjoyed this article and I apologize for my weak English if there are any mistakes in this post.😅

Thanks for reading my article.😁
Have a great day…🙂
