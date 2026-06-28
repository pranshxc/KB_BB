---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-25_subdomain-takeover-dew-to-missconfigured-project-settings-for-custom-domain-.md
original_filename: 2018-10-25_subdomain-takeover-dew-to-missconfigured-project-settings-for-custom-domain-.md
title: Subdomain takeover dew to missconfigured project settings for Custom domain
  .
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
raw_sha256: c7915a2a89df7279876fb6e485b73a141fde2e322461f0f66895866192631f7e
text_sha256: 27f0cf0a2a974c44bc345cdac64b272efe4839736c6c8c6bdc9251531a97a9d7
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Subdomain takeover dew to missconfigured project settings for Custom domain .

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-25_subdomain-takeover-dew-to-missconfigured-project-settings-for-custom-domain-.md
- Source Type: markdown
- Detected Topics: command-injection, cloud-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `c7915a2a89df7279876fb6e485b73a141fde2e322461f0f66895866192631f7e`
- Text SHA256: `27f0cf0a2a974c44bc345cdac64b272efe4839736c6c8c6bdc9251531a97a9d7`


## Content

---
title: "Subdomain takeover dew to missconfigured project settings for Custom domain ."
url: "https://medium.com/@prial261/subdomain-takeover-dew-to-missconfigured-project-settings-for-custom-domain-46e90e702969"
authors: ["Prial Islam Khan (@prial261)"]
programs: ["Flock"]
bugs: ["Subdomain takeover"]
publication_date: "2018-10-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5628
scraped_via: "browseros"
---

# Subdomain takeover dew to missconfigured project settings for Custom domain .

Subdomain takeover dew to missconfigured project settings for Custom domain .
Prial Islam Khan
Follow
3 min read
·
Oct 25, 2018

169

1

Hi readers ,

Today I will write about Subdomain takeover . It’s a common Security issue what is actually developers mistake when they left a Unused/unclaimed 3rd party Service DNS CNAME record for a subdoamin of theirs and Hackers can claim those subdomains with the help of external services it pointing to what could lead to serious issues . You can learn more about Subdomain takeover from detectify blog .

While testing flock.com I got a domain flock.co what is under flock company . So I stared looking at it’s subdomains and got subdomain newdev.flock.co . When I visited the subdomain in browser I got a error like below screenshot :-

Press enter or click to view image in full size
Error Page

This took my attention . So I checked the DNS record for this domain .

$ dig newdev.flock.co
; <<>> DiG 9.10.6 <<>> newdev.flock.co
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 13182
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 1
;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;newdev.flock.co. IN A
;; ANSWER SECTION:
newdev.flock.co. 299 IN CNAME cname.readme.io.
cname.readme.io. 299 IN CNAME readme-cache-prod-1392018356.us-east-1.elb.amazonaws.com.
readme-cache-prod-1392018356.us-east-1.elb.amazonaws.com. 59 IN A 52.0.214.29
readme-cache-prod-1392018356.us-east-1.elb.amazonaws.com. 59 IN A 52.5.249.117
;; Query time: 69 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Mon Jul 09 04:58:06 +06 2018
;; MSG SIZE rcvd: 175

From above record we can say the subdomain is pointing to CNAME cname.readme.io . So I start looking at custom domain documents on readme.io website to understand how they works . From their document I understand that :-

You need a subdomain pointing to your readme.io subdomain [yoursubdomain.readme.io] .
Your subdomain should be configured in domains settings in following page https://dash.readme.io/project/<project
_Name>/v1.0/domains

So to takeover I need to check if cname.readme.io is alreday claimed of not . But Unfortunately it was already claimed :( . But I have seen many such services doesn’t force users to verify their ownership of domains by using same CNAME txt record like their service subdomain . So still there’s a hope .

Get Prial Islam Khan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I opened a account in readme.io and I got a subdomain newdev.readme.io . Then I go to domains settings https://dash.readme.io/project/newdev/v1.0/domains and in Custom Domain Field used newdev.flock.co as value and save changes .

Now when I visited newdev.flock.co It redirected me to http://newdev.flock.co/inactive this page what saying now that Not Yet Active.

Press enter or click to view image in full size
See page title ;)

This is showing as I am using a trail account . In the webpage title you will see my project name what I used while creating the project . So now this domain is serving my contents from newdev.readme.io project page .

How to avoid such issues ? :- Always update your DNS records . remove CNAME or any other DNS records what is not in used .

If you find a security vulnerability feel free to contact them via security@flock.com

Thanks for reading . You can find me on Facebook anytime :- https://www.facebook.com/prial261
