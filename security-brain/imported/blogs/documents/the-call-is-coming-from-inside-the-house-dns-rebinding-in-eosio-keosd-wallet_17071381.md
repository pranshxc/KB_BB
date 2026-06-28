---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-07-19_the-call-is-coming-from-inside-the-house-dns-rebinding-in-eosio-keosd-wallet.md
original_filename: 2018-07-19_the-call-is-coming-from-inside-the-house-dns-rebinding-in-eosio-keosd-wallet.md
title: The call is coming from inside the house — DNS rebinding in EOSIO keosd wallet
category: documents
detected_topics:
- sso
- command-injection
- otp
- api-security
tags:
- imported
- documents
- sso
- command-injection
- otp
- api-security
language: en
raw_sha256: 17071381a8b3a94036f6da4fc1b1ad89d74aba0673374a5e5ac8579ba58e6cc9
text_sha256: 153752690368b59efae4c41ed28212e5fb368db4f22ffd8e436ae5ac097410a4
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# The call is coming from inside the house — DNS rebinding in EOSIO keosd wallet

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-07-19_the-call-is-coming-from-inside-the-house-dns-rebinding-in-eosio-keosd-wallet.md
- Source Type: markdown
- Detected Topics: sso, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `17071381a8b3a94036f6da4fc1b1ad89d74aba0673374a5e5ac8579ba58e6cc9`
- Text SHA256: `153752690368b59efae4c41ed28212e5fb368db4f22ffd8e436ae5ac097410a4`


## Content

---
title: "The call is coming from inside the house — DNS rebinding in EOSIO keosd wallet"
url: "https://medium.com/@root_31068/the-call-is-coming-from-inside-the-house-dns-rebinding-in-eosio-keosd-wallet-e11deae05974"
authors: ["François Proulx (@francoisproulx)"]
programs: ["EOSIO"]
bugs: ["DNS rebinding"]
publication_date: "2018-07-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5799
scraped_via: "browseros"
---

# The call is coming from inside the house — DNS rebinding in EOSIO keosd wallet

The call is coming from inside the house — DNS rebinding in EOSIO keosd wallet
François Proulx
Follow
6 min read
·
Jul 20, 2018

392

2

(Before I begin — this bug was responsibly disclosed and has been fixed in the version 1.0.9 and later of EOSIO software, so I highly recommend you to update)

I’ve been doing Application Security as a full-time job for about 5 years now, and I’ve been an avid reader of bug bounty responsible disclosure stories way before it became “a thing”, but somehow I never participated in public bug bounties. So this is a first for me and I’m excited to discuss my experience with the HackerOne-backed EOSIO program.

In the past few months I’ve been providing InfoSec and AppSec guidance to an awesome team of folks who got me interested in EOSIO and blockchain technology in general. Previously I’ve never been much interested in cryptocurrencies (especially bitcoin), but when I first heard about smart contracts and then Proof Of Stake (vs Proof Of Work — which I think is simply not scalable and a massive waste of energy) my AppSec spider-sense tingled. The idea of blindly executing untrusted arbitrary code that’s flying over a peer-to-peer network is crazy scary, but terribly exciting because of the promise of decentralization and consensus algorithms that modern blockchains provide.

A little more than a month ago, I was writing a script to automate various tasks (like setting up an EOSIO account with the right multi-sig permissions) and I noticed that successive calls to cleos would not prompt for the wallet passphrase on every call. I could see that cleos was spawning a detachedkeosd process so that it would keep alive for 15 minutes after passphrase prompt (this is the default documented behavior — which can be changed in your config.ini).

As I said, I often start my day by combing through the daily security news and bug bounty write-ups on /r/netsec, that day I saw an article about DNS rebinding in IOT devices. This reminded me about a NorthSec 2018 talk by two Akamai security researchers. During that talk they discussed a new tool they’ve developed which significantly increases the performance and usability of DNS rebinding attacks. I heard about DNS rebinding some ten years ago, but it wasn’t until 
Tavis Ormandy
 tweeted about a bug in Blizzard’s daemon and later about the same problem in many Torrent clients that this old (circa 1996) vulnerability category became hot again.

That morning it didn’t take long for me to add it all up… What if keosd was vulnerable to DNS rebinding and given that it accepts EOS signing transaction for 15 minutes after passphrase prompt, that would be a credible remote attack for a threat actor to pull off against whales. That same afternoon, I tested a few basic assumptions by sniffing the plaintext HTTP requests with Wireshark to see how the requests were structured and noticed that while cleos was sending the HTTP requestHost header, it was not compliant RFC7230 section 5.4 (i.e. the keosd listening port 8900 was not specified)…

