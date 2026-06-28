---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-10-26_slack-saml-authentication-bypass.md
original_filename: 2017-10-26_slack-saml-authentication-bypass.md
title: Slack SAML authentication bypass
category: documents
detected_topics:
- oauth
- sso
- saml
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- oauth
- sso
- saml
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 9721d13e0a72335404985e0e8c62e526ad5d0b0c9aa3a43ceb6c660207e3d282
text_sha256: 78351844fec95158c95b37d40b4aa6665cbc3c39ff2e4ab0d3117cade4901e9b
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Slack SAML authentication bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-10-26_slack-saml-authentication-bypass.md
- Source Type: markdown
- Detected Topics: oauth, sso, saml, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `9721d13e0a72335404985e0e8c62e526ad5d0b0c9aa3a43ceb6c660207e3d282`
- Text SHA256: `78351844fec95158c95b37d40b4aa6665cbc3c39ff2e4ab0d3117cade4901e9b`


## Content

---
title: "Slack SAML authentication bypass"
url: "https://blog.intothesymmetry.com/2017/10/slack-saml-authentication-bypass.html"
final_url: "https://blog.intothesymmetry.com/2017/10/slack-saml-authentication-bypass.html"
authors: ["Antonio Sanso (@asanso)"]
programs: ["Slack"]
bugs: ["Authentication bypass"]
bounty: "3,000"
publication_date: "2017-10-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6069
---

###  Slack SAML authentication bypass 

