---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-29_opennms-vulnerabilities-securing-code-against-attackers-unexpected-ways.md
original_filename: 2024-02-29_opennms-vulnerabilities-securing-code-against-attackers-unexpected-ways.md
title: 'OpenNMS Vulnerabilities: Securing Code against Attackers’ Unexpected Ways'
category: documents
detected_topics:
- command-injection
- ssrf
- access-control
- xss
- path-traversal
- automation-abuse
tags:
- imported
- documents
- command-injection
- ssrf
- access-control
- xss
- path-traversal
- automation-abuse
language: en
raw_sha256: 3af1cb525a43d006db7860aab7f2292fcfe17386de82dc1c6a63903aa4b2ee87
text_sha256: a97f223e9ad8426cee446e42b5f24eca7c27b4e14b4cd9840d25266e515721c3
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# OpenNMS Vulnerabilities: Securing Code against Attackers’ Unexpected Ways

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-29_opennms-vulnerabilities-securing-code-against-attackers-unexpected-ways.md
- Source Type: markdown
- Detected Topics: command-injection, ssrf, access-control, xss, path-traversal, automation-abuse
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `3af1cb525a43d006db7860aab7f2292fcfe17386de82dc1c6a63903aa4b2ee87`
- Text SHA256: `a97f223e9ad8426cee446e42b5f24eca7c27b4e14b4cd9840d25266e515721c3`


## Content

---
title: "OpenNMS Vulnerabilities: Securing Code against Attackers’ Unexpected Ways"
page_title: "OpenNMS Vulnerabilities: Securing Code against Attackers’ Unexpected Ways | Sonar"
url: "https://www.sonarsource.com/blog/opennms-vulnerabilities-securing-code-against-attackers-unexpected-ways/"
final_url: "https://www.sonarsource.com/blog/opennms-vulnerabilities-securing-code-against-attackers-unexpected-ways/"
authors: ["Stefan Schiller (@scryh_)"]
programs: ["OpenNMS"]
bugs: ["XSS", "OS command injection", "SNMP", "Security code review"]
publication_date: "2024-02-29"
added_date: "2024-05-08"
source: "pentester.land/writeups.json"
original_index: 399
---

## TL;DR overview

  * Sonar's security research into OpenNMS—a widely used open source network monitoring platform—uncovered multiple vulnerabilities including server-side request forgery and XML external entity injection that allow attackers to pivot from the monitoring system into internal networks.
  * The findings demonstrate how infrastructure management tools can become a lateral movement vector when their code contains unvalidated external resource fetches—even features designed for legitimate admin use.
  * Securing code against unexpected attack paths requires thinking beyond the obvious: OpenNMS's vulnerabilities existed in features where developers typically don't consider attack surfaces.
  * Organizations running OpenNMS should apply available patches and review network monitoring software access controls to limit the blast radius if the monitoring platform is compromised.

Can you spot a vulnerability in the following JSP snippet?

Copy to clipboard
  
  
  <th class="col-2">Reduction&nbsp;Key</th>
  <td class="col-10" colspan="3">
  <% if (alarm.getReductionKey() != null) {%>
  <%=alarm.getReductionKey()%>
  <% } else {%>
  &nbsp;
  <% }%>
  </td>

Found it? If not, it’s easier than you may have expected. The snippet contains part of an HTML table, which outputs the value returned by `alarm.getReductionKey()` in a cell. Since the value is not sanitized, this leads to an XSS vulnerability. More complicated is the question of how an attacker can control this value. Answering this will lead us down a rabbit hole to the basics of the User Datagram Protocol (UDP).

