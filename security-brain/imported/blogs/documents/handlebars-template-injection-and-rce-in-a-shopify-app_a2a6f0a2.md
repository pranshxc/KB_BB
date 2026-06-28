---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-04_handlebars-template-injection-and-rce-in-a-shopify-app.md
original_filename: 2019-04-04_handlebars-template-injection-and-rce-in-a-shopify-app.md
title: Handlebars template injection and RCE in a Shopify app
category: documents
detected_topics:
- command-injection
- supply-chain
- xss
- api-security
tags:
- imported
- documents
- command-injection
- supply-chain
- xss
- api-security
language: en
raw_sha256: a2a6f0a2b7a6e4977380d3febdadde65e15cc28977cb533e5474374e3efe3cac
text_sha256: 8d62f8fd2f13c03abe18daa496a55e47881c0c6f516523e8635abca5fba0085a
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Handlebars template injection and RCE in a Shopify app

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-04_handlebars-template-injection-and-rce-in-a-shopify-app.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, xss, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `a2a6f0a2b7a6e4977380d3febdadde65e15cc28977cb533e5474374e3efe3cac`
- Text SHA256: `8d62f8fd2f13c03abe18daa496a55e47881c0c6f516523e8635abca5fba0085a`


## Content

---
title: "Handlebars template injection and RCE in a Shopify app"
url: "https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html"
final_url: "https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html"
authors: ["Mahmoud Gamal (@Zombiehelp54)"]
programs: ["Shopify"]
bugs: ["SSTI", "RCE"]
bounty: "10,000"
publication_date: "2019-04-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5329
---

###  Handlebars template injection and RCE in a Shopify app 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

[ April 04, 2019  ](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html "permanent link")

  

##  TL;DR

We found a zero-day within a JavaScript template library called handlebars and used it to get Remote Code Execution in the Shopify Return Magic app.  
  

##  The Story:

In October 2018, Shopify organized the HackerOne event "H1-514" to which some specific researchers were invited and I was one of them. Some of the Shopify apps that were in scope included an application called "Return Magic" that would automate the whole return process when a customer wants to return a product that they already purchased through a Shopify store.  
  
Looking at the application, I found that it has a feature called Email WorkFlow where shop owners can customize the email message sent to users once they return a product. Users could use variables in their template such as {{order.number}} , {{email}} ..etc. I decided to test this feature for Server Side Template injection and entered {{this}} {{self}} then sent a test email to myself and the email had [object Object] within it which immediately attracted my attention.  
  
So I spent a lot of time trying to find out what the template engine was, I searched for popular NodeJs templates and thought the template engine was mustache (wrong), I kept looking for mustache template injection online but nothing came up as Mustache is supposed to be a logicless template engine with no ability to call functions which made no sense as I was able to call some Object attributes such as {{this.__proto__}} and even call functions such as {{this.constructor.constructor}} which is the Function constructor. I kept trying to send parameters to this.constructor.constructor() but failed.  
  
I decided that this was not vulnerable and moved on to look for more bugs. Then the fate decides that this bug needs to be found and I see a message from Shopify on the event slack channel asking researchers to submit their "almost bugs" so if someone found something and feels it's exploitable, they would send the bug to Shopify security team and if the team manages to exploit it the reporter will get paid as if they found it. Immediately I sent my submission explaining what I have found and at the impact section I wrote "Could be a Server Side template injection that can be used to take over the server ¯\\_(ツ)_/¯".  
  
Two months passed and I got no response from Shopify regarding my "almost bug" submission, then I was invited to another hacking event in Bali hosted by Synack. There I met the Synack Red Team and after the Synack event has ended, I was supposed to travel back to Egypt, but only 3 hours before the flight I decided to extended my stay for three more days then fly from Bali to Japan where I was supposed to participate in the TrendMicro CTF competition with my CTF team. Some of the SRT also decided to extend their stay in Bali. One of those was Matias so I contacted him to hangout together. After swimming in the ocean and enjoying the beautiful nature of Bali, we went to a restaurant for dinner where Matias told me about a bug he found in a bug bounty program that had something to do with JavaScript sandbox escape so we spent all night missing with objects and constructors, but unfortunately we couldn't escape the sandbox.  
  
