---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '419896'
original_report_id: '419896'
title: Unauthenticated user can upload an attachment to the last updated report draft
weakness: Improper Null Termination
team_handle: security
created_at: '2018-10-06T01:09:10.501Z'
disclosed_at: '2018-10-09T23:55:44.633Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 82
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-null-termination
---

# Unauthenticated user can upload an attachment to the last updated report draft

## Metadata

- HackerOne Report ID: 419896
- Weakness: Improper Null Termination
- Program: security
- Disclosed At: 2018-10-09T23:55:44.633Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The newly launched beta embedded submissions form introduced the concept of anonymous submissions. When an anonymous user starts writing a report through an embedded form, a UUID will be generated to track their submission. Any object that is created will reference this UUID. We call this a `tracer`. Because anonymous submissions also allow the person to upload attachments, we made a minor update to the controller. Here's a snippet of the controller:

```ruby
skip_before_action :authenticate_user!, only: :create

def create
  attachment = Interactors::Attachments::Upload.interact(
    file: params[:file],
    attachable: report_draft,
    as_user: current_user,
  )

  # ...
end

# ...

private

def report_draft
  return unless params[:tracer].present?
  ReportDraft.find_by(tracer: params[:tracer])
end
```

When a `POST` request is sent to the `/attachments` endpoint, the `create` method will be called. This method will call the `report_draft` method, which will try to load the report draft. In case a `tracer` value hasn't been given or the `tracer` value is not found, the method will return `nil`. Any report draft with a `tracer` value that is `nil` is created by an authenticated user, as we identify those based on their author, not the `tracer` value.

At first sight, this seems to be fine because of the `return unless params[:tracer].present?` check. If the parameter wouldn't be submitted, the value would be `nil`, and therefor the `present?` method would return false. However, when the user submits an array with one element that contains a null byte, the `present?` check will return true, and the ActiveRecord query will execute an `IS NULL` query. Here's a code example that shows this behavior:

```
[1] pry(main)> ["\x00"].present?
=> true
[2] pry(main)> ReportDraft.find_by(tracer: ["\x00"])
   ReportDraft Load (1.0ms)  SELECT  "report_drafts".* FROM "report_drafts" WHERE "report_drafts"."tracer" IS NULL LIMIT $1  [["LIMIT", 1]]
=> #<ReportDraft:0x00007fcd94ae6dc0>
```

Here's a normal request that is submitted to the attachments controller when an anonymous user uploads anything:

```
POST /attachments HTTP/1.1
Host: localhost:8080
...

------WebKitFormBoundarylWiasZL7nPVPOJ9M
Content-Disposition: form-data; name="tracer";

04b0e56b-da08-4d3e-8962-f2455cfdbd19
------WebKitFormBoundarylWiasZL7nPVPOJ9M
Content-Disposition: form-data; name="file"; filename="file.txt"
Content-Type: text/plain

file-contents
------WebKitFormBoundarylWiasZL7nPVPOJ9M--
```

In order to properly inject the array containing the null byte, the hex view in Burp Suite can be used. Here is the original request in the hex editor, in which case it has a proper UUID in the `tracer` parameter:

{F356266}

Here is the updated request, where the `tracer` parameter has been changed to an array and the value has been changed to a null byte:

{F356267}

## Impact

This means that if an array with a null byte to the `/attachments` endpoint is submitted, a random report draft will be loaded that was created by an authenticated user. The attachment will then be attached to that report draft. This allows an attacker to inject attachments in other users' report drafts, before it is submitted to the program.

The vulnerability requires user interaction to be exploited. When a user submits the report form, only the attachment IDs will be submitted that are cached in the DOM. This means that the injected attachment will only be submitted when the user refreshes the page **before** submitting the report. This means that they may actually detect the injected attachment, and they will have the ability to delete it.

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
