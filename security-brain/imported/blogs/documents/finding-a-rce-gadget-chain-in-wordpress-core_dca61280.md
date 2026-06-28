---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-10-13_finding-a-rce-gadget-chain-in-wordpress-core.md
original_filename: 2023-10-13_finding-a-rce-gadget-chain-in-wordpress-core.md
title: Finding A RCE Gadget Chain In WordPress Core
category: documents
detected_topics:
- ssrf
- sqli
- command-injection
- automation-abuse
- api-security
- mobile-security
tags:
- imported
- documents
- ssrf
- sqli
- command-injection
- automation-abuse
- api-security
- mobile-security
language: en
raw_sha256: dca61280774b08b4604b3e876b89de8bcfe80c6e8abd760f95046860e72dc145
text_sha256: 83fd04469b0efc35dc448ccf69243c760dbf71fda7667fc71b19dcc3bf5474f7
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# Finding A RCE Gadget Chain In WordPress Core

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-10-13_finding-a-rce-gadget-chain-in-wordpress-core.md
- Source Type: markdown
- Detected Topics: ssrf, sqli, command-injection, automation-abuse, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `dca61280774b08b4604b3e876b89de8bcfe80c6e8abd760f95046860e72dc145`
- Text SHA256: `83fd04469b0efc35dc448ccf69243c760dbf71fda7667fc71b19dcc3bf5474f7`


## Content

---
title: "Finding A RCE Gadget Chain In WordPress Core"
page_title: "Finding A RCE Gadget Chain In WordPress Core | WPScan"
url: "https://wpscan.com/blog/finding-a-rce-gadget-chain-in-wordpress-core/"
final_url: "https://wpscan.com/blog/finding-a-rce-gadget-chain-in-wordpress-core/"
authors: ["Marc Montpas"]
programs: ["WordPress"]
bugs: ["RCE", "PHP pop chain", "Insecure deserialization"]
publication_date: "2023-10-13"
added_date: "2024-01-08"
source: "pentester.land/writeups.json"
original_index: 716
---

October 13, 2023

# Finding A RCE Gadget Chain In WordPress Core

