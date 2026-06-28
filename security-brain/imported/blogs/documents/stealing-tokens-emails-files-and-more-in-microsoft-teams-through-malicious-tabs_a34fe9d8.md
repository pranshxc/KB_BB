---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-14_stealing-tokens-emails-files-and-more-in-microsoft-teams-through-malicious-tabs.md
original_filename: 2021-06-14_stealing-tokens-emails-files-and-more-in-microsoft-teams-through-malicious-tabs.md
title: Stealing tokens, emails, files and more in Microsoft Teams through malicious
  tabs
category: documents
detected_topics:
- api-security
- access-control
- command-injection
- otp
- automation-abuse
- cloud-security
tags:
- imported
- documents
- api-security
- access-control
- command-injection
- otp
- automation-abuse
- cloud-security
language: en
raw_sha256: a34fe9d84817e6b85a5ddcfe61962ac1748678d363c9ab9c08d884a9977bdef3
text_sha256: 37a15e1dfbfe8c09b2b9f483f198acd9cdaf3d5f929858ce50db09c416f9cabf
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Stealing tokens, emails, files and more in Microsoft Teams through malicious tabs

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-14_stealing-tokens-emails-files-and-more-in-microsoft-teams-through-malicious-tabs.md
- Source Type: markdown
- Detected Topics: api-security, access-control, command-injection, otp, automation-abuse, cloud-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `a34fe9d84817e6b85a5ddcfe61962ac1748678d363c9ab9c08d884a9977bdef3`
- Text SHA256: `37a15e1dfbfe8c09b2b9f483f198acd9cdaf3d5f929858ce50db09c416f9cabf`


## Content

---
title: "Stealing tokens, emails, files and more in Microsoft Teams through malicious tabs"
url: "https://medium.com/tenable-techblog/stealing-tokens-emails-files-and-more-in-microsoft-teams-through-malicious-tabs-a7e5ff07b138"
authors: ["Evan Grant (@stargravy)"]
programs: ["Microsoft"]
bugs: ["postMessage", "Token leak"]
publication_date: "2021-06-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3578
scraped_via: "browseros"
---

# Stealing tokens, emails, files and more in Microsoft Teams through malicious tabs

Stealing tokens, emails, files and more in Microsoft Teams through malicious tabs
Trading up a small bug for a big impact
Evan Grant
Follow
15 min read
·
Jun 14, 2021

442

1

Intro

I recently came across an interesting bug in the Microsoft Power Apps service which, despite its simplicity, can be leveraged by an attacker to gain persistent read/write access to a victim user’s email, Teams chats, OneDrive, Sharepoint and a variety of other services by way of a malicious Microsoft Teams tab and Power Automate flows. The bug has since been fixed by Microsoft, but in this blog we’re going to see how it could have been exploited.

In the following sections, we’ll take a look at how we, as baduser(at)fakecorp.ca, a member of the fakecorp.ca organization, can create a malicious Teams tab and use it to eventually steal emails, Teams messages, and files from gooduser(at)fakecorp.ca, and send emails and messages on their behalf. While the attack we will look at has a lot of moving parts, it is fairly serious, as the compromise of business email is said to have cost victims $1.8 billion in 2020.

As an example to get us started, here is a quick clip of this method being used by Bad User to steal a Word document from Good User’s private OneDrive for Business.

Stealing OneDrive files from a Teams user
Teams Tabs, Power Apps and Power Automate Flows

If you are already familiar with Teams and the Power Platform, feel free to skip this section, but otherwise, it may be useful to go over the pieces of the puzzle we’ll be using later.

Microsoft Teams has a default feature that allows a user to launch small applications as a tab in any team they are part of. If that user is part of an Office 365/Teams organization with a Business Basic license or above, they also have access to a set of Teams tabs which consist of Microsoft Power Apps applications.

Press enter or click to view image in full size
A Teams tab with the Bulletins Power App

Power Apps are part of the wider Microsoft Power Platform, and when a user of a particular team launches their first Power App tab, it creates what Microsoft calls a “Dataverse for Teams Environment”, which according to Microsoft “is used to store, manage, and share team-specific data, apps, and flows”.

