---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-20_hacking-into-the-worldwide-jacuzzi-smarttub-network.md
original_filename: 2022-06-20_hacking-into-the-worldwide-jacuzzi-smarttub-network.md
title: Hacking into the worldwide Jacuzzi SmartTub network
category: documents
detected_topics:
- api-security
- mobile-security
- sso
- jwt
- access-control
- command-injection
tags:
- imported
- documents
- api-security
- mobile-security
- sso
- jwt
- access-control
- command-injection
language: en
raw_sha256: 52ed9fb1cad38c67560dad354825cc464b703f9b11e67f1d9244a6ef12efbff2
text_sha256: 7608837bf4b249f129b7a358efb8d297edb24864ffc247a08eff3079c8663a76
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking into the worldwide Jacuzzi SmartTub network

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-20_hacking-into-the-worldwide-jacuzzi-smarttub-network.md
- Source Type: markdown
- Detected Topics: api-security, mobile-security, sso, jwt, access-control, command-injection
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `52ed9fb1cad38c67560dad354825cc464b703f9b11e67f1d9244a6ef12efbff2`
- Text SHA256: `7608837bf4b249f129b7a358efb8d297edb24864ffc247a08eff3079c8663a76`


## Content

---
title: "Hacking into the worldwide Jacuzzi SmartTub network"
url: "https://eaton-works.com/2022/06/20/hacking-into-the-worldwide-jacuzzi-smarttub-network/"
final_url: "https://eaton-works.com/2022/06/20/hacking-into-the-worldwide-jacuzzi-smarttub-network/"
authors: ["Eaton Z. (@XeEaton)"]
programs: ["Jacuzzi Group", "SmartTub"]
bugs: ["SPA", "Android", "JWT", "Privilege escalation", "Mass assignment"]
publication_date: "2022-06-20"
added_date: "2023-02-16"
source: "pentester.land/writeups.json"
original_index: 2532
---

# Hacking into the worldwide Jacuzzi SmartTub network

![](/assets/images/ew-logo-4circle-48.png?cb=64e21a35) Eaton • Jun 20, 2022

Copy Link Share 

