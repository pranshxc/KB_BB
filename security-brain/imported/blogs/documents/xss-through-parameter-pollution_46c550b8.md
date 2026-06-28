---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-05_xss-through-parameter-pollution.md
original_filename: 2021-05-05_xss-through-parameter-pollution.md
title: XSS Through Parameter Pollution
category: documents
detected_topics:
- xss
- business-logic
- command-injection
- automation-abuse
- csrf
- cloud-security
tags:
- imported
- documents
- xss
- business-logic
- command-injection
- automation-abuse
- csrf
- cloud-security
language: en
raw_sha256: 46c550b864711882465874f8c928e58756f3a544762416441cf2ea8cf9506f78
text_sha256: 6973de6e580d1063bf161dff20a48b7edce4349bfebfc17136a9c4ca3daa3c82
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# XSS Through Parameter Pollution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-05_xss-through-parameter-pollution.md
- Source Type: markdown
- Detected Topics: xss, business-logic, command-injection, automation-abuse, csrf, cloud-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `46c550b864711882465874f8c928e58756f3a544762416441cf2ea8cf9506f78`
- Text SHA256: `6973de6e580d1063bf161dff20a48b7edce4349bfebfc17136a9c4ca3daa3c82`


## Content

---
title: "XSS Through Parameter Pollution"
url: "https://infosecwriteups.com/xss-through-parameter-pollution-9a55da150ab2"
authors: ["Saajan Bhujel (@saajanbhujel11)"]
bugs: ["Open redirect", "XSS", "HTTP parameter pollution"]
publication_date: "2021-05-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3676
scraped_via: "browseros"
---

# XSS Through Parameter Pollution

Top highlight

XSS Through Parameter Pollution
Saajan Bhujel
Follow
5 min read
·
May 5, 2021

747

Hi everyone,

I am Saajan Bhujel.

Student of Bachelor of Commerce(B.Com) and also I am a Bug Bounty Hunter.

Press enter or click to view image in full size

This is my 2nd blog, if you find any spelling mistakes, so please bear with me for the next few minutes. And, also I found this vulnerability in the VDP Programs. But before starting this blog I would like to give a piece of small basic information about Cross-site Scripting (XSS) and HTTP Parameter Pollution (HPP).

What is the Cross-site Scripting (XSS)?

Cross-site scripting (also known as XSS) is a web security vulnerability that allows an attacker to inject malicious code into a vulnerable web application.

There are three main types of XSS attacks. These are:

Reflected XSS: where the malicious script comes from the current HTTP request.
Stored XSS: where the malicious script comes from the website’s database.
DOM-based XSS: where the vulnerability exists in client-side code rather than server-side code.
What is the HTTP Parameter Pollution (HPP)?

HTTP Parameter Pollution, as implied by the name, pollutes the HTTP parameters of a web application in order to perform or achieve a specific malicious task/attack different from the intended behavior of the web application.

Now let’s start the blog….

Press enter or click to view image in full size

After spending some days in the programs of Hackerone and Bugcrowd. I got some vulnerabilities on those programs like CSRF and Business logic flaws. But, I got duplicates for all my reports. Then, I thought to myself that, this time hunt on some VDP Programs.

So, I started hunting to find some bugs in the VDP Programs. After 2–3 Hours of hunting, I found that one domain is using a callback parameter in the URL for redirecting users to another subdomain.

And also, I can’t disclose the name of the target. So, Let’s suppose that the target is site.com. And, the URL is something looks like this:

https://site.com/out?callback=https://subdomain.site.com

And, If I open the above link. Then, it will redirect me to subdomain.site.com.

So after seeing this redirection, I tried to change the value of the callback parameter with the https://bing.com. Because I want to confirm that, the website is doing any kind of validation or not. If the website is doing validation or redirection only allows for subdomains of site.com then the website might be not vulnerable to Open Redirect. And, If the website is not doing any kind of validation then the website is vulnerable.

Get Saajan Bhujel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And, after changing the value of the callback parameter. Now, the URL is something looks like this:

https://site.com/out?callback=https://bing.com

Press enter or click to view image in full size
Value of the callback parameter is reflecting in the response

And, If I open the above link. Then, it will also redirect me to bing.com. It means that the website is not doing any kind of validation and It’s vulnerable to Open Redirect. But, after seeing the response of it in the Burpsuite. I thought that, maybe this is also vulnerable for the Cross Site Scripting because the value of the callback parameter is also reflecting back into the response.

So firstly, I tried to break the code because the value is reflecting in the script tag. For, break the variable callbackUrl, I simply put anything%22; in the callback parameter. But, after sending this request I got an error that blocks my request. And, also I am getting the same error for some other values[like ‘,”].

Press enter or click to view image in full size
Error that blocks my request

Now, I have only two options:

The first option is to report this issue as an Open Redirect.
The second option is to find a bypass for getting an XSS.

Then, I remember that some weeks ago, I watched the video of Pwnfunction on HTTP Parameter Pollution. So, I choose the second option is to find a bypass for getting an XSS. And also, I added one more callback parameter in the URL for doing a Parameter pollution attack. And now, the URL is something looks like this:

https://site.com/out?callback=anything&callback=random

Press enter or click to view image in full size
Response of two callback parameters

And, I noticed that if I add two same parameters in the URL. Then, I will get the values of both parameters in the response separated by a comma.

And, you also know that when I used the values[like ‘,”] that time I got an error that blocks my request. But now, I have two same parameters.

So again, I tried to break the variable callbackUrl. But this time, I put %22;something%2f%2f in the second callback parameter. After adding the value, now the URL is something looks like this:

https://site.com/out?callback=anything&callback=%22;something%2f%2f

Press enter or click to view image in full size
Able to break the callbackUrl variable

And, it works I am able to break the code or bypass the filter. It means that website is not doing any validation for the second callback parameter.

Now this time, For getting an XSS alert, I put %22;alert%281%29;%2f%2f in the second callback parameter. And now, the URL is something looks like this:

https://site.com/out?callback=anything&callback=%22;alert%281%29;%2f%2f

Press enter or click to view image in full size
Again getting a block request

And again, The website blocks my request for using brackets. So, I replaced brackets with URL encoded or ` `. But still, I am getting error. Because the website is still doing some validation for all the parameters.

Then, again I used `` with URL encoded. And, Finally I succeed to bypass the filter. And, the final URL is something that looks like this:

https://site.com/out?callback=anything&callback=%22;alert%60XSS_POC_BY_SAAJAN_BHUJEL%60;%2f%2f

Press enter or click to view image in full size
Bypass the filter
Press enter or click to view image in full size
Getting an XSS alert

So now, I am successfully able to bypass the filter and perform an XSS through Parameter Pollution. And, In my case, I am able to bypass some filters for some values [like ‘,”] through parameter pollution attack.

TIP:- If you see that your target is doing some kind of validation checks on the parameters. Then, try to add one or more same parameters. For seeing any changes in the response of the website, maybe you can bypass the validation checks.

Thank you for reading this blog, and I hope you learn something.

Enjoy your day!….
