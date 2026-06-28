---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-31_how-reading-robotstxt-file-got-me-4-xss-reports-.md
original_filename: 2022-08-31_how-reading-robotstxt-file-got-me-4-xss-reports-.md
title: How reading robots.txt file got me 4 XSS reports ?
category: documents
detected_topics:
- idor
- xss
- command-injection
- rate-limit
- automation-abuse
- api-security
tags:
- imported
- documents
- idor
- xss
- command-injection
- rate-limit
- automation-abuse
- api-security
language: en
raw_sha256: a89482034a215c00239c8110ad7781f7e335e02033fc5756605e376cdc38ac98
text_sha256: b849bc4ea4ba02fb37115538dd57a05c881d4d493a67f397f957e18ef73057a5
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# How reading robots.txt file got me 4 XSS reports ?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-31_how-reading-robotstxt-file-got-me-4-xss-reports-.md
- Source Type: markdown
- Detected Topics: idor, xss, command-injection, rate-limit, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `a89482034a215c00239c8110ad7781f7e335e02033fc5756605e376cdc38ac98`
- Text SHA256: `b849bc4ea4ba02fb37115538dd57a05c881d4d493a67f397f957e18ef73057a5`


## Content

---
title: "How reading robots.txt file got me 4 XSS reports ?"
url: "https://c0nqr0r.medium.com/reading-robots-txt-got-me-4-xss-reports-9fd2234c635f"
authors: ["Ahmed Qaramany (@c0nqr0r)"]
bugs: ["XSS"]
publication_date: "2022-08-31"
added_date: "2022-10-06"
source: "pentester.land/writeups.json"
original_index: 2234
scraped_via: "browseros"
---

# How reading robots.txt file got me 4 XSS reports ?

Ahmed Qaramany
 highlighted

How reading robots.txt file got me 4 XSS reports ?
Ahmed Qaramany
Follow
4 min read
·
Aug 31, 2022

1.5K

10

Hello mates,
Back again with new writeup, I hope it will be useful for you Inshallah , In this write-up, I’m gonna share with you how I was able to score more than 5 XSS
at old program private 2019 using recon,

At first I’m not Full-Time Bounty Hunter until now I hunt when I feel excited to hack or search specific kind of bugs and As you know I’m a top fan of recon so let’s start

Scope :

As usual, All people start doing recon when they see *.domain.com or any wide scope, but in my case the scope was 10 or 8 subdomains and not all of them are belongs to one domain there are some different TLDs and domains, so we can’t do any subdomain enumeration here!

Hands on :

I tested some functions as a normal user like login and register and tried to see is there any function to play around but couldn’t find anything interesting so there is only one solution, you can do recon process to collect some data like : Endpoints, JS files, Parameters, Links from web archive and any notes that may help me when I came back to the functions to test it again with my recon data

Recon :

First : Start doing Google Dorking to see if there anything [Found Nothing] Second : Searched for the domain name at Wayback archive [Found Nothing] Third : Opened robots.txt file to see what the developer hide from us, let’s analyze it

Here I found /admin but it redirects to /admin/login.asp [302] so I start with it first because other directories not redirecting us to any .asp endpoint

So what I did is to

Open source code > Search for any secrets or endpoints > [Found Nothing]

Open JS files > Use any tool like gospider or Jsscanner to extract secrets and Endpoints from it or manual analyzing too > [Found Nothing]

Hmmmmm Let’s FUZZ ?

ffuf -u https://sub.domain.com/admin/FUZZ -w aspfiles.txt -mc 200

you can find this list at Github SecLists repository.

Get Ahmed Qaramany’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Came across this page but look like to be static it’s only HTML and CSS buttons are not working!

But source code is working HAHA, let’s analyze it so after reading JS files and HTML source code I found this interesting endpoint

Press enter or click to view image in full size

So fastly I changed the endpoint to https://sub.domain.com/admin/colorpicker_IEPatch.asp

Press enter or click to view image in full size

Nothing take action when I Click to the colors ! Click all the buttons !

Nothing working, I Hate Bug Bounty!

Now I hope I can find parameters that maybe keeps me interact with the server or the client side, so I can insert data to it and see how it works, I left Arjun tool working at this endpoint at the background and during this time I looked for JS files and source code again

Open JS files > Use any tool like gospider or Jsscanner to extract secrets and Endpoints from it or manual analyzing too > [Found Nothing]

Open source code > Search for any secrets or endpoints > [Found somthing]

At same time Arjun got me this from the source code so now we are sure that It reflects data at the body of the page source code

arjun -u https://sub.domain.com/admin/colorpicker_IEPatch.asp
Press enter or click to view image in full size

If you typed “>qaramany< at any parameter it will be reflected inside the script tag and the characters >< reflects without filtering
so lets close the script tag and insert new tag to run our Alert

Payload :

</script><img src=x onerror=alert(document.cookie)>

Now I got first XSS, With same steps I used other scope subdomains to got the other 4 XSS,

It starts from something alot of people don’t care about which is robots.txt, Tested the same directory which is /admin and find that developer forgot to remove it , This developer is great and lazy xD I tested the other 4 subdomains and found they are all vulnerable to XSS too

See you soon guys hope you enjoyed this writeup,

Don’t forget to follow me on Twitter c0nqr0r

Thanks For Reading
