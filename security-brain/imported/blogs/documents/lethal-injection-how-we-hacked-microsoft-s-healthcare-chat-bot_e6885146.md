---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-05-07_lethal-injection-how-we-hacked-microsofts-healthcare-chat-bot.md
original_filename: 2024-05-07_lethal-injection-how-we-hacked-microsofts-healthcare-chat-bot.md
title: 'Lethal Injection: How We Hacked Microsoft''s Healthcare Chat Bot'
category: documents
detected_topics:
- command-injection
- cloud-security
- jwt
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- cloud-security
- jwt
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: e688514653f05a145af7276b98b997030702e9d56e2edfaab7694741fb8e67f9
text_sha256: 86d145aa770e4d7e0577ce4cdbad62e17a482d6f47c0485559358a44d2491196
ingested_at: '2026-06-28T07:32:33Z'
sensitivity: unknown
redactions_applied: false
---

# Lethal Injection: How We Hacked Microsoft's Healthcare Chat Bot

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-05-07_lethal-injection-how-we-hacked-microsofts-healthcare-chat-bot.md
- Source Type: markdown
- Detected Topics: command-injection, cloud-security, jwt, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:33Z
- Redactions Applied: False
- Raw SHA256: `e688514653f05a145af7276b98b997030702e9d56e2edfaab7694741fb8e67f9`
- Text SHA256: `86d145aa770e4d7e0577ce4cdbad62e17a482d6f47c0485559358a44d2491196`


## Content

---
title: "Lethal Injection: How We Hacked Microsoft's Healthcare Chat Bot"
url: "https://www.breachproof.net/blog/lethal-injection-how-we-hacked-microsoft-ai-chat-bot"
final_url: "https://www.breachproof.net/blog/lethal-injection-how-we-hacked-microsoft-ai-chat-bot/"
authors: ["Yanir Tsarimi (@Yanir_)"]
programs: ["Microsoft"]
bugs: ["Chatbot", "Sandbox escape", "Cross-tenant vulnerability", "RCE", "Memory leak"]
bounty: "203,000"
publication_date: "2024-05-07"
added_date: "2024-05-11"
source: "pentester.land/writeups.json"
original_index: 300
---

[breachproof](/)

  * [Blog](/blog)

[Contact](/contact)

# Lethal Injection: How We Hacked Microsoft's Healthcare Chat Bot

![](../../assets/images/blog/lethal-injection-hero.png)

We have discovered multiple security vulnerabilities in the Azure Health Bot service, a patient-facing chatbot that handles medical information. The vulnerabilities, if exploited, could allow access to sensitive infrastructure and confidential medical data. 

All vulnerabilities have been fixed quickly following our report to Microsoft. Microsoft has not detected any sign of abuse of these vulnerabilities. We want to thank the people from Microsoft for their cooperation in remediating these issues: Dhawal, Kirupa, Gaurav, Madeline, and the engineering team behind the service.

The first vulnerability allowed access to authentication credentials belonging to the customers. With continued research, we’ve found vulnerabilities allowing us to take control of a backend server of the service. That server is shared across multiple customers and has access to several databases that contain information belonging to multiple tenants.

**Vulnerabilities Reported**

  * Multiple sandbox escapes, unrestricted code execution as root on the bot backend
  * Unrestricted access to authentication secrets & integration auth providers
  * Unrestricted memory read in the bot backend, exposing sensitive secrets & cross tenant data
  * Unrestricted deletion of other tenants' public resources

## The Discovery

The initial research started at the Azure Health Bot management portal website. Skimming through the features available, we saw that it’s possible to connect your bot to remote data sources, and also provide authentication details.

Since customers would likely connect their bot to 3rd party data, such as patient databases, appointment calendars, and so forth, it’s a very interesting target for an attacker. It’s unlikely to imagine a scenario where the customers wouldn’t want to connect the bot to their data.

