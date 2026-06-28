---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-06_again-subdomain-takeover-via-ideanoteio.md
original_filename: 2023-09-06_again-subdomain-takeover-via-ideanoteio.md
title: Again? Subdomain takeover via ideanote.io
category: notes
detected_topics:
- command-injection
tags:
- imported
- notes
- command-injection
language: en
raw_sha256: 4c02d4a69bd8553b2a843d74ddd4288c939d293d8acc9cdf95ba16eef778cdeb
text_sha256: e8e391d12ca79e8d18c89e9fa6b2c32a0ce3c844b99ba910cc4a566128a6868e
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# Again? Subdomain takeover via ideanote.io

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-06_again-subdomain-takeover-via-ideanoteio.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `4c02d4a69bd8553b2a843d74ddd4288c939d293d8acc9cdf95ba16eef778cdeb`
- Text SHA256: `e8e391d12ca79e8d18c89e9fa6b2c32a0ce3c844b99ba910cc4a566128a6868e`


## Content

---
title: "Again? Subdomain takeover via ideanote.io"
url: "https://kresec.medium.com/again-subdomain-takeover-via-ideanote-io-6c7221161ba"
authors: ["Hasyim"]
bugs: ["Subdomain takeover"]
publication_date: "2023-09-06"
added_date: "2023-09-07"
source: "pentester.land/writeups.json"
original_index: 805
scraped_via: "browseros"
---

# Again? Subdomain takeover via ideanote.io

Again? Subdomain takeover via ideanote.io
KreSec
Follow
3 min read
·
Sep 6, 2023

10

1

Exploiting subdomain takeover Ideanote, Ideanote is a new way to work with ideas. It’s faster, more efficient, and lets you build a fully customizable idea management flow from start to finish.

Press enter or click to view image in full size
Photo by Manja Vitolic on Unsplash
Why does subdomain takeover happen?

In general, when a developer wants to connect his subdomain/rootdomain, he has to play with CNAME. Each service has a different cname,….. Read More

Exploitation

I have prepared a target list to find which subdomain has the cname “custom-domain.ideanote.io” as for the command, I only use the httpx tool.

root@kresec:~# cat randomlist |httpx -silent -cname -sc -title -mc 200
https://ideas.redacted.com [200] [9950] [Ideas] [custom-domain.ideanote.io]
https://ideas.redacted.co [200] [9330] [Ideanote] [custom-domain.ideanote.io]
https://ideate.redacted.to [200] [10296] [Redacted ****] [custom-domain.ideanote.io]
root@kresec:~# dig vuln.redacted.com | grep CNAME
vuln.redacted.com.  0  IN  CNAME  custom-domain.ideanote.io.
Press enter or click to view image in full size
Image 2. if vuln
Vulnerable identification

With the httpx output above I did some identification to find out which ones are really vulnerable to takeover. after doing various experiments i concluded for the vulnerable :
— Title : Ideanote
— Body : The subdomain ideas doesn’t exist
— Status code : 200
— Connected to this cname : custom-domain.ideanote.io

How to Custom domain

Well, besides you can see directly how to custom domain from the official article https://help.ideanote.io/article/muqxtabfk2-how-to-add-a-custom-domain, or you can follow my explanation below :

Get KreSec’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After you successfully create an account, it will be directed to a subdomain under the root domain of ideanote. Then to add a domain you can access the workspace menu, there is a section to enter the domain.

Press enter or click to view image in full size
Image 3. Custom domain

In that menu you can also change the title, description, etc

Press enter or click to view image in full size
Image 4. Setting workspace
Successful takeover

Finally, the subdomain should look like Image 5 below once it has been successfully taken over.

Press enter or click to view image in full size
Image 5. Successful takeover
Yeahh!
Thanks

Thank you very much for those of you who want to clap, share, discuss this post.
You can also help subscribe to my YouTube channel & my community
https://www.youtube.com/@kresec
https://www.youtube.com/@tegalsec1121
https://tegalsec.org/
