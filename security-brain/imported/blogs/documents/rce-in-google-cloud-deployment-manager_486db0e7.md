---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-21_rce-in-google-cloud-deployment-manager.md
original_filename: 2020-05-21_rce-in-google-cloud-deployment-manager.md
title: RCE in Google Cloud Deployment Manager
category: documents
detected_topics:
- api-security
- access-control
- cloud-security
- oauth
- ssrf
- command-injection
tags:
- imported
- documents
- api-security
- access-control
- cloud-security
- oauth
- ssrf
- command-injection
language: en
raw_sha256: 486db0e7876e35aadf041c633c6362d7ce937288764d4903d9622b9a284be545
text_sha256: d1c609924811ef2367a2bbe815daf6a679c7bfe47b9083ac80efc7666d2ef2e2
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# RCE in Google Cloud Deployment Manager

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-21_rce-in-google-cloud-deployment-manager.md
- Source Type: markdown
- Detected Topics: api-security, access-control, cloud-security, oauth, ssrf, command-injection
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `486db0e7876e35aadf041c633c6362d7ce937288764d4903d9622b9a284be545`
- Text SHA256: `d1c609924811ef2367a2bbe815daf6a679c7bfe47b9083ac80efc7666d2ef2e2`


## Content

---
title: "RCE in Google Cloud Deployment Manager"
url: "https://www.ezequiel.tech/2020/05/rce-in-cloud-dm.html"
final_url: "https://www.ezequiel.tech/2020/05/rce-in-cloud-dm.html"
authors: ["Ezequiel Pereira (@epereiralopez)"]
programs: ["Google"]
bugs: ["SSRF", "RCE"]
bounty: "31,337"
publication_date: "2020-05-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4568
---

###  RCE in Google Cloud Deployment Manager 

