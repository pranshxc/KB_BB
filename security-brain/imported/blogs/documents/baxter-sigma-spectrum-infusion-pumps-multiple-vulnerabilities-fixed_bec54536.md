---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-08_baxter-sigma-spectrum-infusion-pumps-multiple-vulnerabilities-fixed.md
original_filename: 2022-09-08_baxter-sigma-spectrum-infusion-pumps-multiple-vulnerabilities-fixed.md
title: 'Baxter SIGMA Spectrum Infusion Pumps: Multiple Vulnerabilities (FIXED)'
category: documents
detected_topics:
- command-injection
- sso
- idor
- automation-abuse
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- sso
- idor
- automation-abuse
- information-disclosure
- api-security
language: en
raw_sha256: bec545364b17a6297f30b09ffe74e36292334d6450f73ce9b4e2a47b78905e5c
text_sha256: d92a4e4b1c484a042f0c1fb9f96223c753271909b930f78aa94652c226b810ec
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Baxter SIGMA Spectrum Infusion Pumps: Multiple Vulnerabilities (FIXED)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-08_baxter-sigma-spectrum-infusion-pumps-multiple-vulnerabilities-fixed.md
- Source Type: markdown
- Detected Topics: command-injection, sso, idor, automation-abuse, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `bec545364b17a6297f30b09ffe74e36292334d6450f73ce9b4e2a47b78905e5c`
- Text SHA256: `d92a4e4b1c484a042f0c1fb9f96223c753271909b930f78aa94652c226b810ec`


## Content

---
title: "Baxter SIGMA Spectrum Infusion Pumps: Multiple Vulnerabilities (FIXED)"
page_title: "Baxter SIGMA Spectrum Infusion Pumps: Multiple Vulnerabilities (FIXED) | Rapid7 Blog"
url: "https://www.rapid7.com/blog/post/2022/09/08/baxter-sigma-spectrum-infusion-pumps-multiple-vulnerabilities-fixed/"
final_url: "https://www.rapid7.com/blog/post/2022/09/08/baxter-sigma-spectrum-infusion-pumps-multiple-vulnerabilities-fixed/"
authors: ["Deral Heiland (@Percent_X)"]
programs: ["Baxter Healthcare"]
bugs: ["Hardcoded credentials", "Memory corruption", "MiTM", "Information disclosure"]
publication_date: "2022-09-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2193
---

Rapid7, Inc. (Rapid7) discovered vulnerabilities in two TCP/IP-enabled medical devices produced by Baxter Healthcare. The affected products are:

  * SIGMA Spectrum Infusion Pump (Firmware Version 8.00.01)
  * SIGMA Wi-Fi Battery (Firmware Versions 16, 17, 20 D29)

Rapid7 initially reported these issues to Baxter on April 20, 2022. Since then, members of our research team have worked alongside the vendor to discuss the impact, resolution, and a coordinated response for these vulnerabilities.

## Product description

Baxter’s SIGMA Spectrum product is a commonly used brand of infusion pumps, which are typically used by hospitals to deliver medication and nutrition directly into a patient’s circulatory system. These TCP/IP-enabled devices deliver data to healthcare providers to enable more effective, coordinated care.

## Credit

The vulnerabilities in two TCP/IP-enabled medical devices were discovered by Deral Heiland, Principal IoT Researcher at Rapid7. They are being disclosed in accordance with [Rapid7’s vulnerability disclosure policy](/security/disclosure/) after coordination with the vendor.

## Vendor statement

"In support of our mission to save and sustain lives, Baxter takes product security seriously. We are committed to working with the security researcher community to verify and respond to legitimate vulnerabilities and ask researchers to participate in our responsible reporting process. Software updates to disable Telnet and FTP (CVE-2022-26392) are in process. Software updates to address the format string attack (CVE-2022-26393) are addressed in WBM version 20D30 and all other WBM versions. Authentication is already available in Spectrum IQ (CVE-2022-26394). Instructions to erase all data and settings from WBMs and pumps before decommissioning and transferring to other facilities (CVE-2022-26390) are in process for incorporation into the Spectrum Operator’s Manual and are available in the [Baxter Security Bulletin](https://www.baxter.com/product-security#additionalresources)."