But before we dive in: Where is this vulnerable code snippet from? It is taken from [OpenNMS](https://www.opennms.com/), a popular enterprise-grade monitoring solution. The impact of this vulnerability tracked as [CVE-2023-0846](https://nvd.nist.gov/vuln/detail/CVE-2023-0846) is vast. An **unauthenticated attacker** can leverage it to inject a JavaScript payload in the admin dashboard, which exploits another vulnerability in the application to **execute arbitrary code** on the OpenNMS server once an admin views the dashboard:

The vulnerabilities were **fixed** in **OpenNMS 31.0.4**.

But how could this even happen? Were the maintainers just not aware of straightforward XSS vulnerabilities like this?

There is even a specific function called `WebSecurityUtils.sanitizeString`, which is used to sanitize reflected values. This function is applied to all other values like `alarm.getDescription()`:

Copy to clipboard
  
  
  <div class="card-header">
  <span>Description</span>
  </div>
  <div class="card-body">
  <%={% mark red %}WebSecurityUtils.sanitizeString(alarm.getDescription(), true){% mark %}%>
  </div>

So, obviously, the maintainers are very well aware of the dangers of XSS. But did `alarm.getReductionKey()` just slip through and was simply forgotten to be sanitized? Probably not. Instead, the value returned by this method was not assumed to be attacker-controllable. It seems pretty unnecessary to sanitize a value, which is safe anyway, doesn’t it?

This blog post illustrates why an assumption like this can be very dangerous. We will deep-dive into the technical details and explain how attackers can spoof SNMP traps originating from localhost by leveraging IPv4-mapped IPv6 addresses in order to control values, which are considered to be uncontrollable. Furthermore, we provide valuable insights from this case study, independent of whether you want to prevent or discover issues like this.

We presented the findings described in this blog post as part of our talk [Monitoring Solutions: Attacking IT Infrastructure at its Core](https://www.youtube.com/watch?v=hGne0DbR6bY) at [TROOPERS23](https://www.sonarsource.com/blog/troopers-2023-conference-takeaways/). 

## Technical Details

In this section, we explain how the uncontrollable value becomes controllable and how attackers may leverage the resulting XSS vulnerability with a second vulnerability, an authenticated command injection.

### Unauthenticated XSS (CVE-2023-0846)

OpenNMS is a monitoring solution that collects data from monitored devices. A standard protocol used for this purpose is SNMP. Usually, the SNMP manager, the OpenNMS server in this case, actively retrieves relevant information from the monitored devices (**SNMP polling**). However, SNMP also supports a feature called **SNMP trap** , which allows monitored devices to immediately deliver unrequested information to the SNMP manager. OpenNMS supports this feature via a dedicated SNMP listener. Received traps are converted to an event if the trap is considered meaningful (e.g., the host sending the trap is a monitored device):

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/0ff8c54c-142b-4e7c-bfbd-e4175f913b4a/opennms_trap_event.png)

The conversion from a raw SNMP trap to an **Event** is done based on an XML file, which defines which values from the trap are mapped to attributes of the event:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/ad209552-c1bf-4b81-8a06-5007f6415e48/opennms_xml.png)

In the example shown above, the XML element `<descr>` contains a template string, which is used to populate the `description` attribute of an Event. This template string can contain placeholder values like `%parm[#1]%`, which are replaced with the corresponding values from the SNMP trap. Since this might be an arbitrary value, the resulting description is sanitized before being output on the dashboard:

Copy to clipboard
  
  
  <div class="card-header">
  <span>Description</span>
  </div>
  <div class="card-body">
  <%=WebSecurityUtils.sanitizeString(event.getDescription(), true)%>
  </div>

Other than these common Events, important traps are converted into an **Alarm** instead of an Event:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/9e9e6c92-b665-4973-bbed-ee71a6f19ecb/opennms_trap_alarm.png)

For Alarms, there are additional attributes. One of these is called the **Reduction Key**. Since Alarms are very noisy, the Reduction Key is used to summarize multiple similar Alarms as one single Alarm. An XML file used to populate the Reduction Key may look like this:

Copy to clipboard
  
  
  <alarm-data reduction-key="%uei%:%dpname%:%nodeid%:%interface%" alarm-type="1" auto-clean="false"/>

All placeholder values are internal variables that are not controllable by a remote attacker.

However, there are also SNMP traps for which the Reduction Key contains placeholder values taken from the SNMP trap:

Copy to clipboard
  
  
  <alarm-data reduction-key="uei.opennms.org/nodes/snmp/interfaceOperDown:%dpname%:%nodeid%:{% mark red %}%parm[#1]%{% mark %}" alarm-type="1" auto-clean="false">
  </alarm-data>

We have already seen that this was obviously not expected since the Reduction Key is not sanitized when being output on the admin dashboard:

Copy to clipboard
  
  
  <th class="col-2">Reduction&nbsp;Key</th>
  <td class="col-10" colspan="3">
  <% if (alarm.getReductionKey() != null) {%>
  <%={% mark red %}alarm.getReductionKey(){% mark %}%>
  <% } else {%>
  &nbsp;
  <% }%>
  </td>

An attacker would still need access to a monitored device in order to control this value since traps from non-monitored devices are discarded. Or is there a way around this?

### Spoofing SNMP Traps