[ October 26, 2017  ](https://blog.intothesymmetry.com/2017/10/slack-saml-authentication-bypass.html "permanent link")

tl;dr I found a severe issue in the [Slack](https://slack.com/)'s [SAML](https://en.wikipedia.org/wiki/SAML_2.0) implementation that allowed me to bypass the authentication. This has now been solved by Slack.  

#  Introduction

IMHO the rule #1 of any bug hunter (note I do not consider myself one of them since I do this really sporadically) is to have a good RSS feed list. In the course of the last years I built a pretty decent one and I try to follow other security experts trying to "steal" some useful tricks. There are many experts in different fields of the security panorama and too many to quote them here (maybe another post). But one of the leading expert (that I follow) on SAML is by far [Ioannis Kakavas](https://twitter.com/ilektrojohn). Indeed he was able in the last years to find serious vulnerability in the SAML implementation of [Microsoft](http://www.economyofmechanism.com/office365-authbypass.html) and [Github](http://www.economyofmechanism.com/github-saml). Usually I am more an ["OAuth guy"](https://www.manning.com/books/oauth-2-in-action) but since both, SAML and OAuth, are nothing else that grandchildren of [Kerberos](https://en.wikipedia.org/wiki/Kerberos_\(protocol\)) learning SAML has been in my todo list for long time. The Github incident gave me the final motivation to start learning it.

#  Learning SAML

As said I was a kind of **SAML-idiot** until begin of 2017 but then I decided to learn it a little bit. Of course I started giving a look the the specification, but the best way I learn things is by doing and hopefully breaking. So I downloaded [this great Burp extension](https://github.com/SAMLRaider/SAMLRaider) called **SAML Raider** (great stuff, it saves so much time, you can edit any assertion on the fly).

Then I tried to look if any of the service that routinely I use are SAML compliant. It turns out that many of them are. To name some:

  * [Github](https://github.com/) (but I guess [Ioannis](https://twitter.com/ilektrojohn) already took all the bugs there). So ping next (I actually found [this](http://blog.intothesymmetry.com/2017/05/cross-origin-brute-forcing-of-saml-and.html) funny JS Github bug giving a look into it, but not pertinent here)
  * [Hackerone](https://www.hackerone.com/), I gave a try here but nada, nisba, niente, nicht, niet
  * [Slack,](https://slack.com/) Bingo see next section (this is probably meant for Enterprise customers)

[![](https://get.slack.help/hc/article_attachments/115014834866/testmode.png)](https://get.slack.help/hc/article_attachments/115014834866/testmode.png)

#  Slack SAML authentication bypass

As said many of the service I use in my routine are SAML aware so I started to poke a bit them. The vulnerability I found is part of the class known as "[_confused deputy problem_](http://en.wikipedia.org/wiki/Confused_deputy_problem)". I already talked about it in one of my [OAuth blog post](http://blog.intothesymmetry.com/2013/05/oauth-2-attacks-introducing-devil-wears.html) (tl;dr this is also why you never want to use OAuth implicit grant flow as authentication mechanism) and is really simple. Basically SAML assertions, between others contains an element called **Audience** and **AudienceRestriction**. Quoting [Ioannis](https://twitter.com/ilektrojohn):

  

> _The Assertion also contains an AudienceRestriction element that defines that this Assertion is targeted for a specific Service Provider and cannot be used for any other Service Provider._

This means that if I present to a ServiceProvider A an assertion meant for ServiceProvider B, then the ServiceProvider A shoud reject it. 

Well between all other things I tried this very really simple attack against a Slack's SAML endpoint /sso/saml and guess what? It worked :o !!

To be more concrete I used an old and **expired (** yes the assertion was also expired!!) Github's Assertion I had saved somewhere in my archive that was signed for a subject different than mine (namely the username was not asanso aka me) and I presented to Slack. Slack happily accepted it and I was logged in Slack channel with the username of this old and expired Assertion that was never meant to be a Slack one!!! Wow this is scary.... Well well this look bad enough so I stopped quite immediately and open a ticket on [Hackerone](http://hackerone.com/)....  

#  Disclosure timeline 

...here the Slack security team was simply amazing... Thanks guys**  
**  
  
**02-05-2017 -** Reported the issue via Hackerone.  
**03-05-2017 -** Slack confirmed the issue.****  
**26-08-2017 -** Slack awarded a 3000$ bounty but still working with the affected customers in order to solve the vulnerability. Hence the ticket was kept open.  
**26-10-2017 -** Slack closed the issue  

#  Acknowledgement

I would like to thank the Slack security team in particular Max Feldman you guys rock, really!!  
  
Well that's all folks. **For more SAML trickery[follow me on Twitter](https://twitter.com/asanso). **

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Labels

[bounty](https://blog.intothesymmetry.com/search/label/bounty) [saml](https://blog.intothesymmetry.com/search/label/saml)

Labels: [bounty](https://blog.intothesymmetry.com/search/label/bounty) [saml](https://blog.intothesymmetry.com/search/label/saml)

Share 

  * Get link
  * Facebook
  * X
  * Pinterest
  * Email
  * Other Apps

### Comments

![](//www.blogger.com/img/blogger_logo_round_35.png)

[PanickedPacman](https://www.blogger.com/profile/04489194998201550244) said… 

Your Hackerone anchor tag is missing .com 

[ 27 October 2017 at 10:10 ](https://blog.intothesymmetry.com/2017/10/slack-saml-authentication-bypass.html?showComment=1509124211045#c7811247350069840047 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/comment/delete/5832863639484084941/7811247350069840047 "Delete Comment")

![](//www.blogger.com/img/blogger_logo_round_35.png)

[ll](https://www.blogger.com/profile/13409233330078201207) said… 

Fixed thanks!! 

[ 28 October 2017 at 12:24 ](https://blog.intothesymmetry.com/2017/10/slack-saml-authentication-bypass.html?showComment=1509218653581#c1860572620309521668 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/comment/delete/5832863639484084941/1860572620309521668 "Delete Comment")

![](//www.blogger.com/img/blogger_logo_round_35.png)

[davide](https://www.blogger.com/profile/12727560342876305194) said… 

Hi, would you share your RSS list? I'm always interested in reading good stuff ;-)  
thanks in advance 

[ 22 November 2017 at 04:39 ](https://blog.intothesymmetry.com/2017/10/slack-saml-authentication-bypass.html?showComment=1511354396742#c11373476006145623 "comment permalink") [ ![](https://resources.blogblog.com/img/icon_delete13.gif) ](https://www.blogger.com/comment/delete/5832863639484084941/11373476006145623 "Delete Comment")

[ Post a Comment ](https://www.blogger.com/comment/fullpage/post/5832863639484084941/3566384980368454393)
