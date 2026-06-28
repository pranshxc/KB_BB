---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-26_aws-waf-bypass-invalid-json-object-and-unicode-escape-sequences.md
original_filename: 2023-07-26_aws-waf-bypass-invalid-json-object-and-unicode-escape-sequences.md
title: 'AWS WAF Bypass: invalid JSON object and unicode escape sequences'
category: documents
detected_topics:
- xss
- sqli
- command-injection
- path-traversal
- otp
- automation-abuse
tags:
- imported
- documents
- xss
- sqli
- command-injection
- path-traversal
- otp
- automation-abuse
language: en
raw_sha256: 1e42a36e3c2f7865e76eb1c62e6d8e243f77dd496f69d8aa8ea8518018d0619e
text_sha256: de25ab6ac9966fb7879c3dd728edb7cf23a4c22d625f66d139ebf418bef3a80b
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# AWS WAF Bypass: invalid JSON object and unicode escape sequences

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-26_aws-waf-bypass-invalid-json-object-and-unicode-escape-sequences.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection, path-traversal, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `1e42a36e3c2f7865e76eb1c62e6d8e243f77dd496f69d8aa8ea8518018d0619e`
- Text SHA256: `de25ab6ac9966fb7879c3dd728edb7cf23a4c22d625f66d139ebf418bef3a80b`


## Content

---
title: "AWS WAF Bypass: invalid JSON object and unicode escape sequences"
url: "https://blog.sicuranext.com/aws-waf-bypass/"
final_url: "https://blog.sicuranext.com/aws-waf-bypass/"
authors: ["Andrea Menin (@AndreaTheMiddle)"]
programs: ["AWS"]
bugs: ["WAF bypass"]
publication_date: "2023-07-26"
added_date: "2023-07-31"
source: "pentester.land/writeups.json"
original_index: 902
---

[WAAP](/tag/waap/)

# AWS WAF Bypass: invalid JSON object and unicode escape sequences

  * [ ![Andrea Menin](/content/images/size/w100/2023/07/copertina.jpg) ](/author/themiddle/)

#### [Andrea Menin](/author/themiddle/)

26 Jul 2023 • 11 min read

Share

![AWS WAF Bypass: invalid JSON object and unicode escape sequences](/content/images/size/w2000/2023/07/Screenshot-from-2023-07-26-15-39-48.png)

In recent times, the security community has been witnessing an increasing number of reports from researchers highlighting various bypass techniques targeting AWS Web Application Firewall**¹**. These bypasses have brought to light not only the absence of certain critical features but also the reliance on default configurations commonly used with both custom and managed rules.

While AWS WAF provides robust protection against a wide range of web application threats, it is essential for organizations to be aware of potential "rule bypasses" that can arise from missing features and default configurations.

**In this blog post, we will explore some of these bypass techniques** , shedding light on the underlying causes and offering insights into best practices for securing your applications.

### TL;DR

  * AWS WAF lacks inspection capabilities for form-urlencoded or XML content type bodies, only supporting plain text and JSON.
  * When a JSON body contains duplicate keys, AWS WAF considers it invalid and, by default, continues processing without blocking the request.
  * Virtual patching for a specific parameter in JSON body can be bypassed using unicode escape sequences.

## AWS WAF & ACLs

The AWS WAF service is designed to protect web applications by filtering and monitoring HTTP requests and responses. It acts as a “first line of defense”, effectively blocking **common web exploits** , such as SQL injection, cross-site scripting (XSS) attacks, and distributed denial-of-service (DDoS) attacks. By integrating seamlessly with other AWS services, WAF allows customers to fortify their applications against known vulnerabilities and emerging threats.

One common use case for the AWS WAF service is in conjunction with a load balancer (ELB) or with Amazon CloudFront, a Content Delivery Network offered by AWS. By integrating AWS WAF with ELB or CloudFront, customers can enforce security policies and prevent malicious requests from reaching their application instances. This setup ensures that potentially harmful traffic is intercepted and neutralized before it reaches the backend servers.

Basically, a user can assign an **ACL** to ELB or CloudFront that could contains managed or custom rules.

**Managed Rules?** AWS WAF provides a set of pre-configured, managed rules that are designed to protect against common web application threats and vulnerabilities. These managed rules are created and maintained by AWS security experts, who continuously update them to address emerging threats. Users can select and enable these managed rules to add an additional layer of protection to their web applications without the need for manual rule creation.

