---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-31_beyond-the-wall-command-injection-still-alive.md
original_filename: 2020-10-31_beyond-the-wall-command-injection-still-alive.md
title: 'Beyond the wall: command injection still alive.'
category: documents
detected_topics:
- command-injection
- sqli
- otp
- automation-abuse
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- sqli
- otp
- automation-abuse
- api-security
- mobile-security
language: en
raw_sha256: 986d5193644529554ba03832ce502ecec1532f7b22294488800e424797ff4135
text_sha256: 39c54e422ab8ab4b30964d7a292c76f25c7bcf3bafa8a838c16f89c7ea3b0230
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: true
---

# Beyond the wall: command injection still alive.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-31_beyond-the-wall-command-injection-still-alive.md
- Source Type: markdown
- Detected Topics: command-injection, sqli, otp, automation-abuse, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: True
- Raw SHA256: `986d5193644529554ba03832ce502ecec1532f7b22294488800e424797ff4135`
- Text SHA256: `39c54e422ab8ab4b30964d7a292c76f25c7bcf3bafa8a838c16f89c7ea3b0230`


## Content

---
title: "Beyond the wall: command injection still alive."
page_title: "Beyond the wall: command injection still alive. | by Ahmed Thabit (Mr.Constant) | Medium"
url: "https://a-constant.medium.com/beyond-the-wall-command-injection-still-alive-577a898df0b5"
authors: ["Ahmed Constant (@a_Constant_)"]
bugs: ["OS command injection"]
publication_date: "2020-10-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4168
scraped_via: "browseros"
---

# Beyond the wall: command injection still alive.

Top highlight

Beyond the wall: command injection still alive.
Ahmed Thabit (Mr.Constant)
Follow
8 min read
·
Oct 31, 2020

104

Notes
I will change the name of the company I will talk about and call it Kings-Landing.
There is a short version of the story (TL;DR) & take away sections at the end of the write-up if you want to save yourself 7minutes || don’t have time for my jokes :)

I don’t like the introductions, so I will get into the point directly.

HTTP history

After a couple of hours of hunting on the main domain of Kings-Landing didn’t reveal anything interesting, it was time for moving to the next sub-domain in the scope.

I’ve built a habit of taking a quick look at the burp HTTP history before moving on from a web app to another.

I notice a request to an endpoint on another subdomain, and the URL was like this.

https://image-service-prd.Kings-Landing.com/v1/images/Daenerys-Targaryen-is-a-b***h.jpg?size=1760x234

I looked at the Request, and asked myself:

Is there any chance that the size of their images is not fixed, and they assign it in their back-end dynamically from the value of the ‘size’ parameter?

And of course, you know what does that means; it’s time for the legendary payload: The single quotation mark

size=1760x234‘

The response? 500 Internal Server Error

what about two single quotation marks?

size=1760x234'’

The error is gone and it’s 200 Ok again.

wow! Maybe there is hope for you, after all!

I know what you’re thinking, but let me stop you here and spare you the listening to -reading actually- the story of the wasted one and half hour of manual and automation -SQLmap- testing for the SQLi because it was not.

what it was? I didn’t know at this point but I know for sure there is something wrong going back there.
if only I can see the output of my payloads! but all I can see is a CloudFront error message.

I was tired enough to give up on this endpoint -temporarily- and have a break, but as a final move, I sent the request to the burp’s scan.

Active Scan++

ActiveScan++ extends Burp Suite’s active and passive scanning capabilities. Designed to add minimal network overhead, it identifies application behavior that may be of interest to advanced testers.
https://portswigger.net/bappstore/***REDACTED-SUSPECT-TOKEN***When I back, this was the scene!

False Positive everywhere!

The burp’s scanner reported the behavior as an SQLi.
You don’t say!

but the Active Scan++ extension had another thought about that case.

This was the first time -since I install this extension several months ago- I see an output from it!

I was sure that this not a false positive and my input is doing something messy on the server-side, but I had a tunnel vision and was embedded by the idea it MUST be an SQLi.

Press enter or click to view image in full size
The Payload was: `sleep 11`

