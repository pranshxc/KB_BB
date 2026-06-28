---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-01_introducing-aladdin.md
original_filename: 2023-03-01_introducing-aladdin.md
title: Introducing Aladdin
category: documents
detected_topics:
- supply-chain
- command-injection
- path-traversal
tags:
- imported
- documents
- supply-chain
- command-injection
- path-traversal
language: en
raw_sha256: 0b1cc1447bfaed0047c93382514c7fc917152986306b64a3286bd1c1ae8c8da2
text_sha256: e98232c168b19914f071bb54888d813b0eb2e3b6b68ad1ce58689b6aa3b0df15
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Introducing Aladdin

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-01_introducing-aladdin.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `0b1cc1447bfaed0047c93382514c7fc917152986306b64a3286bd1c1ae8c8da2`
- Text SHA256: `e98232c168b19914f071bb54888d813b0eb2e3b6b68ad1ce58689b6aa3b0df15`


## Content

---
title: "Introducing Aladdin"
url: "https://labs.nettitude.com/blog/introducing-aladdin/"
final_url: "https://www.lrqa.com/en/cyber-labs/introducing-aladdin/"
authors: ["Lefteris Panos (@lefterispan)"]
programs: ["Microsoft (Windows)"]
bugs: ["Insecure deserialization"]
publication_date: "2023-03-01"
added_date: "2023-03-06"
source: "pentester.land/writeups.json"
original_index: 1447
---

Introducing Aladdin, a new tool and technique for red teamers to bypass misconfigured Windows Defender Application Control (WDAC) and AppLocker. Aladdin exploits a deserialisation issue over .NET remoting in order to execute code inside `addinprocess.exe`, bypassing a 2019 patch released by Microsoft in .NET Framework version 4.8.

## Download Aladdin

