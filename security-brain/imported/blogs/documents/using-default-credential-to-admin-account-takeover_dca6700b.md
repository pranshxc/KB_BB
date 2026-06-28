---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-02_using-default-credential-to-admin-account-takeover.md
original_filename: 2022-10-02_using-default-credential-to-admin-account-takeover.md
title: Using Default Credential to Admin Account Takeover
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: dca6700b35f258689d38e7abd145119eea52075c62c9dcd84746d60dcaea933a
text_sha256: a334d94430fb65aad3809f9464f952419d102d38d463df9b531302840e630d04
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Using Default Credential to Admin Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-02_using-default-credential-to-admin-account-takeover.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `dca6700b35f258689d38e7abd145119eea52075c62c9dcd84746d60dcaea933a`
- Text SHA256: `a334d94430fb65aad3809f9464f952419d102d38d463df9b531302840e630d04`


## Content

---
title: "Using Default Credential to Admin Account Takeover"
url: "https://rohit443.medium.com/using-default-credential-to-admin-account-takeover-677e782ff2f2"
authors: ["Rohit Kumar (Rohit_443)"]
bugs: ["Weak credentials"]
publication_date: "2022-10-02"
added_date: "2022-10-10"
source: "pentester.land/writeups.json"
original_index: 2091
scraped_via: "browseros"
---

# Using Default Credential to Admin Account Takeover

Using Default Credential to Admin Account Takeover
Rohit_443
Follow
2 min read
·
Oct 2, 2022

192

1

Hi, Everyone

I hope you all are doing well.

I am writing my 4th Bug bounty write-up “Using Default Credential to admin account takeover”. while testing on a program , i walk through the application and checked all the functionality ,forms ,login,signup,forget-password etc. After this all, i was going to perform recon phase on this target and that leads to admin account takeover.

Lets start with the finding.

While testing on this target , and go through all the functionality , i have found 3,4 low level bugs. And then i was started doing recon on this target with directory fuzzing using FUFF tool but not getting any useful information. Than i open shodan.io and search for this simple shodan dorks “ssl:company.com 200” and finding many ip belongs to my target. After opening two pages of shodan , i have found an IP address , where company support page is running and there is login page with the forget password functionality. So, in forget password i am using my personal email address and got an error “email address not found”.

Press enter or click to view image in full size
Invalid email

So , the turning part of this story comes here.

At the footer of the same web-page i have found something which is “Have some queries? email us at Support@company.com. and i copied this email address and using it on forget password and this message pop-up on my screen“ You will receive an email with a link to reset your password”

Press enter or click to view image in full size
Valid Email

Here , i have found valid email address for this support portal of the company. and after that i am using this email as username and for password->company123. and successfully login to this portal.

Get Rohit_443’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After login i have access to all internal information of the company , like employee email ,phone , their message , documents and also able to change the password etc. I reported this vulnerability but report was going duplicate as critical vulnerability , but i was happy to find this.

Step to reproduce:

Use this dorks on shodan.io “ssl:company.com 200”
Found a IP address with support page.
At the footer of the web-page ,found valid email as username
Now using Default password company123.
Successfully logged in.
Enumerating all employee data ,like , email,phone, documents etc.

Thank you for reading this write-up i hope you found it useful.

For upcoming write-up.

Follow me on twitter https://twitter.com/Rohit_443
