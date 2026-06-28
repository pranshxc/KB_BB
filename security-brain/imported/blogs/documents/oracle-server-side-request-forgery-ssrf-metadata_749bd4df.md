---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-08_oracle-server-side-request-forgery-ssrf-metadata.md
original_filename: 2022-02-08_oracle-server-side-request-forgery-ssrf-metadata.md
title: Oracle Server Side Request Forgery (SSRF) Metadata
category: documents
detected_topics:
- cloud-security
- ssrf
- api-security
- sso
- idor
- command-injection
tags:
- imported
- documents
- cloud-security
- ssrf
- api-security
- sso
- idor
- command-injection
language: en
raw_sha256: 749bd4dfb8b92ed5fa096697979bc71c993c96cef38ddf36a918b87d4fdf2ab0
text_sha256: 4f61f1b0657ceba7b2f93e1d490d234ccc603e6aae95b01f8f5923b4ad828089
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Oracle Server Side Request Forgery (SSRF) Metadata

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-08_oracle-server-side-request-forgery-ssrf-metadata.md
- Source Type: markdown
- Detected Topics: cloud-security, ssrf, api-security, sso, idor, command-injection
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `749bd4dfb8b92ed5fa096697979bc71c993c96cef38ddf36a918b87d4fdf2ab0`
- Text SHA256: `4f61f1b0657ceba7b2f93e1d490d234ccc603e6aae95b01f8f5923b4ad828089`


## Content

---
title: "Oracle Server Side Request Forgery (SSRF) Metadata"
page_title: "Oracle Server Side Request Forgery (SSRF) | Orca Security"
url: "https://orca.security/resources/blog/oracle-server-side-request-forgery-ssrf-attack-metadata/"
final_url: "https://orca.security/resources/blog/oracle-server-side-request-forgery-ssrf-attack-metadata/"
authors: ["Lidor Ben Shitrit"]
programs: ["Oracle"]
bugs: ["SSRF"]
publication_date: "2022-02-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2921
---

