---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-28_getting-system-on-windows-in-style.md
original_filename: 2023-09-28_getting-system-on-windows-in-style.md
title: Getting SYSTEM on Windows in style
category: documents
detected_topics:
- command-injection
- race-condition
- sso
- access-control
- automation-abuse
- supply-chain
tags:
- imported
- documents
- command-injection
- race-condition
- sso
- access-control
- automation-abuse
- supply-chain
language: en
raw_sha256: 0422924c5e6f4ee5221e9ee6cdedd853864025451906700727425c108b834592
text_sha256: 6c382d3f3fab23e9dea9d5de32e1f389aa85a6cf31baf91110ad9874d55c962c
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# Getting SYSTEM on Windows in style

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-28_getting-system-on-windows-in-style.md
- Source Type: markdown
- Detected Topics: command-injection, race-condition, sso, access-control, automation-abuse, supply-chain
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `0422924c5e6f4ee5221e9ee6cdedd853864025451906700727425c108b834592`
- Text SHA256: `6c382d3f3fab23e9dea9d5de32e1f389aa85a6cf31baf91110ad9874d55c962c`


## Content

---
title: "Getting SYSTEM on Windows in style"
page_title: "Getting SYSTEM on Windows in style | DEFION Research Labs"
url: "https://sector7.computest.nl/post/2023-09-getting-system-on-windows-in-style/"
final_url: "https://defion.security/en/research-labs/getting-system-on-windows-in-style/"
authors: ["Sector 7 (@sector7_nl)"]
programs: ["Microsoft (Windows)"]
bugs: ["RCE", "Local Privilege Escalation", "TOCTOU", "DLL Hijacking"]
publication_date: "2023-09-28"
added_date: "2023-10-03"
source: "pentester.land/writeups.json"
original_index: 739
---

[Home](/en/) › [Research Labs](/en/research-labs/) › Getting SYSTEM on Windows in style

Windows Security 28 September 2023 · 10 min read

# Getting SYSTEM on Windows in style