**Custom Rules?** In addition to managed rules, AWS WAF allows users to create their own custom rules tailored to their specific application requirements.Users can define their own rule conditions, such as matching specific patterns in the HTTP request or response, and set corresponding actions to be taken when a rule is triggered.

## Missing functionalities

AWS WAF makes you able to inspect a HTTP request body in **only** **two** different ways: **plain text or JSON**. As you can imagine, this means that you have to inspect www-form-urlencoded request body as a plain text and not a parsed version of the key=value sequence like on other WAFs (like ModSecurity does, for example).

In my opinion, these limitations can make it challenging to create precise rules that accurately identify malicious patterns or behaviors within request bodies. It's crucial to carefully design and fine-tune rules to strike a balance between security and minimizing false positives. Regular monitoring, analysis of logs, and iterative refinement of rules are essential to optimize the effectiveness of AWS WAF and reduce the risk of false positives.

## JSON duplicate keys

In the realm of JSON, **the treatment of duplicate keys has been a topic of discussion and varying interpretations**. The official standards, such as ECMA-404 _"The JSON Data Interchange Syntax"_ remain silent on the matter, leaving room for ambiguity. However, RFC 8259 _"The JavaScript Object Notation (JSON) Data Interchange Format"_ sheds some light on the recommended behavior.

According to RFC 8259, the names (keys) within a JSON object should ideally be unique. The usage of _"SHOULD"_ in the specification implies that while there might be valid reasons to deviate from this recommendation, careful consideration must be given to the implications before choosing an alternative approach.

The primary rationale behind insisting on unique names in JSON objects lies in achieving interoperability. With unique names, different software implementations will agree on the name-value mappings within an object. However, **when duplicate names are present, the behavior of software receiving such an object becomes unpredictable**.

Various implementations handle duplicates differently. **Some implementations only report the last name-value pair encountered** , while others may report an error or fail to parse the object entirely. On the other hand, some implementations may report all the name-value pairs, including duplicates.

To add to the mix, the ECMA-262 _"ECMAScript® Language Specification"_ **specifies that lexically preceding values for the same key within an object should be overwritten, implying a "last-value-wins" approach**.

As a practical example, attempting to parse a JSON string with duplicated names using the Java implementation by Douglas Crockford (the creator of JSON) would result in an exception being thrown due to the violation of the uniqueness requirement.

### How AWS WAF handle this?

The default behavior of AWS WAF when encountering an invalid JSON in the request body can be exploited to bypass its protection. When AWS WAF detects an invalid JSON, it offers several options for handling the request. **The default option is "None"** , which means that AWS WAF will not take any action and proceed with the request regardless of the invalid JSON.

Another option is to select "Evaluate as plain text." In this case, AWS WAF will evaluate the tokens it has parsed before encountering the invalid JSON.

By taking advantage of the default behavior, **an attacker can intentionally trigger an invalid JSON condition and ensure that AWS WAF does not block or raise any alarms**. This allows them to potentially exploit vulnerabilities or inject malicious content into the system undetected.

**Let's take a look at how different web languages handle this scenario.**

### PHP

In PHP, if a JSON document contains duplicate keys, the `json_decode()` function, which is used to parse JSON, will handle it by **overwriting the earlier occurrence of the key with the later one**. For example, in the JSON document `{"a":1,"a":2}`, the resulting PHP array would be `['a' => 2]`. The second occurrence of the key "a" overwrites the initial value of 1, resulting in the final value of 2.

### Python

In Python's JSON module, when using the `json.loads()` function to parse JSON data that contains duplicate keys, it behaves similar to 'other JSON parsers. **It keeps only the last occurrence of the key-value pair**.

For example, `json.loads('{"a":1,"a":2}')` would indeed produce the dictionary `{'a': 2}`. The second occurrence of the key "a" overwrites the initial value of 1, resulting in the final value of 2.

**Speaking about Flask** , when Flask encounters a request with JSON data containing duplicate key names, it follows the standard JSON parsing rules and only retains the last occurrence of the key-value pair. Flask's `request.json` object will reflect this behavior and provide access to the JSON data with duplicate keys by keeping only the last occurrence.

For example, if the incoming JSON request body is `{"a": 1, "a": 2}`, Flask will parse it and the resulting `request.json` object will contain `{"a": 2}`. The second occurrence of the key "a" overwrites the initial value of 1, conforming to the JSON specification.

It's important to note that Flask does not provide any built-in options or flags to modify this default behavior of handling duplicate keys in JSON. If you require different handling of duplicate keys, you would need to implement custom parsing logic (**don’t do it**) or use external libraries to manipulate the JSON data within your Flask application.

