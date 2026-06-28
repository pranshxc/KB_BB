---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-05_hacking-tmnf-part-1-fuzzing-the-game-server.md
original_filename: 2022-10-05_hacking-tmnf-part-1-fuzzing-the-game-server.md
title: 'Hacking TMNF: Part 1 - Fuzzing the game server'
category: documents
detected_topics:
- command-injection
- access-control
- otp
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- access-control
- otp
- api-security
- supply-chain
language: en
raw_sha256: 2a28681fe45c8f8d6ca53e6c248b908c5a2087e8ab9e820aca78fca786b983bd
text_sha256: c08473ce68607c52e015c4841fc1273f8eb9a6c43b892f65d60b982e55da3744
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking TMNF: Part 1 - Fuzzing the game server

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-05_hacking-tmnf-part-1-fuzzing-the-game-server.md
- Source Type: markdown
- Detected Topics: command-injection, access-control, otp, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `2a28681fe45c8f8d6ca53e6c248b908c5a2087e8ab9e820aca78fca786b983bd`
- Text SHA256: `c08473ce68607c52e015c4841fc1273f8eb9a6c43b892f65d60b982e55da3744`


## Content

---
title: "Hacking TMNF: Part 1 - Fuzzing the game server"
page_title: "Hacking TMNF: Part 1 - Fuzzing the game server | bricked.tech"
url: "https://blog.bricked.tech/posts/tmnf/part1/"
final_url: "https://blog.bricked.tech/posts/tmnf/part1/"
authors: ["-"]
programs: ["Ubisoft"]
bugs: ["RCE", "Memory corruption", "Format string vulnerability"]
publication_date: "2022-10-05"
added_date: "2022-10-06"
source: "pentester.land/writeups.json"
original_index: 2086
---

#  Hacking TMNF: Part 1 - Fuzzing the game server 

October 5, 2022 · 17 min 