It should also be noted that, apart from the team-specific environments, there is a default environment for the organization as a whole. This is important because users can only create connectors and flows in either the default environment, or for teams which they own, and the attack we’re going to look at requires the ability to create Power Automate flows.

Power Automate is a service which lets users create automated workflows which can operate on their Office 365 organization’s data. For example, these flows can be used to do things like send emails on a particular schedule, or send Microsoft Teams messages any time a file on Sharepoint is updated.

Press enter or click to view image in full size
Power Automate flow templates
The bug: trusting a bad domain

When a Power App tab is first created for a team, it runs through a deployment process that uses information gathered from the make.powerapps.com domain to install the application to the team dataverse/environment.

Press enter or click to view image in full size
Installing the app

Teams tabs generally operate by opening an iframe to a page on a domain which is specified as trusted in that application’s manifest. What we see in the above image is a tab that contains an iframe to the page apps.powerapps.com/teams/makerportal?makerPortalUrl=https://make.powerapps.com/somePageHere, which itself is opening an iframe to the make.powerapps.com page passed in makerPortalUrl.

Immediately upon seeing this I was curious if I could make the apps.powerapps.com page load our own content. I noticed a couple of things:

The apps.powerapps.com page will only load the iframe to makerPortalUrl if it is in a Microsoft Teams tab (it uses the Microsoft Teams javascript client sdk).
The child iframe would only load if the makerPortalUrl begins with https://make.powerapps.com

We can see this happen if we view the page’s source, testing out different parameters. Trying to load any url which doesn’t begin with https://make.powerapps.com results in the makerPortalUrl being set to an empty string. However, the validation stops at checking whether the domain begins with make.powerapps.com, and does not check whether it is the full domain.

So, if we set makerPortalUrl equal to something like https://make.powerapps.com.fakecorp.ca/ we will be able to load our own content in the iframe!

Press enter or click to view image in full size
Press enter or click to view image in full size

Cool, we can load an iframe with our own content two iframes deep in a Teams tab, but what does that get us? Microsoft Teams already has a website tab type which lets you load an iframe with a URL of your choosing, and with those you can’t do much. Fortunately for us, some tabs have more capabilities than others.

Stealing auth tokens with postMessage

We can load our own content in an iframe, which itself is sitting in an iframe on apps.powerapps.com. The reason this is more interesting than something like the Website tab type on Teams is that for Power App extension tab types, the app.powerapps.com page communicates both with Teams, by way of the Teams JS SDK, as well as its child iframe using javascript postMessage.

Press enter or click to view image in full size
We can communicate with the parent window via postMessage

Using a Chrome extension, we can watch the postMessages passed between windows as an application is installed and launched. At first glance, the most interesting message is a postMessage from make.powerapps.com in the innermost window (the window which we are replacing when specifying our own makerPortalUrl) to the apps.powerapps.com window, with GET_ACCESS_TOKEN in the data.

The frame which we were replacing was getting access tokens from its parent window without passing any sort of authentication.

Press enter or click to view image in full size
the child iframe requesting an access token via postMessage

I tested this same kind of postMessage from the make.powerapps.com.fakecorp.ca subdomain, and sure enough, I was able to grab the same access tokens. A handler is registered in the WebPlayer.EmbedMakerPortal.js file loaded by apps.powerapps.com which fetches tokens for the requested resource using the https://apps.powerapps.com/auth/onbehalfof endpoint, which in our testing is capable of grabbing tokens for:

- apihub.azure.com
- graph.microsoft.com
- dynamics apps subdomains
- service.flow.microsoft.com
- service.powerapps.com
Press enter or click to view image in full size
Grabbing the access token from a page we control

This is a super exciting thing to see: A tab under our control which can be created in a public team can retrieve access tokens on behalf of the user viewing it. Let’s slow down for a moment though, because I forgot to show an important step: how did we get our own content in a tab in the first place?

