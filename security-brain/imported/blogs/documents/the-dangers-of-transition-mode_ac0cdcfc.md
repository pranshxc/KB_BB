---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-02_the-dangers-of-transition-mode.md
original_filename: 2024-07-02_the-dangers-of-transition-mode.md
title: The Dangers of Transition Mode
category: documents
detected_topics:
- ssrf
- command-injection
- rate-limit
- automation-abuse
- api-security
tags:
- imported
- documents
- ssrf
- command-injection
- rate-limit
- automation-abuse
- api-security
language: en
raw_sha256: ac0cdcfc634cb80d7eace0004f24cf2225f203b7e9ea695314d390211b334ef1
text_sha256: acf1fe404b2cb95deebc82fdc732ada56bda3e65a10de86eb43d07cdd36c4fc6
ingested_at: '2026-06-28T07:32:35Z'
sensitivity: unknown
redactions_applied: false
---

# The Dangers of Transition Mode

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-02_the-dangers-of-transition-mode.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, rate-limit, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:35Z
- Redactions Applied: False
- Raw SHA256: `ac0cdcfc634cb80d7eace0004f24cf2225f203b7e9ea695314d390211b334ef1`
- Text SHA256: `acf1fe404b2cb95deebc82fdc732ada56bda3e65a10de86eb43d07cdd36c4fc6`


## Content

---
title: "The Dangers of Transition Mode"
page_title: "TrustedSec | The Dangers of Transition Mode"
url: "https://trustedsec.com/blog/the-dangers-of-transition-mode"
final_url: "https://trustedsec.com/blog/the-dangers-of-transition-mode"
authors: ["Michael Bond (@bond006_5)", "David Boyd (@fir3d0g)"]
bugs: ["Wifi hacking"]
publication_date: "2024-07-02"
added_date: "2024-07-30"
source: "pentester.land/writeups.json"
original_index: 199
---

