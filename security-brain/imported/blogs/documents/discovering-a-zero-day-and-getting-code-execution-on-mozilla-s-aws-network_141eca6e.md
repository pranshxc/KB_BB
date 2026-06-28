---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-19_discovering-a-zero-day-and-getting-code-execution-on-mozillas-aws-network.md
original_filename: 2019-03-19_discovering-a-zero-day-and-getting-code-execution-on-mozillas-aws-network.md
title: Discovering a zero day and getting code execution on Mozilla's AWS Network
category: documents
detected_topics:
- ssrf
- sso
- command-injection
- automation-abuse
- race-condition
- api-security
tags:
- imported
- documents
- ssrf
- sso
- command-injection
- automation-abuse
- race-condition
- api-security
language: en
raw_sha256: 141eca6e4a3424bee4924578febdfb4719dd8face03b12e0be9f88aaa5d1e605
text_sha256: 06f9f67409dd2539d31afc4e4b4430293940180b73986e8644cfa6641f105af3
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Discovering a zero day and getting code execution on Mozilla's AWS Network

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-19_discovering-a-zero-day-and-getting-code-execution-on-mozillas-aws-network.md
- Source Type: markdown
- Detected Topics: ssrf, sso, command-injection, automation-abuse, race-condition, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `141eca6e4a3424bee4924578febdfb4719dd8face03b12e0be9f88aaa5d1e605`
- Text SHA256: `06f9f67409dd2539d31afc4e4b4430293940180b73986e8644cfa6641f105af3`


## Content

---
title: "Discovering a zero day and getting code execution on Mozilla's AWS Network"
url: "https://blog.assetnote.io/bug-bounty/2019/03/19/rce-on-mozilla-zero-day-webpagetest/"
final_url: "https://www.assetnote.io/resources/research/discovering-a-zero-day-and-getting-code-execution-on-mozillas-aws-network"
authors: ["Shubham Shah (@infosec_au)", "Mathias Karlsson (@avlidienbrunn)"]
programs: ["Mozilla"]
bugs: ["RCE"]
bounty: "500"
publication_date: "2019-03-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5351
---

[Research Notes](/resources/research)

Security Research

March 19, 2019

# Discovering a zero day and getting code execution on Mozilla's AWS Network

No items found.

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/653795bb35bc995a6f921d3f_citrixbleed.svg)

Creative Commons license

