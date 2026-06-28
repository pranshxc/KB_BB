---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-08_pwn2owning-two-hosts-at-the-same-time-abusing-inductive-automation-ignitions-cus.md
original_filename: 2023-02-08_pwn2owning-two-hosts-at-the-same-time-abusing-inductive-automation-ignitions-cus.md
title: 'Pwn2Owning Two Hosts At The Same Time: Abusing Inductive Automation Ignition’s
  Custom Deserialization'
category: documents
detected_topics:
- command-injection
- automation-abuse
- graphql
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- graphql
- api-security
- cloud-security
language: en
raw_sha256: 507fd3198827ddfdc34272426439b84e74e7109f3ca836db1c2ecc702e1e57e6
text_sha256: 023c9f89e51314358efa130d47d11194d5ebc0504a674fff181765e40290a1f0
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# Pwn2Owning Two Hosts At The Same Time: Abusing Inductive Automation Ignition’s Custom Deserialization

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-08_pwn2owning-two-hosts-at-the-same-time-abusing-inductive-automation-ignitions-cus.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, graphql, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `507fd3198827ddfdc34272426439b84e74e7109f3ca836db1c2ecc702e1e57e6`
- Text SHA256: `023c9f89e51314358efa130d47d11194d5ebc0504a674fff181765e40290a1f0`


## Content

---
title: "Pwn2Owning Two Hosts At The Same Time: Abusing Inductive Automation Ignition’s Custom Deserialization"
page_title: "Zero Day Initiative — Pwn2Owning Two Hosts at the Same Time: Abusing Inductive Automation Ignition’s Custom Deserialization"
url: "https://www.zerodayinitiative.com/blog/2023/2/6/pwn2owning-two-hosts-at-the-same-time-abusing-inductive-automation-ignitions-custom-deserialization"
final_url: "https://www.zerodayinitiative.com/blog/2023/2/6/pwn2owning-two-hosts-at-the-same-time-abusing-inductive-automation-ignitions-custom-deserialization"
authors: ["Piotr Bazydło (@chudyPB)"]
programs: ["Inductive Automation Ignition"]
bugs: ["Insecure deserialization", "RCE", "Security code review"]
publication_date: "2023-02-08"
added_date: "2023-03-06"
source: "pentester.land/writeups.json"
original_index: 1559
---

# Blog

#  Pwn2Owning Two Hosts at the Same Time: Abusing Inductive Automation Ignition’s Custom Deserialization 

__ February 08, 2023

__ Piotr Bazydło

Pwn2Own Miami 2022 was a fine competition. At the contest, I successfully exploited three different targets. In this blog post, I would like to show you my personal best research of the competition: the custom deserialization issue in Inductive Automation Ignition. 

There are several things that make this vulnerability interesting, including the following:

· It exists in a custom deserialization routine, which seems to derive some inspiration from the Java XMLDecoder.  
· It allows you to gain Remote Code Execution on two hosts at the same time: the client where the malicious project file is initially loaded, as well as the server that ultimately handles the file.  
· There is a nice platform that can help an attacker deliver the malicious file to potential victims.  
· In addition to the vector that involves a victim opening a malicious file locally on a client, it can also be exploited through a purely remote vector, in two different ways: either via an API call or via the Project Import functionality in the admin panel.

Since the remote vector requires an authentication bypass, at Pwn2Own, I decided to keep it simple and stick with the local vector. 

This vulnerability was discovered through static code analysis. My full write-up for the contest was 50 pages long. Here I will try my best to provide you with as much information as possible, while not producing a blog post of excessive length. First, here’s a quick video of the exploit in action, showing RCE on both the client and the server! I popped `calc.exe` on the client, whereas `cmd.exe /c whoami > C:\poc.txt` was executed on the server.

**Introduction to Ignition Projects**

