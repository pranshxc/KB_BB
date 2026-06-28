---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-24_hacking-my-smart-toothbrush.md
original_filename: 2023-05-24_hacking-my-smart-toothbrush.md
title: Hacking my “smart” toothbrush
category: documents
detected_topics:
- command-injection
- otp
- automation-abuse
- api-security
- cloud-security
- supply-chain
tags:
- imported
- documents
- command-injection
- otp
- automation-abuse
- api-security
- cloud-security
- supply-chain
language: en
raw_sha256: 3dcdbd0831b2a89a93ca760a49be98a952153918afacbc44b1b7335472277a7d
text_sha256: d462c81b43200e22a737dcce683692f5b1e592a4bc1523edfa303d97f9a1cd4f
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking my “smart” toothbrush

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-24_hacking-my-smart-toothbrush.md
- Source Type: markdown
- Detected Topics: command-injection, otp, automation-abuse, api-security, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `3dcdbd0831b2a89a93ca760a49be98a952153918afacbc44b1b7335472277a7d`
- Text SHA256: `d462c81b43200e22a737dcce683692f5b1e592a4bc1523edfa303d97f9a1cd4f`


## Content

---
title: "Hacking my “smart” toothbrush"
page_title: "Hacking my “smart” toothbrush - The Twenty Percent"
url: "https://kuenzi.dev/toothbrush/"
final_url: "https://kuenzi.dev/toothbrush/"
authors: ["Cyrill Künzi"]
bugs: ["IoT", "Reverse engineering", "NFC"]
publication_date: "2023-05-24"
added_date: "2023-06-05"
source: "pentester.land/writeups.json"
original_index: 1118
---

# Hacking my “smart” toothbrush 

__7 minute read

After buying a new [Philips Sonicare](https://www.philips.ch/c-p/HX6851_53/sonicare-protectiveclean-5100-elektrische-schallzahnbuerste) toothbrush I was surprised to see that it reacts to the insertion of a brush head by blinking an LED. A quick online search reveals that the head communicates with the toothbrush handle to remind you when it’s time to buy a new one.

![0](/assets/images/toothbrush/smart.png)  
_From the Philips product page: seems to be REALLY smart!_

## Reverse Engineering

Looking at the base of the head shows that it contains an antenna and a tiny black box that is presumably an IC. The next hint can be found in the manual where it says that: “Radio Equipment in this product operates at 13.56 MHz”, which would indicate that it is an [NFC tag](https://en.wikipedia.org/wiki/Near-field_communication). And indeed when holding the brush head to my phone it opens a link to a product page: <https://www.usa.philips.com/c-m-pe/toothbrush-heads>.

[ ![Brush head](/assets/images/toothbrush/brush_head.jpg) ](/assets/images/toothbrush/brush_head.jpg "Brush head") [ ![Antenna](/assets/images/toothbrush/nfc_chip.jpg) ](/assets/images/toothbrush/nfc_chip.jpg "Antenna")

Using the [NFC Tools](https://play.google.com/store/apps/details?id=com.wakdev.nfctools.pro) app we can learn a lot about this tag:

![](/assets/images/toothbrush/nfc_info.png)

  * It is an [NTAG213](https://www.nxp.com/products/rfid-nfc/nfc-hf/ntag-for-tags-labels/ntag-213-215-216-nfc-forum-type-2-tag-compliant-ic-with-144-504-888-bytes-user-memory:NTAG213_215_216)
  * It uses NfcA
  * It is password protected
  * We can see the link to the Philips webpage

Also using NFC Tools, the memory and memory access conditions can be read:

Address | Data | Type | Access  
---|---|---|---  
0x00 | 04:EC:FC:9C | UID0-UID2/BCC0 | Read-Only  
0x01 | A2:94:10:90 | UID3-UDI6 | Read-Only  
0x02 | B6:48:FF:FF | BCC1/INT./LOCK0-LOCK1 | Read-Only  
0x03 | E1:10:12:00 | OTP0-OTP3 | Read-Only  
0x04 | 03:20:D1:01 | DATA | Read-Only  
0x05 | 1C:55:02:70 | DATA | Read-Only  
0x06 | 68:69:6C:69 | DATA | Read-Only  
0x07 | 70:73:2E:63 | DATA | Read-Only  
0x08 | 6F:6D:2F:6E | DATA | Read-Only  
0x09 | 66:63:62:72 | DATA | Read-Only  
0x0A | 75:73:68:68 | DATA | Read-Only  
0x0B | 65:61:64:74 | DATA | Read-Only  
0x0C | 61:70:FE:00 | DATA | Read-Only  
0x0D… | 00:00:00:00 | DATA | Read-Only  
0x1F | 00:01:07:00 | DATA | Readable, write protected by PW  
0x20 | 00:00:00:02 | DATA | Read-Only  
0x21 | 60:54:32:32 | DATA | Read-Only  
0x22 | 31:32:31:34 | DATA | Read-Only  
0x23 | 20:31:32:4B | DATA | Read-Only  
0x24 | B3:02:02:00 | DATA | Readable,write protected by PW  
0x25 | 00:00:00:00 | DATA | Readable,write protected by PW  
0x26 | 00:00:00:00 | DATA | Readable,write protected by PW  
0x27 | 00:00:00:01 | DATA | Readable,write protected by PW  
0x28 | 00:03:30:BD | LOCK2 - LOCK4 | Readable,write protected by PW  
0x29 | 04:00:00:10 | CFG 0 | Read-Only  
0x2A | 43:00:00:00 | CFG 1 | Read-Only  
0x2B | 00:00:00:00 | PWD0-PWD3 | Write-Only  
0x2C | 00:00:00:00 | PACK0-PACK1 | Write-Only  
  
I repeated this process for one black and two white [W DiamondClean](https://www.usa.philips.com/c-p/HX6062_65/sonicare-w-diamondclean-standard-sonic-toothbrush-heads) brush heads and learned the following:

  * Address 0x00-0x02 contains a unique ID and its checksum
  * Address 0x04-0x0C contains the link to the Philips store
  * Address 0x22 is 31:32:31:34 for black and 31:31:31:31 for white heads respectively
  * Address 0x24 contains the **total brush time**
  * All other readable data is identical between all heads

### Decoding the stored time

Let’s do an experiment to see what changes happen to the tag when using the toothbrush:

  1. Read the tag 
  * When reading a new brush head that has never been in contact with the data at addr. 0x24 is 00:00:02:00.
  * Simply attaching it to the handle (without brushing) changes nothing
  2. Brush for some time 
  * In this case, I let the toothbrush run for 5s
  3. Read the tag again 
  * The data at addr. 0x24 is now 05:00:02:00
  4. Observe the difference 
  * Looks like addr. 0x24 saves the number of seconds that the brush head was in use

When the brush is used for more than 255s, this timer rolls over to the second bit (02:01:02:00 -> 258s).

Trying to overwrite the stored time is unfortunately unsuccessful, as this memory address is password protected.

## Sniffing the password

Luckily it turns out that the required password is sent over plain text! So all I need to do is to sniff the communication between the toothbrush and the head. After digging out my [HackRF](https://greatscottgadgets.com/hackrf/) [software defined radio](https://en.wikipedia.org/wiki/Software-defined_radio) and some trial and error, I came up with the following workflow.

### Record RF signal

![](/assets/images/toothbrush/sniffing_in_progress.jpg)

When opening [gqrx](https://gqrx.dk/) and tuning it to 13.736 MHz while holding the toothbrush close to the antenna, it is visible that the head gets polled multiple times a second. It is a welcome surprise that my simple monopole antenna gets a signal that is strong enough for this purpose. You can download the relevant gqrx configuration file [here](/assets/files/gqrx.conf).

![](/assets/images/toothbrush/gqrx.png)

While brushing, the NFC polling takes a brief pause and the first burst of packets that follows updates the time counter. With the ability of gqrx to make I/Q recordings, we can capture the password RF signals like this:

  1. Turn on the toothbrush
  2. Start recording
  3. Turn off the toothbrush
  4. Stop the recording

The first packets in the file should now contain the password in plain text.

### Convert recording

![](/assets/images/toothbrush/gnuradio.png)

Before this raw I/Q file can be decoded it needs to be converted into a slightly different format to be read by the decoding program.  
I created a small [gnuradio](https://www.gnuradio.org/) companion script that applies a lowpass filter and converts the data into a wav file with two channels that contain the real and imaginary components of the complex signal.  
Make sure to substitute the correct paths in the source/sink blocks and check the sampling frequency (I used 2MHz).  
You can download the script [here](/assets/files/sniff_NFC.grc).

### Decode recording

[ ![Decoded traffic](/assets/images/toothbrush/nfc_lab.png) ](/assets/images/toothbrush/nfc_lab.png "Decoded traffic")

I found the perfect tool for this task called [NFC-laboratory](https://github.com/josevcm/nfc-laboratory). After opening the newly created WAV file, it should look something like the picture above. In this case, the recording is only good enough to see the communication that goes from host to tag (green arrow). But to sniff the password this is perfect.  
When looking at the [datasheet](https://www.nxp.com/docs/en/data-sheet/NTAG213_215_216.pdf#page=32) for the NTAG213, we can see what is happening:

  * Line #0-#6: communication is established with the tags’ unique ID
  * Line #7: The toothbrush sends the **password** (command 0x1B = PWD_AUTH)
  * Line #9: The time counter is updated to the new value (command 0xA2 = WRITE)
  * All lines below are repeated polling without password authentication or writing anything

So the password for this brush head is **67:B3:8B:98** (underlined in the picture).

## Writing to the brush

With the password successfully acquired, it’s now possible to set the counter on the brush head to anything we want by sending the relevant bytes over NFC.  
NFC Tools comes to the rescue again:

  1. Go to Other -> Advanced NFC commands
  2. Set the I/O Class to NfcA
  3. Set the data to 1B:67:B3:8B:98,A2:24:00:00:02:00
  4. Enjoy a factory-new brush head (at least as far as the time counter is concerned)

Here is the breakdown of the command in step 3:

Command | Explanation  
---|---  
1B | PWD_AUTH  
67:B3:8B:98 | The password  
, | Package delimiter  
A2 | WRITE  
24 | To address 0x24  
00:00:02:00 | Timer set to 0s  
  
Below you can see the memory of the brush head before and after the custom NFC commands:

[ ![](/assets/images/toothbrush/nfc_before.png) ](/assets/images/toothbrush/nfc_before.png "Before: 10s on timer") [ ![](/assets/images/toothbrush/nfc_during.png) ](/assets/images/toothbrush/nfc_during.png "Applying the update") [ ![](/assets/images/toothbrush/nfc_after.png) ](/assets/images/toothbrush/nfc_after.png "After: 0s on timer") Observe how the timer at address 0x24 changes 

With this, the toothbrush is now **successfully hacked** and we can play around with the timer as we wish.

Here are some interesting observations:

  * Only the first two bytes at address 0x24 are used for timekeeping. Once the counter reaches FF:FF:02:00 it stops going up (18 hours of continuous brushing).
  * When the stored time is greater than 0x5460 the toothbrush blinks the LED to notify you to change heads. This corresponds to 21’600s -> 180 x 2min -> 3 months of brushing twice a day, which is exactly in line with Philips recommendation to change heads every 3 months.

## Final Remarks

### Password verification protection

You might have noticed the color of the brush head changing throughout of this post. This is because I had to run out and buy a new one after getting locked out of the first one.  
When having a close look at the contents of address 0x2A which is 43:00:00:00 and [page 18](https://www.nxp.com/docs/en/data-sheet/NTAG213_215_216.pdf#page=18) of the datasheet, we can see that the tag is configured to permanently disable all write access after three wrong password attempts. (Which I promptly exceeded when playing around) This means that not even the toothbrush handle itself can write to this head again.

### Password generation

Unfortunately, the password of every brush head is unique and this process of extracting it with an SDR is quite involved and requires special hardware. At the bottom of page 30 in the datasheet, NXP recommends generating the password from the 7-byte UID. Below are all the UID - password pairs I obtained from my 3 heads:

UID | Password  
---|---  
04:79:CF:7A:89:10:90 | FF:34:CE:4C  
04:EC:FC:A2:94:10:90 | 61:F0:A5:0F  
04:D7:29:0A:94:10:90 | 67:B3:8B:98  
  
All my tries to guess to one-way function for generating the passwords failed. Depending on the care that the Philips engineers took, guessing this function could be almost impossible. But if you manage to solve this puzzle, feel free to hit me up with an E-mail.

## Update (August 16, 2023)

After publishing this article, I was pleasantly surprised to see it picked up by some big news sites such as [Hacker News](https://news.ycombinator.com/item?id=36128617) and [Hackaday](https://hackaday.com/2023/05/27/hacking-a-smart-electric-toothbrush-to-reset-its-usage-counter/). The resulting discussions and comments proved to be both enlightening and entertaining. Thanks to everyone who dropped positive comments and messages!  
A special shoutout has to go to [Aaron Christophel](https://www.youtube.com/@atc1441) who got inspired by this post to:

  * Dump and reverse engineer the Philips Sonicare firmware to extract the password generation algorithm: [Video](https://www.youtube.com/watch?v=EPytrn8i8sc)
  * Wrote a password generator: [GitHub](https://gist.github.com/atc1441/41af75048e4c22af1f5f0d4c1d94bb56)
  * And just for fun, he made the toothbrush bust out a [Rick Roll](https://www.youtube.com/watch?v=OkfS_z0FrlE)

Please go check his content if you are interested in the solution to the puzzle.

**__Updated:** May 24, 2023

[Previous](/nlp/ "Language modeling journey: From bigram prediction and DIY transformers to LLaMA 65B
") [Next](/co2/ "Building a cute CO2 gauge
")
