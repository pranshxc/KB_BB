---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-11-10_not-your-stdout-bug-rce-in-cosmos-sdk.md
original_filename: 2023-11-10_not-your-stdout-bug-rce-in-cosmos-sdk.md
title: Not Your Stdout Bug - RCE in Cosmos SDK
category: documents
detected_topics:
- access-control
- command-injection
- otp
- automation-abuse
- api-security
- cloud-security
tags:
- imported
- documents
- access-control
- command-injection
- otp
- automation-abuse
- api-security
- cloud-security
language: en
raw_sha256: c0482d9d94680b8287f5c08b89104f8ffaa927cf2b8459f1dfd6db174c267cab
text_sha256: a959349676de74ea73a1d88acb81472c7baaacd5e4f80812efe599d937514986
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# Not Your Stdout Bug - RCE in Cosmos SDK

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-11-10_not-your-stdout-bug-rce-in-cosmos-sdk.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, automation-abuse, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `c0482d9d94680b8287f5c08b89104f8ffaa927cf2b8459f1dfd6db174c267cab`
- Text SHA256: `a959349676de74ea73a1d88acb81472c7baaacd5e4f80812efe599d937514986`


## Content

---
title: "Not Your Stdout Bug - RCE in Cosmos SDK"
url: "https://maxwelldulin.com/BlogPost/stdout-cosmos-sdk-rce"
final_url: "https://maxwelldulin.com/BlogPost/stdout-cosmos-sdk-rce"
authors: ["Maxwell Dulin (@Dooflin5)"]
programs: ["Cosmos"]
bugs: ["RCE", "DoS", "Security code review"]
bounty: "2,500"
publication_date: "2023-11-10"
added_date: "2023-12-27"
source: "pentester.land/writeups.json"
original_index: 682
---

![](/static/StrikeoutLongTransparentWhite.png)

### [About](/) [Project](/Project) [Blog](/Blog) [Resources](/Resources)

# Blog[![](https://cdn3.iconfinder.com/data/icons/cosmo-color-basic-2/40/rss-512.png)](https://maxwelldulin.com/api/rss/blog)

# Not Your Stdout Bug - RCE in Cosmos SDK

October 11, 2023

