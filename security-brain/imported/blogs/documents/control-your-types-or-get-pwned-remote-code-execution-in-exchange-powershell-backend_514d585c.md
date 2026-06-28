---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-16_control-your-types-or-get-pwned-remote-code-execution-in-exchange-powershell-bac.md
original_filename: 2022-11-16_control-your-types-or-get-pwned-remote-code-execution-in-exchange-powershell-bac.md
title: 'Control Your Types Or Get Pwned: Remote Code Execution In Exchange Powershell
  Backend'
category: documents
detected_topics:
- command-injection
- automation-abuse
- ssrf
- otp
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- ssrf
- otp
- api-security
language: en
raw_sha256: 514d585c1a4984c1d48753c613441c6d86830d358dce11b6783b5f9e6b059792
text_sha256: 5a8a82a12ed6cf515243a6721d0b848762340879d997386829d3ed0b7031e685
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Control Your Types Or Get Pwned: Remote Code Execution In Exchange Powershell Backend

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-16_control-your-types-or-get-pwned-remote-code-execution-in-exchange-powershell-bac.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, ssrf, otp, api-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `514d585c1a4984c1d48753c613441c6d86830d358dce11b6783b5f9e6b059792`
- Text SHA256: `5a8a82a12ed6cf515243a6721d0b848762340879d997386829d3ed0b7031e685`


## Content

---
title: "Control Your Types Or Get Pwned: Remote Code Execution In Exchange Powershell Backend"
page_title: "Zero Day Initiative — Control Your Types or Get Pwned: Remote Code Execution in Exchange PowerShell Backend"
url: "https://www.zerodayinitiative.com/blog/2022/11/14/control-your-types-or-get-pwned-remote-code-execution-in-exchange-powershell-backend"
final_url: "https://www.zerodayinitiative.com/blog/2022/11/14/control-your-types-or-get-pwned-remote-code-execution-in-exchange-powershell-backend"
authors: ["Piotr Bazydło (@chudyPB)"]
programs: ["Checkmk"]
bugs: ["RCE", "Windows"]
publication_date: "2022-11-16"
added_date: "2022-11-17"
source: "pentester.land/writeups.json"
original_index: 1907
---

# Blog

#  Control Your Types or Get Pwned: Remote Code Execution in Exchange PowerShell Backend 

__ November 16, 2022

__ Piotr Bazydło

By now you have likely already heard about the in-the-wild exploitation of Exchange Server, chaining CVE-2022-41040 and CVE-2022-41082. It was originally submitted to the ZDI program by the researcher known as “DA-0x43-Dx4-DA-Hx2-Tx2-TP-S-Q from GTSC”. After successful validation, it was immediately submitted to Microsoft. They patched [both](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41082) [bugs](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41040) along with several other Exchange vulnerabilities in the November Patch Tuesday release.

It is a beautiful chain, with an ingenious vector for gaining remote code execution. The tricky part is that it can be exploited in multiple ways, making both mitigation and detection harder. This blog post is divided into two main parts:

· Part 1 – where we review details of the good old ProxyShell Path Confusion vulnerability (CVE-2021-34473), and we show that it can still be abused by a low-privileged user.  
· Part 2 – where we present the novel RCE vector in the Exchange PowerShell backend.

Here’s a quick demonstration of the bugs in action:

**Part 1: The ProxyShell Path Confusion for Every User (CVE-2022-41040)**

