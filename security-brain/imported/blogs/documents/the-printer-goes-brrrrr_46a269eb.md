---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-25_the-printer-goes-brrrrr.md
original_filename: 2022-05-25_the-printer-goes-brrrrr.md
title: The Printer Goes BRRRRR!!!
category: documents
detected_topics:
- supply-chain
- command-injection
- path-traversal
- business-logic
- api-security
- mobile-security
tags:
- imported
- documents
- supply-chain
- command-injection
- path-traversal
- business-logic
- api-security
- mobile-security
language: en
raw_sha256: 46a269eb765db684c0800c3a32f863f6224614ca5ee435a3865d5a2e16812318
text_sha256: 2164acc0ccdf731d6f156197892ccefc534b51e1bd1ff8af5141ecdf03494df9
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# The Printer Goes BRRRRR!!!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-25_the-printer-goes-brrrrr.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, path-traversal, business-logic, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `46a269eb765db684c0800c3a32f863f6224614ca5ee435a3865d5a2e16812318`
- Text SHA256: `2164acc0ccdf731d6f156197892ccefc534b51e1bd1ff8af5141ecdf03494df9`


## Content

---
title: "The Printer Goes BRRRRR!!!"
page_title: "The printer goes brrrrr!!!"
url: "https://www.synacktiv.com/en/publications/the-printer-goes-brrrrr.html"
final_url: "https://www.synacktiv.com/en/publications/the-printer-goes-brrrrr.html"
authors: ["Mehdi Talbi (@abu_y0ussef)", "Rémi Jullian (@netsecurity1)", "Thomas Jeunet  (@cleptho)"]
programs: ["HP", "Lexmark", "Canon"]
bugs: ["Memory corruption"]
bounty: "60,000"
publication_date: "2022-05-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2609
---

# The printer goes brrrrr!!!

