---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-14_uncursing-the-ncurses-memory-corruption-vulnerabilities-found-in-library.md
original_filename: 2023-09-14_uncursing-the-ncurses-memory-corruption-vulnerabilities-found-in-library.md
title: 'Uncursing the ncurses: Memory corruption vulnerabilities found in library'
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: 8bd1cfd7afa81b317ea6d0f0c6afca97b5e7d72d6002f57efeed44f4045419ff
text_sha256: bfbef77474567581c8ec9292ea2fce835ea74a9d26c22bf9ad46cb9ac31d0996
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# Uncursing the ncurses: Memory corruption vulnerabilities found in library

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-14_uncursing-the-ncurses-memory-corruption-vulnerabilities-found-in-library.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `8bd1cfd7afa81b317ea6d0f0c6afca97b5e7d72d6002f57efeed44f4045419ff`
- Text SHA256: `bfbef77474567581c8ec9292ea2fce835ea74a9d26c22bf9ad46cb9ac31d0996`


## Content

---
title: "Uncursing the ncurses: Memory corruption vulnerabilities found in library"
page_title: "Uncursing the ncurses: Memory corruption vulnerabilities found in library | Microsoft Security Blog"
url: "https://www.microsoft.com/en-us/security/blog/2023/09/14/uncursing-the-ncurses-memory-corruption-vulnerabilities-found-in-library/"
final_url: "https://www.microsoft.com/en-us/security/blog/2023/09/14/uncursing-the-ncurses-memory-corruption-vulnerabilities-found-in-library/"
authors: ["Microsoft Threat Intelligence (@MsftSecIntel)"]
programs: ["ncurses"]
bugs: ["Memory corruption"]
publication_date: "2023-09-14"
added_date: "2023-09-19"
source: "pentester.land/writeups.json"
original_index: 780
---