Overwriting a Teams tab

I mentioned earlier that Teams tabs generally operate by opening an iframe to a page which is specified in the tab application’s manifest. The request to define what page is loaded by a tab can be seen when adding a new tab or even renaming a currently existing tab.

Press enter or click to view image in full size
The PUT request for renaming a tab lets us change the tab url

The url being given in this PUT request is pointing to the Bulletins Power App which is installed in our team environment. To point the tab to our malicious content we simply have to replace that url with our apps.powerapps.com/teams/makerportal?makerPortalUrl=https://make.powerapps.com.fakecorp.ca page.

It should be noted that this only works because we are passing a url with a trusted domain (apps.powerapps.com) according to the application’s manifest. If we try to pass malicious content directly as the tab’s url, the tab will not load our content.

A short and inconspicuous proof of concept

While the attacks we will look at later are longer and overly noisy for demonstration purposes, let’s consider a very quick proof of concept of how we could use what we currently have to steal access tokens from unsuspecting users.

If we host a page similar to the following and overwrite a tab to point to it, we can grab users’ service.flow.microsoft.com token and send it to another listener we control, while also loading the original Power App in an iframe that matches the tab size. While it won’t look exactly like a normally-running Power App tab, it doesn’t look different enough to notice. If the application requires postMessage communication with the parent app, we could even act as a man-in-the-middle for the postMessages being sent and received by adding a message handler to the PoC.

Press enter or click to view image in full size
During the loading you can see two spinning circles. The smaller one is our JS running.

Now that we know we can steal certain tokens, let’s see what we can do with them, specifically the service.flow.microsoft.com token we just stole.

Stealing more tokens, emails, messages and files

The reason we’re focused on the service.flow.microsoft.com token is because it can be used to get us access to more tokens, and to create Power Automate flows, which will allow us to access a user’s email from Outlook, Teams messages, files from OneDrive and SharePoint, and a whole lot more.

We will construct the attack, at a high level, by:

- Grabbing an extra set of tokens from api.flow.microsoft.com
- Creating connectors to the services we want to access.
  - Consent on behalf of the victim user using first party logins
- Creating Power Automate flows on the victim user’s behalf which let us send/receive emails and teams messages, retrieve emails, messages and files.
- Adding ourselves (or a group we’re in) to the owners of the flow.
- Having the victim user send an email to us containing any information we need to access the flows.

For our example we’re going to be showing pieces of a proof of concept which creates:

- Office 365 (for outlook access), and Teams connectors
- A flow which lets us send emails as the user
- A flow which lets us get all Teams messages from channels the victim is in, and send messages on their behalf.
The api.flow.microsoft.com token bundle

The first stop on our quest to get access to everything the victim user holds dear is an api endpoint which will let us generate a handful of new access tokens. Sending an empty POST request to api.flow.microsoft.com/providers/Microsoft.ProcessSimple/environments/<environment>/users/me/onBehalfOfTokenBundle?api-version=2021–01–03 will let us grab the following tokens, with the following scopes:

Press enter or click to view image in full size
the api.flow.microsoft.com token bundle
- graph.microsoft.com
  - scope : Contacts.Read Contacts.Read.Shared Group.Read.All TeamsAppInstallation.ReadWriteForTeam TeamsAppInstallation.ReadWriteSelfForChat User.Read User.ReadBasic.All
- graph.microsoft.net
  - scope : user_impersonation
- appservice.azure.com
  - scope : user_impersonation
- apihub.azure.com
  - scope : user_impersonation
- consent.msp.windows.net/logic-app-aad
  - scope : user_impersonation
- service.powerapps.com
  - scope : user_impersonation

Some of these tokens will become useful to us for constructing a larger attack (specifically the graph.microsoft.com and apihub.azure.com tokens).

Creating connectors and using first party logins

To create flows which let us take control of the victim’s services, we first need to create connectors for those services.

