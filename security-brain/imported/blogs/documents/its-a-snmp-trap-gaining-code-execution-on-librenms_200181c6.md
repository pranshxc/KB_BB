---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-29_its-a-snmp-trap-gaining-code-execution-on-librenms.md
original_filename: 2023-03-29_its-a-snmp-trap-gaining-code-execution-on-librenms.md
title: 'It’s a (SNMP) Trap: Gaining Code Execution on LibreNMS'
category: documents
detected_topics:
- command-injection
- xss
- access-control
- path-traversal
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- xss
- access-control
- path-traversal
- api-security
- supply-chain
language: en
raw_sha256: 200181c6bfd005d4a21c58495e37cef4f908d95ee03ffe7a00b9e001638e2bed
text_sha256: 121636b5f5fff911f9523b14c5f23c818f75f71bcd7e576a0407a77baf0aafad
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# It’s a (SNMP) Trap: Gaining Code Execution on LibreNMS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-29_its-a-snmp-trap-gaining-code-execution-on-librenms.md
- Source Type: markdown
- Detected Topics: command-injection, xss, access-control, path-traversal, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `200181c6bfd005d4a21c58495e37cef4f908d95ee03ffe7a00b9e001638e2bed`
- Text SHA256: `121636b5f5fff911f9523b14c5f23c818f75f71bcd7e576a0407a77baf0aafad`


## Content

---
title: "It’s a (SNMP) Trap: Gaining Code Execution on LibreNMS"
page_title: "It’s a (SNMP) Trap: Gaining Code Execution on LibreNMS | Sonar"
url: "https://www.sonarsource.com/blog/it-s-a-snmp-trap-gaining-code-execution-on-librenms/"
final_url: "https://www.sonarsource.com/blog/it-s-a-snmp-trap-gaining-code-execution-on-librenms/"
authors: ["Stefan Schiller (@scryh_)"]
programs: ["LibreNMS"]
bugs: ["RCE", "Stored XSS", "Security code review"]
publication_date: "2023-03-29"
added_date: "2023-03-31"
source: "pentester.land/writeups.json"
original_index: 1326
---

## TL;DR overview

  * LibreNMS, a widely used open-source network monitoring platform, contains a code execution vulnerability that allows attackers to execute arbitrary commands on the server by sending crafted SNMP trap data.
  * The flaw stems from insufficient sanitization of SNMP community string values before they are used in system commands, a classic command injection pattern in network management software.
  * Because LibreNMS typically runs with elevated permissions and access to network devices, a successful exploit can lead to full infrastructure compromise beyond the monitoring server itself.
  * Organizations using LibreNMS should apply the available patch, restrict SNMP trap sources to trusted devices, and consider network segmentation to limit the blast radius of a potential compromise.

LibreNMS is a fully featured monitoring solution developed in PHP. It is usually deployed at a central position in a company’s network with connectivity to all monitored hosts. This makes LibreNMS an interesting target for threat actors.

In our effort to help secure the open-source world, we decided to audit LibreNMS for security vulnerabilities. During this, we identified an XSS vulnerability, which an unauthenticated attacker could exploit to gain remote code execution by sending a single SNMP trap.

In this article, we will outline the impact of the vulnerability and dive into the technical details. Furthermore, we will determine how this vulnerability can be prevented and derive the essential key learnings.

## Impact

LibreNMS versions `22.10.0` and prior are prone to an **unauthenticated, stored XSS** vulnerability when SNMP is enabled. The vulnerability could be exploited to gain **remote code execution** as demonstrated in the following video:

To exploit the vulnerability, the attacker sends a **spoofed SNMP trap** (1), which injects an XSS payload in the eventlog (2). When an admin views the eventlog dashboard via the web interface (3), the triggered JavaScript payload leverages the `Alert Template` feature to create a new **Blade template** (4), which executes arbitrary PHP code e.g., to establish a reverse shell (5):

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/2ecb645a-d642-4a3f-8b50-1367e7e327e5/librenms-graphic.png)

The vulnerability was fixed with LibreNMS version `22.11.0`. We strongly recommend updating any instance with a version prior to this release.

## Technical Details

In this section, we briefly introduce SNMP and its different modes of operation. We determine how LibreNMS handles SNMP traps and outline the XSS vulnerability. Also, we showcase how custom inline templates rendered with Blade lead to code execution.

### SNMP

The Simple Network Management Protocol (SNMP) is used to manage network devices and collect information about their current state. Monitoring solutions usually rely on or at least support SNMP, because it is available on a huge variety of devices. This can eliminate the need to set up a proprietary agent on the monitored device.

In order to collect information from a monitored device, the monitoring solution usually acts as an **SNMP manager** , which can actively request information from an **SNMP agent** running on the monitored device. This way of actively retrieving information is also known as **SNMP polling**. The downside of this approach is that it can only reflect the device’s state at the time of the last poll. For events, which are critical and should be reported immediately, SNMP supports a feature called **SNMP trap**. A trap is initiated by the monitored device in order to deliver unrequested information to the manager. The manager usually runs a separate daemon like `snmptrapd` to receive these traps. The daemon can be configured to pass all received traps to another application for further processing. 

