---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '181225'
original_report_id: '181225'
title: Missing rel=noopener noreferrer in target=_blank links (Phishing attack)
team_handle: paragonie
created_at: '2016-11-10T01:20:55.334Z'
disclosed_at: '2016-11-13T00:43:51.032Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
---

# Missing rel=noopener noreferrer in target=_blank links (Phishing attack)

## Metadata

- HackerOne Report ID: 181225
- Weakness: 
- Program: paragonie
- Disclosed At: 2016-11-13T00:43:51.032Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Links that use target=_blank need to have rel="noopener noreferrer" in order to mitigate phishing attack (opened page can change the location of page that opened him via window.opener.location = 'http://phishingsite.com/' )

more information about this vulnerability:
https://blog.whatever.io/2015/03/07/on-the-security-implications-of-window-opener-location-replace/
https://www.jitbit.com/alexblog/256-targetblank---the-most-underestimated-vulnerability-ever/

steps to reproduce:

1\. click on any of the links below from airship.
2\. run the following javascript code in new opened page:
```
window.opener.location = 'http://phishingsite.com/'
```
The above will work even if the target domain is changed (not github.com anymore) via clicking on link from target domain.

usage of _blank in airship:

1\. https://github.com/paragonie/airship/blob/master/src/Installer/skins/admin_account.twig#L17
```
            get a password manager such as <a target="_blank" href="https://github.com/keepassx/keepassx/">KeePassX</a>.
```

2\. https://github.com/paragonie/airship/blob/58f96aa0e5002b60e74456502d9bfc9483d77b3d/src/Cabin/Bridge/public/passwords.js#L26
```
        html = 'Good password, as long as it\'s unique!<br />If you\'re not already, consider using a password manager such as <a target="_blank" href="https://github.com/keepassx/keepassx/">KeePassX</a>.';
```

3.\ https://github.com/paragonie/airship/blob/58f96aa0e5002b60e74456502d9bfc9483d77b3d/src/Installer/skins/js/admin_account.js.twig#L26
```
        html = 'Good password, as long as it\'s unique!<br />If you\'re not already, consider using a password manager such as <a target="_blank" href="https://github.com/keepassx/keepassx/">KeePassX</a>.';
```

4\. https://github.com/paragonie/airship/blob/master/src/public/js/wysihtml5/parser_rules/simple.js#L23-L26
```
      set_attributes: {
        target: "_blank",
        rel:    "nofollow"
      },
```

fix:
1. always add rel="noopener noreferrer" for links that have target=_blank, unless the opened window need to change the location using window.opener.location

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