* [Blog](https://trustedsec.com/blog)
  * [The Dangers of Transition Mode](https://trustedsec.com/blog/the-dangers-of-transition-mode)

July 02, 2024

# The Dangers of Transition Mode

Written by Michael Bond and David Boyd 

Penetration Testing

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/DangersOfTransitionMode_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1767064025&s=f96077ca991eb734366a79535bd34654)

Table of contents

  * Remediation
  * Conclusion
  * References

Share

  * [Share URL]( "Share URL")
  * [Share via Email](/cdn-cgi/l/email-protection#734c000611191610074e301b1610185641431c0607564143071b1a005641431201071a101f1656414315011c1e5641432701060007161720161056414255121e0348111c170a4e271b1656414337121d141601005641431c155641432701121d001a071a1c1d5641433e1c17165640325641431b07070300564032564135564135070106000716170016105d101c1e564135111f1c14564135071b165e17121d141601005e1c155e0701121d001a071a1c1d5e1e1c1716 "Share via Email")
  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-dangers-of-transition-mode "Share on Facebook")
  * [Share on X](https://twitter.com/share?text=The%20Dangers%20of%20Transition%20Mode%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-dangers-of-transition-mode "Share on X")
  * [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-dangers-of-transition-mode&mini=true "Share on LinkedIn")

With the introduction of WPA3, it is becoming increasingly difficult to successfully exploit a wireless network. One of the main enhancements introduced in WPA3 is the Simultaneous Authentication of Equals (SAE) model. SAE was designed to replace the vulnerable Pre-Shared Key (PSK) method used in WPA2.

A WPA2 Personal network is susceptible to PSK passphrase brute-force attacks, where the 4-way handshake packets are captured during the authentication process. The hashed PSK is then extracted from these packets and transferred off-line in an attempt to recover the cleartext password with an application like [Hashcat](https://hashcat.net/hashcat/).

Once the cleartext PSK has been recovered, it can be used to connect to the wireless network and eavesdrop on other connected devices, or potentially used to gain a foothold within the internal network. One of the security enhancements with WPA3 is that the packets remain encrypted, and eavesdropping is not possible, even if the PSK password is guessed or known.

Another security enhancement is that WPA3 networks require the use of Protected Management Frames (PMF). With this requirement, management frames are not vulnerable to PKMID clientless attacks.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/BondBoyd_TransitionMode/BondBoyd_1.png?w=320&q=90&auto=format&fit=max&dm=1719499195&s=65fad30e6d592f4fb2b3de09684ff997)Figure 1 - WPA3 Handshake Layout

During a recent Wireless Penetration Test, we encountered a wireless network where WPA3 was advertised. Knowing the WPA3 security enhancements, it was assumed this assessment would be quick, with very little to be reported. However, an interesting discovery was made while reviewing the packet capture. The Service Set Identifier (SSID) of the WPA3 network was also being advertised as a WPA2 network.

To recreate the attack, we configured a lab environment with an SSID utilizing WPA3, in order to test what attack possibilities existed. Additional sample sets were collected against a MikroTik wireless router, a Cisco Meraki AP, an Ubiquiti wireless AP, and an Aruba AP.

To begin, we needed to locate and determine visible and hidden SSIDs, hardware information, signal strength, clients connecting, and encryption protocols in use. Within the lab environment, we leveraged the [aircrack-ng](https://www.aircrack-ng.org/) suite toolkit.

First, we enumerated the SSIDs with airodump-ng. We took note of the channels utilized, as well as the Basic Service Set Identifier (BSSID).
  
  
  sudo airodump-ng <wlan>

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/BondBoyd_TransitionMode/BondBoyd_2.png?w=320&q=90&auto=format&fit=max&dm=1719499196&s=4f206fc9e81f02ed18dd91494f424ad3)Figure 2 - Enumerating SSIDs

Next, we began capturing packets:
  
  
  sudo airodump-ng <wlan> --channel <channel> --bssid <bssid> -w capture

 _Tip: Click the 'Tab' key when seeing multiple SSIDs to add color for better readability and be able and shift through the list._

Looking at the captured data, we found a wireless network that was configured with WPA3 Personal.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/BondBoyd_TransitionMode/BondBoyd_3.png?w=320&q=90&auto=format&fit=max&dm=1719499196&s=dd395f2fc6795f6c2ed1ba12421d4f8f)Figure 3 - WPA3 Encryption Enumerated

Utilizing [Wireshark](https://www.wireshark.org/) for analysis, we uploaded the captured packet information and noticed that the captured packet advertised WPA2-PSK and WPA3-SAE. In addition, we observed that PMF protection was enabled for the SSID.

We used the following Wireshark filter to return specific data of our lab SSID:
  
  
  wlan.fc.type_subtype == 0x0008 && wlan.ssid == <ssid>

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/BondBoyd_TransitionMode/BondBoyd_4.png?w=320&q=90&auto=format&fit=max&dm=1719499199&s=0b118cc87bb1b2154aab1339b1f45f8a)Figure 4 - WPA3 Transition Mode Packet

Performing some quick research, it was discovered that the SSID was in transition mode. Transition mode is where WPA3 is interoperable with WPA2 devices and both modes are advertised. Transition mode was created to support the changeover from WPA2 to WPA3. This mode was intended to allow legacy hardware that did not have support for WPA3.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/BondBoyd_TransitionMode/BondBoyd_5.png?w=320&q=90&auto=format&fit=max&dm=1719499203&s=fe96afd791c5ba5b2da1cf88a47980e6)Figure 5 - Aruba WPA3 Transition Mode

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/BondBoyd_TransitionMode/BondBoyd_6.png?w=320&q=90&auto=format&fit=max&dm=1719499206&s=b8b4016a42bc094a682e826496c390da)Figure 6 - WPA3 Transition Mode (Ubiquiti)

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/BondBoyd_TransitionMode/BondBoyd_7.png?w=320&q=90&auto=format&fit=max&dm=1719499207&s=92bb690151c7c7854532607d2175d3d7)Figure 7 - WPA3 Transition Mode (MikroTik)

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/BondBoyd_TransitionMode/BondBoyd_8.png?w=320&q=90&auto=format&fit=max&dm=1719499207&s=8fcd5f2d7c4bb80024cf2525dd152421)Figure 8 - WPA3 Transition Mode (Meraki)

