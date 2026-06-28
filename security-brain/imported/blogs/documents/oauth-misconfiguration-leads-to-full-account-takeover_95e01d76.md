---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-13_oauth-misconfiguration-leads-to-full-account-takeover.md
original_filename: 2021-02-13_oauth-misconfiguration-leads-to-full-account-takeover.md
title: OAuth Misconfiguration Leads to Full Account takeover
category: documents
detected_topics:
- oauth
- sso
- xss
- command-injection
- mfa
- otp
tags:
- imported
- documents
- oauth
- sso
- xss
- command-injection
- mfa
- otp
language: en
raw_sha256: 95e01d76d39550d04b2d50beb1bb1e1843974593a38b6706e13456aea86dc354
text_sha256: f7c5bb61ee27560c2cd4877bcc951a53f89fbb0f942af51b9fe13bc3b29d982f
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# OAuth Misconfiguration Leads to Full Account takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-13_oauth-misconfiguration-leads-to-full-account-takeover.md
- Source Type: markdown
- Detected Topics: oauth, sso, xss, command-injection, mfa, otp
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `95e01d76d39550d04b2d50beb1bb1e1843974593a38b6706e13456aea86dc354`
- Text SHA256: `f7c5bb61ee27560c2cd4877bcc951a53f89fbb0f942af51b9fe13bc3b29d982f`


## Content

---
title: "OAuth Misconfiguration Leads to Full Account takeover"
url: "https://neroli.medium.com/oauth-misconfiguration-leads-to-full-account-takeover-22b032cb6732"
authors: ["Yasser Mohammed (@boomneroli)"]
bugs: ["OAuth", "Clickjacking", "CSRF", "Account takeover"]
publication_date: "2021-02-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3914
scraped_via: "browseros"
---

# OAuth Misconfiguration Leads to Full Account takeover

1

·

Top highlight

OAuth Misconfiguration Leads to Full Account takeover
Yasser Mohammed (@n3r0li)
Follow
5 min read
·
Feb 13, 2021

551

2

Hi Every one, My name is Yasser (AKA Neroli in CTF’s) and I wanted to share this Finding with you :)

Since its a private program on Bugcrowd i will call it example.com

Let’s start

While I was testing this target I wanted to test the OAuth flaw since it has a lot of misconfigurations that developers don’t recognize,
So I found that the target allows users to log in using either a classic, password-based mechanism or by linking their account to a social media profile using OAuth.

So let’s test this.

OAuth misconfiguration

First thing i opened burp and started to log the requests and just start clicking on buttons

and after linking my profile I started looking at the request history I found the callback request

Press enter or click to view image in full size
The OAuth Callback

and as u can see, no csrf token, In this case if the application fails to use the csrf token , an attacker could potentially hijack a victim user's account on the client application by binding it to their own social media account.

Let’s test it

after intercepting the request and drop it I created a simple csrf POC page that redirect to the link that we just intercepted

and the response:

Press enter or click to view image in full size
the csrf POC response

so yeah we did it :),

so let’s open our account and see what happened …. nothing, I was like What?!

I was just thinking about how I am going to spend the bounty

Viewing my Profile Page, the Social Account is not there,

Tried again and again, Same thing

So I started to do some analysis to understand what is going on

Debugging

First thing I do in my debugging process is logging all the communications between the windows using simple extension,
you can install this Chrome Extension and My console is full with data, after some filtering i found this flaw

Press enter or click to view image in full size

First when i click the link button there is a postmsg with click event sent

and after pressing accept the SDK is loading and the flaw start.

So it seems that before the Linking Action is taken there is something needs to load first

First thing got into my mind is why the link is not working

so when i opened the link that i dropped above I noticed an error in the console

Press enter or click to view image in full size
Error in linking account Callback link

So let’s trace it, this video by STÖK will help you a lot

opening the callback resolver I found that the issue was in this line

Press enter or click to view image in full size
callback resolver

so let’s put some break points to see why

Press enter or click to view image in full size
Callback resolver

as u can see the problem is that the settingsService.qsParams is undefined

so we cannot continue and the process stops

Get Yasser Mohammed (@n3r0li)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

so the only Way that can write to this is that one of the postMessage that been sent above contains the data that fills this parameter.

looking above again i noticed that when the SDK is triaging the click event we got a parameter called language

Press enter or click to view image in full size

and the error we got is bcs the lang is not there

so I guess that this what is solving the problem.

but how we do it

First thing got into my mind is simulating the postMessage and sent a similar one,

luckily the page was vulnerable to clickjacking but it was out of scope so it’s not fixed

so let’s try to create iframe and send some data I read this article which is super useful to understand how to do it but the problem is I couldn’t know how to send this custom event.

at this point I gaved up and created a shitty click-jacking page that the user first needs to click on the link button then i redirect him to the Oauth link.

luckily the triager took so long to triage it and told me why would someone click on the button and also he faced a problem with his browser that made him unable to reproduce the issue and closed it as NotReproducible I was so mad since it was valid bug but.. I got time to rethink on how to bypass this thing,

Bypass

and here I read my Friend Sayed (who is great hacker btw follow him for nice write ups) post

so I did the same and I got and Idea to bypass it XD

following the trace callbacks I started to ask if the data which was sent is coming from the static page or it starts when i click on the button and i got the popup.

and as expected the data was coming from the popup page

Press enter or click to view image in full size
the connectRoute is the popup endpoint

I noticed that the popup endpoint doesn’t have any dynamic tokens or csrf tokens so I crafted a simple url with the parameters that i need

https://examble.com/init?appId=staticID&lang=en-GB&genomeId=StaticID&ssoId=anyID&nextUrl=https%3A%2F%2Fexample.com%2F

when i opened it the SDk is initialized :)

Press enter or click to view image in full size
the SDK loaded and the Trigger pageevent

So I created a simple html page that loads the crafted url and then opens the Oauth callback link

<html>
<head>
 <title></title>
</head>
<body>
  <iframe src="https://examble.com/init?appId=staticID&lang=en-GB&genomeId=StaticID&ssoId=anyID&nextUrl=https%3A%2F%2Fexample.com%2F" onload="setTimeout(myFunction, 9000)" style="opacity: 0.0;"></iframe>
<script>
function myFunction() {
  document.write('<iframe name="cksl7" src="https://example/oauthCallBack?code={code}&cid={id}" style="opacity: 0.0;""></iframe>');
}
</script>
</body>
</html>

and boom it worked

also the 2FA was not available in OAuth login so we got the account :)

Conclusion
Don’t report the bug if you didn’t tried your best.
don’t be random and try to understand what is happening not just reading a lot of write-ups and do as same as the write-ups says.
there is a a lot of time and searching and debugging behind the scene so always try to find the highest impact for the issue.

Thank you all for reading and I hope you find it useful.

References
https://javascript.info/cross-window-communication
https://vinothkumar.me/20000-facebook-dom-xss/
https://opnsec.com/2020/05/dom-xss-in-gmail-with-a-little-help-from-chrome/
https://portswigger.net/web-security/oauth
