---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1536013'
original_report_id: '1536013'
title: Possibility to guess email address from gravatar image URL
weakness: Inadequate Encryption Strength
team_handle: rubygems
created_at: '2022-04-09T08:46:42.657Z'
disclosed_at: '2023-09-14T20:20:00.510Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
asset_identifier: rubygems.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- inadequate-encryption-strength
---

# Possibility to guess email address from gravatar image URL

## Metadata

- HackerOne Report ID: 1536013
- Weakness: Inadequate Encryption Strength
- Program: rubygems
- Disclosed At: 2023-09-14T20:20:00.510Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The hash used for gravatar used in rubygems.org is a simple md5, which could allow an attacker to guess the user's email address. 

https://en.gravatar.com/site/implement/hash/

https://github.com/chrislloyd/gravtastic/blob/master/lib/gravtastic.rb#L79

```ruby
    def gravatar_id
      Digest::MD5.hexdigest(send(self.class.gravatar_source).to_s.downcase)
    end
```

In rubygems.org, there is a setting that can make the email address private, but since the url of gravatar is public, the email address can be guessed unintentionally.

### PoC

1. Start server in local
2. Create user as `test@example.com`
3. Confirm email address is private
    {F1685876}
4. Open the profile of the user created in the secret window and get the url of gravatar
    ```html
    <div id="avatar-frame">
       <img id="profile_gravatar" width="300" height="300" class="profile__header__avatar" src="http://gravatar.com/avatar/55502f40dc8b7c769880b10874abc9d0.png?d=retro&r=PG&s=300" />
    </div>
    ```
5. Confirm that the generated hash matches the hash in the url.
    ```ruby
    require 'digest/md5'

    mail = 'test@example.com'
    puts Digest::MD5.hexdigest(mail)
    ```
    ```
     ❯ ruby test.rb
     55502f40dc8b7c769880b10874abc9d0
    ```

## Impact

The email address of a user who has set the email address as private may be obtained.

There was a similar discussion about wordpress.
https://www.wordfence.com/blog/2016/12/gravatar-advisory-protect-email-address-identity/

Many users seem to be affected because email addresses are now private by default.
https://github.com/rubygems/rubygems.org/pull/2663/files
Avoiding gravatar has too much of an impact, so I suggest that give the user the option to use gravatar (use gravatar by default).

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