Press enter or click to view image in full size
Wireshark packet capture of loopback interface showing HTTP request between `cleos` and `keosd`

I quickly added an /etc/hosts file entry for 127.0.0.1 example.com so I could validate my hypothesis using curl. My hands must’ve been a little bit sweaty as I typed curl -X POST http://example.com:8900/v1/wallet/get_public_keys and saw the public key for my test wallet! Everything indicated that it was exploitable.

$ curl -X POST http://example.com:8900/v1/wallet/get_public_keys
["EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV"]

Then I considered trying the new tool from the Akamai guys, but I was lazy and their public service did not appear to be up. That’s when I found out about whonow tool on GitHub that essentially offered the same functionality, but was readily usable without deploying anything special ahead of time (http://rebind.network).

I quickly spun up a Google Cloud compute instance with a static public IP and crafted the URL with magic hostname that would first have configurable and deterministic DNS resolution behavior

http://a.35.23.3.13.1time.127.0.0.1.5time.repeat.rebind.network:8900

The first part specifies that it should resolve to 35.23.3.13 once, then resolve to 127.0.0.1 (loopback where keosd is waiting on port 8900) and repeat in a loop. Basically this tool / service acts as an authoritative DNS server for the zone rebind.network and resolves by following the specified algorithm in the domain tokens.

Get François Proulx’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I then proceeded to set up a virtual host with nginx to listen on port 8900 and slapped together some ugly bits of HTML and Javascript for the POC.

<html>
<body>
<script>
console.log("Loaded from 35.203.35.123:8900");
setTimeout(function() {
  fetch("/v1/wallet/get_public_keys", { method: "POST" })
  .then(function(r) {
  return r.json();
  })
  .then(function(json) {
  alert(json);
  });
}, 30000); // Wait 30 seconds 
</script>
</body>
</html>

I then ran cleos wallet unlock once to unlock the keosd wallet for 15 minutes and opened Chrome to test it out.

Hooray!
Press enter or click to view image in full size
POC screenshot showing `keosd` accepting requests (right) and a successful DNS rebinding in Chrome (left).
Threat Modeling recap
Press enter or click to view image in full size

Let’s do a napkin threat model, first, our EOS private key sits on disk on the user’s machine encrypted with a key derived from the user’s passphrase. Whenever the user uses cleos and types that passphrase it gets a 15-minute grace period to perform multiple operations in a row. Given that those are separate processes, they happen to communicate using a TCP socket on the loopback interface (port 8900 by default). That’s all fine and good if we consider that the trust boundary is the user’s machine and that it’s fully patched, zero open ports, etc… Then our user who is a savvy EOS community member regularly visits popular blogs, where there is a malvertising campaign (or simply a blog post) from our Threat Actor. The Javascript stealthily opens an <iframe> which instructs the user’s browser to perform DNS resolution for a domain that has its SOA / NS set to a magic DNS server that first returns the IP of the Web server of our Threat Actor. The browser proceeds to load some HTML and Javascript. A few seconds later, the same Javascript which was loaded and is now associated with the Origin of the Threat Actor will perform a fetch which will trigger a second DNS resolution (because the TTL of the A record first returned has conveniently already expired). This time, the DNS server will return 127.0.0.1 as the A record. The browser will “rebind” this new IP to the currently visited origin and Bob’s your uncle… At that point the Threat Actor can issue arbitrary EOS transaction using the active wallet on the victim’s machine.

The root cause

So, what’s the root cause of the bug. Why is this different than a well behaved daemon listening on loopback? Why would this one be exploitable? Simply because, as I said, it does not follow RFC7230 section 5.4 — if it had at least ensured to process HTTP requests and return 200 responses only for whitelisted Host (ex. localhost:8900 or 127.0.0.1:8900 …) everything would’ve been fine. And that is essentially how the vulnerability was addressed in 1.0.9 (there might be other options like mutual authentication between processes, etc.).

The bug bounty

As I said, this was my first experience participating in a public bug bounty and I was pleasantly surprised by the level of attention that Block One gives to the reporters. I reported the bug and they confirmed that they could reproduce my proof of concept within less than 24 hours. We exchanged once or twice about how they planned to address the issue and in which release it should be included.

Block One is quite generous in this bug bounty and I think this is a good return on investment for them and the EOS community as it attracts great security researchers early on to address the most critical security bugs.

Cheers,
