---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-02-03_facebook-mailto-injection-leads-to-social-engineering-spam-attack.md
original_filename: 2018-02-03_facebook-mailto-injection-leads-to-social-engineering-spam-attack.md
title: Facebook mailto injection leads to social engineering & spam attack
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: e614a55d7b76217b4f1df1845d9cebb91c1ccf346c69a5347ba075962d3fd273
text_sha256: bdf13cdb858cc87db8a1df3283131f2b4193c7a5a536ce0ffb6ee2665d296153
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook mailto injection leads to social engineering & spam attack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-02-03_facebook-mailto-injection-leads-to-social-engineering-spam-attack.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `e614a55d7b76217b4f1df1845d9cebb91c1ccf346c69a5347ba075962d3fd273`
- Text SHA256: `bdf13cdb858cc87db8a1df3283131f2b4193c7a5a536ce0ffb6ee2665d296153`


## Content

---
title: "Facebook mailto injection leads to social engineering & spam attack"
url: "https://medium.com/@kankrale.rahul/facebook-mailto-injection-leads-to-social-engineering-spam-attack-68b08e36764a"
authors: ["Rahul Kankrale (@RahulKankrale)"]
programs: ["Meta / Facebook"]
bugs: ["Mailto injection"]
publication_date: "2018-02-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5986
scraped_via: "browseros"
---

# Facebook mailto injection leads to social engineering & spam attack

Facebook mailto injection leads to social engineering & spam attack
Rahul Kankrale
Follow
1 min read
·
Feb 3, 2018

25

Facebook mobile sites: m.facebook & mbasic.facebook provide lite tag to friends feature.

when you goes to tag friends list open for selection and there is Cancel button .

when you see at url of this feature there is cancel_uri parameter which link to previous url of page.

I modified this parameter to openredirect but cant able todo as linkshim protection so i tried another protocol rather than HTTP, like :

mailto, whatsapp, fb, twitter etc.

and all are accepted, then i passed with mailto protocol with all its parameters (reciever email,subject,body, attachment) and all are injectable., and link injected behind Cancel button.

Get Rahul Kankrale’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Once victim got this crafted url and when he click on cancel button his email client will open with prefilled data(inserted by attacker) which trick victim to submit his credential using some social engineering techniques.

Final POC url:

https://m.facebook.com/friends/selector/?return_uri=4&cancel_uri=mailto:kankrale.rahul@gmail.com?subject=To%20access%26body=Submit%20Login&attachment=%22/storage/emulated/0/Download/test.txt%22&friends_key=ids&context&add_photos_uri&is_initial_render=0

Reported to facebook
Accepted risk with no bounty as social engineering involved.
Closed report without fix.
Point to be noted :
adobe got RCE using mailto in past
H1 also accepted same as parameter injection.
Thanks
Rahul Kankrale

Suggestion require for mailto exploit for such a issue : Rahul Kankrale