[ Blog Home](https://orca.security/resources/blog/)

  * [ Research Pod ](https://orca.security/resources/category/research-pod/)

![A misconfigured service can play a crucial role in facilitating a Server Side Request Forgery \(SSRF\) attack. Oracle SSRF metadata can help predict it.](https://orca.security/wp-content/uploads/2022/01/ORC03538_Q1-Blog-Graphics_Featured-Tile_Oracle-Cloud-Metadata-SSRF_1978x1176_r1v1.jpg?w=1044)

# Oracle Server Side Request Forgery (SSRF) Metadata

[ ![Avatar of Lidor Ben Shitrit](https://orca.security/wp-content/uploads/2022/01/avatar-lidor-ben.png) Lidor Ben Shitrit  ](https://orca.security/resources/author/lidor-ben-shitrit/)

Published: Feb 08, 2022 

  * [ __](https://twitter.com/share?text=Oracle%20Server%20Side%20Request%20Forgery%20%28SSRF%29%20Metadata&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Foracle-server-side-request-forgery-ssrf-attack-metadata%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Foracle-server-side-request-forgery-ssrf-attack-metadata%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Foracle-server-side-request-forgery-ssrf-attack-metadata%2F)
  * [ __](mailto:?Subject=Oracle Server Side Request Forgery \(SSRF\) Metadata&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Foracle-server-side-request-forgery-ssrf-attack-metadata%2F)

Analyzing customer environments is always a detective task, but seldom do we find structural flaws in a service provider, which — of course — is a cause for real concern. The presence of a Server Side Request Forgery (SSRF) attack vector can most definitely be alarming, as a successful execution can result in an attacker abusing the functionality of a server to read or update internal resources. Below, I describe how I found an instance of SSRF present on Oracle’s server. 

It was just a regular day when I started looking for security weaknesses in Acme services, a new onboarding account. Acme is a podcast hosting company with a very large customer base. Like many companies that work on a large scale, Acme uses the services of **Apiary** to enable its users to manage their favorite podcasts both fast and securely. Acquired by Oracle in early 2017, Apiary provides a toolset for [REST API](https://en.wikipedia.org/wiki/Representational_state_transfer) development, testing, and management. The significance of Apiary being part of Oracle Cloud Services will become apparent.

After a short while of analyzing the customer’s environment and getting a better understanding of how Apiary interacts with the customer’s website, I decided to investigate a bit deeper as API services can be prone to weaknesses, and vulnerable services could affect Orca’s clients as well.

First, I signed up for Acme Services. I was welcomed with the following page:

![](https://orca.security/wp-content/uploads/2022/01/blog_Research-Pod_OracleSSRF-300x122.png)

The above screenshot shows the Apiary REST API page with a template. The left side of the screen should show a list of available endpoints (of course each client will have a list of their own chosen endpoints). Depending on the purpose of the endpoint, each will have a different selected request method (typically GET, POST, or PUT). The middle of the screen should show information regarding each endpoint, and on the right we can see the REST API console with the various options to modify the request such as URI Parameters, Request Headers, and the Request Body. In our case, we will use our test account which we called “SSRFtest” that was created for the demonstration of this Proof of Concept (PoC).

Focusing on the right side of the screen, we are given an example endpoint, which we can only send GET requests to:

https://polls.apiblueprint.org/questions 

From the name of the endpoint, we can assume that sending a GET request will return a list of questions related to polls. I used the UI console to send the request without modifying the parameters. What we should get is a response with an “OK” status code (200) containing the response data or, in our case, a list of questions:

![](https://orca.security/wp-content/uploads/2022/01/blog_Research-Pod_OracleSSRF-Questions-198x300.png)

However, this response was dissatisfying.

I decided to tamper with the request a bit, thinking that maybe I’d get a different output that would lead me down a more interesting path.

To do so, let’s have a look behind the scenes of this GET request and the various parameters the end user (such as myself) is actually sending to the endpoint. Below I use Burpsuite, to help me intercept the various requests I sent to the server:

![](https://orca.security/wp-content/uploads/2022/01/blog_Research-Pod_OracleSSRF-request-300x182.png)

Below is the subsequent response:

![](https://orca.security/wp-content/uploads/2022/01/blog_Research-Pod_OracleSSRF-response-300x167.png)

In the first of the two screenshots above, we notice that the GET request we just sent via the UI is sent via another Apiary endpoint:

https://jsapi.apiary.io/apis/ssrftest/http-transactions/  
  
This means that the various parameters we just sent via the UI are actually sent as a **POST** Request (instead of the GET request shown in the UI).

As for the Response (Figure 4), as expected, we’re given data that we should have access to:

  1. The response StatusCode – “200” which indicates that the request has succeeded.
  2. Similarly to what we received in the UI, the “body” parameter is now populated with the “questions” response (can be seen at the bottom of the response in the above screenshot).

But, wait. Among the response parameters, there’s one that clearly stands out: the url parameter. As we can see in Figure 4, Apiary seems to be creating a mock endpoint (in this case, a randomly generated url).

http://private-anon-c0d9ee8cdd-megaphoneapi.apiary-mock.com/networks/731851fc-9fad-11e6-a338-072240a555ac/podcasts

From my experience, when encountering these types of endpoints (in which the current environment is explicit; i.e., “apiary-mock”) there’s usually more than one environment (i.e., Staging, Development, QA, Testing, Production, etc.). Hence, there are probably a few other types of environments I could attempt to access.

My assumption proved correct: modifying the POST Request “ _destination_ ” parameter to a random string such as “ _test_ ” would yield the following message: “A Destination header can be one of the following: mock, production, live, proxy.”

The modified POST Request: 

![](https://orca.security/wp-content/uploads/2022/01/blog_Research-Pod_OracleSSRF-postrequest-300x159.png)

And the response:

![](https://orca.security/wp-content/uploads/2022/01/blog_Research-Pod_OracleSSRF-post-response-300x157.png)

Ok, so now that we have verified that changing the destination header can result in a different output, my next move is to change the destination of the request. I replaced the original value, which was “/questions,” with “ _https://jsapi.apiary.io”._

Changing the POST request with the above modified parameters yields a response containing the main **Apiary** website, which basically proves that by using the Apiary endpoint, we can retrieve any website we’d like. So eventually, our requests workflow would look something like the following:

  1. Accessing _https://app.apiary.io/ssrftest/_ (Main Website) → 
  2. Send a _GET_ Request to [https://private-amnesiac-8a57a6-ssrftest.apiary-proxy.com/](https://private-amnesiac-8a57a6-ssrftest.apiary-proxy.com/questions) (Mock Endpoint) →
  3. Send a _POST_ Request to _https://jsapi.apiary.io/_ (Intercepted Endpoint via Burpsuite) →
  4. Modifying the URI Parameter and sending a _GET_ Request to _https://jsapi.apiary.io_(or basically any desired endpoint).

Getting to any endpoint is fun and all, but what about trying to access the Instance Metadata endpoint?

Now, before sending a crafted request for retrieving the Instance Metadata, I would like to briefly explain its role in the cloud.

Various cloud providers such as AWS, Microsoft Azure, and Google Cloud use a cloud server meta-data REST interface on _http://169.254.169.254_.

The instance metadata service (IMDS) provides information about a running instance as well as a variety of details about the instance itself, including its attached virtual network interface cards (VNICs), its attached multipath-enabled volume attachments, and any custom metadata that the end user can define. 

By sending requests to the metadata endpoint, we can retrieve different kinds of information.

Now, as mentioned, Apiary is part of Oracle Cloud, which means I probably should look for the specific Oracle Cloud IMDS endpoints. 

Below is the current Oracle Cloud IMDSv2 and IMDSv1 endpoint mapping:

![](https://orca.security/wp-content/uploads/2022/01/blog_Research-Pod_OracleSSRF_endpoint-mapping-195x300.png)

Oracle Cloud is currently running two versions of Instance Metadata Versions:

_http://169.254.169.254/opc/v2/_ and _http://169.254.169.254/opc/v1/__(deprecated)_

Remember: the original _POST_ request contained the following headers:

“ _body”, “destination”, “headers”, “method” and “uri”._

We also know that the “ _destination_ ” header could be modified to be one of the following – _proxy_ , _production_ , _live_ and _mock_. I tried to change the destination header to “ _production_ ” and the “ _uri_ ” to:

_http://169.254.169.254/opc/v1/identity_

![](https://orca.security/wp-content/uploads/2022/01/blog_Research-Pod_OracleSSRF_identity-300x202.png)

And lo and behold we get the following response:

![](https://orca.security/wp-content/uploads/2022/01/blog_Research-Pod_OracleSSRF_identity-response-300x268.png)

We received the “ _identity_ ” data, which contained the value of three main certificates files:

_cert.pem_

_Intermediate.pem_

_key.pem_

All three files are responsible for the 509 certificate-signing process. The next step is to replicate the same process locally, so we can work directly via the Oracle Call Interface (OCI). 

In order for us to leverage the findings above via the CLI, I set up the following:

  1. I’ll set up A local server by using Python’s Flask module. That way, when we send the request to the actual, our local server will fetch all three certificate files via the custom localhost I’ll set in the next step. In that way, we can authenticate via the certificate files as a valid user.
  2. Reset the _localhost_ address to be the same as the IMDSv1 address (_169.254.169.254_) so when sending OCI commands to the server, it will look up the three certificate files on the IMDSv1 server. In order to do so, I use the following command: _sudo /sbin/ifconfig lo0 169.254.169.254 netmask 255.255.255.0 up_

Once my local environment is set, we can now use the OCI CLI to run various commands such as:

_oci –auth instance_principal iam compartment list –compartment-id ocid1.tenancy.oc1..aaaaaaaat6du5rqytqh7vxfxh3fxbij7abcdefghiklmnopqrstuvwxyz_

We can see the three files being grabbed, as expected:

![](https://orca.security/wp-content/uploads/2022/01/blog_Research-Pod_OracleSSRF_commands-300x134.png)

In the above command, we sent a request for the server to list the _compartments_**,** which is a collection of related resources (such as cloud networks, compute instances, or block volumes) that can be accessed only by those groups that have been given permission by an administrator in your organization:

![](https://orca.security/wp-content/uploads/2022/01/blog_Research-Pod_OracleSSRF-compartments-300x197.png)

As shown and as expected, we managed to leverage the certificate files to extract sensitive data of various Oracle environments via the Apiary service, by using SSRF. The above command is just one example of what a remote attacker might be able to perform against the server.

### **Vulnerability Disclosure**

Following the above findings, we decided that we should report this vulnerability to Oracle’s Security Vulnerability Disclosure. We emailed Oracle the findings above with a detailed POC. Oracle thanked us for the effort and recognized it by adding my name in their Oracle Critical Patch Advisory.

![](https://orca.security/wp-content/uploads/2022/01/blog_Research-Pod_OracleSSRF_patch-300x110.png)

### **Summary: Preventing an SSRF Attack**

It seems that a misconfigured service (one that is still being set with the deprecated IMDSv1 endpoint) can play a crucial role in facilitating an SSRF attack, like in the case with **Apiary**.

By misusing the Apiary web service, a remote attacker is able to retrieve very sensitive information from various endpoints (such as _http://169.254.169.254/opc/v1/__identity)_ and use it to gain even more access and sensitive data of other hosts in the same environment.

We also created a CLI Tool to enumerate services in Oracle Cloud Infrastructure that we hope will prove useful. The tool is available both on Github [here](https://github.com/orcasecurity/orca-toolbox/tree/main/oci_enum) and as a Python package on PyPI [here](https://pypi.org/project/oci-enum/0.1.1/).

Stay tuned for the second part of our journey to discover how we used different lateral movement techniques to advance through an Acme Oracle Cloud account!

  * [ __](https://twitter.com/share?text=Oracle%20Server%20Side%20Request%20Forgery%20%28SSRF%29%20Metadata&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Foracle-server-side-request-forgery-ssrf-attack-metadata%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Foracle-server-side-request-forgery-ssrf-attack-metadata%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Foracle-server-side-request-forgery-ssrf-attack-metadata%2F)
  * [ __](mailto:?Subject=Oracle Server Side Request Forgery \(SSRF\) Metadata&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Foracle-server-side-request-forgery-ssrf-attack-metadata%2F)

## Related articles

[ ![Risk-based Vulnerability Management](https://orca.security/wp-content/uploads/2025/02/orca-blog-risk-prioritization-featured.png?w=750) ](/resources/blog/risk-based-vulnerability-management/)

![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-blue.svg) ![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-white.svg)

Product Info

##  [Risk-Based Vulnerability Management for the Cloud: A 2026 Guide](/resources/blog/risk-based-vulnerability-management/ "Risk-Based Vulnerability Management for the Cloud: A 2026 Guide")

Jun 26, 2026 

[ ![Digital illustration of a data center cross-section showing an adversarial path indicated by glowing red arrows originating from a breached, orange-lit server rack and moving laterally toward a secured, cyan-lit server enclosure with a locked terminal.](https://orca.security/wp-content/uploads/2026/06/orca-blog-private-cloud-security-1.png?w=750) ](/resources/blog/private-cloud-security/)

![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-blue.svg) ![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-white.svg)

Cloud Security Learning

##  [Private Cloud Security: Top Risks and Best Practices (2026)](/resources/blog/private-cloud-security/ "Private Cloud Security: Top Risks and Best Practices \(2026\)")

Jun 26, 2026 

[ ![Digital illustration of a central AI microchip on a cloudy background, processing threats from the left—such as a cracked message bubble and a bug icon—and outputting cybersecurity solutions on the right, including prioritized alert windows and a remediation code terminal.](https://orca.security/wp-content/uploads/2026/06/orca-blog-what-is-generative-ai-in-cybersecurity-1.png?w=750) ](/resources/blog/what-is-generative-ai-in-cybersecurity/)

![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-blue.svg) ![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-white.svg)

Cloud Security Learning

##  [What Is Generative AI in Cybersecurity?](/resources/blog/what-is-generative-ai-in-cybersecurity/ "What Is Generative AI in Cybersecurity?")

Jun 25, 2026 

### Stay in the loop

Keep up to date with everything you need to know about cloud security and our latest research

By submitting my email address I agree to the use of my personal data in accordance with Orca Security [ Privacy Policy](https://orca.security/privacy-policy/).