`sleep 11`
%60sleep%2011%60 [URL encodeing for ` & space]

That was the Active Scan++ report. Pretty simple, it sends the sleep command that makes the server -unsurprisingly- SLEEP for the specified time. I wanted to cut doubt with certainty, so I sent the to the Intruder, and I sent the request 50 times with incrementing in the sleep value.
and the responses delation was matched every single time.

OS Command Injection
Press enter or click to view image in full size

OS command injection vulnerabilities arise when an application incorporates user data into an operating system command that it executes. An attacker can manipulate the data to cause their own commands to run. This allows the attacker to carry out any action that the application itself can carry out, including reading or modifying all of its data and performing privileged actions.

For More Information:
https://owasp.org/www-community/attacks/Command_Injection

At this point, making the server fall asleep has no impact on the security of the server or the app. and due to the annoying server error from the CloudFlear I had no way to see the response of my payloads.

This was the perfect time for the engaging of the super ultimate weapon any hacker has, Google search engine.

The best technique I found to exploit the vulnerability is by making the server send an out-bound by cURL or wget. unfortunately, the server or the Cloudflare didn’t allow any out-bound even the ping, and the nslookup didn’t work.

The Article:
https://gracefulsecurity.com/command-injection-the-good-the-bad-and-the-blind/

I have an OS command, but I can’t see the output -ohh that is why they call it a blind- and I can’t send any request from the server.
I seem to have nothing, but this was the case either for the engineers and scientists who built and developed the computer from a simple switch that has only binary options; ON & OFF. Enter Logic.

Conditional IF

I have a good server who seeps when I tell it to, and by measuring the response time; I can confirm the execution of the sleep command. and I want to execute other commands and confirm the execution. seems like the perfect time for the conditional IF statement.

hey, severe,
SLEEP 10s
IF you can do a flip
AND IF you are NOT that awesome
SLEEP 5s only.

This is the instruction, and now it’s only needed to be coded in a language a computer (Server) can understand. and this was the payload:

`if [ ‘a’ == ‘b’ ]; then sleep 0; else sleep 10; fi`

I sent it with the expectation that the server will sleep for 10s since the a != b, but the server didn’t sleep at all.

Get Ahmed Thabit (Mr.Constant)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Did they patched the bug while my testing! I return to the basic sleep payload and it works.
it must be something somewhere got suspicious from all the programming kay words in the statement. is it over!
Spoiler alert: it’s not. thanks to the URL encoding.

the final payload was:

https://image-service-prd.Kings-Landing.com/v1/images/Daenerys-Targaryen-is-a-b***h.jpg?size=%60%69%66%20%5b%20%27%61%27%20%3d%20%27%62%27%20%5d%3b%20%74%68%65%6e%20%73%6c%65%65%70%20%30%3b%20%65%6c%73%65%20%73%6c%65%65%70%20%31%30%3b%20%66%69%60

And the server falls asleep.

The Real Impact

Now let’s do some series stuff, creating a file.

`echo ‘constant’ > cfile.txt | if [ $(cat cfile.txt) == ‘constant’ ]; then sleep 10; else sleep 2; fi`

The payload is very simple:
hey, server,
MAKE a new file.
NAME it cfile.txt.
PRINT the string ‘constant’ in it.
THEN
IF the cfile.txt has the string ‘constant’ in it SLEEP 10s.
IF NOT SLEEP only 2s.

The fact that the server sloped 10 seconds indicates that the file has been created on the server.

Of course, the server admins won’t love the presence of the file, so i deleted it:

`rm cfile.txt | if [ $(cat cfile.txt) == ‘constant’ ]; then sleep 10; else sleep 2; fi`

this time the sever only slope for 2s; which indicated the deletion of the file.

And of course, all those payloads were URL encoded.

Reporting

At this point, my journey comes to its end. I wrote a detailed report
stated several ways a threat actor can use to compromise the whole back-end server, from uploading a bash shell to deleting the root directory.

Many scenarios, yet the end is the same. Dracarys.

I sent the report to Kings-Landing, And I waited for the duplicate. But I told myself that I won’t care about it this time; because I enjoyed exploiting this bug so much. I mean, how many times a bug hunter encounters an OS injection on a real target!

But unexpectedly, my other two reports -Low & Medium- got closed as a duplicate, and this critical technical one got accepted!!

Really?!!

TimeLine

Oct, 27 2020 | Submitted.
Oct, 28 2020 |First Response.
Oct, 30 2020 | The Bounty received, BUT they downgraded the severity from critical to high!

TL;DR

This is the short version of the story:

a) I found an end-point contains images with a parameter called size.

b) I tried SQL injection, and it fails.

c) I sent the request to the Burp’s scanner, with Active Scanner++ working in the background.

D) The parameter turned out it accepts OS commands, and it responds to the

`sleep 10` with a deletion for 10s

E) This was a blind injection, so I used the IF statement alongside the sleep to run arbitrary commands in the server.

`if [ ‘a’ == ‘b’ ]; then sleep 0; else sleep 10; fi`

F) This payload used to create a file on the server

`echo ‘constant’ > cfile.txt | if [ $(cat cfile.txt) == ‘constant’ ]; then sleep 10; else sleep 2; fi`

G) This is for deleting the file.

`rm cfile.txt | if [ $(cat cfile.txt) == ‘constant’ ]; then sleep 10; else sleep 2; fi`

H) Report. Trigger. Bounty.

Takeaways

Technical

Always take a look at the HTTP history. you will always find something you missed.
Active Scan++ worth having it installed.
Automation is the key. Save your effort for the Logical bugs & investigating the weird behaviors reported by tools.
URL Encoding & double URL Encoding.

Psychological

Kings-Landing is a Public program with dozens of solved reported, yet it had this kind of bugs.
Tunnel vision is:

A very narrow view, inability to see beyond a limited viewpoint.

When you got lost in the details during a test for a specific bug, it will be useful to take a step back, a breath, and reevaluate your viewpoint.
maybe there is another way, maybe there is another bug, But you can’t see that due to your tunnel vision.

Follow Me

https://twitter.com/a_Constant_

https://ke.linkedin.com/in/ahmed-constant-8b7b72174

AhmedConstant - Overview
Arctic Code Vault Contributor Dismiss Sign up for your own profile on GitHub, the best place to host code, manage…

github.com
