---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-05_simple-ibm-i-as400-hacking.md
original_filename: 2022-09-05_simple-ibm-i-as400-hacking.md
title: Simple IBM I (AS/400) Hacking
category: documents
detected_topics:
- access-control
- sso
- ssrf
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- access-control
- sso
- ssrf
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: eab800dc0413600883115a3a69425025f09bfad27492205c4a4965d90a25337e
text_sha256: ab8b0019c0bf7cc51a64b3365850157554eeff261fc1466b4581cf21b3624fc3
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Simple IBM I (AS/400) Hacking

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-05_simple-ibm-i-as400-hacking.md
- Source Type: markdown
- Detected Topics: access-control, sso, ssrf, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `eab800dc0413600883115a3a69425025f09bfad27492205c4a4965d90a25337e`
- Text SHA256: `ab8b0019c0bf7cc51a64b3365850157554eeff261fc1466b4581cf21b3624fc3`


## Content

---
title: "Simple IBM I (AS/400) Hacking"
page_title: "Simple IBM i (AS/400) hacking - Silent Signal Techblog"
url: "https://blog.silentsignal.eu/2022/09/05/simple-ibm-i-as-400-hacking/"
final_url: "https://blog.silentsignal.eu/2022/09/05/simple-ibm-i-as-400-hacking/"
authors: ["pz"]
bugs: ["Local Privilege Escalation", "Midrange system", "Menu security"]
publication_date: "2022-09-05"
added_date: "2022-09-29"
source: "pentester.land/writeups.json"
original_index: 2219
---

![Simple IBM i \(AS/400\) hacking](/wp-content/uploads/2022/09/blog-promo-scaled.jpeg)

# Simple IBM i (AS/400) hacking

[pz](/authors/pz.html) 2022-09-05 

When you get the chance to take a look at the IT systems of financial institutions, telcos, and other big companies, where availability has been a key business concern for decades, you’ll find, that some critical operations run through some obscure systems, in many cases accessed via nostalgic green-on-black terminals, the intricacies of which only a few people inside the company truly know. These systems might be IBM i’s – or as many senior folks know, “AS/400” or “iSeries” – that served through the stormy times of IT since the 1980s!

Some properties, that differentiate IBM i from your average server platform:

  * It is an object-oriented operating system, where object types determine what operations on a piece of data can be performed
  * Thanks to complete ISA abstraction, programs can be executed unmodified even when the hardware architecture changes
  * A database engine is integrated into the operating system, so you can have an SQL view of practically any component of the system
  * The compiler is tightly coupled with the OS, which, besides hardware independence also supports implementing memory safety checks at compile time even for languages like C

Recognizing, that these systems are here to stay, and that information critical to understanding their security architecture is scarce and sometimes inaccurate, we decided to create our own IBM i lab, that allowed us to familiarize ourselves with these systems, create new methodologies and tools to assess their security, and even to identify previously unknown vulnerabilities in them.

This blog post is the first step of publishing our findings to the security community, where I would like to share a walkthrough of the penetration testing result of an IBM i system. The presented techniques stem from misconfigurations common on this platform – this post only covers one privilege escalation path, but the comprehensive configuration audit of the same system uncovered several local and even remote vulnerabilities.

