---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-20_the-hunt-for-albeast-a-technical-walkthrough.md
original_filename: 2024-08-20_the-hunt-for-albeast-a-technical-walkthrough.md
title: 'The Hunt for ALBeast: A Technical Walkthrough'
category: documents
detected_topics:
- oauth
- jwt
- supply-chain
- sso
- access-control
- xss
tags:
- imported
- documents
- oauth
- jwt
- supply-chain
- sso
- access-control
- xss
language: en
raw_sha256: cd8a05efabe9231b1ca875983dcd490acbc1c3ff9aacaf67abb711bec0db8256
text_sha256: 6b01b7836a5a672c315bbd716050cf7029a2df1d9c0e1acef39981c2a4c2aa42
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# The Hunt for ALBeast: A Technical Walkthrough

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-20_the-hunt-for-albeast-a-technical-walkthrough.md
- Source Type: markdown
- Detected Topics: oauth, jwt, supply-chain, sso, access-control, xss
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `cd8a05efabe9231b1ca875983dcd490acbc1c3ff9aacaf67abb711bec0db8256`
- Text SHA256: `6b01b7836a5a672c315bbd716050cf7029a2df1d9c0e1acef39981c2a4c2aa42`


## Content

---
title: "The Hunt for ALBeast: A Technical Walkthrough"
page_title: "ALBeast Vulnerability: AWS ALB Auth Flaw Explained"
url: "https://www.miggo.io/resources/uncovering-auth-vulnerability-in-aws-alb-albeast"
final_url: "https://www.miggo.io/post/uncovering-auth-vulnerability-in-aws-alb-albeast"
authors: ["Liad Eliyahu (@liadeliyahu)"]
programs: ["AWS"]
bugs: ["AWS ALB", "Authentication bypass", "Authorization bypass"]
publication_date: "2024-08-20"
added_date: "2024-08-26"
source: "pentester.land/writeups.json"
original_index: 56
---

