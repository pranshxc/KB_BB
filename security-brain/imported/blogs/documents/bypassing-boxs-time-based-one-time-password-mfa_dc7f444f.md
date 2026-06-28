---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-02_bypassing-boxs-time-based-one-time-password-mfa.md
original_filename: 2021-12-02_bypassing-boxs-time-based-one-time-password-mfa.md
title: Bypassing Box’s Time-based One-Time Password MFA
category: documents
detected_topics:
- mfa
- otp
- sso
- command-injection
- rate-limit
- cloud-security
tags:
- imported
- documents
- mfa
- otp
- sso
- command-injection
- rate-limit
- cloud-security
language: en
raw_sha256: dc7f444fd335f1b97ed5a15a4bbfce4d35cc0bc02452f73d990e91eb7d25215f
text_sha256: 7268ac62abb2e574a9735c5619a7d51deec7d481e9a48eae714c3cee6d8d41f2
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Box’s Time-based One-Time Password MFA

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-02_bypassing-boxs-time-based-one-time-password-mfa.md
- Source Type: markdown
- Detected Topics: mfa, otp, sso, command-injection, rate-limit, cloud-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `dc7f444fd335f1b97ed5a15a4bbfce4d35cc0bc02452f73d990e91eb7d25215f`
- Text SHA256: `7268ac62abb2e574a9735c5619a7d51deec7d481e9a48eae714c3cee6d8d41f2`


## Content

---
title: "Bypassing Box’s Time-based One-Time Password MFA"
page_title: "Bypassing Box's Time-based One-Time Password MFA"
url: "https://www.varonis.com/blog/box-mfa-bypass-totp/"
final_url: "https://www.varonis.com/blog/box-mfa-bypass-totp"
authors: ["Tal Peleg"]
programs: ["Box"]
bugs: ["OTP bypass", "2FA / MFA bypass"]
publication_date: "2021-12-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3119
---

The Varonis research team discovered a way to bypass multi-factor authentication for Box accounts that use authenticator apps such as Google Authenticator.

Using the technique demonstrated below, an attacker could use stolen credentials to compromise an organization's Box account and exfiltrate sensitive data without providing a one-time password.

**We disclosed this issue to Box on November 3rd via HackerOne and the team has since released a fix.**

## **Background**

In January 2021, Box launched the ability for accounts to use TOTP-based authenticator apps such as Google Authenticator, Okta Verify, Authy, Duo, and others, and others.

Box recommends TOTP over SMS-based authentication for obvious reasons-SMS messages can be hijacked via SIM swapping, port-out fraud, and other well-known techniques.

Authenticator apps that comply with the TOTP (time-based one-time password) [algorithm ](https://datatracker.ietf.org/doc/html/rfc6238)are not only easier for the end-user, but much safer than SMS. **Usually**.

## **How does Box MFA work?**

When a user adds an authenticator app to their Box account, the app is assigned a **factor ID** behind the scenes. Any time that user tries to login, Box prompts the user for their email and password followed by a one-time password from their authenticator app.

If the user doesn't provide the second factor, they won't be able to access the files and folders in their Box account. This provides a second line of defense in the event a user has a weak (or leaked) password.

### **What's the issue?**

Our team discovered that the **/mfa/unenrollment** endpoint did not require the user to be fully authenticated in order to remove a TOTP device from a user's account. As a result, we were able to successfully **unenroll** a user from MFA after providing a username and password but **before** providing the second factor.

After performing the unenrollment action, we were able to login without any MFA requirements and gain full access to the user's Box account, including all their files and folders. Prior to Box's fix, attackers could compromise user accounts via credential stuffing, brute force, etc.

**See the attack in action:**

## **Attack Flow**

1\. The attacker enters a user's email address and password on account.box.com/login

2\. If the password is correct, the attacker's browser is sent a new authentication cookie that grants access to a limited set of endpoints, including the **/mfa/unenrollment** endpoint

3\. Instead of passing a valid one-time password from an authenticator app to the **/mfa/verification** endpoint, the attacker POSTs the device's factor ID to the **/mfa/unenrollment** endpoint and successfully unenrolls the device/user account combo from TOTP-based MFA

4\. The attacker can now login again using single-factor authentication and gain full access to the user's account and their data

![](https://www.varonis.com/hubfs/MicrosoftTeams-image-7-1200x1871-png.png)

## **Takeaways**

MFA is a step towards a safer internet and more resilient authentication for the SaaS apps we rely on, but MFA isn't perfect. There has been a massive push towards TOTP-based MFA, but if there are any flaws in its implementation, it can be bypassed.

Although nobody is immune to bugs and vulnerabilities, to minimize the likelihood of introducing an authentication flaw into your application, it's highly recommended to delegate your MFA implementation to a provider (e.g., Okta) that specializes in authentication.

The above example is simply one bypass technique for one SaaS platform. Many more exist-some of which we'll publish soon. Robust authentication is just one layer of defense. It's vital to take a defense-in-depth approach that assumes breach, especially if you're concerned about[ insider threats](/use-case/insider-risk-management?hsLang=en).

Finally, your security is only as good as your weakest link. In addition to requiring MFA, use SSO where possible, enforce strong password policies, monitor sites like [_HaveIBeenPwnd_ ](https://haveibeenpwned.com/)for breached accounts associated with your domain, and avoid using easy-to-find answers ("What's your mother's maiden name?") as part of your authentication flows.

### What should I do now?

Below are three ways you can continue your journey to reduce data risk at your company:

1

[Schedule a demo with us](https://info.varonis.com/en/demo-request?hsLang=en "https://info.varonis.com/en/demo-request") to see Varonis in action. We'll personalize the session to your org's data security needs and answer any questions.

2

[See a sample of our Data Risk Assessment](https://www.varonis.com/hubfs/docs/DRA-sample.pdf?hsLang=en "https://info.varonis.com/hubfs/docs/DRA-sample.pdf?hsLang=en") and learn the risks that could be lingering in your environment. [Varonis' DRA](https://info.varonis.com/en/data-risk-assessment?hsLang=en "https://info.varonis.com/en/data-risk-assessment") is completely free and offers a clear path to automated remediation.

3

Follow us on[ LinkedIn](https://www.linkedin.com/company/varonis "https://www.linkedin.com/company/varonis"), [YouTube](https://www.youtube.com/channel/UCE9xUuH4lhIUDOFR1OHlNNg "https://www.youtube.com/channel/UCE9xUuH4lhIUDOFR1OHlNNg"), and [X (Twitter)](https://twitter.com/varonis "https://twitter.com/varonis") for bite-sized insights on all things data security, including DSPM, threat detection, AI security, and more.

![Tal Peleg](https://www.varonis.com/hubfs/tal-peleg.jpg)

Tal Peleg Tal Peleg is a senior security researcher at Varonis. Also known as TLP, Tal is a full-stack hacker with experience in malware analysis, Windows domains, web servers, and cloud. His research is currently focused on cloud applications and APIs.
