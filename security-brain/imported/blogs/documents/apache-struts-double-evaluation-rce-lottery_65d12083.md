---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-04_apache-struts-double-evaluation-rce-lottery.md
original_filename: 2018-10-04_apache-struts-double-evaluation-rce-lottery.md
title: Apache Struts double evaluation RCE lottery
category: documents
detected_topics:
- supply-chain
- sso
- xss
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- supply-chain
- sso
- xss
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 65d12083f353c96feaf94ef85b2c88f40e79a582a1e7821312f357af8f558adc
text_sha256: 443dadad39e2989f3629bcdb682d1353a94072f5335375df76a9607d6200892e
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Apache Struts double evaluation RCE lottery

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-04_apache-struts-double-evaluation-rce-lottery.md
- Source Type: markdown
- Detected Topics: supply-chain, sso, xss, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `65d12083f353c96feaf94ef85b2c88f40e79a582a1e7821312f357af8f558adc`
- Text SHA256: `443dadad39e2989f3629bcdb682d1353a94072f5335375df76a9607d6200892e`


## Content

---
title: "Apache Struts double evaluation RCE lottery"
page_title: "Apache Struts double evaluation RCE lottery | GitHub Security Lab"
url: "https://securitylab.github.com/research/apache-struts-double-evaluation/"
final_url: "https://securitylab.github.com/research/apache-struts-double-evaluation/"
authors: ["Man Yue Mo (@mmolgtm)"]
programs: ["Apache Struts"]
bugs: ["RCE", "Double OGNL evaluation"]
publication_date: "2018-10-04"
added_date: "2022-12-05"
source: "pentester.land/writeups.json"
original_index: 5662
---

