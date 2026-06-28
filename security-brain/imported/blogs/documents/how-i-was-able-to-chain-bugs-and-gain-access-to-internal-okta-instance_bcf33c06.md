---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-22_how-i-was-able-to-chain-bugs-and-gain-access-to-internal-okta-instance.md
original_filename: 2020-06-22_how-i-was-able-to-chain-bugs-and-gain-access-to-internal-okta-instance.md
title: How i was able to chain bugs and gain access to internal okta instance
category: documents
detected_topics:
- command-injection
- cloud-security
tags:
- imported
- documents
- command-injection
- cloud-security
language: en
raw_sha256: bcf33c06be042c24bdf8f7cbae351625a6238242f39725ed4e1fd51db37c0c87
text_sha256: 5c43ecb2cb9c7de5edf0c376a7b8e599a842bc37fbfe4fe06f79ae632b9c9db2
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# How i was able to chain bugs and gain access to internal okta instance

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-22_how-i-was-able-to-chain-bugs-and-gain-access-to-internal-okta-instance.md
- Source Type: markdown
- Detected Topics: command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `bcf33c06be042c24bdf8f7cbae351625a6238242f39725ed4e1fd51db37c0c87`
- Text SHA256: `5c43ecb2cb9c7de5edf0c376a7b8e599a842bc37fbfe4fe06f79ae632b9c9db2`


## Content

---
title: "How i was able to chain bugs and gain access to internal okta instance"
url: "https://medium.com/@eldeebxboy/how-i-was-able-to-chain-bugs-and-gain-access-to-internal-okta-instance-f2da9ab71367"
authors: ["Mmohammed Eldeeb (@malcolmx0x)"]
bugs: ["Missing authentication"]
publication_date: "2020-06-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4478
scraped_via: "browseros"
---

# How i was able to chain bugs and gain access to internal okta instance

How i was able to chain bugs and gain access to internal okta instance
mmohammed eldeeb
Follow
2 min read
·
Jun 23, 2020

368

Hello all,

this writeup about how i was bale to chain some access to gain access into a private company internal OKTA

the story begin with searching on shodan and i found an host name of something called sudo , However when i click on it i being redirect to OKTA so nothing to do with right?! the host name was ` sudo-test-classic-.....amazonaws.com

i did another recon with censys and i found IP 18.208.x.x thi IP was allowing me to get directly into sudo web page (sudo allow admin to control slack invite user deactivate user …etc)

Press enter or click to view image in full size
what can i do without admin access here? making a dirsearch using my word list i found endpoint /slack/invite
the response of this endpoint give the slack Chanel name
i made request
POST /slack/invite HTTP/1.1
Host: redacted
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
Content-Length: 83
Origin: https://redacted
Connection: close
Referer: https://redacted

{"guestEmailId":"myemail","channelName":"the name i got ","guestType":"multi"}

i got response 500 internal server error ,However i back to my email i got the invitation to their slack

Get mmohammed eldeeb’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

opened the slack i found their OKTA credential on the chat

go back to the OKTA i gain access to their okta

done? no let’s back to the sudo page after login from OKTA we are admin now and we can convert/de-active anyone from slack

Impact
allow attacker to access a slack dev channel
allow attacker to access OKTA
allow attacker to convert/de-active anyone from slack

timeline

reported on 15 dec

rewarded as critical on 19 dec

closed as resolved on 20 dec

Thanks
