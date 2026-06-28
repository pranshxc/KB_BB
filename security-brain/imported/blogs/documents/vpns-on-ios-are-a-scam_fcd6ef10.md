---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-20_vpns-on-ios-are-a-scam.md
original_filename: 2022-08-20_vpns-on-ios-are-a-scam.md
title: VPNs on iOS are a scam
category: documents
detected_topics:
- mobile-security
- sso
- command-injection
- automation-abuse
- api-security
- cloud-security
tags:
- imported
- documents
- mobile-security
- sso
- command-injection
- automation-abuse
- api-security
- cloud-security
language: en
raw_sha256: fcd6ef106ebdbaba74cd2207ceb72cfc2d9cb135b5a15a0579c763f6f7ca5487
text_sha256: bf4f79899963f3b029c437c682f2f4e9ebd60031ac4b67be7ca9dba402d2fdc5
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# VPNs on iOS are a scam

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-20_vpns-on-ios-are-a-scam.md
- Source Type: markdown
- Detected Topics: mobile-security, sso, command-injection, automation-abuse, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `fcd6ef106ebdbaba74cd2207ceb72cfc2d9cb135b5a15a0579c763f6f7ca5487`
- Text SHA256: `bf4f79899963f3b029c437c682f2f4e9ebd60031ac4b67be7ca9dba402d2fdc5`


## Content

---
title: "VPNs on iOS are a scam"
url: "https://www.michaelhorowitz.com/VPNs.on.iOS.are.scam.php"
final_url: "https://www.michaelhorowitz.com/VPNs.on.iOS.are.scam.php"
authors: ["Michael Horowitz (@defensivecomput)"]
programs: ["Apple"]
bugs: ["Privacy issue"]
publication_date: "2022-08-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2283
---

Michael Horowitz |  [Home](index.php) => VPNs on iOS are a scam ![](pix/printlogo.gif)  
---|---  
  
When printed, this page will be automatically re-formatted. There are no separate "Printer Friendly" versions of pages on this site. To preview the printed format, use Print Preview in your browser. 

[Formatted for Printing] | From the personal web site of Michael Horowitz  
---|---  
  
### VPNs on iOS are a scam

UPDATE HISTORY  
May 25, 2022 First published  
May 28, 2022 Totally re-wrote the Work-Arounds section  
May 30, 2022 Minor edits and a new section on Testing Airplane Mode  
May 31, 2022 Expanded the My Suggestion section at the end  
June 16, 2022 Added details on yet another test  
July 3, 2022 Added new section on the bottom about where things currently stand  
July 31, 2022: Two minor updates at the bottom of the page  
Aug 5, 2022: Added new TLDR intro  
Aug 8: Confirmed with iOS 15.6 - new section at the bottom  
Aug 10, 2022: minor updates  
Aug 14, 2022: Added two sentences about Tor in the Wrapping Up section  
Aug 15, 2022: Added a first look at the leaking domains to the Where This Stands section.  
Aug 17, 2022: In the TLDR section, added links to an Ars Technica article on this and to Hacker News comments. Added a link to a similar iOS VPN issue from 2018 in the Introduction section. Added confirmation of the problem from Windscribe in the Where This Stands section. Some minor edits.  
Aug 18, 2022: Minor edits thanks to reader feedback  
Aug 19, 2022: Added a response from Apple in the Where This Stands section and moved that section to the top of the page. Also added a new Tor vs. VPN section for some perspective. Moved the My Suggestion topic higher.  
Aug 20, 2022: New section added on Leaking Domain names  
Aug 21, 2022: New section added about the Disconnect Blog on Leaky iOS VPNs  
Aug 22, 2022: Minor addition to the Leaking Domain names section. Added my prediction in the Where This Stands section. Some minor edits.  
Aug 25, 2022: Added Facebook research to the Leaking Domain names section. Its off-topic, but interesting.  
Aug 27, 2022: Added a new section with a Wireshark examination of the leaking data  
Aug 31, 2022: Yet another Wireshark test/trace. No big woop.  
Sept 4, 2022: Documented yet another Wireshark test/trace, this time using the WireGuard app.  
Sept 16, 2022: Updated the Where This Stands section (at the bottom of the section).  
Sept 21, 2022: Updated the Where This Stands section to note that iPad OS v16 is not yet available for my iPad.  
Oct 12, 2022: Updated the Where This Stands section to put the most recent updates at the top. Also added the latest update: research by others that also found VPN leaks in iOS, this time with iOS 16. And, added an excellent article by IPVanish to the section, dated August 25th.  
Oct 14, 2022: Updated the Where This Stands section add a report (not from me) showing that an iOS 16 VPN leaks, even in Lockdown mode.  
Aug 23, 2023: Updated the Where This Stands section again with an article showing this is still a problem. 

### TL;DR