on  [ May 21, 2020  ](https://www.ezequiel.tech/2020/05/rce-in-cloud-dm.html "permanent link")

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

_[March 2021 update]_ : This write-up was chosen as the [first place winner of the 2020 GCP VRP prize](https://security.googleblog.com/2021/03/announcing-winners-of-2020-gcp-vrp-prize.html), and [LiveOverflow](https://www.youtube.com/c/LiveOverflowCTF) made an [amazing video explaining how the vulnerability was found](https://www.youtube.com/watch?v=g-JgA1hvJzA).

_**TL;DR**_  
  
By using an internal ([dogfood](https://testing.googleblog.com/2014/01/the-google-test-and-development.html)) version of the [Google Cloud Deployment Manager](https://cloud.google.com/deployment-manager), I was able to issue requests to some [Google internal endpoints](https://landing.google.com/sre/sre-book/chapters/production-environment/) through Google's [Global Service Load Balancer](https://landing.google.com/sre/workbook/chapters/managing-load/#global-software-load-balancer), which _could have_ led to RCE.  
  
This could be achieved through a request to the _Deployment Manager_ to create a [Type Provider](https://cloud.google.com/deployment-manager/docs/reference/v2beta/typeProviders), but adding an undocumented field called googleOptions: [Example](https://gist.github.com/ezequielpereira/72c9e9a1547e6ffa70195d9cab7f13b9#file-example-txt).

This begins an [async operation](https://cloud.google.com/deployment-manager/docs/reference/v2beta/operations), in which the _Deployment Manager_ attempts to retrieve a [descriptor document](https://cloud.google.com/deployment-manager/docs/configuration/type-providers/api-requirements#descriptor_document) from the specified [descriptor URL](https://cloud.google.com/deployment-manager/docs/reference/v2beta/typeProviders#descriptorUrl).  
If it fails, it might still provide information in the error message, such as the response from the internal server. If it succeeds, it would allow an attacker to issue complex internal requests.  
  
Examples: [App Engine Admin API (Internal test version)](https://gist.github.com/ezequielpereira/bc3f91ea5003de9fdba322cf4c92ac79#file-example_insert_tp_req-txt), [Issue Tracker Corp API](https://gist.github.com/ezequielpereira/34d37e6b2fd97f3db5b106643d6cf6b6#file-example-txt).  
Note the issue is not limited to requests to APIs, it just works best on them; [example of non-API endpoint](https://gist.github.com/ezequielpereira/01b6301e62bf95815989e60557b8a27a#file-example-txt) (Google Accounts and ID Administration "**GAIA** " backend - Test endpoint) - The descriptorUrl doesn't matter there, since we expect it to fail because **it is not an API**.  
  
Google paid $31,337 as a reward for the bug report.

_[March 2021 update]_ : Google paid an additional $133,337 prize as part of the 2020 GCP VRP prize, thus a total of $164,674 was paid for this report + write-up.

###  Intro

### 

_Deployment Manager_ is a Google Cloud service that provides a way to handle infrastructure resources' creation, deletion, and modification, programmatically ([Infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_code)).

Relevant _Deployment Manager_ concepts are:  

  * **[Type](https://cloud.google.com/deployment-manager/docs/fundamentals#types)** : Describes the properties of a specific kind of infrastructure resource (For example: VMs, issue tickets, user permissions), there are several pre-defined _Types_ available in _Deployment Manager_ (Called __base types__)  

  * **[Type Provider](https://cloud.google.com/deployment-manager/docs/reference/v2beta/typeProviders)** : Provides a service's [RESTful API](https://en.wikipedia.org/wiki/Representational_state_transfer#Applied_to_web_services) endpoint, with its [descriptor document](https://cloud.google.com/deployment-manager/docs/configuration/type-providers/api-requirements#descriptor_document), for _Deployment Manager_ to manage _Types_ within that service (For example: An API to manage VM instances)  

  * **[Resource](https://cloud.google.com/deployment-manager/docs/fundamentals#resource)** : Represents an instance of a single infrastructure resource, provided by a _Type_ (For example: A VM instance)  

  * **[Templates](https://cloud.google.com/deployment-manager/docs/fundamentals#templates)** : Reusable Python or Jinja2 files to programmatically configure _Resources_  

  * **[Deployment](https://cloud.google.com/deployment-manager/docs/fundamentals#deployment)** : A collection of _Resources_ that are deployed and managed together
  * **[Operation](https://cloud.google.com/deployment-manager/docs/reference/v2beta/operations)** : Whenever a creation, modification, or deletion, action is done in the _Deployment Manager_ , an _Operation_ is returned which can be [polled](https://cloud.google.com/deployment-manager/docs/reference/v2beta/operations/get) to check for completion or error

The main way to interact with the _Deployment Manager_ is through its REST APIs, of which there are two documented versions: [v2](https://cloud.google.com/deployment-manager/docs/reference/latest) (Generally available) and [v2beta](https://cloud.google.com/deployment-manager/docs/reference/v2beta) (In public beta) ([Read more about Google products' launch stages](https://cloud.google.com/products#product-launch-stages)).  
A key difference between both versions, is that _Type Providers_ are only available in the v2beta version.  

**_Note_**  
_It is a bit hard to understand**Google Cloud Deployment Manager** at first glance, if you are interested in it, I would recommend you play around with it, especially through the v2beta REST API. [Read the docs](https://cloud.google.com/deployment-manager/docs), and try [creating Deployments](https://cloud.google.com/deployment-manager/docs/deployments#api) and [Type Providers](https://cloud.google.com/deployment-manager/docs/configuration/type-providers/creating-type-provider#api) to get the hang of it._  
_I tried to link useful resources throughout this write-up, hoping to make it easier to understand._  

###  Security research

### 

My first approach to researching the _Deployment Manager_ was to look for hidden or internal _Types_ , since some Google services (Such as [Google App Engine Flexible](https://cloud.google.com/appengine/docs/flexible)) use the _Deployment Manager_ internally (You can see it in your [project's logs](https://console.cloud.google.com/logs) when deploying an app), but I found none.  
  
Then, I looked at the Jinja2 and Python templates of the _Deployments_.  
Through some trial and error, I was able to [create _Deployments_](https://cloud.google.com/deployment-manager/docs/reference/v2beta/deployments/insert), with specially crafted templates, that would return data as a Python exception on their _Operations_.  
This way, I was able to inspect the Python libraries, read the Python code, and list/read files, but the templates' interpreting script runs on an isolated container with zero privileges, not even network connectivity.  
  
After those attempts, I tried [creating _Type Providers_](https://cloud.google.com/deployment-manager/docs/reference/v2beta/typeProviders/insert) pointing to internal Google Corp APIs, such as issuetracker.corp.googleapis.com, but the _Operations_ always failed with an error saying it did not receive a valid response for the descriptor document, and showing the HTML for the login portal to which [issuetracker.corp.googleapis.com](http://issuetracker.corp.googleapis.com/) redirects to when accessed externally.  
And specifying any [private IP address](https://en.wikipedia.org/wiki/IP_address#Private_addresses) failed with an error saying it was not a valid address (Attempts to bypass it, with domains and redirections pointing to private IPs, gave the same result).  
  
These failed attempts were quite demotivating, so I did not continue researching the _Deployment Manager_ for a while (Remember I did not do all this research all at once on a single day, it was a very slow process).  
  
One day, I decided to look into the _Deployment Manager API_ methods, by [enabling it on the Google Cloud Console](https://console.cloud.google.com/apis/library/deploymentmanager.googleapis.com), going to the [metrics page](https://console.cloud.google.com/apis/api/deploymentmanager.googleapis.com/metrics), and looking at the **Filters** section, where there is a drop-down list titled **Methods** with all of them, _including undocumented ones_ \- Methods _usually_ include the API version in their names.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZSqLerLVk6sOXVfRWl-gDrq0JuJ0UdAhofwg4HJQB_mV5cM7GaTR7Pycn6Dlkm6ntP2aK02tXPrqTYjqvBTxFAdMLcWiURbcBQHeT8bVviEynSqH5T5VTHBmanq1VogQvfA07X17KHqHi/s640/Pic1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZSqLerLVk6sOXVfRWl-gDrq0JuJ0UdAhofwg4HJQB_mV5cM7GaTR7Pycn6Dlkm6ntP2aK02tXPrqTYjqvBTxFAdMLcWiURbcBQHeT8bVviEynSqH5T5VTHBmanq1VogQvfA07X17KHqHi/s1600/Pic1.png)

  
I noticed there were two more API versions besides v2 and v2beta (The documented ones), called alpha and dogfood.  
And I could call methods on those versions, just by replacing v2 or v2beta with either alpha or dogfood in every API call.  
  
I played around a bit with the alpha version, but I did not find anything interesting in it.  
  
The dogfood version was a bit more interesting though, especially because I have noticed the word _dogfood_ being used for [internal testing](https://testing.googleblog.com/2014/01/the-google-test-and-development.html) in Google services.

Dogfood product versions in Google are usually only intended for googlers, so they use a product and report bugs before the changes make their way to the customers.

Maybe this version had internal features, only intended for googlers!  
  
When I [listed the base types](https://cloud.google.com/deployment-manager/docs/reference/v2beta/types/list) on that version, most of them returned an extra field in their definitions: googleOptions.

  

_A couple examples of what this looked like_

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjBTH50aJLrnMR847_YwPg9oaN9uBhsgO86fWQfYtrTjbQb7YcYtSI4uhEIe9ksE0TZB-DYd8jWxPG4EmjSD6I0dylJY4jLO-pz4KX8WdaNfrFfDzCXS-WarOxuqBZFDwTpWEMAluA5Fmj6/s640/Pic2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjBTH50aJLrnMR847_YwPg9oaN9uBhsgO86fWQfYtrTjbQb7YcYtSI4uhEIe9ksE0TZB-DYd8jWxPG4EmjSD6I0dylJY4jLO-pz4KX8WdaNfrFfDzCXS-WarOxuqBZFDwTpWEMAluA5Fmj6/s1600/Pic2.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhDTkicZhCt6DYx9z3mQ9PHD3JwZNXxKMgxYaS2GRKrnX6NEyqi9qEg7R0cA_DTNFnTq4deElv-0E39XjYK295THJxnuCl2jVZPwsUF4uMJSym2TQ5PIX1hWa24h5YwS1YkMor-WIHx8mI7/s640/Pic3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhDTkicZhCt6DYx9z3mQ9PHD3JwZNXxKMgxYaS2GRKrnX6NEyqi9qEg7R0cA_DTNFnTq4deElv-0E39XjYK295THJxnuCl2jVZPwsUF4uMJSym2TQ5PIX1hWa24h5YwS1YkMor-WIHx8mI7/s1600/Pic3.png)

  
When I [listed my own _Type Providers_](https://cloud.google.com/deployment-manager/docs/reference/v2beta/typeProviders/list), they also included this extra field, and specifying the $outputDefaults [system parameter](https://cloud.google.com/apis/docs/system-parameters#definitions) in my query, I could see which fields did the googleOptions field have inside.

I played around with them, [creating _Type Providers_](https://cloud.google.com/deployment-manager/docs/reference/v2beta/typeProviders/insert) with different values in those fields, and came up with an idea of what each one of them do and their expected values (Note that at this point I wasn't able to figure out what most of them did):  

  * injectProject  
 _Boolean_. Regardless of what value I specified, the _Deployment Manager API_ always set it to _false_ on my _Type Providers_. Effect unknown.  

  * deleteIntent  
 _Enum_. I was able to find a single valid value: CREATE_OR_ACQUIRE. Effect unknown.  

  * isLocalProvider  
 _Boolean_. Whenever I set it to _true_ , the _Type Provider_ was always successfully created, regardless of values in any other field, but attempting to create _Deployments_ using it always failed with an error saying the descriptor document could not be retrieved.  

  * ownershipKind  
 _Enum_. The valid values were UNKNOWN, USER and GOOGLE. No effects were observed by setting it to any of these values, but I always set it to GOOGLE during my research.
  * transport  
 _Enum_. The valid values I found at first were: UNKNOWN_TRANSPORT_TYPE and HARPOON. No effects were observed by setting it to any of these values.
  * credentialType  
 _Enum_. The valid values I found at first were: UNKNOWN_CREDENTIAL_TYPE and OAUTH. No effects were observed by setting it to any of these values.
  * gslbTarget  
 _String_. Either empty or something like blade:_< TARGET>_ or gslb:_< TARGET>_. No effects were observed by setting it to any value.
  * descriptorUrlServerSpec  
 _String_ , either the same as gslbTarget or empty. No effects were observed by setting it to any value.

This was very promising, **GSLB** is Google's **[Global Service Load Balancer](https://landing.google.com/sre/workbook/chapters/managing-load/#global-software-load-balancer)** , and it acts like a mix between an internal DNS server and a load balancer.

[According to the SRE Book](https://landing.google.com/sre/sre-book/chapters/production-environment/), when **GSLB** is provided a symbolic name (Kind of like a domain name), it will direct traffic to a linked **BNS address** (_Borg Naming Service_), which is the Google equivalent of an internal IP address.  
  
It surely looks like this could be used to achieve **SSRF to internal servers**!  
But whatever values I tried on gslbTarget and descriptorUrlServerSpec, they did not seem to have any effect.  
  
I then tried to brute force valid credentialType values, and found a new one: GAIAMINT.

I had seen that name referenced before, for example, [in this Google Git commit](https://chromium.googlesource.com/chromiumos/platform/mttools/+/fd204daec02b1f4e3423e501335b61a6e84ae8ec).  
  
When testing _Deployments_ with a _Type Provider_ using that value, I also tested what happened if I set the Type Provider to use an OAuth 2.0 access token as its [authentication mechanism](https://cloud.google.com/deployment-manager/docs/configuration/type-providers/creating-type-provider#authentication).  

Thanks to this, I noticed that a fake API I had set, instead of receiving an access token in the Authorization header, the header was now set to something like this instead: EndUserCreds 1 _< URL-safe Base64 data>_ ([Example](https://gist.github.com/ezequielpereira/f1fccd537ac252344b34b5bd873a1a6c#file-euc_example-txt)).  
  
I am not sure how to decode that, but it looks like it has some [protobuf](https://developers.google.com/protocol-buffers) data inside some other binary format, and some strings can be retrieved: anonymous, 331656524293@cloudservices.gserviceaccount.com (The email of the service account _Deployment Manager_ uses for tokens on my project), cloud-dm and cloudgaia::vjgv73:9898.  
This looks like it is intended for internal use, and some googlers confirmed it is intended for authentication between internal Google systems, it is probably not possible to use it externally.  
  
But besides this oddity, I was unable to brute force any other valid values for credentialType, nor any value for transport.  
  
At this point I also tried adding _staging__ to the beginning of the API version, since I noticed the [Google Compute Engine API](https://cloud.google.com/compute/docs/apis) does that for the **Staging** environment (Fact mentioned in a few places, like in [this GitHub PR](https://github.com/kubernetes/kubernetes/pull/48642#discussion_r126505288)), and **it worked**!  
But the **Staging** environment seemed to work exactly the same way as the **Production** one.  
  
After several failed attempts to achieve anything significant, I stopped researching _Deployment Manager_ for a couple weeks.

### Breakthrough: Exploiting Proto over HTTP  

One day, I got the idea of using [protocol buffers](https://developers.google.com/protocol-buffers) (A Google-developed binary serialization format) to find out the missing values of the credentialType and transport _Enums_ , since in protobuf, _Enums_ are [represented as numbers](https://developers.google.com/protocol-buffers/docs/encoding#structure), not _Strings_ , so I could just count up from 1 until I stop finding new values.

  
Protobufs are used mainly for [gRPC](grpc.io/), a remote procedure call (RPC) system developed by Google, and [supported by many Google APIs](https://googleapis.github.io/HowToRPC.html).  
Unfortunately, the _Deployment Manager API_ does not support _gRPC_ , but it does support a relatively-unknown feature: **Proto over HTTP**.  
  

**Proto over HTTP** is an [experimental gRPC fallback](https://googleapis.github.io/HowToRPC.html#grpc-fallback-experimental) feature available in _some_ Google APIs, not very well documented, availability varies per API, and different APIs might implement it a bit differently. Not every API that supports _gRPC_ supports _Proto over HTTP_ , and viceversa, so I had to check it on the _Deployment Manager API_ , and when I did so, I determined:  

  * URL paths stay the same (/deploymentmanager/_< VERSION>_/projects/_< PROJECT>_/global/_..._)
  * The Content-Type header needs to be set to application/x-protobuf
  * In **Production** , it fails with the error message: Proto over HTTP is not allowed for service
  * **It works** in **Staging**!

Knowing this, I called the [get Type Provider](https://cloud.google.com/deployment-manager/docs/reference/v2beta/typeProviders/get) method of the API, and decoded the response protobuf using a tool called _protoc_ (Protocol Buffers compiler) and its _[\--decode_raw](https://stackoverflow.com/a/12378656) _option.  
This gave me unnamed proto field numbers, and the values assigned to them.  
  
Comparing the values from the retrieved proto and the values in the JSON API, I quickly matched each field number to its field name, and reverse engineered the _Type Providers_ [proto message](https://developers.google.com/protocol-buffers/docs/overview#simple) definition.  
  
Quick example of all of this:

  1. I create a Type Provider through the JSON API:  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgSs4RdrztfdgbijPuW7CCf6tbnIuD7mEpa-riDFaKorJHF5tnTZ1x9LffOVIkLnlvpSrHdl08iX6WUA6pZB9FKFT4P2QAIFe5WN4mfoxQU2XytcXe9uhn9XY58MjI_sUg8D-UlkG82WU9w/s640/Screenshot+from+2020-08-23+16-00-40.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgSs4RdrztfdgbijPuW7CCf6tbnIuD7mEpa-riDFaKorJHF5tnTZ1x9LffOVIkLnlvpSrHdl08iX6WUA6pZB9FKFT4P2QAIFe5WN4mfoxQU2XytcXe9uhn9XY58MjI_sUg8D-UlkG82WU9w/s1288/Screenshot+from+2020-08-23+16-00-40.png)

  2. I get that same Type Provider through the JSON API:  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgKJyQOtNwQrWn0XnNVPcPhcSGvmlcAGEpSC2LSVeferhysJefU5gPxg4WWHhbDPf_uO20j72HQxwH2Vj0KkFaSjNHOuyvSvNg7GxO2_102F0baYYaB9SvKPz64dRnZidUluRHwkA2VAQgK/s640/Screenshot+from+2020-08-23+16-00-10.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgKJyQOtNwQrWn0XnNVPcPhcSGvmlcAGEpSC2LSVeferhysJefU5gPxg4WWHhbDPf_uO20j72HQxwH2Vj0KkFaSjNHOuyvSvNg7GxO2_102F0baYYaB9SvKPz64dRnZidUluRHwkA2VAQgK/s1290/Screenshot+from+2020-08-23+16-00-10.png)

  3. I get that same Type Provider through the Proto over HTTP API:  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEisehC8T6q_hyphenhyphendVyG4kf4vUuwf7BQdVlw0RO2v351T-wZkvfcEW4JtotEoLH5StWsi9T6K6y4vBG0VFJN58dd0EJu1RcHWGfkOr5mecAXuh0Yi2KES2Gx-qknHhmZtNk0r5RtJqZeI8oyMG/s640/Screenshot+from+2020-08-23+15-49-47.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEisehC8T6q_hyphenhyphendVyG4kf4vUuwf7BQdVlw0RO2v351T-wZkvfcEW4JtotEoLH5StWsi9T6K6y4vBG0VFJN58dd0EJu1RcHWGfkOr5mecAXuh0Yi2KES2Gx-qknHhmZtNk0r5RtJqZeI8oyMG/s1292/Screenshot+from+2020-08-23+15-49-47.png)

  4. I decode the response with protoc:  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEyNey2iMtutdfy21xv9O6sLN9wyowSpcrWUByFDIIrEje0T44Kcnc1McSoAA15W6cZBB1ZoE3dFn_1ml9IyHhx0SI7948KTkodlm26Do4BgO_Nd75i0JovMbD6H4rTmFjbulLHXhF9frP/s640/Screenshot+from+2020-08-23+16-05-01.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEyNey2iMtutdfy21xv9O6sLN9wyowSpcrWUByFDIIrEje0T44Kcnc1McSoAA15W6cZBB1ZoE3dFn_1ml9IyHhx0SI7948KTkodlm26Do4BgO_Nd75i0JovMbD6H4rTmFjbulLHXhF9frP/s1281/Screenshot+from+2020-08-23+16-05-01.png)

  5. I figure out which number corresponds to each field (For example, 1=name, 2=id, 3=insertTime,...)
  6. I construct an approximaiton of the original proto message definition with that information  

After some meddling with it, by [creating _Type Providers_](https://cloud.google.com/deployment-manager/docs/reference/v2beta/typeProviders/insert) with different values in the proto fields through **Proto over HTTP** , and decoding the protobuf answers, I got a [good enough approximation](https://gist.github.com/ezequielpereira/c1dfcaae99856f42ee9a94e3669973ab#file-dm-proto) of the values I was missing:  

  * transport
  * GSLB \- It directs requests from the _Deployment Manager_ to the internal Google endpoints specified in gslbTarget and descriptorUrlServerSpec  

  * credentialType
  * ENDUSERCREDS, TYPE_CREDENTIAL \- They seem to act the same way as OAUTH and UNKNOWN_CREDENTIAL_TYPE  

Setting transport to GSLB was the key to **issuing internal requests**!  

###  The bug

### 

With the newly discovered GSLB value for transport, I can craft _Type Providers_ such that the _Deployment Manager_ directs requests to **internal Google endpoints**... _As long as I know where to point_ _gslbTarget to_.  
  
[Here is an example](https://gist.github.com/ezequielpereira/bc3f91ea5003de9fdba322cf4c92ac79#file-example_insert_tp_req-txt) for creating a _Type Provider_ for [Google App Engine Admin API](https://cloud.google.com/appengine/docs/admin-api/apis) \- **Test environment** (Which since my [2018 GAE RCE](https://www.ezequiel.tech/p/36k-google-app-engine-rce.html), has been [**blocked externally** by a 429 error](http://test-appengine.sandbox.googleapis.com/)).  
I got blade:apphosting-admin by listing _Types_ on the dogfood version, the appengine.v1.version _Type_ had gslbTarget set to this value.  
I added -nightly at the end because, _before_ the GAE Test API got blocked externally in 2018, I had noticed the string _nightly_ a lot in it.  
  
This _Type Provider_ worked flawlessly, and I successfully [created a _Deployment_](https://cloud.google.com/deployment-manager/docs/reference/v2beta/deployments/insert) that used it to launch a new app into **GAE Test** to check if [my 2018 bug](https://www.ezequiel.tech/p/36k-google-app-engine-rce.html) was properly fixed (It was).  
  
If I specified some invalid gslbTarget (And I always set descriptorUrlServerSpec to the same value as gslbTarget), the _Operation_ for creating a _Type Provider_ would fail, either with an error message saying it could not connect to the GSLB endpoint, the error the internal endpoint returned (Often **404 Not Found**), or that the response was not a valid descriptor document (For example, some endpoints returned a normal **HTML**) along with the response data.  
One endpoint even returned an error page with a Java stack trace and a message along the lines of: Debugging information, only visible to internal IPs!  
Therefore, I could retrieve some internal information this way.  
  
If I specified some valid gslbTarget, like blade:corp-issuetracker-api for issuetracker.corp.googleapis.com (I got the GSLB name from some of my past research), I would be able to **perform calls to the API**!  
Even though I had no idea how the format for _Issue Tracker_ 's resources would be like, this could be easily overcome by calling [listTypes](https://cloud.google.com/deployment-manager/docs/reference/v2beta/typeProviders/listTypes) on the new _Type Provider_.  
  
These were interesting issues, but I was a bit doubtful of their impact, especially since requests were being made with the _Deployment Manager_ service account's credentials for my project, which would _probably_ be restricted to which endpoints it would be allowed to talk to.  
  
While researching this, I had told some googlers that I had found a way to perform requests to GSLB endpoints, and they told me to write it down on a [VRP grant](https://www.google.com/about/appsecurity/research-grants/) ticket, so that the SRE team could have a heads up of what I was up to, in case they detected my requests.  
  
They also explained one potential issue with requests to GSLB endpoints:  

> **If service A makes a request with service B on behalf of user C, the authorization of user C is checked. If there are no credentials for C, then the authorization of A is checked instead.**

This was really interesting, since I had noticed that the service account credentials used by _Deployment Manager_ were [delegated](https://cloud.google.com/iam/docs/creating-short-lived-service-account-credentials#sa-credentials-permissions) by cloud-dm-staging@prod.google.com (I could see the delegator's ID in the [Cloud Console logs](https://console.cloud.google.com/logs)), and I assume it means that Google prod account has, at least, permissions to **delegate tokens for some service accounts**.  
I would just have to find a way to do so, and remove the service account's credentials so the identity of the _Deployment Manager_ would be used instead.  
  
By this time, it was night in Uruguay, so I just wrote down my research in the grant ticket and stopped researching for the day.  
  
Next morning, my dogs woke me up at about 6 AM, and I noticed notifications of updates on the grant ticket, including one that arrived just as I was reading them:  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjSUGoCKk1COuRsXw0t53X8WaTqAVFGBOyVaSRqSu8wjtAgNhZoJH-RYak77Hu6WYc3JBZVn06j2nc4wK7ziu5VMGGOA3WQc3ChLj0u3ZMTfVFZOn6ikcepcAzcJUI8PS7HKbLoB3ybGgot/s640/Pic4.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjSUGoCKk1COuRsXw0t53X8WaTqAVFGBOyVaSRqSu8wjtAgNhZoJH-RYak77Hu6WYc3JBZVn06j2nc4wK7ziu5VMGGOA3WQc3ChLj0u3ZMTfVFZOn6ikcepcAzcJUI8PS7HKbLoB3ybGgot/s1600/Pic4.png)

  
Eduardo then quickly submitted a VRP report for me, triaged it, escalated it to **P0** , and issued a **Nice catch!**  
It took less than **5 minutes** from **_report submission_** to **_Nice catch!_** , maybe the fastest RCE VRP report ever :).  
  
Later that day, I asked Eduardo a few questions, and he told me this bug was now being treated as an incident, but just because RCE bugs are treated like so.  
Because of this, they asked me to stop further research into it, and send them the details of my actions and findings.  
  
I asked about the potential way this issue could have been exploited, and my understanding is:  

  * Privilege escalation _may_ be achieved through the identity of the _Deployment Manager_ service (cloud-dm-staging@prod.google.com), so it **_might_** have access to internal services a normal service account would _not_ have access to
  * It is **not known** if there are attack vectors that would allow an attacker to **achieve a shell** into Google's internal systems, but the privileges _**could**_ be high enough

  
Because of this probable **maximum impact** , Google treated this as **RCE** , and issued a **$31,337** reward ([Their current standard amount for RCE](//g.co/vrp)).  
[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjMAOWGwWlZM2K3GYzLBrC2vwjSNpiUZNlQECVidmR-SLSgafauX5Awb9bCFlNGQdZvX_usyydwcCm_beCrnhYtvu7-VdKyV7oTIqexNmZaJ9w8ymq6qvN_S8NqBXi-gGAmO3cegl5oVsp2/s640/Pic5.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjMAOWGwWlZM2K3GYzLBrC2vwjSNpiUZNlQECVidmR-SLSgafauX5Awb9bCFlNGQdZvX_usyydwcCm_beCrnhYtvu7-VdKyV7oTIqexNmZaJ9w8ymq6qvN_S8NqBXi-gGAmO3cegl5oVsp2/s1600/Pic5.png)  
  
**Thanks so much to the Google VRP!**  
It was a very interesting bug to research, and I would love to see what other issues could be found in **Google Cloud Deployment Manager**.  
  

###  Extra notes

The issue has now been fixed. The fix seems to just be that now gslbTarget and descriptorUrlServerSpec are ignored when specified on the [create](https://cloud.google.com/deployment-manager/docs/reference/v2beta/typeProviders/insert), [patch](https://cloud.google.com/deployment-manager/docs/reference/v2beta/typeProviders/patch), or [update](https://cloud.google.com/deployment-manager/docs/reference/v2beta/typeProviders/update) _Type Provider_ operations.  
The dogfood version _might_ still be accessible for a while on the API, but that does not mean it is a security issue by itself. There _could be_ some hidden security hole in it though ;).  
  
Also, _after_ reporting my findings to Google, and even _after_ finishing the first few drafts of this write-up, I had the idea of checking whether the [discovery document](https://developers.google.com/discovery/v1/reference/apis) for the dogfood version of the **Staging Deployment Manager API** could be accessed **publicly**.  
Lo an behold, **it can** : <https://staging-deploymentmanager.sandbox.googleapis.com/$discovery/rest?version=dogfood> ([Copy on GitHub](https://gist.github.com/ezequielpereira/8a0b5e3aed6b95327043c8bdd433b731#file-staging-deploymentmanager-sandbox-googleapis-com_dogfood-json), just in case it stops working in the future).  
  
The **discovery document** includes the googleOptions field, and provides a little bit more insight into what its fields do, but not nearly enough, so even if I had noticed the document before, I would have probably had to perform the same steps I performed during my research.  

###  Timeline

### 

  * _May 7th, 2020_ : Issue found and mentioned in a VRP grant ticket
  * _May 8th, 2020_ : Googler checks the issue, submits RCE report and quickly escalates it
  * _May 19th, 2020_ : Reward of $31,337.00 issued
  * _May 20th, 2020_ : Issue confirmed as fixed
  *  _March 2021_ : Prize of $133,337 issued for the vulnerability write-up  

2.11.0.0

2.11.0.0

2.11.0.0

2.11.0.0

2.11.0.0

2.11.0.0

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//resources.blogblog.com/img/blank.gif)

[martin](https://martin.uy/blog)[May 21, 2020 at 6:23:00 PM GMT-3](https://www.ezequiel.tech/2020/05/rce-in-cloud-dm.html?showComment=1590096205999#c3341251086465812041)

Felicitaciones Ezequiel!!! Muy bueno tu trabajo y merecida la recompensa.

Reply[Delete](https://www.blogger.com/comment/delete/6070397520912981280/3341251086465812041)

Replies

Reply

  2. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Info TecnoBlog - <🤖>](https://www.blogger.com/profile/16244197633429492165)[May 23, 2020 at 4:37:00 PM GMT-3](https://www.ezequiel.tech/2020/05/rce-in-cloud-dm.html?showComment=1590262640025#c7455402729659733091)

Congratulations!!

Reply[Delete](https://www.blogger.com/comment/delete/6070397520912981280/7455402729659733091)

Replies

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Info TecnoBlog - <🤖>](https://www.blogger.com/profile/16244197633429492165)[May 23, 2020 at 4:45:00 PM GMT-3](https://www.ezequiel.tech/2020/05/rce-in-cloud-dm.html?showComment=1590263128146#c1519576501637999778)

This comment has been removed by the author.

[Delete](https://www.blogger.com/comment/delete/6070397520912981280/1519576501637999778)

Replies

Reply

Reply

  3. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Info TecnoBlog - <🤖>](https://www.blogger.com/profile/16244197633429492165)[May 23, 2020 at 5:11:00 PM GMT-3](https://www.ezequiel.tech/2020/05/rce-in-cloud-dm.html?showComment=1590264711318#c7350067568841400932)

Wow

Reply[Delete](https://www.blogger.com/comment/delete/6070397520912981280/7350067568841400932)

Replies

Reply

  4. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Hickory](https://www.blogger.com/profile/13016127578577761426)[May 24, 2020 at 1:29:00 PM GMT-3](https://www.ezequiel.tech/2020/05/rce-in-cloud-dm.html?showComment=1590337754024#c1242313487526034070)

Have you noticed $31337 spells eleet? lol nicely done dude!

Reply[Delete](https://www.blogger.com/comment/delete/6070397520912981280/1242313487526034070)

Replies

Reply

  5. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[prasana kannan](https://www.blogger.com/profile/09346923032813142685)[May 28, 2020 at 1:19:00 PM GMT-3](https://www.ezequiel.tech/2020/05/rce-in-cloud-dm.html?showComment=1590682746033#c8196813560980565573)

Awesome..!! Very Inspiring. Thanks for sharing.

Reply[Delete](https://www.blogger.com/comment/delete/6070397520912981280/8196813560980565573)

Replies

Reply

  6. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[HUNTER](https://www.blogger.com/profile/00909093146217958687)[June 14, 2020 at 5:49:00 PM GMT-3](https://www.ezequiel.tech/2020/05/rce-in-cloud-dm.html?showComment=1592167793649#c5454666866517586055)

Nice 

Reply[Delete](https://www.blogger.com/comment/delete/6070397520912981280/5454666866517586055)

Replies

Reply

  7. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Vishal Surelia](https://www.blogger.com/profile/16426142026970023454)[June 23, 2020 at 7:50:00 PM GMT-3](https://www.ezequiel.tech/2020/05/rce-in-cloud-dm.html?showComment=1592952653419#c8819806522912303497)

Thanks for sharing with us.

Reply[Delete](https://www.blogger.com/comment/delete/6070397520912981280/8819806522912303497)

Replies

Reply

  8. ![](//resources.blogblog.com/img/blank.gif)

Anonymous[March 18, 2021 at 8:50:00 AM GMT-3](https://www.ezequiel.tech/2020/05/rce-in-cloud-dm.html?showComment=1616068231723#c1083643185290067427)

Awesome stuff !!! Really cool too !!! 

Reply[Delete](https://www.blogger.com/comment/delete/6070397520912981280/1083643185290067427)

Replies

Reply

  9. ![](//resources.blogblog.com/img/blank.gif)

Anonymous[March 18, 2021 at 10:51:00 AM GMT-3](https://www.ezequiel.tech/2020/05/rce-in-cloud-dm.html?showComment=1616075481139#c2625752744338376636)

congratulations!

Reply[Delete](https://www.blogger.com/comment/delete/6070397520912981280/2625752744338376636)

Replies

Reply

  10. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[AnonyHackPH](https://www.blogger.com/profile/06111147928083300130)[March 21, 2021 at 10:47:00 AM GMT-3](https://www.ezequiel.tech/2020/05/rce-in-cloud-dm.html?showComment=1616334462910#c4128865154667668613)

Congratulations dudeee!

Reply[Delete](https://www.blogger.com/comment/delete/6070397520912981280/4128865154667668613)

Replies

Reply

  11. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[H](https://www.blogger.com/profile/13980405794484012371)[March 21, 2021 at 12:36:00 PM GMT-3](https://www.ezequiel.tech/2020/05/rce-in-cloud-dm.html?showComment=1616341006270#c8385436455221395339)

You Rock!  

Reply[Delete](https://www.blogger.com/comment/delete/6070397520912981280/8385436455221395339)

Replies

Reply

  12. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Security specialist Wolf](https://www.blogger.com/profile/06663173573267062145)[March 23, 2021 at 6:16:00 AM GMT-3](https://www.ezequiel.tech/2020/05/rce-in-cloud-dm.html?showComment=1616491014108#c949331141990431979)

How do I contact you?

Reply[Delete](https://www.blogger.com/comment/delete/6070397520912981280/949331141990431979)

Replies

Reply

  13. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Unknown](https://www.blogger.com/profile/16255623705814804470)[April 18, 2021 at 9:41:00 AM GMT-3](https://www.ezequiel.tech/2020/05/rce-in-cloud-dm.html?showComment=1618749702102#c5109286246271002360)

Great work!!

Reply[Delete](https://www.blogger.com/comment/delete/6070397520912981280/5109286246271002360)

Replies

Reply

Add comment

Load more...

#### Post a Comment

[](https://www.blogger.com/comment/frame/6070397520912981280?po=5712829231004617315&hl=en&saa=85391&origin=https://www.ezequiel.tech&skin=emporio)
