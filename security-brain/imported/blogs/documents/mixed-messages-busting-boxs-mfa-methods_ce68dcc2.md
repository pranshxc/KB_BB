---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-18_mixed-messages-busting-boxs-mfa-methods.md
original_filename: 2022-01-18_mixed-messages-busting-boxs-mfa-methods.md
title: 'Mixed Messages: Busting Box’s MFA Methods'
category: documents
detected_topics:
- mfa
- otp
- sso
- command-injection
- cloud-security
tags:
- imported
- documents
- mfa
- otp
- sso
- command-injection
- cloud-security
language: en
raw_sha256: ce68dcc2597007931884d0fd9acacb513f6b976078c6ccea8607fae9ff8ca71b
text_sha256: e04d004e24003d00d7d125c87da3b8cb51f6c4ec515d18935536d44ad3391ac6
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Mixed Messages: Busting Box’s MFA Methods

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-18_mixed-messages-busting-boxs-mfa-methods.md
- Source Type: markdown
- Detected Topics: mfa, otp, sso, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `ce68dcc2597007931884d0fd9acacb513f6b976078c6ccea8607fae9ff8ca71b`
- Text SHA256: `e04d004e24003d00d7d125c87da3b8cb51f6c4ec515d18935536d44ad3391ac6`


## Content

---
title: "Mixed Messages: Busting Box’s MFA Methods"
page_title: "Mixed Messages: Busting Box’s MFA Methods | Varonis"
url: "https://www.varonis.com/blog/box-mfa-bypass-sms"
final_url: "https://www.varonis.com/blog/box-mfa-bypass-sms"
authors: ["Tal Peleg"]
programs: ["Box"]
bugs: ["OTP bypass", "2FA / MFA bypass"]
publication_date: "2022-01-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2999
---

Varonis Threat Labs discovered a way to bypass multi-factor authentication (MFA) for Box accounts that use an SMS code for login verification.  
  
Using this technique, an attacker could use stolen credentials to compromise an organization’s Box account and exfiltrate sensitive data _without_ access to the victim’s phone.  
  
We disclosed this issue to Box on November 2, 2021 via HackerOne and Box released a fix.  
  
Sound familiar? This is the second Box MFA bypass we’ve discovered recently. You can read about our [authenticator-based MFA bypass](/blog/box-mfa-bypass-totp/?hsLang=en).

## What’s the Score?

With increased pressure to adopt and enforce multi-factor authentication, many SaaS providers now offer multiple MFA options to provide users a second line of defense against credential stuffing and other password attacks. Varonis Threat Labs has been analyzing MFA implementations to see just how secure they really are.

According to Box, 97,000 companies and 68% of the Fortune 500 rely on the company’s solutions to access information from anywhere and collaborate with anyone.

Like many applications, Box allows users without Single Sign-On (SSO) to use an authenticator app, like Okta Verify or Google Authenticator, or SMS with a one-time passcode as a second step in authentication.

## How SMS Verification Works in Box

After entering a username and password in Box’s login form, Box sets a session cookie and redirects the user to either:

  * A form to enter a time-based one-time password (TOTP) if the user is enrolled with an authenticator app, or
  * A form to enter an SMS code if the user enrolled to receive a passcode via SMS

When the user navigates to the SMS verification form, a code is sent to their phone. They must enter this code to gain access to their Box.com account.

## What’s the Issue? Mixing MFA Modes

If the user does not navigate to the SMS verification form, no SMS message will be sent, but a session cookie is still generated. A malicious actor only needs to enter the user’s email and password—stolen from a password leak or phishing attack, for example—to get a valid session cookie. No SMS message code required.

After the cookie is generated, the threat actor can abandon the SMS-based MFA process (which is what the user is enrolled in) and instead initiate the TOTP-based MFA process—thus mixing MFA modes.

The attacker completes the authentication process by posting a factor ID and code from their own Box account and authenticator app to the TOTP verification endpoint using the session cookie they received by providing the victim’s credentials.

Box did not verify whether the victim was enrolled in TOTP verification and did not validate that the authenticator app used belonged to the user that was logging in. This made it possible to access the victim’s Box account without the victim’s phone and without notifying the user via SMS.

See the attack in action:

## Attack Flow

  1. Attacker enrolls in multi-factor authentication using an authenticator app and stores the device’s factor ID.
  2. Attacker enters a user’s email address and password on account.box.com/login.
  3. If the password is correct, the attacker’s browser is sent a new authentication cookie and redirects to: **/2fa/verification**.
  4. The attacker, however, does not follow the redirect to the SMS verification form. Instead, they pass their own factor ID and code from the authenticator app to TOTP verification endpoint:**/mfa/verification**.
  5. The attacker is now logged in to the victim’s account and the victim does not receive an SMS message.

![Blog_BoxSMSMFA_Diagram_202201_FNL](https://www.varonis.com/hs-fs/hubfs/Blog_BoxSMSMFA_Diagram_202201_FNL.png?width=849&name=Blog_BoxSMSMFA_Diagram_202201_FNL.png)  

## Takeaways

With all the buzz around mandatory MFA from companies like [Salesforce](https://www.okta.com/blog/2021/11/the-salesforce-mfa-requirement-secure-your-applications-and-users-before-february-2022/) and Google, as well an [executive order from the White House](https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/), we want to underscore that MFA implementations are prone to bugs, just like any other code.

MFA can provide a false sense of security. Just because MFA is enabled doesn’t necessarily mean an attacker must gain physical access to a victim’s device to compromise their account.

Our team has demonstrated not one, but two application flaws that allowed us to access a victim’s MFA-enabled Box account with only username and password. Spoiler alert: Box is not the only major SaaS provider that we've been able to bypass.

This highlights the need for a data-centric approach. CISOs should ask themselves:

  * Would I know if MFA was disabled or bypassed for a user across all my SaaS applications?
  * How much data can an attacker access if they compromise a normal user account?
  * Is any data unnecessarily exposed to too many users (or exposed publicly)?
  * If a user accesses data abnormally, will I get an alert?

We recommend you start by securing data where it lives. When you limit access and monitor the data itself, your likelihood of data exfiltration due to a perimeter bypass drops significantly.

If you have general questions for our research team, please [reach out](https://info.varonis.com/en/contact-us?hsLang=en)! If you think you’re under attack, open a case with our [incident response team](https://info.varonis.com/en/incident-response?hsLang=en).

### About Varonis for Box

Easily visualize excessive external sharing, spot personal accounts activity, and uncover risky misconfigurations. By integrating permissions, user activity, and data sensitivity, you can identify and address exposures, detect internal and external threats, and accelerate cross-cloud investigations. You can [request a demo or start a free trial here](https://info.varonis.com/en/demo-request?hsLang=en).

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