According to the Ignition manual, projects are one of the two main components of this platform, the other component being Ignition Gateway. Projects allow you to specify views, data operations, reports and so forth. Moreover, an official [“Ignition Exchange”](https://www.inductiveautomation.com/exchange/) platform exists, which allows users to share their projects globally. This results in a very interesting vector, where a project file can be shared through the vendor’s website. Some of the projects I found have been downloaded hundreds of times. As file handling bugs in this product were in scope for this Pwn2Own, I decided to learn something more about project files.

Let’s have a quick look at project file structure. In recent Ignition versions, a project file is a ZIP-compressed archive containing multiple files and directories. We will highlight several basic components:  
\-- `project.json` – this file contains basic information about the project, such as its name.  
\-- `ignition\global-props` directory – this directory stores properties of the project. This directory will include files named `data.bin` and `resource.json`.  
\-- `com.inductiveautomation.perspective` directory – this directory stores all the data concerning the visual aspects of the projects, such as page configurations, views and styles.  
\-- `com.inductiveautomation.reporting` directory – this directory stores all the data concerning reports. 

Every project contains multiple pairs of corresponding `data.bin` and `resource.json` files. The following screenshot presents several `data.bin` files that are included in the sample project delivered by the vendor:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/9731cdf0-880d-4f50-9fbc-e884b88fce52/databinfiles.png)

_Figure 1 - Example of the data.bin files_

Some of these files contain JSON data, whereas others are gzip-compressed. Let’s open one of the gzip-compressed files in a text editor, after decompression:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/8843b40f-d88a-4cb9-8f73-8700627714a6/databincontent.png)

_Figure 2 - Fragment of the exemplary data.bin file_

Red flags! This file contains:  
\-- Full names of Java classes.  
\-- Something that looks like setters.

At this stage, I knew that I was dealing with something interesting and that it involved a custom serialization mechanism. I decided to dig further and see where it leads.

**data.bin Handling and Two Deserializers**

The main class responsible for the handling of `data.bin` files is called `XMLDeserializer`. It implements multiple `deserialize` methods. The following code snippet presents the one that is interesting for us:

The method checks to see if the input is in a binary format by calling the `isBinaryFormat` function. Depending on the result, it calls either `deserializeBinary` or `deserializeXML`. This decision is based on a magic number stored in the first bytes of the file, and it is not interesting for us.

It seems that both the binary and XML deserializers can be used to achieve remote code execution. They are based on the same deserialization handling classes. I focused solely on the XML deserialization, as it seemed less error-prone and I did not want any surprises during the contest. I had no sample XML file and I had to recreate the format from scratch.

**Inner Workings of`XMLDeserializer`**

This section describes the main aspects of the Ignition `XMLDeserializer`. It contains a lot of source code, which may be hard to follow during the first read. Don’t worry, the end of this chapter contains a summary, which fully describes the deserialization scheme. If you feel overwhelmed by the amount of code, go straight to the end of this section.

Now, let’s have a look at the fragments of the `deserializeXML` function.

At [1], we see the reference to the `org.xml.sax.XMLReader`.

At [2], the `ParseContext` is created. This is an Ignition-specific class.

At [3], code initializes the `XMLParser` object. This is also an Ignition-specific class. The constructor accepts the `ParseContext` object as a parameter.

At [4], code sets the content handler of the SAX `XMLReader` to the `XMLParser`.

At [5], the XML is parsed.

It seems that the `XMLParser` and the `ParseContext` are the key objects here. They will define the behavior of the `XMLReader`. When we deal with the SAX `XMLReader`, we should see calls to two main methods:  
\-- `startElement`, which will be called when a new element starts (like ).  
\-- `endElement`, which will be called when an element ends (like ).

Let’s look at three main parts of `XMLParser`: the constructor, the `startElement` method and the `endElement` method.

The constructor basically sets the `context` member to the provided context (the `ParseContext` class implements the `ParsingHandler` interface, so we are good here).

Two lines can be highlighted here:  
\-- The `subName` string is retrieved using the `getSubElementName` method.  
\-- The code calls `this.context.onElementStart`, which accepts both `name` and `subName` as arguments.

