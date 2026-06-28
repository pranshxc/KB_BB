---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-12_the-printer-goes-brrrrr-again.md
original_filename: 2023-05-12_the-printer-goes-brrrrr-again.md
title: The Printer Goes Brrrrr, Again!
category: documents
detected_topics:
- sso
- command-injection
- otp
- automation-abuse
- graphql
- api-security
tags:
- imported
- documents
- sso
- command-injection
- otp
- automation-abuse
- graphql
- api-security
language: en
raw_sha256: 6a577ef556c1e60735dbbe5da568e01ec44aa99bebde4fee45cbeb65d661946a
text_sha256: 057eaad816d8347b66ec953f3ddc810b20628f63eb3fdd4c6603e60c4bdb211b
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: true
---

# The Printer Goes Brrrrr, Again!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-12_the-printer-goes-brrrrr-again.md
- Source Type: markdown
- Detected Topics: sso, command-injection, otp, automation-abuse, graphql, api-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: True
- Raw SHA256: `6a577ef556c1e60735dbbe5da568e01ec44aa99bebde4fee45cbeb65d661946a`
- Text SHA256: `057eaad816d8347b66ec953f3ddc810b20628f63eb3fdd4c6603e60c4bdb211b`


## Content

---
title: "The Printer Goes Brrrrr, Again!"
page_title: "The printer goes brrrrr, again!"
url: "https://www.synacktiv.com/en/publications/the-printer-goes-brrrrr-again.html"
final_url: "https://www.synacktiv.com/en/publications/the-printer-goes-brrrrr-again.html"
authors: ["Rémi Jullian (@netsecurity1)", "Mehdi Talbi (@abu_y0ussef)", "Thomas Jeunet  (@cleptho)"]
programs: ["Canon"]
bugs: ["Printer hacking", "Buffer Overflow", "Memory corruption"]
publication_date: "2023-05-12"
added_date: "2023-05-15"
source: "pentester.land/writeups.json"
original_index: 1161
---

# The printer goes brrrrr, again!