We did find it interesting that each one of the wireless cards only detected WPA3 being advertised for the SSID and not WPA2. [Wifite2](https://github.com/derv82/wifite2) was used to perform additional scanning.

Sadly, upon reviewing the Wifite2 repository, there were no references to WPA3 attacks. The [kimcoder](https://github.com/kimocoder/wifite2) fork of Wifite2 is still being maintained, so hopefully there will be support for WPA3 attacks in the future.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/BondBoyd_TransitionMode/BondBoyd_9.png?w=320&q=90&auto=format&fit=max&dm=1719499208&s=c549e87d048ba38760008f7fd95296d0)Figure 9 - Wifite WPA2 Scanning

However, utilizing Wifite2 paid off, and we were successful in capturing a WPA2 handshake. A PKMID attack was also attempted, but this failed due to PMF being enabled.

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/BondBoyd_TransitionMode/BondBoyd_10.png?w=320&q=90&auto=format&fit=max&dm=1719499209&s=1bfa202e011d98032536f7c5c31f6214)Figure 10 - Wifite WPA2 Captured Handshake

This handshake was taken offline, converted to a useable format, and then brute-forced with Hashcat to recover the plaintext PSK.

## Remediation

If WPA2 is no longer needed on the network, then disable transition mode. Disabling transition mode is not complicated, pending the AP make and model, simply turn off transition mode or disable WPA2 from the SSID configuration. A reset of the SSID or a reboot of the AP may be required.

If WPA2 is still required due to legacy hardware or applications, configure a strong complexed password and consider periodically changing the password.

## Conclusion

As demonstrated, a little creativity goes a long way during a wireless assessment. We wanted to expose the possible false sense of security for those using transition mode within their networks. Continue to utilize a strong PSK password to help mitigate password recovery for captured WPA2 handshakes.

If you have questions or comments, we would love to hear from you! Feel free to reach out on X/Twitter [@bond006_5](https://x.com/bond006_5) and [@fir3d0g](https://x.com/fir3d0g) or find us on the [TrustedSec Discord](https://discord.com/invite/trustedsec).

## References

<https://www.wi-fi.org/news-events/newsroom/wi-fi-alliance-introduces-wi-fi-certified-wpa3-security>

<https://www.wi-fi.org/knowledge-center/faq/what-are-protected-management-frames>

<https://www.networkworld.com/article/3316567/what-is-wpa3-wi-fi-security-protocol-strengthens-connections.html>

Recovering WPA2 Handshakes with Hashcat:

<https://hashcat.net/wiki/doku.php?id=cracking_wpawpa2>

WPA3 Meraki Basics:

<https://documentation.meraki.com/MR/Wi-Fi_Basics_and_Best_Practices/WPA3_Encryption_and_Configuration_Guide>

MikroTik WiFi Configuration:

<https://help.mikrotik.com/docs/display/ROS/WiFi>

Aruba WPA3 Configuration:

<https://www.arubanetworks.com/techdocs/Instant_83_WebHelp/Content/Instant_UG/Authentication/wpa3_authentication.htm>

Cisco WPA3 Deployment Guide:

<https://www.cisco.com/c/en/us/td/docs/wireless/controller/9800/technical-reference/wpa3-dg.html>

Ubiquiti Unifi:

<https://help.ui.com/hc/en-us/categories/6583256751383>

Share

  * [Share URL]( "Share URL")
  * [Share via Email](/cdn-cgi/l/email-protection#5b64282e39313e382f6618333e38307e696b342e2f7e696b2f3332287e696b3a292f3238373e7e696b3d2934367e696b0f292e282f3e3f083e387e696a7d3a362b6039343f22660f333e7e696b1f3a353c3e29287e696b343d7e696b0f293a3528322f3234357e696b16343f3e7e681a7e696b332f2f2b287e681a7e691d7e691d2f292e282f3e3f283e38753834367e691d3937343c7e691d2f333e763f3a353c3e292876343d762f293a3528322f3234357636343f3e "Share via Email")
  * [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-dangers-of-transition-mode "Share on Facebook")
  * [Share on X](https://twitter.com/share?text=The%20Dangers%20of%20Transition%20Mode%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-dangers-of-transition-mode "Share on X")
  * [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fthe-dangers-of-transition-mode&mini=true "Share on LinkedIn")