Written by Mehdi Talbi, Rémi Jullian, Thomas Jeunet \- 25/05/2022 - in Exploit, Reverse-engineering \- [Download](the-printer-goes-brrrrr#) __

Network printers have been featured for the first time at Pwn2Own competition in Austin 2021. Three popular LaserJet printers were included in the completion: HP, Lexmark and Canon. During the event, we (Synacktiv) managed to compromise all of them allowing us to win the whole competition. In this post, we will focus on how we achieved code execution on the Canon printer.  

Looking to improve your skills? Discover our **trainings** sessions! [Learn more](../offers/trainings). 

Network printers are good target candidate from an attacker perspective since they are rarely reinstalled or supervised and thus constitutes a perfect place to hide on a network. Moreover, they provide the attackers with persistent access to sensitive documents that may be scanned or printed. The Canon _ImageCLASS MF644Cdw_ printer was one of three printers that could be targeted during the Pwn2Own competition in Austin 2021.

Each team willing to take part in the Pwn2Own registers for one or several devices which they want to compromise during the competition. Then, if they succeed during one of three attempts, they earn "master of pwn" points, a cash prize (that will vary depending on the targeted equipment), and the equipment itself. The "master of pwn" points are used to establish an overall ranking which allows at the end of the competition to attribute the title of "Master of Pwn" to the winner. We managed to compromise the Canon printer during our first attempt, and thus won a $20,000 cash prize as well as 2 "master of pwn" points.

![](/sites/default/files/inline-images/Printer_Table.webp)

## Bootloader analysis

The first step to bootstrap the research is to obtain the binary executed by the device. To do so, an approach is to dump the memory storage of the device. Looking at the printed circuit board, we can identify some interesting integrated circuits and a potential UART connector:

![printable circuit board](/sites/default/files/inline-images/PCB_1.webp)

According to what is printed on it, the Flash circuit is a W25Q16JV, a 16Mbit serial NOR Flash. Using the pin configuration described in its datasheet available on the [winbond website](https://www.winbond.com/hq/product/code-storage-flash-memory/serial-nor-flash/?__locale=en&partNo=W25Q16JV), it is straightforward to extract the Flash content using a SOP8 clip and a CH341A, using [flashrom](https://www.flashrom.org/Flashrom).

![W25Q16JV pin configuration](/sites/default/files/inline-images/pin_config_0.webp)

The dumped binary file does not contain a filesystem nor ELF or PE executable, but might contain a compiled binary anyway as stated by this [binwalk](https://github.com/ReFirmLabs/binwalk) output:
  
  
  $ binwalk flash.bin
  
  DECIMAL  HEXADECIMAL  DESCRIPTION
  --------------------------------------------------------------------------------
  336448  0x52240  Zlib compressed data, default compression
  337968  0x52830  Zlib compressed data, default compression
  341524  0x53614  Zlib compressed data, default compression
  348537  0x55179  Copyright string: "Copyright (C) 1997-2015 by CANON Inc."
  350068  0x55774  Certificate in DER format (x509 v3), header length: 4, sequence length: 859
  351488  0x55D00  SHA256 hash constants, little endian
  361256  0x58328  Unix path: /home/nca/workspace/RB-EMERALD/printing_pf/release/modules/dryos/../dryos/src/mohacs_boot/device/lcd_7line.c
  361468  0x583FC  Unix path: /home/nca/workspace/RB-EMERALD/printing_pf/release/modules/dryos/../dryos/src/mohacs_boot/device/emmc.c
  361748  0x58514  Unix path: /home/nca/workspace/RB-EMERALD/printing_pf/release/modules/dryos/../dryos/src/mohacs_boot/device/sicdlIntegritycheck.c
  362256  0x58710  Unix path: /home/nca/workspace/RB-EMERALD/printing_pf/release/modules/dryos/../dryos/src/mohacs_boot/device/sicdlRomData.c
  365496  0x593B8  Unix path: /home/nca/workspace/RB-EMERALD/printing_pf/release/modules/dryos/../dryos/src/oscore/stdlib/iobuf.c
  365712  0x59490  Unix path: /home/nca/workspace/RB-EMERALD/printing_pf/release/modules/dryos/../dryos/src/mohacs_boot/drysh/cmd_chkcachelib.c
  444441  0x6C819  Certificate in DER format (x509 v3), header length: 4, sequence length: 1288
  […]

Then, we loaded the dumped binary file in [IDA Pro](https://hex-rays.com/ida-pro/) in order to reverse the binary. After finding the absolute address, we deduced the loading address of this binary as 0x10000000. However, it was not the firmware running on the device but only the bootloader to start it, while the actual firmware was stored on the eMMC at address 0x1500000 and mapped at address 0x40b00000.
  
  
  if ( emmc_direct_read(0x40B00000, 0x1500000u, 0x40u) != 0x40 )
  {
  printf("BOOTABLE HEADER READ ERROR\n");
  return -1;
  }
  if ( BOOTLOADER_GET_ROM_HEADER_INFO(&v7, (nca1_header *)0x40B00000) )
  {
  printf("BOOTABLE GET ROM HEADER ERROR \n");
  return -1;
  }
  if ( BOOTLOADER_ROM_HEADER_HEADER_CHKSUM(&v7, 0x40B00000) )
  {
  printf("BOOTABLE ROM HEADER CHECK ERROR \n");
  return -1;
  }
  printf("BOOTLOADER BOOTABLE START\n");

The bootloader is able to "download" a firmware to the eMMC. According to the decompiled code, the format of the firmware is composed of a header starting with a 4 bytes' magic and, depending on this magic, the content is obfuscated.
  
  
  int __fastcall firmware_header_check(_BYTE a1[4], int a2, int a3, unsigned int a4)
  {
  unsigned int magic; // r0
  unsigned int v6; // [sp+0h] [bp-8h] BYREF
  
  v6 = a4;
  like_memcpy((unsigned __int8 *)&v6, a1, 4u, a4);
  magic = bswap32(v6);
  v6 = magic;
  if ( magic == 'NCFW' )
  return 1;
  if ( magic == 0xAFAF9C9C )
  return 0;
  do_assert("unknown = 0x%08x\n", magic);
  return 2;
  }

The routine used to deobfsucate the firmware is the following:
  
  
  _BYTE *__fastcall NCFW_deobfuscate(_BYTE *data, unsigned int size, char offset)
  {
  unsigned int i; // r3
  unsigned int tmp; // r4
  
  for ( i = 0; i < size; ++i )
  {
  tmp = (unsigned __int8)(data[i] - (offset + i) - 1);
  data[i] = ~((2 * tmp) | (tmp >> 7));
  }
  return data;
  }

## Firmware analysis

Several methods can be used in order to obtain the firmware. While it should be possible to retrieve it by dumping the eMMC, we managed to obtain it in an easier way, simply by setting an HTTP proxy, with the printer's administration panel web interface, and then to check for updates. As plain-text HTTP is used for firmware updates, one can easily get the firmware download URL if an update is available. Another method is to extract the firmware from the "_MF643Cdw/ MF641Cw Firmware Update Tool"_ , which is available on Canon support website. This tool is provided as either a PE file (e.g _win-mf643-641-fw-v1005.exe_) or a macOS disk image file (e.g _mac-mf643-641-fw-v1005-64.dmg_), and allows firmware update using either a Windows or MacOS workstation. The PE file is also a self-extracting archive, containing another PE (e.g _mf643c_mf642c_mf641c_v1005_typea_w.exe_), from which three _NCFW_ packages can be extracted as they are simply appended as raw files. These NCFW packages can thus be extracted as following:
  
  
  user@debian:~/ 7z x win-mf643-641-fw-v1005.exe
  user@debian:~/ grep --byte-offset --only-matching --text 'NCFW' mf643c_mf642c_mf641c_v1005_typea_w.exe
  470016:NCFW
  140927837:NCFW
  152682373:NCFW
  user@debian:~ dd if=mf643c_mf642c_mf641c_v1005_typea_w.exe of=package1.bin bs=1 skip=470016 count=$((140927837-470016))
  user@debian:~ dd if=mf643c_mf642c_mf641c_v1005_typea_w.exe of=package2.bin bs=1 skip=140927837 count=$((152682373-140927837))
  user@debian:~ dd if=mf643c_mf642c_mf641c_v1005_typea_w.exe of=package3.bin bs=1 skip=152682373

Three NCFW packages can be identified, the firmware itself (134MB), a language package (12MB), and a DCON package (506K) related to the DC controller. It should be noted that the CEFW package exists only for firmware updates coming from the internet.

The package format is depicted by the following figure:

![Package Format](/sites/default/files/inline-images/package_format_1.webp)

  1. The _CEFW_ package is only present when the printer downloads directly its upgrade from one of Canon websites. The content is gzipped and the header contains in particular: header size, uncompressed size and actual package size. The uncompressed data holds one to many _NCFW_ packages.
  2. The _NCFW_ package has a header containing in particular header size and package size, with the content obfuscated with the previously shown routine. The deobfuscated data holds one to many _NCA_ packages.
  3. The NCA package represents a block of data written on the eMMC. Its header contains the eMMC address where the package should be written to, its size and apparently its release date (directly in hex, 0x20220222 for the 22nd of February 2022 for instance) and its version. In most cases, the first _NCA_ package in a _NCFW_ package is special and contains a _SIG_ package and one to many _Mm_ packages:
  4. The _Sig_ package holds cryptographic signature of the data of the different _NCA_ packages.
  5. The _Mm_ package is only a header containing in particular the eMMC address of the others _NCA_ package in the same _NCFW_ package. Thus, it allows to know how many _NCA_ package remain.

An IDA loader has been implemented in order to load a Canon firmware in IDA. The loader is available in the [Synacktiv's Github repository](https://github.com/synacktiv/canon-mf644/).

In this post, we will focus on the firmware in version 10.02, which was running on the targeted device during the contest (the latest available firmware at that time).

The operating system on the printer is based on a custom Real Time Operating System named “ _DryOS_ ”:
  
  
  DRYOS version 2.3, release #0059

We also identified this operating system during a [previous work](https://www.synacktiv.com/publications/treasure-chest-party-quest-from-doom-to-exploit), on a quite old Canon based printer (MX920 series), which is running a former version (release _#0049_). This system is itself based on µITRON, a Japanese RTOS specification. _DryOs_ is used by Canon not only for their printers, but also for DSL cameras.

As we knew this operating system provides a debug shell called _DryShell_ , we tried to find the UART on the main board, using a Saleae logic analyzer. We also found that several debug messages were sent by the bootloader on the UART:

![Logic analyzer capture using Saleae](/sites/default/files/inline-images/UART_Canon.webp)

After identifying the UART, we made simple soldering points (TX, RX and GND) in order to use a USB to serial adapter. This allowed using tools like _pyserial_ in order to benefit from the debug shell. Once the printer boot initialization process is finished, the _DryOs shell_ prompt is displayed and several commands can be used:
  
  
  Dry> vers
  DRYOS version 2.3, release #0059
  Dry-MK 2.66
  Dry-DM 1.21
  Dry-FSM 0.10
  Dry-EFAT 1.22
  Dry-stdlib 1.57
  Dry-PX 1.15
  Dry-drylib 1.22
  Dry-shell 1.19
  Dry-command alpha 065

Commands like _xd_ or _xm_ can be used for respectively dump or modify the memory, and thus were quite useful during the exploitation of our vulnerability.

## Hunting for bugs

The firmware is quite big since it contains more than 100k functions, automatically discovered by IDA. As the firmware doesn't contain any symbol information, a common task when analyzing such firmware is to identify strings that may be used for debug purposes. By briefly looking at a few functions, we found a logging function used more than 19k times in the firmware. Here are few examples where this function is called:
  
  
  logf(2802, 3, "[CPC] %s ERROR [Fail getOperationParam]\n", "pjcc_act_checkUserPassword2");
  logf(3604, 3, "[CADM] %s: cadmMessage.message.pEventMessage is NULL", "cadm_sendEventMessage");
  logf(3520, 6, "[USBD] %s EPNo = 0x%X EPNoSS = 0x%X\n", "ScanBULK Out", (unsigned __int8)v14[0], v1)

While this logging function is not always used with a fixed pattern, the third argument often matches a string like "[PREFIX] %s", with the first variadic function argument being the name of the function. We thus developed an IDA Python script, based on [BIP](https://github.com/synacktiv/bip), to take profit of HexRay's API in order to rename some functions automatically.

In order to identify the attack surface and choose a network service that could be targeted, we ran a quick _nmap_ scan to find all UDP and TCP ports that were exposed in the default configuration. We then tried to find, for each network service, the related DryOs task and its entry-point:

Service | Port | Task name | Notes  
---|---|---|---  
HTTP/HTTPS | 80/TCP, 443/TCP | HtpInit | Canon HTTP Server  
LPD | 515/TCP | LPDCtrl | Line Printer Daemon Protocol  
IPP/IPPS | 631/TCP,10443/TCP | IPP_INIT | Internet Printing Protocol  
Jetdirect | 9100/TCP | RAWctrl | Allow printing using PDL (Page Description Language)  
Canon MFNP | 8610/TCP  
8610/UDP | pscan_TCP_Task  
pscan_UDP_Task | Print/Scan jobs over the network (based on BJNP protocol)  
Canon CADM | 9007/TCP  
9013/TCP  
47545/TCP  
47547/TCP (SSL)  
47545/UDP | cadm_tcp_res  
cadm_tcp_cal  
cadm_tcp_adm  
cadm_tcp_sec  
cadm_udp_adm | Canon administration proprietary protocol  
NetBIOS | 137/UDP, 138/UDP | smbinit | NetBIOS  
SNMP | 161/UDP | SNAgent | Simple Network Management Protocol  
SLP | 427/UDP | SLPSvcAgent | Service Location Protocol  
WSD | 3702/UDP | WSINinit | Web Services Dynamic Discovery  
Zeroconf | 5353/UDP | BN_BNSet | Multicast DNS (Bonjour Apple)  
  
A custom HTTP server runs in order to implement a web administration panel, based on CGI scripts. Most of the CGI scripts can be reached post authentication, and thus were excluded from our analysis. The HTTP server is also used to handle IPP requests (Internet Printing Protocol) as IPP is based on HTTP. Unsurprisingly, the HTTP server also handles TLS and thus allows HTTPS and IPPS. Such as the HTTP server, the TLS stack doesn't seem to be based on an open-source project. In addition to IPP, other standard printing-related protocols such as LDP or Jetdirect are implemented. In order to allow device and service discovery in typical office computer network, protocols like SLP, WSD and Zeroconf are also supported. MFNP is a Canon custom protocol, based on BJNP, which allows for instance print and scan job creation over the network. Finally, another Canon custom protocol named CADM allows printer administration over the network either over TCP (47545), TCP+TLS (47547) or UDP (47545). We decided to focus on this protocol as analyzing the packet flow processing and reverse engineering the command handlers was straightforward.

## The vulnerability

The vulnerability is present in the CADM service. The following figure illustrates the format of CADM messages:

![CADM Message Format](/sites/default/files/inline-images/cadm_1.webp)

The header starts with the magic value 0xCDCA. The _param len_ field encodes the length of the payload and the _operation code_ field specifies the type of operation. CADM supports several operations such as adding a new user (operation code = 12), changing the password of a user (operation code = 15) or simply echoing back submitted payload (operation code = 1). There are 41 available handlers defined at offset 0x44557b58 through the following structure:
  
  
  struct pjcc_handlers {
  uint16_t operation_code;
  uint16_t field_2;
  void  *field_4;
  uint32_t field_8;
  uint32_t (*decode_func)(void);
  uint32_t (*encode_func)(void);
  uint32_t (*release_func)(void);
  uint32_t (*field_14)(void);
  uint32_t field_1c;
  uint32_t field_20;
  }

The vulnerability is present in the decoding function of the handler responsible for checking the password (operation code = 0x83), namely, the function _pjcc_act_checkUserPassword2_(0x4198ecf0).

The payload is depicted by the following figure. The payload is made of 3 distinct buffers along with their size encoded into 1 byte field.

![Checkpass Message Format](/sites/default/files/inline-images/cadm_checkpass_format_0.webp)

As shown by the following snippet of code, the vulnerable function allocates a structure of 428 bytes and copies inside its inlined buffers the data from the packet without checking the size:
  
  
  uint32_t pjcc_dec_ope_checkUserPassword2(int *a1, int a2, int *a3)
  {
  /* ... */
  
  alloc = (pjcc_checkpassword_payload *)pjcc_zeroAlloc(428);
  pjcc_checkpass_obj = alloc;
  
  v7 = pjcc_dec_ubyte(a1, alloc);
  v12 = pjcc_dec_ulong(a1, (int)&pjcc_checkpass_obj->field_4);
  
  v14 = pjcc_dec_ubyte(a1, &pjcc_checkpass_obj->buffer_len);
  v17 = pjcc_dec_buffer(a1, pjcc_checkpass_obj->buffer_len, (char *)
  pjcc_checkpass_obj->buffer, v15);
  
  v19 = pjcc_dec_ubyte(a1, &pjcc_checkpass_obj->salt_len);
  v22 = pjcc_dec_buffer(a1, pjcc_checkpass_obj->salt_len, (char *)
  pjcc_checkpass_obj->salt, v20);
  
  v24 = pjcc_dec_ubyte(a1, &pjcc_checkpass_obj->hash_len);
  
  result = pjcc_dec_buffer(a1, pjcc_checkpass_obj->hash_len, (char *)
  pjcc_checkpass_obj->hash, v25);
  
  /* ... */
  }

The vulnerable object _pjcc_checkpass_obj_ has the following structure:
  
  
  struct pjcc_checkpassword_payload
  {
  unsigned uint8_t type;
  unsigned uint8_t field_4;
  unsigned uint8_t buffer_len;
  unsigned uint8_t buffer[256];
  unsigned uint8_t salt[32];
  unsigned uint8_t salt_len;
  unsigned uint8_t hash[128];
  unsigned uint8_t hash_len;
  };

The buffers _salt_ and _hash_ are vulnerable to heap-based overflow are depicted by the following figure:

![Overflow](/sites/default/files/inline-images/cadm_checkpass_struct_0.webp)

## Exploitation

The exploitation of this vulnerability requires to dig into the allocator internals.

### DryOs Allocator

The DryOs Allocator is simply a "best-fit” allocator that maintains a singly linked list of free chunks. This freelist is stored at address 0x45f17540. As shown by the following figure, it is a linked list of free chunks:

![DryOS Allocator](/sites/default/files/inline-images/allocator.webp)

The allocation function iterates over the freelist and returns the first chunk that fulfills the requested size. The current chunk is fragmented and a new chunk is created if the remaining space (chunk_size - request_size > metadata_size) is larger than the size of the chunk’s metadata (40 bytes). The allocated chunk is then unlinked from the freelist.

![Malloc](/sites/default/files/inline-images/alloc_0.webp)

  
Chunks in the freelist are ordered by their address and when a chunk is freed, it is inserted back in the freelist. The chunk is merged with adjacent free chunks.

In order to track allocations, we have implemented a DryShell command that dumps the freelist.

### Exploitation Scenario

Our exploitation strategy is to overflow the hash buffer and corrupt the next field of the chunk that is adjacent in memory to our vulnerable object. Our goal is to force a subsequent allocation at an arbitrary address.

The first step of the exploitation is to fragment the heap in order to insert large chunks. The goal is to allocate our vulnerable object from a large chunk in order to prevent our fake chunk to be served at an early stage once the vulnerable chunk is inserted back in the freelist. Requesting the UI using HTTPS is sufficient to create the desired heap state:
  
  
  DryOs > !hd
  magic = 0x0, size = 0x5ff930, next = 0x49c1dc88
  magic = 0x46524545, size = 0x48, next = 0x49c1e7c0
  magic = 0x46524545, size = 0x78, next = 0x49c30e50
  magic = 0x46524545, size = 0x30, next = 0x49c30f10
  magic = 0x46524545, size = 0x60, next = 0x49c35c98
  magic = 0x46524545, size = 0x48, next = 0x49d0b578
  magic = 0x46524545, size = 0x60, next = 0x49d14c70
  magic = 0x46524545, size = 0x60, next = 0x49d15a18
  magic = 0x46524545, size = 0x240, next = 0x49d22268
  magic = 0x46524545, size = 0x2848, next = 0x49d24b68
  magic = 0x46524545, size = 0x9198, next = 0x49d2ddd8
  magic = 0x46524545, size = 0x292140, next = 0x0

The second step is to trigger the overflow and corrupt the _next_ field of a freed chunk. In the exploit we set the _next_ pointer to the address 0x44557b14. This address has been selected because it precedes several CADM structures (state machine, handlers, etc.) that contain multiple function pointers. Moreover, this address is a good candidate for a fake chunk since the memory at 0x44557b14 + 4 contains a very large value (_size_ field). A large size allows us to request a large allocation that cannot be fulfilled by the previous free chunks in the freelist. The memory at 0x44557b14 + 8 contains a NULL pointer (_next_ field) that allows to close the freelist. Please note that there is no need to have the string ‘FREE’ at the selected address since there are no security checks made by the allocator.

![Overflow](/sites/default/files/inline-images/overflow2_1.webp)

The final step is to send a large CADM echo packet in order to get our fake chunk and overlap CADM data structures with controlled data. More precisely, we rewrite these data structures with the original content in order to not break the CADM state machine. We only corrupt the handler responsible for processing the echo request (pjcc_act_echo) such that it points to our shellcode. The shellcode is also embedded in the echo’s payload. It gets immediately executed after processing the CADM echo packet according to the CADM state machine.

### Post Exploitation

In order to illustrate a successful exploitation of the vulnerability, we decided to write a shellcode that displays a picture (Synacktiv's logo) on the LCD printer's screen. Therefore, the first step was to understand how the screen's framebuffer works. We identified that it is mapped at 0x40900000. Then, we used the _xm_(modify memory) command of the DryShell in order to write a green pixel (0x00FF00) as a long value:
  
  
  Dry> xm --help
  usage: xm [-|addr [access [e_addr value flag]]]
  - : usage
  addr : [0-9a-fA-F]*
  access : b(byte:default) | w(word) | l(long word)
  e_addr : [0-9a-fA-F]*
  value : [0-9a-fA-F]*
  flag : f(fill) | s(search) | u(unmatch)
  -> + : auto increment
  Dry> xm 0x40900000 l 0x40900000 0x00ff00 f

We noticed that the first pixel from the LCD printer's screen changed to green and was quickly restored to its previous value. Thus, we understood that the frame buffer is simply an array where 3 bytes are used to store a single pixel value. Each of these 3 bytes defines respectively the Red, Green and Blue intensity for a pixel. As the screen resolution is 800x480 pixels, the framebuffer size is thus 800x480x3.

![Framebuffer](/sites/default/files/inline-images/frame_buffer.webp)

In order to implement a quite small shellcode, a TCP socket is used to read each pixel value from a picture, sent by a Python script, using _PIL_ (Python Imaging Library) and implementing the server side.

The shellcode implements this by calling the following network-related functions:

  *  _netSocket_ (0x424bbfb4)
  *  _netConnect_ (0x424bc298)
  *  _netRecv_ (0x424bc554)

It is worthwhile to note that the _sin_family_ field specified in the _sockaddr_in_ structure must be set to _0x100_ to specify _AF_INET_ (i.e it changes from Linux where _AF_INET_ is 0x02). As the shellcode calls _netRecv_ in an infinite loop, _DryOS_ is able to perform tasks context switches, and only the CADM service is impacted by the exploitation of the vulnerability. Another approach could have been chosen, by creating a proper _DryOs_ task, and restoring the hijacked function context.

The exploit code is available in the [Synacktiv's Github repository](https://github.com/synacktiv/canon-mf644/). You can also take a look at our Ninja beeing displayed on the printer's screen:

Video file

Share this article
