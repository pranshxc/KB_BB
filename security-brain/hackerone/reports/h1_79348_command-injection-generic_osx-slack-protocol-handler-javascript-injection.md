---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '79348'
original_report_id: '79348'
title: OSX slack:// protocol handler javascript injection
weakness: Command Injection - Generic
team_handle: slack
created_at: '2015-07-29T05:47:55.388Z'
disclosed_at: '2016-06-24T16:17:17.826Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 72
tags:
- hackerone
- command-injection-generic
---

# OSX slack:// protocol handler javascript injection

## Metadata

- HackerOne Report ID: 79348
- Weakness: Command Injection - Generic
- Program: slack
- Disclosed At: 2016-06-24T16:17:17.826Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The Mac Slack app version 1.1 introduced the slack:// protocol handler. Due to improper input sanitization, arbitrary Javascript code can be run in the context of the client app if the user clicks on a slack:// link on a website or email. I have confirmed this issue still exists in the 1.1.1 release.

PoC
=== 
If a user clicks this link, a message will be posted on their behalf to their general channel.
    <a href="slack://test?team=1&a=');eval(atob('VFNTU0Iuc2VuZE1zZ0Zyb21Vc2VyKHdpbmRvdy5UUy5jaGFubmVscy5nZXRHZW5lcmFsQ2hhbm5lbCgpLmlkLCAiSGVsbG8sIEkgYW0gcHJvb2Ygb2YganMgaW5qZWN0aW9uIik7'));String('">Click me for a good time</a>

or go to http://computerality.com/t/slack_report.html

The example javascript that is run in the context of the client app is:
    TSSSB.sendMsgFromUser(window.TS.channels.getGeneralChannel().id, "Hello, I am proof of js injection");

Details
======
The Objective-C function responsible for handling the scheme processing is:
 -[SLAppDelegate handleURLEvent:withReplyEvent:]

The argument is passed into the format string: "TSSSB.handleDeepLink(‘%@‘);”. Then the resulting string is evaluated in javascript via the stringByEvaluatingJavaScriptFromString method call.

An attempt is made to sanitize input by calling stringByAddingPercentEscapesUsingEncoding. This function will perform escaping of certain characters but leave the single quote character unmodified.

In the PoC link, the team argument is set to any value. When an invalid team id is used, a popup appears but the rest of the Javascript still runs. Next, the a parameter is processed. We escape and end the TSSSB.handleDeepLink() function call. Next we want to run arbitrary Javascript without having any spaces. To do this, we use the base64 decoding function atob() and call eval() on the result. Finally, the Javascript needs to continue to be valid so we create an unused object using the String constructor.

If you have any other questions or if anything needs clarification, please let me know.

Thanks!

-Jay

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
