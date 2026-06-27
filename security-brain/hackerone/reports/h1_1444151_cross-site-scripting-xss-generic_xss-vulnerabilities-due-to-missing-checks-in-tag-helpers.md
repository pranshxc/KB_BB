---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1444151'
original_report_id: '1444151'
title: XSS vulnerabilities due to missing checks in tag helpers
weakness: Cross-site Scripting (XSS) - Generic
team_handle: rails
created_at: '2022-01-08T18:53:39.226Z'
disclosed_at: '2023-07-28T00:45:26.113Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 41
asset_identifier: https://github.com/rails/rails
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS vulnerabilities due to missing checks in tag helpers

## Metadata

- HackerOne Report ID: 1444151
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: rails
- Disclosed At: 2023-07-28T00:45:26.113Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Rails offers some protections against XSS in its helpers for the views. Several tag helpers in ActionView::Helpers::FormTagHelper and ActionView::Helpers::TagHelper are vulnerable against XSS because their current protection does not restrict properly the set of characters allowed in the names of tag attributes and in the names of tags.

I am providing a proposal of changes to fix the problems following the official Rails guide for contributing, including tests, changelogs, etc. It is just a proposal and I am willing to improve it with your feedback and backport it to the supported versions. Let me know if you would like me to add you to a private repository where I can create a pull request and we can discuss the changes comfortably.

The first group of vulnerabilities is related to the `options` argument in methods from `FormTagHelper` like `check_box_tag, label_tag, radio_button_tag, select_tag, submit_tag, text_area_tag, text_field_tag, etc.` In particular in these 3 cases:
- When providing prefixed HTML "data-*" attributes.
- When providing prefixed HTML "aria-*" attributes.
- When providing a hash of other types of non-boolean attributes.

For example:

`check_box_tag('thename', 'thevalue', false, data: { malicious_input => 'thevalueofdata' })`

In that method call, when the variable `malicious_input` is controlled in part or completely by a user of the application, an attacker can provide an input that will break free from the tag and execute arbitrary JavaScript code. For some applications, that code can be executed in the browser of a different user visiting the application. A simplified proof of concept with only reflected XSS would be this HTML ERB view file:

`<%= check_box_tag('thename', 'thevalue', false, data: { params[:payload] => 'thevalueofdata' }) %>`

Followed by a request that included the malicious URL parameter: `http://...?payload=something="something"><img src="/nonexistent" onerror="alert(1)"><div class`

That example only shows an alert window, but it is possible to steal passwords or other private information from the user, substitute parts of the website with fake content, attack other websites visited by the user, perform scans of the network of the user, etc. And some applications are probably using more dangerous stored user input instead of URL parameters, allowing attackers to perform stored XSS attacks on other users.

Here is another example with `aria-*` HTML attributes were the same simple payload can be tested:
`check_box_tag('thename', 'thevalue', false, aria: { malicious_input => 'thevalueofaria' })`

And finally, another example with other non-boolean attributes:
`check_box_tag('thename', 'thevalue', false, malicious_input => 'theothervalue')`

This same vulnerable structure can also be attacked successfully in the other methods listed at the beginning: `label_tag, radio_button_tag, select_tag, submit_tag, text_area_tag, text_field_tag...`

The second group of vulnerabilities is related to the more generig methods `tag` and `content_tag` from `TagHelper`. They are vulnerable in the `options` argument like the previous group of methods, but they are also vulnerable in their first argument, for the names of the generated tags, using the same kind of attack to break free from the tag and execute arbitrary Javascript code. For example:

- `tag(malicious_input)`
- `tag.public_send(malicious_input.to_sym)`
- `content_tag(malicious_input)`

In the 3 cases, this is an example of a simple payload that works:
`img%20src=%22/nonexistent%22%20onerror=%22javascript_payload%22`

As said before for other examples, that only shows an alert window, but it is possible to use the same attack to potentially steal passwords or other private information from the user, substitute parts of the website with fake content, perform scans of the network of the user, etc.

## Impact

As mentioned in the description, the Rails applications that use those helpers with some kind of user-supplied input are vulnerable to XSS attacks. Currently, there are some protections againts XSS in the affected methods, but it is not enough.

In the description I have provided simple payloads as an example that only created an alert window. However, it is possible to use the same attack to potentially steal passwords or other private information from the user, substitute parts of the website with fake content, perform scans of the network of the user, etc. In some applications it is probably possible to perform more dangerous stored XSS attacks. So fixing this problem is recommended and consistent with the Rails security policy ( https://rubyonrails.org/security ).

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
