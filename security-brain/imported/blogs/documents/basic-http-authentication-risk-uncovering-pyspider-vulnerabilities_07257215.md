---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-09-02_basic-http-authentication-risk-uncovering-pyspider-vulnerabilities.md
original_filename: 2024-09-02_basic-http-authentication-risk-uncovering-pyspider-vulnerabilities.md
title: 'Basic HTTP Authentication Risk: Uncovering pyspider Vulnerabilities'
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- csrf
- access-control
- otp
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- csrf
- access-control
- otp
language: en
raw_sha256: 07257215ab0d2af3cfb610bde9e5f8ed08ea0066cf0d0839f71455ec0747eceb
text_sha256: 35c39f09de880d5a4789e3cfee3e7f90154a11789d7b94e3a02ee4fafda17685
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# Basic HTTP Authentication Risk: Uncovering pyspider Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-09-02_basic-http-authentication-risk-uncovering-pyspider-vulnerabilities.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, csrf, access-control, otp
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `07257215ab0d2af3cfb610bde9e5f8ed08ea0066cf0d0839f71455ec0747eceb`
- Text SHA256: `35c39f09de880d5a4789e3cfee3e7f90154a11789d7b94e3a02ee4fafda17685`


## Content

---
title: "Basic HTTP Authentication Risk: Uncovering pyspider Vulnerabilities"
page_title: "Basic HTTP Authentication Risk: Uncovering pyspider Vulnerabilities | Sonar"
url: "https://www.sonarsource.com/blog/basic-http-authentication-risk-uncovering-pyspider-vulnerabilities/"
final_url: "https://www.sonarsource.com/blog/basic-http-authentication-risk-uncovering-pyspider-vulnerabilities/"
authors: ["Yaniv Nizry (@YNizry)"]
programs: ["pyspider"]
bugs: ["Reflected XSS", "CSRF", "Security code review"]
publication_date: "2024-09-02"
added_date: "2024-09-04"
source: "pentester.land/writeups.json"
original_index: 23
---

## TL;DR overview

  * Sonar's security research team uncovered critical vulnerabilities in PySpider, a popular Python web scraping framework, stemming from inadequate authentication and unsafe code execution patterns.
  * The most severe issue is that PySpider's built-in web UI relies on weak HTTP Basic Authentication, and in certain configurations operates with no authentication at all—exposing the interface to unauthorized access.
  * Attackers who gain access to the PySpider UI can execute arbitrary Python code on the server through the script editor, leading to full remote code execution.
  * Developers using PySpider should immediately secure the web UI with strong authentication, restrict network access to trusted hosts, and apply all available security patches.