Written by Rémi Jullian, Mehdi Talbi, Thomas Jeunet \- 12/05/2023 - in Exploit \- [Download](the-printer-goes-brrrrr-again#) __

For the second time at Pwn2Own competition, network printers have been featured in Toronto 2022. The same brands were included this year as in Austin 2021: HP, Lexmark and Canon with equivalent model. Unlike the previous event, we only targeted the Lexmark and Canon but nevertheless manage to compromise both. Sadly, the bug we exploited for the Canon printer was previously used by another team in the competition. Anyway, this is how we achieved code execution on the Canon printer.

Looking to improve your skills? Discover our **trainings** sessions! [Learn more](../offers/trainings). 

If you are interested in how to bootstrap this research, refer to our other [article](the-printer-goes-brrrrr). This article along with the published tools might explain why we have seen so many entries on this target during the last edition: **14**.

For this Pwn2Own edition, we targeted another protocol available by default on the printer and prominent in many networks: NetBIOS.

## NetBIOS

NetBIOS, strictly speaking, is an API providing different services (Name service, Datagram distribution service and Session service) that can run over multiple network protocols. Nowadays only NetBIOS level 2 over TCP/IP (NBT) remains, and here we will focus on the name service that allows name registration and resolution. NetBIOS communication happens between names that have to be previously resolved.

### Implementation in DryOS

From the debug strings, it appears that NetBIOS implementation in Dry-OS is based on an app called `netcifsnqendapp`:
  
  
  nblogf0("netcifsnqendapp/IMP/nq/nddaemon.c", "ndStart", 404, 0x64u);
  nblogf_info("netcifsnqendapp/IMP/nq/nddaemon.c", "ndStart", 406, 0xC8u, "====> Name Daemon is starting up");
  if ( Nsinitialize() )
  {
  /* ... */
  }
  

After a brief research, this implementation looks to be closed source. However, abusive usage of log-related functions allows retrieving functions name as well as file names where functions were implemented. This section will introduce how the NetBIOS protocol is implemented within Dry-OS.

#### Context allocation

The function `initialize` implemented in `nddaemon.c` calls three functions in order to allocate custom contexts : `ndDatagramInit`, `ndNameInit` and `ndAdapterListInit`.

`ndDatagramInit` allocates 2 arrays of chars of 255 bytes each, given as parameters to `cmNetBiosParseName` (alloc of 510 bytes). The function is used to decode a NetBIOS name and will be described later in the blogpost.

`ndNameInit` calls `ndInternalNameInit` which allocates a table of 20 entries of type `netbios_internal_name_entry` (100 bytes per entry) used to store internal netbios names (i.e related to the printer). By default 2 entries are populated, the NetBIOS name of the printer (e.g "CANONA5A2C6") and the NetBIOS workgroup to which the printer belongs (e.g "WORKGROUP").

`ndNameInit` also calls `ndExternalNameInit` which allocates table of 20 entries of type `netbios_external_name_entry` (88 bytes per entry), used to store resolved external NetBIOS name request (i.e entries not related to the printer).

Finally, `ndAdapterListInit` allocates an adapter table used to store up to 2 adapters context.

Once all contexts have been allocated, the function `CreateService` is called 4 times, with a custom identifier, in order to create sockets and bind on ports:

Identifier | Binding address | Description  
---|---|---  
0 | 0.0.0.0:137 (UDP) | Implement NetBIOS name service  
1 | 0.0.0.0:138 (UDP) | Implement NetBIOS datagram service  
3 | 127.0.0.1:1022 (UDP) | Implement a local NetBIOS resolver (handle request from `nsGetHostByName`)  
4 | 127.0.0.1:1023 (UDP) | Implement a NetBIOS datagram forwarder (handle request from `nsSendToName`)  
  
#### NetBIOS name registration

The first entry of type `netbios_internal_name_entry` will be announced on the network using `ndInternalNameRegister`, which sends a NetBIOS Name Registration (Claim) request on port UDP/137 as described in [RFC 1001 - 15.1.1](https://datatracker.ietf.org/doc/html/rfc1001#section-15.1.1). The call stack associated with NetBIOS internal name registration is:
  
  
  initialize
  processConfigChange
  ndInternalNameRegisterAllNames
  ndInternalNameRegister
  sendRegistrationRequest
  sySendToSocket

#### Packet reception

The task dedicated to NetBIOS uses `sySelectSocket` in order to monitor the 4 file descriptors created using `CreateService`. Once a fd is ready to be read, a call to `syRecvFromSocket` is made with a fixed length of 1500 bytes. According to the fd on which the packet was received, one of the following functions is called:

0.0.0.0:137 (UDP) | ndNameProcessExternalMessage  
---|---  
0.0.0.0:138 (UDP) | ***REDACTED-SUSPECT-TOKEN***127.0.0.1:1022 (UDP) | ndNameProcessInternalMessage  
127.0.0.1:1023 (UDP) | ***REDACTED-SUSPECT-TOKEN***From an attacker point of view, it is thus interesting to look at both `ndNameProcessExternalMessage` and `ndDatagramProcessExternalMessage` as they implement a network protocol that does not support authentication, and is not likely to be filtered. By looking at these functions we quickly found some references to `cmNetBiosParseName`, thus we decided to look at how NetBIOS name encoding works under the hood.

### NetBIOS name encoding

According to RFC 1001, there are two levels of encoding. The first level maps a 16 bytes NetBIOS name into a 32 byte wide field using a reversible, half-ASCII, biased encoding:

![netbios first level encoding](/sites/default/files/inline-images/netbios_encoding-level1_1.webp)

For example, using this encoding scheme the NetBIOS name _SYNACKTIV_ maps to _FDFJEOEBEDELFEEJFGCACACACACACACA_

The second level maps the domain system name into the "compressed" representation required for interaction with the domain name system. The RFC 883 depicts the format of a domain name. According to this RFC, a domain name is expressed in terms of a sequence of labels. Each label is represented as a one octet length field followed by that number of octets. Actually, the length field is a 6-bit field. If the high order two bits of the length field are set to 1, then the following 14 bits are an offset pointer into the full message to the actual label string from another domain name that belongs in this name. A zero length value indicates the root label which is always null.

For instance, the NetBIOS name _SYNACKTIV_._synacktiv.synacktiv.com_ is encoded into a NetBIOS packet as following:

![NetBIOS packet](/sites/default/files/inline-images/netbios_encoding-level2-level2.webp)

## The vulnerability

The vulnerability is present inside the `cmNetBiosParseName` function:
  
  
  uint8_t *cmNetBiosParseName(
  netbios_datagram_hdr *pkt_hdr,
  uint8_t *pkt_after_hdr,
  char *first_level_name,
  char *second_level_name,
  unsigned int len_remaining_255)
  {
  /* ... */
  
  ptr_buff = resolveLabel(pkt_hdr, &pkt_after_hdr_);
  v12 = ptr_buff + 1;
  if ( *ptr_buff == '\x20') {
  // parse first level encoding
  for ( i = 0; i < 16; ++i ) {
  v15 = 16 * *v12 - 16;
  v16 = v12[1];
  v12 += 2;
  first_level_name[i] = (v16 - 'A') | v15;
  }
  v17 = *pkt_after_hdr_;
  
  if (*pkt_after_hdr_ )
  v5 = '.';
  else
  *second_level_name = 0;
  
  // parse second level encoding
  if (v17) {
  do {
  new_src_ptr = resolveLabel(pkt_hdr, &pkt_after_hdr_);
  label_len = (unsigned __int8)*new_src_ptr;
  src = new_src_ptr + 1;
  n = label_len;
  if (len_remaining_255 > label_len) {
  memcpy(second_level_name, src, n); // [1]
  new_dest = &second_level_name[n];
  len_remaining_255 -= n;
  *new_dest = v5;
  second_level_name = new_dest + 1;  // [2]
  }
  }
  while (*pkt_after_hdr_);
  *(second_level_name - 1) = 0;
  }
  }
  }

This function performs the first level decoding of the first label. If the subsequent label does not start with a NUL byte, then the function continues with the second level decoding. Each label is decoded in the `resolveLabel` function. This function returns a pointer to the label start from which its length is read. The decoded label is then copied into an allocated buffer of 255 bytes if there is still enough space in the destination buffer. However, if the length of the label field is zero, then no copy will take place but the destination buffer (`second_level_name`) will be increased by one. This scenario is illustrated by the following picture.

![NetBIOS domain name representation and compression](/sites/default/files/inline-images/netbios.webp)

After decoding the first level label, the parser will encounter a label offset (i.e., high order two bits of the length field is set to 1) that points to a NUL byte. In that case no byte will be copied, but the destination buffer will be increased by one. If we repeat this process several times, then we can increase the destination buffer by 255 bytes. A following valid label will be therefore copied beyond the limit of the allocated buffer which leads to a heap-based overflow.

Luckily, the order of allocations made during NetBIOS context initialization helps us as the destination buffer (`second_level_name`) comes from an allocation followed in memory by an array of `netbios_internal_name_entry` structure, which is interesting to override in an exploitation scenario !

Please not that due to scheduling issue, a context switch may occur in a rare few cases between the 2 allocations which would make these 2 allocations not contiguous in memory.

The call stack allowing to trigger the vulnerability is given hereafter:
  
  
  ndStart
  syRecvFromSocket
  ndNameProcessExternalMessage
  cmNetBiosParseName
  

## Exploitation

The heap overflow described in the section below allows overriding (partially) an array of 20 structures of type `netbios_internal_name_entry`. Each structure is 0x64 bytes long, and overriding only one allows getting a Write-What-Where (WWW) primitive of 2 bytes. The way to obtain this is by sending a Positive Name Query Response ([RFC 1002 - Section 4.2.13](https://datatracker.ietf.org/doc/html/rfc1002#autoid-28)), with a corrupted state, in order to trigger a Negative Name Query Response ([RFC 1002 - Section 4.2.14](https://datatracker.ietf.org/doc/html/rfc1002#autoid-29)), that will write 2 bytes of controlled data, at a controlled address. The 2 bytes written will be the Transaction ID specified in the Positive Name Query Response, in order to build the header ([RFC 1002 - Section 4.2.2.1](https://datatracker.ietf.org/doc/html/rfc1002#section-4.2.1.1)) of the Negative Name Query Response.

The call stack allowing to trigger this write primitive is:
  
  
  ndStart
  syRecvFromSocket
  ndNameProcessExternalMessage
  ndInternalNamePositiveQuery
  ***REDACTED-SUSPECT-TOKEN***In the `netbios_internal_name_entry` structure, several fields are important in order to obtain this primitive:

![NetBIOS internal name](/sites/default/files/inline-images/netbios_name_internal.webp)

1\. The NetBIOS name, an array of 16 bytes specified in the query, and located in the structure at offset 0x04. This name is used to find the matching `netbios_internal_name_entry` structure in the array of 20 entries.

2\. A pointer to a `netbios_adapter` structure, located at offset 0x24. This structure contains another pointer at offset 0x38, used to write the Negative Name Query Response payload. Usually, this pointer is used to build a NetBIOS response payload, and the first 2 bytes are set to the Transaction ID (`NAME_TRN_ID` as defined in [RFC 1002, Section 4.2.2.1](https://datatracker.ietf.org/doc/html/rfc1002#section-4.2.1.1)). In the context of the exploit, this pointer defines the address where the 2 controlled bytes will be written (the “WHERE”). The fake `netbios_adapter` structure will be written in memory using the BJNP protocol, allowing writing controlled data at a fixed address.

3\. An `uint16_t` field, located at offset 0x20 allowing to write 2 bytes (the “WHAT”) at the address pointed by the pointer written previously.

4\. An `uint16_t` field, located at offset 0x2c, allowing to pass a state check (must be set to 8) to reach the function `returnNegativeRegistrationResponse`.

5\. An `uint16_t` field, located at offset 0x3c, whose value is the expected transaction request id, specified in the request.

Using the primitive twice allows to override a function pointer (4 bytes). The `pjcc_dec_ope_echo` function pointer, related to the PJCC protocol, is targeted in order to redirect the execution flow to a shellcode.

Thus, the exploitation steps are the following:

1\. Use the heap-overflow vulnerability to prepare the WWW allowing to write the 2 lower-bytes of the function pointer `pjcc_dec_ope_echo`

2\. Trigger the WWW by sending a Positive Name Query Response

3\. Use the heap-overflow vulnerability again, to prepare the WWW with the WHERE address now pointing on the 2 upper-bytes of the function pointer `pjcc_dec_ope_echo`

4\. Trigger the WWW by sending another Positive Name Query Response

5\. Send a BJNP SessionStart message to store the shellcode at a fixed address

6\. Send a PJCC ECHO message. The overridden function pointer leads to shellcode execution.

The scenario is summarized in the following figure:

![Exploit scenario](/sites/default/files/inline-images/overflow_1.webp)

We used the same post exploitation as in Austin 2021, so you can refer to [our previous article](the-printer-goes-brrrrr) for details.

And ... here is our famous ninja, displayed on the printer's screen after successfully exploiting the vulnerability during [our Pwn2Own attempt](https://twitter.com/thezdi/status/1601253066380124161) :

![Synacktiv ninja displayed on the printer screen](/sites/default/files/inline-images/p2o_ninja_v2_1.webp)

Such as for our previous exploit, we released the source code on our [Github repository:](https://github.com/synacktiv/canon-mf644)

## The patch

During the Pwn2Own contest, (9th December 2022) we targeted the firmware in version 11.04, latest firmware available at that time. On the 14th of April 2023, Canon released a note mentioning security fixes (likely) related to the Pwn2Own, with a list of 10 CVEs including 6 buffer overflows affecting our device:

  * CVE-2023-0851
  * CVE-2023-0852
  * CVE-2023-0853
  * CVE-2023-0854
  * CVE-2023-0855
  * CVE-2023-0856

Thus, we decided to download the new firmware version (12.03) in order to check if our vulnerability has been patched, and to confirm that indeed, we had a collision with another team. Please note that at the time of writing, this new firmware was not directly available via an OTA update. Thus, we downloaded [Firmware Update Tool V12.03](https://hk.canon/en/support/0400623316?model=3102C013#) from Canon website, and performed the upgrade using USB.

We directly looked at the vulnerable function and checked the modification related to the vulnerable function `cmNetBiosParseName`:

![cmNetBiosParseName](/sites/default/files/inline-images/diff_cmNetBiosParseName.webp)

With the new patch, specifying a label length (`label_len`) of 0 will now decrement the field remaining length (`len_remaining_255`) of 1. Thus it's not possible anymore to increment the destination pointer, without decrementing the field remaining length.

Share this article
