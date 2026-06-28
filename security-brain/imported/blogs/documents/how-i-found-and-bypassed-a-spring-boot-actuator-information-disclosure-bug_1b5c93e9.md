---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-19_how-i-found-and-bypassed-a-spring-boot-actuator-information-disclosure-bug.md
original_filename: 2024-07-19_how-i-found-and-bypassed-a-spring-boot-actuator-information-disclosure-bug.md
title: How I Found and Bypassed a Spring Boot Actuator Information Disclosure Bug
category: documents
detected_topics:
- information-disclosure
- sso
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- information-disclosure
- sso
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 1b5c93e9b6d17ecd78453120799297fb1d368ff6504eb4fbfbe602e035fa703e
text_sha256: edf7a613033a386ab68093ee641adaccee46bb3bdf958cb9dbdfa6044d56fb38
ingested_at: '2026-06-28T07:32:35Z'
sensitivity: unknown
redactions_applied: false
---

# How I Found and Bypassed a Spring Boot Actuator Information Disclosure Bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-19_how-i-found-and-bypassed-a-spring-boot-actuator-information-disclosure-bug.md
- Source Type: markdown
- Detected Topics: information-disclosure, sso, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:35Z
- Redactions Applied: False
- Raw SHA256: `1b5c93e9b6d17ecd78453120799297fb1d368ff6504eb4fbfbe602e035fa703e`
- Text SHA256: `edf7a613033a386ab68093ee641adaccee46bb3bdf958cb9dbdfa6044d56fb38`


## Content

---
title: "How I Found and Bypassed a Spring Boot Actuator Information Disclosure Bug"
url: "https://cametom006.medium.com/how-i-found-and-bypassed-a-spring-boot-actuator-information-disclosure-bug-c4930b740a50"
authors: ["Fahad Faisal (@cametome006)"]
bugs: ["Spring Boot", "Information disclosure"]
publication_date: "2024-07-19"
added_date: "2024-07-22"
source: "pentester.land/writeups.json"
original_index: 152
scraped_via: "browseros"
---

# How I Found and Bypassed a Spring Boot Actuator Information Disclosure Bug

Fahad Faisal
 highlighted

How I Found and Bypassed a Spring Boot Actuator Information Disclosure Bug
Fahad Faisal
Follow
4 min read
·
Jul 18, 2024

137

1

Greetings, community! Today, I want to share the fascinating journey of how I discovered an information disclosure bug in a Spring Boot Actuator while hunting on a bug bounty program on the Inspectiv platform, and the steps I took to bypass it.

METHODOLOGY

First, I employed the haktrails tool to gather all the subdomains associated with the target. This tool, which you can find here, is particularly effective in enumerating subdomains by leveraging the securitytails API.

Once I had a comprehensive list of subdomains, I filtered out the live ones using httpx. With the active subdomains identified, I proceeded to the fuzzing phase. For this, I utilized a custom directory fuzzing wordlist tailored to the specifics of the target.

The Spring Boot Actuator Gold Mine

After analyzing the fuzzing results, I discovered a subdomain had an exposed /actuator directory. This directory revealed all the available Actuator endpoints, which I decided to investigate further based on the responses received from the /actuator endpoint.

/dump: Displayed a clutter of threads, including stack traces.
/trace: Showed the last several HTTP messages, potentially including session identifiers.
/logfile: Output the contents of the log file.
/shutdown: Allowed for the shutdown of the application.
/mappings: Displayed all the MVC controller mappings.
/env: Provided access to the configuration environment.
/restart: Restarted the application.

The following Actuator endpoints were particularly noteworthy:

/env: Provided access to the configuration environment. While the credentials were redacted, some internal data was still exposed.
/metrics/http.client.requests: Exposed email addresses of customers and SQL statements used internally.
Press enter or click to view image in full size

I decided to report the issue to the relevant team. They promptly triaged and rewarded me for the report, acknowledged the potential security risks, and took the necessary steps to mitigate them.

Attempting to Bypass the Fix

A couple of months later, while reviewing old reports, I decided to recheck the subdomains to see if any other Actuator hosts were still active. Upon examining the fuzzing results, I discovered that one host’s IP address still had an exposed /actuator endpoint. However, when attempting to access it, I encountered a 401 Unauthorized response. This indicated that the team had implemented a fix, likely using firewall rules, to restrict unauthorized access to sensitive Actuator endpoints.

Get Fahad Faisal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

With my curiosity at its peak, I turned to a tool 4-ZERO-3,available at https://github.com/Dheerajmadhukar/4-ZERO-3, which contains various techniques to bypass 403/401 restrictions. I’d like to give a shout-out to the author of this tool for their valuable contribution.

Press enter or click to view image in full size

After the results came out from, this tool,I discovered that the firewall rules could be bypassed by manipulating the Actuator URL. Specifically, appending a semicolon (;) followed by additional endpoints, such as /env, to the Actuator URL allowed me to access otherwise restricted information. For instance, accessing https://test.com/actuator;/env successfully bypassed the firewall restrictions and provided access to sensitive data.

After reporting the issue, the team promptly addressed the vulnerability. As a precautionary measure, they temporarily excluded the exposed Actuator endpoints from the program policy while actively working on implementing a robust fix. I extend my sincere thanks to @GodfatherOrwa for providing me with valuable insights and tips that helped me in finding this issue.

This experience underscores the crucial need for regular monitoring of our digital assets. By harnessing shared expertise and effective tools, we fortify our defenses and protect sensitive data from emerging threats.

Thank you for reading my story. Stay tuned for more insights in my next blog post!
