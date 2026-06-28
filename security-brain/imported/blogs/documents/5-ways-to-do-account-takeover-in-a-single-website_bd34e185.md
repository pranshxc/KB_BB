---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-27_5-ways-to-do-account-takeover-in-a-single-website.md
original_filename: 2020-09-27_5-ways-to-do-account-takeover-in-a-single-website.md
title: 5 Ways to do Account Takeover in a Single Website
category: documents
detected_topics:
- rate-limit
- otp
- oauth
- jwt
- idor
- command-injection
tags:
- imported
- documents
- rate-limit
- otp
- oauth
- jwt
- idor
- command-injection
language: en
raw_sha256: bd34e185d345dce373a98fd5b308d884651d21406969a2939ad9e19ecb075df1
text_sha256: 492bfd51212a1eb215031aed5233cdea5358854c96b1cf30ba7ea364e5c76875
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# 5 Ways to do Account Takeover in a Single Website

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-27_5-ways-to-do-account-takeover-in-a-single-website.md
- Source Type: markdown
- Detected Topics: rate-limit, otp, oauth, jwt, idor, command-injection
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `bd34e185d345dce373a98fd5b308d884651d21406969a2939ad9e19ecb075df1`
- Text SHA256: `492bfd51212a1eb215031aed5233cdea5358854c96b1cf30ba7ea364e5c76875`


## Content

---
title: "5 Ways to do Account Takeover in a Single Website"
url: "https://medium.com/@vasuyadav0786/5-ways-to-do-ato-in-a-single-website-cfe7e5da987e"
authors: ["letmeslidein (@VasuYadaav)"]
bugs: ["Account takeover", "Lack of rate limiting", "OTP bypass", "IDOR", "OAuth", "JWT"]
publication_date: "2020-09-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4234
scraped_via: "browseros"
---

# 5 Ways to do Account Takeover in a Single Website

5 Ways to do Account Takeover in a Single Website
Vasuyadav
Follow
5 min read
·
Sep 27, 2020

959

5

Good day, everyone!
I was hunting on one application yesterday and got five separate ATO’s, all without user involvement, and I was as surprised as you are, so I decided to make a write-up.
Also, this is my first attempt at writing, so please excuse any errors.

The website didn’t allow public disclosure so let’s take it as target.com and let’s head straight to the bugs.

ATO 1-Through JWT Misconfiguration

So, anytime I hunt for flaws, the first thing I check for is ATO, so I created an account, and the application was JWT tokens for authentication, so I quickly copied my JWT and went to jwt.io to decode it, and it looked something like this-

After investigating this, I was 50% certain that there was a weakness, therefore the next step was to find a means to obtain other people’s user ids.

So I assumed it might have leaked in response to our request for a password reset, but it wasn’t disclosing the user id instead, it was leaking something more juicy, which will be described later.

Then I tried to login with wrong password and checked the response of the request and it was leaking the user id

Then I immediately created a 2 account, obtained its user id, and proceeded to jwt.io to replace it and obtain the JWT Token, after which I entered in with my 1 account but updated the JWT, and guess what? I was in into my 2 account.

Here’s a fast JWT meme for you.

ATO 2-Through OAUTH Misconfiguration

After that, I quickly reported it, and then I thought of testing for OAUTH bugs. Normally, I only test for Facebook OAUTH bugs, and I did the same for this target as well, but FB OAUTH was not working, and I never test google sign in because I’ve never had a bug, but I thought I’d give it a try, so I intercepted it and tried to sign in with my Google account, and I saw this.

Press enter or click to view image in full size

At this point, I was certain that you had received another ATO, so I changed my email and forwarded the request, and I was signed into a different account.

After two ATO’s, I was like this, and who among us isn’t happy?

I also submitted this one, and typically once I have 1 or 2 bugs in a target, I stop hunting and watch a web series; right now, I’m binge-watching “The Office,” which I adore, but this time I figured I’d check for some more bugs and go on to the 3 ATO.

Get Vasuyadav’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

ATO 3- No Rate Limit on OTP Verification

I went to the reset password function and the application was using 4 digit OTP code for verification and whenever you see a OTP then I know

Yes, you are correct.
I quickly fired burp and entered 1000 payloads to see if there was any rate limiting and if OTP could be brute forced. With this, I was able to get my three ATO in one application and report it, but the journey didn’t end there.

ATO 4-OTP Bypass Through Response Manipulation

Another technique to get around OTP is to manipulate the response.
In Response Manipulation, all one has to do is check the response and play with it, so I went to Inruder and checked what the response was after one accurate OTP was submitted, and it was-

There was no access token, and the OTP was just being validated at the beginning, so I tried response manipulation by entering the wrong OTP and then changing the response to the response I got after entering the proper OTP.

AT0 5-IDOR on Reset Password

The last one was also an Basic IDOR, When I requested for reset password then the request response looks like this

Then OTP came to my email and I entered the OTP but when I entered new password and captured that request

Then I noticed there was no OTP field, but there was a user id, which was encrypted but was being leaked in the response, so I just replaced it with the user id of another account, and bam, my other account’s password was changed.

I received a total of 5 ATOs, and note that these are the ones that did not require user input; there were others, such as csrf, but I wanted to concentrate on these.

If you enjoyed the article, please share it with your friends and follow me on Twitter and LinkedIn. If you are a complete newbie, like I was a few months ago, don’t hesitate to contact me on the following handles with your questions, and I will be happy to answer them.

Have a wonderful day ahead of you, and don’t forget to keep hunting and share your discoveries with the community.

Twitter-”https://twitter.com/VasuYadaav”

Linkedin-”https://www.linkedin.com/in/vasu-yadav-82ba701a0/”

Thanks to John-”https://twitter.com/johnjhacking” for the memes and for always helping me out do follow him if you don’t yet.
