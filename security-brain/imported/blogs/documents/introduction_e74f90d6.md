---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-04_openai-allowed-unlimited-credit-on-new-accounts.md
original_filename: 2023-05-04_openai-allowed-unlimited-credit-on-new-accounts.md
title: '## **Introduction**'
category: documents
detected_topics:
- sso
- command-injection
- automation-abuse
- business-logic
- api-security
tags:
- imported
- documents
- sso
- command-injection
- automation-abuse
- business-logic
- api-security
language: en
raw_sha256: e74f90d640544fda2fb1118cbb8691092da5d354d0727d1369a94f899c1a0c41
text_sha256: a1a27f44224561c2b3bb77304155c38ce0c89e297d714585ccfa8477aadce0f7
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# ## **Introduction**

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-04_openai-allowed-unlimited-credit-on-new-accounts.md
- Source Type: markdown
- Detected Topics: sso, command-injection, automation-abuse, business-logic, api-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `e74f90d640544fda2fb1118cbb8691092da5d354d0727d1369a94f899c1a0c41`
- Text SHA256: `a1a27f44224561c2b3bb77304155c38ce0c89e297d714585ccfa8477aadce0f7`


## Content

---
title: "OpenAI Allowed “Unlimited” Credit on New Accounts"
page_title: "OpenAI Allowed Unlimited Credit on New Accounts"
url: "https://checkmarx.com/blog/openai-allowed-unlimited-credit-on-new-accounts/"
final_url: "https://checkmarx.com/blog/openai-allowed-unlimited-credit-on-new-accounts/"
authors: ["David Sopas (@dsopas)"]
programs: ["OpenAI (ChatGPT)"]
bugs: ["AI", "LLM", "Logic flaw", "Account verification bypass"]
publication_date: "2023-05-04"
added_date: "2023-05-04"
source: "pentester.land/writeups.json"
original_index: 1190
---

## **Introduction**

Even if you lived under a rock in the last few months, I’m sure you still have heard about OpenAI – especially their ChatGPT project. If you still don’t know what it is, let ChatGPT introduce itself: 

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

When OpenAI first allowed users to sign up for an account, it was offering a free credit as a trial to try their AI projects (around $7). 

Although it was enough for any user willing to start using ChatGPT, it was clearly insufficient for those looking forward to being the first to come up with some sort of integrated product. 

What we’ve found during the OpenAI signup process, was that there is a mechanism in place which validates user phone-numbers, which is used as a layer of validation to ensure users are unique individuals in order to prevent abuse of the free credit trial. By intercepting and modyfing the OpenAI API request, we’ve identified a vulnerability which allows us to bypass these restrictions. This allowed us to sign up for an arbitrary number of user accounts using the same phone number, getting as many free credits as we wanted. 

## **Vulnerability Details**

###  _Account Validation Behavior_

Before going into the details of how this vulnerability might be exploited, allow me to explain how the registration process worked: 

1\. Register an e-mail 

2\. Click on the e-mail activation link 

3\. Enter a phone number 

4\. Enter the validation code received by SMS 

Both e-mail and phone number must be unique, otherwise, the user would be informed that the account already exists, and no free credits would be granted. 

###  _Bypass Validation_

After understanding this process, we dove into the API underneath the web application. 

Providing a valid e-mail could be achieved by using a catch-all e-mail account on a private mail domain, or any of the many temporary e-mail services. You could even automate that with a script to monitor an inbox and follow the activation link for you. Bypassing the phone number restriction, however, was a bit more challenging. 

As a result, this is what we did: 

1\. Register Account A (https://auth0.openai.com/u/signup/) with our unique phone number 

2\. Register Account B (https://auth0.openai.com/u/signup/) with the same phone number. 

Account B was created but without being assigned the free credits. Account B was informed that the entered phone number had already got the free credits. 

How to bypass it? 

After intercepting the traffic with Burp proxy, we noticed the following request: 

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

Our first thought was to do subtle changes to the “phone_number”, prepending the country code (_00351_): 

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

This resulted in the following response: 

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

At this point, we noticed that we could use different variations of essentially the same phone number, and get the same number associated to different accounts. This would allow a malicious user to have multiple accounts with as many credits as they need, while effortlessly using the same phone number. 

Just using this technique, the attacker could keep adding leading zeros in order to create an arbitrary number of phone number variations. 

However, the amount of zeros would likely be finite, and we wanted to increase our credit value to a more respectable and significant sum, and deliver a better proof-of-concept to OpenAI. 

This is where the open-source tool REcollapse was put to use (<https://github.com/0xacb/recollapse>). This tool allows a user to fuzz inputs and bypass validations and discover normalization, canonicalization, and sanitization in web applications and APIs. 

After some initial testing, some patterns were observed to be sanitized by OpenAI API. Using Unicode encoding on certain non-ASCII bytes allowed us to bypass it and register more accounts. 

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E) ![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

##  **Root Cause?**

The likely root cause for this issue is that one upstream component, probably around user management, observes the phone number as a unique value, under the assumption that if it is invalid, it simply will not function for the purpose of account validation. 

Given the arbitrary prepended zeros and inline non-ASCII bytes, these permutations of the original value are not identical at an early point where comparison is made. However, once the system attempts to validate the phone number associated with the account, this tainted phone number is passed on to another component (or components), which sanitizes the value for prefixed zeros and unwanted bytes before using it as a proper phone number. 

This late-stage normalization can cause a massive, if not infinite, set of different values (e.g., 0123, 00123, 12u000a3, 001u000au000b2u000b3 etc.) that are treated as unique identifiers to collapse into a single value (123) upon use, which allows bypassing the initial validation mechanism altogether. 

The likely solution to this is to run the same normalization before ever processing the value, so that it is identical, both when used as a unique value upstream, and as a phone number downstream. 

## **Disclosure**

We can say that OpenAI was on top of this issue after we sent the report, even in the middle of a big Microsoft investment and lots of project changes. 

### _**OpenAI feedback:**_

> _Thank you again for your detailed report. We have validated the finding and have fixed the issue._
> 
> _We appreciate your reporting this to us and adhering to the OpenAI coordinated vulnerability disclosure policy (_[_https://openai.com/policies/coordinated-vulnerability-disclosure-policy_](https://openai.com/policies/coordinated-vulnerability-disclosure-policy) _)._

###  **Timeline:**

2 December 2022 – Report sent to OpenAI 

6 December 2022 – OpenAI replied back that they were investigating the issue 

28 February 2023 – We requested an update on the issue 

1 March 2023 – OpenAI replied that the issue was fixed 

4 May 2023 – Full Disclosure 

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

It was a pleasure to collaborate so effectively with the OpenAI , who took ownership and were professional through the disclosure and remediation process. For this reason, and a great researcher experience, we’re granting OpenAI the Checkmarx Seal of Approval. 

And, as always, our security research team will continue to focus on ways to improve application security practices everywhere

Tags:

AppSec

Awareness

English

Open-Source Security

vulnerability disclosure
