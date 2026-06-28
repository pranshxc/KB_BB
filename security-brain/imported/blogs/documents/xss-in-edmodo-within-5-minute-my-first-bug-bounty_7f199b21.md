---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-04_xss-in-edmodo-within-5-minute-my-first-bug-bounty.md
original_filename: 2019-03-04_xss-in-edmodo-within-5-minute-my-first-bug-bounty.md
title: XSS in Edmodo within 5 Minute (My First Bug Bounty)
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: 7f199b21438293f2371e65c29cb2330132c0b6ea214b428c18d58b7f66fe463b
text_sha256: 35e19358f0825eb25431e45870965177c7404ec0827020da4a0a5caad44bc014
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# XSS in Edmodo within 5 Minute (My First Bug Bounty)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-04_xss-in-edmodo-within-5-minute-my-first-bug-bounty.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `7f199b21438293f2371e65c29cb2330132c0b6ea214b428c18d58b7f66fe463b`
- Text SHA256: `35e19358f0825eb25431e45870965177c7404ec0827020da4a0a5caad44bc014`


## Content

---
title: "XSS in Edmodo within 5 Minute (My First Bug Bounty)"
url: "https://medium.com/@valakeyur/xss-in-edmodo-within-5-minute-my-first-bug-bounty-889e3da6167d"
authors: ["Vala Keyur (@valakeyur)"]
programs: ["Edmodo"]
bugs: ["Reflected XSS"]
publication_date: "2019-03-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5380
scraped_via: "browseros"
---

# XSS in Edmodo within 5 Minute (My First Bug Bounty)

Keyur Vala
 highlighted

XSS in Edmodo within 5 Minute (My First Bug Bounty)
Keyur Vala
4 min read
·
Mar 4, 2019

--

4

Hello Bug Hunters,

What I will tell you in this article is how I managed to exploit the XSS in Edmodo?

This bug was found by me a month ago. Inspired the story of 
Parth Shah
. He wrote an article based on Stored XSS.

As I was surfing the edmodo.com website, I found two or more URLs at that point in time. There is nothing on that page except a login page and an outdated layout of the Edmodo website. I think let’s see if I can find anything on this page.

I decided to capture the login request of that page after some time on Target URL: https://www.edmodo.com/bookmarklet-login

When I opened this URL, I saw a login screen with a sky blue background. Here is a screenshot of the login page. However, nothing happened when I tried SQL and XSS Input. My next step was to dig deep into the application and check all parameters of the request after logging in.

Press enter or click to view image in full size

In the request, username, password, and login information are passed. All of these passes when the user logs in. However, I see there is a parameter called URL passed with the request.

Press enter or click to view image in full size

My mind goes into overdrive when the URL parameter is passed in the request!

Now, I’m gonna try to put a string like “Test Example”. I will show the response and it will be reflected on the page. Inputs do not involve any validation or filtering. I tested other payloads and they were also set correctly. Likewise, the payload is also breaking the input tag on the response side. Special characters and XSS payloads will be accepted without any errors.

Step to Generate XSS [Reflected]:

Step - 1: Open https://www.edmodo.com/bookmarklet-login. Enter the random username and password.

Press enter or click to view image in full size

Step - 2: Note the request. Note the “URL” parameter passing in the request.

Press enter or click to view image in full size

Step - 3: Put the url= ”/><script>alert(document.domain)</script.

Press enter or click to view image in full size

Step - 4: Check the response. the payload breaks the input tag on the response side.

Press enter or click to view image in full size

Step -5: Payload successfully executed Woooohooo…!

Press enter or click to view image in full size

My reaction after Successfully Executing Payload is like this..:P

Finding a single vulnerability can take a lot of time and effort, but if you go too deep, something will definitely be found.

Get Keyur Vala’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I was very excited because it was my first valid bug. I always awaited a response from Edmodo. I immediately made a POC video and sent it to the team. The team was very responsive. The swag was delivered a few weeks later.

Press enter or click to view image in full size
Timeline:

09-Jan-2019: Report Sent

10-Jan-2019: Report in Verification Process.

10-Jan-2019: Report Verified Successfully.

11-Jan-2019: Reward Sent

20-Jan-2019: Reward Received. (Swag)

Things to Know :
Always dig deeper into the web application.
check every parameter which is passing in the request.
Always Never Give Up. There is always something when you go into the deep.
Always do more practice reading books and read more and more writeups.

Thank you for reading this. Focusing now more on reward-based programs. Any suggestions are welcome.

About Me:

An IT security consultant and researcher with over 3.5+ years of expertise in Web & Mobile Penetration Testing. Competent and skilled IT & Web Security Researcher & Developer. Apart from professional experience, I have enthusiasm and diligence for hacking, finding new bugs and vulnerabilities. Having work knowledge in reputed fields.

Helping Enterprise, Medium, and small businesses to be cyber safe. By providing high-end cyber security consulting and the best possible solutions. Working with a vast cyber security community of consultants, companies, and solution providers to reach the cyber-safe goal.

Facebook, Twitter, Linkedin, Medium: @valakeyur

Thank You,

Keyur Vala