For the penetration testing the Client provided network access to the machine in the internal network, one low-level user account with special authority *NONE and limit capabilities value set to *PARTIAL. The user had an initial program configured after logging in on TLS wrapped [TN5250](https://en.wikipedia.org/wiki/IBM_5250), so direct CL command execution was not possible.

## Initial Program Breakout

> Native programs of IBM i are commonly accessed remotely on a telnet-like protocol, called TN5250. However, instead of providing raw shell access, TN5250 usually displays menu-based user interfaces</span> (the “green screen”). While the default menu allows access to the Command Language (CL) prompt (the “shell”), this can be replaced by configuring custom initial programs for users, that provide only limited features, such as executing predefined database queries.

The first task was trying to break out of the initial program limitation. After enumerating all the application menus, it became apparent, that there is no potential to run CL commands. Fortunately, the 5250 terminals and thus the TN5250 protocol supports an extended keyboard layout, allowing to trigger special menus by sending special key events, even when they are not available from the user interface of the initial program:

[ ![Special keys as displayed in a 5250 terminal emulator](/wp-content/uploads/2022/09/blog3.png) ](/wp-content/uploads/2022/09/blog3.png) Special keys as displayed in a 5250 terminal emulator

The attention interrupt key (ATTN) allows the authenticated user to interrupt/end a process and display a menu with additional functions:

[ ![Operational Assistant menu triggered by the Attention Interrupt key](/wp-content/uploads/2022/09/blog1-1024x646-2.png) ](/wp-content/uploads/2022/09/blog1-1024x646-2.png) Operational Assistant menu triggered by the Attention Interrupt key

This new menu has multiple options, including CL command execution, but one can just simply press F9 to bring up the command line:

[ ![CL prompt after initial program escape](/wp-content/uploads/2022/09/blog2-1024x631-2.png) ](/wp-content/uploads/2022/09/blog2-1024x631-2.png) CL prompt after initial program escape

From this point, the test user is no longer restricted to the functions of the initial program but can execute arbitrary commands (with its own privileges) on the operating system. The administrators can override the default behavior of the ATTN key by [modifying the User Profile](https://www.ibm.com/docs/en/i/7.1?topic=fields-attention-key-handling-program).

## Privilege Escalation by Profile Swapping

Information gathering about the accessible user profiles (`WRKUSRPRF`) exposes, that one of the profiles has the following special authority:

[ ![User Profile with \\*ALLOBJ privilege](/wp-content/uploads/2022/09/blog4.png) ](/wp-content/uploads/2022/09/blog4.png) User Profile with \\*ALLOBJ privilege

User Profiles are objects that represent users of the system. Special Authorities are system-wide roles that can be assigned to user profiles. The *ALLOBJ Special Authority [“essentially gives a user access to all functions on the system”](https://www.ibm.com/docs/en/i/7.4?topic=authority-allobj-special). Throughout the available documentation the word [“authority”](https://www.ibm.com/docs/en/i/7.2?topic=concepts-types-authority) is used to describe several different concepts, like roles granted for users, object access permissions or access control entries – in this post we try to resolve ambiguity by providing more expressive synonyms.

The “`WRKOBJ M<REDACTED> *USRPRF`” command shows, that the target User Profile authority is *USE to *PUBLIC.

[ ![Object Authority of the target high-privileged profile](/wp-content/uploads/2022/09/blog5.png) ](/wp-content/uploads/2022/09/blog5.png) Object Authority of the target high-privileged profile

> On IBM i all objects – including User Profiles – have an associated list of access controls entries. In the above example, the *USE authority (permission) is provided for the *PUBLIC subject – this special entry serves as a fallback when the accessing user doesn’t match any other access control entry. The *USE authority allows impersonation of the User Profile, in this case for all authenticated users of the system.

This means, that because of weak object configuration we can impersonate this user and run CL commands with *ALLOBJ authority. The current system security level is 40 in this case we can do at least two things:

  * Submit a new Job – The [SBMJOB](https://www.ibm.com/docs/en/i/7.2?topic=ssw_ibm_i_72/cl/sbmjob.htm) command allows specifying a User Profile with which a new Job (a command scheduled for execution) should be submitted. This will succeed if the submitting user has *USE authority over the specified User Profile, just like in our case.
  * Use the IBM i API from a program to associate a new User Profile to our session – We can use the [Get Profile Handle API](https://www.ibm.com/docs/en/i/7.3?topic=ssw_ibm_i_73/apis/QSYGETPH.htm) to obtain a handle to a usable (as in *USE permission) User Profile, then invoke the [Set Profile Handle API](https://www.ibm.com/docs/en/i/7.2?topic=ssw_ibm_i_72/apis/QWTSETP.htm) with the handle to make the current thread execute under the new User Profile.

The SBMJOB command is not ideal, because it is not interactive enough, therefore we invoke the IBM i API from a CL script similar to the following to escalate the privileges:
  
  
  PGM PARM(&U) 
  DCL VAR(&U) TYPE(*CHAR) LEN(10)
  DCL VAR(&E) TYPE(*CHAR) LEN(4)
  
  DCL VAR(&H) TYPE(*CHAR) LEN(10)
  
  CHGVAR VAR(%BIN(&E)) VALUE(0)
  
  CALL PGM(QSYGETPH) PARM(&U)
  
  CHGVAR VAR(%BIN(&E)) VALUE(0)
  
  CALL PGM(QWTSETP)
  
  ENDPGM
  

The script is intentionally wrong 

Compilation is done by the STRPDM (Start the Programming Development Manager – the built-in development environment of IBM i) command and the resulting PGM (program object) expects a parameter, the name of the User Profile to impersonate:

`CALL PENTEST/PRIVESC M<REDACTED>`

Due to the complexity of IBM i privilege management, similar misconfigurations are common, especially on systems with a high number of users. While discovering an exploitable path was sufficient to progress towards project goals, it is important to uncover similar vulnerabilities in the system via configuration review. For this, we developed a tool that can – among other things – assist experts in identifying misconfigurations, that could allow profile swapping to higher privileges for all User Profiles (running in our lab on the screenshots):

[ ![Finding as part of a comprehensive audit report](/wp-content/uploads/2022/09/blog0_audit_escalate.png) ](/wp-content/uploads/2022/09/blog0_audit_escalate.png) Finding as part of a comprehensive audit report [ ![Automated assistance to identify extensive object authorities](/wp-content/uploads/2022/09/blog0-dspusr.png) ](/wp-content/uploads/2022/09/blog0-dspusr.png) Automated assistance to identify extensive object authorities

At this point, the test user has obtained *ALLOBJ Special Authority, but we still can not modify our User Profile to persist our new privileges, because even with *ALLOBJ Special Authority one [“cannot directly perform operations that require another special authority”](https://www.ibm.com/docs/en/i/7.4?topic=authority-allobj-special) and for User Profile modification *SECADM Special Authority is required.and for User Profile modification *SECADM Special Authority is required.

## Becoming Security Administrator

> At this point, our user already has high privileges thanks to the *ALLOBJ Special Authority, so we don’t cross security boundaries here. However, further escalation steps like this are sometimes necessary to bypass controls – similarly to how UAC bypass is sometimes necessary in Windows environments.

As there were more than 2000 users in the system we used SQL to find candidates for further privilege escalation.

The following CL command queries the system users for basic information:

`DSPUSRPRF USRPRF(*ALL) TYPE(*BASIC) OUTPUT(*OUTFILE) OUTFILE(PENTEST/USERDB)`

A simple SQL query in the STRSQL command reveals the potential candidates:

[ ![Querying users with \\*SECADM Sepcial Authority from SQL](/wp-content/uploads/2022/09/blog6-1.png) ](/wp-content/uploads/2022/09/blog6-1.png) Querying users with \\*SECADM Sepcial Authority from SQL

And the result:

[ ![List of potential targets returned by the database engine](/wp-content/uploads/2022/09/blog7.png) ](/wp-content/uploads/2022/09/blog7.png) List of potential targets returned by the database engine

With the already obtained *ALLOBJ privilege, we can execute the privilege escalation script again (“`CALL PENTEST/PRIVESC USERWITHSECADM`“) to grant our test user *SECADM authority. The goal has been reached.

## Beyond the Green Screen

One of the challenges of securing IBM i systems is that the high integration of features provides access to the same attack surface through different interfaces, all of which need individual protections.

During this project, the remote services which are typically used to run CL commands were protected by exit programs (and in the case of the green screen, an initial program) that denied access with the test user. The administrators were probably not aware that the DDM service was also reachable on the system, and that it also allows command execution.

> Distributed Data Management (DDM) is a service of IBM i that allows transparent access to data stored across multiple different systems.
> 
> Exit programs are special programs that can be registered to “hook” the built-in authentication process to provide additional security controls.

Our IBM i audit/pentest framework helps to run CL commands over multiple remotely accessible services. The following screenshot demonstrates command execution over DDM in our test environment:

[ ![IBM i command execution from Linux workstation](/wp-content/uploads/2022/09/blog8-1024x55-2.png) ](/wp-content/uploads/2022/09/blog8-1024x55-2.png) IBM i command execution from Linux workstation

Running the `WRKOBJ USERB1/TESTCMD` command over TN5250 confirms the successful execution of the command sent over DDM:

[ ![Command execution result](/wp-content/uploads/2022/09/blog9.png) ](/wp-content/uploads/2022/09/blog9.png) Command execution result

Being able to remotely execute commands over a variety of protocols allows bypassing security checks, and automation, which would be cumbersome over TN5250. In this case, we could become Security Administrator even if the green screen wasn’t available or the initial program breakout wasn’t possible.

## Summary

This little case study shows, that while approaching IBM i systems requires learning the unusual ways of the platform, these systems are affected by really similar misconfigurations as our more common targets – in the end, all systems are programmed and configured by humans, usually under pressure to “just make it work”. In an environment where security visibility is severely limited, we believe it’s especially important to support the identification of mistakes, by proper guidance and tooling. Stay tuned for our next publications on IBM i!

[Twitter](https://twitter.com/intent/tweet?text=Simple IBM i \(AS/400\) hacking&url=https://blog.silentsignal.eu/2022/09/05/simple-ibm-i-as-400-hacking/ "Share on Twitter") [Facebook](https://facebook.com/sharer.php?u=https://blog.silentsignal.eu/2022/09/05/simple-ibm-i-as-400-hacking/ "Share on Facebook")

[# AS400](/tags#AS400) [# IBM i](/tags#IBM+i) [# pentest](/tags#pentest) [# privesc](/tags#privesc)
