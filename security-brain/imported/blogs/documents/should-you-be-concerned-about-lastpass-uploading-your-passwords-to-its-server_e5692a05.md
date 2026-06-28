---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-18_should-you-be-concerned-about-lastpass-uploading-your-passwords-to-its-server.md
original_filename: 2019-03-18_should-you-be-concerned-about-lastpass-uploading-your-passwords-to-its-server.md
title: Should you be concerned about LastPass uploading your passwords to its server?
category: documents
detected_topics:
- command-injection
- automation-abuse
- information-disclosure
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- information-disclosure
- business-logic
- api-security
language: en
raw_sha256: e5692a05e61c686d7fcc6b012923d850fd5af60d6d404af22fa115b4cc4f3e62
text_sha256: 72dec06921f2880bc78b11d91281892bab8eec8490d578cafc632df078eaef92
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Should you be concerned about LastPass uploading your passwords to its server?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-18_should-you-be-concerned-about-lastpass-uploading-your-passwords-to-its-server.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, information-disclosure, business-logic, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `e5692a05e61c686d7fcc6b012923d850fd5af60d6d404af22fa115b4cc4f3e62`
- Text SHA256: `72dec06921f2880bc78b11d91281892bab8eec8490d578cafc632df078eaef92`


## Content

---
title: "Should you be concerned about LastPass uploading your passwords to its server?"
page_title: "Should you be concerned about LastPass uploading your passwords to its server? | Almost Secure"
url: "https://palant.info/2019/03/18/should-you-be-concerned-about-lastpass-uploading-your-passwords-to-its-server/"
final_url: "https://palant.info/2019/03/18/should-you-be-concerned-about-lastpass-uploading-your-passwords-to-its-server/"
authors: ["Wladimir Palant (@WPalant)"]
programs: ["LastPass"]
bugs: ["Information disclosure", "Logic flaw"]
publication_date: "2019-03-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5354
---

# Should you be concerned about LastPass uploading your passwords to its server?