Microsoft has published a patch for [CVE-2023-38146](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-38146) on patch Tuesday of September 2023. The advisory for this vulnerability mentions that the impact is remote code execution, which was demonstrated by [@carrot_c4k3](https://mastodon.social/@carrot_c4k3) \- the researcher who first reported the vulnerability to Microsoft in May of 2023. Her [ThemeBleed writeup](https://exploits.forsale/themebleed/) and proof-of-concept demonstrate how an attacker might exploit the vulnerability for code execution by luring an unsuspecting victim into opening a booby-trapped `.themepack` file.

We had also identified and reported the same vulnerability in August of 2023. But, our proof-of-concept exploit took a slightly different path with a distinct outcome. It turns out that it is possible to exploit this vulnerability for initial access as well as privilege escalation!

In this writeup, we'll cover the code path that we've identified to the vulnerability as well as how we exploited it for privilege escalation.

## Background

Windows users can modify their desktop environment to better suit their preferred style. This is done through the use of [theme files](https://learn.microsoft.com/en-us/windows/win32/controls/themesfileformat-overview) which are simple INI-style config files with the `.theme` extension. These files consist of key-value entries for text colors, scrollbar colors, desktop icons and the like. Next to simple graphical elements, Windows themes must contain an entry denoting the theme's associated "Visual Styles". This entry can be used to specify color and sizing information for UI elements. Optionally, it can also specify a `Path` entry pointing to an `.msstyles` file. These are Portable Executable (PE) files that should only contain resources which control the styling of "deeper" elements of the operating system's UI, such as windows and buttons. Once a user chooses a theme, if the `[VisualStyles]\Path` entry exists and points to a valid `.msstyles` file, it will be stored in their registry hive at `HKCU\Software\Microsoft\Windows\CurrentVersion\ThemeManager\DllName`. Usually, it is set to the visual styles file for the Windows default theme, `Aero.msstyles`.

Any user may use any theme or modify one to their heart's content, but they may not use any visual styles files that are not provided by Microsoft. That is because `.msstyles` PEs are signed and validated at some point during processing.

While investigating signature verification routines in Windows 11, we noticed an oddity in how theme loading code handled `.msstyles` files. This oddity was our path to the discovery of CVE-2023-38146, which seems to stem from some code changes to Windows theme loading that were introduced in Windows 11.

## User theme loading

Naturally, a user's theme should be applied to their desktop session when they log in or whenever it needs to be re-applied. This process is performed by [Winlogon](https://learn.microsoft.com/en-us/windows/win32/secauthn/winlogon) as part of the user's desktop creation and in response to a number of events that may occur in a user's session.

On a vulnerable build of Windows 11, Winlogon (re-)loads the currently logged-in user's as follows:

  1. Some event that requires (re-)loading the current user's theme occurs (e.g. user logs on), causing `winlogon.exe` to invoke a series of functions eventually calling `UXInit!CThemeServicesInit::LoadCurrentTheme`.
  2. `UXInit!CThemeServicesInit::LoadCurrentTheme` reads the registry key `HKCU\Software\Microsoft\Windows\CurrentVersion\ThemeManager\DllName` for the to be logged in user to obtain the path to the theme's visual style file (the `.msstyles` file).
  3. Eventually, `UXInit!LoadThemeLibrary` is called to load the theme's `.msstyles` file using `LoadLibraryEx` while specifying the `LOAD_LIBRARY_AS_DATAFILE` flag to ensure that no code, if any, is executed. Afterwards, the loaded `.msstyles` module's `PACKTHEM_VERSION` resource section is read. This is expected to contain a version number represented as a 2-byte integer.
  4. If the value is equal to 999 (0x03e7), the function `UXInit!ReviseVersionIfNecessary` checks if the `.msstyles` path followed by `_vrf.dll` exists. For example, if the `.msstyles` file is located at `C:\a.msstyles`, then the function would check for the existence of `C:\a.msstyles_vrf.dll`.
  5. If this path exists, its signature is verified for validity.
  6. If that signature verification passes, the `_vrf.dll` file is loaded into `winlogon.exe` and the function `<loaded_vrf_dll>!VerifyThemeVersion` is called.

It is worth noting that all of the steps above are executed before any validation of the embedded `.msstyle` file signature.

## Vulnerability

In the process above, steps (5) and (6) must be performed as one atomic operation from the point of view of the filesystem with no modifications being allowed to the `_vrf.dll` file in between. Otherwise, it is possible to swap the `_vrf.dll` file after step (5) but before step (6), which would be a Time-of-check to time-of-use (TOCTOU) vulnerability.

And this is exactly the vulnerability as can be seen in the decompilation of `UXInit!ReviseVersionIfNecessary` (irrelevant parts omitted for brevity):
  
  
  // ...snip...
  if ( !PathFileExistsW(vrf_file_path) ) // [1]
  return 0x80004005;
  *&themeSig_object = &CThemeSignature::`vftable`;
  *(&themeSig_object + 1) = 0i64;
  v16[0] = 0ui64;
  CThemeSignature::_Init(&themeSig_object, v7, v8);
  err = CThemeSignature::Verify(&themeSig_object, vrf_file_path); // [2]
  CThemeSignature::~CThemeSignature(&themeSig_object);
  if ( (err & 0x80000000) != 0 )
  {
  // ...snip...
  // Do further checks using NtGetCachedSigningLevel
  // ...snip...
  }
  vrf_library = LoadLibraryW(vrf_file_path); // [3]
  v11 = vrf_library;
  if ( !vrf_library )
  return 0x80004005;
  VerifyThemeVersion = GetProcAddress(vrf_library, "VerifyThemeVersion");
  memset(v16, 0, 20);
  themeSig_object = xmmword_180028E88;
  err = VerifyThemeVersion();
  // ...snip...

The function will first check that the `_vrf.dll` file exists `[1]`, then its signature is verified `[2]`. Next, `LoadLibraryW` will open the file again `[3]`. Because no locking is applied to the file between `[2]` and `[3]`, it may be modified between these steps. By first placing a visual styles file that is properly signed and setting the current theme to use that path, and then replacing it at just the right moment with an arbitrary DLL, it is possible to load that DLL into `winlogon.exe`, executing its code as SYSTEM.

## Exploitation

In order to successfully exploit the TOCTOU vulnerability, one would have to race against the vulnerable code path as it is repeatedly invoked while constantly switching between a properly signed visual styles file and a malicious one.

This means that a method to trigger the vulnerable code path in `winlogon.exe` repeatedly and quickly is necessary to improve the chances of a successful race in a short time window. Alternatively, a way to increase the race window duration or even skip it altogether would be sufficient as long as it is possible to trigger the vulnerable code path at least once.

Regardless of the specifics, the exploit outline would be:

  1. Prepare a `.msstyles` file with a `PACKTHEM_VERSION` of 999 at some path `$x`.
  2. Change the registry key `HKCU\Software\Microsoft\Windows\CurrentVersion\ThemeManager\DllName` to point to `$x`.
  3. Put a validly signed `.msstyles` file at `$x_vrf.dll`.
  4. Trigger the theme loading code path.
  5. Replace the file `$x_vrf.dll` with our malicious version, hopefully between the signature verification check and the `LoadLibraryW` call.
  6. If all goes well, then our payload is now executing inside `winlogon.exe`, which is running as `NT AUTHORITY\SYSTEM`.
  7. Otherwise, repeat steps (3) to (5).

### Winning ^W Avoiding the race

While it may be fun to exploit race conditions, it's even better if there is no need to race at all. Since an attacker has full control of the theme's visual styles DLL path, there is no need to race. All they would have to do is specify a UNC path pointing to a file on a remote SMB share that is under their control. Doing so would allow them to control exactly which version of the `_vrf.dll` is returned for which file read operation.

The only requirement is that the share at the other end is set up to host a properly signed `.msstyles` file and returns a validly signed `_vrf.dll` file on the first read and a malicious `_vrf.dll` file the second time.

### Triggering the vulnerable code path

As previously mentioned, Winlogon is responsible for creating the user's desktop upon user logon. So it stands to reason that logging out then back in again should trigger the vulnerable code path. And indeed, that does cause a theme reload and combined with a visual styles file path pointing to a remote SMB share, we're guaranteed to exploit the vulnerability successfully in one shot. However, it seemed a bit complicated so we set out to find another way.

We ended up finding out that changing the UI's scaling to a value > 100% will trigger a theme reload at least once, but is a bit flaky in our tests. Since racing is no longer needed, that does not matter anyway and a single theme reload is sufficient to exploit the vulnerability. On the upside, changing the UI's scaling can be easily done with some PowerShell:
  
  
  function Set-Scaling {
  # Posted by IanXue-MSFT on
  # https://learn.microsoft.com/en-us/answers/questions/197944/batch-file-or-tool-like-powertoy-to-change-the-res.html
  # $scaling = 0 : 100% (default)
  # $scaling = 1 : 125% 
  # $scaling = 2 : 150% 
  # $scaling = 3 : 175% 
  param($scaling)
  $source = @'
  [DllImport("user32.dll", EntryPoint = "SystemParametersInfo")]
  public static extern bool SystemParametersInfo(
  uint uiAction,
  uint uiParam,
  uint pvParam,
  uint fWinIni);
  '@
  $apicall = Add-Type -MemberDefinition $source -Name WinAPICall -Namespace SystemParamInfo -PassThru
  $apicall::SystemParametersInfo(0x009F, $scaling, $null, 1) | Out-Null
  }
  # .. Set up exploit
  # Trigger the vulnerable code path
  Set-Scaling -scaling 2
  
  # Reset the scaling
  Set-Scaling -scaling 0
  
  # .. Cleanup

### Putting it all together

Modifying the exploit template from earlier, a reliable exploit could look like this:

  1. Prepare a `.msstyles` file with a `PACKTHEM_VERSION` of 999 and store it on an attacker-controlled SMB share at `\\<share host>\path\to\file.msstyles`
  2. Change the registry key `HKCU\Software\Microsoft\Windows\CurrentVersion\ThemeManager\DllName` to point to `\\<share host>\path\to\file.msstyles`.
  3. Put a validly signed `.msstyles` file at `\\<share host>\path\to\file.msstyles_vrf.dll`
  4. Trigger a theme re-load by setting the UI scaling to some value > 100%
  5. Wait until the file at `\\<share host>\path\to\file.msstyles_vrf.dll` is read once
  6. Replace the file `\\<share host>\path\to\file.msstyles_vrf.dll` with a malicious version.
  7. When the file is requested for the second time by `LoadLibraryW`, it's presented instead with the malicious version, thereby achieving code execution inside `winlogon.exe`

For our exploit, we set up a remote host that is running a samba share and a scapy-based Python script to perform the file replacement step. The script detects when the first read operation has been sent over the wire, after which it replaces the validly signed `file.msstyles_vrf.dll` on disk with our malicious DLL.

## Demo

The video below shows the exploit in action. We start with a standard authenticated user, `lowuser`, then run the exploit script. It sets the user's visual styles DLL key described above to `\\192.168.64.1\public\asdf.msstyles`. Afterwards, it changes the UI's scaling to 150%, causing `winlogon.exe` to reload the user's theme. Once the `.msstyles` file is loaded and its `PACKTHEM_VERISON` resource is checked, `winlogon.exe` verifies the signature of `\\192.168.64.1\public\asdf.msstyles_vrf.dll`. This signature verification step passes since the first file presented by the SMB share is correctly signed. Afterwards, `winlogon.exe` loads the DLL one more time at which point our Python script has replaced it with an unsigned malicious DLL. The result can be seen as the malicious DLL spawns an interactive command prompt as `NT AUTHORITY\SYSTEM`.

Your browser does not support the video tag. 

## Fix analysis

Microsoft's patch updated the code for `LoadThemeLibrary` in both `uxtheme.dll` and `UXInit.dll` to remove the `PACKTHEM_VERSION` check and the `ReviseVersionIfNecessary` function entirely. Hence, the initially vulnerable code path no longer loads any DLLs in that path besides the `LOAD_LIBRARY_AS_DATAFILE` loading of the `.msstyles` PE.

On the other hand, the fix did not address how visual styles signatures are validated. The responsible code is still vulnerable to a TOCTOU vulnerability, so it may be possible for attackers to exploit any processing bugs that occur after signature validation.

## Detection

Since the fix removes the "visual style version verification" functionality entirely, it seems safe to assume that Microsoft has deemed it unnecessary. Therefore, any attempt to load a DLL whose path ends in `.msstyles_vrf.dll` is likely a CVE-2023-38146 exploit attempt.

From our research desk to your environment

The offensive expertise behind this research is the same expertise that tests your own systems. Find the vulnerabilities that matter before attackers do. 

[Pentesting Services →](/en/pentesting-services/)

[← Back to Research Labs](/en/research-labs/)
