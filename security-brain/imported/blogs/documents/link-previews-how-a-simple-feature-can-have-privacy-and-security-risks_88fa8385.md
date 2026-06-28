---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-25_link-previews-how-a-simple-feature-can-have-privacy-and-security-risks.md
original_filename: 2020-10-25_link-previews-how-a-simple-feature-can-have-privacy-and-security-risks.md
title: 'Link Previews: How a Simple Feature Can Have Privacy and Security Risks'
category: documents
detected_topics:
- mobile-security
- sso
- command-injection
- automation-abuse
- information-disclosure
- api-security
tags:
- imported
- documents
- mobile-security
- sso
- command-injection
- automation-abuse
- information-disclosure
- api-security
language: en
raw_sha256: 88fa8385dd4b4add0e5fd6c3eb3fb7beb9c8d43cc2383adfe8287b33d583c661
text_sha256: bf2f295fedca18734de0440e69fd18003f0b42ef61c1db106ea65a4da945348c
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Link Previews: How a Simple Feature Can Have Privacy and Security Risks

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-25_link-previews-how-a-simple-feature-can-have-privacy-and-security-risks.md
- Source Type: markdown
- Detected Topics: mobile-security, sso, command-injection, automation-abuse, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `88fa8385dd4b4add0e5fd6c3eb3fb7beb9c8d43cc2383adfe8287b33d583c661`
- Text SHA256: `bf2f295fedca18734de0440e69fd18003f0b42ef61c1db106ea65a4da945348c`


## Content

---
title: "Link Previews: How a Simple Feature Can Have Privacy and Security Risks"
page_title: "Link Previews: How a Simple Feature Can Have Privacy and Security Risks | Mysk Blog – In-Depth Cybersecurity & Mobile App Privacy Research"
url: "https://www.mysk.blog/2020/10/25/link-previews/"
final_url: "https://mysk.blog/2020/10/25/link-previews/"
authors: ["Talal Haj Bakry (@parasarora06)", "Tommy Mysk"]
programs: ["Discord", "Meta / Facebook", "Google", "LINE", "LinkedIn", "Slack", "Twitter", "Zoom"]
bugs: ["Information disclosure"]
publication_date: "2020-10-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4180
---

#  [Link Previews: How a Simple Feature Can Have Privacy and Security Risks](https://mysk.blog/2020/10/25/link-previews/)