Get Evan Grant’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When a connector is created, a user can use a consent link to login via a login.microsoft.com popup and grant permissions for the service for which the connector is being made (like Office 365, Teams, or Sharepoint). Some connectors, however, come with a first party login url, which lets us bypass the regular interactive login process and authorize the connector using only the authorization tokens already gathered.

Creating a connector on the victim’s behalf takes only three requests, the final of which is a POST request to the first party login url, with the apihub.azure.com access token.

Press enter or click to view image in full size
consenting to a connector with a stolen apihub.azure.com token

After this third request, the connector will be ready to use with any flow we create.

Creating a flow

Given the number of potential connector types, flow triggers, and actions we can perform, there are an endless number of ways that we could leverage this access. They range anywhere from simply forwarding every email which is received by the victim to the attacker, to only performing actions if a particular RSS feed updates, to creating REST endpoints that let us trigger any number of different actions in different services.

Additionally, if the organization happens to have premium Power Apps/Automate licensing, there are many more options available. It is honestly a very useful system (even if you’re not trying to exploit a whole Office 365 org).

For our attack, we will look at creating a flow which gives us access to endpoints which take JSON input, and perform the actions we want (send emails, teams messages, downloads files, etc). It is a noisier method, since it requires the attacker to send requests (authenticated as themselves), but it is convenient for demonstration. Not all flows require the attacker to be authenticated, or require user interaction.

Choosing flow triggers

A flow trigger is how a flow will be kicked off / knows when to begin. The three main types are automatic (when an email comes in, forward it to this address), instant (when a request is received at this endpoint, trigger the flow), and scheduled (run the flow every xyz seconds/minutes/hours).

The flow trigger we would prefer to use is the “when an HTTP request is received” trigger, which lets unauthenticated users trigger the flow, but that is a premium feature, so instead we will use the “Manually Trigger a Flow” trigger.

Press enter or click to view image in full size
The trigger for our Microsoft Teams flow

This trigger requires authentication, but because it is assumed that the attacker is part of the organization this shouldn’t be a problem, and there are ways to limit information about who is running what flows.

Creating the flow logic

Flows allow you to create an automated process piece by piece, passing the outputs of one action to the next. For example, in the flow we created to let us get all Teams messages from a user, as well as send messages to any channel on their behalf, we determine what action to take, who to send the message to and other details depending on the input passed to the trigger.

Sending a message is quick and simple, but to retrieve all messages for all teams and channels, we first grab a list of all teams, then get each channel per team, then all messages per channel, and roll it up into one big gross ball and have the flow send it to the attacker via email.

Press enter or click to view image in full size
The Teams flow for our PoC

Now that we have the flow created, we need to know how we can create it, and share it with ourselves as the attacker, using the tokens we’ve stolen and what those requests look like. Luckily in our case, it is just a couple of simple requests.

A POST request, containing JSON object representing the flow, to create it and get the unique flow name.
A GET request to grab the flow trigger uri, which will let us trigger the flow as the attacker once we have added ourselves to the owners group.
Adding a group to flow owners

For the trigger we chose, we need to be able to access the flow trigger uri, which can only be done by users who have access to the flow. As a result, we need to add a group we belong to (which seems less suspicious than just adding ourselves) to the flow owners.

The easiest choice here is some large, all-encompassing group, but in our case we’re using the group which is generated automatically for any team created in Microsoft Teams.

In order to grab the unique group id, we use the graph.microsoft.com token we stole from the victim earlier. We then modify the flow’s owners to include that group.

Press enter or click to view image in full size
adding a group to the flow owners
Running the flow and sending ourselves the uris we need

In the proof of concept we’re building, we create a flow that lets us send emails on behalf of the victim user. This can be leveraged at the end of the attack to send ourselves the list of the flow trigger uris we need in order to perform the actions we want.

Press enter or click to view image in full size
sending an email using the Outlook connector and flow we’ve created

For example, at the end of the email/Teams proof of concept we’re building, an email is sent on the victim’s behalf which sends us the flow trigger uris for both the Outlook and Teams flows we’ve created.

Press enter or click to view image in full size
The message we receive from the victim with the flow trigger uris

