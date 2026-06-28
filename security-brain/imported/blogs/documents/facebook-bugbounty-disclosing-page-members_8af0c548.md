---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-20_facebook-bugbounty-disclosing-page-members.md
original_filename: 2018-12-20_facebook-bugbounty-disclosing-page-members.md
title: Facebook BugBounty - Disclosing page members
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 8af0c54814a35a78715d2dd70d0a7474a2c4317c5a51fd9671bfc801edada64d
text_sha256: 72c10476da2797042ec6d5774a65a6cfa83582e7824002b62a787513cbdd17aa
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook BugBounty - Disclosing page members

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-20_facebook-bugbounty-disclosing-page-members.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `8af0c54814a35a78715d2dd70d0a7474a2c4317c5a51fd9671bfc801edada64d`
- Text SHA256: `72c10476da2797042ec6d5774a65a6cfa83582e7824002b62a787513cbdd17aa`


## Content

---
title: "Facebook BugBounty - Disclosing page members"
page_title: "Facebook BugBounty  - Disclosing page members"
url: "https://www.tnirmal.com.np/2018/12/facebook-bugbounty-disclosing.html"
final_url: "https://www.tnirmal.com.np/2018/12/facebook-bugbounty-disclosing.html"
authors: ["Nirmal Thapa / mpz (@tnirmalz)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
publication_date: "2018-12-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5512
---

###  Facebook BugBounty - Disclosing page members 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

\-  [ December 20, 2018  ](https://www.tnirmal.com.np/2018/12/facebook-bugbounty-disclosing.html "permanent link")

* * *

Because of some privacy reasons, identity of page members (admins/mods/analysts) is kept secret by facebook and normal page visitors cannot find the details about these members. But back in July 2018, when I was hunting for bugs in Facebook, I found multiple ways to disclose members of a facebook page.

### Disclosing post creators with 'Get Messages' feature

This feature named “Get Messages” is available on Facebook pages when uploading posts and stuff.

![](https://cdn-images-1.medium.com/max/1000/1*FgypJmkJ5OjqCmBkiZ5jWw.png)Get Messages feature

Mainly e-commerce and online shopping websites use this feature with one of their product so whenever a visitor wants to know more about that particular product, they can simply click on the “Send message” button. A post with this feature enabled looks something like the below screenshot.

![](https://cdn-images-1.medium.com/max/1000/1*dVW-6FzCY1RlpZc_d_qobA.png)A post with “Get messages” feature enabled

The bug here is, if we click on this “Send message button”, profile ID of the creator is leaked in one of the responses coming from host <https://x-edge-chat.facebook.com> which is not visible in general..

![](https://cdn-images-1.medium.com/max/1000/1*uwMDkao18qq3luA2FGb6fw.png)Inbox demo

.. but if we check burp suite logs, we can see that the ID of the creator is leaked.

![](https://cdn-images-1.medium.com/max/1000/1*g4livVEaktCCIE6Ihzp9Ew.png)Creator’s profile leaked

In the above screenshot, 100027117349417 is the ID of my test account.

**Impact?**

This particular bug is really easy to exploit and if an attacker needs to find the creator of a Facebook page, s/he can just go to the page, find posts with this feature enabled, click on send message button, check the logs and BOOM profile ID of the creator is disclosed.

**Timeline**

6th July 2018: Issue found and reported.

10th July 2018: First Reply by Facebook Security

11th July 2018: Issue triaged

27th July 2018: Issue fixed

4th Sep 2018: Bounty awarded *Nice bounty :P*

* * *

### Disclosing the identity of people sending messages on the behalf of the page

When I was going through Burp Suite logs to report the above issue, I noticed this weird response too.

![](https://cdn-images-1.medium.com/max/1000/1*YFgz3tyY4Ve30BhaHNDrUg.png)Unknown_response.png

I was pretty sure this was something else and could lead to another leak so I just saved this screenshot and decided to look into this issue later.

*Fast forward to 1 week later*

I tried to reproduce this issue by simply sending a message to the page as a normal visitor..

![](https://cdn-images-1.medium.com/max/1000/1*sHMmFnAPZ8DGvmzOqo8b-Q.png)Sending message to a page as normal visitor

.. and replied from the page

![](https://cdn-images-1.medium.com/max/1000/1*1j-1qvf_SpHnh4B19Hh9XA.png)Replying to the above visitor from page

As soon as I recieved this “Hello visitor” message, I checked Burp Suite logs and saw this exact same response like before.

![](https://cdn-images-1.medium.com/max/1000/1*OSoOVxw7cFDfUCEK4xUpJw.png)Message senders’ profile leaked

Here, 100027405052940 is the profile ID of page member who replied “Hello visitor”. This means.. You send a message to a Facebook page, someone who has ability to read/reply messages replies to you and immediately his profile ID is leaked.

Impact?

Very very very easy to exploit. Anyone can just randomly send message to a facebook page, someone replies to that message and BOOM, their profile ID is leaked. ;)

**Timeline**

6th Jul 2018: Initial Discovery of bug

14th Jul 2018: Mystery behind the ‘leak’ found and reported

18th Jul 2018 3:37 AM: Issue triaged

18th Jul 2018 10:53 PM: Issue fixed

1st Aug 2018: Bounty awarded

* * *

T̶h̶a̶t̶’̶s̶ ̶a̶l̶l̶ ̶f̶o̶r̶ ̶2̶0̶1̶8̶.̶ ̶I̶ ̶h̶o̶p̶e̶ ̶t̶o̶ ̶d̶i̶v̶e̶ ̶m̶o̶r̶e̶ ̶i̶n̶t̶o̶ ̶F̶a̶c̶e̶b̶o̶o̶k̶ ̶B̶u̶g̶B̶o̶u̶n̶t̶y̶ ̶p̶r̶o̶g̶r̶a̶m̶ ̶i̶n̶ ̶2̶0̶1̶9̶ ̶❤

Thank you for reading this post. If you have any queries/suggestions, I’m available on [Twitter](https://twitter.com/tnirmalz) :)

Happy Hacking!! .. until next time.

[bugbounty](https://www.tnirmal.com.np/search/label/bugbounty)

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

#### Post a Comment

[](https://www.blogger.com/comment/frame/1981508766266852527?po=8893567075262649749&hl=en&saa=85391&origin=https://www.tnirmal.com.np&skin=contempo)
