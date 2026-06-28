---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-30_how-i-hacked-my-way-to-the-top-of-darpas-hardware-bug-bounty.md
original_filename: 2022-01-30_how-i-hacked-my-way-to-the-top-of-darpas-hardware-bug-bounty.md
title: How I hacked my way to the top of DARPA’s hardware bug bounty
category: documents
detected_topics:
- supply-chain
- sso
- command-injection
- rate-limit
- automation-abuse
- api-security
tags:
- imported
- documents
- supply-chain
- sso
- command-injection
- rate-limit
- automation-abuse
- api-security
language: en
raw_sha256: 455548d8d5384bc2fc8a559bcacbedcf6b7b927f0b540dcefb66c426d92b40a6
text_sha256: d28f3f74b5f60205e40bde9407acf5fb3cd66e423040fc1c66bd7d149967dcb4
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked my way to the top of DARPA’s hardware bug bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-30_how-i-hacked-my-way-to-the-top-of-darpas-hardware-bug-bounty.md
- Source Type: markdown
- Detected Topics: supply-chain, sso, command-injection, rate-limit, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `455548d8d5384bc2fc8a559bcacbedcf6b7b927f0b540dcefb66c426d92b40a6`
- Text SHA256: `d28f3f74b5f60205e40bde9407acf5fb3cd66e423040fc1c66bd7d149967dcb4`


## Content

---
title: "How I hacked my way to the top of DARPA’s hardware bug bounty"
url: "https://readme.security/how-i-hacked-my-way-to-the-top-of-darpas-hardware-bug-bounty-b66ec53b1973"
final_url: "https://readme.synack.com/how-i-hacked-my-way-to-the-top-of-darpas-hardware-bug-bounty"
authors: ["Malcolm Stagg (@malcolmst)"]
programs: ["DARPA FETT"]
bugs: ["Hardware hacking"]
publication_date: "2022-01-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2966
---

###### Illustration: Si Weon Kim

**_Go inside one of the most technically challenging bug bounties ever with the researcher who subverted secure hardware designed by MIT and the University of Cambridge._**

