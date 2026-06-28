---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-11_attacking-titan-m-with-only-one-byte.md
original_filename: 2022-08-11_attacking-titan-m-with-only-one-byte.md
title: Attacking Titan M with Only One Byte
category: documents
detected_topics:
- access-control
- mobile-security
- sso
- command-injection
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- access-control
- mobile-security
- sso
- command-injection
- automation-abuse
- information-disclosure
language: en
raw_sha256: c4c5015d485079c1a38dd7be6736c54f0593c1010b9c0ce324664cd386dd7b87
text_sha256: 14ff278800566ec834600d9e62cc1250cbf23a0f567614a36d15a5a56c13736a
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Attacking Titan M with Only One Byte

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-11_attacking-titan-m-with-only-one-byte.md
- Source Type: markdown
- Detected Topics: access-control, mobile-security, sso, command-injection, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `c4c5015d485079c1a38dd7be6736c54f0593c1010b9c0ce324664cd386dd7b87`
- Text SHA256: `14ff278800566ec834600d9e62cc1250cbf23a0f567614a36d15a5a56c13736a`


## Content

---
title: "Attacking Titan M with Only One Byte"
page_title: "Attacking Titan M with Only One Byte - Quarkslab's blog"
url: "https://blog.quarkslab.com/attacking-titan-m-with-only-one-byte.html"
final_url: "https://blog.quarkslab.com/attacking-titan-m-with-only-one-byte.html"
authors: ["Damiano Melotti (@DamianoMelotti)", "Maxime Rossi Bellom (@max_r_b)"]
programs: ["Google"]
bugs: ["Memory corruption", "Local Privilege Escalation"]
bounty: "75,000"
publication_date: "2022-08-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2333
---

#  [ Attacking Titan M with Only One Byte ](./attacking-titan-m-with-only-one-byte.html "Permalink to Attacking Titan M with Only One Byte")

Posted Thu 11 August 2022  
Authors [Damiano Melotti](./author/damiano-melotti.html), [Maxime Rossi Bellom](./author/maxime-rossi-bellom.html)  
Category [ Android ](./category/android.html)  
Tags [reverse-engineering](./tag/reverse-engineering.html), [fuzzing](./tag/fuzzing.html), [vulnerability](./tag/vulnerability.html), [exploitation](./tag/exploitation.html), [Android](./tag/android.html), [2022](./tag/2022.html)

* * *

Following our presentation at Black Hat USA, in this blog post we provide some details on CVE-2022-20233, the latest vulnerability we found on Titan M, and how we exploited it to obtain code execution on the chip.

* * *

## Introduction