Using these flow trigger uris, we can now read the victim’s emails and Teams messages, and send messages and emails on their behalf (despite being authenticated as Bad User).

Putting it all together
Press enter or click to view image in full size
The “TL;DR” shot: actions the malicious tab performs on opening

There are a number of ways in which we could build an attack with this vulnerability. It is likely that the best way would be to only use javascript on the malicious tab to steal the service.flow.microsoft.com token, and then perform the rest of the actions from an attacker-controlled server, so we reduce the traffic being generated by the victims and aren’t cut off by them navigating away from the tab.

For our quick and dirty PoC however, we just perform the whole attack with one big javascript section in our malicious tab. The pseudocode for our attack looks like this:

Setting up a malicious tab with a payload like the one above will cause the victim to create connectors and flows, and add the attacker as an owner to them, as well as send them an email containing the flow trigger uris.

As a real example, here is a quick clip of a similar payload running and sending the attacker the victim’s Teams messages, and letting the attacker send a message to a private team masquerading as the victim.

Press enter or click to view image in full size
stealing and sending Teams messages
Considerations for the attacker

If you’ve gone through the above and thought “cool, but it would be really easy for an admin to determine who is using these flows maliciously,” you’d be correct. However, there are a number of steps one could take to limit the exposure of the attacking user if a similar attack is being carried out in a penetration test.

Flows allow you to specify whether the inputs and outputs to each action should be kept secret / scrubbed from the flow’s run history. This means that it would be harder to observe what data is being taken, and where it is being sent.
Not all flows require the user to make authenticated requests to trigger. Low and slow methods like having flows trigger on a RSS feed update (30 minute minimum period), or on a schedule, or automatically (like when a new email comes in from any account, read the email body and perform those actions).
Running the attack as one long javascript payload isn’t ideal and takes too long in real situations. Just grabbing the service.flow.microsoft.com token and conducting the rest of the attack from an attacker-controlled machine would be much less conspicuous.
Flows can be used to creatively cover an attacker’s tracks. For example, if you exfiltrate data via email in a flow, you can add a final step which deletes any emails sent to the attacker’s mail from the Sent Items folder.
Considerations for org administrators

While it may be difficult to determine who in a team has set up a malicious tab, or what user is running the flows (if the inputs/outputs have been made secret), there is a potential indicator to identify whether a user has had malicious flows run on their behalf.

When a user logs into make.powerapps.com or flow.microsoft.com to create a flow, a Microsoft Power Automate free license is automatically added to their set of licenses (if they didn’t already have one assigned to them). However, when flows are created on a user’s behalf by a malicious tab, they don’t have the license assigned to them. This license status can be cross referenced with which users have flows created under their name at admin.powerplatform.microsoft.com

Press enter or click to view image in full size
Press enter or click to view image in full size
organization admin portal

Notice that Bad User has logged into the flow.microsoft.com web interface, but Good User, despite having flows in their name listed in admin.powerplatform.microsoft.com, does not show as having a license for Power Automate. This could indicate that the flows were not created intentionally by Good User.

Luckily, the attack is limited to authenticated users within a Teams organization who have the ability to create Power Apps tabs, which means it can’t just be exploited by an untrusted/unauthenticated attacker. However, the permission to create these tabs is enabled by default, so it may be a good idea to consider limiting apps by default and enable them on request.

Takeaways

While that was a long and not quite straightforward attack, the potential impact of such an attack could be huge, especially if it happens to hit an organization administrator. That such a small initial bug (the improper validation of the make.powerapps.com domain) could be traded-up until an attacker is exfiltrating emails, Teams messages, OneDrive and SharePoint files is definitely concerning. It means that even a small bug in a not-so-common service like Microsoft Power Apps could lead to the compromise of many other services by way of token bundles and first party logins for connectors.

So if you happen to find a small bug in one service, see how far you can take it and see if you can trade a small bug for a big impact. There are likely other creative and serious potential attacks we didn’t explore with all of the potential access tokens we were able to steal. Let me know if you spot one 🙂.

Thanks for reading!