I couldn't take constructors out of my head and I remembered the template injection bug I found in Shopify. I looked at the HackerOne report and thought that the template can't be mustache so I installed mustache locally and when I parsed {{this}} with mustache it actually returns nothing which is not the case with the Shopify application. I searched again for popular NodeJs template engines and I found a bunch of them, I looked for those that used curly brackets {{ }} for template expressions and downloaded them locally, one of the libraries was handlebars and when I parsed {{this}} it returned [object Object] which is the same as the Shopify app. I looked at handlebars documentation and found out that it's also supposed to not have much logic to prevent template injection attacks. But knowing that I can access the function constructor I decided to give it a try and see how I can pass parameters to functions.  
  
After reading the documentation, I found out that in handlebars developers can register functions as helpers in the template scope. We can pass parameters to helpers like this {{helper "param1" "param2" ...params}}. So the first thing I tried was {{this.constructor.constructor "console.log(process.pid)"}} but it just returned console.log(process.pid) as a string. I went to the source code to find out what was happening. At the runtime.js file, there was the following function:  
  
So what this function does is that it checks if the current object is of type 'function' and if so it just calls it using current.call(context) where context is the template scope, otherwise, it would just return the object itself.  
  
I looked further in the documentation of handlebars and found out that it had built in helpers such as "with", "blockHelperMissing", "forEach" ...etc  
  
After reading the source code for each helper, I had an exploitation in mind using the "with" helper as it is used to shift the context for a section of a template by using the built-in with block helper. So I would be able to perform curren.call(context) on my own context. So I tried the following:  
  
Basically that should pass console.log(process.pid) as the current context, then when the handlebars compiler reaches this.constructor.constructor and finds that it's a function, it should call it with the current context as the function argument. Then using {{#with this}} we call the returned function from the Function constructor and console.log(process.pid) gets executed.  
  
However, this did not work because function.call() is used to invoke a method with an owner object as an argument, so the first argument is the owner object and other arguments are the parameters sent to the function being called. So if the function was called like current.call(this, context), the previous payload would have worked.  
  
I spent two more nights in Ubud then flew to Tokyo for the TrendMicro CTF. Again in Tokyo, I couldn't take objects and constructors out of my mind and kept trying to find a way to escape the sandbox.  
  
I had another idea of using Array.map() to call Function constructor on my context, but it didn't work because the compiler always passes an extra argument to any function I call which is an object containing the template scope which causes an error as my payload is considered a function argument not the function body.  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiMujYnFAeaBgUip4mEusio-ur-EOpn-gQQ6cxhETQ3S_xw4eGYRPeLko9nAIMv2eWXhwGl-aJk6GDRjCYLOB-zozeApPFBbuYa2jeA8gVEgTcci4hAS3Jec3P0ZX4VcbpqUVjJhcsY2vhu/s1600/Screen+Shot+2019-04-01+at+10.50.40+PM.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiMujYnFAeaBgUip4mEusio-ur-EOpn-gQQ6cxhETQ3S_xw4eGYRPeLko9nAIMv2eWXhwGl-aJk6GDRjCYLOB-zozeApPFBbuYa2jeA8gVEgTcci4hAS3Jec3P0ZX4VcbpqUVjJhcsY2vhu/s1600/Screen+Shot+2019-04-01+at+10.50.40+PM.jpg)

  
There seemed to be many possible ways to escape the sandbox but I had one big problem facing me which is that whenever a function is called within the template, the template compiler sends the template scope Object as the last parameter.  
  
For example, if I try to call something like constructor.constructor("test","test"), the compiler will call it like constructor.constructor("test", "test", this) and this will be converted to a string by calling Object.toString() and the anonymous function created will be:  
which will cause an error.  
  
I tried many other things but still no luck, then I decided to open the JavaScript documentation for Object prototype and look for something that could help escape the sandbox.  
  
I found out that I could overwrite the Object.prototype.toString() function using Object.prototype.defineProperty() so that it calls a function that returns a user controlled string (my payload).  
  
Since I can't define functions using the template, all I have to do is to find a function that is already defined within the template scope and returns a user controlled input.  
  
For example, the following nodejs application should be vulnerable:  
test.js  
example.html  
  
Now if you run this template, console.log(process.pid) gets executed.  
I reported that to Shopify and mentioned that if there was a function within the scope that returns a user controlled string, it would have been possible to get RCE.  
  