During a recent team gathering in Belgium, we had an impromptu [Capture The Flag](https://en.wikipedia.org/wiki/Capture_the_flag_\(cybersecurity\)) game that included a challenge with an SQL Injection vulnerability occurring inside an `INSERT` statement, meaning attackers could inject random stuff into the targeted table’s columns, and query information from the database, the intended “flag” being the credentials of a user on the affected blog.

The vulnerable SQL query inserted new rows into the` wp_termmeta` table, which while we knew it could potentially lead to [Object Injection attacks](https://owasp.org/www-community/vulnerabilities/PHP_Object_Injection) due to the inserted [metadata being passed through maybe_unserialize upon retrieval](https://core.trac.wordpress.org/browser/tags/6.2/src/wp-includes/meta.php#L657), we didn’t think too much about it since the common thought on the matter was that there was no known current RCE gadget chain in WordPress Core, and thus the challenge was “safe” since it didn’t use any other external plugins.

This proved to be enough to win that flag, however, the thought that there might be an alternative solution to the challenge piqued our curiosity. What if _there was_ a working RCE gadget chain in Core waiting to be found?

Turns out, there _was_ a way, which the [WordPress Security Team fixed on version 6.3.2](https://wordpress.org/news/2023/10/wordpress-6-3-2-maintenance-and-security-release/) by preventing several classes used in the final chain from either being unserialized at all, or restricting what some of their unserialized properties may contain.

## Building An RCE Gadget Chain For WordPress Core

There are many ways to initiate this POP chain, but we elected to use one that is very flexible: triggering [the __toString magic method](https://www.php.net/manual/en/language.oop5.magic.php#object.tostring) when whatever is being unserialized (or one of its internal components) is used like a string. To do so, we flagged [WordPress’ WP_Theme class](https://core.trac.wordpress.org/browser/tags/6.2/src/wp-includes/class-wp-theme.php#L503) as a potentially good starting point for our chain:
  
  
   /**
    * When converting the object to a string, the theme name is returned.
    *
    * @since 3.4.0
    *
    * @return string Theme name, ready for display (translated)
    */
  public function __toString() {
    return (string) $this->display( 'Name' );
  }
  

When used as a string, it calls `$this‑>display( 'Name' );`, which itself calls `$this‑>get( 'Name' );`:
  
  
  public function get( $header ) {
    if ( ! isset( $this->headers[ $header ] ) ) {
     return false;
    }
  
    if ( ! isset( $this->headers_sanitized ) ) {
     $this->headers_sanitized = $this->cache_get( 'headers' );
     if ( ! is_array( $this->headers_sanitized ) ) {
      $this->headers_sanitized = array();
     }
    }
  
    if ( isset( $this->headers_sanitized[ $header ] ) ) {
     return $this->headers_sanitized[ $header ];
    }
  
    // If themes are a persistent group, sanitize everything and cache it. One cache add is better than many cache sets.
    if ( self::$persistently_cache ) {
     foreach ( array_keys( $this->headers ) as $_header ) {
      $this->headers_sanitized[ $_header ] = $this->sanitize_header( $_header, $this->headers[ $_header ] );
     }
     $this->cache_add( 'headers', $this->headers_sanitized );
    } else {
     $this->headers_sanitized[ $header ] = $this->sanitize_header( $header, $this->headers[ $header ] );
    }
  
    return $this->headers_sanitized[ $header ];
  }
  

`WP_Theme::get( $header )` accesses a lot of internal properties assuming they are arrays, a reasonable assumption to make in normal times. However, since we fully control the instance (we serialized it ourselves!), we can make those properties contain anything, including other classes that implement [the ArrayAccess interface](https://www.php.net/manual/en/class.arrayaccess.php).

These types of classes behave roughly like arrays, implementing their “array‑like” functionality by putting their logic in the `offsetGet`, `offsetSet`, `offsetExists`, and `offsetUnset` methods.

## Pivoting, And Pivoting Again

This is where this POP chain code logic becomes kind of convoluted.

Scavenging for classes that use the ArrayAccess interface in interesting ways led us to [the WP_Block_List class](https://core.trac.wordpress.org/browser/tags/6.2/src/wp-includes/class-wp-block-list.php#L81):
  
  
  public function offsetGet( $index ) {
    $block = $this->blocks[ $index ];
  
    if ( isset( $block ) && is_array( $block ) ) {
     $block                  = new WP_Block( $block, $this->available_context, $this->registry );
     $this->blocks[ $index ] = $block;
    }
  
    return $block;
  }
  

The `$index` parameter contains `'Name'`, and we can set `$this‑>blocks` to whatever we want, which means we have full control over what `$block` contains. This is handy because the code instantiates a `WP_Block` class using three parameters we have full control over.
  
  
  public function __construct( $block, $available_context = array(), $registry = null ) {
    $this->parsed_block = $block;
    $this->name         = $block['blockName'];
  
    if ( is_null( $registry ) ) {
     $registry = WP_Block_Type_Registry::get_instance();
    }
  
    $this->registry = $registry;
  
    $this->block_type = $registry->get_registered( $this->name );
  

The `WP_Block` class’ constructor uses the `$registry` parameter, which it expects to be an instance of a class that extends `WP_Block_Type_Registry`, to get registered block types via [its get_registered() method](https://core.trac.wordpress.org/browser/tags/6.2/src/wp-includes/class-wp-block-type-registry.php#L132). Note that we control both `$registry` _and_ `$this‑>name` here.
  
  
  public function get_registered( $name ) {
    if ( ! $this->is_registered( $name ) ) {
     return null;
    }
  
    return $this->registered_block_types[ $name ];
  }
  

As you can see again, we have _another_ interesting POP chain primitive right there. The `$this‑>registered_block_types[ $name ]` snippet allows us to do the `offsetGet` trick again, with the important difference that this time around, we actually decide which array index we’re retrieving!

Knowing that, let’s pivot back to [the WP_Theme class](https://core.trac.wordpress.org/browser/tags/6.2/src/wp-includes/class-wp-theme.php#L643), which _also_ implements the `ArrayAccess` interface.
  
  
  public function offsetGet( $offset ) {
    switch ( $offset ) {
     // (... Bunch of less interesting offset to choose from ...)
     case 'Parent Theme':
      return $this->parent() ? $this->parent()->get( 'Name' ) : '';
  

The point of interest here is what happens when we try to grab the `Parent Theme` offset. The method calls [$this‑>parent()](https://core.trac.wordpress.org/browser/tags/6.2/src/wp-includes/class-wp-theme.php#L731), which essentially just returns `$this‑>parent` if it is set, and calls that object’s `get()` method.

Now, `get()` is a very common method name, so surely we might be able to have `$this‑>parent` contain an instance of a class other than `WP_Theme`, which also happens to contain a method with the same name?

## Will It Get() Better?

The [WpOrg\Requests\Session class](https://core.trac.wordpress.org/browser/tags/6.2/src/wp-includes/Requests/src/Session.php#L148) (formerly known as [Requests_Session](https://developer.wordpress.org/reference/classes/requests_session/) before WordPress introduced more namespaces in Core) has what we’re looking for:
  
  
  public function get($url, $headers = [], $options = []) {
    return $this->request($url, $headers, null, Requests::GET, $options);
  }
  

Note that we only know the first parameter (`$url`), and can’t change it because it’s hardcoded. The method is almost just an alias for the [WpOrg\Requests\Session::request() method](https://core.trac.wordpress.org/browser/tags/6.2/src/wp-includes/Requests/src/Session.php#L210), it only hardcodes the HTTP method to be used (not that it matters to us):
  
  
  public function request($url, $headers = [], $data = [], $type = Requests::GET, $options = []) {
    $request = $this->merge_request(compact('url', 'headers', 'data', 'options'));
  
    return Requests::request($request['url'], $request['headers'], $request['data'], $type, $request['options']);
  }
  

The `request` method is relatively straightforward, it does some processing with the parameters it received before handing off the actual request process to `Requests::request()`.

Let’s have a look at what [the $this‑>merge_request() method](https://core.trac.wordpress.org/browser/tags/6.2/src/wp-includes/Requests/src/Session.php#L268) does:
  
  
  protected function merge_request($request, $merge_options = true) {
    if ($this->url !== null) {
     $request['url'] = Iri::absolutize($this->url, $request['url']);
     $request['url'] = $request['url']->uri;
    }
  
    if (empty($request['headers'])) {
     $request['headers'] = [];
    }
  
    $request['headers'] = array_merge($this->headers, $request['headers']);
  
    if (empty($request['data'])) {
     if (is_array($this->data)) {
      $request['data'] = $this->data;
     }
    } elseif (is_array($request['data']) && is_array($this->data)) {
     $request['data'] = array_merge($this->data, $request['data']);
    }
  
    if ($merge_options === true) {
     $request['options'] = array_merge($this->options, $request['options']);
  
     // Disallow forcing the type, as that's a per request setting
     unset($request['options']['type']);
    }
  
    return $request;
  }
  }
  

TL;DR: This method merges the parameters it received with some of its internal properties (`$this‑>url`, `$this‑>headers`, `$this‑>options`, etc.)… which we happen to control too since we created that instance from scratch! 🙂

As such, we have _very_ high control of whatever requests we’re about to launch, which could be useful in SSRF attack scenarios. With the exception of the request’s type (aka. method) and path, we can basically control everything. However, we promised we’d get code execution, and we will.

We’ll leave SSRF as an exercise for the reader, but getting to this point is a pretty good way to better grasp what comes next.

## Popping Shells With Captain Hook
  
  
  public static function request($url, $headers = [], $data = [], $type = self::GET, $options = []) {
  
          // (...) Uninteresting code (...)
  
    $options['hooks']->dispatch('requests.before_request', [&$url, &$headers, &$data, &$type, &$options]);
  

The [WpOrg\Requests\Requests::request() method](https://core.trac.wordpress.org/browser/tags/6.2/src/wp-includes/Requests/src/Requests.php#L429) has _at least_ one thing that catches the eye of anyone who’s remotely familiar with WordPress’ fondness for dynamic function callbacks (like it uses for making actions and filters work). One of them is a line where it grabs `$options['hooks']`, which is presumably meant to contain a [WpOrg\Requests\Hooks](https://core.trac.wordpress.org/browser/tags/6.2/src/wp-includes/Requests/src/Hooks.php) instance.

If you recall (or might actually just guess at this point, we control everything!), we actually have a say in what instance should go in `$options['hooks']`! Except now, we’ll give it exactly what it expects, perhaps with a couple personalized hooks and tricks to have it call functions and methods of our choice.

The Hooks::dispatch method is defined as the following:
  
  
  public function dispatch($hook, $parameters = []) {
    if (is_string($hook) === false) {
     throw InvalidArgument::create(1, '$hook', 'string', gettype($hook));
    }
  
    // Check strictly against array, as Array* objects don't work in combination with `call_user_func_array()`.
    if (is_array($parameters) === false) {
     throw InvalidArgument::create(2, '$parameters', 'array', gettype($parameters));
    }
  
    if (empty($this->hooks[$hook])) {
     return false;
    }
  
    if (!empty($parameters)) {
     // Strip potential keys from the array to prevent them being interpreted as parameter names in PHP 8.0.
     $parameters = array_values($parameters);
    }
  
    ksort($this->hooks[$hook]);
  
    foreach ($this->hooks[$hook] as $priority => $hooked) {
     foreach ($hooked as $callback) {
      $callback(...$parameters);
     }
    }
  
    return true;
  }
  

As expected, this is very reminiscent of how add_action() and add_filter() work. We can define `$this‑>hooks` to whatever we want, and have the method call it. Still, we’re facing two relatively important issues:

  * The first parameter we control _has_ to be a URL due to the `Session::merge_request()` from earlier
  * We’re sending a total of 5 parameters, which can be a problem if our goal is to call PHP functions, like `system()`, because they’re stricter about parameter types, and count.

Since user‑defined functions and methods do _not_ share that latter constraint, what we can do to make it easier on us is to recurse once by having the method call itself with the parameters we provided, which will effectively shift all the variables we control to the left.

In other words, the first Hooks::dispatch() call we did used the following parameters:
  
  
  $options['hooks']->dispatch('requests.before_request', [&$url, &$headers, &$data, &$type, &$options])
  

and recursing into the method once is functionally equivalent to letting us do:
  
  
  $options['hooks']->dispatch($url, $headers, &$data, &$type, &$options])
  

As mentioned before: user‑defined methods ignore additional, undefined parameters. Since the `Hooks::dispatch()` method only uses two, the `$data`, `$type`, and `$options` variable will simply not be used at all, while the `$url` variable will be used as the hook’s name instead of a parameter.

### How Do You Build The Payload?

Putting all the necessary pieces in the right order for everything to work is relatively tricky since we have to make sure a number of things align properly. However, the resulting code allows to run any PHP commands, including [system()](https://www.php.net/manual/en/function.system.php), allowing an attacker to execute arbitrary commands on the server. For obvious reasons, we will not be sharing the actual proof of concept publicly.

### Share this:

  * [ Share on X (Opens in new window) X ](https://wpscan.com/blog/finding-a-rce-gadget-chain-in-wordpress-core/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://wpscan.com/blog/finding-a-rce-gadget-chain-in-wordpress-core/?share=facebook)
  * 

Like Loading…

## Posted by

![Unknown's avatar](https://0.gravatar.com/avatar/6fc96ab17c597fba35b3e50fdac0963304b08d097a3cb8c7a12b5aab370ca908?s=48&d=identicon&r=G)

[Marc Montpas](https://wpscan.com/blog/author/marcs0h/)

### Leave a comment [Cancel reply](/blog/finding-a-rce-gadget-chain-in-wordpress-core/#respond)

Δ

## Get News and Tips From WPScan

Type your email… 

Subscribe