In this post I’m going to cover a type of RCE vulnerability in [Apache Struts](https://struts.apache.org/) called a double evaluation. This type of issue is not normally considered critical by the Struts security team as it relies partly on the user of the framework putting some untrusted data in a template or a configuration file. However, as the behaviour of double evaluation is fairly counter-intuitive, developers can easily get caught out and expose their Struts applications to RCE. This [article](http://blog.orange.tw/2018/08/how-i-chained-4-bugs-features-into-rce-on-amazon.html) is a very good example of how a skilled attacker can make use of double evaluations to trigger RCE in real world applications. (The example is using a framework called Seam, but the problem is the same as with Struts.) There is also an entry in [OWASP](https://www.owasp.org/index.php/Expression_Language_Injection) that contains examples from Spring with regard to [CVE-2011-2730](https://seclists.org/fulldisclosure/2011/Sep/78).

In April 2018, I reported the issues I found to the Struts security team. At the end of August, 2018, I received the following response:

> Thanks for your interest on helping Struts, I appreciate your help J Please consider that I don’t recognized that as a vulnerability. OGNL has ability of double evaluations. It’s the user business to check end user provided data for dangerous code injection when he/she would like to double evaluate end user raw data against OGNL.

In other words, it is now the user’s responsibility to make sure that they don’t accidentally trigger double evaluations in Struts. Regardless of whether these should be considered vulnerabilities in Struts itself, I figured that I should disclose these issues publicly so that the users can be made aware of them.

## Mitigation

This post is rather technical and includes lots of detail about the discovery of the vulnerabilities. Users who want to know about the background of the problem should look at the section below this called “Double Evaluation “. In the currrent section, I’ve written a brief summary of advice for Struts users who just want to know how to stay safe:

  1. Do not use the either the `${..}` or `%{..}` syntax in [Struts tags](https://struts.apache.org/getting-started/using-tags.html) or Struts configurations (including the XML configurations and in-code configurations with the [convention plugin](https://struts.apache.org/plugins/convention/)) at all. For Struts tags, the use of `%{..}` is against the security advice given [here](https://struts.apache.org/docs/s2-029.html) and [here](https://struts.apache.org/docs/s2-036.html), while the use of `${..}` is against the advice given [here](https://struts.apache.org/docs/s2-053.html). For XML, it is not against any existing advice, but the problem is the same. The `${..}`/`%{..}` syntax doesn’t always do what you might expect and the exact behavior depends on individual tags/configurations. Even if it is not a security problem, it can be buggy. If you must use one of these syntaxes and you are 100% certain about what you are doing, then do not pass user input into them. Bear in mind that user input can often come in surprising ways, e.g. via binding of properties in an `Action`, or some stored database entities that originate from user input.

  2. Do not use the [`AliasInterceptor`](https://struts.apache.org/core-developers/alias-interceptor.html) with any of the names or aliases set with user input. So, in following example, neither `name` nor `value` in the `param` tag should come from remote user input (e.g. `#{#parameters['name'][0] : #parameters['value'][0]}` or if `name` and `value` are properties of `SomeAction` with pubic setters). In this case, any value that `name` or `value` happens to be will be evaluated directly as OGNL.
  
  <action name="someAction" class="com.examples.SomeAction">
  <param name="aliases">#{ name : value }</param>
  <interceptor-ref name="alias"/>
  <interceptor-ref name="basicStack"/>
  <result name="success">good_result.ftl</result>
  </action>
  

  3. Do not try to sanitize OGNL input by looking for `${..}` or `%{..}` in user input. Some tags/configurations, as well as the `AliasInterceptor`, will just evaluate user input as OGNL without them being wrapped inside the special `${..}` or `%{..}` syntax. This makes it hard to sanitize input.

## Double evaluation

Generally speaking, double evaluation, as its name suggests, is when an expression string gets evaluated as code, and then, if the result is another string, it gets evaluated as code again.

Let’s take a look at some concrete examples. The very first issue of this kind that I know of is [S2-012](https://struts.apache.org/docs/s2-012.html). This issue was rated “Moderately Critical” and was described as a showcase app vulnerability. Back then, the showcase app had the following action in the configuration:
  
  
  <action name="save" class="org.apache.struts2.showcase.action.SkillAction" method="save">
  <result type="redirect">edit.action?skillName=${currentSkill.name}</result>
  </action>
  

The key here is `${currentSkill.name}`. The `${}` (or `%{}` as I’ll explain later) here is a special syntax that indicates the content inside it should be treated as an OGNL expression. The expression first evaluates to the `name` property of the field `currentSkill` of the action. This property is set from a form submitted by the end user. Normally we would not expect this to be a problem because whatever `currentSkill.name` is, it should be then treated as a string literal, or html. For example, in a JSP template such as
  
  
  <h1><%=request.getParameter("name") %></h1>
  <div id=${param["name"]}>
  <h1>${param["name"]}</h1>
  </div>
  

if the `name` request parameter happens to be `${1+1}`, then all of the above will output as `${1+1}`, instead of carrying on to evaluate `${1+1}` and outputing 2. (You may have problems with html injection with the above, but that’s a different issue, and JSP does provide a means to deal with it.)

However, with double evaluations, if a user sets this `name` property to a string of the form `${expr}`, then after evaluating `${currentSkill.name}`, `expr` will be treated as an OGNL script and will be evaluated again, which, of course, results in RCE. Moreover, this issue did not just affect the showcase app, but any application that contained something like this in the configuration file:
  
  
  <action name="someAction">
  <result type="redirect">someString...${some user input}</result>
  </action>
  

The next issue is [S2-015](https://struts.apache.org/docs/s2-015.html). This is rated as “Highly Critical” and the set-up is very similar to S2-012. The security bulletin ticket provides this as an example of a vulnerable configuration:
  
  
  <result type="httpheader">
  <param name="headers.foobar">${message}</param>
  </result>
  

and this as the PoC (`%24%7B1%2B1%5D` is the encoded form of `${1+1}`):
  
  
  http://localhost:8080/example/HelloWorld.action?message=%24%7B1%2B1%5D
  

What is interesting here is that the expression `${message}` in the vulnerable configuration first evaluates to the `message` property of the `HelloWorld` class in the showcase app. In this (rather old) case, the property has a public setter, therefore it gets bound automatically to a query parameter named `message` in the request. This is how the OGNL script from the PoC gets into the `${message}` expression in the configuration file. While this is not uncommon for MVC frameworks, it is quite easy to get caught out and forget that properties in an action can be controlled by an end user.

Three years after S2-015, the next issues of this type that were found were [S2-029](https://struts.apache.org/docs/s2-029.html) and [S2-036](https://struts.apache.org/docs/s2-036.html). Issue S2-029 was rated as “Important”, while S2-036 rated as “Medium”. The only details I found on these issues are [here](http://www.freebuf.com/vuls/99432.html). For the benefit of readers who can’t read Chinese, I’ll summarize the details of S2-029 here. This issue affects two [Struts tags](https://struts.apache.org/getting-started/using-tags.html), the `text` and `i18n` tags, when the `name` attribute in these tags is set to an OGNL expression, for example:
  
  
  <s:i18 name="%{#parameters['name']}">xxxx</s:i18n>
  <s:text name="%{#parameters['name']}">xxxx</s:text>
  

Again, if the `name` parameter evaluates to another valid OGNL expression, then it will be evaluated again and cause an RCE. The [vulnerable code](https://github.com/apache/struts/blob/d5e0fe9207e86f11eb3ef3a77bd6dcb3aa2028ce/core/src/main/java/org/apache/struts2/components/I18n.java#L109-L110) in the `i18n` class at that time was:
  
  
  public boolean start(Writer writer) {
  boolean result = super.start(writer);
  
  try {
  String name = this.findString(this.name, "name", "Resource bundle name is required. Example: foo or foo_en");  //<-- first evaluation in `findString`
  ResourceBundle bundle = (ResourceBundle) findValue("getTexts('" + name + "')"); //<-- second evaluation in `findValue`
  

In the first line of the `try` block, the `name` property of the tag was first evaluated using the `findString` method (which evaluates its argument as OGNL under the hood). In the next line, the result of this evaluation goes into `findValue`, which again evaluates its argument as OGNL under the hood. The [vulnerable code](https://github.com/apache/struts/blob/ab6750211ba8fc99bffdc156d3bb8f61031ed13d/core/src/main/java/org/apache/struts2/components/Text.java#L147-L156) in `Text` has a slightly longer flow and it uses [`getText`](https://github.com/apache/struts/blob/ab6750211ba8fc99bffdc156d3bb8f61031ed13d/core/src/main/java/org/apache/struts2/components/Text.java#L156) instead of `findValue` for the second evaluation. The issue in `i18n` was fixed [here](https://github.com/apache/struts/commit/8dfe178585d06858eb307cfb2a1bf1995243476a), while the one in `Text` was fixed [here](https://github.com/apache/struts/commit/996475d755820914ea4695729ec46159f12625e0#diff-96f62a0945767c9e6d1bbd13ba6f0111). You may notice that the commit dates of these are much later than the dates of the original issues. Looking at details of S2-029 and S2-036, my speculation is that they were fixed originally by excluding some classes that are accessible to OGNL to stop the reporters’ exploits from working. It seems the fix was then bypassed in S2-036, which prompted a proper fix and, as a result, more classes got excluded.

## Finding double evaluations

Now that I’ve explained what double evaluation is about, and shown some code patterns that lead to double evaluation, let’s try to find them with queries. As with the previous posts, the queries here should be imported as an Eclipse project from [here](https://github.com/Semmle/SecurityQueries). You can run the queries using the CodeQL for Eclipse plugin.

_[EDIT]: You can also use our free CodeQL extension for Visual Studio Code. See installation instructions at https://securitylab.github.com/tools/codeql/._

As I’ve seen with previous double evaluation issues, this type of problem arises when attributes in configuration files get evaluated twice. When a Struts application starts, configuration and template files are parsed and their attributes are used to initialize properties in the corresponding classes. So our sources in this case are properties of classes that can be initialized from configuration or template files. I had a quick look and included the following classes:
  
  
  /** A `Class` whose fields may be initialized from a config file.*/
  class InputClass extends RefType {
  InputClass() {
  hasQualifiedName("org.apache.struts2.views.jsp", "StrutsBodyTagSupport") or
  hasQualifiedName("org.apache.struts2.components", "Component") or
  hasQualifiedName("com.opensymphony.xwork2", "Result") or
  hasQualifiedName("org.apache.struts.action", "Action") or
  hasQualifiedName("com.opensymphony.xwork2.interceptor", "Interceptor")
  }
  }
  

The fields in subclasses of `StrutsBodyTagSupport` and `Component` classes can be initialized from Struts tags in template files, while `Result`, `Action` and `Interceptor` may have their fields initialized from Struts configuration files. There may be other classes as well, but these are the ones that I looked at.

The sink in this case, is again the [OGNL sink](https://github.com/Semmle/SecurityQueries/blob/cae102b26de72d1a01738b50c29864913e0536a0/semmle-security-java/lib/struts/OGNL.qll#L6) that I’ve used previously, as I’m interested in expressions that get evaluated as OGNL. To summarize, I’d like to identify the following issues in the source code of Struts:

  1. The source is a `FieldAccess` of a field from `InputClass`.
  2. The sink is an OGNL sink.
  3. The path must go through the OGNL sink at least once.

Of the above conditions, 3 is the most difficult one to define. If I just do a normal taint tracking with 1 being the source and 2 the sink, then I’ll get all the cases where a field is evaluated only once, which is not what I’m looking for. In order to find these issues, I’m going to need to chain two dataflow configurations together. The first one tracks a `FieldAccess` of an `InputClass` to an OGNL evaluation site, and the second starts from this evaluation site and tracks it into the second OGNL evaluation sink.

![double_eval_config](/assets/img/post-images/double_eval_tracking.png)

However, I cannot just use the previous OGNL sink as the sink of my first dataflow configuration. To understand why this is the case, consider the following paths:
  
  
  String result = findString(this.inputField); //<-- flow from here: findString(this.inputField) ->...-> compileAndExecute(this.inputField)
  String constantResult = findString("someConstant"); //<-- not tainted, but still ended up in compileAndExecute
  findValue(result); //<-- flows into the second evaluation
  findValue(constantResult); //<-- no double evaluation here
  

In the above, I have both `inputField` and `someConstant` being evaluated twice. The evaluation of `inputField` is problematic, but the evaluation of `someConstant` is ok. However, if I start my second taint-tracking from the point of `compileAndExecute`, then as I back-track to the body of `findString`, I would lose the information of where I came from. Consequently, I could either continue into `findString(this.inputField)->result->findValue(result)` or `findString("someConstant")->constantResult->findValue(constantResult)`. The following diagram illustrates this.

![double_eval_problem](/assets/img/post-images/double_eval_problem.png)

As you can see, if I start from `compileAndExecute` when tracking the second evaluation, then when I get to the body of `findString`, I’ll struggle to know where to continue my tracking. From a taint-tracking point of view, both paths into `findString(inputField)` and `findString(constant)` are possible, and I’ll end up getting results in both `findValue(constantResult)` and `findValue(result)`. What I really need is a taint-tracking configuration that looks more like this:

![double_eval_solution](/assets/img/post-images/double_eval_solution.png)

In other words, I want the tracking of the first evaluation to stop as soon as I know that a function is evaluating its argument as OGNL. I can then carry on using the call site of this function as the source to track for the second evaluation. I’ll call these functions “entry points” into OGNL from now on.

## Looking for entry point functions to OGNL

For a function to be an entry point to OGNL, it must first evaluate one of its parameters as OGNL. In other words, at least one of its parameters flows into an OGNL sink. So I’ll start with a taint-tracking configuration that tracks parameters of a function into an OGNL sink:
  
  
  class OgnlCallConfiguration extends DataFlow3::Configuration {
  OgnlCallConfiguration() {
  this = "OgnlCallConfiguration"
  }
  
  override predicate isSource(DataFlow::Node source) {
  exists(Method m | m.getAParameter() = source.asParameter() and
  source.asParameter().getType() instanceof TypeString
  )
  }
  
  override predicate isSink(DataFlow::Node sink) {
  isOgnlSink(sink)
  }
  ... standard edges and barriers
  }
  
  

This can then be used to identify methods that evaluate their parameters as OGNL under the hood:
  
  
  class OgnlCallMethod extends Method {
  OgnlCallMethod() {
  exists(OgnlCallConfiguration cfg, DataFlow::Node source |
  cfg.hasFlow(source, _) and source.asParameter() = this.getAParameter()
  )
  }
  }
  

To identify the entry point methods, I want to find `OgnlCallMethods` that may be called by a non-`OgnlCallMethod`, because that will be the point where I enter OGNL evaluation in the code.
  
  
  public String ognlCallEntry(string expr) {
  return ognlCallNonEntry(expr);
  }
  
  public void execute() {
  ognlCallEntry(this.field);
  }
  

In the above code, `ognlCallEntry` is the entry point as it is the first place in `execute` where I know `this.field` is going to be evaluated as an OGNL expression, while `ognlCallNonEntry` is not.

So, I add a simple condition to make sure that the entry point function is not always called by another `OgnlCallMethod`:
  
  
  class OgnlEntryPointMethod extends OgnlCallMethod {
  OgnlEntryPointMethod() {
  exists(Method m | m.polyCalls(this) and not m instanceof OgnlCallMethod)
  }
  }
  

Running a query to look for `OgnlEntryPointMethod`, I quickly noticed that I got some results, such as `stripExpressionIfAltSyntax`, that do not evaluate its parameters as OGNL at all. Looking at the code path in the path explorer, I saw that this is because the return value of `stripExpressionIfAltSyntax` ended up flowing into `findValue` and getting evaluated.

![stripExpression](/assets/img/post-images/stripExpression.png)

After a further check of the results, I manually removed a couple of the obvious functions that have similar problems. I’ve added the final `OgnlEntryPointMethod` class to [`OGNL.qll`](https://github.com/Semmle/SecurityQueries/blob/master/semmle-security-java/lib/struts/OGNL.qll).

## Taint-tracking pipeline

Now that I’ve identified the OGNL entry point methods. I can start writing my taint-tracking configurations. In the first taint-tracking configuration, I want to follow a field that may come from a user configuration in to an OGNL sink:
  
  
  class InputClass extends RefType {
  InputClass() {
  hasQualifiedName("org.apache.struts2.views.jsp", "StrutsBodyTagSupport") or
  hasQualifiedName("org.apache.struts2.components", "Component") or
  hasQualifiedName("com.opensymphony.xwork2", "Result") or
  hasQualifiedName("org.apache.struts.action", "Action") or
  hasQualifiedName("com.opensymphony.xwork2.interceptor", "Interceptor")
  }
  }
  
  /** A `Field` that may take value from a config file.*/
  class ConfigurableField extends Field {
  ConfigurableField() {
  getDeclaringType().getASupertype*() instanceof InputClass
  }
  }
  

So the source of my dataflow configuration will be an access to these fields, as well as the return of the `getParams` method in `ActionConfig`, which, as its name suggests, also takes input from a configuration file.
  
  
  override predicate isSource(DataFlow::Node source) {
  exists(ConfigurableField f | f.getAnAccess() = source.asExpr() and
  not f instanceof ConstantField)
  or
  //`ActionConfig` params are also taken from configuration.
  exists(MethodAccess ma, Method m | ma.getMethod() = m and
  m.getDeclaringType().hasName("ActionConfig") and
  m.hasName("getParams") and source.asExpr() = ma
  )
  }
  

The sink is now an argument of an `OgnlEntryPointMethod` (or a method that it overrides, to take polymorphism into account).
  
  
  override predicate isSink(DataFlow::Node sink) {
  exists(MethodAccess ma, OgnlEntryPointMethod entry, Method m | ma.getMethod() = m and
  ma.getAnArgument() = sink.asExpr() and entry.overridesOrInstantiates*(m)
  )
  }
  

The `additionalFlowStep`s are pretty much the standard ones that I used before, but I don’t use [`isTaintFieldStep`](https://github.com/Semmle/SecurityQueries/blob/fe2fd1bee433b3009642a673f9a8fcbccbc5ef8c/semmle-security-java/lib/dataflow_extra/ExtraEdges.qll#L9) because the assumption that it makes is no longer valid in this case and, after testing, it gave me too many bogus results. To compensate for this, I added an extra edge to track through the fields of `ActionMapping`, which is a commonly used class.
  
  
  /** Tracks through constructor and getter of `ActionMapping`.*/
  predicate actionMapperEdge(DataFlow::Node node1, DataFlow::Node node2) {
  exists(ConstructorCall c | c.getAnArgument() = node1.asExpr() and
  c.getConstructedType() instanceof ActionMapping and c = node2.asExpr()
  ) or
  exists(MethodAccess ma | ma.getMethod() instanceof ActionMappingGetMethod and
  node1.asExpr() = ma.getQualifier() and node2.asExpr() = ma
  )
  }
  

This dataflow configuration will identify the locations where an expression coming from the Struts configuration may get evaluated. I’ll now feed the call site of these sinks into a second dataflow configuration, the `DoubleEvalConfig`, to identify cases where the input gets evaluated twice:
  
  
  from DoubleEvalConfig cfg, DataFlow::PathNode source, DataFlow::PathNode sink,
  InputCfg input, DataFlow::Node inputSrc, DataFlow::Node inputSink
  where cfg.hasFlowPath(source, sink) and input.hasFlow(inputSrc, inputSink) and
  //use call site of `InputCfg` as source of `DoubleEvalConfig`
  exists(MethodAccess ma | ma = source.getNode().asExpr() and ma.getAnArgument() = inputSink.asExpr())
  select source, source, sink, "$@ from configuration first $@ and then evaluated $@.", inputSrc, "Input", source, "evaluated", sink, "here"
  

where `DoubleEvalConfig` will track into an OGNL sink or an argument of an `OgnlEntryPointMethod`. The final query is in [`double_eval_final.ql`](https://github.com/Semmle/SecurityQueries/blob/master/semmle-security-java/queries/struts/double_evaluation/double_eval_final.ql) I added some extra filters and this one is particularly worth mentioning:
  
  
  not exists(MethodAccess ma | source.getNode().asExpr() = ma and sink.getNode().asExpr() = ma.getAnArgument())
  

After inspecting the results, I saw some “circular” results such as:
  
  
  actionName = conditionalParse(actionName, invocation);
  

where `actionName` got evaluated once by `conditionalParse`, and then set to itself again, which means it may get evaluated again if the enclosing method is called again on the same instance. After some testing, I ruled this scenario out as being unlikely and removed it from the results.

After running this query, I got 18 results, which I then reported to the Struts security team in April 2018 with corresponding RCE exploits. As mentioned before, they rejected them as user errors rather than vulnerabilities in Struts, and do not intend to patch them.

## Double evaluation results in Struts tags

I’ll first go through the results in Struts tags, the location of the source code, as well as the vulnerable configurations.

### UIBean and its subclasses

The first result is in the abstract class `UIBean`. There are two attributes that double evaluate in this class. The first one is the `name` attribute. It first gets evaluated by the `findString` method, and then gets evaluated again by `findValue`. The other one is the `key` attribute, which is used to set the `name` attribute when it is not set in the configuration.

As this code is inside the `evaluateParams` method of `UIBean`, any subclass that does not override this method is affected. A quick query shows that 27 tags may be affected (not counting the inline classes, and probably fewer because there is some branching involved). For example, the following configuration of the `Hidden` tag
  
  
  <s:hidden name="%{#parameters['name']}"/>
  

is prone to RCE if the request parameter `name` is some malicious OGNL payload.

Actually, this can probably pass as a “feature”, because these tags actually treat the `name` and `key` attributes as OGNL and do a single evaluation without the `%{..}` syntax anyway. For example
  
  
  <s:hidden name="#parameters['name']"/>
  

will do a single evaluation of `#parameters['name']` as OGNL and return the string value of the parameter `name`. So really this tag supports both single and double evaluations, depending on whether the `%{..}` syntax is used in the tag. What is curious about these tags is that, when the `%{..}` syntax is used, the result of the first evaluation will be evaluated as an OGNL expression, without the need to be enclosed in the `%{..}` syntax. So, if this tag is in the `HellowWorld.jsp` template
  
  
  <s:hidden name="%{#parameters['name']}"/>
  

then the following request (where `1%2B1` is the encoded form of `1+1`)
  
  
  http://localhost:8080/blank-1.0.0/example/HelloWorld?name=1%2B1
  

will see `name` being evaluated to `2`. This can make it rather hard to sanitize for OGNL in the user input as anything that can be evaluated as OGNL will be evaluated.

### Param tag used with Bean tag

The next result is in the `Param` tag. Depending on whether the `value` attribute is set or not, the `name` attribute evaluated in two different places. They then go into the `addParameter` method of `component`.
  
  
  String name = findString(this.name); //<-- First evaluation
  ....
  if (suppressEmptyParameters) {
  if (value != null && StringUtils.isNotBlank(value.toString())) {
  component.addParameter(name, value); //<-- second evaluation
  } else {
  component.addParameter(name, null); //<-- second evaluation
  

It turns out that, if `component` is a `Bean`, then its `addParameter` method will call the `setProperty` method of `OgnlReflectionProvider`, which evaluates `name` as OGNL. For example, the following in a JSP template
  
  
  <s:bean name = "org.apache.struts2.util.Counter" var = "counter">
  <s:param name = "%{#parameters['property']}" value = "20"/>
  <s:param name = "last" value = "25" />
  </s:bean>
  

is vulnerable to RCE if the `property` query parameter is an OGNL string. Interestingly, the `name` attribute in the `Param` tag does not support single evaluation, so if I do
  
  
  <s:bean name = "org.apache.struts2.util.Counter" var = "counter">
  <s:param name = "#parameters['property']" value = "20"/>
  <s:param name = "last" value = "25" />
  </s:bean>
  

then the `#parameters['property']` in the `name` attribute will be treated as a string literal and not be evaluated at all. So, you either have double evaluations with the `%{..}` syntax or no evaluation at all. This is again different from the `Text` and `i18n` tags that were fixed with S2-029 and S2-036, where the `%{..}` indicates a single evaluation and double evaluation is not supported at all. So, what you get from `%{..}` depends on the specific tag and attribute.

To be fair, it is probably not very likely that anyone would dynamically select a property of a `Bean` based on user input anyway, given that the `Bean` and its fields are known at the time of the configuration.

### Text tag, again

The last one in Struts tags is in the `Text` tag. Here the `name` attribute first gets evaluated by `findString` and passed into the `getText` method of `TextProviderHelper` as the `defaultMesssage` argument.
  
  
  actualName = findString(name, "name", "You must specify the i18n key. Example: welcome.header"); //<-- first evaluated
  String defaultMessage;
  if (StringUtils.isNotEmpty(body)) {
  defaultMessage = body;
  } else {
  defaultMessage = actualName;  //<-- defaultMessage tainted
  }
  
  Boolean doSearchStack = false;
  if (searchStack != null) {
  Object value = findValue(searchStack, Boolean.class);
  doSearchStack = value != null ? (Boolean) value : false;
  }
  
  String msg = TextProviderHelper.getText(actualName, defaultMessage, values, getStack(), doSearchStack); //<-- goes into `getText`
  

In the `getText` method, if `searchStack` is set to true, then `defaultMessage` will be evaluated again. So for example, this tag will be vulnerable to RCE.
  
  
  <s:text name="%{#parameters['name']}" searchValueStack = "true"/>
  

This is a rather unlikely configuration as `searchValueStack` is set to false by default and it is marked as deprecated. Struts has also fixed this [here](https://github.com/apache/struts/commit/5b167b8efdf0b124b57e0baba5f9fb0e7f3b7c1a), but the fix has not been ported to 2.5.17 and 2.3.35 yet (latest version at the time of writing).

These are the results in the Struts tag. The configurations that trigger them are probably not very likely to be found in real world applications, and the use of `%{..}` in Struts tags is against Struts’ advice in S2-029 and S2-036 anyway. (However, it is perfectly inline with Struts’ advice in [S2-053](https://struts.apache.org/docs/s2-053.html), which in fact contains a potentially vulnerable tag `<@s.hidden name="%{redirectUri}"/>` if the property `redirectUri` in the action has a public setter. Then again, having public setters in an `Action` is also against the security advice of [Struts](https://struts.apache.org/security/#do-not-define-setters-when-not-needed), so it is probably OK.)

## Double evaluations in Struts configurations

Now let’s take a look at the results in Struts configurations. The vulnerable configurations here currently do not go against Struts’ advice and in the case of the `AliasInterceptor`, do not even require the use of the special `${..}`/`%{..}` syntax.

### AliasInterceptor, RCE without warning

This is perhaps the most interesting result of the lot as you do not need to use any of the `${..}` or `%{..}` syntax to be vulnerable. There are two places where double evaluation takes place:
  
  
  final Map<String, String> parameters = config.getParams();  //<-- parameters comes from config file.
  
  if (parameters.containsKey(aliasesKey)) {
  
  String aliasExpression = parameters.get(aliasesKey);  //<-- `aliasExpression` tainted.
  ValueStack stack = ac.getValueStack();
  Object obj = stack.findValue(aliasExpression);  //<-- first evaluation.
  
  if (obj != null && obj instanceof Map) {
  ...
  Map aliases = (Map) obj;
  for (Object o : aliases.entrySet()) {
  Map.Entry entry = (Map.Entry) o;
  String name = entry.getKey().toString();  //<-- `name` is tainted
  String alias = (String) entry.getValue(); //<-- `alias` is tainted
  Evaluated value = new Evaluated(stack.findValue(name));  //<-- second evaluation of `name` 
  ...
  if (value.isDefined()) {
  try {
  newStack.setValue(alias, value.get());  //<-- second evaluation of `alias`
  

This affects configurations like
  
  
  <param name="aliases">#{ #parameters['name'][0] : value }</param>
  <interceptor-ref name="alias"/>
  <interceptor-ref name="basicStack"/>
  <result name="success">good_result.ftl</result>
  

or
  
  
  <param name="aliases">#{ 'name' : #parameters['value'][0] }</param>
  <interceptor-ref name="alias"/>
  <interceptor-ref name="basicStack"/>
  <result name="success">good_result.ftl</result>
  

which may cause some surprise when you receive a request like this:
  
  
  https://myDomain.com/myApp?name=expr
  

Note that in both cases, the value of the request parameter is interpreted as OGNL directly, without needing to be wrapped inside the special `%{..}`/`${..}` syntax.

### ServletActionRedirectResult, ActionChainResult, PostbackResult, here we go again

It is a rather unfortunate coincidence that the vulnerable `Result` types in CVE-2018-11776 also have double evaluation issues. Furthermore, you don’t even need to enable `alwaysSelectFullNamespace` or use the convention plugin, and there is also no need to have an unset namespace. However, the user does have to put some untrusted input in the configuration inside a `${..}` or `%{..}` syntax. I’ll go through the result in `ServletActionRedirectResult` here:
  
  
  public void execute(ActionInvocation invocation) throws Exception {
  actionName = conditionalParse(actionName, invocation);  //<-- actionName first evaluated
  if (namespace == null) {
  namespace = invocation.getProxy().getNamespace();
  } else {
  namespace = conditionalParse(namespace, invocation);  //<-- namespace first evaluated
  }
  if (method == null) {
  method = "";
  } else {
  method = conditionalParse(method, invocation);  //<-- method first evaluated
  }
  
  String tmpLocation = actionMapper.getUriFromActionMapping(new ActionMapping(actionName, namespace, method, null));
  
  setLocation(tmpLocation);  //<-- all goes into tmpLocation, and then goes to the field `location`.
  
  super.execute(invocation);  //<-- goes into the `execute` method of `ServletRedirectResult`
  

In the above, the fields `actionName`, `namespace` and `method` are all evaluated once in the `execute` method of the `ServletActionRedirectResult` class, and then get combined into `tmpLocation`, which is used to set the `location` field. The code then calls the `execute` method in the base class `StrutsResultSupport`:
  
  
  public void execute(ActionInvocation invocation) throws Exception {
  lastFinalLocation = conditionalParse(location, invocation); //<-- evaluates `location` the second time.
  doExecute(lastFinalLocation, invocation);
  }
  

So, configurations like this
  
  
  <result type="redirectAction">
  <param name="actionName">${#parameters['redirect']}</param>
  <param name="namespace">/namespace</param>
  </result>
  

or
  
  
  <result type="redirectAction">
  <param name="actionName">myAction</param>
  <param name="namespace">${#parameters['redirectNamespace']}</param>
  </result>
  

or
  
  
  <result type="redirectAction">
  <param name="actionName">myAction</param>
  <param name="namespace">/namespace</param>
  <param name="method">${#parameters['redirectMethod']}</param>
  </result>
  

are all prone to RCE, with a request such as
  
  
  https://myDomain.com/myApp?redirect=%{expr}
  

This somehow reminds me of S2-012. Note that these configurations do not support single evaluations at all, meaning that you either don’t use the `%{..}`/`${..}` syntax and the attributes won’t be evaluated, or they will be evaluated twice.

### `StreamResult`

The issue in `StreamResult` has a very simple flow:
  
  
  protected void doExecute(String finalLocation, ActionInvocation invocation) throws Exception {
  ....
  try {
  if (inputStream == null) {
  LOG.debug("Find the inputstream from the invocation variable stack");
  inputStream = (InputStream) invocation.getStack().findValue(conditionalParse(inputName, invocation)); //<-- evaluates twice on the same line.
  

The field `inputName` first gets evaluated by `conditionalParse`, then again by the `findValue` method of `OgnlValueStack`. This affects the following kind of configurations:
  
  
  <result name="success" type="stream">
  <param name="contentType">image/jpeg</param>
  <param name="inputName">${#parameters['inputName'][0]}</param>
  <param name="contentDisposition">attachment;filename="document.pdf"</param>
  <param name="bufferSize">1024</param>
  </result>
  

The `inputName` field in this case actually “supports” both single and double evaluation. When it is not wrapped inside `${..}`, it will be evaluated once, as OGNL:
  
  
  <result name="success" type="stream">
  <param name="contentType">image/jpeg</param>
  <param name="inputName">#parameters['inputName'][0]</param>
  <param name="contentDisposition">attachment;filename="document.pdf"</param>
  <param name="bufferSize">1024</param>
  </result>
  

Double evaluation occurs when it is wrapped in the `${..}`/`%{..}` syntax. This also means that to attack it, the payload does not need to be wrapped inside the `${..}`/`%{..}` syntax:
  
  
  https://myDomain.com/myApp?inputName=expr
  

Interestingly, the [official documentation](https://struts.apache.org/core-developers/stream-result.html) actually uses the `${..}` syntax in the `inputName` field. Of course, `imageStream` in that example is never going to have a public setter because that would go against Struts’ advice.

### `JasperReportsResult`

I’ve not actually tested these, because they only affect the [jasper report plugin](https://struts.apache.org/plugins/jasperreports/), which does not seem to be widely used. This affects the `dataSource`, `exportParameters` and `reportParameters` fields. The `JasperReportsResult` is first initialized by the `initializeProperties` method
  
  
  private void initializeProperties(ActionInvocation invocation) throws Exception {
  ...
  if (dataSource != null)
  dataSource = conditionalParse(dataSource, invocation);  //<-- first evaluation
  ...
  reportParameters = conditionalParse(reportParameters, invocation);  //<-- first evaluation
  exportParameters = conditionalParse(exportParameters, invocation);  //<-- first evaluation
  }
  

during which various fields are evaluated using the `conditionalParse` method. Some fields then get evaluated again
  
  
  protected void doExecute(String finalLocation, ActionInvocation invocation) throws Exception {
  initializeProperties(invocation); //<-- first evaluation of various fields
  ...
  if (conn == null)
  stackDataSource = new ValueStackDataSource(stack, dataSource, wrapField); //<-- second evaluation of `dataSource` [1]
  ...
  Map reportParams = (Map) stack.findValue(reportParameters);  //<-- second evaluation of `reportParameters`
  ...
  try {
  ...
  Map exportParams = (Map) stack.findValue(exportParameters);  //<-- second evaluation of `exportParameters`
  ...
  }
  

In [1], `dataSource` goes into the constructor of `ValueStackDataSource`, which gets evaluated again.
  
  
  public ValueStackDataSource(ValueStack valueStack, String dataSourceParam, boolean wrapField) {
  this.valueStack = valueStack;
  this.dataSource = dataSourceParam;
  this.wrapField = wrapField;
  
  Object dataSourceValue = valueStack.findValue(dataSource);  //<-- second evaluation
  

Again, these three fields “support” both single and double evaluations, and will evaluate as OGNL once anyway.

## Conclusions

In this post, I’ve explained the issue of double evaluation and showed how to find examples in Struts using CodeQL. I’ve also shown how the `%{..}`/`%{..}` syntax behaves differently depending on the attribute that it is used in. My advice for Struts users is to stop using this syntax in Struts tags and Struts configurations to avoid security issues and other bugs. One question remains: Struts has made some [improvements](https://github.com/apache/struts/commit/9fcbd912bc9ba8eed1ca9bc9422daf79d8b2f6ac) to the `SecurityMemberAccess` in the latest version of Struts which makes double evaluation harder to exploit, so maybe these aren’t exploitable after all?

…Let’s just say there’s more than one way to skin a cat…

Finally, I’ve set up a Struts application that is vulnerable to one of the above issues [here](https://github.com/mmosemmle/alias-example). Do have a go at popping a calculator there. I’ve set the Struts dependency 2.5.12 to simplify the exploit developement so that people can focus on the “interesting” part of the problem. Having said that, the app won’t give up without a fight! (If you think it is as simple as `http://localhost:8080/alias-1.0.0/HelloWorld?name=expr`, then you should definitely try it out!) Answer will be revealed after I write about how to bypass the Ognl security measures in 2.5.16.

## Timeline

  * 20 April 2018: Initial private disclosure of the issues to Vendor
  * 28 August 2018: Vendor rejected issues as vulnerabilities in the framework
  * 04 October 2018: Public disclosure

_Note: Post originally published on LGTM.com on October 04, 2018_
