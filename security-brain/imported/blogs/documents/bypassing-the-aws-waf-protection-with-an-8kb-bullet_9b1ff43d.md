---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-03_bypassing-the-aws-waf-protection-with-an-8kb-bullet.md
original_filename: 2022-02-03_bypassing-the-aws-waf-protection-with-an-8kb-bullet.md
title: Bypassing the AWS WAF protection with an 8KB bullet
category: documents
detected_topics:
- command-injection
- api-security
- ssrf
- xss
- sqli
- file-upload
tags:
- imported
- documents
- command-injection
- api-security
- ssrf
- xss
- sqli
- file-upload
language: en
raw_sha256: 9b1ff43dc6ded571c95a458e4d1c60d2eb940e22758866f9b736a56d1fca0eb5
text_sha256: 6527996e1cacf52d7e0eba21fb9a5b8bcaab313b77dc97393797d860a4646dc3
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing the AWS WAF protection with an 8KB bullet

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-03_bypassing-the-aws-waf-protection-with-an-8kb-bullet.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, ssrf, xss, sqli, file-upload
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `9b1ff43dc6ded571c95a458e4d1c60d2eb940e22758866f9b736a56d1fca0eb5`
- Text SHA256: `6527996e1cacf52d7e0eba21fb9a5b8bcaab313b77dc97393797d860a4646dc3`


## Content

---
title: "Bypassing the AWS WAF protection with an 8KB bullet"
page_title: "Bypassing the AWS WAF Protection with an 8KB Bullet"
url: "https://kloudle.com/blog/the-infamous-8kb-aws-waf-request-body-inspection-limitation"
final_url: "https://kloudle.com/blog/bypassing-the-aws-waf-protection-with-an-8kb-bullet/"
authors: ["Kloudle (@Kloudleinc)"]
programs: ["AWS"]
bugs: ["WAF bypass"]
publication_date: "2022-02-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2939
---

## Introduction

A Web Application Firewall (WAF) is a very common resource or a service that infrastructure and application administrators rely on to protect applications facing the Internet. A WAF sits in front of a web application facing the Internet and inspects the HTTP traffic that is reaching the perimeter to ensure nothing suspicious or malicious goes through.

Most WAFs allow you to edit and create custom rules of inspection that can be used for granular analysis of the incoming HTTP traffic and block even the most sophisticated attack payloads.

This blogpost talks about a documented limitation within the AWS WAF when inspecting a request body, what particular configurations are vulnerable and how an attacker can take advantage of this limitation.

## The 8KB Limitation

The AWS WAF is a popular service in the long list of security tools that AWS provides. The AWS WAF essentially plays the role of a gatekeeper for Web Applications running across various compute resources. There are a whole bunch of free managed rules that you can configure to protect your application against threats like SQL Injection, SSRF, XSS etc. The rule creation feature allows you to create customized rules for your application and business needs.

You can use the AWS WAF to protect applications on CloudFront, the Application Load Balancer, API Gateway for your REST APIs, AWS Lambda and AWS AppSync for GraphQL APIs. Regardless of the use case, the AWS WAF nicely fits into the AWS compute infrastructure ensuring attackers don’t attack your web application thus ensuring data and infrastructure security.

There is a caveat however. AWS WAF only inspects the first 8,192 bytes (8 KB) of the web request body. If a web request body is larger than 8KB, the packet is forwarded to the web server resource for processing!

If you have ever tried to create a rule set within the AWS WAF, you would have been greeted with the following warning.

