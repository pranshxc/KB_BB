---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-23_cookie-tossing-to-rce-on-google-cloud-jupyterlab.md
original_filename: 2020-12-23_cookie-tossing-to-rce-on-google-cloud-jupyterlab.md
title: Cookie Tossing to RCE on Google Cloud JupyterLab
category: documents
detected_topics:
- csrf
- supply-chain
- sso
- xss
- command-injection
- otp
tags:
- imported
- documents
- csrf
- supply-chain
- sso
- xss
- command-injection
- otp
language: en
raw_sha256: 9f2ab453fab19fb38cdff91c76e086e3b117222f5600f619783b8dbf40043dfd
text_sha256: bd0b5c1e49f27712ed60cb907a98a5a2090278bd1f23eada0153501dfdee4c67
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Cookie Tossing to RCE on Google Cloud JupyterLab

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-23_cookie-tossing-to-rce-on-google-cloud-jupyterlab.md
- Source Type: markdown
- Detected Topics: csrf, supply-chain, sso, xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `9f2ab453fab19fb38cdff91c76e086e3b117222f5600f619783b8dbf40043dfd`
- Text SHA256: `bd0b5c1e49f27712ed60cb907a98a5a2090278bd1f23eada0153501dfdee4c67`


## Content

---
title: "Cookie Tossing to RCE on Google Cloud JupyterLab"
page_title: "s1r1us - Cookie Tossing to RCE on Google Cloud Jupyter Notebooks"
url: "https://blog.s1r1us.ninja/research/cookie-tossing-to-rce-on-google-cloud-jupyter-notebooks"
final_url: "https://blog.s1r1us.ninja/research/cookie-tossing-to-rce-on-google-cloud-jupyter-notebooks"
authors: ["s1r1us (@s1r1u5_)"]
programs: ["Google"]
bugs: ["Self-XSS", "DoS", "CSRF", "RCE"]
bounty: "3,133.70"
publication_date: "2020-12-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4053
---

Search this site

Embedded Files

Skip to main content

Skip to navigation

