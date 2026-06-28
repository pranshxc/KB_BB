---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-11_vulnerabilities-due-to-xml-files-processing-xxe-in-c-applications-in-theory-and-.md
original_filename: 2023-02-11_vulnerabilities-due-to-xml-files-processing-xxe-in-c-applications-in-theory-and-.md
title: 'Vulnerabilities due to XML files processing: XXE in C# applications in theory
  and in practice'
category: documents
detected_topics:
- ssrf
- xss
- sso
- idor
- access-control
- command-injection
tags:
- imported
- documents
- ssrf
- xss
- sso
- idor
- access-control
- command-injection
language: en
raw_sha256: dcb15e9efd321c70f1b4e26b982fb1488727342e80d4cb6e93a3d2efa0afbe33
text_sha256: 8216707a64215b5e68d81b78eecfa6db7d9618cf55edbce19a0c04ebe1087f92
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Vulnerabilities due to XML files processing: XXE in C# applications in theory and in practice

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-11_vulnerabilities-due-to-xml-files-processing-xxe-in-c-applications-in-theory-and-.md
- Source Type: markdown
- Detected Topics: ssrf, xss, sso, idor, access-control, command-injection
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `dcb15e9efd321c70f1b4e26b982fb1488727342e80d4cb6e93a3d2efa0afbe33`
- Text SHA256: `8216707a64215b5e68d81b78eecfa6db7d9618cf55edbce19a0c04ebe1087f92`


## Content

---
title: "Vulnerabilities due to XML files processing: XXE in C# applications in theory and in practice"
url: "https://pvs-studio.com/en/blog/posts/csharp/0918/"
final_url: "https://pvs-studio.com/en/blog/posts/csharp/0918/"
authors: ["Sergey Vasiliev (@_SergVasiliev_)"]
programs: ["BlogEngine.NET"]
bugs: ["XXE"]
publication_date: "2023-02-11"
added_date: "2023-02-26"
source: "pentester.land/writeups.json"
original_index: 1544
---

![Unicorn with delicious cookie](data:,)

