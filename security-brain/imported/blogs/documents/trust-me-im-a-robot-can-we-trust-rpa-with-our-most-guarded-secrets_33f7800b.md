---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-18_trust-me-im-a-robot-can-we-trust-rpa-with-our-most-guarded-secrets.md
original_filename: 2022-08-18_trust-me-im-a-robot-can-we-trust-rpa-with-our-most-guarded-secrets.md
title: 'Trust Me, I’m a Robot: Can We Trust RPA With Our Most Guarded Secrets?'
category: documents
detected_topics:
- command-injection
- automation-abuse
- supply-chain
- sso
- access-control
- sqli
tags:
- imported
- documents
- command-injection
- automation-abuse
- supply-chain
- sso
- access-control
- sqli
language: en
raw_sha256: 33f7800b4541ac82380ac2f4e7bc7f35f58f7368ed7cf4ab1f85bbaeeb3479c9
text_sha256: 232e80b14475b61265956ff48fecf0fe49e3ee01deb035407347baeffc2ffa9f
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: true
---

# Trust Me, I’m a Robot: Can We Trust RPA With Our Most Guarded Secrets?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-18_trust-me-im-a-robot-can-we-trust-rpa-with-our-most-guarded-secrets.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, supply-chain, sso, access-control, sqli
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: True
- Raw SHA256: `33f7800b4541ac82380ac2f4e7bc7f35f58f7368ed7cf4ab1f85bbaeeb3479c9`
- Text SHA256: `232e80b14475b61265956ff48fecf0fe49e3ee01deb035407347baeffc2ffa9f`


## Content

---
title: "Trust Me, I’m a Robot: Can We Trust RPA With Our Most Guarded Secrets?"
url: "https://www.cyberark.com/resources/threat-research-blog/trust-me-i-m-a-robot-can-we-trust-rpa-with-our-most-guarded-secrets"
final_url: "https://www.cyberark.com/resources/threat-research-blog/trust-me-i-m-a-robot-can-we-trust-rpa-with-our-most-guarded-secrets"
authors: ["Nimrod Stoler (@n1mr0d5)", "Nethanel Coppenhagen"]
programs: ["Blue Prism"]
bugs: ["Robotic Process Automation", "Insecure deserialization", "SQL injection", "MiTM"]
publication_date: "2022-08-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2290
---

# Trust Me, I’m a Robot: Can We Trust RPA With Our Most Guarded Secrets?

