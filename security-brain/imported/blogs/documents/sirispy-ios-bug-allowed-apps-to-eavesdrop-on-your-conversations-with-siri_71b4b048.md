---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-26_sirispy-ios-bug-allowed-apps-to-eavesdrop-on-your-conversations-with-siri.md
original_filename: 2022-10-26_sirispy-ios-bug-allowed-apps-to-eavesdrop-on-your-conversations-with-siri.md
title: SiriSpy - iOS bug allowed apps to eavesdrop on your conversations with Siri
category: documents
detected_topics:
- supply-chain
- access-control
- command-injection
- automation-abuse
- api-security
- mobile-security
tags:
- imported
- documents
- supply-chain
- access-control
- command-injection
- automation-abuse
- api-security
- mobile-security
language: en
raw_sha256: 71b4b0480950b511ea685618e9e167cbb5cb68571a924aabdd6b76f2708dd604
text_sha256: d4f30ce9c3d367b4ec620d7850143dc43c8541003079e73fc3ce3fc5c33fbff4
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# SiriSpy - iOS bug allowed apps to eavesdrop on your conversations with Siri

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-26_sirispy-ios-bug-allowed-apps-to-eavesdrop-on-your-conversations-with-siri.md
- Source Type: markdown
- Detected Topics: supply-chain, access-control, command-injection, automation-abuse, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `71b4b0480950b511ea685618e9e167cbb5cb68571a924aabdd6b76f2708dd604`
- Text SHA256: `d4f30ce9c3d367b4ec620d7850143dc43c8541003079e73fc3ce3fc5c33fbff4`


## Content

---
title: "SiriSpy - iOS bug allowed apps to eavesdrop on your conversations with Siri"
page_title: "SiriSpy - iOS bug allowed apps to eavesdrop on your conversations with Siri | Rambo Codes"
url: "https://rambo.codes/posts/2022-10-25-sirispy-ios-bug-allowed-apps-to-eavesdrop"
final_url: "https://rambo.codes/posts/2022-10-25-sirispy-ios-bug-allowed-apps-to-eavesdrop"
authors: ["Guilherme Rambo (@_inside)"]
programs: ["Apple"]
bugs: ["iOS", "MacOS", "Bluetooth", "Local Privilege Escalation", "TCC bypass"]
bounty: "7,000"
publication_date: "2022-10-26"
added_date: "2022-11-01"
source: "pentester.land/writeups.json"
original_index: 1986
---

# [SiriSpy - iOS bug allowed apps to eavesdrop on your conversations with Siri](/posts/2022-10-25-sirispy-ios-bug-allowed-apps-to-eavesdrop)

## Oct 26 2022 1:00 PM

**TL;DR:** Any app with access to Bluetooth could record your conversations with Siri and audio from the iOS keyboard dictation feature when using AirPods or Beats headsets. This would happen without the app requesting microphone access permission and without the app leaving any trace that it was listening to the microphone.

## Access to Sensitive Data on Apple's Platforms

One of the biggest myths when it comes to security and privacy on mobile devices is the old saying that Facebook is using your device's microphone to listen to everything you say, in order to sell more targeted ads. There's never been any evidence of that, and iPhones have very strong security measures in place to prevent such a thing.

_This section might be too basic for folks who are already familiar with how this stuff works under the hood, feel free to skip it._

The system that protects you from unfettered access to your sensitive data on Apple's operating systems is TCC (Transparency, Consent, and Control), which is directly responsible for most of the permission prompts you see when an app asks to access your location, calendar, microphone, camera, etc.

Access to system resources is mediated with the use of daemons, which are system processes that run in the background, many times with elevated privileges when compared to regular apps. Apps can then request information from those daemons, effectively opening a little door from their sandbox to the outside world.

Those doors are usually very tightly controlled on Apple's platforms with the use of code signing and entitlements. Out of the box, modern Apple devices will only run apps with a code signature that's been approved by Apple. You can think of a code signature of an app as the equivalent of a government-issued ID, where the government is Apple. Entitlements are like licenses, little bits of information that have also been verified by Apple and can give apps access to system resources that are normally not accessible.

All of these protections can be quite effective. However, their effectiveness relies heavily on how well Apple's engineers have implemented them in the system daemons, and sometimes unforeseen workarounds can result in a situation where the door has been very well shut and secured, but the window has been left wide open.

## AirPods and Siri

Since the introduction of the H1 chip with the AirPods (2nd generation), users can trigger "Hey, Siri" with AirPods, and talk to the assistant without much effort ~~and then receive a reply in the form of "here's what I found on the web..."~~. One thing you may or may not have noticed if you've used Siri with modern AirPods is that there's no disruption to audio quality when you're talking to Siri, even though you're using the microphone in the AirPods to do so. This is very different from when you're using it for a video conference, for example, where you'll notice a significant drop in the output audio quality.

