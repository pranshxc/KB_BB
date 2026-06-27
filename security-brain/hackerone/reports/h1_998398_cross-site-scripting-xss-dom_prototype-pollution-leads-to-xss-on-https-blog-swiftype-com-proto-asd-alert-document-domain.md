---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '998398'
original_report_id: '998398'
title: Prototype Pollution leads to XSS on https://blog.swiftype.com/#__proto__[asd]=alert(document.domain)
weakness: Cross-site Scripting (XSS) - DOM
team_handle: elastic
created_at: '2020-10-05T13:36:28.671Z'
disclosed_at: '2021-08-16T18:54:38.948Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 144
asset_identifier: '*.swiftype.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# Prototype Pollution leads to XSS on https://blog.swiftype.com/#__proto__[asd]=alert(document.domain)

## Metadata

- HackerOne Report ID: 998398
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: elastic
- Disclosed At: 2021-08-16T18:54:38.948Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 
deparam function which parses location.hash in https://s.swiftypecdn.com/install/v2/st.js  is vulnerable to prototype pollution.
There is a script gadget in the same js file which leads to XSS.


## Steps To Reproduce:
Visit (Refresh if you don't see a pop up)
https://blog.swiftype.com/#__proto__[asd]=alert(document.domain)

## Root Cause
https://s.swiftypecdn.com/install/v2/st.js is the vulnerable file.
deparam function parses the ` location.hash` incorrectly which leads to Prototype Pollution.

```

 t.deparam = h = function(e, n) {
            var i = {}
              , r = {
                "true": !0,
                "false": !1,
                "null": null
            };
            return t.each(e.replace(/\+/g, " ").split("&"), function(e, o) {
                var s, a = o.split("="), u = b(a[0]), c = i, h = 0, p = u.split("]["), f = p.length - 1;
                if (/\[/.test(p[0]) && /\]$/.test(p[f]) ? (p[f] = p[f].replace(/\]$/, ""),
                p = p.shift().split("[").concat(p),
                f = p.length - 1) : f = 0,
                2 === a.length)
                    if (s = b(a[1]),
                    n && (s = s && !isNaN(s) ? +s : "undefined" === s ? l : r[s] !== l ? r[s] : s),
                    f)
                        for (; h <= f; h++)
                            u = "" === p[h] ? c.length : p[h],
                            c = c[u] = h < f ? c[u] || (p[h + 1] && isNaN(p[h + 1]) ? {} : []) : s; //pollution here
                    else
                        t.isArray(i[u]) ? i[u].push(s) : i[u] !== l ? i[u] = [i[u], s] : i[u] = s;
                else
                    u && (i[u] = n ? l : "")
            }),
            i
        }

```

Gadget found in the same js, which is very interesting gadget I found so far :xD

```

    
        pInstall._convertStringHooksToFunctions = function() {
            var functionHooks = {};
            $.each(this._userServerConfiguration.install.hooks, function(hookName, hookFunction) {
                functionHooks[hookName] = eval(hookFunction) //eval everything in the object
            }),
            this._userServerConfiguration.install.hooks = functionHooks
        }
        

```

## Impact: 
XSS

## Impact

XSS

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