When Assetnote Continuous Security (CS) monitors your attack surface, one of the things it looks for are instances of [WebPageTest](https://github.com/WPO-Foundation/webpagetest). WebPageTest is a website performance testing tool that lets you test network related metrics for any given URL/host.

Although basic authentication can be enabled by modifying the [settings.ini](https://github.com/WPO-Foundation/webpagetest/blob/master/www/settings/settings.ini.sample#L155) file, and is recommended to prevent any anonymous access. Most deployments of WebPageTest that Assetnote CS identifies are unauthenticated, and the array of testing tools provided by WebPageTest can be used offensively to gain access to internal resources by server-side request forgery (commonly known as SSRF, but for WebPageTest, it is a feature).

In November 2017, Assetnote CS discovered the following assets on Mozilla’s AWS environment:

  * wpt-vpn.stage.mozaws.net
  * wpt1.dev.mozaws.net

Both of these were instances of WebPageTest did not require authentication, and it was the first time Assetnote CS had detected it for a bug bounty. Working with [Mathias](https://twitter.com/avlidienbrunn), we audited the source code, and in just a few hours we were able to create an attack chain that led to remote-code execution.

While it was a zero day at the time of discovery, we worked with the Mozilla and WebPageTest team on getting the vulnerability fixed upstream. The commit which patches the bugs outlined in this blog post was pushed in [this commit](https://github.com/WPO-Foundation/webpagetest/commit/c026e4799455b8bc06c8e40f137d800d8d6803cc#diff-f49d3a5c5c3e48d9e57e843e3f679444), on the 17th of January, 2018.

The first thing in the codebase that caught our attention was the ability to upload and extract arbitrary Zip files via <span class="code_single-line">/www/work/workdone.php</span>. This script contained some logic to restrict access from sources other than 127.0.0.1, as seen from the code snippet below:
  
  
  ...
  !strcmp($_SERVER['REMOTE_ADDR'], "127.0.0.1")
  ...
  
  

We’ll come back to that later.

In the same file, we found another potential vector - logic to upload an arbitrary Zip and have it extracted to a known location:

Lines 133 - 136: **/www/work/workdone.php**
  
  
  if (isset($_FILES['file']['tmp_name'])) {
  ExtractZipFile($_FILES['file']['tmp_name'], $testPath);
  CompressTextFiles($testPath);
  }
  
  

If we could spoof our IP to come from 127.0.0.1, it seems like we could get code execution through this vector.

However, we found that it’s not as straightforward as we thought it was, due to Line 321 in **/www/work/workdone.php** :
  
  
  SecureDir($testPath);
  
  

The logic of the <span class="code_single-line">SecureDir</span> function can be found on Lines 2322 - 2347 in **/www/common_lib.inc** :
  
  
  /**
  * Make sure there are no risky files in the given directory and make everything no-execute
  *
  * @param mixed $path
  */
  function SecureDir($path) {
  $files = scandir($path);
  foreach ($files as $file) {
  $filepath = "$path/$file";
  if (is_file($filepath)) {
  $parts = pathinfo($file);
  $ext = strtolower($parts['extension']);
  if (strpos($ext, 'php') === false &&
  strpos($ext, 'pl') === false &&
  strpos($ext, 'py') === false &&
  strpos($ext, 'cgi') === false &&
  strpos($ext, 'asp') === false &&
  strpos($ext, 'js') === false &&
  strpos($ext, 'rb') === false &&
  strpos($ext, 'htaccess') === false &&
  strpos($ext, 'jar') === false) {
  @chmod($filepath, 0666);
  } else {
  @chmod($filepath, 0666);  // just in case the unlink fails for some reason
  unlink($filepath);
  }
  } elseif ($file != '.' && $file != '..' && is_dir($filepath)) {
  SecureDir($filepath);
  }
  }
  }
  
  

Since the SecureDir function occurs later during the code flow, there is an exploitable race condition where the PHP files that are extracted to the webserver were accessible for a short period of time before being deleted.

The first pre-requesite of the chain was rather easy, as a valid test ID was obtained by running a Traceroute on <span class="code_single-line">https://google.com</span> through the WebPageTest interface on <span class="code_single-line">wpt-vpn.stage.mozaws.net</span>:

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a00233d1b7ba45beed944b_wpt1.png)

_Running a traceroute using WebPageTest_

After running the traceroute, WebPageTest redirected us to a URL that contained the test ID used in later steps:

  * [http://wpt-vpn.stage.mozaws.net/result/**171124_GW_9/**](http://wpt-vpn.stage.mozaws.net/result/171124_GW_9/)

[‍](http://wpt-vpn.stage.mozaws.net/result/171124_GW_9/)But we still needed to somehow spoof that we are <span class="code_single-line">127.0.0.1</span> in order to access the vulnerable functions in this script.

We were able to meet this condition by exploiting the following logic:

Line 70: **/www/common.inc**
  
  
  if (isset($_SERVER["HTTP_FASTLY_CLIENT_IP"]))
  $_SERVER["REMOTE_ADDR"] = $_SERVER["HTTP_FASTLY_CLIENT_IP"];
  
  

This allowed us as remote users to arbitrarily set <span class="code_single-line">$_SERVER["REMOTE_ADDR"]</span> by sending a <span class="code_single-line">FASTLY-CLIENT-IP</span> request header set to <span class="code_single-line">127.0.0.1</span>.

Combining all of these elements together, we were able to set up two Burp Intruder attacks to finally get code execution.

One Burp Intruder attack was used to upload a malicious Zip file, and another attempted to access the extracted PHP file, while it existed on the system. Our solution to exploiting the race condition at the time was to simply up Burp Intruder’s threads to ~200.

Today, using tools such as [Turbo Intruder](https://portswigger.net/blog/turbo-intruder-embracing-the-billion-request-attack), due to the speed of the requests being sent, it’s possible to make this exploit much more reliable.

We were able to use this technique to achieve code execution on Mozilla as seen in the screenshot below:

![](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a0027dea9112c1a99a36cc_wpt-burp1.png)

_phpinfo() output from wpt-vpn.stage.mozaws.net_

The Bugzilla report in which we first reported this vulnerability is now public, and can be viewed [here](https://bugzilla.mozilla.org/show_bug.cgi?id=1420520). 

The report contains thorough reproduction steps that should be sufficient for testers wishing to recreate these bugs.

We were awarded $500 as a part of Mozilla’s bug bounty program.

Written by:

Shubham Shah

Your subscription could not be saved. Please try again. 

Your subscription has been successful. 

Get updates on our research

Subscribe to our newsletter and stay updated on the newest research, security advisories, and more!

Enter your email address to subscribe

Provide your email address to subscribe. For e.g abc@xyz.com 

SUBSCRIBE 

### More Like This

[Security ResearchNew!Doing the Due Diligence: Analyzing the Next.js Middleware Bypass (CVE-2025-29927)Read moreRead on ASN Blog](/resources/research/doing-the-due-diligence-analyzing-the-next-js-middleware-bypass-cve-2025-29927)

[Security ResearchNew!How an obscure PHP footgun led to RCE in Craft CMSRead moreRead on ASN Blog](/resources/research/how-an-obscure-php-footgun-led-to-rce-in-craft-cms)

[Security ResearchNew!Citrix Denial of Service: Analysis of CVE-2024-8534Read moreRead on ASN Blog](/resources/research/citrix-denial-of-service-analysis-of-cve-2024-8534)

[Security ResearchNew!Nginx/Apache Path Confusion to Auth Bypass in PAN-OS (CVE-2025-0108)Read moreRead on ASN Blog](/resources/research/nginx-apache-path-confusion-to-auth-bypass-in-pan-os)

[Security ResearchNew!Leveraging An Order of Operations Bug to Achieve RCE in Sitecore 8.x - 10.xRead moreRead on ASN Blog](/resources/research/leveraging-an-order-of-operations-bug-to-achieve-rce-in-sitecore-8-x---10-x)

[Security ResearchNew!Insecurity through Censorship: Vulnerabilities Caused by The Great FirewallRead moreRead on ASN Blog](/resources/research/insecurity-through-censorship-vulnerabilities-caused-by-the-great-firewall)

[Back to All](/resources/research)

### Ready to get started?

Get on a call with our team and learn how Assetnote can change the way you secure your attack surface. We'll set you up with a trial instance so you can see the impact for yourself.

[Request a Demo](/demo)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/64241df2676aeba82706ffe8_assetnote-logo.svg)

Address:  
Level 10, 12 Creek Street, Brisbane QLD, 4000  
‍  
Contact:  
[contact@assetnote.io  
  
](mailto:contact@assetnote.io)Press Inquiries:[  
](mailto:contact@assetnote.io)[press@assetnote.io](mailto:press@assetnote.io)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/661f041240ed96ed7a03fe6f_61dc1beb212a1202fc512a76_SOC%202-03-p-500.png)

[](https://twitter.com/assetnote)[](https://www.linkedin.com/company/assetnote/)

Platform Features

[Continuous Asset Discovery](/platform/asset-discovery)

[Deep Asset Enrichment](/platform/asset-enrichment)

[Assetnote Exposure Engine](/platform/assetnote-exposure-engine)

[Expert Security Research](/platform/expert-security-research)

[Collaborative Workflows](/platform/collaborative-workflows)

[Customization](/platform/customization)

Use Cases

[Continuous Asset Discovery and Inventory](/use-cases/continuous-asset-discovery-and-inventory)

[Real-Time Exposure Monitoring](/use-cases/continuous-security-monitoring)

[Attack Surface Reduction](/use-cases/attack-surface-reduction)

[Mergers & Acquisitions](/use-cases/mergers-and-acquisitions)

[Bug Bounty Readiness](/use-cases/bug-bounty-readiness)

© 2026 Assetnote. All rights reserved.

[Privacy Policy](https://assetnote.io/policies/privacy-policy)
