---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-04_cross-tenant-information-disclosure-unraveling-microsoft-connections-custom-conn.md
original_filename: 2023-08-04_cross-tenant-information-disclosure-unraveling-microsoft-connections-custom-conn.md
title: 'Cross-Tenant Information Disclosure: Unraveling Microsoft Connections, Custom
  Connectors, and OAuth 2.0 in Power Automate'
category: documents
detected_topics:
- oauth
- automation-abuse
- access-control
- command-injection
- otp
- csrf
tags:
- imported
- documents
- oauth
- automation-abuse
- access-control
- command-injection
- otp
- csrf
language: en
raw_sha256: a8e7d8ba26254081f01f3e96b555c8d0a1ca03d549c5da7fa9df68d15800ca16
text_sha256: 2c49f41fed3141247a0b8ee1a18f0594ecdba5d69fd108fcd1502af801379221
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Cross-Tenant Information Disclosure: Unraveling Microsoft Connections, Custom Connectors, and OAuth 2.0 in Power Automate

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-04_cross-tenant-information-disclosure-unraveling-microsoft-connections-custom-conn.md
- Source Type: markdown
- Detected Topics: oauth, automation-abuse, access-control, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `a8e7d8ba26254081f01f3e96b555c8d0a1ca03d549c5da7fa9df68d15800ca16`
- Text SHA256: `2c49f41fed3141247a0b8ee1a18f0594ecdba5d69fd108fcd1502af801379221`


## Content

---
title: "Cross-Tenant Information Disclosure: Unraveling Microsoft Connections, Custom Connectors, and OAuth 2.0 in Power Automate"
url: "https://fatnassifiras.medium.com/cross-tenant-information-disclosure-unraveling-microsoft-connections-custom-connectors-and-oauth-6487321d28b3"
authors: ["Firas Fatnassi (@Fatnass1F1ras)"]
programs: ["Microsoft"]
bugs: ["OAuth", "Cross-tenant vulnerability"]
publication_date: "2023-08-04"
added_date: "2023-08-08"
source: "pentester.land/writeups.json"
original_index: 881
scraped_via: "browseros"
---

# Cross-Tenant Information Disclosure: Unraveling Microsoft Connections, Custom Connectors, and OAuth 2.0 in Power Automate

Cross-Tenant Information Disclosure: Unraveling Microsoft Connections, Custom Connectors, and OAuth 2.0 in Power Automate
Firas Fatnassi
Follow
10 min read
·
Aug 4, 2023

65

1

This article is about a vulnerability I recently discovered in the Microsoft Power Automate Platform, which involved chaining exploits between two authentication features.

Power Automate: Simplify your workflows and boost productivity with automated processes effortlessly.

Connections: Connections serve as bridges that allow Power Automate (Microsoft’s automation platform) to communicate with external services or applications. They enable data exchange and actions between Power Automate and external services or applications, such as Microsoft 365, Dropbox, Salesforce, etc.

Custom Connectors: A custom connector is a way to create your own bridge between Power Automate and a specific service or application that isn’t natively supported. It allows you to build custom integrations, enabling Power Automate to interact with your unique systems or APIs. This extends the capabilities of Power Automate beyond the standard connectors that come built-in.

In order to fully understand this write-up, you need to have a basic understanding of how the OAuth 2.0 protocol works. It’s relatively simple, and I’ll provide a brief overview. If you are already familiar with it, feel free to skip ahead to the issue.

What is OAuth 2.0 and how does it work:
Press enter or click to view image in full size
https://datatracker.ietf.org/doc/html/rfc6749#section-4.1
OAuth 2.0 is a widely used security protocol enabling applications (Power Automate in this write-up’s case) to access resources on behalf of users without exposing their login credentials.
There are 3 flows in OAuth 2.0; in this context, we are concerned with the code flow.
When the flow begins, you will be redirected to the authorization server, where you need to authenticate (if you haven’t already) and consent to the authorization request. After completing this step, you will be redirected back to the original page in your browser, triggering the client (Power Automate) to exchange the received code for an access token from the authorization server. Once the authorization server validates everything, it will generate the access token.

