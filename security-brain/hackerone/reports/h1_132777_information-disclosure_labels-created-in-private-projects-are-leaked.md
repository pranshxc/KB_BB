---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '132777'
original_report_id: '132777'
title: Labels created in private projects are leaked
weakness: Information Disclosure
team_handle: gitlab
created_at: '2016-04-20T03:52:17.524Z'
disclosed_at: '2016-05-03T01:00:20.457Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- information-disclosure
---

# Labels created in private projects are leaked

## Metadata

- HackerOne Report ID: 132777
- Weakness: Information Disclosure
- Program: gitlab
- Disclosed At: 2016-05-03T01:00:20.457Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

# Vulnerability details
An insecure direct object reference vulnerability exists in the code that assigns labels to issues and merge requests, that allows an attack to read labels of private projects. This probably doesn't leak a lot of super confidential data, but since it's hard to predict how people use labels, it'd be good to fix this issue.

# Proof of concept
**Note**: this proof of concept demonstrates the attack with an issue, but the same issue exists when a merge request is created. To start off, sign in as a victim (`jane`) and create a project (`private-project`). Set the visibility level to private for this project. When this is set up, create a label at http://gitlab-instance/jane/private-project/labels. When I reproduced this issue for myself, I used `SomeCompany Secret feature` as label name. The label had ID `1`. Now sign in as the attacker (`john`). John wants access to the label that Jane created for her private program. John creates a new project called `random-project` and creates a new issue at http://gitlab-instance/john/random-project/issues. No need to select a label in the New issue form.

Now intercept the traffic before you click the "Submit issue" button. The request that is sent to the GitLab server looks something like this:

```
POST /john/random-project/issues HTTP/1.1
Host: 159.xxx.xxx.xxx
...

utf8=%E2%9C%93&authenticity_token=zD0fqQphsFSNP6gl6KWhTw5iaTtk3cGlDz1Gn563roNyiSq2ACIXGp8%2FmBMo9q70ZP3M0mCWmsq7XJCmzkdADg%3D%3D&issue%5Btitle%5D=a&issue%5Bdescription%5D=a&issue%5Bassignee_id%5D=&issue%5Bmilestone_id%5D=&issue%5Blabel_ids%5D%5B%5D=
```

Now add the label ID that you want access to as value to the `issue[label_ids][]` array. The request will now look something like this (note the appended `1`):

```
POST /john/random-project/issues HTTP/1.1
Host: 159.xxx.xxx.xxx
...

utf8=%E2%9C%93&authenticity_token=zD0fqQphsFSNP6gl6KWhTw5iaTtk3cGlDz1Gn563roNyiSq2ACIXGp8%2FmBMo9q70ZP3M0mCWmsq7XJCmzkdADg%3D%3D&issue%5Btitle%5D=a&issue%5Bdescription%5D=a&issue%5Bassignee_id%5D=&issue%5Bmilestone_id%5D=&issue%5Blabel_ids%5D%5B%5D=1
```

Forward the request and go back to the browser. You'll see that the label that belongs to the private project shows up as attached label:

{F88003}

# Impact
An attacker could easily iterate over all existing label IDs to attach all labels to an issue. This way potential confidential information (either in the name or description) is revealed to an attacker. Like said in the introduction, because you don't know how people use these labels, this can contain confidential information.

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
