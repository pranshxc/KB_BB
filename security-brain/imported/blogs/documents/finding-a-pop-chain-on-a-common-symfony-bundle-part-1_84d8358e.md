---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-12_finding-a-pop-chain-on-a-common-symfony-bundle-part-1.md
original_filename: 2023-09-12_finding-a-pop-chain-on-a-common-symfony-bundle-part-1.md
title: 'Finding A Pop Chain On A Common Symfony Bundle: Part 1'
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
raw_sha256: 84d8358eb6cee3f7af18153f00b07bb01edaa1d05209c75dcde7479a586accd7
text_sha256: a1ccaead01c5ef7edb5abe071c8ffee62d1735090ab738358341aac5922a4124
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# Finding A Pop Chain On A Common Symfony Bundle: Part 1

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-12_finding-a-pop-chain-on-a-common-symfony-bundle-part-1.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `84d8358eb6cee3f7af18153f00b07bb01edaa1d05209c75dcde7479a586accd7`
- Text SHA256: `a1ccaead01c5ef7edb5abe071c8ffee62d1735090ab738358341aac5922a4124`


## Content

---
title: "Finding A Pop Chain On A Common Symfony Bundle: Part 1"
page_title: "Finding a POP chain on a common Symfony bundle: part 1"
url: "https://www.synacktiv.com/en/publications/finding-a-pop-chain-on-a-common-symfony-bundle-part-1.html"
final_url: "https://www.synacktiv.com/en/publications/finding-a-pop-chain-on-a-common-symfony-bundle-part-1.html"
authors: ["Rémi Matasse (@_remsio_)"]
programs: ["doctrine-bundle (Symfony package)"]
bugs: ["Insecure deserialization", "Security code review"]
publication_date: "2023-09-12"
added_date: "2023-09-22"
source: "pentester.land/writeups.json"
original_index: 786
---

# Finding a POP chain on a common Symfony bundle: part 1

