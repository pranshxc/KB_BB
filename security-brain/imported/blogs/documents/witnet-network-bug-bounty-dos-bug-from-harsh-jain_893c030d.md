---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-17_witnet-network-bug-bounty-dos-bug-from-harsh-jain.md
original_filename: 2020-08-17_witnet-network-bug-bounty-dos-bug-from-harsh-jain.md
title: 'Witnet Network Bug Bounty: DOS Bug from Harsh Jain'
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 893c030d845a93f636a763fddea4128f610217bbcb797b042db64bfc0c6ffc6d
text_sha256: c12d1c0508a7b16223d1a086e39899ab8d6c23af63d6370c41f361671a4d8204
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Witnet Network Bug Bounty: DOS Bug from Harsh Jain

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-17_witnet-network-bug-bounty-dos-bug-from-harsh-jain.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `893c030d845a93f636a763fddea4128f610217bbcb797b042db64bfc0c6ffc6d`
- Text SHA256: `c12d1c0508a7b16223d1a086e39899ab8d6c23af63d6370c41f361671a4d8204`


## Content

---
title: "Witnet Network Bug Bounty: DOS Bug from Harsh Jain"
url: "https://medium.com/witnet/witnet-network-acknowledged-dos-bug-f7d55b709051"
authors: ["Harsh Jain"]
programs: ["Witnet"]
bugs: ["DoS"]
publication_date: "2020-08-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4315
scraped_via: "browseros"
---

# Witnet Network Bug Bounty: DOS Bug from Harsh Jain

Witnet Network Bug Bounty: DOS Bug from Harsh Jain
Harsh Jain
Follow
2 min read
·
Aug 17, 2020

105

Press enter or click to view image in full size

For those unaware, Witnet is a Decentralised Permissionless Oracle Network planning to release Mainnet in the middle of October this year. Currently they are doing regress testing and running a Testnet Incentive Program, including a Bug Bounty Program.

I have been running a Witnet node from the start of this Testnet. Alongside that, I also started looking into the code and checking out how the nodes were communicating. In order to join the network, a new node communicates with its peers and exchanges VERSION and VERACK messages to consolidate the connection. If the exchange of these messages doesn’t happen within handshake timeout duration, another thread terminates the connection. Even if the message is erroneous, the connection is live for at least thehandshake timeout period.

As a result, if the number of messages can somehow be increased by decreasing their individual size, we can effectively overload the node with a large number of messages and even consume the resources of the thread that terminates the connection.

Get Harsh Jain’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Witnet is using PROTOBUF encoded messages for communication. The format of PROTOBUF messages is as follows: firstly, four bytes tell the length of message L, and the next L bytes encompass the actual message. So, the smallest size of the message is 4 bytes: 0x00000000, with 0 being the length of the actual message.

For 1Mbps transfer of data from a malicious node, peers will receive around 32000 messages per second (each message containing 32 bits). This is a huge number of messages to be processed in 1 second, and as a result requires substantial resources from nodes and the handshake timeout function is not called.

This bug was therefore raised because the connection was not closed, and nodes would wait for timeout duration before terminating it. This attack was responsibly disclosed on 31 July. The team acknowledged the DOS possibility and fixed it within a week.

Bug Acknowledgment: https://bit.ly/3kSviaN

Bug Fix: https://github.com/witnet/witnet-rust/pull/1444

Witnet bug bounty program: https://bit.ly/3iI2DmO