There is a great chance that you are already familiar with the original ProxyShell Path Confusion vulnerability (CVE-2021-34473), which allowed [Orange Tsai](https://www.twitter.com/orange_8361) to access the Exchange PowerShell backend during Pwn2Own Vancouver 2021. If you are not, I encourage you to read the details in [this blog post](https://www.zerodayinitiative.com/blog/2021/8/17/from-pwn2own-2021-a-new-attack-surface-on-microsoft-exchange-proxyshell).

Microsoft [patched](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34473) this vulnerability in July of 2021. However, it turned out that the patch did not address the root cause of the vulnerability. Post-patch, unauthenticated attackers are no longer able to exploit it due to the implemented access restrictions, but the root cause remains.

First, let’s see what happens if we try to exploit it without authentication.

_HTTP Request_

_HTTP Response_

As expected, a 401 Unauthorized error was returned. However, can you spot something interesting in the response? The server says that we can try to authenticate with either Basic or NTLM authentication. Let’s give it a shot.

_HTTP Request_

_HTTP Response_

Exchange says that it is cool now! This shows us that:

· The ProxyShell Path Confusion still exists, as we can reach the PowerShell backend through the autodiscover endpoints.  
· As the autodiscover endpoints allow the use of legacy authentication (NTLM and Basic authentication) by default, we can access those endpoints by providing valid credentials. After successful authentication, our request will be redirected to the selected backend service.

Legacy authentication in Exchange is described by Microsoft [here](https://learn.microsoft.com/en-us/exchange/hybrid-deployment/block-legacy-auth-2019-hybrid). The following screenshot presents a fragment of the table included in the previously mentioned webpage.

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/e78b295f-4003-4fda-b888-999479ad3fe9/1+services-authentication.png)

_Figure 1 - Legacy authentication in Exchange services, source: https://learn.microsoft.com/_

According to the documentation and some manual testing, it seems that an Exchange instance was protected against this vulnerability if:

· A custom protection mechanism was deployed that blocks the Autodiscover SSRF vector (for example, on the basis of the URL), _or  
_ · If legacy authentication was blocked for the Autodiscover service. This can be done with a single command (though an Exchange Server restart is probably required):

`Set-AuthenticationPolicy -BlockLegacyAuthAutodiscover:$true`

So far, we have discovered that an authenticated user can access the Exchange PowerShell backend. We will now proceed to the second part of this blog post to discuss how this can be exploited for remote code execution.

**Part 2: PowerShell Remoting Objects Conversions – Be Careful or Be Pwned (CVE-2022-41082)**

In this part, we will focus on the remote code execution vulnerability in the Exchange PowerShell backend. It is a particularly interesting vulnerability, and is based on two aspects:

· PowerShell Remoting conversions and instantiations.  
· Exchange custom converters.

It has been a very long ride for me to understand this vulnerability fully and I find that I am still learning more about PowerShell Remoting. The PowerShell Remoting Protocol has a very extensive specifications and there are some hidden treasures in there. You may want to look at the [official documentation](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-psrp/602ee78e-9a19-45ad-90fa-bb132b7cecec), although I will try to guide you through the most important aspects. The discussion here should be enough to understand the vulnerability.

**PowerShell Remoting Conversions Basics and Exchange Converters**

There are several ways in which serialized objects can be passed to a PowerShell Remoting instance. We can divide those objects into two main categories:

· Primitive type objects  
· Complex objects

Primitive types are not always what you would think of as “primitive”. We have some basic types here such as strings and byte arrays, but “primitive types” also include types such as URI, XMLDocument and ScriptBlock (the last of which is blocked by default in Exchange). Primitive type objects can usually be specified with a single XML tag, for example:

Complex objects have a completely different representation. Let’s take a quick look at the example from the documentation:

First, we can see that the object is specified with the “Obj” tag. Then, we use the “TN” and “T” tags to specify the object type. Here, we have the _System.Drawing.Point_ type, which inherits from _System.ValueType_. 

An object can be constructed in multiple ways. Shown here is probably the simplest case: direct specification of properties. The “Props” tag defines the properties of the object. You can verify this by comparing the presented serialized object and the [class documentation](https://learn.microsoft.com/en-us/dotnet/api/system.drawing.point?view=netframework-4.8).

One may ask: How does PowerShell Remoting deserialize objects? Sadly, there is no single, easy answer here. PowerShell Remoting implements multiple object deserialization (or conversion) mechanisms, including quite complex logic and as well as some validation. I will focus on two main aspects, which are crucial for our vulnerability.

a) Verifying if the specified type can be deserialized  
b) Converting (deserializing) the object

 _Which Types Can Be Deserialized?_

PowerShell Remoting will not deserialize all .NET types. By default, it allows those types related to the remoting protocol itself. However, the list of allowed types can be extended. Exchange does that through two files:

· Exchange.types.ps1xml  
· Exchange.partial.types.ps1xml

An example entry included in those files will be presented soon.

In general, the type specified in the payload that can be deserialized is referenced as the “Target Type For Deserialization”. Let’s move to the second part.

_How Is Conversion Performed?_

In general, conversion is done in the following way.

· Retrieve properties/member sets, deserializing complex values if necessary.  
· Verify that this type is allowed to be deserialized.  
· If yes, perform the conversion.

Now the most important part. PowerShell Remoting implements multiple conversion routines. In order to decide which converter should be used, the _System.Management.Automation.LanguagePrimitives.FigureConversion(Type, Type)_ method is used. It accepts two input arguments:

· _Type fromType_ – the type from which the object will be obtained (for example, string or byte array).  
· _Type toType_ – the target type for deserialization.

The _FigureConversion_ method contains logic to find a proper converter. If it is not able to find any converter, it will throw an exception. 

As already mentioned, multiple converters are available. However, the most interesting for us are:

· ConvertViaParseMethod – invokes _Parse(String)_ method on the target type. In this case, we control the string argument.  
· ConvertViaConstructor – invokes the single-argument constructor that accepts an argument of type _fromType_. In this case, we can control the argument, but limitations apply.  
· ConvertViaCast – invokes the proper cast operator, which could be an implicit or explicit cast.  
· ConvertViaNoArgumentConstructor – invokes the no-argument constructor and sets the public properties using reflection.  
· CustomConverter – there are also some custom converters specified.

As we can see, these conversions are very powerful and provide a strong reflection primitive. In fact, some of them were already mentioned in the well-known [Friday the 13th JSON Attacks](https://www.blackhat.com/docs/us-17/thursday/us-17-Munoz-Friday-The-13th-JSON-Attacks-wp.pdf) Black Hat paper. As we have mentioned, though, the _toType_ is validated and we are not able to use these converters to instantiate objects of arbitrary type. That would certainly be a major security hole.

**SerializationTypeConverter – Exchange Custom Converter**

Let’s have a look at one particular item specified in the _Exchange.types.ps1xml_ file:

There are several basic things that we can learn from this XML fragment:

· _Microsoft.Exchange.Data.IPvxAddress_ class is included in the list of the allowed target types.  
· The _TargetTypeForDeserialization_ member gives the full class name.  
· A custom type converter is defined: _Microsoft.Exchange.Data.SerializationTypeConverter_

The _SerializationTypeConverter_ wraps the _BinaryFormatter_ serializer with _ExchangeBinaryFormatterFactory_. That way, the _BinaryFormatter_ instance created will make use of the allow and block lists. 

To sum up, some of our types (or members) can be retrieved through _BinaryFormatter_ deserialization. Those types must be included in the _SerializationTypeConverter_ allowlist, though. Moreover, custom converters are last-resort converters. Before they are used, PowerShell Remoting will try to retrieve the object through a constructor or a _Parse_ method.

**RCE Payload Walkthrough**

It is high time to show you the RCE payload and see what happens during the conversion.

This XML fragment presents the specification of the “-Identity” argument of the “Get-Mailbox” Exchange Powershell cmdlet. We have divided the payload into three sections: Object type, Properties, and Payload.

· Object type section – specifies that there will be an object of type _System.ServiceProcess.ServiceController_.  
· Properties section – specifies the properties of the object. One thing that should catch your attention here is the property with the name _TargetTypeForDeserialization_. You should also notice the byte array with the name _SerializationData_. (Note that Powershell Remoting accepts an array of bytes in the form of a base64 encoded string).  
· Payload section – contains XML in the form of a string. The XML is a XAML deserialization gadget based on _ObjectDataProvider_.

**Getting Control over TargetTypeForDeserialization**

In the first step, we are going to focus on the Properties section of the RCE payload. Before we do that, let’s quickly look at some fragments of the deserialization code. The majority of the deserialization routines are implemented in the _System.Management.Automation.InternalDeserializer_ class.

Let’s begin with this fragment of the _ReadOneObject(out string)_ method:

At [1], it invokes the _ReadOneDeserializedObject_ method, which may return an object.

At [2], the code flow continues, provided an object has been returned. We will focus on this part later.

Let’s quickly look at the _ReadOneDeserializedObject_ method. It goes through the XML tags and executes appropriate actions, depending on the tag. However, only one line is particularly interesting for us.

At [1], it calls _ReadPSObject_. This happens when the tag name is equal to “Obj”.

Finally, we analyze a fragment of the _ReadPSObject_ function.

At [1], the code retrieves the type names (strings) from the _< TN> _tag.

At [2], the code retrieves the properties from the _< Props> _tag.

At [3], the code retrieves the member set from the _< MS> _tag.

At [4], the code tries to read the primary type (such as string or byte array).

At [5], the code initializes a new deserialization procedure, provided that the tag is an _< Obj>_ tag.

So far, we have seen how _InternalDeserializer_ parses the Powershell Remoting XML. As shown earlier, the Properties section of the payload contains a _< Props> _tag. It seems that we must look at the _ReadProperties_ method.

At [1], the _adaptedMembers_ property of the _PSObject_ object is set to some PowerShell-related collection.

At [2], the property name is obtained (from the _N_ attribute).

At [3], the code again invokes _ReadOneObject_ in order to deserialize the nested object.

At [4], it instantiates a _PSProperty_ object, based on the deserialized value and the property name.

Finally, at [5], it extends _adaptedMembers_ by adding the new _PSProperty_. **This is a crucial step, pay close attention to this.**

Let’s again look at the Payload section of our RCE payload:

We have two properties defined here:

· The _Name_ property, which is of type _string_ and whose value is the string “Type”.

· The _TargetTypeForDeserialization_ property, whose value is a complex object specified as follows:

o The type (_TN_ tag) is _System.Exception_.  
o There is a value stored as a base64 encoded string, representing a byte array.

We have already seen that nested objects (defined with the _Obj_ tag) are also deserialized with the _ReadOneObject_ method. We have already looked at its first part (object retrieval). Now, let’s see what happens further:

At [1], the code retrieves the _Type targetTypeForDeserialization_ through the _GetTargetTypeForDeserialization_ method.

At [2], the code tries to retrieve a new object through the _LanguagePrimitives.ConvertTo_ method (if _GetTargetTypeForDeserialization_ returned anything). The _targetTypeForDeserialization_ is one of the inputs. Another input is the object obtained with the already analyzed _ReadOneDeserializedObject_ method.

As we have specified the object of the _System.Exception_ type (_TN_ tag), the _GetTargetTypeForDeserialization_ method will return the _System.Exception_ type. Why does the exploit use _Exception_? For two reasons:

· It is included in the allowlist exchange.partial.types.ps1xml.  
· It has a custom converter registered: _Microsoft.Exchange.Data.SerializationTypeConverter._

These two conditions are important because they allow the object to be retrieved using the _SerializationTypeConverter_ , which was discussed above as a wrapper for _BinaryFormatter_. Note that there are also various other types available besides _System.Exception_ that meet the two conditions mentioned here, and those types could be used as an alternative to _System.Exception_.

Have you ever tried to serialize an object of type _Type_? If yes, you probably know that it is serialized as an instance of _System.UnitySerializationHolder_. If you base64-decode the string provided in the Properties part of our payload, you will quickly realize that it is a _System.UnitySerializationHolder_ with the following properties:

· _m_unityType_ = _0x04_ ,  
· _m_assemblyName_ = _"PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35",  
_ · _m_data_ = _"System.Windows.Markup.XamlReader"._

To sum up, our byte array holds the object, which constructs a _XamlReader_ type upon deserialization! That is why we want to use the _SerializationTypeConverter_ – it allows us to retrieve an object of type _Type_. An immediate difficulty is apparent here, though, because Exchange’s _BinaryFormatter_ is limited to types on the allowlist. Hence, it’s not clear why the deserialization of this byte array should succeed. Amazingly, though, _System.UnitySerializationHolder_ is included in the _SerializationTypeConverter’s_ list of allowed types!

Let’s see how it looks in the debugger:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/39abe93d-084f-4e0b-8867-695111310a5f/2+debugger-exception.png)

