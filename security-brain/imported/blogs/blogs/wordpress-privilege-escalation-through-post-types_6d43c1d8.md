---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-17_wordpress-privilege-escalation-through-post-types.md
original_filename: 2018-12-17_wordpress-privilege-escalation-through-post-types.md
title: WordPress Privilege Escalation through Post Types
category: blogs
detected_topics:
- access-control
- xss
- command-injection
- api-security
- file-upload
- csrf
tags:
- imported
- blogs
- access-control
- xss
- command-injection
- api-security
- file-upload
- csrf
language: en
raw_sha256: 6d43c1d8bb0484c0f8a7144b745de4fa1979dc1d874a941099e184fca9cf3066
text_sha256: 56160a28882094bdcc1fa2a91366f109d549c2724b592393724722f4a1c9dde6
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# WordPress Privilege Escalation through Post Types

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-17_wordpress-privilege-escalation-through-post-types.md
- Source Type: markdown
- Detected Topics: access-control, xss, command-injection, api-security, file-upload, csrf
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `6d43c1d8bb0484c0f8a7144b745de4fa1979dc1d874a941099e184fca9cf3066`
- Text SHA256: `56160a28882094bdcc1fa2a91366f109d549c2724b592393724722f4a1c9dde6`


## Content

---
title: "WordPress Privilege Escalation through Post Types"
page_title: "WordPress Privilege Escalation through Post Types | Sonar"
url: "https://www.sonarsource.com/blog/wordpress-post-type-privilege-escalation/"
final_url: "https://www.sonarsource.com/blog/wordpress-post-type-privilege-escalation/"
authors: ["Simon Scannell (@scannell_simon)"]
programs: ["WordPress"]
bugs: ["Privilege escalation", "Stored XSS", "Object injection"]
publication_date: "2018-12-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5516
---

## TL;DR overview

  * Sonar researchers found a WordPress privilege escalation vulnerability where users could bypass access controls on custom post types to perform unauthorized actions.
  * The flaw exploits inconsistencies in how WordPress checks capabilities for custom post types, allowing a lower-privileged user to edit, delete, or publish content they should not have access to.
  * Custom post types are widely used by WordPress plugins, meaning the vulnerability has a broad impact surface across sites using affected plugin configurations.
  * WordPress patched the authorization check; plugin developers should verify that custom post type registrations explicitly define capability requirements rather than relying on defaults.

A logic flaw in the way WordPress created blog posts allowed attackers to access features only administrators were supposed to have (CVE-2018-20152). This lead to a Stored XSS and Object Injection in the WordPress core and more severe vulnerabilities in WordPress’s most popular plugins Contact Form 7 and Jetpack.  

## Impact

WordPress is at the core a Blogging Software that allows user to create and publish posts. Over time, different post types were introduced, such as pages and media entries (images, videos etc.). Plugins can register new post types, such as products or contact forms. Depending on the purpose of the post type a plugin registers, it offers unique and new features. For example, a contact form plugin might allow to create a contact form with a file upload field (e.g. for resumès). The user creating the contact form can define which filetypes should be allowed. An evil user could also allow php files to be uploaded and then execute arbitrary code on his site. This is not an issue per se, as plugins can restrict access to the post types they register to administrators only and trust WordPress to handle that restriction for them. The privilege escalation discussed here allows lower privileged users to bypass the security checks implemented by WordPress and create posts of any type and misuse the features of custom post types. This leads to a Stored XSS and Object Injection in the WordPress core. Depending on the plugins installed, more severe vulnerabilities can be exploited. When for example WordPress’s most popular plugin, Contact Form 7, which has over 5 million active installs, was used, attackers were able to read the database credentials of the target Wordpress site. Most of the top WordPress plugins are vulnerable to this privilege escalation.  

## Technical Background

To register new post types, plugins make a call to `register_post_type()` with the name of the new post type and some meta information.

Copy to clipboard
  
  
  1  // Example post type
  2  register_post_type( 'example_post_type', array(
  3  'label' => 'Example Post Type',  // The name of the type in the front end
  4  'can_export' => true,  // Make it possible to export posts of this type,
  5  'description' => 'Just an example!' // A short description
  6  ));

### How custom post types are secured

Each post type has its own editor page (e.g.  _example.com/wordpress/wp-admin/?page=example_post_type_editor_).

![Editor page for Contact Form that can be accessed by administrators.](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/2817fbd8-d211-46b7-b677-e4850fe65f02/body-69dabda3-69c1-43bf-9cda-0d210577f821_wordpress_post_type.png)

If the plugin developer decides that only administrators should be allowed to use the post type of the plugin, he will simply check if the user is an administrator at the top of the page and end execution otherwise.

**/wp-content/plugins/example_plugin/example_post_type_editor.php**