During the last year and a half, we (Damiano Melotti, Maxime Rossi Bellom & Philippe Teuwen) studied the Titan M, a security chip introduced by Google in their Pixel smartphones, starting from the Pixel 3. Among other events, we presented our results at [Black Hat EU 2021](https://www.youtube.com/watch?v=UNPblJup5ko), together with a [whitepaper](https://github.com/quarkslab/titanm/blob/master/BHEU_2021/EU-21-Rossi_Bellom-2021_A_Titan_M_Odyssey-wp.pdf) that contains all the background knowledge we acquired in the first part of this research. In this blog post, we dive into [CVE-2022-20233](https://nvd.nist.gov/vuln/detail/CVE-2022-20233), the latest vulnerability we found on the chip's firmware. First, we show how we found this vulnerability, using emulation-based fuzzing with AFL++ in Unicorn mode. Then, we go over the exploitation and its inherent challenges, that eventually led us to obtain code execution on the chip.

## Background

The Titan M was introduced by Google in their Pixel devices in 2018. The main goal was to reduce the attack surface available to attackers, mitigating hardware tampering and side-channel attacks. Indeed, the chip lies on a separate system-on-a-chip (SoC) in the device, runs its own firmware, and communicates with the Application Processor (AP) through the SPI bus. It implements several APIs that guarantee a higher level of protection for the most security sensitive features of the smartphone, such as secure boot or a hardware-backed Keystore with _StrongBox_.

In the first steps of this research, we focused on reverse engineering the Titan M firmware, which is based on [Embedded Controller (EC)](https://chromium.googlesource.com/chromiumos/platform/ec/), a lightweight open source OS for micro-controllers. This OS is fairly simple, and is built around the concept of _tasks_ , with a fixed stack size and no heap (so no complex dynamic allocation). This is an important point that will turn out to be useful later: the Titan M chip has essentially a static memory layout, therefore we can assume some objects to always be located at the same address.

The simplicity of the OS also helps when it comes to security, especially by completely eliminating some temporal memory safety bugs associated with dynamic allocation. In addition, thanks to it's Memory Protection Unit (MPU), the chip's memory is configured such that no Write and eXecute permissions are granted to a region at the same time. Secure boot is implemented thanks to some signature checks performed before loading the firmware. Despite these properties, no common exploit mitigation techniques can be found on the chip, except for a hardcoded stack canary that is placed at the end of the tasks' stacks to detect errors. This leaves Titan M fairly exposed to memory corruption vulnerabilities, therefore we decided to explore how to fuzz it and look for some of them.

## Fuzzing Titan M

As broadly known, fuzzing is an extremely effective way to find memory corruption bugs in code bases written in unsafe languages, such as C. However, fuzzing a security chip without access to the sources, and with plenty of hardware-dependent code, can be quite a challenge. We decided to explore two different techniques, namely black-box and emulation-based fuzzing.

### Black-box fuzzing

We have already shown how to perform black-box fuzzing in our previous presentations, but briefly going over it again is useful to understand the differences with the other approach we explored. In general, black-box fuzzing of targets like Titan M can be quite simple: all we need is a channel to interact with what we want to test, and a way to tell if it crashes or reaches unexpected states. In our case, in the previous steps of this research, we had developed [nosclient](https://github.com/quarkslab/titanm/tree/master/nugget_toolkit/), a custom client that runs natively on Android and communicates directly with the kernel driver responsible for the communication with the chip. The possibility to send arbitrary messages gave us both the channel to communicate with Titan M, and the signal to infer what happened while processing them, represented by the return code from the library functions we use.

Most of the tasks communicating with Android use [Protobuf](https://github.com/protocolbuffers/protobuf) to serialize messages. Therefore, we could leverage this grammar, accessible thanks to the open source definitions in the [AOSP](https://android.googlesource.com/platform/external/nos/host/generic/+/refs/tags/android-platform-12.1.0_r1/nugget/proto/nugget/app/), to mutate these messages with [libprotobuf-mutator](https://github.com/google/libprotobuf-mutator). For Nugget, one of the tasks that is not using Protobuf, we used the evergreen [Radamsa](https://gitlab.com/akihe/radamsa/) to generate our test cases.

This approach did bring some interesting results, which when it comes to fuzzing, can be measured in bugs. We could find again several bugs we already knew about, while fuzzing an older version of the firmware, including the buffer overflow we had exploited during last year's research. Moreover, we discovered two new crashes in the latest version of the firmware at the time, although both were caused by the same null pointer dereference, that was not considered serious enough to be a vulnerability and end up in an Android Security Bulletin.

Despite its relatively straightforward setup, and the advantage of testing in the real world, black-box fuzzing comes with a number of shortcomings. First of all, detection is extremely difficult, since we can only spot the bugs that cause crashes or faulty return codes. But most importantly, a well-known limitation is that black-box fuzzing tends to only exercise the targets' shallow states, given the lack of visibility over their internals. As a consequence, we might have been only scratching the surface of the Titan M firmware, which could also explain why all the detected crashes happened after just a few minutes of fuzzing.

### Emulation-based fuzzing

An alternative approach that we focused on is emulation-based fuzzing. In short, given that the firmware is publicly available, why not try to _emulate_ its execution on our laptop? Leveraging our background knowledge on how it works, coming from hours of reverse engineering, we can set up an emulation framework to run the firmware instruction by instruction, and analyze its behavior. This is also a very good feedback for a coverage-guided fuzzer, which can prioritize inputs leading to new instructions being reached and adjust its mutator accordingly.

There exist a number of different ways to implement a solution like this. We tried a few, but we ended up using the [Unicorn](https://www.unicorn-engine.org/) emulator engine, and [AFL++](https://github.com/AFLplusplus/AFLplusplus/) as fuzzing framework. Unicorn is a QEMU-based project that only supports CPU emulation, without full-system emulation. Rather than a limitation, this was an advantage in our case, since we could set up our scripts very easily, and implement some ad-hoc tweaks to improve the detection of bugs or work around some issues. In addition, Unicorn integrates very well with AFL++, thanks to its _unicorn mode_ , which essentially allows to fuzz pretty much anything that can be emulated with Unicorn. The only step required is the definition of the `place_input_callback`, a function that writes inputs in the target's memory at every interaction.

Thanks to this, we could also test other functions in the Titan M firmware, while not forgetting about reasonable attack scenarios. Nonetheless, after a couple of fuzzing campaigns around the SPI rescue feature that did not lead to any significant result, we decided to focus on the tasks again, replicating a similar experiment as the one we did in a black-box setting. AFL++ allows to have custom mutators, hence we plugged libprotobuf-mutator again and emulated three tasks of the firmware separately: `Keymaster`, `Identity`, and `Weaver`. We decided to ignore AVB due to the limited attack surface it exposes, with most of the interactions happening while the device is in bootloader mode.

First and foremost, we asked ourselves whether we could once again find the bugs we already knew about, to prove the effectiveness of this new solution. Fortunately, the answer was positive, with the exception of one bug, which takes us to the limitations of emulation-based fuzzing. As we all know, indeed, there is no free lunch, and also in this case, this approach brings some drawbacks.

  * Multiple hardware-dependent functions: these parts of the code cannot be easily emulated, thus we had to hook them and inevitably reduce the coverage of our testing.

  * Still limited detection: while improving the bare black-box approach, we still can only detect bugs that cause Unicorn errors, consequently missing the various in-page overflows, off-by-ones, etc.

  * Lack of full system emulation: this choice in itself also brings the drawback of ignoring certain functions, which inevitably implies missing some bugs. That is the reason why we did not succeed in finding again the vulnerability we just mentioned above.

To address the second issue, Unicorn allows to set a number of custom hooks to monitor certain memory accesses or specific fragments of code. We did implement some heuristics to catch some patterns of bugs, like broken calls to `memcpy` that ended up reading from the Boot ROM (that is mapped at address `0x0`). On the other hand, this comes at a cost: hooks impact performance, and there is always a trade-off between the time spent reverse engineering to identify these patterns, and the time you actually let the fuzzer run freely.

## The vulnerability

But now, let's get into the tasty part. While fuzzing the Keymaster task, we discovered an interesting crash caused by a `UC_ERR_WRITE_UNMAPPED`, while processing an `ImportKey` request. This crash was occurring in a `strb` instruction, meaning that the firmware was trying to write 1 byte in an unmapped memory area. Note that the vulnerable firmware was introduced by Google's Pixel security update of May 2022.

A simple message that triggers the vulnerability is the following:
  
  
  ImportKeyRequest
  params {
  params {
  tag: ALGORITHM
  integer: 4
  }
  params {
  tag: DIGEST
  integer: 40706
  }
  }
  symmetric_key {
  material: "<1h5\003H\232@\233"
  }
  

As we can see from the Protobuf [definitions](https://android.googlesource.com/platform/external/nos/host/generic/+/refs/tags/android-platform-12.1.0_r1/nugget/proto/nugget/app/keymaster/keymaster.proto#184), `ImportKey` messages contain a `KeyParameters` field, which in turn is made of one or more `KeyParameter` objects. The bug occurs while processing the [tags](https://android.googlesource.com/platform/external/nos/host/generic/+/refs/tags/android-platform-12.1.0_r1/nugget/proto/nugget/app/keymaster/keymaster_defs.proto#39) in a key parameter: the vulnerable function loops through the list of parameters, and for each one it checks if the tag is `0x20005`, corresponding to `DIGEST`. When such parameters are found, the function takes the associated `integer` field, and after some checks it uses it as an offset of a stack buffer to set a byte to 1. By passing a large enough integer as parameter, it is possible to write out of bounds that one byte value of `0x01`.

The code snippet below, both in assembly and decompiled view, shows these checks as well as the `strb` instruction causing the out of bounds write and subsequent crash. At that point, `r1` is `0x1`, `r7` is the buffer address and `r3` is the integer field of the current `KeyParameter`.
  
  
  ldr.w  r1,[r2,#-0x4]
  ldr  r3,[PTR_DAT_0005d808] ; 0x20005
  cmp  r1,r3
  bne  increment_loop_vars
  ldr  r3,[r2,#0x0]
  uxtb  r0,r3
  cmp  r0,#0x4
  bhi  error_exit
  movs  r1,#0x1
  lsl.w  r0,r1,r0
  tst  r0,#0x15
  beq  error_exit
  strb  r1,[r7,r3]
  
  
  
  if (((nugget_app_keymaster_KeyParameter *)(offset + -1))->tag == 0x20005) {
  masked = *offset & 0xff;
  if ((4 < masked) || ((1 << masked & 0x15U) == 0)) {
  return 0x26;
  }
  *(undefined *)(buffer + *offset) = 1;
  *param_3 = *param_3 + 1;
  *param_4 = offset;
  }
  

The vulnerability can actually be triggered as many times as the number of parameters with a `DIGEST` tag, with the only limitation of remaining within the maximum size of the `KeyParameters` list. This results in multiple, 1-byte, out-of-bounds writes. Such writes are however far from arbitrary, due to the checks on the offset. Without entering into details of the bit-wise operations, the least significant byte can only be `0x0`, `0x2` or `0x4`.

At this point, it may seem that this is a very minor and hardly exploitable issue. However, do not forget that Titan M's memory is completely static, as we mentioned earlier. In addition, the bug can be reached by different code paths, considering the various messages that contain a `KeyParameters` field. Provided that we can write at the right place, there are plenty of different things that can be done by setting a single byte to 1, from a simple DoS to altering a _size_ variable somewhere in memory and causing a corruption elsewhere.

## Exploitation

At this point, we wrote a small script to generate and highlight all the possible writable addresses in Ghidra. Then we started searching for interesting targets, and as it turned out, triggering the vulnerability just _once_ was enough to compromise the chip.

### What to overwrite

During our tests, we understood that we could get to the vulnerable code with `r1` containing `0x14019`. After applying a `0xa204` offset to this (note that the least significant byte allows to pass the checks), we could reach `0x1e21d`. This address is part of a structure that we called `KEYMASTER_SPI_DATA`, containing information about the exchange of Keymaster messages with Android. In particular, we can overwrite one byte of the memory location pointing to where incoming requests for the Keymaster task are stored: by default this is `0x192c8`, but if we write `0x1` to `0x1e21d`, the value becomes `0x101c8`. As a result, the following Keymaster requests would be stored quite far from where they are supposed to be, with catastrophic consequences for the Titan M.

### The UART console

Before diving into the tale of how we exploited this vulnerability, let us take a moment to refresh how we can actually interact with the chip. The only tool we use is our _nosclient_ , which allows us to forge arbitrary messages and send them directly to the driver. After sending a request, Titan M replies with a return code, and a response, which is empty in case of errors. With only this information available, developing any exploit is particularly challenging: not only we do not have access to any debugger capability, but we also cannot see any stack traces nor immediate side-effects of an attack.

This is where the UART console exposed by the chip becomes extremely handy. There are two ways of accessing it, and both of them present different challenges. The first way relies on a special debugging cable called _SuzyQable_. This is officially mentioned as the cable to debug [Chrome OS microcontrollers](https://chromium.googlesource.com/chromiumos/third_party/hdctools/+/HEAD/docs/ccd.md), and since Titan M is based on the same operating system, it actually turns out to also work with it. To activate it, we only need to boot the Pixel smartphone in fastboot mode, and use the command `fastboot oem citadel suzyq on`. Then, when connecting the device using the _SuzyQable_ , we can access the UART console as a `tty` interface on our laptop. In parallel, the cable also allows to communicate with the device through `adb`. Unfortunately though, as soon as the chip crashes or even after a `reboot` command is sent over this console, the channel is closed and the interface needs to be activated again going back to fastboot mode. This is very impractical, which is the reason why we went with the second way.

The second solution can be seen as the _MacGyver_ one. The Titan M exposes the UART pins on the motherboard, so all we needed to do was solder two wires and obtain the very same shell as the one we could get with the cable. In this case, the console never closes and stays active no matter what happens to the device or the chip.

![](resources/2022-08-11_titan-m/uart.png)

The Titan M console is extremely basic and allows simple interactions with the chip, to investigate statistics, versions, and similar things. Most importantly though, it is the place where debugging logs are printed. Indeed, going back to exploit development, this clearly does not provide any information on what goes wrong when something does not work, but it is still very useful: for example, we could always try to jump to a function that prints something and verify that our exploit is working fine up to that point.

### Hijacking execution flow

As we said, thanks to the out of bounds write, we changed the address where incoming Keymaster requests were stored. This location is still in the memory space of the chip, thus an incoming message would end up overwriting other data in the Titan M's memory. For this reason, we tried sending larger and larger commands, monitoring the UART logs. After a bit of testing, we realized that if we placed a valid code address after `556` bytes of payload, we could jump to such an address, practically redirecting execution to a function of our choice. We were able to detect that thanks to some logs being printed in the UART console.

![](resources/2022-08-11_titan-m/payload.gif)

We suppose that this portion of memory was being used by some task (probably `idle`), which may have pushed a return address to its stack, that was now overwritten. At this point, we knew we could jump to an arbitrary function. How can we translate that into an actual exploit?

### Return Oriented Programming

Given the memory protections in place, we cannot write our own shellcode and jump to it, as writable memory is not executable. Instead, we can rely on a code-reuse attack, and mount an exploit based on Return Oriented Programming. The objective was to build a read-anywhere primitive: this way, we could leak the secrets Titan M is protecting with a crafted command from _nosclient_.

Unfortunately, we could not write our ROP chain exactly where we wrote our first gadget, because it would corrupt some memory that would make the chip crash before our exploit would be complete. Consequently, the first challenge was to _pivot_ the stack. Ideally, we wanted to decrease the stack pointer: assuming the stack to be moving towards larger addresses, we wanted to rely on the payload we could place in those 556 bytes, which we knew we could set as we wanted without causing any nasty side-effect. We found only one gadget to do so, which however also does a few more things:
  
  
  sub sp, #0x20; mov r4, r0; ldr r3, [r0]; add.w r5, r4, #0x70; ldr r3, [r3, #8]; blx r3;
  

Despite that, we wrote a ROP chain that would call it several times, while making sure that `r0` was pointing to a memory area we also controlled, and where we wrote some gadgets to make the `ldr` and `blx` instructions work as we wanted. In the picture below, we graphically show this approach for the first iterations (it is actually done several more times). The red arrows follow the execution flow, and the blue ones the stack pointer. Note that the scale is not respected.

![](resources/2022-08-11_titan-m/exploit_1.png)

After having _climbed up_ the stack a few times, we could proceed with the actual attack. The only way we could return our leaked bytes back to Android was to copy them in the response of an SPI command. For this to happen, we needed to be in the context of the command handler, which is called taking its address from memory after parsing the command code. We could therefore overwrite its address, but how should we set it? As replacing the actual code was impossible, all we could do was to make it jump into some memory area that we could also control, and write there more gadgets for our ROP chain. This is done in the space we created in the first step, making sure to ignore the slots we used in the previous ROP chain (basically assigning them to registers that we do not use).

This step was probably the most challenging one, as it entails finding the right gadget to make the stack pivot to a memory area that remains under our control when the handler is triggered. Unfortunately again, no such gadget existed, so we had to be creative. The way we solved this was quite tricky: by emulating the execution of the Keymaster _DestroyAttestationIds_ command handler, we understood that there was one single 32-bit slot in its stack that was not overwritten by some previous functions in the call chain. Therefore, we wrote one single gadget there, that would act as a trampoline to actually move the stack far enough from the Keymaster stack and reach an area where our payload would be preserved.

![](resources/2022-08-11_titan-m/exploit_2.png)

Wrapping up so far, the exploit goes as follows:

  1. move up on the stack from where we get code execution;

  2. once we have enough space, execute a ROP chain that:

  * replaces the Keymaster _DestroyAttestationIds_ command handler with one gadget, popping some registers from the stack;

  * writes _one_ gadget on the Keymaster stack, that ends up being executed when the handler is triggered, and moves the stack pointer enough to reach an area where what we write will not be tampered with by the normal execution of the firmware;

  * copies the final ROP chain to such an area.

Once we got here, finishing the exploit was relatively straightforward, as we controlled execution from the handler context. We called `memcpy` with the user-provided arguments, to copy what we wanted to read in the Keymaster SPI response buffer. We then jumped back to the Keymaster stack, like the normal command handler would have done.

## Impact

Thanks to the leak functionality that we built with this exploit, we can now read arbitrary memory on the chip. This means we can now have access to any readable address. As a consequence, we can dump the secrets stored in the chip (such as the Root of Trust sent by the Pixel bootloader when the Titan M is updated). Moreover, we can access the Boot ROM, that was not previously available. This is possible despite the slightly customized version of `memcpy` present in the chip, which checks if the `src` or `dst` buffers equal `0x0`. In fact, instead of jumping directly to the entry point of the function, we skip those checks and jump directly to the basic block where the copying happens.

One of the most interesting consequences of this attack is the ability to retrieve any StrongBox protected key, defeating the highest level of protection of the Android Keystore. Similarly to what happens in TrustZone, these keys can only be used inside Titan M, while they are stored in an encrypted _key blob_ on the device.

The procedure is the following:

  * read a key blob from the Android OS (from any application);

  * send a valid, well-formed _BeginOperation_ request, containing such a key blob:

  * the handler for this command decrypts the key and stores it into a specific memory address. This prepares the chip to perform the requested operation;

  * run the exploit and leak the memory where the plaintext key is now stored.

To demonstrate the effectiveness of this attack we also developed a dummy application that simply creates a StrongBox-protected AES key and encrypts a string with it. With our exploit and the approach explained above, we can leak the corresponding key from the Titan M, and by re-using the same initialization vector we can successfully decrypt the string offline (or rather "off phone").

Sorry, your web browser doesn't support embedded videos.

As a reminder, there are two conditions to perform this attack. First, we need to be able to send commands to the chip, either from a _rooted_ device (required to use _nosclient_), or physically accessing the SPI bus.

Then, we need a way to access the key blobs on the Android file system, which can be done again by being root, or with some exploit to bypass File Based Encryption or the _uid_ access control.

## Mitigations

We reported this vulnerability to Google, and of course the best mitigation is the patch provided in the June security bulletin. However, we do want to point out an interesting feature that would have made the _StrongBox_ key blob leak impossible. Indeed, an application can create a key that is _authentication-bound_ , specifying `setUserAuthenticationRequired(true)` when building it with `KeyGenParameterSpec`. This way, users need to authenticate before using the key and the key blob is encrypted a second time using a special key derived from the user password that we do not have.

## Conclusion

The Titan M chip is the most secure component of Google's Pixel phones and the anchor to which all the security of the device is ultimately linked. Despite good architectural decisions and many efforts made to minimize its attack surface, making exploitation of vulnerabilities very hard, and the lack of appropriate tools to debug the chip, in our project we managed to:

  * Reverse engineer the communications between Android and the chip.

  * Develop _nosclient_ , an open source tool that lets a researcher send arbitrary commands to the chip.

  * Discover vulnerabilities using black box fuzzing.

  * Emulate the chip and discover a vulnerability using emulation-based fuzzing.

  * Leverage some implementation weaknesses and exploit the vulnerability to achieve code execution on the chip and exfiltrate sensitive data (cryptographic keys) that should never leave it.

The vulnerability was reported to Google in May 2022 and a fix was released in the Pixel Security update of June 2022.

## Disclosure timeline

To provide transparency of our vulnerability disclosure process and illustrate the complexity of coordinating the reporting, triaging, and fixing bugs in embedded software, a detailed timeline of all relevant events of the reporting process is provided below.

  * **2022-03-02** : Vulnerability reported. Opened [issue 222318108](https://issuetracker.google.com/issues/222318108) in Google's Issue Tracker, providing a technical description of the bug and a Proof of Concept (PoC) exploit using Quarkslab's [nosclient tool](https://github.com/quarkslab/titanm/).

  * **2022-03-02** : Google's Android Security Team (AST) acknowledged the report and asked for a PoC program.

  * **2022-03-07** : Quarkslab provided a standalone copy of the _nosclient_ code repository with the PoC.

  * **2022-03-08** : AST asked for some more obvious way to reproduce the bug, such as triggering a crash with a callstack, demonstrable code execution, or some way to observe memory corruption with a debugger. Asked for a PoC for a more recent version of the firmware.

  * **2022-03-10** : Quarkslab replied that it does not have tools for debugging the Titan M chip. However, with the precise description of the bug that was included in the report, it should be possible to identify it in the source code.

  * **2022-03-15** : Quarkslab sent a new version of _nosclient_ that adds a functionality to write the one byte value `0x01` to any memory address (with the constraints shown above) using the bug, which should make it possible for AST to observe memory corruption using a debugger.

  * **2022-03-16** : Google AST was able to run the PoC and reviewed the source code of the mentioned functions and other code paths, but did not see any out of bounds write as reported. They stated they were unable to find or reproduce the security issue. Nonetheless they passed the report to the Titan M engineering team for further investigation.

  * **2022-03-16** : Quarkslab asked which version of the firmware was used for testing and if that version is publicly available.

  * **2022-03-18** : Google AST indicated they used the firmware build of the March OTA for Pixel 5/Redfin devices, which is public. Also said that they would continue the investigation to try to find the issue.

  * **2022-03-20** : Quarkslab informed Google AST that it managed to achieve code execution on the chip on a Pixel 3 phone with the firmware version that Google used for testing. The PoC demonstrates gaining control of execution flow and redirecting it to an internal firmware function (`task_print_list`) that prints the list of tasks to the logs, which can be observed by attaching to the UART console. The exploit's source code, a description of how it works, and sample log output was provided.

  * **2022-03-30** : Google AST asked clarification about how Quarkslab retrieved the UART logs.

  * **2022-03-31** : Quarkslab indicated that engineers had soldered wires to the chip's UART points in the PCB. They also mentioned the alternative of the special _SuzyQable_ , which should be available to Google.

  * **2022-03-31** : Google replied saying they would continue investigating the issue.

  * **2022-04-18** : Quarkslab asked for a status update.

  * **2022-04-18** : Google indicated that they were waiting for the necessary hardware to investigate the issue, and would communicate as soon as there is an update.

  * **2022-04-27** : Quarkslab informed Google that a presentation about the Titan M vulnerability research project was accepted at the TROOPERS conference in Germany to be held at the end of June, 2022.

  * **2022-04-29** : Google told Quarkslab that they identified the vulnerability and a potential fix, proposing a conference call to discuss the status.

  * **2022-05-04** : Conference call between Quarkslab engineers, Google Android Security Team members, and a Titan engineering team member. Google indicated that they planned to release a fix in June. Quarkslab recalled that the TROOPERS conference was coming up, and another talk had been submitted to Black Hat USA, acceptance pending. They also offered to continue investigating ways to exploit the vulnerability in a way that would be easier to reproduce and verify. Google appreciated Quarkslab's feedback on the disclosure process so far and said they would follow up on the necessity for a different exploit.

  * **2022-05-27** : Google notified the imminent release of a fix in the June 2022 Pixel update and asked Quarkslab to confirm the acknowledgments information. Google assigned **CVE-2022-20233** to the vulnerability.

  * **2022-06-05** : Google published the June 2022 Pixel update with fixes for CVE-2022-20233 (Severity: Critical) and 4 other vulnerabilities (3 ranked High severity, 1 Moderate) in the Titan M component.

  * **2022-06-07** : Google informed Quarkslab that they had assigned the vulnerability a reward of 10,000 USD per its Android Security Rewards program.

  * **2022-06-08** : Quarkslab thanked Google for the reward and asked what criteria were used to assign it, given that the public information about Android's bug bounty states that the top possible reward for a code execution bug in Titan M is 1 million USD, two orders of magnitude higher than the assigned one.

  * **2022-06-10** : Google replied that the bug was fixed and released in the June Pixel Update Bulletin and that with regards to the payment amount each report is reviewed individually for reward by a committee, and that while it is possible to receive an award up to the amounts listed on the publicly stated bounty program website, based on severity and impact to the Android ecosystem, this particular report was only eligible for 10,000 USD.

  * **2022-06-10** : Quarkslab thanked Google for the response but stated that it actually did not include an answer to the question about the criteria used to assign the reward, and asked in case another vulnerability was to be reported in the future, how would a reporter get it considered for the top range advertised in the program.

  * **2022-06-17** : Google replied that they would do an internal review and provide an update soon.

  * **2022-06-20** : Quarkslab sent Google a new exploit that demonstrates code execution on the chip and exfiltration of encryption keys from it. A detailed description of the exploitation technique, the exploit's source code, and a video showing its use to exfiltrate a StrongBox-protected AES key were provided.

  * **2022-06-21** : Google acknowledged the new submission and said they would review it.

  * **2022-06-24** : Google asked for the source code of the sample Android application used in the demo video.

  * **2022-06-29** : Quarkslab sent the source code of the sample Android app, a description of how it works, and an explanation of how it is exploited using the reported vulnerability.

  * **2022-06-30** : Quarkslab's engineers Damiano Melotti and Maxime Rossi Bellom presented their Titan M vulnerability research project at the TROOPERS conference.

  * **2022-07-18** : Google notified Quarkslab that the reward was increased to 75,000 USD.

  * **2022-08-11** : Quarkslab's engineers Damiano Melotti and Maxime Rossi Bellom presented their Titan M vulnerability research project at the Black Hat USA Briefings in Las Vegas.

* * *

If you would like to learn more about our security audits and explore how we can help you, [get in touch with us](https://content.quarkslab.com/talk-to-our-experts-blog)!
