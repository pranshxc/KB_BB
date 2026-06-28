---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-05_incident-response-during-christmas.md
original_filename: 2021-01-05_incident-response-during-christmas.md
title: Incident Response during Christmas
category: documents
detected_topics:
- command-injection
- automation-abuse
- graphql
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- graphql
- api-security
- cloud-security
language: en
raw_sha256: 7be33a72a994e85959211104588275ecad513236e2eac0fb5b1929d0b1397cc3
text_sha256: 435905162c1331ed6e7097d079982454810a11ee0d98a72e828baa8a3fda2676
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Incident Response during Christmas

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-05_incident-response-during-christmas.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, graphql, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `7be33a72a994e85959211104588275ecad513236e2eac0fb5b1929d0b1397cc3`
- Text SHA256: `435905162c1331ed6e7097d079982454810a11ee0d98a72e828baa8a3fda2676`


## Content

---
title: "Incident Response during Christmas"
url: "https://tmosh.medium.com/incident-response-during-christmas-33c7fabb1429"
authors: ["TMO"]
bugs: ["Subdomain takeover"]
publication_date: "2021-01-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4027
scraped_via: "browseros"
---

# Incident Response during Christmas

Incident Response during Christmas
… or how i have taken over 30 subdomains of four global Fortune 500 companies.
TMO
Follow
7 min read
·
Jan 5, 2021

5

2020 has been a tough year for all of us. Digital transformation was driven by COVID-19 and we increasingly seeing security incidents and ransomware attacks coming up in the news.

That is a good peg to check how global companies do on incident response during the Christmas vacation time. While also many hacking groups take some days off during that time, other groups become even more active —naturally it can be said that company response and mitigation times increases during Christmas time and there is a lower chance for the attackers to get detected and a possible higher success rate on attacks.

Target selection

I wanted to test this thesis and have picked some companies at random to test their response time to vulnerabilities in between the years. While response time to a responsible disclosure is not the same as a response to a real security incident I wanted to test how the companies react if you report a critical bug. I have not chosen companies which run big bug bounty programs as this should increase my chance finding a higher risk bug. However I’ve looked at companies which might at least have a Security Incident Response Team or a Responsible Disclosure Policy (except Company B).

Get TMO’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Company A | Chemical Sector | Responsible Disclosure Policy
Company B | Consumer Goods | No SIRT/RDP
Company C | Multi-Industry (Mainly Tech Sector)| Private VDP
Company D | Multi-Industry (Mainly Tech Sector) | Responsible Disclosure Policy

Scope

Always set a proper scope and do not try to hunt every possible bug. I wanted to focus on subdomain takeovers as those bugs are easy to demonstrate, and have a high impact — but are also quite easy to fix and mitigate. With a subdomain takeover attackers can for example:

serve malicious content with the impersonation of the company (reputation risk)
setup phishing pages and target employees and/or customers (implicit trust of the domain)
Steal cookies (Cookies which are bound to the top-level domain)

The list is not exhaustive, but just well-known examples. Just imagine the possible impact if somebody would have taken over a domain during the first Christmas week and would be able to control it until new years eve — that is roughly two weeks of control! I concentrated only on the two main domains of the company — the local domain as well as their international domain (.com); so all subdomain takeovers demonstrated below have been found on domain with the highest risk and impact to the company.

Methodology

Once selecting the targets I’ve followed my usual methodology for gathering possible subdomains:

amass (no brute option)
Sublister
Subfind3r
Assetfinder
Domains from crt.sh
Domains from certspotter
AltDNS over all the unique domains (236 entries)
Custom wordlist (2.7M entries)
MassDNS over all unique Domains found so far

As one might expect the input list for MassDNS was quite long so it took some time to resolve all the domains. MassDNS is pointing to a local resolver which is running Unbound — if the company runs their own DNS servers such an action is quite easy detectable. Your request will first go to the IANA root servers, from there down to the top-level domain name server and down to the authoritative name server of the company. My server was sending around 40K packets/second — so do not use this if you want to run undetected.

Finding vulnerable subdomains

After MassDNS was finished I was presented with a list in the following format (example):