[![](https://lh3.googleusercontent.com/sitesv/AA5AbUAJUoHWRZiKEdP05iYyPnqXAQ5ZPd2fimKsXHzCDVgJb17nrqNY2PQWPswywcMCprwl6Y2J7DJSm4KKVhz61L686w2-vMLY5HSLSWOY1zlCJqIZ8O4u23P4jQXYSJ1D2McOgs0J4rN0BbCQyns39yO0fWO5RXeyy9wVcLgDkExHKWjTNYuWgS6pMJP2Cqc=w16383)](/home)[s1r1us](/home)

  * [Home](/home)

  * [Questions](/questions)

  * [why much of science progress happened in west?](/questions/why-much-of-science-progress-happened-in-west)

  * [my curse of curiosity and the problem of choice](/questions/my-curse-of-curiosity-and-the-problem-of-choice)

  * [Books](/books)

  * [Advisories](/advisories)

  * [CTF](/CTF)

  * [BountyCon 2020](/CTF/bountycon2020)

  * [H1-2006-CTF](/CTF/h1-2006-ctf)

  * [Hack.lu](/CTF/hack-lu)

  * [Facebook CTF'19 writeup](/CTF/facebook-ctf19-writeup)

  * [CSAW'19 CTF](/CTF/csaw19-ctf)

  * [tangled_browsers](/CTF/tangled_browsers)

  * [ByteBandits CTF 2020](/CTF/bytebandits-ctf-2020)

  * [Google CTF - 2020](/CTF/IuseBing)

  * [zer0ptsCTF2021-challenges](/CTF/zer0ptsctf2021-challenges)

  * [site-isolation](/CTF/site-isolation)

  * [BsidesAHM2021](/CTF/bsidesahm2021)

  * [Research](/research)

  * [Cookie Tossing to RCE on Google Cloud Jupyter Notebooks](/research/cookie-tossing-to-rce-on-google-cloud-jupyter-notebooks)

  * [test'>">test{{7*7}}](/research/testtest77)

  * [Prototype Pollution](/research/PP)

  * [BrokenConflu](/research/brokenconflu)

  * [Why should we follow spec?](/research/why-should-we-follow-spec)

  * [cve-2021-21224-v8-rce-rca](/research/cve-2021-21224-v8-rce-rca)

  * [About Me](/about-me)

  * [Looking Back Looking Forward: 2021](/about-me/Looking-Back-Looking-Forward)

  * [Inspiration](/inspiration)

[![](https://lh3.googleusercontent.com/sitesv/AA5AbUAJUoHWRZiKEdP05iYyPnqXAQ5ZPd2fimKsXHzCDVgJb17nrqNY2PQWPswywcMCprwl6Y2J7DJSm4KKVhz61L686w2-vMLY5HSLSWOY1zlCJqIZ8O4u23P4jQXYSJ1D2McOgs0J4rN0BbCQyns39yO0fWO5RXeyy9wVcLgDkExHKWjTNYuWgS6pMJP2Cqc=w16383)s1r1us](/home)

  * [Home](/home)

  * [Questions](/questions)

  * [why much of science progress happened in west?](/questions/why-much-of-science-progress-happened-in-west)

  * [my curse of curiosity and the problem of choice](/questions/my-curse-of-curiosity-and-the-problem-of-choice)

  * [Books](/books)

  * [Advisories](/advisories)

  * [CTF](/CTF)

  * [BountyCon 2020](/CTF/bountycon2020)

  * [H1-2006-CTF](/CTF/h1-2006-ctf)

  * [Hack.lu](/CTF/hack-lu)

  * [Facebook CTF'19 writeup](/CTF/facebook-ctf19-writeup)

  * [CSAW'19 CTF](/CTF/csaw19-ctf)

  * [tangled_browsers](/CTF/tangled_browsers)

  * [ByteBandits CTF 2020](/CTF/bytebandits-ctf-2020)

  * [Google CTF - 2020](/CTF/IuseBing)

  * [zer0ptsCTF2021-challenges](/CTF/zer0ptsctf2021-challenges)

  * [site-isolation](/CTF/site-isolation)

  * [BsidesAHM2021](/CTF/bsidesahm2021)

  * [Research](/research)

  * [Cookie Tossing to RCE on Google Cloud Jupyter Notebooks](/research/cookie-tossing-to-rce-on-google-cloud-jupyter-notebooks)

  * [test'>">test{{7*7}}](/research/testtest77)

  * [Prototype Pollution](/research/PP)

  * [BrokenConflu](/research/brokenconflu)

  * [Why should we follow spec?](/research/why-should-we-follow-spec)

  * [cve-2021-21224-v8-rce-rca](/research/cve-2021-21224-v8-rce-rca)

  * [About Me](/about-me)

  * [Looking Back Looking Forward: 2021](/about-me/Looking-Back-Looking-Forward)

  * [Inspiration](/inspiration)

  * More

  * [Home](/home)

  * [Questions](/questions)

  * [why much of science progress happened in west?](/questions/why-much-of-science-progress-happened-in-west)

  * [my curse of curiosity and the problem of choice](/questions/my-curse-of-curiosity-and-the-problem-of-choice)

  * [Books](/books)

  * [Advisories](/advisories)

  * [CTF](/CTF)

  * [BountyCon 2020](/CTF/bountycon2020)

  * [H1-2006-CTF](/CTF/h1-2006-ctf)

  * [Hack.lu](/CTF/hack-lu)

  * [Facebook CTF'19 writeup](/CTF/facebook-ctf19-writeup)

  * [CSAW'19 CTF](/CTF/csaw19-ctf)

  * [tangled_browsers](/CTF/tangled_browsers)

  * [ByteBandits CTF 2020](/CTF/bytebandits-ctf-2020)

  * [Google CTF - 2020](/CTF/IuseBing)

  * [zer0ptsCTF2021-challenges](/CTF/zer0ptsctf2021-challenges)

  * [site-isolation](/CTF/site-isolation)

  * [BsidesAHM2021](/CTF/bsidesahm2021)

  * [Research](/research)

  * [Cookie Tossing to RCE on Google Cloud Jupyter Notebooks](/research/cookie-tossing-to-rce-on-google-cloud-jupyter-notebooks)

  * [test'>">test{{7*7}}](/research/testtest77)

  * [Prototype Pollution](/research/PP)

  * [BrokenConflu](/research/brokenconflu)

  * [Why should we follow spec?](/research/why-should-we-follow-spec)

  * [cve-2021-21224-v8-rce-rca](/research/cve-2021-21224-v8-rce-rca)

  * [About Me](/about-me)

  * [Looking Back Looking Forward: 2021](/about-me/Looking-Back-Looking-Forward)

  * [Inspiration](/inspiration)

# 

Cookie Tossing to RCE on Google Cloud JupyterLab

## 

TL;DR

Cookie Tossing and Tornado webserver quirk leads to CSRF bypass which in turn leads to RCE on Jupyter Lab.

By the way, You can check the filedescriptor's video about this bug here.

## 

What is a Jupyter Lab?

JupyterLab is a web-based interactive development environment for Jupyter notebooks, code, and data. JupyterLab is flexible: configure and arrange the user interface to support a wide range of workflows in data science, scientific computing, and machine learning.

Simply, we can run code and also use the terminal in the web interface.

The most important thing is we can also edit the code of the Jupyter application itself.

![](https://lh3.googleusercontent.com/sitesv/AA5AbUDq33nmcGl7ks7_rc3N7zeyMW3YRb1PFOC9Iz3NQPCU3_uvP_gKyJ2FEqCKK7UTxtVzEu6UbeJDgXlnc7qZ2S7sVgjdoi7_5c2iM0F1tQovNxvGvyaSGOPa_WvKzXZdfSQAAlvyrigypGzyI7dKxud3Hmfg-IiPT36HvRG14QcS0Ztv8mHIZk5evo-z2sfAuHHhXbMHawumNEo9Naf4WGJzHk3NoEJd5Dra9XBA=w1280)

## 

How I found the Bug?

In my junior year, I am very interested in AI along with CTFs and I did an intern in Data Science. Most of the time I used Jupyter Notebooks for training models. So, I have a basic understanding of how it works.

Later, I started doing bug bounties and my target is Google Cloud AI HUB.

### 

Google Cloud AI HUB

In AI Hub, we can create notebooks, when a notebook is created what happens in the background is it creates a VM instance, installs Jupyter Notebook, and assigns the random domain (random-id.notebooks.googleusercontent.com) for the notebook instance. Login to the notebook instance takes place via Google SSO.

### 

Self XSS

I know straight XSS in notebooks is not possible, because the markdown and other features are pretty secure. But, we have access to the code base of Jupyter notebooks itself in our VM instance why can’t we just edit the front page index.html and get XSS? Indeed, we can change the source code of Jupyter Notebook by logging to VM instance and change the file located at /opt/conda/share/jupyter/lab/static (check above image).

We can make the victim visit our notebook instance and pop an alert, but it’s of no use because it is a self XSS.

Now, I started thinking of ways to make it impactful. I looked for improper CORS implementations, but everything seems to be good. One more interesting target to look at is cookies when we have self XSS. I've checked cookies and _xsrf cookie caught my eye.

CSRF mitigation is done via checking the cookie value in _xsrf and the X-XSRFToken header value. If both of these values are equal then allow the request.

### 

Self XSS to DOS

Because, we can set cookie _xsrf=1 from our domain on notebooks.googleusercontent.com, which makes every next request from victim notebook getting dropped because of invalid _xsrf token. We are able to change the _xsrf token in the cookie, if we can change the X-XSRFToken header also we can achieve CSRF on notebooks. But, we can't set this header because the browser makes XHR preflight request when we set X-XSRFToken header in the request.

What we have is a kind of DOS, which is of no impact.

So, I made my mind it’s a dead-end and later started reviewing the source code of Jupyter Notebook.

### 

Tornado Web Server comes to rescue for CSRF

I noticed Jupyter uses a tornado webserver

There is one interesting thing about the tornado server for mitigating CSRF.

If xsrf_cookies is set, the Tornado web application will set the _xsrf cookie for all users and reject all POST, PUT, and DELETE requests that do not contain a correct _xsrf value. If you turn this setting on, you need to instrument all forms that submit via POST to contain this field. You can do this with the special UIModule xsrf_form_html(), available in all templates

The code for xsrf_form_html()

So, what does this mean is we can send CSRF token in the request URL, instead of the X-XSRFToken header.

Wow, that’s a nice little feature, we can just use _xsrf token in the request instead of the header.

### 

Cookie Precedence

We don't need to worry about the cookie precedence shown below because the cookie on the base domain precedes the cookie on a subdomain.

POST /test HTTP/1.1

.....

Cookie: _xsrf=actual_cookie; _xsrf=fake_one 

### 

POC for CSRF

Now we have CSRF, the important task is to show the impact.

### 

Jupyter Lab Extensions for RCE

JupyterLab extensions can customize or enhance any part of JupyterLab. They can provide new themes, file viewers and editors, or renderers for rich outputs in notebooks. Extensions can add items to the menu or command palette, keyboard shortcuts, or settings in the settings system.

The first thing I looked at is the extensions because they allow us to run arbitrary code in the victim instance.

It turns out to be with the CSRF, we can install arbitrary extensions in the victim notebook instance.

Now the task is to create a malicious extension that gives RCE in victim notebook instances.

I created this extension which opens a WebSocket connection to the terminal endpoint and runs arbitrary code. (It can be done in other easier ways)

And pushed it to npm[ https://www.npmjs.com/package/@mohansrk/test](https://www.npmjs.com/package/@mohansrk/test)

### 

Final POC

We need to send json request body, luckily server accepts enctype with json body in it. 

Once we got RCE, we have access to most of the Google Cloud because the VM instances have Editor Role by default.

### 

Protection

All the Jupyter Notebooks are vulnerable to this attack.

To fix this issue, add Origin header with proper validation.

### 

Timeline

Reported - Mar 10, 2020

Closed as Duplicate - Mar 23, 2020

Noticed that duplicate they assigned is my previous report and its completely different CSRF - Mar 23, 2020

After some explanation, Re-opened and Accepted - Apr 2, 2020

Rewarded $3133.70 \- Apr 21, 2020 

Marked as Fixed - Oct 17, 2020

  

Finally, This bug is not possible without filedescriptor's awesome research on cookies and I am grateful for the CTF makers and all the people over here([https://blog.s1r1us.ninja/inspiration](https://blog.s1r1us.ninja/inspiration)).

cover credit: [https://imgur.com/](https://imgur.com/)

Google Sites

Report abuse

Page details

Page updated

Google Sites

Report abuse
