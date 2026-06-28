---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-02-23_the-fuzzthe-bugthe-action-a-race-condition-bug-in-facebook-chat-groups-leads-to-.md
original_filename: 2018-02-23_the-fuzzthe-bugthe-action-a-race-condition-bug-in-facebook-chat-groups-leads-to-.md
title: The Fuzz…The Bug..The Action – A Race Condition bug in Facebook Chat Groups
  leads to spy on conversations!
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- race-condition
- api-security
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- race-condition
- api-security
- mobile-security
language: en
raw_sha256: 5f4be24e98ec4986619dfbedb3bb140363a5660eaa2d689bfd3862824fc322e8
text_sha256: 5249a99451273f46f799dcecc242c579b38d0394b49b5c98836b824f227830e3
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# The Fuzz…The Bug..The Action – A Race Condition bug in Facebook Chat Groups leads to spy on conversations!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-02-23_the-fuzzthe-bugthe-action-a-race-condition-bug-in-facebook-chat-groups-leads-to-.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, race-condition, api-security, mobile-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `5f4be24e98ec4986619dfbedb3bb140363a5660eaa2d689bfd3862824fc322e8`
- Text SHA256: `5249a99451273f46f799dcecc242c579b38d0394b49b5c98836b824f227830e3`


## Content

---
title: "The Fuzz…The Bug..The Action – A Race Condition bug in Facebook Chat Groups leads to spy on conversations!"
page_title: "The Fuzz…The Bug..The Action – A Race Condition bug in Facebook Chat Groups leads to spy on conversations! – Seekurity"
url: "https://www.seekurity.com/blog/general/the-fuzz-the-bug-the-action-a-race-condition-bug-in-facebook-chat-groups-leads-to-spy-on-conversations"
final_url: "https://seekurity.com/blog/2018/02/23/seif-elsallamy/general/the-fuzz-the-bug-the-action-a-race-condition-bug-in-facebook-chat-groups-leads-to-spy-on-conversations"
authors: ["Seif Elsallamy (@seifelsallamy)"]
programs: ["Meta / Facebook"]
bugs: ["Race condition"]
publication_date: "2018-02-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5966
---

