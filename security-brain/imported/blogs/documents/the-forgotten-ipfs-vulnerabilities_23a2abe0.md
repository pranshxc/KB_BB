---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-28_the-forgotten-ipfs-vulnerabilities.md
original_filename: 2022-09-28_the-forgotten-ipfs-vulnerabilities.md
title: The forgotten IPFS vulnerabilities
category: documents
detected_topics:
- command-injection
- sso
- xss
- path-traversal
- cors
- information-disclosure
tags:
- imported
- documents
- command-injection
- sso
- xss
- path-traversal
- cors
- information-disclosure
language: en
raw_sha256: 23a2abe0cf7224232d34484e4e700948b90b2712368d8f88eae6134cbdfe28cd
text_sha256: 4640eec6b3bed0a2cafc9551bf7287332792c6c5aec305326a6550f396bb9c6f
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# The forgotten IPFS vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-28_the-forgotten-ipfs-vulnerabilities.md
- Source Type: markdown
- Detected Topics: command-injection, sso, xss, path-traversal, cors, information-disclosure
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `23a2abe0cf7224232d34484e4e700948b90b2712368d8f88eae6134cbdfe28cd`
- Text SHA256: `4640eec6b3bed0a2cafc9551bf7287332792c6c5aec305326a6550f396bb9c6f`


## Content

---
title: "The forgotten IPFS vulnerabilities"
page_title: "The forgotten IPFS vulnerabilities | Consensys Diligence"
url: "https://consensys.net/diligence/blog/2022/09/the-forgotten-ipfs-vulnerabilities/"
final_url: "https://diligence.security/blog/2022/09/the-forgotten-ipfs-vulnerabilities/"
authors: ["tintinweb", "Joran Honig (@joranhonig)"]
programs: ["Filecoin Security"]
bugs: ["Web3 hacking", "Path traversal", "CORS misconfiguration", "HTML injection"]
publication_date: "2022-09-28"
added_date: "2022-10-10"
source: "pentester.land/writeups.json"
original_index: 2106
---

[ Back to all posts ](/blog/)

#  The forgotten IPFS vulnerabilities 

tintinweb 

September 28, 2022 

![The forgotten IPFS vulnerabilities](/images/blog-rhythms/rhythm-2113776817.png)

