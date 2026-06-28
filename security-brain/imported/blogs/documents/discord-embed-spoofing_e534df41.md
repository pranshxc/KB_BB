---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-02_discord-embed-spoofing.md
original_filename: 2020-03-02_discord-embed-spoofing.md
title: Discord embed spoofing
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: e534df414e53d29656ca9312af2e1e6c8166f70f34c57c8b418a1de63d1ec7d2
text_sha256: 907daed130fc73a32b5ec953e068c3fa144becc20fc455712b8c047e3b9d5c5f
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Discord embed spoofing

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-02_discord-embed-spoofing.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `e534df414e53d29656ca9312af2e1e6c8166f70f34c57c8b418a1de63d1ec7d2`
- Text SHA256: `907daed130fc73a32b5ec953e068c3fa144becc20fc455712b8c047e3b9d5c5f`


## Content

---
title: "Discord embed spoofing"
url: "https://medium.com/@DarkMatterMatt/discord-embed-spoofing-c6d07ab1decc"
authors: ["DarkMatterMatt"]
programs: ["Discord"]
bugs: ["Phishing"]
publication_date: "2020-03-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4742
scraped_via: "browseros"
---

# Discord embed spoofing

Discord embed spoofing
DarkMatterMatt
Follow
2 min read
·
Mar 2, 2020

2

1

TLDR: I found a vulnerability in the way the Discord clients parse URLs which makes my custom embed content appear to come from a legitimate domain.

The message https://discord.gg%2ek.vu will show an embed from https://discord.gg.k.vu but display as https://discord.gg/%2ek.vu

Discord uses Node’s url.parse()function to process URLs in messages. Node’s parser expects to receive a URL which has already had its percent encoding decoded into special characters. Discord’s web and desktop clients forget to do this and instead attempt to parse the raw user input.

Get DarkMatterMatt’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

A % symbol is never allowed in a hostname (ietf.org/rfc/rfc2396.html#section-3.2.2) so the parser considers the hostname as the text before the%. This results in the server (which decodes the %2e to a .) and the client seeing different URLs.

$ node parseUrl.js "https://discord.gg%2ek.vu"
Url {
  protocol: 'https:',
  slashes: true,
  auth: null,
  host: 'discord.gg',
  port: null,
  hostname: 'discord.gg',
  hash: null,
  search: null,
  query: null,
  pathname: '%2ek.vu',
  path: '%2ek.vu',
  href: 'https://discord.gg/%2ek.vu'
}

The server which loads the embed content acts the same way as a normal web browser and decodes the %2e before loading the embed from https://discord.gg.k.vu. The desktop and web clients incorrectly parse the URL and display it as https://discord.gg/%2ek.vu, suggesting that the URL came from discord.gg.

Press enter or click to view image in full size
It’s from discord.gg, right?

This vulnerability can be used for much more realistic phishing attacks as the blue text that the user is clicking is different to the website that it links to. For example, clicking “Join the Official Fortnite Discord Server!” in the image below sends the victim to a cloned Discord login page. The user has just seen the discord.gg URL so they are unlikely to be suspicious of the login page.

Press enter or click to view image in full size
Phishing potential: clicking on the link in the embed will take you to my domain

I contacted Discord security about this vulnerability and they claim that it is not a security vulnerability as “there is no guarantee the link in a message matches the link in the title.” As such, there is no patch available and all desktop and web clients are currently vulnerable. Mobile devices do not display the deceiving slash.
