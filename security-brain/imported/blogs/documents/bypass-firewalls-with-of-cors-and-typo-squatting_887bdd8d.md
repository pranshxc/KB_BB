---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-02_bypass-firewalls-with-of-cors-and-typo-squatting.md
original_filename: 2023-01-02_bypass-firewalls-with-of-cors-and-typo-squatting.md
title: Bypass firewalls with of-CORs and typo-squatting
category: documents
detected_topics:
- cors
- supply-chain
- jwt
- idor
- ssrf
- command-injection
tags:
- imported
- documents
- cors
- supply-chain
- jwt
- idor
- ssrf
- command-injection
language: en
raw_sha256: 887bdd8d0ad10aadefeab996b272801db42d5fd9cd811344b0ec1c00bfa5b959
text_sha256: 6677c9311748a8456843056f7b71c4ef13d4d191f4b0f7625caeda50db9c3442
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: true
---

# Bypass firewalls with of-CORs and typo-squatting

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-02_bypass-firewalls-with-of-cors-and-typo-squatting.md
- Source Type: markdown
- Detected Topics: cors, supply-chain, jwt, idor, ssrf, command-injection
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: True
- Raw SHA256: `887bdd8d0ad10aadefeab996b272801db42d5fd9cd811344b0ec1c00bfa5b959`
- Text SHA256: `6677c9311748a8456843056f7b71c4ef13d4d191f4b0f7625caeda50db9c3442`


## Content

---
title: "Bypass firewalls with of-CORs and typo-squatting"
page_title: "Bypass firewalls with of-CORs and typo-squatting ◆ Truffle Security Co."
url: "https://trufflesecurity.com/blog/of-cors/index.html"
final_url: "https://trufflesecurity.com/blog/of-cors"
authors: ["Chris Grayson", "Truffle Security (@trufflesec)"]
programs: ["Tesla"]
bugs: ["CORS misconfiguration"]
publication_date: "2023-01-02"
added_date: "2023-01-06"
source: "pentester.land/writeups.json"
original_index: 1708
---