After fiddling with this feature, we noticed something interesting in the request that retrieves our data connection details and auth secrets. This is what a regular request looks like:
  
  
  https://portal-eastus.healthbot.microsoft.com/v4/test-301x6x6/integration/data-connections/1679070537717/
  

In this URL, “test-301x6x6” is our unique health bot instance ID, and “1679070537717” is the ID of the unique data connection we created. 

The response to this request was the following JSON:
  
  
  {
  "odata.metadata": "https://hbstenant2steausprod.table.core.windows.net/$metadata#test301x6x6/@Element",
  "etag": "W/\"datetime'2023-03-17T17%3A08%3A44.7784337Z'\"",
  "partitionKey": "DataConnection",
  "rowKey": "1679070537717",
  "timestamp": "2023-03-17T17:08:44.7784337Z",
  "type": "custom",
  "name": "test data connection",
  "description": "desc",
  "base_url": "https://website.com/a",
  "auth_provider": "",
  "static_parameters": "[{\"type\":\"header\",\"key\":\"Test\",\"value\":\"true\"}]"
  }
  

People familiar with Azure will recognize this as an _Azure Table API response_. And it makes sense, the service stores our connection data in the Azure Table service, and it pulls that data directly from there.

Our intuition was to start toying with the ID number of our data connection. We believe that the data connections of all customers are in the same table, and if we can query whatever ID we want from the table, we can view the data connections of other customers.