We can skip a detailed analysis of the `endElement` method, as its functioning is analogous to the previously shown method:  
\-- It retrieves the `subName` in the same way as `startElement` does.  
\-- It calls `this.context.onElementEnd`.

We must investigate the `getSubElementName`, as it is something new and not typical for SAX.

As shown here, `getSubElementName` just checks if the element’s name contains either a colon or hyphen, and retrieves the part after the first such character. If there is no colon or hyphen it returns `null`.

At this point, we know that the `XMLDeserializer` will call the following two methods:  
\-- `ParseContext.onElementStart` when an XML element starts.  
\-- `ParseContext.onElementEnd` when an XML element ends. 

These methods are crucial, as they define the whole behavior of the deserializer. Let’s have a look at the first of them.

We can see that this function implements special handling for an element with the name `objects`. This suggests an element containing serialized objects. We can also expect the function to act differently in response to “main” elements (no colon or hypen) versus sub-elements. Let’s start with the main elements.

For a main element, at [4] an object of type `DeserializationHandler` is retrieved via the `lookupHandler` method. An important point to remember: the handler retrieval is based on the element name. Then, the handler’s `startElement` method will be called at [5]. Finally, the handler will be added to the stack (list) at [6].

Let’s go back to the sub-elements. At [3], the code retrieves the last handler from the stack (see [6]). It then calls its `startSubElement` method.

Finally, we will analyze the `onElementEnd` function, together with the very important `foundObject` method.

When dealing with a sub-element, the code retrieves the last handler from the stack and calls the handler’s `endSubElement` method at [2]. Please note that it accepts the whole current object as an input!

When the code deals with something that is not a sub-element, the last handler is removed from the stack at [3]. Then, it calls the handler’s `endElement` method at [4]. This method also accepts the whole current object.

Finally, the deserialized object is retrieved with the handler’s `getObject` method, and the retrieved `obj` is passed to `foundObject`. 

If the stack size is equal to 0, this indicates that a root object’s deserialization has been completed. In this case, the deserialized object is added to the `this.rootObjects` list at [7]. Note that this means that the XML can contain multiple root objects! If we still have handlers on the stack, the `endObject` method of the previous handler is called at [8].

**XMLDeserializer - Summary**

Now we will summarize the behavior of `XMLDeserializer`. `XMLDeserializer` retrieves a deserialization handler based on the first tag that defines an object (a root tag). During the deserialization process, it will call the following methods on the handler methods at the appropriate times:  
\-- `startElement`  
\-- `startSubElement`  
\-- `endElement`  
\-- `endSubElement`  
\-- `endObject`

Let’s try to visualize it with a simplified schema, which presents an order of the calls. It should provide you an idea of the whole deserialization flow (read from the top to the bottom):

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/75698006-c939-4584-b611-6b2060b0160e/deserialization-flow.png)

_Figure 3 - Sample deserialization flow_

We can:  
\-- Define multiple objects that we want to be deserialized (here: handler1 and handler4).  
\-- Define an object nested in an object (handler2 and handler 3). Nested objects might represent values to be assigned to members of a root object. 

The exact outcome of the deserialization is highly dependent on the selected deserialization handlers. Let’s check them out.

**Deserialization Handlers**

We know that deserialization handlers are retrieved with the `lookupHandler` method.

At [1], the handlers are obtained through the `staticHandlers.get` method. 

[2] presents the `addStaticHandler` function. It shows that the handlers are inserted into the `staticHandlers` HashMap. The key into the HashMap is equal to the output of the `handler.getElementName` method.

We will look at the available handlers now. They are defined in `initializeDeserializationHandlers`. There are more than 40 unique handlers implemented and the following screenshot presents a few of them. Does any of them catch your eye?

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/e1c19dc1-27f8-4a97-b4cb-d9f2d473a16e/samplehandlers.png)

_Figure 4 - Sample deserialization handlers_

The `ObjectDeserializationHandler` immediately drew my attention. It looks very generic, and generic things tend to be powerful. Let’s look at its definition.

