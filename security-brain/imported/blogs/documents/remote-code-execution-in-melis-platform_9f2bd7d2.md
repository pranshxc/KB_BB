---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-18_remote-code-execution-in-melis-platform.md
original_filename: 2022-10-18_remote-code-execution-in-melis-platform.md
title: Remote Code Execution in Melis Platform
category: documents
detected_topics:
- command-injection
- path-traversal
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- path-traversal
- api-security
- supply-chain
language: en
raw_sha256: 9f2bd7d222f29cfbab5071582ac42bf53b3f5b1c43e1a6dfc69d6196360a0d70
text_sha256: c6d700e15a0b798d9b15e8e4c0bc596758bd00ac81829366f61690655b87dd46
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Remote Code Execution in Melis Platform

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-18_remote-code-execution-in-melis-platform.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `9f2bd7d222f29cfbab5071582ac42bf53b3f5b1c43e1a6dfc69d6196360a0d70`
- Text SHA256: `c6d700e15a0b798d9b15e8e4c0bc596758bd00ac81829366f61690655b87dd46`


## Content

---
title: "Remote Code Execution in Melis Platform"
page_title: "Remote Code Execution in Melis Platform | Sonar"
url: "https://blog.sonarsource.com/remote-code-execution-in-melis-platform/"
final_url: "https://www.sonarsource.com/blog/remote-code-execution-in-melis-platform/"
authors: ["Karim El Ouerghemmi", "Thomas Chauchefoin (@swapgs)"]
programs: ["Melis Platform"]
bugs: ["RCE", "Path traversal", "Insecure deserialization", "Security code review"]
publication_date: "2022-10-18"
added_date: "2022-10-24"
source: "pentester.land/writeups.json"
original_index: 2026
---

## TL;DR overview

  * Sonar's research identified a remote code execution vulnerability in Melis Platform—a PHP CMS—enabling an authenticated attacker to execute arbitrary server-side code through an insecure PHP code path.
  * The vulnerability exploits improper handling of user-controlled data in a CMS feature that reaches a dangerous PHP function, a class of flaw that static analysis with taint tracking can reliably surface.
  * CMS platforms are particularly high-risk targets for RCE because they serve content for many websites: a single compromised CMS instance can affect every site hosted on that server.
  * Melis Platform users should apply the security patch; PHP CMS developers should integrate SonarQube into their deployment workflow to detect injection vulnerabilities in custom modules and themes before they are deployed.