Hi Folks, Long time no see, it’s Seif Elsallamy, Remember me ? if not 🙁 you may go through my previous blogs [Stored XSS in the heart of the Russian email provider giant (Mail.ru)](https://www.seekurity.com/blog/general/stored-xss-in-the-heart-of-the-russian-email-provider-giant-mail-ru/) , [Rolling around and Bypassing Facebook’s Linkshim protection on iOS](https://www.seekurity.com/blog/general/rolling-around-and-bypassing-facebook-linkshim-protection-on-ios/)

Today I’m gonna show you a race condition bug which i recently fall in love with those kind of vulnerabilities especially in when it comes to Facebook also i want to mention that this bug is super simple to understand It’s not complicated, the only complicated part is how to test and finding it.

**First thing first, What is Race condition ?**  
So a [race condition](https://www.owasp.org/index.php/Testing_for_Race_Conditions_\(OWASP-AT-010\)) is a flaw that produces an unexpected result when the timing of actions impact other actions. An example may be seen on a multithreaded application where actions are being performed on the same data. Race conditions, by their very nature, are difficult to test for.

As example we got a coupon code or a voucher that gonna give us $10 for shopping online. we enters this code multiple times very fast (before the coupon code expires in the server side) so instead of getting $10 we may get $20 or $30 maybe $100 depends on the server.

So I think the main reason for me to love this vulnerability is the unexpected results that may occurs.

I think that developers doesn’t consider Race Conditioning while building most of the applications, It’s really unexpected behavior/vulnerability.

##### Enough the Blah Blah Blah, show me some action… 😀

##### **The Fuzz…The Bug..The Action…**

On Facebook by creating a group conversations didn’t consider the race condition to occur results unexpected behaviour that may put some Facebook users at a risk which is “the ability to spy on a group conversations”

So by creating a group conversation invite some users to it choose one of the users that you invited speedily remove and re-add this user to the conversation multiple times (kind of a typical test for exploiting race condition bugs) this user will be invisible BUT can read write remove users and add also there is no “seen” sign after the user looks for chat inside the conversation.

**_So let’s imagine an attack scenario (in the era of the spies)._****_Want a bed story? prepare your doll:_**  
-We got 4 innocent users let’s choose a random names for them  
Symbian, Ali, Hiram and Mahmoud  
-So yesterday Symbian , Ali and Mahmoud were hanging out together.  
-Symbian was whispering Ali then they both laughed very hard and Mahmoud was really upset and he keeps asking Symbian about what they laughed for but every time Mahmoud asking they both laugh again.  
-So at night everyone drive to his home Mahmoud called Hiram complains about the thing that Symbian and Ali were laughing for.  
-So Hiram told Mahmoud about a bug on Facebook to spy on group conversations and he told Mahmoud that he gonna add him to a group conversation with Symbian and Ali to spy on their chat.  
-So Hiram opens up the computer added Symbian and Ali to a group conversation and then Added Mahmoud and Removed him speedily multiple times till he became invisible.  
-Then Hiram sent “sorry I got some error on Facebook I’ll be back later” and left the conversation.  
-Now Symbian and Ali are the only ones in this conversation  
and Mahmoud is with them but he is invisible so he can spy on their chat to know what were they both laughing for.  
– Then Symbian “typing…” and Mahmoud is really excited while he was watching the indicator of “typing…” then Symbian said “good night :D” and left the conversation then Ali left it too.  
-Sorry Mahmoud hehe :D!

So this is the time that you  _allll weee waiting forrrrr!  
_

###### **The PoC Video!**

The bug was responsibly reported to Facebook by @Seekurity team and we got a really satisfying reward, Thanks for Facebook team for keeping us safe.

Thank You too for reading this!!

## **A minute if you please!**

Building a website, an application or any kind of business? Or already have one? Worried about your security? Think twice before going public and let us [protect your business](https://www.seekurity.com/#pricing)!

[](https://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2018%2F02%2F23%2Fseif-elsallamy%2Fgeneral%2Fthe-fuzz-the-bug-the-action-a-race-condition-bug-in-facebook-chat-groups-leads-to-spy-on-conversations&linkname=The%20Fuzz%E2%80%A6The%20Bug..The%20Action%20%E2%80%93%20A%20Race%20Condition%20bug%20in%20Facebook%20Chat%20Groups%20leads%20to%20spy%20on%20conversations%21 "Facebook")[](https://www.addtoany.com/add_to/pinterest?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2018%2F02%2F23%2Fseif-elsallamy%2Fgeneral%2Fthe-fuzz-the-bug-the-action-a-race-condition-bug-in-facebook-chat-groups-leads-to-spy-on-conversations&linkname=The%20Fuzz%E2%80%A6The%20Bug..The%20Action%20%E2%80%93%20A%20Race%20Condition%20bug%20in%20Facebook%20Chat%20Groups%20leads%20to%20spy%20on%20conversations%21 "Pinterest")[](https://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2018%2F02%2F23%2Fseif-elsallamy%2Fgeneral%2Fthe-fuzz-the-bug-the-action-a-race-condition-bug-in-facebook-chat-groups-leads-to-spy-on-conversations&linkname=The%20Fuzz%E2%80%A6The%20Bug..The%20Action%20%E2%80%93%20A%20Race%20Condition%20bug%20in%20Facebook%20Chat%20Groups%20leads%20to%20spy%20on%20conversations%21 "Twitter")[](https://www.addtoany.com/add_to/whatsapp?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2018%2F02%2F23%2Fseif-elsallamy%2Fgeneral%2Fthe-fuzz-the-bug-the-action-a-race-condition-bug-in-facebook-chat-groups-leads-to-spy-on-conversations&linkname=The%20Fuzz%E2%80%A6The%20Bug..The%20Action%20%E2%80%93%20A%20Race%20Condition%20bug%20in%20Facebook%20Chat%20Groups%20leads%20to%20spy%20on%20conversations%21 "WhatsApp")[](https://www.addtoany.com/add_to/telegram?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2018%2F02%2F23%2Fseif-elsallamy%2Fgeneral%2Fthe-fuzz-the-bug-the-action-a-race-condition-bug-in-facebook-chat-groups-leads-to-spy-on-conversations&linkname=The%20Fuzz%E2%80%A6The%20Bug..The%20Action%20%E2%80%93%20A%20Race%20Condition%20bug%20in%20Facebook%20Chat%20Groups%20leads%20to%20spy%20on%20conversations%21 "Telegram")[](https://www.addtoany.com/add_to/linkedin?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2018%2F02%2F23%2Fseif-elsallamy%2Fgeneral%2Fthe-fuzz-the-bug-the-action-a-race-condition-bug-in-facebook-chat-groups-leads-to-spy-on-conversations&linkname=The%20Fuzz%E2%80%A6The%20Bug..The%20Action%20%E2%80%93%20A%20Race%20Condition%20bug%20in%20Facebook%20Chat%20Groups%20leads%20to%20spy%20on%20conversations%21 "LinkedIn")[](https://www.addtoany.com/add_to/google_gmail?linkurl=https%3A%2F%2Fseekurity.com%2Fblog%2F2018%2F02%2F23%2Fseif-elsallamy%2Fgeneral%2Fthe-fuzz-the-bug-the-action-a-race-condition-bug-in-facebook-chat-groups-leads-to-spy-on-conversations&linkname=The%20Fuzz%E2%80%A6The%20Bug..The%20Action%20%E2%80%93%20A%20Race%20Condition%20bug%20in%20Facebook%20Chat%20Groups%20leads%20to%20spy%20on%20conversations%21 "Gmail")[](https://www.addtoany.com/share)

Action Race Condition  Bug  Chat  conversations  Facebook  Fuzz  Groups  in  leads  on  spy  to