_Figure 2 - Deserialization leading to the retrieval of the XamlReader Type_

Even though the _targetTypeForDeserialization_ is _Exception_ , _LanguagePrimitives.ConvertTo_ returned the _Type_ object for _XamlReader_(see variable _obj2_). This happens because the final type of the retrieved object is not verified. Finally, this _Type_ object will be added to the _adaptedMembers_ collection (see the _ReadProperties_ method).

**Getting Code Execution Through XamlReader, or Any Other Class**

We have already deserialized the _TargetTypeForDeserialization_ property, which is a _Type_ object for the _XamlReader_ type. Perfect! As you might expect, allowing users to obtain an arbitrary _Type_ object through deserialization is not the best idea. But we still need to understand: why does PowerShell Remoting respect such a user-defined property? To begin answering this, let’s consider what the code should do next:

· It should deserialize the _< S> _tag defined after the _< Props> _tag (payload section of the input XML). This is a primitive _string_ type, thus it retrieves the string.  
· It should take the type of the main object, which is defined in the _< TN> _tag (here: _System.ServiceProcess.ServiceController_).  
· It should try to create the _System.ServiceProcess.ServiceController_ instance from the provided string.

Our goal is to switch types here. We want to perform a conversion so that the _System.Windows.Markup.XamlReader_ type is retrieved from the string. Let’s analyze the _GetTargetTypeForDeserialization_ function to see how this can be achieved.