The `getElementName` method returns the literal string “o”. If we want to use this handler, the XML tag of our root object must have the name “o”. We can also see that this handler defines multiple very interesting members, such as `Class clazz` and `String methodName`. In addition, the `AbstractDeserializationHandler` class defines the `Object object` member. It seems that we are making progress towards RCE, but we still need to fully understand this handler.

In following chapters, I will go through the methods of the `ObjectDeserializationHandler`. Again, if you do not want to read all the source code, you can go straight to the “ObjectDeserializationHandler – Summary” section. 

**ObjectDeserializationHandler - startElement**

Let me start with the suspiciously simple `startElement` method.

The call to `AttributesMap.getClass` leads to the execution of the majority of code here. I am going to keep it simple, so you must know two things.

1) The class name will be retrieved from the XML tag’s “cls” attribute.  
2) It will retrieve the corresponding object of type `Class` by calling `ClassNameResolver.classForName`.

A quick look at the relevant constructor code in `ClassNameResolver` is now necessary.

One can see that the constructor defines some HashMaps and Arrays. The static `createBasic` factory method creates a new `ClassNameResolver` instance and then calls the `addDefaults` method. This method inserts elements into the `aliasMap`, `classMap` and the `searchPaths` members. 

We can now analyze the `classForName` method fragment. I believe that it is the root cause of this vulnerability. The following code snippet also includes the `classForNameImpl` function

The `classForNameImpl` method retrieves the class using the Java `Class.forName` method. If we can reach this part of the code with our class name, we should be able to retrieve any class.

Now back to the `classForName`. At [1], it checks if the class is included in the `aliasMap`. If not, it will just call the desired `classForNameImpl` at [2]. If a `ClassNotFoundException` is thrown, it will iterate through the defined search paths and once again try to retrieve the class at [5].

In general, we have two major security problems here:  
\-- Ignition resolves the user-specified class without any validation.  
\-- Even if the list of aliases and paths is generated with the `addDefaults` method, nevertheless `"java.lang"` is included in the search path. As `"java.lang"` includes many classes that can be potentially abused, the default search paths are dangerous.

One can also notice that if the provided class name starts with the “[“ character, an array type will be specified.

To sum up, we know that we can retrieve any class and we know how to define the first fragment of our malicious XML:

**ObjectDeserializationHandler - startSubElement**

The following code snippet presents the `startSubElement` method of `ObjectDeserializationHandler`.

We can see that we have two sub-elements defined for this handler: “ctor” (probably constructor) and “c” (probably call). In case of both the “ctor” and the “c” element, the method retrieves the `methodSig` member through the `getSignature` method. The signature defines the input arguments. For example, the signature of a method which accepts one argument, having type `Array<String>`:

In the case of a call, the `methodName` member is retrieved from the “m” XML attribute. 

This function looks interesting, especially if we see that at some point the Java `newInstance` method is called. We are going to stop now and go straight to the remaining methods. Soon we will circle back and connect all the dots.

**ObjectDeserializationHandler – endObject**

Before we move on to the `endSubElement` method, the `endObject` function must be analyzed. It is an important fragment of the deserialization flow, as it is called on any non-root object.

It just adds the freshly deserialized object to the `args` list. This list of objects is very important for the next method we will analyze.

**ObjectDeserializationHandler – endSubElement**

We can finally move to the most important method - `endSubElement`.

Let’s divide it into three main parts.

a) Argument retrieval

At [1], a new array of objects is created.

At [2], the arguments that were added with the `endObject` method are retrieved.

b) Handling the case of a “ctor” sub-element

At [3], the code checks to see if the sub-element name is equal to “ctor”.

At [4], the constructor is retrieved with the method signature extracted in the `startSubElement` method.

At [5], the object is initialized with the Java `newInstance` method, passing the deserialized argument list.

As you can see, we are able to initialize a new object, with any public constructor and with arbitrary argument values.

c) Handling the case of a “c” sub-element