In 2021 we privately disclosed multiple vulnerabilities in the [InterPlanetary File System](https://ipfs.tech/) (IPFS) to the [Protocol Labs Security Team](https://security.filecoin.io/bug-bounty/) but never really talked about it.

Let’s change that!

* * *

In total, we disclosed `8` vulnerability notes, with some outlining multiple sub-issues. Most of them were fixed immediately. At least one was under embargo until a protocol update could be rolled out. Happy reading & stay safu frens 🧡.

## 🏆 IPNS - Downgrading and Name Takeover

📓 **Vulnerability Note** : [js-ipns - Downgrading Attack and Name Takeover](/diligence/vulnerabilities/jsipns-downgrading-attack-and-name-takeover/)

IPFS is based on a content addressing scheme. If you upload data to the IPFS network, it is addressable by its content identifier (CID). If your data changes, so does the CID. As simple as that. But what if you want to serve changing data under a static IPFS compatible address? e.g. the front-end for a prominent [decentralized exchange](https://uniswap.org/blog/ipfs-uniswap-interface).

InterPlanetary Name System (IPNS) to the rescue 🚀.

Instead of addressing data by content, an IPFS CID can be ‘pinned’ to a public key under the `/ipns/<your-pubkey>` path. The pin can only be updated if you hold the corresponding private key. Unless you can poison neighboring nodes directly 🤓.

Here’s what we’ve disclosed to the IPFS team:

  1. An IPNS name entry downgrading vector made possible because an IPNS messages sequence number is not part of the signed entry.
  2. An IPNS name takeover vector that allows anyone to poison a nodes’ DHT cache and overwrite IPNS records because the DHT protocols target `put-key` is not verified with the actual `record.pubKey` from the IPNS message.

If you are curious, this is what an IPNS entry looks like:
  
  
  message IpnsEntry {
  enum ValidityType {
  EOL = 0; // setting an EOL says "this record is valid until..."
  }
  
  optional bytes value = 1;
  optional bytes signature = 2;
  
  optional ValidityType validityType = 3;
  optional bytes validity = 4;
  
  optional uint64 sequence = 5;
  
  optional uint64 ttl = 6;
  
  // in order for nodes to properly validate a record upon receipt, they need the public
  // key associated with it. For old RSA keys, its easiest if we just send this as part of
  // the record itself. For newer ed25519 keys, the public key can be embedded in the
  // peerID, making this field unnecessary.
  optional bytes pubKey = 7;
  
  optional bytes signatureV2 = 8;
  
  optional bytes data = 9;
  }
  

And this is some live footage of one node poisoning another:

[![demo](https://user-images.githubusercontent.com/2865694/188964102-a218b678-942d-47aa-92d6-41bcffa08518.png)](https://streamable.com/ecbqxw)

There’s a detailed explanation and walkthrough in the PoC section of the [Vulnerability Note](/diligence/vulnerabilities/jsipns-downgrading-attack-and-name-takeover/). Have fun!

## 🏆 IPNS - Signed Message Malleability

📓 **Vulnerability Note** : [js-ipns - Signed Message Malleability Problem](/diligence/vulnerabilities/jsipns-signed-message-malleability-problem/)

This one is cool, too 😎!

Remember, IPNS allows to serve changing CID’s under a fixed address (`/ipns/<pubkey>`). This is accomplished by having a node sign data (`target CID`, `lifetime`, ..) with an IPNS private key. Nodes can query the peer-to-peer network to provide signed records corresponding to a public key. The library validates the signed data, and the payload is used to resolve the target CID for the IPNS entry.

It was found that `js-ipns` failed to properly verify the structure of the signed IPNS message. This would allow to perform a kind of a signed message forging attack that would validate fine with `js-ipns` even though the data fields changed.

Essentially, it is shown, that the simplest attack would be a truncation attack that truncates the value field of a signed IPNS message while reusing the signature essentially forging a message in the name of the original signer.
  
  
  Signed: [value][validity][type=EOL]
  
  [QmWEekX7EZLUd9VXRNMRXW3LXe4F6x7mB8oPxY5XLptrBq][2033-05-18T03:33:20.000000000Z][EOL] (value=QmWEekX7EZLUd9VXRNMRXW3LXe4F6x7mB8oPxY5XLptrBq)
  [QmWEekX7EZLUd9VXRNMRXW3][LXe4F6x7mB8oPxY5XLptrBq2033-05-18T03:33:20.000000000Z][EOL] (value=QmWEekX7EZLUd9VXRNMRXW3)
  [][QmWEekX7EZLUd9VXRNMRXW3LXe4F6x7mB8oPxY5XLptrBq2033-05-18T03:33:20.000000000Z][EOL] (value=)
  

Check out the original [Vulnerability Note](/diligence/vulnerabilities/jsipns-signed-message-malleability-problem/), which includes a fun PoC that illustrates the problem!

## 🏆 IPFS - Fuse mount allows for symlinks outside the mount directory

📓 **Vulnerability Note** : [Ipfs Fuse mount allows for symlinks outside the mount directory](/diligence/vulnerabilities/ipfs-fuse-sandbox/)

Joran’s excellent [write-up on stealing info using ipfs fuse](https://joranhonig.nl/stealing-info-using-ipfs-fuse/) perfectly explains the issue.

In short: `go-ipfs` uses fuse for user space mounting of IPFS nodes via the Brazil library. The library is not secure by default which can be problematic to unsuspecting projects linking the library 🤷‍♂️. In the end, it allowed an attacker to create symlinks on an IPFS mount that referenced other potentially sensitive files.
  
  
  vagrant init ubuntu/groovy64
  vagrant up
  vagrant ssh
  
  $ wget https://dist.ipfs.io/go-ipfs/v0.7.0/go-ipfs_v0.7.0_linux-amd64.tar.gz
  $ tar -xvzf go-ipfs_v0.7.0_linux-amd64.tar.gz
  $ cd go-ipfs
  $ sudo bash install.sh
  
  $ sudo mkdir /ipfs /ipns
  $ sudo chown vagrant: /ipfs /ipns
  
  $ echo "secret" > secret_file
  $ mkdir poc
  $ ln -s /home/vagrant/secret_file ./poc/not_so_secret
  
  $ ipfs init
  $ ipfs daemon --mount &
  $ ipfs add -r ./poc
  $ ipfs pin add <hash of poc node>
  
  $ cat /ipfs/<hash_of_poc_node>/not_so_secret
  secret
  

More details can be found in the [Vulnerability Note](/diligence/vulnerabilities/ipfs-fuse-sandbox/).

## 🏆 IPFS - IPFS Desktop Path Traversal File Overwrite

📓 **Vulnerability Note** : [jsipfs - ipfs-http-response - HTML Injection in Dirlisting](/diligence/vulnerabilities/ipfs-desktop-path-traversal/)

IPFS Desktop is a standalone desktop application that bundles `go-ipfs` with an electron-based front-end. You can download IPFS files and save them to your file system.

What could go wrong? - Relative Path Traversal.

If your CID references a name, including relative path traversal, the file might not be stored at the location the user wants it to be placed, but at any dir, the CID path encodes. The file-write is performed with privileges of the currently logged-in user and silently overwrites files 🤷‍♂️.

![demo](https://user-images.githubusercontent.com/2865694/119120821-054a9280-ba2d-11eb-83c7-a506bbbb49a3.gif)

Check out the details [here](/diligence/vulnerabilities/ipfs-desktop-path-traversal/).

## 🏆 IPFS - API CORS Bypass Full Admin Write

📓 **Vulnerability Note** : [js-ipfs api CORS Bypass Full Admin Write](/diligence/vulnerabilities/jsipfs-api-cors-bypass-full-admin-write/)

Imagine you’re running an IPFS node with the API endpoint enabled. A malicious user tricks you into visiting a website they control, and that website talks to your local API endpoint performing privileged commands in your name. Pretty dangerous.

The security of the writeable admin API endpoint is enforced by client-side CORS, which is not the best idea. So what happens if a malicious website initiates a non-CORS “fire & forget” `POST` request to the admin API?

![demo](https://user-images.githubusercontent.com/2865694/117191596-05b61d00-ade1-11eb-8954-eb9d456066fe.png)

Curious how this works in detail? Check out the [Vulnerability Note](/diligence/vulnerabilities/jsipfs-api-cors-bypass-full-admin-write/).

## 🏆 IPFS - Path Traversal and Control Char Injection

📓 **Vulnerability Note** : [Ipfs - Path Traversal and Control Char Injection](/diligence/vulnerabilities/ipfs-path-traversal-and-control-char-injection/)

### Path Traversal - arbitrary overwrite

Imagine you are downloading and unpacking a CID’s files, but the creator of the CID added relative path information to the filename. `js-ipfs` and `go-ipfs` would concatenate and unpack the files just fine but to the folder defined by the malicious CID creator, silently overwriting existing files. This can be unexpected and dangerous 🤷‍♂️.

![demo1](/diligence/vulnerabilities/ipfs-path-traversal-and-control-char-injection/99956028-9c3bd800-2d85-11eb-998f-2445c62f4318.gif)

### Console Control Char Injection

CID path information may contain control chars that allow a malicious CID owner to disguise the actual name of files. Perfectly chainable with the path traversal to make the CID look benign.

![demo2](/diligence/vulnerabilities/ipfs-path-traversal-and-control-char-injection/99956024-99d97e00-2d85-11eb-98e3-05ca01733156.gif)

### P2P Proxy Panic

This is just a low severity proxy panic. Easy to fix.

For details, consult the referenced [Vulnerability Note](/diligence/vulnerabilities/jsipfs-api-cors-bypass-full-admin-write/).

## 🏆 IPFS - go-ipfs-files improperly handles writing ipfs nodes to files

📓 **Vulnerability Note** : [go-ipfs-files improperly handles writing ipfs nodes to file](/diligence/vulnerabilities/ipfs-files-pathbom/)

The `go-ipfs-files` implementation of WriteTo doesn’t implement any sanitization on the names (paths) reported for file nodes. An attacker can provide arbitrary paths for symlinks, directories, and files.

The ability to write to any location is a far-stretching capability that an attacker can use to extract information and potentially reach remote code execution.

More information in the [Vulnerability Note](/diligence/vulnerabilities/ipfs-files-pathbom/).

## 🏆 IPFS - Dirlisting HTML Injection

📓 **Vulnerability Note** : [jsipfs - ipfs-http-response - HTML Injection in Dirlisting](/diligence/vulnerabilities/jsipfs-dirlisting-html-injection/)

Well, this one is rather boring, but it is still something that should be addressed anyways. The gateway mode in `js-ipfs` provides an autogenerated directory listing for IPFS CID’s that resolve to a folder. This directory listing is generated by `ipfs-http-response`. The problem is that the `dir-view` component in `ipfs-http-response` does not encode CID metadata for use in HTML before string-concatenating it into a static HTML dir-viewer page that is later served via the `js-ipfs` HTTP gateway. Say hello to all types of HTML injections 👋.

This is how it looks like. Boring, huh?!

![ipfs-marquee](https://user-images.githubusercontent.com/2865694/127372211-df569f74-8168-4475-9476-bd7c12291b5f.gif)

You can find a detailed explanation in this [Vulnerability Note](/diligence/vulnerabilities/jsipfs-dirlisting-html-injection/).

## 🏆 Gateway Security

And here’s a link to a blog post on [Gateway Security Issues](/diligence/blog/2021/06/ipfs-gateway-security/) we published last year.

![gateway checker](/diligence/blog/2021/06/ipfs-gateway-security/img2.png)

Have fun and help keeping core Open Source projects safe & secure, practice responsible disclosure, and participate in the projects’ Bug Bounty programs.

peace out 🫶.

* * *

Thinking about smart contract security? We can provide training, ongoing advice, and smart contract auditing. [Contact us](/contact/).