At [1], it tries to retrieve an object of the _PSMemberInfo_ type using the _GetPSStandardMember_ method. It passes two parameters: _backupTypeTable_ (this contains the Powershell Remoting allowed types/converters) and the hardcoded string “TargetTypeForDeserialization”.

At [2], the code retrieves the _Value_ member from the obtained object and tries to cast it to _Type_. When successful, the _Type_ object will be returned. If not, _null_ will be returned.

_GetPSStandardMember_ method is not easy to understand, especially when you are not familiar with the classes and methods used here. However, I will try to summarize it for you in two points:

At [1], the _PSMemberSet_ object is retrieved through the _TypeTableGetMemberDelegate_ method. It takes our specified type (here, _System.ServiceProcess.ServiceController_) and compares it against the list of allowed types. If the provided type is allowed, it will extract its properties and create the new member set.

The following screenshot presents the _PSMemberSet_ retrieved for the _System.ServiceProcess.ServiceController_ type:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/d662ac97-30bb-4fa6-abe9-1e3af92a571d/3+debugger-memberset.png)

_Figure 3 - PSMemberSet retrieved for the System.ServiceProcess.ServiceController type_

At [2], the collection of members is created from multiple sources. If a member is not included in the basic member set (obtained from the list of allowed types), it will try to find such a member in a different source. **This collection includes the adapted members, which contain the deserialized properties obtained through the _Props_ tag.**

Finally, it will try to retrieve the _TargetTypeForDeserialization_ member from the final collection. 

Let’s have a quick look at the specification of the _System.ServiceProcess.ServiceController_ in the list of allowed types. It is defined in the default Powershell Remoting types list, located in C:\Windows\System32\WindowsPowerShell\v1.0\types.ps1xml.

As you can see, **this type does not have the _TargetTypeForDeserialization_ member specified.** Only the _DefaultDisplayPropertySet_ member is defined. According to that, the _targetTypeForDeserialization_ will be retrieved from _adaptedMembers_. As the Exchange _SerializationTypeConverter_ converter allows us to retrieve a _Type_ through deserialization, we can provide a new conversion type to _adaptedMembers_!

Following screenshot presents the obtained _psmemberinfo_ , which defines the _XamlReader_ type:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/ca8aedc4-873c-4ca1-99e2-85d4318ba82e/4+debugger-xamlreader.png)

_Figure 4 - Retrieved XamlReader type_

Success! _GetTargetTypeForDeserialization_ returned the _XamlReader_ type. You probably remember that PowerShell Remoting contains several converters. One of them allows calling the _Parse(String)_ method. According to that, we can call the _XamlReader.Parse(String)_ method, where the input will be equal to the string provided in the _< S> _tag. Let’s quickly verify it with the debugger.

The following screenshot presents the debugging of the _LanguagePrimitive.ConvertTo_ method. The _resultType_ is indeed equal to the _XamlReader_ :

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/47df0040-ce79-4197-a5de-b105a1e8b610/5+debugger-convertTo.png)

_Figure 5 - Debugging of the ConvertTo method - resultType_

The next screenshot presents the _valueToConvert_ argument. It includes the string (XAML gadget) included in our payload:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/349280ce-dba3-4952-9d07-a4f58683c246/6+debugger-convertTo-2.png)

_Figure 6 - Debugging of the ConvertTo method - valueToConvert_

We will soon reach the _LanguagePrimitives.FigureParseConversion_ method. The following screenshot illustrates debugging this method. One can see that:

· _fromType_ is equal to _String.  
_ · _toType_ is equal to _XamlReader_.  
· _methodInfo_ contains the _XamlReader.Parse(String string)_ method.

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/54ae6aed-897d-4179-b5d8-affb0e505b26/7+Picture1.png)

_Figure 7 – Debugging the LanguagePrimitives.FigureParseConversion method_

Yes! We have been able to get the _XamlReader.Parse(String string)_ method through reflection! We also fully control the input that will be passed to this function. Finally, it will be invoked through the _System.Management.Automation.LanguagePrimitives.ConvertViaParseMethod.ConvertWithoutCulture_ method, as presented in the following screenshot:

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/b194bd6f-ca55-4ae5-a19b-b5c19a3e0049/8+debugger-parse.png)

