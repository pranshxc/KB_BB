---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-19_how-to-harpon-big-blue.md
original_filename: 2021-03-19_how-to-harpon-big-blue.md
title: How to Harpon Big Blue!
category: documents
detected_topics:
- supply-chain
- idor
- ssrf
- xss
- command-injection
- rate-limit
tags:
- imported
- documents
- supply-chain
- idor
- ssrf
- xss
- command-injection
- rate-limit
language: en
raw_sha256: f2304614c8e3358135ecbf3a1379cf9959b834ed393f59ebe6ed7148af2954f8
text_sha256: f0a204440e5c5d170252e0bf34d58310c5619aa5c8b46669ea6d3d2031b368de
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# How to Harpon Big Blue!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-19_how-to-harpon-big-blue.md
- Source Type: markdown
- Detected Topics: supply-chain, idor, ssrf, xss, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `f2304614c8e3358135ecbf3a1379cf9959b834ed393f59ebe6ed7148af2954f8`
- Text SHA256: `f0a204440e5c5d170252e0bf34d58310c5619aa5c8b46669ea6d3d2031b368de`


## Content

---
title: "How to Harpon Big Blue!"
url: "https://clarkvoss.medium.com/how-to-harpon-big-blue-c163722638d8"
authors: ["Clark Voss (@clark_voss)"]
programs: ["IBM"]
bugs: ["Logic flaw", "Exposed registration page"]
publication_date: "2021-03-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3804
scraped_via: "browseros"
---

# How to Harpon Big Blue!

How to Harpon Big Blue!
Clark Voss
Follow
7 min read
·
Mar 19, 2021

100

1

A story about creating backdoors in IBM’s Websphere Portal! This is a feature I’m told…

Press enter or click to view image in full size

How this all started…

Last year while working on a Synack target I notice a website with a long string, like below.

https://example.com/wps/portal/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8ziHd3DQgMNnM3N_M1DjA08PX0NgoNcnQwt3Ez1wwkpiAJKG-AAjgZQ_ejCTkFGTsYGBu7uRlj0I6TDCOm3MCBHP4oDKbI_DKIfT_AU5IaCgCIAZSmAOw!!/dz/d5/L2dBISEvZ0FBIS9nQSEh/

I recognized that this was a serialized string, and after a bit of poking around, found out it was an IBM Websphere Portal, but that’s about all I knew at the time. So now you know as much as I did when I started. WebSphere Portal is an enterprise software used to build and manage web portals. Now you are all caught up, and before we do the deep dive, this write-up will go over how I found this and how to exploit it. Creating a backdoor account in a WebSphere Portal website is just the start of the attack. This can be used for all sorts of things, like finding secret URLs, gathering user data, impersonation, and soo much more. WebSphere Portal is used by government, medical, and shipping service websites.

Let us begin.

I always start by looking at the HTML to see what I’m up against. I found something in the HTML I found very interesting.

src=”/wps/contenthandler/mac/!ut/p/digest!xbnABNVrRrLQ2pjPx5pxWA/mashup/ra:collection?themeID=ZJ_5Q90G1K0KG7AF0AKJJD75G0004&amp;locale=en&amp;mime-

Press enter or click to view image in full size
Content Handler URL

After reading how this works, I found you can use the URL below to download the page collection.

https://example.com/wps/contenthandler/mac/?uri=ra:oid:collection

The URL above has some parts worth mentioning to understand how this all works.

WPS is the main URL, then we have the unauthenticated contenthandler to display or download things, we have MAC which is the friendly path of the main site, this can be different per web site, and we specify the URI which consists of directory ra and the oid or object ID which in this case is collection. There are common directories like nm, ac, um, and ra.

The below list are packages that define content elements of the portal and its surrounding infrastructure.