Bonus: At least for me when I was learning about the OAuth 2.0 protocol, I used to wonder why there’s an extra step of getting a code and then exchanging it for a token (Which actually can be avoided using another flow out of the 3). As it turns out, this additional step serves as an important security layer.

Imagine using the access token flow directly, where the token is returned in the second step after user consent. If someone is standing behind you at a coffee shop and manages to capture the code while you’re authorizing access, or if you use a shared computer, they could potentially gain access to your resources later using that token.

However, with the code flow, even if someone captures the code, they can’t do anything with it. To exchange it for an access token, the client needs to send both the code and its client_secret to the authorization server securely. The client_secret is a secret known only by the client and the authorization server and the request is done via a back-channel you won’t even see it.

Now that we know how OAuth2 works let’s jump into the real work.

Okay, so creating connections is pretty straightforward, You just go to the connections page pick an application, and go through the whole Oauth2 flow from signing-in to consenting…

Once you choose an application to connect with, and you click on the “Create” button the flow starts.

Press enter or click to view image in full size
Connection auth flow.
Upon clicking the create “Button” a request to create a consent link is triggered.
A get request from the server is sent to that consent link that was returned in the response.
Then we are redirected to a small authentication pop-up to authenticate ourselves.
Once we choose which account we want to use, 3 other requests are initiated to finish the OAuth 2.0 flow.
Press enter or click to view image in full size
Rest of the flow.
Here couple of back-and-forth redirects between the client and authZ server to exchange the code with the final code (Access Token normally but here it is called code as well so to distinguish I’ll call it final code; final code = access token). Also in a normal scenario, it should be 1 request but it seems here it’s load balancing stuff as you can see the domain was global at first and then got changed to Canada. I think it’s to make sure we’re dealing with the closest AuthZ server for performance purposes.
Once we get the final code a POST request is sent to the confirmConsentCodeendpoint to link the final code with the connection. In the normal flow, this would be using the access token returned from the AuthZ server to access resources from the resource server.

That was a walk-through on how connections are created. Now, out of all the requests only 1 caught my attention, The POST request in the 1st image which is responsible for creating the consentLinkbecause in its body it contains a redirectUrl parameter meaning we control to which URL we can get redirected. So, here I thought of 2 things:

Change the redirectUrl to my controlled server (typical OAuth 2.0 attack) and send the link to the victim to leak its code. Unfortunately, that did not work because as soon as the system flags that the URL is changed it’ll display the following to the victim:
Press enter or click to view image in full size

Which obviously exposes us.

2. Here, I thought maybe I could CSRF the victim by just sending him the consentLink with the default URL, assuming that if he finishes the flow his account will get linked to my connection and thus I can access his information. This didn’t work as well because at some point after the victim chose which account to authenticate with, the screen froze at a loading page:

Press enter or click to view image in full size

Here, I would say it's related to front-end stuff as the flow wasn’t initiated from the victim’s browser. Consequently, the front-end doesn't know what to do. Like what requests to initiate at every point. Usually, there are some promises that handle this but it would only work if the victim himself clicked Create the button at the first step from his browser so that frontend and backend are synced together which wasn’t the case. Dead-end huh? That’s what I thought, also, but I knew there was something.

Here, comes the custom connectors I told you about above.

Creating a custom connector is quite complicated as you have many options on how you want to connect the Power Automate platform to your custom app or whatever. But we will go with the most basic one which actually creates a blank custom connector and then selects the OAuth 2.0. I believe if you understood the connections thing, just reading how a custom connector is created you would notice the issue.

Before we start describing the custom connector creation process. One thing to know is that connections are built on top of custom connectors. It’s just that the Power Automate Team collected the most common and used applications and then made them ready for us. But, still, they made the custom connectors feature public so that we can connect to other applications.

Press enter or click to view image in full size

Once you click on continue you will be redirected to another page where you will fill in the required information.

Press enter or click to view image in full size