[pyspider](https://docs.pyspider.org/en/latest/) is a powerful and versatile web crawling framework that caters to various use cases. With its user-friendly approach, robust features, and extensive support for different technologies, it's a great choice for developers who want to build reliable and efficient web scrapers in Python. Unfortunately in the last years, the project was neglected and left unmaintained, and as a result of our reporting, the maintainer archived the GitHub repository to highlight that the project is not updated anymore. This also means that security vulnerabilities are not fixed.

Driven by our dedication to both open-source security and the advancement of our Code Quality technology, we leverage [SonarQube Cloud](https://sonarcloud.io/) to conduct frequent vulnerability scans on open-source projects. This not only benefits the broader open-source community but also strengthens our own tools – and the best part? SonarQube Cloud offers free code analysis for any open-source project, making it accessible to everyone.

This article delves into the consequences of vulnerabilities found by our engine and uncovers the risk of using basic HTTP authentication. We'll also explore how attackers might leverage this vulnerability.

## Impact

An attacker might manipulate an authenticated victim to click on a malicious link, resulting in code execution on the host running pyspider. After we reported our findings, the maintainer has archived the repository on GitHub, making sure users are aware the project isn’t supported anymore (refer to the Patch and Timeline sections for more info).

## Technical Details

In this section, we will cover the technical details of the findings, and interesting security information for developers opting to use the basic HTTP authentication in their application.

### Background

Before delving into the details of the findings, we first need to understand some basic features of the application. pyspider provides users with a convenient [WebUI component](https://docs.pyspider.org/en/latest/Command-Line/#webui) that allows project management, task monitoring, viewing results, and crawl script code editors. From a security point of view, the code editor feature allows running arbitrary Python code on the machine through the web interface, by design. To protect an externally exposed instance, pyspider offers the ability to enable authentication via the [\--need-auth](https://docs.pyspider.org/en/latest/Command-Line/#-need-auth) flag.

### Discovering vulnerabilities

SonarQube Cloud, our cloud-based code analysis service, employs cutting-edge static analysis techniques to identify quality issues, bugs, and security weaknesses within your code. During a routine scan of public open-source projects, SonarQube Cloud identified the following issues in pyspider's WebUI component ([see it yourself on SonarQube Cloud](https://sonarcloud.io/project/issues?resolved=false&types=VULNERABILITY&id=SonarSourceResearch_pyspider-blogpost&open=AY9xKZX48flNzQPVUOH6)):

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/aaa3c4d9-505e-413c-81df-9bca1c73fe2d/dashboard_sonar.png)

The first one is a detected vulnerability covering a Cross-Site Scripting (XSS) reflection on the `/update` route via the `name` parameter:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/d9430d1e-330d-45ad-ae10-3b7477cc1659/XSS_sonar.png)

The second finding is a security hotspot warning us that there is a risk of Cross-Site Request Forgery (CSRF) when using Flask without any protection.

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/17ea3d24-1bda-44fd-a1cb-7910043745f5/CSRF_sonar.png)

