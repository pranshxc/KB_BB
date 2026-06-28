---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-15_hello-lucee-let-us-hack-apple-again.md
original_filename: 2024-02-15_hello-lucee-let-us-hack-apple-again.md
title: Hello Lucee! Let us hack Apple again?
category: documents
detected_topics:
- command-injection
- supply-chain
- mfa
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- supply-chain
- mfa
- otp
- automation-abuse
- api-security
language: en
raw_sha256: f98a2dbeff3d12be2067230b8223ae682556f17dfb65f96dd47e88ac3796cd7e
text_sha256: 7f8059fab3b01c17a9dde30a0c3432415f9dbfd9b21d104ea2914afe8c20f393
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: false
---

# Hello Lucee! Let us hack Apple again?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-15_hello-lucee-let-us-hack-apple-again.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, mfa, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: False
- Raw SHA256: `f98a2dbeff3d12be2067230b8223ae682556f17dfb65f96dd47e88ac3796cd7e`
- Text SHA256: `7f8059fab3b01c17a9dde30a0c3432415f9dbfd9b21d104ea2914afe8c20f393`


## Content

---
title: "Hello Lucee! Let us hack Apple again?"
page_title: "Hello Lucee! Let us hack Apple again? — ProjectDiscovery Blog"
url: "https://blog.projectdiscovery.io/hello-lucee-let-us-hack-apple-again/"
final_url: "https://projectdiscovery.io/blog/hello-lucee-let-us-hack-apple-again"
authors: ["Harsh Jaiswal (@rootxharsh)", "Rahul Maini (@iamnoooob)"]
programs: ["Apple", "Lucee"]
bugs: ["RCE", "Insecure deserialization", "ColdFusion", "Security code review"]
bounty: "20,000"
publication_date: "2024-02-15"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 428
---

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FBlog%20Header%20Background%20Image.07fydz4trtf5v.png&w=3840&q=75)

[Vulnerability Research](/blog/category/vulnerability-research/1)•

[Nuclei & Templates](/blog/category/nuclei-templates/1)

# Hello Lucee! Let us hack Apple again?

By Harsh Jaiswal & Rahul Maini

February 15, 2024

10 min read

![Hello Lucee! Let us hack Apple again?](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2024%2F02%2FBlog---Apple-1.png&w=828&q=75)

#### Table of Contents

  * Attempt 1 - Request Handling and REST Mappings
  * Attempt 2 - CFML Expression Interpreter, Cookies and Sessions.
  * Attempt 3 - Variable Interpreter, Functions and Mura CMS
  * Vulnerability Detection
  * Applying patch
  * Conclusion

#### Authors

[![Harsh Jaiswal](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2023%2F08%2F1585309233118.jpeg&w=96&q=75)Harsh Jaiswal](/blog/author/harsh/1)[![Rahul Maini](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2023%2F11%2FTKTMQH41W-U04DH0WJJLX-eec5b4b57170-512.jpeg&w=96&q=75)Rahul Maini](/blog/author/rahul/1)

#### Share

