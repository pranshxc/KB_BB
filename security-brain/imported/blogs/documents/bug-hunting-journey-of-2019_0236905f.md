---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-31_bug-hunting-journey-of-2019.md
original_filename: 2019-12-31_bug-hunting-journey-of-2019.md
title: Bug Hunting Journey of 2019
category: documents
detected_topics:
- access-control
- automation-abuse
- idor
- xss
- command-injection
- rate-limit
tags:
- imported
- documents
- access-control
- automation-abuse
- idor
- xss
- command-injection
- rate-limit
language: en
raw_sha256: 0236905ffea902b5965883a8b1c3772f89a7e96e41195e562d2589341ef1a8d9
text_sha256: a4dff0d57d0ff17c199619a08f317d2267c59966f20a3dcd5c6a13b996278ba2
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Bug Hunting Journey of 2019

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-31_bug-hunting-journey-of-2019.md
- Source Type: markdown
- Detected Topics: access-control, automation-abuse, idor, xss, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `0236905ffea902b5965883a8b1c3772f89a7e96e41195e562d2589341ef1a8d9`
- Text SHA256: `a4dff0d57d0ff17c199619a08f317d2267c59966f20a3dcd5c6a13b996278ba2`


## Content

---
title: "Bug Hunting Journey of 2019"
url: "https://medium.com/@sudhanshur705/bug-hunting-journey-of-2019-95e5190aca7c"
authors: ["Sudhanshu Rajbhar (@sudhanshur705)"]
programs: ["Alibaba", "Yahoo! / Verizon Media"]
bugs: ["XSS", "Privilege escalation", "Information disclosure"]
bounty: "2,500"
publication_date: "2019-12-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4853
scraped_via: "browseros"
---

# Bug Hunting Journey of 2019

Bug Hunting Journey of 2019
Sudhanshu Rajbhar
Follow
8 min read
·
Dec 31, 2019

794

4

Heyyy Everyoneee,

I hope you all are doing good, this year is about to end.

So I thought I should share a last writeup about some of the bugs which I have found this year.This is going to be a little long.I have been working on this for the last few days ,I hope you will like it.

I will be starting from the xss bugs which I found in a Private Program websites,I decided to look into the android apps in hope of finding some new endpoints that might be vulneable.

Here we go….

I never checked their android apps before so I decided to give it a try.I downloaded the android apps from app.evozi.com, after downloading them I used apktool to decompile them.Then I search for http/https endpoints.

You can use grep to search for strings starting with https,http.

I was suprised to see some new domains which I didn’t find earlier,tried putting the same vulnerable endpoints in which I have found xss earlier,result successful popup.

But sad, someone already reported it, 11 days ago.

You can use this tool for extracting endpoints/URLs from apk files. https://github.com/s0md3v/Diggy

s0md3v/Diggy
Diggy can extract endpoints/URLs from apk files. It saves the result into a txt file for further processing…

github.com

I didn’t knew about apktool,grep at first so I was doing it all manually. Extracting the apk file , then converting the classes.dex file into jar using dex2jar and then finally searching for http,https

Press enter or click to view image in full size

By seeing the above screenshot you could easily see that I was doing it the hard way(wrong way).Later on I started looking for an easy way and found s0md3v’s tool.

Now moving on to Verizon Media

I won’t be mentioning much more details about the bugs found in VerizonMedia program as they don’t allow disclosure of their bugs,I will be only talk about the process how I came across this bugs.

I decided to start hunting on Verizon Program, I was just crazy to find a xss in yahoo subdomain.

Fired up my burpsuite and I collected the subdomains from various subdoman enumeration tools like subfinder,assetfinder,findomain,etc . one by one I was opening the subdomains in my browser,I was monitoring them in burp (I was focused more on finding some strange looking subdomains) and also selecting all the inscope hosts and spidering them in hope of finding some more subdomains, following Jhaddix way (Checkout out his videos, if you haven’t).

I continued following the same routine,well it was so boring and tedious but still I continued looking for a xss.

One day I found a strange 3 level yahoo subdomain in Target area,I clicked on it all I can see there is only two endpoints but there were many parameters,so I started testing these parameters ,my input got reflected into the source page for eg : ‘“><shirley>
as it is,I used the payload “><img src=x onerror=alert(document.domain)> to make the xss popup.