The key distinction between a hotspot and a vulnerability lies in the **immediacy of the security risk**. ([read more in the official documentation](https://docs.sonarsource.com/sonarqube/latest/user-guide/security-hotspots/#vulnerability-or-hotspot))

  * **Hotspot:** A hotspot flags a potentially risky code section that might become a vulnerability in certain contexts. It's like a yellow traffic light – proceed with caution and review the code. The overall application security might not be compromised, but further analysis is recommended.  

  * **Vulnerability:** A detected vulnerability represents a high likelihood of a security weakness that can be exploited by attackers. It's akin to a red traffic light – stop and fix the issue immediately. Vulnerabilities pose a clear and present danger to the application's security.

Let's consider a CSRF hotspot rule:  
The scanner might highlight a POST endpoint that doesn't include a CSRF token. This is a hotspot because, without a token, an attacker could potentially craft a malicious request that tricks a user's browser into submitting the form unintentionally. However, a CSRF attack can be mitigated already depending on the cookie’s [SameSite](https://web.dev/articles/samesite-cookies-explained) type used in the application. Or, the application logic of that endpoint doesn't have any security impact nor require authentication in the first place. For those reasons, it might be considered a low-priority hotspot for review, depending on the specific context of the application.

### Basic HTTP authentication CSRF (CVE-2024-39163)

In the case of pyspider, the hotspot was relevant and exploitable. As mentioned before, access to the pyspider WebUI is equivalent to code execution. In instances where authentication is not enabled, it's considered a risk introduced by the pyspider user rather than a vulnerability. We are interested to see what can go wrong if authentication is enabled.

Before trying to validate the CSRF hotspot, let's see how pyspider implements authentication. Setting up the application using the `--need-auth` flag, and trying to access the web interface we are introduced to the following browser-default login prompt:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/1e4e3dc9-f178-44cb-9399-3b51bdfe34a5/login_prompt.png)

This authentication method is used under the hood is [_Basic HTTP authentication_](https://datatracker.ietf.org/doc/html/rfc7617). While this is a rather legacy authentication mechanism it is still supported by modern browsers. On top of that they handle it conveniently, by using the built-in UI prompt and sending the credentials in the subsequent requests via the `Authorization` header:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/4858d20d-ac35-48de-a76c-564ce972f76c/network_flow.png)

Unlike the other common way of authentication and maintaining a session via cookies, the browser doesn't implement any CSRF mitigation for the basic HTTP authentication and the corresponding `Authorization` header, such as [SameSite cookies](https://web.dev/articles/samesite-cookies-explained). The browser adds the `Authorization` header containing the Basic auth credentials to all cross-site requests as well. This means that the only thing standing between a CSRF vulnerability and the application are mitigations on the endpoint level (a [CSRF token](https://portswigger.net/web-security/csrf#:~:text=Common%20defences%20against%20CSRF), for instance).

Because no mitigation steps are taken, an attacker would just need to understand which requests are made to execute arbitrary code on the machine and craft a malicious website that replicates them, exploiting the CSRF vulnerability. Manipulating an authenticated victim to visit the attacker’s website will result in arbitrary code execution.

### Reflected XSS Vulnerability (CVE-2024-39162)

The second detected vulnerability reported by SonarQube Cloud is an XSS in the `/update` endpoint. 

Copy to clipboard
  
  
  @app.route('/update', methods=['POST', ])
  def project_update():
  # ...
  name = request.form['name']
  # ...
  if name not in ('group', 'status', 'rate'):
  return 'unknown field: %s' % name, 400

This simple example showcases how a reflected XSS looks like on the code level. A parameter is taken from the request (a user input) and if certain conditions match, the value is reflected back to the user.

While this is a `POST`-only endpoint, an attacker cannot simply craft a malicious link with a reflected XSS payload, but by leveraging the first finding, an attacker can create a malicious website that uses CSRF and elevate it to XSS. From there, code execution on the server is an intended feature. 

### Patch

After disclosing the vulnerabilities the maintainer stated that this project is no longer maintained and archived the repository on GitHub as a result. We recommend avoiding using unmaintained code, or as a last resort, disabling the _WebUI_ component of pyspider.

## Timeline

**Date**| **Action**  
---|---  
2024-04-03| We reported all issues to the maintainers  
2024-04-29| We pinged the maintainers  
2024-05-03| We pinged the maintainers again mentioning that 60 days had passed  
2024-06-03| We notified the maintainers that the [90-day disclosure](https://googleprojectzero.blogspot.com/p/vulnerability-disclosure-policy.html) window has passed and we will release a blog post about the findings  
2024-06-11| The maintainer stated the project is unmaintained and archived the repository  
2024-07-05| CVE-2024-39163 and CVE-2024-39162 were assigned  
  
## Summary

This blog post delves into the critical role of code analysis in safeguarding applications. We showcase the power of SonarQube Cloud, our cloud-based service that identifies security vulnerabilities often buried within your codebase. SonarQube Cloud ensures Code Quality practices enhancing code readability, maintainability, and security. Code Quality and proactive code analysis empower developers to build more secure applications.

We explored real-world examples of vulnerabilities unearthed by SonarQube Cloud, highlighting the potential dangers they pose. And explained how legacy basic HTTP authentication could be convenient to use but might contain some security risks. Additionally, we demonstrated the differences between a “vulnerability” finding vs a “hotspot”, and why developers shouldn’t neglect them.

## Related Blog Posts

  * [Dangerous Import: SourceForge Patches Critical Code Vulnerability](https://www.sonarsource.com/blog/dangerous-import-sourceforge-patches-critical-code-vulnerability/)
  * [Parallel Code Security: The Challenge of Concurrency](https://www.sonarsource.com/blog/avocado-nightmare-2/)
  * [Apache Dubbo Consumer Risks: The Road Not Taken](https://www.sonarsource.com/blog/apache-dubbo-consumer-risks/)
  * [Micro Services, Major Headaches: Detecting Vulnerabilities in Erxes' Microservices](https://www.sonarsource.com/blog/micro-services-major-headaches-detecting-vulnerabilities-in-erxes-microservices/)
