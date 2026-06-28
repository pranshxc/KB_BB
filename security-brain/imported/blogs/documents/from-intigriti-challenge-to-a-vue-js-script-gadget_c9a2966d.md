---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-22_from-intigriti-challenge-to-a-vuejs-script-gadget.md
original_filename: 2021-11-22_from-intigriti-challenge-to-a-vuejs-script-gadget.md
title: From Intigriti challenge to a Vue.js script gadget
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: c9a2966d22a80c67b75da3d01cb39d4c9491efa6657e7194ea271193ad89de79
text_sha256: 1f40e48bb67045f28ffac56af95634ecc2b9307f8763b20a36b574bdcf4ce761
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# From Intigriti challenge to a Vue.js script gadget

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-22_from-intigriti-challenge-to-a-vuejs-script-gadget.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `c9a2966d22a80c67b75da3d01cb39d4c9491efa6657e7194ea271193ad89de79`
- Text SHA256: `1f40e48bb67045f28ffac56af95634ecc2b9307f8763b20a36b574bdcf4ce761`


## Content

---
title: "From Intigriti challenge to a Vue.js script gadget"
page_title: "From Intigriti challenge to a Vue.js script gadget - '><img/src='/%ff/'/onerror=alert(/blog.xss.am/)>'<"
url: "https://blog.xss.am/2021/11/vuejs-script-gadget-intigriti/"
final_url: "https://blog.xss.am/2021/11/vuejs-script-gadget-intigriti/"
authors: ["Davit (@davwwwx)"]
bugs: ["XSS", "CSP bypass"]
publication_date: "2021-11-22"
added_date: "2024-07-08"
source: "pentester.land/writeups.json"
original_index: 3149
---

# From Intigriti challenge to a Vue.js script gadget

[__Davwwwx](/about "Author") included in [__Challenges](/categories/challenges/)

__ 22-11-2021  __334 words __2 minutes

![/2021/11/vuejs-script-gadget-intigriti/featured-image.png](/svg/loading.min.svg)

Intigiriti’s November [challenge](https://challenge-1121.intigriti.io/) by [IvarsVids](https://twitter.com/IvarsVids) was about a [Vue.js](https://vuejs.org/) one-pager that reflected user input with some replacements. After visiting the challenge homepage at <https://challenge-1121.intigriti.io/> we quickly notice it reflects `s` query parameter not escaping HTML less than and greater than signs resulting in [HTML injection](https://challenge-1121.intigriti.io/challenge/index.php?s=reflectme%3C/title%3E%3Cscript%3Ealert%28%29%3C/script%3E).

[ ![/2021/11/vuejs-script-gadget-intigriti/reflection.png](/svg/loading.min.svg) ](/2021/11/vuejs-script-gadget-intigriti/reflection.png "s parameter reflection")s parameter reflection

But the page refuses the execute the injected script because of the content security policy `base-uri 'self'; default-src 'self'; script-src 'unsafe-eval' '<emitted>' 'strict-dynamic'; object-src 'none'; style-src '<emitted>'` [ ![/2021/11/vuejs-script-gadget-intigriti/blocked.png](/svg/loading.min.svg) ](/2021/11/vuejs-script-gadget-intigriti/blocked.png "CSP blocking")CSP blocking

As we see `unsafe-eval` directive is present, which means dynamically eval’ed script will be allowed, so we can try vue.js template injection. To achieve that we should inject our element with `app` “id”, close the `<title>` with a payload like `</title><div id=app></div>` and inject the payload within the div. Template delimiters are set to `v-{{` and `}}` on line 45 but after trying to inject templates or general script gadgets from [Portswigger’s cheatsheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet#vuejs-reflected) the WAF is replacing keywords with `%` characters. [ ![/2021/11/vuejs-script-gadget-intigriti/replaced.png](/svg/loading.min.svg) ](/2021/11/vuejs-script-gadget-intigriti/replaced.png "replacing keywords")replacing keywords

Looking for a potential execuntion sink I refered to Vue api at <https://vuejs.org/v2/api/> and found [slot-scope](https://vuejs.org/v2/api/#slot-scope-deprecated) deprecated special attribute which is expecting `function argument expression`. Trying to inject payload like `</title><div id=app><p slot-scope="function(){alert()}"></div>` we get the following expection. [ ![/2021/11/vuejs-script-gadget-intigriti/exception.png](/svg/loading.min.svg) ](/2021/11/vuejs-script-gadget-intigriti/exception.png "thrown exception")thrown exception

So to execute javascript we should close the function expression and then execute our javascript code, but also please note the injection point is within a smaller scope and `window` parameters are not within this scope. To escape to `window` scope we can try the classic `this.constructor.constructor` chain. Injecting a payload like the following we get another exception`</title><div id="app"><p slot-scope="){}}])-this.constructor.constructor('alert(origin)')()})};//"></div>` [ ![/2021/11/vuejs-script-gadget-intigriti/exception2.png](/svg/loading.min.svg) ](/2021/11/vuejs-script-gadget-intigriti/exception2.png "thrown exception 2")thrown exception 2

WAF has replaced `is` from `this` with `%is%` as it is another known script gadget attribute, but we can bypass this using a function from the local scope, e.g. `</title><div id="app"><p slot-scope="){}}])-_c.constructor.constructor('alert(origin)')()})};//"></div>` [ ![/2021/11/vuejs-script-gadget-intigriti/success.png](/svg/loading.min.svg) ](/2021/11/vuejs-script-gadget-intigriti/success.png "successfull execution")successfull execution

For the intended solution check Intigriti’s guide at <https://www.youtube.com/watch?v=-_7uL7l0qZk>.

Updated on 22-11-2021

[Read Markdown](/2021/11/vuejs-script-gadget-intigriti/index.md)

[__](javascript:void\(0\); "Share on Twitter")[__](javascript:void\(0\); "Share on Facebook")[__](javascript:void\(0\); "Share on Hacker News")[__](javascript:void\(0\); "Share on Reddit")

__[web security](/tags/web-security/), [script gadget](/tags/script-gadget/), [xss](/tags/xss/), [intigriti](/tags/intigriti/), [vuejs](/tags/vuejs/) [Back](javascript:void\(0\);) | [Home](/)

[__Intigriti's February XSS Challenge Writeup](/2021/02/intigriti-february-xss-challenge/ "Intigriti's February XSS Challenge Writeup") [OrangeSite - "1 CAT COMPANY CTF" spring xxe challenge __](/2021/11/cyhub-off-by-slash-xxe/ "OrangeSite - "1 CAT COMPANY CTF" spring xxe challenge")
