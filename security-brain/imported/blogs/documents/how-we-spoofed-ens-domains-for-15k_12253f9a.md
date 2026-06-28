---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-15_how-we-spoofed-ens-domains-for-15k.md
original_filename: 2022-04-15_how-we-spoofed-ens-domains-for-15k.md
title: How we spoofed ENS domains for $15k
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 12253f9afc853e21e3f448b861e4559f33a4f6725e15c1093c100941551221fa
text_sha256: 1581608318b54eb189a9662d93e6c526e62fd3ed481029e19a1a4dc8c6298fee
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# How we spoofed ENS domains for $15k

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-15_how-we-spoofed-ens-domains-for-15k.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `12253f9afc853e21e3f448b861e4559f33a4f6725e15c1093c100941551221fa`
- Text SHA256: `1581608318b54eb189a9662d93e6c526e62fd3ed481029e19a1a4dc8c6298fee`


## Content

---
title: "How we spoofed ENS domains for $15k"
url: "https://medium.com/@hacxyk/how-we-spoofed-ens-domains-52acea2079f6"
authors: ["Hacxyk. (@Hacxyk)"]
programs: ["ENS"]
bugs: ["Homograph attack"]
bounty: "15,000"
publication_date: "2022-04-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2704
scraped_via: "browseros"
---

# How we spoofed ENS domains for $15k

How we spoofed ENS domains for $15k
Hacxyk
Follow
4 min read
·
Apr 16, 2022

140

Press enter or click to view image in full size
TL;DR: We found a flaw that allowed us to spoof Ethereum domain names and received a $15k bounty.
What is a ENS Domain?

Chances are you have already seen a ETH domain (on Twitter) even if you didn’t know what it was.

Press enter or click to view image in full size

ETH domains look like normal Internet domains, except the suffix is .eth instead of the usual .com. One needs a user agent or a browser extension (MetaMask) that support ETH domains. ENS domains are usually used for sending/receiving Ethereum payments and occassionally IPFS.

Registration Rules

Traditional domains are case-insensitive and only allow alphanumeric characters and hypen (International domains are just punycode which still abide by the same rules). This is done at the registrar level. ENS domains do not have such restrictions on the registrar level. You may ask, why? This has to do with the way ENS works.

Instead of storing the domain name in plain text, the ENS smart contract only stores the hash (Keccak-256) of it. Therefore, the “registrar” doesn’t know what domain name is being registered, and it won’t be able to place any restrictions.

This makes ENS domains easily spoofable.

NFT

ENS is also an NFT, meaning they can be sold on a marketplace like OpenSea/LooksRare. Each ENS NFT has a name ID, which is a combined results of several Keccak-256 hashes.

For example, nick.eth’s name ID is calculated as follows.

keccak256("\0" * 32, keccak256("nick"))

If a domain has multiple levels, the process is done recursively.

But here’s a problem. If the smart contract only stores a hash, how can markerplaces show their original name?

ENS official provides a metadata service for deriving the name from a lookup table. For example:

https://metadata.ens.domains/mainnet/0x57f1887a8BF19b14fC0dF6Fd9B2acc9Af147eA85/42219085255511335250589442208301538195142221433306354426240614732612795430543/

{"is_normalized":true,"name":"nick.eth","description":"nick.eth, an ENS name."}

From it we know the hash (Name ID) 42219085255511335250589442208301538195142221433306354426240614732612795430543 represents nick.eth.

Get Hacxyk’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In the following, we will show several known spoofing attacks, followed by our discovery.

👉 Homograph Attack

Using non-ascii characters can make two domains look idential visually. Browsers have a set of rules to determine if a domain is intended to deceive people.

For ENS, any non-ascii domain is simply marked non-normalized and a warning is displayed.

Press enter or click to view image in full size

The warning is from the metadata service.

👉 Spoofing with Uppercase Letters

Not being able to use non-ascii characters eliminates a lot of possibilities. Nevertheless, there’s a known attack vector that uses uppercase letters. For example, Bitcoin and bitcoin’s hashes are different. The matadata service did not consider this scenario and did not return a warning. This was since patched.

Press enter or click to view image in full size
👉 Spoofing with Subdomain

ENS supports subdomains. We discovered that the metadata service did not consider that a name can contain the dot character. It was possible to register a ENS domain with foo.bar as the name. The metadata would return foo.bar.eth instead of marking it invalid.

✔️ Correct name ID: keccak256(keccak256("\0" * 32, keccak256("bar"), keccak256("foo"))
❌ Invalid name ID : keccak256("\0" * 32, keccak256("foo.bar"))

In our test, we successfully registered eth-usd.data.eth, despite not owning data.eth (It belongs to Chainlink). Both OpenSea and LooksRare did not show a warning.

Press enter or click to view image in full size

People who would buy this domain thinking it’s legit would lose their money. This was fixed in the ENS metadata service and hence LooksRare and OpenSeas which rely on it.

Bug Bounty

We reported this issue to ENS, LooksRare and OpenSea. LooksRare told us the issue was on ENS side and contacted ENS. ENS promptly fixed the issue and awarded a bounty. OpenSea unforunately closed the report as “Phishing is out of scope”.

Timeline

April 6th — Issue reported to ENS, LooksRare and Opensea
April 6th — LooksRare received the report and contacted ENS
April 6th — ENS pushed a fix
April 9th — OpenSea closed the report as out of scope
April 11th — ENS awarded $15k for the issue