Copy to clipboard
  
  
  if(!current_user_is_administrator()) {
  die("You are not an administrator and not allowed to use this post type.");
  }

### WordPress post submission

Although all registered post types have their own editor, they can all use the WordPress post submission API and insert and update the posts with the WordPress function `wp_write_post()`. The function takes user input such as `$_POST['post_type']`, `$_POST['post_title']` and `$_POST['post_content']` so it knows how to process the post.

In the first step of WordPress’s post submission process, WordPress has to know if the user wants to edit an existing post or create a new one. To do this, WordPress checks if the user has sent an ID of a post. WordPress will allow either `$_GET['post']` or `$_POST['post_ID']`. If an ID is set, the user wants to edit an existing post with that ID. Otherwise the user wants to create a new post.

**/wp-admin/post.php**

Copy to clipboard
  
  
  if ( isset( $_GET['post'] ) )
  $post_id = $post_ID = $_GET['post'];
  elseif ( isset( $_POST['post_ID'] ) )
  $post_id = $post_ID = $_POST['post_ID'];
  
  if($post_id)
  ⋮

In the next step, WordPress has to determine which post type the user is trying to create. If a post ID has been sent, WordPress will pull the `post_type` column from the database from the `wp_posts` table. If the user wants to create a new post, the target post type will be `$_POST['post_type']`.

**/wp-admin/post.php**

Copy to clipboard
  
  
  if ( isset( $_GET['post'] ) )
  $post_id = $post_ID = $_GET['post'];
  elseif ( isset( $_POST['post_ID'] ) )
  $post_id = $post_ID = $_POST['post_ID'];
  
  if($post_id)
  $post_type = get_post_type($post_id);
  else
  $post_type = $_POST['post_type'];
  

Once WordPress knows the post type of the post the user is trying to create or edit, it will check if the user is actually allowed to use that post type. WordPress does this by verifying a nonce that can only be obtained from the editor page of the post type in question.

To do the nonce verification, WordPress will utilize the following code:

**/wp-admin/post.php**

Copy to clipboard
  
  
  if($post_id)
  $post_type = get_post_type($post_id);
  else
  $post_type = $_POST['post_type'];
  
  $nonce_name = "add-" . $post_type;
  if(!wp_verify_nonce($_POST['nonce'], $nonce_name))
  die("You are not allowed to use this post type!");

If the `$post_type` was a  _post_ , the `$nonce_name` would be  _add-post_. If `$post_type` was  _example_post_type_ , the `$nonce_name` would be  _add-example_post_type_. This nonce can only be obtained by users that have the capability to create these post types, because only these users can access the editor page of that post type, which is the only way to get the nonce.

### WordPress’s failure

Although lower privileged attackers, such as attackers in the contributor role, can’t access the page and nonce of the example post type, he can always get the nonce of a normal post, which has the simple internal post type  _post_. This means he could simply set the post ID to a post with the post type  _post_. This would allow him to pass the nonce verification.

**/wp-admin/post.php**

Copy to clipboard
  
  
  // Send a post ID of a post of post type 'post'
  if($post_id)
  // This would return 'post'
  $post_type = get_post_type($post_id);
  else
  $post_type = $_POST['post_type'];
  
  // All users can by default create 'posts' and get the nonce to pass this check
  $nonce_name = "add-" . $post_type;
  if(!wp_verify_nonce($nonce_name))
  die("You are not allowed to create posts of this type!");

However, this method only allows updating an existing post and it is not possible to overwrite the `post_type` of a post. If a post ID is set, WordPress will remove the `post_type` from the parameters before updating the post.

However, WordPress will only remove the `$post_type` parameter if `$_POST['post_ID']` is set. An attacker can send a post ID via `$_POST['post_ID']` **or** `$_GET['post']`. If an attacker sends a post ID via `$_GET['post']` the following will happen:

  1. WordPress sees that a post ID is set and pulls its post type from the database.
  2. WordPress checks if the attacker sent a valid nonce for that post type (which he can always get for a normal `post`)
  3. Once the nonce check is passed WordPress determines if it should call either `wp_update_post()` or `wp_insert_post()`. It does this by checking if `$_POST['post_ID']` is set. If it is, `wp_update_post` will be called and the `$post_type` parameter will be removed, thus not allowing the attacker to overwrite the post type. If it is not set, WordPress will call `wp_insert_post()` and use `$_POST['post_type']` as the post type of the new post.

Because WordPress forgets to also check `$_GET['post']` in the third step, an attacker can pass the nonce verification and create a new post with an arbitrary post type. The code snippets shown are simplified and abstracted, the real code spans across multiple files and function calls, which makes the process prone to such flaws.

**/wp-admin/post.php**

