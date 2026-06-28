---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-29_getting-secret-key-to-building-custom-burp-extension.md
original_filename: 2022-12-29_getting-secret-key-to-building-custom-burp-extension.md
title: Getting Secret Key to Building Custom Burp Extension
category: documents
detected_topics:
- sqli
- command-injection
- mobile-security
tags:
- imported
- documents
- sqli
- command-injection
- mobile-security
language: en
raw_sha256: 24e0353e96ed76a23eb9e663c5e64941d6600b4b16c7705923cbcaa32e78d97c
text_sha256: 5df5972a83e7e6c1114af1352bd0aac7c91c9a1f2b6d1fdb98749e2e7f205cbe
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Getting Secret Key to Building Custom Burp Extension

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-29_getting-secret-key-to-building-custom-burp-extension.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `24e0353e96ed76a23eb9e663c5e64941d6600b4b16c7705923cbcaa32e78d97c`
- Text SHA256: `5df5972a83e7e6c1114af1352bd0aac7c91c9a1f2b6d1fdb98749e2e7f205cbe`


## Content

---
title: "Getting Secret Key to Building Custom Burp Extension"
url: "https://medium.com/@ashlyn.lau_17206/hooking-secret-key-to-building-custom-burp-extension-c6aeb6fd312a"
authors: ["Ashlyn Lau (@ashlyn_lau)"]
bugs: ["SQL injection"]
publication_date: "2022-12-29"
added_date: "2022-12-30"
source: "pentester.land/writeups.json"
original_index: 1722
scraped_via: "browseros"
---

# Getting Secret Key to Building Custom Burp Extension

Getting Secret Key to Building Custom Burp Extension
Ashlyn L
Follow
4 min read
·
Dec 29, 2022

2

Press enter or click to view image in full size
Signature Validation

Oops, can we just wrap up the testing and proceed to report writing? 🤭 NO!!!

For those who have read my previous “boring” blog about “How I Create Message Signature using Frida Hooking” where it will spill out signed message without full understanding of hashing logic and the secret keys used. Although this is good enough for manual API testing, it may not be time efficient cause is only limited to testing single payload at a time.

This article will take it further to automate the message signing on the fly. This also means that we need to have full understanding of the signing code logic and the secret key used in order to recreate them into Burp plugin. If you ask which approach is better? It really boils down to striking a balance between time, effort and quality in the security testing.

After decompiled and analyzed the testing APK binary, I have full understanding of the message signing logic. In this case, the logic goes like this:

Sort the JSON parameters by Ascending order
Convert the JSON object into one single string
Append the string with the Secret Key
Lastly, MD5 hash it.

Now, the only mystery puzzle is the content of the Secret Key. Without much effort, found a function where I can hook and output the secret key.

getappkey.js:

console.log("Script loaded successfully ");
Java.perform(function () {
  var hook = Java.use("com.game.sdk.app.GlobalConfig");
  hook.getAppKey.implementation = function (){
  var result = this.getAppKey();
  console.log("After result:" + result);
  return result;
  }
});

Its time to spin out the Objection mobile runtime exploration tool and retrieve the Secret Key.

Press enter or click to view image in full size
Hooking Class Method to obtain Secret Key

By and large, the requests that we want to intercept and tamper will be as shown below, the number of parameters varies depending on the API call.

POST /user/<redacted> HTTP/2
Host: target
Charset: UTF-8
Content-Type: application/json
Accept-Language: en
User-Agent: Dalvik/2.1.0 (Linux; U; Android 11; SM-A326B Build/RP1A.200720.012)
Accept-Encoding: gzip, deflate
Content-Length: 108

{"uid":"70616800","appID":"1","sign":"letplugindothework","timestamp":"1671087996"}

I will not go in-depth on how to create a custom Burp extension (probably will put you to sleep if I did). Here, I will only touch on the custom codes when dealing with JSON parameter type.

Get Ashlyn L’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After trial and error, I realised I was not able to use the built-in interface methods to manipulate the parameter values due to the supported parameter types as following:

Press enter or click to view image in full size
JSON Parameter Type Not Supported

Mr Google led me to this URL and from here I have stolen pieces of codes from the various examples to get the job done.

How do I analyze json parameters and update their values?
Takafumi | Last updated: Jan 26, 2021 12:12PM UTC Please tell me about extender. The following process did not work in…

forum.portswigger.net

So basically, we need to replace the entire IHttpRequestResponse request after the request has been modified.

public void processHttpMessage(int toolFlag, boolean messageIsRequest, IHttpRequestResponse messageInfo) throws NoSuchAlgorithmException
{
 Map<String, String> map = new HashMap();
 // only process requests
 if (messageIsRequest) {
  byte reqBytes[] = messageInfo.getRequest();
  IRequestInfo reqInfo = helpers.analyzeRequest(reqBytes);
  String strReqBody = helpers.bytesToString(reqBytes);
 
 [snipped]

 String newRequest = modifyRequest(strReqBody,signed);
 byte[] updatedRequest = checkContentLength(newRequest.getBytes(), helpers);
 messageInfo.setRequest(updatedRequest);
}
}

What left to do is to load the custom Burp extension into Burpsuite. Remember to also load the Logger++ extension so that all your stdout will be showing in the Extension Output tab. This is very useful for troubleshooting your extension.

Press enter or click to view image in full size
Custom Plugin Loaded in Burpsuite

After all it's done, it's time to enjoy the labour of your passion. In this scenario, identified a potential SQL Injection parameter and need the help of SQLMap to automate the detection. With the Burp custom extension, we can re-direct SQLMap requests to Burpsuite where it will intercept the message and replace with a new signature and then submit to server.

python3 sqlmap.py -r onlinequery.req --dbms=mysql --proxy=http://127.0.0.1:8080 --batch
Thanksgiving 2022

I would like to thank all my followers, you are the ones who motivate me to keep writing this blog. Hope I can do a better job in 2023!

Happy New Year! :)