![](https://www.microsoft.com/en-us/security/blog/wp-content/themes/security-blog-2025/dist/images/single-bg.jpg)

![](https://www.microsoft.com/en-us/security/blog/wp-content/themes/security-blog-2025/dist/images/single-bg-dark.jpg)

  1. [ Home ](https://www.microsoft.com/en-us/security/blog/)
  2. Uncursing the ncurses: Memory corruption vulnerabilities found in library 

Search

![Colleagues working in a library on laptops](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/09/Ncurses-featured-image.webp)

[ Research ](https://www.microsoft.com/en-us/security/blog/content-type/research/) September 14, 2023  13 min read 

#  Uncursing the ncurses: Memory corruption vulnerabilities found in library 

By [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/author/microsoft-security-threat-intelligence/ "Posts by Microsoft Threat Intelligence")

* * *

## Share

  * [ Link copied to clipboard!  ](https://www.microsoft.com/en-us/security/blog/2023/09/14/uncursing-the-ncurses-memory-corruption-vulnerabilities-found-in-library/)
  * [ ](https://www.facebook.com/sharer/sharer.php?u=https://www.microsoft.com/en-us/security/blog/2023/09/14/uncursing-the-ncurses-memory-corruption-vulnerabilities-found-in-library/)
  * [ ](https://twitter.com/intent/tweet?url=https://www.microsoft.com/en-us/security/blog/2023/09/14/uncursing-the-ncurses-memory-corruption-vulnerabilities-found-in-library/&text=Uncursing+the+ncurses%3A+Memory+corruption+vulnerabilities+found+in+library)
  * [ ](https://www.linkedin.com/sharing/share-offsite/?url=https://www.microsoft.com/en-us/security/blog/2023/09/14/uncursing-the-ncurses-memory-corruption-vulnerabilities-found-in-library/)

## Tags

  * [Elevation of privilege](https://www.microsoft.com/en-us/security/blog/tag/elevation-of-privilege/)
  * [Linux](https://www.microsoft.com/en-us/security/blog/tag/linux/)
  * [macOS](https://www.microsoft.com/en-us/security/blog/tag/macos/)

## Threats intelligence

  * [Vulnerabilities and exploits](https://www.microsoft.com/en-us/security/blog/threat-intelligence/vulnerabilities-and-exploits/)

## Content types

  * [Research](https://www.microsoft.com/en-us/security/blog/content-type/research/)

## Products and services

  * [Microsoft Defender](https://www.microsoft.com/en-us/security/blog/product/microsoft-defender/)
  * [Microsoft Defender for Endpoint](https://www.microsoft.com/en-us/security/blog/product/microsoft-defender-for-endpoint/)
  * [Microsoft Defender Vulnerability Management](https://www.microsoft.com/en-us/security/blog/product/microsoft-defender-vulnerability-management/)

## Topics

  * [Threat intelligence](https://www.microsoft.com/en-us/security/blog/topic/threat-intelligence/)

Microsoft has discovered a set of memory corruption vulnerabilities in a library called [_ncurses_](https://invisible-island.net/ncurses/), which provides APIs that support text-based user interfaces (TUI). Released in 1993, the _ncurses_ library is commonly used by various programs on Portable Operating System Interface (POSIX) operating systems, including Linux, macOS, and FreeBSD. Using environment variable poisoning, attackers could chain these vulnerabilities to elevate privileges and run code in the targeted program’s context or perform other malicious actions.

One of the most [common vulnerabilities](https://msrc.microsoft.com/blog/2019/07/a-proactive-approach-to-more-secure-code/) found in modern software, memory corruption vulnerabilities, can allow attackers to gain unauthorized access to systems and data by modifying a program’s memory. The impact of memory corruption vulnerabilities can range from leaking sensitive information and performing a simple denial-of-service (DoS) to elevating privileges and executing arbitrary code.

Microsoft has shared these vulnerabilities with the relevant maintainers through [Coordinated Vulnerability Disclosure](https://www.microsoft.com/msrc/cvd?rtc=1) (CVD) via [Microsoft Security Vulnerability Research](https://www.microsoft.com/msrc/msvr) (MSVR). Fixes for these vulnerabilities, now identified as [CVE-2023-29491](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29491) with a CVSS score of 7.8, have been successfully deployed by the maintainers of the _ncurses_ library, Thomas E. Dickey, in [commit 20230408](https://invisible-island.net/ncurses/NEWS.html#index-t20230408). We wish to thank Thomas for his professionalism and collaboration in resolving those issues. We also worked with Apple on addressing the macOS-specific issues related to these vulnerabilities, and we thank Apple for their response and partnership. Lastly, during our analysis, a researcher named [Gergely Kalman](https://twitter.com/gergely_kalman) engaged us privately over Twitter and contributed relevant use cases in addition to his own hand-coded fuzzer. We thank Gergely for his contributions in advancing this research and community engagement. Users of  _ncurses_ are encouraged to update their instances and systems.

In this blog post, we share information about _ncurses_ and the discovered memory corruption vulnerabilities. We also share this research to emphasize the importance of collaboration among researchers, industry partners, and the larger security community in the effort to improve security for all.

## Understanding terminal databases

Terminal databases are used by _ncurses_ to be terminal-independent, meaning the capabilities of the terminal are not required to be known ahead-of-time. Terminal databases contain a set of capabilities that ultimately determine the control characters that are sent to the terminal (instructing the terminal to perform basic interactions) and describe various properties of the terminal. Terminal databases come in two major formats: the older and less commonly used termcap (terminal capability) format, and the improved terminfo format. Since terminals can differ on the types of control characters they expect and the operations they support, terminfo became necessary to address this discrepancy. In its textual syntax, capabilities are separated by commas, and come in three forms:

  * Boolean capabilities: for example, the _am_ capability specifies that the terminal supports automatic margins. In the terminfo textual syntax, Boolean capabilities appear by their name alone, without any additions.
  * Numeric capabilities: for instance, the _cols_ capability contains the number of columns in a line. In the terminfo textual syntax, numeric capabilities are recognized with a “#” symbol after their name, followed by the numeric value, such as “cols#80”.
  * String capabilities: for instance, the _clear_ capability describes the control character that should be transmitted to the terminal to clear the screen. In the terminfo textual syntax, string capabilities are recognized with a “=” symbol after their name, followed by the string value, such as “clear=\E[H\E[2J”.

POSIX systems usually pre-ship with tens of such databases. It’s possible to parse the capabilities of the current database with the [infocmp](https://linux.die.net/man/1/infocmp) utility:

![Screenshot of the infocmp utility code output](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/09/Figure-1.-infocmp-output-reveals-the-current-terminfo-database-along-with-its-capabilities-1024x559.webp)_Figure 1. infocmp output reveals the current terminfo database along with its capabilities_

## Environment variable poisoning

Every modern operating system contains a set of environment variables that might affect the behavior of programs. A well-known technique for attackers is to manipulate those environment variables to cause programs to perform actions that would benefit their malicious purposes, hence “poisoning” them. There have been multiple cases of environment variable poisoning in the past, for instance:

  * [CVE-2023-22809](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22809): users were allowed to elevate their privileges by poisoning the EDITOR environment variable (and similar other environment variables) and running [sudoedit](https://linux.die.net/man/8/sudoedit), which ultimately allowed them to edit arbitrary files.
  * [CVE-2022-0563](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0563): the environment variable INPUTRC is indirectly used by the [chsh](https://linux.die.net/man/1/chsh) and [chfn](https://linux.die.net/man/1/chfn) [set-UID](https://en.wikipedia.org/wiki/Setuid) Linux binaries. It was discovered that INPUTRC could be poisoned to dump the contents of sensitive files on the system.
  * [CVE-2020-9934](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-9934): the HOME environment variable could be poisoned to bypass Transparency, Consent, and Control (TCC) on macOS, thus gaining access to otherwise inaccessible sensitive data. We have found a [similar bypass](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30970) and [reported it in 2021](https://www.microsoft.com/security/blog/2022/01/10/new-macos-vulnerability-powerdir-could-lead-to-unauthorized-user-data-access/).
  * [CVE–2023-32369](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32369): the PERL5OPT and BASH_ENV environment variables could be poisoned to bypass [System Integrity Protection](https://developer.apple.com/documentation/security/disabling_and_enabling_system_integrity_protection) (SIP) in macOS, thus elevating privileges. We have reported the vulnerability in [April 2023](https://www.microsoft.com/security/blog/2023/05/30/new-macos-vulnerability-migraine-could-bypass-system-integrity-protection/).
  * The [LD_PRELOAD](https://man7.org/linux/man-pages/man8/ld.so.8.html) environment variable is commonly used in Linux for [code injection](https://attack.mitre.org/techniques/T1574/006/) purposes.
  * The WINDIR and SYSTEMROOT environment variables have been used in the past on Windows for bypassing [User Account Control](https://learn.microsoft.com/windows/security/identity-protection/user-account-control/how-user-account-control-works) (UAC).

We have discovered that during initialization, the _ncurses_ library searches for several environment variables, including an environment variable similarly named TERMINFO. When using terminfo databases, the program consults a fixed directory path unless a TERMINFO environment variable is present, which instead points the program to an alternative directory that contains compiled terminfo database files. Moreover, there are interesting common programs that use _ncurses_ , most notably [_top_](https://ss64.com/osx/top.html) on macOS, which is a [set-UID](https://en.wikipedia.org/wiki/Setuid) binary (which runs with elevated privileges) that also uses the TERMINFO environment variable. Therefore, finding vulnerabilities in _ncurses_ have the potential to affect many programs and possibly elevate privileges. It’s noteworthy that the potential of poisoning the TERMINFO environment variable was highlighted several times in the past (for example, [here](https://blog.trailofbits.com/2023/02/16/suid-logic-bug-linux-readline/)), but we have not seen comprehensive research on the topic of terminfo capabilities for offensive security purposes.

For completeness, while this blog post focuses on how attackers could poison the TERMINFO environment variable to potentially exploit _ncurses_ vulnerabilities, the HOME environment variable could have been similarly manipulated. Assuming the TERMINFO environment variable was never defined, _ncurses_ looks for a _$HOME/.terminfo_ directory. This could have been abused by planting a _.terminfo_ directory at an arbitrary path and poisoning the HOME environment variable, so the technique is quite similar.

## Stack-based terminfo capabilities

The terminfo capabilities are richer than they first appear. In a nutshell, capabilities are allowed to receive up to nine parameters (p1-p9) and use them in a stack data structure. Furthermore, capabilities work with a stack-like structure and instructions that can push (place an item in the stack) and pop (get an item from the stack) data, perform logical-arithmetic operations, and even support conditions. Here are some examples:

**Operation**| **Description**  
---|---  
**%{number}**|  Push a constant value to the stack.  
**%p x**| Push the parameter to the stack.  
**%+, %-, %*, %/, %m**|  Pop two numbers from the stack and push the arithmetic result of the stack. Addition, substruction, multiplication, division, and remainder operations are supported.  
**% &, %|, %^**| Pop two numbers from the stack and push the bitwise result to the stack. Bitwise OR, AND, and XOR are supported.  
**%=, % <, %>, %A, %O**| Pop two numbers and compare them, pushing the logical result back to the stack. The operations of comparison, less-than, and greater-than are supported, as well as logical AND and OR operations.  
**%l**|  Pop a string from the stack and push its length back to the stack.  
**%?[condition]%t[body 1]%e[body2]%;**| Perform a condition. The _%t_ operation pops a numeric value from the stack and compares it to 0. The result determines what body to execute (the “else” body is optional and comes after the _%e_ delimiter).  
**%s, %c**|  Pop a string from the stack and print it out to the terminal.  
**%d, %x**|  Pop a number from the stack and print it out to the terminal.  
  
While not Turing-complete, terminfo offers functionality that resembles very basic programming. Due to the complicated logic required by _ncurses_ , security issues are expected to be found, and indeed there have been numerous _ncurses_ vulnerabilities [in the past](https://www.cvedetails.com/vulnerability-list/vendor_id-72/product_id-38464/GNU-Ncurses.html).

It’s interesting to note that while the version of _ncurses_ we checked was 6.4 (latest at the time of research), the _ncurses_ version on macOS was 5.7, but had several security-related patches [maintained by Apple](https://github.com/apple-oss-distributions/ncurses). Nevertheless, all our findings are true for all _ncurses_ versions, thus affecting both Linux and macOS.

## Discovered vulnerabilities

We discovered several memory corruption vulnerabilities through code auditing and [fuzzing](https://owasp.org/www-community/Fuzzing). In addition to using our own [AFL++ based fuzzer](https://github.com/AFLplusplus/AFLplusplus), the use cases contributed by [Gergely Kalman](https://twitter.com/gergely_kalman) assisted in advancing this research.

The discovered vulnerabilities could have been exploited by attackers to elevate privileges and run code within a targeted program’s context. Nonetheless, gaining control of a program through exploiting memory corruption vulnerabilities requires a multi-stage attack. The vulnerabilities may have needed to be chained together for an attacker to elevate privileges, such as exploiting the stack information leak to gain arbitrary read primitives along with exploiting the heap overflow to obtain a write primitive.

## Stack information leak

The function that runs the capability logic is called [_tparm_](https://linux.die.net/man/3/tparm). It is a C variadic function, meaning its number of arguments is not predefined (similarly to _printf_). The way variadic functions work in C is usually with the [_va_list_](https://en.cppreference.com/w/c/variadic/va_list) structure and its macros, [_va_start_](https://en.cppreference.com/w/c/variadic/va_start), [_va_arg_](https://en.cppreference.com/w/c/variadic/va_arg), and [_va_end_](https://en.cppreference.com/w/c/variadic/va_end). The common scenario for such functions is to parse a format-string, conclude the number of parameters it expects, and use the _va_arg_ macro iteratively to fetch those arguments. However, since an attacker can be in full control of the capability’s string, we can make _tparm_ call _va_arg_ more times than it should, effectively leaking information from the call stack. Since we are allowed up to nine parameters, we can leak up to eight unintended arguments, including arguments from the program’s stack:

![Screenshot of code](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/09/Figure-2.-Demonstrating-an-information-leak-proof-of-concept-1024x585.webp)_Figure 2. Demonstrating an information leak proof of concept_

## Parameterized string type confusion

The stack used by the _tparm_ function is just an allocated array with 20 entries (referred as _STACK_FRAME_ in the source code). Each frame can hold either a number (32-bit signed integer) or a string (pointer). To distinguish between a number and a string, the frame uses a Boolean value, which represents whether the data is numeric or not:

![Screenshot of code](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/09/Figure-3.-A-terminfo-stack-entry.webp)_Figure 3. A terminfo stack entry_

Certain push operations can be easily concluded, for example, when pushing an arithmetic result (such as _%+_) or a literal (_%{number}_). However, for parameters, things are different. There is no easy way to know ahead of time whether a parameter is expected to be a string or numeric. Therefore, _tparm_ uses a heuristic—it walks the capability string statically, and when it sees _%s_ or _%l_ , it concludes that the last parameter push was a string. This approach can be abused in multiple ways. For example, the macOS _top_ utility calls [_mvcur_](https://linux.die.net/man/3/mvcur), which in turn calls _tparm_ with the _cup_ capability, along with integer parameters. Treating the parameter as a string can trigger [_strlen_](https://cplusplus.com/reference/cstring/strlen/) on the integer address:

![Screenshot of code](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/09/Figure-4.-Type-confusion-causes-strlen-to-be-invoked-on-low-addresses.webp)_Figure 4. Type confusion causes strlen to be invoked on low addresses_

The crash we triggered occurs during an initialization of the _mvcur_ operation, which assesses the “cost” of moving the cursor by invoking _tparm_ with a constant, non-attacker-controlled value. We can improve the attack by using conditions—if the parameter’s value is not that constant value, then treat the parameter as a string, otherwise treat it as a number. Implementation with capabilities is straightforward:

![A line of code reading cup=%?%p1%p2%<%t\\E\[%i%p1%d;%p2%dH%e%p1%s%;,](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/09/Test-1.1-1-1024x81.webp)

This should be read as:

![Screenshot stating “IF p1 < p2 THEN \(use the usual ‘cup’ capability\) ELSE treat p1 is a string”
](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/09/Test-1.2-1-1024x67.webp) ![Screenshot of code](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/09/Figure-5.-Using-conditions-to-only-trigger-strlen-when-desired.webp)_Figure 5. Using conditions to only trigger strlen when desired_

This primitive is quite powerful, as we can trigger _strlen_ on an arbitrary number, effectively gaining a read primitive. Gaining a read primitive defeats the Address Space Layout Randomization (ASLR) security mechanism to leak address information and, if the binary happens to contain valuable secrets in its memory (like passwords), an attacker could potentially read those as well.

## Cost calculating padding off-by-one

We have mentioned _mvcur_ uses a cost-calculating function to determine the costs of certain capabilities. The cost-calculation is done by the function __nc_msec_cost_ , and it assesses the number of milliseconds it takes to print out a capability, which is strongly derived by delays that could be a part of a capability. Delays are numeric literal values wrapped between ‘ _$ <_’ and ‘ _>_ ’, and they even support a decimal point. We discovered an off-by-one error—if the function sees a decimal point character, it skips one character assuming a digit, with an insufficient check after:

![Screenshot of code](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/09/Figure-6.-Off-by-one-bug-causes-the-string-to-be-assessed-beyond-its-boundaries.webp)_Figure 6. Off-by-one bug causes the string to be assessed beyond its boundaries_

Therefore, it’s possible to have the cost-calculating function read beyond the boundary of the capability string by closing the delay markup with a ‘ _>_ ’ character immediately following the decimal dot.

![Screenshot of code](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/09/Figure-7.-Reading-past-the-capability-string-limit-might-cause-a-segmentation-fault.webp)_Figure 7. Reading past the capability string limit might cause a segmentation fault_

## Heap out-of-bounds during terminfo database file parsing

The terminfo database files are binary files commonly compiled from the text representation with a utility called [_tic_](https://linux.die.net/man/1/tic). The format of the database consists of the following parts:

  * The header: contains a magic value, the size of the terminal name, the number of Boolean capabilities, the number of numeric capabilities, the number of string capabilities, and the total size of string capabilities.
  * The terminal name
  * The capabilities:
  * The Boolean capabilities
  * The numeric capabilities
  * The string capability offsets
  * The string capabilities themselves
  * Optional extended entries (in the same order: Boolean, numeric, and strings)

The optional extended entries are user-defined entries. We discovered that the function that performs that database parsing (__nc_read_termtype_) can write beyond the boundaries of a heap-allocated chunk, as such:

![Screenshot of code](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/09/Figure-8.-Heap-out-of-bounds-due-to-realloc-call.webp)_Figure 8. Heap out-of-bounds due to realloc call_

  1. The code uses [_calloc_](https://linux.die.net/man/3/calloc) to allocate room for the strings. While _STRCOUNT_ is a constant representing the maximum length of standard string capabilities (414), _str_count_ is attacker-controlled and defined in the header of the attacker’s terminfo file. This controls the size of the allocated chunk saved in _ptr- >Strings_.
  2. After parsing all the standard capabilities, _ncurses_ starts parsing the extended capabilities. The code assigns _ptr- >num_Strings_ to _STRCOUNT+ ext_str_count_ , which might be **smaller** than the non-extended string count, effectively shrinking _ptr- >Strings_ with a [_realloc_](https://linux.die.net/man/3/realloc) call.
  3. Immediately after the _realloc_ call, we can see _ptr- >Strings_ being written beyond its boundaries. Extended string capabilities are parsed and appended after standard string capabilities. The _convert_strings_ function attempts to achieve this by storing data in _ptr- >Strings + str_count_. However, while _ptr- >Strings _was shrunk to _STRCOUNT+ext_str_count_ , _str_count_ is user-controlled and can be greater than _STRCOUNT_.
  4. If _str_count >= STRCOUNT_, then _ptr- >Strings + str_count + ext_str_count_ will be greater than _ptr- >Strings + STRCOUNT + ext_str_count _and _convert_strings_ will cause a heap buffer overflow.

## Denial of service with canceled strings

The _ncurses_ library has a notion of marking strings as “cancelled”. This is useful for terminfo database inheritance and skipping absent capabilities in general. As an example, the function _convert_strings_ that converts strings from the terminfo database file format to the appropriate data structures in memory sets strings as _CANCELLED_STRING_ if the index referring to them is negative.

![Screenshot of code](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/09/Figure-9.-convert_strings-setting-a-string-to-be-CANCELLED.webp)_Figure 9. convert_strings setting a string to be CANCELLED_

The value of the _CANCELLED_STRING_ constant is -1, and before processing, the _ncurses_ codebase looks for these strings and converts them to _ABSENT_STRING_ (constant 0). Unfortunately, it does so only for ordinary strings; extended strings do not get that treatment. Specifically, a heuristic determines that strings that begin with the “k” character should be treated as keypad functionality. This allows an attacker to specify an extended string in a way that will make _ncurses_ dereference -1 (0xFFFFFFFFFFFFFFFF):

![Screenshot of code](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/09/Figure-10.-ncurses-dereferencing-1-when-attempting-to-parse-a-cancelled-string-for-keypad-functionality.webp)_Figure 10. ncurses dereferencing -1 when attempting to parse a cancelled string for keypad functionality_

## Protection and detection with Microsoft Defender for Endpoint

While organizational devices and networks may become increasingly secure, attackers continue to exploit unpatched vulnerabilities and misconfigurations as a vector to access sensitive systems and information. Exploiting vulnerabilities in the _ncurses_ library could have notable consequences for users, allowing attackers to perform malicious actions like elevating privileges to run code in a targeted program’s context and access or modify valuable data and resources. Responding to the evolving threat landscape requires us to expand our expertise across devices and platforms as part of our commitment to continuously improve security _from_ Microsoft, not just _for_ Microsoft.

This case displays how responsible vulnerability disclosure and collaborative research informs our comprehensive protection capabilities across platforms. [Microsoft Defender Vulnerability Management](https://learn.microsoft.com/microsoft-365/security/defender-vulnerability-management/defender-vulnerability-management?view=o365-worldwide) is able to quickly discover and remediate such vulnerabilities on both Linux and macOS. Additionally, [Microsoft Defender for Endpoint](https://www.microsoft.com/security/business/threat-protection/endpoint-defender) has similar detections for potential abuse of terminfo databases for set-UID binaries, such as macOS’s [_top_](https://ss64.com/osx/top.html):

![Screenshot of code](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2023/09/Figure-11.-Microsoft-Defender-for-Endpoint-detecting-suspicious-TERMINFO-use-1024x572.webp)_Figure 11. Microsoft Defender for Endpoint detecting suspicious TERMINFO use_

After discovering the vulnerabilities in the _ncurses_ library, we worked with the maintainer, Thomas E. Dickey, and Apple to ensure the issues were resolved across platforms. Additionally, this case displays the value of community engagement to improve security for all as researcher Gergely Kalman’s use case contributions assisted our research efforts. We wish to again thank Thomas and the Apple product security team for their efforts and collaboration in addressing [CVE-2023-29491](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29491), as well as Gergely for his contributions in furthering this research.

As the threat landscape continues to evolve and threats across all platforms continue to grow, Microsoft strives to continuously secure users’ computing experiences, regardless of the platform or device in use. We will continue to work with the security community to share vulnerability discoveries and threat intelligence in the effort to build better protection for all.

**Jonathan Bar Or, Emanuele Cozzi, Michael Pearse**

_Microsoft Threat Intelligence team_

## References

  * <https://invisible-island.net/ncurses/>
  * <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-29491>
  * <https://invisible-island.net/ncurses/NEWS.html#index-t20230408>
  * <https://twitter.com/gergely_kalman>
  * <https://linux.die.net/man/1/infocmp>
  * <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22809>
  * <https://linux.die.net/man/8/sudoedit>
  * <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0563>
  * <https://linux.die.net/man/1/chsh>
  * <https://linux.die.net/man/1/chfn>
  * <https://en.wikipedia.org/wiki/Setuid>
  * <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-9934>
  * <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-30970>
  * <https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-32369>
  * <https://developer.apple.com/documentation/security/disabling_and_enabling_system_integrity_protection>
  * <https://man7.org/linux/man-pages/man8/ld.so.8.html>
  * <https://attack.mitre.org/techniques/T1574/006/>
  * <https://ss64.com/osx/top.html>
  * <https://blog.trailofbits.com/2023/02/16/suid-logic-bug-linux-readline/>
  * <https://www.cvedetails.com/vulnerability-list/vendor_id-72/product_id-38464/GNU-Ncurses.html>
  * <https://github.com/apple-oss-distributions/ncurses>
  * <https://owasp.org/www-community/Fuzzing>
  * <https://github.com/AFLplusplus/AFLplusplus>
  * <https://linux.die.net/man/3/tparm>
  * <https://en.cppreference.com/w/c/variadic/va_list>
  * <https://en.cppreference.com/w/c/variadic/va_start>
  * <https://en.cppreference.com/w/c/variadic/va_arg>
  * <https://en.cppreference.com/w/c/variadic/va_end>
  * <https://linux.die.net/man/3/mvcur>
  * <https://cplusplus.com/reference/cstring/strlen/>
  * <https://linux.die.net/man/1/tic>
  * <https://linux.die.net/man/3/calloc>
  * <https://linux.die.net/man/3/realloc>

## Further reading

For the latest security research from the Microsoft Threat Intelligence community, check out the Microsoft Threat Intelligence Blog: <https://aka.ms/threatintelblog>. 

To get notified about new publications and to join discussions on social media, follow us on Twitter at <https://twitter.com/MsftSecIntel>.

![](https://www.microsoft.com/en-us/security/blog/wp-content/themes/blog-in-a-box/dist/images/default-avatar.png)

  * [ X ](https://x.com/MsftSecIntel)
  * [ LinkedIn ](https://www.linkedin.com/showcase/microsoft-threat-intelligence/)

##  Microsoft Threat Intelligence 

[ See Microsoft Threat Intelligence posts ](https://www.microsoft.com/en-us/security/blog/author/microsoft-security-threat-intelligence/)

## Related posts

  * ![A graphic showing a phishing hook representing social engineering and phishing](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2026/03/MS_Actional-Insights_Phishing-social-engineering.jpg)

June 25  33 min read 

##  [ Photo ZIP campaign targeting hospitality industry delivers Node.js implant for persistent access  ](https://www.microsoft.com/en-us/security/blog/2026/06/25/photo-zip-campaign-targeting-hospitality-industry-delivers-node-js-implant-persistent-access/)

Microsoft Threat Intelligence identified an active multi-stage intrusion campaign targeting hospitality organizations in Europe and Asia. 

  * ![Image of a man on a laptop with the icon for financially motivated threats in overlay](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2026/06/StealC-Amadey-featured.webp)

June 24  19 min read 

##  [ StealC and Amadey: Breaking down infostealers and the cybercrime services that deliver them  ](https://www.microsoft.com/en-us/security/blog/2026/06/24/stealc-and-amadey-breaking-down-infostealers-and-the-cybercrime-services-that-deliver-them/)

On June 24, 2026, Microsoft’s Digital Crimes Unit (DCU) facilitated the takedown, suspension, and blocking of domains that formed the backbone of the StealC and Amadey infrastructure. 

  * ![Global AI Red Team Insights](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2026/05/MS_Actional-Insights_AI.webp)

June 22  6 min read 

##  [ Guarding AI memory  ](https://www.microsoft.com/en-us/security/blog/2026/06/22/guarding-ai-memory/)

What happens when threat actors target what AI remembers? Microsoft breaks down the risks and the defenses.