2020-10-25by [Talal Haj Bakry](https://x.com/hajbakri) and [Tommy Mysk](https://x.com/tommymysk)

Link previews in chat apps can cause serious privacy problems if not done properly. We found several cases of apps with vulnerabilities such as: leaking IP addresses, exposing links sent in end-to-end encrypted chats, and unnecessarily downloading gigabytes of data quietly in the background.

We think link previews are a good case study of how a simple feature can have privacy and security risks. We’ll go over some of the bugs we found while investigating how this feature is implemented in the most popular chat apps on iOS and Android.

##  Table of Contents 

  * Spoiler
  * What are link previews?
  * Approach 0: Don’t generate a link preview 👍
  * Approach 1: The sender generates the preview ✅
  * Approach 2: The receiver generates the preview 😱
  * Approach 3: A server generates the preview 🤔
  * Digging Deeper
  * Unauthorized Copies of Private Information
  * Getting Servers to Download Large Amounts of Data
  * Crashing Apps and Draining the Battery
  * Exposing IP Addresses
  * Leaking Encrypted Links
  * Running Potentially Malicious Code on Link Preview Servers
  * App Developers Respond to our Findings
  * Discord
  * Facebook Messenger and Instagram
  * Google Hangouts
  * LINE 👕👕
  * LinkedIn
  * Slack
  * Twitter
  * Viber
  * Zoom
  * █████████
  * ██████
  * Where to go from here?
  * Boring Yet Necessary Information

**UPDATE (February 5, 2021)** : Facebook disabled link previews in Europe as the feature doesn’t comply with the regulations in Europe. Facebook Messenger and Instagram will no longer display link previews in chats for users in Europe.

[ ![](/assets/img/common/psylo-iOS-Default-1024x1024@1x.webp) ](https://apps.apple.com/app/psylo-private-browser-proxy/id6741358035)

Like our research? Try Psylo.

**Psylo** is our privacy-first browser for iOS and iPadOS, with a built-in proxy network, per-tab isolated web sessions, and anti-fingerprinting. Using it helps fund more work like this.

[Read why we built it →](/2025/06/17/introducing-psylo/)

[Download Psylo →](https://apps.apple.com/app/psylo-private-browser-proxy/id6741358035)

## Spoiler#

Instagram servers download any link sent in Direct Messages even if it’s 2.6 GB

How hackers can run any JavaScript code on Instagram servers

## What are link previews?#

You’ve probably noticed that when you send a link through most chat apps, the app will helpfully show a preview of that link.

Whether it’s a news article, a Word or PDF document, or a cute gif, you’ll see a short summary and a preview image inline with the rest of the conversation, all without having to tap on the link. Like so:

![Link previews in Signal](/wp-content/uploads/2020/10/link_preview_example_signal-576x1024.png)

![](/wp-content/uploads/2020/10/link_preview_example_signal-576x1024.png) Link previews in Signal

Sounds like a nice feature, doesn’t it? But could a simple feature like this come with a few unexpected privacy and security concerns?

Let’s take a step back and think about how a preview gets generated. How does the app know what to show in the summary? It must somehow automatically open the link to know what’s inside. But is that safe? What if the link contains malware? Or what if the link leads to a very large file that you wouldn’t want the app to download and use up your data?

Let’s go over the different approaches that an app could take to show a link preview.

## Approach 0: Don’t generate a link preview 👍#

This one is straightforward: Don’t generate a preview at all. Just show the link as it was sent. This is the safest way to handle links, since the app won’t do anything with the link unless you specifically tap on it.

In our testing, the apps listed below follow this approach:

  * Signal (if the link preview option is turned **off** in settings)
  * Threema
  * TikTok
  * WeChat

## Approach 1: The sender generates the preview ✅#

In this approach, when you send a link, the app will go and download what’s in the link. It’ll create a summary and a preview image of the website, and it will send this as an attachment along with the link. When the app on the receiving end gets the message, it’ll show the preview as it got from the sender without having to open the link at all. This way, the receiver would be protected from risk if the link is malicious.

This approach assumes that whoever is sending the link must trust it, since it’ll be the sender’s app that will have to open the link.

In our testing, the apps listed below follow this approach:

  * iMessage
  * Signal (if the link preview option is turned **on** in settings)
  * Viber
  * WhatsApp

## Approach 2: The receiver generates the preview 😱#

This one is bad. This approach means that whenever you receive a link from someone, your app will open the link automatically to create the preview. This will happen before you even tap on the link, you only need to see the message.

What’s wrong with this approach?

Let’s briefly explain what happens when an app “opens” a link. First, the app has to connect to the server that the link leads to and ask it for what’s in the link. This is referred to as a GET request. In order for the server to know where to send back the data, the app includes your phone’s [IP address](https://en.wikipedia.org/wiki/IP_address) in the GET request. Normally, this would be fine if you know that you’re planning on opening the link.

But, what if an attacker wants to know your approximate location without you noticing, down to a city block?

If you’re using an app that follows this approach, all an attacker would have to do is send you a link to their own server where it can record your IP address. Your app will happily open the link even without you tapping on it, and now the attacker will know where you are.

You can see for yourself how an [IP address can determine your approximate location](https://www.maxmind.com/en/locate-my-ip-address).

Not only that, this approach can also be a problem if the link points to a large file, like a video or a zip file. A buggy app might try to download the whole file, even if it’s gigabytes in size, causing it to use up your phone’s battery and data plan.

Our testing _did_ find two apps that followed this approach:

  * ██████████████████
  * ██████████████████████

We reported this problem to the security teams at ████████ and ██████, and we’re happy to report that both apps have been fixed before we published this blog post. (Actually, ██████ is still in the process of fixing the issue, hence their name is redacted until a fix is deployed).

## Approach 3: A server generates the preview 🤔#

This takes the “middle” approach, quite literally. When you send a link, the app will first send the link to an external server and ask it to generate a preview, then the server will send the preview back to both the sender and receiver.

At first glance this seems sensible. Neither the sender nor receiver will open the link, and it avoids the IP leaking problem in [_Approach 2_](/2020/10/25/link-previews/#approach2).

But say you were sending a private Dropbox link to someone, and you don’t want _anyone_ else to see what’s in it. With this approach, the server will need to make a copy (or at least a partial copy) of what’s in the link to generate the preview. Now the question is: Does the server keep that copy? If so, how long does it keep it for? What else do these servers do with this data?

This approach shouldn’t work for apps that use [end-to-end encryption](https://en.wikipedia.org/wiki/End-to-end_encryption), where no servers in between the sender and receiver should be able to see what’s in the chat (at least in theory, anyway).

These were some of the apps that followed this approach, although they differ significantly in how their servers opened links:

  * Discord
  * Facebook Messenger
  * Google Hangouts
  * Instagram
  * LINE (this one actually deserves a 🤬, but we’ll get to it later)
  * LinkedIn
  * Slack
  * Twitter
  * Zoom
  * █████████

## Digging Deeper#

Now that we’ve covered the basic approaches to generate link previews, we can go over the more specific details of the risks and the privacy implications we’ve discovered. Here we’ll describe each of the risks we found in our testing:

### Unauthorized Copies of Private Information#

Links shared in chats may contain private information intended only for the recipients. This could be bills, contracts, medical records, or anything that may be confidential. Apps that rely on servers to generate link previews ([_Approach 3_](/2020/10/25/link-previews/#approach3)) maybe be violating the privacy of their users by sending links shared in a private chat to their servers.

How so? Although these servers are trusted by the app, there’s no indication to users that the servers are downloading whatever they find in a link. Are the servers downloading entire files, or only a small amount to show the preview? If they’re downloading entire files, do the servers keep a copy, and if so for how long? And are these copies stored securely, or can the people who run the servers access the copies?

Also, some countries have restrictions on where user data can be collected and stored, most notably in the European Union as enforced by the [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation).

In our testing, apps vary widely in how much data gets downloaded by their servers. Here’s a rundown of what we found:

  * **Discord:** Downloads up to 15 MB of any kind of file.
  * **Facebook Messenger:** Downloads entire files if it’s a picture or a video, even files _gigabytes_ in size. * 👋
  * **Google Hangouts:** Downloads up to 20 MB of any kind of file.
  * **Instagram:** Just like Facebook Messenger, but not limited to any kind of file. The servers will download anything no matter the size.* 👋
  * **LINE:** Downloads up to 20 MB of any kind of file. (This one still deserves a big 👎 as we’ll discuss later)
  * **LinkedIn:** Downloads up to 50 MB of any kind of file.
  * **Slack:** Downloads up to 50 MB of any kind of file.
  * **Twitter:** Downloads up to 25 MB of any kind of file.
  * **Zoom:** Downloads up to 30 MB of any kind of file.
  * ████████: ███████████████████████

(👋 We did contact Facebook to report this problem, and they told us that they consider this to be working as intended.)

Though most of the app servers we’ve tested put a limit on how much data gets downloaded, even a 15 MB limit still covers most files that would typically be shared through a link (most pictures and documents don’t exceed a few MBs in size). So if these servers do keep copies, it would be a privacy nightmare if there’s ever a data breach of these servers. This is especially a concern for business apps like Zoom and Slack.

Slack, for example, has confirmed that they only cache link previews for [around 30 minutes](https://api.slack.com/robots).

So that secret design document that you shared a link to from your OneDrive, and you thought you had deleted because you no longer wanted to share it? There might be a copy of it on one of these link preview servers.

### Getting Servers to Download Large Amounts of Data#

As we covered in the previous section, apps that follow [_Approach 3_](/2020/10/25/link-previews/#approach3) will rely on servers to generate link previews. Most of these servers will limit how much data gets downloaded, since downloading too much data could in theory use up a server’s capacity and cause service disruptions.

But as we highlighted in the last section, there were two apps that stood out in our testing: Facebook Messenger and Instagram, whose servers would download even very large files.

It’s still unclear to us why Facebook servers would do this when all the other apps put a limit on how much data gets downloaded.

### Crashing Apps and Draining the Battery#

In [_Approach 1_](/2020/10/25/link-previews/#approach1) and [_Approach 2_](/2020/10/25/link-previews/#approach2), the apps will open the link to generate a link preview when sending or receiving a link. In most cases, the apps wouldn’t have to download a lot of data to show the preview, at least if done properly. The problem arises when the app puts no limit on how much data gets downloaded when generating a preview.

Let’s say someone sent you a link to a _really large_ picture like this [1.38 GB picture](http://www.spitzer.caltech.edu/glimpse360/raw/mosaic_000.tif) of the Milky Way (if you’re using data, _don’t_ tap on it!), a buggy app that follows [_Approach 2_](/2020/10/25/link-previews/#approach2) will attempt to download the whole file on your phone, draining your battery and using up your data. This could also lead your app crashing if it doesn’t know how to deal with large files.

Before they were fixed, both █████████ and ████████ apps had this problem. Viber is still vulnerable to this problem.

### Exposing IP Addresses#

As we explained earlier, in order to open a link your phone has to communicate with the server that the link points to. Doing so means that the server will know the IP address of your phone, which could reveal your approximate location. Normally, this wouldn’t be much of a problem if you can avoid tapping on links you believe to be malicious.

In [_Approach 1_](/2020/10/25/link-previews/#approach1), where the sender’s phone opens the link to generate the preview, the server will know the sender’s IP. This might not be a problem if we can assume that the sender trusts the link that they’re sending, since they’re the ones taking action to send a link.

[_Approach 2_](/2020/10/25/link-previews/#approach2), however, is entirely unsafe. Since the receiver’s phone will be opening the link to generate the preview, the receiver’s IP will be known to the server. This would happen without any action taken by the receiver, and this can put them in danger of having their location exposed to the server without their knowledge.

███████████████████████████████████████████████████████████████████████████████████████████████████.

### Leaking Encrypted Links#

Some chat apps encrypt messages in such a way that only the sender and receiver can read the messages, and no one else (not even the app’s servers). This is referred to as [end-to-end encryption](https://en.wikipedia.org/wiki/End-to-end_encryption). Among the apps we tested, these were the ones that utilized this type of encryption:

  * iMessage
  * LINE
  * Signal
  * Threema
  * Viber
  * WhatsApp

Since only the sender or receiver can read encrypted messages and the links contained in them, [_Approach 3_](/2020/10/25/link-previews/#approach3) shouldn’t be possible in these apps since it relies on having a server to generate link previews.

But, didn’t we say that LINE followed [_Approach 3_](/2020/10/25/link-previews/#approach3)?

Well, it appears that when the LINE app opens an encrypted message and finds a link, it sends that link to a LINE server to generate the preview. We believe that this defeats the purpose of end-to-end encryption, since LINE servers know all about the links that are being sent through the app, and who’s sharing which links to whom.

Basically, if you’re building an end-to-end encrypted app, please don’t follow [_Approach 3_](/2020/10/25/link-previews/#approach3).

### Running Potentially Malicious Code on Link Preview Servers#

Most websites these days contain Javascript code to make them more interactive (and sometimes to show you ads and track you, but that’s a topic for another day). When generating link previews, no matter which of the above approaches is followed, it’s a good idea to avoid running any code from these websites, since as a service provider you can’t trust code that may be found in all the random links that get shared in chats.

We did find, however, at least two major apps that did this: Instagram and LinkedIn. We tested this by sending a link to a website on our server which contained JavaScript code that simply made a callback to our server. We were able to confirm that we had at least 20 seconds of execution time on these servers. It may not sound like much, and our code didn’t really do anything bad, but [hackers can](https://www.csoonline.com/article/3253572/what-is-cryptojacking-how-to-prevent-detect-and-recover-from-it.html) [be creative](https://react-etc.net/entry/exploiting-speculative-execution-meltdown-spectre-via-javascript).

## App Developers Respond to our Findings#

### Discord#

Discord follows [_Approach 3_](/2020/10/25/link-previews/#approach3), and their servers download up to 15 MB to generate link previews. However, we still have concerns about how long this data gets stored on their servers.

We contacted Discord to report our findings on September 19th, 2020, but we have not received a response from them.

### Facebook Messenger and Instagram#

Facebook Messenger and Instagram Direct Messages follow [_Approach 3_](/2020/10/25/link-previews/#approach3), and since they are both owned and operated by Facebook they actually share the same server infrastructure. These servers were the only ones in our testing that put no limit on how much data gets downloaded.

To demonstrate this, we hosted a 2.6 GB file on our server, and we sent a link to that file through an Instagram DM. Since the file was on our server, we were able to see who’s downloading the file and how much data gets downloaded in total.

The moment the link was sent, _several_ Facebook servers immediately started downloading the file from our server. Since it wasn’t just one server, that large 2.6 GB file was downloaded several times. In total, approximately **_24.7 GB_** of data was downloaded from our server by Facebook servers.

This was so surprising to us, so we had to take a video of what we saw:

Instagram servers download any link sent in Direct Messages even if it’s 2.6 GB

As we mentioned earlier, Facebook was given a noticed of these issues when we submitted two reports to them along with the videos on September 12th, 2020.

Facebook servers download any link sent in Facebook Messenger even if it’s 2.6 GB

How hackers can run any JavaScript code on Instagram servers

### Google Hangouts#

Google Hangouts follows [_Approach 3_](/2020/10/25/link-previews/#approach3), and their servers download up to 20 MB to generate link previews. Again, there is the concern about how long this data gets stored on their servers.

We submitted a report to Google on September 16th, 2020, but we have not received a response from them.

### LINE 👕👕#

Even though LINE is an end-to-end encrypted chat app, they do forward links sent in a chat to an [external server](http://poker.line.naver.jp) that generates link previews. This server also forwarded the IP addresses of both the sender and receiver to that link. 🤦‍♀️

We sent a report with our findings to the LINE security team. They agreed with us that their servers shouldn’t be forwarding the IP addresses of their users to generate link previews, but they still think it’s acceptable for an end-to-end encrypted chat app to use an external server to generate link previews. They have however updated [their FAQ](https://help.line.me/line/android/pc?lang=en&contentId=20005811) to include this information and to show how to disable link previews.

As of versions 10.18.0 for Android and 10.16.1 for iOS, the apps no longer leak IP addresses when generating link previews.

LINE leaks IP addresses of users and bypasses end-to-end encryption ??

### LinkedIn#

LinkedIn Messages follows [_Approach 3_](/2020/10/25/link-previews/#approach3), and their servers download up to 50 MB to generate link previews. But their servers were vulnerable to running Javascript code, which allowed us to bypass the 50 MB download limit. We also had concerns about how long the link preview data gets stored on their servers.

We sent a report with our findings to the LinkedIn security team on September 16th, 2020 but we have yet to receive a response from them at the time of publishing this blog post.

How hackers can run any JavaScript code on LinkedIn servers

### Slack#

Slack follows [_Approach 3_](/2020/10/25/link-previews/#approach3), and their servers download up to 50 MB to generate link previews. However, we are still concerned about how long this data gets stored on their servers, especially since Slack is used primarily by businesses which may be sharing sensitive or confidential links through chats and channels.

Slack reported to us that link previews are only cached for approximately 30 minutes. This is also confirmed in [their documentation](https://api.slack.com/robots).

### Twitter#

Twitter Direct Messages follows [_Approach 3_](/2020/10/25/link-previews/#approach3), and their servers download up to 25 MB to generate link previews. There is still the problem of how long this data gets stored on their servers.

We contacted Twitter and they told us that this is working as intended. They have not disclosed how long the link preview data is kept for.

### Viber#

Viber is end-to-end encrypted and follows [_Approach 1_](/2020/10/25/link-previews/#approach1), where the sender would generate the link preview. Though we did find a bug: if you send a link to a large file, your phone will automatically try to download the whole file even if it’s several gigabytes in size.

It’s also worth mentioning that even though Viber chats are end-to-end encrypted, tapping on a link will cause the app to forward that link to Viber servers for the purposes of fraud protection and personalized ads. You can find more info about this on their [support website](https://help.viber.com/en/article/what-happens-when-you-tap-a-link-inside-a-viber-message).

A bug in Viber causes the app to download large files even gigabytes in size

### Zoom#

Zoom follows [_Approach 3_](/2020/10/25/link-previews/#approach3), and their servers download up to 30 MB to generate link previews. However, we still have concerns about how long this data gets stored on their servers, especially since Zoom is used primarily by businesses which may be sharing sensitive or confidential links through chats.

We submitted a report to Zoom on September 16th, 2020, and they have told us that they’re looking into this issue and that they’re discussing ways to ensure user privacy.

### █████████#

██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████.

███████████████████████████████████████████████████████████████.

██████████████████████████████████████████████████████████████████████████████████████████.

### ██████#

██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████.

████████████████████████████████████████████████████████████████████.

## Where to go from here?#

Since we’re only two people doing this research in our spare time, we could only cover a small set of the millions of apps out there. Link previews aren’t just limited to the handful of chat apps we looked at: there are many email apps, business apps, dating apps, games with built-in chat, and other kinds of apps that could be generating link previews improperly, and may be vulnerable to some of the problems we’ve covered here.

We think there’s one big takeaway here for developers: Whenever you’re building a new feature, always keep in mind what sort of privacy and security implications it may have, especially if this feature is going to be used by thousands or even millions of people around the world. Link previews are nice a feature that users generally benefit from, but here we’ve showcased the wide range of problems this feature can have when privacy and security concerns aren’t carefully considered.

If you’re not a developer, we hope this report gives you an appreciation for the subtleties of the small differences in the same exact feature, and how these differences can have a massive impact on security and privacy.

![](/wp-content/uploads/2020/10/link-preview-comparison01-1024x548.png) Comparison of all the apps we tested

## Boring Yet Necessary Information#

Here’s the table summarizing all the apps we tested and their version numbers:

App Name | iOS Version | Android Version  
---|---|---  
Discord | 39.0 | 38.4  
Facebook Messenger | 280.0.0.32.106 | 8.61.0  
Google Hangouts | 35.0.324846370 | 35.0.327050771  
Instagram | v158.1.0.29.120 | 158.0.0.30.123  
LINE | 10.14.0 | 10.15.2  
LinkedIn | 9.16.387 | 4.1.489  
Slack | 20.09.10 | 20.09.10.0  
Twitter | 8.37.1 | 8.63.0-release.00  
Viber | 13.8.0 | 13.8.1.0  
Zoom | 5.2.2 (45104.0831) | 5.2.2 (45092.0831)  
██████ | ██████ | ██████  
██████ | ██████ | ██████  
  
[ ![](/assets/img/common/psylo-iOS-Default-1024x1024@1x.webp) ](https://apps.apple.com/app/psylo-private-browser-proxy/id6741358035)

Found this research useful?

Help fund more of it by trying **Psylo** , our privacy-first browser for iOS and iPadOS — with a built-in proxy network, per-tab isolated web sessions, and anti-fingerprinting.

[Read why we built it →](/2025/06/17/introducing-psylo/)

[Download Psylo →](https://apps.apple.com/app/psylo-private-browser-proxy/id6741358035)