_Figure 8 - Execution of the XamlReader.Parse method_

As you may be aware, XamlReader allows us to achieve code execution through loading XAML (see [ysoserial.net](https://github.com/pwntester/ysoserial.net)). When we continue the process, our command gets executed.

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/8adba186-5a63-444d-b177-f61bccb62db8/9+rce.png)

_Figure 9 - Remote Code Execution through the Exchange PowerShell backend_

There are also plenty of other classes besides _XamlReader_ that could be abused in a similar way. For example, you can call the single-argument constructor of any type, so you can be creative here!

**TL;DR – Summary**

Getting to understand this vulnerability has been a long and complicated process. I hope that I have provided enough details for you to understand this issue. I would like to summarize the whole Microsoft Exchange chain in several points:

· The path confusion in the Autodiscover service (CVE-2021-34473) was not fixed, but rather it was restricted to unauthenticated users. Authenticated users can still easily abuse it using Basic or NTLM authentication.

· PowerShell Remoting allows us to perform object deserialization/conversion operations.

· PowerShell Remoting includes several powerful converters, which can:

o Call the public single-argument constructor of the provided type.  
o Call the public _Parse(String)_ method of the provided type.  
o Retrieve an object through reflection.  
o Call custom converters.  
o Other conversions may be possible as well.

· PowerShell Remoting implements a list of allowed types, so an attacker cannot (directly) invoke converters to instantiate arbitrary types.

· However, the Exchange custom converter named _SerializationTypeConverter_ allows us to obtain an arbitrary object of type _Type_.

· This can be leveraged to fully control the type that will be retrieved through a conversion.

· The attacker can abuse this behavior to call the _Parse(String)_ method or the public single-argument constructor of almost any class while controlling the input argument.

· This behavior easily leads to remote code execution. This blog post illustrates exploitation using the _System.Windows.Markup.XamlReader.Parse(String)_ method.

It was not clear to us how Microsoft was going to approach fixing this vulnerability. Direct removal of the _System.UnitySerializationHolder_ from the _SerializationTypeConverter_ allowlist might cause breakage to Exchange functionality. One potential option was to restrict the returned types, for example, by restricting them to the types in the “Microsoft.Exchange.*” namespace. Accordingly, I started looking for Exchange-internal exploitation gadgets. I found more than 20 of them and reported them to Microsoft to help them with their mitigation efforts. That effort appears to have paid off. Microsoft patched the vulnerability by restricting the types that can be returned through the deserialization of _System.UnitySerializationHolder_ according to a general allowlist, and then restricting them further according to a specific denylist. It seems that the gadgets I reported had an influence on that allowlist. I will probably detail some of those gadgets in a future blog post. Stay tuned for more…

**Summary**

I must admit that I was impressed with this vulnerability. The researcher clearly invested a good amount of time to fully understand the details of PowerShell Remoting, analyze Exchange custom converters, and find a way to abuse them. I had to take my analysis to another level to fully understand this bug chain and look for potential variants and alternate gadgets.

Microsoft patched these bugs in the November release. They also published a [blog](https://msrc-blog.microsoft.com/2022/09/29/customer-guidance-for-reported-zero-day-vulnerabilities-in-microsoft-exchange-server/) with additional workarounds you can employ while you test and deploy the patches. You should also make sure you have the September 2021 Cumulative Update (CU) installed. This adds the [Exchange Emergency Mitigation](https://learn.microsoft.com/en-us/exchange/exchange-emergency-mitigation-service?view=exchserver-2019) service. This automatically installs available mitigations and sends diagnostic data to Microsoft. Still, the best method to prevent exploitation is to apply the most current security updates as they are released. We expect more Exchange patches in the coming months. 

In a future blog post, I will describe some internal Exchange gadgets that can be abused to gain remote code execution, arbitrary file reads, or denial-of-service conditions. These have been reported to Microsoft, but we are still waiting for these bug reports to be addressed with patches. Until then, you can follow me [@chudypb](https://www.twitter.com/chudypb) and follow the team on [Twitter](https://www.twitter.com/thezdi) or [Instagram](https://www.instagram.com/thezdi) for the latest in exploit techniques and security patches.

  * [Exchange](/blog/tag/Exchange)
  * [Microsoft](/blog/tag/Microsoft)
  * [0-day](/blog/tag/0-day)