![Cosmovisor RCE Banner](https://maxwelldulinwebsite.s3.us-east-2.amazonaws.com/cosmovisor_rce/PostBanner.png)

Imagine, you're hunting for bugs in a project. You're reading through the documentation of a widely used framework with millions of dollars at stake. Then, you stumble across [this](https://github.com/cosmos/cosmos-sdk/tree/cosmovisor/v0.1.0/cosmovisor#cosmosvisor-quick-start): 

> Cosmovisor is small process manager for Cosmos SDK application binaries that **monitors stdout for incoming chain upgrade proposals**. If it sees a proposal that gets approved, cosmovisor can automatically **download the new binary** , ..., **switch from the old binary to the new one** , and finally restart the node with the new binary. 

Wait, what? It looks like the watchdog program scans through `stdout` to determine if an update has occurred. If that's true, then this is completely insane! All you would have to do is find a way to write to `stdout` and the process manager would update your binary. Is this real? 

This was the position we were in: a horrible design flaw staring us in the face. While Nathan and I were reviewing the Cosmos SDK, this documentation caught my eye. And there was no going back. Both of us had been here before though. Most of the time, these "obvious" issues turn into sad and unfruitful dead ends. But this time, for once, it was real. Our deep dive into the codebase, and all our time chasing down all those loose ends, had finally paid off. I want you to join us on our journey through the high of discovering, exploiting, and reporting this bug. 

For those outside of the blockchain space, this is an interesting application security issue that requires no blockchain-specific knowledge. For those in web3, this is a fascinating wake up call that not all bugs are in smart contracts; they can be within the infrastructure of the blockchain too. Enjoy! :) 

##  Background 

###  Cosmos SDK 

Ethereum allows for the execution of arbitrary code on the blockchain. However, as the first of its kind, it has several drawbacks: 

  * The transactions per second (tps) is extremely slow at around 14 per second.
  * Gas, or paying for your code to be executed on the network, is expensive.
  * Lack of customization of the functionality of the blockchain provided to its developers.
  * Lack of built-in _interoperability_ between other blockchains. Bridges exist but are clunky and prone to vulnerabilities.

What's the solution to these problems? Create something that is faster, cheaper and allows for customization as well as interoperability between other blockchains. The **Cosmos SDK** is a blockchain development framework that perfectly meets all of these criteria to make _application-specific_ blockchains. Application-specific blockchains are services made for a specific project, allowing more control over the ecosystem for the developers and users. 

For instance, instead of having a trading platform as a smart contract on Ethereum, a project can create their own blockchain that natively runs all the required code for the trading platform. This allows for the developer to customize various low level features of the blockchain, such as gas costs, node settings and more. Additionally, the Cosmos SDK has Inter-Blockchain Communication (IBC) as a central feature, which allows for developers to communicate with other Cosmos blockchains by default to transfer funds or other operations. 

Cosmos comes with various **modules** that developers can pick and choose from depending on their needs. Each of these modules provides some sort of additional capability for the blockchain, and the plug and play nature of them makes building the blockchain significantly faster. For instance, there is a `bank` module for handling ownership over tokens and a `governance` module for voting on changes to the blockchain. 

###  Cosmovisor 

![Cosmos Node Output](https://maxwelldulinwebsite.s3.us-east-2.amazonaws.com/cosmovisor_rce/CosmosNodeOutput.png)Figure 1: Cosmos Node Output

A _node_ is an individual instance of a blockchain running within the network. `[Cosmovisor](https://docs.cosmos.network/v0.50/tooling/cosmovisor)` helps manage the node as a watchdog program. It keeps track of the logs, performs upgrades and allows for easy starting and syncing of additional nodes for the blockchain. An image of the node running is shown above in _Figure 1_. 

When an upgrade is required, a user _proposes_ an update via the `governance` module, which everyone votes on. If the proposal gets enough votes from the other users, then at a specific block (point in time) the blockchain will get updated with this new information. From fine-tuning parameters to changing the code of the chain itself, this is a general purpose method for updating the blockchain in a decentralized fashion. 

If a proposal is approved and includes an update to the chain, the `governance` module will output a string to `stdout`. The Cosmovisor software will download the new binary, as specified by `stdout`, and restart itself using this new application. The automatic download and upgrade is awesome for keeping the blockchain up-to-date, but it would be horrifying if a single user could force an upgrade. Remember this for later! 

Since Cosmovisor functions as a _wrapper_ or watchdog method around the Cosmos blockchain binary, most of the configurations are controlled with _environment variables_ . A few important ones are listed below: 

  * `DAEMON_NAME`: The name of the binary of the blockchain that is being executed.
  * `DAEMON_ALLOW_DOWNLOAD_BINARIES`: Allow Cosmovisor to download the new application binary and replace the current one. Defaults to `false` but many projects have instructions to turn this on.
  * `DAEMON_RESTART_AFTER_UPGRADE`: If an upgrade occurs (either manually or via the feature above), restart the application automatically. This defaults to `true`.

##  First Blood 

###  Magic Regex 

While reading through the code, Nathan found the regex responsible for parsing the upgrade information: 

![Upgrade Regex](https://maxwelldulinwebsite.s3.us-east-2.amazonaws.com/cosmovisor_rce/UpgradeRegexExplained.png)Figure 2: Upgrade Regex

The Cosmovisor was searching every single line of both stdout and stderror using the regex shown in _Figure 2_. From reading source code and looking at test files, we get a good idea of how this works: 

  1. **Upgrade Name** \- `".*"`: The name of the upgrade itself. The cosmovisor will create a folder for the new upgrade with this name.
  2. **Upgrade Height** \- `(height)(\d+)`: The block number in which the blockchain should be updated. All systems need to be updated at the same time in order to keep the blockchain running smoothly.
  3. **Upgrade Information** \- `(\S+)):\s+(\S*)`: Upgrade JSON. This has various fields for determining how to perform the upgrade and looks extremely juicy for potential exploitation. Below are two of the important fields: 
  * **Target System** : The architecture that this upgrade binary is for. For instance, `linux/amd64`.
  * **Link** : An HTTP link to the location to grab the binary from. This can include a SHA hash on it as well. For instance, `https://maxwelldulin.com/hacker.sh`.

###  Initial Testing - Project Tests 

When testing ideas, it's important to _"fail fast"_. I try to find the fastest and laziest way that I can test out theories. If I'm being generous, 1 out of 1000 big ideas work for me. This is done in order to save time on bad rabbit holes. To me, building out a full Cosmos SDK blockchain with Cosmovisor would likely result in time wasted. So, how do we test this fast? 

My buddy [Zach Minneker](https://twitter.com/seiranib) enlightened me to use the _tests_ of projects when doing binary fuzzing. Why not use tests here as well? Tests usually have examples of happy paths for getting functionality working. Additionally, the projects usually develop _wrappers_ for testing functionality without having many external dependencies for setup, allowing for the isolation of specific code. In this case, Cosmovisor has an in-depth set of tests that are easy to run and modify for our own needs. Playing with these was incredibly useful for understanding how the update process functions. 

The test suite used _files_ as input for stdout/stderr. We copied an existing test for the upgrade functionality and created a file with our payload. To our surprise, this magically worked! The injected string in the test file triggers the update. This is absolute madness. 

###  Secondary Testing - Creating a Print Sink 

The test framework was quite fruitful for our initial testing. From modifying the code and running tests, we were convinced that a bad string would be able to trigger the Cosmovisor update functionality. However, we needed to reproduce this within a real blockchain. This is because there may exist functionality preventing this attack from working that we did not fully understand, or simply didn’t see during our code analysis. So, we looked for a blockchain running a vulnerable version of Cosmovisor, and ended up setting up a [Desmos](https://desmos.network/) node for testing, mostly because they have great [documentation](https://docs.desmos.network/testnet/create-local). 

Like before, we want to _"fail fast"_. Instead of trying to find a way to print an arbitrary string (aka _print sink_), we compiled our own print statement into easy-to-hit functionality. We called the added code to trigger the print statement and **Cosmovisor saw the update and processed it!**

Seeing the call to `fmt.Println(...)` perform the update was surreal. This is when the idea became reality. Reading the documentation, running the tests and setting up the test environment was 100% worth it! Now, let's find a _real_ print sink to trigger this vulnerability on a real project. 

##  Finding a Print Sink 

Sometimes, trying to pwn an application requires gaining super esoteric knowledge. Don't be afraid to enter these murky waters when granted strange primitives. Take the time to really understand what you're working with. In the case of [Qualys](https://www.qualys.com/2023/07/19/cve-2023-38408/rce-openssh-forwarded-ssh-agent.txt), they could load and unload DLLs but nothing else but were still able to get code execution. 

To exploit this, we are going to become experts on _how_ the Cosmos SDK logs data and _what_ it logs. This is a great example of the requirement of learning extremely niche stuff in order to exploit a vulnerability. To our surprise, this took days upon days of reading code in order to exploit because of unexpected functionality of the Cosmos SDK logging. I will not bore you with the description of how we got there; I'll simply explain how it works below. Just know, this took lots of trial and error to come to. 

###  Logging in Cosmos SDK 

![Cosmos Logger Code](https://maxwelldulinwebsite.s3.us-east-2.amazonaws.com/cosmovisor_rce/CosmosSDKLogger.png)Figure 3: Cosmos Logger Code and Output

  
The Cosmos SDK uses the [logger](https://docs.tendermint.com/master/nodes/logging.html) from Tendermint, the consensus and networking layer of Cosmos. The logger utilizes conditional logic for _when_ to output to stdout/stderr depending on the verbosity setting. The node operator specifies the log verbosity of the application binary at startup. 

Depending on the type of output the developer of the module wants to give, different functions are called. There are three: `Error()`, `Info()` (default visibility) and `Debug()`. Using these functions and the requested visibility of the logs, the data will be outputted accordingly. The tiered logging setup is common within large projects such as this one. 

The function used for logging requires a single parameter but can accept more, The first parameter is a _string_ to be outputted describes the logs and the data to come. After this, a developer can provide multiple `key` and `value` pairs that will be outputted. The output looks like this: `LogString key1=value1, key2=value2`. An example of this can be seen in _Figure 3_ for both the code being executed (left) and the log output (right). 

The `key=value` within the string is **quote escaped**. What does this mean? The logger will turn `"` into `\"` whenever we output a double quote to the logs. Does this matter? Immensely! This was a huge set back for us because this breaks the regex parsing mentioned above in _Figure 2_. The quote escaping was the real reason we got stuck for this attack. 

###  What We Need 

From many hours of reviewing the logger code and dynamic testing, we understood the limitations of the system. So, what can we do? What types of _sinks_ should we look for in the code? 

  * **Beginning of Logging Function** : The initial string at the beginning of the log is _not quote escaped_. So, if we could find a sink to get a string added into the first parameter of the logger, then it will get rendered properly.
  * **fmt.PrintLn()** : This is the standard logging mechanism in Golang. Even though there is a set logging mechanism, not every developer will use it.

###  The Perfect Sink 

After a week of work, Nathan and I read through the Cosmos SDK four times each and had downloaded various projects using the SDK to see if they had issues. Eventually, we started looking for usages of `sprintf()` within the beginning parameter of the logger function. 

Sometimes, going through the same code with new knowledge allows us to see new issues compared to before. I commonly find bugs on a third or fourth pass through a codebase since code from one place may help me understand code in another location. After a week of searching and at the very end of night seven, we found the [param](https://github.com/cosmos/cosmos-sdk/blob/main/x/params/proposal_handler.go#L35) module with this beautiful [sink](https://github.com/cosmos/cosmos-sdk/blob/883264db1bdfd8aa89af715a09cbd1f7b835b1b7/x/params/proposal_handler.go#L35): 

![Perfect Logger Sink](https://maxwelldulinwebsite.s3.us-east-2.amazonaws.com/cosmovisor_rce/LoggerCodeSnippet.png)Figure 4: Perfect Logger Sink in Params Module

The code in _Figure 4_ is for proposing a new `param` change within the Cosmos SDK. The parameters provided could be an arbitrary key and an arbitrary value. According to our specifications, the sink was the initial string of the logger and was using `%s` within a format string for `sprintf()`, which is not quote escaped. With these specifications, we should be able to put double quotes inside of here and create valid JSON! To make matters _better_ , there is no input validation prior to this within the Cosmos SDK; we can provide literally any string for these, making it the _perfect_ sink. 

Could this situation get better? Yes! The code path (`param` module) is available in every blockchain using the Cosmos SDK. Second, the code utilizes the `.Info()` function, which is the default visibility of the logger. Finally, it does not require any crazy setup, circumstances or special authorization. We can call a _single_ function from the Cosmos SDK CLI in order to hit this code. All of this together means that a single call to any Cosmos blockchain could result in get code execution or knock the node offline. 

##  Exploitation 

All that is required is to make a single call to the Cosmos blockchain via the CLI. Depending on the version of the SDK, `param` will either be its own module or be under `governance`. For our own testing, we chose to use `Desmos`, since we had a working node already installed on the system which uses `gov`. NOTE: This is not a flaw in Desmos specifically. 

The parameter change proposal is a JSON file when used from the CLI. The _sink_ is within this proposal JSON data. Below is an example of valid JSON, with `<payload_here>` as filler for our attack data: 
  
  
  {
  "title": "TitleDK",
  "description": "DescDK",
  "changes": [
  {
  "key": "PwnMe",
  "value": "**PAYLOAD HERE** ",
  "subspace": "bank"
  }
  ],
  "address": "desmos1jtu..."
  }
  

The payload for `value` field is below. I removed this from the JSON above because it is really messy. It should be noted that since the string is within the JSON the payload needs to be quote escaped here (`\"` instead of `"`). 

![Injected Upgrade Payload](https://maxwelldulinwebsite.s3.us-east-2.amazonaws.com/cosmovisor_rce/ExploitInjectedUpgrade.png)Figure 5: Injected Upgrade Payload

How does this sink payload work? Remember the regex from above? Our goal is to match this perfectly within either the `key` or `value` proposal field. The fields within the payload, as seen in _Figure 5_ , are shown below: 

  * **chain2** : The chain upgrade name. This can be an arbitrary string but needs to match the regex.
  * **linux/amd64** : Architecture key for the `binaries` field. In this case, we were testing on a Linux system but it can be set up on others as well.
  * **http://hacker.com/hacker.sh** : The exploit code link. Cosmovisor will reach out to this URL in order to get the new binary to execute. Since we arbitrarily control this field with stdout, we get code execution from this. Whooo!
  * **Space** : After the fake JSON blob, we must put a **space** afterwards. This is required because we want the regex parsing to stop prior to using unintended characters in the logging output. From our initial testing, not including a space caused failures because of a comma in the logs after our `value`. 

Below is the CLI call for sending the proposal to hit the print sink for Desmos. A similar call can be used for other projects though: 
  
  
  $ desmosd tx gov \
  submit-legacy-proposal param-change \
  **proposal.json** --from test_user
  

The call is simply executing the _parameter change_ proposal from the CLI. The real magic comes from the `proposal.json` file crafted above, which contains the string to force our upgrade. 

What does this look like for real? Watch the proof of concept below. This goes from executing the command to getting RCE on the box. 

Figure 6: Exploit Video PoC

If you want to follow along, there is a completely Dockerized proof of concept on my Github at [mdulin2](https://github.com/mdulin2/cosmovisor_rce_exploit). This contains a demo environment that will automatically install a Cosmos SDK (Cronos, Desmos or Osmosis) and run the node. Then, within the docker container, there is a bash script with the environment configured that will run the exploit. Feel free to play around with the environment to get a better grasp at what is going on. 

##  Impact 

When the remote download flag is turned on, then this vulnerability results in **remote code execution** (RCE). A compromised validator could get all of its funds stolen. However, the worst case is that a malicious actor could have compromised all nodes in order to force the network to perform malicious actions, such as token transfers to themselves. 

If the remote download flag is turned off, the vulnerability acts as a **denial of service** (DoS) bug. This is because when the update fails, the node does not reboot. Being able to take down a blockchain is catastrophic; it leads to a lack of trust in the system and does not allow actions to be performed by its users. Both of these attacks have horrifying consequences: either compromising nodes or taking the blockchain offline. 

Fortunately (or unfortunately), the Cosmovisor documentation at the beginning of the article, was in an _old version of the README.md_. The bug only existed in the v0.1.0 version of the tool. However, it existed in the Cosmos-SDK main branch until version 46.0 since the updated Cosmovisor was kept in a separate branch for whatever reason. So, who is really vulnerable? 

  * People still using v0.1.0 of Cosmovisor. Since there were no notices of security related updates, there are likely many long time nodes running that are vulnerable to this attack.
  * Installing directly from the SDK. Many projects fork the main Cosmos-SDK and are using a version prior to 46.0. So, users compiling from source or building from these repos are also vulnerable. I call this the Android Problem. 

Because of these requirements, we were unsure of just how many potential node operators across the Cosmoverse would be vulnerable to this attack, since it’s impossible to know which version of Cosmovisor is being run locally on a node. But the prevalence of forked, un-upgraded versions of the Cosmos SDK made us realize this was likely a non-trivial issue, and might affect more chains than we initially thought. 

One question remained though: how was this already fixed in the newest versions of Cosmovisor? After some digging, we realized we had rediscovered a bug! A developer saw this as a [potential issue](https://github.com/cosmos/cosmos-sdk/releases/tag/cosmovisor%2Fv1.0.0) and [rewrote](https://github.com/cosmos/cosmos-sdk/commit/13559f9132637326e24408a93e28c71f7a76c848) the tool to use _files_ instead of stdout. Good on them for figuring this out! They mentioned this attack was theoretically possible but there was never any mention of an exploit path in the Github issue and no urgency regarding upgrades. 

##  Reporting 

![Advisory from Cosmos](https://maxwelldulinwebsite.s3.us-east-2.amazonaws.com/cosmovisor_rce/Advisory.png)Figure 7: Advisory from Cosmos

Honestly, we were just trying to _understand_ the Cosmos SDK when we found this bug and one another one. Luckily for us, the Cosmos SDK has a [bug bounty program](https://hackerone.com/cosmos). 

Unluckily for us, the bug in this blog post was considered _out of scope_. Recently, they [expanded](https://medium.com/the-interchain-foundation/amulet-strengthening-security-across-the-interchain-fa4b0bafadb4) the program to make these classes of vulnerabilities in scope but it was after I had reported this bug. I wonder if this report had anything to do with that? Anyway, this is an awesome step in the right direction for the Cosmos SDK team. With millions of dollars at stake, it should be the [impact](https://medium.com/immunefi/what-is-primacy-of-impact-fd09b820c91) on the ecosystem that matters and not some scope document that does not cover every impact imaginable. As a result, they gave us a $1250 bonus for our work, which was super nice of them, especially considering this was a bug in older version of the Cosmos SDK, and it was unclear exactly what the scope of impact was. 

We found another vulnerability within the Cosmos SDK as well. This bug was a simple role based authorization bug within the [circuit](https://docs.cosmos.network/main/modules/circuit) module. Read the [HackerOne](https://hackerone.com/reports/2120609) report or the [Github](https://github.com/cosmos/cosmos-sdk/pull/17511) pull request to get more insight on this. This vulnerability netted us more than the bug in this post; $2K and a $500 bonus for a good report. 

Overall, we took home 3.75K for two bugs in the Cosmos SDK. The [team](https://twitter.com/amuletdotdev) was really nice to work with and I'd be happy to report bugs to [this program](https://hackerone.com/cosmos) in the future. These were the first two bugs that I had reported via HackerOne and I had a good experience doing it. This also ended up with a [disclosure](https://forum.cosmos.network/t/amulet-security-advisory-for-cosmovisor-asa-2023-001/11456) on the Cosmos SDK forums, which was cool to see after all of this work. A screenshot of this is shown in _Figure 7_ of the disclosure. 

##  Takeaways 

From every finding and every project, there is always so much to learn. Whether it's a new thing or an old trick that just was particularly useful this time around, I always try to document a few takeaways. 

  * **Fail fast** : Do the absolute minimum you can to disprove an idea. If this does not work, then keep doing the easiest thing until you're convinced that you've got something. This will save a tremendous amount of time in the long run.
  * **Esoteric Knowledge** : Exploitation sometimes requires the usage of strange primitives. In our case, we needed a string outputted to stdout. Taking the time to understand the ecosystem at play will drastically increase your chances of exploitation. Without a deep understanding of the logger, this exploit would not have been possible.
  * **Multiple passes** : Going through a code base multiple times is good. I used to be hesitant of this but when new knowledge comes you never know what you may have missed originally.
  * **Good reports** : Nathan and I spent a good amount of time crafting three separate Dockerized PoCs for this vulnerability with easy to follow instructions for a variety of different Cosmos based blockchains. For the second bug, we wrote up our own test file to showcase the bug. From this, we got a substantial amount of extra money, which made the time spent absolutely worth it. So, take the time to write up easy-to-follow PoCs with thorough explanations to get better payouts. The developers fixing the bugs you find greatly appreciate it as well. 

##  Conclusion 

For me, this was a major confidence boost. Finding a serious RCE/DoS bug and an access control vulnerability is a great start to our journey in the Cosmos world. Bug bounty programs reward those who obtain specialized knowledge and who are willing to go where other people are not. 

Thanks for joining me in my understanding of a bug that Nathan Kirkland and I discovered in the Cosmos SDK. I hope you found this interesting and learned from the security discussions. Thanks to Max Arnold and Nathan Kirkland for reviewing the post and the Cosmos SDK team for disclosing and fixing the bugs. Feel free to reach out to me (contact information is in the footer) if you have any questions, comments about this article or anything else. Additionally, if you want an audit of your Cosmos project, feel free to reach out as well. Cheers from **Maxwell "ꓘ" Dulin**. 

  
  

[Maxwell Dulin](https://www.linkedin.com/in/maxwelldulin/)![](/static/Mail.png)Email me![![](/static/twitter.png)Twitter](https://twitter.com/Dooflin5)[![](/static/g.png)Github](https://github.com/mdulin2)[![](/static/admin.png)Admin](/Login)[![](https://cdn0.iconfinder.com/data/icons/basic-ui-elements-round/700/08_rss-512.png)Blog RSS Feed](https://maxwelldulin.com/api/rss/blog)[![](https://cdn0.iconfinder.com/data/icons/basic-ui-elements-round/700/08_rss-512.png)Resources RSS Feed](https://maxwelldulin.com/api/rss/resources)