Later, when I met Ibrahim (@the_st0rm) I told him about my idea and he told me that I can use bind() to create a new function that when called will return my RCE payload.  
From JavaScript documentation:  
  
` The bind() method creates a new function that, when called, has its this keyword set to the provided value, with a given sequence of arguments preceding any provided when the new function is called.  
`  
  
So now the idea is to create a string with whichever code I want to execute then bind its toString() to a function using bind() after that overwrite the Object.prototype.toString() function with that function.  
  
I spent a lot of time trying to apply this using handlebars templates, and eventually during my flight back to Egypt I was able to get a fully working PoC with no need to use functions defined in the template scope.  
  
  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZgfGjx4gINW6O_cVPLw82gIZFy9Zpw146TIRu0OfBiE_W6MqrNAe4CHFERb3rHGccPIc-l0KpQia1Lgzg8Gu6hj-BX2ZXmJt6IPdigexxd4QShVzq1BUgxC5bgbV1wT84W0h8PP2QESN7/s1600/Screen+Shot+2019-04-02+at+12.38.24+AM.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZgfGjx4gINW6O_cVPLw82gIZFy9Zpw146TIRu0OfBiE_W6MqrNAe4CHFERb3rHGccPIc-l0KpQia1Lgzg8Gu6hj-BX2ZXmJt6IPdigexxd4QShVzq1BUgxC5bgbV1wT84W0h8PP2QESN7/s1600/Screen+Shot+2019-04-02+at+12.38.24+AM.jpg)

Basically, what the template above does is:  
  
And when I tried it with Shopify, I got:  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHF99IpwEXrNTpBOocrgPKwkq0EV86nMRw55ca0zytoqC1he-dTPmF5pEyRNqNVG-8WSnefCnenAiUW4dYb99cG5OGOr2LpSVVTBLzFCr6kx51B5CLGTjY90GIxgPGsPpVbWJlpRiubnub/s1600/Screen_Shot_2018-12-16_at_6.56.00_PM.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHF99IpwEXrNTpBOocrgPKwkq0EV86nMRw55ca0zytoqC1he-dTPmF5pEyRNqNVG-8WSnefCnenAiUW4dYb99cG5OGOr2LpSVVTBLzFCr6kx51B5CLGTjY90GIxgPGsPpVbWJlpRiubnub/s1600/Screen_Shot_2018-12-16_at_6.56.00_PM.jpg)

  
Matias also texted me with an exploitation that he got which is much simpler than the one I used:  
  
With that said, I was able to get RCE on Shopify's Return Magic application as well as some other websites that used handlebars as a template engine.  
  
The vulnerability was also submitted to npm security and handlebars pushed a fix that disables access to constructors. The advisory can be found here: <https://www.npmjs.com/advisories/755>  

##  In a nutshell

You can use the following to inject Handlebars templates:  
  

  
Matias also had his own exploitation that is much simpler:  
  
Sorry for the long post, if you have any questions please drop me a tweet [@Zombiehelp54](https://twitter.com/Zombiehelp54)

[javascript](https://mahmoudsec.blogspot.com/search/label/javascript) [nodejs](https://mahmoudsec.blogspot.com/search/label/nodejs) [sandbox](https://mahmoudsec.blogspot.com/search/label/sandbox)

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

  1. ![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEij5LsvD1iUHMlIk8Sutm8H_rdVxLfYVAJ1ydG08nqJnED8cwBk2tzIoeGFf8OaxAj5h1dPbdCjMumPXXvnkkx-0RP2oMvac4G-Mbop7FrgmbGHi_lFtgmgv6-PUdAlfg/s45-c/IMG_20200723_190548.jpg)

[Mahmoud NourEldin](https://www.blogger.com/profile/03323345687035377784)[April 4, 2019 at 11:13 AM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1554401608050#c8330072682947425366)

Wow, very interesting blog

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/8330072682947425366)

Replies

Reply

  2. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Ahiezer](https://www.blogger.com/profile/05087025833749110426)[April 4, 2019 at 1:22 PM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1554409322260#c1908558410239597105)

Wow, fantastic word.

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/1908558410239597105)

Replies

Reply

  3. ![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiLX_4JrKxfpgCGLJW-0KCCJ-N-1buHcEn_1AuyTftmtKCUUYr_5zZ1yIz0erQ24n0UknpfmtFrGchFQ7kui9Y1ND_Phg6KsfNJoKVRkoTq3Pqme1S8RoJuApGgsRckSg/s45-c/15+-+1+%285%29.jpg)

[NINAD SARANG](https://www.blogger.com/profile/11022084178113509326)[April 6, 2019 at 10:18 AM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1554571091907#c8846725776341730190)

nice finding. keep it up and keep posting such interesting issues

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/8846725776341730190)

Replies

Reply

  4. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Unknown](https://www.blogger.com/profile/17115657838655629925)[April 7, 2019 at 8:05 PM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1554692705670#c7193971441374468071)

the 2nd  
  
`{{#with (string.sub.apply 0 codelist)}}`  
  
its right?  
  
i think its should be `{{#with (this.apply 0 codelist)}}`

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/7193971441374468071)