A particular aspect to mention here is that SNMP relies on **UDP**. In contrast to TCP, UDP does not require a handshake to initiate a connection: the data of a received package is directly processed. Because of this, the source IP address of UDP packets can be spoofed by attackers. This also makes SNMP prone to **spoofed traps** if no additional access control settings are enabled.

### LibreNMS SNMP Handlers

LibreNMS supports SNMP traps by using `snmptrapd` as documented [here](https://docs.librenms.org/Extensions/SNMP-Trap-Handler/). The default configuration does not require authentication. The only requirement for an attacker to make LibreNMS process a spoofed SNMP trap is to determine the IP address of any monitored device.

The variety of events that can be reported via an SNMP trap is huge and specific to the individual device. For this purpose, LibreNMS contains plenty of different trap handlers:

Copy to clipboard
  
  
  $ ls LibreNMS/Snmptrap/Handlers|wc -l
  143
  $ ls LibreNMS/Snmptrap/Handlers
  AdvaAccThresholdCrossingAlert.php
  AdvaAttributeChange.php
  AdvaNetThresholdCrossingAlert.php
  AdvaNetworkElementAlmTrap.php  
  AdvaObjectCreation.php  
  AdvaObjectDeletion.php  
  AdvaSnmpDyingGaspTrap.php  
  AdvaStateChangeTrap.php
  ...
  VmwTrapUtil.php
  VmwVmHBDetected.php
  VmwVmHBLost.php
  VmwVmPoweredOff.php
  VmwVmPoweredOn.php
  VmwVmSuspended.php
  WarmBoot.php

A usual trap handler e.g. for a Cisco device reporting a MAC violation looks like this:

**librenms/LibreNMS/Snmptrap/Handlers/CiscoMacViolation.php**

Copy to clipboard
  
  
  <?php
  class CiscoMacViolation implements SnmptrapHandler
  {
  public function handle(Device $device, Trap $trap)
  {
  // retrieve interface name from trap
  $ifName = $trap->getOidData($trap->findOid('IF-MIB::ifName'));
  
  // retrieve MAC address from trap
  $mac = $trap->getOidData($trap->findOid('CISCO-PORT-SECURITY-MIB::cpsIfSecureLastMacAddress'));
  
  // create entry in eventlog
  Log::event("SNMP Trap: Secure MAC Address Violation on port $ifName. Last MAC address: $mac", $device->device_id, 'trap', 4);
  }
  }

The trap handler retrieves some information from the trap (interface name and MAC address) and then creates an entry in the eventlog by calling `Log::event`. The first parameter of this method is the event **message**. The third parameter (populated with the static string `'trap'`) is the event **type**.

### XSS via event type

When the created event is displayed in the eventlog via the `EventlogController` class, the event message is sanitized using `htmlspecialchars` to prevent XSS. The event type is retrieved via the method `formatType`:

**librenms/app/Http/Controllers/Table/EventlogController.php**

Copy to clipboard
  
  
  <?php
  class EventlogController extends TableController
  {
  // ...
  
  public function formatItem($eventlog)
  {
  return [
  // ...
  // message sanitized to prevent XSS:
  'message' => htmlspecialchars($eventlog->message),
  
  // type retrieved via formatType:
  'type' => $this->formatType($eventlog),
  ];
  }
  }

The `formatType` method handles some specific values for the type. If the type does not match any of these values, it is returned as-is:

**librenms/app/Http/Controllers/Table/EventlogController.php**

Copy to clipboard
  
  
  <?php
  private function formatType($eventlog)
  {
  // handle some specific types ...
  if ($eventlog->type == ...) {
  // ...
  }
  
  // ... otherwise return type as-is
  return $eventlog->type;
  }

If an attacker can control the type value, this leads to an XSS vulnerability.

As it turned out, one of the many handlers called `HPFault` does not set the event type to a static value but takes its value from the SNMP trap:

**librenms/LibreNMS/Snmptrap/Handlers/HpFault.php**

Copy to clipboard
  
  
  <?php
  class HpFault implements SnmptrapHandler
  {
  public function handle(Device $device, Trap $trap)
  {
  // type is taken from SNMP trap (can be arbitrary)
  $type = $trap->getOidData($trap->findOid('HP-ICF-FAULT-FINDER-MIB::hpicfFfLogFaultType'));
  switch ($type) {
  // ... same cases for specific types ...
  default:
  // default case: type can almost be arbitrary (excluding static strings from cases above)
  Log::event('Fault - Unhandled ' . $trap->getOidData($trap->findOid('HP-ICF-FAULT-FINDER-MIB::hpicfFfFaultInfoURL')), $device->device_id, $type, 2);
  break;
  }
  }
  }

The type value taken from the SNMP trap can be arbitrarily set by an attacker leading to an XSS vulnerability. An attacker can inject a JavaScript payload in the SNMP trap, which is executed when an admin views the eventlog.

### Blade Templates

The impact of this vulnerability is greatly increased due to a feature called [Alert Templates](https://docs.librenms.org/Alerting/Templates/). This feature allows administrators to create custom templates that will be populated with specific values when an alert occurs.

The template engine used for this feature is Blade. The user-provided custom templates are [rendered inline](https://laravel.com/docs/10.x/blade#rendering-inline-blade-templates) by using the `Blade::render` method:

**librenms/includes/html/forms/alert-templates.inc.php**

Copy to clipboard
  
  
  <?php
  Blade::render($vars['template']);

Attackers with the ability to control the value passed to this method can **directly gain code execution**. This is due to the fact that Blade templates allow [executing arbitrary PHP code](https://laravel.com/docs/10.x/blade#raw-php) via the `@php` directive:

Copy to clipboard
  
  
  @php
  system("id>/tmp/pwned");
  @endphp

## Key learnings and Patch

In this section, we highlight the importance of a secure SNMP configuration, determine the root cause of the XSS vulnerability and outline why it is so important to follow a defense-in-the-depth approach. We also propose a safer approach to run untrusted data in a template engine. At last, we take a look at the patch.

### SNMP

SNMP should always be used with proper authentication. On the one hand, this applies to SNMP managers, which should be required to authenticate themselves before being able to request information from an SNMP agent. On the other hand, this also applies to the monitored devices, which should not be able to submit information via an SNMP trap without prior authentication. For this purpose, `snmptrapd` provides different authentication methods, as documented [here](http://www.net-snmp.org/docs/man/snmptrapd.conf.html).

### XSS

Technically, the root cause of the XSS vulnerability is simply a lack of proper output encoding. Though, this example is more interesting and demonstrates a pattern we haven’t encountered the first time. The vulnerable event type parameter was originally set to static values only within the existing SNMP trap handlers. Thus there didn’t seem to be a need to sanitize this value. More and more handlers were added by different developers. Eventually, one of these handlers violated the original assumption by populating the event type with a user-controllable value, immediately introducing an XSS vulnerability.

This example demonstrates why it is so important to follow a defense-in-the-depth approach. Variables should always be assumed to be tainted when passing to a sensitive sink. In this case, the event type should be encoded before inserting it into the outputted HTML. This greatly reduces the risk of introducing new vulnerabilities when the surrounding code changes and the original assumption of the variable not being user-controllable is not true anymore.

### Template Engine

The impact of the XSS vulnerability is greatly increased due to the `Alert Template` feature. Running untrusted input in a template engine can be very dangerous. The impact depends on the template engine in use. It should be ensured that the engine provides a sandbox. Twig, for example, provides a [sandbox extension](https://twig.symfony.com/doc/3.x/api.html#sandbox-extension), which is specifically designated for the purpose of evaluating untrusted input.

### Patch

The XSS vulnerability [was mitigated](https://github.com/librenms/librenms/commit/00d5e2f4778c334d7bb9ec9e086624906dc6effd) by encoding the value returned by `formatType` using `htmlspecialchars`:

Copy to clipboard
  
  
  <?php
  private function formatType($eventlog)
  {
  // ...
  return htmlspecialchars($eventlog->type);
  }

The `Alert Template` feature was not changed and still uses the Blade template engine. This is very dangerous, as any vulnerability that gives an attacker admin privilege directly leads to remote code execution.

## Timeline

**Date**| **Action**  
---|---  
2022-10-26| We report the issue to the maintainers via huntr.dev.  
2022-11-20| The maintainers confirm the issues.  
2022-11-24| Patched version 22.11.0 is released.  
  
## Summary

In this article, we detailed a critical vulnerability in the monitoring solution LibreNMS, which could be exploited to gain remote code execution by sending a single SNMP trap.

We briefly explained SNMP and how its trap feature is used in LibreNMS. Furthermore, we detailed the discovered XSS vulnerability and deduced its impact, which is greatly increased due to the unsafe usage of the Blade template engine.

In the last section, we summarized the key learnings by highlighting the importance of a secure SNMP configuration and outlined why it is so important to follow a defense-in-the-depth approach. In the end, we suggested safe alternatives to run untrusted data in a template engine and took a brief look at the patch of the XSS vulnerability.

## Related Blog Posts

  * [Checkmk: Remote Code Execution by Chaining Multiple Bugs (1/3)](https://www.sonarsource.com/blog/checkmk-rce-chain-1/)
  * [Cacti: Unauthenticated Remote Code Execution](https://www.sonarsource.com/blog/cacti-unauthenticated-remote-code-execution/)
  * [Zabbix - A Case Study of Unsafe Session Storage](https://www.sonarsource.com/blog/zabbix-case-study-of-unsafe-session-storage/)
  * [Path Traversal Vulnerabilities in Icinga Web](https://www.sonarsource.com/blog/path-traversal-vulnerabilities-in-icinga-web/)
