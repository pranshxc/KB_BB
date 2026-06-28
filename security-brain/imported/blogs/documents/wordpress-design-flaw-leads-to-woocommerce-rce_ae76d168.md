---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-05_wordpress-design-flaw-leads-to-woocommerce-rce.md
original_filename: 2018-11-05_wordpress-design-flaw-leads-to-woocommerce-rce.md
title: WordPress Design Flaw Leads to WooCommerce RCE
category: documents
detected_topics:
- command-injection
- access-control
- xss
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- access-control
- xss
- automation-abuse
- api-security
language: en
raw_sha256: ae76d1686eda3cd06d71c1424b4ed60c8adcb47197d77602d4949a5a682487fb
text_sha256: ef3122e8c6079e8f79aa0aa2fab3f6a5692cd09d844f5b12fc7a275c21923a82
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# WordPress Design Flaw Leads to WooCommerce RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-05_wordpress-design-flaw-leads-to-woocommerce-rce.md
- Source Type: markdown
- Detected Topics: command-injection, access-control, xss, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `ae76d1686eda3cd06d71c1424b4ed60c8adcb47197d77602d4949a5a682487fb`
- Text SHA256: `ef3122e8c6079e8f79aa0aa2fab3f6a5692cd09d844f5b12fc7a275c21923a82`


## Content

---
title: "WordPress Design Flaw Leads to WooCommerce RCE"
page_title: "WordPress Design Flaw Leads to WooCommerce RCE | Sonar"
url: "https://www.sonarsource.com/blog/wordpress-design-flaw-leads-to-woocommerce-rce/"
final_url: "https://www.sonarsource.com/blog/wordpress-design-flaw-leads-to-woocommerce-rce/"
authors: ["Simon Scannell (@scannell_simon)"]
programs: ["Automattic (WooCommerce)"]
bugs: ["RCE"]
publication_date: "2018-11-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5605
---

## TL;DR overview

  * A design flaw in WordPress's role and capability system enabled remote code execution in WooCommerce by allowing shop manager accounts to escalate privileges to full administrator access.
  * The vulnerability exploits a gap in how WooCommerce interacts with WordPress's user role system, where a shop manager can modify their own role to gain unrestricted capabilities.
  * Once elevated to administrator, the attacker can install plugins or edit theme files to execute arbitrary PHP code on the server.
  * Both WordPress and WooCommerce released patches; the finding highlights the security risks of complex permission models in plugin-dependent CMS architectures.

A flaw in the way WordPress handles privileges can lead to a privilege escalation in WordPress plugins. This affects for example WooCommerce, the most popular e-commerce plugin with over 4 million installations. The vulnerability allows shop managers to delete certain files on the server and then to take over any administrator account (CVE-2018-20714).  

## Impact

We detected and reported a  _file deletion_ vulnerability in WooCommerce, which was fixed in version **3.4.6.** Arbitrary file deletion vulnerabilities aren’t considered critical in most cases as the only thing an attacker can cause is a Denial of Service by deleting the index.php of the website. This post details how deleting certain plugin files in WordPress can disable security checks and then leads to a full site takeover. At fault is an unpatched design flaw in the privilege system of WordPress. Affected were over 4 million WooCommerce shops. No other requirements other than an attacker being in control of an account with the user role  _shop manager_ were required.  _Shop managers_ are employees of the store that can manage orders, products, and customers. Such access could be obtained via XSS vulnerabilities or phishing attacks. Once the vulnerability described here is exploited, the shop manager can take over any administrator account and then execute code on the server.

## Technical Details

The way WordPress handles privileges is by assigning certain capabilities to different roles. When the shop manager role is defined, it is assigned the `edit_users` capability so that they are allowed to edit customer accounts of the store. This happens during the installation process of the plugin.

**woocommerce/includes/class-wc-install.php**

Copy to clipboard
  
  
  1  // Shop manager role.
  2  add_role(
  3  'shop_manager',  // Internal name of the new role
  4  'Shop manager',  // The label for displaying
  5  array(  // Capabilities
  6  ⋮
  7  'read_private_posts'  => true,
  8  'edit_users'  => true,
  9  'edit_posts'  => true,
  10  ⋮
  11  )
  12  );

The role is then stored in the database as a core setting of WordPress. This means that the user role is now independent of the plugin and will exist even if the plugin is inactive. Whenever an authenticated user tries to edit another user, a call to `current_user_can()` is made to ensure only privileged users can perform that action.

**Example of a call to current_user_can()**