![AWS WAF limitation](https://imgs.kloudle.com/blog/bypassing-the-aws-waf-protection-with-an-8kb-bullet/1673700071-aws-waf-limitation.png)

This limitation is [well documented](https://docs.aws.amazon.com/waf/latest/developerguide/web-request-body-inspection.html) and presented via multiple warning messages every time you are creating a ruleset that contains a body inspection rule.

## What does the limitation mean in the real world?

Imagine you have a web application running on an EC2 instance. A load balancer sits in front of the EC2 instance. All web traffic trying to reach the web application from the Internet goes through AWS WAF before reaching the load balancer.

Now, if the web application is vulnerable to a vulnerability that an Internet located attacker can exploit, most SREs, application and infrastructure administrators would presume the AWS WAF to thwart the attacker.

Now the WAF functions as advertised for any web traffic that is less than 8KB in size, but as soon as the attack traffic exceeds 8KB, a malicious payload will go right through the AWS WAF, the load balancer and will be processed by the application.

![aws waf limitation setup](https://imgs.kloudle.com/blog/bypassing-the-aws-waf-protection-with-an-8kb-bullet/1673700069-aws-waf-limitation-setup.png)

Here’s an example of an application hosted on AWS as described in the setup above. This application accepts a domain or a web URL as user input and attempts to fetch and show the HTTP response headers that the supplied input sends when a web request is made to it.

![aws waf 8kb limitation](https://imgs.kloudle.com/blog/bypassing-the-aws-waf-protection-with-an-8kb-bullet/1673700072-aws-waf-8kb-limitation.png)

The server side logic for this functionality is built using the cURL command. The user input is passed to cURL as is, without any sanitisation. This results in a vulnerability called [Command Injection](https://owasp.org/www-community/attacks/Command_Injection) which allows the user to enter their own commands by using special characters to separate the server side cURL command and their own command.

For example due to the vulnerability, entering the input kloudle.com;id will cause the server to fetch the HTTP headers for kloudle.com and then run the id command.

However, because we have the AWS WAF configured with rules to block exactly these types of attacks, the attack fails.

![test webacl](https://imgs.kloudle.com/blog/bypassing-the-aws-waf-protection-with-an-8kb-bullet/1673700073-test-webacl.png)

The AWS WAF sends us a Forbidden message as our HTTP request was not allowed to reach the web application.

![403 forbidden HTTP request](https://imgs.kloudle.com/blog/bypassing-the-aws-waf-protection-with-an-8kb-bullet/1673700067-403-forbidden-http-request.png)

## Making the attack work

Given that the attack payload was sent via a POST request and that we were blocked, as an attacker, we can safely assume that a rule that inspects the HTTP request body is in place. Using the knowledge of the 8KB limitation, we can now craft an attack that can be used to bypass the AWS WAF and reach the web application.

We use an interception proxy to add extra parameters to the request body to make its size larger than 8KB. This causes the AWS WAF to ignore the request and forwards it to the web application.

It is important to note that the attack payload must come after 8KB of junk data in the request body for the bypass to work.

![AWS WAF 8KB limitation attack](https://imgs.kloudle.com/blog/bypassing-the-aws-waf-protection-with-an-8kb-bullet/1673700067-aws-waf-8kb-limitation-attack.png)

![WAF bypassed request body larger than 8KB](https://imgs.kloudle.com/blog/bypassing-the-aws-waf-protection-with-an-8kb-bullet/1673700074-waf-bypassed-request-body-larger-than-8kb.png)

The response now contains the HTTP headers for kloudle.com and the output of the id command, showing that the AWS WAF was bypassed because the request body is larger than 8KB.

## How do you fix this?

Now that we understand the limitation and how attackers can abuse this to still attack your protected web applications, how do we go about fixing this? If we look at the warning that AWS presents when adding a rule that will inspect the request body, they recommend that a size constraint rule be run before the body inspection to block requests with body size greater than 8 KBs that a size constraint rule must be added alongside other rules to ensure packets larger than 8KB.

A SizeConstraint rule can be added to the ACL to perform actions on the request when a size criteria is met. AWS supports multiple criteria that can be used to work with web requests that are less than, equal to or greater than a specified number of bytes. Adding a SizeConstraint rule to block web packets of size equal to or more than 8192 bytes will ensure any malicious attempts to breach the WAF are denied. The downside to having this rule in place is that legitimate requests like file uploads or POST requests containing large VIEWSTATE data in .NET applications may also get blocked. In such cases, you may want to set the SizeConstraint rule action to Count instead of Block and evaluate if the application does receive any web request body larger than 8KB.

Most AWS admins often rely on the Core rule set managed rule group which contains a `SizeRestrictions_BODY` rule that does block requests with request body size that is at most 8,192 bytes, however as this can lead to restricted functionality in applications that do work with larger request body sizes, the rule action is set to `Count` instead of `Block`, resulting in this same scenario to play out.

Look out for a detailed fix about this on [Kloudle Academy today](https://kloudle.com/academy/a-detailed-guide-on-protecting-against-the-8kb-aws-waf-limitation)!

Update: Osama Elnaggar has also done an in-depth analysis about this limitation. You can read more about this [here](https://osamaelnaggar.com/blog/aws_waf_dangerous_defaults/).

## Conclusion

Attackers are constantly researching new ways of bypassing protection mechanisms that SREs and infrastructure owners impose. Although documented by AWS, the 8KB limitation is not well known and worse, the implications of the limitations are not well understood. In the event when a new team member joins, they inherit the infrastructure and nuances such as these, and are often unaware of the potential dangers they can create. Some organisations even choose to accept these risks as part of their infrastructure design and proceed to believe the most secure configuration is already in place.

This blog post showed what the 8KB limitation looks like in an AWS WAF configuration and how an attacker can abuse it to attack and exploit vulnerabilities on web applications behind the AWS WAF. The damage that an attacker can cause is only limited by the vulnerability that can be exploited, like in the case of the recently disclosed Log4J set of vulnerabilities, it could mean a complete compromise of the server instances from the Internet.
