---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-23_but-you-told-me-you-were-safe-attacking-the-mozilla-firefox-renderer-part-1.md
original_filename: 2022-08-23_but-you-told-me-you-were-safe-attacking-the-mozilla-firefox-renderer-part-1.md
title: 'But You Told Me You Were Safe: Attacking The Mozilla Firefox Renderer (Part
  1)'
category: documents
detected_topics:
- sso
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- sso
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: d3f9615c116fe6274f080f782367cc45c36ee9b6254c12f9800cd841511b3cf1
text_sha256: 81ec91ab36fc72551dfeb269ef142dc6491bc61146c61af168c4951a454264bd
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# But You Told Me You Were Safe: Attacking The Mozilla Firefox Renderer (Part 1)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-23_but-you-told-me-you-were-safe-attacking-the-mozilla-firefox-renderer-part-1.md
- Source Type: markdown
- Detected Topics: sso, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `d3f9615c116fe6274f080f782367cc45c36ee9b6254c12f9800cd841511b3cf1`
- Text SHA256: `81ec91ab36fc72551dfeb269ef142dc6491bc61146c61af168c4951a454264bd`


## Content

---
title: "But You Told Me You Were Safe: Attacking The Mozilla Firefox Renderer (Part 1)"
page_title: "Zero Day Initiative — But You Told Me You Were Safe: Attacking the Mozilla Firefox Renderer (Part 1)"
url: "https://www.zerodayinitiative.com/blog/2022/8/17/but-you-told-me-you-were-safe-attacking-the-mozilla-firefox-renderer-part-1"
final_url: "https://www.zerodayinitiative.com/blog/2022/8/17/but-you-told-me-you-were-safe-attacking-the-mozilla-firefox-renderer-part-1"
authors: ["Hossein Lotfi (@hosselot)", "Manfred Paul (@_manfp)"]
programs: ["Mozilla"]
bugs: ["Browser hacking", "RCE", "Prototype pollution"]
bounty: "100,000"
publication_date: "2022-08-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2272
---

# Blog

#  But You Told Me You Were Safe: Attacking the Mozilla Firefox Renderer (Part 1) 

__ August 18, 2022

__ Hossein Lotfi