Copy to clipboard
  
  
  // An attacker sets $_GET['post'] to a post of a post type he can access
  if ( isset( $_GET['post'] ) )
  $post_id = $post_ID = $_GET['post'];
  elseif ( isset( $_POST['post_ID'] ) )
  $post_id = $post_ID = $_POST['post_ID'];
  
  if($post_id)
  // The post type is now 'post'
  $post_type = get_post_type($post_id);
  else
  $post_type = $_POST['post_type'];
  
  // Since the attacker has access to that post type, he can get the nonce and
  // pass the nonce verification check
  $nonce_name = "add-" . $post_type;
  if(!wp_verify_nonce($nonce_name))
  die("You are not allowed to create posts of this type!");
  
  $post_details = array(
  'post_title' => $_POST['post_title'],
  'post_content' => $_POST['post_content'],
  'post_type' => $_POST['post_type']
  );
  
  // WordPress only unsets the post_type if $_POST['post_ID'] is set and forgets to
  // check $_GET['post']
  if(isset($_POST['post_ID'])) {
  
  unset($post_details['post_type']);
  $post_details['ID'] = $post_id;
  wp_update_post($post_details);
  } else {
  // If we just set $_GET['post'] we will enter this branch and can set the
  // post type to anything we want it to be!
  wp_insert_post($post_details);
  }

### Exploitation: Reading the wp-config.php via Contact Forms 7

By now you should understand that lower privileged users can abuse this bug to create posts of any type and that the impact on a target site depends on what plugins are installed and what features the post types that come with the installed plugins offer.

To give a concrete example, it was possible for attackers in the role of a contributor to abuse a feature in WordPress’s most popular plugin, Contact Form 7, to read the contents of the wp-config.php file of the target site. This file contains database credentials and encryption keys.

Up to version 5.0.3 of Contact Forms 7, it was possible to set local file attachments. When an admin creates a contact form and a visitor of the page contacts him through it, an email is sent to the administrator with all the data the user has entered. Local file attachments are a setting for a contact form where administrators can define local files to be sent as an attachment with each email.

This means an attacker could simply create a new contact form, set the local file attachment to` ../wp-config.php` and set the email to which the data should be sent to his own, submit the form and then read the contents of the most important WordPress file.

### Fix for plugin developers

Plugin developers should further tighten the security of their plugins by explicitly setting the `capability` and `capability_type` parameters when calling `register_post_type()`. In the WordPress documentation you can find more information on [securing post types](https://codex.wordpress.org/Function_Reference/register_post_type#capability_type) with `register_post_type`.

Copy to clipboard
  
  
  // Example post type
  register_post_type( 'example_post_type', array(
  'label' => 'Example Post Type',  
  
  'capability_type' => 'page'  // capability_type of page makes sure that
  // only editors and admins can create posts of 
  // that type
  ));

### XMLRPC and REST API of WordPress

It is possible to create posts via the XMLRPC and the REST API of WordPress, which do not perform nonce verification for a specific post type. However, when creating posts via these APIs, it is not possible to set arbitrary `post meta` fields. Most vulnerabilities in plugins that we have discovered are only exploitable if users can set these post meta fields.

## Timeline

**Date**| **What**  
---|---  
2018/08/31| Reported the vulnerability to Contact Form 7 via the contact form on their website  
2018/09/02| Reported the vulnerability to WordPress on Hackerone  
2018/09/04| Contact Form 7 fixes the vulnerability  
2018/09/27| WordPress security team triages the vulnerability on Hackerone  
2018/10/12| WordPress proposes a patch on Hackerone  
2018/10/18| We verify the patch  
2018/12/13| WordPress releases a patch in version 5.0.1  
  
## Summary

Attackers with a user role as low as a contributor, the second lowest role in WordPress, can create posts of post types they usually should not have access to. This gives attackers access to features that were intended for administrators only. We have identified 2 vulnerabilities in WordPress’s Top 5 Popular plugins so far. We estimate that thousands of plugins are potentially vulnerable. Furthermore, a Stored XSS and Object Injection was identified in one of WordPress’s internal post types. The Stored XSS can be triggered via a click-jacking attack. Once the JavaScript is executed, a full site takeover is possible.

### Related Posts

  * [WordPress 5.1 CSRF to Remote Code Execution](https://blog.sonarsource.com/wordpress-post-type-privilege-escalation/)
  * [WordPress <= 5.2.3: Hardening Bypass](https://blog.sonarsource.com/wordpress-post-type-privilege-escalation/)
  * [WordPress Design Flaw Leads to WooCommerce RCE](https://blog.sonarsource.com/wordpress-post-type-privilege-escalation/)
  * [WordPress File Delete to Code Execution](https://blog.sonarsource.com/wordpress-post-type-privilege-escalation/)
  * [WordPress 5.0.0 Remote Code Execution ](https://blog.sonarsource.com/wordpress-post-type-privilege-escalation/)