editLayout : “ibm.portal.Content”
MainPage: “wps.content.root”
editPageProperties : “ibm.portal.Page Properties”,
assignRoles : “ibm.portal.Resource Permissions”,
editAppProperties: “ibm.portal.Template and Application Properties”,
editAppLayout: “ibm.portal.Template and Application Layout”,
assignAppRoles: “ibm.portal.Application Roles”,
assignAppMembers: “ibm.portal.Application Membership”,
showAppPolicyStatus: “ibm.portal.Policy Status”
hiddenPages: “ibm.portal.HiddenPages”

You can use the above list to construct a URL to find more about a site by constructing the URL, like below.

https://example.com/wps/contenthanlder/mac/?uri=nm:oid:wps.content.root

Press enter or click to view image in full size
Downloading wps.content.root

The list of packages can change per site, but there are a few that are common like wps.content.root, and ibm.portal.HiddenPages.

I found I could use the contenthandler to download pages using the above list that reveals hidden parts of the site, users, permissions, and memberships that should not be accessible to unauthenticated users. Below are just a few examples.

Downloading a list of users.

Press enter or click to view image in full size
List of Backend Users

Or what access level those users have.

Press enter or click to view image in full size
Access Level

You may run into restricted parts of the site, so I should mention that Websphere has authenticated and unauthenticated parts of their site like below.

contenthandler = Unauthenticated

mycontenthandler = Authenticated

portal = Unauthenticated

myportal = Authenticated

The first issue here is you can use the unauthenticated content handler to download parts of the site that can divulge information that should not be accessible to unauthenticated users. This is a feature.

Now we want to download the hidden pages that will expose URLs that allow access to the backend.

The URL for downloading hidden pages.

https://examples/wps/contenthandler/?uri=nm:oid:ibm.portal.HiddenPages

Once you download the ibm.portal.HiddenPages, you can then find paths like the friendly path.

https://examples.com/wps/portal/client/welcome/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8ziHd3DQgMNnM3N_M1DjA08PX0NgoNcnQwt3Ez1wwkpiAJKG-AAjgb6BbmhigBypoQ7/dz/d5/L2dBISEvZ0FBIS9nQSEh/?uri=nm:oid:Z6_00000000000000A0BR2B300GG2

Press enter or click to view image in full size
Friendly Path WebSphere Portal

Once you use the URL above you will get redirected to the Friendly path. I found that if you make it to the friendly path you can then make it to the sign-up page. This is a feature.

Get Clark Voss’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now you can sign up a user. You are probably wondering how this is possible? Good question, if we look at a default install of Websphere Portal.

Press enter or click to view image in full size

I found that the site defaults to allow anonymous portal users not only access to the sign-up page but allows for the ability to create backend users, issue number two.

Once you put in basic information and click OK you may get two different messages.

The first message is a Congratulations! message. You did it!

Press enter or click to view image in full size
Congratulation Message

The second message you could get could be an error message like below.

Press enter or click to view image in full size
Error Creating User

Both messages mean you created a user on the backend. On some websites, the login is blocked or you get redirected to the website's main login page. Keep in mind, you create a backend user that wasn’t registered for the main site's content. I have experienced that a user of the main site was created and I was able to access restricted content due to the lack of registration but normally the user you created is just for administrating the site.

The next question is if the login redirects or is blocked how do you log in with the user you just created? Great question!

I found that unauthenticated or anonymous users have access to what is called the service-document. This is a list of links to documents and resources. This is a feature.

https://example.com/wps/contenthandler/!ut/p/digest!KUVNi3mCXU3yrSbamw858g/model/service-document/?locale=en
Press enter or click to view image in full size
Service Document

This then gives you URLs that in some cases require authentication. The kind of authentication being used is basic authentication. This is where we can use the basic authentication to enter the credentials made earlier like going to a similar URL like below.

https://example.com/wps/mycontenthandler/!ut/p/dav/fs-type1/users/anonymous portal user

This will prompt you for credentials.

Press enter or click to view image in full size
Prompted for Username and Password

You can also use this to brute force administration credentials as well, which then would allow you to be an administrator of the site, issue number three. The default administrator is wpsadmin with password wpsadmin. This is a feature.