![github](https://i0.wp.com/labs.nettitude.com/wp-content/uploads/2016/06/github-e1466539795501.png?resize=35%2C35&ssl=1) **GitHub: **[**https://github.com/nettitude/Aladdin**](https://github.com/nettitude/Aladdin)

## A travel to the magic land of .NET deserialization

Once upon a time, in the mysterious land of cybersecurity, there was a red teamer named Aladdin. Aladdin was frustrated, since most of the payloads that he was using at the time were not able to run on a system with application control lists enabled, and those powerful EDR creatures that the evil Blue Lord had created were killing all his beacons.

One day, while out on a mission, Aladdin stumbled upon a strange magic lantern. As he picked it up, a genie appeared before him and granted him three wishes. Without hesitation, Aladdin thought of his first wish.

> _“I wish I could find a payload that would be able to execute on a WDAC enabled Windows 10 system”._

The genie granted his wish and disappeared, leaving Aladdin with the magic lantern at hand. Excited to test out his new power, Aladdin set to research existing techniques for bypassing [WDAC](https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/wdac-and-applocker-overview) / [AppLocker](https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker/applocker-overview). While consulting the majestic oracle named Google, he came across an article from the magician James Forshaw named “[DG on Windows 10 S: Executing Arbitrary Code](https://www.tiraniddo.dev/2017/07/dg-on-windows-10-s-executing-arbitrary.html)”. The article was written in 2017 and went into great detail about the Microsoft .NET process `addinprocess.exe`, residing in every Windows workstation (with Microsoft .NET installed). **Add-ins** are effectively a form of plugin [model](https://learn.microsoft.com/en-us/previous-versions/visualstudio/visual-studio-2008/bb384241\(v=vs.90\)?redirectedfrom=MSDN) that the .NET Framework provides, enabling developers to create plugins for their applications. The model achieves this by constructing a communication pipeline between the host and the add-in.

As discovered by the magician, the process once launched would use the method [ChannelServices.RegisterChannel](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.remoting.channels.channelservices.registerchannel) to register a .NET remoting channel, a topic he was quite familiar with [exploiting](https://www.tiraniddo.dev/2014/11/stupid-is-as-stupid-does-when-it-comes.html). The topic was also covered by [other](https://codewhitesec.blogspot.com/2022/01/dotnet-remoting-revisited.html) magicians more recently. Besides creating a .NET remoting channel, the magician identified that the process would use the [BinaryFormatter](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.serialization.formatters.binary.binaryformatter?view=net-7.0) Class to deserialize input in binary format, while setting the [TypeFilterLevel](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.serialization.formatters.typefilterlevel?view=net-7.0) to Full.

Microsoft clearly state that BinaryFormatter cannot be made secure.

![](/globalassets/cyber-labs/introducing-aladdin/word-image-15703-1.jpeg?epslanguage=en)

According to [Microsoft](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.serialization.formatters.typefilterlevel?view=net-7.0), “.NET Framework remoting provides two levels of automatic deserialization, Low and Full. The Full deserialization level supports automatic deserialization of **all **types that remoting supports in all situations”. When decompiled, `addinprocess.exe` uses `TypeFilterLevel.Full`.

![](/globalassets/cyber-labs/introducing-aladdin/word-image-15703-2.jpeg?epslanguage=en)

This effectively meant that any data passed to the .NET Remoting channel would be deserialized, without worrying about any security controls that the `Low` deserialization level for .NET Framework remoting would enforce.

Aladdin, following the magician’s steps, identified that in order to launch the `addinprocess.exe`, the argument of **/guid** :[GUID] and the argument of **/pid** :[existing PID] should be provided.

The **/guid** argument was user controlled and was being used as the IPC channel name. The /**pid** argument referred to the process identifier of an already running process, that `addinprocess.exe` would wait until exit.

![](/globalassets/cyber-labs/introducing-aladdin/word-image-15703-3.jpeg?epslanguage=en)

After reading through the article multiple times, Aladdin set out to create a new WDAC enabled Windows 10 system in order to test the original [proof of concept](https://github.com/tyranid/DeviceGuardBypasses). Useful resources for creating such a policy were that of [WDACTools](https://github.com/mattifestation/WDACTools) from Matt Graeber and [Building a windows defender application control lab](https://fortynorthsecurity.com/blog/building-a-windows-defender-application-control-lab/) from FortyNorth.

The POC effectively was creating a correctly formatted set of bytes, based on the [.NET remoting protocol](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-nrls/b6ae24ca-e43a-41d9-a758-0809a1b5d946), followed by the serialized provided assembly and the IPC endpoint

![](/globalassets/cyber-labs/introducing-aladdin/word-image-15703-4.jpeg?epslanguage=en)

The output of the POC was a binary array being placed in a template JScript SCT [payload](https://github.com/tyranid/DeviceGuardBypasses/blob/master/CreateAddInIpcData/Resources/Template.txt).

![](/globalassets/cyber-labs/introducing-aladdin/word-image-15703-5.jpeg?epslanguage=en)

Aladdin went ahead and tried out the generated SCT payload, but to no avail.

![](/globalassets/cyber-labs/introducing-aladdin/word-image-15703-6.png?epslanguage=en)

Unfulfilled, he sought further consultation from the great oracle Google, which revealed that the giant Microsoft had already put out some magic [defences](https://github.com/microsoft/dotnet-framework-early-access/blob/master/release-notes/NET48/dotnet-48-changes.md) that stopped this powerful attack.

![](/globalassets/cyber-labs/introducing-aladdin/word-image-15703-7.png?epslanguage=en)

As he began poking and prodding at the patch, the magic lantern glowed brightly, reminding him that he had two additional wishes.

![](/globalassets/cyber-labs/introducing-aladdin/word-image-15703-8.png?epslanguage=en)

Aladdin decided to use his second wish.

> _“I wish I could find a bypass for the patch applied by the great giant”_

The genie again granted his wish and disappeared, leaving Aladdin with the magic lantern at hand and a blog post from the mage Nick Landers – [Re-Animating ActivitySurrogateSelector](https://silentbreaksecurity.com/blog/technical/adversary-simulation/re-animating-activitysurrogateselector/).

Reading the article initially, Aladdin was feeling that he was reading some arcane powerful knowledge that he could not understand, but with every additional read, it became increasingly evident that the patch, besides adding a type check in the [GetObjectData](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.serialization.iserializable.getobjectdata?view=net-7.0) function looking for object types of `ActivityBind` or `DependencyObject`, also introduced a new function named [DisableActivitySurrogateSelectorTypeCheck](https://github.com/microsoft/referencesource/blob/dae14279dd0672adead5de00ac8f117dcf74c184/System.Workflow.ComponentModel/AuthoringOM/Serializer/ActivitySurrogateSelector.cs#L123).

![](/globalassets/cyber-labs/introducing-aladdin/word-image-15703-9.jpeg?epslanguage=en)

The function was effectively responsible for checking a flag via [ConfigurationManager.AppSettings](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.configurationmanager.appsettings?view=dotnet-plat-ext-7.0), which in turn was a property that allowed the programmatic reading / writing of the `AppSettingsSection` of an application.

One of the great things that the mage Nick Landers discovered was the following C# code that disabled the type check:

ConfigurationManager.AppSettings.Set(

"microsoft:WorkflowComponentModel:DisableActivitySurrogateSelectorTypeCheck",

"true");

And a new [commit](https://github.com/pwntester/ysoserial.net/pull/41) was made to the powerful project YSoSerial.Net.

Aladdin immediately started thinking on how to incorporate this bypass into the original POC, and after a few moments / hours / days (time is relative) of tinkering, managed to:

  1. Create a gadget that disables the `ActivitySurrogateSelector` using the ysoserial.net project (`payload1.bin`).
  2. Modify the original POC of James Forshaw by first setting `DisableActivitySurrogateSelectorTypeCheck` to true.
  3. Generate a simple payload that would pop a message box using the POC of James Forshaw (`payload2.bin`).
  4. Spawn Addinprocess in his test VM with the correct arguments. Once spawned, the `addinprocess.exe` created a new named pipe under `\\.\pipe\32a91b0f-30cd-4c75-be79-ccbd6345de11`, where .NET remoting was listening.
  5. Send the first binary payload to the newly created pipe from cmd, to disable `ActivitySurrogateSelector` (`type payload1.bin > \\.\pipe\32a91b0f-30cd-4c75-be79-ccbd6345de11`)
  6. Send the second binary payload to the named pipe, to trigger the deserialization code execution (`type payload2.bin > \\.\pipe\32a91b0f-30cd-4c75-be79-ccbd6345de11`).
  7. Stare at his screen.

![](/globalassets/cyber-labs/introducing-aladdin/word-image-15703-11.jpeg?epslanguage=en)

The genie had granted his wish, and he was able to execute an arbitrary C# assembly via deserialization inside the Microsoft signed process `addinprocess.exe`.

The original POC also provided an SCT template that executes the attack via JScript, using `Scripting.FileSystemObject`. This object is useful since it allows writing to a named pipe although the scriptlet hosting environment is severely limited to which COM objects can be created, in a WDAC enabled system.

Without losing any time, Aladdin proceeded to create a [tool](https://github.com/nettitude/Aladdin) that given a C# assembly DLL, would generate a `BinaryFormatter` serialized payload incorporating the bypass and the .NET Remoting bytes needed to communicate over the named pipe. Using the provided SCT template as a base, Aladdin also created templates for HTA / VBS / CHM / VBA allowing the execution of the payload from these old trusty vectors.

![Text Description automatically generated](/globalassets/cyber-labs/introducing-aladdin/text-description-automatically-generated.png?epslanguage=en)

Happy that everything was working, and his payloads were not being caught, Aladdin became immediately worried that this technique could be abused for evil purposes and as such he went ahead and researched what could be done in order to prevent it.

The big giant Microsoft goes into great lengths detailing the risks of `BinaryFormatter` [deserialization vulnerabilities](https://learn.microsoft.com/en-us/dotnet/standard/serialization/binaryformatter-security-guide) and includes advice on blocking the `addinprocess.exe` executable via their recommended [block rules](https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules). These rules could also be applied via a supplemental WDAC policy or via a third-party application control software.

If prevention controls cannot be applied, then process creation visibility could help detecting the execution of process (which in most environments should not be that common).

![Graphical user interface, text, application, email Description automatically generated](/globalassets/cyber-labs/introducing-aladdin/graphical-user-interface-text-application-email.png?epslanguage=en)

While finalizing the code, Aladdin saw the magic lantern glowing again, reminding him that he had a third and final wish. Without much hesitation Aladdin decided to use his last wish:

> _“I wish I could write an article about this tool”_

## Download Aladdin

![github](https://i0.wp.com/labs.nettitude.com/wp-content/uploads/2016/06/github-e1466539795501.png?resize=35%2C35&ssl=1) **GitHub: **[**https://github.com/nettitude/Aladdin**](https://github.com/nettitude/Aladdin)

# ![](/globalassets/cyber-labs/github-logo-small.png)

### **GitHub Projects**

Check out our latest projects at [GitHub](https://github.com/nettitude)