## Exploitation and remediation

This section details the potential for exploitation and our remediation guidance for the issues discovered and reported by Rapid7, so that defenders of this technology can gauge the impact of, and mitigations around, these issues appropriately.

## Battery units store Wi-Fi credentials (CVE-2022-26390)

Rapid7 researchers tested Spectrum battery units for vulnerabilities. We found all units that were tested store Wi-Fi credential data in non-volatile memory on the device.

When a Wi-Fi battery unit is connected to the primary infusion pump and the infusion pump is powered up, the pump will transfer the Wi-Fi credential to the battery unit.

### Exploitation

An attacker with physical access to an infusion pump could install a Wi-Fi battery unit (easily purchased on eBay), and then quickly power-cycle the infusion pump and remove the Wi-Fi battery – allowing them to walk away with critical Wi-Fi data once a unit has been disassembled and reverse-engineered.

Also, since these battery units store Wi-Fi credentials in non-volatile memory, there is a risk that when the devices are de-acquisitioned and no efforts are made to overwrite the stored data, anyone acquiring these devices on the secondary market could gain access to critical Wi-Fi credentials of the organization that de-acquisitioned the devices.

### Remediation

To mitigate this vulnerability, organizations should restrict physical access by any unauthorized personnel to the infusion pumps or associated Wi-Fi battery units.

In addition, before de-acquisitioning the battery units, batteries should be plugged into a unit with invalid or blank Wi-Fi credentials configured and the unit powered up. This will overwrite the Wi-Fi credentials stored in the non-volatile memory of the batteries. Wi-Fi must be enabled on the infusion pump unit for this overwrite to work properly.

## Format string vulnerabilities

### “Hostmessage” (CVE-2022-26392)

When running a telnet session on the Baxter Sigma Wi-Fi Battery Firmware Version 16, the command “hostmessage” is vulnerable to format string vulnerability. 

**Exploitation**

An attacker could trigger this format string vulnerability by entering the following command during a telnet session:

![image4-1.png](https://www.rapid7.com/cdn/images/blte640f9b314fc2353/683ddcc23323a5134180a7af/image4-1.png)

To view the output of this format string vulnerability, `_settrace state=on`_ must be enabled in the telnet session. _`set trace`_ does not need to be enabled for the format string vulnerability to be triggered, but it does need to be enabled if the output of the vulnerability is to be viewed.

Once _`set trace`_ is enabled and showing output within the telnet session screen, the output of the vulnerability can be viewed, as shown below, where each _`%x`_ returned data from the device’s process stack.

![image7-1.png](https://www.rapid7.com/cdn/images/blt26e66ffa54760886/683ddce6590d7fac3dde1a4d/image7-1.png)

### SSID (CVE-2022-26393)

Rapid7 also found another format string vulnerability on Wi-Fi battery software version 20 D29. This vulnerability is triggered within SSID processing by the _`get_wifi_location (20)`_ command being sent via XML to the Wi-Fi battery at TCP port 51243 or UDP port 51243.

![image2-1.png](https://www.rapid7.com/cdn/images/bltacf2eac30bb73cc1/683ddd183d7b5e6f66136518/image2-1.png)

**Exploitation**

This format string vulnerability can be triggered by first setting up a Wi-Fi access point containing format string specifiers in the SSID. Next, an attacker could send a _`get_wifi_location (20)`_ command via TCP Port 51243 or UDP port 51243 to the infusion pump. This causes the device to process the SSID name of the access point nearby and trigger the exploit. The results of the triggering of format strings can be viewed with trace log output within a telnet session as shown below.

![image3-1.png](https://www.rapid7.com/cdn/images/bltbdb1a7314dd5a10c/683ddd414c5a095ca75e09bd/image3-1.png)

The SSID of _`AAAA%x%x%x%x%x%x%x%x%x%x%x%x%x%x`_ allows for control of 4 bytes on the stack, as shown above, using the _`%x`_ to walk the stack until it reaches 41414141. By changing the leading _`AAAA`_ in the SSID, a malicious actor could potentially use the format string injection to read and write arbitrary memory. At a minimum, using format strings of _`%s`_ and _`%n`_ could allow for a denial of service (DoS) by triggering an illegal memory read (_`%s`_) and/or illegal memory write (_`%n`_).

Note that in order to trigger this DoS effect, the attacker would need to be within normal radio range and either be on the device's network or wait for an authorized _`get_wifi_location`_ command (the latter would itself be a usual, non-default event).

**Remediation**

To prevent exploitation, organizations should restrict access to the network segments containing the infusion pumps. They should also monitor network traffic for any unauthorized host communicating over TCP and UDP port 51243 to infusion pumps. In addition, be sure to monitor Wi-Fi space for rogue access points containing format string specifiers within the SSID name.

## Unauthenticated network reconfiguration via TCP/UDP (CVE-2022-26394)

All Wi-Fi battery units tested (versions 16, 17, and 20 D29) allowed for remote unauthenticated changing of the SIGMA GW IP address. The SIGMA GW setting is used for configuring the back-end communication services for the devices operation.

### Exploitation

An attacker could accomplish a remote redirect of SIGMA GW by sending an XML command 15 to TCP or UDP port 51243. During testing, only the SIGMA GW IP was found to be remotely changeable using this command. An example of this command and associated structure is shown below:

![image1-2.png](https://www.rapid7.com/cdn/images/blt92a68579dd4c0f6b/683ddd67abf2ad86193c427b/image1-2.png)

This could be used by a malicious actor to man-in-the-middle (MitM) all the communication initiated by the infusion pump. This could lead to information leakage and/or data being manipulated by a malicious actor.

### Remediation

Organizations using SIGMA Spectrum products should restrict access to the network segments containing the infusion pumps. They should also monitor network traffic for any unauthorized host communicating over TCP and UDP port 51243 to the infusion pumps.

## UART configuration access to Wi-Fi configuration data (additional finding)

The SIGMA Spectrum infusion pump unit transmits data unencrypted to the Wi-Fi battery unit via universal asynchronous receiver-transmitter (UART). During the power-up cycle of the infusion pump, the first block of data contains the Wi-Fi configuration data. This communication contains the SSID and 64-Character hex PSK.

![image5-1.png](https://www.rapid7.com/cdn/images/blt9d0336140c5b2025/683ddd8d70aa9524b4fe2f85/image5-1.png)

### Exploitation

A malicious actor with **physical access** to an infusion pump can place a communication shim between the units (i.e., the pump and the Wi-Fi battery) and capture this data during the power-up cycle of the unit.

![image6-1.png](https://www.rapid7.com/cdn/images/bltd299f359fc471fbe/683dddb12a9b688da22bd17b/image6-1.png)

### Remediation  

To help prevent exploitation, organizations should restrict physical access by unauthorized persons to the infusion pumps and associated Wi-Fi battery units.

Note that this is merely an additional finding based on physical, hands-on access to the device. While Baxter has addressed this finding through better decommissioning advice to end users, this particular issue does not rank for its own CVE identifier, as local encryption is beyond the scope of the hardware design of the device.

## Disclosure timeline

Baxter is an exemplary medical technology company with an obvious commitment to patient and hospital safety. While medtech vulnerabilities can be tricky and expensive to work through, we're quite pleased with the responsiveness, transparency, and genuine interest shown by Baxter's product security teams.

  * **April, 2022:** Issues discovered by [Deral Heiland](https://twitter.com/Percent_X) of Rapid7
  * **Wed, April 20, 2022:** Issues reported to [Baxter product security](https://www.baxter.com/product-security#disclosure)
  * **Wed, May 11, 2022:** Update requested from Baxter
  * **Wed, Jun 1, 2022:** Teleconference with Baxter and Rapid7 presenting findings
  * **Jun-Jul 2022:** Several follow up conversations and updates between Baxter and Rapid7
  * **Tue, Aug 2, 2022:** Coordination tracking over [VINCE](https://www.kb.cert.org/vince/) and more teleconferencing involving Baxter, Rapid7, CERT/CC, and [ICS-CERT](https://www.cisa.gov/uscert/ics/advisories) (VU#142423)
  * **Wed, Aug 31, 2022:** Final review of findings and mitigations
  * **Thu Sep 8, 2022:** Baxter advisory [published](https://www.baxter.com/product-security#additionalresources)
  * **Thu, Sep 8, 2022:** Public disclosure of these issues
  * **Thu, Sep 8, 2022:** ICS-CERT [advisory published](https://www.cisa.gov/uscert/ics/advisories/icsma-22-251-01)

  

 _**Additional reading:**_

  * [_Rapid7 Discovered Vulnerabilities in Cisco ASA, ASDM, and FirePOWER Services Software_](/blog/post/2022/08/11/rapid7-discovered-vulnerabilities-in-cisco-asa-asdm-and-firepower-services-software/)
  * [ _CVE-2022-31660 and CVE-2022-31661 (FIXED): VMware Workspace ONE Access, Identity Manager, and vRealize Automation LPE_](/blog/post/2022/08/05/cve-2022-31660-and-cve-2022-31661-fixed-vmware-workspace-one-access-identity-manager-and-vrealize-automation-lpe/)
  * [ _QNAP Poisoned XML Command Injection (Silently Patched)_](/blog/post/2022/08/04/qnap-poisoned-xml-command-injection-silently-patched/)
  * [_Primary Arms PII Disclosure via IDOR (FIXED)_](/blog/post/2022/08/02/primary-arms-pii-disclosure-via-idor/)

[![LinkedIn](/linkedin-logo.svg)](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2022%2F09%2F08%2Fbaxter-sigma-spectrum-infusion-pumps-multiple-vulnerabilities-fixed&title=Baxter%20SIGMA%20Spectrum%20Infusion%20Pumps%3A%20Multiple%20Vulnerabilities%20\(FIXED\))[![Facebook](/facebook-logo.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2022%2F09%2F08%2Fbaxter-sigma-spectrum-infusion-pumps-multiple-vulnerabilities-fixed)[![X](/x-logo.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2022%2F09%2F08%2Fbaxter-sigma-spectrum-infusion-pumps-multiple-vulnerabilities-fixed&text=Baxter%20SIGMA%20Spectrum%20Infusion%20Pumps%3A%20Multiple%20Vulnerabilities%20\(FIXED\))[![Bluesky](/bluesky-dark-logo.svg)](https://bsky.app/intent/compose?text=Baxter%20SIGMA%20Spectrum%20Infusion%20Pumps%3A%20Multiple%20Vulnerabilities%20\(FIXED\)%20https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2022%2F09%2F08%2Fbaxter-sigma-spectrum-infusion-pumps-multiple-vulnerabilities-fixed)

#### Article Tags

  * [Vulnerability Disclosure](/blog/tag/vulnerability-disclosure/)
  * [Research](/blog/tag/research/)
  * [IoT](/blog/tag/iot-security-news/)

[![Deral Heiland](/_next/image/?url=https%3A%2F%2Fwww.rapid7.com%2Fcdn%2Fimages%2Fblt9f9db121928e3816%2F6840441898bc4eb9f1818b21%2FDeral-Heiland.jpg&w=256&q=75)Deral HeilandAuthor Posts](/blog/author/deral-heiland/)