**Discussion links:** [X](https://x.com/XeEaton/status/1538950676084047873) | Reddit ([gadgets](https://www.reddit.com/r/gadgets/comments/vi7vu5/researcher_hacks_into_backend_for_network_of/), [netsec](https://www.reddit.com/r/netsec/comments/vgsr81/hacking_into_the_worldwide_jacuzzi_smarttub/))

**News coverage:**

  * [New York Post](https://nypost.com/2022/06/22/jacuzzis-could-be-hacked-and-turned-into-hot-stinky-soup/)
  * [Gizmodo](https://gizmodo.com/jacuzzi-smart-tubs-expose-user-data-research-1849093671) (best headline award🏆)
  * [Motherboard – VICE](https://www.vice.com/en/article/88q9b5/researcher-hacks-into-backend-for-network-of-smart-jacuzzis)
  * [TechCrunch](https://techcrunch.com/2022/06/22/jacuzzi-flaws-admin-exposed-users/) ([Front page screenshot – June 22, 2022](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/68037f99-6d13-4f1e-8ca0-8a6b0c25ca00/full))
  * [PortSwigger](https://portswigger.net/daily-swig/jacuzzi-customer-details-could-be-exposed-by-smarttub-web-bugs-claims-researcher)

**June 22, 2022 update:** Clarified that SmartTub shut down the smarttub.io admin panel themselves, and not Auth0.

**July 25, 2022 update:** [Read the response Jacuzzi Group sent to their retail partners a month ago.](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/6f0b2f58-2c31-44a9-2ec2-e8473abe5300/full)

## **Background**

Jacuzzi Brands is a widely recognized hot tub and spa manufacturer. There are several brands under their umbrella:

  * [Jacuzzi Hot Tubs](https://www.jacuzzi.com/)
  * [Sundance Spas](https://www.sundancespas.com/)
  * [D1 Spas](https://www.d1spas.com/)
  * [ThermoSpas](https://thermospas.com/)

When you go to buy a hot tub, Jacuzzi is likely what comes to mind first, and you’d probably go check out offerings from Jacuzzi Hot Tubs. They make the best ones and [have been in business a long time](https://www.jacuzzi.com/en-us/our-brand/heritage.html).

I ordered a hot tub from a local dealer in June 2021. Delivery took place in December 2021. As part of the order, I optioned the SmartTub feature.

## **What is SmartTub?**

SmartTub consists of two elements: a module inside the tub itself with cell data reception that can access/control tub functionality, and an Android/iPhone app. The tub module is always connected to a central server, providing tub status updates and listening for commands. Command examples: turning on lights, jets, setting water temperate, and more. The module is OEM and can be installed as a factory option, or retrofitted at any time after delivery.

You could consider SmartTub an [IoT](https://en.wikipedia.org/wiki/Internet_of_things)/smart device. Aside from the Android/iPhone app, it also integrates with [Alexa](https://www.amazon.com/Jacuzzi-Brands-SmartTub/dp/B07FZX1N5S), [Google Assistant](https://assistant.google.com/services/a/uid/000000a11c0ebe6d), [Wear OS](https://play.google.com/store/apps/details?id=com.jacuzzi.smarttubwear), and [Apple Watch](https://apps.apple.com/ly/app/smarttub/id1318260634?platform=appleWatch).

SmartTub is available for multiple brands. Below is a screenshot from the app:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/d7eba9da-ee02-4e82-7da7-470f0ae74700/full)

[More about SmartTub on the Jacuzzi website](https://www.jacuzzi.com/en-us/smarttub/smarttub.html)

## **Setting up SmartTub**

On delivery day I was eager to set up SmartTub. After waiting a little while for the dealer to do the pairing/activation, I created my account using the app and started messing around with it. I went to add the account password to my password manager and checked what website/URL should be associated with it. The account confirmation email came from _smarttub.io_ , so that is what I used.

## **A flash of data**

After setting the password in my password manager, I went to the smarttub.io site to see what was there. There was an [Auth0](https://auth0.com/)-branded login page. SmartTub uses Auth0 for their login and user account system. If you don’t want to build your own login and user account system, Auth0 is a good choice and saves you a lot of time by providing a full & secure user account system out of the box. Anything you build from scratch is unlikely to be as secure as Auth0’s offerings.

I entered my details, thinking this was a website alternative to the mobile app. I was greeted with an Unauthorized screen:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/c67bb051-8f76-4d57-ef4c-36acec3bbc00/full)

Right before that message appeared, I saw a header and table briefly flash on my screen. Blink and you’d miss it. I had to use a screen recorder to capture it. I was surprised to discover it was an admin panel populated with user data:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/4b496658-a066-4708-b5e3-590c68565100/full)

Glancing at the data, there is information for multiple brands, and not just from the US. There are a few @jacuzzi.eu emails and a @hotmail.co.uk one, so it seems data from overseas is here too.

The unauthorized redirect makes further investigation impossible, so let’s try to bypass it!

## **Breaking in**

smarttub.io hosted a single-page-application (SPA) built using [React](https://reactjs.org/). Admin panels are commonly built as an SPA, so seeing it used here is unsurprising. I downloaded the JavaScript bundle and searched for instances of “unauthorized”. I found where it sets the URL to the error path, and also where it seemingly creates the unauthorized [div](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div):

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/9dc13454-b615-4561-db8e-e84aac598500/full) ![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/60a43176-4fcf-4c96-c149-e7b38ea99b00/full)

If you look closely in the second image, it checks if the user is admin. If they aren’t, they get redirected to the unauthorized page. This is the _isAdmin_ check:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/82363747-cd5d-4c54-8e6e-7f6ae9cac100/full)

The login works by sending the username and password to Auth0. On success, access and ID tokens are returned. The access token is then sent to [Auth0’s /userinfo endpoint](https://auth0.com/docs/api/authentication#get-user-info) and this information is returned:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/30649809-e628-4c4e-992f-460e2b425d00/full)

This information contains a list of _roles_ , and _isAdmin_ is checking whether _Admin_ is there. In my case, it is not. If the HTTP response could be intercepted to add in the missing Admin role, it’s possible the unauthorized page would no longer show. I used [Fiddler](https://www.telerik.com/fiddler/fiddler-classic) to modify the HTTP response accordingly, and I was finally able to access the admin panel in full.

## **Unrestricted Access**

Once into the admin panel, the amount of data I was allowed to was staggering. I could view the details of every spa, see its owner and even remove their ownership:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/d44b7480-e211-43f9-0a94-8d8e78aacd00/full)

I could view every user account, and even edit them:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/041aee0b-6eae-43d1-7227-790bc828d100/full) ![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/5e05638e-67b2-4ac9-2c01-10610ff69f00/full)

Please note that no operations were attempted that would actually _change_ any data. Therefore, it’s unknown if any changes would actually save. I assumed they would, so I navigated carefully.

## **A _second_ admin panel**

The first admin panel revealed user and spa information. That is pretty bad, but things get worse through the discovery of a _second_ admin panel.

This second admin panel was discovered while reviewing the Android app APK. There is link to an admin console in a configuration function:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/23094558-cf84-4fd2-c843-4a5c4fefda00/full) ![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/0a12bbae-bca9-4378-3489-cda1fc699900/full)

This login screen is not Auth0 branded, so I didn’t expect my credentials to work. I tried them anyway – they seemed to work, but I got a message saying I do not have permission:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/18209c72-7c24-44a6-48d2-348ea5438400/full)

This is a standard browser [alert](https://developer.mozilla.org/en-US/docs/Web/API/Window/alert), coming from JavaScript code. Could the same bypass trick on the first admin panel be used here?

## **Breaking in – Again**

I downloaded the JavaScript bundle. It’s completely different than the first admin panel, but still uses React. I found the code that shows the browser alert, and the _isAdmin_ check.

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/1496eb43-63d5-458f-fb0f-2d4fe7520200/full)

There appears to be other groups besides admin and user. There is one for a “tools admin” and one for the development team. To get user information, the access token [JWT](https://jwt.io/) is decoded client-side, instead of using it to call /userinfo. And, the _groups_ section of the user information is being checked this time, instead of _roles_.

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/b2fff3b7-1d0a-416b-b8c1-e2f72d70bf00/full)

To attempt to bypass this, I used [Chrome Local Overrides](https://developer.chrome.com/blog/new-in-devtools-65/#overrides) to load a modified JavaScript bundle file. The modifications I made were to simply change _canUseTools_ , _checkAdmin_ , and _checkDevTeam_ to return true in all cases. This way, I didn’t need to intercept the HTTP response each time to modify the groups.

Logging in using the modifications worked and I could see the panel, populated with user data yet again:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/cec9f020-857b-4b91-b3a5-2f52fc213300/full)

It’s worth noting that being a member of the tools admin and development team groups unlocks additional menu options that are apparently off-limits to “normal” admins (under the More menu):

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/44b2b6fe-b6aa-4f39-88be-97123913d200/full)

The spa and user access is mostly the same as the previous panel. There’s a few new options though, particularly an option to extend your cell data subscription (or shorten someone else’s…):

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/cd8f2232-010f-41ab-97cd-09aab373fe00/full)

As for other internal sections, including sections that normal admins can’t even access, here is a list of what I observed could be done. Out of respect for Jacuzzi/SmartTub, screenshots of these private/secret/internal areas will not be shown.

  * **Promotions section** – create promo codes for the in-app shopping feature. You can buy accessories, chemicals, and renew your cell data subscription.
  * **Products section** – create, modify, and delete tub colors, cabinet colors, equipment options, revisions, and models. This is basically the database of options for hot tubs.
  * **Dealers section** – create, modify, and delete licensed hot tub dealers.
  * **Registered phones** – unclear what this does exactly. Seems to be some kind of notification system for customer phones. Email addresses are visible, but no phone numbers.
  * **Serial Number Update section** – unclear what this does exactly. Seems like a serial number replacement feature, with options to “fix” certain things.
  * **Manufacturing Logs section** – a list of serial numbers and IDs for some type of device. Maybe the SmartTub modules as they roll of the assembly line. Each entry has a “Mark Done” button.

## **Production Data**

It’s worth noting that both admin panels are accessing the same data source/database, and are accessing production data. I confirmed this by looking up my own account.

## **User Data and California Laws**

Worldwide user data was exposed, which included first name, last name, and email address. There is a phone number field, but thankfully I never saw it filled in anywhere, and you aren’t asked for it when creating an account.

It would be trivial to create a script to download all user information. It’s possible it’s already be done. Jacuzzi is incorporated in California which has data breach notification laws. I’m uncertain whether the exposed data meets the bar for the law’s requirements, and it may not be technically possible to identify California residents in the SmartTub network. Jacuzzi did not respond when I brought up the California laws.

## **Disclosure Timeline**

All times in EST.

  * **Dec 3, 2021, 2:17 PM:** Email sent to address listed on [SmartTub’s Google Play page](https://play.google.com/store/apps/details?id=com.jacuzzi.smarttub) (jacuzzi.app@jacuzzi.com). The email was short and I wrote that I had found security issues with SmartTub, and to please connect me with a security contact. I discovered the security issues just a few hours prior to sending this email. No response was ever received from this address.
  * **Dec 6, 2021, 4:31 PM:** Same email sent to a different address shown in the in-app help section: support@smarttub.net.
  * **Dec 6, 2021, 10:12 PM:** Response from SmartTub support (support@smarttub.net) asking for more details.
  * **Dec 6, 2021, 11:45 PM:** Comprehensive email reply sent with screenshots and explanations. Advice on suggested fixes also given.
  * **Dec 16, 2021, 2:30 PM:** Email reply sent asking if last email was received.
  * **Jan 3, 2022, 2:14 PM:** DM sent to [@JacuzziOfficial on Twitter](https://twitter.com/JacuzziOfficial), asking if they are able to provide an update on the email ticket/reference ID, or if they can provide a different way to contact SmartTub.
  * **Jan 4, 2022, 1:22 PM:** @JacuzziOfficial confirms the only way to reach someone at SmartTub is via the support email I have been using. They were of no further help.
  * **Jan 4, 2022, 1:25 PM:** Happy-new-year email reply sent, asked for an update.
  * **Jan 4, 2022, 1:40 PM:** After about 1 month of no communication, I came up with an alternative. I contacted _Auth0’s_ security team, asking if they would be willing to help their customer.
  * **Jan 4, 2022, 5:44 PM:** Auth0 security rep asks me to use [their submission form](https://auth0.com/responsible-disclosure-policy) to securely provide more details.
  * **Jan 4, 2022, 7:27 PM:** Auth0 form submitted. This opens a submission on Auth0’s [Bugcrowd](https://bugcrowd.com/).
  * **Jan 4, 2022, 8:28 PM:** Auth0 security rep reproduces the issue, starts “internal process of reaching out to the customer”.
  * **Jan 4, 2022, 8:29 PM – Mar 7, 2022, 5:23 PM:** For brevity, this is a summary of activity on the Bugcrowd submission: Auth0 also had trouble reaching SmartTub, but eventually got in touch and SmartTub said they would look into the issues. SmartTub told Auth0 they would shut down the smarttub.io admin panel to “prevent any issues moving forward”. I told Auth0 the second admin panel was still vulnerable. Auth0 was not able to get any further responses from SmartTub, and, understandably, they said they were unable to help further and I should try contacting SmartTub again. This entire time period, I never got any response from SmartTub.
  * **Mar 15, 2022, 5:42 PM:** I send a new email to support@smarttub.net, jacuzzi.app@jacuzzi.com, and a new one I found on Google Play listed under their [Wear OS app](https://play.google.com/store/apps/details?id=com.jacuzzi.smarttubwear): jacuzzi.engineering@gmail.com.
  * **Mar 15, 2022, 5:50 PM:** I was delighted to finally receive a response from someone letting me know they’ve escalated the issue to management, and to expect communication soon. The reply came from support@smarttub.net.
  * **Mar 24, 2022, 2:33 PM:** After no communication, I reply letting them know I had heard nothing.
  * **Mar 31, 2022, 2:04 PM:** I sent another reply asking if they are receiving my emails.
  * **Apr 12, 2022, 3:17 PM:** I begin to wonder if the communication breakdown could be caused by their CMS/support system not processing email replies correctly. To date, I have never received a _reply to a reply_. I send a new email asking for an update.
  * **Apr 21, 2022, 10:00 AM:** It seems my theory may have been incorrect. My new email was not responded to. I decide to email the Auth0 security rep asking if they could email SmartTub, and copy me on the message.
  * **May 2, 2022, 7:46 AM:** I decide to send one last new email to support@smarttub.net, asking for an update. They never responded.
  * **May 5, 2022, 2:13 AM:** Auth0 security rep confirmed Auth0 is unable to help further.
  * **Jun 4, 2022:** I notice the second admin panel has finally been secured.
  * **Jun 20, 2022:** Report published.

**Summary:** After multiple contact attempts through 3 different Jacuzzi/SmartTub email addresses and Twitter, a dialog was not established until Auth0 stepped in. Even then, communication with Jacuzzi/SmartTub eventually dropped off completely, without any formal conclusion or acknowledgement they have addressed all reported issues.

I would like to thank the Auth0 security team. Auth0 didn’t have to help since this was not their problem, but they did, and without their assistance, this disclosure would probably have remained stalled. I was happy to see they are willing to help their customers.

In the end, the second admin panel was secured. I wasn’t notified and decided to check it randomly one day because I wanted to start preparing this report. This is how it looks when I checked on June 4th, 2022 – after logging in, you get this message from the server and there is no way around it:

![](https://eaton-works.com/cdn-cgi/imagedelivery/VwwCqBIYNXeyNQwEQ8uyVQ/f3fd34e4-a810-4827-c050-3f4e101a0600/full)

**Dear Jacuzzi:** I would like to discuss a few other security concerns not mentioned in this report. [Please contact me](https://eaton-works.com/contact/) – I want to help!