Our [website uses cookies](https://pvs-studio.com/en/privacy-policy/) to enhance your browsing experience. 

Accept

![to the top](https://wcdn.pvs-studio.com/static/images/icons/arrows/to_the_top.png)

  * [ Support ](https://pvs-studio.com/en/about-feedback/)
  * En

  * English

  * Français

  * ![User icon](https://wcdn.pvs-studio.com/static/images/icons/user_pa.svg)

  * [Authorization](/login/?next=/en/blog/posts/csharp/0918/)
  * [Registration](/login/?register=true&next=/en/blog/posts/csharp/0918/)

  * ![Search button](https://wcdn.pvs-studio.com/static/images/icons/search.svg)

[ ![PVS-Studio logo: cool unicorn](https://wcdn.pvs-studio.com/static/images/logo/pvs_logo_4.svg) ](https://pvs-studio.com/en/)

  * [ Analyzer](https://pvs-studio.com/en/pvs-studio/) Analyzer

  * [About PVS-Studio](https://pvs-studio.com/en/pvs-studio/)
  * [Download PVS-Studio](https://pvs-studio.com/en/pvs-studio/download/)
  * [What's new in 7.43](https://pvs-studio.com/en/whatsnew/)
  * [FAQ](https://pvs-studio.com/en/pvs-studio/faq/)
  * [SAST (CWE, OWASP, MISRA)](https://pvs-studio.com/en/pvs-studio/sast/)
  * [Online Examples](https://pvs-studio.com/en/pvs-studio/examples/)

  * [ Documentation](https://pvs-studio.com/en/docs/) Documentation

  * [General documentation](https://pvs-studio.com/en/docs/)
  * [Warnings](https://pvs-studio.com/en/docs/warnings/)

  * [ License](https://pvs-studio.com/en/order/) License

  * [Purchase a license](https://pvs-studio.com/en/order/)
  * [Choose a license](https://pvs-studio.com/en/order/license/)
  * [For clients](https://pvs-studio.com/en/for-clients/)
  * [For students](https://pvs-studio.com/en/order/for-students/)
  * [For Open Source](https://pvs-studio.com/en/order/open-source-license/)
  * [For Microsoft MVPs](https://pvs-studio.com/en/order/mvp/)

  * [ Blog](https://pvs-studio.com/en/blog/posts/) Blog

  * [Blog](https://pvs-studio.com/en/blog/posts/)
  * [Video](https://pvs-studio.com/en/blog/video/)
  * [Books](https://pvs-studio.com/en/blog/books/)
  * [Entertainment](https://pvs-studio.com/en/blog/quest/)
  * [Events PVS-Studio](https://pvs-studio.com/en/blog/events/)
  * [Checked projects](https://pvs-studio.com/en/blog/inspections/)
  * [Error examples](https://pvs-studio.com/en/blog/examples/)
  * [Terminology](https://pvs-studio.com/en/blog/terms/)
  * [64-bit Lessons](https://pvs-studio.com/en/blog/lessons/)

  * [ About us](https://pvs-studio.com/en/about/) About us

  * [History](https://pvs-studio.com/en/about/)
  * [Customers](https://pvs-studio.com/en/about/customers/)
  * [Careers](https://pvs-studio.com/en/about/careers/)
  * [Contacts](https://pvs-studio.com/en/address/)

  * [ Book a demonstration ](https://pvs-studio.com/en/pvs-studio/request-demo/)
  * [ Try for free ](https://pvs-studio.com/en/pvs-studio/try-free/)
  * 

  * ####  Analyzer 

  * [About PVS-Studio](https://pvs-studio.com/en/pvs-studio/)
  * [Download PVS-Studio](https://pvs-studio.com/en/pvs-studio/download/)
  * [What's new in 7.43](https://pvs-studio.com/en/whatsnew/)
  * [FAQ](https://pvs-studio.com/en/pvs-studio/faq/)
  * [SAST (CWE, OWASP, MISRA)](https://pvs-studio.com/en/pvs-studio/sast/)
  * [Online Examples](https://pvs-studio.com/en/pvs-studio/examples/)

  * ####  Documentation 

  * [General documentation](https://pvs-studio.com/en/docs/)
  * [Warnings](https://pvs-studio.com/en/docs/warnings/)

  * ####  License 

  * [Purchase a license](https://pvs-studio.com/en/order/)
  * [Choose a license](https://pvs-studio.com/en/order/license/)
  * [For clients](https://pvs-studio.com/en/for-clients/)
  * [For students](https://pvs-studio.com/en/order/for-students/)
  * [For Open Source](https://pvs-studio.com/en/order/open-source-license/)
  * [For Microsoft MVPs](https://pvs-studio.com/en/order/mvp/)

  * ####  Blog 

  * [Blog](https://pvs-studio.com/en/blog/posts/)
  * [Video](https://pvs-studio.com/en/blog/video/)
  * [Books](https://pvs-studio.com/en/blog/books/)
  * [Entertainment](https://pvs-studio.com/en/blog/quest/)
  * [Events PVS-Studio](https://pvs-studio.com/en/blog/events/)
  * [Checked projects](https://pvs-studio.com/en/blog/inspections/)
  * [Error examples](https://pvs-studio.com/en/blog/examples/)
  * [Terminology](https://pvs-studio.com/en/blog/terms/)
  * [64-bit Lessons](https://pvs-studio.com/en/blog/lessons/)

  * ####  About us 

  * [History](https://pvs-studio.com/en/about/)
  * [Customers](https://pvs-studio.com/en/about/customers/)
  * [Careers](https://pvs-studio.com/en/about/careers/)
  * [Contacts](https://pvs-studio.com/en/address/)

  * ####  Personal account 

  * [Authorization](/login/?next=/en/blog/posts/csharp/0918/)
  * [Registration](https://auth.pvs-studio.com/en/register/)

  * ####  Language 

  * English

  * Français

[ Support ](https://pvs-studio.com/en/about-feedback/) [Try for free](https://pvs-studio.com/en/pvs-studio/try-free/)

[Home](https://pvs-studio.com/en/)

>

[Posts](https://pvs-studio.com/en/blog/posts/)

>

[ C# ](https://pvs-studio.com/en/blog/posts/csharp/)

>

Vulnerabilities due to XML files... 

![Sergey Vasiliev](https://wcdn.pvs-studio.com/media/media/content_author/Vasiliev_thm_fix_80x80.png)

[Sergey Vasiliev](https://pvs-studio.com/en/blog/?author=sergey-vasiliev)

Feb 11 2022 

Tags:

[#CSharp](https://pvs-studio.com/en/blog/posts/?tag=CSharp) [#Knowledge](https://pvs-studio.com/en/blog/posts/?tag=Knowledge) [#Security](https://pvs-studio.com/en/blog/posts/?tag=Security)

# Vulnerabilities due to XML files processing: XXE in C# applications in theory and in practice

Feb 11 2022 

Author: [Sergey Vasiliev](https://pvs-studio.com/en/blog/?author=sergey-vasiliev)

  * What is XXE?
  * XXE components in C#
  * Tainted data
  * XML parsers
  * Example of vulnerability in BlogEngine.NET
  * How to protect the code?
  * Conclusion

How can simple XML files processing turn into a security weakness? How can a blog deployed on your machine cause a data leak? Today we'll find answers to these questions, learn what XXE is and how it looks like.

![0918_XXE_BlogEngine/image1.png](https://import.pvs-studio.com/docx/blog/0918_XXE_BlogEngine/image1.png?ver=06-04-2025-11-34-45)

Before we begin, note that there are several types of vulnerabilities related to XML processing. The most popular vulnerabilities are XXE, XEE, and XPath injection. In this article we inspect XXE. If you're interested in the essence of an XEE attack, you can read this article: "[How Visual Studio 2022 ate up 100 GB of memory and what XML bombs had to do with it](/en/blog/posts/csharp/0865/)". We'll get to XPath injection some time later. :)

## What is XXE?

XXE (XML eXternal Entities) is an application security weakness. The possible source of this attack — compromised data processed by an insecurely configured XML parser. This attack can result in disclosure of data from the target machine or server-side request forgery (SSRF).

XML files may contain the document type definition ([DTD](https://en.wikipedia.org/wiki/Document_type_definition)), which describes the structure of an XML file. DTD allows us to define and use XML entities.

It can look like this:
  
  
  <?xml version="1.0" encoding="utf-8" ?>
  <!DOCTYPE order [
    <!ENTITY myEntity "lol">
  ]>
  <order>&myEntity</order>

In this XML, we declare _myEntity_ and use it further — _& myEntity_. In this case, the entity is internal and is defined as literal. If an XML parser expands this entity, it substitutes _& myEntity_ with the actual value — _lol_. Besides, some internal entities can expand through others. XML bombs can be created this way and perform [XEE attacks](/en/blog/terms/6545/).

However, entities can be external. They can refer to some local files or access external resources:
  
  
  <!ENTITY myExternalEntity SYSTEM "https://test.com/target.txt">

Here's an example of an XML file where an external entity refers to a local file:
  
  
  <?xml version="1.0" encoding="utf-8" ?>
  <!DOCTYPE order [
    <!ENTITY myExternalEntity SYSTEM "file:///D:/HelloWorld.cs">
  ]>
  <order>&myExternalEntity</order>

In this case, an XML parser substitutes _myExternalEntity_ with the contents of the file along path _D:/HelloWorld.cs_. If it's properly configured, of course.

XXE attack exploits the feature above. 

Here's an example. Let's assume that there's an application that accepts queries as XML files and processes items with the corresponding ID.

The application works with the following XML file format:
  
  
  <?xml version="1.0" encoding="utf-8" ?>
  <order>
  <itemID>62</itemID>
  </order>

Simplified C# code:
  
  
  static void ProcessItemWithID(XmlReader reader, String pathToXmlFile)
  {
  ....
  while (reader.Read())
    {
      if (reader.Name == "itemID")
      {
       var itemIdStr = reader.ReadElementContentAsString();
        if (long.TryParse(itemIdStr, out var itemIdValue))
        {
         // Process item with the 'itemIdValue' value
          Console.WriteLine(
            $"An item with the '{itemIdValue}' ID was processed.");
        }
        else
        {
         Console.WriteLine($"{itemIdStr} is not valid 'itemID' value.");
        }
      }
    }
  }

The logic is simple:

  * If ID is a number, the application will report that the corresponding item was processed;
  * If ID is not a number, the application will issue an error. 

Thus, for the XML file above, the application will display the following line: 
  
  
  An item with the '62' ID was processed.

If we insert something else in the ID instead of the number ("_Hello world_ ", for example), the application reports an error:
  
  
  "Hello world" is not valid 'itemID' value.

If an XML parser (_reader_) processes external entities, this is a security flaw. Below is an XML file that can be used to compromise the application:
  
  
  <?xml version="1.0" encoding="utf-8" ?>
  <!DOCTYPE order [
  <!ENTITY xxe SYSTEM "file:///D:/MySecrets.txt">
  ]>
  <order>
  <itemID>&xxe</itemID>
  </order>

The _xxe_ external entity is declared in this file. When an XML parser process this file, it substitutes _& xxe_ with the contents of the file along path _D:/MySecrets.txt_. For example, _"This is an XXE attack target."_. As a result, the application will display the following: 
  
  
  "This is an XXE attack target." is not valid 'itemID' value.

Thus, an application will be vulnerable to XXE attacks, if:

  * a developer configured an XML parser in such a way that it insecurely processes external entities;
  * an attacker can directly/indirectly pass compromised data to the parser.

If an attacker can obtain the value of the entity, they can get the file contents from the compromised device. This is already dangerous. Besides, an attacker can get more data about the system as a whole and find other security weaknesses.

XXE can also lead to an SSRF attack. The hacker may not have access to some resources (access restricted for external users), but the exploited application may have it. Since XXE allows to make requests over the network, a compromised application is a breach in the resource protection. 

Speaking about the importance and danger of XXE — this security weakness is often mentioned in various standards, tops, and enumerations.

**CWE**

The Common Weakness Enumeration has a separate entry for XXE: [CWE-611: Improper Restriction of XML External Entity Reference](https://cwe.mitre.org/data/definitions/611.html).

**CWE Top 25**

Every year 25 most common and dangerous weaknesses are selected from the CWE list to compile the [CWE Top 25](https://cwe.mitre.org/top25/archive/2021/2021_cwe_top25.html). 

In 2021, XXE lost 4 positions compared to 2020, but remained in the top on the 23d place.

**OWASP ASVS**

[OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) __(Application Security Verification Standard)__ contains requirements for secure development. It also has an entry about XXE: _OWASP ASVS 4.0.3 (ID 5.5.2): Verify that the application correctly restricts XML parsers to only use the most restrictive configuration possible and to ensure that unsafe features such as resolving external entities are disabled to prevent XML eXternal Entity (XXE) attacks_.

**OWASP Top 10**

The OWASP Top 10 2017 had a separate category for XXE: [A4:2017-XML External Entities (XXE)](https://owasp.org/www-project-top-ten/2017/A4_2017-XML_External_Entities_\(XXE\)). In the OWASP Top 10 2021 a separate category for XXE was eliminated. XXE now belongs to [A05:2021-Security Misconfiguration](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/).

![0918_XXE_BlogEngine/image2.png](https://import.pvs-studio.com/docx/blog/0918_XXE_BlogEngine/image2.png?ver=06-04-2025-11-34-45)

## XXE components in C#

As I mentioned above, XXE needs at least two components: an insecurely configured parser and data from the attacker that this parser processes.

### Tainted data

Everything is quite simple here. The application has several places where it accepts external data. It has to be processed carefully — not all people use an application for its intended purpose.

Such application places are console application arguments, various form fields, query data, etc. The first thing that comes to mind is console input.
  
  
  var taintedVar = Console.ReadLine();

We don't know what's inside _taintedVar_. This variable can contain data in the expected format or a string to compromise the system. We can't trust it.

You can read more about it in the "Taint sources" section of "[OWASP, vulnerabilities, and taint analysis in PVS-Studio for C#. Stir, but don't shake](/en/blog/posts/csharp/0831/). You should also be suspicious of public access parameters. The data in those methods may be safe or not. You can read about it [here](/en/blog/posts/csharp/0835/).

### XML parsers

An XML parser is vulnerable to XXE, if:

  * it processes DTD;
  * it uses insecure _XmlResolver_.

If an XML parser does not set a limit on the entities' maximum size (or the size is large), this may worsen the attack, since the attacker will be able to extract larger amounts of data.

#### Configuring the parser

The desired behavior is set with the following properties: 

  * _ProhibitDtd_ ;
  * _DtdProcessing_ ;
  * _XmlResolver_ ;
  * _MaxCharactersFromEntities_. 

Some XML parsers have all these options, others — don't. Their semantic meaning does not change from type to type.

**ProhibitDtd**

The _ProhibitDtd_ property has the _Obsolete_ attribute. Now the _DtdProcessing_ property is used instead of _ProhibitDtd_. Still, it can be used in the old code. The _true_ value prohibits DTD processing, _false_ — allows it.

**DtdProcessing**

The _DtdProcessing_ property __ has the _System.Xml.DtdProcessing_ type __ and can take the _Prohibit_ , _Ignore_ and _Parse_ values:

  * _Prohibit_ — prohibits DTD processing. If the parser meets DTD when processing an XML file, an exception of the _XmlException_ type is thrown.
  * _Ignore_ — the parser just skips DTD.
  * _Parse_ — the parser processes DTD.

You probably have a question now, and I'll answer it. If the _ProhibitDtd_ and _DtdProcessing_ properties occur together in code (for example, in _XmlReaderSettings_), they are related to each other. So, if you prohibit DTD in one property and allow in another, only the last option set would be applied. :)

**XmlResolver**

The _XmlResolver_ property is responsible for the object used to process external entities. The safest option — absence of resolver at all (_null_ value). In this case, even if DTD processing is enabled, external entities won't expand.

**MaxCharactersFromEntities**

Another option of interest for us. _MaxCharactersFromEntities_ is responsible for the maximum allowable size of entities. The bigger the value, the potentially more information will be extracted during an XXE attack.

#### XML parser types

The most common standard types to work with XML are _XmlReader_ , _XmlTextReader_ , _XmlDocument_. Note that the list is not limited to them.

Once again, the configuration of a parser is dangerous, if:

  * this parser processes DTD;
  * it has a dangerous resolver (for example, _XmlUrlResolver_ in its default state).

**XmlReader**

The _XmlReaderSettings_ object, created explicitly or implicitly, configures behavior of the _XmlReader_. The _XmlReaderSettings_ type has all the settings listed earlier.

A parser with a dangerous configuration may look like this:
  
  
  var settings = new XmlReaderSettings()
  {
  DtdProcessing = DtdProcessing.Parse,
  XmlResolver = new XmlUrlResolver(),
  MaxCharactersFromEntities = 0
  };
  
  using (var xmlReader = XmlReader.Create(xmlFileStringReader, settings))
  ....

Here the developer explicitly allowed DTD processing, set a resolver for external entities, and removed the limitations on their size.

**XmlTextReader**

In this case, we are dealing with the same properties: _ProhibitDtd_ , _DtdProcessing_ , _XmlResolver_.

An example of a dangerously configurated parser:
  
  
  using (var xmlTextReader = new XmlTextReader(xmlFileStringReader))
  {
  xmlTextReader.XmlResolver = new XmlUrlResolver();
  xmlTextReader.DtdProcessing = DtdProcessing.Parse;
  ....
  }

**XmlDocument**

In the _XmlDocument_ type, we are interested in the _XmlResolver_ property. In this case, a dangerously configurated parser can look like this:
  
  
  XmlDocument xmlDoc = new XmlDocument();
  xmlDoc.XmlResolver = new XmlUrlResolver();

_xmlDoc_ in this configuration expands external entities and can be considered dangerous.

#### Default parser settings

Above we looked at examples where XML parsers were configured explicitly. However, all the listed types have some default settings, and there's a couple of interesting things about them.

Firstly, these settings are different for different .NET versions.

Secondly, the settings vary from type to type. For example, the DTD processing can be enabled or disabled by default.

In some cases, an XML parser can have a dangerous configuration by default, even if dangerous settings were not set explicitly.

As a result, we have to remember different types of parsers, different default settings in different types and .NET versions. It's a good amount of information that can be difficult to keep in mind (especially at first).

So, sometimes we can't say if an XML parser is XXE-resistant by only looking at code. For example, here:
  
  
  XmlDocument doc = new XmlDocument();
  doc.Load(xmlReader);

It's unclear whether _doc_ can process external entities or not — we need to know the framework version first.

The values of the 'dangerous' settings changed between .NET Framework 4.5.1 and .NET Framework 4.5.2. Below is the table that shows in which .NET versions parsers with default settings are XXE-resistant by default, and in which they're not.

Instances of types |  .NET Framework 4.5.1 and lower |  .NET Framework 4.5.2 and higher (including .NET Core and .NET)  
---|---|---  
XmlReader (XmlReaderSettings) |  Safe |  Safe  
XmlTextReader |  Vulnerable |  Safe  
XmlDocument |  Vulnerable |  Safe  
  
Yes, _XmlReader_ (created via _XmlReaderSettings_) is safe in .NET Framework 4.5.1 and lower because DTD processing is disabled in it.

Even though in the new framework versions parsers are configured securely by default, the best option is to explicitly configure the necessary settings. Yes, there'll be a lot more code. At the same time, it'll be more obvious and stable when you port it between different .NET Framework versions.

Done with the theory. Next let's look at the real vulnerability. Make yourself a cup of coffee and let's go!

## Example of vulnerability in BlogEngine.NET

Above, we analyzed the theoretical component of XXE, talked a little more specifically about these security weaknesses in .NET, looked at what the insecure components of the vulnerability look like from the point of view of the code. Now it's time for practice. BlogEngine.NET is here to help.

![0918_XXE_BlogEngine/image3.png](https://import.pvs-studio.com/docx/blog/0918_XXE_BlogEngine/image3.png?ver=06-04-2025-11-34-45)

Description from the project's __[website](https://blogengine.io/):_BlogEngine is an open source blogging platform since 2007. Easily customizable. Many free built-in Themes, Widgets, and Plugins._

The project's source code is [available on GitHub](https://github.com/BlogEngine/BlogEngine.NET). 

For us, this project is interesting because 3 XXE vulnerabilities were found there. They were fixed in BlogEngine.NET [v3.3.8.0](https://github.com/BlogEngine/BlogEngine.NET/tree/v3.3.8.0). This means we'll take the previous version for the experiment – [v3.3.7.0](https://github.com/BlogEngine/BlogEngine.NET/tree/v3.3.7.0). If you want, you can easily reproduce the described steps and see the real XXE yourself.

First, we download the desired version — [v3.3.7.0](https://github.com/BlogEngine/BlogEngine.NET/tree/v3.3.7.0). There should be no problems with building the project — it's very simple. I built the project with Visual Studio 2022. 

After the project is built, we run it. If everything is successful, we'll see the site of the following type:

![0918_XXE_BlogEngine/image4.png](https://import.pvs-studio.com/docx/blog/0918_XXE_BlogEngine/image4.png?ver=06-04-2025-11-34-45)

If the website is not available for other machines on the same network by default, I highly recommend you make it. A bit of configuring makes 'playing' with XXE more interesting.

When searching for vulnerabilities, you may have different inputs. For example, the system may represent a black box for you. Then you'll have to collect information about the system, search for influence points on it, and so on. If the system represents a white box, it changes the approach and the tools used to achieve the goal (or at least expands their list).

Here's an interesting thing about open-source projects. Seems like every person can work with the code and contribute to its quality / security. However, there are some [drawbacks](/en/blog/posts/cpp/0900/). On the other hand, hackers would have more ways to investigate the code — since they have access to the sources, they will easily find vulnerabilities. Would these vulnerabilities be reported?

There's no answer to this question. Let's get back to our business.

Since the project is open-source, we'll take advantage of this. To search for vulnerabilities, in addition to our own knowledge, we use [PVS-Studio](/en/pvs-studio/) — a solution that searches for errors and security weaknesses. We need a group of security-related diagnostics — OWASP. You can read about turning on the corresponding warnings [here](/en/docs/manual/6536/).

In Visual Studio you need to set "Show All" for the OWASP group on the "Detectable Errors (C#)" tab: Extensions > PVS-Studio > Options > Detectable Errors (C#).

![0918_XXE_BlogEngine/image5.png](https://import.pvs-studio.com/docx/blog/0918_XXE_BlogEngine/image5.png?ver=06-04-2025-11-34-45)

After that make sure that you enabled the display of the corresponding warnings. In this case we're interested in the 'OWASP' group of the 'High' certainty level. Thus, you need to click on the necessary buttons — they'll be framed.

![0918_XXE_BlogEngine/image6.png](https://import.pvs-studio.com/docx/blog/0918_XXE_BlogEngine/image6.png?ver=06-04-2025-11-34-45)

Then, run the solution analysis (Extensions > PVS-Studio > Check > Solution) and wait for the results.

With the CWE filter (remember that XXE corresponds to CWE-611) or OWASP ASVS ID (OWASP ASVS 5.5.2) it is easy to find what we are interested in – 3 warnings [V5614](/en/docs/warnings/v5614/).

![0918_XXE_BlogEngine/image7.png](https://import.pvs-studio.com/docx/blog/0918_XXE_BlogEngine/image7.png?ver=06-04-2025-11-34-45)

From the point of view of code, these errors are similar. We will analyze the most interesting one (located in several methods), and for the rest I will just provide basic information.

**XMLRPCRequest.cs**

Warning: V5614 [CWE-611, OWASP-5.5.2] Potential XXE vulnerability inside method. Insecure XML parser is used to process potentially tainted data from the first argument: 'inputXml'. BlogEngine.Core XMLRPCRequest.cs 41

In fact, the analyzer points at 3 lines to make the warning more understandable: a 'dangerous' method call, taint source, and a place where the tainted data is used by a dangerously configured parser.
  
  
  public XMLRPCRequest(HttpContext input)
  {
  var inputXml = ParseRequest(input);
  
  // LogMetaWeblogCall(inputXml);
  this.LoadXmlRequest(inputXml); // Loads Method Call 
  // and Associated Variables
  }

According to the message, _inputXml_ may contain tainted data (see [taint checking](/en/blog/terms/6496/)) which is used by an insecurely configured parser inside the _LoadXmlRequest_ method. Thus, it's a rather complex interprocedural case: data comes from one method (_ParseRequest_) and then is passed to another (_LoadXmlRequest_) where it's used.

Let's start with data — we need the _ParseRequest_ method's code.
  
  
  private static string ParseRequest(HttpContext context)
  {
  var buffer = new byte[context.Request.InputStream.Length];
  
  context.Request.InputStream.Position = 0;
  context.Request.InputStream.Read(buffer, 0, buffer.Length);
  
  return Encoding.UTF8.GetString(buffer);
  }

Let's accompany the code with the taint distribution route, to make clear what we're talking about.

![0918_XXE_BlogEngine/image8.png](https://import.pvs-studio.com/docx/blog/0918_XXE_BlogEngine/image8.png?ver=06-04-2025-11-34-45)

It all starts with the _context.Request_ property that has the _HttpRequest_ type. The analyzer considers it a taint source, since data received as a query may be compromised.

There are several ways to extract the data and working with a stream (the _InputStream_ property) is one of them. Thus, the tainted data is passed to _InputStream_

Next, we call the _System.IO.Stream.Read_ method for this stream. This method reads data from _InputStream_ into the byte array (_buffer)_. As a result, now _buffer_ can also contain tainted data. 

After that the _Encoding.UTF8.GetString_ method is called. It constructs a string from the byte array (_buffer)_. Since the source data for creating a string is tainted, the string is also tainted. After the construction, the string returns from the method.

So, the attackers may compromise the value returned by the _ParseRequest_ method. At least in theory. 

Let's go back to the original method:
  
  
  public XMLRPCRequest(HttpContext input)
  {
  var inputXml = ParseRequest(input);
  
  // LogMetaWeblogCall(inputXml);
  this.LoadXmlRequest(inputXml); // Loads Method Call 
  // and Associated Variables
  }

Done with _ParseRequest_. Suppose that the _inputXml_ variable can contain tainted data. Next step — analyze the _LoadXmlRequest_ method that takes _inputXml_ as an argument.

The method is long (100+ lines), so here's the shortened version. The fragment that triggered the analyzer is marked.
  
  
  private void LoadXmlRequest(string xml)
  {
  var request = new XmlDocument();
  try
  {
  if (!(xml.StartsWith("<?xml") || xml.StartsWith("<method")))
  {
  xml = xml.Substring(xml.IndexOf("<?xml"));
  }
  
  request.LoadXml(xml);  // <=
  }
  catch (Exception ex)
  {
  throw new MetaWeblogException("01", 
  $"Invalid XMLRPC Request. ({ex.Message})");
  }
  ....
  }

As we see, the argument is processed by an XML parser: _request.LoadXml(xml)_. PVS-Studio thinks that _request_ is vulnerable to XXE. Our job is to prove it. Or refute. Then this warning will be marked as [false positive](/en/blog/terms/6461/). Here we need the theory described in the beginning of this article.

The object type that the _request_ reference points to is _XmlDocument_. The parser has default settings, which means we need to find out the .NET version. You can find it in the project's properties.

![0918_XXE_BlogEngine/image9.png](https://import.pvs-studio.com/docx/blog/0918_XXE_BlogEngine/image9.png?ver=06-04-2025-11-34-45)

Now let's look at the table at the beginning of the article. We see that in applications on .NET Framework 4.5.1 and lower instances of the _XmlDocument_ type are vulnerable to XXE by default.

It looks like we got all conditions for potential XXE: 

  * there's data that can be compromised: _ParseRequest_ -> _inputXml_ -> _xml_ ;
  * there's a parser with a dangerous configuration that works with this data: _request.LoadXml(xml)_.

Theoretically, this is an XXE, but it's still a [potential vulnerability](/en/blog/terms/6441/). We have to prove that the attack is possible. To do this we need to dig into the code a bit more.

We started our analysis with the constructor of the _XMLRPCRequest_ type. It's called in one place:
  
  
  internal class MetaWeblogHandler : IHttpHandler
  {
  ....
  public void ProcessRequest(HttpContext context)
  {
  try
  {
  var rootUrl = Utils.AbsoluteWebRoot.ToString();
  
  // context.Request.Url.ToString().Substring(0,  
  // context.Request.Url.ToString().IndexOf("metaweblog.axd"));
  
  var input = new XMLRPCRequest(context); // <=
  ....
  }
  ....
  }
  ....
  }

Yeah, we came across an HTTP handler. Here's an entry for it in the config:
  
  
  <add name="MetaWeblog" 
  verb="*" 
  path="metaweblog.axd" 
  type="BlogEngine.Core.API.MetaWeblog.MetaWeblogHandler, BlogEngine.Core" 
  resourceType="Unspecified" 
  requireAccess="Script" 
  preCondition="integratedMode" />

Now we know the address to send a request to and make the desired handler work. Let's try to reproduce the attack. 

First, we need an XML file with which we'll steal data from the machine where the blog is deployed:
  
  
  <?xml version="1.0"?>
  <!DOCTYPE xxe [
   <!ENTITY externalEntity SYSTEM 
     "file:///C:/Windows/System32/drivers/etc/hosts">
  ]>
  <xxe>&externalEntity</xxe>

If an XML parser processes external entities, then instead of &_externalEntity;_ it should paste the contents of the [hosts](https://en.wikipedia.org/wiki/Hosts_\(file\)) file.

We make a request, send XML, and see how our handler will work. For convenience, it makes sense to save XML to a file (in this example - _xxe.xml_), so, if necessary, you can easily change its contents without changing the query command itself.
  
  
  curl -d "@xxe.xml" -X POST http://vasiliev-pc:8081/metaweblog.axd

So, the handler caught our request and called the _XMLRPCRequest_ constructor, which we inspected earlier.

![0918_XXE_BlogEngine/image10.png](https://import.pvs-studio.com/docx/blog/0918_XXE_BlogEngine/image10.png?ver=06-04-2025-11-34-45)

Go inside the constructor and check the data in the _inputXml_ variable.

![0918_XXE_BlogEngine/image11.png](https://import.pvs-studio.com/docx/blog/0918_XXE_BlogEngine/image11.png?ver=06-04-2025-11-34-45)

Everything goes according to plan — the data is tainted, as we assumed (and wanted), and is passed to the _LoadXmlRequest_ method as an argument. Let's observe further.

![0918_XXE_BlogEngine/image12.png](https://import.pvs-studio.com/docx/blog/0918_XXE_BlogEngine/image12.png?ver=06-04-2025-11-34-45)

Due to the dangerous default settings, the parser worked exactly as we expected – it loaded the contents of the hosts file. Then the following code fragment is executed:
  
  
  // Method name is always first
  if (request.DocumentElement != null)
  {
  this.MethodName = request.DocumentElement.ChildNodes[0].InnerText;
  }

Luckily (for the hacker :)) the contents of the hosts file will be written to the _MethodName_ property — exactly what we need. The next code fragment we need is large _switch_ , where certain actions are performed depending on the method name:
  
  
  switch (this.MethodName)
  {
  case "metaWeblog.newPost":
  ....
  break;
  case "metaWeblog.editPost":
  ....
  break;
  case "metaWeblog.getPost":
  ....
  break;
  ....
  default:
  throw new MetaWeblogException("02", $"Unknown Method. ({MethodName})");
  }

Here we need the _default_ branch to where execution will go since there's no suitable method. In this branch an exception is thrown. The exception's message will have the name of the method for which the mapping failed. In our case, the method's name is the contents of the hosts file.

When an exception is thrown, we return to the handler and get to the catch section where an unknown method is reported:

![0918_XXE_BlogEngine/image13.png](https://import.pvs-studio.com/docx/blog/0918_XXE_BlogEngine/image13.png?ver=06-04-2025-11-34-45)

As a result, to our initial request:
  
  
  curl -d "@xxe.xml" -X POST http://vasiliev-pc:8081/metaweblog.axd

We get the following answer:

![0918_XXE_BlogEngine/image14.png](https://import.pvs-studio.com/docx/blog/0918_XXE_BlogEngine/image14.png?ver=06-04-2025-11-34-45)

So, we managed to obtain the contents of the hosts file, using an XXE attack. We got it on the machine with a deployed blog. If we know the location of other files, we can try to get their contents as well. And not only from the attacked machine, but also from other machines of the network to which we have access. Here, in the context of network requests, we can also talk about SSRF.

So, we have just seen XXE both from the point of view of the application (code) and from the point of view of the user (attacker). This is a real vulnerability – [CVE-2018-14485](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-14485) ([here](https://nvd.nist.gov/vuln/detail/CVE-2018-14485) is the entry in the NVD). 

What should we do with vulnerabilities? That's right, fix it. The commit can be found [here](https://github.com/BlogEngine/BlogEngine.NET/commit/3c61785f6c952e3f8d16eab1bb425e0368ea4a65). After that, the XML parser's configuration was changed, so now it can't process external entities. To do this, it is enough to set the value of the _XmlResolver_ property to _null_ :
  
  
  var request = new XmlDocument() { XmlResolver = null };

Now if we try to get the same hosts file, it won't get into the output.

![0918_XXE_BlogEngine/image15.png](https://import.pvs-studio.com/docx/blog/0918_XXE_BlogEngine/image15.png?ver=06-04-2025-11-34-45)

By the way, PVS-Studio knows that the parser with this configuration (_XmlResolver_ – _null_) won't process external entities. Thus, the analyzer won't issue a warning for the fixed code.

Two other warnings that we've seen before also point to vulnerabilities. We are not going to analyze them (the code is similar), but below is basic information about them.

**CVE-2019-10718**

  * Warning: V5614 [CWE-611, OWASP-5.5.2] Potential XXE vulnerability. Insecure XML parser 'doc' is used to process potentially tainted data from the 'xml' variable. PingbackHandler.cs 341
  * Additional information: [NVD](https://nvd.nist.gov/vuln/detail/CVE-2019-10718), [CVE](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-10718). 
  * Commit with a fix: [link](https://github.com/BlogEngine/BlogEngine.NET/commit/3c61785f6c952e3f8d16eab1bb425e0368ea4a65).

**CVE-2019-11392**

  * Warning: V5614 [CWE-611, OWASP-5.5.2] Potential XXE vulnerability. Insecure XML parser 'doc' is used to process potentially tainted data from the 'stream' variable. SyndicationHandler.cs 191
  * Additional information: [NVD](https://nvd.nist.gov/vuln/detail/CVE-2019-11392), [CVE](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11392). 
  * Commit with a fix: [link](https://github.com/BlogEngine/BlogEngine.NET/commit/4869ca9582c6d8f104190c3df3f14fb51058b481).

## How to protect the code?

  * Know about the problem. The fact that vulnerabilities may appear due to the processing of XML files may be an unexpected discovery. The more people know about the problem, the better.
  * Use newer framework versions. Developers strive to improve safety of products 'out of the box'. In the case of .NET, new versions of the framework are more secure.
  * Explicitly configure secure settings for XML parsers. Prohibit the processing of DTDs and external entities if they are not needed. This minimizes the possible risk (in particular, when you copy the code), and also more clearly indicates your intentions. If you need DTD processing, set as many restrictions as possible.
  * Use specialized tools to search for security defects: SAST, DAST, etc. For example, using SAST solutions on a regular basis will allow you to find such defects even at the stage of writing code. By the way, you can try PVS-Studio, mentioned in the article, [here](/en/pvs-studio/try-free/).

## Conclusion

Now you are a little more savvy in security and XXE issues, and also know that even a simple blog deployed on your machine can become a source of vulnerabilities.

In fact, the XXE theme is more serious and, of course, there is still a lot to dig into. But at least just knowing about this security flaw and understanding it at a basic level will already be useful.

Praemonitus, praemunitus.

As always, I invite you to [subscribe to my Twitter](https://twitter.com/_SergVasiliev_) so as not to miss anything interesting.

[#CSharp](https://pvs-studio.com/en/blog/posts/?tag=CSharp) [#Knowledge](https://pvs-studio.com/en/blog/posts/?tag=Knowledge) [#Security](https://pvs-studio.com/en/blog/posts/?tag=Security)

![blog-subscribe](https://wcdn.pvs-studio.com/static/images/icons/blog_bell.svg) ![blog-subscribe](https://wcdn.pvs-studio.com/static/images/icons/blog_bell_active.svg)

![blog-favorite](https://wcdn.pvs-studio.com/static/images/icons/blog_star.svg) ![blog-favorite](https://wcdn.pvs-studio.com/static/images/icons/blog_star_active.svg)

0

0

0

0

[ SHARE  ](https://www.reddit.com/r/programming/submit?url=https://pvs-studio.com%2Fen%2Fblog%2Fposts%2Fcsharp%2F0918%2F&title=Vulnerabilities due to XML files processing: XXE in C# applications in theory and in practice)

Tags:

[#CSharp](https://pvs-studio.com/en/blog/posts/?tag=CSharp) [#Knowledge](https://pvs-studio.com/en/blog/posts/?tag=Knowledge) [#Security](https://pvs-studio.com/en/blog/posts/?tag=Security)

Subscribe to the newsletter

Want to receive a monthly digest of the most interesting articles and news? Subscribe! 

By clicking this button you agree to our [Privacy Policy](https://pvs-studio.com/en/privacy-policy/) statement 

Popular related articles 

  * [ Under the hood of SAST: how code analysis tools look for security flaws  Date: Jan 26 2023  Author: Sergey Vasiliev Here we'll discuss how SAST solutions find security flaws. I'll tell you about different and complementary approaches to detecting potential vulnerabilities, explain why each of them is necessary...  ](https://pvs-studio.com/en/blog/posts/cpp/1028/)
  * [ Catastrophic backtracking: how can a regular expression cause a ReDoS vulnerability?  Date: Nov 03 2022  Author: Andrey Moskalev Regular expressions come in handy when you need to search for and replace text. However, in some cases, they may cause the system to slow down or even make vulnerable to ReDoS attacks.  ](https://pvs-studio.com/en/blog/posts/csharp/1007/)
  * [ Trojan Source: Invisible Vulnerabilities  Date: Apr 15 2022  Author: Guest We present a new type of attack in which source code is maliciously encoded so that it appears different to a compiler and to the human eye. This attack exploits subtleties in text-encoding standards…  ](https://pvs-studio.com/en/blog/posts/cpp/0935/)
  * [ XSS: attack, defense - and C# programming  Date: Aug 24 2021  Author: Valery Komarov XSS - or cross-site scripting - is one of the most common vulnerabilities in web applications. It has been on the OWASP Top 10 list (the list of the most critical security risks to web applications...  ](https://pvs-studio.com/en/blog/posts/csharp/0857/)
  * [ .NET Digest #1  Date: Jul 05 2024  Author: Artem Rovenskii Welcome to our first news and event digest for the .NET world! The C# developers from PVS-Studio have gathered the most interesting and useful insights for you to keep you up to date with the latest.…  ](https://pvs-studio.com/en/blog/posts/csharp/1140/)

* * *

Get notifications about comments to this article

You subscribed to the comments

Subscribe Unsubscribe [ Subscribe ](/login/?next=/en/blog/posts/csharp/0918/)

* * *

## Comments (0)

Next comments ![next comments](https://wcdn.pvs-studio.com/static/assets/spoiler.svg) Leave a comment ![close comment form](https://wcdn.pvs-studio.com/static/images/icons/close.svg)

Input name

Leave a comment

##  Want to try PVS‑Studio for free? 

[ Get free trial ](/en/pvs-studio/try-free/)

###  Achievements 

  * [ Blog ](https://pvs-studio.com/en/blog/posts/)
  * [ Checked projects ](https://pvs-studio.com/en/blog/inspections/)
  * [ Detected errors ](https://pvs-studio.com/en/blog/examples/)
  * [ Customers ](https://pvs-studio.com/en/about/customers/)
  * [ Early access program ](https://pvs-studio.com/en/pvs-studio-eap/)

###  PVS-Studio 

  * [ About PVS-Studio ](https://pvs-studio.com/en/pvs-studio/)
  * [ Download ](https://pvs-studio.com/en/pvs-studio/download/)
  * [ Request a trial key ](https://pvs-studio.com/en/for-clients/)
  * [ Documentation ](https://pvs-studio.com/en/docs/)
  * [ Online Examples ](https://pvs-studio.com/en/pvs-studio/examples/)
  * [ Troubleshooting ](https://pvs-studio.com/en/docs/manual/0029/)

###  Licensing 

  * [ Purchase a license ](https://pvs-studio.com/en/order/)
  * [ Choose a license ](https://pvs-studio.com/en/order/license/)
  * [ For clients ](https://pvs-studio.com/en/for-clients/)
  * [ For students ](https://pvs-studio.com/en/order/for-students/)
  * [ For Open Source ](https://pvs-studio.com/en/order/open-source-license/)
  * [ For Microsoft MVP ](https://pvs-studio.com/en/order/mvp/)

###  Company 

  * [ About us ](https://pvs-studio.com/en/about/)
  * [ Jobs ](https://pvs-studio.com/en/about/careers/)
  * [ Contacts ](https://pvs-studio.com/en/address/)
  * [ Feedback ](https://pvs-studio.com/en/about-feedback/)
  * [ Subscribe to newsletter ](https://pvs-studio.com/en/subscribe/)

Contact us for technical information  
or other questions 

[ Contact us ](/en/about-feedback/)

[ ![Social logo](https://wcdn.pvs-studio.com/static/images/mail/logo_x.svg) ](https://x.com/pvs_studio)

[ ![Social logo](https://wcdn.pvs-studio.com/static/images/logo/linkedIn_logo.svg) ](https://www.linkedin.com/company/pvs-studio/)

[ ![Social logo](https://wcdn.pvs-studio.com/static/images/logo/feedly_icon.svg) ](https://feedly.com/i/subscription/feed%2Fhttps%3A%2F%2Fpvs-studio.com%2Fen%2Fb%2Frss%2F)

[ ![Social logo](https://wcdn.pvs-studio.com/static/images/icons/youtube.svg) ](https://www.youtube.com/c/PVSStudio_channel/)

[ ![Social logo](https://wcdn.pvs-studio.com/static/images/logo/habr_white.svg) ](https://habr.com/en/company/pvs-studio/blog/)

Contact us for technical information  
or other questions 

[ Contact us ](/en/about-feedback/)

![PVS-Studio logo](https://wcdn.pvs-studio.com/static/images/logo/pvs_logo_7.svg)

[Sitemap](https://pvs-studio.com/en/sitemap/)

[Terms of use](https://pvs-studio.com/en/terms-of-use/)

©2008 - 2026, PVS‑Studio LLC

### Let's make a programming language. AST

[ Registration! ](https://pvs-studio.com/en/webinar/30/)