Vulnerabilities and exploits in common targets like browsers are often associated with memory safety issues. Typically this involves either a direct error in memory management or a way to corrupt internal object state in the JavaScript engine. One way to eliminate such memory safety issues is to use a memory-safe language such as Rust or even JavaScript itself. At Pwn2Own Vancouver 2022, Manfred Paul compromised the Mozilla Firefox browser using a full chain exploit that broke the mold. Although his exploit used some memory corruptions, the vulnerable code was written in a memory-safe programming language: JavaScript! In fact, both vulnerabilities used in the chain were related to one rather notorious language aspect of JavaScript – prototypes. In this blog, we will look at the first vulnerability in the chain, which was used to compromise the Mozilla Firefox renderer process. This vulnerability, known as CVE-2022-1802, is a prototype pollution vulnerability in the await implementation. You can find more information about this vulnerability on the Zero Day Initiative advisory page tracked as [ZDI-22-799](https://www.zerodayinitiative.com/advisories/ZDI-22-799/). Mozilla fixed this vulnerability in Firefox 100.0.2 via [Mozilla Foundation Security Advisory 2022-19](https://www.mozilla.org/en-US/security/advisories/mfsa2022-19/).

Note: this blog series is heavily reliant on the details provided by Manfred Paul at the Pwn2Own competition.

**Compromising The Renderer Process**

Modern JavaScript features the [module syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules), which allows developers to split code into individual files. An even newer feature is the support of asynchronous modules, or, more precisely, the feature known as [top level await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#top_level_await). In Firefox’s JavaScript engine, SpiderMonkey, large parts of this feature are implemented using built-in JavaScript code. Consider the following function from the SpiderMonkey codebase, in [/js/src/builtin/Module.js](https://searchfox.org/mozilla-central/rev/cdb2004ea504bab2b66a1196c2267053e5882528/js/src/builtin/Module.js#749):

There are three facts we must note the code shown above:

1 -- This function runs in the same JavaScript context as the user’s code. This is true for most JavaScript-based functions in Firefox. This means that global state, including prototypes of global objects, is shared between this built-in code and untrusted website code. 

2 -- The function has a default argument of `execList = []`. In practice, the function is called without specifying this argument (except for the recursive call in the function itself). Therefore, a new empty array object is constructed and used for this argument. Like any other ordinary array, this array object has the unique object `Array.prototype` as its prototype. 

3 -- The function invokes `std_Array_push` on this array object. The `std_Array_push` function leads to a call to the `Array.prototype.push` JavaScript method. While the usage of `std_Array_push` function instead of `Array.prototype.push` helps prevent side effects up to a certain point, the function still can interact with the object’s prototype. (Note that in various other places within this same built-in JavaScript file `/js/src/builtin/Module.js`, a different function is used to assign array values: `DefineDataProperty`. In contrast to `std_Array_push`, `DefineDataProperty` is safe and will not interact in any way with the object’s prototype.)

The semantics of `Array.prototype.push` with a single argument are very roughly equivalent to the following:

Notably, the assignment is not just the definition of a data property on the object itself. Instead, it searches the object’s prototype chain for existing properties as per usual JavaScript semantics. If the imported module defines a getter/setter for property `0` on the Array prototype (`Array.prototype`), this assignment operation will trigger the setter function. This call technically violates the ECMAScript specification that defines `GatherAsyncParentCompletions` in terms of abstract lists and not actual JavaScript arrays. Crucially, this has yet another effect: it leaks the value that is assigned to our setter, so we recover the value “m” representing a module! This object is not the same as the module namespace returned by `import()`, but rather, it is an internal type of the JavaScript engine not meant to be accessible to untrusted script. It exposes some unsafe methods via its prototype, such as `GatherAsyncParentCompletions`. Calling `GatherAsyncParentCompletions` results in a call to the `UnsafeSetReservedSlot` method, which can be used to achieve memory corruption if we pass in a non-module object.

**Triggering The Vulnerability**

It is easy to trigger the vulnerability and obtain a Module object:

As described, we simply need to attach a setter to the `0` property of `Array.prototype` and wait for it to be called. Note that this snippet will only work when imported as a module from another file. The last line exists solely to mark the module as asynchronous, which is needed to trigger the bug.

**Achieving Memory Corruption**

To achieve memory corruption, we can now call `mod.gatherAsyncParentCompletions` with an object of the form `{asyncParentModules:[obj]}`, resulting in a call to `UnsafeSetReservedSlot` . This will attempt to write the value `obj.pendingAsyncDependencies-1` to the internal object slot with number `MODULE_OBJECT_PENDING_ASYNC_DEPENDENCIES_SLOT=20`. In SpiderMonkey, objects have space for up to 16 so-called fixed slots which are for internal use only. This number is defined by the `MAX_FIXED_SLOTS` constant. Slots with a higher index are indexed from an array pointed to by the `slots_` field. This means our write will be directed to the array pointed to by `slots_`. No bounds checking exists to make sure that the `slots_` array is large enough to accommodate the specified index, because the `UnsafeSetReservedSlot` function assumes, as the name implies, that the caller will pass only suitable objects.

The general idea now is to:

1 -- Create a new array object. 

2 -- Set some named properties of the object to force the allocation of a `slots_` array for the object. Among these properties, we should create one with the name `pendingAsyncDependencies`. 

3 -- Write to a few numbered elements of the object to ensure the allocation of `elements_` (the backing store for array elements).

By getting the alignment right, `slots_[4]` will then point to the capacity value of `elements_`, which we can then overwrite. This is not trivial. Fortunately, the heap allocator is very simple and deterministic. All of the allocations so far will take place in the [nursery](https://hacks.mozilla.org/2014/09/generational-garbage-collection-in-firefox/) heap, which is a special area for small short-lived objects. Memory in that area will be allocated by a simple bump allocator. After increasing the capacity, we can write out-of-bounds of the object’s `elements_` array and corrupt other nearby objects. From here, arbitrary read and write primitives are easily constructed by overwriting the data pointer of a typed array. Note that corruption in objects in the nursery heap cannot be used for very long since the objects created there will be soon moved to the tenured heap. The best way to proceed is to use corruption in the nursery heap as a first stage only, and immediately use it to produce corruption in the tenured heap. For example, this can be done by corrupting `ArrayBuffer` objects.

**Executing Shellcode**

Firefox uses [W^X JIT](https://jandemooij.nl/blog/wx-jit-code-enabled-in-firefox/), which means all JIT-produced executable pages are non-writable. This prevents us from overwriting executable JIT code with our shellcode. There is an already well-known method to force JIT to emit arbitrary ROP gadgets by embedding chosen floating-point constants into a JIT-compiled JavaScript function. This results in the appearance of arbitrary short byte sequences in an executable page. Manfred Paul further enhanced this technique. Now it does not even need ROP at all! Instead of using a JavaScript function, the floating-point constants are embedded into a WebAssembly method, so they are compiled into consecutive memory in order of appearance. This makes it possible to insert not just ROP gadgets, but even somewhat longer stretches of shellcode by encoding them in the floating-point constants. There are still some restrictions, though: no 8-byte block may appear twice, or the constant will only be emitted once. Also, due to ambiguity in representation, byte sequences that are equal to NaN might not be encoded correctly. Therefore, Manfred Paul opted for a minimal first-stage shellcode that offers just the following two pieces of functionality:

1 -- The ability to read a pointer from the Windows PEB structure. 

2 -- The ability to invoke a function given the function’s address.

The attacker, from ordinary JavaScript, triggers execution of the shellcode’s first function to leak a value from the PEB. Next, the JavaScript uses this value together with the arbitrary read primitive to locate kernel32.dll and its functions in memory. Once it has located the address for `VirtualProtect`, it invokes the shellcode’s second function to mark the backing store of an `ArrayBuffer` object as executable, making it possible to run a second-stage shellcode without constraints and compromise the renderer process.

Now that we have code execution inside the renderer, it is time to prepare to attack the sandbox. This will be covered in the second blog, coming next week.

**Final Notes**

For a long time, developers have tried to fight memory corruption vulnerabilities by introducing various mitigations, and they have succeeded in making it more difficult for attackers to fully compromise applications. However, attackers have also come up with their own creative methods to bypass mitigations. Using a memory-safe programming language is a critical move. If the introduction of memory corruption vulnerabilities can be avoided in the first place, it would not be necessary to rely upon the strength of mitigations. This post looked at a great vulnerability demonstrating that even if you replace existing code with JavaScript, you could still be prone to memory corruption.

Stay tuned to this blog for part two of this series coming next week. Until then, you can find me on Twitter at [@hosselot](https://twitter.com/hosselot) and follow the team on [Twitter](https://www.twitter.com/thezdi) or [Instagram](https://www.instagram.com/thezdi) for the latest in exploit techniques and security patches.

  * [Firefox](/blog/tag/Firefox)
  * [Mozilla](/blog/tag/Mozilla)
  * [Pwn2Own](/blog/tag/Pwn2Own)
