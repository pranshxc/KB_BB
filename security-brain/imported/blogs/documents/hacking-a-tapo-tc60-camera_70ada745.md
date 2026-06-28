---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-08-23_hacking-a-tapo-tc60-camera.md
original_filename: 2023-08-23_hacking-a-tapo-tc60-camera.md
title: Hacking a Tapo TC60 Camera
category: documents
detected_topics:
- mobile-security
- sso
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- mobile-security
- sso
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 70ada745cf169b00203f9925791b789bf75cf8ea6495b14b72bfe2c8bbb3d3c8
text_sha256: c137d0469e1cb5f8939c77849dccda3bc794ee3785b1ac448f6cb2fe434f7123
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking a Tapo TC60 Camera

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-08-23_hacking-a-tapo-tc60-camera.md
- Source Type: markdown
- Detected Topics: mobile-security, sso, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `70ada745cf169b00203f9925791b789bf75cf8ea6495b14b72bfe2c8bbb3d3c8`
- Text SHA256: `c137d0469e1cb5f8939c77849dccda3bc794ee3785b1ac448f6cb2fe434f7123`


## Content

---
title: "Hacking a Tapo TC60 Camera"
url: "https://medium.com/@two06/hacking-a-tapo-tc60-camera-e6ce7ca6cad1"
authors: ["James (@two06)"]
programs: ["Tapo"]
bugs: ["IoT", "Hardware hacking", "Reverse engineering"]
publication_date: "2023-08-23"
added_date: "2023-09-05"
source: "pentester.land/writeups.json"
original_index: 835
scraped_via: "browseros"
---

# Hacking a Tapo TC60 Camera

Hacking a Tapo TC60 Camera
James
Follow
17 min read
·
Aug 23, 2023

154

5

A little while ago, I spotted a Tapo TC60 “Smart Security Camera” on sale at Amazon UK. After my adventures with a smart lockbox and an old safe lock, I wanted to try hacking something with a few more features. This is what happened.

Press enter or click to view image in full size

Inside the box, we get the usual collection of manuals, a power adapter, and the camera itself. The camera was much smaller than I expected, with no obvious way into the case.

Press enter or click to view image in full size

I powered it on, and set it up on the Tapo app. I probably should have captured the setup traffic in BurpSuite, but I’m more interested in the hardware for this post.

Press enter or click to view image in full size

With the setup complete, I started taking the camera to bits. First removing the stand, then finding a disassembly video of the TC100 on YouTube, which showed how to get into the main camera body.

Press enter or click to view image in full size

There are 4 clips holding the front of the case on, which releases when another of the IFixIt picks are inserted. This gives us access to the main board.

Press enter or click to view image in full size

One of the first things to do when approaching something like this is try and identify the chips on the board, as well as any UART/JTAG interfaces. Identifying the chips will give us a high-level understanding of what the device is doing, and help us understand where we might find interesting data. This board has a few obvious components.

Press enter or click to view image in full size

The big chip is an Ingenic T31, a system on chip video processor. There is very little information on this chip available, but we know it’s going to be handing video for us.

There is also a RTL8188FTV, a WiFi and network USB chip, designed for use in devices including IP-cameras. There are some other ICs, including an audio amplifier, and the usual selection of passive components. Crucially, there is no memory chip on this side of the board.

Turning the board over, we can see the camera assembly, which can be removed. Taking this off reveals the sensor and another IC.

Press enter or click to view image in full size

This is a XMC 25QH64C, a serial flash memory chip. This is almost certainly where the firmware for this device is stored.

Examining the board also reveals some pads, which look suspiciously like a UART interface, just above the T31 chip.

A quick check with a multi-meter reveals one of the pins is tied to ground, one likely to Vcc, leaving two unidentified pins. Probing these pins with the oscilloscope reveals what looks like data going out.

Press enter or click to view image in full size

Connecting up the logic analyser verifies that this is indeed a UART interface. We can see the U-Boot logs being displayed when the power is connected.

Press enter or click to view image in full size
Press enter or click to view image in full size

Now we know which pin is TX, we can connect up the Tigard board and try and talk to the device.

Scrolling through the console data, there are no obvious ways to interrupt the boot sequence.

At this point I started researching prior work on this device. While I couldn’t find anything on the TC60, I did find some information on the TC200 and TC100. It seems like the TC100 is essentially the same device, so a lot of the information could be useful.

The most useful source of information was this blog post, which also links to a GitHub project related to the TC200.

These projects contain some useful information, such as the escape sequence for the U-Boot loader, allowing us to interrupt the boot sequence and drop into a root shell.

------Firmware check pass!-----
Autobooting in 1 seconds
isvp_t31# 
isvp_t31# slp
Unknown command 'slp' - try 'help'
isvp_t31# setenv bootargs console=ttyS1,115200n8 mem=45M@0x0 rmem=19M@0x2d00000 root=/dev/mtdblock6 rootfstype=squashfs spdev=/dev/mtdblock7 noinitrd init=/bin/sh
isvp_t31# 
isvp_t31# printenv
baudrate=115200
bootargs=console=ttyS1,115200n8 mem=45M@0x0 rmem=19M@0x2d00000 root=/dev/mtdblock6 rootfstype=squashfs spdev=/dev/mtdblock7 noinitrd init=/bin/sh
bootcmd=sf probe;sf read 0x80700000 0x80200 0x175000; bootm 0x80700000
bootdelay=1
ethaddr=00:d0:d0:00:95:27
gatewayip=193.169.4.1
ipaddr=193.169.4.81
loads_echo=1
netmask=255.255.255.0
serverip=193.169.4.2
stderr=serial
stdin=serial
stdout=serial

Environment size: 437/16380 bytes
isvp_t31# sf probe;sf read 0x80700000 0x80200 0x175000; bootm 0x80700000
<snipped>

BusyBox v1.19.4 (2022-09-30 05:46:09 CST) built-in shell (ash)
Enter 'help' for a list of built-in commands.

/bin/sh: can't access tty; job control turned off
/ # ls
bin  etc  mnt  proc  root  sp_rom  tmp  var
dev  lib  overlay  rom  sbin  sys  usr  www
/ # help
Built-in commands:
------------------
  . : [ [[ alias bg break cd chdir command continue echo eval exec
  exit export false fg getopts hash help jobs kill let local printf
  pwd read readonly return set shift source test times trap true
  type ulimit umask unalias unset wait

/ # id
uid=0(root) gid=0(root)

From here, we need to mount the /proc directory, which gets us access to some of the usual linux tools. We can also cat out the /etc/passwd file, which gives us the hash for the root user.

root:$1$Xr8fF4xx$BFl2tPv719kYGwDH5TFrm.:0:0:root:/root:/bin/ash
nobody:*:65534:65534:nobody:/var:/bin/false
admin:*:500:500:admin:/var:/bin/false
guest:*:500:500:guest:/var:/bin/false
ftp:*:55:55:ftp:/home/ftp:/bin/false
/ # cat /etc/shadow
root:x:0:0:99999:7:::
daemon:*:0:0:99999:7:::
ftp:*:0:0:99999:7:::
network:*:0:0:99999:7:::
nobody:*:0:0:99999:7:::

My research into prior work on this device also turned up an academic paper, talking about some potential risks around poorly secured IoT devices. This included a hypothetical scenario where an owner of a TC100 camera leaves it unattended during a power cut (so the camera doesn’t record being tampered with), and a house-mate uses this opportunity to extract the device firmware. This is then analysed off-line, eventually granting them access to the live feed from the device (assuming they are on the same network as the device). We will try and re-create this attack.

The camera model used in the paper has its flash chip located in a different position on the board, allowing easy access with a SOP8 clip. The authors were also able to bridge a connection on the board to put the main IC in reset mode. As we covered briefly in a previous post, we need to stop the main IC talking to the flash memory while we dump it, otherwise it will skew our results. In this device, the flash chip and the main IC share the same power rails. Supplying power to the chip while dumping its memory will also cause the main IC to power on. In our case, the main IC is on the opposite side of the board to the flash chip. The flash chip is also located under the camera lens assembly. While it would still be possible to extract the firmware this way, it would be much more complicated to do in the hypothetical scenario of a malicious actor with limited time to access the device. We need another approach.

When looking to attack a device, it is useful to have access to the manufacturers firmware. While some credential material is likely configured by the user during setup, an analysis of the firmware on the device may well reveal default credentials or other weaknesses which we can exploit, without having to extract the firmware from a running device. Fortunately (or unfortunately, depending on your point of view), manufactures are becoming more aware of these attacks and are often not supplying firmware downloads on their website. TPLink (who make the Tapo cameras), are one such company. They do provide copies of the GPL code used in these devices, which have contained useful information in other models of camera (see the linked research above). In our case, there did not appear to be any useful information in these files. We need the factory firmware.

The TC60 has an “over the air” firmware update function. The camera likely reaches out to an update server and downloads the firmware image. The app also shows the current firmware version, and details of any pending updates, so it probably also talks out to an update server. As it’s much easier to intercept traffic between the app and the device, compared with trying to intercept traffic from the device itself, this is the path i tried first. After configuring my phone to proxy traffic through BurpSuite, I opened the Tapo app and clicked around. In the response body of one of the requests sent to the camera was a URL to download the firmware update.

Press enter or click to view image in full size

I downloaded the firmware and ran it through binwalk, with the -E flag. This shows the entropy of the file.

binwalk -E Tapo_TC60v4_en_1.3.7_Build_230627_Rel.41895n_up_boot-signed_1691484740866.bin

WARNING: Failed to import matplotlib module, visual entropy graphing will be disabled

DECIMAL  HEXADECIMAL  ENTROPY
--------------------------------------------------------------------------------
0  0x0  Rising entropy edge (0.994108)

This doesn’t look good. High entropy likely means the firmware is encrypted, which we can verify using binwalk to try and extract and data.

binwalk -e Tapo_TC60v4_en_1.3.7_Build_230627_Rel.41895n_up_boot-signed_1691484740866.bin

DECIMAL  HEXADECIMAL  DESCRIPTION
--------------------------------------------------------------------------------

As expected, binwalk isn’t able to extract any data. running strings over the file also yields no results. The firmware on the camera must contain the keys we need to decrypt the download, but that’s not much use if we can’t access them. Luckily, we have a UART shell.

As this device has an SD card slot, we can also dump the firmware via this shell. The “tapo 200 research project” blog has detailed instructions on how to extract the firmware. At a high level, we can mount the SD card, map the flash ram to files on disk and copy them into a flashdump.bin file. The full instructions are provided in the linked post, which I won’t recreate here.

Now, we can run binwalk over the extracted firmware, which gives us access to the file system contents.

❯ binwalk flashdump.bin

DECIMAL  HEXADECIMAL  DESCRIPTION
--------------------------------------------------------------------------------
15892  0x3E14  LZO compressed data
26624  0x6800  uImage header, header size: 64 bytes, header CRC: 0xA3F3CA56, created: 2022-09-29 21:36:29, image size: 155294 bytes, Data Address: 0x80100000, Entry Point: 0x0, data CRC: 0xCEE6C40F, OS: Firmware, CPU: MIPS, image type: Firmware Image, image name: "u-boot-lzo.img"
26688  0x6840  LZO compressed data
141029  0x226E5  CRC32 polynomial table, little endian
145193  0x23729  LZO compressed data
148629  0x24495  Android bootimg, kernel size: 0 bytes, kernel addr: 0x70657250, ramdisk size: 543519329 bytes, ramdisk addr: 0x6E72656B, product name: "mem boot start"
188181  0x2DF15  PEM certificate
188910  0x2E1EE  PEM certificate
190126  0x2E6AE  PEM certificate
191346  0x2EB72  PEM certificate
192538  0x2F01A  PEM certificate
196864  0x30100  gzip compressed data, from Unix, last modified: 2022-09-29 22:06:28
393216  0x60000  LZO compressed data
484818  0x765D2  CRC32 polynomial table, little endian
488822  0x77576  LZO compressed data
524800  0x80200  uImage header, header size: 64 bytes, header CRC: 0x1805EB61, created: 2022-09-29 22:06:13, image size: 1296787 bytes, Data Address: 0x80010000, Entry Point: 0x8031B470, data CRC: 0xD607E5B7, OS: Linux, CPU: MIPS, image type: OS Kernel Image, compression type: lzma, image name: "Linux-3.10.14__isvp_swan_1.0__"
524864  0x80240  LZMA compressed data, properties: 0x5D, dictionary size: 8388608 bytes, uncompressed size: -1 bytes
1823232  0x1BD200  Squashfs filesystem, little endian, version 4.0, compression:xz, size: 2405062 bytes, 647 inodes, blocksize: 131072 bytes, created: 2022-09-29 22:06:33
4456448  0x440000  Squashfs filesystem, little endian, version 4.0, compression:xz, size: 3053252 bytes, 162 inodes, blocksize: 131072 bytes, created: 2022-09-29 22:06:35
8404500  0x803E14  LZO compressed data
8415232  0x806800  uImage header, header size: 64 bytes, header CRC: 0xA3F3CA56, created: 2022-09-29 21:36:29, image size: 155294 bytes, Data Address: 0x80100000, Entry Point: 0x0, data CRC: 0xCEE6C40F, OS: Firmware, CPU: MIPS, image type: Firmware Image, image name: "u-boot-lzo.img"
8415296  0x806840  LZO compressed data
8529637  0x8226E5  CRC32 polynomial table, little endian
8533801  0x823729  LZO compressed data
8537237  0x824495  Android bootimg, kernel size: 0 bytes, kernel addr: 0x70657250, ramdisk size: 543519329 bytes, ramdisk addr: 0x6E72656B, product name: "mem boot start"
8576789  0x82DF15  PEM certificate
8577518  0x82E1EE  PEM certificate
8578734  0x82E6AE  PEM certificate
8579954  0x82EB72  PEM certificate
8581146  0x82F01A  PEM certificate
8585472  0x830100  gzip compressed data, from Unix, last modified: 2022-09-29 22:06:28
8781824  0x860000  LZO compressed data
8873426  0x8765D2  CRC32 polynomial table, little endian
8877430  0x877576  LZO compressed data
8913408  0x880200  uImage header, header size: 64 bytes, header CRC: 0x1805EB61, created: 2022-09-29 22:06:13, image size: 1296787 bytes, Data Address: 0x80010000, Entry Point: 0x8031B470, data CRC: 0xD607E5B7, OS: Linux, CPU: MIPS, image type: OS Kernel Image, compression type: lzma, image name: "Linux-3.10.14__isvp_swan_1.0__"
8913472  0x880240  LZMA compressed data, properties: 0x5D, dictionary size: 8388608 bytes, uncompressed size: -1 bytes
10211840  0x9BD200  Squashfs filesystem, little endian, version 4.0, compression:xz, size: 2405062 bytes, 647 inodes, blocksize: 131072 bytes, created: 2022-09-29 22:06:33
12845056  0xC40000  Squashfs filesystem, little endian, version 4.0, compression:xz, size: 3053252 bytes, 162 inodes, blocksize: 131072 bytes, created: 2022-09-29 22:06:35

Re-visiting the academic paper, we see that the authors followed the process outlined in the “tapo 200 research project” blog, namely, extracting the configuration data from the device and decrpyting offline. The configuration data is still encrypted on our device and, like the other devices, we can either decrypt the data manually, off-line, or there is a utility present on the device which allows it to be decrypted. We can verify this works, using the following steps via our UART shell.

Mount /proc
Mount /dev
Mount /tmp
run the uc_convert utility
mount -t proc none /proc
mount -t tmpfs tmpfs /dev -o mode=0755,size=512K
mount tmpfs /tmp -t tmpfs -o size=20633600,nosuid,nodev,mode=1777
mknod /dev/slp_flash_chrdev c 222 0
/bin/uc_convert -t 0

This creates a directory in /tmp, which contains the decrtypyed device configuration.

Get James’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In our hypothetical attack scenario, we could perform this step on the device, via our UART shell and exfiltrate the decrypted data either via terminal logs or writing to the SD card. We wouldn’t need to grab the firmware at all, which certainly helps for this device, where the flash chip is located under the camera lens assembly.

Press enter or click to view image in full size

However, as we can see, the “third_account” username and password values are blanked out. This differs from the device presented in the paper (where the authors were able to crack the hash for this account and use the credentials to access the video stream). So that’s it, game over, right? Not quite…

We have access to the device as root. Can we simply add an account under the third_account section and gain acccess to the video feed?

After some investigation, it turns out the answer is yes, with some caveats. Extracting the config using the uc_convert utility, we can find the user account details in /tmp/etc/uc_conf/user_management, as shown above.

The “root” account blob contains credentials configured when we set up the camera. The passwd field is a simple MD5 hash of the password. We can try and crack this, but that might take some time, if the user selected a strong password. The ciphertext blob is RSA encrypted, which we’ll cover shortly.

The third_account blob is, by default, disabled. The username and password values are set to “—-”. This account is used to allow access to the RTSP stream from the camera, and must be enabled via the mobile app. enabling this comes with some warnings:

Press enter or click to view image in full size

I initially assumed that only the username and password values were required to access the RTSP stream. I modified the config, adding a “backdoor” account with a known password hash (note that this needs to be uppercase, or it won’t work), wrote the config back to flash, rebooted the camera and attempted to access the RTSP stream from VLC. This gave me an authentication error.

After lots of experimenting, it turns out that the ciphertext value must also be set to match the username and password values. The mobile app uses the passwd value to validate the password when you perform a “change password” option on the RTSP account, but the RTSP steam uses the ciphertext value. I’m not a reverse engineer, however, we can verify that this is likely RSA encrypted data using binary ninja and ghidra.

If we throw the cet application (which is what this device uses for RTSP) into binary ninja cloud, and search for ‘ciphertext’, we get the following result:

Press enter or click to view image in full size

Looking at this function in more detail, we see it calls the following function after reading the ciphertext block in our config file:

int32_t $v0_14 = rsa_decrypt("oP4b0Q2dUvDXKwK9gLnBfVpxcHUDg4V2…", 0xac)

rsa_decrypt is an external reference to libdecrypter.so which we can find by grepping the firmware we dumped from the device earlier.

Opening this file with Ghidra, we can find the rsa_decrypt export and start our analysis from there.

Press enter or click to view image in full size

In the private_decrypt function, we can see the code loading an RSA key from somewhere, then doing a base64 decode and an RSA decrypt.

Press enter or click to view image in full size

I tried to figure out where the RSA key is loaded from, but I’m just not smart enough to figure out this decompiled code:

Press enter or click to view image in full size

Running strings over the file turns up some RSA keys, but I wasn’t able to figure out how to use them to decrypt the config file. I’m glossing over this step, as this post is long enough already, but you can run `strings libdecrypt.so` if you want to follow allong

I had a hunch that the decryption keys are hard-coded, and likely the same on each device. Not being smart enough to reverse the decryption code properly, I did the next best thing and ordered another device to test this theory.

I set up this second device on a new tapo account, performed the initial setup then took it apart and connected to the UART interface. Note that the second device as connected to the same WiFi network. I doubt TPLink are using that as the seed for an encryption key, but I’ve been wrong before.

With access to the uart console, I ran a simple python script to automate dumping the encrypted config. This is a modified version of the script persented in the c200 research project blog.

Press enter or click to view image in full size

From here, I connected via serial, opened the user_manage file in vi (yes, that’s handily supplied on the device), and overwrite the username, passwd and ciphertext values in the file. For the username and passwd, I used backdoor and the MD5 hash of Password206 . For the cipher text, I copied one generated on the original device, which was generated by setting the username and password via the mobile app.

I wrote the modified config back to flash, rebooted the camera and tried to connect to the RTSP stream with VLC:

Press enter or click to view image in full size

As we can see, the re-used ciphertext value was accepted, granting us access to the cameras video stream (thats the sensepeak mat on my bench, if you were wondering). Actually performing this attack took around 5 minutes, starting from an un-opened camera body to having access to the stream.

While we may not have re-created the exact attack presented in the paper, we’ve certainly achieved what we set out to do. As we are not dumping the flash ram, we are going to need to supply power to the device. This means we are no longer dependent on waiting for a random power cut to enable our attack. As we are interacting with the device with UART, we need to supply power, which will also enable video capture. You’ll have to use you imaginations to figure out how this could be done without being detected ;). While the steps taken to add the backdoor account have been discussed here, I’ve left out some steps and I’m choosing not to release the python code I used to backdoor the camera. You won’t be able to re-create this attack with the information in this post alone.

For completions sake, let’s see if we can get the off-line decryption vector working.

The prior work we are referencing goes into detail on how the decryption code works, including where the decryption key is located. The academic paper noted that the key in their device, a TC100, differed from the key in the blog post (a TC200). They found the key in the same location, and were able to decrypt their config data using the same technique. Let’s see if our device uses the same approach.

First, we load the uc_convert binary into binary ninja cloud.

Press enter or click to view image in full size

We’ve already established that I’m not a reverse engineer, but eventually I can figure out that this is parsing arguments.

This would probably end up looking something like this:

int main(int argc, char **argv)
{
  if(argc < 3)
  {
  showhhelp();
  return -1
  }
  while((c = getopt(argc, argv, "t:d:c")))
  {
  switch (c){
  case 'd':
  updateFWDescription(); //we dont care what this does
  break;
  case 't':
  int foo = atoi(optarg);
  break;
  case 'c':
  //do a thing
  break;
  default:
  return -1;
  }
}

At this point, i started to look for the other functions. The only other function which stood out was this one, which I quickly realised as beyond my ability to reverse engineer.

Press enter or click to view image in full size

Back to the drawing board.

The prior work we are referencing was able to locate the string used to derive the encryption key, which in their example was “C200 1.0”. The authors of the research paper found their key to be “C100 2.0”. In both cases this was the model number and firmware hardware version. Let’s just grep the firmware dump we have for our model number…

Press enter or click to view image in full size

This seems promising. Let’s try that in the hash function we have from the prior work.

Press enter or click to view image in full size

And after converting that from ASCII to hex, we can run the OpenSSL command:

openssl enc -d -des-ecb -nopad -K 3463666461643831 -in mtdblock3.bin -out test.bin`

If you’re wondering where the bin file here came from, I dumped it from the camera, using the SD card to exfiltrate it, in the same way as the full firmware dump, except I only dumped the “config” partition.

Press enter or click to view image in full size

And after extracting, we get our config data.

So, this model camera is using the same method to protect its config data as the C100 and C200, all be it with a different key. It’s worth noting that I’m really standing on the shoulders of giants here, there’s no way I’d have figured out that encryption method myself.

Let’s wrap this up. To recap, we’ve seen how with physical access to one of these cameras we can dump the firmware. We can also connect to the UART console, access a root shell and add a backdoor account to the camera to allow surupticious access to the video stream. This backdoor accoount is not immidiatly obvious in the app, and would likely not be detected unless the user wanted to enable RSTP access. We’d need physical access to the device, and to be on the same network to actually view the feed, so the potential for attack here is quite low. We’ve also seen how we can decrypt the device config offline, using methods presented in other research. Finally, we learnt that I really have no idea how Ghidra works.