Quickly I decided to report it.Later,saw many people getting duplicate of this report, felt sad for them :( .If I had found that xss after 1–2days I would have surely gotten duplicate too.

I had created a python script by following some blog posts from google about how to open urls from a text file one by one in browser at that time,btw there is any easy to do this ,using this addon Open Multiple URLs it’s available for both Chrome and Firefox just supply it a list of urls and it will open them in your browser all at once.

Moving on to the next bug,

I started targetting Facebook just after few days I was done with Yahoo,I have already published an article about that subdomain takeover so there isn’t much left to talk about.

If you haven’t checked it out already yet,just open the below link,I have talked about in detail how I was able to find this domain:

How Recon helped me to to find a Facebook domain takeover
Heyy Everyoneee,

medium.com

Press enter or click to view image in full size

I followed the same methodology and was able to find two more subdomain takeovers this time in a Private BugBounty Program.

Checked the whois records of some company’s owned website,compared the results and then used similar terms to find more domains.Used webscreenshot, then I started going through them to look for interesting stuffs -> found 2 unclaimed github pages.

Let’s now talk about some Privilege Escalation Bugs:

We can use some automation here with the help of Burp addons like Autorize,Autorepeater.You can follow these two links here :

Escalating Privileges like a Pro
As the description of the tool on Github says that - Autorize is an automatic authorization enforcement detection…

gauravnarwani.com

(gauravnarwani97)

Watch this video, it will guide you how to use Autorepeater and Autorize.(@stokfredrik & @Fisher)

Picked up some private programs from hackerone which have websites that have user management system where I can see they have setup different user roles, so I can check privilege escalation issues.

For a quick check,I like to start by creating a new account with no permission (absolutely nothing).Then after configuring autorize, with the inscope target.(You can checkout the above mentioned video and articles they include the steps also how to setup autorize for testing privilege escalation issues).

Login into the high Privilege user account and start going through every endpoint on that web application as much possible, and after some time looking at the autorize tab to see if it has find something.

The extension autorize automatically repeats every request with the session of the low privileged user and detects authorization vulnerabilities.
(https://portswigger.net/bappstore/f9bbac8c4acf4aefa4d7dc92a991af2f)

Get Sudhanshu Rajbhar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I was able to found 2 privsec issues in one program and 1 issue in another.One of them which was a low Privilege user was able to view the details of other users in an organization.

Screenshot of the request and response.(Private Program)

Press enter or click to view image in full size

I really like the website which have already having a check box like table in their doc, so that the users can very easily identify what all permisison a specific type of user is able to perform.

Well if there isn’t already a table like that, make it yourself it will help you while testing.

Result:Btw, Got duplicate for all three of them :(

Again back to Verizon Media

This is going to be about the information disclosure bug,basically I found an endpoint which was disclosing the public/private RSA key just like this

[privateKey] => — — — BEGIN RSA PRIVATE KEY — —

………………………Redacted………………………………

— — — END RSA PRIVATE KEY — — —

I was applying the same methodology which I used in Facebook ,in case of Facebook it was about 4k unique domains.But here in case of Verizon Media, there were f**king more than 10k+ domains just from using domain-admin@oath.com as the search term in https://tools.whoisxmlapi.com/reverse-whois-search

Another 10k+ domains if I use Oath Inc as the search term.Although I followed the same way like before,collecting all the subdomains -> screenshot.

Going through them but here if we talk about Yahoo’s site many of them redirects to Yahoo search, Will be right back…,Sorry, the page you requested was not found,etc.It’s going to take a lot of time if I followed the old way.

I was looking for some other new methodology this time,started reading recon writeups,searching on twitter.

Got to know about some of the @tomnomnom’s awesome tools-> httprobe,meg,assetfinder but still I needed to figure out how should I use them.

At first I watched

where @tomnomnom talked about his recon techniques, he mentioned about how we can use meg to find bugs Path-based xss, Open redirects,CRLF injection,CORS misconfigurations.There were some more videos also of him which I have watched you can find them on his channel and one on Nahamsec stream.

Like this one which he did with @stokfredrik

I used httprobe to resolve all the domains which I found from https://tools.whoisxmlapi.com/reverse-whois-search and saved the output to a file.

cat domains|httprobe -c 100|tee hosts

Press enter or click to view image in full size

Then with the help of sed ,removed http[s]:// part from the contents of the hosts file and used sort -u command to removed the duplicate ones pipe the output to assetfinder which will find subdomains for us and after .

cat hosts | sed ‘s/^http\(\|s\):\/\///g’\ | sort -u | assetfinder —subs-only |tee subdomains

Press enter or click to view image in full size

After i got the subdomains again used httprobe and after that I used whatweb (got to know about this tool from Nahamsec stream,Shubham Shah mentioned about it there).

WhatWeb helps in recognisesing web technologies used by a particular website,here’s the tool in action

Press enter or click to view image in full size

Using grep , I took out only those websites which were built upon PHP

cat whatweb-result|grep “PHP”

Saved all the PHP websites in one file, used webscreenshot to took screenshot of them and also made bash loop for dirsearch (for bruteforcing directories).

for i in `cat target`;do
dirsearch -u $i -e *
done;

From the screenshot, I found a website which was having blank page, I checked the source code and found few php endpoints there.Opened them,but there wasn’t anything.So I checked the dirsearch scan results for this website , interesting there was 200 ok response on /.svn/all-wcprops

Quickly opened it and I saw there many php files name with their full path.Like this there were many php endpoints.

/var/www/test.php

…………../db.php

I made a wordlist with all these php endpoints , stripping the path.Again used dirsearch on this website with this newly created wordlist.

When I opened one of this php endpoint, it was disclosing the private/public Rsa key.I quickly reported it.I wasn’t sure if it would have get accepted or not as I having a doubt if this website was in the scope or not.

It was fixed within 1–2 days they shutdown the website, and turns out that the website was ou of scope but still I was awarded with a bounty of $2500, which is really great of them.

For dirbruteforcing I have switched to ffuf now,give it a try you will love it :)

Thankyou so much,if you have read it till the end really appreciated your time.Godluck for 2020 :)

Sya Everyonee!!!