[One leaked credential can silently compromise your entire SaaS stack. Find out the 6 critical risks you need to know.](https://trufflesecurity.com/library/guides/exposed-nhi-saas-worms-in-stack)

[](../)

TRUFFLEHOG

[CUSTOMERS](../customers)

COMPANY

RESOURCES

[LOG IN](https://trufflehog.org/)

[Contact Us](https://trufflesecurity.com/contact)

[One leaked credential can silently compromise your entire SaaS stack. Find out the 6 critical risks you need to know.](https://trufflesecurity.com/library/guides/exposed-nhi-saas-worms-in-stack)

[](../)

Chris Grayson

### [The Dig](../blog)

January 3, 2023

# Bypass firewalls with of-CORs and typo-squatting

# Bypass firewalls with of-CORs and typo-squatting

Chris Grayson

January 3, 2023

#### We used a new Appsec combo to get a few thousand dollars from exploiting Cross-Origin Resource Sharing (CORS) misconfigurations on internal networks in bug bounties. 

Check out this example of [hacking Tesla](https://bugcrowd.com/disclosures/0e3f3821-1d26-466b-8599-7cc2f206f4d9/several-internal-applications-have-open-cors-allowing-external-folks-to-access-the-content). It was so much fun that we’re here to share our tooling and techniques with everyone. Rest assured that this same approach will work for plenty of other bug bounty targets.

Usually internal networks are out of scope for bug bounties due to the strict rules against lateral movement and social engineering but we devised a method to attack these internal apps directly without the use of either. Internal apps also often [contain secrets in their javascript](https://trufflesecurity.com/blog/trufflehog-the-chrome-extension/). We’re aware we’re walking very close to the line, but we don’t believe it’s been crossed.

  

![](https://framerusercontent.com/images/gYHG5d1YSkFAuc12d3wQaCRyw.png?width=1094&height=816)

  

Feeling antsy and just want to get your hands on some code?? Understandable. [The code can be found under the Truffle Security GitHub organization](https://github.com/trufflesecurity/of-cors). Happy hacking.

  

![](https://framerusercontent.com/images/1hyT3PwHoiDEg6RkAMyfNd3kWyQ.png?width=1580&height=962)

##### A QUICK CORS PRIMER

The same origin policy (SOP) is a foundational element of modern browser security. Without it all of the websites you visit in your browser could access data from one another (we’d be pulling data from your beanie baby fan site page right now if we could).

  

![](https://framerusercontent.com/images/ERYeHirPsfcyUyu4qOVyHH82zN8.png?width=1600&height=270)

  

The SOP, while super important, is a bit more rigid than modern web developers might like. [Time](https://dev.to/benregenspan/the-state-of-jsonp-and-jsonp-vulnerabilities-in-2021-52ep) and [time again](https://medium.com/@chiragrai3666/exploiting-postmessage-e2b01349c205) there have been clever ways to try to get around the SOP, often to [disastrous effect](https://blog.miki.it/2014/7/8/abusing-jsonp-with-rosetta-flash/). CORS is an officially supported security standard that tries to address this demand, enabling developers to “opt in” to explicit SOP carve-outs on the web sites they create.

  

![](https://framerusercontent.com/images/yuNqB9N7MQ6AvjPNCmWgCLPoKI.png?width=1600&height=465)

  

CORS can be configured in two different ways. The first is to specify an origin that can read responses. In this case, logged in users can have their user data accessed. The second is to use a **wildcard,** which will not send login session information and is usually assumed to be safe for that reason. That’s often true for externally facing websites but can go horrendously wrong for internal facing web apps that don’t use authentication.

  

  
  
  GET /hello/world HTTP/1.1 
  User-Agent: Really Cool Browser .
  Origin: some.other.origin.com 
  Accept-Language: en-us 
  Accept-Encoding: gzip, deflate 
  Connection: Keep-Alive 
  
  HTTP/1.1 200 OK 
  Date: Mon, 12 Dec 2022 00:00:00 GMT 
  Server: Some Cool Server 
  Content-Length: 230 
  Access-Control-Allow-Origin: * 
  Content-Type: text/html; charset=iso-8859-1 
  Connection: Closed

  

[PortSwigger has done an excellent job explaining this](https://portswigger.net/web-security/cors) and talks through these misconfigurations in much more detail. For this post we will just stay focused on the issue of using wildcards for internal apps.

You’ll find such an example of an incomplete view of wildcard CORS on websites like <https://enable-cors.org/> which fails to mention one of the most dangerous aspects of enabling CORS; its use on internal networks. People’s browsers straddle multiple networks so when a victim visits an evil website that evil website can hit all of the internal apps on internal networks.

Take a look at a couple Tweets we found that are born out of a lack of understanding of this threat. Note both posters have over 10,000 followers:

  

![](https://framerusercontent.com/images/62Kgjyi8atQmwfjWKnZKnmiU8o.png?width=1238&height=488)

  

To this lack of clarity, we say “thank you” for our recent bug bounty victory.

##### CAN YOU FIND CORS MISCONFIGURATIONS? OF-CORS YOU CAN!

We’d like to introduce you to our new CORS exploitation toolkit, affectionately known as of-CORS. of-CORS is a web application and set of scripts that, when spun up, can sneakily prod target corporate networks for CORS misconfigurations using typosquatting and phone home with data when found. With a modicum of configuration and setup you too can poke around in the networks of large bug bounty targets for that sweet, sweet bounty loot.

  

The core hypothesis of-CORS was built to test was “large internal corporate networks are exceedingly likely to have impactful CORS misconfigurations.” As such we wanted a toolkit that would do all the following:

  * Enumerate likely internal subdomains for target organizations

  * Launch a JavaScript payload to prod for CORS misconfigurations against configured domains

  * Utilize a service worker to make requests long after the victim is redirected off the typosquatting domain

  * Accept results from the victim’s browser and provide some level of result queryability in a UI

  * Make some level of attempt to hide itself

  * Is likely to be visited by employees of target organizations

Achieving these goals took a bit of work in a handful of domains.

##### The Web Application

The of-CORS web application is a Python3 application built using Django and Django Rest Framework. When a victim visits the web application a lookup is done to determine what internal domains are configured to be probed. A browser service worker is then registered to do the probing and the user’s browser is quickly redirected away to the _assumed_ intended destination.

For example, let’s say that we have registered eslamotors.com and pointed it to our of-CORS instance. An internal Tesla employee then accidentally visits <https://foobar.eslamotors.com/bing/bang/bong.php> (whoops, typo alert!). of-CORS then looks up the core domain of “eslamotors.com” to determine the list of domains that a payload should be launched for. This JavaScript payload for running the probing is then registered as a service worker and the employee’s browser is redirected to <https://foobar.teslamotors.com/bing/bang/bong.php>. The service worker continues to run in the background, issuing HTTPS requests to all of the configured domains and reporting back to of-CORS any identified CORS misconfigurations _as well as_ the HTML content for the misconfigured domains.

Just like that, we have a setup for probing internal network CORS misconfigurations with minimal indication to the victim. Any internal apps without authentication and permissive CORS will send all their data to your instance of of-CORS.

##### The Infrastructure

We wanted a toolkit that enabled us to receive HTTPS requests for a myriad of different domains. We also wanted the ability to spin new domains and targets up and down with relative ease. Thus we needed someone else to handle the SSL/TLS certificate management.

The deployment we landed on was using Cloudflare for SSL/TLS termination and DNS management and Heroku for application hosting. Cloudflare allows for wildcard CNAME routing and Heroku allows for configuring arbitrary domains to point to existing Heroku stacks. Together they achieve the infrastructure flexibility we needed for rapid iteration.

Even with this relatively simple deployment, managing infrastructure can be a real pain. To address this we implemented Terraform configuration that wires up Cloudflare, Heroku, and of-CORS in the correct configuration based on a single YAML file.

##### Getting Victims to Visit Our Application

Bug bounty rules can vary wildly from one organization to the next, but a common rule even across this variability is that researchers cannot engage in social engineering to aid in their attacks. Thus we were left with the problem of “how do we get victims to visit our malicious website.”

Human error and bad typing to the rescue! We decided to go the route of purchasing [typo-squat](https://www.kaspersky.com/resource-center/definitions/what-is-typosquatting) domains that were very similar to the internal domains used by the organizations we targeted. You’ll need to do a little reconnaissance to learn what internal second level domains your target company uses. You can often find this in old commits in Github repos, android builds, and sometimes even StackOverflow questions. An example of an internal Uber domain found via GitHub is shown below:

  

![](https://framerusercontent.com/images/jFNK3vhdAvfjyLcEPMNqSTtrk2Y.png?width=1040&height=642)

  

Next you’ll need to purchase a common typo of this internal second level domain. We recommend the off-by-one copy paste error that occurs when you drop the first or last character (ex: _orpinternal.com_ for a company that owns the domain _corpinternal.com_).

You’ll need to setup DNS for your purchased domain to route all subdomains to the of-CORS web server, and you’ll also need to configure TLS for the subdomains in something like Cloudflare (we made this a little easier for you to configure as explained in the section below).

##### Configuring the Stack

So we’ve got the application, the sneaky domains to get victims to come say hi, and the infrastructure. Now we just need the data! The of-CORS configuration file not only specifies the infrastructure setup, but also which payloads should be generated for which domains. Take a look at the following sample configuration file:

  

  
  
  terraform: 
  # You must change this to a unique string that is a valid Heroku app name 
  heroku_app_name: best-cors-hunter 
  # Fill this out with your Cloudflare API token ***REDACTED***: this-is-my-api-token 
  
  hosts: 
  testing: 
  host_domain: 127.0.0.1:8080 
  redirect_domain: google.com 
  targets: 
  - enable-cors.org 
  - example.com

  

Under the hosts.testing configuration directive we see a host_domain value of 127.0.0.1:8080, a redirect_value domain of google.com, and two targets configured for enable-cors.org and example.com. In this configuration of-CORS will expect to receive requests at 127.0.0.1:8080, will subsequently launch a payload targeting subdomains of example.com and enable-cors.org when a request is received, and will redirect the victim’s browser to google.com after the browser service worker is registered.

  
The last piece of the puzzle here is the identification of good candidate subdomains to target under google.com and enable-cors.org. We do this by relying on [OWASP’s amass tool](https://github.com/OWASP/Amass) to perform subdomain enumeration and then we do our own light testing to determine which of the identified subdomains (if any) are likely internal domains. Funny enough, we throw out all domains that are external facing in this step, which is the opposite of what bountiers typically do with amass.

Note that detailed and explicit steps for configuring of-CORS can be found in its GitHub repository’s README.md file.

Now that we’ve given you a quick tour let’s see of-CORS in action!

##### of-CORS in Action, a Tesla Story

While there were a handful of bug bounty targets that we went after, our engagement with Tesla was the most positive, and they allowed us to publicly disclose the bug! Check it out here:

  

<https://bugcrowd.com/disclosures/0e3f3821-1d26-466b-8599-7cc2f206f4d9/several-internal-applications-have-open-cors-allowing-external-folks-to-access-the-content>

  
We set up of-CORS with the typo-squat domain of eslamotors.com and configured it to probe for CORS misconfigurations across approximately 150 subdomains of teslamotors.com. We only had to wait a few days before we got a hit:

  

![](https://framerusercontent.com/images/IGhwrdCH9NnwOS9G8Z4pB9sMk.png?width=1600&height=744)

  

Eureka! They found it. When this unfortunate victim requested the page from of-CORS we registered a service worker that probed all of the configured subdomains. Of those 150 domains that were tested _12_ of them were configured to allow cross-origin access with CORS. The affected domains are shown below in the of-CORS UI:

  

![](https://framerusercontent.com/images/YQuxaVKB8ol5Hv8l9kjwypj80P4.png?width=1600&height=711)

  

Because of-CORS saves the HTML content that is returned from sites with CORS misconfigurations we also had the ability to review the pages for all of the affected sites. The HTML content for location.teslamotors.com is shown below:

  

![](https://framerusercontent.com/images/U0ubD8yj5Q8UMRkU1mfmafoK3I.png?width=1260&height=883)

  

We reported our findings through Tesla’s bug bounty [program on BugCrowd](https://bugcrowd.com/disclosures/0e3f3821-1d26-466b-8599-7cc2f206f4d9/several-internal-applications-have-open-cors-allowing-external-folks-to-access-the-content) and the issue was quickly escalated, accepted, resolved, and paid out (a testament to the maturity of Tesla’s bug bounty program generally and security teams specifically).

We demonstrated the ability to access and exfiltrate data from Tesla’s internal network just by setting an innocuous trap and waiting for employees to wander into it. Delightful.

## Conclusion

CORS may be an old topic at this point but it is still very relevant when it comes to properly securing your web applications, and this goes for external _and_ internal services. With of-CORS you too can help bug bounty programs identify internal misconfigurations and enjoy some bounty loot.

The of-CORS code and documentation can be found on our GitHub page.  
A cheekier version of this story is told in our [recent video on the topic](https://www.youtube.com/watch?v=wgHqfeNgt5s).

  

  
  

#### We used a new Appsec combo to get a few thousand dollars from exploiting Cross-Origin Resource Sharing (CORS) misconfigurations on internal networks in bug bounties. 

Check out this example of [hacking Tesla](https://bugcrowd.com/disclosures/0e3f3821-1d26-466b-8599-7cc2f206f4d9/several-internal-applications-have-open-cors-allowing-external-folks-to-access-the-content). It was so much fun that we’re here to share our tooling and techniques with everyone. Rest assured that this same approach will work for plenty of other bug bounty targets.

Usually internal networks are out of scope for bug bounties due to the strict rules against lateral movement and social engineering but we devised a method to attack these internal apps directly without the use of either. Internal apps also often [contain secrets in their javascript](https://trufflesecurity.com/blog/trufflehog-the-chrome-extension/). We’re aware we’re walking very close to the line, but we don’t believe it’s been crossed.

  

![](https://framerusercontent.com/images/gYHG5d1YSkFAuc12d3wQaCRyw.png?width=1094&height=816)

  

Feeling antsy and just want to get your hands on some code?? Understandable. [The code can be found under the Truffle Security GitHub organization](https://github.com/trufflesecurity/of-cors). Happy hacking.

  

![](https://framerusercontent.com/images/1hyT3PwHoiDEg6RkAMyfNd3kWyQ.png?width=1580&height=962)

##### A QUICK CORS PRIMER

The same origin policy (SOP) is a foundational element of modern browser security. Without it all of the websites you visit in your browser could access data from one another (we’d be pulling data from your beanie baby fan site page right now if we could).

  

![](https://framerusercontent.com/images/ERYeHirPsfcyUyu4qOVyHH82zN8.png?width=1600&height=270)

  

The SOP, while super important, is a bit more rigid than modern web developers might like. [Time](https://dev.to/benregenspan/the-state-of-jsonp-and-jsonp-vulnerabilities-in-2021-52ep) and [time again](https://medium.com/@chiragrai3666/exploiting-postmessage-e2b01349c205) there have been clever ways to try to get around the SOP, often to [disastrous effect](https://blog.miki.it/2014/7/8/abusing-jsonp-with-rosetta-flash/). CORS is an officially supported security standard that tries to address this demand, enabling developers to “opt in” to explicit SOP carve-outs on the web sites they create.

  

![](https://framerusercontent.com/images/yuNqB9N7MQ6AvjPNCmWgCLPoKI.png?width=1600&height=465)

  

CORS can be configured in two different ways. The first is to specify an origin that can read responses. In this case, logged in users can have their user data accessed. The second is to use a **wildcard,** which will not send login session information and is usually assumed to be safe for that reason. That’s often true for externally facing websites but can go horrendously wrong for internal facing web apps that don’t use authentication.

  

  
  
  GET /hello/world HTTP/1.1 
  User-Agent: Really Cool Browser .
  Origin: some.other.origin.com 
  Accept-Language: en-us 
  Accept-Encoding: gzip, deflate 
  Connection: Keep-Alive 
  
  HTTP/1.1 200 OK 
  Date: Mon, 12 Dec 2022 00:00:00 GMT 
  Server: Some Cool Server 
  Content-Length: 230 
  Access-Control-Allow-Origin: * 
  Content-Type: text/html; charset=iso-8859-1 
  Connection: Closed

  

[PortSwigger has done an excellent job explaining this](https://portswigger.net/web-security/cors) and talks through these misconfigurations in much more detail. For this post we will just stay focused on the issue of using wildcards for internal apps.

You’ll find such an example of an incomplete view of wildcard CORS on websites like <https://enable-cors.org/> which fails to mention one of the most dangerous aspects of enabling CORS; its use on internal networks. People’s browsers straddle multiple networks so when a victim visits an evil website that evil website can hit all of the internal apps on internal networks.

Take a look at a couple Tweets we found that are born out of a lack of understanding of this threat. Note both posters have over 10,000 followers:

  

![](https://framerusercontent.com/images/62Kgjyi8atQmwfjWKnZKnmiU8o.png?width=1238&height=488)

  

To this lack of clarity, we say “thank you” for our recent bug bounty victory.

##### CAN YOU FIND CORS MISCONFIGURATIONS? OF-CORS YOU CAN!

We’d like to introduce you to our new CORS exploitation toolkit, affectionately known as of-CORS. of-CORS is a web application and set of scripts that, when spun up, can sneakily prod target corporate networks for CORS misconfigurations using typosquatting and phone home with data when found. With a modicum of configuration and setup you too can poke around in the networks of large bug bounty targets for that sweet, sweet bounty loot.

  

The core hypothesis of-CORS was built to test was “large internal corporate networks are exceedingly likely to have impactful CORS misconfigurations.” As such we wanted a toolkit that would do all the following:

  * Enumerate likely internal subdomains for target organizations

  * Launch a JavaScript payload to prod for CORS misconfigurations against configured domains

  * Utilize a service worker to make requests long after the victim is redirected off the typosquatting domain

  * Accept results from the victim’s browser and provide some level of result queryability in a UI

  * Make some level of attempt to hide itself

  * Is likely to be visited by employees of target organizations

Achieving these goals took a bit of work in a handful of domains.

##### The Web Application

The of-CORS web application is a Python3 application built using Django and Django Rest Framework. When a victim visits the web application a lookup is done to determine what internal domains are configured to be probed. A browser service worker is then registered to do the probing and the user’s browser is quickly redirected away to the _assumed_ intended destination.

For example, let’s say that we have registered eslamotors.com and pointed it to our of-CORS instance. An internal Tesla employee then accidentally visits <https://foobar.eslamotors.com/bing/bang/bong.php> (whoops, typo alert!). of-CORS then looks up the core domain of “eslamotors.com” to determine the list of domains that a payload should be launched for. This JavaScript payload for running the probing is then registered as a service worker and the employee’s browser is redirected to <https://foobar.teslamotors.com/bing/bang/bong.php>. The service worker continues to run in the background, issuing HTTPS requests to all of the configured domains and reporting back to of-CORS any identified CORS misconfigurations _as well as_ the HTML content for the misconfigured domains.

Just like that, we have a setup for probing internal network CORS misconfigurations with minimal indication to the victim. Any internal apps without authentication and permissive CORS will send all their data to your instance of of-CORS.

##### The Infrastructure

We wanted a toolkit that enabled us to receive HTTPS requests for a myriad of different domains. We also wanted the ability to spin new domains and targets up and down with relative ease. Thus we needed someone else to handle the SSL/TLS certificate management.

The deployment we landed on was using Cloudflare for SSL/TLS termination and DNS management and Heroku for application hosting. Cloudflare allows for wildcard CNAME routing and Heroku allows for configuring arbitrary domains to point to existing Heroku stacks. Together they achieve the infrastructure flexibility we needed for rapid iteration.

Even with this relatively simple deployment, managing infrastructure can be a real pain. To address this we implemented Terraform configuration that wires up Cloudflare, Heroku, and of-CORS in the correct configuration based on a single YAML file.

##### Getting Victims to Visit Our Application

Bug bounty rules can vary wildly from one organization to the next, but a common rule even across this variability is that researchers cannot engage in social engineering to aid in their attacks. Thus we were left with the problem of “how do we get victims to visit our malicious website.”

Human error and bad typing to the rescue! We decided to go the route of purchasing [typo-squat](https://www.kaspersky.com/resource-center/definitions/what-is-typosquatting) domains that were very similar to the internal domains used by the organizations we targeted. You’ll need to do a little reconnaissance to learn what internal second level domains your target company uses. You can often find this in old commits in Github repos, android builds, and sometimes even StackOverflow questions. An example of an internal Uber domain found via GitHub is shown below:

  

![](https://framerusercontent.com/images/jFNK3vhdAvfjyLcEPMNqSTtrk2Y.png?width=1040&height=642)

  

Next you’ll need to purchase a common typo of this internal second level domain. We recommend the off-by-one copy paste error that occurs when you drop the first or last character (ex: _orpinternal.com_ for a company that owns the domain _corpinternal.com_).

You’ll need to setup DNS for your purchased domain to route all subdomains to the of-CORS web server, and you’ll also need to configure TLS for the subdomains in something like Cloudflare (we made this a little easier for you to configure as explained in the section below).

##### Configuring the Stack

So we’ve got the application, the sneaky domains to get victims to come say hi, and the infrastructure. Now we just need the data! The of-CORS configuration file not only specifies the infrastructure setup, but also which payloads should be generated for which domains. Take a look at the following sample configuration file:

  

  
  
  terraform: 
  # You must change this to a unique string that is a valid Heroku app name 
  heroku_app_name: best-cors-hunter 
  # Fill this out with your Cloudflare API token ***REDACTED***: this-is-my-api-token 
  
  hosts: 
  testing: 
  host_domain: 127.0.0.1:8080 
  redirect_domain: google.com 
  targets: 
  - enable-cors.org 
  - example.com

  

Under the hosts.testing configuration directive we see a host_domain value of 127.0.0.1:8080, a redirect_value domain of google.com, and two targets configured for enable-cors.org and example.com. In this configuration of-CORS will expect to receive requests at 127.0.0.1:8080, will subsequently launch a payload targeting subdomains of example.com and enable-cors.org when a request is received, and will redirect the victim’s browser to google.com after the browser service worker is registered.

  
The last piece of the puzzle here is the identification of good candidate subdomains to target under google.com and enable-cors.org. We do this by relying on [OWASP’s amass tool](https://github.com/OWASP/Amass) to perform subdomain enumeration and then we do our own light testing to determine which of the identified subdomains (if any) are likely internal domains. Funny enough, we throw out all domains that are external facing in this step, which is the opposite of what bountiers typically do with amass.

Note that detailed and explicit steps for configuring of-CORS can be found in its GitHub repository’s README.md file.

Now that we’ve given you a quick tour let’s see of-CORS in action!

##### of-CORS in Action, a Tesla Story

While there were a handful of bug bounty targets that we went after, our engagement with Tesla was the most positive, and they allowed us to publicly disclose the bug! Check it out here:

  

<https://bugcrowd.com/disclosures/0e3f3821-1d26-466b-8599-7cc2f206f4d9/several-internal-applications-have-open-cors-allowing-external-folks-to-access-the-content>

  
We set up of-CORS with the typo-squat domain of eslamotors.com and configured it to probe for CORS misconfigurations across approximately 150 subdomains of teslamotors.com. We only had to wait a few days before we got a hit:

  

![](https://framerusercontent.com/images/IGhwrdCH9NnwOS9G8Z4pB9sMk.png?width=1600&height=744)

  

Eureka! They found it. When this unfortunate victim requested the page from of-CORS we registered a service worker that probed all of the configured subdomains. Of those 150 domains that were tested _12_ of them were configured to allow cross-origin access with CORS. The affected domains are shown below in the of-CORS UI:

  

![](https://framerusercontent.com/images/YQuxaVKB8ol5Hv8l9kjwypj80P4.png?width=1600&height=711)

  

Because of-CORS saves the HTML content that is returned from sites with CORS misconfigurations we also had the ability to review the pages for all of the affected sites. The HTML content for location.teslamotors.com is shown below:

  

![](https://framerusercontent.com/images/U0ubD8yj5Q8UMRkU1mfmafoK3I.png?width=1260&height=883)

  

We reported our findings through Tesla’s bug bounty [program on BugCrowd](https://bugcrowd.com/disclosures/0e3f3821-1d26-466b-8599-7cc2f206f4d9/several-internal-applications-have-open-cors-allowing-external-folks-to-access-the-content) and the issue was quickly escalated, accepted, resolved, and paid out (a testament to the maturity of Tesla’s bug bounty program generally and security teams specifically).

We demonstrated the ability to access and exfiltrate data from Tesla’s internal network just by setting an innocuous trap and waiting for employees to wander into it. Delightful.

## Conclusion

CORS may be an old topic at this point but it is still very relevant when it comes to properly securing your web applications, and this goes for external _and_ internal services. With of-CORS you too can help bug bounty programs identify internal misconfigurations and enjoy some bounty loot.

The of-CORS code and documentation can be found on our GitHub page.  
A cheekier version of this story is told in our [recent video on the topic](https://www.youtube.com/watch?v=wgHqfeNgt5s).

  

  
  

## [More from THE DIG](../blog)

Thoughts, research findings, reports, and more from Truffle Security Co.

[![](https://framerusercontent.com/images/gc8s3t3Vc2qmwhdmcd0kiE3Z9dw.png?width=1200&height=600)Jun 18, 2026Your PR scan is missing half the problem](./pr-scan-missing-half-the-problem)[![](https://framerusercontent.com/images/9clzmnPHl1RUTb35545Z0QjeaCo.png?width=1200&height=600)Jun 2, 2026Admin on Apache Org Exposed for 2.5 Years in Deleted PyPI Package](./admin-apache-exposed-deleted-pypi-package)[![](https://framerusercontent.com/images/WeB35OGPgqrFpsRGCxRbRHAFRZE.png?width=1200&height=600)May 22, 2026CISA's Leaked Admin GitHub Token Remained Live 2 Days After Krebs Reported It Leaked](./cisa-leaked-admin-github-token-remained-live-2-days)

# [T](../blog)he Dig

Thoughts, research findings, reports, and more from Truffle Security Co.

[![](https://framerusercontent.com/images/gc8s3t3Vc2qmwhdmcd0kiE3Z9dw.png?width=1200&height=600)Jun 18, 2026Your PR scan is missing half the problem](./pr-scan-missing-half-the-problem)[![](https://framerusercontent.com/images/9clzmnPHl1RUTb35545Z0QjeaCo.png?width=1200&height=600)Jun 2, 2026Admin on Apache Org Exposed for 2.5 Years in Deleted PyPI Package](./admin-apache-exposed-deleted-pypi-package)

STAY STRONG

DIG DEEP

[](../)

TRUFFLEHOG

[Open-source](../trufflehog)

[Enterprise](../trufflehog-enterprise)

[Analyze](../trufflehog-analyze)

[GCP Analyze](../trufflehog-gcp-analyze)

NEW!

[Forager](../trufflehog-forager)

[Security](../security)

[Integrations](../integrations)

[Pricing](../pricing)

[CUSTOMERS](../customers)

COMPANY

[About](../about)

[Careers](../careers)

[Press](../press)

[FAQ](../faq)

[Partners](../partners)

NEW!

[Contact us](../contact)

RESOURCES

[Blog](../blog)

[Newsletter](../newsletter)

[Library](../library)

[Events](../events)

[Videos](../videos)

[GitHub](https://github.com/trufflesecurity)

[Enterprise docs](https://docs.trufflesecurity.com/)

[Open-source docs](https://github.com/trufflesecurity/trufflehog#trufflehog)

[How to rotate](https://howtorotate.com/)

[Brand assets](../branding)

NEW!

DOING IT THE RIGHT WAY

[SINCE 2021](../partners)

[](https://github.com/trufflesecurity/)[](https://www.linkedin.com/company/trufflesecurity)[](https://www.youtube.com/@TruffleSecurity)[](https://twitter.com/trufflesec)

[#trufflehog-community](https://join.slack.com/t/trufflehog-community/shared_invite/zt-pw2qbi43-Aa86hkiimstfdKH9UCpPzQ)[#Secret Scanning](https://discord.gg/8Hzbrnkr7E)

© 2026 Truffle Security Co.

[Privacy policy](../privacy-policy)

[Terms and conditions](../terms-conditions)

[Data processing agreement](../data-processing-agreement)

[Acceptable use policy](../acceptable-use-policy)

STAY STRONG

DIG DEEP

[](https://github.com/trufflesecurity/)[](https://www.linkedin.com/company/trufflesecurity)[](https://www.youtube.com/@TruffleSecurity)[](https://twitter.com/trufflesec)

[#trufflehog-community](https://join.slack.com/t/trufflehog-community/shared_invite/zt-pw2qbi43-Aa86hkiimstfdKH9UCpPzQ)[#Secret Scanning](https://discord.gg/8Hzbrnkr7E)

© 2026 Truffle Security Co.

[Privacy policy](../privacy-policy)

[Terms and conditions](../terms-conditions)

[Data processing agreement](../data-processing-agreement)

[Acceptable use policy](../acceptable-use-policy)

infra