2019-03-18 [Lastpass](/categories/lastpass/)/[Security](/categories/security/)/[Password-Managers](/categories/password-managers/) 6 mins [21 comments](/2019/03/18/should-you-be-concerned-about-lastpass-uploading-your-passwords-to-its-server/#comments)

TL;DR: Yes, very much.

I’ve written [a number of blog posts on LastPass security issues](/category/lastpass/) already. The [latest one so far](/2018/07/09/is-your-lastpass-data-really-safe-in-the-encrypted-online-vault) looked into the way the LastPass data is encrypted before it is transmitted to the server. The thing is: when your password manager uploads all data to its server backend, you normally want to be very certain that the data visible to the server is useless both to attackers who manage to compromise the server and company employees running that server. Early last year I reported a number of issues that allowed subverting LastPass encryption with comparably little effort. The most severe issues have been addressed, so all should be good now?

Sadly, no. It is absolutely possible for a password manager to use a server for some functionality while not trusting it. However, LastPass has been designed in a way that makes taking this route very difficult. In particular, the decision to fall back to server-provided pages for parts of the LastPass browser extension functionality is highly problematic. For example, whenever you access Account Settings you leave the trusted browser extension and access a web interface presented to you by the LastPass server, something that the extension tries to hide from you. Some other extension functionality is implemented similarly.

#### Table of Contents

  * The glaring hole
  * The attack
  * The fix
  * Conclusion

## The glaring hole

So back in November I discovered an API meant to accommodate this context switch from the extension to a web application and make it transparent to the user. Not sure how I managed to overlook it on my previous strolls through the LastPass codebase but the `getdata` and `keyplug2web` API calls are quite something. The response to these calls contains your local encryption key, the one which could be used to decrypt all your server-side passwords.

There has been a number of reports in the past about that API being accessible by random websites. I particularly liked [this security issue uncovered by Tavis Ormandy](https://bugs.chromium.org/p/project-zero/issues/detail?id=1225) which exploited an undeclared variable to trick LastPass into loosening up its API restrictions. Luckily, all of these issues have been addressed and by now it seems that only lastpass.com and lastpass.eu domains can trigger these calls.

Oh, but the chances of _some_ page within lastpass.com or lastpass.eu domain to be vulnerable aren’t exactly low! Somebody thought of that, so there is an additional security measure. The extension will normally ignore any `getdata` or `keyplug2web` calls, only producing a response once after this feature is unlocked. And it is unlocked on explicit user actions such as opening Account Preferences. This limits the danger considerably.

Except that the action isn’t always triggered by the user. There is a “breach notification” feature where the LastPass server will send notifications with arbitrary text and link to the user. If the user clicks the link here, the `keyplug2web` API will be unlocked and the page will get access to all of the user’s passwords.

## The attack

LastPass is run by LogMeIn, Inc. which is based in United States. So let’s say the NSA knocks on their door: “Hey, we need your data on XYZ so we can check their terrorism connections!” As we know by now, NSA does these things and it happens to random people as well, despite not having any ties to terrorism. LastPass data on the server is worthless on its own, but NSA might be able to pressure the company into sending a breach notification to this user. It’s not hard to choose a message in such a way that the user will be compelled to click the link, e.g. “IMPORTANT: Your Google account might be compromised. Click to learn more.” Once they click it’s all over, my proof-of-concept successfully downloaded all the data and decrypted it with the key provided. The page can present the user with an “All good, we checked it and your account isn’t affected” message while the NSA walks away with the data.

The other scenario is of course a rogue company employee doing the same on their own. Here LastPass claims that there are internal processes to prevent employees from abusing their power in such a way. It’s striking however how their response mentions “a single person within development” — does it include server administrators or do we have to trust those? And what about two rogue employees? In the end, we have to take their word on their ability to prevent an inside job.

## The fix

I reported this issue via Bugcrowd on November 22, 2018. As of LastPass 4.25.0.4 (released on February 28, 2019) this issue is considered resolved. The way I read the change, the LastPass server is still able to send users breach notifications with text and image that it can choose freely. Clicking the button (button text determined by the server) will still give the server access to all your data. Now there is additional text however saying: “LastPass has detected that you have used the password for this login on other sites, too. We recommend going to your account settings for this site, and creating a new password. Use LastPass to generate a unique, strong password for this account. You can then save the changes on the site, and to LastPass.” Ok, I guess this limits the options for social engineering slightly…

No changes to any of the other actions which will provide the server with the key to decrypt your data:

  * Opening Account Settings, Security Challenge, History, Bookmarklets, Credit Monitoring
  * Linking to a personal account
  * Adding an identity
  * Importing data if the binary component isn’t installed
  * Printing all sites

Some of these actions will prompt you to re-enter your master password. That’s merely security theater however, you can check that they have `g_local_key` global variable set already which is all they need to decrypt your data.

One more comment on the import functionality: supposedly, a binary component is required to read a file. If the binary component isn’t installed, LastPass will fall back to uploading your file to the server. The developers apparently missed that the [API to make this work locally](https://developer.mozilla.org/en-US/docs/Web/API/FileReader) has been part of any browser released since 2012 (yes, that’s seven years ago).

## Conclusion

I wrote the original version of [this Stack Exchange answer](https://security.stackexchange.com/a/137307/4778) in September 2016. Back then it already pointed out that mixing trusted extension user interface with web applications is a dangerous design choice. It makes it hard to secure the communication channels, something that LastPass has been struggling with a lot. But beyond that, there is also lots of implicit trust in the server’s integrity here. While LastPass developers might be inclined to trust their servers, users have no reason for that. The keys to all their online identities are data that’s too sensitive to entrust any company with it.

LastPass has always been stressing that they cannot access your passwords, so keeping them on their servers is safe. This statement has been proven wrong several times already, and the improvements so far aren’t substantial enough to make it right. LastPass design offers too many loopholes which could be exploited by a malicious server. So far they didn’t make a serious effort to make the extension’s user interface self-contained, meaning that they keep asking you to trust their web server whenever you use LastPass.
