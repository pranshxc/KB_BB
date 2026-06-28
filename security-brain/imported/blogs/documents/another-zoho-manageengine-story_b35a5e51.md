---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-11_another-zoho-manageengine-story.md
original_filename: 2020-05-11_another-zoho-manageengine-story.md
title: Another Zoho ManageEngine Story
category: documents
detected_topics:
- sso
- ssrf
- sqli
- command-injection
- password-reset
- automation-abuse
tags:
- imported
- documents
- sso
- ssrf
- sqli
- command-injection
- password-reset
- automation-abuse
language: en
raw_sha256: b35a5e51e42d01002eecef2085099cd33119cc4eab8d4f0490409ff74246b57f
text_sha256: 3c7c3389d84f1098baf644a9a173e23853e480714fcd3e09d7c7ad9b036551c4
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Another Zoho ManageEngine Story

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-11_another-zoho-manageengine-story.md
- Source Type: markdown
- Detected Topics: sso, ssrf, sqli, command-injection, password-reset, automation-abuse
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `b35a5e51e42d01002eecef2085099cd33119cc4eab8d4f0490409ff74246b57f`
- Text SHA256: `3c7c3389d84f1098baf644a9a173e23853e480714fcd3e09d7c7ad9b036551c4`


## Content

---
title: "Another Zoho ManageEngine Story"
url: "https://medium.com/@frycos/another-zoho-manageengine-story-7b472f1515f5"
authors: ["Florian Hauser (@frycos)"]
programs: ["Zoho"]
bugs: ["Authentication bypass"]
publication_date: "2020-05-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4595
scraped_via: "browseros"
---

# Another Zoho ManageEngine Story

Another Zoho ManageEngine Story
frycos
Follow
6 min read
·
May 11, 2020

43

1

This is another white-box analysis story about a product from Zoho Corp (see my older blog post on OpManager SQLi). Since several critical findings in ManageEngine products (CVE-2020–10189, CVE-2019–8394) were currently discovered, I thought do give them another chance to practice some code auditing.

Browsing to www.manageengine.com a huge list of products is shown, some of them well-known, others not so much. So I tried to concentrate on a product which is widely used as well (not being ServiceDesk Plus or Desktop Central). What I found was ADManager Plus (being prone to several unauthenticated critical vulnerabilities):

An Active Directory (AD) management and reporting solution that allows IT administrators and technicians to manage AD objects easily and generate instant reports at the click of a button!

One can find this solution being deployed in various internal networks at big companies but also publicly exposed (have a look at Shodan).

So, I downloaded the trial version of ADManager Plus as well as set up a Windows Domain Controller (big thanks to the awesome DetectionLab project). As you might have guessed, I’m still primarily interested in critical bugs which could be exploited from an unauthenticated perspective.

Since this is a Java web application (served in a Tomcat web container), looking at the web.xml file (there are several!) is always a good starter. These files usually contain declarations on Filters, Listeners and of course Java Servlets. To get a first impression of the technology stack, this file was investigated in greater detail. Several things were of interest:

Several filters had something to do with “Security” as e.g. SecurityFilter
The SecurityFilter was not applied to all URL patterns
A lot of URL patterns end in .do (a good indicator for using Struts)
Several more references to configuration files like struts-config.xml, api-struts-config.xml (Struts it is!)

Reading the <servlet-mapping/> sections defining the mapping between servlet classes and URL patterns made clear that not all URL patterns had to pass the SecurityFilter mentioned above.

A small side note: Even though, I didn’t talk about the implementation of SecurityFilter in the first place, this article should give you some insight into my methods to analyze code in general. I’m making a lot of assumptions during my code walkthroughs and I’m also totally aware that I (could) miss things this way ¯\_(ツ)_/¯.

All URLs with the /servlet/ prefix somehow seemed to be less protected than e.g. the RestAPI counterparts. This is why I focused on them in the beginning. Now, step by step I looked into the servlets’ implementation beginning with the first three starting at the top.

As it turned out, number three already was a jackpot: com.manageengine.ads.fw.servlet.UpdateProductDetails.

Sending a POST request to /servlet/UpdateProductDetails with an empty body at least gave us a 200 response with a simple answer “Failed” (well, at least no 401). So next, I had a look into the code of doPost(…) implementation.

Press enter or click to view image in full size

Following the HttpServletRequest object parameter “request” (under our control!) brought us to a dead end almost immediately…or did it?

Let’s have a look at this function isUserAuthenticated(…) more closely. Interestingly, username and password were processed as part of the request object but reaching the code returning Boolean.valueOf(true) was possible even without running into the unwanted ADSErrorHandlers. This seemed to be a rewarding example for a logical bug: not sending a username parameter at all bypasses the credential check.

Press enter or click to view image in full size

Bypassing the second outer if-statement was straight-forward by setting the parameter UPDATE_HA_VIRTUAL_HOST to “true”. Therefore, we reached the line 194 with “return Boolean.valueOf(true)”.

Get frycos’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Going back to our UpdateProductDetails.class I followed the code and observed various request parameters fed into functions which seemed to operate on database tables like “ADSProductDetails”. Checking the schema in the PostgreSQL instance (installed as bundle together with ADManager Plus) revealed interesting columns like is_remotely_hosted.

Reading a bit of ADManager Plus documentation and playing with the web interface showed me that this table stored references to other ManageEngine products used in combination. E.g. ServiceDesk Plus absolutely would make sense to be installed in parallel since Helpdesk staff usually wants to operate on Windows Active Directories as well (Password Resets etc.). Thus, administration of the Active Directory should primarily take place in ADManager Plus but a ServiceDesk instance could be connected to as well. After setting up a ServiceDesk VM and connecting both ManageEngine products with the Integration function, a new row was inserted into the database table ADSProductDetails. Well, you already might have guessed it: with our servlet we were able to insert and/or update these entries.

Press enter or click to view image in full size

The following request made sure that all conditions were met to bypass the authentication check and additionally inserted a row into the table with a host of my choice. You could check with a listening netcat of course to ensure your configuration was correct. ADManager Plus will kindly ask if the connection was possible indeed.

Press enter or click to view image in full size

Of course this is not the only kind of modification possible with this servlet. The most powerful part was reachable with another request parameter: EVENTS.

The inner class EventExecutor extends java.lang.Thread and it’s start() method would trigger the implemented run() accordingly. The static method executeEvents(…) of DBSyncModulesContainer took the original EVENTS parameter (being a JSONArray object) and finally passed it to the method execute(…) of various Executor implementations.

The getExecutor() method would trigger a database read operation and based on the key EXECUTOR_CLASS resolved to the implementing class ADMPExecutorImpl. Now, we’ll finish with one example of inserting another critical setting into the database but you’ll get the idea what you’re capable of when looking at the first lines of code of ADMPExecutorImpl.execute().

But even this specific Executor implementation was only the tip of the iceberg. At the end of the execute() function, there was another call to super.execute(jsonRow), i.e. calling ExecutorImpl.execute(…) just being another fallback code branch. Want to set/overwrite Mail Settings, Proxy Settings or…let’s say SSOConfig (Single-Sign-On)?

Press enter or click to view image in full size

After trying to understand how the EVENTS parameter had to be hierarchically structured, we got this:

Press enter or click to view image in full size

There are so many additional ways to abuse this servlet that I’ll leave these to an exercise for the reader.

Enjoy!