At [6], the code checks to see if the sub-element name is equal to “c”.

At [7], it retrieves the method having the specified method name and signature that were extracted in the `startSubElement` method.

At [8], it invokes this method on the already initialized object, using the provided arguments.

Before the function ends, it clears the argument array at [9].

**ObjectDeserializationHandler - endElement**

This final code snippet presents the `endElement` method.

This method is very simple. If the `object` member was not already set, a new object is instantiated with the default public constructor that has no arguments (Java `newInstance` method).

We can see that `ObjectDeserializationHandler` leads to insecure reflection! We can provide any class, constructor, methods and arguments, though we are restricted to public constructors and methods. The handler will retrieve the specified class, instantiate it with the specified constructor and invoke the specified methods. We can even provide method arguments, where again we can control the type. This mechanism is ripe for misuse.

**ObjectDeserializationHandler – Summary**

Let’s try to summarize `ObjectDeserializationHandler`. It allows us to retrieve any Java class through the `startElement` method. It also allows us to retrieve an arbitrary constructor and arbitrary methods through the `startSubElement` and `endSubElement` methods. Both the constructor and the methods can be invoked with arbitrary arguments. To sum up, we have almost unlimited reflection capabilities here, with the main restriction being that we are limited to public methods.

One more word about the arguments. Ignition already defines its own handlers for some basic types, such as int, string and array. If we would like to provide some more complex types as arguments, we can use the `ObjectDeserializationHandler` again to create the desired argument values. 

The following figure presents a visualization of a sample serialized object and the deserialization process:

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/49f5cc55-fe8c-491c-8a82-4a36c0089238/object-deserialization-flow.png)

_Figure 5 - High-level description of the deserialization flow for the ObjectDeserializationHandler handler_

In the first step, the deserializer retrieves the `MyClass` class. Then, it gets the constructor that accepts one string as an input and initializes the object with it. It passes string “inputForConstructor” as an argument to the constructor. After that, it retrieves the method `MyClass.myMethod` function that accepts one argument of type `string`. It invokes the method on the already initialized `MyClass` object, passing the string “inputForMethod” as an argument. Finally, it adds the `MyClass` object to the `rootObjects` list.

**Malicious Serialized Object – RCE Payload**

We now have everything we need to know to create a malicious serialized object that gives us code execution. Since we have access to almost unlimited reflection, the task is very simple. For my Pwn2Own PoC, I used the `java.lang.ProcessBuilder` class. I chose the constructor that accepts one array of strings, and then used the zero-parameter `start` method.

The following XML presents the complete payload, which pops calculator.

**Payload Delivery – Importing Project Files**

We can now move on to the payload delivery phase. First, we will briefly describe the project import operation. Importing a project can be performed in two main ways:  
\-- Through the web application.  
\-- Through the Ignition Designer client. 

We will focus on the latter, as this is the vector that was eligible under the rules of the competition. The project import operation can be summarized as follows:  
\-- The engineer starts the Ignition Designer client.  
\-- The engineer connects to a remote or local Ignition server.  
\-- The engineer opens a local ZIP project file in the client.  
\-- The client reads the default initial properties for the project.  
\-- (Optional) The engineer modifies the default properties.  
\-- The engineer finalizes the project import operation. The client sends the project to the server via the API.  
\-- The server imports the project and handles its files. 

Two of these points are highlighted for a reason. I have already mentioned that this vulnerability produces RCE on both the client and the server. In my exploitation scenario, those are the steps that give us code execution on the client and the server, respectively.

The following screenshot presents the structure of my malicious project.

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/5bc69c1c-5525-4907-81ea-1464304ed08d/project-structure.png)

_Figure 6 - Example of the malicious project structure_

We have two malicious files here:  
\-- ignition/global-props/data.bin – default project properties are retrieved from this file by the Ignition Designer client.  
\-- Com.inductiveautomation.reporting/reports/Audit Report/data.bin – a report specification is retrieved by the Ignition server from this file. 