You may get redirected and automatically log in and, in some cases, you may see a page that is displayed that shows some information that is not particularly interesting about anonymous users. Now that you are logged in with your new account, browse to the below URL which is the sign-up page URL and you will get redirected to the Administration portion of the site.

https://example.com/wps/portal/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8ziDVCAo4FTkJGTsYGBu7uRfjhYgaN7WGiggbO5mb95iLGBp6evQXCQq5OhhZupfhQx-vEowNSPrFC_IDc0FABEybE8/dz/d5/L2dBISEvZ0FBIS9nQSEh/dz/d5/L0lJSkdKSUtVSklKQ2dwUkNncFJBL29Od3dBQUFZUUFBRUl3UWxDVTVBQUdNSUtTcEtGTFJ0R0ZvIS80TmxFTklVTVFuRmR1WXBNaFFUVWs1Q2ltcHBBL1o2XzAwMDAwMDAwMDAwMDAwQTBCUjJCMzAwR1YwL1o3XzAwMDAwMDAwMDAwMDAwQTBCUjJCMzAwSU8wL25vcm1hbC9hby90aG0vT0NOL1o2XzAwMDAwMDAwMDAwMDAwQTBCUjJCMzAwR0cy/#Z7_00000000000000A0BR2B300IO0

There you go! You created a backdoor account. This account will have different permissions depending on how the site is configured. You may be able to delete content, search for other users, discover content, view the site map, create content used to deliver XSS attacks, the world is your oyster. There may be a WAF stopping some attacks but the WAF will not stop you from creating, editing, and gathering data.

Press enter or click to view image in full size
Delete Content
Press enter or click to view image in full size
Finding Admins
Press enter or click to view image in full size
Search for Users to Impersonate

Once you have access you can also get to the IBM Web Content Manager which IBM says accelerates the creation, maintenance, and delivery of content across intranet, extranet, Internet, and portal sites and is an administration part of WebSphere. Below are common tools that can aid in clearing your tracks or deleting all content on the site. Permissions on what you can do vary.

Managing workflows by using the workflow checker tool:

https://example.com/wps/wcm/myconnect/?MOD=workflowenablement&alllibraries=true&workflow=&fix=true

Clearing version history:

https://example.com/wps/wcm/myconnect?MOD=ClearVersions&day=date&month=month&year=year&keep=number_of_entries&restrictOn=item_type&library=library_name&fix=true&preserve_dates=true

The export cache settings task:

https://example.com/wps/wcm/myconnect?MOD=ExportCacheSettings&processLibraries=false

History Cropper:

https://example.com/wps/wcm/myconnect?MOD=ClearHistory&day=date&month=month&year=year&keep=number_of_entries&restrictOn=item_type&library=library_name&fix=true

Data Module:

https://example.com/wps/wcm/myconnect?MOD=data&processLibraries=false&taskType=export&exportLibrary=&output.dir=%2FIBM%2Fexport&single.export.dir=false

Unlock Library Module:

https://example.com/wps/wcm/myconnect?MOD=UnlockLibrary&library=libraryname

Reset EventLog Module

https://example.com/wps/wcm/myconnect?MOD=reseteventlog&library=libraryname&remove=true

Large Resource Finder Module

https://example.com/wps/wcm/myconnect?MOD=FindLargeResources
Press enter or click to view image in full size
History Cropper

I would like to also mention that authenticated users of a website can access these parts of the site. You may configure a user on the main site and they may have excessive permissions on the backend or are able to elevate their permissions once they are logged in or create their own backdoor account that is not monitored.

Last year I reported this to IBM in hopes of a resolution. Almost a year later their fix is to put a WAF in front of the sign-up page and not fix the fact that anonymous users can create accounts. I have been able to bypass similar WAF fixes using other methods that I will keep to myself for now. So the fix is to fire up your WAF, block the sign-up page, and good luck. I have created a Nuceli script in order to easily find these, here. I’m working on making this into an RCE, SSRF, and a few other attacks that I will write about later this year. Now go out and find these! If I can find them, so can you, don’t get discouraged! I hope you enjoyed reading.