subdomain1.company.com. A 192.0.2.1
subdomain2.company.com. A 192.0.2.2
subdomain3.company.com. CNAME subdomain4.company.com.
subdomain4.company.com. A 192.0.2.3

For a subdomain takeover I was mainly interested in the CNAME entries and want to check if those point to a service which is unused / not claimed. I started aquatone to allow for a visual identification of the targets but in parallel I grepped for all CNAME entries and run a quick for loop with dig to check for all domains which don’t resolv correctly (NXDOMAIN):

for domain in `cat massdns.txt | grep CNAME | cut -d" " -f1 | sed 's/\.$//'`
do
  echo -n "Subdomain: $domain";
  dig $domain | "grep status"
done | grep NXDOMAIN

This little multi-liner puts out all CNAMES which are present in the DNS system, but do not resolve to an actual IP. All of those i manually analyzed then (via dig <subdomain>) and checked to which service they are pointing.

Subdomain takeovers are also possible if the domain does not resolve as NXDOMAIN, but succeeds with NOERROR — however such a possibility you can only detect via visual identification.

I’ve come across three different services and will describe how i have taken over the subdomains.

Press enter or click to view image in full size
Subdomain pointing to .cloudapp.azure.com

The CNAME entry was pointing to <servicename>.<region>.cloudapp.azure.com— however this subdomain did not resolve to any service, therefore the service was unused in Microsoft Azure. I have deployed a new virtual machine in Microsoft Azure, installed nginx and claimed the unused DNS Name:

Press enter or click to view image in full size
Subdomain takeover of cloudapp.azure.com
Subdomain pointing to .azurewebsites.net

I had several services pointing to <servicename>.azurewebsites.com. This subdomain is used by Microsoft Azure App Services:

Azure App Service enables you to build and host web apps, mobile back ends, and RESTful APIs in the programming language of your choice without managing infrastructure. It offers auto-scaling and high availability, supports both Windows and Linux, and enables automated deployments from GitHub, Azure DevOps, or any Git repo.

We cannot easily deploy a virtual machine to proof the subdomain takeover, but we need to deploy an Azure Service. I took the easy approach and followed the original Microsoft Quickstart Guide to deploy an Hello World application as a Proof-of-concept. Afterwards I added the custom domain to the App Service and i was able to control the subdomain.

Press enter or click to view image in full size
Subdomain takeover of azurewebsites.com
Subdomain pointing to unused domain

The last one was a CNAME entry subdomain.company.com which was pointing to company-abc.com. This domain however was not registered (probably expired) and i was able to register the domain directly with my preferred domain registrar. I pointed the domain to my personal server as a proof-of-concept.

Response times

Finally we come to another interesting part: response times. I am not disclosing any company names.

Press enter or click to view image in full size
Response Time

As we can see above, only one company has fixed the subdomain takeover of two domains up to today. This was the company which was running a private VDP at a crowd sourcing platform.

The two companies which have a CERT team confirmed the vulnerability and forwarded it internally, however the subdomains are still pointing to my services and the bugs have not been fixed.

The company without a CERT team has not yet reached out back to me, i have tried contacting them via different channels and also tried reaching out directly to some contacts on LinkedIn.

Conclusion

A subdomain takeover is still a high impact action — but it is even quite easy to mitigate. As a company you are currently not using the subdomain (that is why it was possible to take it over), so you cannot loose anything by any mitigation— if you do not want to delete it, at least point it to your primary domain. This action you can execute within minutes (while it takes hours until the TTL times out) but it effectively secures your environment while you in the back can clarify who ordered that subdomain and if it can be completely deleted from the DNS system or if it must be pointed to another service. As a company you have full access to your DNS Zone records and you should either automatically monitor or on a regular base review your subdomains.

Taking the impact of a subdomain takeover into account I was somehow shocked on the response times. All actions and responses only happened after the Christmas period, no responses or actions have been taken, from any of the companies, on the actual Christmas days. One reason for this might be that a reported bug does not get assigned the same criticality like an actual security incident — however, i was expecting something else from global players. We can only anticipate on the response time of an actual breach, hopefully it will never happen and the company acknowledge and recognize that IT Security is not an on-off, but a topic where you continuously need to invest and spend resources. If you do not do it — be sure, attackers do.
