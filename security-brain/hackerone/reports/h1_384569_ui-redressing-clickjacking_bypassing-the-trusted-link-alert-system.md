---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '384569'
original_report_id: '384569'
title: Bypassing the Trusted Link Alert System
weakness: UI Redressing (Clickjacking)
team_handle: vanilla
created_at: '2018-07-20T14:31:59.105Z'
disclosed_at: '2019-06-07T20:20:56.148Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
asset_identifier: '*.vanillaforums.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- ui-redressing-clickjacking
---

# Bypassing the Trusted Link Alert System

## Metadata

- HackerOne Report ID: 384569
- Weakness: UI Redressing (Clickjacking)
- Program: vanilla
- Disclosed At: 2019-06-07T20:20:56.148Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
I have discovered a means of bypassing the system that will alert users of an untrusted link utilizing the Right to Left Overrride unicode character. The alert looks like this: https://i.imgur.com/9rp1K7b.mp4

**Description:**
For this demonstration, I have added "facebook.com" to the trusted sites. Here is the screen: https://i.imgur.com/7bYOgmH.png 

If a link leads to http://facebook.com, Vanilla will not give an alert. This looks like this: https://i.imgur.com/12Ou6F9.mp4

To bypass this system, I have utilized the Right to Left Override unicode character. The character reverses the text following it, so http://{rtlo}facebook.com would appear as http://moc.koobecaf. However, when a domain contains unicode characters, the domain is formatted to a different version. So http(s)://{rtlo}facebook.com actually leads to xn--facebook-ps49b.com. If an attacker purchases this domain, he can provide a link that could appear as facebook.com and will be trusted by Vanilla. No warning will be given, and they will be taken directly to the dangerous link. This is shown here: https://i.imgur.com/inHussi.mp4
NOTE: In the gif, I used whatever.com in square brackets, this can be changed to facebook.com to complete the illusion.

NOTE: I did not purchase the domain. I added it to my /etc/hosts file, but it is purchasable here: https://i.imgur.com/iQ68Pm7.png

## Steps to reproduce:

1. Enumerate for the trusted domains of a forum
2. Navigate to any text field you can use BBCode on. In order to gain a meaningful shell or something of the like, another user needs to see it.
3. Find a way to copy the U+202e character. Windows offers a tool called character map, but you can also do this here: http://www.unicode-symbol.com/u/202E.html
4. Go to another text field away from Vanilla to prepare your payload. I personally like the url bar of a new tab.
5. In the text field, type (if you know the trusted site will force https, like google use that) http://trusteddomain.com
6. Then paste the character after the double slashes.
7. You will see the link in reverse. For example, http://{rtlo}link.com turns into http://moc.knil.
8. Memorize the reverse version and retype it in another field. Then place the character in the same spot. 
9. Paste this into a tab and hit enter. You will see the ACE formatted url that you must buy. google.com With the character is https://xn--moc-4t7s.elgoog/
10. Craft your final payload and copy it (I used Ctrl A and Ctrl C in a new tab). Go back to your vanilla.
11. Type [whatyouwanttodisplay.com]() Paste the payload into the parentheses. 

## Anything else we should know?
Please watch the attached gifs for further clarification.
This affects any forum whether its live or local. 
This was difficult to pin a category on, but I would consider it Bypass of a Forced Warning.

This makes phishing and social engineering **exponentially** easier. 
The user won't know until it's too late.

## Impact

The attacker could get a reverse shell on anybody. If that person has authority in a Vanilla system and credentials are found for the account, the attacker could potentially have total control of the forum. If the server host clicks the link, a www-data shell will be given on the site. By default, everyone locally has read privileges on the configuration files, database credentials could be compromised as well. 
The attack could do anything that a normal attacker does with a false link, he could lead the user to phishing, malware, keyloggers, a shell, etc.

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
