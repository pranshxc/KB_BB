---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-01_mining-takeovers-for-fun-and-profit.md
original_filename: 2023-03-01_mining-takeovers-for-fun-and-profit.md
title: Mining Takeovers for Fun and Profit
category: documents
detected_topics:
- cloud-security
- sso
- idor
- command-injection
- rate-limit
- automation-abuse
tags:
- imported
- documents
- cloud-security
- sso
- idor
- command-injection
- rate-limit
- automation-abuse
language: en
raw_sha256: 6dad04f8abbbd6894a607cb500b774e61b11033335b5c02265f150d3ddbeeace
text_sha256: a96d9c0bab0d207ea656d133176f2837a249a30c9e48d8a3aaca279251e6ace6
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Mining Takeovers for Fun and Profit

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-01_mining-takeovers-for-fun-and-profit.md
- Source Type: markdown
- Detected Topics: cloud-security, sso, idor, command-injection, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `6dad04f8abbbd6894a607cb500b774e61b11033335b5c02265f150d3ddbeeace`
- Text SHA256: `a96d9c0bab0d207ea656d133176f2837a249a30c9e48d8a3aaca279251e6ace6`


## Content

---
title: "Mining Takeovers for Fun and Profit"
page_title: "Mining Takeovers for Fun and Profit | FireShell Security Team"
url: "https://fireshellsecurity.team/mining-takeovers-for-fun-and-profit/"
final_url: "https://fireshellsecurity.team/mining-takeovers-for-fun-and-profit/"
authors: ["Artur Marzano (@MacmodSec)"]
bugs: ["Subdomain takeover"]
publication_date: "2023-03-01"
added_date: "2023-03-06"
source: "pentester.land/writeups.json"
original_index: 1444
---

