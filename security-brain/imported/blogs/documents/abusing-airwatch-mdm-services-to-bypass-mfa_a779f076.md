---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-11_abusing-airwatch-mdm-services-to-bypass-mfa.md
original_filename: 2020-12-11_abusing-airwatch-mdm-services-to-bypass-mfa.md
title: Abusing AirWatch MDM Services to Bypass MFA
category: documents
detected_topics:
- mfa
- sso
- rate-limit
- api-security
- mobile-security
- supply-chain
tags:
- imported
- documents
- mfa
- sso
- rate-limit
- api-security
- mobile-security
- supply-chain
language: en
raw_sha256: a779f076814ccae392c42b7093522ed160cbd1d9615fc2f8d645a82ccc208f78
text_sha256: 875892d3a3c779ff1ede9c2b57f80dc0ea5ccae7b3a4c344151f1ea343abfbc1
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: true
---

# Abusing AirWatch MDM Services to Bypass MFA

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-11_abusing-airwatch-mdm-services-to-bypass-mfa.md
- Source Type: markdown
- Detected Topics: mfa, sso, rate-limit, api-security, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: True
- Raw SHA256: `a779f076814ccae392c42b7093522ed160cbd1d9615fc2f8d645a82ccc208f78`
- Text SHA256: `875892d3a3c779ff1ede9c2b57f80dc0ea5ccae7b3a4c344151f1ea343abfbc1`


## Content

---
title: "Abusing AirWatch MDM Services to Bypass MFA"
page_title: "Abusing AirWatch MDM Services to Bypass MFA | Into the Abyss"
url: "https://emptynebuli.github.io/tooling/2020/12/11/aircross.html"
final_url: "https://emptynebuli.github.io/tooling/2020/12/11/aircross.html"
authors: ["Matt Burch (@emptynebuli)"]
programs: ["VMware (AirWatch)"]
bugs: ["Android", "2FA / MFA bypass", "Username enumeration"]
publication_date: "2020-12-11"
added_date: "2024-05-11"
source: "pentester.land/writeups.json"
original_index: 4071
---

# Abusing AirWatch MDM Services to Bypass MFA

Dec 11, 2020 ~ Apr 18, 2024 