I always wondered why that was the case. Knowing that the drop in output quality when using the microphone is a physical limitation of the Bluetooth standards used by AirPods and other similar headsets, how talk to Siri had been implemented on AirPods without disrupting audio quality had always been a bit of a mystery to me, but I never put much thought or effort into figuring that out.

As part of my work developing [AirBuddy](https://airbuddy.app), I'm constantly testing various aspects of AirPods and other Apple and Beats headsets in order to develop new features, troubleshoot issues, or just learn more about how these devices work under the hood.

I'm a fan of creating tools that make my job easier, so a while back I wrote a little command-line tool that I call `bleutil`, which can be used to interact with Bluetooth Low Energy devices on macOS. I use it all the time to debug what's going on with my AirPods by looking at the advertisement packets they're sending out.

![Screenshot of a Terminal window on macOS showing the invocation bleutil scan --mfg-prefix 4c0012 and a long list of timestamps, UUIDs, RSSI levels, MAC addresses and hex bytes](/assets/img/SiriSpy/bleutil.jpg)

While working on a new feature for this tool, which can be used to connect to a Bluetooth LE device and query its GATT¹ database, I decided to add the ability to subscribe to notifications to a service's characteristics using this tool, which would then stream a hexadecimal representation of the values over time to the Terminal window.

_¹ If you're not familiar with Bluetooth Low Energy terminology, GATT stands for "Generic Attribute Profile". It's a standard adopted by Bluetooth LE devices that allows them to send data back and forth using services and characteristics. You can think of services as folders on a file system, where each service can have a bunch of characteristics within it, which are like files._

I had never looked into the services and characteristics present on AirPods and similar devices because most of the information I use to power AirBuddy's features comes from advertisements or Bluetooth Classic, which don't require me to connect to the devices over Bluetooth LE and interact with the GATT database.

Naturally, while testing this new feature I was working on, I was wearing my AirPods. I noticed that the AirPods included a service with the UUID `9bd708d7-64c7-4e9f-9ded-f6b6c4551967`, and with characteristics that supported notifications². I ran my tool against my AirPods and left it running for a while, but no events came through.

_² In Bluetooth LE GATT, when a characteristic supports notifications (or indications), it means that other devices can subscribe to be notified when the data stored by that characteristic changes, without having to be constantly asking (polling) for the current data. It's essential for real-time communication between devices._

Digging a bit into it, I learned that `9bd708d7-64c7-4e9f-9ded-f6b6c4551967` is the DoAP service, a service used for Siri and Dictation support.

I decided to test it again. This time, while my tool was running and waiting for events to come from the AirPods, I invoked Siri while wearing them. As soon as I did that, a firehose of hex bytes started to stream down my Terminal window. Not only that, but as I spoke to Siri through my AirPods, I noticed that the bytes would change rapidly, and would settle down as I went silent again. Could it be that I was looking at audio data? 😨

You can watch a reproduction in the video below:

Demo video.

As it turns out, I was in fact looking at audio data coming from the AirPods. My first thought was "oh, so that's how they do it, this is cool". My second thought was "oh, no!".

_I always have mixed feelings when I discover something like this: a mix of excitement for having found a cool new thing to investigate and learn from, and disappointment/concern that this issue has been there in the wild, sometimes for years._

Finding out that I could get audio from AirPods without asking for permission to use the microphone on macOS was the first step.

The second step was checking Apple's other platforms to see if they were also affected. So I wrote a little app that I could run on iPhone, iPad, Apple Watch, and the Apple TV, then tried it out on devices running both the shipping version of iOS 15 and the latest iOS 16 beta at the time (this happened in late August).

The third step was figuring out what the audio data was. I was definitely seeing a bunch of bytes coming in, but who knows, maybe they were encrypted or something. The seemingly direct correlation between me speaking to Siri and the bytes changing had already made me think they weren't, but I had to confirm it.

### Decoding DoAP Audio

I know a little bit about how digital audio works, but it's definitely an area I've had very little experience in throughout my career in software development, limiting myself to using high level APIs such as Apple's `AVFoundation` whenever I have to deal with audio or video.

The first thing I tried was to grab the hex dump from my Terminal window, paste it into [HexFiend](https://hexfiend.com), then use the "open raw data" option in tools such as Audacity and Adobe Audition, trying various combinations of sample rate, bit rate, endianness, etc.

I did notice with some combinations of parameters that the garbled mess I was hearing did vaguely match the loudness of what I had said during the recording, which again told me the data was likely unencrypted.

In hindsight, I should've realized that it wouldn't make any sense for the audio being sent over Bluetooth LE to be uncompressed, given the bandwidth constraints of the technology. Now all I had to do was figure out which codec was being used, then I'd be able to decode the audio and play it back.

After looking through some of the system components responsible for this feature, I noticed that [Opus](https://opus-codec.org) was referenced quite a bit. Looking at the website for the Opus codec:

> Opus is unmatched for interactive speech [...]

Well, sounds a lot like the sort of thing you'd use for talking to digital assistants.

So I compiled the Opus library for all of Apple's platforms, then wrote a little app that would connect to the AirPods and keep the connection open in the background, listening to notifications and audio data.

It sounds simple, but the paragraph above comprises several hours of work – almost a full day – after which I had this:

Demo video.

Here's a summary of what the app does:

  * Asks for Bluetooth permission³
  * Finds a connected Bluetooth LE device that has the DoAP service
  * Subscribes to its characteristics to be notified of when streaming starts and stops, and when audio data comes in
  * When streaming starts, creates a new wav file, then feeds the Opus packets coming from the AirPods into a decoder, which then writes the uncompressed audio to the file
  * Once streaming stops, closes the wav file, then sends a local push notification to demonstrate that the app has successfully recorded the user in the background

In a real-world exploit scenario, an app that already has Bluetooth permission for some other reason could be doing this without any indication to the user that it's going on, because there's no request to access the microphone, and the indication in Control Center only lists "Siri & Dictation", not the app that was bypassing the microphone permission by talking directly to the AirPods over Bluetooth LE.

_³ Yes, even though this exploit bypasses the microphone permission, it still needs access to Bluetooth, so that permission is not bypassed. However, most users would not expect that giving an app access to Bluetooth could also give it access to their conversations with Siri and audio from dictation. And, as you'll see in the following paragraphs, I was also able to find a way around the Bluetooth permission on macOS._

### Full TCC Bypass on macOS

In the course of figuring out how things work for my report on the vulnerability described above, I had to investigate how Apple's operating systems communicate with the AirPods, which led me to discover another issue.

The system process responsible for handling of the DoAP protocol on Apple's platforms is `BTLEServerAgent` (or `BTLEServer`, depending on the platform). This agent or daemon provides an interface over the mach service `com.apple.BTLEAudioController.xpc`, which other processes on the system can use to request audio from the AirPods DoAP service.

There are hundreds (if not thousands) of mach services exposed by system agents and daemons on Apple's operating systems, but sandboxing restrictions and entitlement requirements prevent most apps from talking to them.

For services that are exposed to third-party apps, system daemons usually check for a specific entitlement before allowing an app to send requests to them, or put up a TCC prompt on the app's behalf, only allowing the communication to go through once the user has approved it.

[You can probably see where this is going](/posts/2022-03-15-how-a-macos-bug-could-have-allowed-for-a-serious-phishing-attack-against-users/): `BTLEServerAgent` did not have any entitlement checks or TCC prompts in place for its `com.apple.BTLEAudioController.xpc` service, so any process on the system could connect to it, send requests, and receive audio frames from AirPods. This exploit would only work on macOS, because the more restricted sandbox of iOS prevents apps from accessing most global mach services directly.

So at least on macOS, apps would be able to record your conversations with Siri or dictation audio without any permission prompts at all. Even worse, this particular exploit would also allow the app to request DoAP audio on-demand, bypassing the need to wait for the user to talk to Siri or use dictation.

Here's a demo of this in action:

Demo video.

Once again, these issues show that no matter how private and secure Apple's products and software can be, there's always more work to be done.

## Timeline

  * August 26, 2022: I discovered the issues and reported them to Apple’s security team
  * August 29, 2022: I got a reply confirming that they were investigating
  * October 24, 2022: iOS 16.1 and remaining Apple operating systems updated with the fix (CVE-2022-32946)
  * October 25, 2022: ~~after reaching out, I was told I'll be receiving a US$7000 bug bounty payment for reporting these issues~~ (see update below)

_November 9, 2022 - Update: The original version of this article mentioned a bug bounty payment of US$7000. However, this was due to an issue with the way Apple's security team had communicated about the bounty. They broke down the two vulnerabilities discovered into separate CVEs, one of which was awarded a bounty of US$7000, while the other one was awarded US$22500. So the total bounty payment for the bugs described in this report was of US$29500. Apple's security team apologized for the confusion, and has since released a new web platform for bug submissions, which should make this a lot better going forward._

## Update: Mitigations

When I first published this writeup, I hadn't included details about the mitigations Apple has put in place for the issues discussed, because to be honest they're not that interesting. Since a few folks have asked for details on this, here they are.

The main issue – direct access to AirPods DoAP over BLE GATT – was addressed by restricting access to the service. Even though AirPods and iPhones, Macs, etc are standard Bluetooth devices, Apple has a system in place to limit which services third-party apps can access, so they just added the DoAP service to that deny list.

For the second issue – talking to BTLEServerAgent on macOS – the system agent now correctly checks that the calling process has the `com.apple.bluetooth.system` entitlement before allowing communication to continue. This is the same entitlement that also opens up access to those "forbidden" GATT services.

Now, if an app attempts to talk to the agent without the appropriate entitlement, it closes the connection, then logs a passive-aggressive message to the console:

![Not an entitled process. Good bye.](/assets/img/SiriSpy/entitlement-console-message.jpg)
