---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-01_privilege-escalation-to-stored-xss.md
original_filename: 2021-10-01_privilege-escalation-to-stored-xss.md
title: Privilege Escalation to stored XSS
category: documents
detected_topics:
- xss
- access-control
- command-injection
- otp
tags:
- imported
- documents
- xss
- access-control
- command-injection
- otp
language: en
raw_sha256: 308008eecc78cb277826dc870ac82327140d74a297c2597100b3e8b6ab5399f3
text_sha256: 0cb7ab2cbff144d79f89dbf442571183baf5bcc9a304be9e1f5c7336ce24e516
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Privilege Escalation to stored XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-01_privilege-escalation-to-stored-xss.md
- Source Type: markdown
- Detected Topics: xss, access-control, command-injection, otp
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `308008eecc78cb277826dc870ac82327140d74a297c2597100b3e8b6ab5399f3`
- Text SHA256: `0cb7ab2cbff144d79f89dbf442571183baf5bcc9a304be9e1f5c7336ce24e516`


## Content

---
title: "Privilege Escalation to stored XSS"
url: "https://rohit443.medium.com/privilege-escalation-to-stored-xss-dff01314bc7e"
authors: ["Rohit Kumar (Rohit_443)"]
bugs: ["Privilege escalation", "HTTP response manipulation", "Stored XSS"]
bounty: "500"
publication_date: "2021-10-01"
added_date: "2022-10-10"
source: "pentester.land/writeups.json"
original_index: 3269
scraped_via: "browseros"
---

# Privilege Escalation to stored XSS

Top highlight

Privilege Escalation to stored XSS
Rohit_443
Follow
3 min read
·
Oct 1, 2021

132

Hello everyone

I am writing my second bug bounty write-up which is privilege escalation to stored xss.In which i am able to bypass privilege from a normal user to partner user and successfully exploit xss to existing partner.

What is privilege escalation attack..?

Privilege escalation can be defined as an attack that involves gaining illicit access of elevated rights, or privileges, beyond what is intended or entitled for a user. This attack can involve an external threat actor or an insider.

What is Stored XSS..?

Cross site scripting (XSS) is a common attack vector that injects malicious code into a vulnerable web application. In that it does not directly target the application itself. Instead, the users of the web application are the ones at risk.

Press enter or click to view image in full size
Stored cross-site-scripting

Lets get started with the finding.

After submitting 3,4 low level bugs to this program i am decided to go for some high level vulnerability. Just exploring all the dynamic function of the website i find their is partner login function to access all the partner resources.

So,i just click on this function and here i have to choose a partner and enter email id. Now i am trying to verify but got an error that unable to verify information.

So i again send a verification code and capture the request in burp-suite and -Do intercept response to this request. and in response there is parameter of true and false. i just manipulate it from false to true. And successfully bypassed now i have partner privilege as their existing partner. And also able to access all the resources of partners.I just make a video poc and submit this report to the program.

But what happened next.

After some days i checked that the issue was fixed.So i leave the target and move on.

Get Rohit_443’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But after 3 month i came back here and find that my id is still working as a partner ID. So after verify my email id here i have to fill a long form i just try to insert a xss payload in one of the filled of the form and its executed successfully.whenever they visited this partner account the xss payload executed successfully.

payload: RK”><svg/onmouseover=alert(document.cookie)>

Step to reproduce:

After login as a normal user.
Now you can go to partner user functionality. and choose existing partner and enter your own email to verify this.
Enter the valid code which you receive on email and capture the request in burp-suite-Do-intercept response to this request.
In the response change parameter from false->true and click on go.
Here you bypass the verification.
Now here you have a form to fill all the detail including your address and phone number.insert xss payload in the address field and submit this.and xss payload fired successfully.
Whenever the real partner user visited this. attacker can get their session cookies.

For upcoming writeup.

Follow me on twitter @Rohit_443
