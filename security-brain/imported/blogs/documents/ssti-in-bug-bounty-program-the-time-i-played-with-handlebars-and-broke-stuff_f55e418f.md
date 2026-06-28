---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-09-05_ssti-in-bug-bounty-program-the-time-i-played-with-handlebars-and-broke-stuff.md
original_filename: 2024-09-05_ssti-in-bug-bounty-program-the-time-i-played-with-handlebars-and-broke-stuff.md
title: 'SSTI in Bug Bounty Program: The Time I Played with Handlebars and Broke Stuff'
category: documents
detected_topics:
- sso
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- sso
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: f55e418fd0bf63bec8dce50a567498567f8238d2b1fef75bc1f7a1f004144ab0
text_sha256: 2d16bbe3f167575311a89ce45d29de69fa047784ba13caeed2366aa5161f168c
ingested_at: '2026-06-28T07:32:38Z'
sensitivity: unknown
redactions_applied: false
---

# SSTI in Bug Bounty Program: The Time I Played with Handlebars and Broke Stuff

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-09-05_ssti-in-bug-bounty-program-the-time-i-played-with-handlebars-and-broke-stuff.md
- Source Type: markdown
- Detected Topics: sso, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:38Z
- Redactions Applied: False
- Raw SHA256: `f55e418fd0bf63bec8dce50a567498567f8238d2b1fef75bc1f7a1f004144ab0`
- Text SHA256: `2d16bbe3f167575311a89ce45d29de69fa047784ba13caeed2366aa5161f168c`


## Content

---
title: "SSTI in Bug Bounty Program: The Time I Played with Handlebars and Broke Stuff"
url: "https://medium.com/@ali.zamini/ssti-in-bug-bounty-program-the-time-i-played-with-handlebars-and-broke-stuff-7dc1f9834a3d"
authors: ["Ali Zamini"]
bugs: ["SSTI"]
publication_date: "2024-09-05"
added_date: "2024-09-18"
source: "pentester.land/writeups.json"
original_index: 18
scraped_via: "browseros"
---

# SSTI in Bug Bounty Program: The Time I Played with Handlebars and Broke Stuff

SSTI in Bug Bounty Program: The Time I Played with Handlebars and Broke Stuff
Ali Zamini
Follow
3 min read
·
Sep 5, 2024

107

1

Hey, everybody! 🎉 I’m super excited to share this wild bug I recently found in a public bug bounty program. This one was a fun ride, so grab some popcorn and let me tell you all about it.

So, the scope for this target was as wide as the ocean — *.target.tld. Naturally, I went into full detective mode and started hunting for subdomains. And what’s the first thing any seasoned bounty hunter does? That’s right, a good old-fashioned Google Dork: site:*.target.tld -out_of_scope. 🤓

After scrolling through a bunch of results, I stumbled upon a subdomain that piqued my curiosity. Let’s call it mb.target.tld. I hit the page and there it was—a shiny form that let me search for device capabilities using their ID. So, of course, I did what any of us would do—I poked it with a stick to see what breaks. 🛠️

The “Not too funny fixes” that Started It All

While exploring the page, I noticed a comment in one of the JavaScript files:

Seems that result format/handling/etc has been changed
  I did some not too funny fixes to make it work here as well
  - onAlldevices - result data is string, eval it
  - onSingleDevice - without 'callback' response is lost somewhere

I love it when developers leave hints like this! 🕵️ The mention of eval was enough to make me curious.

The Game Begins: Send, Inspect, Modify, Repeat

I started sending requests to the form and inspecting the responses. The original request looked something like this:

GET /[REDACTED_PATH]/DeviceCapabilityDetails?id=1&callback=eval HTTP/1.1

In the respond there was some information like bellow:

eval({"Id":1,"Brand":"Alcatel", "SOME_OTHER_INFO":"INFO"});

The page was printing SOME_OTHER_INFO: INFO from the response. Seeing eval being used made me even more curious, so I started experimenting with the callback parameter. I quickly realized that whatever I placed in the callbackfunction was included in the response without any sanitization. For example:

GET /[REDACTED_PATH]/DeviceCapabilityDetails?id=1&callback=terrestrial HTTP/1.1
terrestrial({"Id":1,"Brand":"Alcatel", "SOME_OTHER_INFO":"INFO"});

This didn’t print anything on the page, likely due to an error, but it confirmed that my input was being executed.

Tweaking the Output: Changing Page Content

My next step was to manipulate the output on the page. I modified the SOME_OTHER_INFO field in the following request:

GET /[REDACTED_PATH]/DeviceCapabilityDetails?id=1&callback=eval({"Id":1,"Brand":"Alcatel", "SOME_OTHER_INFO":"Terrestrial"});// HTTP/1.1

Success! The page displayed SOME_OTHER_INFO: Terrestrial. Now we were getting somewhere.

Handlebars in Play: Executing Code

Knowing that Handlebars was likely being used, I decided to push the limits a bit. I started by executing a simple operation:

GET /[REDACTED_PATH]/DeviceCapabilityDetails?id=1&callback=eval({"Id":1,"Brand":"Alcatel", "SOME_OTHER_INFO":4*4});//

And just as I expected, the template engine processed the 4*4 and printed 16 on the page. 🎯

Get Ali Zamini’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

At this point, I wanted to see if I could execute more complex code. I tried the following:

callback=({"SOME_OTHER_INFO":(function(){return+this;})()});//

This printed [object Object]. Then, I went a bit further:

callback=({"SOME_OTHER_INFO":(function(){return+this.constructor.constructor;})()});//

That printed function anonymous() {}, confirming that I was interacting with the underlying JavaScript engine.

Next I injected the bellow payload:

callback=({"SOME_OTHER_INFO":(function(){return+Object.keys(this);})()});//

Which retrieved properties of the window object, and explore the DOM. close, stop, focus, blur, open, alert, confirm, prompt,..

Unfortunately, after reviewing the results I realized I don’t have access to chile_process to ran a command line code so I wasn’t able to escalate this to full RCE (ether the target was sandbox or Security Restrictions) , but it was clear that this SSTI could have led to more serious consequences.

Lessons Learned

Here are the key takeaways from this experience:

Always sanitize and validate user data: Especially when dealing with callbacks and template engines like Handlebars.
Keep your libraries up to date: Older versions of template engines often have known vulnerabilities. It’s worth the time to upgrade.

That’s it for this write-up! While I couldn’t fully exploit the SSTI to run arbitrary commands, the vulnerability itself posed a significant risk and was definitely worth reporting.

Thanks for reading, and happy hacking! 🕵️‍♂️

#BugBounty #SSTI #WebSecurity #Infosec #Handebars #CyberSecurity
