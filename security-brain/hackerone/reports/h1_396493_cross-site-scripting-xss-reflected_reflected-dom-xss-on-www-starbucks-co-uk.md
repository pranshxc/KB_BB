---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '396493'
original_report_id: '396493'
title: Reflected DOM XSS on www.starbucks.co.uk
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: starbucks
created_at: '2018-08-17T11:25:53.034Z'
disclosed_at: '2020-06-16T21:21:07.555Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: www.starbucks.co.uk
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected DOM XSS on www.starbucks.co.uk

## Metadata

- HackerOne Report ID: 396493
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: starbucks
- Disclosed At: 2020-06-16T21:21:07.555Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

`www.starbucks.co.uk` is vulnerable to reflected DOM XSS due to 2 seemingly unexploitable issues. The first issue is unfixed for over a year now, #252908, the second issue originates in a 3rd party module called prettyPhoto. 

**Description:**

Visiting the following link results in a JavaScript alert (use Firefox or Edge, Chrome's XSS Auditor blocks this particular payload):

`https://www.starbucks.co.uk/shop/card/egift/thank-you/anything%2522onclick=%2522confirm(document.domain)#!\'\,\*\,/1`

This is possible because:

1. there is a seemingly harmless HTML attribute injection into a `<link rel="canonical">` element (unfixed for over a year, see #252908) and
2. the prettyPhoto JavaScript module allows to trigger the `click` event on any existing HTML element.

The following is done by prettyPhoto in https://www.starbucks.com/static/resource/shop_js/676938998_en-US:

```js
function d() {
  url = location.href;
  hashtag = (url.indexOf("#!") != -1) ? decodeURI(url.substring(url.indexOf("#!") + 2, url.length)) : false;
  return hashtag
}

hashIndex = d();
hashRel = hashIndex;
hashIndex = hashIndex.substring(hashIndex.indexOf("/") + 1, hashIndex.length - 1);
hashRel = hashRel.substring(0, hashRel.indexOf("/"));
hashIndex = parseInt(hashIndex);
hashRel = hashRel.replace(/([ #;&,.+*~\':"!^$[\]()=>|\/])/g, "\\$1");
setTimeout(function() {
  b("a[rel^='" + hashRel + "']:eq(" + hashIndex + ")").trigger("click")
}, 50)
```

Notice how the user-controlled `hashRel` variable is [sanitized to prevent DOM XSS](https://www.saotn.org/prettyphoto-dom-based-xss/#how-to-fix-prettyphoto-dom-based-xss) in a quite obscure manner. It only works because it prefixes `=` with a `\` ruining all standard DOM XSS payloads known to me. Also notice that `\` is **not** escaped which means that it's possible to inject arbitrary valid jQuery selectors.

Combining these two issues makes it possible to execute arbitrary JavaScript, by injecting an `onclick` HTML attribute into the `<link rel="canonical">` element and triggering it via the prettyPhoto JavaScript module by setting `hashRel` to `\'\,\*\,`. Due to the used jQuery version and it's lax parsing the following triggers the `click` event on all existing elements:

```js
$("a[rel^='\\\\'\\\\,\\\\*\\\\,']:eq(NaN)").trigger("click")
```

**Steps To Reproduce:**

Tested on latest Firefox and Edge:

1. `https://www.starbucks.co.uk/shop/card/egift/thank-you/anything%2522onclick=%2522confirm(document.domain)#!\'\,\*\,/1`

**Recommendation:**

Regarding the HTML attribute injection I suggested a fix in #252908. Regarding prettyPhoto, I don't believe it's actively maintained anymore so a customization will be necessary in my opinion. White-listing allowed characters in `hashRel` is the way to go with something like `\w+`.

## Impact

Attackers can execute arbitrary JavaScript in the victims' browsing context by tricking them into visiting an URL under the attackers' control. I believe you are aware of the dangers of XSS, but I am more then happy to show an actual exploit if needed.

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