VPNs on iOS are broken. At first, they appear to work fine. The iOS device gets a new public IP address and new DNS servers. Data is sent to the VPN server. But, over time, a detailed inspection of data leaving the iOS device shows that the VPN tunnel leaks. Data leaves the iOS device outside of the VPN tunnel. This is not a classic/legacy DNS leak, it is a data leak. I confirmed this using multiple types of VPN and software from multiple VPN providers. The latest version of iOS that I tested with is 15.6.1. This data leak was [first publicized](https://protonvpn.com/blog/apple-ios-vulnerability-disclosure/) by ProtonVPN in March 2020 and iOS v13. (Added this section on Aug. 5, 2022)

August 17, 2022: Ars Technica picked this up: [VPN security - iOS VPNs have leaked traffic for more than 2 years, researcher claims](https://arstechnica.com/information-technology/2022/08/ios-vpns-still-leak-traffic-more-than-2-years-later-researcher-claims/). So too, did [Hacker News](https://news.ycombinator.com/item?id=32488308), [9to5mac.com](https://9to5mac.com/2022/08/18/ios-vpn-apps/), [The Register](https://www.theregister.com/2022/08/19/apple_ios_vpn/) (particularly well done article by Thomas Claburn), [HowToGeek](https://www.howtogeek.com/832559/are-vpns-broken-on-iphone/) and _many_ others. My 15 minutes of fame. 

### Introduction

The [VPN page](https://defensivecomputingchecklist.com/vpn.php) of my [DefensiveComputingChecklist.com](https://defensivecomputingchecklist.com) site has a section with assorted tires that can be kicked to verify that a VPN is working. Some things are obvious, like checking for a new public IP address, new DNS servers and checking that WebRTC is disabled. This blog is about a less than obvious VPN test, one that requires a professional class router to confirm. 

The basis for this is quite simple. Once a VPN connection (the official term is a "tunnel") is established, all data coming and going from the VPN-connected device is supposed to go through the VPN. Does it? That's what I set out to verify. Certainly _most_ data passes through the VPN tunnel, but I was curious about _all_ data.

Granted, some VPN software supports an option called split tunneling which breaks this simple rule, but that does not interest me. All VPN client software that I have seen, that offers split tunneling has it off by default. The three VPN apps that I tested with had it off by default, and I left it off. 

I set out to verify that the VPN tunnel is the all-consuming thing it's supposed to be. That resistance to it is futile. That the tunnel assimilates all the bits and bytes coming and going between the device in question and the Internet :-) I refer to "the tunnel" because the iPad I tested with is Wi-Fi only. Things are more complicated on an iPhone which does both Wi-Fi and 4G/5G/LTE. 

I don't come to the topic at random. In researching my [Defensive Computing with a VPN](https://defensivecomputingchecklist.com/vpn.php) writeup, I ran across a March 2020 blog by ProtonVPN, [VPN bypass vulnerability in Apple iOS](https://protonvpn.com/blog/apple-ios-vulnerability-disclosure/), that describes a bug in iOS 13 and 14. The nature of the bug is that the VPN tunnel does not assimilate all the bits. Some escape. The Borg would not be happy. 

Update. Aug 19, 2022: In May 2020, when iOS was at version 13.3.1, Mullvad had also warned about this: [iOS vulnerability puts VPN traffic at risk](https://mullvad.net/en/blog/2020/5/4/ios-vulnerability-puts-vpn-traffic-risk/). 

What ProtonVPN wrote about is a data leak, rather than a DNS leak. Connections that exist at the time the VPN tunnel is created, should be terminated and re-started so that they travel through the VPN tunnel. In iOS 13 and 14, this does not happen, at least not by default.

Interestingly, the Windscribe desktop VPN client software has an option for this, called "Kill TCP sockets after connection" (see [TCP Socket Termination](https://windscribe.com/support/article/20/tcp-socket-termination)). However, the option does not exist in their iOS software. I checked a handful of iOS VPN clients for other VPN providers and found none with an option about terminating existing connections/sockets when establishing the VPN tunnel.

I followed up on the ProtonVPN blog for a couple reasons. For one, it was last updated in October 2020 when iOS 14 was first released. iOS is now at version 15. And, the last update said that a new iOS feature would soon be included in their app to fix the problem. But, ProtonVPN never followed up on this. Did they add this new feature? Does it fix the problem? They left the issue hanging. On Aug 18, 2022, after this issue got some publicity, ProtonVPN again updated their blog, more on this below. 

Update Aug 17, 2022: After this blog posting was picked up by Ars Technica, I heard from Matt Volante who had written about iOS not using a VPN in a different use case. See [Trust broken when using VPN on iOS Exchange ActiveSync system client](https://medium.com/visitedspace/trust-broken-when-using-vpn-on-ios-exchange-activesync-system-client-e213bba4aafc) (Feb 12, 2018). He found iOS version 11.2.5 would use a cellular connection for Exchange ActiveSync communications, even when a device was VPN connected to Wi-Fi. Like me, he felt that the issue was in iOS, not in the two VPN client apps that he tested with. It turns out that VPN provider Disconnect has a very similar gripe and they blogged about it in March 2022. There is a whole section on the Disconnect blog below. 

When this topic got some publicity, Apple responded to me and said things are working as designed. So, there you go, I suppose you can stop reading here.

They also said they introduced a fix in iOS 14, which means VPNs were leaking on iOS 13 and earlier. But a couple (at least) VPN providers complain that the fix is partial and buggy. Again, more below. 

### WHERE THIS STANDS

August 1, 2023: [Removal of kill switch from our iOS app due to Apple IP leak issue](https://www.ivpn.net/blog/removal-of-kill-switch-from-our-ios-app-due-to-apple-ip-leak-issue/) by Juraj Hilje and Viktor Vecsei of IVPN. Quoting: _"When using Apple services on iOS 16+, a VPN connection does not fully protect your privacy against Apple. Even with an active VPN connection and kill switch enabled, traffic from your iOS 16+ device to Apple servers can leak outside the VPN tunnel and expose your local IP address to Apple. For this reason, during the next release we are removing the kill switch feature from the IVPN iOS app. Connections to non-Apple servers are not vulnerable to this leak, thus general privacy benefits of your VPN connection are unaffected."_ In simple terms, Apple is still sending data to their own servers outside the VPN tunnel. 

October 14, 2022: A new wrinkle, iOS 16 VPNs leak even in the new Lockdown Mode. See: [MacRumors: iOS 16 VPN Tunnels Leak Data, Even When Lockdown Mode Is Enabled](https://www.macrumors.com/2022/10/13/ios-16-vpns-leak-data-even-with-lockdown-mode/) by Hartley Charlton and [iPhone VPN Security Issues Persist in iOS 16, Researchers Claim](https://www.cnet.com/tech/services-and-software/report-iphone-vpn-security-issues-persist-in-ios-16/) by Attila Tomaschek of CNET. 

October 12, 2022: The issue of VPNs leaking on iOS has been taken up by others. See [iOS VPN apps have another flaw, shows new research: excluding many Apple apps](https://9to5mac.com/2022/10/12/ios-vpn-apps-2/) by Ben Lovejoy for 9to5Mac (Oct. 12, 2022) and [Most Apple apps on iOS 16 bypass VPN connections](https://appleinsider.com/articles/22/10/12/most-apple-apps-on-ios-16-bypass-vpn-connections) by Andrew Orr (Oct 12, 2022). Tommy Mysk ran a Wireshark trace on an iPhone running iOS 16. He found these Apple apps sending data outside the VPN tunnel: Apple Store, Clips, Files, Find My, Health, Maps, Settings and Wallet. I had also noticed that the App Store was a frequent leaker. He also found DNS leaks. He used a Mac for collecting data and thus was able to get a much larger sample, than I was able to. He did not write up a blog, but his [tweet about this](https://twitter.com/mysk_co/status/1579997801047822336) includes a video. 

\- - - - - - - - - - -

September 21, 2022: I tried to update my iPad to iOS version 16, but 15.7 is the latest and greatest, I can not yet test iOS 16.

September 16, 2022: Just thinking: 

  * What if this is a bug? What does it say about Apple that they can not or will not fix the problem? It's an obscure thing, so they can get away with leaving it broken. And, maybe that is the decision they have made. 
  * What if this is not a bug? What if Apple does not want to send some of their data traffic through a VPN? Maybe they judge their stuff too important to trust to a VPN tunnel that might experience technical problems even when the Internet connection is fine. 
  * Either way Apple looks bad. And, either way, nothing is likely to change.

August 25, 2022: An excellent article from VPN provider IPVanish: [iOS VPN leaks: why they happen and how to prevent exposure](https://www.ipvanish.com/blog/ios-vpn-leaks/). Quoting: _"IPVanish cannot fix the iOS VPN leaks (really no consumer VPN on the market can). We are limited to workarounds and tools that Apple provides us to build our applications. We attempted to use a few VPN features provided by Apple with little success since they break the overall user experience of the application. As this is an issue native to iOS, it’s up to Apple to address it. The IPVanish product team tried to do a proof of concept with the 'includeAllNetworks' flag enabled, but something as simple as a network change would often cause a crash or connection failure. Our tests found issues with underlying network protocols, leaving an overall buggy experience."_ They go into three different types of leaks and the solutions for each type. Great article. (added October 12, 2022)

August 22, 2022: What's next? My best guess is nothing. That is, I expect nothing to change and the issue of leaking VPNs will be forgotten. They will still leak, but iOS users will not know. Apple is too big for anyone to hold their feet to the fire. And, the topic is too obscure an issue for it to ever get much publicity again. VPN companies are unlikely to publicize the fact that their VPNs leak on iOS, though I suspect that many want to. Maybe, if a large group of them all complained together, that could shame Apple into doing the right thing. Maybe.

August 20, 2022: I feel sorry for many VPN companies as they are caught in the middle. At least some of them knew about iOS VPNs leaking, but what are they to do with this information? Sure, they can report it to Apple, but that was clearly shouting into the void. If they publicize the problem, they may well lose customers to VPN companies that say nothing. Worse, Apple may not appreciate the bad publicity and they may find their app banned from iOS app store. So, when ProtonVPN went public about the problem, that was an act of courage. Still, they did eventually drop the ball. Likewise, Disconnect (see below) also seems to be a whistleblower.

\- - - - - - - - - - - - - - - - - - - - - -

August 19, 2022: Apple responded to me yesterday. 

Strange timing, in that it happened just after this issue got some publicity. Very reminiscent of how Facebook responded [ just after their bad publicity](https://www.techdirt.com/2022/08/12/data-privacy-matters-facebook-expands-encryption-just-after-facebook-messages-obtained-via-search-warrant-used-to-charge-teen-for-abortion/) having to do with leaking abortion messages. 

The Apple response started with _"The behavior you are seeing is expected."_ Take a second to let that sink in. I did not know how right I was when picking a title for this page - VPNs on iOS are indeed a scam.

_Should_ it work this way is the real question. I think not and at least three VPN providers also feel this way. 

Then too, Apple could have said this in May or June or July or earlier this month. This blog posting has been public the whole time. 

Apple also said that the Always On VPN feature of MDM offers a fix. Mobile Device Management is over my head. It is used by large corporations to manage hundreds or thousands of iOS devices. That's pretty much everything I know about it. According to Apple, MDM lets the corporate IT techies force all data leaving an iOS device to go to the company. But, MDM is is not available to consumers. 

Finally, Apple mentioned an API option ("includeAllNetworks") that was introduced in iOS version 14 and pointed me to developer documentation at developer.apple.com. I am not an iOS developer, so I am not qualified to offer an opinion on this. Still, I can summarize. 

  1. The new option is on/off flag that indicates whether iOS sends all data through the VPN tunnel, or not. So, clearly iOS 13 and earlier were the Wild Wild West for VPNs. When both ProtonVPN and Mullvad blogged about VPNs leaking, they were referring to iOS version 13.
  2. The flag is OFF by default. Interesting choice for a company that sells their stuff based on security and privacy. 
  3. If the flag is ON, and the VPN connection dies, iOS drops all network traffic. A built in kill switch. Sounds great.

Apple suggested we ask our VPN providers if they are using this flag.

The flag is documented in a section on the NEVPNProtocol which is described as having settings common to both IKEv2 and IPsec VPN configurations.This begs the question: What about OpenVPN? What about WireGuard? I asked Apple this today. 

For some perspective, this is what ProtonVPN [wrote](https://protonvpn.com/blog/apple-ios-vulnerability-disclosure/) about iOS version 14 in October 2020: "Although Apple has not fixed the VPN bypass problem directly on iOS 14..." That's interesting. Apple says the issue is fixed in iOS 14, Proton says it is not. Proton went on to say that iOS 14 has a Kill Switch, but they did not provide details, so its not clear if they are referring to the flag that Apple mentioned yesterday. However, at the time, they expected that the Kill Switch would block existing connections when a VPN was enabled. 

Another development yesterday was that Proton updated their [blog posting](https://protonvpn.com/blog/apple-ios-vulnerability-disclosure/), the one that first went up in March 2020: 

_"Recent testing has shown that while the kill switch capability Apple provided to developers with iOS 14 does in fact block additional network traffic, certain DNS queries from Apple services can still be sent from outside the VPN connection."_

So, this complicates things a bit. It raises the question of whether the data leaking out of the VPN tunnel is from new connections to the outside world or whether it is left over from old connections that were initially made before the VPN tunnel was created. I don't know that anyone looking at router logs can tell. How much does this matter? Not sure.

It is not clear, to me at least, if they did some additional tests of their own, or whether they are referring to my testing. That they only refer to DNS makes me think they did their own testing.

Proton also said: _"We've raised this issue with Apple multiple times. Unfortunately, its fixes have been problematic. Apple has stated that their traffic being VPN-exempt is 'expected' ... We call on Apple to make a fully secure online experience accessible to everyone, not just those who enroll in a proprietary remote device management framework designed for enterprises."_

\- - - - - - - - - - - - - 

August 17, 2022: I had contacted tech support at Windscribe about this. In response, Yegor Sak, the Co-Founder of Windscribe, said that they are aware of this problem and they have submitted multiple reports to Apple. This was my first confirmation that it's not just me, that my iPad was not hit by sun spots and is the only one on the planet acting this way. 

August 15, 2022: I finally ran a different trace. This time, I used a pcWRT router which has Parental Controls. Part of the parental controls is a feature that shows the domains accessed by each device connected to the router. I set that up, then connected my iOS 15.6 iPad to the pcWRT router and made a WireGuard connection using ProtonVPN. As I used the iPad, the pcWRT router showed increasing requests to apple.com well after the VPN had been established. If I get a chance, I will add screen shots here.

August 10, 2022: I emailed [CISA](https://www.cisa.gov/) about this six times. No response. 

July 31, 2022: iOS 15.6 was released a couple days ago. My tests with this new version are below. Also, I recently learned that Apple owns all IP addresses that start with 17.

July 3, 2022: I first contacted Apple about this at the end of May 2022. Since then, there have been a number of emails between myself and the company (yes, plain old un-encrypted email - no security at all). To date, roughly five weeks later, Apple has said virtually nothing to me. They have not said whether they tried to re-create the problem. They have not said whether they agree on this being a bug. They have not said anything about a fix. 

It takes so little time and effort to re-create this, and the problem is so consistent, that if they tried at all, they should have been able to re-create it. None of my business. Maybe they are hoping, that like ProtonVPN, I will just move on and drop it. Dunno.

### Disconnect Blog on Leaky iOS VPNs

Added this section August 21, 2022

When this blog got some publicity, a couple people notified me about a blog that security company Disconnect wrote in March 2022. It too is about leaky VPNs on iOS. See [Leak advisory: Apple and *All* iOS App Developers Are Able to Unmask VPN Users](https://blog.disconnect.me/ios-vpn-leak-advisory/). 

The issue being discussed by Disconnect in more akin to what Matt Volante reported (above) than what I wrote about. Simply put, if a device is connected to both Wi-Fi and 4G/LTE/5G, then iOS allows both itself and any app that wants to, to bypass a Wi-Fi connected VPN and send data over the cellular connection. The simple solution is obvious, disable the Internet connection that is not being protect by a VPN. 

In the blog, Disconnect complains that there is nothing any VPN vendor can do to prevent this. So, they did what they could, they warn their customers as you can see in this [screen shot](https://disconnectblogimages.s3.amazonaws.com/advisory.jpg) that they published. 

The article goes into a lot of technical detail, mostly for app developers, on the multiple iOS APIs (Network.framework, MPTCP and Sockets) that allow apps to bypass a VPN. It also criticizes Apple, quite correctly in my opinion, for keeping this information from their millions of customers. I am starting to think of Apple like the Wizard of Oz, where the public persona is quite different from what's going on behind the curtain.

This Disconnect blog also touched on another topic, the "includeAllNetworks" flag that Apple mentioned to me a couple days ago as the cure-all for all diseases. Apparently it is buggy as heck. Other VPN providers have told me privately the same thing, but Disconnect goes into the buggy details in public. The flag is documented [here](https://developer.apple.com/documentation/networkextension/nevpnprotocol/3131931-includeallnetworks) and, as noted above, it was introduced in iOS 14.

On the up side, Disconnect says that it "stops the ability of Apple and third-party developers to exploit the cellular interface when a VPN is established." As for problems with it: 

  1. There is very limited documentation 
  2. It is not compatible with all VPN types (even I noticed this)
  3. It causes massive breakage
  4. In their testing, it was unusable

Yikes. There is a decision to be made, to trust Disconnect or Apple. Personally, I trust Disconnect. 

They even detail some of the bugs: 

  * _"For many VPNs, like ours, that rely on the natively supported IPSec/IKEv2 VPN protocols, when the API property is active a packet tunnel provider VPN will break any other user installed personal VPNs (even when a packet tunnel provider VPN isn't connected or isn't even active)..."._ This issue is discussed in the Apple Developer Forum: [Failed to register Personal IncludeAllNetworks VPN Session NESMIKEv2VPNSession](https://developer.apple.com/forums/thread/669086). This is over my head.  
  

  * _" ... for other VPNs utilizing the Wireguard secure network tunnel, setting includeAllNetworks in our tests has repeatedly resulted in internet connectivity failure, for example when switching between wi-fi and cellular. Often times the failure requires rebooting the entire device, which is a particularly brutal user experience. As of today's date Wireguard is aware of but has not taken advantage of the new VPN API property."_

I doubt that many VPN companies hang around the proverbial water cooler together, but Disconnect goes on to say "There does appear to be at least one VPN provider offering IncludeAllNetworks as part of their 'kill switch' feature, but none of the leading consumer and corporate VPNs that we tested have integrated includeAllNetworks."

Considering the bugs that Disconnect ran into, it is not clear if the use of the "includeAllNetworks" flag is, at this point, a good thing or a bad thing. But again, there is no reason to trust any VPN on iOS. I have added a warning to that effect on my [Defensive Computing Checklist](https://defensivecomputingchecklist.com/vpn.php) site.

### TOR vs. VPN

Added this section August 19, 2022

A comparison to **Tor** is interesting on a few levels. 

The biggest difference between a VPN and Tor is that Tor does not work at the operating system level. That is, Tor does less than a VPN when it comes to hiding your public IP address (and thus your location). Tor provides a new public IP address for every website you visit in the Tor Browser. However, it does nothing for other browsers on the same computing device. It does nothing for any other software on the computing device and nothing for the OS itself. In contrast, a VPN provides a new public IP address for the entire operating system. 

So, while using the Tor browser, all sorts of software on the same device is surely leaking the public IP address. This is mentioned on the [Tor website](https://www.torproject.org), but the warnings are buried in the middle of other stuff, it is not front and center. Have you ever read an article about Tor that included this warning? I have not. As the iOS VPN issue I write about on this page has gained publicity, I have not seen an article that says Tor leaks the public IP address all the time; by design. 

One warning from the Tor Project is on their [Tor Browser](https://support.torproject.org/tbb/) page, where they ask _"Does using Tor Browser protect other applications on my computer?"_ and respond to themselves with _"Only Tor Browser's traffic will be routed over the Tor network. Any other application on your system (including other browsers) will not have their connections routed over the Tor network, and will not be protected ... If you need to be sure that all traffic will go through the Tor network, take a look at the Tails live operating system..."_

And, suppose every VPN tunnel on iOS worked perfectly. 

Creating the VPN connection/tunnel is a thing the end user does. Before they connect to a VPN, their public IP address has surely leaked. Some VPN software has an option to run automatically when the system/device starts up. Maybe that will prevent the leaking of the public IP address, maybe not. It needs to be tested and could change with every release of the operating system. 

This brings me back to my suggested solution (more below) to connect to a router that has an existing VPN connection. This will be harder to setup initially, but easier to use on an ongoing basis. 

Another comparison between a VPN and Tor is that there is no official Tor software for iOS, in part because Apple won't allow it. Apple exerts control over iOS that Google does not over Android and Microsoft does not over Windows. Quoting the [Tor Project](https://support.torproject.org/): _"We recommend an iOS app called Onion Browser ... However, Apple requires browsers on iOS to use something called Webkit, which prevents Onion Browser from having the same privacy protections as Tor Browser."_ Apple likes to brag about privacy, but ...

### MY SUGGESTION

At this point, I see no reason to trust any VPN on iOS. My suggestion would be to make the VPN connection using VPN client software in a router, rather than on an iOS device.

I am not a fan of making a VPN connection on your _only_ router, but suggest having a second router dedicated to VPN connections. When you need a VPN, connect to the second router (Wi-Fi or Ethernet), when you don't need a VPN, connect to your main router. 

I recommend [pcWRT](https://www.pcwrt.com/) as a second router dedicated to VPN usage. I recently wrote up my [experiences with it](https://www.routersecurity.org/pcwrt.php). There is only one model and it sells for $129 US. It offers three VPN clients, for WireGuard, OpenVPN and IKEv2. I ran the same evaluation on pcWRT that I did here for iOS. In fact, I ran it for days on end and found no data that ever traveled outside the VPN tunnels created by the pcWRT router. Here on iOS, it took only a few minutes to find a VPN leak. 

### TESTING METHODOLOGY

My methodology is simple, I will log every new outbound request from my iPad (in other contexts a "request" might be called a socket, a session, a connection or a thread). I will start the logging, establish a VPN connection and use the iPad normally. If all goes well, I should see the outbound request(s) that establish the VPN tunnel and nothing else afterwards. If all data travels through the VPN connection/tunnel, the router will see no new outbound requests from the iPad, after the VPN tunnel has been established. The iPad is Wi-Fi only, so there is no cellular connection to complicate things. 

Although the testing is simple, it is not something that most people can do. Consumer routers, and those provided by an ISP, are not going to have the ability to log outbound requests. This may well have contributed to the bug in iOS going undetected for a long time.

The outbound firewall rule that logged requests from the iPad is shown below. It keys off the LAN side IP address of my iPad and logs any new outbound request that it makes. (the LAN side address of my iPad was not actually 10.1.2.3). I tested with a Peplink Balance 20x router running firmware 8.2.0. 

![Outbound Firewall rule in Peplink router](pix/ios.vpn.testing.fw.logging.rule.jpg)  
Outbound Firewall rule in Peplink router 

### FIRST TEST

During the first test, the iPad was running iOS version 15.4.1. I tested using version 3.1.3 (2205050847) of the ProtonVPN app. The app made an IKEv2 connection to a VPN server in Spain at IP address 37.19.214.3. Both the app ([screen shot)](pix/ios.vpn.testing.proton.status.webp) and a couple web sites confirmed that this was the public IP address. 

In simplified form, this is what the router log showed just after I started the VPN connection:  11:57:52 SRC=10.1.2.3 DST=37.19.214.1 LEN=408 PROTO=UDP SPT=4500 DPT=4500  
11:57:52 SRC=10.1.2.3 DST=23.200.168.178 LEN=64 PROTO=TCP SPT=57025 DPT=443 SYN  
11:57:52 SRC=10.1.2.3 DST=37.19.214.1 LEN=300 PROTO=UDP SPT=500 DPT=500  
11:57:52 SRC=10.1.2.3 DST=137.220.51.178 LEN=589 PROTO=TCP SPT=57024 DPT=443 SYN  
---  
Establishing the IKEv2 VPN tunnel  
  
The most important take-away from this is that the VPN tunnel was established at 11:57:52. 

As for the data items in the log: SRC is the source IP address, DST is the destination IP address, LEN is the length of the outgoing data, PROTO is the protocol (TCP or UDP), SPT is source port, and DPT is the destination port. Not sure what SYN is.

Note that while the public IP address is 37.19.214.3, the two UDP outbound connections were made to 37.19.214.1. This is normal. The IKEv2 connection was made first with an outbound UDP request to port 4500, then a UDP request port 500. This too is normal. We also see that there were two other outbound requests made the same second that the VPN tunnel was established. For my purposes, neither was important.

Then, I checked what Peplink calls the Active Sessions for the iPad. As shown below, this was the first indication of trouble.

![Active Sessions for iPad after VPN established](pix/ios.vpn.testing.sessions.jpg)  
Active Sessions for iPad after VPN established 

While this confirms that the iPad was connected to 37.19.214.1, it also shows a connection/session that is not the VPN tunnel. Although the tunnel was established when I made this screen shot, the iPad was still communicating with port 5223 at IP address 17.57.144.12 which Peplink identified as Apple Push. I later learned that all IP address that start with 17 belong to Apple. 

The bug that ProtonVPN first wrote about in March 2020, **still exists**. iOS 15.4.1 still does not terminate existing connections/sessions when it creates a VPN tunnel. This presents assorted dangers. Connections outside the VPN communicate your real public IP address and there is no guarantee that they are encrypted. They are also vulnerable to ISP spying. And, a VPN provides what should be a trustworthy DNS service. Outside the VPN, anything goes.

Next, I used assorted apps on the iPad and watched the router log. 

Twenty eight minutes after the VPN connection was established, this showed up in the log. 

12:26:33 SRC=10.1.2.3 DST=137.220.51.178 LEN=589 PROTO=TCP SPT=57026 DPT=443 SYN  
  
---  
A request to NextDNS outside the VPN tunnel  
  
Another request to dns.nextdns.io. Not good. 

**A FLOOD**

Twelve minutes later, a flood. 

12:41:21 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=57740 DPT=57740  
12:41:21 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=57740 DPT=57740  
12:41:16 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=65009 DPT=65009  
12:41:16 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=65009 DPT=65009  
12:41:05 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=57740 DPT=57740  
12:41:00 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=65009 DPT=65009  
12:41:00 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=65009 DPT=65009  
12:41:00 SRC=10.1.2.3 DST=17.178.104.183 LEN=44 PROTO=UDP SPT=65009 DPT=16386  
12:40:57 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=57740 DPT=57740  
12:40:57 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=57740 DPT=57740  
12:40:55 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=16403 DPT=16403  
12:40:55 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=16403 DPT=16403  
12:40:53 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=57740 DPT=57740  
12:40:53 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=57740 DPT=57740  
12:40:52 SRC=10.1.2.3 DST=17.178.104.183 LEN=44 PROTO=UDP SPT=57740 DPT=16386  
12:40:52 SRC=10.1.2.3 DST=17.178.104.182 LEN=44 PROTO=UDP SPT=57740 DPT=16384  
12:40:52 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=65009 DPT=65009  
12:40:51 SRC=10.1.2.3 DST=17.178.104.183 LEN=44 PROTO=UDP SPT=65009 DPT=16386  
12:40:51 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=16403 DPT=16403  
12:40:51 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=16403 DPT=16403  
12:40:50 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=57740 DPT=57740  
12:40:50 SRC=10.1.2.3 DST=17.178.104.183 LEN=44 PROTO=UDP SPT=57740 DPT=16386  
12:40:50 SRC=10.1.2.3 DST=17.178.104.182 LEN=44 PROTO=UDP SPT=57740 DPT=16385  
12:40:50 SRC=10.1.2.3 DST=17.178.104.182 LEN=44 PROTO=UDP SPT=57740 DPT=16384  
12:40:47 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=65009 DPT=65009  
12:40:47 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=65009 DPT=65009  
12:40:47 SRC=10.1.2.3 DST=17.178.104.183 LEN=44 PROTO=UDP SPT=65009 DPT=16386  
12:40:47 SRC=10.1.2.3 DST=17.178.104.182 LEN=44 PROTO=UDP SPT=65009 DPT=16384  
12:40:46 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=16403 DPT=16403  
12:40:46 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=16403 DPT=16403  
12:40:46 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=16403 DPT=16403  
12:40:45 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=65009 DPT=65009  
12:40:45 SRC=10.1.2.3 DST=17.178.104.183 LEN=44 PROTO=UDP SPT=65009 DPT=16386  
12:40:45 SRC=10.1.2.3 DST=17.178.104.182 LEN=44 PROTO=UDP SPT=65009 DPT=16385  
12:40:45 SRC=10.1.2.3 DST=17.178.104.182 LEN=44 PROTO=UDP SPT=65009 DPT=16384  
12:40:42 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=16403 DPT=16403  
12:40:42 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=16403 DPT=16403  
12:40:42 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=16403 DPT=16403  
12:40:42 SRC=10.1.2.3 DST=17.178.104.182 LEN=44 PROTO=UDP SPT=16403 DPT=16385  
12:40:40 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=16403 DPT=16403  
12:40:40 SRC=10.1.2.3 DST=99.99.99.99 LEN=44 PROTO=UDP SPT=16403 DPT=16403  
12:40:40 SRC=10.1.2.3 DST=17.178.104.183 LEN=44 PROTO=UDP SPT=16403 DPT=16386  
12:40:40 SRC=10.1.2.3 DST=17.178.104.182 LEN=44 PROTO=UDP SPT=16403 DPT=16385  
12:40:40 SRC=10.1.2.3 DST=17.178.104.182 LEN=44 PROTO=UDP SPT=16403 DPT=16384  
12:38:58 SRC=10.1.2.3 DST=37.19.214.1 LEN=408 PROTO=UDP SPT=4500 DPT=4500  
12:38:58 SRC=10.1.2.3 DST=37.19.214.1 LEN=300 PROTO=UDP SPT=500 DPT=500  
12:38:58 SRC=10.1.2.3 DST=17.253.99.99 LEN=76 PROTO=UDP SPT=123 DPT=123  
12:38:58 SRC=10.1.2.3 DST=17.253.99.99 LEN=76 PROTO=UDP SPT=123 DPT=123  
12:38:58 SRC=10.1.2.3 DST=17.253.99.99 LEN=76 PROTO=UDP SPT=123 DPT=123  
12:38:58 SRC=10.1.2.3 DST=137.220.51.178 LEN=589 PROTO=TCP SPT=57027 DPT=443  
---  
The flood gates are open!  
  
At this point I stopped the activity logging to avoid flooding the router log.

My first thought was that the VPN connection had failed. But no, ProtonVPN [reported](pix/ios.vpn.testing.proton.status.webp) that the connection to Madrid had been active for 49 minutes. The flood started at roughly 12:39 PM and VPN connection was first made at 11:58 AM. To borrow a phrase from Apollo 13: Cupertino, we have a problem. 

Speaking of the VPN, the iPad made the same two IKEv2 connections at 12:38:58 - a UDP request to port 4500 and a UDP request to port 500, both to the currently in-use VPN server (37.19.214.1). Maybe there are keys that need to re-established? I don't know.

There is more to look at in the 2.5 minutes of activity shown above. 

Note: One thing that was a mystery to me, turns out to be normal. Specifically, the 28 requests to IP address 99.99.99.99 which is standing in for my public IP. All the requests were UDP and the same length (44). Looking at just those 28 requests a pattern emerges, as shown below. There were three different target ports and the source port number was always the same as the destination port number. Someone more knowledgeable about this wrote to say: "All of these requests are basically 'loopback' checks. Your device is checking that the SRC address (your private IP) and the DST address (which is your public IP) are really the same place. Network stacks need to understand whether two interfaces are really the same or not, for many reasons, e.g. so that if software sends out a broadcast request, it is not sent over multiple 'identical' interfaces, which would lead to duplicate packets. This is normal, and one would expect the source and destination ports to be the same."

12:41:21 SPT=57740 DPT=57740  
12:41:21 SPT=57740 DPT=57740  
12:41:05 SPT=57740 DPT=57740  
12:40:57 SPT=57740 DPT=57740  
12:40:57 SPT=57740 DPT=57740  
12:40:53 SPT=57740 DPT=57740  
12:40:53 SPT=57740 DPT=57740  
12:40:50 SPT=57740 DPT=57740

* * *

12:41:16 SPT=65009 DPT=65009  
12:41:16 SPT=65009 DPT=65009  
12:41:00 SPT=65009 DPT=65009  
12:41:00 SPT=65009 DPT=65009  
12:40:52 SPT=65009 DPT=65009  
12:40:47 SPT=65009 DPT=65009  
12:40:47 SPT=65009 DPT=65009  
12:40:45 SPT=65009 DPT=65009 

* * *

12:40:55 SPT=16403 DPT=16403  
12:40:55 SPT=16403 DPT=16403  
12:40:51 SPT=16403 DPT=16403  
12:40:51 SPT=16403 DPT=16403  
12:40:46 SPT=16403 DPT=16403  
12:40:46 SPT=16403 DPT=16403  
12:40:46 SPT=16403 DPT=16403  
12:40:42 SPT=16403 DPT=16403  
12:40:42 SPT=16403 DPT=16403  
12:40:42 SPT=16403 DPT=16403  
12:40:40 SPT=16403 DPT=16403  
12:40:40 SPT=16403 DPT=16403  
---  
iPad requests to my public IP address  
  
The 20 outbound requests that were not to my public IP address and not the VPN server are shown below.

12:41:00 DST=17.178.104.183 LEN=44 PROTO=UDP SPT=65009 DPT=16386  
12:40:52 DST=17.178.104.183 LEN=44 PROTO=UDP SPT=57740 DPT=16386  
12:40:52 DST=17.178.104.182 LEN=44 PROTO=UDP SPT=57740 DPT=16384  
12:40:51 DST=17.178.104.183 LEN=44 PROTO=UDP SPT=65009 DPT=16386  
12:40:50 DST=17.178.104.183 LEN=44 PROTO=UDP SPT=57740 DPT=16386  
12:40:50 DST=17.178.104.182 LEN=44 PROTO=UDP SPT=57740 DPT=16385  
12:40:50 DST=17.178.104.182 LEN=44 PROTO=UDP SPT=57740 DPT=16384  
12:40:47 DST=17.178.104.183 LEN=44 PROTO=UDP SPT=65009 DPT=16386  
12:40:47 DST=17.178.104.182 LEN=44 PROTO=UDP SPT=65009 DPT=16384  
12:40:45 DST=17.178.104.183 LEN=44 PROTO=UDP SPT=65009 DPT=16386  
12:40:45 DST=17.178.104.182 LEN=44 PROTO=UDP SPT=65009 DPT=16385  
12:40:45 DST=17.178.104.182 LEN=44 PROTO=UDP SPT=65009 DPT=16384  
12:40:42 DST=17.178.104.182 LEN=44 PROTO=UDP SPT=16403 DPT=16385  
12:40:40 DST=17.178.104.183 LEN=44 PROTO=UDP SPT=16403 DPT=16386  
12:40:40 DST=17.178.104.182 LEN=44 PROTO=UDP SPT=16403 DPT=16385  
12:40:40 DST=17.178.104.182 LEN=44 PROTO=UDP SPT=16403 DPT=16384 

* * *

12:38:58 DST=17.253.99.99 LEN=76 PROTO=UDP SPT=123 DPT=123  
12:38:58 DST=17.253.99.99 LEN=76 PROTO=UDP SPT=123 DPT=123  
12:38:58 DST=17.253.99.99 LEN=76 PROTO=UDP SPT=123 DPT=123  
12:38:58 DST=137.220.51.178 LEN=589 PROTO=TCP SPT=57027 DPT=443  
---  
The parts of the flood that were not to my public IP address  
  
The first request (12:38:58) mimics one we have seen before, the target is NextDNS on the expected port (443). Interestingly, this was the only TCP request, all the rest were UDP.

The next three requests were to UDP port 123, which is the Time of Day port. The target IP addresses all start with 17.253 and are clearly NTP time servers owned by Apple. Here again, the 99 is a placeholder for a number, I am not publishing the exact IP addresses for reasons that are off topic. These requests occurred in the same second as the call out to NextDNS. 

The remaining 16 requests were to two IP addresses: 17.178.104.182 and 17.178.104.183. Both belong to Apple. Certainly it is fair to say, at this point, that the flood of outbound requests that bypassed the VPN tunnel came from iOS itself. 

The destination ports at the two Apple IP addresses were 16384, 16385 and 16386 so they clearly have a common purpose. According [to Apple](https://support.apple.com/en-us/HT202944) these UDP ports are used for either the Real-Time Transport Protocol or Real-Time Control Protocol by either FaceTime or Game Center. I was not using FaceTime or playing a game on the iPad. The source port numbers are the same as those used above for the requests sent to my public IP address. Not sure what that indicates. 

### SECOND TEST

To verify that the bug is in iOS itself, I ran a second test under different conditions. 

The first thing I changed was the OS; the iPad was updated to version 15.5, which, as I write this, is the latest version. I also changed VPN providers, software and protocols. This test used an iOS app from OVPN that only supports WireGuard.

The OVPN app was version 0.5.0 from Feb. 19, 2022. The VPN server that I connected to was 139.28.219.36 in France. My test procedure was the same: I configured the Peplink Balance 20x router to log all outbound connections made by the iPad, I connected to the VPN, used the iPad and watched the router log. 

This time, the establishing of the VPN tunnel seemed to be done with a single outbound UDP connection (shown below) to port 9929 at 139.28.219.35.  16:08:59 SRC=10.1.2.3 DST=139.28.219.35 LEN=176 PROTO=UDP SPT=50700 DPT=9929  
---  
Establishing the WireGuard VPN tunnel  
  
As with the first test, which used IKEv2, the IP address that the world sees is one off from the IP address that the router connected to. I made a [screen shot](pix/ios.vpn.testing.ovpn.status.webp) of the OVPN app which shows a public IP address of 139.28.219.36, one higher than the IP the router connected to. Other web sites confirmed this as the public IP. Some day, I have learn why this happens. 

After the VPN was established, I checked the Active Sessions for the iPad. The only connection the router showed was the VPN tunnel. No Apple Push this time.

I used the iPad and watched the log...

Seven minutes later **another flood** of requests are seen traveling outside the VPN tunnel. I stopped the router logging after the flood shown below. I am simply interested in whether there is a problem, yes or no. I am not interested in fully defining/debugging the problem. That's for Apple.

As before, there were many requests to my public IP address. Quite the puzzlement. They were all UDP and the Source Port number (SPT) was always the same as the Destination Port number (DPT). The table below shows these connections. It is sorted by destination/target port, rather than time of day, to better show the three destination ports: 16403, 51941 and 52666. Just for fun, a Google search for "Apple iOS UDP port 52666" turned up nothing. 

16:16:46 SRC=10.1.2.3 ID=59313 PROTO=UDP SPT=16403 DPT=16403  
16:16:46 SRC=10.1.2.3 ID=55901 PROTO=UDP SPT=16403 DPT=16403  
16:16:38 SRC=10.1.2.3 ID=40208 PROTO=UDP SPT=16403 DPT=16403  
16:16:38 SRC=10.1.2.3 ID=28964 PROTO=UDP SPT=16403 DPT=16403  
16:16:34 SRC=10.1.2.3 ID=35868 PROTO=UDP SPT=16403 DPT=16403  
16:16:34 SRC=10.1.2.3 ID=8209 PROTO=UDP SPT=16403 DPT=16403  
16:16:31 SRC=10.1.2.3 ID=39229 PROTO=UDP SPT=16403 DPT=16403 

* * *

16:17:18 SRC=10.1.2.3 ID=63831 PROTO=UDP SPT=51941 DPT=51941  
16:17:18 SRC=10.1.2.3 ID=40276 PROTO=UDP SPT=51941 DPT=51941  
16:17:02 SRC=10.1.2.3 ID=50924 PROTO=UDP SPT=51941 DPT=51941  
16:16:54 SRC=10.1.2.3 ID=52733 PROTO=UDP SPT=51941 DPT=51941  
16:16:54 SRC=10.1.2.3 ID=18792 PROTO=UDP SPT=51941 DPT=51941  
16:16:46 SRC=10.1.2.3 ID=18096 PROTO=UDP SPT=51941 DPT=51941  
16:16:46 SRC=10.1.2.3 ID=40090 PROTO=UDP SPT=51941 DPT=51941  
16:16:46 SRC=10.1.2.3 ID=31786 PROTO=UDP SPT=51941 DPT=51941  
16:16:38 SRC=10.1.2.3 ID=50271 PROTO=UDP SPT=51941 DPT=51941  
16:16:38 SRC=10.1.2.3 ID=50661 PROTO=UDP SPT=51941 DPT=51941  
16:16:38 SRC=10.1.2.3 ID=36010 PROTO=UDP SPT=51941 DPT=51941 

* * *

16:16:48 SRC=10.1.2.3 ID=6173 PROTO=UDP SPT=52666 DPT=52666  
16:16:44 SRC=10.1.2.3 ID=14513 PROTO=UDP SPT=52666 DPT=52666  
16:16:40 SRC=10.1.2.3 ID=4581 PROTO=UDP SPT=52666 DPT=52666  
16:16:40 SRC=10.1.2.3 ID=30535 PROTO=UDP SPT=52666 DPT=52666  
16:16:40 SRC=10.1.2.3 ID=16925 PROTO=UDP SPT=52666 DPT=52666  
16:16:36 SRC=10.1.2.3 ID=43384 PROTO=UDP SPT=52666 DPT=52666  
16:16:36 SRC=10.1.2.3 ID=38165 PROTO=UDP SPT=52666 DPT=52666  
16:16:36 SRC=10.1.2.3 ID=17988 PROTO=UDP SPT=52666 DPT=52666  
16:16:34 SRC=10.1.2.3 ID=53627 PROTO=UDP SPT=52666 DPT=52666  
16:16:34 SRC=10.1.2.3 ID=42495 PROTO=UDP SPT=52666 DPT=52666  
16:16:31 SRC=10.1.2.3 ID=57859 PROTO=UDP SPT=52666 DPT=52666  
16:16:31 SRC=10.1.2.3 ID=62414 PROTO=UDP SPT=52666 DPT=52666  
16:16:31 SRC=10.1.2.3 ID=16697 PROTO=UDP SPT=52666 DPT=52666  
---  
Outbound iPad requests to my Public IP address (WireGuard)  
  
The outbound requests to the actual Internet, shown below, fall into two categories. The last/top two requests were to IP addresses belonging to Amazon Web Services in Europe. They were TCP requests to the normal, ordinary, commonplace HTTPS port (443). 

The rest were to Apple owned IP addresses on UDP ports 16384, 16385 and 16386. Same as the first test. Again, I am not publishing the exact Apple IP addresses (99.99 is a stand-in) for reasons that are off topic. 

16:22:34 SRC=10.1.2.3 DST=15.160.79.209 ID=0 PROTO=TCP SPT=49173 DPT=443  
16:17:22 SRC=10.1.2.3 DST=15.160.35.79 ID=0 PROTO=TCP SPT=49169 DPT=443 

* * *

16:16:38 SRC=10.1.2.3 DST=17.173.99.99 ID=40457 PROTO=UDP SPT=51941 DPT=16386  
16:16:38 SRC=10.1.2.3 DST=17.173.99.99 ID=51493 PROTO=UDP SPT=16403 DPT=16385  
16:16:33 SRC=10.1.2.3 DST=17.173.99.99 ID=40240 PROTO=UDP SPT=51941 DPT=16386  
16:16:33 SRC=10.1.2.3 DST=17.173.99.99 ID=41763 PROTO=UDP SPT=51941 DPT=16384  
16:16:33 SRC=10.1.2.3 DST=17.173.99.99 ID=26637 PROTO=UDP SPT=16403 DPT=16385  
16:16:31 SRC=10.1.2.3 DST=17.173.99.99 ID=36462 PROTO=UDP SPT=51941 DPT=16386  
16:16:31 SRC=10.1.2.3 DST=17.173.99.99 ID=15857 PROTO=UDP SPT=51941 DPT=16385  
16:16:31 SRC=10.1.2.3 DST=17.173.99.99 ID=39550 PROTO=UDP SPT=52666 DPT=16386  
16:16:31 SRC=10.1.2.3 DST=17.173.99.99 ID=28383 PROTO=UDP SPT=51941 DPT=16384  
16:16:31 SRC=10.1.2.3 DST=17.173.99.99 ID=42153 PROTO=UDP SPT=52666 DPT=16385  
16:16:31 SRC=10.1.2.3 DST=17.173.99.99 ID=60829 PROTO=UDP SPT=52666 DPT=16384  
16:16:31 SRC=10.1.2.3 DST=17.173.99.99 ID=20614 PROTO=UDP SPT=16403 DPT=16386  
16:16:31 SRC=10.1.2.3 DST=17.173.99.99 ID=36357 PROTO=UDP SPT=16403 DPT=16385  
16:16:31 SRC=10.1.2.3 DST=17.173.99.99 ID=32360 PROTO=UDP SPT=16403 DPT=16384  
---  
Outbound iPad requests to the Internet (WireGuard)  
  
### WRAPPING UP THE INITIAL 2 TESTS

Comedian [Steven Wright](https://en.wikipedia.org/wiki/Steven_Wright) used to joke that he had to get a new shadow because the old one wasn't doing what he was doing. That's what we have here. A VPN that is not doing what it is supposed to do. Data is leaving my iPad and not traveling through the VPN tunnel.

It is surprising to find this problem has persisted for so long. My testing took very little hardware, software or expertise. With the billions of iOS users, it is hard to imagine that no one else bothered testing this. Then again, the world was a bit distracted in March of 2020. 

It also seems that Apple has a level of trust that they do not deserve. Back in March 2020, Steve Gibson [said](https://www.grc.com/sn/sn-760.htm) "... Apple's going to fix this. I'm sure it's already been fixed in-house. They're probably moments away from pushing out a fix to this because it's gotten a lot of attention in the industry ... I imagine within a few days this'll be fixed." A slightly more skeptical John Dunn of Sophos [wrote](https://nakedsecurity.sophos.com/2020/03/30/apples-ios-13-4-hit-by-vpn-bypass-vulnerability/) at the time that "A patch might not appear for weeks". It has been over two years. 

I emailed Apple at their special email address for reporting security issues on May 19, 2022 and, for a week, there was no response. On May 26th, I emailed again and, this time, Apple responded the next day. More in the section on Where This Stands. 

### WORK-AROUNDS

[This section was totally re-written May 28, 2022]

One suggested solution was an **always-on VPN**. Quoting ProtonVPN: _"Apple recommends using[Always-on VPN](https://support.apple.com/guide/deployment/vpn-overview-depae3d361d0/1/web/1.0) to mitigate this issue. This method requires using device management, so unfortunately it doesn’t mitigate the issue for third-party applications such as Proton VPN."_ So, not a solution for us consumers. But, ProtonVPN had two other suggested work-arounds. 

The last update to the ProtonVPN blog (dated Oct. 19, 2020) said _"Although Apple has not fixed the VPN bypass problem directly on iOS 14, they have provided the Kill Switch capability to app developers. By enabling Kill Switch, existing connections will be blocked whenever VPN is enabled. We will be adding this capability in an upcoming release of Proton VPN."_ This is a puzzling statement as the purpose of a VPN **Kill Switch** is to disconnect the Internet should the VPN tunnel fail. It is not normally involved in existing connections at the time the VPN is enabled. 

Since the blog was written, ProtonVPN has indeed added a kill switch option to their iOS app (see [screen shot](pix/protonvpn.ios.app.settings.webp)). The description of the feature in the app is _"blocks all network traffic when VPN tunnel is lost"_ , which is par for the course as Kill Switches go. It also has _nothing_ to do with leaks outside the VPN tunnel while the tunnel is alive and well. Apples and Oranges. 

Still, I tested for VPN leaks with the Kill Switch enabled (it is disabled by default). It made no difference, the VPN still leaked. You can see this below.

The VPN tunnel is the UDP connection from port 4500 to port 4500 at IP address 188.241.83.106, which is ProtonVPN in Paris. We also see the iPad has two TCP connections labeled "Secure IMAP/Gmail". Both connections are to port 993 at IP address 172.253.62.108. Shodan reports that this IP address is indeed [used for Gmail](https://www.shodan.io/host/172.253.62.108). And Google does use port 993 for [IMAP access to Gmail](https://support.google.com/mail/answer/7126229). 

![Gmail outside the VPN tunnel](pix/gmail.outside.tunnel.webp)  
Gmail outside the VPN tunnel 

The last suggested work-around involved using **Airplane Mode** to disconnect the VPN. Funny thing about Airplane Mode on my Wi-Fi only iPad running iOS 15.5. _It does not seem to do anything_.

With the Wi-Fi on, I enabled Airplane Mode and the Wi-fi did not go off (see [screen shot](pix/airplane.mode.and.wifi.webp)). I also found that Airplane Mode did not interrupt an active VPN connection. I made a WireGuard connection using OVPN, then turned on Airplane Mode and the VPN connection remained alive and well.

With that as background, here is exactly what ProtonVPN said regarding this last work-around:

Internet connections established after you connect to VPN are not affected. But connections that are already running when you connect to VPN may continue outside the VPN tunnel indefinitely. There is no way to guarantee that those connections will be closed at the moment you start a VPN connection. However, we've discovered the following technique to be almost as effective:  
1\. Connect to any Proton VPN server.  
2\. Turn on airplane mode. This will kill all Internet connections and temporarily disconnect Proton VPN.  
3\. Turn off airplane mode. Proton VPN will reconnect, and your other connections should also reconnect inside the VPN tunnel, though we cannot guarantee this 100%.

First thing to notice is that this is something ProtonVPN discovered, it is not advice from Apple. Then, there are the hedging phrases: _"almost as effective"_ and _"we cannot guarantee"_. 

Still, how can it be that in their testing, Airplane Mode killed all Internet connections and in my testing it did not? Perhaps another bug in iOS? Or, maybe because blog was written for iOS 13 and I tested with iOS 15.5? I dug out an old iPod running iOS 12.5.5 and, sure enough, Airplane Mode turned off the Wi-Fi. 

A bit of Googling turned up this Apple support item: [Use Airplane Mode on your iPhone, iPad, iPod touch, and Apple Watch](https://support.apple.com/en-us/HT204234) from September 2021. At first, the article says _"When you turn on Airplane Mode, it turns off all radios except for Bluetooth"_. But later it says _"you can use Wi-Fi and Bluetooth while in Airplane Mode. You just need to turn them on separately"_ and _"If you turn on Wi-Fi or Bluetooth while you're in Airplane Mode, they'll be on the next time you use Airplane Mode, unless you turn them off while in Airplane Mode."_ So, Airplane Mode is like a box of chocolates, you never know what you're gonna get. 

All told, this a poor look for the tech support team at ProtonVPN. Even if Airplane Mode is a work-around, they failed to explain all the issues with it. And, the suggestion that the Kill Switch is applicable at all, was off-base. Worse than their blog, when I contacted them recently about this, they said I should use the Kill Switch. Ugh.

### TESTING THE AIRPLANE MODE FIX

Added this section on May 30, 2022

I fought through the poorly written Apple support article about Airplane Mode, such that enabling it on my iPad would disable the Wi-Fi. And, then things got ugly.

With Airplane Mode OFF, the Settings app shows that Wi-Fi is connected, displaying the SSID of my network. But, there is no Wi-Fi icon in the top right corner of the iPad display (the half circles next to the battery percentage). So, is it on or not? No web pages would load, in multiple browsers, so it seems not. That the Settings app tells me it is connected to Wi-Fi seems like a bug. 

Interestingly, my router also reported a half-connected state. While it showed the iPad in the list of connected devices, there were no active connections from the iPad to anywhere on the Internet. I did not bother with firewall logging. 

The Wi-Fi connection was defined to use a Private Wi-Fi Address (really a MAC address). I turned this off, in the hope it was part of the problem. This reset the Wi-Fi connection. The router showed the iPad as a connected device with the new MAC/WiFi address, however, web pages would still not load and there was still no Wi-Fi indicator in the top right corner.

Airplane Mode broke my iPad.

At this point I turned the iPad off, waited a minute and turned it back on. When it booted, the Wi-Fi indicator in the top right corner was on, then went off, then it came back on along with the VPN indicator. VPN? I wasn't doing anything with a VPN. I wasn't but ProtonVPN was. Their app (version 3.1.3) has an Always-on VPN option that is, sadly, not an option. It is always on. 

I turned off the ProtonVPN connection and all was well with the Wi-Fi. My guess is that something went wrong between Airplane Mode and the Always-on option. You're on. You're off. You're on. You're off. 

I seem to be accumulating bugs, not only on the iPad but also in my Peplink Balance 20x router. While testing Airplane Mode, I was checking all the active sessions/connections from all the devices connected to the router (there were very few). I saw an active session for a device that I did not realize was connected. So, I turned off the Wi-Fi on the device. Surprisingly, the active session remained for what seemed quite a while. The router reported that the device went off-line, but a session remained active. I reported it as a bug to Peplink. Any comments above, about Active Sessions shown by the router, are now suspect. Ugh. 

### YET ANOTHER TEST

Added this section on June 16, 2022

I have been in contact with Apple about this and they requested a dump of the system, after the problem happens, so I did another test. I was able to re-create the problem, this time using VPN software from Windscribe that made an OpenVPN connection. Using VPN software from three different VPN companies clearly points at iOS itself as the source of the problem.

After the VPN connection was made, I tried a number of apps and none generate traffic outside the VPN tunnel. It was not until I went into the iOS app store, to update some apps, that the flood of traffic outside the tunnel started. As before, there were requests to both Apple IP addresses and my public IP address. 

### TESTING iOS 15.6

Added this section on August 8, 2022

The VPN still leaks on iOS version 15.6.

I powered off my iPad and powered it back on to start with a clean slate. Using the ProtonVPN app version 4.0.0, I made a WireGuard connection to a server in London at 37.120.198.179. 

As always, with the VPN connected, my router (Peplink Balance 20X firmware 8.2.0) showed multiple sockets/sessions. A VPN that does not leak, should have only one. But, there seems to be a Peplink bug in this regard, they report active sockets/sessions even after a device has gone off-line. I reported this to Peplink and have heard nothing back for quite a while. So, this counts for nothing, just an FYI. Still, after a few minutes the other sessions seem to have timed out and the router showed just one socket/session to the VPN server. 

Then, after I started the Gmail app on the iPad, I saw these two new sockets/sessions. 

![Two VPN data leaks](pix/ios.vpn.leaking.version15.6.webp)  
Two VPN data leaks in iOS 15.6 

Apple owns all IP addresses that start with 17, and the outbound request to TCP port 5223 at 17.57.147.5 is identified by the router as Apple Push. Google owns all IP addresses that start with 172.253 and the outbound request to TCP port 993 at 172.253.63.109 is clearly Gmail.

For whatever reason these outbound requests did not show up in the router's firewall log. However, the log did show outbound TCP requests to 104.70.71.223 on ports 59922, 59924, 59925, 59926, 59927, 59928 and 59929. There was also an outbound request to the missing TCP port in this sequence, 59923, but that went to 23.62.24.145. Both of these destination IP addresses belong to Akamai. 

\- - - - - - - - - - - -

Then, I tested with a different router, a Pepwave Surf SOHO running firmware 8.2.1. I also used an app from a different VPN provider (Windscribe with app version 3.3.0) and used OpenVPN rather than WireGuard. OpenVPN connected via UDP to port 123 (this non-standard port is a configuration option offered by the Windscribe app). The app said that I was connected to a VPN server in Vancouver Canada 104.218.61.20 and this was confirmed by a site that displays the public IP address. As we have seen before in other tests, the router disagreed, it said there was a connection to 104.218.61.1. 

I watched the router display of current sockets/sessions until it showed the single connection to the VPN server. Shortly thereafter, it showed a new socket, to TCP port 5223 at IP address 17.57.147.5 which belongs to Apple. The interesting thing was that I had not touched the iPad at all. 

Then, I turned on logging and it quickly showed a bunch of outbound requests to two IP addresses that start with 185 (see below). These requests were blocked due to other firewall rules in the router, but had these requests traveled through the VPN tunnel, the router would not have objected. So, more leaking. Interestingly, it appears that these two IP addresses might belong to Windscribe. I will follow up with them. If so, then their app is leaking data. 

16:38:49 DST=185.245.85.99 LEN=48 PROTO=TCP SPT=49394 DPT=443  
16:38:49 DST=185.107.81.130 LEN=48 PROTO=TCP SPT=49342 DPT=443  
16:38:17 DST=185.245.85.99 LEN=64 PROTO=TCP SPT=49394 DPT=443  
16:38:17 DST=185.107.81.130 LEN=64 PROTO=TCP SPT=49342 DPT=443  
16:38:01 DST=185.245.85.99 LEN=64 PROTO=TCP SPT=49394 DPT=443  
16:38:01 DST=185.107.81.130 LEN=64 PROTO=TCP SPT=49342 DPT=443  
16:37:53 DST=185.245.85.99 LEN=64 PROTO=TCP SPT=49394 DPT=443  
16:37:53 DST=185.107.81.130 LEN=64 PROTO=TCP SPT=49342 DPT=443  
16:37:49 DST=185.245.85.99 LEN=64 PROTO=TCP SPT=49394 DPT=443  
16:37:49 DST=185.107.81.130 LEN=64 PROTO=TCP SPT=49342 DPT=443  
16:37:47 DST=185.245.85.99 LEN=64 PROTO=TCP SPT=49394 DPT=443  
16:37:47 DST=185.107.81.130 LEN=64 PROTO=TCP SPT=49342 DPT=443  
16:37:46 DST=185.245.85.99 LEN=64 PROTO=TCP SPT=49394 DPT=443  
16:37:46 DST=185.107.81.130 LEN=64 PROTO=TCP SPT=49342 DPT=443  
16:37:45 DST=185.245.85.99 LEN=64 PROTO=TCP SPT=49394 DPT=443  
16:37:45 DST=185.107.81.130 LEN=64 PROTO=TCP SPT=49342 DPT=443  
16:37:44 DST=185.245.85.99 LEN=64 PROTO=TCP SPT=49394 DPT=443  
16:37:44 DST=185.107.81.130 LEN=64 PROTO=TCP SPT=49342 DPT=443  
16:37:43 DST=185.245.85.99 LEN=64 PROTO=TCP SPT=49394 DPT=443  
16:37:43 DST=185.107.81.130 LEN=64 PROTO=TCP SPT=49342 DPT=443  
16:37:42 DST=185.245.85.99 LEN=64 PROTO=TCP SPT=49394 DPT=443  
16:37:42 DST=185.107.81.130 LEN=64 PROTO=TCP SPT=49342 DPT=443  
---  
VPN Leaks to IPs starting with 185  
  
Soon thereafter, the log showed more outbound requests outside the VPN tunnel (see below). These were all to Apple, targeting UDP ports 16384, 16385 and 16386. 

16:49:29 DST=17.133.234.32 ID=4183 PROTO=UDP SPT=50904 DPT=16385  
16:49:29 DST=17.133.234.32 ID=22349 PROTO=UDP SPT=16403 DPT=16385  
16:49:27 DST=17.133.234.33 ID=28675 PROTO=UDP SPT=50904 DPT=16386  
16:49:27 DST=17.133.234.32 ID=5968 PROTO=UDP SPT=50904 DPT=16385  
16:49:27 DST=17.133.234.32 ID=36514 PROTO=UDP SPT=50904 DPT=16384  
16:49:27 DST=17.133.234.33 ID=42933 PROTO=UDP SPT=56509 DPT=16386  
16:49:27 DST=17.133.234.32 ID=26999 PROTO=UDP SPT=56509 DPT=16385  
16:49:27 DST=17.133.234.32 ID=7681 PROTO=UDP SPT=56509 DPT=16384  
16:49:27 DST=17.133.234.33 ID=9389 PROTO=UDP SPT=16403 DPT=16386  
16:49:27 DST=17.133.234.32 ID=39755 PROTO=UDP SPT=16403 DPT=16385  
16:49:27 DST=17.133.234.32 ID=49291 PROTO=UDP SPT=16403 DPT=16384  
---  
More VPN Leaks - to Apple using UDP  
  
And finally, still more leaks, before I gave up and shut down logging:

16:51:13 DST=96.6.22.62 PROTO=TCP SPT=64498 DPT=443  
16:51:13 DST=96.6.22.62 PROTO=TCP SPT=64497 DPT=443  
16:51:12 DST=23.54.68.44 PROTO=TCP SPT=64496 DPT=443  
16:51:12 DST=96.6.22.62 PROTO=TCP SPT=64495 DPT=443  
16:51:11 DST=23.5.227.168 PROTO=TCP SPT=64494 DPT=443  
16:51:11 DST=23.5.227.168 PROTO=TCP SPT=64493 DPT=443  
16:51:07 DST=104.20.93.59 PROTO=TCP SPT=64492 DPT=443  
16:51:07 DST=137.220.51.178 PROTO=TCP SPT=64491 DPT=443  
---  
Still more VPN Leaks to assorted destinations  
  
A couple of these IP address belong to Akamai, and they serve many different Apple domains and sub-domains, according to an IP address search at Shodan. One of the Akamai IP addresses (23.54.68.44) seems dedicated to mesu.apple.com. IP address 104.20.93.59 seems to belong to Windscribe. The final IP address, 137.220.51.178, is NextDNS. 

Leak, leak, leak.

### LEAKING DOMAINS

Added this section on August 20, 2022

Examining IP addresses can only go so far, so I took a first look at the domains that are leaking outside the VPN tunnel. Using iOS 15.6, I connected my iPad to a [pcWRT router](https://www.pcwrt.com/) that offers parental controls. One parental control feature is a summary of the domains accessed by each device connected to the router. 

Here, at the right, we see this summary for my iPad shortly after establishing a VPN connection. The blacked out destination is the IP address of the VPN server.  | ![](pix/pcwrt.domain.counters.early.crop.jpg)  
---|---  
And, here we see the same summary a bit later, after I used the iPad for a few minutes. It is no surprise that the number of requests to the VPN server increased (13 to 19). We also see that five domains were not accessed at all, after the VPN connection was made. However, the number of requests to the apple.com domain increased from 16 to 35. In this test, **all the data leaking outside the VPN tunnel went to Apple**.  | ![](pix/pcwrt.domain.counters.late.crop.jpg)  
  
This summary does not break things down by sub-domain and I later learned that the router could that. Another test (Aug 22, 2022) showed that, after the VPN was established, all the detected requests were to courier.push.apple.com, and they were all to TCP port 5223. 

**URL LOGGING**

This time, I used another new approach. My Peplink router has a URL Logging feature that sends log data to an external logging server. A Synology NAS can function as a log server, so with a little configuring, I got the router to send URL logs to my Synology NAS. The result is shown below. 

The iPad was now running iOS version 15.6.1. It used the Windscribe VPN app to make an OpenVPN connection. The URL logging was started in the router _after_ VPN connection was made which means that all the requests below were outside the VPN. Had they been inside, the router would not have seen them. 

Time |  Domain |  Destination  
IP Address |  Source  
Port |  Destination  
Port  
---|---|---|---|---  
18:41:58|  graph.facebook.com |  \-- |  50340 |  443  
18:37:55|  inappcheck.itunes.apple.com |  \-- |  50339 |  443  |  18:31:46|  p3-buy.itunes.apple.com |  \-- |  50338 |  443  | 18:31:46|  images.wsj.net | 143.204.146.37 |  50337 |  443  |  18:31:46|  bartender.mobile.dowjones.io | 99.84.191.68 |  50336 |  443  | 18:31:46|  firebaselogging-pa.googleapis.com | 108.177.122.95 |  50335 |  443  | 18:22:28|  imap.gmail.com | 172.253.63.108|  50334 |  993 | 18:22:28|  imap.gmail.com | 172.253.63.108|  50333 |  993  | 18:22:28|  imap.gmail.com | 172.253.63.108|  50332 |  993  |  18:22:28|  click.mail.zillow.com | 54.189.2.119 |  50331 |  443  |  18:22:28|  configuration.ls.apple.com | 23.216.85.59|  50330 |  443  |  18:22:28|  photos.zillowstatic.com | 143.204.146.19 |  50329 |  443  |  18:22:28|  maps.googleapis.com | \-- |  50328 |  443  |  18:22:28|  imap.gmail.com | 172.253.63.108 |  50327 |  993  |  18:22:28|  imap.gmail.com | 172.253.63.108 |  50326 |  993  |  18:22:28|  www.zillow.com | 143.204.146.98 |  50325 |  443  |  18:22:28|  fonts.googleapis.com | \-- |  50324 |  443  |  18:22:28|  themes.googleusercontent.com | \-- |  50323 |  443  |  18:22:28|  fonts.gstatic.com | 172.253.115.94 |  50322 |  443  |  18:22:27|  s.zillowstatic.com | 143.204.146.15 |  50321 |  443  |  18:22:27|  www.zillowstatic.com | 143.204.146.90 |  50320 |  443  | 18:07:36|  setup.icloud.com | \-- |  50319 |  443  |  18:07:36|  iosapps.itunes.apple.com| \-- |  50318 |  443  |  17:50:29|  collector-pxhyx10rg3.perimeterx.net | 35.190.10.96 |  50317 |  443  |  17:50:29|  doh.dns.apple.com | 17.253.20.247|  50316 |  443  |  17:50:29|  firebaselogging-pa.googleapis.com | 74.125.21.95 |  50315 |  443  | Router log of URLs outside VPN tunnel  
  
A quick glance makes it obvious that I used both Zillow and Gmail while running this test. I also tried to read the Wall Street Journal which explains the images.wsj.net and bartender.mobile.dowjones.io domains. I don't know what perimeterx.net is but clearly they are collecting something. Some destination IP addresses have been redacted for my own reasons. 

A close look at the source port numbers shows an interesting trend, they constantly increase by 1. Only Apple knows what that indicates. 

Two things in the above report annoy me no end 

  1. The first is Apple having their own DNS server doh.dns.apple.com. My iPad is configured to use NextDNS system-wide. It seems that Apple does what they want, both with DNS and with VPNs, regardless of what the iOS user indicates they want. 
  2. Facebook. Of course. The iPad does not have either the Facebook or Instagram apps installed. One of the installed Apps (I can not tell which one by looking at the router) is phoning home to Facebook, spying on me, and doing so outside the VPN, thus adding insult to injury. 

**FACEBOOK (off topic)**

OK, this is off-topic, but I found it interesting. The iOS App Privacy Report also showed accesses to graph.facebook.com as you see here at the right. Clicking on the domain name brings up the apps that were phoning home to Facebook to spy on me.  | ![](pix/ios.app.privacy.report.600w.webp)  
---|---  
The report unmasked these five apps. However, I forgive Brave because the Facebook access was probably done by a website it was displaying. As for the New York Times, Flipboard, Feedly and The Atlantic. Phooey.  A more technical response to this would be use to use DNS to insure that the device can never contact graph.facebook.com at all.  The App Privacy Report is a great feature. It was introduced in iOS 15. That said, it does not appear to collect data when the device is connected to a VPN.  | ![](pix/ios.app.privacy.report.facebook.600w.webp)  
  
### WIRESHARK TESTING

Added this section on August 27, 2022

No analysis of data traffic is complete with a full packet trace examined by Wireshark. So, I finally did one. This test lasted only a minute (give or take) so what it found may well be just the tip of the iceberg. 

The Peplink Balance 20x router can collect full packet logs by itself, a feature Peplink calls "Network capture", and that is how I collected the data which is stored, initially, in the router itself. The collection stops when there is 20 megabytes of data, which can be easily downloaded from the router to a computer. The cap on the amount of collected data is why the test was so short. 

The iPad was running iOS 15.6.1 and had been connected to a VPN for maybe an hour before I started the pcap trace/log. The ProtonVPN app was used to make a WireGuard connection to a VPN server at 66.115.146.172 on UDP port 443.

Let me preface this discussion with a warning: I am no expert at using Wireshark.

I started my analysis at Statistics -> Conversations to see an overview of the collected sessions. The router had captured 13 TCP conversations and 11 UDP ones.

Below are all the TCP conversations that started from the iPad (192.168.8.78). Considering that the VPN is using UDP, there should be no TCP sessions leaving the iPad. So, still more proof of iOS VPNs leaking.

![TCP conversations from the iPad](pix/ios.vpn.leak.wireshark.tcp.convos.webp)  
TCP conversations from the iPad (Address A) 

The target IP addresses were 104.70.51.110, 104.70.71.223 and 23.50.230.157. My research shows that these IP addresses are used to host both akamaitechnologies.com and apple.com domains. For example: a104-70-71-223.deploy.static.akamaitechnologies.com and gspa35-kr-ssl.ls.apple.com. 

I can not be sure, but the fact that the source port is consistently increasing by 1, may indicate that these are new sessions rather than old ones.

As for the UDP conversations, we see below that the vast majority of packets were sent to the VPN server (66.115.146.172).

![UDP conversations from the iPad](pix/ios.vpn.leak.wireshark.udp.convos.webp)  
UDP conversations from the iPad (Address A) 

But ... seven times the iPad sent UDP packets to the router (192.168.8.8) at port 53, which is old, insecure, easily-spied-on, easily-modified-in-flight DNS. Yikes. Again, Apple said _"The behavior you are seeing is expected."_

Below is a Wireshark report showing the VPN-connected iPad sending old school, unencrypted, easily spied on, DNS requests to the router.

![UDP conversations from the iPad](pix/ios.vpn.leak.wireshark.dns.webp)  
DNS requests from the iPad (192.168.8.78) 

The first two and the last two lines above show data correctly flowing through the Wireguard VPN tunnel. The middle three lines, however, show the iPad sending three DNS queries to the router (192.168.8.8). These are three of the UDP requests sent to port 53 of the router. 

This is **doubly bad**. The iPad is configured to use NextDNS system-wide. If iOS is going to send data outside the VPN tunnel, the least it could do is send the DNS queries to the configured DNS provider. But, no. 

Clearly, Apple is no more trustworthy than Enron. Not only does iOS 15.6.1 ignore the VPN connection, it also ignores the DNS settings.

Again, this test lasted one lousy minute. Who knows what skeletons would have turned up in a longer test. 

**ANOTHER TEST** (August 31, 2022)

The last test was short lived due to the limited amount of storage in the router for collecting captured packets. So, I decided to try again, and this time I changed both the VPN vendor and the type of VPN connection.

This test was run with the Windscribe VPN app (version 3.3.0) making an OpenVPN connection over UDP port 80. Logging of all packets by the router was turned on after the VPN tunnel had been established. The logging lasted about 45 seconds. 

Wireshark showed that the test iPad had only one UDP conversation partner, the VPN server. However, it also showed a TCP conversation partner, so, as expected, more data outside the VPN tunnel.

The first packet in this conversation came from the remote IP address so it was from connection that started before the packet capture. The remote IP address was 17.57.144.10, one of Apple's own (as noted earlier, they own all IP addresses that start with 17). The connection was to port 5223 on the Apple side and this port has been seen a number of times in earlier tests. According to Shodan, the IP address is associated with three names: courier.push.apple.com, courier2.push.apple.com, and windows.courier.push.apple.com. 

**TESTING WITH THE WIREGUARD APP** (Sept 4, 2022) ![Wireguard iOS app](pix/wireguard.ios.app440.webp)

I have already tested with three different apps from three different VPN companies, but since the Wireshark tests are so short, I decided to do another one, and, while at it, to test a fourth app.

This time I used the [Wireguard iOS app](https://apps.apple.com/app/wireguard/id1441195209). The app, as you can see here, is from the WireGuard Development Team, not from a VPN company. I used it to connect to Windscribe because Windscribe lets their customers create a small Wireguard configuration file that can be imported into the WireGuard app. Shades of the old days with OpenVPN. I had previously used the Windscribe-generated WireGuard config files in the [pcWRT router](https://www.routersecurity.org/pcwrt.php). 

The WireGuard app was version 1.0.15 (26), the iPad was running iOS 15.6.1.

This time I started the logging before creating the VPN tunnel, so I can no longer use the Wireshark Conversations feature, as it includes conversations before the VPN started. But, the log from the creation of the VPN tunnel turned up some interesting DNS entries.

The VPN server name was dfw-192-wg.whiskergalaxy.com and the first step in creating the VPN connection is, naturally, a DNS query for this name. You see this in the Wireshark report below. The iPad is 192.168.8.79. 

![DNS queries for the VPN server](pix/wireshark.log.oldDNS.crop.webp)  
DNS queries for the VPN server 

This has nothing to do with a VPN leak, rather it is yet another example of iOS not honoring the system wide DNS setting. The iPad is supposed to be using NextDNS system wide. Tests run in web browsers show they do use it. But, not here.

These two DNS requests (an A and an AAAA request) violate the system-wide setting in two respects. First, they are old school un-encrypted DNS requests to UDP port 53 rather than secure/encrypted DNS requests. And, they are sent to the router (192.168.8.8) not to NextDNS. 

I am not sure here if the fault is with iOS or the WireGuard app. I will try to contact the WireGuard Development Team. Contacting Apple is likely a waste of time.

As for VPN leaks, this test found a single example. In the trace excerpt shown [here](pix/wireguard.app.wireshark.log.webp) we see that the vast majority of communication from the iPad (192.168.8.79) is to the Wireguard VPN server at 23.95.42.212. Fine.

But, we also see a couple communications from the iPad outside the tunnel. These two outbound requests were to TCP port 5223 at IP address 17.57.144.11.

According [to Shodan](https://www.shodan.io/host/17.57.144.11), this IP address is used for courier.push.apple.com, courier2.push.apple.com, and windows.courier.push.apple.com. According [to Apple](https://support.apple.com/en-us/HT202944) port 5223 is used by their Push Notification Service. Apps that use this service include iCloud DAV Services (Contacts, Calendars, Bookmarks), Push Notifications, FaceTime, iMessage, Game Center and Photo Stream. 

The packet trace lasted only 97 seconds but it showed a few other outbound requests, exactly like this to 17.57.144.11. It also showed the iPad on the receiving end of communication from this IP address. Pretty chatty.

To dig a bit further, the TCP flags in the packet trace show that this socket/thread/session started before the VPN tunnel was created. This confirms the recent update made by ProtonVPN to their blog, that existing sockets are not all killed when the VPN connection is first made. It did seem that some were killed, but an exact analysis of that is beyond me.

And, this rabbit hole keeps getting deeper. The packet trace also showed something interesting on the LAN side. I'll write that up soon.

Update September 13, 2022: I notified the WireGuard development team about this VPN leak on September 5th. No response.  
  
---  
  
  
  
[Home](index.php) => VPNs on iOS are a scam  |  | TOP  
michael--at--michaelhorowitz.com  |  |  Last Updated: August 21, 2025 11PM UTC  
---|---|---  
|  ![License Plate](pix/license_mh.1986.jpg)  
Copyright 2001-2026 | Copyright 2001-2026 |  
  
Printed at: June 28, 2026 4:58am ET

Viewed 373,690 times since May 25, 2022 (250/day over 1,494 days)