[](https://x.com/intent/post?url=)[](https://www.linkedin.com/shareArticle?mini=true&url=)

Last year we conducted an [in-depth analysis of multiple vulnerabilities within Adobe ColdFusion](https://projectdiscovery.io/blog/adobe-coldfusion-rce/), we derived valuable insights, one of which revolved around CFM and CFC handling, parsing and execution. We wondered if there are any other CFML Servers. Does this ring a bell? Allow us to introduce [Lucee](https://github.com/lucee/Lucee). We've previously compromised Lucee's Admin panel, showcasing a [pre-auth Remote Code Execution (RCE) on multiple Apple servers](https://httpvoid.com/Apple-RCE.md) that utilized Lucee as its underlying server. 

Our journey led us through multiple attempts, we will delve into our unsuccessful endeavours and, ultimately, our achievement of RCE on Apple’s production server. Notably, our exploitation extended to potentially compromising Lucee's update server, thereby unveiling a classic supply chain attack to compromise any Lucee installation with malicious updates.

### Attempt 1 - Request Handling and REST Mappings

After checking out Lucee's admin panel in our earlier research, we found that it's pretty locked down. There are only four CFM files you can get access while being unauthenticated, so there's not much room for finding bugs there. We need to dig into how Lucee handles requests. We're looking for specific paths, parameters, headers, and so on, to understand how requests are handled.

After reviewing the web.xml file, We set up the JVM debugger via IntelliJ and added Lucee's source code. We plan to start going through the code by putting a breakpoint at Request::exe(). This way, we can step through the code bit by bit and see how Lucee handles requests.

Java

Copy
  
  
  1public static void exe(PageContext pc, short type, ...) {
  2		try {
  3...
  4
  5  if (type == TYPE_CFML) pc.executeCFML(pc.getHttpServletRequest().getServletPath(), throwExcpetion, true);
  6  else if (type == TYPE_LUCEE) pc.execute(pc.getHttpServletRequest().getServletPath(), throwExcpetion, true);
  7  else pc.executeRest(pc.getHttpServletRequest().getServletPath(), throwExcpetion);
  8		}
  9		finally {
  10...
  11		}
  12	}

Another interesting class that deals with Request and Response in Lucee is `core/src/main/java/lucee/runtime/net/http/ReqRspUtil.java`. In this class, there are functions to work with various aspects of the Request, like setting/getting certain headers, query parameters, and the request body, among other things.

While looking into this class, we noticed a call to JavaConverter.deserialize(). As the name suggests, it is a wrapper on readObject() to handle Java Deserialization.

Java

Copy
  
  
  1public static Object getRequestBody(PageContext pc, boolean deserialized, ...) {
  2
  3		HttpServletRequest req = pc.getHttpServletRequest();
  4
  5		MimeType contentType = getContentType(pc);
  6		...
  7  if(deserialized) {
  8  int format = MimeType.toFormat(contentType, -1);
  9  obj = toObject(pc, data, format, cs, obj);
  10  }
  11		...
  12		return defaultValue;
  13	}
  14
  15public static Object toObject(PageContext pc, byte[] data, int format, ...) {
  16
  17		switch (format) {
  18  ...
  19  case UDF.RETURN_FORMAT_JAVA: //5
  20  try {
  21  return JavaConverter.deserialize(new ByteArrayInputStream(data));
  22  }
  23  catch (Exception pe) {
  24  }
  25  break;
  26		}

It appears that when the request's content/type header is set to`application/java`, we should theoretically end up here, right? Well, we promptly dispatched a `URLDNS` gadget with the required content type. And the result? Drumroll, please... Nothing. Could it be that the `deserialized` condition didn't pass? To investigate, we add a breakpoint on `getRequestbody()` , only to find out that we don't even reach this point.

But why? we traced through the function calls and realized that certain configurations must be in place to satisfy the if/else statements to lead us to the sink. Given the complexity of the stack, let's briefly summarize the key points.

cli

Copy
  
  
  1Request:exe() - Determines the type of request and handles it appropriately.
  2↓
  3PageContextImpl:executeRest() - Looks for Rest mappings and executes the RestRequestListener.
  4↓
  5RestRequestListener() -- Sets the "client" attribute with the value "lucee-rest-1-0" on the request object.
  6↓
  7ComponentPageImpl:callRest() - Examines the "client" attribute; if it's "lucee-rest-1-0", proceeds to execute callRest() followed by _callRest().
  8↓
  9ComponentPageImpl:_callRest() - If the rest mapping involves an argument, invokes ReqRspUtil.getRequestBody with the argument deserialized: true.
  10↓
  11ReqRspUtil.getRequestBody() - If the deserialized argument is true, triggers the toObject() function, which deserializes the request body based on the provided content type.
  12↓
  13toObject() - Java Deserialization on the request body if the content type is "application/java".
  14↓
  15JavaConverter.deserialize() - The final step where the Java Deserialization process occurs.

To reproduce this RCE, a rest mapping with a function that takes at least one argument must be configured. Deploy below Rest mapping.

java

Copy
  
  
  1component restpath="/java"  rest="true" {
  2  remote String function getA(String a) httpmethod="GET" restpath="deser" {
  3  return a;
  4  }
  5}

![](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2024%2F01%2Fimage-1.png&w=3840&q=75)

Surprisingly, we discovered that Lucee's critical update server utilizes a REST endpoint - <https://update.lucee.org/rest/update/provider/echoGet>. This server is pivotal in managing all update requests originating from various Lucee installations.

![](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2024%2F01%2Fimage-2.png&w=3840&q=75)

At the time of finding, this server was vulnerable to our exploit which could have allowed an attacker to compromise the update server, opening the door to a supply chain attack. Acknowledging the severity of the situation, Lucee's maintainers promptly implemented a hotfix to secure their update server, subsequently releasing an updated version of Lucee with the necessary fixes - [CVE-2023-38693](https://dev.lucee.org/t/lucee-critical-security-alert-august-15th-2023-cve-2023-38693/12893).

However, **our finding did not apply to Apple's host** , as they did not expose any REST mappings. Let's try again!

### Attempt 2 - CFML Expression Interpreter, Cookies and Sessions.

After gaining a more in-depth understanding of the codebase, we began selectively examining classes, and one that caught our attention was `CFMLExpressionInterpreter`. The intriguing nature of this class prompted us to delve into its details. Upon reviewing the class, it became evident that when the constructor's boolean argument, limited, is set to `False` (default is `True`), the method `CFMLExpressionInterpreter.interpret(…)` becomes capable of executing CFML expressions. 

Something like CFMLExpressionInterpreter(false).interpret("function(arg)") should let us execute any function of Lucee.

With this insight, we conducted a thorough search within the codebase to identify instances where `CFMLExpressionInterpreter(false)` was initialized, and we discovered several occurrences. One in particular was of interest `StorageScopeCookie` by the name of it seems to be related to cookies.

Java

Copy
  
  
  1public abstract class StorageScopeCookie extends StorageScopeImpl {
  2
  3protected static CFMLExpressionInterpreter evaluator = new CFMLExpressionInterpreter(false);
  4
  5	protected static Struct  _loadData(PageContext pc, String cookieName, int type, String strType, Log log) {
  6		String data = (String) pc.cookieScope().get(cookieName, null);
  7		if (data != null) {
  8  try {
  9  Struct sct = (Struct) evaluator.interpret(pc, data);
  10  ...
  11  }
  12  ...
  13  }
  14  ...
  15  }
  16
  17}

It appears that the `StorageScopeCookie._loadData()` function accepts the cookie name as one of its arguments, retrieves its value from PageContext, and subsequently passes it to interpret().

After a thorough follow of multiple code flows, these three were standing out and seemed like could be called by the Lucee application.

  * sessionInvalidate() -> invalidateUserScope() -> getClientScope() -> ClientCookie.getInstance() -> StorageScopeCookie._loadData(…) 
  * sessionRotate() -> invalidateUserScope() -> getClientScope() -> ClientCookie.getInstance() -> StorageScopeCookie._loadData(…) 
  * PageContext.scope() -> getClientScope() -> ClientCookie.getInstance() -> StorageScopeCookie._loadData(…) 

Java

Copy
  
  
  1public final class ClientCookie extends StorageScopeCookie implements Client {
  2
  3	private static final String TYPE = "CLIENT";
  4
  5	public static Client getInstance(String name, PageContext pc, Log log) {
  6		if (!StringUtil.isEmpty(name)) name = StringUtil.toUpperCase(StringUtil.toVariableName(name));
  7		String cookieName = "CF_" + TYPE + "_" + name;
  8		return new ClientCookie(pc, cookieName, _loadData(pc, cookieName, SCOPE_CLIENT, "client", log));
  9	}
  10}

Upon invoking sessionInvalidate() or sessionRotate(), we successfully accessed ClientCookie.getInstance(), constructing the cookie name as `CF_CLIENT_LUCEE`.

![](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2024%2F01%2Fimage-3.png&w=3840&q=75)

This implies that any application utilizing sessionInvalidate() or sessionRotate() could potentially expose a Remote Code Execution (RCE) vulnerability via the CF_CLIENT_LUCEE cookie. Where, "Lucee" represents the application context name, which might vary depending on the deployed application.

Our initial search within the Lucee codebase for the usage of these functions in any unauthenticated CFM file or Component (CFC) yielded no results. Expanding our investigation to Mura/Masa CMS, also deployed by Apple on their Lucee server, we identified two calls. One of these calls was unauthenticated under the logout action.

Java

Copy
  
  
  1public function logout() output=false {
  2  ...
  3	if ( getBean('configBean').getValue(property='rotateSessions',defaultValue='false') ) {
  4  ...
  5  sessionInvalidate();
  6  ...

Unfortunately, the successful exploitation of this vulnerability depends on the rotateSessions setting being enabled in Mura/Masa, which is, by default, set to false. Consequently, we are unable to trigger this vulnerability on Apple's deployment.

Feeling a tinge of disappointment, we redirected our focus to the `PageContext.scope()` flow. After a thorough debugging session, it became apparent that the cookie name in this scenario would be `CF_CLIENT_`. More crucially, to exploit this code execution, we would need to enable the Client Management setting from the Lucee admin, which is, by default, disabled. Therefore, once again, we find ourselves unable to trigger this vulnerability on Apple's configuration.

![My Disappointment Is Immeasurable And My Day Is Ruined | Know Your Meme](/_next/image?url=https%3A%2F%2Fi.kym-cdn.com%2Fentries%2Ficons%2Foriginal%2F000%2F025%2F543%2Feca.png&w=3840&q=75)

Regardless here's a PoC for the same:

![](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2024%2F01%2Fimage-4.png&w=3840&q=75)

### Attempt 3 - Variable Interpreter, Functions and Mura CMS

After various unsuccessful attempts, an alternative idea struck us. What if we could identify more functions that potentially accept user input as a String and could lead to code execution?

Our attention was drawn to `VariableInterpreter.parse(,,limited)`, which initializes `CFMLExpressionInterpreter(limited)`. It occurred to us that if there are calls to `VariableInterpreter.parse(,,false)`, there might be a way for code execution.

Considering this, We identified some vulnerable sinks in the VariableInterpreter class. If any of the following functions pass user input to parse(), it could serve our purpose:

  * getVariable → VariableInterpreter.parse(,,false)
  * getVariableEL → VariableInterpreter.parse(,,false)
  * getVariableAsCollection → VariableInterpreter.parse(,,false)
  * getVariableReference → VariableInterpreter.parse(,,false)
  * removeVariable → VariableInterpreter.parse(,,false)
  * isDefined → VariableInterpreter.parse(,,false)

To narrow down the search, we investigated classes importing the `VariableInterpreter` class and identified the following suspects:

  * [core/src/main/java/lucee/runtime/PageContextImpl.java](https://github.com/lucee/Lucee/blob/f7b88cc49b908dd61e9dfad6a4e567745408182a/core/src/main/java/lucee/runtime/PageContextImpl.java)
  * [core/src/main/java/lucee/runtime/functions/decision/IsDefined.java#L41](https://github.com/lucee/Lucee/blob/f7b88cc49b908dd61e9dfad6a4e567745408182a/core/src/main/java/lucee/runtime/functions/decision/IsDefined.java)
  * [core/src/main/java/lucee/runtime/functions/struct/StructGet.java#L37](https://github.com/lucee/Lucee/blob/f7b88cc49b908dd61e9dfad6a4e567745408182a/core/src/main/java/lucee/runtime/functions/struct/StructGet.java)
  * [core/src/main/java/lucee/runtime/functions/struct/StructSort.java#L74](https://github.com/lucee/Lucee/blob/f7b88cc49b908dd61e9dfad6a4e567745408182a/core/src/main/java/lucee/runtime/functions/struct/StructSort.java)
  * [core/src/main/java/lucee/runtime/functions/system/Empty.java#L34](https://github.com/lucee/Lucee/blob/f7b88cc49b908dd61e9dfad6a4e567745408182a/core/src/main/java/lucee/runtime/functions/system/Empty.java)
  * [core/src/main/java/lucee/runtime/tag/SaveContent.java#L87](https://github.com/lucee/Lucee/blob/f7b88cc49b908dd61e9dfad6a4e567745408182a/core/src/main/java/lucee/runtime/tag/SaveContent.java)
  * [core/src/main/java/lucee/runtime/tag/Trace.java#L170](https://github.com/lucee/Lucee/blob/f7b88cc49b908dd61e9dfad6a4e567745408182a/core/src/main/java/lucee/runtime/tag/Trace.java)

Given the complexity of PageContextImpl, We chose to initially focus on the other classes. Starting with function classes, We tested `StructGet("abc")` and successfully hit the breakpoint at `VariableInterpreter.parse()`. However, attempting the payload used earlier for `CFMLExpressionInterpreter.interpret()` calls didn't execute `imageRead()`. 

After reviewing `parse()`, We realized that the payload needed to be modified to `x[imageRead('')]` due to the call being made to `CFMLExpressionInterpreter.interpretPart()` after splitting the string from `[` and it worked. `imageRead()` executed. We can call arbitrary functions from `StrucGet("")`.

This led us to conclude that the following functions allow CFML evaluation, allowing Remote Code Execution (RCE) when they contain user input:

  * StructGet("...")
  * isDefined("...")
  * Empty("...")

We did a quick search in Masa/Mura CMS's codebase, where, despite not finding calls for StructGet() and Empty(), we stumbled upon an abundance of calls for isDefined(). (Cue the happy noises!)

Now, the reason for so many calls is that isDefined(String var), is used to check if a given string is defined as a variable or not. Meaning that isDefined(”url.search”) doesn’t mean our query parameter `search`'s value is being passed here. We’d need a call like isDefined(”#url.search#”) which means our given string will be checked if it is defined as variable or not.

After grepping for `isDefined\(._#_ \)` we came across a few calls, most importantly the call in FEED API at [core/mura/client/api/feed/v1/apiUtility.cfc#L122](https://github.com/MasaCMS/MasaCMS/blob/2ef41b22388ce3e625d4248e994e84ddafc12dfe/core/mura/client/api/feed/v1/apiUtility.cfc) and in the JSON API both of which could be triggered pre-auth.

Java

Copy
  
  
  1function processRequest(){
  2	try {
  3		var responseObject=getpagecontext().getresponse();
  4		var params={};
  5		var result="";
  6
  7		getBean('utility').suppressDebugging();
  8
  9		structAppend(params,url);
  10		structAppend(params,form);
  11		structAppend(form,params);
  12		...
  13		if (isDefined('params.method') && isDefined('#params.method#')){
  14  ...
  15		}
  16	}
  17}

The `param` struct is populated from both the`url` and `form` structs, which store GET and POST parameters, respectively. Consequently, the `param` struct contains user input. Performing `isDefined("#param.method#")` poses a risk of Remote Code Execution (RCE), when Mura/Masa CMS is deployed on a Lucee server.

And finally: We perform our code execution on Apple!

![](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2024%2F01%2Fimage-10.png&w=3840&q=75)

These findings were reported to both Apple and the Lucee team. Apple fixed the report within 48 hours while Lucie's team notified us that they are aware of this nature and have already implemented a fix by adding an optional setting within the Admin panel:

![](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2024%2F02%2Fimage.png&w=3840&q=75)

### Vulnerability Detection

The below template could be used to identify If your Lucee instance is vulnerable to a cookie parsing issue that could lead to Remote Code Execution. We've also added detection template into [nuclei-templates](https://github.com/projectdiscovery/nuclei-templates/pull/9148) project.

yaml

Copy
  
  
  1id: lucee-rce
  2
  3info:
  4  name: Lucee < 6.0.1.59 - Remote Code Execution
  5  author: rootxharsh,iamnoooob,pdresearch
  6  severity: critical
  7  metadata:
  8  max-request: 1
  9  shodan-query: http.title:"Lucee"
  10  verified: true
  11  tags: lucee,rce,oast
  12
  13http:
  14  - raw:
  15  - |
  16  GET / HTTP/1.1
  17  Host: {{Hostname}}
  18  Cookie: CF_CLIENT_=render('<cfscript>writeoutput(ToBinary("{{base64('{{randstr}}')}}"))</cfscript>');
  19
  20
  21  matchers:
  22  - type: dsl
  23  dsl:
  24  - contains(body, "{{randstr}}")
  25  - contains(header, "cfid")
  26  - contains(header, "cftoken")
  27  condition: and

### Applying patch

First and foremost, make sure you're using the latest stable release of Lucee. Then apply the below settings within the Lucee admin panel to disable evaluation of these functions:

![](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2024%2F02%2FScreenshot-2024-01-29-at-14.45.00.png&w=3840&q=75)

  
They also implemented a fix for the cookies that were being parsed as CFML expressions.

[limit cookie parsing and add additional env var alias for limit eval… · lucee/Lucee@bd3d2d2…uation![](https://github.githubassets.com/assets/pinned-octocat-093da3e6fa40.svg)GitHublucee![](https://opengraph.githubassets.com/d651165762eac6445f3a5d08ad4b92ea0dbbd5ec834de2eae1411dccf93fc5a5/lucee/Lucee/commit/bd3d2d25625f190a7a3518adcb2bfc7496aff42c)](https://github.com/lucee/Lucee/commit/bd3d2d25625f190a7a3518adcb2bfc7496aff42c)

## Conclusion

Our deep dive into Lucee, an alternative CFML server, yielded insightful results and uncovered critical vulnerabilities. We pinpointed vulnerabilities in Lucee's request handling and REST mappings, exposing a critical Java deserialization flaw. The potential impact was substantial, especially considering the vulnerability's potential exploitation of Lucee's vital update server, which could have facilitated supply chain attacks.

Furthermore, our exploration of Lucee's CFML expression interpretation, cookies, and sessions uncovered vulnerabilities that could lead to remote code execution. Exploiting functions like sessionInvalidate(), sessionRotate(), StructGet() and IsDefined(), we identified pathways to remote code execution, particularly within Mura/Masa CMS, a CMS deployed on top of Lucee by Apple.

Promptly following our responsible disclosure to both Apple and the Lucee team, swift action ensued. Apple responded and implemented a fix within 48 hours, swiftly addressing the reported issues, while Lucee swiftly implemented fixes to shore up the vulnerabilities. This collaborative effort highlights the importance of responsible disclosures and bug bounty programs.

## Related stories

Related stories

[View all](/blog/category/vulnerability-research/1)

[![Nuclei Templates - April 2026](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2026%2F05%2Fapril-month.png&w=828&q=75)](/blog/nuclei-templates-april-2026)

### [Nuclei Templates - April 2026Two releases shipped this cycle - v10.4.2 (April 15) and v10.4.3 (May 5) - delivering deep KEV coverage, a major push into AI/LLM attack surface, fresh Perforce visibility, and broad quality improvements across the template library. 🚀 April Stats Release New Templates CVEs Added First-time Contributors v10.4.2 121 61 15 v10.4.3 105 62 12 Total 226 123 27 * 226 new templates shipped across both releases * 123 CVEs covered, including ~10 actively exploited vulnerabilities ](/blog/nuclei-templates-april-2026)

[![Beyond the Model: Neo Hunts, Exploits, and Proves 22 Zero-Days.](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2026%2F03%2FEveryone-is-finding-vulns.--The-hard-part-is-proving-them.--Blog-Thumbnail-.png&w=828&q=75)](/blog/everyone-is-finding-vulns-the-hard-part-is-proving-them)

### [Beyond the Model: Neo Hunts, Exploits, and Proves 22 Zero-Days.LLMs are a genuine leap forward for vulnerability discovery. Anthropic reported 500+ zero-days from Opus 4.6 and OpenAI's Codex Security discovered 14 CVEs across projects like OpenSSH and GnuTLS. If you've experimented with LLMs for security testing, you've probably been impressed too. The practical reality for a security team deploying AI is messier than the headlines or early POC results suggest. Noise compounds fast. Anthropic brought in external security researchers to help validate the vo](/blog/everyone-is-finding-vulns-the-hard-part-is-proving-them)

[![Inside the benchmark: app architectures, walkthroughs of findings, and what each scanner actually caught](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2026%2F03%2FInside-the-Benchmark--Blog-Thumbnail---Updated-.png&w=828&q=75)](/blog/inside-the-benchmark-pp-architectures-finding-walkthroughs-and-what-each-scanner-actually-caught)

### [Inside the benchmark: app architectures, walkthroughs of findings, and what each scanner actually caughtThis is Part 2 of our vibe coding security benchmark study. In Part 1, we compared how LLM-based security tools like ProjectDiscovery's Neo and Claude Code performed against traditional SAST and DAST scanners on AI-generated code. We found that LLM-based tools like Neo and Claude Code detected many high-value findings that traditional scanners missed. Between Neo and Claude Code, Neo produced more true positives and fewer false positives because it could validate hypotheses against a running app](/blog/inside-the-benchmark-pp-architectures-finding-walkthroughs-and-what-each-scanner-actually-caught)
