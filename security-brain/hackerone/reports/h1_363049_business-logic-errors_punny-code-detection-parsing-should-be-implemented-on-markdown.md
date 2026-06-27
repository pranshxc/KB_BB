---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '363049'
original_report_id: '363049'
title: Punny code Detection Parsing should be implemented on Markdown
weakness: Business Logic Errors
team_handle: liberapay
created_at: '2018-06-07T11:24:38.717Z'
disclosed_at: '2018-06-07T17:25:42.979Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
asset_identifier: '*.liberapay.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Punny code Detection Parsing should be implemented on Markdown

## Metadata

- HackerOne Report ID: 363049
- Weakness: Business Logic Errors
- Program: liberapay
- Disclosed At: 2018-06-07T17:25:42.979Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello Liberapay Security Team,

#Description 
When we insert any URL in Markdown Box in `liberapay.com/profile_name/edit/statement`, it reflects on our main profile page. 
There was main issue which I discovered was about Punny code parsing method which was not enabled on Markdown.

#Step to Reproduce
For demonstration, let's take two url.
Normal Url - apple.com and Punny Code url - аррlе.com

1) Go to liberapay.com/profile_name/edit/statement, and enter this url like this.
2) Now looking at url,it's not distinguishable ,however another one is punny code.

[Note:Since hackerone report posts detects punnycode ,so I am not inserting https in both urls ,but you can try with this format in the below screenshot.]

3) Go to markdown box and type in this format both the urls and save it.
{F306263}

4) After saving,move on to profile front page, liberapay.com/profile_name and check both the urls are displaying apple.com,however when person will click 1st link,it'll redirect to normal apple.com ,but second url on clicking will redirect to punny code url.
It's because both the urls have been decoded in the same way while in the markdown without any punny code parsing method.

{F306270}

For verification,click on my profile link ,here I already mentioned both urls,check and verify.
https://liberapay.com/kunal609


#Reason to Report
+ Since punnycode is not detecting in markdown,then it'll look exactly the same,isn't it.
+ Judging both the urls which I have mentioned,one can't differentiate between as they look exactly the same before submitting and after submitting in profile page.
+ In this way, one can redirect to another domain.
+ Also ,punny code url can be registered so a person can be redirect to other site.



#Solution
+ We can initiate punny code parsing or warning link ,where when punny code will be inserted and rendered afterwards in Markdown then ,it should display their original Punny code URL in profile page.
+ So before clicking any link,user can check that it's punny code url and not safe to click in the first place.


Thanks
Kunal
(Low impact,but still punny code parsing must be initiated in between Markdown Process for URL rendering)

## Impact

As explained in reason

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
