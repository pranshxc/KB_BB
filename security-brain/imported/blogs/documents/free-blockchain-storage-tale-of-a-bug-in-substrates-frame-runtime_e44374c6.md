---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-07_free-blockchain-storage-tale-of-a-bug-in-substrates-frame-runtime.md
original_filename: 2020-07-07_free-blockchain-storage-tale-of-a-bug-in-substrates-frame-runtime.md
title: Free blockchain storage – Tale of a bug in Substrate’s FRAME runtime
category: documents
detected_topics:
- sso
- command-injection
- file-upload
- otp
tags:
- imported
- documents
- sso
- command-injection
- file-upload
- otp
language: en
raw_sha256: e44374c6f4e4e677dfdc35be5ac1d816047b5499b300f93d78518d4dfa87b18e
text_sha256: f859a2750bc5ed8b39395dcb1b9e6014ee3d06f1496723efbff7f41ff0b7ed94
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Free blockchain storage – Tale of a bug in Substrate’s FRAME runtime

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-07_free-blockchain-storage-tale-of-a-bug-in-substrates-frame-runtime.md
- Source Type: markdown
- Detected Topics: sso, command-injection, file-upload, otp
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `e44374c6f4e4e677dfdc35be5ac1d816047b5499b300f93d78518d4dfa87b18e`
- Text SHA256: `f859a2750bc5ed8b39395dcb1b9e6014ee3d06f1496723efbff7f41ff0b7ed94`


## Content

---
title: "Free blockchain storage – Tale of a bug in Substrate’s FRAME runtime"
page_title: "Free blockchain storage - Tale of a bug in Substrate's FRAME runtime - Mudit Gupta's Blog"
url: "https://mudit.blog/free-blockchain-storage-bug-substrate/"
final_url: "https://mudit.blog/free-blockchain-storage-bug-substrate/"
authors: ["Mudit Gupta (@Mudit__Gupta)"]
programs: ["Parity Technologies"]
bugs: ["Blockchain"]
bounty: "250"
publication_date: "2020-07-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4429
---

# Free blockchain storage – Tale of a bug in Substrate’s FRAME runtime

[Writeups](https://mudit.blog/category/hacking/writeups/) / By  [ Mudit Gupta  ](https://mudit.blog/author/zzkpn5vzmz7z6btdaraokego6lgwp24781/ "View all posts by Mudit Gupta") /  July 7, 2020  / [Blockchain](https://mudit.blog/tag/blockchain/), [Parity](https://mudit.blog/tag/parity/), [substrate](https://mudit.blog/tag/substrate/)

![](https://mudit.blog/wp-content/uploads/2020/07/cyber-security-3400555_960_720.jpg.webp)

This is the story of a simple bug in the FRAME runtime of Parity’s Substrate blockchain framework. The bug allowed attackers to do infinitely large transactions without paying any extra fees. The vulnerability was the result of a buggy implementation of fee calculation in the FRAME runtime of Substrate. By exploiting this vulnerability, an attacker could’ve added their manga collection to the payload of a simple transaction without paying any extra fees. This would’ve resulted in the manga collection becoming a part of the blockchain, forever. Cheapest decentralized blockchain storage!

Sample fees for a 2 megabyte payload before the bug-fix:  
![](https://mudit.blog/wp-content/uploads/2020/07/Screenshot-from-2020-07-05-10-50-18.png)  

Sample fees for a 2 megabyte payload after the bug-fix:  
![](https://mudit.blog/wp-content/uploads/2020/07/Screenshot-from-2020-07-05-10-52-32.png.webp)

Please note that this bug is now fixed and a runtime upgrade has been deployed to Kusama, Polkadot and Polymesh Aldebaran testnet.

### Bug details

The transaction fee is supposed to increase as the size of the transaction increases. There’s a constant `TransactionByteFee` that is supposed to be added to the total fee for every byte of data contained in the transaction. This would’ve prevented the above exploit from working but due to a very tiny bug in the code, this fee was not being applied under certain circumstances.

The fee was being calculated as:
  
  
  fee = base_fee + targeted_fee_adjustment * (len_fee + weight_fee);

  * `base_fee` is a static fee applied to all transactions (analogous to the 21k gas fee in Ethereum).
  * `targeted_fee_adjustment` is a fee multiplier that is based on recent activity on the chain. If the recent blocks have been full, this multiplier will increase and if the recent blocks have been empty, this multiplier will decrease.
  * `len_fee` is the extra fee charged for the size of a transaction. Transactions with bigger payloads will have a bigger `len_fee`.
  * `weight_fee` is based on the compute requirements of a transaction. A more resource-intensive transaction will have a higher `weight_fee`.

There are two problems here. Firstly, the `len_fee` is being affected by the `targeted_fee_adjustment` multiplier. However, as per the [W3F docs](https://research.web3.foundation/en/latest/polkadot/Token%20Economics.html#setting-transaction-fees), it should not be. The second problem is that the `targeted_fee_adjustment` multiplier was allowed to go as low as zero. The combined result of these two problems is that when the chain is not busy, no `len_fee`, and `weight_fee` are charged and anyone can submit large transactions to inflate the blockchain size.

### Reproduction steps

The vulnerability was very easy to exploit. All you had to do was to send a huge payload alongside a valid transaction. Sample reproduction steps are as follows:

  1. Open the Polkadot UI – [](https://polkadot.js.org/apps/#/explorer)<https://polkadot.js.org/apps>.
  2. Click on the “Extrinsics” tab on the left.
  3. Select the “remark” extrinsic from the “system” frame.
  4. Click on “file upload” on the right and upload your payload (anything you want to put on the blockchain).
  5. Submit the transaction.

### Resolution

The [fix](https://github.com/paritytech/substrate/pull/6334) was twofold but simple. Firstly, the `len_fee` was moved out so that it was not affected by the `targeted_fee_adjustment` multiplier. The new fee formula is
  
  
  fee = base_fee + len_fee + targeted_fee_adjustment * weight_fee;

In addition, the `targeted_fee_adjustment` was adjusted so that the minimum multiplier is one instead of zero. This brings the implementation closer to what the W3F research suggested. It makes exploit like the one mentioned in this post impossible.

### Timeline

  * Reported – 17/06/2020
  * Acknowledged – 17/06/2020
  * Fixed – 17/06/2020

### Addendum

I’d like to thank Parity Technologies for being responsive and fixing the bug within hours of the report. Kusama and Polkadot were upgraded soon after the bug fix. Parity offered me a 250 USD bug bounty for this disclosure which they have kindly donated to the [Smile Foundation](https://www.smilefoundationindia.org/) on my behalf. I’d like to thank them for that as well.

Everyone is welcome to try their hands on Kusama and report any bugs to Parity. Below is a direct quote from Fredrik, CTO at parity:

> We are thankful to Mudit for reporting this to us. We created Kusama for this specific purpose of testing the underlying economic assumptions before they reach Polkadot and are happy that it worked in this case. We encourage everyone to continue hunting bugs on Kusama and reporting them to us!
> 
> Fredrik Harrysson, CTO at Parity

Happy hacking!