August 18, 2022 Nimrod Stoler and Nethanel Coppenhagen

  * Share this Article
  * [Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Ftrust-me-i-m-a-robot-can-we-trust-rpa-with-our-most-guarded-secrets)
  * [Twitter](https://twitter.com/share?text=Trust%20Me%2C%20I%E2%80%99m%20a%20Robot%3A%20Can%20We%20Trust%20RPA%20With%20Our%20Most%20Guarded%20Secrets%3F&url=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Ftrust-me-i-m-a-robot-can-we-trust-rpa-with-our-most-guarded-secrets&via=CyberArk)
  * [Email](/cdn-cgi/l/email-protection#635c101601090600175e200c0d17060d1746515305110c0e4651530e1a4651532b160146515245020e1358010c071a5e200b0600084651530c1617465153140b0217465154104651530b021313060d0a0d044651530217465153201a01061122110846515246532246532237111610174651532e064651204651532a462651465b53465a5a0e46515302465153310c010c1746502246515320020d46515334064651533711161017465153313322465153340a170b4651532c16114651532e0c101746515324160211070607465153300600110617104650254653222a0d4651530c1611465153000c0e130f0a0002170607465153020d07465153000b020f0f060d040a0d04465153060d17061113110a1006465153140c110f0746512046515317111610174651530a104651530d0c17465153091610174651530a0e130c1117020d17465153462651465b53465a574651530a17462651465b53465a5a1046515302465153150a17020f4651530f0a0d084651530a0d465153170b064651530f0c0d04465153000b020a0d4651530c05465153060d17061113110a1006465153101600000610104d4651532a054651531a0c16462651465b53465a5a1506465153061506114651530e020d0204060746515313060c130f06465153140b0c465153070a070d462651465b53465a5a1746515317111610174651530c0d064d4d4d4653224653220b171713104650224651254651251414144d001a0106110211084d000c0e4651251106100c1611000610465125170b110602174e110610060211000b4e010f0c0446512517111610174e0e064e0a4e0e4e024e110c010c174e00020d4e14064e17111610174e1113024e140a170b4e0c16114e0e0c10174e041602110706074e10060011061710)
  * [LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Ftrust-me-i-m-a-robot-can-we-trust-rpa-with-our-most-guarded-secrets&title=Trust%20Me%2C%20I%E2%80%99m%20a%20Robot%3A%20Can%20We%20Trust%20RPA%20With%20Our%20Most%20Guarded%20Secrets%3F&summary=In%20our%20complicated%20and%20challenging%20enterprise%20world%2C%20trust%20is%20not%20just%20important%20%E2%80%94%20it%E2%80%99s%20a%20vital%20link%20in%20the%20long%20chain%20of%20enterprise%20success.%20If%20you%E2%80%99ve%20ever%20managed%20people%20who%20didn%E2%80%99t%20trust%20one...)

![](https://www.cyberark.com/wp-content/uploads/2022/08/hero-blog.jpeg)

In our complicated and challenging enterprise world, trust is not just important — it’s a vital link in the long chain of enterprise success. If you’ve ever managed people who didn’t trust one another, you probably know that a team without trust isn’t really a team: It’s just a group of individuals, working together, often making disappointing progress, at best.

We know how it is sometimes difficult to establish trust between human group members, so what about robots? Can we trust robots when they are introduced into our workplace?

Our research in this post is focused on robotic process automation (RPA). So, first things first: There aren’t really any electro-mechanical robots involved. RPA is **not** about physical robots. It is a software technology that makes it easy to build, deploy and manage **software robots** that emulate human actions, interacting with digital systems and software. RPA is designed to handle and automate repetitive, routine tasks found in most business processes.

Many industries are currently benefiting from RPA, from banking and finance to human resources, healthcare, customer service, and marketing and sales, all with one common denominator: the extensive use of enterprise credentials. Whether it is financial data, employee files, medical records or customer details, access credentials to those enterprise applications are placed in the “hands of the robot.”

So, back to our original question: Can we trust (RPA) robots?”

**A Fictional Story of the McGuire & Finn Attack**

It all started one afternoon at the (totally fictitious) McGuire & Finn private banking firm. McGuire & Finn was established in 1913 by two young financiers. In the more than a century that it’s been in business, the firm has never experienced a single cyberattack…but that’s about to change!

Six months ago, McGuire & Finn deployed a state-of-the-art RPA platform and has since completely integrated RPA processes into its daily work routines. The time savings generated, as well as the reliability of the data reported and prepared by the robots, allow McGuire & Finn’s staff to work more efficiently on increasingly complex tasks, leaving the uninteresting, repetitive jobs to the robots.

On that afternoon, one of McGuire & Finn’s customer support personnel received an email with an urgent call:

_“Your password will expire in 1 day(s)”_

and a few lines afterwards:

_“Please follow the link below to update your password=***REDACTED***

This was a devious phishing email, leveraging a remote code execution attack against the corporate email application known as CVE-2021-31949.

By clicking the link on that phishing email, the unsuspecting McGuire & Finn customer support person started the grim chain of events.

With their foot in the door, the attackers can now run some reconnaissance on the network to conclude that a Blue Prism RPA infrastructure is installed. A few more seconds elapse and a fresh copy of the Blue Prism demo package is downloaded from the internet.

**RPA Architecture**

Diving somewhat into the technical details, we begin with the architecture of the Blue Prism RPA infrastructure.

![](https://www.cyberark.com/wp-content/uploads/2022/08/image1.png)

Fig. 1: Blue Prism architecture. Source: <https://bpdocs.blueprism.com/bp-6-7/en-us/helpBPServer.htm>

In Figure 1 above, we see the basic Blue Prism RPA architecture: an application server connected to a database server on the one hand, and multiple runtime resources and interactive clients on the other hand.

The runtime resources, or digital workers as they are elsewhere called, are the actual software robots. These are the machines (or sometimes just virtual machines) that would perform the business processes and interact with the enterprise’s digital systems. Interactive clients are graphic control consoles, generally connected to the application server. The interactive clients allow RPA admins, users, developers, testers and auditors to manage the RPA infrastructure, each from their own endpoints.

A client-server software architecture is in charge of the connection between the application server, runtime resources and interactive clients.

To facilitate client-server communications and build a service-oriented backend, Blue Prism is using the Windows Communications Foundation (WCF) as its primary recommended connection mode. In the next section, we take a first peek at WCF and how it is configured and used.

**WCF**

Windows Communication Foundation (WCF) is an SDK for developing and deploying services on Windows. WCF provides a runtime environment for .NET applications, which unifies the capabilities of Microsoft’s .Net into a single, common, general service-oriented programming model for communication.WCF provides a common approach using a common API that allows developers to focus on their applications rather than on the communication protocol.

Windows Communication Foundation has actually replaced .Net Remoting, which is now considered legacy technology by Microsoft[i].

**Blue Prism WCF Stack**

The Blue Prism software is supporting four different WCF connection modes:

  * **WCF: SOAP with Message Encryption & Windows Authentication**
  * **WCF: SOAP with Transport Encryption & Windows Authentication**
  * **WCF: SOAP with Transport Encryption**
  * **WCF: Insecure**

To better understand what each of these stands for, we need to first familiarize ourselves with Windows Authentication.

**Microsoft Security Stack**

Name | What? | How?  
---|---|---  
Transport Encryption | Message Encryption | Session Security  
Further encryption of all network data | Encryption of SOAP information HTTP headers are cleartext | Signing and encrypting network data  
Chain of certificates authored by a certificate authority (CA) | AD domain username and password | AD domain username and password  
NTLM | Authentication | AD domain username and password  
  
**Windows Authentication**

The Blue Prism application is using the NTLM protocol to affect a Windows Authentication in a Windows Active Directory domain scenario. The NTLM protocol is used to authenticate a client to a server. The client is the one that wishes to authenticate itself (an interactive client or a runtime resource), and the server is the one that validates this authentication (the Blue Prism application server).

NTLM is a challenge-response authentication protocol. When the client requests access to a service associated with the domain, the service sends a challenge to the client, requiring them to perform a mathematical operation using its authentication token (usually some form of username and password), and then return the result of this operation to the service. The service may validate the result or send it to the domain controller (DC) for validation. If the service or DC confirms that the client’s response is correct, the client is allowed access to the server.

![](https://www.cyberark.com/wp-content/uploads/2022/08/image2.png)

Source: en.hackndo.com/ntlm-relay/

**Session Security – Signing and Sealing**

Blue Prism applications use Microsoft’s NTLM session security for both signing and sealing of messages.

In order to reinforce the NTLM protocol, due to its inherent deficiencies[ii], message integrity and confidentiality are used. Since a malicious NTLM client may change a valid message on the fly quite easily, NTLM can be configured to apply a message authentication code (MAC) to each message. This MAC is verified by the recipient and provides a strong assurance that the message was not modified while traversing the network. “Sealing” a message means applying encryption to prevent it from being viewed by a third party in transit. NTLM uses a variety of symmetric encryption mechanisms, while the keys are some permutations of the client’s user password.

These functionalities prohibit domain users that don’t have access to the client’s user password from impersonating the client on the network and is an important addition to the plain NTLM authentication protocol.

**Message Encryption (WCF)**

Securing messages between clients and services is essential to protecting data. Windows Communication Foundation (WCF) is a SOAP message-based distributed programming platform that provides message encryption functionality for exchanging secure messages based on existing security infrastructure for SOAP messages.

WCF message-level security encrypts request and response messages. This way, confidential information incorporated in client-server communications, such as credentials and passwords used by the RPA infrastructure, may be encrypted in such a way that only the intended message recipient can read the message. Message security provides end-to-end channel security and is independent of the transport protocol. Anyone watching the wire exchange at that level should remain oblivious to the contents of the message.

**Transport Encryption (WCF)**

The final brick in the Microsoft .NET security stack is described as transport encryption, but it has a much more important role than just another layer of encryption.

As seen above, the security stack already includes two different levels of encryption, session security and message encryption, so why another level?

WCF transport encryption is using Transport Layer Security (TLS) to create another encryption layer, but it also uses the intricate certificate system applied in TLS to do two different things:

  * Encrypt network data using encryption keys not related to the user’s password; and
  * Authenticate the server to the client, making it almost impossible to break the chain of WCF client-server communications, which is in charge primarily of protecting clients from rogue servers.

TLS uses a server certificate signed by a third-party certificate authority. Clients, such as the Blue Prism interactive client or the Blue Prism runtime robots, would only connect to an application server if it presents a properly configured and signed certificate. When things are properly defined, fabricating such a certificate is not feasible. This makes it extremely difficult for an attacker to masquerade as an application server on the Blue Prism infrastructure. Such an attacker would have to present a signed certificate to elicit clients to connect, and that is practically impossible without having access to the certificate authority signing keys.

To sum up, the Blue Prism RPA application is heavily encrypted, as supported by the Microsoft Windows and WCF infrastructure for authorization, signing and confidentiality purposes.

**The Story Continues**

By this time, the fictitious McGuire & Finn’s perimeter is already breached. After arming the phishing email and sending it to a weak link at the private banking firm, our attacker has gained a certain foothold inside its Windows Active Directory domain.

With the Blue Prism demo package, the attackers can now learn more about the client-server infrastructure Blue Prism uses.

**Attack I: Stealing Blue Prism’s Master Encryption Keys**

Looking into the Blue Prism code, the attacker quickly notes that it is using Microsoft’s WCF client-server architecture. WCF, in stark distinction to its predecessor, .NET Remoting, is about clients calling a closed list of specified **methods** on the server. Calling client-server methods is always unidirectional, similar to calling a function.

Looking into the Blue Prism code, all interesting server methods are detailed in the **IServer** class under a special Blue Prism .NET dll called AutomateAppCore.dll.

Each server method is preceded with a OperationContract attribute, which tells the .NET framework to allow the following method to be called from connected clients and prepares the surrounding serialization and deserialization of input and output parameters (more on this in **Attack 3** below).

![](https://www.cyberark.com/wp-content/uploads/2022/08/image3.png)

Each of these method names is then implemented in the clsServer class below:

![](https://www.cyberark.com/wp-content/uploads/2022/08/image4.png)

The clsServer class is the home of all WCF server method implementations, plus many more helper function implementations. This considerably inflates the size of the clsServer module.

In the image above, the blue numbers to the left of the code are line numbers. We are currently at line 18,000+, and the entire file reaches more than 34,000 lines of code! That’s a large module by any criterion.

Let’s zoom in on one of the WCF server methods:

![](https://www.cyberark.com/wp-content/uploads/2022/08/image5.png)

WCF server methods in the Blue Prism code include a security preamble called SecuredMethod (in yellow) that defines the level of permissions required by a client in order to call the method. Then comes the method name, its parameters and return type, and then, usually as the first executable line of the method, a call to CheckPermissions()(in red), which is in charge of making sure the client caller is indeed a Blue Prism authenticated user and authorizes that the calling user has the required permissions in accordance with the security preamble.

A client calling a server method without the required permissions will be rejected and the server will throw an exception.

There may be certain cases where server methods should be called when users are not yet authenticated. For such cases, Blue Prism uses the UnsecuredMethod preamble, like so:

![](https://www.cyberark.com/wp-content/uploads/2022/08/image6.png)

Naturally, a client requesting a login is not yet authenticated. So, Login functions are defined as unsecured methods, and clients that have not authenticated themselves to the server may call them.

The clsServer class contains a lot of methods and many lines, but our attackers refused to give up. After scanning 34,000+ lines for the third or fourth time, to their astonishment, around line 2,600, the following cryptic method is revealed:

![](https://www.cyberark.com/wp-content/uploads/2022/08/image7.png)

Let’s zoom in on it:

![](https://www.cyberark.com/wp-content/uploads/2022/08/image8.png)

This GetEncryptionSchemes() method seem to be part of the IServer class (although it is physically located in clsServer), but it obviously has no SecuredMethod preamble and no call to CheckPermissions().

The method itself seems to be requesting a database connection and calling a local GetEncryptionSchemes with the connection and **true**. The return from GetEcnryptionSchemes is a collection of encryption schemes that is returned to the client caller.

![](https://www.cyberark.com/wp-content/uploads/2022/08/image9.png)

In the local GetEncryptionScheme() helper method, the true parameter gets the name: “**includeKey** ”. This is getting interesting!

Following the code to GetEncryptionSchemeFromDB(), we see that the includeKey parameter (which is true in our case) is also transferred to the function.

Digging into this helper method, we see that when **includeKey** is true, the function copies the master encryption algorithm and the key itself in the collection that returns to the client caller.

![](https://www.cyberark.com/wp-content/uploads/2022/08/image10.png)

This sounds very promising, but can we call the method from an unauthenticated client?

Let’s see the demo…  

**Attack I: Conclusions**

The attacker’s persistence at McGuire & Finn has certainly paid off in this case. After reading and re-reading a total of more than 100,000 lines of code, the attackers managed to find this single WCF server function, which led them to obtain Blue Prism’s encryption master keys, and completely unauthenticated to Blue Prism, being only a domain user.

However, come to think of it, the attackers only have half of what is necessary to launch any kind of successful attack. Holding the master encryption keys for a symmetric encryption means they only have half of the “treasure map.” An attacker would need to chain this first attack with another attack, as in the following examples:

  * In gaining access to a database administrator’s account or finding a malicious DBA, the attacker gets access to the encrypted credentials. Since the attacker already has access to the encryption master keys, they can easily decrypt all credentials and other encrypted information on the database and exploit those credentials.
  * The attacker may set up a man-in-the-middle attack between the Blue Prism application server and the MSSQL server. They can then eavesdrop on communications between the application server and the MSSQL server. It is assured that credentials will be transferred on the network when the robots need them to log in to enterprise applications. For more, see: <https://blog.blindspotsecurity.com/2017/12/advanced-sql-server-mitm-attacks.html>
  * If the attacker can find database backups somewhere on the network that are not completely encrypted, they would gain access to the encrypted credentials and passwords, which they can decrypt with the encryption master keys.

But our attacker would not stop here, as they are contemplating another interesting attack vector: a SQL injection.

**Attack II: SQL Injection Is Dead! Long Live SQL Injection!**

Knowing he needs access to the Blue Prism’s database and seeing all the database operations in the code, our attacker decided to look for a SQL injection attack.

SQL injection attacks are one of the oldest, most known and most dangerous vulnerabilities. In this attack, a malicious code is inserted into a string that is later passed to a database instance for parsing and execution. The rule for preventing SQL injection attacks is to strictly perform input validation and use parameterized queries.

The Blue Prism application religiously follows that rule, as shown in the below example:

![](https://www.cyberark.com/wp-content/uploads/2022/08/image15.png)

In this code, the strings are obfuscated, but when debugging, we can see that:

217290= “UPDATE BPASysconfig set ResourceRegistrationMode = @mode”

217217=”@mode”

So the SQL command string contains an “UPDATE” SQL command with the table name and value to be set. But instead of the user-controlled value, an at (“@”) sign and the string “mode” is appended to the SQL command string. This way, the SQL command remains constant, and no user-controlled information can be inserted into the SQL command itself.

One line below, an AddWithValue function is used to actually insert the parameter value. But, again, this is not part of the SQL command string, and therefore, whatever the value of the parameter may be, it will not trigger a SQL injection.

Our attacker scanned dozens of Blue Prism functions, and ALL of them were very well-protected against SQL injection.

**Stored Procedures**

Another method to prevent SQL injections, also used by Blue Prism, is to use stored procedures. Stored procedures are a set of SQL statements with an assigned name that can be reused and shared by multiple programs. They are particularly important from a security perspective, since they can be used to allow access to some parts of a table in a database while denying direct operations on the table. That means users cannot directly write SQL queries that do what they want to the database tables, but can only use existing, pre-programmed SQL queries that have been approved by the software developers.

So, when our attacker realized that all SQL commands were properly programmed to prevent SQL injection, he decided to look into the Blue Prism stored procedures and see if he could find anything there.

![](https://www.cyberark.com/wp-content/uploads/2022/08/image16.png)

In the figure above is a list of Blue Prism’s stored procedures. They contain all sorts of routines that gather analytics to display on the Blue Prism charts and home screen.

However, at the top (in the red rectangle) there is a “System Stored Procedures” folder. Inside, there are hundreds of default stored procedures that are installed with the MSSQL installation. Our attacker went through them one by one until he found this one:

![](https://www.cyberark.com/wp-content/uploads/2022/08/image17.png)

As the name “sp_sqlexec” suggests, it takes in one parameter, p1, and simply executes that string as a SQL statement.

That’s great for our attacker!

If only he could find a way to call this sp_sqlexec stored procedure from a Blue Prism client.

Going back to the code and scanning all the server functions, our attacker found the GetChartData() function, which is used by a client to read analytics from the server.

![](https://www.cyberark.com/wp-content/uploads/2022/08/image18.png)

A client may call GetChartData() with a dataSourceName, which is actually the name of a MSSQL stored procedure, and a dictionary of parameters. In addition, according to the “SecuredMethod”, the caller only needs to be a Blue Prism user with no specific permissions.

The GetChartData() function calls this.GetChartData, which gets us here:

![](https://www.cyberark.com/wp-content/uploads/2022/08/image19.png)

The dataSourceName is simply copied into the SQL command and the command type is StoredProcedure.

Let’s see a demo of how our attacker does this:

**Attack II: Conclusions**

The attackers at McGuire & Finn used stored procedures to perform a successful SQL injection attack, even though stored procedures are usually used to prevent them. By allowing any Blue Prism client to call the GetChartData() method, our attacker managed to misuse that function to invoke the sp_sqlexec stored procedure. The sp_sqlexec stored procedure simply executes any user-provided SQL command, leading to a simple SQL injection attack.

With this attack, our attacker can:

  * Get encrypted credentials that can be decrypted with the key obtained in the first attack.
  * Run code on all the robots, since all the processes’ codes are stored in the database.
  * Run code on the Blue Prism’s MSSQL server with elevated privileges.

With the success of their attacks so far, in which they have stolen the encryption master keys and taken over the MSSQL server to steal stored credentials from the database, the attackers at McGuire & Finn are now set to launch their most impactful attack ever, one that would place all the credentials in their hands and allow them to control (almost) the entire Blue Prism RPA infrastructure: the insecure deserialization attack!

**Attack III: Insecure Deserialization**

The Microsoft WCF platform, as a client-server communications facilitator, is serializing function calls and their parameters across the network from the client to the server and back.

**Serialization** is the process of converting a data object into a series of bytes that save the state of the object in an easily transmittable form. It is essentially a mechanism to transform an object into a byte stream that can be transferred through the network to the receiver.

**Deserialization** is exactly the other way around. It recreates an object and its state (whatever the data of the object was), from a byte stream sent across the network.

Deserialization vulnerabilities concerning Microsoft’s **.NET Remoting** have been extensively reviewed by James Forshaw[iii] and others[iv]. By cleverly injecting malicious class information in the serialized data, attackers can force a receiving target that is deserializing the data to practically run malicious code.

Deserialization vulnerabilities are devastating. If an attacker can perform a proper deserialization attack that injects its own byte stream into the serialized data, it means the attacker is already running code in the context of the server. The attacker can then take control of other machines on the infrastructure using only WCF, without even touching the vendor’s code.So, all the vendor-specific protections aren’t even called, and an unauthenticated attacker, exploiting a deserialization flaw, can gain full control over the server and possibly other machines on the network.

An example of insecure (Java) deserialization is the **Equifax breach**[v]. In September 2017, Equifax announced it had suffered a major breach, with over 143 million consumers’ personal data compromised. This was due to an insecure Java deserialization vulnerability, which led to remote code execution on Equifax servers and the theft of millions of customer records.

To better understand why serialization and deserialization are required, let’s look at some examples from the Blue Prism code:

![](https://www.cyberark.com/wp-content/uploads/2022/08/image11.png)

In this server-side code printout, a server method called GetSkill() is implemented. It has a SecuredMethod preamble with its allowed client permissions, and it is calling the CheckPermissions() method right at the beginning to make sure the calling client is indeed authenticated by the RPA platform and that the client has the appropriate permissions.

The GetSkill() method takes one parameter, a Guid class, does something with it, and returns one parameter, a Skill class.

On the client side, the call to the server-side method looks like this:

![](https://www.cyberark.com/wp-content/uploads/2022/08/image12.png)

The client-side protected method PopulateStageData() seems to initialize some of its local parameters, and then, on line 273, it calls:

App.gSv.GetSkill(…)

This is how a client-side code calls the server-side application server, with Microsoft’s Windows Communications Foundation (WCF) making this client-server architecture programming easy for developers. By simply calling the server method with its parameters inside the client-side code, the developer sets in motion a huge, complex machine that prepares the SOAP message to be sent to the server. The details of the client, along with the specific method being executed and the method’s parameters, are all nicely **serialized** into the SOAP message.

The WCF client code then sends that message to the server over the network. The server would decipher that message, make sure all parameters are present, and then **deserialize** the stream of bytes back into code objects (yes, **real, live code objects!**) and invoke the required server-side method with those parameters.

If attackers are able to insert their own parameters into the previously serialized data stream, the deserialization process would take those malicious parameters and make code objects out of them. In certain scenarios, these code objects may “persuade” a server to actually run code.

After the WCF infrastructure on the server has deserialized and regenerated the id Guid object, the WCF code would call the GetSkill() method with the Guid object, collect its return value (in our case, it is a Skill class), build a reply SOAP message with the serialized Skill class, and send it across the network back to the client.

Now, it is the client WCF code’s turn to deserialize the Skill class byte stream information from the SOAP message, build a Skill class object from the deserialized information, and return that value, as if the method was locally called. WCF is indeed a marvel, isn’t it?

By changing the serialized message (on either the client or server side)), attackers may insert their own objects (usually called “gadgets”) into the data stream, thereby forcing the WCF deserializer to rebuild object classes that the sender did not intend. In extreme cases, an attacker can force a deserialization of malicious byte data, which would run arbitrary code on the deserializing side.

**Launching the Attack**

By looking into the decompiled server code, our attackers have found a weak link in the server method ScheduleCreateSchedule(). The exact class used by Blue Prism – **SessionRunnerSchedule** is incorporating an Object parameter, called mAbortLock, which is effectively a wildcard parameter. An attacker can insert their gadget code into this wildcard parameter and abuse the deserializing side.

In the next screenshot, we can see the use of object mAbortLock in the SessionRunnerSchedule class:

![](https://www.cyberark.com/wp-content/uploads/2022/08/image13.png)

This translates to the following XML data on wire after serialization from the client to the server side:

![](https://www.cyberark.com/wp-content/uploads/2022/08/image14.png)

In this screenshot, we can see the “Header” of the message in the yellow rectangle, the “Body” of message in green, and right below that, the method name to be executed on the server: “SchedulerCreateSchedule”. Then, at the bottom in a yellow rectangle, we can see the serialized **mAbortLock** parameter, which equals “true.”

The attacker’s plan is to replace the benign “true” value of the **mAbortLock** object with a malicious gadget that would deliver a set of malicious objects to the server.

However, since the actual WCF code is protected by digital signatures and is difficult to change, our attacker decides to use a tool called **Frida** to make the required change after the data has been serialized by the sender (the client in our case) and before it is actually sent through the network to be deserialized by the receiver (in our case, the server).

**What’s Frida?**

Frida is an open-source dynamic instrumentation framework. Using Frida, we can hook into existing functions running on the system and basically inject code or change ingoing or outgoing parameters and return values. The exact use of Frida is outside the scope of this blog post. For further information about using Frida, see: <https://frida.re/>.

Let’s see the attack demo…

By injecting a malicious gadget instead of the mAbortLock object in the serialized byte stream, the attackers managed to leverage their hold over the McGuire & Finn network and gain remote code execution on the Blue Prism application server, which is running as an **elevated user**.

Such an attacker would gain access to everything on the MSSQL server and would gain unabridged access to the application server (including the encryption master keys we extracted on the first attack vector) to run code on all robots, and in certain cases to run code on interactive clients[vi].

To the best of our knowledge, this is the first time an insecure deserialization attack has been demonstrated against a fully encrypted WCF application.

Although beyond the scope of this blog post, by taking over the Application Server, elevated attackers would be able to change all Runtime Resource process codes, thus practically remotely running code on all Runtime Resource. With their control over the Application Server, attackers can use a kind of ’reverse’ deserialization attack, where the Application Server would return the malicious code back to a calling Interactive Client. By doing that, an attacker-controlled Application Server would ’infect’ calling Interactive Clients to eventually remotely run code on them as well.

**Final Conclusions and Mitigations**

In this blog post, we set out to see if we can trust robots with our most valued secrets and credentials. Our road has been a bumpy one, but all’s well that ends well. During our Blue Prism research, we discovered eight vulnerabilities in different levels of severity, from critical to medium, three of which have been detailed in this blog post. Since CyberArk Labs reported the issues to Blue Prism over a period of more than four months, the Blue Prism security team has been working tirelessly to resolve them and has included us throughout the entire process. Blue Prism’s cooperation in defining and fixing vulnerabilities is unmatched. At this point in time, all security issues we reported have been fixed.

**Some mitigations:**

  * Always treat **recommended** vendor procedures as a must. If you can’t, make sure you understand the security implications and build your defenses accordingly.
  * Protect MSSQL and Blue Prism application server network communications. Make sure to use the highest means of encryption to minimize the chances of a MITM attack.
  * Incorporate defense-in-depth, e.g., network monitors, endpoint protections, etc.
  * As attackers use the principle of least resistance, install external credential vault and other defenses to drive attackers to look for less resistant victims.

**Disclosure Timeline**

  * April 11, 2022: A disclosure report was sent to Blue Prism security
  * April 14, 2022: Blue Prism responded that they received our report and are considering its content
  * August 8, 2022: Blue Prism issues a security bulletin
  * August 10, 2022: CVEs were issued
  * August 10, 2022: Public disclosure

[i] See: <https://docs.microsoft.com/en-us/previous-versions/dotnet/netframework-3.0/72x4h507(v=vs.85)?redirectedfrom=MSDN>

[ii] See, for example, <https://serverfault.com/questions/266607/is-there-a-security-concern-exposing-ntlm-authentication-over-http-or-should-it>

[iii] <https://www.tiraniddo.dev/2019/10/bypassing-low-type-filter-in-net.html>

[iv] <https://research.nccgroup.com/2019/03/19/finding-and-exploiting-net-remoting-over-http-using-deserialisation/>

[v] <https://cynation.com/the-equifax-data-breach/>

[vi] Although beyond the scope of this blog post, by taking over the Application Server, elevated attackers would be able to change all Runtime Resource process codes, thus practically remotely running code on all Runtime Resource. With their control over the Application Server, attackers can use a kind of ’reverse’ deserialization attack, where the Application Server would return the malicious code back to a calling Interactive Client. By doing that, an attacker-controlled Application Server would ’infect’ calling Interactive Clients to eventually remotely run code on them as well.
