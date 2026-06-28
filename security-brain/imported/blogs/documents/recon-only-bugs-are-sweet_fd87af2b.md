---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-05_recon-only-bugs-are-sweet.md
original_filename: 2023-07-05_recon-only-bugs-are-sweet.md
title: Recon only bugs are sweet!
category: documents
detected_topics:
- xss
- rate-limit
- idor
- ssrf
- command-injection
- otp
tags:
- imported
- documents
- xss
- rate-limit
- idor
- ssrf
- command-injection
- otp
language: en
raw_sha256: fd87af2b23a8ad9c586f7c61b1e8263777cec8b9f69e1210f8ed64ec016e744e
text_sha256: fea8454509f2b6eb523f9e04ea6345a97ca75d442d2fd7060c3762647dd791b9
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Recon only bugs are sweet!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-05_recon-only-bugs-are-sweet.md
- Source Type: markdown
- Detected Topics: xss, rate-limit, idor, ssrf, command-injection, otp
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `fd87af2b23a8ad9c586f7c61b1e8263777cec8b9f69e1210f8ed64ec016e744e`
- Text SHA256: `fea8454509f2b6eb523f9e04ea6345a97ca75d442d2fd7060c3762647dd791b9`


## Content

---
title: "Recon only bugs are sweet!"
page_title: "Recon only  bugs are sweet! – Hazem's Blog"
url: "https://hazemhussien99.wordpress.com/2023/07/05/recon-only-bugs-are-sweet/"
final_url: "https://hazemhussien99.wordpress.com/2023/07/05/recon-only-bugs-are-sweet/"
authors: ["Hazem Hussien (@_bughunter)"]
bugs: ["Information disclosure", "Local file disclosure (LFD)", "Stored XSS", "Self-XSS", "vHost misconfiguration"]
publication_date: "2023-07-05"
added_date: "2023-07-24"
source: "pentester.land/writeups.json"
original_index: 964
---

* * *

Jul 5

## Recon only bugs are sweet!

![](https://hazemhussien99.wordpress.com/wp-content/uploads/2023/07/thumb.png?w=1024)

**Sections** :  
– Introduction  
– Bug #1: Log files exposing authentication tokens.  
– Bug #2: Exposed directory leaking source code.  
– Bug #3: Stored XSS in a forum website.  
– Bug #4: Self XSS in Shopify.  
– Bug #5: Accessing internal network via vhost.  
– Conclusion.

**Introduction**  
Hello! My name is Hazem Hussien, I’m a bug hunter and a security enthusiast from Egypt, This is going to be my first writeup, it’s a very short and simple writeup about a few recon only bugs that i found while bug hunting.

What are “Recon Only” bugs ?  
They are security vulnerabilities that are found without much manual exploitation and could be found using reconnaissance techniques such as dorking or directory brute forcing on an http web server (i just made that definition up :), this is just the way i see them and obviously not an official technical term).  
Let’s call our target target.com.

**Bug #1: Log files exposing authentication tokens.**  
After the usual subdomain enumeration and probing, i noticed a subdomain that the following name  
static01.target.com  
it doesn’t look too interesting since it has the word static in its name which probably means static files like html and css, but i know that some times static files could contain interesting data like pdf files (could contain some sort of PII ) or log files (could contain secret keys/tokens/endpoints) so i tried google dorking using that domain to see if i find anything.
  
  
  Google dorking tip, if you see an interesting subdomain, don't be afraid to query it by itself in google :)  
  for example, site:interesting.subdomain.com ext:txt  
  What i noticed while dorking is that if you use the following dork:  
  site:*.target.com  
  it won't actually show all the results, but if you do it this way:  
  site:static01.target.com  
  It will show you results that didn't show up in the earlier dork, don't understand why that happens exactly maybe its fixed now but thought of sharing this anyways.

and upon dorking i see the following endpoint the first few results the following url

<a href="[https://static01.targetcom/<redacted>/data/https://static01.targetcom/<redacted>/data/<company_name>/2017/10/04/150708633422569163.txt](https://static01.targetcom/<redacted>/data/https://static01.targetcom/<redacted>/data/<company_name>/2017/10/04/150708633422569163.txt)

they look like log files cause of the full date used as the directory and upon opening them  
and upon seeing them i see hundreds of log entried, some entries contained data of the following manner:
  
  
  2018-06-03 10:27:40.490, <D>D, <T>REDACTEDMainActivty, <M>initUserLoginStatus -- user has logged in, mAuth = <redacted_auth_token>, mSaltKey = <redacted>

I tried exploiting using these keys as cookies to subdomains that are meant for employees only and many other attempts but none worked, decided to just report as it and it was triaged as medium.