What happens in the Security tab is really what interests us. As you can see you can provide OAuth 2.0 details of your custom application. Including Client ID, Client Secret…

The client_id is a fixed, unique identifier for a client application in OAuth 2.0. Sounds good? So I was thinking what would happen if I specify the Microsoft Teams client_id there? Well, that’s what this attack is about.

Get Firas Fatnassi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So I filled:

client_id with Microsoft Teams.
client_secret with anything as it does not matter.
authorization_url with `https://login.windows.net/common/oauth2/authorize`, since that’s a known Auth server and is aware of the Microsoft Teams `client_id` it should be registered there. Thus, it’ll happily generate a code for us.
token_url with our controlled server, this is to leak the code, because if you remember in the OAuth 2.0 code flow, after obtaining the code, the client will send a request to the Auth server /token endpoint representing the code received from the authorization_server as an exchange for the access token (Final code) here. But keep in mind here we are putting our controlled server so it’s not really an Auth server URL. This is just to get the code as I said.
refresh_url does not matter. Below is how it looks after filling in the information.
Press enter or click to view image in full size

Finally, we create the connector. And jump into the Test tab.

Press enter or click to view image in full size

As you can see in the above image in the Test tab we can make a new connection to test if our custom connector is working. If you look closely at the image you will see that it looks exactly like the flow of creating a connection (As I told connections are built on top of custom connectors).

After choosing an account in the Auth pop-up. I received the code in my webhook.

Press enter or click to view image in full size
Leaked code in our server logs.

Seems like we broke the feature. We managed to trick the Authorization server into generating an OAuth 2.0 code under the Microsoft Teams app, and we leaked it by injecting our controlled server as the token URL. Cool!

Basically, now if we want to attack someone we just send him the consentLink as it is with the default URL from the response without even the need to tamper with it. Once he follows the link we get a code that’s tied to his account session and belongs to the Microsoft Teams client (APP).

Here you would be asking why I even talked about normal connections if the exploit is in custom connectors. Well, you should also be asking what can I do with that code as I need an access token at the end to access things (Which is the final code in this context).

Remember the connections creation final process here is the image once again.

Press enter or click to view image in full size

Request number 23303 is the one responsible for exchanging the code with the final code. It looks like the following:

Press enter or click to view image in full size

As you can see you give it code it returns the final code in the Location header.

And then finally that code is used in a POST request that looks like the following to link it with the connection object:

Press enter or click to view image in full size

Just to not confuse you with the final code thing which you can see in the image above. If I had to guess how things are working in the background I would say that the final code is an identifier for the access token but it’s just used in the backend. We do not see it.

Okay, the attack scenario would look like the following:

The attacker initiates a connection creation process, during which he will capture and save 2 requests. The one responsible for exchanging the code with the final code (Access Token) and the one used to link that final code with the connection.
Then he creates a custom connector with the client_id of whatever app he wants to compromise the user in. (Just note that it has to be the same app he created a connection to in the first step).
Then he gets the consentLink from the Test tab by trying to create a new connection to that custom connector.
Put the link on his web page. Induce the user to visit it.
As soon as the user visits the page we receive the code in our webhook.
Use it with the first captured request as an exchange for the final code.
Then link the final code with the connection created in the first step.

To make things clear let’s say you want to compromise the victim's APP_1 account then you have to first create a connection to APP_1, then a custom connector with the APP_1 client_id.

The exploit web page would look like the following:

Press enter or click to view image in full size

Here I made an exploit to take over both SharePoint and teams. You can embed as many links as you want. And leak their codes then you have access to whatever information the victim had access to.

Takeaways from this vuln:
I spent around three days trying to demystify the flow of each feature and connecting the dots. Give it time.
Without a solid understanding of the OAuth 2.0 protocol, I wouldn’t have been able to exploit the vulnerability. RFCs are really helpful.

Shout-out to the MSRC team for handling and fixing the issue. As well as some fellows from the community for reviewing the draft of this write-up.

Twitter: https://twitter.com/Fatnass1F1ras
