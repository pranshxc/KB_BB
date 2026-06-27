---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '469668'
original_report_id: '469668'
title: Passwords being stored as plain text in logging
weakness: Cleartext Storage of Sensitive Information
team_handle: nextcloud
created_at: '2018-12-18T16:44:58.604Z'
disclosed_at: '2019-08-31T12:45:35.999Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 30
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# Passwords being stored as plain text in logging

## Metadata

- HackerOne Report ID: 469668
- Weakness: Cleartext Storage of Sensitive Information
- Program: nextcloud
- Disclosed At: 2019-08-31T12:45:35.999Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

When an exception occurs, any password sent to or being processed by the server may be stored as plain text in the log.

I noticed that some methods are already being filtered in `ExceptionSerializer.php`, but many methods are missing from this list.

Suggestion: instead of relying on a list of sensitive methods, filter every method with a `$password` parameter.

----

Steps to reproduce (example):

1. Install NextCloud without SMTP server
1. Create a new user at `https://nextcloud/settings/users`
1. Check the logging at `https://nextcloud/settings/admin/logging`

Results in 2 exceptions:

```
[ocs_api] Error: OCP\AppFramework\OCS\OCSException: Unable to send the invitation mail at <<closure>>

0. /var/www/html/lib/private/AppFramework/Http/Dispatcher.php line 166
                                      vvvvvvvv
   addUser("[redacted]", "[redacted - PASSWORD]", "[redacted]", "[redacted]", [], [], "10 GB", "en")
                                      ^^^^^^^^
1. /var/www/html/lib/private/AppFramework/Http/Dispatcher.php line 99
   executeController(OCA\Provisioning ... {}, "addUser")
2. /var/www/html/lib/private/AppFramework/App.php line 118
   dispatch(OCA\Provisioning ... {}, "addUser")
3. /var/www/html/lib/private/AppFramework/Routing/RouteActionHandler.php line 47
   main("OCA\\Provisioni ... r", "addUser", OC\AppFramework\ ... {}, {_route: "ocs.pr ... "})
4. <<closure>>
   __invoke({_route: "ocs.pr ... "})
5. /var/www/html/lib/private/Route/Router.php line 297
   call_user_func(OC\AppFramework\ ... {}, {_route: "ocs.pr ... "})
6. /var/www/html/ocs/v1.php line 82
   match("/ocsapp/cloud/users")
7. /var/www/html/ocs/v2.php line 24
   require_once("/var/www/html/ocs/v1.php")

POST /ocs/v2.php/cloud/users
from 172.18.0.4 by [redacted] at 2018-12-17T19:38:41+00:00
```

```
[ocs_api] Error: Swift_TransportException: Connection could not be established with host 127.0.0.1 [Connection refused #111] at <<closure>>

 0. /var/www/html/3rdparty/swiftmailer/swiftmailer/lib/classes/Swift/Transport/StreamBuffer.php line 58
    establishSocketConnection()
 1. /var/www/html/3rdparty/swiftmailer/swiftmailer/lib/classes/Swift/Transport/AbstractSmtpTransport.php line 143
    initialize({protocol: "",ho ... ]})
 2. /var/www/html/3rdparty/swiftmailer/swiftmailer/lib/classes/Swift/Mailer.php line 65
    start()
 3. /var/www/html/lib/private/Mail/Mailer.php line 180
    send(Swift_Message {}, [])
 4. /var/www/html/settings/Mailer/NewUserMailHelper.php line 169
    send(OC\Mail\Message {})
 5. /var/www/html/apps/provisioning_api/lib/Controller/UsersController.php line 307
    sendMail(OC\User\User {}, OC\Mail\EMailTemplate {})
 6. /var/www/html/lib/private/AppFramework/Http/Dispatcher.php line 166
                                       vvvvvvvv
    addUser("[redacted]", "[redacted - PASSWORD]", "[redacted]", "[redacted]", [], [], "10 GB", "en")
                                       ^^^^^^^^
 7. /var/www/html/lib/private/AppFramework/Http/Dispatcher.php line 99
    executeController(OCA\Provisioning ... {}, "addUser")
 8. /var/www/html/lib/private/AppFramework/App.php line 118
    dispatch(OCA\Provisioning ... {}, "addUser")
 9. /var/www/html/lib/private/AppFramework/Routing/RouteActionHandler.php line 47
    main("OCA\\Provisioni ... r", "addUser", OC\AppFramework\ ... {}, {_route: "ocs.pr ... "})
10. <<closure>>
    __invoke({_route: "ocs.pr ... "})
11. /var/www/html/lib/private/Route/Router.php line 297
    call_user_func(OC\AppFramework\ ... {}, {_route: "ocs.pr ... "})
12. /var/www/html/ocs/v1.php line 82
    match("/ocsapp/cloud/users")
13. /var/www/html/ocs/v2.php line 24
    require_once("/var/www/html/ocs/v1.php")

POST /ocs/v2.php/cloud/users
from 172.18.0.4 by [redacted] at 2018-12-17T19:38:41+00:00
```

## Impact

Get various user names, e-mail addresses and passwords from log files.

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
