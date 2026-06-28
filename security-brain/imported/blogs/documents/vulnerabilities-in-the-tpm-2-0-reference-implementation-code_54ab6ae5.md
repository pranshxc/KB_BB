---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-14_vulnerabilities-in-the-tpm-20-reference-implementation-code.md
original_filename: 2023-03-14_vulnerabilities-in-the-tpm-20-reference-implementation-code.md
title: Vulnerabilities in the TPM 2.0 reference implementation code
category: documents
detected_topics:
- cloud-security
- supply-chain
- sso
- access-control
- command-injection
- mfa
tags:
- imported
- documents
- cloud-security
- supply-chain
- sso
- access-control
- command-injection
- mfa
language: en
raw_sha256: 54ab6ae5177c4aea19c4910cef4de40f15330c1e2c5a7c13a7510b3d809670c0
text_sha256: cf26a5b4a7237470072fbed3367dbd424db9ad905ccbaac750aa1f5028691f14
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Vulnerabilities in the TPM 2.0 reference implementation code

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-14_vulnerabilities-in-the-tpm-20-reference-implementation-code.md
- Source Type: markdown
- Detected Topics: cloud-security, supply-chain, sso, access-control, command-injection, mfa
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `54ab6ae5177c4aea19c4910cef4de40f15330c1e2c5a7c13a7510b3d809670c0`
- Text SHA256: `cf26a5b4a7237470072fbed3367dbd424db9ad905ccbaac750aa1f5028691f14`


## Content

---
title: "Vulnerabilities in the TPM 2.0 reference implementation code"
page_title: "Vulnerabilities in the TPM 2.0 reference implementation code - Quarkslab's blog"
url: "https://blog.quarkslab.com/vulnerabilities-in-the-tpm-20-reference-implementation-code.html"
final_url: "https://blog.quarkslab.com/vulnerabilities-in-the-tpm-20-reference-implementation-code.html"
authors: ["Francisco Falcon (@fdfalcon)"]
programs: ["Microsoft", "VMware", "Google", "IBM", "Lenovo", "Qemu", "Nuvoton", "Trusted Computing Group", "STMicroelectronics", "Aruba Networks", "CERT/CC", "libtpms"]
bugs: ["Memory corruption", "Out-of-bounds Read", "Out-of-bounds Write"]
bounty: "20,000"
publication_date: "2023-03-14"
added_date: "2023-03-15"
source: "pentester.land/writeups.json"
original_index: 1379
---

#  [ Vulnerabilities in the TPM 2.0 reference implementation code ](./vulnerabilities-in-the-tpm-20-reference-implementation-code.html "Permalink to Vulnerabilities in the TPM 2.0 reference implementation code")

Posted Tue 14 March 2023  
Author [Francisco Falcon](./author/francisco-falcon.html)  
Category [ Vulnerability ](./category/vulnerability.html)  
Tags [TPM](./tag/tpm.html), [Trusted Platform Module](./tag/trusted-platform-module.html), [CVE-2023-1017](./tag/cve-2023-1017.html), [CVE-2023-1018](./tag/cve-2023-1018.html), [vulnerability](./tag/vulnerability.html), [2023](./tag/2023.html)

* * *

In this blog post we discuss the details of two vulnerabilities we discovered in the Trusted Platform Module (TPM) 2.0 reference implementation code. These two vulnerabilities, an out-of-bounds write ([CVE-2023-1017](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1017)) and an out-of-bounds read ([CVE-2023-1018](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1018)), affected several TPM 2.0 software implementations (such as the ones used by virtualization software) as well as a number of hardware TPMs.

* * *

## Introduction

In October 2021, Microsoft released Windows 11. One of the installation requirements that stood out was the need for a Trusted Platform Module (TPM) 2.0. An implication of this requirement is that, in order to be able to run Windows 11 within a virtual machine, virtualization software must provide a TPM to VMs, either by doing passthrough to the hardware TPM on the host machine, or by supplying a virtual TPM to them.

We found this to be an interesting topic for vulnerability research, since the addition of virtual TPMs means extended attack surface on virtualization software that can be reached from within a guest, and so it could potentially be used for a virtual machine escape. As a result of the research effort, we discovered two security issues: an out-of-bounds write identified as [CVE-2023-1017](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1017), and an out-of-bounds read identified as [CVE-2023-1018](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1018). They can be triggered from user-mode applications by sending malicious TPM 2.0 commands with encrypted parameters. Interestingly, these two vulnerabilities turned out to have a way longer reach than we initially thought: given that they originate in the reference implementation code published by the Trusted Computing Group (TCG for short, the nonprofit organization that publishes and maintains the TPM specification), these security bugs affected not only every virtualization software we tested, but hardware implementations as well.

Note that most of our assessments in this blog post (e.g. regarding exploitability, impact, or which platforms are affected) are based on our analysis of software-based virtual TPMs, because we can debug them in an easy way to perform dynamic analysis (well, debugging Hyper-V's virtual TPM is harder because it runs as an [IUM process](https://learn.microsoft.com/en-us/windows/win32/procthread/isolated-user-mode--ium--processes), but that's another story). On the contrary, getting visibility of what's happening at runtime in the firmware of a TPM, running in a separate chip without debugging interfaces, is an entirely different problem to tackle. Even doing static analysis of the firmware of a hardware TPM proved to be difficult: the few TPM firmware updates we attempted to analyze happened to be encrypted. Therefore, the lack of specific assessment on hardware TPMs doesn't mean that they are not affected; it just means that we couldn't evaluate how most of them are impacted due to the lack of observability. However, using the Proof-of-Concept code published in this blog post, we have verified that at least some discrete TPM chips are vulnerable. After attempting the OOB write, the chip would stop responding (i.e. it didn't recognize commands anymore) and require a hard reboot of the computer to be operational again, thus confirming its vulnerable condition.

## Affected platforms

This is a non-exhaustive list of affected software and hardware platforms. Products listed here are those in which we could certainly demonstrate the existence of the vulnerabilities with the help of the PoC provided within this blog post, but it's very likely for other TPMs - either virtual or physical- to be vulnerable as well.

  * The vulnerable code was present in the latest available version (at the time we performed our research) of the TPM 2.0 reference implementation: [Trusted Platform Module Library Specification, Family "2.0", Level 00, Revision 01.59 – November 2019](https://trustedcomputinggroup.org/wp-content/uploads/Trusted-Platform-Module-Library-Family-2.0-Level-00-Revision-1.59_pub.zip);
  * Microsoft Hyper-V on Windows 10 (affected module: `TPMEngUM.dll` version 10.0.19041.1415);
  * VMware Workstation version 16.2.4 build-20089737 (affected module: `tpm2emu.exe` \- no version information in the executable);
  * [Libtpms/SWTPM](https://github.com/stefanberger/libtpms), used by Qemu and VirtualBox (compiled from the master branch, commit `520a2fa27d27a4ab18f4cf1c597662c6a468565f`);
  * Nuvoton hardware TPM (firmware version: 1.3.0.1);
  * In general, all TPMs 2.0 whose firmware is based on the Trusted Computing Group reference implementation code are expected to be affected.

## A threat to cloud computing

All the major cloud computing providers offer instances with virtual TPMs. This exposes an interesting scenario, since a malicious actor could attempt to exploit these vulnerabilities in the virtual TPM in order to escape from a virtual machine and compromise the host system.

  * Amazon AWS has [NitroTPM](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html);
  * Microsoft Azure provides virtual TPMs as part of [Trusted Launch](https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch);
  * Google Cloud offers virtual TPMs as part of [Shielded VMs](https://cloud.google.com/blog/products/identity-security/virtual-trusted-platform-module-for-shielded-vms-security-in-plaintext);
  * Oracle Cloud Infrastructure provides virtual TPMs as part of [Shielded Instances](https://blogs.oracle.com/cloud-infrastructure/post/introducing-shielded-instances-for-oci-compute).

Those providers using a virtual TPM based on the TCG reference implementation are expected to be vulnerable. In the case of Google Cloud, the blog post linked above mentions that the core of their virtual TPM comes from [code published by IBM](https://sourceforge.net/projects/ibmswtpm2/), which is extracted automatically from the full source code of the TPM 2.0 spec, and we verified that the bugs in the `CryptParameterDecryption` function are present in it. In the case of Microsoft Azure, the documentation linked before mentions that their virtual TPM is "compliant with the TPM 2.0 spec", and we have verified that the virtual TPM included in the version of Hyper-V that is available on Windows 10 is indeed vulnerable. The bugs were also present in Microsoft's [open source reference implementation](https://github.com/microsoft/ms-tpm-20-ref). 

Regarding Amazon AWS and Oracle Cloud Infrastructure, we don't have much details about what they use, except that the NitroTPM documentation mentions that it "_conforms to the TPM 2.0 specification_ " with a link to the TCG website.

## Fixes

### Reference implementation

  * The Trusted Computing Group published [errata version 1.4 for TCG Trusted Platform Module Library](https://trustedcomputinggroup.org/wp-content/uploads/TPM-2.0-Library-Spec-v1.59-Errata-v1.4_pub.pdf), with suggested fixes for the two bugs.

### Software products

  * Microsoft patched the bugs in Hyper-V in their March, 2023 security update. Their assessment of impact for the OOB write is low in TPM 2.0 in Pluton/HCL/Overlake/Manticore standard server for Azure because the overwrite is only 2 bytes and their team have not identified a consistent and easily achievable way to obtain EoP or RCE with only 2 bytes.
  * Microsoft also patched their open source reference implementation with commit [9bdd9f0aaba5e54b3c314cfff02cf532281a067e](https://github.com/microsoft/ms-tpm-20-ref/commit/9bdd9f0aaba5e54b3c314cfff02cf532281a067e). 
  * VMware is expected to issue fixes for the bugs in April, 2023. 
  * Libtpms patched the bugs in commit [324dbb4c27ae789c73b69dbf4611242267919dd4](https://github.com/stefanberger/libtpms/commit/324dbb4c27ae789c73b69dbf4611242267919dd4).
  * Chromium OS patched the vulnerabilities in commit [3b87ed233acb4c76c27872e1ac0b74dc032199f1](https://chromium.googlesource.com/chromiumos/third_party/tpm2/+/3b87ed233acb4c76c27872e1ac0b74dc032199f1%5E%21/).
  * IBM patched their open source implementation in commit [102893a5f45dbb0b0ecc0eb52a8dd4defe559f92](https://sourceforge.net/p/ibmswtpm2/tpm2/ci/102893a5f45dbb0b0ecc0eb52a8dd4defe559f92/).

### Hardware products

  * Nuvoton published security advisory [SA-003](https://www.nuvoton.com/support/security/security-advisories/sa-003/) for their _NPCT65x_ TPM chip. 
  * Lenovo published security advisory [LEN-118320](https://support.lenovo.com/us/en/product_security/LEN-118320) regarding affected products using said Nuvoton TPM.

Check the website of your computer manufacturer for TPM firmware updates.

## Technical details

### A primer on TPM encrypted parameters

As described in the [Trusted Platform Module Library Specification, Family 2.0, Part 1: Architecture](https://trustedcomputinggroup.org/wp-content/uploads/TCG_TPM2_r1p59_Part1_Architecture_pub.pdf) document, Section 21 - "_Session-based encryption_ ", several TPM 2.0 commands have parameters that may need to be encrypted going to or from the TPM. Session-based encryption may be used to ensure confidentiality of these parameters. Quoting the specification:
  
  
  Not all commands support parameter encryption. If session-based encryption is allowed, only the first
  parameter in the parameter area of a request or response may be encrypted. That parameter must have
  an explicit size field. Only the data portion of the parameter is encrypted. The TPM should support
  session-based encryption using XOR obfuscation. Support for a block cipher using CFB mode is platform
  specific. These two encryption methods (XOR and CFB) do not require that the data be padded for
  encryption, so the encrypted data size and the plain-text data size is the same.
  
  [...]
  
  Session-based encryption uses the algorithm parameters established when the session is started and
  values that are derived from the session-specific sessionKey.
  
  [...]
  
  If sessionAttributes.decrypt is SET in a session in a command, and the first parameter of the command is
  a sized buffer, then that parameter is encrypted using the encryption parameters of the session.
  

A TPM 2.0 command with encrypted parameters is composed of a base command header, followed by a `handleArea`, then a `sessionArea`, finishing with the (encrypted) `parameterArea`. The following diagram illustrates said structure:
  
  
  +---------------------+
  |  |
  |  |
  | Base command header |
  |  |
  |  |
  +---------------------+
  |  |
  |  handleArea  |
  |  |
  +---------------------+
  |  |
  |  sessionArea  |
  |  |
  +---------------------+
  |  |
  |  parameterArea  |
  |  |
  +---------------------+
  

In the TPM 2.0 reference implementation, the `ExecuteCommand` function in `ExecCommand.c` checks that the `authorizationSize` field of the `sessionArea` is at least `9` ([1]). After that, at [2], it calculates the start of the `parameterArea` (located right after the `sessionArea`) and saves it to the `parmBufferStart` variable. At `[3]` it calculates the size of the `parameterArea`, and saves it to the `parmBufferSize` variable. Then it calls `ParseSessionBuffer()` ([3]), passing `parmBufferStart` and `parmBufferSize` as parameters ([5], [6]).
  
  
  //  ExecuteCommand()
  //
  //  The function performs the following steps.
  //  a) Parses the command header from input buffer.
  //  b) Calls ParseHandleBuffer() to parse the handle area of the command.
  //  c) Validates that each of the handles references a loaded entity.
  //
  //  d) Calls ParseSessionBuffer() () to:
  //  1) unmarshal and parse the session area;
  //  2) check the authorizations; and
  //  3) when necessary, decrypt a parameter.
  
  [...]
  
  LIB_EXPORT void
  ExecuteCommand(
  unsigned  int  requestSize,  //  IN: command buffer size
  unsigned  char  *request,  //  IN: command buffer
  unsigned  int  *responseSize,  //  OUT: response buffer size
  unsigned  char  **response  //  OUT: response buffer
  )
  {
  [...]
  // Find out session buffer size.
  result = UINT32_Unmarshal(&authorizationSize, &buffer, &size);
  if(result != TPM_RC_SUCCESS)
  goto Cleanup;
  // Perform sanity check on the unmarshaled  value. If it is smaller than
  // the smallest possible session or larger  than the remaining size of
  // the command, then it is an error. NOTE:  This check could pass but the
  // session size could still be wrong. That  will be determined after the
  // sessions are unmarshaled.
  [1]  if(  authorizationSize < 9
  || authorizationSize > (UINT32) size)
  {
  result = TPM_RC_SIZE;
  goto Cleanup;
  }
  // The sessions, if any, follows authorizationSize.
  sessionBufferStart = buffer;
  // The parameters follow the session area.
  [2]  parmBufferStart = sessionBufferStart + authorizationSize;
  // Any data left over after removing the authorization sessions is
  // parameter data. If the command does not have parameters, then an
  // error will be returned if the remaining size is not zero. This is
  // checked later.
  [3]  parmBufferSize = size - authorizationSize;
  // The actions of ParseSessionBuffer() are described in the introduction.
  [4]  result = ParseSessionBuffer(commandCode,
  handleNum,
  handles,
  sessionBufferStart,
  authorizationSize,
  [5]  parmBufferStart,
  [6]  parmBufferSize);
  [...]
  

Function `ParseSessionBuffer` in `SessionProcess.c` parses the `sessionArea` of the command. If a session has the `Decrypt` attribute set ([1]), and if the command code allows for parameter encryption, then `ParseSessionBuffer` calls `CryptParameterDecryption()` ([2]), propagating the `parmBufferSize` ([3]) and `parmBufferStart` ([4]) parameters:
  
  
  //  ParseSessionBuffer()
  //
  //  This function is the entry function for command session processing. It iterates sessions in session area
  //  and reports if the required authorization has been properly provided. It also processes audit session and
  //  passes the information of encryption sessions to parameter encryption module.
  //
  //  Error Returns  Meaning
  //
  //  various  parsing failure or authorization failure
  //
  TPM_RC
  ParseSessionBuffer(
  TPM_CC  commandCode,  //  IN:  Command code
  UINT32  handleNum,  //  IN:  number of element in handle array
  TPM_HANDLE  handles[],  //  IN:  array of handle
  BYTE  *sessionBufferStart,  //  IN:  start of session buffer
  UINT32  sessionBufferSize,  //  IN:  size of session buffer
  BYTE  *parmBufferStart,  //  IN:  start of parameter buffer
  UINT32  parmBufferSize  //  IN:  size of parameter buffer
  )
  {
  [...]
  // Decrypt the first parameter if applicable. This should be the last operation
  // in session processing.
  // If the encrypt session is associated with a handle and the handle's
  // authValue is available, then authValue is concatenated with sessionAuth to
  // generate encryption key, no matter if the handle is the session bound entity
  // or not.
  [1]  if(s_decryptSessionIndex != UNDEFINED_INDEX)
  {
  // Get size of the leading size field in decrypt parameter
  if(  s_associatedHandles[s_decryptSessionIndex] != TPM_RH_UNASSIGNED
  && IsAuthValueAvailable(s_associatedHandles[s_decryptSessionIndex],
  commandCode,
  s_decryptSessionIndex)
  )
  {
  extraKey.b.size=
  EntityGetAuthValue(s_associatedHandles[s_decryptSessionIndex],
  &extraKey.t.buffer);
  }
  else
  {
  extraKey.b.size = 0;
  }
  size = DecryptSize(commandCode);
  [2]  result = CryptParameterDecryption(
  s_sessionHandles[s_decryptSessionIndex],
  &s_nonceCaller[s_decryptSessionIndex].b,
  [3]  parmBufferSize, (UINT16)size,
  &extraKey,
  [4]  parmBufferStart);
  

### Vulnerabilities in the CryptParameterDecryption function

Function `CryptParameterDecryption` in `CryptUtil.c` performs in-place decryption of an encrypted command parameter.
  
  
  //  10.2.9.9  CryptParameterDecryption()
  //
  //  This function does in-place decryption of a command parameter.
  //
  //  Error Returns  Meaning
  //
  //  TPM_RC_SIZE  The number of bytes in the input buffer is less than the number of
  //  bytes to be decrypted.
  //
  TPM_RC
  CryptParameterDecryption(
  TPM_HANDLE  handle,  //  IN: encrypted session handle
  TPM2B  *nonceCaller,  //  IN: nonce caller
  UINT32  bufferSize,  //  IN: size of parameter buffer
  UINT16  leadingSizeInByte,  //  IN: the size of the leading size field in
  //  byte
  TPM2B_AUTH  *extraKey,  //  IN: the authValue
  BYTE  *buffer  //  IN/OUT: parameter buffer to be decrypted
  )
  {
  SESSION  *session = SessionGet(handle); // encrypt session
  // The HMAC key is going to be the concatenation of the session key and any
  // additional key material (like the authValue). The size of both of these
  // is the size of the buffer which can contain a TPMT_HA.
  TPM2B_TYPE(HMAC_KEY, ( sizeof(extraKey->t.buffer)
  + sizeof(session->sessionKey.t.buffer)));
  TPM2B_HMAC_KEY  key;  // decryption key
  UINT32  cipherSize = 0; // size of cipher text
  pAssert(session->sessionKey.t.size + extraKey->t.size <= sizeof(key.t.buffer));
  // Retrieve encrypted data size.
  if(leadingSizeInByte == 2)
  {
  // The first two bytes of the buffer are the size of the
  // data to be decrypted
  [1]  cipherSize = (UINT32)BYTE_ARRAY_TO_UINT16(buffer);
  [2]  buffer = &buffer[2];  // advance the buffer
  }
  #ifdef TPM4B
  else if(leadingSizeInByte == 4)
  {
  // the leading size is four bytes so get the four byte size field
  cipherSize = BYTE_ARRAY_TO_UINT32(buffer);
  buffer = &buffer[4];  //advance pointer
  }
  #endif
  else
  {
  pAssert(FALSE);
  }
  [3] if(cipherSize > bufferSize)
  return TPM_RC_SIZE;
  // Compute decryption key by concatenating sessionAuth with extra input key
  MemoryCopy2B(&key.b, &session->sessionKey.b, sizeof(key.t.buffer));
  MemoryConcat2B(&key.b, &extraKey->b, sizeof(key.t.buffer));
  if(session->symmetric.algorithm == TPM_ALG_XOR)
  // XOR parameter decryption formulation:
  //  XOR(parameter, hash, sessionAuth, nonceNewer, nonceOlder)
  // Call XOR obfuscation function
  [4]  CryptXORObfuscation(session->authHashAlg, &key.b, nonceCaller,
  &(session->nonceTPM.b), cipherSize, buffer);
  else
  // Assume that it is one of the symmetric block ciphers.
  [5]  ParmDecryptSym(session->symmetric.algorithm, session->authHashAlg,
  session->symmetric.keyBits.sym,
  &key.b, nonceCaller, &session->nonceTPM.b,
  cipherSize, buffer);
  return TPM_RC_SUCCESS;
  }
  

**Two security issues arise in this function** :

  * **Bug #1 - OOB read** ([CVE-2023-1018](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1018)): At [1], the function uses the `BYTE_ARRAY_TO_UINT16` macro to read a 16-bit field (`cipherSize`) from the buffer pointed by `parmBufferStart` without checking if there's any parameter data past the session area. The only length check was performed earlier in function `ExecuteCommand`, but that check only verified that the `sessionArea` of the command is at least 9 bytes in size. As a result, if a malformed command doesn't contain a `parameterArea` past the `sessionArea`, it will trigger an **out-of-bounds memory read** , making the TPM access memory past the end of the command.

Note that the `BYTE_ARRAY_TO_UINT16` macro doesn't perform any bounds check:
  
  
  #define BYTE_ARRAY_TO_UINT16(b)  (UINT16)( ((b)[0] << 8) \
  + (b)[1])
  

The `UINT16_Unmarshal` function should have been used instead, which performs proper size checks before reading from a given buffer.

  * **Bug #2 - OOB write** ([CVE-2023-1017](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-1017)): If a proper `parameterArea` is provided (avoiding bug #1), the first two bytes of the `parameterArea` are interpreted as the size of the data to be decrypted (`cipherSize` variable at [1]). Right after reading `cipherSize`, at [2], the `buffer` pointer is advanced by 2. At [3] there's a sanity check (if the `cipherSize` value is greater than the actual buffer size, then it bails out), but there's a problem here: after reading the `cipherSize` 16-bit field and advancing the `buffer` pointer by 2, the function forgets to subtract 2 from `bufferSize`, to account for the two bytes that were already processed. Therefore, it is possible to successfully pass the sanity check at [3] with a `cipherSize` value that is, in fact, larger by 2 than the actual size of the remaining data. As a consequence, when either `CryptXORObfuscation()` or `ParmDecryptSym()` functions are called (at [4] and [5], respectively) to actually decrypt the data in the `parameterArea` following the `cipherSize` field, the TPM ends up writing 2 bytes past the end of the buffer, resulting in an **out-of-bounds write**.

An OOB write of just 2 bytes may not seem like a very powerful primitive at first, but remember that last year our colleagues Damiano Melotti and Maxime Rossi Bellom managed to [obtain code execution on Google's Titan M chip](https://blog.quarkslab.com/attacking-titan-m-with-only-one-byte.html) with an OOB write of a single byte with value `0x01`.

## Impact

1) OOB read: function `CryptParameterDecryption` in `CryptUtil.c` can read 2 bytes past the end of the received TPM command. If an affected TPM doesn't zero out the command buffer between received commands, it can result in the affected function reading whatever 16-bit value was already there from the previous command. This is dependent on the implementation: for example, VMware doesn't clear out the command buffer between requests, so the OOB read can access whatever value is already there from the previous command; on the contrary, Hyper-V's virtual TPM pads the unused bytes in the command buffer with zeros every time it receives a request, so the OOB access ends up reading just zeros.

2) OOB write: functions `CryptXORObfuscation`/`ParmDecryptSym` in `CryptUtil.c` (called from `CryptParameterDecryption`) can write 2 bytes past the end of the command buffer, resulting in memory corruption.

This second bug is definitely the most interesting one. The chances of being able to overwrite something useful depend on how each implementation allocates the buffer that receives TPM commands. As an example:

  * VMware uses an oversized buffer of size 0x10000, way bigger than the usual maximum TPM command size of 0x1000 bytes;
  * Hyper-V uses a static variable of size 0x1000 as the command buffer;
  * SWTPM uses `malloc()` to allocate a command buffer of size 0x1008 (8 bytes for a `send command prefix` that can be used to modify the `locality`, plus 0x1000 bytes for the maximum TPM command size).

Therefore, the chances of having something useful adjacent to the command buffer that we can overwrite with the OOB write are really implementation-dependent. All the three virtual TPMs mentioned above use a completely different approach for allocating the command buffer. In a similar way, the likeliness of having something useful to overwrite located right after the command buffer in the firmware of a given hardware TPM depends entirely on how that specific hardware vendor allocates the buffer that holds incoming commands.

## Triggering the bugs

In order to reproduce any of the 2 bugs described above, it is necessary to send 2 commands to the target TPM. In both cases, the first command must be a `TPM2_StartAuthSession` command, to start an authorization session. For simplicity, we can specify `TPM_ALG_XOR` as the symmetric algorithm to be used. As a result, we get a TPM response containing a _session handle_.

After that, we need to send a command that supports parameter encryption. We used `TPM2_CreatePrimary`, although a few other commands should probably work as well. We pass the _session handle_ obtained in the previous step in the `sessionArea` of the `TPM2_CreatePrimary` command, and we set the `Decrypt` flag in the `sessionAttributes` field. Then:

  * To reproduce bug #1 (OOB read), we send the `TPM2_CreatePrimary` command with a minimal valid `sessionArea`, and no data after it, i.e. with a missing `parameterArea`.
  * To reproduce bug #2 (OOB write), we send the `TPM2_CreatePrimary` command with its total size equal to the maximum supported TPM command size (`0x1000` bytes). In this case we do include a `parameterArea`, with the `cipherSize` field set to `0xfe5` (`0x1000 - sizeof(command_base_header) - sizeof(handleArea) - sizeof(sessionArea)`), followed by `0xfe3` bytes with any value (filling the place of the encrypted parameter) to complete the `0x1000` bytes of the whole `TPM2_CreatePrimary` command.

## Proof-of-Concept

You can [download here](resources/2022-12-05_tpm_vulns/tpm-vulns-poc.zip) a Proof-of-Concept to reproduce both vulnerabilities. The `.zip` file contains a Python version of the PoC, meant to be run on Linux systems, and a C version in case you intend to run it from a Windows machine.

## Conclusions

We discovered two security issues in the code of the TPM 2.0 reference implementation: an out-of-bounds read and an out-of-bounds write. As a result, every TPM (either software or hardware implementations) whose firmware is based on the reference code published by the Trusted Computing Group is expected to be affected.

Interestingly, although all affected TPMs share the exact same vulnerable function, which stems from the reference implementation code, the likeliness of successful exploitation depends on how the command buffer is implemented, and that part is left to each implementation. From what we saw, everyone seems to handle it in a different way: some clear out the command buffer between received requests, but others don't; some allocate the command buffer in the heap via `malloc()`, while others use a global variable for it.

We were able to verify that these vulnerabilities are present in the software TPMs included in major desktop virtualization solutions such as VMware Workstation, Microsoft Hyper-V and Qemu. Virtual TPMs available in the biggest cloud computing providers were also likely affected. For instance, Google Cloud uses code published by IBM automatically extracted from the TCG reference implementation, and we verified that the bugs were present in the code provided by IBM. In the case of Microsoft Azure, we already mentioned that Hyper-V on Windows 10 is affected, and since the Azure hypervisor is based on Hyper-V, we expect these two vulnerabilities to be present on Microsoft's cloud platform as well.

Finally, we expect most TPM hardware vendors to be affected too. The lack of a debugging setup to get visibility on what's going on in the TPM firmware at runtime makes it harder to confirm the presence of the vulnerabilities in a physical chip. Static analysis could be an alternative to assess whether a hardware TPM is vulnerable or not, but in the few TPM firmware updates we managed to get our hands on were encrypted.

## Acknowledgments

I'd like to thank Iván Arce, for the lot of valuable inputs and ideas he provided while discussing these bugs, as well as for taking care of handling such a complicated disclosure process with so many parties involved.

## Disclosure timeline

This timeline is not exhaustive and only lists events that we deemed relevant to the disclosure process.

  * **2022-11-24** Quarkslab sent the vulnerability report to VMWare.
  * **2022-11-24** Quarkslab sent the vulnerability report and PoC to Microsoft.
  * **2022-11-24** VMWare acknowledged the report.
  * **2022-11-25** Quarkslab notified CERT/CC of vulns in TCG TPM2 reference implementation, and opened a case in the VINCE portal. The vulnerabilities are tracked as VU#782720.1 and VU#782720.2.
  * **2022-11-28** Quarkslab notified CERT-FR of vulns in TCG TPM2 reference implementation.
  * **2022-11-28** CERT-FR, CERT/CC and Google acknowledged the report.
  * **2022-11-28** Quarkslab filed the vulnerability report in Google's security issue tracker stating that since their virtual TPM (vTPM) for Google Cloud Platform Shielded VMs [uses the reference implementation](https://cloud.google.com/blog/products/identity-security/virtual-trusted-platform-module-for-shielded-vms-security-in-plaintext), it is likely vulnerable.
  * **2022-11-28** CERT/CC asked if a date is set for disclosure of the bugs.
  * **2022-11-28** Quarkslab informed CERT/CC, VMWare and Google that the disclosure date was set to February 28th, 2023.
  * **2022-11-28** Google requested a Proof-of-Concept program for Linux.
  * **2022-11-28** Quarkslab sent Linux PoC to Google.
  * **2022-11-29** Quarkslab sent the vulnerability report to STMicroelectronics, an automated acknowledgement was received.
  * **2022-11-29** CERT/CC communicated to all vendors that it reserved two CVE IDs to identify the vulnerabilities.
  * **2022-11-29** Google asked if the report was sent to the Trusted Computing Group and if the vulnerability is under a coordinated embargo, as it wanted to push a fix to public code and executables.
  * **2022-11-29** Microsoft told Quarkslab that the report met their criteria for security servicing.
  * **2022-11-29** Quarkslab told Google that the disclosure date was set to February 28th, 2023 to let other vendors work on fixes, as it is likely that vendors of TPM hardware will require more time to release fixed firmware, that CERT/CC has contacted the TCG and to discuss disclosure with other vendor on CERT's VINCE portal. 
  * **2022-11-29** Cisco indicated that it started tracking the report internally.
  * **2022-12-02** Quarkslab noticed that more than 1600 vendors (up from 43 the prior day) had access to the vulnerability report on the VINCE portal and asked CERT/CC if it was a mistake or as intended.
  * **2022-12-02** CERT/CC clarified that expanding access to all registered vendors was as intended because several PC OEM and hardware vendors expressed interest in reaching out to other vendors up and down their supply chain.
  * **2022-12-02** Quarkslab told CERT/CC that the probability of information about the vulnerabilities being leaked is now considered significantly higher, and they should make preparations for that scenario.
  * **2022-12-02** Aruba Networks asked if there was a PoC program for Linux, Quarkslab provided all parties with a PoC in Python that uses `/dev/tpm0` to communicate with the TPM.
  * **2022-12-02** Intel indicated that it was investigating the report.
  * **2022-12-02** Fujistu PSIRT asked if Quarkslab analyzed TPM chips, Quarkslab replied that hardware TPMs were not analyzed due to lack of debugging or monitoring capabilities to determine what is running inside of them to find out if the bugs are triggered.
  * **2022-12-04** Nuvoton indicated that _current_ versions of their TPM chip firmware are not affected.
  * **2022-12-05** Trusted Computing Group VRT indicated that it was tracking the issue and coordinating triage with TPM Group co-chairs.
  * **2022-12-05** SUSE Linux identified `libtpms` as affected and asked if the maintainers were notified.
  * **2022-12-05** Quarkslab replied to SUSE Linux saying that it had not notified the `libtpms` maintainers and deferred to CERT/CC for coordination with them.
  * **2022-12-05** CERT/CC indicated that it had notified the IBM security group, which owns the vulnerable code.
  * **2022-12-05** Google notified Quarkslab that they've shared the PoC internally, forwarded comments about disclosure to the appropriate team and were in contact with Trusted Computing Group and would coordinate with them as appropriate.
  * **2022-12-05** Quarkslab asked Google if it had an estimated date for the rollout of fixes, and if it planned to issue fixes for the vTPM code in GCP only or also to any externally visible code.
  * **2022-12-05** The TCG notified all vendors that their Vulnerability Response Team (VRT) was engaged on the issue and reached out to the TPM Group co-chairs for triaging the report and would provide actionable information when available.
  * **2022-12-05** A CERT notified all parties that information about the vulnerabilities was publicly available on the issue tracker of a China-based Linux distribution.
  * **2022-12-06** CERT/CC notified all parties that upon their request the China-based Linux distribution had removed public access to the issues leaking the vulnerabilities. The coordinated disclosure date remains February 28th, 2023 and CERT/CC reminded everyone not to disclosure the issues publicly and to communicate the private nature of the report to any third parties that may receive the information.
  * **2022-12-07** Conference call between CERT/CC and Quarkslab to discuss how to proceed in light of the leak, both parties agree to not modify the planned disclosure date and try to speed up the vendor's processes to release fixes. CERT/CC requested permission to share the PoC programs with the US DHS CISA Threats team. Quarkslab granted permission.
  * **2022-12-07** Microsoft asked Quarkslab for additional information to reproduce the bugs.
  * **2022-12-08** CERT-JP said it had notified multiple vendors in Japan making them aware of the embargo date.
  * **2022-12-09** Quarkslab provided a new version of the PoC programs for Linux and Windows on CERT/CC's VINCE portal.
  * **2022-12-12** Quarkslab asked Google for an update and estimated date to release fixes.
  * **2022-12-13** Crestron Electronics asked if an output of `DeviceIOControl error 87 (Invalid Parameter)` of the Windows PoC indicates that the TPM is not vulnerable. Quarkslab replied that the error message revealed a bug in the PoC(!) that will be fixed shortly, and that determining if a given TPM chip is vulnerable or not without any log or debugging capabilities is difficult and without source code access it is only possible to do it by reverse engineering firmware which is a very time-consuming effort.
  * **2022-12-13** Siemens asked if the vulnerabilities were present in previous versions of TCG's TPM and if implementations of older versions are also affected. Quarkslab explained that the vulnerabilities were found in the code included in the TPM2.0 specification document and that they are present in all of IBM's `ibmswtpm2` TPM2.0 [reference implementation releases](https://sourceforge.net/projects/ibmswtpm2/files/) dating back to at least March 21st, 2017. Therefore any implementation of TPM2.0 based on them is likely affected. Quarkslab did not check any TPM1.2 implementation.
  * **2022-12-14** Infineon stated that Infineon TPM chips are NOT affected by the reported issues.
  * **2022-12-14** Microsoft reiterated their request for additional information to reproduce the bugs.
  * **2022-12-16** Quarkslab updated the PoC programs for Linux and Windows fixing a bug that prevented testing certain TPMs.
  * **2022-12-16** Quarkslab asked Google for an update and answers to the questions sent previously on Dec. 5th and 12th. Also notified Google that it found out that a fix for the vulns we reported [was committed to the Chromium OS TPM2 code](https://chromium.googlesource.com/chromiumos/third_party/tpm2/+/3b87ed233acb4c76c27872e1ac0b74dc032199f1) on December 1st, and that since the repository is publicly visible, Quarkslab considered knowledge about the existence of the bugs to be public now. Asked Google for their plan to roll out these fixes to supported devices.
  * **2022-12-16** Quarkslab provided Microsoft a detailed description of how to debug the vTPM in Hyper-V to reproduce the bugs.
  * **2022-12-16** Microsoft confirmed that it could reproduce the bugs. Quarkslab noted that they should coordinate disclosure with CERT/CC and the TCG.
  * **2022-12-18** Google said they were with the proposed February 28, 2023 embargo date, and that were working with TCG and CERT to resolve the issue, and would get back with an answer to the remaining question as soon as they have one.
  * **2022-12-19** Microsoft asked if it would be possible to coordinate disclosure for April 2023, to align with their security release of that month. Quarkslab replied that disclosure is being coordinated by CERT/CC, and that since other vendors are involved and a fix was already committed to a publicly available source code repository, it is more likely that the release of fixes and public disclosure will have to be accelerated rather than delayed. Suggested to discuss the matter with CERT/CC and other vendors.
  * **2022-12-23** Quarkslab updated the PoC programs for Linux and Windows to query and print the manufacturer strings of the TPM implementation.
  * **2022-12-26** Quarkslab updated the PoC programs for Linux and Windows to query and print the firmware version of the TPM implementation, also provided the output of a run of the PoC identifying a vulnerable chip.
  * **2023-01-03** Google VRP informed that the bugs do not meet criteria for a reward, as they don't affect Google products but nonetheless passed the report to Chrome VRP for further evaluation.
  * **2023-01-05** Google followed up indicating that while they consider the code changes to be public, they do not consider them to break embargo per discussion with CERT and TCG. Also that they cannot provide an answer to the question about their plan to roll out fixes to their devices.
  * **2023-01-09** VMware asked if the disclosure date could be extended until the end of March or April.
  * **2023-01-16** Quarkslab replied to VMware stating that the vulnerabilities should be considered public knowledge and the disclosure process involved multiple vendors as well as CERT and TCG, so it would be difficult to move it but they should discuss with them.
  * **2023-01-16** Quarkslab asked Google VRP to clarify if the bugs are eligible because Google products aren't affected, are affected but not exploitable, or are in a third-party component. Noted that the fix committed in the Chromium OS repository seemed to indicate that at least one product was affected.
  * **2023-01-17** Google replied that the issue was sent to the VRP panel for reconsideration.
  * **2023-01-17** Chrome VRP informed that they were considering the issue. Gave access to the corresponding entry in their (separate) bug tracking system.
  * **2023-01-17** Quarkslab gets access to the issue in the Chromium bug tracker. The entry, dated January 4th, indicated that the bugs were reported externally, were fixed, and their analysis deemed them not exploitable.
  * **2023-02-01** STMicroelectronics reported that their products are not affected...
  * **2023-02-02** Chrome VRP awards 20K USD for the bugs.
  * **2023-02-08** Call with CERT to synchronize status and discuss further steps. Quarkslab agrees to publish technical details on March 14th, CERT and TCG will publish their security advisories and errata on February 28th.
  * **2023-02-15** Microsoft informed that they will try to accelerate the release of the patches, and asked if they could preview the blog post to be published on March 14th.
  * **2023-02-15** Quarkslab replied to Microsoft providing an updated PoC and agreed to send a draft of the blog post when it is ready.
  * **2023-02-28** CERT/CC published their [vulnerability note](https://kb.cert.org/vuls/id/782720).
  * **2023-02-28** Trusted Computing Group published their [security advisory](https://trustedcomputinggroup.org/wp-content/uploads/TCGVRT0007-Advisory-FINAL.pdf) and [errata](https://trustedcomputinggroup.org/wp-content/uploads/TPM-2.0-Library-Spec-v1.59-Errata-v1.4_pub.pdf).
  * **2023-03-06** Nuvoton published a [security advisory](https://www.nuvoton.com/support/security/security-advisories/sa-003/).
  * **2023-03-06** Lenovo published a [security advisory](https://support.lenovo.com/us/en/product_security/LEN-118320).
  * **2023-03-06** libtpms [added tests cases](https://github.com/stefanberger/libtpms/commit/6e95c68503964d22d21704bdf99cd19dcb8748b1) for the vulnerabilities.
  * **2023-03-09** Microsoft committed a [fix](https://github.com/microsoft/ms-tpm-20-ref/commit/9bdd9f0aaba5e54b3c314cfff02cf532281a067e) to their open source reference implementation.
  * **2023-03-10** Draft of the blog post sent to Microsoft.
  * **2023-03-13** Microsoft replied with their impact assessment for Azure servers.
  * **2023-03-14** This blog post is published.

* * *

If you would like to learn more about our security audits and explore how we can help you, [get in touch with us](https://content.quarkslab.com/talk-to-our-experts-blog)!
