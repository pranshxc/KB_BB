---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-18_blind-os-command-injection-via-activation-request.md
original_filename: 2023-05-18_blind-os-command-injection-via-activation-request.md
title: Blind OS Command Injection via Activation Request
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 0d2a70875f9b18fb88cb845f75931284aed16087ae9a652ad4b74be758f7b452
text_sha256: 9804f18b34bf62201cfc58d5cc451815a3aaa5f2925e7d9ade54246bb2a9c192
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Blind OS Command Injection via Activation Request

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-18_blind-os-command-injection-via-activation-request.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `0d2a70875f9b18fb88cb845f75931284aed16087ae9a652ad4b74be758f7b452`
- Text SHA256: `9804f18b34bf62201cfc58d5cc451815a3aaa5f2925e7d9ade54246bb2a9c192`


## Content

---
title: "Blind OS Command Injection via Activation Request"
page_title: "Zero Day Initiative — CVE-2023-20869/20870: Exploiting VMware Workstation at Pwn2Own Vancouver"
url: "https://www.zerodayinitiative.com/blog/2023/5/17/cve-2023-2086920870-exploiting-vmware-workstation-at-pwn2own-vancouver"
final_url: "https://www.zerodayinitiative.com/blog/2023/5/17/cve-2023-2086920870-exploiting-vmware-workstation-at-pwn2own-vancouver"
authors: ["Nguyễn Hoàng Thạch (@hi_im_d4rkn3ss)"]
programs: ["VMware"]
bugs: ["Memory corruption", "Buffer Overflow", "Out-of-bounds Read"]
bounty: "80,000"
publication_date: "2023-05-18"
added_date: "2023-05-29"
source: "pentester.land/writeups.json"
original_index: 1137
---

# Blog

#  CVE-2023-20869/20870: Exploiting VMware Workstation at Pwn2Own Vancouver 

__ May 18, 2023

__ The ZDI Research Team