![](https://hazemhussien99.wordpress.com/wp-content/uploads/2023/07/medium-1.png?w=404)

**Bug #2: Exposed directory leaking source code.**  
After the usual subdomain enumeration and probing, I thought of running waybackurls on my domains and see if i can get any interesting endpoints, Found boring endpoint called /shop/ on a boring looking subdomain <https://dsfs.target.com/>, I haven’t had much success of brute forcing the ones i thought interesting, so i thought of bruteforcing the boring looking ones, upon bruteforcing, I found multiple php files leaked and configuration files like web.config and .htaccess

Note: when i say interesting subdomains i mean subdomains have interesting words in them like internal,admin,proxy,config or using software that could be vulnerable like grafana.target.com or jenkins.target.com and by boring subdomains i mean subdomains which host static files most of the time or

These were some of the endpoints found if you wanna add them to your wordlist (i recommend adding the files names only :))
  
  
  /[shop/.htaccess](https://dsfs.target.com/shop/.htaccess)
  [/shop/web.config](https://dsfs.target.com/shop/web.config)
  [/shop/adver.php](https://dsfs.target.com/shop/adver.php)
  /[shop/date.php](https://dsfs.target.com/shop/date.php)

This is called Local File Disclosure (LFD for short) and should be usually triaged as medium/high depending on the information leaked, I reported it right away but it was triaged as low because according to the triager, even though i could download backend PHP files, the files didn’t leak much sensitive info so it was treated as low.

**Bug #3: Stored XSS in a forum website.**  
After the usual subdomain enumeration and probing, i thought of grabbing the HTML titles of the gathered hosts, httpx is great for this, as an example:
  
  
  cat host.txt | httpx -silent -nc -title | tee -a httpxOutput.txt

One host had the word “php” in the title, looked very interesting.  
I opened it in the browser & the website’s language was chinese but i managed to translate the button names & titles from Google Translate, turned out it was a forum site.  
I managed to create an account in seconds and thought of testing the main feature of the whole forum (to actually post forum posts ) and voila!

![](https://hazemhussien99.wordpress.com/wp-content/uploads/2023/07/forum.png?w=1024)

i think i took it a bit too far with redacting but i can’t read chinese so i don’t know which info should be redacted so sorry about that 😀

Payload used: 
  
  
  "><img src=x onerror=prompt`1`>

Sadly it was a duplicate, It was reported by someone else 4 days before my submission.

**Bug #4: Self XSS in Shopify**

Many companies don’t accept this bug, but since Shopify accepts it and pays for it, i have no problems reporting it.  
Turns out reading old reports is considered doing recon as well :), came across this H1 report <https://hackerone.com/reports/1441988> , and tried bypassing the protections in place.  
Unfortunately, i wasn’t able to bypass the protections in place, but i found a simple self XSS in the same field, didn’t think of a way to exploit it further, so just decided to report it.  
Luckily it was accepted, you can see the disclosed report here.  
<https://hackerone.com/reports/1591403>

**Bug #5: Accessing internal network via vhost.**  
This is a very straight forward bug, after the usual subdomain enumeration and probing, i found an interesting subdomain, call it redacted.target.net

Doing a directory brute force on it didn’t yield much results, but i thought about doing a vhost brute force on it, and i got lucky 🙂  
Note: doing a vhost brute force on a website is as easy as running the following command using ffuf
  
  
  ffuf -u <https://target.com/> -H “Host: FUZZ” -w /home/user/path/to/vhost/wordlist.txt -fs <regular_content_length>

Checkout Ffuf’s readme for more details <https://github.com/ffuf/ffuf>

When using 127.0.0.1 in the Host header, it allowed me to access the internal network and i could see the tomcat page installed internally

![](https://hazemhussien99.wordpress.com/wp-content/uploads/2023/07/tomcat.png?w=747)

The obvious way to go on from here is to set the host header to 127.0.0.1 and start forcing for endpoints, the following is a command that does just that:
  
  
  ffuf -u [https://target.com/](https://target.com/endpoint/)FUZZ -H “Host: 127.0.0.1” -w /home/user/path/to/wordlist.txt -fs <regular_content_length>

but since this was a public VDP, I didn’t bother with further exploitation really & just reported it right away and it was accepted.

## Conclusion

A few words i wanted to say before ending this writeup, all these bugs were found on public bug bounty programs that have been public for years/months, so don’t think just because a program is public and old that it won’t have bugs on it, these bugs were really simple and found via very basic recon techniques, I still hope you learned something from my writeup.

if you would like to collaborate feel free to ping me on twitter, I run a twitter account where i post bug bounty tips here & there so feel free to DM me on it @[_bughunter](https://twitter.com/_bughunter).

I intend on publishing more writeups on my blog so if you have any suggestions on improving them i would be happy to hear :).

### Share this:

  * [ Share on X (Opens in new window) X ](https://hazemhussien99.wordpress.com/2023/07/05/recon-only-bugs-are-sweet/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://hazemhussien99.wordpress.com/2023/07/05/recon-only-bugs-are-sweet/?share=facebook)
  * 

Like Loading…

By:

Hazem Hussien

Posted in:

* * *

### Leave a comment [Cancel reply](/2023/07/05/recon-only-bugs-are-sweet/#respond)

Δ
