---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-11_my-experience-on-hacking-the-dutch-government.md
original_filename: 2022-08-11_my-experience-on-hacking-the-dutch-government.md
title: My Experience on Hacking the Dutch Government
category: documents
detected_topics:
- xss
- command-injection
- otp
- csrf
- api-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- csrf
- api-security
language: en
raw_sha256: bb197e3b88b03f1f54b0b0c92daca090fb48e0d07df5d72cd0bdac237b9141d3
text_sha256: d9c739e7861d86604b583c9929996e8a080c94e49594234cf39227858fd7bb90
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# My Experience on Hacking the Dutch Government

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-11_my-experience-on-hacking-the-dutch-government.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, csrf, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `bb197e3b88b03f1f54b0b0c92daca090fb48e0d07df5d72cd0bdac237b9141d3`
- Text SHA256: `d9c739e7861d86604b583c9929996e8a080c94e49594234cf39227858fd7bb90`


## Content

---
title: "My Experience on Hacking the Dutch Government"
url: "https://gonzx.medium.com/my-experience-on-hacking-the-dutch-government-a2c5a5f43d83"
authors: ["Jefferson Gonzales (@gonzxph)"]
programs: ["Dutch Government"]
bugs: ["XSS", "Open redirect", "CSRF", "Account takeover"]
publication_date: "2022-08-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2334
scraped_via: "browseros"
---

# My Experience on Hacking the Dutch Government

Top highlight

My Experience on Hacking the Dutch Government
Jefferson Gonzales
Follow
4 min read
·
Aug 11, 2022

214

5

Press enter or click to view image in full size

Hello, fellow Bug Hunters! It’s me again Jefferson Gonzales, and in this article, I’ll tell you about how I got my dream Dutch Government SWAG, and without wasting your time let’s get started.

On May last year 2021, I noticed that many Bug Hunters had posted on Twitter and LinkedIn that they had received swag from the Dutch Government, I saw the T-Shirt, which was so awesome and had a print saying “I hacked the Dutch government and all I got was this lousy t-shirt,” and I wanted to wear that t-shirt as well, so I searched for a list of Dutch Government domains and found it on github.

https://raw.githubusercontent.com/mil1200/NCSC-NL/27312c1088b3a271289b29407212689afa9dd116/NCSC-NL-subdomains.txt

I manually checked all of that domain for two weeks and all I got is a Static Website and I didn’t found any bugs, so I need to find a good target that is not a Static Website, after checking manually I found a target which is number 1043 on the list

The first I did is to use Waybackurls so I can collect all the hidden parameters, and when my waybackurls done scanning I found an interesting parameter that was reflected on the web page

Press enter or click to view image in full size
Waybackurl resuls in Termux

The value of the parameter ?photographer= was reflected on the page, to test if it’s possible for XSS I add a value Gonz”> to ?photographer= and it was reflected without sanitizing the symbols

Press enter or click to view image in full size

Final Payload:

https://www.nederlandsesoorten.nl/linnaeus_ng/app/views/search/nsr_search_pictures.php?photographer="><script>alert(document.cookie)</script>

Press enter or click to view image in full size
Open Redirect to XSS

While waiting for the fix on the above report I hunt again and I found another latest dutch government website list, you can download it below

https://www.communicatierijk.nl/binaries/communicatierijk/documenten/publicaties/2016/05/26/websiteregister/websiteregister-rijksoverheid-2022-01-27.ods

After I downloaded and looking for a new target I found a good one

nictiz.nl

Since in the main domain there’s no any juicy endpoint I scan the subdomain using the tool called Sublist3r and I found an interesting one

terminologie.nictiz.nl

The thing that caught my attention is there’s a Login but there’s no Signup or Register

I tried a default user/pass

admin:admin
admin:admin123
demo:demo

When I try the demo:demo credential I redirected into the dashboard, but inside the Dashboard of a Demo privilege user there’s no interesting functions since you can’t edit or modify any content it’s like it’s the same as user without authentication

Get Jefferson Gonzales’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But using the demo credential I found an open redirect vulnerability

https://terminologie.nictiz.nl/art-decor/login?returnToUrl=//google.com

but I need to escalate this bug to a better vulnerability so it will be qualified to their Vulnerability Disclosure Program.

I used the below payload to escalate into XSS

Payload: javascript:alert(1)

So when I click the below link and login using the demo credential the XSS will be executed

https://terminologie.nictiz.nl/art-decor/login?returnToUrl=javascript:alert(document.cookie)

Press enter or click to view image in full size
CSRF to Account Takeover

My third target was

repository.scp.nl

It has a big scope to hunt since there’s a Login and Register, first I created an account and then login

When I update my name I found out that there’s no CSRF Token implemented so I can modify any users name with CSRF attack, but this is not a critical bug since I can only modify the name

I need to find a way to make it a serious bug, so I looked through all of the features and discovered the change password feature, which allows me to change my password without having to enter the old one.

Press enter or click to view image in full size

I immediately generated a CSRF POC using Burp Suite CSRF Generator, tested it on my second account, and it successfully changed the password on my second account.

Report Responses

1st Bug:
Submitted Date: May 3, 2021
Resolved Date: September 16, 2021

2nd Bug:
Submitted Date: August 15, 2021
Resolved Date: September 21, 2021

3rd Bug:
Submitted Date: August 17, 2021
Resolved Date: October 1, 2021

After a month, my swag still hasn’t arrived, so I go to my local post office and pick it up myself.

Thank you for reading this writeup.

You can contact me on

Twitter: @gonzxph

LinkedIn: @gonzxph