Per the Azure Table API [documentation](https://learn.microsoft.com/en-us/rest/api/storageservices/query-entities), here’s how a request to retrieve data from a table looks like:

So here we have 3 variables we must fill: 

  * table name
  * partition key
  * row key

We have all the required variables since the previous Table API response discloses all that information. Our guess was, that was the URL the backend server uses to get the information behind the scenes:

Here you can see:

  1. hbstenant2steausprod - the account name Microsoft used for storing the data.
  2. test301x6x6 - our Azure health bot instance ID. This is not a secret.
  3. (PartitionKey=’DataConnection’,RowKey=’1679070537717’): Pulling DataConnection with the ID from the request.  
  

The input in our control is the ID. The idea was to send an ID that would allow us to “break out” of our tenant and read other tenants' data. How do we do that?

Since it’s all appended to a URL, the idea was to leverage URL traversal to cancel out the prepended information added by the server, and then add our own:

As you can see, we encoded the slashes (%2F) which were injected into the URL, effectively turning the request into:

And **voila**! This request successfully returned the connection data of the other tenant.

![](../../assets/images/blog/api-request.png)

‍

## Hacking The Bot Backend - 3 ways to pwn the Node.js vm2 sandbox 

‍

Exploring further into the service, we saw that you can execute your JavaScript code in an isolated environment. This feature lets you process data coming from the chat as part of the conversation with the end customer.

We started by doing simple JS recon inside the sandbox - looking at global variables, we figured we were running inside a vm2 sandbox, a popular Node.js sandboxing library that has since been discontinued due to multiple, unrelated security flaws. 

The goal was simple: to be able to execute shell commands and try to find a way to access cross-tenant data. 

How do you usually execute shell commands with Node.js? Simple, you import the child_process module and call exec/execSync:

‍

But you didn’t think it’d be that easy, did you? In general, _require_ inside the vm2 sandbox is a patched version that doesn’t let you import anything harmful. However, Microsoft wanted to provide a few standard modules to make your life easier. So what we have is a custom require function, which has a very specific whitelist of boring modules. 

But we wanted to understand what’s going on under the hood. Lucky for us, Javascript lets you view the source code of any function. You call .toString() on the function, and voila, you get the source code:

Looks pretty harmless at first glance. It’s a simple check if the required module is in the whitelisted array, and if it is, the original Node.js require function will be called.

Well, if you look closer, they called _.indexOf() instead of the native array indexOf function for some reason. And _.indexOf() is a function from the underscore module. Which is whitelisted. Can you see where we’re going with this?

Bypassing the whitelist and achieving remote code execution is no problem when you can just override the indexOf function, which is conveniently already present as a global, you don’t even need to import it.

And then:

![](../../assets/images/blog/rce-screenshot.png)

‍

Since that backend is shared, we were running as root inside a server that processed the chats of other customers. All research was done in the “debug” environment and was done carefully to not expose any sensitive information. 

Microsoft quickly patched the bug within 24 hours, but we’re not done with this sandbox yet.

‍

#### Underscore strikes again

After Microsoft patched the require() flaw, we dove deeper into understanding the mechanics of the vm2 sandbox. We knew that the modules that are whitelisted are part of the unisolated Node.js root context, the idea was to look into each module individually and try to find interesting functionalities that can be abused.

We spent a few hours reading the documentation and code of all whitelisted modules, most of them were just boring data parsing libraries that didn’t help. **But then something in Underscore.js caught our attention** :

![](../../assets/images/blog/underscore-template-docs.png)

Hmm, a function that compiles JavaScript templates, with an arbitrary code execution feature. We’re sensing a pattern here.

To understand why it’s interesting, you need to understand a simple concept of how the vm2 sandboxing works. In simple terms, they create a “bridge” between the sandbox and the host, and everything you execute inside the sandbox goes through proxy functions which restrict what you can do to a very limited set of features.

For example, if we try to access the Node.js global “process” variable from within the sandbox, the variable won’t be found as it’s not part of the sandboxed context. 

However, when you pass down functions from the root context to the sandbox, the code is already “compiled”. It’s usually pretty dangerous since code inside the sandbox can tamper with the modules and cause unexpected behavior outside the sandbox.

Back to the template function, since the underscore module was passed down from outside the sandbox, the code will be compiled in the non-sandboxed context, therefore, we can achieve code execution simply:

Microsoft quickly patched this as well, and we move on to the final flaw.

‍

#### A Distant Memory

This time we had to think a little bit “outside the box” since we were running out of interesting features in the whitelisted modules. We looked into the “buffer” module which is a built-in Node.js module.

The thing that caught our attention was “Buffer.allocUnsafe”. This function lets you allocate an uninitialized memory buffer. To explain what it means in simple terms, let's compare Buffer.alloc and Buffer.allocUnsafe:

  * Buffer.alloc: will provide a memory buffer that is zeroed out. If we try to read from the allocated buffer, we’ll get a bunch of zeroes.
  * Buffer.allocUnsafe: faster than alloc, will provide a memory buffer that hasn’t been zeroed out. That means that if the memory allocated was previously used for an HTTP request for example, we will be able to see the HTTP request by reading from the newly allocated buffer.

This is pretty dangerous since if we can use allocUnsafe inside the sandbox, we might be able to access sensitive info from the memory of the application. The vm2 developers were aware of this and restricted the use of Buffer.allocUnsafe.

Since the entire buffer module was whitelisted, we had access to SlowBuffer, which is the same as allocUnsafe. This one was not restricted by the sandbox, since it’s not supposed to be there by default: 

Running this code a few times yielded interesting data from the application, for example, a few JWT secrets for internal Azure identities, Kubernetes API calls, cross-tenant data, and more.

After that, Microsoft made multiple important security changes:

  * They had changed the service architecture to run a completely separate ACI instance per customer. Making any future sandbox breach irrelevant. 
  * They changed the sandboxing from vm2 to the isolated-vm library, which uses V8 isolates, a much better and more secure solution.

‍

#### Final Words

This marks the first publication from Breachproof. We aim to publish a lot of more quality research that has real impact. Much more is coming. 

If you're a company dealing with sensitive data and need help securing it - feel free to [contact us](/contact).

‍

 _Authored by_[ _Yanir Tsarimi_](https://twitter.com/Yanir_)

© 2024 Breachproof. All rights reserved

[![](../../assets/images/site/rss-square-icon.svg)](https://breachproof.net/blog/rss.xml)[![](../../assets/images/site/linkedin-square-icon.svg)](https://www.linkedin.com/company/breachproof)[![](../../assets/images/site/x-social-media-black-icon.png)](https://x.com/breachproof)