### JavaScript

In JavaScript, the `JSON.parse()` function is used to parse JSON data. When confronted with duplicate keys, the JSON parser will keep only the last occurrence of the key-value pair. For example, `{"a":1,"a":2}` would result in an object with the key "a" having the value 2.

### Why this is a problem?

In many cases, AWS WAF rules are created with the default behavior on the invalid JSON handler. By taking advantage of the default settings, an attacker can bypass a rule by **sending the same JSON parameter key name twice** , each time including different values, one harmless and one containing an attack payload.

![](https://blog.sicuranext.com/content/images/2023/07/image.png)

let's try creating a rule that checks if the string "etc/passwd" is inside any value of the JSON request body.

![](https://blog.sicuranext.com/content/images/2023/07/image-1.png)

so, basically here we’re saying “ _if any value of the JSON request body contains the string etc/passwd then block the request with a 403 status code_ “.

Now, sending a request with a JSON body that contains a RCE or LFI targeting the etc/passwd file, will results in a block:

![](https://blog.sicuranext.com/content/images/2023/07/image-2.png)request blocked by AWS WAF

Given we selected the default behavior on invalid JSON body handler, we can bypass this block just by sending two “cmd” keys:

![](https://blog.sicuranext.com/content/images/2023/07/image-3.png)rule bypass

## Virtual Patching on JSON Body

One of the primary and widely recognized applications of a Web Application Firewall is virtual patching. Virtual patching serves as an effective strategy to address vulnerabilities in web applications without making changes to the underlying codebase.

Let’s consider an example where a web application accepts a JSON parameter called “id” that is vulnerable to SQL injection attacks. Attackers can exploit this vulnerability by injecting malicious SQL code into the “id” parameter, potentially gaining unauthorized access to the application’s database.

To address this vulnerability using virtual patching, **a WAF can be configured with a rule specifically designed to restrict the “id” value to only numeric values**. This rule acts as a temporary patch, ensuring that any non-numeric input submitted as the “id” parameter is blocked or sanitized before reaching the application’s backend.

**Doing so with AWS WAF is a bit tricky**. You need to have 2 statements: the first one checks if the “id” parameter length is greater than 0, and the second statement checks if the value of the “id” parameter contains only characters from 0 to 9.

![](https://blog.sicuranext.com/content/images/2023/07/image-4.png)![](https://blog.sicuranext.com/content/images/2023/07/image-5.png)

In this first statement we’re saying: _“if a request JSON contains the key ‘id’ and the size of the value of this key is greater than 0 then do something…”_. Also, as you can see in the screenshot above, we must specify the JSON key to inspect using a JSON Pointer. For example: given this JSON `{"foo": {"bar":{"id":1}}}` to inspect only the “id” value we should configure the following JSON Pointer `/foo/bar/id`.

Now, the second statement:

![](https://blog.sicuranext.com/content/images/2023/07/image-6.png)![](https://blog.sicuranext.com/content/images/2023/07/image-7.png)

In this statement we’re saying: _“if the JSON parameter ‘id’ value does not contains only numeric characters, then block the request with a 403 status code”_.

This rule seems works well, as you can see here:

![](https://blog.sicuranext.com/content/images/2023/07/image-8.png)

And if I try to inject SQL syntax in the value:

![](https://blog.sicuranext.com/content/images/2023/07/image-9.png)request blocked by AWS WAF

AWS WAF, in its current implementation, **does not decode escape sequences inside JSON keys** when matching a given JSON Pointer of a rule. This behavior can be exploited to bypass rules that specifically target the value of a parameter, such as the “id” parameter. By replacing any character of the key with a Unicode escape sequence, an attacker can effectively evade the rule and potentially pass malicious content undetected.

![](https://blog.sicuranext.com/content/images/2023/07/image-10.png)

So, in our example I can easily bypass my rule by replacing the “i” character of the “id” JSON key with the unicode escape sequence `\u0069`:

![](https://blog.sicuranext.com/content/images/2023/07/image-11.png)rule bypass

## How other WAFs handle this?

ModSecurity is a powerful open-source web application firewall (WAF) module that provides advanced security features and protection for web applications. ModSecurity offers a wide range of security capabilities, including rule-based filtering, HTTP traffic monitoring, real-time logging, and threat intelligence integration.

In this case, ModSecurity is able to decode Unicode escape sequences within JSON keys before matching any rules. Let do an example rule and check if it works as expected.

![](https://blog.sicuranext.com/content/images/2023/07/image-16.png)a ModSecurity WAF Rule

In the rule above we’re configuring ModSecurity to check if the parameter “id” doesn’t contains only numeric characters in its value. If this is true, then block the request with a 403 response status code.

![](https://blog.sicuranext.com/content/images/2023/07/image-17.png)ModSecurity Rule with notes![](https://blog.sicuranext.com/content/images/2023/07/image-13.png)request blocked by ModSecurity Rule

Even if I try to replace some characters with an unicode escape sequence (as done before), ModSecurity blocks my request:

![](https://blog.sicuranext.com/content/images/2023/07/image-14.png)can't bypass ModSecurity Rule

After this request, ModSecurity writes a log that show me that the “id” paramter has been decoded before executing my rule:

`ModSecurity: Access denied with code 403 (phase 2). Match of "rx ^[0-9]+$" against "ARGS:id" required.`

## Conclusion

AWS WAF is a valuable service that provides protection against a range of web application attacks. However, **it’s important to understand its limitations and potential bypass** **techniques**. While AWS WAF provides a convenient and scalable solution for web application protection, considering the specific bypass discussed in this blog post, leveraging ModSecurity can provide an additional layer of defense.

Based on my experience, when it comes to virtual patching, ModSecurity offers a distinct advantage over AWS WAF. With ModSecurity, virtual patching capabilities are more flexible and powerful, allowing for comprehensive protection against vulnerabilities in web applications. ModSecurity’s extensive rule set and customizable rule engine enable security practitioners to create targeted virtual patches that address specific application vulnerabilities.

## Bonus Track: CRS or not CRS

Within AWS WAF, there is a managed rule group called Core rule set (CRS), which **may cause some confusion due to its similarity to the well-known OWASP Core Rule Set (CRS) project**. However, it’s important to note that the AWS WAF Core Rule Set is distinct from the OWASP CRS in terms of its scope and number of rules.

![](https://blog.sicuranext.com/content/images/2023/07/image-15.png)

The AWS WAF “Core rule set” comprises a modest collection of 22 rules specifically designed to address common security threats and vulnerabilities. While this rule set provides a basic level of protection, it is significantly smaller in scale compared to the extensive OWASP CRS, which consists of more than 500 rules grouped into over 10 categories of attacks.

You can find more information about the OWASP Core Rule Set project at the website [https://coreruleset.org](https://coreruleset.org/?ref=blog.sicuranext.com)

## ¹ Other AWS WAF Bypass Techniques

[AWS WAF Clients Left Vulnerable to SQL Injection Due to Unorthodox MSSQL Design Choice - GoSecureWhile doing research on Microsoft SQL (MSSQL) Server, GoSecure ethical hackers found an unorthodox design choice that ultimately led to a WAF bypass.![](https://www.gosecure.net/wp-content/uploads/2019/10/cropped-favicon-270x270.png)GoSecureMarc Olivier Bergeron![](https://www.gosecure.net/wp-content/uploads/1-sql-server.png)](https://www.gosecure.net/blog/2023/06/21/aws-waf-clients-left-vulnerable-to-sql-injection-due-to-unorthodox-mssql-design-choice/?ref=blog.sicuranext.com)[Bypassing the AWS WAF protection with an 8KB bullet — Kloudle WebsiteThe AWS WAF and Shield service can be used to protect web applications against a lot of different types of attacks. However, it has a limitation on the size of the packet that it can inspect that could result in attackers being able to bypass its protection features.![](https://kloudle.com/apple-touch-icon.png)Akash Mahajan - Founder CEO Kloudle![](https://uploads-ssl.webflow.com/610cc7a5a58576a806711235/61fd02026e3eb5846fff5515_Option2%20\(1\).png)](https://kloudle.com/blog/the-infamous-8kb-aws-waf-request-body-inspection-limitation/?ref=blog.sicuranext.com)

## Follow Andrea Menin:

  * Twitter: [https://twitter.com/AndreaTheMiddle](https://twitter.com/AndreaTheMiddle?ref=blog.sicuranext.com)
  * LinkedIn: [https://www.linkedin.com/in/andreamenin/](https://www.linkedin.com/in/andreamenin/?ref=blog.sicuranext.com)
  * YouTube: [https://www.youtube.com/rev3rsesecurity](https://www.youtube.com/rev3rsesecurity?ref=blog.sicuranext.com)