![](https://blog.bricked.tech/posts/tmnf/part1/res/cover.png)

Table of Contents

  * Motivation
  * Why TrackMania?
  * Why XML-RPC?
  * Harnessing
  * Reverse engineering
  * Server setup
  * Sending RPC commands
  * Gheeeeedra ❤️ 🐉
  * Recap
  * LibAFL
  * Generic setup
  * The grammar
  * The XML-RPC format
  * Generating the Nautilus grammar
  * Harness
  * Letting it rip
  * Repro mode
  * Format string bugs, as far as the eye can see…
  * ““fixing”” the format string bug
  * finding more subtle bugs
  * Conclusion
  * Useful links

> If you’re just here for the exploit, [check out part 2](../part2). Otherwise, keep on reading for all the technical details and struggles I encountered along the way.

# Motivation#

A while back I started getting interested in fuzzing. I had followed some basic fuzzing courses at university, but those didn’t go much further than taking a FOSS project and throwing AFL++ at it. There were a couple of concepts I wanted to explore a bit further:

  * Binary-only (snapshot) fuzzing
  * Fuzzing network services and/or desocketting
  * Fuzzing with highly structured input.

## Why TrackMania?#

Trackmania was kind of a perfect target to tick these boxes. It has a Linux server binary, so shouldn’t be too difficult to harness. It also takes a bunch of different inputs over the network. One of those is the XML-RPC mechnism. And last but not least, it has a bug bounty! 😄

… or at least, TrackMania2020 does. In this post, I’ll be fuzzing Trackmania Nations Forever (2008). It is a bit smaller and has way fewer mitigations, but otherwise quite similar to the modern server.

## Why XML-RPC?#

XML-RPC has two things going for it. One; it is not trivial to fuzz because it requires valid XML inputs with very specific tags. Second, but not unimportantly, bugs in this area are easy to mitigate by firewalling the RPC port. Imagine if I find some critical bug in the normal game session handler. The odds of Nadeo digging into their 2008 code base to fix my bug is pretty much zero. I’d rather not destroy a small, fun community-driven game just to write an example fuzzer.

# Harnessing#

One of the first issues we will run into is how to feed an input to the server. Actually sending a packet over TCP is messy; it’s hard to multi-thread, fairly slow, and involves constantly rerunning a lot of unrelated netcode.

To solve this, we will write a wrapper around the server to make it only process RPC calls. In general fuzzing terminology, this is wrapper is called a “harness”.

The harness prepares the target for use in a fuzz loop. The fuzzer will provide us with an XML input, but it is up to the harness to make sure it is fed to the target correctly. For some targets, this is trivial. Got a fuzz case to feed to objdump? Just run `objdump -D <<input_file>>`.

Our case is a little more tricky. The server doesn’t take RPC input from the command line, nor does it exit cleanly after handling a single input. The general approach I used for my harness is the following:

  1. Run the Trackmania server until it starts processing an XML-RPC message
  2. Take a snapshot
  3. Restore the snapshot
  4. Inject a new input into memory
  5. Continue the server until the current function returns
  6. goto 3

To make this harness work, we need to know where to take that first snapshot. I.e. when does the server start processing our RPC message? Answering that question will require some reverse engineering, so let’s get the server up and running.

## Reverse engineering#

### Server setup#

The binary I’m working with is the `TrackmaniaServer` which you can download from [tm-forums](https://www.tm-forum.com/viewtopic.php?t=14203).1 Once you’ve downloaded and extracted the server, it should be pretty easy to get it going. I’m using some special command line arguments to keep the server running on the main thread (`/nodaemon`) and to run it without registering online (`/lan`):
  
  
  ./TrackmaniaServer /lan /nodaemon /nolog /dedicated_cfg=dedicated_cfg.txt \
  /game_settings=MatchSettings/Nations/NationsGreen.txt
  

### Sending RPC commands#

The Trackmania wiki does a pretty good job at explaining how to connect over XML-RPC. The [page on GbxRemote](https://wiki.trackmania.io/en/dedicated-server/XML-RPC/HowToConnect) even comes with some sample python code for us to ~~steal~~ _take inspiration from_.  
The example does a login by sending a valid XML payload that calls the `Authenticate` method. After running the code, you should see an “Okay” response from the server.

If we send a completely invalid RPC payload (for example `AAAAAAAA`), we get the following response:
  
  
  <?xml version="1.0" encoding="UTF-8"?>
  <methodResponse>
  <fault>
  <value>
  <struct>
  <member>
  <name>faultCode</name>
  <value>
  <int>-503</int>
  </value>
  </member>
  <member>
  <name>faultString</name>
  <value>
  <string>
  Call XML not a proper XML-RPC call.
  Call is not valid XML.  XML parsing failed
  </string>
  </value>
  </member>
  </struct>
  </value>
  </fault>
  </methodResponse>
  

As you can see, the XML parsing failed. Validating the XML is likely one of the first steps in the RPC call. We can look for this error message to find the RPC handler in the binary.

### Gheeeeedra ❤️ 🐉#

Time to fire up [Ghidra](https://ghidra-sre.org/) and dig around for the main RPC entry point. If we’re lucky, looking for the string we just saw should get us there fairly easily.  
Searching for “not a proper XML-RPC call” yields exactly one result and If we check the cross-references we find that it is used in exactly one function.

> In the initial version of this blog, I included code snippets that I painstakingly reversed by hand. When I offered a draft of this post to Kim (a Trackmania modder) they pointed out that the standalone version of the client actually ships with a MAP file, containing full debug symbols.
> 
> For your reading pleasure, I went back and swapped out all of the code snippets in this blog post. I really wish I’d known about that earlier 😭
  
  
  undefined4 __thiscall
  _xmlrpc_registry_process_call(CScene2d *param_1_00, /* ... */,
  char * xml_msg, size_t len) {
  // ..
  uVar3 = _xmlrpc_mem_block_new(param_1,0, "XML-RPC CALL", xml_msg, len);
  if (*piVar1 == 0) {
  _xmlrpc_env_init(local_c);
  _xmlrpc_parse_call(local_c,uVar4,uVar2,&param_1,&local_14);
  if (local_c[0] == 0) {
  _xmlrpc_dispatchCall(piVar1,param_2,param_1,local_14,&local_10);
  if (*piVar1 == 0) {
  _xmlrpc_serialize_response(piVar1,uVar3,local_10);
  _xmlrpc_DECREF(local_10);
  }
  _xmlrpc_strfree(param_1);
  _xmlrpc_DECREF(local_14);
  }
  else {
  _xmlrpc_env_set_fault_formatted
  (piVar1,-502,"Call XML not a proper XML-RPC call.  %s",local_4);
  }
  // ...
  }
  

This function has one incoming reference, so that seems to be the handler we’re looking for. Here’s the abridged version of that function:
  
  
  int __cdecl
  CIPCRemoteControl::ProcessCall(CFastString *user_data, /* ... */,
  CIPCRemoteControl_SAuthParams *session_object) {
  // ...
  max_size = _xmlrpc_limit_get(1);
  if (size <= max_size) {
  _xmlrpc_env_init(&xml_env);
  // ...
  uVar3 = _xmlrpc_registry_process_call
  (&xml_env,*s_Internal,0,user_data->buffer, user_data->size
  s_AuthParams = (CIPCRemoteControl_SAuthParams *)0x0;
  // ... 
  return (uint)(local_c == 0);
  }
  FUN_00a4eff0(-509,"Request too big");
  return 0;
  }
  

Most of this function isn’t super interesting, but there are a couple of things we will need for our fuzzer.

First, the actual XML string is passed in the `user_data` parameter. The format used is a size field, followed by data. I’m oversimplifying it a bit here, but for all we care the input is a struct with these members:
  
  
  // struct CFastString * user_data:
  struct CFastString {
  int size;
  char * buffer;
  }
  

Second, there is also a `session_object` being passed to this function. Some more reversing will reveal that this is a pointer to an object that contains session metadata. Most of it is not relevant, but offset `0x10` in this object is where the authorization level is stored. Setting it to `0` gives this session permission to perform any XML-RPC call, which is perfect for our use case.

## Recap#

With all that out of the way, here is what our final harness will look like:

  1. Start at `CIPCRemoteControl::ProcessCall` by restoring a snapshot
  2. Inject a new input: 
  1. Update `size` and `buffer` for our newly generated input
  2. Edit `session_object` to bypass authentication 2
  3. Run until `CIPCRemoteControl::ProcessCall` returns

# LibAFL#

LibAFL is an amazing library for building odd fuzzers like this. As a user, you get to glue together a pretty advanced fuzzer in Rust (🦀🦀🦀🦀) and most of the hard parts are already taken care of. However, the codebase is still fairly new and changes often so expect to fix your fuzzer if you update LibAFL.

The fuzzer I ended up building is a mixture of the [qemu launcher example](https://github.com/AFLplusplus/LibAFL/tree/main/fuzzers/qemu_launcher) and [this LibAFL-based QuickJS fuzzer](https://github.com/andreafioraldi/libafl_quickjs_fuzzing). It uses Qemu for its coverage and snapshotting abilities, and Nautilus to generate the XML messages.

Instead of going through every component one by one, I’ll highlight a few interesting components. If you are looking for more LibAFL specifics, I’d recommend:

  * [epi052’s blog post series on libAFL, specifically part4](https://epi052.gitlab.io/notes-to-self/blog/2021-11-26-fuzzing-101-with-libafl-part-4/)
  * [The source code for this fuzzer, available on Github](https://github.com/RickdeJager/TrackmaniaFuzzer)

## Generic setup#

First things first, let’s get the server to boot in libafl_qemu:
  
  
  fn main() -> Result<(), Error> {
  // Trackmania will want to load stuff relative to their server dir.
  std::env::set_current_dir(std::path::Path::new("../Server")).unwrap();
  
  let args = vec![
  "qemu-i386".to_string(),
  SERVER_BINARY.to_string(),
  "/nodaemon".to_string(),
  "/lan".to_string(),
  "/nolog".to_string(),
  "/dedicated_cfg=dedicated_cfg.txt".to_string(),
  "/game_settings=MatchSettings/Nations/NationsGreen.txt".to_string(),
  ];
  
  let env: Vec<(String, String)> = Vec::new();
  let emu = Emulator::new(&args, &env);
  // Uncomment the next line to run the server
  // unsafe{ emu.run(); }
  // ...
  

There you go, we’re already running in Qemu! 😄

Next order of business; preparing the emulator for fuzzing. Set a breakpoint on `CIPCRemoteControl::ProcessCall` and run the emulator until it stops. At this point, we need to remove the breakpoint to prevent it from being hit over and over again. To trigger the breakpoint, just send any XML-RPC call.
  
  
  // ...
  emu.set_breakpoint(XML_RPC_CALL);
  unsafe { emu.run() };
  println!("RPC initialized");
  emu.remove_breakpoint(XML_RPC_CALL);
  // ...
  

Before Qemu takes its snapshot, we need to set up the binary as we discussed in Harnessing. Arguments are passed via the stack on i386, so we need to grab `esp` to read them.
  
  
  // ...
  let esp: u32 = emu.read_reg(Regs::Esp).unwrap();
  
  // Grab the two arguments we need, plus the return address
  let mut user_data = [0; 4];
  let mut session_object = [0; 4];
  let mut ret = [0; 4];
  unsafe {
  emu.read_mem(esp, &mut ret);
  emu.read_mem(esp + 4, &mut user_data); // arg1
  emu.read_mem(esp + 12, &mut session_object); // arg3
  }
  let ret = u32::from_le_bytes(ret);
  let user_data = u32::from_le_bytes(user_data);
  
  let session_object = u32::from_le_bytes(session_object);
  let session_auth = session_object + 0x10;
  // ...
  

Now that we have all the addresses we need, we can map a new input buffer and set up authorization. While we’re here, let’s also set a breakpoint on the return address of the handler.
  
  
  // ...
  let input_addr: u32 = emu
  .map_private(0, (2*MAX_XML_SIZE) as usize, MmapPerms::ReadWrite)
  .unwrap();
  println!("Mapped input buffer at {:x}", input_addr);
  
  let xml_size_p = user_data;
  let xml_data_p = user_data + 4;
  unsafe {
  // Edit the auth details in-place
  // 0 (God rights), 1 (SuperAdmin), 2 (Admin), 3 (User), 4 (Default)
  emu.write_mem(socket_auth, &0i32.to_le_bytes());
  // Set the data pointer to point to our mapped buffer
  emu.write_mem(xml_data_p, &input_addr.to_le_bytes());
  }
  // Set a breakpoint on the return address
  emu.set_breakpoint(ret);
  // ...
  

## The grammar#

Even without a grammar, you could easily find some bugs in this code base.3 This is a double-edged sword, the code base is _too_ buggy to fuzz without a grammar, and will throw assertion errors on non-valid XML 😅.  
While aborts make for annoying crash exploits, I’m sure we can do a lot better. By using a grammar, we can guarantee to only produce valid XML payloads, which helps in finding some deeper bugs.

### The XML-RPC format#

The TrackMania wiki provides a nice overview of [how the XML-RPC protocol is used in TrackMania](https://wiki.trackmania.io/en/dedicated-server/XML-RPC/gbxremote-protocol). Since our harness is set up to take care of the receiving, we just need to provide valid XML content. Here is an example of an XML-RPC message:
  
  
  <?xml version="1.0"?>
  <methodCall>
  <methodName>Authenticate</methodName>
  <params>
  <param><value>SuperAdmin</value></param>
  <param><value>SuperAdmin</value></param>
  </params>
  </methodCall>
  

As you can see there are some custom values we need to teach our grammar. Notably, the `methodName` to call, the (correct?) arguments, the value types and parameters etc.

### Generating the Nautilus grammar#

To generate XML messages, we need to write a grammar that tells Nautilus how to generate a valid message. There are two ways to do this in LibAFL; you either feed a grammar.json file to Nautilus, or you can provide a `Vec<Vec<String>>`. I chose to use the second option, because it allows me to generate the grammar from Rust, directly in the fuzzer.  
Again, I won’t bore you with all the details—you can find those on [Github](https://github.com/RickdeJager/TrackmaniaFuzzer)—but I will go over some of the interesting bits here.

We start our grammar with a root rule, with exactly one variable (`METHOD_CALL`).
  
  
  add_rule!(
  "RPC-CALL",
  "<?xml version=\"1.0\"?><methodCall>{METHOD_CALL}</methodCall>"
  );
  

Next, we need to define what a `METHOD_CALL` is. The short answer is that it’s a pair of a `methodName` and `params`. With a little reversing and some good old trial-and-error, I figured out that nothing interesting happens for an unknown `methodName` or incomplete `params`. I scraped the TrackMania wiki for a list of all method names and their arguments. With some regex magic, we can automatically add rules for each method with the correct arguments.

> _(note: a non-terminal is expressed as`{EXAMPLE}` in the grammar. However, if you see that notation in a `format!` macro, `{EXAMPLE}` will be substituted for the variable `EXAMPLE`. Keep this in mind for the next few code snippets, otherwise, they will be somewhat confusing)_
  
  
  let method_re = Regex::new(r"\w+ (.*)\((.*)\)").unwrap();
  for line in include_str!("grammar_data/methods-arg.list").lines() {
  // Extract method name and types
  let caps = method_re.captures(line).unwrap();
  let method_name = caps.get(1).unwrap().as_str();
  let args = caps.get(2).unwrap().as_str();
  let args: Vec<&str> = match args.is_empty() {
  true => Vec::new(),
  false => args.split(", ").collect(),
  };
  
  // prepare parameters
  let mut params = "".to_string();
  for arg in args {
  let typed_rule = match arg {
  // Map the regex match to a token for our grammar
  "int" => "{INT_VALUE}",
  "double" => "{DOUBLE_VALUE}",
  "string" => "{STRING_VALUE}",
  "boolean" => "{BOOLEAN_VALUE}",
  "struct" => "{STRUCT_VALUE}",
  "array" => "{ARRAY_VALUE}",
  "base64" => "{BASE64_VALUE}",
  x => unreachable!("Unexpected type: >{}<", x),
  };
  params.push_str(&format!("<param>{typed_rule}</param>"));
  }
  
  // Add a rule for this method
  add_rule!(
  "METHOD_CALL",
  format!("<methodName>{method_name}</methodName><params>{params}</params>")
  )
  }
  

Okay, that was a bit much, but also covers a ton of messages already. The rest of the grammar is dedicated to adding values for each type we just defined (`{INT_VALUE}`, …). Most of them are simple, for example `{INT_VALUE}` is defined as:
  
  
  <value><i4>{INT}<i4></value>
  

And in turn, an `{INT}` is one or more digits. You can either do this fully recursively or define a few rules manually. The latter keeps the numbers fairly low, which makes more sense for this application. For convenience, I defined a `{NATURAL_NUMBER}` subrule here, so we can reuse it for doubles as well.
  
  
  // Integers
  for elem in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] {
  add_rule!("DIGIT", elem);
  }
  add_rule!("INT", "");
  add_rule!("INT", "{NATURAL_NUMBER}");
  add_rule!("INT", "-{NATURAL_NUMBER}");
  add_rule!("NATURAL_NUMBER", "{DIGIT}");
  add_rule!("NATURAL_NUMBER", "{DIGIT}{DIGIT}");
  add_rule!("NATURAL_NUMBER", "{DIGIT}{DIGIT}{DIGIT}");
  

Now you just have to go through and repeat the process for every defined type. Make sure to include some special values that may have meaning. For example, I included these constants for my `{STRING}` type to trigger format string bugs:
  
  
  "%999999s", "%99 ", "%0999d", "http://", "gbx://"
  

The only painful value to generate is the `{STRUCT}`. It’s also one of the most important values to get right if you want to get decent coverage. A struct consists of one or more named members. I dumped the valid member names from the binary by hand and added rules for each member.

## Harness#

We’ve already done most of the heavy lifting for our harness in the setup part. The last thing we need to do is update the size field, and inject the input.  
Nautilus generates its inputs in a special format. To inject the input, we first need to “unparse” it into a `Vec<u8>`. Once we have the raw bytes stored in `buf`, they can be injected directly into the memory of the target process.
  
  
  let mut run_client = |state: Option<_>, mut mgr, _core_id| {
  let mut buf = vec![];
  // The wrapped harness function
  let mut harness = |input: &NautilusInput| {
  // Convert the NautilusInput into raw bytes,
  // skipping inputs that are too large.
  if !grammar::unparse_bounded(&context, input, 
  &mut buf, MAX_XML_SIZE as usize) {
  return ExitKind::Ok;
  }
  
  unsafe {
  // Write our data into the expected format
  emu.write_mem(input_addr, &buf);
  let len_u32 = buf.len() as u32;
  emu.write_mem(xml_size_p, &len_u32.to_le_bytes());
  
  // Run the emulator until next BP
  emu.run();
  }
  
  ExitKind::Ok
  };
  // ...
  }
  

# Letting it rip#

Within seconds of starting the fuzzer, you’ll find dozens of crashes (objectives) rolling out. Great! But if you open one, you’ll notice it looks like mostly garbage data. That is because LibAFL saved the NautilusInput – the thing the mutator spits out – not the unparsed input we injected.

## Repro mode#

With a bit more code, we can loop over the saved crashes and convert each NautilusInput back to a concrete crash file. In our case, that just means we get the plain XML files as output. The actual code is very similar to the unparse step we performed in the harness:
  
  
  // Take the entire output directory, copy all files over to a concrete directory.
  fn create_concrete_outputs(context: &NautilusContext) {
  let crashes = std::fs::read_dir(CRASH_DIR).expect("Failed to read crashes");
  let out_dir = PathBuf::from(CRASH_DIR_CONCRETE);
  let mut tmp = vec![];
  for path in crashes {
  let path = path.unwrap().path();
  // Skip libafl lock files
  if path.extension().unwrap_or_else(|| std::ffi::OsStr::new(""))
  == "lafl_lock" {
  continue;
  }
  // Check if this file was already converted.
  let out_file = out_dir.join(path.file_name().unwrap());
  if !out_file.exists() {
  let input = NautilusInput::from_file(path)
  .expect("Failed to create NautilusInput");
  grammar::unparse_bounded(&context, &input, &mut tmp,
  MAX_XML_SIZE as usize);
  
  std::fs::write(&out_file, &tmp).expect("Failed to write file contents");
  println!("Converted {:?}", &out_file);
  }
  }
  }
  

## Format string bugs, as far as the eye can see…#

Using the new repro mode we just added, we can start looking at some objectives. For example, here’s one of the crashing inputs that the fuzzer found:
  
  
  <?xml version="1.0"?>
  <methodCall>
  <methodName>GetChallengeInfo</methodName>
  <params>
  <param>
  <value>%999999s</value>
  </param>
  </params>
  </methodCall>
  

While this bug is probably already exploitable, it is still a pretty simple fuzz case. All the mutator has to do is select a “methodName” that will produce an error, slap a pre-specified token in there to test for printf bugs, and boom. This crash occurs so often that it stops us from getting any other meaningful coverage.

## ““fixing”” the format string bug#

To find some deeper bugs, we first need to patch the format string bug. I’m still interested in `sprintf` bugs and the like, so I don’t just want to remove all `%`’s from my grammar. The cleanest way to patch the bug is to just disable printing to stdout entirely. The server already has a “daemon” mode that does exactly this, but I’d rather not run the binary in daemon mode to avoid threading issues.

With some more reversing, I found two writes that seem to be responsible for “silencing” the binary when you enable daemon mode.
  
  
  // ...
  ppid = ___getpid();
  ___fprintf(stdout,"Trackmania server daemon started with pid=%d (parent=%d).\n",
  pid,ppid);
  g_exit_code = 1;
  g_silent_flag = 1;
  *(undefined4 *)(g_server_obj + 0x4c) = 0;
  return;
  // ...
  

I added those to the initial setup of my fuzzer and what do you know? No more log output!
  
  
  // Silence the binary, as if we were in daemon mode
  unsafe {
  // Write a 1 to the global I named `g_silent_flag`
  emu.write_mem(0x08ce05e0u32, &1u32.to_le_bytes());
  // Find the server object ...
  let mut g_server_obj = [0; 4];
  emu.read_mem(0x08cbaab4u32, &mut g_server_obj);
  let g_server_obj = u32::from_le_bytes(g_server_obj);
  // ... and set a flag on it to 0
  emu.write_mem(g_server_obj+0x4cu32, &0u32.to_le_bytes());
  }
  

## finding more subtle bugs#

Now that we don’t crash Trackmania on nearly every try, we actually get to explore and find some more subtle bugs. I didn’t find anything super damning, but my favorite crash is this one:
  
  
  <?xml version="1.0"?>
  <methodCall>
  <methodName>ForceSpectatorTargetId</methodName>
  <params>
  <param>
  <value>
  <i4>-1</i4>
  </value>
  </param>
  <param>
  <value>
  <i4>-1</i4>
  </value>
  </param>
  <param>
  <value>
  <i4>2</i4>
  </value>
  </param>
  </params>
  </methodCall>
  

Our fuzzer found that! Isn’t that neat?  
It becomes even cooler once you start to root cause the bug. If you lookup the specification for the method, you’ll recognize the magic numbers that our fuzzer found:

> “Force spectators to look at a specific player. You have to pass the id of the spectator (or -1 for all) and the id of the target (or -1 for automatic), and an integer for the camera type to use (-1 = leave unchanged, 0 = replay, 1 = follow, 2 = free). Only available to Admin.

With a bit of digging, I found that the bug occurs when you try to force freecam on all spectators. The game tries to check the game version of the spectator, which doesn’t exist because we didn’t specify one. This can only be triggered by an admin, so it is not a super critical bug. It’s cool because all of these parameters had to be set correctly to hit this edge case.

A cleaned-up set of crashing fuzz cases can [be found here](https://github.com/RickdeJager/TrackmaniaFuzzer/tree/main/ExampleCrashes). For these, I manually went through the output of the fuzzer, minimized and cleaned up the payload, and linted the XML for readability.

# Conclusion#

While I was hoping for some more bugs, I’m still happy with the results. The main pitfall is that these RPC calls are a lot simpler, and a lot more generic than I expected. Most of the unpacking is done once by a helper function. After that, the actual calls themselves are quite simple.

Nevertheless, I was able to exploit the printf bug for Remote Code Execution in [part 2 of this series](../part2/).

## Useful links#

  * <https://github.com/EvoTM/awesome-trackmania>
  * <https://wiki.xaseco.org/wiki/ManiaPlanet_internals>
  * <https://en.wikipedia.org/wiki/XML-RPC>
  * <https://wiki.trackmania.io/en/dedicated-server/XML-RPC/Methods>

* * *

  1. For people following along at home, I’m running `TmForever v2011-02-21` (sha256: 2402c87885c3a44b6e8500d06b052bfc9c4159b3239dd0eab8424b98d52ed4d1) ↩︎

  2. Okay, I lied. I’m only going to do this once and just include the spoofed session in the snapshot. I left it in here because I think it’s a nice example in case your use case _does_ require a slightly more complicated harness. ↩︎

  3. Spoilers, but I’ve found the same format string bug by just generating a seed set of XML RPC messages and mutating that with a dictionary. ↩︎

  * [Poc](https://blog.bricked.tech/tags/poc/)
  * [Writeup](https://blog.bricked.tech/tags/writeup/)
  * [Real-World](https://blog.bricked.tech/tags/real-world/)

  * [ ](https://x.com/intent/tweet/?text=Hacking%20TMNF%3a%20Part%201%20-%20Fuzzing%20the%20game%20server&url=https%3a%2f%2fblog.bricked.tech%2fposts%2ftmnf%2fpart1%2f&hashtags=poc%2cwriteup%2creal-world)
  * [ ](https://www.linkedin.com/shareArticle?mini=true&url=https%3a%2f%2fblog.bricked.tech%2fposts%2ftmnf%2fpart1%2f&title=Hacking%20TMNF%3a%20Part%201%20-%20Fuzzing%20the%20game%20server&summary=Hacking%20TMNF%3a%20Part%201%20-%20Fuzzing%20the%20game%20server&source=https%3a%2f%2fblog.bricked.tech%2fposts%2ftmnf%2fpart1%2f)
  * [ ](https://reddit.com/submit?url=https%3a%2f%2fblog.bricked.tech%2fposts%2ftmnf%2fpart1%2f&title=Hacking%20TMNF%3a%20Part%201%20-%20Fuzzing%20the%20game%20server)
  * [ ](https://facebook.com/sharer/sharer.php?u=https%3a%2f%2fblog.bricked.tech%2fposts%2ftmnf%2fpart1%2f)
  * [ ](https://api.whatsapp.com/send?text=Hacking%20TMNF%3a%20Part%201%20-%20Fuzzing%20the%20game%20server%20-%20https%3a%2f%2fblog.bricked.tech%2fposts%2ftmnf%2fpart1%2f)
  * [ ](https://telegram.me/share/url?text=Hacking%20TMNF%3a%20Part%201%20-%20Fuzzing%20the%20game%20server&url=https%3a%2f%2fblog.bricked.tech%2fposts%2ftmnf%2fpart1%2f)
  * [ ](https://news.ycombinator.com/submitlink?t=Hacking%20TMNF%3a%20Part%201%20-%20Fuzzing%20the%20game%20server&u=https%3a%2f%2fblog.bricked.tech%2fposts%2ftmnf%2fpart1%2f)