SNMP relies on the connectionless protocol UDP. Although UDP is superior to the connection-oriented protocol TCP in terms of speed, it is susceptible to spoofing attacks. An attacker can send a fake SNMP trap to OpenNMS with an arbitrary source IP address. 

For the trap to be accepted by OpenNMS, the attacker still needs to know the IP address of a monitored device. However, there is a default entry for localhost, which represents the OpenNMS server itself. Thus, if an attacker would be able to spoof an SNMP trap from localhost, this would be accepted regardless of the configured monitored devices.

When sending a spoofed SNMP trap from the IPv4 address `127.0.0.1`, though, this trap doesn’t even reach the application:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/feadc3f5-bc51-444d-9f1f-0660aadd730b/opennms_ipv4.png)

The operating system kernel, which is usually Linux for OpenNMS, drops packets on an external interface originating from localhost. This makes sense since you should not receive a packet originating from localhost on an external interface.

If the SNMP trap is instead encapsulated into an IPv6 packet with the source IP address set to the IPv4-mapped IPv6 address `::ffff:127.0.0.1`, the operating system accepts the packet and forwards it to the application:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/671c171b-c1cf-456e-8f3b-bfb1d386f583/opennms_ipv6.png)

OpenNMS now converts this IP address to localhost and considers this to be a valid SNMP trap from the server itself. A similar approach was documented by Google Project Zero back in 2015 when [exploiting a buffer overflow in ntpd](https://googleprojectzero.blogspot.com/2015/01/finding-and-exploiting-ntpd.html).

For OpenNMS, this means that an utterly unauthenticated attacker can raise an Alarm and inject an XSS payload into the admin dashboard. Since the payload is part of an urgent Alarm, an admin will very likely view it and trigger the payload.

The payload executed in the context of the admin account gives an attacker access to considerably more attack surfaces. Functionalities of the application, which are only reachable for an authenticated admin, are now open to attacks from a remote threat actor.

### Authenticated Command Injection

OpenNMS uses **Detectors** to discover running services on a monitored device. An admin adding a Detector can select its implementation class. The default Detectors do not contain any particular interesting class, but amongst the other implementations in the classpath, there is a class called `GpDetector`. This class contains a parameter called `script`, which can be set when adding the Detector:

Copy to clipboard
  
  
  public class GpDetector extends BasicDetector<GpRequest, GpResponse>{
  // ...
  private String m_script;
  // ...
  public void setScript(final String script) {
  m_script = script;
  }
  // ...

Once the Detector is added, it can be used to start a discovery, which triggers the `connect` method. Within this method, the script parameter is further passed to `execRunner.exec`:

Copy to clipboard
  
  
  public void connect(final InetAddress address, final int port, final int timeout) throws IOException, Exception {
  // ...
  final String script = "" + getScript() + " " + getHoption() + " " + hostAddress + " " + getToption() + " " + convertToSeconds(timeout);
  if (getArgs() == null) setExitStatus({% mark red %}execRunner.exec(script){% mark %});

Basically, the `execRunner.exec` method splits the provided string by spaces and passes the resulting array to `Runtime.exec`. Since there are no restrictions on the first element of the array, an attacker can simply provide `/bin/bash` followed by the `-c` option and an arbitrary string, which is executed as a bash command.

This straightforward command injection vulnerability dramatically increases the impact of the XSS vulnerability, as an attacker can combine both of these to take over an OpenNMS server:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/7e71540c-19cd-4c2f-8bf8-d72df385f7c6/opennms_exploit.png)

  1. The attacker sends a spoofed SNMP trap via IPv6. The source address is set to the IPv4-mapped IPv6 address of localhost (`::ffff:127.0.0.1`).
  2. The trap listener receives and accepts this trap as a valid trap from the default host localhost. Due to the severity of the trap, it is converted to an Alarm. When the corresponding XML file is used to create a Reduction Key, the XSS payload, which the attacker placed in the SNMP trap, is injected.
  3. The raised Alarm draws the attention of an admin, who views it on the dashboard.
  4. At this point, the injected JavaScript payload is triggered. The payload adds a custom Detector and initiates a new discovery with this Detector.
  5. This triggers the command inserted into the script attribute, which, for example, establishes a reverse shell to the attacker’s machine.

### Patch

The patch for the XSS vulnerability is straightforward. Similar to other dynamic values, the value returned by `alarm.getReductionKey()` is now also sanitized via the `WebSecurityUtils.sanitizeString` method ([commit](https://github.com/OpenNMS/opennms/commit/e85ef9995658e5768c1b9817cbfd966f7bcf25e6)):

Copy to clipboard
  
  
  <% if (alarm.getReductionKey() != null) {%>
  -  <%=alarm.getReductionKey()%>
  +  <%=WebSecurityUtils.sanitizeString(alarm.getReductionKey())%>
  <% } else {%>

The command injection vulnerability was fixed by limiting script file locations to be located below the OpenNMS home directory ([commit](https://github.com/OpenNMS/opennms/pull/5676/commits/b4698fd84910e0b778495b4e53733f18506ea1fb)):

Copy to clipboard
  
  
  public void connect(final InetAddress address, final int port, final int timeout) throws IOException, Exception {
  // ...
  +  if (!ScriptUtil.isDescendantOf(System.getProperty("opennms.home"), getScript())) {
  +  throw new IOException("The location of the script must not be outside $OPENNMS_HOME.");
  +  }
  // ...

## Key Learnings

The probably oldest suggestion to secure software is: “Don’t trust user input!”. It seems so obvious that it’s almost annoying to hear this over and over again. But it is still a thing today, even for popular applications. How can this be possible? Are vendors so ignorant that this message hasn’t reached them? Or don’t they just care? Although there are cases like this, even for caring vendors, there is one key challenge here: What data is attacker-controllable?

When directly accessing a URL query parameter, it is self-evident. When retrieving the reduction key of a specific alarm, which happens to contain dynamic data extracted from an SNMP trap, which an attacker can spoof, it might not be so obvious.

That’s why all variables should be sanitized, escaped, or encoded before being used. Even if a variable is currently not attacker-controllable, a change in the code in some totally different component can falsify this assumption and immediately introduce a vulnerability. Funnily, we have seen a very similar case to this with [LibreNMS](https://www.sonarsource.com/blog/it-s-a-snmp-trap-gaining-code-execution-on-librenms/).

So, let’s change our perspective to the offensive side: How can issues like this be discovered? When you try to break into a house, you can waste hours and hours banging your head at the main door, not noticing that it is much easier to enter the house through a small window on the side, which was left open. Or, you can enter through the chimney. Or, you can dress up as the cleaner, who is let into the house every day. But this is about software and not burglary. And software is much more complex, which opens it to a wide variety of creative attacks. Spending time determining different ways to make the application process your input is absolutely worth it and can unveil critical vulnerabilities.

## Timeline

**Date**| **Action**  
---|---  
2022-10-10| We report all issues to the vendor  
2022-10-11| Vendor confirms receipt of our report  
2022-12-14| Vendor releases version Horizon 31.0.2 (Stroopwafel)  
This version fixes the XSS vulnerability  
2023-02-08| Vendor releases version Horizon 31.0.4 (Otap)  
This version fixes the command injection vulnerability  
2023-02-22| CVE-2023-0846 assigned to XSS vulnerability  
  
## Summary

This blog post covered an XSS vulnerability in the monitoring solution OpenNMS. Although a vulnerability like this can be easily prevented, the false assumption of specific data not being controllable by an attacker may tempt developers to omit sanitization. We deep-dived into the ways an attacker may choose in order to take advantage of this. Further, we outlined how this had a critical impact on OpenNMS once combined with another command injection vulnerability.

The key takeaway from this is: Always sanitize! Code is not static. It evolves over time, and old assumptions may become invalid. That’s why we at Sonar follow a Clean as You Code approach. This ensures that you don’t only achieve Code Quality once but also maintain it throughout the constant evolvement of your application. You can learn more about Code Quality [here](https://www.sonarsource.com/blog/what-is-clean-code/).

At last, we would like to thank the OpenNMS Group for the excellent communication and the patch they provided.

## Related Blog Posts

  * [It’s a (SNMP) Trap: Gaining Code Execution on LibreNMS](https://www.sonarsource.com/blog/it-s-a-snmp-trap-gaining-code-execution-on-librenms/)
  * [Checkmk: Remote Code Execution by Chaining Multiple Bugs (1/3)](https://www.sonarsource.com/blog/checkmk-rce-chain-1/)
  * [Cacti: Unauthenticated Remote Code Execution](https://www.sonarsource.com/blog/cacti-unauthenticated-remote-code-execution/)
  * [Zabbix - A Case Study of Unsafe Session Storage](https://www.sonarsource.com/blog/zabbix-case-study-of-unsafe-session-storage/)
  * [Path Traversal Vulnerabilities in Icinga Web](https://www.sonarsource.com/blog/path-traversal-vulnerabilities-in-icinga-web/)
