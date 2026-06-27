---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '462503'
original_report_id: '462503'
title: Claiming package names in GitLab's automatic package referencer.
weakness: Business Logic Errors
team_handle: gitlab
created_at: '2018-12-14T17:54:10.835Z'
disclosed_at: '2019-04-05T17:30:51.575Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# Claiming package names in GitLab's automatic package referencer.

## Metadata

- HackerOne Report ID: 462503
- Weakness: Business Logic Errors
- Program: gitlab
- Disclosed At: 2019-04-05T17:30:51.575Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi team,

GitLab has a pretty neat feature that auto-links packages to their respective registry. The problem is that GitLab currently assumes that packages have been uploaded to a registry by default. For example, if no `homepage` key is pointing to GitLab in a `package.json` file, Gitlab assumes that the package has been uploaded to the npm registry. This not always the case, in fact, I have come across many packages that were defined for local use only and never published — this can be seen on multiple popular projects belonging to Facebook. To demonstrate my point I picked one of your projects and claimed the package on npm, so now if users navigate to https://gitlab.com/gitlab-org/gitter/desktop/blob/master/package.json and click on `gitter-desktop`, they will be redirected to my "malicious" npm module where there are clear instructions on how to install the package.

{F390411}

```html
<div class="blob-viewer" data-type="auxiliary">
   <i aria-hidden="true" data-hidden="true" class="fa fa-cubes fa-fw"></i>
   This project manages its dependencies using
   <strong>npm</strong>
   and defines a package named
   <strong><a target="_blank" rel="noopener noreferrer" href="https://www.npmjs.com/package/gitter-desktop">gitter-desktop</a></strong>.
   <a target="_blank" rel="noopener noreferrer" href="https://www.npmjs.com/">Learn more</a>
</div>
```

npm modules are particularly dangerous since by design, npm executes certain scripts from dependencies during the installation process as demonstrated in https://hackerone.com/reports/399166 and https://vince-uploaded.s3.amazonaws.com/static/vulcoord/files/319816_attach_npmwormdisclosure.pdf.

I would also like to add, it is really easy to automate this hijacking process and I would be more than happy to demonstrate an exploit on my own personal GitLab instance where I can claim lots of these package links in various test projects, if you are interested.

## Impact

An adversary can trick an unsuspecting user into installing and executing a malicious package from the npm registry. What makes this attack possible is the fact that the package appears to belong to a trusted entity due to GitLab linking to the malicious packet from the project's page.

\- Ed

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