As part of our goal to continuously improve the static analysis engines powering our [Code Quality solution](https://www.sonarsource.com/solutions/clean-code/), we scan many open-source projects. In this case, a scan yielded three critical findings ([CVE-2022-39296](https://github.com/melisplatform/melis-asset-manager/security/advisories/GHSA-7fj2-rrq6-rphq), [CVE-2022-39297](https://github.com/melisplatform/melis-cms/security/advisories/GHSA-m3m3-6gww-7gj9), and [CVE-2022-39298](https://github.com/melisplatform/melis-front/security/advisories/GHSA-h479-2mv4-5c26)) in a software called Melis Platform. 

Melis Platform is an open-source suite with business-oriented features, like an e-commerce component, a CMS, etc. One of its strengths is the support of multiple frameworks to ease the development of custom functionality. Itself, Melis Platform is based on the PHP framework Laminas—an open-source fork of the Zend Framework. 

In this publication, we describe how our SAST engine detected a critical deserialization vulnerability in Melis Platform thanks to its extensive support of popular PHP frameworks. This issue exists since Melis 2.2.0, released roughly 5 years ago, up to and including 5.0.0, and was patched in Melis 5.0.1. 

In the second part of this blog post, we describe how we could confirm its exploitability before reporting it to the project's maintainers.

## Analyzing Laminas-based projects with our SAST engine

In this section, we will see why it is important for a SAST analyzer to have framework-specific knowledge when scanning for vulnerabilities in modern applications. We will do so by looking at our analysis of Melis which is based on Laminas, a popular PHP framework formally known as Zend.

Under the hood, the Sonar AppSec team is responsible for configuring the SAST engine. By defining data sources, dangerous methods ("sinks"), and validation functions ("sanitizers") for each framework, the engine becomes able to perform a comprehensive taint analysis on such projects. This configuration is then validated against synthetic test cases, as well as real-world code bases like Melis Platform.

### Object Injection Vulnerability

During the automated analysis of this project, our SAST engine pointed out an Object Injection vulnerability. You can see what it looks like directly [in the new SonarQube Cloud interface](https://sonarcloud.io/project/issues?resolved=false&types=VULNERABILITY&id=SonarSourceResearch_melisplatform-blogpost&open=AYPmnZsKaFe_ACNVG-cP):

![remote code execution in melis platform body](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/59356396-0903-4f47-8f8a-373040b77eaf/body-eaf5be04-82a2-41f8-8380-2f0a71f84a80_Screenshot%2B2022-10-17%2Bat%2B17.48.38.png)

Let’s have a look at the flow of data as it was reported; it all starts with `MelisPluginRendererController`:

**melis-front/src/Controller/MelisPluginRendererController.php**

Copy to clipboard
  
  
  class MelisPluginRendererController extends MelisAbstractActionController
  {
  public function getPluginAction()
  { 
  // [...]
  $post = $this->getRequest()->getPost()->toArray();  // [1]
  $pluginHardcodedConfig = array();
  if (!empty($post['pluginHardcodedConfig']))
  {
  $pluginHardcodedConfig = $post['pluginHardcodedConfig']; // [2]
  $pluginHardcodedConfig = html_entity_decode($pluginHardcodedConfig, ENT_QUOTES);
  $pluginHardcodedConfig = html_entity_decode($pluginHardcodedConfig, ENT_QUOTES);
  $pluginHardcodedConfig = unserialize($pluginHardcodedConfig); // [3]

This code can be reached without any prior authentication.

The flow starts at `$this->getRequest()->getPost()->toArray()`, at [1]. For identifying this as a source of potentially malicious content, the built-in knowledge about the Laminas framework in our SAST engine comes in handy as the method `getRequest()` is not defined in the source code being scanned. The class `MelisPluginRendererController` extends `MelisAbstractActionController` which itself extends `Laminas\Mvc\Controller\AbstractActionController`. 

From this point, it can be deduced that the method being called is in fact Laminas’ `Laminas\Mvc\Controller::getRequest()` which returns a `Laminas\Http\Request` object. The call chain `getPost()->toArray()` on that object is well understood by our analyzer to return an array basically representing PHP’s superglobal `$_POST` which is user-controlled, and hence potentially malicious. 

An element of the user-controlled array is retrieved [2], and, after decoding, is used in the call to PHP’s `unserialize()` function [3]. Calling this function with user input that is neither sanitized nor validated is [known to lead to serious vulnerabilities](https://owasp.org/www-community/vulnerabilities/PHP_Object_Injection). 

### Patch

Maintainers chose to fix this issue by restricting the classes that can be deserialized: by setting the parameter `$allowed_classes` of `unserialize()` to false, this function is now only able to deserialize simple types, i.e. strings, arrays, and numbers. SonarQube Cloud is able to detect this change and won't raise an issue once this parameter is set to a restrictive value, such as false. 

To exploit this class of vulnerabilities in PHP, it is required to craft something called a "popchain" based on available classes in the context of the impacted applications. In this case, there was no publicly documented popchain and our vulnerability research team had to come up with a new one. Indeed, before reporting this vulnerability to the project's maintainers, we needed to make sure it's exploitable.

Let's see how we did it!

## Crafting a popchain for the Laminas framework

### Popchains?

This concept was first introduced by Stefan Esser in 2009 in his talk [Utilizing Code Reuse/ROP in PHP Application Exploits](https://infocon.org/cons/SyScan/SyScan%202010%20Taipei/SyScan%202010%20Taipai%20presentations/Stefan%20Esser%20-UtilizingCodeReuseOrReturnOrientedProgrammingInPHPApplicationExploits.pdf). You can also find a more academic approach to this topic in a paper written by our very own Head of R&D, Johannes Dahse: [ _Code Reuse Attacks in PHP: Automated POP Chain Generation_](https://dl.acm.org/doi/10.1145/2660267.2660363).

This technique is based on the fact that the execution flow of the program deserializing PHP objects can be affected by the instances being created. After filling out all the serialized properties of the new instance, this process automatically calls the method `__wakeup()` of this instance. When the class instance goes out of scope or at the end of the request, its destructor (`__destruct()`) is called. 

As a result, attackers can try to identify a series of calls starting from one of these methods that could lead to a dangerous action: writing a file to an arbitrary location, executing a command, etc. 

This chain of classes can be made of either:

  * Direct calls, for instance, `$instance->method()`;
  * Indirect calls, with other magic methods or methods of interfaces if the instance is used in such a way. For instance, iterating over a class implementing Iterator automatically calls methods like `rewind()`, `valid()`, etc.

![remote code execution in melis platform body diagram](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/a46a0ca0-2aa9-4064-afe3-442e67eea8d9/body-c1763b3c-b99b-4b59-96a6-214b8e28fa0d_popchain_1.png)

Such gadget chains have to be created on a case-by-case basis, based on classes available to PHP at the time of the deserialization and to autoloaders. It is not possible to declare a new class during this process. To the best of our knowledge, there aren't any public generic chains that would rely solely on built-in classes. Memory corruption vulnerabilities in the deserialization parser and built-in classes were found to be exploitable in the past, but won't be discussed further in this article.

You can already understand that exploiting such vulnerabilities can be very tedious if we have to create new chains from scratch every time. Charles Fol, a security engineer working for Ambionics, created the tool [PHPGGC](https://github.com/ambionics/phpggc) to help others on this task, by collecting existing gadgets for popular targets and frameworks. This tool happens to list a chain for Laminas!

### Prior work on Laminas

A chain leading to the deletion of an arbitrary file was added to PHPGGC by [@MrTuxracer](https://twitter.com/MrTuxracer), and happens to be a perfect example to demonstrate what a simple chain can look like; let's break it down. Its code can be found in [gadgetchains/Laminas/FD/1](https://github.com/ambionics/phpggc/tree/master/gadgetchains/Laminas/FD/1).

It all starts with `unserialize()` creating a new instance of the class `Laminas\Http\Response\Stream`. During the deserialization process, PHP looks for any implementation of the methods `__unserialize()` or `__wakeup()` and executes them. There isn't any in this case, and the script continues.

However, when the PHP interpreter decides to clean this instance from memory, the destructor is called and it happens to call `unlink()` on a property we could set during the deserialization process:

**laminas-http/src/Response/Stream.php**

Copy to clipboard
  
  
  <?php
  
  namespace Laminas\Http\Response;
  
  // [...]
  class Stream extends Response
  {
  // [...]
  protected $streamName;
  
  public function __destruct()
  {
  // [...]
  if ($this->cleanup && is_string($this->streamName) && file_exists($this->streamName)) {
  ErrorHandler::start(E_WARNING);
  unlink($this->streamName);
  ErrorHandler::stop();
  }
  }
  }

![remote code execution in melis platform body- popchain](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/09d7f514-63d8-4944-a047-3b4bfd0e07d0/body-094f3e0a-b33b-4d7c-a0ab-d9d420d8b6b5_popchain_2.png)

Advanced readers can also note the existence of a way to drop references to the newly created instance during the deserialization process; it becomes handy if anything prevents the destructor from being called (e.g. an exception is raised after the call to `unserialize()`). This option is already supported by PHPGGC with its `--fast-destruct` argument. 

Deleting files is already a strong primitive: we could probably force the reinstallation of the application, but this is a destructive operation. Is there a way to craft our own chain to take control of the vulnerable instance, as real attackers would do?

### Finding a new gadget chain for Laminas

It's not the first time that we had to craft a new gadget chain to achieve our goals on an application blindly unserializing untrusted data. This experience taught us that cache systems are often good targets. 

By nature, these components are designed in a way to be loosely coupled with the rest of the application (e.g. automatically trigger save at the end of the lifecycle of the request by using destructors) and support a broad range of storage backends, including filesystems. It can also be assumed that gaining the ability to control what's stored in the cache can be abused later upon its retrieval, this data is always considered to be trusted; more on that later. 

The affected application lists [`laminas/laminas-cache`](https://github.com/laminas/laminas-cache) as a dependency, which in turn requires the supported storage backends: `apcu`, `blackhole`, `mongodb`, `filesystem`, `memcached`, `memory`, `redis`, and `session`. 

After looking at various classes of the high-level cache implementation, one caught our eye because of its destructor indicating that its role is to "save [...] deferred items that have not been committed":

**laminas-cache/src/Psr/CacheItemPool/CacheItemPoolDecorator.php**

Copy to clipboard
  
  
  <?php
  
  namespace Laminas\Cache\Psr\CacheItemPool;
  
  # [...]
  class CacheItemPoolDecorator implements CacheItemPoolInterface
  {
  /**
  * Destructor.
  *
  * Saves any deferred items that have not been committed
  */
  public function __destruct()
  {
  $this->commit();
  }

That means that somehow, there may be a way to use this class to save new items in the cache. Going deeper in this code path, we can notice how all values of `$this->deferred` are handed out to the storage backend to save them in a persistent way:

**src/Psr/CacheItemPool/CacheItemPoolDecorator.php**

Copy to clipboard
  
  
  public function commit()
  {
     // [...]
     foreach ($this->deferred as &$item) {
         if (! $this->save($item)) {
             $notSaved[] = $item;
         }
     }
     // [...]
  }

**src/Psr/CacheItemPool/CacheItemPoolDecorator.php**

Copy to clipboard
  
  
  public function save(CacheItemInterface $item)
  {
  // [...]
  try {
  // get item value and serialize, if required
  $value = $item->get();
  
  // reset TTL on adapter, if required
  if ($itemTtl > 0) {
  $options->setTtl($itemTtl);
  }
  
  $saved = $this->storage->setItem($item->getKey(), $value);
  // saved items are a hit? see integration test CachePoolTest::testIsHit()
  $item->setIsHit($saved);
  // [...]
  }

Good thing that we have this filesystem storage backend available! Because we have control over all the variables of the deserialized classes, we can point the filesystem storage to any file on the local disk and write arbitrary data to it. 

Such a primitive is very powerful in the PHP world, as we only have to create a file with the extension `.php` in the root folder, and any leading data before the first occurrence of `<?php` is going to be ignored by the interpreter. That way, we can create a PHP script on the disk and reach it directly to execute its contents. 

The visualization below summarizes the overall class structure that needs to be put in the popchain for everything to work:

![remote code execution in melis platform body](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/37e72aa1-d284-4bf3-bfc4-a0cb14bda52b/body-d8cbb1d2-b922-48cc-9af5-4413c40f24be_popchain_3.png)

After calling the destructor of the `CacheItemPoolDecorator` instance, the following method invocations happen (we filtered out the calls that are not important, but a lot of things are going to happen):

![remote code execution in melis platform body sheet](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/486f2f5c-1672-404b-8347-2dcab239820e/body-895fe3ab-c84a-41fc-8e67-0dfeb35078db_popchain_4.png)

We tested this chain, successfully gained code execution on our test instance, and published it to PHPGGC. 

If you enjoyed reading this section, don't hesitate to peek at one of our previous publications about a complex chain that was crafted for Drupal during the CTF of Insomni'hack 2019: [CTF Writeup: Complex Drupal POP Chain](https://blog.sonarsource.com/complex-drupal-pop-chain/). And yes, it's also targeting the cache layer!

## Timeline

**Date**| **Action**  
---|---  
2021-06-08| We report all issues to the official contact address with patches and a 90-day disclosure policy.  
2022-09-23| The issue is acknowledged by the vendor.  
2022-09-23| A new version of the affected components is released. CVE-2022-39296, CVE-2022-39297, and CVE-2022-39298 are assigned to our findings.  
  
## Summary

In this article, we presented how our SAST engine is able to detect critical vulnerabilities in real-world projects thanks to our careful support of most frameworks on the market. We also described how attackers would be able to use the deserialization process to impact the underlying server. 

We would like to thank Melis Platform for their patches. Melis users are urged to upgrade their instances to 5.0.1 and above to benefit from these patches.

If you loved what you've just read, and want to help us bring our static analysis technology to the next level, don't hesitate to look at our [open security engineering positions](https://jobs.lever.co/sonarsource/).
