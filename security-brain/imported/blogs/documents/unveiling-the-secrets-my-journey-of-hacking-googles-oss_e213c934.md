---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-31_unveiling-the-secrets-my-journey-of-hacking-googles-oss.md
original_filename: 2023-03-31_unveiling-the-secrets-my-journey-of-hacking-googles-oss.md
title: 'Unveiling the Secrets: My Journey of Hacking Google’s OSS'
category: documents
detected_topics:
- xss
- command-injection
- csrf
- api-security
tags:
- imported
- documents
- xss
- command-injection
- csrf
- api-security
language: en
raw_sha256: e213c934d9e0023f50b2b16b46a9f744b21deb6848fd4b8172938c606e58a6de
text_sha256: 3591f07c2ed3be9c6ddea86ba052f2c1a507a674346a01b5a08569faeff05284
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Unveiling the Secrets: My Journey of Hacking Google’s OSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-31_unveiling-the-secrets-my-journey-of-hacking-googles-oss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, csrf, api-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `e213c934d9e0023f50b2b16b46a9f744b21deb6848fd4b8172938c606e58a6de`
- Text SHA256: `3591f07c2ed3be9c6ddea86ba052f2c1a507a674346a01b5a08569faeff05284`


## Content

---
title: "Unveiling the Secrets: My Journey of Hacking Google’s OSS"
url: "https://7h3h4ckv157.medium.com/unveiling-the-secrets-my-journey-of-hacking-googles-oss-cdd9ef3c7aa"
authors: ["7𝖍3𝖍4𝖈kv157 (@7h3h4ckv157)"]
programs: ["Google"]
bugs: ["CSRF", "Self-XSS"]
publication_date: "2023-03-31"
added_date: "2023-03-31"
source: "pentester.land/writeups.json"
original_index: 1315
scraped_via: "browseros"
---

# Unveiling the Secrets: My Journey of Hacking Google’s OSS

Unveiling the Secrets: My Journey of Hacking Google’s OSS
7h3h4ckv157
Follow
4 min read
·
Mar 31, 2023

416

1

- August 22, 2022

Press enter or click to view image in full size
Let’s dive into it!

Dear Infosec,

I am excited to share with you my experience of discovering a security vulnerability in Google’s open-source software (OSS) last year. Imagine acquiring an acknowledgement from one of the biggest tech companies in the world for uncovering a security vulnerability in their open-source software. It was an exhilarating experience, but also one that taught me a lot about the importance of security research and the challenges that come with it.

In this blog post, I want to share my journey of hacking Google’s OSS, from the initial discovery to the reporting process and beyond. I hope that by sharing my experience, others will be inspired to pursue similar work and contribute to the ongoing effort to keep our digital world safe and secure.

Google Cloud Platform (GitHub) contain code samples used on cloud.google.com Here’s the GitHub link. I decided to put my skills to the test by reviewing a Python repository (REDACTED) because it’s a language I’m acquainted with and have some experience.

About the Vulnerability

Upon reviewing the code, I found unsanitized input can be accepted from the HTTP request inside the below function where it is used to render an HTML page returned to the user.

def exam_task_handler(): 

  payload = request.get_data(as_text=True) or '(empty payload)'  
  print('Received task with payload: {}'.format(payload))  
  return'Printed task payload: {}'.format(payload)
Press enter or click to view image in full size
Proof
<py-script>
PyScript is a framework that allows users to create rich Python applications
in the browser using HTML's interface and the power of Pyodide
WASM, and modern web technologies. 

The PyScript framework provides users at every experience level 
with access to an expressive, easy-to-learn programming language with 
countless applications.

(Copied)
</py-script>

But the function bears value through a POST request, If the endpoint only abides by the payload through a POST request, this vulnerability would indeed fall under the classification of Self-XSS. To prevent the execution of JS in the browser it’s essential to sanitize all input from the HTTP request before using it in any context, including rendering an HTML page. Sanitization can involve removing or encoding any potentially malicious characters to prevent them from being executed as code.

Making Impact
CSRF + Self-XSS

By chaining these two bugs together, I was able to demonstrate the potential risks of even seemingly minor vulnerabilities in the code. Self-XSS with CSRF permits me to bypass this restriction and trigger an impactful XSS.

Get 7h3h4ckv157’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Steps that I used:

1. Visit the service

2. Navigate to the /example_task_handler endpoint

3. You will receive a "Method not allowed" error 
  because only HTTP POST requests are allowed.

4. Intercept the request and change the method type from GET to POST.
  
5. Trigger the XSS payload 
  which will allow you to execute malicious code on your own system 
  (Self-XSS)
  
6. Chain the Self-XSS vulnerability with a CSRF attack 
  (meaningful impact)

While performing the CSRF attack: The malicious POST request from victim’s browser to a vulnerable web application, and the request appears to come from a legitimate user. The victim’s browser is then tricked into submitting the request, which can cause the application to perform an unintended action on behalf of the user. If the POST request contains a payload that includes a Self-XSS vulnerability, then the script will execute in the victim’s browser, allowing the attacker to execute arbitrary code and potentially steal sensitive information or perform unauthorized actions.

I reported this issue to Google, as usual I have some conversations with them through comments and then finally they accepted my report.

triaged
14:17 | 22.08.2022

closed
15:59 | 22.08.2022

triaged
17:56 | 22.08.2022

accepted
19:38 | 23.08.2022

fixed
05:53 | 22.09.2022

This was something I get back from them.

ks…@google.com 26.09.2022 | 12:46 | #34

Hello! For credit you can be visible on Honorable mentions

Press enter or click to view image in full size
Honorable Mention

The decision to participate in bug bounty programs or disclose vulnerabilities should be driven by a desire to improve security and promote responsible disclosure practices, rather than solely by the potential for financial reward. Honorable mention is a valuable recognition in building a reputation within the security community and can lead to future opportunities for collaboration, networking, and career advancement.

It’s true that securing code samples in open-source projects may not always result in a monetary bounty from the project maintainers or companies that offer bug bounty programs. But it’s important to improve the security of software systems that people rely on. Many security researchers and professionals participate in bug bounty programs or disclose vulnerabilities as a way to give back to the community and help make the internet a safer place. Even if there is no financial reward, the recognition and sense of accomplishment that comes with discovering and mitigating a security risk can be a powerful motivator.

Therefor I reported another bug directly through GitHub Issues.

Check this out: Link

Don’t forget to connect with me on twitter

Thank you for taking the time to read my blog post. I hope you found it informative and engaging. If you have any questions or comments, please don’t hesitate to reach out to me on Twitter: @ 7h3h4ckv157

I look forward to connecting with you on social media!

Connect through Twitter
Connect through LinkedIn