Copy to clipboard
  
  
  1  $target_user_id = $_GET['target_user_id']; 
  2  if(current_user_can('edit_user', $target_user_id)) { 
  3  edit_user($target_user_id); 
  4  }

The logic of the call is “ _Can the user trying to perform this action edit the specific user with the ID_`$target_user_id` _?_ “

By default the `edit_users` capability allows users who have this privilege, e.g. shop managers, to edit any user, even administrators, and perform actions such as updating their passwords. For security reasons, WooCommerce needs to specify that shop managers should be able to edit users, but only those with the customer role.

To do so, plugins such as WooCommerce can add meta capabilities. Meta capabilities are implemented as functions that are called by `current_user_can()`. Instead of simply returning  _true_ as the default behavior, the return value of the meta privilege function will decide whether or not the current user can perform that action. An abstracted version of WooCommerce’s meta privilege filter is shown below.

**Example of a meta capability**

Copy to clipboard
  
  
  1  function disallow_editing_of_admins( $capability, $target_user_id ) { 
  2
  3  // If the user is an admin return false and disallow the action 
  4  if($capability == "edit_user" && user_is_admin($target_user_id)) { 
  5  return false; 
  6  } else { 
  7  return true; 
  8  }
  9  } 
  10  add_filter( 'map_meta_cap', 'disallow_editing_of_admins'); 

As an example, when `current_user_can(‘edit_user’, 1)` is called, the filter will be executed to determine if the user with the ID 1 (`$target_user_id`) is an admin and if so disallow editing and return  _false_. Otherwise, it will let the user proceed. The actual, more complex meta cap hook of WooCommerce is stored in `woocommerce/includes/wc-user-functions.php` on line 408.

### The Design Flaw

While these filters work, they only get executed when the plugin is active. The issue is that user roles get stored in the database and exist even if the plugin is disabled. This means that if WooCommerce was disabled for some reason, the meta privilege check which restricts shop managers from editing administrators would not execute and the default behavior of allowing users with `edit_users` to edit any user, even administrators, would occur. This would allow shop managers to update the password of the admin account and then take over the entire site.

### Disabling the plugin as a shop manager

By default, only administrators can disable plugins. However, RIPS detected an arbitrary file deletion vulnerability in WooCommerce. This vulnerability allows shop managers to delete any file on the server that is writable. By deleting the main file of WooCommerce, `woocommerce.php`, WordPress will be unable to load the plugin and then disables it.

The file deletion vulnerability occurred in the logging feature of WooCommerce. Logs are stored as .log files in the `wp-content` directory. When a shop manager wants to delete a log file, he submits its filename as a GET parameter. As the following code snippets show this is handled insecurely. 

**woocommerce/includes/admin/class-wc-admin-status.php**

Copy to clipboard
  
  
  1  class WC_Admin_Status
  2  {
  3  public static function remove_log()
  4  {
  5  ⋮
  6  $log_handler = new WC_Log_Handler_File();
  7  $log_handler->remove(wp_unslash($_REQUEST['handle']));
  8  }

**woocommerce/includes/log-handlers/class-wc-log-handler-file.php**

Copy to clipboard
  
  
  1  class WC_Log_Handler_File extends WC_Log_Handler
  2  {
  3  public function remove($handle)
  4  {
  5  ⋮
  6  $file = trailingslashit(WC_LOG_DIR) . $handle;
  7  ⋮
  8  unlink($file);

The issue is that the filename (`$handle`) is appended to the Log directory (`wp-content/wc-logs/`) and then passed to `unlink()`. When setting `$handle../../plugins/woocommerce-3.4.5/woocommerce.php` the file `wp-content/wc-logs/../../plugins/woocommerce-3.4.5/woocommerce.php` would be deleted, causing WooCommerce to get disabled.  

## Timeline

**Date**| **What**  
---|---  
2018/08/30| The Arbitrary File Deletion Vulnerabiliy was reported to the Automattic security team on Hackerone.  
2018/09/11| The vulnerability was triaged and verified by the security team.  
2018/10/11| A patch was released.  
  
## Summary

In a previous post, we demonstrated how to exploit a file delete vulnerability in WordPress and how to elevate the file delete into a remote code execution vulnerability. The downside of that method was that all data was lost on the target site. The method detailed in this blog post shows how a file deletion vulnerability in any WordPress plugin can be used to escalate privileges where meta privileges are used. This design flaw still persists. File deletion vulnerabilities are not uncommon and even occur in the WordPress core itself. Note, that file delete vulnerabilities can also be exploited with Phar deserialization under certain circumstances.