In December, 2020, I originally released this content through [Optiv SourceZero](https://www.optiv.com/insights/source-zero/blog/abusing-airwatch-mdm-services-bypass-mfa). To ensure future control over this content and provide central storage, I have copied here.

Many organizations use multi-factor authentication (MFA) to mitigate the impact of credential compromise, especially when Internet-exposed authentication is required. This has been a positive industry trend, as credential access to an organization has limited success in these security architectures. However, the increased complexity of implementing MFA, combined with convenience demands of large user bases can lead to unforeseen access paths through MFA solutions. Security research of VMWare’s AirWatch Mobile Device Management (MDM) product suite has identified MFA is only implemented during the registration process. Furthermore, prior to and/or in parallel of this registration single-factor authentication (SFA) attacks can be carried out against the solution, allowing for the compromise of user credentials and/or the registration of malicious devices. The focus of this article is to examine the SFA attack surface exposed throughout the AirWatch MDM product suite.

AirWatch, like many MDM solutions, provides organizations containerized access management across untrusted or unmanaged devices, providing a secure mechanism to connect to internal corporate resources. This is facilitated by deploying a localized or cloud-based appliance, which communicates back to a global infrastructure maintained by AirWatch through the domain awmdm.com. Mobile users would then establish communications to this environment through the installation of a mobile package. These are commonly known as Android Packages (APK) or iOS Application Archives (IPA), which are publicly accessible through the Android and Apple marketplaces.

Once installed, the AirWatch application will request one of two things from the user: an email address or a server endpoint.

[![Figure 1: AirWatch MDM Login Portal](/assets/images/airwatch_bypass_mfa_img1.png)](/assets/images/airwatch_bypass_mfa_img1.png "Figure 1: AirWatch MDM Login Portal") **Figure 1: AirWatch MDM Login Portal**

Submitting an email address will initiate an API request to the URI of _discovery.awmdm.com_ :
  
  
  GET /autodiscovery/DeviceRegistry.aws/v2/domainlookup/domain/vmware.com HTTP/1.1
  User-Agent: Agent/20.08.0.23/Android/11
  Accept-Language: en-US
  deviceType: 5
  Authorization: 53edf056709f7e16a1c3fb6ac56aea51:W8Xo4AEfsUJuzVVtqArEZmRPDpkXiYSE26OUE0HJpZs=
  aw-auth-signature-method: HMAC-SHA256
  aw-auth-group-id: com.airwatch.androidagent
  aw-auth-signature-version: 1
  aw-auth-realm: device
  aw-device-uid: 53edf056*******
  aw-auth-device-uid: 53edf056*******
  Date: 10/20/2020 13:11:45
  Host: discovery.awmdm.com
  Connection: close
  Accept-Encoding: gzip, deflate
  

**Figure 2: AirWatch MDM Client Discovery Request**

This request is triggered against the following RESTful API:

  * /autodiscovery/DeviceRegistry.aws/v2/domainlookup/domain/

The _domain_ variable is leveraged to perform search functionality with AirWatch’s discovery service and return the AirWatch authentication endpoint and activation GroupID associated with the requested _domain_. The GroupID, or ActivationCode, is a required value when attempting to authenticate against the AirWatch solution. However, this information is considered public knowledge and is not protected or sensitive information. VMWare security’s response to the sensitivity of these values was as follows:

**_GroupIDs (ActivationCode) are used for the following and we do not consider them sensitive information:_**

**_“Group ID - public customer/org identifier used to associate a public device enrollment with the customer. Typically used to map email domain to a product specific identifier.”_**

The request that is generated from the MDM application contains an authorization header and some additional validation checks. However, none of this information is server-side validated and the request header can be condensed to the following:
  
  
  GET /autodiscovery/awcredentials.aws/v2/domainlookup/domain/vmware.com HTTP/1.1
  Host: discovery.awmdm.com
  User-Agent: Agent/20.08.0.23/Android/11
  Accept-Encoding: gzip, deflate
  Connection: close
  

**Figure 3: AirWatch MDM Discovery Request - Condensed**

Discovery services have been observed through three different endpoints. Two are publicly documented APIs and the third is server-side content derived from the discovery process.

  * /autodiscovery/awcredentials.aws/v1/domainlookup/domain/
  * /autodiscovery/awcredentials.aws/v2/domainlookup/domain/
  * /DeviceManagement/Enrollment/validate-userCredentials

Requests generated against the v1/v2 API return a JSON response body detailing the domain’s authentication endpoint and GroupID values.

[![Figure 4: AirWatch MDM Discovery Response](/assets/images/airwatch_bypass_mfa_img2.png)](/assets/images/airwatch_bypass_mfa_img2.png "Figure 4: AirWatch MDM Discovery Response") **Figure 4: AirWatch MDM Discovery Response**

Unlike these two API requests, the third discovery interface requires knowledge of the authentication endpoint URL and returns the appropriate GroupID value. Additionally, communication with _validate-userCredentials_ requires submission of a SessionID (SID). However, this value is easily recoverable by following the standard MDM registration process. Submitting a POST request to _/DeviceManagement/Enrollment/EmailDiscovery_ returns a validation SID that can be used in the _validate-userCredentials_ request.
  
  
  POST /DeviceManagement/Enrollment/EmailDiscovery HTTP/1.1
  Host: vmware.awmdm.com
  User-Agent: Agent/20.08.0.23/Android/11
  Content-Length: 93
  Accept: gzip, deflate
  Content-Type: application/x-www-form-urlencoded
  Accept-Encoding: gzip, deflate
  Connection: close
  
  DevicePlatformId=2&EmailAddress=test@vmware.com&FromGroupID=False&FromWelcome=False&Next=Next
  

**Figure 5: VMWare EmailDiscovery API**

Two critical values need to be submitted in this POST for proper registration of the request:

  * **DevicePlatformId:** This is an ID value of the device type. In examining the standard MDM package functionality, my research observed this field to be populated with a value of 2.
  * **EmailAddress:** This is leveraged to trigger the discovery functionality. An email address must be submitted for the API to attempt registration and recover the GroupID value.

The remaining values were just defaulted to False to allow processing of the request. Upon submission, the API will respond with a 302 redirecting clients to their device’s app store for installation of the AirWatch Intelligence HUB application. However, this response also contains the authorization SID to continue communication with the API once the package is installed.
  
  
  <html><head><title>Object moved</title></head><body>
  <h2>Object moved to <a
  href="/DeviceManagement/Enrollment/DisplayAgentAppStoreLink?groupid=False&welcome=
  False&sid=1e69ee15-4749-44fe-8d91-a67bf7fd971e">here</a>.</h2>
  </body></html>
  

**Figure 6: EmailDiscovery Server Response Body**

This SID value (`sid=1e69ee15-4749-44fe-8d91-a67bf7fd971e`) can then be passed as part of the parametrized request to _validate-userCredentials_.
  
  
  GET /DeviceManagement/Enrollment/validate-userCredentials?groupid=True&welcome=False&id=1e69ee15-4749-44fe-8d91-a67bf7fd971e HTTP/1.1
  Host: vmware.awmdm.com
  User-Agent: Agent/20.08.0.23/Android/11
  Content-Length: 0
  Accept: gzip, deflate
  Content-Type: application/x-www-form-urlencoded
  Accept-Encoding: gzip, deflate
  Connection: close
  

**Figure 7: AirWatch validate-userCredentials API Request**

This request generates an HTML-formatted server response. Hidden within the content body are localized JavaScript code blocks. A substring query against this content returns the GroupID, within the second occurrence of _else if_ statements.

[![Figure 8: AirWatch GroupID Disclosure](/assets/images/airwatch_bypass_mfa_img3.png)](/assets/images/airwatch_bypass_mfa_img3.png "Figure 8: AirWatch GroupID Disclosure") **Figure 8: AirWatch GroupID Disclosure**

Again, VMware does not consider this information to be sensitive. So, it does not represent a vulnerability on its own. However, to perform any further attacks against the environment, this information is critical. All AirWatch authentication interfaces require the submission of a GroupID value; without this information it would not be possible to carry out an authentication attack against the environment.

Upon recovering the endpoint and GroupID values, AirWatch discloses the configuration settings of the MDM environment. This further allows an unauthenticated attacker to identify sub-groups, authentication integrations and numerous additional configuration settings of the environment. This is all made possible through the following API endpoint:

  * /deviceservices/enrollment/airwatchenroll.aws/validategroupidentifier

  
  
  POST /deviceservices/enrollment/airwatchenroll.aws/validategroupidentifier HTTP/1.1
  Host: vmware.awmdm.com
  User-Agent: Agent/20.08.0.23/Android/11
  Content-Length: 118
  Content-Type: application/json
  Accept-Encoding: gzip, deflate
  Connection: close
  
  {"Header":{"SessionId":"00000000-0000-0000-0000-
  000000000000"},"Device":{"InternalIdentifier":""},"GroupId":"VMWprod"}
  

**Figure 9: AirWatch validategroupidentifier API Request**

Similar to the v1/v2 API discovery endpoints, _validategroupidentifier_ does not require authorization. Communication with this endpoint requires the submission of a JSON formatted message body and is directed towards an organization’s authentication endpoint. Within this message body, there are a few variables of note:

  * **SessionId:** Communication with several of the JSON processing AirWatch APIs requires an SID. This value is represented as an RFC 4122 v4 value. Zeroing out this value initializes the query and resets the communication with the endpoint. Valid communication with the endpoint will provide a randomized _SessionId_ in response.
  * **GroupId:** This is the GroupID value that has been identified or discovered through the previously documented process.

Successful submission of this request, returns the following response:
  
  
  {
  "Header": {
  "ProtocolRevision": 0,
  "Language": null,
  "SessionId": "6debe689-709d-4f6a-b038-fe5f61fde336",
  "Mode": 2,
  "AgentToken": "978969b0-d2cf-4dd6-8e3c-eef546010b34",
  "ProtocolType": 0,
  "App": 0,
  "AppVersion": null
  },
  "Status": {
  "Code": 1,
  "Notification": ""
  },
  "NextStep": {
  "InstallUrl": "",
  "ServiceUrl": "https://vmware.awmdm.com/DeviceManagement/Enrollment/begin-
  samlAuthentication?sid=6debe689-709d-4f6a-b038-fe5f61fde336",
  "DeviceUserMode": 0,
  "StagingRequired": false,
  "DisplayStagingMessage": null,
  "UserIdentifier": null,
  "AfwProvisioningMode": 0,
  "RegistrationTypePo": 0,
  "RegistrationTypeDo": 0,
  "VidmForCico": false,
  "IsLbusEnabled": false,
  "ClosedNetworkEnrollment": false,
  "Type": 18,
  "SettingsPayload": "",
  "AgentSettings": null,
  "RequireServicesFromStore": false,
  "IsCaptchaRequired": false,
  "CaptchaValue": null,
  "AndroidEnrollmentTarget": 0,
  "KnoxPlayForWorkCapable": false,
  "AndroidWorkTempPassword": null,
  "UserEmailAddress": null,
  "showEnrollmentInfoMessages": false,
  "AFWUserAuthToken": null,
  "AFWAccountIdentifer": null,
  "IsDeviceAfwCertified": false,
  "GreenBoxUrl": null,
  "VidmServerUrl": null,
  "IsVidmConfigured": false,
  "IsGreenBoxCatalogEnabled": false,
  "IsContainerModeEnabled": false,
  "ScepPayload": null,
  "BeaconConsoleSettingsServer": null,
  "CollectImeiNumber": false,
  "IsCustomOnboardingExperienceEnabled": false,
  "CustomOnboardingMessage": null,
  "CustomOnboardingUserName": null,
  "CustomOnboardingWelcomeText": null
  }
  }
  

**Figure 10: AirWatch validategroupidentifier API Response**

The response body of this request is variable to an extent depending on how the endpoint is configured. However, the high-level JSON objects of _Header_ / _Status_ / _NextStep_ remain constant. Within this request body, there are a few returned variables of note:

  * **SessionId:** This is the server-side generated RFC 4122 value authorizing the request to have successfully been submitted. If there was an error in the request body, the SID would be zeroed out in this response. Future requests against the API should include this value to link the request chain together.
  * **ServiceUrl / GreenBoxUrl / VidmServerUrl:** These values represent the authentication endpoints for identity validation through third-party authenticator integrations. How these values are populated will change depending on how the environment is configured.
  * **Type:** This is one of the most valuable messages; this value provides identification of how the environment is configured to support user authentication.

At the time of composing this whitepaper the following five _Type_ values have been enumerated:

  * **Type 1:** This value indicates the environment’s evaluation license has expired or the environment is not active.
  * **Type 2:** This value indicates the environment is configured with AirWatch identity services and will support SFA.
  * **Type 4:** This value indicates the environment is not configured with a third-party authenticator, and the environment supports SFA.
  * **Type 8:** This value indicates the environment will require token registration prior to allowing user authentication to occur.
  * **Type 18:** This environment has a SAML integration and would require MFA.

If the environment has a third-party integration for authentication services, the _ServiceUrl_ / _GreenBoxUrl_ / _VidmServerUrl_ variables would then be populated by these values indicating the authentication endpoint where the MDM client would be directed for authentication services. In the above response, the specific configuration of _Type 18_ reflects the environment is configured to support SAML based authentication. As a result, the _ServiceUrl_ variable is populated with the SAML based authenticator URL. Navigating to this URL, it is possible to attempt authentication within the context of the integrator.

[![Figure 11: IDP Authetnication Endpoint](/assets/images/airwatch_bypass_mfa_img4.png)](/assets/images/airwatch_bypass_mfa_img4.png "Figure 11: IDP Authetnication Endpoint") **Figure 11: IDP Authetnication Endpoint**

Based on the configuration of AirWatch, different endpoints will be referenced to enforce the variable integrators. If SFA is enabled or the user is required to submit values to the _airwatchenroll.aws_ API, CAPTCHA protection is enabled to limit brute-force authentication attempts.

[![Figure 12: AirWatch MDM Authentication CAPTCHA](/assets/images/airwatch_bypass_mfa_img5.png)](/assets/images/airwatch_bypass_mfa_img5.png "Figure 12: AirWatch MDM Authentication CAPTCHA") **Figure 12: AirWatch MDM Authentication CAPTCHA**

Although these security protections appear to protect the authentication interface from abuse, research identified that CAPTCHA enforcement and MFA are protection mechanisms that are only enforced during user registration and SFA is solely leveraged post completion of this process. Many of the API functions within AirWatch rely on SFA. Furthermore, previous registration of a user is not required to establish an SFA attack surface. All the vulnerable API endpoints are publicly accessible to an unauthenticated attacker, allowing for password attacks. Specifically, the following two API endpoints can be abused for SFA, and they also provide limited user enumeration of valid domain accounts.

  * /deviceservices/enrollment/airwatchenroll.aws/validatelogincredentials
  * /deviceservices/authenticationendpoint.aws

During AirWatch user registration, the Intelligence HUB application will communicate with _validatelogincredentials_ and pass the authentication credentials to the endpoint. Surprisingly, even if a third-party authentication is configured within the environment, this API is still provided as a communication interface. A HUB generated request to this endpoint would contain the following message body:
  
  
  {
  "Username": "test",
  "Password": "test",
  "EmailUserAccount": "",
  "EmailAddress": "",
  "EnableEmailPrompt": false,
  "Header": {
  "ProtocolRevision": 9,
  "ProtocolType": 0,
  "Language": "en",
  "SessionId": "a5ae38ff-e51a-437f-81e6-5eece675fe59",
  "Mode": "Native",
  "App": 4,
  "AppVersion": "20.09.0.15"
  },
  "SamlCompleteUrl": "aw:\/\/",
  "Device": {
  "Identifier": "3c411751c74c4f6cbceac8e39dd053d4c226d78d",
  "Type": 5,
  "Manufacturer": "Google",
  "Model": "Pixel 2 XL",
  "Product": "taimen",
  "OsVersion": "11",
  "IsEnterprise": false,
  "IsCompromised": false,
  "Serial": "",
  "IMEI": "",
  "IsDeviceAFWCertified": true,
  "AfwProvisioningCapability": 1,
  "InternalIdentifier": "3c411751c74c4f6cbceac8e39dd053d4c226d78d",
  "BundleIdentifier": "com.airwatch.androidagent",
  "AospEnrollment": false
  },
  "CaptchaValue": ""
  }
  

**Figure 13: Original validatelogincredentials Request**

Again, this can be compressed down to the following required values:
  
  
  {
  "Username": "test",
  "Password": "test",
  "Header": {
  "SessionId": "f4e74df0-f22f-48f5-9496-1d5b66526ed3"
  },
  "SamlCompleteUrl": "aw:\/\/",
  "Device": {
  "InternalIdentifier": "3c411751c74c4f6cbceac8e39dd053d4c226d78d"
  }
  }
  

**Figure 14: validatelogincredentials Compressed Request**

Submitting the authentication request to the endpoint allows for a verbose response to be returned in the JSON _Status_ object. The content in this response is read by the HUB agent and is typically reflected directly within the app.
  
  
  "Status": {
  "Code": 2,
  "Notification": "Invalid User Credentials"
  }
  

**Figure 15: validatelogincredentials Status Response**

Depending on the environment’s configuration, this response could allow for user enumeration. During research of this vulnerability, it was discovered that the ability to enumerate users is dependent on the authentication integrator and configuration of the endpoint. If functional, user enumeration would contain the following indicators:
  
  
  "Notification": "Invalid User Credentials"
  

**Figure 16: validatelogincredentials - Valid User Response**

At the time of writing, not all authentication types have been enumerated and the full extent of user enumeration is unknown.

Also, the CAPTCHA validator (of consecutive authentication requests) was discovered to be linked to the _InternalIdentifier_ or the Universal Device ID (UDID) value and the active SID. By resetting these values for each request, it is possible to successfully execute authentication attempts against this endpoint without any identity protections.

The secondary authentication endpoint of _authenticationendpoint.aws_ is leveraged within two functions for the Boxer email agent: registration and authentication. As part of the AirWatch configuration, it is possible to bypass the Intelligence HUB application altogether and directly register users through the Boxer application. AirWatch has indicated the Boxer application only supports SFA and is incapable of supporting MFA in its current form. Based on this understanding, Boxer represents a perpetual SFA attack interface and can be leveraged to bypass all MFA protections implemented within the AirWatch product suite.

[![Figure 17: AirWatch Boxer Registration](/assets/images/airwatch_bypass_mfa_img6.png)](/assets/images/airwatch_bypass_mfa_img6.png "Figure 17: AirWatch Boxer Registration") **Figure 17: AirWatch Boxer Registration**
  
  
  POST /deviceservices/authenticationendpoint.aws HTTP/1.1
  Host: awm.test.local
  User-Agent: Agent/20.08.0.23/Android/11
  Content-Length: 426
  Accept: application/json
  Content-Type: UTF-8
  Accept-Encoding: gzip, deflate
  Connection: close
  
  <AWAuthenticationRequest>
  <Username>
  <![CDATA[test]]>
  </Username>
  <Password>
  <![CDATA[test]]>
  </Password>
  <ActivationCode>
  <![CDATA[aCode]]>
  </ActivationCode>
  <BundleId>
  <![CDATA[com.boxer.email]]>
  </BundleId>
  <Udid>
  <![CDATA[ae869987f1324beba92dfaca4edc4f0d896fdf49]]>
  </Udid>
  <DeviceType>5</DeviceType>
  <AuthenticationType>2</AuthenticationType>
  <AuthenticationGroup>
  <![CDATA[com.boxer.email]]>
  </AuthenticationGroup>
  </AWAuthenticationRequest>
  

**Figure 18: Boxer Registration Authentication Request**

Both the Boxer registration and authentication API functions leverage the same API endpoint of _authetnicationendpoint.aws_. The variable factor in this request is the Request Header _Content-Type_ value. During the registration process, this value is populated as _UTF-8_ , allowing for the submission of an XML formatted message body. This communication is a transactional request and does not require any prior authorization to being performed.

The Boxer authentication endpoint contains the following request message body:
  
  
  POST /deviceservices/authenticationendpoint.aws HTTP/1.1
  Host: awm.test.local
  User-Agent: Agent/20.08.0.23/Android/11
  Content-Length: 259
  Accept: application/json; charset=utf-8
  Content-Type: application/json; charset=utf-8
  Accept-Encoding: gzip, deflate
  Connection: close
  
  {
  "ActivationCode": "aCode",
  "BundleId": "com.box.email",
  "Udid": "409853f111044398a463119d878f34665e23271f",
  "Username": "test",
  "AuthenticationType": "2",
  "RequestingApp": "com.boxer.email",
  "DeviceType": "2",
  "Password": "test",
  "AuthenticationGroup": "com.air-watch.boxer"
  }
  

**Figure 19: Boxer Authentication Request**

The Boxer authentication request is triggered by modifying the Request Header _Content-Type_ to be _application/json_ and submitting a JSON object in the request. Both the registration and authentication endpoints contain the following submission variables:

  * **ActivationCode:** This is the publicly disclosed AirWatch GroupID value. Udid: This is the unique identifier of the mobile device making the authentication request. This is used as a primary key in the AirWatch registration database, and from what I have been able to determine is unvalidated.
  * **Username:** The target username for the authentication request.
  * **AuthenticationType:** This value was captured from default requests and is believed to be attributed to the leveraged access path. There are specific accepted numeric values for this field.
  * **DeviceType:** This value was captured from default requests and is believed to be attributed with the device type being leveraged. There are specific accepted numeric values for this field.
  * **Password=***REDACTED*** The target password is attributed to the authentication request.

Additionally, in both instances, the server responds back with a JSON message body:

[![Figure 20: Boxer API Authentication Response](/assets/images/airwatch_bypass_mfa_img7.png)](/assets/images/airwatch_bypass_mfa_img7.png "Figure 20: Boxer API Authentication Response") **Figure 20: Boxer API Authentication Response**

Examining the response _StatusCode_ , it is possible to perform limited user enumeration and/or SFA. Research against this API has identified the following _StatusCode_ values:

  * **AUTH–1:** This value indicates the submitted _ActivationCode_ was incorrect.
  * **AUTH-1001:** This value indicates the submitted username or password were incorrect.
  * **AUTH-1002:** This value indicates the submitted username has been locked out.
  * **AUTH-1003:** This value indicates the submitted username had been disabled in the AD domain.
  * **AUTH-1006:** This value indicates a valid username, password and _ActivationCode_ were submitted.

This API is publicly accessible and at the time of writing, AirWatch does not provide any functionality to disable access to this communication endpoint and/or disable the Boxer service all together. It may be possible to disable Boxer registration services; however, AirWatch was unable to provide a test environment to confirm this.

Based on these response codes, it is possible for an attacker to enumerate through a list of values containing random `GroupID` or `Username` values and successfully execute a SFA attack. To fully weaponize this attack surface, I developed [airCross](https://github.com/optiv/airCross) as a PoC toolkit for performing `GroupID` and SFA attempts against an AirWatch environment.

The rough PoC of airCross has been replaced by [Dauthi](https://github.com/emptynebuli/dauthi) which is a MDM analysis framework designed to perform SFA validation against numerous platforms.

Upon discovering these deficiencies, we reported them to VMWare’s security team. During conversations of the vulnerability, VMWare security personnel indicated it did not represent a deficiency with the product’s functionality and was not considered a security issue that would be remediated. Instead, VMWare provided several mitigation steps that could be introduced into the environment:

  * **Implementation SAML/IDP Services:** AirWatch support identified that SAML/IDP/MFA integrations are only supported during user registration processes through the Intelligence HUB application, and Boxer only supports SFA, preventing mitigation of this vulnerability.
  * **Disable Boxer Enrollment Services:** AirWatch support indicated this setting would disable the Boxer registration services but was unable to provide any information regarding whether the authentication API endpoint would be removed. As this endpoint is multi-purposed for both access to the Boxer email client and Boxer registration services, it is probable this will not remove the attack surface.
  * **Disable Discovery Services:** This will prevent public disclosure of the AirWatch endpoint and GroupID. As this information is considered to be public, this is of limited value to preventing the attack surface against the environment. The GroupID value can be brute-forced, and if successful, can be leveraged in an authentication attack against the environment.

## Mitigations

My research on this issue has been unable to validate if any of the suggested mitigation steps would reduce or eliminate the SFA / MFA bypass attack surface. Based on this understanding, the following recommendations can be implemented to reduce the MDM attack vector:

  * **Strong Corporate Password Policy:** Implementing a policy of a 12-character minimum password length can improve password strength, especially when combined with blacklisting of common password patterns such as “SeasonYear.”
  * **Limit User Device Registration:** A successfully compromised account could be leveraged to attack other internet-exposed authentication portals or an attacker could choose to self-register a malicious device and obtain access to the corporate AirWatch policy. By limiting MDM registration to a single UDID and/or a list of validated UDID values, an attacker would be unable to register a malicious device associated to a previously registered and valid user.
  * **Monitor MDM Authentication Requests:** Ensure the MDM application is closely monitored for malicious activity, such as brute-force authentication attempts. This action would provide an early warning of malicious activity.

## Disclosure Timeline

  * **February 20, 2020:** Issue initially reported to VMWare.
  * **June 9, 2020:** VMWare indicated an inability to validate the vulnerability after numerous communication touchpoints.
  * **October 30, 2020:** PoC development
  * **October 16, 2020:** VMWare indicated the reported vulnerability did not represent a functionality deficiency and operated as expected.
  * **October 20, 2020:** VMWare provided technical configuration documentation on mitigation steps for the SFA surface.
  * **October 23, 2020:** VMWare support services identified AirWatch’s Boxer interface is only capable of supporting SFA and the previously provided mitigation steps were non-applicable.
  * **November 2, 2020:** VMWare support indicated documented support articles, allowing for Boxer authentication services to be disabled, did not exist.

[](/tooling/2020/12/11/aircross.html)
