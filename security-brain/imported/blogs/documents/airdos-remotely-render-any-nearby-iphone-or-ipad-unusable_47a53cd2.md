---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-10_airdos-remotely-render-any-nearby-iphone-or-ipad-unusable.md
original_filename: 2019-12-10_airdos-remotely-render-any-nearby-iphone-or-ipad-unusable.md
title: 'AirDoS: Remotely render any nearby iPhone or iPad unusable'
category: documents
detected_topics:
- access-control
- command-injection
- rate-limit
- api-security
- mobile-security
tags:
- imported
- documents
- access-control
- command-injection
- rate-limit
- api-security
- mobile-security
language: en
raw_sha256: 47a53cd2bf1cd6b450d0840b0c26fd2b506fb8f6251985161ac4770b73ccf992
text_sha256: 66ec32d70069a0326859660b24e59abcc2cf48087296d33a0cf6fb65017a5e4a
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# AirDoS: Remotely render any nearby iPhone or iPad unusable

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-10_airdos-remotely-render-any-nearby-iphone-or-ipad-unusable.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, rate-limit, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `47a53cd2bf1cd6b450d0840b0c26fd2b506fb8f6251985161ac4770b73ccf992`
- Text SHA256: `66ec32d70069a0326859660b24e59abcc2cf48087296d33a0cf6fb65017a5e4a`


## Content

---
title: "AirDoS: Remotely render any nearby iPhone or iPad unusable"
url: "https://kishanbagaria.com/airdos/"
final_url: "https://kishan.org/airdos/"
authors: ["Kishan Bagaria (@KishanBagaria)"]
programs: ["Apple"]
bugs: ["DoS"]
publication_date: "2019-12-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4897
---

# AirDoS: Remotely render any nearby iPhone or iPad unusable

What if you could walk into a room and make every* iPhone or iPad unusable while you're there? Wait, that sounds evil. What if you could get that one annoying person off their iPhone who's always on it?

I discovered a denial-of-service bug in iOS that I'm calling AirDoS which lets an attacker infinitely spam all nearby iOS devices with the AirDrop share popup. This share popup blocks the UI so the device owner won't be able to do anything on the device except Accept/Decline the popup, which will keep reappearing. It will persist even after locking/unlocking the device.

*This bug is still subject to the AirDrop receiving setting, meaning if your AirDrop setting is set to "Everyone", anyone can be the attacker, but if it's set to "Contacts Only", only someone in your contacts can be the attacker.

How would you stop this if someone were to use this attack on you? Simply run away! It'll get you out of range from the attacking device. Okay, I'm not sure how well this'd work in an airplane.

Besides getting away from the attacker, who is also unidentifiable most of the time, you can stop this by turning off AirDrop/WiFi/Bluetooth. This can be done if you can access Control Center from the lock screen but not if you have it disabled. Either way, you can ask Siri to turn off WiFi or Bluetooth. Restarting your device may also give you some time to turn AirDrop off before the attack takes place again.

To prevent this attack from taking place at all, turn on AirDrop only when you need it and don't ever keep it set to "Everyone".

I reported this bug to Apple in August 2019. It's been fixed in iOS 13.3 with a rate limit (after declining the same device 3 times, iOS will automatically decline any subsequent requests).

I've posted my PoC exploit [on GitHub](https://github.com/KishanBagaria/AirDoS). It supports multiple devices but deliberately doesn't support devices that have their AirDrop receiving setting set to "Contacts Only" to reduce the impact of publicly posting the exploit.

Huge thanks to Milan Stute and Alexander Heinrich, for authoring [opendrop](https://github.com/seemoo-lab/opendrop) which powers the exploit and which originally inspired me to try this out (literally found it after five minutes of playing with opendrop).

This is a simple bug and can also be exploited for a single device with a simple infinite loop and opendrop:
  
  
  while true; do opendrop send -r 0 -f totally-random-file; done
  

### macOS

macOS shows the AirDrop share popup differently than iOS and doesn't block the UI. An attacker could still send a lot of share requests to spam someone but since the UI is non-blocking, they can easily turn off AirDrop or WiFi/Bluetooth. [Here's a video](https://www.youtube.com/watch?v=4gTEhVFSDn4) of how it looks like on macOS.

A fix for this has been implemented in macOS Catalina 10.15.2, Security Update 2019-002 Mojave and Security Update 2019-007 High Sierra.

### Timeline

**2019-08-19** : Report sent to Apple

**2019-10-03** : Asked for status update

**2019-10-03** : Apple replied: "We are still investigating this issue. If we determine that our products are affected, then we may prepare a security update for our customers."

**2019-11-14** : Apple emailed: "We will be addressing the issue you reported with a mitigation in an upcoming security update and would appreciate your assessment of whether our latest beta of iOS 13.3 addresses the issue. […] While it will not receive a CVE, we want to publicly acknowledge your assistance in our security advisory."

**2019-11-15** : I replied confirming bug is fixed in iOS 13.3 public beta 2 and asked when can I publicly disclose

**2019-11-15** : Apple replied: "We would appreciate it if you can withhold public discussion of this issue until the security update is released to our customers. The security update is currently planned for mid-December 2019."

**2019-12-10** : iOS 13.3 released, [security](https://support.apple.com/en-us/HT210788) [advisories](https://support.apple.com/en-us/HT210785) published and publicly disclosed
