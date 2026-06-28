---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-10_unauthorized-access-to-django-admin-dashboard-by-endpoint-leaked-on-github.md
original_filename: 2021-05-10_unauthorized-access-to-django-admin-dashboard-by-endpoint-leaked-on-github.md
title: Unauthorized access to Django Admin Dashboard by endpoint leaked on GitHub
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: a57b6cae6bdc37b7df1fe06cd683a013743a749748ab7be306bfacbd38ec8068
text_sha256: febd334f665bee10c885e9a8cf55e5d6f7ce5e87f629d21b21bc059146c2b5cf
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Unauthorized access to Django Admin Dashboard by endpoint leaked on GitHub

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-10_unauthorized-access-to-django-admin-dashboard-by-endpoint-leaked-on-github.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `a57b6cae6bdc37b7df1fe06cd683a013743a749748ab7be306bfacbd38ec8068`
- Text SHA256: `febd334f665bee10c885e9a8cf55e5d6f7ce5e87f629d21b21bc059146c2b5cf`


## Content

---
title: "Unauthorized access to Django Admin Dashboard by endpoint leaked on GitHub"
page_title: "Unauthorised access to Django Admin Dashboard by endpoint leaked on GitHub | by Santosh Kumar Sha(@killmongar1996) | Medium"
url: "https://notifybugme.medium.com/unauthorized-access-to-django-admin-dashboard-by-endpoint-leaked-on-github-5336969ddbbc"
authors: ["Santosh Kumar Sha (@killmongar1996)"]
bugs: ["Missing authentication", "Forced browsing"]
publication_date: "2021-05-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3667
scraped_via: "browseros"
---

# Unauthorized access to Django Admin Dashboard by endpoint leaked on GitHub

Member-only story

Unauthorised access to Django Admin Dashboard by endpoint leaked on GitHub
Santosh Kumar Sha(@killmongar1996)
Follow
4 min read
·
May 10, 2021

255

4

Hi, everyone

My name is Santosh Kumar Sha, I’m a security researcher from India(Assam). In this article, I will be describing how I was able to Unauthorized access to Admin Dashboard by endpoint leaked by GitHub.

I am now offering 1:1 sessions to share my knowledge and expertise:

topmate.io/santosh_kumar_sha

TOOLS used for the exploitation

1. Subfinder (https://github.com/projectdiscovery/subfinder)

2. httpx (https://github.com/projectdiscovery/httpx)

3. gau(Corben) — https://github.com/lc/gau

4. waybackurls(tomnomnom) — https://github.com/tomnomnom/waybackurls

5. Aquatone

Story Behind the bug:

This is the write of my Recent bug that i found . While I was doing recon for gathering all domain from internet archives using waybackurls and gau and also by using subfinder. So, i collected all the subdomain from passive and active recon. And started resolving all the domain after resolving i run the aquatone to screenshot all the url. while taking the scrrenshot I came across an screenshot where it say “Django not found” error in one the url

Here it goes:

Suppose we assume the target name is example.com where every thing is in-scope like this:
