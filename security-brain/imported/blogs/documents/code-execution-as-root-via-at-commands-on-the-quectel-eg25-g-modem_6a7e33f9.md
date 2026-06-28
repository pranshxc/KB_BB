---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-03_code-execution-as-root-via-at-commands-on-the-quectel-eg25-g-modem.md
original_filename: 2021-04-03_code-execution-as-root-via-at-commands-on-the-quectel-eg25-g-modem.md
title: Code execution as root via AT commands on the Quectel EG25-G modem
category: documents
detected_topics:
- command-injection
- jwt
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- jwt
- api-security
- supply-chain
language: en
raw_sha256: 6a7e33f97d0af423c5c9d78886a12d9c957df5116ff684826b8684e3183dbcc8
text_sha256: d0b66861b0c6b898625254ad4e269282b910c955037edbca3207799d543aac48
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Code execution as root via AT commands on the Quectel EG25-G modem

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-03_code-execution-as-root-via-at-commands-on-the-quectel-eg25-g-modem.md
- Source Type: markdown
- Detected Topics: command-injection, jwt, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `6a7e33f97d0af423c5c9d78886a12d9c957df5116ff684826b8684e3183dbcc8`
- Text SHA256: `d0b66861b0c6b898625254ad4e269282b910c955037edbca3207799d543aac48`


## Content

---
title: "Code execution as root via AT commands on the Quectel EG25-G modem"
page_title: "Code execution as root via AT commands on the Quectel EG25-G modem | nns.ee"
url: "https://nns.ee/blog/2021/04/03/modem-rce.html"
final_url: "https://blog.nns.ee/2021/04/03/modem-rce"
authors: ["nns"]
programs: ["Quectel"]
bugs: ["OS command injection", "RCE"]
bounty: "2,000"
publication_date: "2021-04-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3766
---

# [Code execution as root via AT commands on the Quectel EG25-G modem](/2021/04/03/modem-rce/)

[ CVE-2021-31698CRITICAL: 9.8 ](https://nvd.nist.gov/vuln/detail/CVE-2021-31698)

Apr 03, 2021

As I mentioned towards the end of my [previous blog post](/2021/04/01/modem-blog), where I detailed running my blog on the PinePhone's GSM/WWAN/GPS modem, I suspected that the daemon responsible for parsing AT commands on the modem's side is susceptible to OS command injection, as it uses a _lot_ of `system()` calls. My hunch turned out to be true.

## Communication with the PinePhone

Among other channels, the PinePhone communicates with the Quectel modem by sending [AT commands](https://en.wikipedia.org/wiki/Hayes_command_set) to the modem over a serial line - `/dev/ttyUSB2` on the PinePhone's side and `/dev/ttyHSL0` on the modem's side.

The modem, which runs a [full Linux install](/2021/04/01/modem-blog) separate from the PinePhone's main OS, receives these commands, parses them, and executes them according to program logic. After this, the modem either returns `OK` or `ERROR` over the serial line back to the PinePhone. The daemon primarily responsible for this is `atfwd_daemon`.

## Analyzing `atfwd_daemon`

Getting the daemon is easy. It's possible to set up [`adb` access](https://xnux.eu/devices/feature/modem-pp.html#toc-unlock-adb-access) and extract it using `adb`. It's also possible to simply extract it from the firmware's update packages, as it's not encrypted in any way.

Loading `atfwd_daemon` in Ghidra reveals that the executable uses `system()` in 233 different places across the file. That's... quite a lot.

While using `system()` with user input is never a good idea, most of the calls cannot be exploited due to being hardcoded or the fact that user input is converted to an integer using `sprintf()`:

[![/img/2021-04-03-modem-rce/1BSw4BQZ.png](/img/2021-04-03-modem-rce/1BSw4BQZ.png)](/img/2021-04-03-modem-rce/1BSw4BQZ.png)

However, there are a few places where user input is `sprintf()`-d as `%s` and no checks or sanitization is performed on user input.

One of these places is in a routine called `quectel_handle_fumo_cfg_command()`:

[![/img/2021-04-03-modem-rce/EnUTEnhj.png](/img/2021-04-03-modem-rce/EnUTEnhj.png)](/img/2021-04-03-modem-rce/EnUTEnhj.png)

Here we can see that `param1[1]` is being formatted as `ipth_dme -dmacc %s &`, which is then passed to `system()`. What's interesting to note here is that `ipth_dme` does not exist on the system at all, so this program would never run.

Traversing the program execution flow, we can see that the switch case in the previous screenshot is triggered when some part of user input begins with "dmacc". This is checked in a routine called `quectel_parse_fumo_cfg_cmd_params()`:

[![/img/2021-04-03-modem-rce/DSuRVPK1.png](/img/2021-04-03-modem-rce/DSuRVPK1.png)](/img/2021-04-03-modem-rce/DSuRVPK1.png)

The rest of the input remains relatively untouched.

Going further up the program flow, we can see that the command in question which parses this input is `+QFUMOCFG`:

[![/img/2021-04-03-modem-rce/wCONynTY.png](/img/2021-04-03-modem-rce/wCONynTY.png)](/img/2021-04-03-modem-rce/wCONynTY.png)

## Code execution

From this, we can deduce that arbitrary command execution is possible. We can, for example, use backticks to execute our commands in a subshell. As an example, to reboot the modem:
  
  
  AT+QFUMOCFG="dmacc","`reboot`"

Due to the fact that the daemon runs as root, the code is also being executed as the root user on the modem.

As an example, in this [Asciinema recording](https://asciinema.org/a/IANZkjwk9lw82pOKFLsWvsi9k), I `cat /etc/passwd` and run `id`, and return the data to the PinePhone's OS over a serial line:

[![asciicast](https://asciinema.org/a/IANZkjwk9lw82pOKFLsWvsi9k.svg)](https://asciinema.org/a/IANZkjwk9lw82pOKFLsWvsi9k)

It's very possible that this vulnerability affects other Quectel products as well, as firmware is commonly reused, but I do not possess other hardware to test it on.

* * *

### Timeline

  * **03/04/2021** \- Attempted to contact vendor
  * **13/04/2021** \- Vendor confirmed vulnerability
  * **23/04/2021** \- Vendor issued $2,000 bounty
  * **24/04/2021** \- Assigned ID CVE-2021-31698
  * **08/09/2021** \- Write-up published

[ ![Rasmus Moorats](/img/av.jpg) ](/about)

Author | [Rasmus Moorats](/about)

Ethical Hacking and Cybersecurity professional with a special interest for hardware hacking, embedded devices, and Linux.