Written by Rémi Matasse \- 12/09/2023 - in Pentest \- [Download](finding-a-pop-chain-on-a-common-symfony-bundle-part-1#) __

The Symfony `doctrine/doctrine-bundle` package is one of the most common bundles installed along Symfony applications. At the time we are releasing this blogpost, it has been downloaded [144 million times](https://packagist.org/packages/doctrine/doctrine-bundle), making it an interesting target for unserialize exploitation. If you want to improve your knowledge about PHP unserialize exploitation and see why weak typed languages are considered less secure, this blogpost is for you.

The first part of this article aims to show a full methodology of POP chain research, it details the full code analysis methodology used to identify a valid vulnerable path. The [second part](https://www.synacktiv.com/en/publications/finding-a-pop-chain-on-a-common-symfony-bundle-part-2) of it will be focused on the full build of a valid POP chain via a basic trial and error logic based on the code analyzed on this section.

Looking to improve your skills? Discover our **trainings** sessions! [Learn more](../offers/trainings). 

##  Targeting Symfony indirectly

As stated in [our blogpost](https://www.synacktiv.com/publications/php-filters-chain-what-is-it-and-how-to-use-it), finding POP chain in the main Symfony framework seems quite difficult due to its minimalism. Many basic features only come with extra dependencies such as [Doctrine](https://symfony.com/doc/current/doctrine.html) which is used as its ORM (Object Relation Mapping). This ORM is also one of the most commonly used along many other PHP projects : Drupal, Laravel, PrestaShop, etc. It is used to manage and abstract database access from the application.

To make Doctrine and Symfony compatible, the `doctrine-bundle` was created since Symfony version 2.1 if we believe the first paragraph of the [first README](https://github.com/doctrine/DoctrineBundle/blob/0c967b847e5320093bedcacbdd701bca5ea34534/README.md) released on the project.

> Because Symfony 2 does not want to force or suggest a specific persistence solutions on the users this bundle was removed from the core of the Symfony 2 framework. Doctrine2 will still be a major player in the Symfony world and the bundle is maintained by developers in the Doctrine and Symfony communities.
> 
> IMPORTANT: This bundle is developed for Symfony 2.1 and up. For Symfony 2.0 applications the DoctrineBundle  
>  is still shipped with the core Symfony repository.

## Methodology: identifying interesting entrypoints

Finding POP chains can be time-consuming, because the scope on which they are based is huge when digging in PHP dependencies. This is why it is important to keep in mind where to start, and see how to jump from one object to another, step by step.

The full methodology and logic followed to find them and make them work together is described in the following sections.

### PHP unserialization, finding what you want via static analysis

First, it is mandatory to find a `__wakeup`, `__unserialize` or a `__destruct` method [implemented](https://www.php.net/manual/en/language.oop5.overloading.php) in the project dependencies. The `__toString` method can also be called, but the object unserialized has to be called inside a function such as `print` or `echo` after its unserialization, which is unlikely to happen.

Without going too deep in the details (more details on use cases and tricks can be found on [payload all the things](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Insecure%20Deserialization/PHP.md)), when a serialized string is put through unserialization, the `__wakeup` method [will be called first](https://www.php.net/manual/fr/language.oop5.magic.php#object.wakeup) (or `__unserialize` instead). The object will then eventually get destroyed, therefore calling its `__destruct` method if it is defined.

### Sorting __wakeup, __unserialize and __destruct

To make the assumptions, and the flow of this blogpost easier to follow, each step of the logic followed in order to identify the full chain will be presented with a figure. So the first target during this research is to sort `__wakeup`, `__unserialize` or `__destruct `functions from the code base analyzed.

![looking_for_a_pop_chain](/sites/default/files/inline-images/unserialize_first_target.webp) First assumption while looking for a POP chain.

#### Grepping your classes

`doctrine-bundle` dependencies can be installed from `composer`. After that, a simple grep can do the trick : the `doctrine/doctrine-bundle` dependencies contain many possible entrypoints.
  
  
  $ composer require doctrine/doctrine-bundle
  ./composer.json has been created
  Running composer update doctrine/doctrine-bundle
  Loading composer repositories with package information
  Updating dependencies
  Lock file operations: 35 installs, 0 updates, 0 removals
  - Locking doctrine/cache (2.2.0)
  - Locking doctrine/dbal (3.5.3)
  - Locking doctrine/deprecations (v1.0.0)
  - Locking doctrine/doctrine-bundle (2.8.2
  [...]
  $ cd vendor
  $ grep -Ri 'function __destruct'
  doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheAdapter.php:  public function __destruct()
  doctrine/dbal/src/Logging/Connection.php:  public function __destruct()
  symfony/framework-bundle/Tests/Kernel/flex-style/src/FlexStyleMicroKernel.php:  public function __destruct()
  symfony/dependency-injection/Loader/Configurator/ServiceConfigurator.php:  public function __destruct()
  symfony/dependency-injection/Loader/Configurator/AbstractServiceConfigurator.php:  public function __destruct()
  symfony/dependency-injection/Loader/Configurator/ServicesConfigurator.php:  public function __destruct()
  symfony/dependency-injection/Loader/Configurator/PrototypeConfigurator.php:  public function __destruct()
  symfony/cache/Adapter/TagAwareAdapter.php:  public function __destruct()
  symfony/cache/Traits/AbstractAdapterTrait.php:  public function __destruct()
  symfony/cache/Traits/FilesystemCommonTrait.php:  public function __destruct()
  symfony/error-handler/BufferingLogger.php:  public function __destruct()
  symfony/routing/Loader/Configurator/ImportConfigurator.php:  public function __destruct()
  symfony/routing/Loader/Configurator/CollectionConfigurator.php:  public function __destruct()
  symfony/http-kernel/DataCollector/DumpDataCollector.php:  public function __destruct()

#### Sorting the possible entrypoints

On deeply hardened projects such as Symfony, a protection against unserialization is often set by throwing an error when the `__wakeup` function is called, since it is called before the `__destruct` function. As shown in the following result, this in depth hardening is set on many Symfony classes.
  
  
  $ grep -hri 'function __wakeup' -A4 . 
  public function __wakeup()
  {
  throw new \BadMethodCallException('Cannot unserialize '.__CLASS__);
  }
  
  --
  public function __wakeup()
  {
  throw new \BadMethodCallException('Cannot unserialize '.__CLASS__);
  }
  
  --
  [...]

Keep in mind that it is possible to sort the classes implementing `__destruct` but not containing the `BadMethodCallException` keyword:
  
  
  $ grep -rl '__destruct' | xargs grep -L BadMethodCallException
  doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheAdapter.php
  doctrine/dbal/src/Logging/Connection.php
  symfony/dependency-injection/Loader/Configurator/ServiceConfigurator.php
  symfony/dependency-injection/Loader/Configurator/AbstractServiceConfigurator.php
  symfony/dependency-injection/Loader/Configurator/ServicesConfigurator.php
  symfony/dependency-injection/Loader/Configurator/PrototypeConfigurator.php
  symfony/var-dumper/Caster/ExceptionCaster.php
  symfony/http-kernel/Tests/DataCollector/DumpDataCollectorTest.php

Luckily for us, the `Doctrine\Common\Cache\Psr6\CacheAdapter` class seems pretty promising! It was used as the default doctrine cache adapter along the `doctrine/cache` package until the [Doctrine version 1.11.x](https://www.doctrine-project.org/projects/doctrine-cache/en/2.2/index) (maintained since 2019). It was then deprecated, however, it was kept for backward compatibility, and even if the code should not be used anymore, `doctrine/cache` was kept for backward compatibility.
  
  
  <?php
  
  namespace Doctrine\Common\Cache\Psr6;
  
  final class CacheAdapter implements CacheItemPoolInterface
  {
  [...]
  public function commit(): bool
  {
  [...]
  }
  
  public function __destruct() { 
  $this->commit(); 
  }
  }

As we can see, the `__destruct` function is reachable and directly calls the `commit` function of the object, let's see what can be done from this point.

#### What about __call function definitions?

Another path explored during this research was to analyze classes defining a `__call` function.

The [PHP documentation explains](https://www.php.net/manual/en/language.oop5.overloading.php) that:

> `__call()` is triggered when invoking inaccessible methods in an object context
  
  
  $ grep -Ri 'function __call' .
  ./doctrine/dbal/src/Schema/Comparator.php:  public function __call(string $method, array $args): SchemaDiff
  ./doctrine/dbal/src/Schema/Comparator.php:  public static function __callStatic(string $method, array $args): SchemaDiff
  ./symfony/event-dispatcher/Debug/TraceableEventDispatcher.php:  public function __call(string $method, array $arguments): mixed
  ./symfony/dependency-injection/Loader/Configurator/EnvConfigurator.php:  public function __call(string $name, array $arguments): static
  ./symfony/dependency-injection/Loader/Configurator/AbstractConfigurator.php:  public function __call(string $method, array $args)
  ./symfony/cache/Traits/RedisClusterNodeProxy.php:  public function __call(string $method, array $args)

While it will not be described in this blogpost since it did not pay out here, keep in mind that it should also be covered if you look for POP chains since it can be reached in most cases.

### Jumping from controlled functions

![cacheadapter_access](/sites/default/files/inline-images/jumping_controlled_function_1.webp) PhpAdapter commit function reached via __destruct call.

The `commit` function we reached is normally used to update the deferred items cached by the Doctrine cache. Basically, it deletes items which reached expiry and saves all the others in the cache definition.

The phpdoc (@var lines) on the class attributes suggests that `$cache` should implement the `Cache` interface, and `$deferredItems` should be an array of either `CacheItem` or `TypedCacheItem`. This is only for documentation purposes and does not enforce strong typing, meaning that any call to their methods can be hijacked because we can control which class will be implemented thanks to unserialization.

From this point, 4 functions can be called from `$this->cache` or `$this->deferredItems` objects. Let's have a look to each object implementing them to see if interesting code can be reached.
  
  
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
  
  $now  = microtime(true);
  $itemsCount  = 0;
  $byLifetime  = [];
  $expiredKeys = [];
  
  foreach ($this->deferredItems as $key => $item) {
  $lifetime = ($item->getExpiry() ?? $now) - $now; // [1]
  
  if ($lifetime < 0) {
  $expiredKeys[] = $key;
  
  continue;
  }
  
  ++$itemsCount;
  $byLifetime[(int) $lifetime][$key] = $item->get(); // [2]
  }
  
  $this->deferredItems = [];
  
  switch (count($expiredKeys)) {
  case 0:
  break;
  case 1:
  $this->cache->delete(current($expiredKeys)); // [4]
  break;
  default:
  $this->doDeleteMultiple($expiredKeys);
  break;
  }
  
  if ($itemsCount === 1) {
  return $this->cache->save($key, $item->get(), (int) $lifetime); // [3]
  }
  
  $success = true;
  foreach ($byLifetime as $lifetime => $values) {
  $success = $this->doSaveMultiple($values, $lifetime) && $success;
  }
  
  return $success;
  }
  
  public function __destruct() { 
  $this->commit(); 
  }
  }

  * **[1]** The `getExpiry()` function from any object

This function is not a good match, it does not reach interesting code and is only defined in 2 classes:
  
  
  $ grep -ri 'function getexpiry' -A 3
  doctrine/cache/lib/Doctrine/Common/Cache/Psr6/TypedCacheItem.php:  public function getExpiry(): ?float
  doctrine/cache/lib/Doctrine/Common/Cache/Psr6/TypedCacheItem.php-  {
  doctrine/cache/lib/Doctrine/Common/Cache/Psr6/TypedCacheItem.php-  return $this->expiry;
  doctrine/cache/lib/Doctrine/Common/Cache/Psr6/TypedCacheItem.php-  }
  --
  doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheItem.php:  public function getExpiry(): ?float
  doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheItem.php-  {
  doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheItem.php-  return $this->expiry;
  doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheItem.php-  }

  * **[2]** The `get()` function from any object

This function definition seems promising. It is defined at least in 53 files in the `doctrine/doctrine-bundle` dependencies.
  
  
  $ grep -ri 'function get(' | wc -l
  53

However, the `$item->getExpiry()` code is reached before, and we saw that only 2 objects implements a `getExpiry` function. Both of them only return a value, which makes `get` calls unreachable as shown on the following code snippet.
  
  
  <?php
  
  final class CacheAdapter implements CacheItemPoolInterface
  {
  [...]
  public function commit(): bool
  {
  [...]
  foreach ($this->deferredItems as $key => $item) {
  $lifetime = ($item->getExpiry() ?? $now) - $now; // [1]
  
  if ($lifetime < 0) {
  $expiredKeys[] = $key;
  
  continue;
  }
  
  ++$itemsCount;
  $byLifetime[(int) $lifetime][$key] = $item->get(); // [2]
  }
  
  }
  
  }

  * ******[3]** The `save($param1, $param2, int $param3)` function from any object

`save` is a common function name and without surprise, many classes or traits are defining it.
  
  
  $ grep -ri 'function save('  .
  ./psr/cache/src/CacheItemPoolInterface.php:  public function save(CacheItemInterface $item): bool;
  ./doctrine/cache/lib/Doctrine/Common/Cache/Psr6/CacheAdapter.php:  public function save(CacheItemInterface $item): bool
  ./doctrine/cache/lib/Doctrine/Common/Cache/Cache.php:  public function save($id, $data, $lifeTime = 0);
  ./doctrine/cache/lib/Doctrine/Common/Cache/CacheProvider.php:  public function save($id, $data, $lifeTime = 0)
  ./symfony/http-foundation/Session/Storage/MockArraySessionStorage.php:  public function save()
  ./symfony/http-foundation/Session/Storage/SessionStorageInterface.php:  public function save();
  ./symfony/http-foundation/Session/Storage/NativeSessionStorage.php:  public function save()
  ./symfony/http-foundation/Session/Storage/MockFileSessionStorage.php:  public function save()
  ./symfony/http-foundation/Session/Session.php:  public function save()
  ./symfony/http-foundation/Session/SessionInterface.php:  public function save();
  ./symfony/cache/Adapter/ProxyAdapter.php:  public function save(CacheItemInterface $item): bool
  ./symfony/cache/Adapter/PhpArrayAdapter.php:  public function save(CacheItemInterface $item): bool
  ./symfony/cache/Adapter/TraceableAdapter.php:  public function save(CacheItemInterface $item): bool
  ./symfony/cache/Adapter/ChainAdapter.php:  public function save(CacheItemInterface $item): bool
  ./symfony/cache/Adapter/ArrayAdapter.php:  public function save(CacheItemInterface $item): bool
  ./symfony/cache/Adapter/NullAdapter.php:  public function save(CacheItemInterface $item): bool
  ./symfony/cache/Adapter/TagAwareAdapter.php:  public function save(CacheItemInterface $item): bool
  ./symfony/cache/Traits/RedisCluster6Proxy.php:  public function save($key_or_address): \RedisCluster|bool
  ./symfony/cache/Traits/AbstractAdapterTrait.php:  public function save(CacheItemInterface $item): bool
  ./symfony/cache/Traits/RedisCluster5Proxy.php:  public function save($key_or_address)
  ./symfony/cache/Traits/Redis6Proxy.php:  public function save(): \Redis|bool
  ./symfony/cache/Traits/Redis5Proxy.php:  public function save()
  ./symfony/http-kernel/HttpCache/Store.php:  private function save(string $key, string $data, bool $overwrite = true): bool

Many of these classes are useless for our purpose, but `Symfony\Component\HttpFoundation\Session\Storage\MockFileSessionStorage` can be used to write a file. This is one of the main targets for this POP chain. To reach its code, it is necessary to define one `$item` which has an `expiration` inferior to the current time. `$key` will be its first parameter.
  
  
  <?php
  
  final class CacheAdapter implements CacheItemPoolInterface
  {
  [...]
  public function commit(): bool
  {
  [...]
  foreach ($this->deferredItems as $key => $item) {
  $lifetime = ($item->getExpiry() ?? $now) - $now; // [1]
  
  if ($lifetime < 0) {
  $expiredKeys[] = $key;
  
  continue;
  }
  
  ++$itemsCount;
  $byLifetime[(int) $lifetime][$key] = $item->get(); // [2]
  }
  [...]
  if ($itemsCount === 1) {
  return $this->cache->save($key, $item->get(), (int) $lifetime); // [3]
  }
  
  }
  
  }

  * **[4]** The `delete($param1)` function from any object

Unlike the `save` function, `delete` definitions are less common in PHP projects. However, it only makes it easier to look for them in all the files.
  
  
  $ grep -ri 'function delete('  .
  ./doctrine/cache/lib/Doctrine/Common/Cache/Cache.php:  public function delete($id);
  ./doctrine/cache/lib/Doctrine/Common/Cache/CacheProvider.php:  public function delete($id)
  ./doctrine/dbal/src/Query/QueryBuilder.php:  public function delete($delete = null, $alias = null)
  ./doctrine/dbal/src/Connection.php:  public function delete($table, array $criteria, array $types = [])
  ./symfony/cache-contracts/CacheTrait.php:  public function delete(string $key): bool
  ./symfony/cache-contracts/CacheInterface.php:  public function delete(string $key): bool;
  ./symfony/cache/Psr16Cache.php:  public function delete($key): bool
  ./symfony/cache/Adapter/TraceableAdapter.php:  public function delete(string $key): bool
  ./symfony/cache/Adapter/ArrayAdapter.php:  public function delete(string $key): bool
  ./symfony/cache/Adapter/NullAdapter.php:  public function delete(string $key): bool
  ./symfony/cache/Traits/Redis6Proxy.php:  public function delete($key, ...$other_keys): \Redis|false|int
  ./symfony/cache/Traits/Redis5Proxy.php:  public function delete($key, ...$other_keys)

From these classes, `Symfony\Component\Cache\Adapter\PhpArrayAdapter` can be used to arbitrary `include` a file. This is the final target of this POP chain.

To reach it, it is necessary to define one `$item` which has an `expiration` higher than the current time. `$item` will be its first parameter.
  
  
  <?php
  
  final class CacheAdapter implements CacheItemPoolInterface
  {
  [...]
  public function commit(): bool
  {
  [...]
  foreach ($this->deferredItems as $key => $item) {
  $lifetime = ($item->getExpiry() ?? $now) - $now; // [1]
  
  if ($lifetime < 0) {
  $expiredKeys[] = $key;
  
  continue;
  }
  
  ++$itemsCount;
  $byLifetime[(int) $lifetime][$key] = $item->get(); // [2]
  }
  
  switch (count($expiredKeys)) {
  case 0:
  break;
  case 1:
  $this->cache->delete(current($expiredKeys)); // [4]
  break;
  default:
  $this->doDeleteMultiple($expiredKeys);
  break;
  }
  [...]
  }
  }

This chain is used to `include` a file from an arbitrary path.

### First step, MockFileSessionStorage to get file write

Now that we know better where we can search, let's dig more!

The first step while looking for vulnerable code in PHP code would be to see if user supplied data is passed to dangerous functions such as `system`, `eval`, `include`, `require`, `exec`, `popen`, `call_user_func`, `file_put_contents`. There are many others, however, the main idea here is that since the potential vulnerable scope was refined to `save()` functions, it is now necessary to audit each reachable save functions from the analyzed dependencies to identify the POP chain.

As we can see, the only reachable and interesting function seems to be `file_put_contents` in the `save` function of the `Symfony\Component\HttpFoundation\Session\Storage\MockFileSessionStorage` class.
  
  
  $ grep -hri 'function save(' -A50 . | grep system
  $ grep -hri 'function save(' -A50 . | grep eval
  $ grep -hri 'function save(' -A50 . | grep include
  $ grep -hri 'function save(' -A50 . | grep require
  * When versioning is enabled, clearing the cache is atomic and does not require listing existing keys to proceed,
  * but old keys may need garbage collection and extra round-trips to the back-end are required.
  $ grep -hri 'function save(' -A50 . | grep exec
  $ grep -hri 'function save(' -A50 . | grep popen
  $ grep -hri 'function save(' -A50 . | grep call_user_func
  [...]
  $ grep -hri 'function save(' -A50 . | grep file_put_content
  file_put_contents($tmp, serialize($data));
  $ grep -ri 'file_put_contents($tmp, serialize($data))' .
  ./symfony/http-foundation/Session/Storage/MockFileSessionStorage.php:  file_put_contents($tmp, serialize($data));
  $ grep -i 'file_put_contents($tmp, serialize($data))' -B 21 -A 12 ./symfony/http-foundation/Session/Storage/MockFileSessionStorage.php
  public function save()
  {
  if (!$this->started) {
  throw new \RuntimeException('Trying to save a session that was not started yet or was already closed.');
  }
  
  $data = $this->data;
  
  foreach ($this->bags as $bag) {
  if (empty($data[$key = $bag->getStorageKey()])) {
  unset($data[$key]);
  }
  }
  if ([$key = $this->metadataBag->getStorageKey()] === array_keys($data)) {
  unset($data[$key]);
  }
  
  try {
  if ($data) {
  $path = $this->getFilePath();
  $tmp = $path.bin2hex(random_bytes(6));
  file_put_contents($tmp, serialize($data));
  rename($tmp, $path);
  } else {
  $this->destroy();
  }
  } finally {
  $this->data = $data;
  }
  
  // this is needed when the session object is re-used across multiple requests
  // in functional tests.
  $this->started = false;
  }

While looking promising at first, the extension of the generated file cannot be defined, which makes it less interesting.
  
  
  <?php
  
  namespace Symfony\Component\HttpFoundation\Session\Storage;
  
  class MockFileSessionStorage extends MockArraySessionStorage
  {
  private string $savePath;
  
  public function save()
  {
  [...]
  
  try {
  if ($data) {
  $path = $this->getFilePath();
  $tmp = $path.bin2hex(random_bytes(6));
  file_put_contents($tmp, serialize($data));
  rename($tmp, $path);
  } else {
  $this->destroy();
  }
  } finally {
  $this->data = $data;
  }
  $this->started = false;
  }
  private function getFilePath(): string
  {
  return $this->savePath.'/'.$this->id.'.mocksess';
  }
  
  }

However, as we can see, we can control a serialized data injected in a file, which can be executed as PHP code if executed.
  
  
  $ php -r "echo serialize('<?php phpinfo(); ?>');" > /tmp/test_serialize
  $ php /tmp/test_serialize 
  s:19:"phpinfo()
  PHP Version => 8.1.22
  [...]
  questions about PHP licensing, please contact license@php.net.

The `$path = $this->getFilePath()` code is used to define the path of the file written in the `file_put_contents` [method](https://www.php.net/manual/en/function.file-put-contents.php).
  
  
  <?php
  
  namespace Symfony\Component\HttpFoundation\Session\Storage;
  
  class MockFileSessionStorage extends MockArraySessionStorage
  {
  [...]
  private function getFilePath(): string
  {
  return $this->savePath.'/'.$this->id.'.mocksess';
  }
  
  }

The `.mocksess` is suffixed to the file, preventing us from getting code execution by creating a `.php` file in the folder exposing sources to the user. However, getting an arbitrary file write is the only prerequisite needed before proceeding to the second step. The following schema wraps up this first element of the POP chain.

![file_write_path](/sites/default/files/inline-images/file_write_primitive_1.webp) POP chain path to write any file with any content ending with the extension .mocksess

### Second step, finding the path to file inclusion

The same methodology can be applied to look for `delete` function calls.
  
  
  $ grep -hri 'function delete(' -A50 . | grep file_put_content | grep system
  $ grep -hri 'function delete(' -A50 . | grep eval
  [...]
  $ grep -hri 'function delete(' -A50 . | grep include
  $ grep -hri 'function delete(' -A50 . | grep require
  $ grep -hri 'function delete(' -A50 . | grep exec
  [...]
  $ grep -hri 'function delete(' -A50 . | grep popen
  $ grep -hri 'function delete(' -A50 . | grep call_user_func
  [...]

After searching for many common dangerous functions, it was clear that there was no quick win in those. This then means we need to dive into all of them individually. Let's start by looking for the good old weak typing trick used at the start of this POP chain, allowing us to call `delete` functions from other objects.
  
  
  $ grep -hri 'function delete(' -A3 .
  public function delete($id);
  --
  public function delete(string $key): bool
  {
  return $this->deleteItem($key);
  }
  --  
  public function delete(string $key): bool
  {
  return $this->deleteItem($key);
  }
  --
  public function delete($id)
  {
  return $this->doDelete($this->getNamespacedId($id));
  }
  --
  public function delete($table, array $criteria, array $types = [])
  {
  if (count($criteria) === 0) {
  throw InvalidArgumentException::fromEmptyCriteria();
  --
  public function delete($key): bool
  {
  try {
  return $this->pool->deleteItem($key);
  [...]
  
  $ grep -Ri 'return $this->pool->deleteItem($key);' .
  ./symfony/cache/Psr16Cache.php:  return $this->pool->deleteItem($key);
  
  

As we can see, the `deleteItem` function seems promising since it is called from many `delete` functions, let's see what can be reached from it.

From a call to the `PhpArrayAdapter` function `deleteItem`, it is possible to reach its `initialize` method which includes an arbitrary file. Since we already have a file write, we would be able to include it in order to get code execution.
  
  
  $ grep -hri 'function deleteItem(' -A6 .
  public function deleteItem(mixed $key): bool
  {
  if (!\is_string($key)) {
  throw new InvalidArgumentException(sprintf('Cache key must be string, "%s" given.', get_debug_type($key)));
  }
  if (!isset($this->values)) {
  $this->initialize();
  [...]
  
  $ grep -Ri '  $this->initialize();' . 
  ./symfony/cache/Adapter/PhpArrayAdapter.php:  $this->initialize();
  [...]
  $ grep 'function initialize' -A10 ./symfony/cache/Adapter/PhpArrayAdapter.php
  private function initialize()
  {
  if (isset(self::$valuesCache[$this->file])) {
  $values = self::$valuesCache[$this->file];
  } elseif (!is_file($this->file)) {
  $this->keys = $this->values = [];
  
  return;
  } else {
  $values = self::$valuesCache[$this->file] = (include $this->file) ?: [[], []];
  }

Unfortunately for us, it is not possible to use a PHP filter chain to get command execution from this path alone. This is due to the `elseif (!is_file($this->file)` condition, which verifies that the file is present on the file system, preventing any call to the `php://` wrapper.

To sum up, the goal is now to find a way to reach `PhpArrayAdapter` in order to reach its `deleteItem` function to put together the puzzle pieces.

![PhpArrayAdapter_identifed_as_target](/sites/default/files/inline-images/include_target.webp) File inclusion via the initialize function from PhpArrayAdapter.

#### Getting rekt by PHP strong typing

Now that our plan is well-defined, let's see how to reach `PhpArrayAdapter` from our previously discovered `delete` function.
  
  
  $ grep -Ri 'return $this->pool->deleteItem($key);' .
  ./symfony/cache/Psr16Cache.php:  return $this->pool->deleteItem($key);

At first sight, the `Psr16Cache` class seems perfect to reach our target as we might be able to reach any other `deleteItem` function by defining its `pool` attribute as a `PhpArrayAdapter` object. However, as we said, while PHP is a weakly typed language, it is also possible to harden it by enforcing strong typing. Unfortunately for us, this is the case in the `Psr16Cache` class.
  
  
  cat ./symfony/cache/Psr16Cache.php
  <?php
  
  [...]
  class Psr16Cache implements CacheInterface, PruneableInterface, ResettableInterface
  {
  use ProxyTrait;
  
  private ?\Closure $createCacheItem = null;
  private ?CacheItem $cacheItemPrototype = null;
  private static \Closure $packCacheItem;
  
  public function __construct(CacheItemPoolInterface $pool)
  {
  $this->pool = $pool;
  }

The check that the parameter `$pool` is a `CacheItemPoolInterface` interface prevents us to use a `PhpArrayAdapter` class instead.

#### PHP traits analysis

Now that the most straight forward path has been invalidated, let's see what options are left to us.
  
  
  $ grep -Ri 'function delete(' .
  ./doctrine/cache/lib/Doctrine/Common/Cache/Cache.php:  public function delete($id);
  ./doctrine/cache/lib/Doctrine/Common/Cache/CacheProvider.php:  public function delete($id)
  ./doctrine/dbal/src/Query/QueryBuilder.php:  public function delete($delete = null, $alias = null)
  ./doctrine/dbal/src/Connection.php:  public function delete($table, array $criteria, array $types = [])
  ./symfony/cache-contracts/CacheTrait.php:  public function delete(string $key): bool
  [...]

In the objects defining the `delete` function, the `CacheTrait` trait seems promising. The PHP documentation defines a trait as [a way to reuse code](https://www.php.net/manual/en/language.oop5.traits.php), which is basically a way to write a function or an attribute and to define them inside another class. All there is to do is to add it in the class via the `use` keyword.
  
  
  $ cat ./symfony/cache-contracts/CacheTrait.php | grep 'function delete(' -A 3
  public function delete(string $key): bool
  {
  return $this->deleteItem($key);
  }

A `CacheTrait` calls the `deleteItem` function of the object using it. If by chance our target, the `PhpArrayAdapter` class, uses the `CacheTrait`, we would then be able to call its `deleteItem` function and therefore reach the `require` function needed to get code execution.
  
  
  $ grep -Ri 'use CacheTrait' .
  ./symfony/cache/Traits/ContractsTrait.php:  use CacheTrait {
  $ grep -Ri 'use ContractsTrait' .
  ./symfony/cache/Adapter/ProxyAdapter.php:  use ContractsTrait;
  ./symfony/cache/Adapter/PhpArrayAdapter.php:  use ContractsTrait;
  [...]

Even if the `PhpArrayAdapter` class does not directly use the `CacheTrait`, it uses the `ContractsTrait` which uses it because traits can be nested.

#### Finally, reaching PhpArrayAdapter for the win

After a deeper investigation we finally discovered that the `PhpArrayAdapter` had already everything needed to reach its vulnerable `initialize` function. The `CacheTrait` `deleteItem` function is defined, allowing to call the `initialize` function to finally reach the `include` function to execute the PHP code we put in a file at the beginning.
  
  
  $ cat ./symfony/cache-contracts/CacheTrait.php | grep 'function delete(' -A 3
  public function delete(string $key): bool
  {
  return $this->deleteItem($key);
  }
  $ cat ./symfony/cache/Adapter/PhpArrayAdapter.php | grep 'function deleteItem(' -A6
  public function deleteItem(mixed $key): bool
  {
  if (!\is_string($key)) {
  throw new InvalidArgumentException(sprintf('Cache key must be string, "%s" given.', get_debug_type($key)));
  }
  if (!isset($this->values)) {
  $this->initialize();
  $ cat ./symfony/cache/Adapter/PhpArrayAdapter.php | grep 'function initialize(' -A9
  private function initialize()
  {
  if (isset(self::$valuesCache[$this->file])) {
  $values = self::$valuesCache[$this->file];
  } elseif (!is_file($this->file)) {
  $this->keys = $this->values = [];
  
  return;
  } else {
  $values = self::$valuesCache[$this->file] = (include $this->file) ?: [[], []];

![phparrayadapter_full_chain](/sites/default/files/inline-images/phparrayadapter_full_chain.webp) File inclusion code reached from PhpArrayAdapter

### Recap all the vulnerable code

This POP chain started from the `__destruct` function of the `CacheAdapter` object which calls its `commit` function. After digging its code, we identified that the `MockFileSessionStorage` can be reached via a weak typing trick on the `save` function, this allowed us to get file write. Finally, `PhpArrayAdapter` could be reached from a weak typing trick on the `delete` function, leading to an arbitrary file inclusion after a few more steps.

The following diagram recaps every piece of code covered by the POP chain.

![all_popchain_impacted](/sites/default/files/inline-images/complete_scheme.webp) Full recap of the code reached by the POP chain in the doctrine/doctrine-bundle package.

## Conclusion

Looking for POP chain in huge dependencies is time-consuming, but playing with so much sources is a good way to understand PHP's mechanism deeply.

In the first part of this research, we saw that weak typing can be used as a tool to reach unexpected functions.

As we could see, it is not always required to use fancy tools to find interesting code path. Understanding an exploitation path and knowing what we are looking for is most of the time sufficient to get the work done! That being said, the methodology used in this article is really time-consuming and could be greatly optimized combined with the usage of a debugger such as `Xdebug` for example.

In the next part, we will build the full POP chain based on the sources we already dissected and show a full exploit of a vulnerable Symfony application containing the `doctrine/doctrine-bundle` package. Since this chain is in fact based on 2 different PHP objects and on a code base evolving through PHP versions, some interesting tricks are involved so stay tuned!

Share this article
