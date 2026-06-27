---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '221043'
original_report_id: '221043'
title: CSRF token validation is missing
weakness: Cross-Site Request Forgery (CSRF)
team_handle: nextcloud
created_at: '2017-04-14T18:25:57.134Z'
disclosed_at: '2017-04-19T06:55:51.732Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# CSRF token validation is missing

## Metadata

- HackerOne Report ID: 221043
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: nextcloud
- Disclosed At: 2017-04-19T06:55:51.732Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Greetings,

Hello Security Team,

### Summary
I know this is a medium risk issue but i want you guys to be aware of it that the CSRF token validation is missing at the time of login on `https://portal.nextcloud.com/login.php` login page.

### PoC Code:
```
<form name="frmlogin" action="https://portal.nextcloud.com/login.php" method="post" onsubmit="return ValidateForm();">
	<div class="row">
		<div class="col-xs-12">
			<div class="form-group">
				<label class="control-label">Email</label>
				<input type="text" name="member_username" id="member_username" value="" class="form-control">
			</div>
		</div><!-- col-sm-12 -->
		<div class="col-xs-12">
			<div class="form-group">
				<label class="control-label">Password</label>
				<input type="password" name="member_password" class="form-control">
			</div>
		</div><!-- col-sm-12 -->
		<div class="col-xs-12">
			<div class="form-group text-center">
				<button class="btn btn-search btn-primary col-xs-12 mb10" style="padding:10px;margin-top:10px;" type="submit" name="login" value="Login Now">Login Now</button>
				<a href="https://support.nextcloud.com/#password_reset">Forgot Password?</a>
			</div>
		</div><!-- col-sm-12 -->
	</div><!-- End Row -->
</form>
<script type="text/javascript">
	var tabs = '';
	//<![CDATA[
	function ValidateForm()
	{
		var f = document.frmlogin;
		if(f.member_username.value=='')
		{
			alert('Please enter the Username.');
			f.member_username.focus(); return false;
		}
		if(f.member_password.value=='')
		{
			alert('Please specify the Password.');
			f.member_password.focus(); return false;
		}
	}
	//]]>
</script>
```
### PoC Attached is the html code: {F175917}

### Impact:
* An attacker can Brute force their password.
* Brute force Attack


Regards,
j3

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
