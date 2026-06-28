---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-11-27_bypassing-a-noexec-by-elf-roping.md
original_filename: 2023-11-27_bypassing-a-noexec-by-elf-roping.md
title: Bypassing a noexec by elf roping
category: documents
detected_topics:
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- api-security
language: en
raw_sha256: 5fbf26b23c1968a87d578fd36b7d99fd9aa05e0069db084f2d934135a37ed731
text_sha256: f6ad9c8398f344bab04f0f367639e9e1ffd0bfc4a7860191b8dce7f6ecfecfd6
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing a noexec by elf roping

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-11-27_bypassing-a-noexec-by-elf-roping.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `5fbf26b23c1968a87d578fd36b7d99fd9aa05e0069db084f2d934135a37ed731`
- Text SHA256: `f6ad9c8398f344bab04f0f367639e9e1ffd0bfc4a7860191b8dce7f6ecfecfd6`


## Content

---
title: "Bypassing a noexec by elf roping"
page_title: "Bypassing a noexec by elf roping - The Cave"
url: "https://blog.xilokar.info/bypassing-a-noexec-by-elf-roping.html"
final_url: "https://blog.xilokar.info/bypassing-a-noexec-by-elf-roping.html"
authors: ["Xilokar (@xilokar)"]
bugs: ["noexec bypass", "Local Privilege Escalation"]
publication_date: "2023-11-27"
added_date: "2024-01-25"
source: "pentester.land/writeups.json"
original_index: 664
---

* [home](https://blog.xilokar.info)

[The Cave](https://blog.xilokar.info)

[Stuff that does not matter](https://blog.xilokar.info)

# Bypassing a noexec by elf roping

published on Mon 27 November 2023 by [Xilokar](https://blog.xilokar.info/pages/about-me.html)

In this post, I will show you how I bypassed a noexec permission in a limited chrooted env.

## Short Context

Ok, so you have found this vuln in this software. You're happy. You can upload file, and you have the opportunity to execve a provided string. All seems done and you can enjoy a well deserved beer.

But no.

The service you hacked is well limited in facts. The upload directory is a tmpfs with noexec mount option. And the service runs in a chrooted env with no shell (sorry, no /bin/sh -c /tmp/upload/myscript.sh)

## Disclaimer

I don't pretend this a new approach or something never seen before. Just something I wasn't aware of ;)

## Initial attempts

Luckily for us, even if the chroot is hardened, the provided application are dynamic executables, so we have access to ld.so and libc.so. In facts, in this system, it is the same musl binary.

My first attempt was to upload an elf in the tmpfs, and try an /lib/ld.so /tmp/uploaded.bin in order to bypass the missing -x permission on the file.

While I later learnt it used to be a classical noexec bypass, kernels nowdays refuse to mmap part of a file on a nonexec fs with the PROT_EXEC flag set, so no luck here.

## First Victory

While playing with ld.so, I noticed something that proved very interesting, memory locations of ld.so and the uploaded.bin elf file, while randomized due to ASLR, were fixed relative to each other. This is not the case when executing an elf the normal way.

Another thing to notice, is even if my elf binary is non-executable (and hence non executed), it still can be loaded. You just have to have no PROT_EXEC segment in it and ld.so and the kernel will happily map it.

Once loaded, the last thing ld.so will normally do, is to branch to your entry point. Obviously, since we have changed the segments to be non executable, it will fail miserabily.

When exploiting, and you encounter a non-executable writeable address space is to go roping.

Remember that our loaded elf and libc.so are at a static offset ? So with a little math, we can tell ld.so that our entry point is far away from our loaded segments, but rather in the libc.so .text section ;)

And it works !

We just need now to carefully choose where we are going to jump.

But if we are going to rop, we need to be able to build a full ropchain on our stack, and unfortunately, the stack when entering the entry point is not really adapted... We just have a pointer to the argv and env strings in the stack.

Our best chance would be to be able with one gadget to swap the stack to a memory controlled region. But this turns out to be difficult (at least with the libc.so I was targeting) without a little more help.

A very well suitable function to switch stack is the longjmp which restore an executable context.

There are already calls in the ld.so that makes use of it.
  
  
  FUN_00148920("Error recording dependencies for %s", lVar9);
  if (DAT_001919e8 != 0) {
  /* WARNING: Subroutine does not return */
  longjmp(DAT_001919e0,1);
  }
  

What is interesting is that the pointer to the structure used for the longjmp call is a writeable global.

## Abusing Relocation

(hum, I may have spoiled a little here ... )

What's fun with elf loading is relocations. It basicly tells the loader, "Hey, I will need to use this function, please write me its position here, so that I can use it". (There are Far better tutorials on relocation on the internet...).

In fact you can even add an addendum to the position of the symbol you want the loader to inform you about.

Remember how we tell the loader to set our entry point to where we want inside the libc.so ? Well, we can use the same trick to let the loader know that we want address of symbol_a + addendum written inside the libc.so writeable .data section. For exemple at the position of the pointer used during the longjmp call.
  
  
  fffffffffe7fd9e0  001800000101 R_AARCH64_ABS64  000000000000000 puts
  

And what's even more beautiful, is that we can use the loader to have the relocation point to our own object:
  
  
  struct init_stack rop_exec_stack = {
  .sp = &rop_stack.rop_chain,
  .x30 = GADGET(START_STACK_GADGET),
  };
  
  void *address_of_rtld_fail = (void*)&rop_exec_stack;
  

After patching the elf:
  
  
  fffffffffe7fd9e0  001800000101 R_AARCH64_ABS64  0000000000186140 \
  rop_exec_stack + 0
  

Now, we juste have to point entry to the call to longjmp, and our first and only gadget will have everything done for us... We have set the stack pointer to our rop-chain that we can carefully write now...

## Wrapping it all together

I must admit this was not the funniest part, finding suitables gadgets is very time consuming (especially on AARCH64 I found).

We can still use the loader to have it calculate values and offsets for us

But after some amount of time, I was able to write a rop chain that malloc a huge buffer, mprotect it to have it executable, memcpy a payload (embedded in the uploade.bin file) and then jump in it.

And it is easy (as in, easy once done) to embedded a static elf in our payload and have it executed.

![](/medias/pwned-strace.png)

Now, you can work on escaping the chroot, but that is another story...

## Final thoughts

This was fun (and hard) to work on this. I wrote this one shot, after final succes, so typos / error may be present (don't hesitate to contact me !)

Feel free to share this blog post (and others ;) ) if you found it interesting.

This entry was tagged [#Reverse](https://blog.xilokar.info/tag/reverse.html)

### [About me __](https://blog.xilokar.info/pages/about-me.html)

### Social Network

  * [Twitter __](https://twitter.com/xilokar)
  * [Mastodon __](https://mamot.fr/@Xilokar)

### Categories

  * [Misc __](https://blog.xilokar.info/category/misc.html)

### Feeds

  * [atom feed __](https://blog.xilokar.info/feeds/all.atom.xml)

Blog generated by [Pelican](http://getpelican.com/) using (slighty modified) [Pujangga](https://github.com/habibillah/pujangga) theme.