[![Miggo logo](https://cdn.prod.website-files.com/67abed9eb85482c7968f46d2/67aebd0a506169a16bfa7332_98fabd45c2e31dc8b57720283b3e5125_miggo-logo.svg)](/)

Product

[AI Runtime Defense PlatformSee & Secure AI and Agentic Risks](/runtime-defense-platform-for-applications-ai-and-agents)

[Miggo ADR PlatformProtect Every Application You Build or Use](/why-adr)

Product

[Runtime Defense Platform for Applications, AI, and AgentsDetect and respond to AI and agentic driven threats](/runtime-defense-platform-for-applications-ai-and-agents)[**Miggo Know** Know your live applications inside-out](/product/security-observability)[Miggo ProveFind and prevent the exploitable risks that matter](/use-cases/runtime-vulnerability-prioritization)[Miggo ShieldProactive protection for application threats](/product/miggo-waf-copilot)

See Miggo in Action

![RCE detection alert card showing a 9.9 Critical risk score, with an attack path visualization tracing from internet through Cloudflare, Kafka, and a flagged service to a PostgreSQL database with PII, and a fix available indicator.](https://cdn.prod.website-files.com/67abed9eb85482c7968f46d2/6807935dba4a82698a5be7d4_book_a_demo_top_nav.svg)

Book a Demo

[](/book-a-demo "Book a Demo")

Solutions

[Runtime Vulnerability PrioritizationAttain contextual runtime vulnerability prioritization](/use-cases/runtime-vulnerability-prioritization)[Instant Defense with Virtual Patching (WAF Copilot)Block AI Attacks with Custom WAF Rule](/product/miggo-waf-copilot)[WAF Copilot for AWS WAFClose the AI-Accelerated Patch Gap in Seconds.](/product/waf-copilot-for-aws-waf)[Runtime Detection and Response (ADR)Respond to attacks in real time](/use-cases/runtime-attack-detection-and-response)[1st and 3rd Party Application ProtectionBlock vulnerability exploitation](/use-cases/1st-and-3rd-party-application-protection)[Runtime Intelligence with Grafana CloudFrictionless, risk decisions powered by Grafana telemetry](/product/miggo-security-grafana-labs)

AI Application Security

[AI Runtime ObservabilityContinuous Discovery & Control over Agentic Topology](/use-cases/ai-runtime-observability)[Agentic Detection & ResponseSee and secure AI and agentic risks](/use-cases/agentic-detection-response-for-ai-applications)

industries

[Health](/industries/industries-health)[Technology](/industries/technology)[Financial Services](/industries/financial-services)

Resources

Resources

[React2ShellLive Coverage of the Exploit](https://www.miggo.io/react2shell)[BlogThe lastest on products and research](/blog)[Reports and WebinarsAccess the latest reports and webinars](/reports-webinar)[EventsConferences, meetups, and live sessions](/miggo-at-rsac-2026)[NewsCompany announcements and press](/news)[AcademyA knowledge hub for AI and Application Security](/academy)[Predictive Vulnerability DatabaseAccess the new Predictive Vulnerability Database](https://www.miggo.io/vulnerability-database)[Predictive Vulnerability DatabaseShort description here](https://www.miggo.io/vulnerability-database)

fEATURED

![The Security Patch that Created a Vulnerability: Miggo Security Releases Detector for CVE-2026-23111 to Catch an Attack Before a Fix](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/6a32a70548ea634f021f64e8_Blog_1200x630_CVE-2026-23111_Press_Release_md.webp)

The Security Patch that Created a Vulnerability: Miggo Security Releases Detector for CVE-2026-23111 to Catch an Attack Before a Fix

[](/post/the-security-patch-that-created-a-vulnerability-miggo-security-releases-detector-for-cve-2026-23111-to-catch-an-attack-before-a-fix)

[More From Our Blog](/blog)

[Company](/company "button")

Book a Demo

[](/book-a-demo "Book a Demo")

Book a Demo

[](/book-a-demo "Book a Demo")

[Home](/)

/

[Blogs](/blog)

/

The Hunt for ALBeast: A Technical Walkthrough

Research

August 20, 2024

# The Hunt for ALBeast: A Technical Walkthrough

Miggo’s inside visibility into app behavior enabled Miggo Research to uncover and address the ALBeast vulnerability affecting thousands.

[![Photo of Liad Eliyahu](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/680681536f118be398699f94_Liad_Eliyahu_160x160%402x.jpg)](/author/liad-eliyahu)

[Liad Eliyahu, ](https://www.linkedin.com/in/liadeliyahu/)

[Head of Research](/author/liad-eliyahu)

![](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/691f1b3717592f018599b204_Blog_1200x630_The-Hunt-for-ALBeast_-A-Technical-Walkthrough.webp)

[Back to the Blog](/blog)

### CONTENTS

Enjoying this content?

Suscribe to our newsletter

Thank you!

You're subscribed!

Oops! Something went wrong while submitting the form.

Share

When Miggo onboards customers, we gain visibility into application behaviors from within. This unique perch allows Miggo Research to discover and address new vulnerabilities impacting thousands of organizations. That’s exactly what happened with ALBeast. This blog details the technical aspects of that discovery, including Miggo’s recommendations for mitigation. For a broader overview, we invite you to check out our initial blog about ALBeast.  
Skip to our first encounter with ALBeast

## Discovering ALBeast: An Unexpected Security Flaw

We identified a critical configuration-based vulnerability that enables authentication and authorization bypass in applications using the AWS ALB authentication feature, provided they do not comply with the updated AWS documentation issued after Miggo’s disclosure. This vulnerability allows attackers to directly access affected applications, particularly if they are exposed to the internet.

### Here are the primary issues:

  * **Misconfiguration:** Applications misconfigured as ALB target groups and accessible directly, bypassing the ALB, can be exploited. Attackers can use a shared public key server for all AWS accounts in the region (e.g., `https://public-keys.auth.elb.region.amazonaws.com/key-id`) to set an arbitrary key ID (`kid`). This allows the attacker to supply a public key that the application uses to validate the forged ALB JWT token. Following our report, AWS updated their documentation to refine best practices for configuring Security Group restrictions.  
  

  * **Misimplementation:** Until recently, the AWS ALB [user authentication docs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-authenticate-users.html#user-claims-encoding) did not include guidance on validating a token’s signer—a crucial field for ensuring that the token was signed by the trusted ALB. Without this validation, applications might trust an attacker-crafted token. The absence of this best practice leaves applications vulnerable to ALBeast attacks. Note that ALB tokens do not contain an `aud` field, which complicates validation.  
  

  * **Issuer Forgery:** An attacker can forge an **authentic** ALB-signed token with arbitrary identities, claims, and issuers (IdP) using its controlled ALB. This means that misconfigured applications that verify the identity issuer are also vulnerable to ALBeast.

We reported these issues to the AWS security team on April 6th, and have since been closely collaborating with AWS throughout the disclosure and remediation process. 

## Systems Affected by ALBeast

ALBeast can impact applications hosted in any environment–AWS, other public cloud providers, or on-prem. Since discovering ALBeast, Miggo has identified over 15,000 (out of 371,000*) potentially vulnerable applications using AWS ALB’s authentication feature. 

We’ve done our best to contact each affected organization with our findings and provide support where needed.

Out of multiple implementations and open-source projects we encountered, the vast majority (> 95%) lack the `signer` validation implementation. A significant share does not restrict access according to the latest recommendations, allowing applications to be accessed from the internet and other footholds in the VPC.

There are two AWS ALB authentication mechanisms, both of which make applications vulnerable:

  1. [OIDC using IdP  
](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-authenticate-users.html#oidc-requirements)
  2. [AWS Cognito](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-authenticate-users.html#cognito-requirements)

## Miggo Recommendations

### For AWS Customers

** _1\. Validate the signer of the ALB JWT token is the expected ALB_**

On May 1st, 2024, AWS updated their ALB user authentication docs with the following:

> “ _To ensure security, you must verify the signature before doing any authorization based on the claims and validate that the signer field in the JWT header contains the expected Application Load Balancer ARN.”_

The `signer` is a field that AWS inserts into the JWT header to mention which instance of ALB signed this token. 

AWS added this piece of code to validate the signer, which is the ALB instance that signs the token:  

  
  
  
  import jwt  
  import requests  
  import base64  
  import json  
  
  # Step 1: Validate the signer  
  expected_alb_arn = 'arn:aws:elasticloadbalancing:region-code: \  
  account-id:loadbalancer/app/load-balancer-name/load-balancer-id'  
  
  encoded_jwt = headers.dict['x-amzn-oidc-data']  
  jwt_headers = encoded_jwt.split('.')[0]  
  decoded_jwt_headers = base64.b64decode(jwt_headers)  
  decoded_jwt_headers = decoded_jwt_headers.decode("utf-8")  
  decoded_json = json.loads(decoded_jwt_headers)  
  received_alb_arn = decoded_json['signer']  
  
  assert expected_alb_arn == received_alb_arn, "Invalid Signer"  
  
  # Step 2: Get the key id from JWT headers (the kid field)  
  kid = decoded_json['kid']  
  
  # Step 3: Get the public key from regional endpoint  
  url = 'https://public-keys.auth.elb.' + region + '.amazonaws.com/' + kid  
  req = requests.get(url)  
  pub_key = req.text  
  
  # Step 4: Get the payload  
  payload = jwt.decode(encoded_jwt, pub_key, algorithms=['ES256'])  
  

**_2\. Ensure that applications receive traffic exclusively from the trusted ALB_**

On July 19th, 2024, AWS updated the authentication feature documentation to clarify best practices for configuring Security Groups:

> _“Also, as a security best practice we recommend you restrict your targets to only receive traffic from your Application Load Balancer. You can achieve this by configuring your targets' Security Group to reference the load balancer's Security Group ID.”  
> _

![Screenshot of AWS ALB Documentation changes made after the report](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/67e439223ff3b73928457632_66c38749a6a97199a93aff80_66c2473caad799fc32e42706_AD_4nXfIHi1SijYVat5CqKcr-wrnQo3HhdQ4MO5Us3rHyjLWCckxCYS7ND7ExU5OSGfGmGiyRAQYbCY_uS09uJBDkc8AWvt1QiL4uXQVGGnVri1i14yey-d-Gfr_l01cE0g1CmevIvaKbMV0WI5ZPyPEozaOrZ5u.png)

AWS ALB Documentation changes made after the report

For more details, see the Target Groups [reference](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-register-targets.html#target-security-groups) and the ALB Security Groups [reference](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-update-security-groups.html#security-group-recommended-rules).

**_A Note by Miggo Research_**

 _Ultimately, AWS does not view issuer forging as a vulnerability. They state that the service operates as intended and that the_[ _shared responsibility model_](https://aws.amazon.com/compliance/shared-responsibility-model/) _applies to this issue, implying that applications should follow the latest documentation by updating their code and Security Groups configurations._

_The root problem of the ALBeast vulnerability is addressed through the aforementioned customer-required changes. AWS has opted to track the number of customers in problematic configurations and communicate this information to them, rather than refactor the ALB component itself. As a result, only applications that adhere to the updated documentation on signer validation by the application and the refined Security Groups recommendations are considered safe._

### For AWS 

ALB verifies the original issuer and stores it in the encrypted cookie. However, on follow-up requests, ALB uses the new issuer from the ALB configuration without validating it against the original issuer. We recommend that AWS modify ALB to retrieve and validate the original issuer from the encrypted cookie.

Not all ALB applications validate the `issuer`. Even if they do, one issuer could be shared among multiple organizations. For example, in the Google SSO use case, the `issuer` is `https://accounts.google.com` could be used across multiple organizations. Further improvements to strengthen ALB security could include:

  1. Adding an `aud` validation mechanism. AWS ALB could implement an `aud` mechanism to prevent this issue. This could be made in addition to the docs' recommendations to validate the `signer` __ field.  

  2. Notifying users regarding the exposure of ALB-connected application instances (EC2, EKS, etc.) in target groups that receive traffic from sources other than the ALB (Docs were updated on July 19th).  
‍  

  3. Updating AWS Docs to mention verifying the `signer` field in the `X-Amzn-Oidc-Data` _,_ which verifies that requests came from a trusted ALB (Docs were updated on May 1st).

## Story Time: Our First Encounter With ALBeast

We first learned of an issue when onboarding a customer using AWS Application Load Balancer (AWS ALB) for user authentication. Interested in learning more about this mechanism, we researched how it works and how Miggo’s ADR ([Application Detection and Response](/why-adr)) might be able to detect malicious behavior in applications that use it.

This is when we uncovered two widespread customer misconfigurations and one AWS implementation decision within the AWS ALB itself.

## Key Definitions

### **What is an ALB?**

An Application Load Balancer (ALB) is a service that automatically distributes incoming application traffic across multiple targets, such as EC2 instances, containers, and IP addresses, within one or more Availability Zones. It operates at Layer 7, allowing routing decisions based on content, such as URL path or host field in HTTP headers, authentication enforcement, or firewall integration. ALBs increase web applications' scalability, reliability, and fault tolerance by load-balancing network traffic across different servers, ensuring no single server bears too much demand.

### **What are JWT and JWK?**

JWT and JWKs facilitate secure authentication and data integrity in web applications.

JWT (JSON Web Tokens) are compact, URL-safe tokens that securely transmit information between parties. They consist of a header, a payload (which contains claims about a user), and a signature to prevent tampering.

JWK (JSON Web Key) is a JSON format representing cryptographic keys. These keys are used to encrypt or verify JWT signatures. JWKs are often grouped in a JWK Set (JWKS), serving as a public key directory for verifying JWT authenticity.

## This animation helps illustrate the resulting authentication flow:

![Graphic showing ALB authentication flow](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/6926c531eab89459aa09db82_Screenshot%25202024-08-20%2520at%25201.22.37%20\(2\).webp)

ALB authentication flow demonstration

  
To understand the authentication and request-response flow of AWS ALB, please see the diagram below, which we pulled directly from [AWS Docs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-authenticate-users.html).

![Graphic showing ALB authentication flow from AWS Documentation](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/67e439223ff3b73928457650_66c38748a6a97199a93aff72_66c24a7dcd28265be7f525a1_AD_4nXeN1fI1z7Yx06Vo23gBp_WGEnqp2L83haJy8getr3KhPa8IJDM2HyHTTlLekCof6IUBQd_2zL7zkCOKNdRxV-ri_0Q9j4RUhlnWy7Gfb6DtgmpAp_6S2mCvod6FMFyPCDIifGfkFzw3isMhvWO-5pzNP6k.png)

ALB authentication flow from AWS Documentation

## The Initial Red Flag

Now, let’s note how the ALB authentication docs previously recommended applications verify an ALB token (steps 9-10 in the figure): 
  
  
  import jwt  
  import requests  
  import base64  
  import json  
  
  # Step 1: Get the key id from JWT headers (the kid field)  
  encoded_jwt = headers.dict['x-amzn-oidc-data']  
  jwt_headers = encoded_jwt.split('.')[0]  
  decoded_jwt_headers = base64.b64decode(jwt_headers)  
  decoded_jwt_headers = decoded_jwt_headers.decode("utf-8")  
  decoded_json = json.loads(decoded_jwt_headers)  
  kid = decoded_json['kid']  
  
  # Step 2: Get the public key from regional endpoint  
  url = 'https://public-keys.auth.elb.' + region + '.amazonaws.com/' + kid  
  req = requests.get(url)  
  pub_key = req.text  
  # Step 3: Get the payload  
  payload = jwt.decode(encoded_jwt, pub_key, algorithms=['ES256'])

See the original in full [here](https://web.archive.org/web/20240105021033/https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-authenticate-users.html).

We were immediately struck by the beginning of step 2: In a given region, a single JWK-like service provides cryptographic keys for applications operating in that area.

This means that even though these applications may have different requirements, use different systems for verifying identities (known as IdPs), and belong to different customers, they both trust the keys provided by this single service, differentiated only by the `kid` parameter. Regardless of their differences, they can potentially use the key of another application.

## Attacking Applications With Forged Tokens

Assuming an application has not yet followed the latest AWS update and validated the `signer`, if we wanted to target an application in the `us-east-1` region, what would stop us from:

  1. Configuring an `us-east-1` ALB with a personal IdP
  2. Signing a malicious token with the ALB
  3. Passing the malicious token to the application inside `x-amzn-oidc-data`

…Well, nothing!

So, that’s exactly what we did. We configured an ALB, minted a token, and passed it along to a dummy application we created in the same region. 

…but this first attempt was thwarted.

The ALB would have none of it. It detected the `x-amzn-oidc-data`, discarded it, redirected the user to sign in using the configured IdP, and continued with its regular flow. Our malicious header, though potentially valid, didn’t even reach the application! 

It’s ok, we’re stubborn. Now, on a mission, we understood we needed a way to bypass the ALB. This proved tricky. We tried several attack techniques, most of them variations of request smuggling, but mitigations in place prevented us from smuggling our request through.  
  
We ended up writing two simple Python Flask applications behind ALBs. The first one prints the headers back to the user, which is nicer when playing with requests using BurpSuite:
  
  
  
  from flask import Flask, request, jsonify  
  app = Flask(__name__)  
  
  @app.route('/', methods=['GET', 'POST'])  
  def home():  
  return jsonify({  
  "Received Headers": dict(request.headers),  
  "Body": request.get_data(as_text=True) if request.data else "No Body"  
  })  
  
  if __name__ == '__main__':  
  context = ('/home/ubuntu/test/idp/pyop/example/https.crt',  
  '/home/ubuntu/test/idp/pyop/example/https.key')  
  app.run(debug=True, host="0.0.0.0", port=443, ssl_context=context)  
  

The second one verifies the JWT header using AWS recommended code and from the documentation and issuer verification that we added as needed:
  
  
  
  from flask import Flask, request, jsonify  
  import jwt  
  import base64  
  import json  
  import requests  
  region = "eu-central-1"  
  expected_iss = "https://cognito-idp.eu-central-1.amazonaws.com/eu-central-1_QKBTDh9s5"  
  
  def validate_jwt(token):  
  jwt_headers = token.split('.')[0]  
  decoded_jwt_headers = base64.b64decode(jwt_headers)  
  decoded_jwt_headers = decoded_jwt_headers.decode("utf-8")  
  decoded_json = json.loads(decoded_jwt_headers)  
  kid = decoded_json['kid']  
  url = 'https://public-keys.auth.elb.' + region + '.amazonaws.com/' + kid  
  req = requests.get(url)  
  pub_key = req.text  
  payload = jwt.decode(token, pub_key, algorithms=['ES256'])  
  if payload['iss'] == expected_iss:  
  return payload  
  raise Exception("Bad issuer")  
  
  app = Flask(__name__)  
  
  @app.route('/', methods=['GET', 'POST'])  
  def home():  
  headers = dict(request.headers)  
  result = ''  
  if 'X-Amzn-Oidc-Data' in headers:  
  try:  
  result = validate_jwt(headers['X-Amzn-Oidc-Data'])  
  except BaseException as ex:  
  return str(ex)  
  return f"Welcome {result['email']}"  
  return "unauthenticated"  
  
  if __name__ == '__main__':  
  context = ('/home/ubuntu/test/idp/https.crt', '/home/ubuntu/test/idp/https.key')  
  app.run(debug=True, host="0.0.0.0", port=443, ssl_context=context)  
  
  
  
  

At this point, we were able to forge a JWT token signed by AWS for any app exposed to the internet that doesn’t verify the issuer (`iss`) field as part of the identity validation process and the `signer` field during the JWT validation. We didn’t have any means to pierce an ALB, but we were creative and found ones that were directly exposed instead.  
  
Having gotten this far, we had to ask: Is this capability interesting? Sure, we could forge a token, but would applications verify the JWT’s issuer beyond the user identity supplied in the `sub` field?  
  
It never hurts to check.

To our surprise, we looked through open-source projects with an ALB integration and quickly found applications that didn’t verify the `issuer` and were vulnerable to attack! While most of the open-source projects we audited were vulnerable to ALBeast by not verifying the `signer`, some had failed to include the `issuer` __ altogether from the start.

## Broadening The Scope Of Our Attack

It turned out that we had discovered a way to forge a token with an arbitrary identity for applications that implement the ALB auth mechanism, even when deployed on another cloud provider! 

This vulnerability could be exploited in the following scenarios:

  1. The application could be accessed directly, bypassing the ALB.
  2. The application did not verify the signer field as part of the JWT verification (a real issue for almost every application at the time of our research).
  3. The application did not verify the issuer IdP (`iss`) field as part of the user identity validation (though most applications do validate the Issuer IdP).

We should have been satisfied, but we couldn’t help but wonder… How far could we take this?  
  
We continued our research to find out if we could also forge the issuer. We first tried changing the issuer in the OIDC configuration section of the ALB, but the authentication failed with status code `401`. The ALB verifies the issuer during the authentication process. Our malicious configuration said the issuer is `google.com`, but the token is signed with a key that doesn’t exist on `google.com`. The mismatch caused the ALB to return a `401` __ status __ code.

![Screenshot showing editing the ALB configuration section on AWS console](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/67e439213ff3b73928457612_66c38748a6a97199a93aff6c_66c24a7d141c433fa9e84c30_AD_4nXe_zYejOs-HLutvLYe9LvdyYFvonDjW4VsWaVAa6gYeKWxr1-diJ4njQ2dQjBLJBVQnujJc1cUFqre269G93nK13aWOaScVkUXwr-20Sy9FUhhO6DhBVuJbL9mmt-4wscBilwX1vqy6q5yt6Xh0PdRqts7I.png)

Editing the ALB configuration section on AWS console

‍

![Screenshot showing ALB authentication failure after issuer modification](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/67e439213ff3b73928457615_66c38748a6a97199a93aff75_66c24a7d8e3dfd89b79c41ba_AD_4nXcgwTnVRIJQwo20NVWXii3srHgkjYDfaablFbBRLJhbyDC6IL6TuCEiShWxr8e78MGB4eqFg1y3fsSi6oJn4lq-TEDJQdm75DYVvAvH0adu0Q5I7SDvqsl18QIRcJtq8fNDE3GiWXEIJ0OtMi4Pw9edj3Q-.png)

ALB authentication failure after issuer modification

While brainstorming how to bypass their validation, we noted two important connections:

  1. The session between the user and the ALB
  2. The headers that are derived from the session and the configuration sent from the ALB to the application

This begged the question: What if some parameters in the user’s session (from the first connection) were out of sync with the configuration or what the application receives (in the second connection)?  
  
We found the answer by reviewing AWS’s documentation on the  
`AWSELBAuthSessionCookie` cookie:

> “… the load balancer shards a cookie that is greater than 4K in size into multiple cookies. If the total size of the user claims and access token received from the IdP is greater than 11K bytes in size …”

This is a major indicator that what’s inside the `AWSELBAuthSessionCookie` is an encrypted form of the user claims and the token from the IdP. To prove the cookie is encrypted and the claims are inside, we configured the required scopes to be as minimal as possible:

![Screenshot showing ALB configured to contain only OpenID scope](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/67e439223ff3b73928457638_66c38749a6a97199a93b0014_66c24a7dffa9c5fbc7666d1a_AD_4nXcbkHEFdl65yYZGHSaJrDEpLFJGf134hlwgWBTxuQzflPH88qlVmJbLWieAQ7E5GEat1nqvrSLXMJXenj0asHDBVob0NPYX5S9Sah6dXDxo1tJx61d1mgw6Yw7UQhVKYWyDnAcu3ixZwx0x_dHPZXkOEpbq.png)

ALB configured to contain only OpenID scope

We then authenticated and got this cookie:  

![Screenshot showing ALB encrypted cookie with OpenID scope values](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/6926c643f9541bb2a9a1438b_AlBeast_inline_image_6.webp)

ALB encrypted cookie with OpenID scope values

As you can see in the top right corner, it’s 1452 bytes long.  
‍  
Then, we added a few scopes to get more claims (email, profile, address):  

![Screenshot showing setting additional scopes in the ALB configuration](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/67e439223ff3b73928457635_66c38748a6a97199a93aff68_66c2473be97e605251876677_AD_4nXcg-hgk4T9Hs9WvIz5PTNxxhpqqH5995-yDjIO35F8K6IqTlcb4vafmSNg18KFsRYnQU_jDTw0StfoIA0Sl2hkbOfo5TJDBVmyLBd6tSlamZBpJZALCQbBXQEASNnpa3eM7qeFyZL5l7k_nCh8UBmt0RJ6o.png)

Setting additional scopes in the ALB configuration

We can also control the length of the claims data by extending properties in our controlled IdP:  

![Screenshot showing setting a large user address value in Okta configuration](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/67e439213ff3b73928457618_66c38748a6a97199a93aff6f_66c24a7d19e9d6173afdcb07_AD_4nXeKFyHkjgSYpwFTdrq0a3UcLEb9hfQUUwZGsFlsGxLwUfur_wBdV33fO8doC7mQc_sMOx2C5SN6mrHQpWJzacoy7I11qVgxwMSm9F7DFupWpBaodSmrh5H59_BYRKVFSTDvB7-Tt0EtmE-46fdo7YSHNl4R.png)

Setting a large user address value in Okta configuration

This resulted in a much larger cookie, 2,540 bytes long.

![Screenshot demonstrating ALB results in a much larger cookie after the scope modifications](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/67e439223ff3b7392845762f_66c38748a6a97199a93aff78_66c24a7db74bc06b9debd129_AD_4nXedESmj32DNBjaVRq7pbbg3UOWbBNLLIAz3mpuLBez6rntTqtOEQMxI9rIi927ZUqxAj3zWvNXeKe9Azh8cR8DhceOIezbjvXfrfGNrrB9YBCb9kioPDEh0ovmpPpiCrbKe3gdE4xfYY3VFDGGIl2qK0urh.png)

![Another screenshot demonstrating that ALB results in a much larger cookie after the scope modifications](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/6926c72eb1b97731a6fb53b9_AlBeast_inline_image_8.png)

ALB results in a much larger cookie after the scope modifications

Bingo. We discovered at least one place where the ALB stores data - it creates a session cookie and stores the token. At this point, all we needed was to find one more place where the ALB stores our data to see if we could force a desync between them.

We looked at the `X-Amzn-Oidc-Data` header, which contained the JWT signed by the ALB. It had a one-minute expiration time. 

Hurrah, we’ve found another place where data is stored!

## Putting Our Theories To The Test

What would happen if we authenticated, got a session with a token in `AWSELBAuthSessionCookie`, changed the ALB configuration, and the token expired? We knew that the ALB would have to mint a new token. Would the ALB take the issuer from the encrypted token? Or…would it take it from the configuration as-is?

Remember, the user could be set to anything. The ALB only determines if the issuer we provided is valid after it communicates with the IdP. In the session, the issuer is validated after the IdP check, whereas in the configuration, it is specified before the validation occurs.  
‍  
To our surprise, the ALB indeed took the issuer from the configuration! In other words, we would be able to use our own controlled ALB to sign a valid token in the same region as any application we felt like attacking, and we could even control the `issuer`. This means we could also forge a completely valid JWT token for any target application that could be accessed directly and not through the ALB!

![Screenshot showing legitimately AWS signed token with attacker controlled issuer](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/6926c820939d019d8f3392c1_issuer-forged%20\(1\).webp)

Legitimately AWS signed token with attacker controlled issuer

## F2F With ALBeast

**We had discovered how to forge a token that would be accepted by any target application in a few simple steps:**

  * Create an ALB in the target region pointing to our IdP.
  * Mint a token with desired claims.
  * This token has a valid _issuer_ : our IdP.
  * Its public key is stored in the regional JWKs server, trusted by the target application.
  * Reconfigure the ALB to target the target `issuer`.
  * Wait for the token to expire, then refresh it.
  * The refreshed token now contains the target `issuer`.
  * Send this token directly to the target application, bypassing the ALB.
  * The target application validates the issuer and confirms that all is in order.
  * We’ve now provided the application with a forged token!  

This is **HUGE.**

![Graphic demonstrating ALBeast attack](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/6926c8a6cbb01068f3a68ada_AlBeast_inline_image_10.png)

ALBeast attack demonstration

Any ALB that uses this feature exposes the `/oauth2/idpresponse` endpoint. Combined with a technique to search instances online serving the same TLS certificate, finding potentially vulnerable instances became a turkey shoot.

## _Responsible Disclosure_

 _In the course of our research, we found and reported vulnerable configurations in open-source applications and organizations with responsible disclosure programs. Publication of these findings will be handled separately and aligned with each policy._

_Among the open-source projects, we found two vulnerable AWS repositories:_

_1._[_AWS Configuration for ALB Identity library for .NET_](https://github.com/awslabs/aws-alb-identity-aspnetcore/blob/3df4f4b62775ac2d77564d57421f301f12d43e0c/Amazon.ApplicationLoadBalancer.Identity.AspNetCore/ALBIdentityMiddleware.cs#L46) _‍_

 _2._[_AWS ALB library for Istio_](https://github.com/awslabs/aws-alb-route-directive-adapter-for-istio/blob/master/authzadaptor.go) _‍_

 _After we reported the vulnerable implementations to AWS, the repositories were archived and claimed to be in a “retirement” process._

## Disclosure Timeline

**March 21, 2024** \- Miggo discovers a customer’s service that uses ALB authentication. An application suspected to be vulnerable to auth bypass ignites the generic research.

**April 06, 2024** \- Miggo reports the vulnerability to AWS.

**April 07, 2024** \- AWS starts an investigation.

**May 01, 2024** \- AWS updates the documentation of the ALB authentication feature to verify the _signer_ field.

**June 05, 2024** \- AWS confirms they view the case closed.

**June 15, 2024** \- Miggo reports to AWS about incomplete documentation regarding preventive actions that should be defined by Security Groups.  
**July 11, 2024** \- AWS confirms the issue is affecting customers. They are actively monitoring and reaching out to those who are impacted.**  
July 19, 2024** \- AWS updates the documentation of the ALB authentication feature regarding Security Group best practices.  
**August 20, 2024** \- Public disclosure.  
**August 20, 2024** \- Post public disclosure. Since Miggo publicly disclosed ALBeast on August 20, AWS has asserted that it is incorrect to call ALBeast an authentication and authorization bypass of ALB or any other AWS service because the technique relies on a bad actor having access to a misconfigured customer application that does not authenticate requests. 

We agree! That’s why we call it a configuration-based vulnerability. The problem remains that even with the suggested configuration changes that AWS added to the documentation, customers still need to change their code implementation to be protected.  
  
This exemplifies the cracks in the shared responsibility model, which is the “lightning in the cloud” that no one wants to talk about. As part of the shared responsibility model, CSPs must proactively inform their customers of these issues and the required modifications in the application implementation but ultimately rely on customers to act on them. If possible, CSPs should amend their product to minimize the required customer modifications. Just updating the documentation is not enough.  
  
Simply put, if an application uses the ALB authentication feature and does not follow the two new best practices added to the documentation, then it remains vulnerable.  
  
We arrived at the 15,000 instance conservative estimate by scanning all IPv4 addresses in the AWS public range that responded with ALB headers and with an indication that the authentication feature of the ALB was enabled. This scan revealed 15,000 potentially vulnerable unique IP addresses; we assume there are more.

> _“Without Miggo Security, I can’t help but wonder how long ALBeast would have remained undetected. Given the source of this vulnerability and the fact that ALBeast impacted thousands of customers is an industry wake-up call while further highlighting the danger of supply chain vulnerabilities.  
>  
>  We need to be vigilant in understanding and applying good security practices ourselves, but also be realistic that companies like large cloud providers can have flaws that have devastating effects on their customers. Adopting security by design, implementing guardrails against risky configurations, and continuously learning and adapting remain key tenets of defense strategy.  
>  
> In a sea of application security specialists, Miggo has proven capable of supporting these principles while helping to uncover many oversights.”_ **_\- Han Chae, Head of Security at HyperScience_**

We would like to express our appreciation to AWS for their prompt attention to this issue and their swift updates to the documentation following our disclosure. The responsiveness of their security team has been crucial in addressing these vulnerabilities and safeguarding their customers who are using the AWS ALB authentication feature.

Want to learn more? Find more materials about ALBeast, the shared responsibility model and how Miggo can help:

  1. [ALBeast Security Advisory by Miggo Research](/resources/albeast-security-advisory-alb-vulnerability)
  2. [How Miggo Can Help](/resources/adr-mitigates-albeast-aws-alb-vulnerability)

### Let's keep in touch!

Feel free to contact on Twitter: Liad Eliyahu ([@liadeliyahu](https://x.com/liadeliyahu))
  
  
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/Flip.min.js"></script>
  
  <script>
  document.addEventListener("DOMContentLoaded", (event) => {
  gsap.registerPlugin(Flip);
  const state = Flip.getState("");
  const element = document.querySelector("");
  element.classList.toggle("");
  Flip.from(state, {
  duration: 0,
  ease: "none",
  absolute: true,
  });
  });
  </script>
  
  
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/Flip.min.js"></script>
  
  <script>
  document.addEventListener("DOMContentLoaded", (event) => {
  gsap.registerPlugin(Flip);
  const state = Flip.getState("");
  const element = document.querySelector("");
  element.classList.toggle("");
  Flip.from(state, {
  duration: 0,
  ease: "none",
  absolute: true,
  });
  });
  </script>

## Continue Reading

[![The Security Patch that Created a Vulnerability: Miggo Security Releases Detector for CVE-2026-23111 to Catch an Attack Before a Fix](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/6a32a70548ea634f021f64e8_Blog_1200x630_CVE-2026-23111_Press_Release_md.webp)The Security Patch that Created a Vulnerability: Miggo Security Releases Detector for CVE-2026-23111 to Catch an Attack Before a FixResearchA Linux vulnerability introduced by a security fix remained exposed for 2.5 years. Miggo built the first working exploit and detection.Read More](/post/the-security-patch-that-created-a-vulnerability-miggo-security-releases-detector-for-cve-2026-23111-to-catch-an-attack-before-a-fix)

[![The $6M Exposure Gap: Solving the 41-Day WAF Defense Lag](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/6979237fbbd6f169db9eaaf3_1200x630_The%20%246M%20Exposure%20Gap.webp)The $6M Exposure Gap: How Your WAF Can Mitigate Vulnerability Attacks in Your EnvironmentResearchThe React2Shell crisis proved it: traditional WAFs miss 52% of exploits. Discover how to close the $6M exposure gap with AI-native runRead More](/post/the-6m-exposure-gap-how-your-waf-can-mitigate-vulnerability-attacks-in-your-environment)

[![Red Herrings and AI Slop: Debunking React2Shell Misinformation](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/6936d50206ff121c8d3095b4_1200x630_Red%20Herrings%20and%20AI%20Slop.webp)Red Herrings and AI Slop: Debunking React2Shell MisinformationResearchReact2Shell sparked confusion, bad PoCs, and wrong assumptions. Here’s a clear look at what really happened—and what the vulnerability actually is.Read More](/post/red-herrings-and-ai-slop-debunking-react2shell-misinformation)

More from Our Blog

[](/blog "More from Our Blog")

## Continue Reading

No items found.

More from Our Blog

[](/blog "More from Our Blog")

![](https://cdn.prod.website-files.com/67abed9eb85482c7968f46d2/67b40f836628451a28a942d7_pre-footer.png)

## Detect and Respond To Threats Faster.

![Checkmark icon](https://cdn.prod.website-files.com/67abed9eb85482c7968f46d2/68dd1df12b86375680471a68_Check.svg)

POC success = 100% 

![Checkmark icon](https://cdn.prod.website-files.com/67abed9eb85482c7968f46d2/68dd1df12b86375680471a68_Check.svg)

AI services mapped, ~1% exploitable 

![Checkmark icon](https://cdn.prod.website-files.com/67abed9eb85482c7968f46d2/68dd1df12b86375680471a68_Check.svg)

1‑click protection enabled

Book a Demo

[](/book-a-demo "Book a Demo")

[![Miggo Security logo](https://cdn.prod.website-files.com/67abed9eb85482c7968f46d2/67aebd0a506169a16bfa7332_98fabd45c2e31dc8b57720283b3e5125_miggo-logo.svg)](/)

COMPANY

[Careers](https://www.miggo.io/company#join-us)

[About Miggo](https://www.miggo.io/company)

PRODUCT

[Miggo Know](https://www.miggo.io/product/security-observability)

[Miggo Prove](https://www.miggo.io/use-cases/runtime-vulnerability-prioritization)

[Miggo Shield](https://www.miggo.io/product/miggo-waf-copilot)

[Miggo ADR](https://www.miggo.io/why-adr)

SOLUTIONS

[AI Runtime Vulnerability Prioritization](https://www.miggo.io/use-cases/runtime-vulnerability-prioritization)

[1st and 3rd Party Application Protection](https://www.miggo.io/use-cases/1st-and-3rd-party-application-protection)

[Runtime Detection and Response](https://www.miggo.io/use-cases/runtime-attack-detection-and-response)

[Block AI Attacks with Custom WAF Rule](https://www.miggo.io/product/miggo-waf-copilot)

[ Secure AI Applications](https://www.miggo.io/use-cases/secure-ai-applications)

RESOURCES

[React2Shell](https://www.miggo.io/react2shell)

[ Blog](https://www.miggo.io/blog)

[Reports and Webinars](https://www.miggo.io/reports-webinar)

[ News](https://www.miggo.io/news)

[Academy](https://www.miggo.io/academy)

[Predictive Vulnerability Database](https://www.miggo.io/vulnerability-database?__hstc=17958374.d1b1f2a1a1468d5e8f1f8a6be5f7ae39.1751623172052.1759843861245.1759902048032.45&__hssc=17958374.10.1759902048032&__hsfp=2903186342)

Legal

[Terms of Use](https://www.miggo.io/terms-of-use)

[Privacy Policy](https://www.miggo.io/privacy-policy)

© 2026 Miggo Security

[](https://www.youtube.com/@MiggoSecurity)[](https://twitter.com/MiggoSecurity)[](https://www.linkedin.com/company/miggo-security/)

![Cyber 150](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/69d4eb77442f6caa70857daa_Cyber150.png)

![Latio Runtime Innovator](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/69955a4b382917db0e1236ff_IMG_3971.png)

![AICPA SOC](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/694116791f8633179aabb482_68079cc601a43f95fbfc8563_soc.png)

![Latio](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/6942542ad82c14730b4427f6_68ef695ef4211550493d1ae2_Security%20innovator.svg)

![Gartner](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/694253ecc2ba5bb86628b59e_68dcfaa4c576ee1c2905f56e_gartner%20cool%20vendor%20\(1\).png)

![Frost & Sullivan](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/69415bd04607d4764c35ce4a_692da38f4f066237d9982a26_frost_sullivan_badge%20\(2\).png)

![AI Trustworthy Pledge 2025](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/69415b8767405ff8282a77b8_6929881a5486a80d0db9d60e_AI%20Trustworthy%20Pledge%20Badge.png)

![aws](https://cdn.prod.website-files.com/67b77c5d91f2665db9ae6ccd/694116894025f4ed776c373f_69287fe2ebf5fc84983561e8_aws_badge%20\(2\).png)