To sum up, if the engineer who loads this project connects to the remote Ignition server, we get code execution on two different machines: the engineer’s workstation as well as the Ignition server!

**Exploitation #1 – the Client RCE**

Let’s see what happens when we open the already presented malicious XML file in Ignition Designer.

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/53be476e-2ef7-4d3b-86a4-c8c3a97039f8/rce-client-error.png)

_Figure 7 - Remote Code Execution on the client - ClassCastException_

The calc was popped, thus our exploit works. However, a `ClassCastException` was thrown and the project import cannot be finalized. This makes sense: Ignition Designer expects an object of type `GlobalProps` type, but it instead received a `ProcessBuilder`. 

Luckily, this issue can be solved easily. Do you remember that we are able to provide multiple objects in one payload? I am going to skip the source code for this one, but the Designer project properties deserialization operates as follows:  
\-- It deserializes the data.bin file.  
\-- It retrieves the first object from the `rootObjects` list.  
\-- It casts it to the `GlobalProps` type. 

The solution is simple. Our payload must contain two objects: a legitimate `GlobalProps` object and a malicious `ProcessBuilder` object. Both will be deserialized, but only the first one will be used by the Designer. The following XML presents an exemplary payload that contains two objects.

With this modification, we get code execution on the client and the victim can finalize the project import operation, allowing us to go on to compromise the server. The following screenshot demonstrates clean code execution on the client.

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/4a4070ec-b1f0-4f74-8adb-5bbceb2a41d0/rce-client-clean.png)

_Figure 8 - Remote Code Execution on the client without exception_

Bonus points for style: This attack on the Designer client leaves few traces. Our malicious XML file will be overwritten with the new data.bin properties file as soon as the “Import Project” button is clicked.

**Exploitation #2 – the Server RCE**

As explained above, when the victim clicks the “Import Project” button (see previous screenshot), the server imports the project and performs the deserialization of the included data.bin files. After a while, we should get our payload executed. The following screenshot presents the reverse shell obtained from the server.

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/3526bbcb-6928-4b85-ad1a-3db71b755b35/revshell.png)

_Figure 9 - Remote Code Execution on the server - reverse shell_

**Pure Remote Exploitation**

There are at least two ways to exploit this vulnerability via the network, and both require authentication.

1) Project Import through the configuration panel

Projects can be imported through the Ignition configuration panel. When the malicious project gets imported, Ignition Gateway processes it and deserialization is triggered. The following screenshot shows the Project Import functionality.

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/e0d411be-ec99-4a86-a995-bbce683271dd/Picture10.png)

_Figure 10 - Remote Exploitation - Project Import functionality_

2) Gateway API

When a user loads a project through the Ignition Designer client, Ignition Designer sends it to the Gateway via the API. A remote attacker can use this API directly to load a project and gain code execution on the server.

Moreover, in separate research, Gateway API authentication was bypassed by Chris Anastasio and Steven Seeley. The PoC for their authentication bypass can be found [here](https://github.com/sourceincite/randy).

When you have a valid API cookie, you can load a malicious project with the following HTTP request:

**Conclusion**

Inductive Automation Ignition is a powerful product that provides great deal of functionality for ICS engineers. One must remember, though, that a rich feature set can also mean a large attack surface. In this blog post, I have shown you the custom deserialization implementation used by Ignition when processing project files. The wide flexibility it offers opens the door to misuse.

I hope you liked this post. If you ever see names of Java classes in an unknown data structure, I encourage you to dig deeper. There is a chance that you will find something interesting there! Until my next post, you can follow me [@chudypb](https://www.twitter.com/chudypb) and follow the team on [Twitter](https://www.twitter.com/thezdi) or [Instagram](https://www.instagram.com/thezdi) for the latest in exploit techniques and security patches.

  * [Inductive Automation](/blog/tag/Inductive+Automation)
  * [Pwn2Own](/blog/tag/Pwn2Own)
  * [Deserialization](/blog/tag/Deserialization)
