---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-28_how-i-got-my-first-bounty-hof-from-google-csrf-lead-to-account-delete.md
original_filename: 2020-12-28_how-i-got-my-first-bounty-hof-from-google-csrf-lead-to-account-delete.md
title: How I Got My First Bounty & Hof From Google (CSRF Lead To Account Delete)
category: documents
detected_topics:
- csrf
- command-injection
- otp
tags:
- imported
- documents
- csrf
- command-injection
- otp
language: en
raw_sha256: 56ffaa843a0a2b0561db92a034eddcef21dc821cdd9a01a724fd1fcd781742f9
text_sha256: c612f644b98c321b2be0bd340a1b2c36610abf65d954bc1b46e50db88a7fd004
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# How I Got My First Bounty & Hof From Google (CSRF Lead To Account Delete)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-28_how-i-got-my-first-bounty-hof-from-google-csrf-lead-to-account-delete.md
- Source Type: markdown
- Detected Topics: csrf, command-injection, otp
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `56ffaa843a0a2b0561db92a034eddcef21dc821cdd9a01a724fd1fcd781742f9`
- Text SHA256: `c612f644b98c321b2be0bd340a1b2c36610abf65d954bc1b46e50db88a7fd004`


## Content

---
title: "How I Got My First Bounty & Hof From Google (CSRF Lead To Account Delete)"
url: "https://bhupendra1238.medium.com/how-i-got-my-first-bounty-hof-from-google-csrf-lead-to-account-delete-85f9906ba9ec"
authors: ["Bhupendra Rajbhar (@bhupendra1238)"]
programs: ["Google"]
bugs: ["CSRF"]
publication_date: "2020-12-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4044
scraped_via: "browseros"
---

# How I Got My First Bounty & Hof From Google (CSRF Lead To Account Delete)

How I Got My First Bounty & Hof From Google (CSRF Lead To Account Delete)
BHUPENDRA RAJBHAR
Follow
5 min read
·
Dec 29, 2020

503

5

Press enter or click to view image in full size

I am Bhupendra Rajbhar (Final Year Computer Engineering Student ) I have been started my bug bounty journey from march 2020 it was a really tough situation for everyone due to the Covid-19 virus hope now everyone safe and well Basically in this blog you will come to know how I have Got my first bounty/reward from google with HOF after the lots of duplicates from another program I decided to hunt on google And the big question is What was the bug? How I exploit and make it a high risk.
*Well This not an English Grammar blog so Please ignore any grammatical mistakes also this is my first Blog Hope everyone will understand*

Vulnerability : Cross-Site Request Forgery (CSRF) Lead To Account Delete

What is Cross-Site Request Forgery (CSRF) ?

Cross-site request forgery (also known as CSRF) is a web security vulnerability that allows an attacker to induce users to perform actions that they do not intend to perform. It allows an attacker to partly circumvent the same-origin policy, which is designed to prevent different websites from interfering with each other.
For More Information's About CSRF You Can Read This Articles : https://portswigger.net/web-security/csrf

!!! Never Lose Your Patience During Bug Bounty Hunting !!!

Always check each and every single endpoints in the targets I had explored the entire application and after sometimes spent I had found account *delete button* After seeing such button always feel like Ohh Yes!!

Immediately I had Fired My burp and intercept the request on that endpoints and generate CSRF Exploits code for that endpoint with the help of burp as the thought was coming in my mind about that endpoint is going to be true After seeing the CSRF Authentication token was not present in that exploits code I was like Ohh Yes!! as every noob bug hunter knows what will be next The exploits code is given below.

Press enter or click to view image in full size

Wait !! The Twist Is Coming now !! I saved This exploits code and send it to the victim browser but this code was unable to delete the victim full account I was getting confused on that points because this code was deleted only the victim entire account personal details except for the account which will not come under critical severity I had tried more than 5 times.

I Took a Break for few minutes and did my favorite things watching tom and jerry on youtube and came back analyzed my exploits code again now lots of thought came to my mind about how I can make it more critical and in the end, I was decided to not closed Html Tag The code is now look like this.

Press enter or click to view image in full size

Now Sent to victim's browser and submit the button And Boom !!! The Victim Full Account get deleted :) XD

Ohh Yeh Baby !!

Immediately I had Created the report with video proof of concept and submitted it to Google . Reported : Aug 6, 2020, 12:29 PM

Get BHUPENDRA RAJBHAR’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

It Triaged The Next day in the morning Got Response from google is this given below .

Press enter or click to view image in full size

Lmao !! It was really disappointed me Even I had sent proper video POC to them then also they weren’t able to reproduce the vulnerability :(

I took bath as it was early morning and start creating again that report with proof of concepts now this time I was written some extra points like html tag should not be closed and make them to reproduced and reported again !! And Now Got what I expected !! Nice catch

Press enter or click to view image in full size

Step To Produce CSRF :-

Create Two Account One For Victim (victimbhupi@gmail.com) and second For the Attacker(attackerbhupi@gmail.com).
2. Create CSRF Exploits code for Vulnerable Endpoint (Using Burp suit)
3. Save it in an HTML file and send it to The victim Browser.
4. When Victim Click Submit Button CSRF Exploits Code will be executed in the Victim Browser.
5. Boom!! Victim Account Will be permanently deleted.

Timelines :-

Reported : Aug 6, 2020, 12:29 PM
Triaged : Aug 7, 2020, 12:26 AM
Not Reproduce : Aug 12, 2020, 4:49 AM
Again Reported : Aug 12, 2020, 10:56 AM
status: Assigned → Accepted : Aug 13, 2020, 1:35 PM
Bounty : Yes

Thankyou All Of You ! for reading my blog If You Like This Blog do Clap on it.

For any quick query or getting in touch with me, You can follow me on

LinkedIn : https://www.linkedin.com/in/bhupendra1238/

Twitter : https://twitter.com/bhupendra1238