When the Defense Advanced Research Projects Agency (DARPA) announced in the summer of 2020 that it was having its first-ever bug bounty to test the defenses of its System Security Integration Through Hardware and Firmware (SSITH) program, I knew I had to be part of it. Previously, I did some hardware research, including reverse-engineering and [rooting](https://en.wikipedia.org/wiki/Privilege_escalation) consumer Blu-ray players, while I was in college. DARPA’s SSITH program posed an altogether different, enticing challenge: SSITH hardware is advanced, incorporating novel techniques to thwart many common cyberattacks. DARPA wanted to test the defenses of prototypes developed under the program, so the Pentagon research agency partnered with [Synack](https://www.synack.com/) and the Department of Defense’s [Defense Digital Service](https://www.dds.mil/) to give cybersecurity researchers a chance to find weaknesses via the Finding Exploits to Thwart Tampering (FETT) bug bounty.

I’ve also worked on DARPA projects before. At the time, I had just finished competing as a finalist in the DARPA Spectrum Collaboration Challenge, using AI techniques to better manage the radio frequency spectrum, and was still competing in a [separate DARPA event](https://www.subtchallenge.com/) aimed at finding new approaches for robots to autonomously explore subterranean environments.

In June 2020, I completed Synack’s Capture-the-Flag hacking event to join their team for the FETT bug bounty. By August, I was a new security researcher on the Synack Red Team, granting me rare access to DARPA’s SSITH hardware.

Four SSITH performers had made their hardware approaches available for testing. Lockheed Martin’s [“Hardware Architecture Resilient by Design”](https://www.lockheedmartin.com/en-us/news/features/2020/beating-hackers-the-hard-way.html) architecture incorporated a security co-processor to monitor program execution and detect anomalies. MIT’s [“Sanctum”](https://people.csail.mit.edu/devadas/pubs/sanctorum.pdf) moved program execution into a secure enclave, while SRI International and the University of Cambridge’s [“CHERI”](https://www.cl.cam.ac.uk/research/security/ctsrd/cheri/) added pointer capabilities for memory protection. Finally, University of Michigan’s [“Morpheus”](https://cse.engin.umich.edu/stories/morpheus-vs-everybody) used quickly changing encryption to prevent attacks. These approaches each had their own unique ways of making common attacks such as buffer overflows and code injection impossible to exploit, even while running software with known vulnerabilities. To test the limits of this technology, DARPA posed a challenge to the researchers: Can you write your own vulnerable software that would enable an attacker to bypass the SSITH protections?

## **Attack №1: Sanctum**

I first turned my sights to MIT’s Sanctum and its secure, encrypted [enclave](https://en.wikipedia.org/wiki/Trusted_execution_environment) where code execution took place in isolation. Hardware protections prevented access to the memory space used by the enclave, even by the operating system itself. The idea was that if an attacker gained complete control over the system, they still could not access the enclave.

To control program execution at a high level within each enclave, Sanctum’s firmware — known as the Security Monitor — presented an [API](https://en.wikipedia.org/wiki/API) to the operating system. Accessing this API required kernel privileges, so my first task was to write a [Loadable Kernel Module](https://en.wikipedia.org/wiki/Loadable_kernel_module) (LKM) to be loaded by the host operating system, allowing my test code to interact with the Security Monitor API. Fortunately, I had written LKMs before in my Blu-ray research. After a little trial-and-error to correctly match the needed configuration to allow my LKM to be loaded, I had access to Sanctum’s Security Monitor API.

The Security Monitor API required several steps before enclave execution, including locking the memory space, decrypting and loading the enclave, and setting the entry point where it would begin code execution. Each step in the enclave setup was cryptographically signed to prevent an attacker with full access to the API from performing any unauthorized steps. If the correct sequence was not followed, the enclave’s signature would be invalid, and it would fail to run.

My first step in attacking Sanctum was to perform a thorough review of [MIT’s open-source code](https://github.com/mit-enclaves/ssith-mit-sanctum) for the enclaves and Security Monitor. A thought crossed my mind: If two enclaves were to be created simultaneously, would the security safeguards protect both? Looking further, I found there was a flaw in how the Security Monitor handled the cryptographic signatures. There appeared to be nothing preventing a [thread](https://en.wikipedia.org/wiki/Thread_\(computing\)) belonging to one enclave from running inside another. I could perhaps set up a second enclave to run arbitrary code within the first!![1_2tBY1Xvn-_dshqk5Q7uDVw](https://readme.synack.com/hs-fs/hubfs/1_2tBY1Xvn-_dshqk5Q7uDVw.webp?width=1400&height=650&name=1_2tBY1Xvn-_dshqk5Q7uDVw.webp)

Figure 1: First attack on Sanctum: an attack thread belonging to a second enclave is run inside the first enclave.

To test this idea, I wrote an exploit capable of extracting the decrypted contents of an enclave. I used my LKM to load this exploit into [shared memory](https://en.wikipedia.org/wiki/Shared_memory), then set up two enclaves. I spun up the first normally in order for it to have a valid cryptographic signature. I crafted the second one minimally, with the address of the exploit specified as its thread entry point. Since only the cryptographic signature of the first enclave needed validation, I had complete control over the attack thread belonging to the second enclave. Finally, I ran this attack thread inside the first enclave. Success! By the time the enclave finished running, I had obtained its decrypted memory contents, and had performed the first successful attack on Sanctum.

## **Other attacks on Sanctum**

Over the next few months of the FETT challenge, I used my LKM to find three additional vulnerabilities in Sanctum, mostly involving the sequence of memory protections used in the Security Monitor API. One of the most interesting was an [integer overflow](https://en.wikipedia.org/wiki/Integer_overflow) flaw in the Security Monitor firmware, which allowed me to overwrite any memory in the system.

Sanctum had a feature that enabled messages to be passed between enclaves through [virtual mailboxes](https://en.wikipedia.org/wiki/Mailbox_\(computing\)). I noticed a possible flaw in the validation of an enclave’s mailbox count. If enough mailboxes were defined, an integer overflow might occur when calculating the memory size needed for the enclave. The result would be a tiny enclave with a huge number of addressable mailboxes. By sending a message to one of these mailboxes outside the memory bounds of the enclave, I realized it might be possible to instruct the Security Monitor to overwrite just about any memory address in the system!![1_tPJM0gNY9C2tD7xWNgo97A](https://readme.synack.com/hs-fs/hubfs/1_tPJM0gNY9C2tD7xWNgo97A.webp?width=1400&height=602&name=1_tPJM0gNY9C2tD7xWNgo97A.webp)

_Figure 2: Attempted attack on Sanctum: An attack payload is sent to an out-of-bounds mailbox for the first enclave, overwriting the second enclave’s cryptographic signature._

I used my LKM to create an enclave with a huge number of mailboxes — approximately 1 quintillion — to trigger the integer overflow. I then sent a message to a mailbox that I believed corresponded to memory used by a second enclave to overwrite its cryptographic signature. With anticipation, I ran the program. It immediately crashed the system.

To see what might have gone wrong, I devised a way to look at the mailbox data, and found that something was getting received — but not the data I had tried to send. That led me to another bug in Sanctum’s source code, this time in a [pointer dereference](https://en.wikipedia.org/wiki/Dereference_operator) operation. My payload had been replaced by the Security Monitor’s internal [stack data](https://en.wikipedia.org/wiki/Call_stack). Ironically, a code bug was making the mailbox count vulnerability much harder to exploit.

I started looking for another destination for this internal data. One possible target was the memory buffer used for calculating a cryptographic signature. If overwritten, this could reset a thread count to zero, making my exploit persistent in memory for launching a later attack. However, sending data to this new destination would be extremely difficult since it contained several incorrectly set values for it to be a usable destination.

Agonizing over this problem for hours, I finally came up with a solution: Two of the required values could be correctly set during the final step of the enclave’s creation. This would leave just one remaining byte, which would have to be solved with brute force. Fortunately, with only 256 combinations, it wouldn’t take long to solve.![1_NM0rZyL8oDXAZCKd_eI1Uw](https://readme.synack.com/hs-fs/hubfs/1_NM0rZyL8oDXAZCKd_eI1Uw.webp?width=1400&height=743&name=1_NM0rZyL8oDXAZCKd_eI1Uw.webp)

_Figure 3: Successful attack on Sanctum: A payload of stack data is sent to an out-of-bounds mailbox, overwriting an enclave’s thread count after brute forcing a byte value. The enclaves are then deleted, leaving behind a persistent thread for launching a later attack._

I modified my test code to brute force the unknown byte and create an attack thread for running the exploit. Next, I could send data into an out-of-bounds mailbox, making the attack thread persistent. Finally, I would create a brand-new enclave, and run it with the persistent attack thread. This time, my code worked! I once again had an attack on Sanctum, capable of executing arbitrary code and obtaining the decrypted contents of an enclave.

## **Next attack: CHERI’s memory allocators**

CHERI added hardware-enforced [capabilities](https://en.wikipedia.org/wiki/Capability-based_addressing) such as memory bounds for [pointers](https://en.wikipedia.org/wiki/Pointer_\(computer_programming\)). If a buffer overflow occurred, the memory bounds would stop it from being exploited. Capabilities could be easily added to the source code of existing programs with only minor modifications, although to enforce the capabilities, the architecture demanded modifying all layers of the system, including the processor, compiler, and operating system. DARPA made a custom [BSD](https://en.wikipedia.org/wiki/List_of_BSD_operating_systems)-based operating system available to researchers, who were challenged to write their own vulnerable code capable of bypassing CHERI’s protections.

The first thing I noticed about CHERI is that it had a massive amount of code available to review. Like MIT’s Sanctum, CHERI was also [open-source](https://github.com/CTSRD-CHERI). After studying the processor definition and compiler source code without much success, I turned my focus to the [memory allocators](https://en.wikipedia.org/wiki/C_dynamic_memory_allocation) in the C language standard library, “[libc](https://en.wikipedia.org/wiki/C_standard_library).” These memory allocators are an important part of the CHERI system, since they are where capabilities are added to user-defined buffers.

Generally, when a developer wants to allocate a buffer in a C program, they will call the “malloc” (memory allocate) function with the size of the buffer they want to have available. Malloc then returns the address of a buffer, with the guarantee that at least that many bytes are available in that location, but with no enforcement of buffer boundaries. In CHERI, the system enforces buffer bounds, so malloc must return a pointer with not only a valid address, but also a capability containing appropriate buffer bounds, ensuring that a buffer overflow cannot take place.

Whenever a capability is returned from a function, the code that obtains it theoretically has access to resources included within its bounds. For CHERI’s protections to**** fully work, a program must only be provided with whatever capabilities are needed for its execution, no more and no less. This was correctly handled in malloc, which returned a single capability containing the bounds of the allocated buffer. The buffer contents had been erased at that point, ensuring that no stray capabilities were accidentally returned to the calling code, which could result in unintended access to other memory regions.

While studying the allocator code, I noticed a possible flaw in “realloc,” which is used to increase or reduce the size of an allocated buffer. When enlarging a buffer, for efficiency, realloc attempts to extend the existing buffer into nearby, unused buffers whenever possible. When doing so in CHERI, it erased the contents of the neighboring buffer to prevent capability leakage, but I noticed it did not erase the 64-byte metadata region at the very beginning of the neighboring buffer. This metadata potentially contained CHERI capabilities that could be used to give the calling code access to a much larger region of memory than was intended by the memory allocator.![1_GBWj7zLxbZ9Sm4ReNrd--w](https://readme.synack.com/hs-fs/hubfs/1_GBWj7zLxbZ9Sm4ReNrd--w.webp?width=1400&height=438&name=1_GBWj7zLxbZ9Sm4ReNrd--w.webp)

_Figure 4: A leaked capability pointer on memory reallocation was used to bypass CHERI’s memory protections._

To test this, I wrote an intentionally vulnerable program where two buffers are allocated, the second buffer deleted, and the first buffer reallocated to extend into the second buffer. I believed this sequence of steps would result in the execution of the potentially vulnerable code path, causing a leakage of capability pointers. I set up the first few elements of the buffer for a contrived example where a user could select a location and write some data to the pointer stored there. The remaining elements were left untouched, so that any leaked CHERI capabilities would not be overwritten.

Examining the memory contents of the buffer metadata, I found it contained leaked CHERI capability pointers for a very large region of memory, which had been previously obtained from the operating system by the memory allocator. When running the contrived example, if the user copied a large amount of data into a location containing a leaked capability pointer, the result was effectively a buffer overflow allowing an attacker to overwrite neighboring buffers. This vulnerability was the first to successfully bypass CHERI’s protections.

## **Last attack: CHERI’s operating system**

Heading into the final week of the event, I had still found only one CHERI vulnerability, and was hoping to find another. I had since turned my attention to studying the file I/O and the network stack of the operating system and soon found something suspicious in a function used by the operating system’s [async I/O](https://en.wikipedia.org/wiki/Asynchronous_I/O) (AIO) operations.

Since I/O operations tend to be quite slow, AIO functions allow a program to continue performing other tasks while an I/O operation takes place. When each function is called, a structure containing a buffer for holding any transferred data is passed to the function. I noticed the kernel function that processed this structure neglected to check whether the buffer contained valid CHERI capabilities! That opened the door for an attacker to specify a buffer length larger than the buffer bounds, causing the AIO function to overflow the buffer. Interestingly, I noticed that this same, seemingly vulnerable, kernel function was also used in two other operations: pipes to redirect the output of a program to a file, and the [Berkeley Packet Filter](https://en.wikipedia.org/wiki/Berkeley_Packet_Filter) used to intercept network traffic.![1_xdozYoXTehSFfO-xcAT1rA](https://readme.synack.com/hs-fs/hubfs/1_xdozYoXTehSFfO-xcAT1rA.webp?width=1400&height=749&name=1_xdozYoXTehSFfO-xcAT1rA.webp)

_Figure 5: Multiple operating system functions were found to bypass CHERI’s memory protections when specifying a malicious buffer length_

I created intentionally vulnerable programs as proof-of-concept demonstrations for these three operations. Each program contained a vulnerability enabling an attacker to instruct the operating system to perform an operation that would overflow a buffer. When I ran them, due to the missing capability check in the kernel function, the buffer overflows worked! I had found my second successful bypass of CHERI’s memory protections.

## Summing up

The few months I spent working on the FETT bug bounty were incredibly meaningful. It was very satisfying to see MIT and SRI/Cambridge quickly respond to my findings and in many cases even send over their patches to validate the fixes. The challenge reinforced my love of cybersecurity research and gave me the chance to join the Synack Red Team, which has allowed me to apply the skills and knowledge I have acquired to finding interesting and challenging vulnerabilities like these. I feel fortunate to have had the opportunity to help test and enhance SSITH’s defenses, and I am excited to see how hardware approaches like these will bring about more secure computing in the future.