_This post covers an exploit chain demonstrated by Nguyễn Hoàng Thạch (_[_@hi_im_d4rkn3ss_](https://twitter.com/hi_im_d4rkn3ss) _) of STAR Labs SG Pte. Ltd. during the Pwn2Own Vancouver event in 2023. During the_[ _contest_](https://www.zerodayinitiative.com/blog/2023/3/24/pwn2own-vancouver-2023-day) _, he used an uninitialized variable bug and a stack-based buffer overflow in VMware to escalate from a guest OS to execute code on the underlying hypervisor. His successful demonstration earned him $80,000 and 8 points towards Master of Pwn. All Pwn2Own entries are accompanied by a full whitepaper describing the vulnerabilities being used and how they were exploited. The following blog is an excerpt from that whitepaper detailing CVE-2023-20869 and CVE-2023-20870 with minimal modifications._

* * *

Prior to being patched by VMware, a pair of vulnerabilities existed within the implementation of the virtual Bluetooth USB device inside VMware Workstation. During the event, the VMware version used was 17.0.1 build-21139696. An attacker could leverage these two bugs together to execute arbitrary code in the context of the hypervisor. To exploit this vulnerability, the attacker must have the ability to execute high-privileged code on the guest OS. Bluetooth functionality is also required, but this is enabled by default. These bugs were patched in late April with [VMSA-2023-0008](https://www.vmware.com/security/advisories/VMSA-2023-0008.html).

**CVE-2023-20870 – The Uninitialized Variable Info Leak**

In VMware Workstation, in the _USB Controller_ setting, there is the “Share Bluetooth devices with the virtual machine” option. This is enabled by default. It allows guest OSes to use Bluetooth devices. This functionality is handled by the _Vbluetooth_ component, which is implemented in the _vmware-vmx.exe_ binary. The VBluetooth device information can be read by `lsusb` command (in Linux) as follows:

Each time a guest OS sends a [USB Request Block](https://docs.kernel.org/driver-api/usb/URB.html) (URB) request to the VBluetooth device, the function `VUsbBluetooth_OpNewUrb()` is invoked to allocate memory to read or write data. The following code snippet is the `sub_140740EB0` function in _vmware-vmx.exe_ :

This function returns a `VUsbURB` object. Data is stored in this object in the `urb_data` buffer. This buffer is allocated by the `RBuf_New()` function and assigned to `urb_data` at [1]. Note that the `RBuf_New()` function calls the `malloc` function to allocate memory, so the memory is uninitialized. Then, the URB data is handled by `VUsbBluetooth_OpSubmitUrb()` function. This code snippet is from the `sub_140740F50` function in _vmware-vmx.exe_ :

`total_urb_len` is the length of data the guest OS wants to read from or write to the URB. This value is controllable by the attacker. At [2], `total_urb_len` is assigned to `urb->urb_actualsize` without a check. Then, based on the endpoint type and URB packet, the corresponding function is invoked. Afterwards, `urb->urb_actualsize` is set again in the handler function, but only if the packet is valid. We can see in the `VUsbBluetooth_OpSubmitUrb()` function that if the `urb_data->bRequest` is an invalid opcode (checked at [3]), `urb->urb_actualsize` will not be set, and it will remain set to an attacker-controllable value.

Finally, the `UHCI_UrbResponse()` function is invoked to send data back to the guest. The following snippet is in the `sub_1401F7C50` function in _vmware-vmx.exe_ , corresponding to assembly code from address `0x1401F7CBF`: 

A maximum of `urb->urb_actualsize` bytes of data from the `urb->urb_data` buffer will be returned to the guest. Since an attacker could control the value of `urb->urb_actualsize` and the `urb->urb_data` buffer is uninitialized, the guest OS could read uninitialized data from the heap.

**CVE-2023-20869 – The Stack-based Overflow**

The VBluetooth device also implements an [Service Discovery Protocol](https://learn.microsoft.com/en-us/windows-hardware/drivers/bluetooth/communicating-with-sdp-servers#:~:text=The%20Bluetooth%20driver%20stack%20supports,range%20of%20the%20local%20radio.) (SDP) feature. When a guest OS wants to send an SDP packet to a specific Bluetooth peer, it must initialize a [L2CAP](https://www.amd.e-technik.uni-rostock.de/ma/gol/lectures/wirlec/bluetooth_info/l2cap.html) connection to this peer. This is done by sending an `L2CAP_CMD_CONN_REQ` packet to the `L2CAP_SIGNALLING_CID` channel with the Protocol/Service Multiplexer (PSM) field set to 0x1. The result is a newly created SDP socket. This socket is used when processing subsequent SDP operations.

The SDP protocol data unit (PDU) format is well explained [here](https://www.amd.e-technik.uni-rostock.de/ma/gol/lectures/wirlec/bluetooth_info/sdp.html). When the host OS processes an SDP PDU from the guest, it invokes `SDPData_ReadElement()` to parse the PDU. Here’s a look at the `SDPData_ReadElement()` function from the `sub_14083C1D0` function in _vmware-vmx.exe_ :

The switch-case [1] is used to parse the _data element size descriptor_ to determine the size of the raw data. Then this size is passed to `SDPData_ReadRawInt()` to parse the _unsigned int_ at [2].

Here’s another code snippet. This one is from the `sub_14083C570` function in _vmware-vmx.exe_. Since the PDU is submitted by the guest OS, an attacker can control the `size` argument, which leads to a possible stack buffer overflow at [3]/[4].

These bugs were combined at Pwn2Own Vancouver to pop calc on the target system. The exploit itself started in the guest OS while the calculator spawned on the host OS.

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/317a86cd-6022-4701-978b-44550bdd807c/STARVMWareClose.png)

* * *

_Thanks again to Nguyễn Hoàng Thạch for providing this write-up and for his participation in Pwn2Own Vancouver. He has participated in multiple Pwn2Own contests, and we certainly hope to see more submissions from him in the future. Until then, follow the team on_[ _Twitter_](https://www.twitter.com/thezdi) _,_[_Mastodon_](https://infosec.exchange/@thezdi) _,_[_LinkedIn_](https://www.linkedin.com/company/zerodayinitiative) _, or_[ _Instagram_](https://www.instagram.com/thezdi) _for the latest in exploit techniques and security patches._

  * [VMware](/blog/tag/VMware)
  * [Pwn2Own](/blog/tag/Pwn2Own)
  * [Exploit](/blog/tag/Exploit)