Replies

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Mahmoud Gamal](https://www.blogger.com/profile/07210431214489547529)[April 8, 2019 at 10:06 AM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1554743190285#c824017851188933754)

When the template compiler calls `apply()` it calls it on the current context, which in this case is `conslist[0]` which is the function constructor. So the way you call `apply()` doesn't really matter as the compiler will always call it on the current context.  
Matias used `#each` helper to shift the context for the section where `apply()` is called to the Function constructor.  
Btw it wouldn't have been possible to use `#with` as the with helper has the following line in its implementation:  
'''  
if (_utils.isFunction(context)) {  
context = context.call(this);  
}  
'''  
Basically what this does is that it checks if the context is a function, and if so it calls it and sets the context to whichever the function returns and in that case it will be an anonymous function returned by the function constructor rather than the Function constructor itself.  
In my exploit, I used `#blockHelperMissing` which does the same thing as `#with` except that it doesn't have the `_utils.isFunction(context)` check.  
  
Thanks for the question.  
  

[Delete](https://www.blogger.com/comment/delete/277132840497237240/824017851188933754)

Replies

Reply

  2. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Mahmoud Gamal](https://www.blogger.com/profile/07210431214489547529)[April 8, 2019 at 10:08 AM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1554743282328#c6755197828110879939)

Your comment actually made me rethink about how I used `apply()` to call `bind()` in my initial exploit. I should have just used `bind()` the same way `apply()` was used (by shifting the context to `str.toString`). I've modified the exploit so it becomes more clean and easy to understand.  
  
Thanks again, Unknown person!  
  

[Delete](https://www.blogger.com/comment/delete/277132840497237240/6755197828110879939)

Replies

Reply

  3. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Balla](https://www.blogger.com/profile/17892820044874189553)[May 26, 2020 at 5:49 AM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1590497363474#c6623176083008964129)

Hi bro ... i found a company using handlebars with this same version ..can u send me your poc pls..  

[Delete](https://www.blogger.com/comment/delete/277132840497237240/6623176083008964129)

Replies

Reply

Reply

  5. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[aymen azer](https://www.blogger.com/profile/16769629299660361203)[April 8, 2019 at 2:35 PM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1554759308321#c8031768506175604994)

السلام عليكم اخي انا اريد ان اصبح باحث امني ارجو ان تساعدني باجوبة بسيطة اريد مسدر لتعلم الثغرات البرمجية و ما هي لغات البرمجة التي احتاجها مع العلم اني عندي خلفية بسيطة في الجافا و c++ و الاسامبلي

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/8031768506175604994)

Replies

Reply

  6. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[c0d3r.b0y](https://www.blogger.com/profile/14790775478741369930)[June 10, 2019 at 3:26 AM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1560162393615#c4317639525742623916)

Great finding. I have been recently finding a most secure template engine for node.js. I went through all and most of them are not sandboxed i.e. allows RCE easily. Is it fixed by handlebars ?

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/4317639525742623916)

Replies

Reply

  7. ![](//resources.blogblog.com/img/blank.gif)

Anonymous[July 16, 2019 at 5:34 AM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1563280470062#c276333820978644229)

it'll be nice to know which versions you've been referring to. RCE and XSS are not new to handlebars; were they using an outdated version?  
The link you referred to dates back to 2016, but your blog is in 2019.  
Great post btw! Thanks for sharing the details!  

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/276333820978644229)

Replies

  1. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Mahmoud Gamal](https://www.blogger.com/profile/07210431214489547529)[July 17, 2019 at 4:35 AM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1563363341675#c4565706720046034017)

Versions of handlebars prior to 4.0.14 were vulnerable. Also, the link date is Feb 14th, 2019. 

[Delete](https://www.blogger.com/comment/delete/277132840497237240/4565706720046034017)

Replies

Reply

Reply

  8. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[MS Dynamics](https://www.blogger.com/profile/06314770845829180340)[November 6, 2019 at 1:34 AM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1573032843168#c2235459889999169582)

Thanks for posting. Its an Important topic to be read.[Node JS training in hyderabad](https://www.visualpath.in/Node-js-online-training.html)  

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/2235459889999169582)

Replies

Reply

  9. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Data science ](https://www.blogger.com/profile/06807799679980324911)[November 28, 2019 at 1:49 AM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1574934551418#c3563380899412588094)

This is great information and all relevant to me. I know when I engage with my readers on my blog posts, not only does it encourage others to leave comments, but it makes my blog feel more like a community – exactly what I want!  
[Data Science Training in Hyderabad](http://www.rstrainings.com/data-science-online-training.html)  
  
[Hadoop Training in Hyderabad](http://www.rstrainings.com/hadoop-online-training.html)  
  
[Java Training in Hyderabad](http://www.rstrainings.com/java-online-training.html)  
  
[Python online Training in Hyderabad](http://www.rstrainings.com/python-online-training.html)  
  
[Tableau online Training in Hyderabad](http://www.rstrainings.com/tableau-online-training.html)  
  
[Blockchain online Training in Hyderabad](http://www.rstrainings.com/blockchain-online-training.html)  
  
[informatica online Training in Hyderabad](http://www.rstrainings.com/informatica-online-training.html)  
  
[devops online Training](http://www.rstrainings.com/devops-online-training.html)

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/3563380899412588094)

Replies

Reply

  10. ![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjUAzASw4jIDDNN0iESQbWkz1U1h2Jg-l2tGTzcsfJFlheUNud_VHFU8MO8k2Mv7xYkd0yo7AjJfVQeQNbE8sAjWqszXht19XGSIDq3aHkVsUQ0dIX-14n25bmgBz3NqA/s45-c/why-sirt-is-the-best-college-removebg-preview.png)

[Priya](https://www.blogger.com/profile/08857276639634575138)[December 14, 2019 at 3:17 AM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1576322277814#c2200949760688315693)

I like your post very much. It is very much useful for everyone. I hope you will share more info about this.  
[ Node JS Online training](https://www.visualpath.in/Node-js-online-training.html)  
[ Node JS training in Hyderabad](https://www.visualpath.in/Node-js-online-training.html)  

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/2200949760688315693)

Replies

Reply

  11. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[rtusharkumarrastogi](https://www.blogger.com/profile/17523047820737486405)[January 13, 2020 at 9:13 PM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1578978806299#c4536730386813094828)

Welcome to the world of develop for MSK clinic.Best services provider in clinic. We provide genuine likes, followers and views to your Ultrasound guided injection.  
Regards  
[Ultrasound guided injection](https://www.kentmskclinic.co.uk/ultrasound-guided-injections/)

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/4536730386813094828)

Replies

Reply

  12. ![](//blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhzx-yMNXDCL9CuUbbQJoXWOBCQ4DYXOYRVt0wiPCXZikNl1sm8ZjfheqesDV08dVi47p9_Rc0dfX8dPLZJvGHHAX5KaNFEl1RMV7sQPKookaRejDG6LB116VRy6P8hbA/s45-c/286a8a5.jpg)

[Atul](https://www.blogger.com/profile/00753873762433078285)[February 6, 2020 at 11:32 PM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1581060755556#c1297137560539612958)

  
It was great experience after reading this. thanks for sharing such good stuff with us.  
[JavaScript Institute in Delhi](https://javascript-training-course-delhi.site123.me/)  

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/1297137560539612958)

Replies

Reply

  13. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Pankaj](https://www.blogger.com/profile/16104862098308527463)[February 7, 2020 at 2:15 AM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1581070518049#c3751814293192167157)

This comment has been removed by the author.

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/3751814293192167157)

Replies

Reply

  14. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Buy Adderall Online-Adderall Online(Generic Adderall Online))](https://www.blogger.com/profile/17486334202025759621)[February 15, 2020 at 1:59 AM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1581760773296#c3608616620899618825)

If you are feeling very depressed, have any panic disorders, Mental Stress, Anxiety Disorders visit the page and resolve all these problams and also New Year Offer begain offer limited period.  
Call Now For Buy Anxiety Medicines at very cheap price as compair to other dealer: +1-850-424-1335  
Website: <https://redditpharma.com/product/adderall-dosage/>  
<https://redditpharma.com/product/ambien-dosage/>  
<https://redditpharma.com/buy-alprazolam-online/>  
<https://redditpharma.com/buy-hydrocodone-online/>  
<https://redditpharma.com/buy-oxycodone-online/>  
<https://redditpharma.com/buy-codeine-online/>  

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/3608616620899618825)

Replies

Reply

  15. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[seojonsmith](https://www.blogger.com/profile/00930122964712009272)[February 24, 2020 at 1:08 AM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1582535318697#c8867341050040492845)

Buy highest quality generic drugs, xanax online, SSD chemical solution Online, with fast & free services.

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/8867341050040492845)

Replies

Reply

  16. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Mexicanpills](https://www.blogger.com/profile/15083070674847932614)[February 24, 2020 at 2:17 AM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1582539434277#c4619635471680002250)

Amazing post. Thanks  
  
[Buy Xanax Online](https://mexicanpills.us/product-category/buy-xanax-online/)  

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/4619635471680002250)

Replies

Reply

  17. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[Buy Adderall Online-Adderall Online(Generic Adderall Online))](https://www.blogger.com/profile/17486334202025759621)[February 26, 2020 at 4:11 AM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1582719087664#c8093707299680017032)

topmedsreview: Provide the best information about anxiety, panic disorder, mental stress, depression, Hyperactivitys issuse. Top meds review is a social platform providing the best medical information, medicine review, and health guidance. Our website provides credible information, depth reference material about health subjects that matter to everyone.  
  
[Anxiety Medicines](https://www.topmedsreview.com/)  
[Soma Addiction](https://www.topmedsreview.com/soma-addiction/)  
[Types Of Xanax Bars](https://www.topmedsreview.com/types-of-xanax-bars/)

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/8093707299680017032)

Replies

Reply

  18. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[SaiRangaTracedeals](https://www.blogger.com/profile/04912463086567401002)[March 16, 2020 at 4:38 AM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1584358705697#c3450350284985165376)

Thanks for sharing this article. Save you huge money & time. Download the Tracedeals Online Deals & Coupons&Sign In to get daily alerts from your favorite stores  
[Offers,Coupons & Deals App](https://tracedeals.page.link/app)  
[Coupons and Offers App for Shopping Online](https://tracedeals.page.link/app)  
[Online Shopping Deals & Coupons App](https://tracedeals.page.link/app)  
[Online Shopping Offers & Coupons App](https://tracedeals.page.link/app)  

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/3450350284985165376)

Replies

Reply

  19. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[dhramik](https://www.blogger.com/profile/04662952961975439793)[March 22, 2020 at 12:12 AM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1584861161559#c3205425993301547225)

The New Modern JavaScript Boot camp Course (2020) [ProgrammingFree course ](https://worldwebcourse.online/the-new-modern-javascript-bootcamp-course-2020/)

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/3205425993301547225)

Replies

Reply

  20. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[kazzouzi](https://www.blogger.com/profile/08982166774634238549)[May 20, 2020 at 4:56 AM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1589975773817#c7546749027392248396)

to execute shell command use  
{{this.push "return require('child_process').execSync('ls -la');"}}

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/7546749027392248396)

Replies

Reply

  21. ![](//www.blogger.com/img/blogger_logo_round_35.png)

[mors](https://www.blogger.com/profile/10723311206636603055)[July 4, 2020 at 9:11 PM](https://mahmoudsec.blogspot.com/2019/04/handlebars-template-injection-and-rce.html?showComment=1593922301096#c8488397382892320858)

عااااااااااااااااااااااااااااااااااااااش

Reply[Delete](https://www.blogger.com/comment/delete/277132840497237240/8488397382892320858)

Replies

Reply

Add comment

Load more...

#### Post a Comment

[](https://www.blogger.com/comment/frame/277132840497237240?po=1508108208797849527&hl=en&saa=85391&origin=https://mahmoudsec.blogspot.com&skin=contempo)
