---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-17_stealing-downloads-from-slack-users.md
original_filename: 2019-05-17_stealing-downloads-from-slack-users.md
title: Stealing Downloads from Slack Users
category: documents
detected_topics:
- command-injection
- csrf
- api-security
tags:
- imported
- documents
- command-injection
- csrf
- api-security
language: en
raw_sha256: b536b7b17ce88aae1e476c08bb55074a1ff097dc703e1ba9761f6747ad4d0a91
text_sha256: dd17b2725f39c68587fe6db581e704d43a24335078b15f6815cb577cf7bfc2be
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Stealing Downloads from Slack Users

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-17_stealing-downloads-from-slack-users.md
- Source Type: markdown
- Detected Topics: command-injection, csrf, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `b536b7b17ce88aae1e476c08bb55074a1ff097dc703e1ba9761f6747ad4d0a91`
- Text SHA256: `dd17b2725f39c68587fe6db581e704d43a24335078b15f6815cb577cf7bfc2be`


## Content

---
title: "Stealing Downloads from Slack Users"
url: "https://medium.com/tenable-techblog/stealing-downloads-from-slack-users-be6829a55f63"
authors: ["David Wells"]
programs: ["Slack"]
bugs: ["CSRF"]
publication_date: "2019-05-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5258
scraped_via: "browseros"
---

# Stealing Downloads from Slack Users

Stealing Downloads from Slack Users
David Wells
Follow
5 min read
·
May 17, 2019

1.1K

1

I’m going to go over an interesting feature abuse that could have been used to steal and even manipulate downloads from Slack users using the Slack desktop app on Windows. The vulnerability was reported to Slack via HackerOne based on our coordinated disclosure policy and Slack has patched this issue in one of its latest updates, v3.4.0. The vulnerability could have allowed a remote attacker to submit a masqueraded link in a slack channel, that “if clicked” by a victim, would silently change the download location setting of the slack client to an attacker owned SMB share. This could have allowed all future downloaded documents by the victim to end up being uploaded to an attacker owned file server until the setting is manually changed back by the victim. While on the attacker’s server, the attacker could have not only stolen the document, but even inserted malicious code in it so that when opened by victim after download (through Slack application), their machine would have been infected. This entire technique relied on how Slack treated clickable links and what was possible with certain slack:// links. We will go over some interesting applications of this attack.

Changing Settings

Slack is an Electron app, which makes reverse engineering quite easy for us. As a Slack user, one feature that I was already familiar with was the support for “slack://” hyperlinks. I figured this may be an interesting attack vector, so with some grepping I found the area of code that processes these protocol links. Looking at the functions, we can see an interesting one in protocol-link.ts module, which has the ability to change Slack app settings if clicked.

We can find what available settings can be changed by looking in the Settings-Reducer.ts module, which contains all Slack settings.

Press enter or click to view image in full size

Nearly all of these settings are modifiable through slack://settings links.

Download Location Hijack

After researching all of the settings we can change, I found the most interesting setting reachable through a slack:// protocol handler was the “PrefSSBFileDownloadPath” setting. This changed the download destination path of a user. Crafting a link like “slack://settings/?update={‘PrefSSBFileDownloadPath’:’<pathHere>’}” would change the default download location if clicked (until manually changed back).

Get David Wells’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The links however, cannot contain certain characters, as Slack filters them out. One of these characters is the “:” (colon) which means we can’t actually supply a path with drive root. An SMB share, however, completely bypassed this sanitation as there is no root drive needed. After setting up a remote SMB share, we could send users or channels a link that would redirect all downloads to it after they click the link.

Once this is clicked, we can see that the change was successfully made in the advanced settings.

Press enter or click to view image in full size

If we now download a document…

Press enter or click to view image in full size

It is instead uploaded to this remote SMB share.

Press enter or click to view image in full size
Attack Vectors

From a practical standpoint, the link text should be obscured as it looks sketchy on its own and savvy users probably won’t click it. There are a couple of options available for this.

Authenticated Channel Member

Researching Slack documentation, it didn’t appear to be possible to hyperlink words in a Channel at first:

However, playing around with Slack API (and later seeing documentation for it), I found you could accomplish text hyperlinking through “attachments” feature. This can be accomplished by adding an “attachment” field to your slack POST request with appropriate fields:

Press enter or click to view image in full size

When this Slack message is submitted to a channel, it will now have hyperlinked “http://google.com” to my malicious slack link instead when clicked.

Press enter or click to view image in full size

When clicked, this will instantly change the victim’s Slack download location.

Unauthenticated Channel Member

This applies if we aren’t a member of a Slack channel. This is quite interesting as you may wonder…”Can we get our malicious link to enter into Slack channels we aren’t even a part of?”

YES! It’s possible!

This can be accomplished through RSS feeds. Slack channels can subscribe to RSS feeds to populate a channel with site updates which can contain links. Lets consider an example with reddit.com, here I could make a post to a very popular Reddit community that Slack users around the world are subscribed to (in this test case however, I chose a private one I owned). I will drop an http link (because slack:// links are not allowed to be hyperlinked on Reddit) that will redirect to our malicious slack:// link and change settings when clicked.

Press enter or click to view image in full size

Once posted to this subreddit, our test Slack channel (that is subscribed to this subreddit feed), is now populated with the new article entry and previews the text which includes the link.

Press enter or click to view image in full size

There is a slight drawback to this technique however. When a victim clicked this link, the browser prompted a dialog such as the one seen below. The victim would have had to click “Yes,” which then instantly changes their Slack client’s download location.

Final Thoughts

This technique could be unmasked by savvy Slack users, however if decades of phishing campaigns have taught us anything, it’s that users click links, and when leveraged through an untrusted RSS feed, the impact can get much more interesting. Furthermore, we could have easily manipulated the download item when we control the share it’s uploaded to, meaning the Slack user that opens/executes the downloaded file will actually instead be interacting with our modified document/script/etc off the remote SMB share, the options from there on are endless.

Slack investigated and found no indication that this vulnerability was ever utilized, nor reports that its users were impacted.
