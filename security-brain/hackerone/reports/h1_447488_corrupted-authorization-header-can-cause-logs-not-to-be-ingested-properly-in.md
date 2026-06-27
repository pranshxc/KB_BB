---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '447488'
original_report_id: '447488'
title: Corrupted Authorization header can cause logs not to be ingested properly in
  ████████
team_handle: security
created_at: '2018-11-20T04:48:27.549Z'
disclosed_at: '2019-04-04T19:50:22.462Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 17
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# Corrupted Authorization header can cause logs not to be ingested properly in ████████

## Metadata

- HackerOne Report ID: 447488
- Weakness: 
- Program: security
- Disclosed At: 2019-04-04T19:50:22.462Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

HackerOne ingests different logs in ██████, one of them being nginx access logs from our load balancers. The default log format of our load balancer configuration is shown below. As can be seen in the format, the HTTP user specified in the `Authorization` header (`$remote_user`) is placed between the `$remote_addr` and `[$time_local]`. A log entry is delimited with white space and the `$remote_user` variable isn't surrounded with quotes. When a user isn't specified, its value is set to `-`.

During a white box test of another component in a network, it was identified that an additional delimiter can be injected, which seems to cause ingestion of the log entry to fail and the log entry to be discarded.

**H1 nginx log format**
```
log_format cf_custom '$remote_addr - $remote_user [$time_local] '
                     '"$request" $status $body_bytes_sent '
                     '"$http_referer" "$http_user_agent" "$host" '
                     '$request_time $upstream_response_time $pipe '
                     '$http_cf_ray $cookie___cfduid '
                     '"$http_x_forwarded_proto" "$http_x_forwarded_for" '
                     '"$http_x_amzn_trace_id"';
```

Consider the following cURL command:

```
curl -X POST -u '- A:B' https://hackerone.com/graphql\?secret\=1
```

This will result in the following request being submitted:

**HTTP request**
```
POST /graphql?secret=1 HTTP/2
Host: hackerone.com
Authorization: Basic LSBBOkI=
User-Agent: curl/7.54.0
Accept: */*
```

When this request is processed by nginx, the `$remote_user` (`- A`) is being added to the log entry. However, since the delimiter (the whitespace) isn't escaped and no quotes are surrounding the value, an additional column is added to the log entry. When this is ingested by █████████, the log for that particular request doesn't seem to appear in the Events source. However, as the request itself is valid, it'll be proxied to the upstream.

Because our Rails logs have a different format (JSON), we do have the ability to still determine which requests were sent to our backend. There are very few requests who are stopped on our load balancer and none of them have the ability to interact directly with out database. This lowers the impact of the vulnerability. However, in order for us to rely on either access log that is being ingested, we should address this issue.

It is currently unknown where the root cause of this vulnerability lies. nginx, by default, uses a very similar log item format: http://nginx.org/en/docs/http/ngx_http_log_module.html. Similar to the HackerOne configuration, the `$remote_user` is not enclosed in double quotes. The fact that nginx doesn't encode the whitespace may actually be something they want to fix going forward. However, it seems rather odd that █████████ completely discards a log entry. Let's figure out where the vulnerability comes from and what we can do to fix it.

The `$cookie___cfduid` parameter may also be vulnerable to the same attack.

## Impact

This may impact our ability to give a conclusive answer during incident response or debugging based on the nginx load balancer access logs.

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