![Diamonds.png](https://i.imgur.com/3gtnDYk.png)

## Introduction

This article describes an experiment aimed at finding domains likely vulnerable to _DNS takeover_ , a well-known technique that can be used to steal decomissioned, but active domains. In this experiment I will show how I was able to find with little effort more than 200 domains that could be theoretically taken over across different providers and parent domains by using data from a public search tool ([SecurityTrails](securitytrails.com)) and an open-source repository ([can-i-take-over-dns](https://github.com/indianajson/can-i-take-over-dns)).

_Please note that I did not find any new vulnerabilities nor develop any sort of attack tools or techniques during this research_. I just analyzed what was already there, not being responsible in any way for whatever damages could be caused by the usage of the methods described below.

## Background

A _Subdomain takeover_ is a vulnerability that happens when there is a CNAME record pointing a domain `app.site.com` to a domain `name.b.com`, in which domain `b.com` belongs to a third-party platform that allows their customers to choose subdomains of their `b.com` zone for usage with their services.

For example, let’s imagine we are the current owners of `site.com` working with a provider named `host.net`. We decide to use a managed application service from `host.net` named `service` to host our app `myapp`. After configuring the service in `host.net`, it gives us a subdomain in their `service.host.net` zone hosting our app - let’s say `myapp.service.host.net`. We’d like to access our app through our domain, not theirs, so we create a CNAME in the `site.com` zone pointing `app.site.com` to `myapp.service.host.net`.

Later on we decide to remove our app from `host.net`, releasing the domain name in their zone. If we don’t remember to remove the CNAME (we won’t), another customer of `host.net` can come in and set up their own app named `myapp` in the managed app service. They would be able to host any content they wanted under our `app.site.com` subdomain, effectively taking over it.

![SubdomainTakeover.gif](https://i.imgur.com/Pw7OE5u.gif)

A _DNS takeover_ is a similar vulnerability, but instead of allowing an attacker to hijack the contents that users see when they access one of your subdomains, it allows attackers to gain control over an entire zone, being able to create any records they want to. It happens when an entity registers a domain in their registrar, delegates administration of the domain to another more convenient provider, and in the future deletes the domain in that provider. Since the delegation is still in the registrar, an attacker can create an account in the provider and recreate the domain.

For example, suppose we are a loyal customer of the `cloud.net` provider. We just bought `bigcorp.com` for the next year from GoDaddy (our preferred registrar), but we actually want to manage the `bigcorp.com` zone using our `cloud.net` provider and not GoDaddy. Next we would have to create a zone for `site.com` in our `cloud.net` provider, and then access GoDaddy and create an `NS` record delegating the `bigcorp.com` site to the nameservers of `cloud.net`, which could be `ns1.cloud.net` and `ns2.cloud.net`.

Suppose we get tired of `bigcorp.com` and decide to use `bigcorp.io` instead. We would keep paying for `bigcorp.com` for the following years, since we don’t want to lose the name. Then at some point someone would remove the `bigcorp.com` zone from the `cloud.net` portal, thinking it has no business being there if it’s not in use, thus creating what is called a **lame delegation** \- when a domain points to nameservers that don’t actually respond authoritatively to queries for that domain. If an attacker realizes that `bigcorp.com` has a lame delegation to `cloud.net` nameservers, this person could create an account in our provider and recreate `bigcorp.com`, being able to create all sorts of records there. For instance, they would be able to create subdomains of `bigcorp.com` for phishing purposes, or create an `MX` record to intercept all emails directed to `bigcorp.com`.

![DNSTakeover.gif](https://i.imgur.com/3zitvvi.gif)

In case you want to learn more before going further, [Patrik Hudak’s blog](https://0xpatrik.com/) has some pretty good educational articles describing these attacks, including other ways to find candidates for takeover with subdomain enumeration techniques, and how to develop other attacks after a subdomain takeover is exploited.

## The Problem & The Plan

I wanted to know what could be done to better understand, and possibly help mitigate risks of DNS takeovers in the internet. Of course it’s an unreasonable goal, but one can dream, right? The first question that I wanted to answer was whether we could come up with a simple and effective way to find domains that were likely vulnerable to DNS takeover.

The problem is that no one really knows which records exist in a registrar apart from the registrar itself, since it owns the zonefiles. One could find a huge list of random domains somewhere and scan them for possible DNS takeover scenarios, but this is too time-consuming and in most cases unlikely to yield good results. To find possible scenarios we need a way to dump a list of domains that delegate their zones to nameservers of vulnerable providers.

At this point I was just thinking, but then I was casually talking to my friend Kali Nathalie about pentesting the other day, and she mentioned that _SecurityTrails_ had a subdomain search tool with a pretty good database, so I browsed to it and found that, not only does it have a great database, but it also provides _reverse NS_ and _reverse CNAME_ lookups, our missing piece of the puzzle. That’s something you don’t find very often, since the DNS protocol does not specify these sorts of lookups - there’s no reason why it should, really.

Now the plan was:

![Plan.png](https://i.imgur.com/vHpro0k.png)

First I extracted all nameservers of the vulnerable providers from indianajson’s [can-i-take-over-dns](https://github.com/indianajson/can-i-take-over-dns) repository. His repository currently documents the state of 28 providers regarding DNS takeover, 19 of which are currently listed as “Vulnerable” or “Edge Case”. Besides the “Not Vulnerable” nameservers, all CloudFlare nameservers were ignored for this step, since a successful attack is unlikely due to their high number of nameservers.

I had a list of 379 nameservers from 18 providers to search:

**Provider** | **# of nameservers evaluated**  
---|---  
Azure | 228  
NS1 | 72  
Google Cloud | 28  
DNSMadeEasy | 7  
Hurricane Electric | 5  
DNSimple | 4  
Dotster | 4  
EasyDNS | 4  
000Domains | 4  
Bizland | 4  
Name.com | 4  
Digital Ocean | 3  
Domain.com | 2  
TierraNet | 2  
Reg.ru | 2  
Yahoo Small Business | 2  
Linode | 2  
MyDomain | 2  
  
For the top 3 providers in the table I just guessed their nameservers by trial and error since they weren’t explicited in indianajson’s repository, so the real number could be more or less than what I found.

Also note that, in most cases, many nameservers in the same provider will serve records from the same zonefiles, some acting as backups in case others fail. That should not stop us from analyzing them though, since some domains might not appear in the database as being associated with all nameservers of their provider. As long as we have the time to do so, the chances are we will be getting more domains this way.

I decided to try one of the Azure nameservers manually, going through the pages in SecurityTrails and dumping the domains from the search results table with Javascript:
  
  
  var my_rows = document.querySelectorAll("tbody>tr a")
  var my_domains = []
  
  my_rows.forEach((row) => {
  row.childNodes.forEach(
  (link) => {
  my_domains.push(link.textContent)
  }
  )
  })
  
  console.log(my_domains.join("\n"))
  

In the first nameserver I tried I found 3728 domains pointing to it. Then I ran `dig` over all 3728 domains to see whether any of them returned a `SERVFAIL` or a `REFUSED` error:
  
  
  $ cat domains-poc.txt | while read name; do res=$(dig $name  | grep -Po 'status: [^,]+'); echo "$name $res"; done > results.txt
  

In the `results.txt` I found 8 zones vulnerable to DNS takeover reporting `SERVFAIL`s - 3 under `.com`, 1 under `.com.br`, 1 under `.com.np` and the rest in `.app`, `.bg`, `.dev`. This was very scary as it was so easy to find. I double-checked them with `dig +norecurse <DOMAIN> NS` and indeed they were pointing to the nameserver I was testing. I even logged into my Azure account to check whether I could verify that the names were available in the zone registration page, and indeed they were.

I thought that this could be a red flag - some nameservers could be authoritative for hundreds of thousands of zones, so 8 zones that could be taken over in a small set of 3728 (0.2%) seemed like a lot.

Now, if I wanted to step up the game, I’d need deeper access to SecurityTrail’s database. All I had at the moment was a search box limited to 10.000 results per query, paginated across pages limited to 100 results. Besides that, SecurityTrails’ API is limited to 50 queries per month and doesn’t include the SQL API unless you pay a minimum of U$500 for a subscription, which is _slightly_ out of my budget for personal research projects.

I decided to go the easy way and just stick to the 10.000 limit, since I figured I wouldn’t be able to run billions of DNS queries in a short time anyway. So I made a quick Selenium script using the [Undetected Chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) webdriver to scrape the data from SecurityTrails (this wouldn’t be so easy without Selenium, since SecurityTrails is behind CloudFlare):
  
  
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as ec
  from selenium.webdriver.common.by import By
  import undetected_chromedriver as uc
  import re
  
  
  options = uc.ChromeOptions() 
  
  driver = uc.Chrome(use_subprocess=True, options=options)
  driver.get("https://securitytrails.com/")
  driver.maximize_window()
  driver.add_cookie({
  "name": "SecurityTrails",
  "value": "<My SecurityTrails Session Cookie>"
  })
  
  
  def reverse_ns_sample(domain, output_file):
  domains = []
  
  lookup_url = f"https://securitytrails.com/list/ns/{domain}"
  
  driver.get(lookup_url)
  
  wait = WebDriverWait(driver, 12)
  driver.implicitly_wait(5)
  
  end_of_page = 100
  end_of_results = -1
  pagination_text = ''
  
  while end_of_page != end_of_results:
  sample = driver.find_elements(By.CSS_SELECTOR, "tbody>tr a")
  try:
  page_domains = [el.text for el in sample]
  except Exception:
  pass
  
  output_file.write('\n'.join(page_domains) + '\n')
  domains += page_domains
  
  pagination = wait.until(
  ec.presence_of_element_located(
  (By.CLASS_NAME, 'pagination-details')
  )
  )
  pagination_text = pagination.text.replace('\n', ' ').replace('\r', ' ')
  pagination_numbers = re.search(
  r'- ([\d,+]+) of ([\d,+]+) results',
  pagination_text
  ).groups()
  end_of_page = pagination_numbers[0]
  end_of_results = pagination_numbers[1]
  
  next_page_btns = driver.find_elements(By.CSS_SELECTOR, ".tooltip li a")
  try:
  for btn in next_page_btns:
  if btn.text == '›':
  btn.click()
  except Exception:
  pass
  
  n_domains = len(domains)
  print(f'[+] {n_domains} domains written to output file.')
  
  return domains
  
  
  total_n_domains = 0
  with open('nameservers.txt') as f:
  nameservers = list(map(lambda x: x.rstrip(), f.readlines()))
  
  with open('output.txt', 'a+', encoding='utf-8') as output_file:
  for nameserver in nameservers:
  print(f'[+] Fetching results from {nameserver}')
  try:
  reverse_ns_sample(nameserver, output_file)
  total_n_domains += 1
  except Exception as e:
  print(f'[+] Error on nameserver {nameserver}: "{e}"')
  
  driver.quit()
  
  print(f'[+] Found a total of {total_n_domains}.')
  

I was pretty surprised that I wasn’t blocked from the platform after a little more than 48 hours of queries, but these were all legitimate queries made by my browser after all. Or maybe I’m lying, I just made up this code, and in reality I went through thousands of pages of results manually, copying and pasting domains. Who knows…

After that it was time to actually check these domains. I was not going to do it sequentially with `dig`, because I suspected half a million queries would take some time to finish, so I used [zdns](https://github.com/zmap/zdns) to make the queries (and [jq](https://github.com/stedolan/jq) to analyze the results):
  
  
  $ cat output.txt | ./zdns SOA --threads 10 --name-servers=8.8.8.8,8.8.4.4 > soa-results.json
  

Note that I lowered the number of threads here instead of using the default of 1000 threads because I was worried that the queried servers would start refusing queries if I sent too many in a short amount of time. That would generate false positives, which wasn’t what I wanted. I’m not sure whether they do that or not, but it seemed possible.

Then I filtered for `SERVFAIL`s and `REFUSED`s:
  
  
  $ jq -r 'select(.status == "SERVFAIL" or .status == "REFUSED") | "\(.name),\(.status)"' soa-results.json > lame-names.txt
  

The last thing I needed to do was get the nameservers of our lame names, in order to really validate that the information we got from SecurityTrails was accurate:
  
  
  $ cat lame-names.txt | awk -F',' '{print $1}' | ./zdns NS --iterative --threads 3 > lame-ns-results.json
  

Finally I just went through these results, removing the ones that pointed to nameservers that weren’t into our base set. Whatever domains were left in the list were likely vulnerable to takeover :-)

## Results

For this analysis, I considered that a domain is _likely vulnerable to takeover_ (LVT) if:

  1. Its NS record points to nameservers extracted from the crowdsourced repository of vulnerable providers, and
  2. The provider refuses to answer a SOA query for the domain with a `SERVFAIL` or `REFUSED` status (lame delegation)

This definition is pretty good for our purposes, but note that false positives could arise from it - the `can-i-take-over-dns` repository could not be a completely accurate source, or a provider might refuse to answer a query for reasons other than the zone being available for register in their platform, such as the domain being “blacklisted/suspended” or rate-limiting being applied.

This experiment generated a set of 414.537 unique domains to analyze, which were distributed as follows (top 15):

![AnalyzedDomainsDistribution.png](https://i.imgur.com/mA0N3c9.png)

From the base set of unique domains, the vast majority of domains (414.212 - 99.9%) responded to the SOA query with a _NOERROR_ (98.72%) or _NXDOMAIN_ (1.19%) status, which is pretty good, but 324 domains returned a _SERVFAIL_ and 1 domain returned a _REFUSED_.

I went on to double-check the nameservers of these 325 domains to filter out the ones that weren’t actually pointing to our set of vulnerable nameservers. 112 (34%) of these domains had NS records that weren’t in our base set of nameservers, leaving us with **213 domains that were likely vulnerable to takeover**. _I won’t be releasing the list of domains for obvious reasons_ , but here’s how they were distributed in case you’re curious about it:

![LVTDomainsPerProvider.png](https://i.imgur.com/DJY8Ru5.png)

And here’s the full list of the parent domains in which the LVT domains were found:

**Parent domain** | **# of LVT domains**  
---|---  
com | 132  
net | 13  
org | 11  
xyz | 5  
io | 5  
com.br | 4  
ng | 3  
ml | 3  
nu | 2  
nl | 2  
info | 2  
com.fj | 2  
co.uk | 2  
biz | 2  
us | 1  
uk | 1  
team | 1  
solutions | 1  
shop | 1  
pro | 1  
org.fj | 1  
net.fj | 1  
in | 1  
im | 1  
host | 1  
fm | 1  
fi | 1  
eu | 1  
dev | 1  
com.co | 1  
com.au | 1  
co.nz | 1  
co.in | 1  
co.fk | 1  
co | 1  
click | 1  
cc | 1  
ca | 1  
bot | 1  
az | 1  
  
## Mitigation ideas

It’s clear that lame delegations are a problem for registrars, and that vulnerability to DNS takeovers is a problem for providers of DNS services. Below are some ideas to mitigate this sort of issue:

  * _Lame Delegation Cleanup_. Registrars can continuously check NS records in their zones for lame delegations, remove the corresponding records and notify the corresponding customers. If an NS record exists for a domain, but the associated nameservers don’t answer to queries for that domain, it has no function and should be deleted as quickly as possible. This is allegedly done by some registrars, but the protocols for it have to be reviewed and standardized considering this kind of risk - some entities can take up to 30 days notifying customers of the issue to effectively remove a lame NS record from their zones.

  * _Nameserver Segregation_. Providers can distribute their zones into sets of multiple distinct nameservers and assign them to customers randomly in a way that it becomes impractical, or even impossible, for an attacker to carry out DNS takeovers due to the high amount of attempts the attacker would have to perform in order to get at least one of the nameservers that were registered as authoritative for the affected domain. AWS and CloudFlare seem to implement controls which are similar to this approach. _A simple way to extend this approach and effectively mitigate the issue_ : when processing the request for a new zone, the provider could just query the domain just like we did in this article to figure out whether it currently has a lame delegation to a subset of its nameservers. Then, if so, the provider could just _avoid_ registering the zone in that subset of nameservers, using other nameservers from their pool instead. If the provider has no available nameservers to hand out after this procedure, then it should just return an error.

  * _Detection & Response_. Providers can keep logs of who is claiming which zones and develop automatic detection of strange patterns, such as a recently-removed zone being claimed by a different customer than the previous one, or the same customer trying to register many recently-removed zones previously owned by other customers in a short amount of time. This can then be used to notify customers of suspicious behavior and guide possible restrictive actions.

  * _Developing Awareness_. Vulnerable providers can warn customers explicitly when they try to remove a zone, informing them that they must remove the NS record at their registrar _prior_ to removing the delegated zone.

## Future work

### Expanding Scope

This work was executed with limited resources and during the course of 3 days. To better understand this sort of issue it would be beneficial if someone were to try expanding it to a larger sample of domains, for example in the order of tens of millions. I imagine that one could possibly find many more LVT domains by having access to [SecurityTrails’ SQL API](https://docs.securitytrails.com/docs/examples-2) and a big quota.

### Automatic Takeover Verification

A tool could be written to check whether a domain is really available for registry in a provider using the provider’s API, or even go one step further and actually perform the takeover automatically. In cases where the provider implements some sort of nameserver segregation, the tool could try repeatedly until it gets the right nameserver. This kind of tool would make it easier to verify this sort of situation directly, although it might be a little bit hard to maintain, since it’s likely that providers will make changes to their infrastructure from time to time, possibly even mitigating takeover scenarios.

### Find Subdomain Takeovers

The same kind of mass experiment can be performed for the case of subdomain takeovers, although it was out of the scope of this work. If one knows of a base target domain associated with a service vulnerable to subdomain takeovers (like those described in EdOverflow’s [can-i-take-over-xyz](https://github.com/EdOverflow/can-i-take-over-xyz) repo), one could use a reverse CNAME database such as SecurityTrail’s to find every domain that points to this service. For example, suppose Azure AppServices - which uses `.azurewebsites.net`, a domain with more than 1 million subdomains - is vulnerable. One could use SecurityTrails’ database to get all of the more than 1 million subdomains of `.azurewebsites.net`, check which ones fit the pattern of subdomain takeover (such as those returning `NXDOMAIN`), and then check whether these domains have reverse CNAMEs that could be taken over. This could be an exhaustive task in some cases or not so much in others, depending on the size of the subdomain space for the analyzed service and on the % of dangling CNAMEs pointing to its subdomains.

### Other Data Sources

After writing this article I found other data sources that provide interesting reverse lookups such as the reverse NS lookup that was used in this analysis. Although some of these are somewhat limited/expensive, data from these sources could be used instead of SecurityTrails’ to perform similar analyses, comparing or complementing the results:

**Source** | **Interesting Lookups** | **Limits**  
---|---|---  
[SecurityTrails](https://securitytrails.com) | Reverse NS, Reverse CNAME, Reverse MX | Max 10.000 results/lookup  
[ViewDNS](https://viewdns.info) | Reverse NS, Reverse MX | Unknown  
[DomainTools](https://research.domaintools.com/) | Reverse NS | Subscription members only  
[WhoisXMLAPI](https://www.whoisxmlapi.com/) | Reverse NS, Reverse MX | 5 pages of 300 results/minute  
[DNSLytics](https://dnslytics.com/reverse-ns) | Reverse NS, Reverse MX | Subscription members only (max 2.500 results/lookup)  
  
Some time later I improved the first draft of the scraper used in this analysis and added basic support for ViewDNS and WhoisXMLAPI lookups. I won’t be maintaining it for long probably, but it can be a starting point for others trying to perform this kind of analysis: [Macmod/NameScraper](https://github.com/Macmod/NameScraper).

The [Forward DNS dataset](https://opendata.rapid7.com/sonar.fdns_v2) from Rapid7’s Project Sonar could also be an interesting source of information for similar analyses. Although they don’t provide a web-based search tool, they provide daily compressed datasets of all sorts of DNS lookup results, in JSON, and going many years back. This data could be analyzed with `zgrep` and `jq` \- like what @buckhacker did in 2018 in his [How to do 55.000+ Subdomain Takeover in a Blink of an Eye](https://medium.com/@thebuckhacker/how-to-do-55-000-subdomain-takeover-in-a-blink-of-an-eye-a94954c3fc75) article.

## Conclusion

Although not widely exploited yet, DNS takeovers pose a relevant risk for customers, registrars and providers of DNS services. That risk could be increased by attackers having access to public databases mapping _nameservers_ to _domains for which they are authoritative_ (reverse NS lookups), and by the fast pace with which DNS zones are being registered and removed from DNS providers. Registrars and providers have the means to verify and mitigate these risks in their DNS services, but they are probably still not taking action as quickly and as effectively as they should to protect their customers.

Finally, about the title of the article - I did have lots of _fun_ doing this, but I didn’t really _profit_ anything, so for now I just hope this article was instructive for readers and that this will inspire researchers, registrars and providers to think about the problem =)

__[Data Analysis](/data-analysis/) , [DNS](/dns/) , [DNS Takeover](/dns-takeover/) , [Research](/research/) , [Subdomain Takeover](/subdomain-takeover/) , [Takeover](/takeover/)
