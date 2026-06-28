---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-25_information-disclosure-leads-to-sensitive-credential.md
original_filename: 2021-12-25_information-disclosure-leads-to-sensitive-credential.md
title: Information Disclosure leads to sensitive credential($$$)
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 595788f21ccdd05441749a60db84bd356983f8af868696f5219d67bcd70c5881
text_sha256: 456d3520d6bc68af2a0b9bd3168ebfa3ee0ca21351e447de97b7c3a47645290f
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: true
---

# Information Disclosure leads to sensitive credential($$$)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-25_information-disclosure-leads-to-sensitive-credential.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: True
- Raw SHA256: `595788f21ccdd05441749a60db84bd356983f8af868696f5219d67bcd70c5881`
- Text SHA256: `456d3520d6bc68af2a0b9bd3168ebfa3ee0ca21351e447de97b7c3a47645290f`


## Content

---
title: "Information Disclosure leads to sensitive credential($$$)"
url: "https://medium.com/@mamunwhh/information-disclosure-leads-to-sensitive-credential-35e779f6f4db"
authors: ["khan mamun (@mamunwhh)"]
bugs: ["Information disclosure"]
bounty: "150"
publication_date: "2021-12-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3064
scraped_via: "browseros"
---

# Information Disclosure leads to sensitive credential($$$)

Information Disclosure leads to sensitive credential($$$)
khan mamun
Follow
2 min read
·
Dec 25, 2021

90

2

Hi Hackers, hope you are fine.my name is 
khan mamun
(white hat hacker) This is my 3rd write up.

Today i gonna share, How i find Information Disclosure leads to sensitive credential.[url,password,username] this is so much interesting so why not share with you!!

Let’s go, first of all, i use nuclei tool normally [Thanks my friend 
FOYSAL AHMED FAHIM
,he is most talented Ethical hacker of BD]I used this tool for find subdomain with subfinder. ok. When this is done, I see a password in the info of nuclei tool.

[info][https://watch.site.com] [password=***REDACTED***

password look like password=***REDACTED*** ,Then I thought why not check its url(watch.site.com). Then I open this url in which I got a password and next go to the view page source and type the username with cltrl + f.Because I thought that would be great to have a username. yes i found it.wow. that’s great,I’m not found just a password I got a url(https://www.site.com this is main url on this website)and also username.

when i found this Url,password and Username.then I checked these are valid or invalid. I try to login on this url(www.site.com),username and password.Done I confirm that valid all of because I’m logged.

Get khan mamun’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Step By Step:

Navigate url: watch[.]site[.]com
Go to View page source
Search ‘username’
We can see that,url: site[.]com,password and username.
We are logged with this credential.

Bounty : $150

tips: always navigate the view page source.Remember that have bug in[info]if you can gain it.

Thanks so much.

If something goes wrong, please forgive me:)

My twitter: https://twitter.com/mamunwhh

If you want check my YT channel: https://www.youtube.com/channel/UCwFn0AfyutumdIDWCUyR21Q
