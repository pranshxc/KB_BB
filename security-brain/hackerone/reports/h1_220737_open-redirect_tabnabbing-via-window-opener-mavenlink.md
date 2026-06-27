---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '220737'
original_report_id: '220737'
title: Tabnabbing via Window.Opener @Mavenlink
weakness: Open Redirect
team_handle: mavenlink
created_at: '2017-04-13T11:34:41.678Z'
disclosed_at: '2017-05-09T19:19:11.434Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- open-redirect
---

# Tabnabbing via Window.Opener @Mavenlink

## Metadata

- HackerOne Report ID: 220737
- Weakness: Open Redirect
- Program: mavenlink
- Disclosed At: 2017-05-09T19:19:11.434Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Details:
When you open a link in a new tab ( target="_blank" ), the page that opens in a new tab can access the initial tab and change it's location using the window.opener property.

POC: 
Edit your website in work sample, with the website URL of http://daniel-tomescu.com/hackerone/landpage.php, which has the following code.

<html>
<script>
window.opener.location.replace('http://daniel-tomescu.com/hackerone/scampage.php');
</script>

My cool page with some funny cat pictures.<br> <br>

<img style="height:400px; width:300px;" src="http://static.tumblr.com/81b6d42b4064def5e9062d5f4410c820/betml74/Yl5ml0lia/tumblr_static_impress.jpg">
</html>

Create a work sample, and add that website, but make sure to publicize your profile, in order for other users to see,  you can then click on the link to the website. This opens in a new tab, and the existing tab is silently redirected to the a website without asking the user. In a real life example, this would redirect to a phishing site to try gain credentials for users.

The javascript code that does all the magic: 
window.opener.location.replace(newURL);

Ways to solve this:

Don't open links in new tabs using the target="_blank"
Add attribute rel="noreferrer" which also disables referrer
Set the window.opener attribute to null on the new tab before redirecting, like this: <script>var w=window.open(url, "target=_blank");w.opener=null;</script>
I hope you see why this is dangerous: this method has huge potential for tricking users that click on external links from this site to be a victim of a scam page because the redirecting is made in the background, while the user is focused on another tab.

More then that, some browsers like Mozilla for Android don't even display the URL, just the page title, so the user has no way of knowing that he was redirected to a scam page.

Note that the target page doesn't have to be in the same-origin policy, so can be an entirely different domain, and the redirect happens silently while user is viewing another page.

Hope that all helps, let me know if you need more information. I can provide screenshots and/or screencasts if necessary.

Wonder if this is eligible for a bounty? :)
Hope you'll triaged this.

Kind Regards,
Jolan Saluria

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
