---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-06_self-xss-to-stored-xss-think-out-the-box.md
original_filename: 2019-08-06_self-xss-to-stored-xss-think-out-the-box.md
title: self XSS to stored XSS [ think out the box]
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
raw_sha256: b0e255c16c8709f932ffaedaebd24060d4fabb0d83022c112a7d63abd484c5a6
text_sha256: f5568411734450200f41e7c30c6f51002a5c57efc1eb46c09776240f93526da3
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# self XSS to stored XSS [ think out the box]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-06_self-xss-to-stored-xss-think-out-the-box.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `b0e255c16c8709f932ffaedaebd24060d4fabb0d83022c112a7d63abd484c5a6`
- Text SHA256: `f5568411734450200f41e7c30c6f51002a5c57efc1eb46c09776240f93526da3`


## Content

---
title: "self XSS to stored XSS [ think out the box]"
url: "https://medium.com/@protostar0/self-xss-to-stored-xss-think-out-the-box-44b094f113f9"
authors: ["Abdelhak Kharroubi"]
programs: ["TIBCO"]
bugs: ["Self-XSS", "Stored XSS"]
publication_date: "2019-08-06"
added_date: "2022-10-12"
source: "pentester.land/writeups.json"
original_index: 5096
scraped_via: "browseros"
---

# self XSS to stored XSS [ think out the box]

self XSS to stored XSS [ think out the box]
Abdelhak Kharroubi
Follow
2 min read
·
Aug 6, 2019

3

first , i found self xss in wiki page of tibco web site ,

when create page in wiki ,the javascript code executed only when edit this page . [the edit mode have some permission to use some html tags with filter ]

and because its a self xss , i didn't send the report to security team;

after one week ,i remember this bug and , i was thinking if other user have possibility to edit this page ,

when i test it , i get that any user can edit my wiki page with code javascript in edit mode . :) :) .

that can be stored xss with some fishing message like ‘ edit this page ‘.

Step to reproduce

see the video

1-login in your account in https://community.tibco.com/
2- go add new wiki
3-click to create page
4-click in source code
5-past this payload

<noscript><p title=”</noscript><svg/onload=alert(document.cookie)>”>

+ add some fishing message like ( edit my source code if you can or change text type plz)

Get Abdelhak Kharroubi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

6-go to simple vision and back to source (look to the video
the javascript code will executed

7-the victim with other account can edit page wiki when will he go to source code of wiki will executed java script

ps (any user can edit the wiki of attacker and see the code source )

part 1

part 2

poc
Press enter or click to view image in full size
Press enter or click to view image in full size

Hall of Fame

https://www.tibco.com/security/disclo...
