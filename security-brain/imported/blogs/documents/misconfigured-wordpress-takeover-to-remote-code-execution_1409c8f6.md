---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-22_misconfigured-wordpress-takeover-to-remote-code-execution.md
original_filename: 2020-04-22_misconfigured-wordpress-takeover-to-remote-code-execution.md
title: Misconfigured WordPress takeover to Remote Code Execution
category: documents
detected_topics:
- command-injection
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- api-security
- cloud-security
language: en
raw_sha256: 1409c8f6ab4d116e92cb3fc7f2a4c53ddb3ac7ed60181252de3762f6eb15e4ca
text_sha256: f5994cb1f5ced26b9a6dc2820b33a6de844eee2c3e28d1946553ad4e40f2bab2
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Misconfigured WordPress takeover to Remote Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-22_misconfigured-wordpress-takeover-to-remote-code-execution.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `1409c8f6ab4d116e92cb3fc7f2a4c53ddb3ac7ed60181252de3762f6eb15e4ca`
- Text SHA256: `f5994cb1f5ced26b9a6dc2820b33a6de844eee2c3e28d1946553ad4e40f2bab2`


## Content

---
title: "Misconfigured WordPress takeover to Remote Code Execution"
page_title: "Misconfigured WordPress takeover to Remote Code Execution – Smaran Chand"
url: "https://smaranchand.com.np/2020/04/misconfigured-wordpress-takeover-to-remote-code-execution/"
final_url: "https://smaranchand.com.np/2020/04/misconfigured-wordpress-takeover-to-remote-code-execution/"
authors: ["Smaran Chand (@smaranchand)"]
bugs: ["Wordpress takeover", "RCE", "Security misconfiguration"]
publication_date: "2020-04-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4638
---

[April 22, 2020](https://smaranchand.com.np/2020/04/misconfigured-wordpress-takeover-to-remote-code-execution/)

# Misconfigured WordPress takeover to Remote Code Execution

Hello Everyone, I hope you guys are doing well. I am sharing a recent issue which I discovered today only. And this is the most instant write-up I have ever published. In summary, I ended up with Remote Code Execution (RCE) by exploiting the misconfigured WordPress although it isn’t the same thing which you just thought now.

So it all commenced when I noticed a subdomain of a well-reputed company http://subdomain.domain.com opened it and this is what I saw on the landing page. 

![](https://smaranchand.com.np/wp-content/uploads/2020/04/wp_setup_misconfig.png)WordPress Installation landing page.

Now Tellme who won’t be happy when someone sees it?

It seems like they have installed/unzipped the WordPress CMS maybe from Github but haven’t completed the installation maybe of certain reasons. I was pretty very much sure that this is a potential takeover but the happiness even couldn’t last 30 seconds. 

![](https://smaranchand.com.np/wp-content/uploads/2020/04/wp_setup_misconfig2.png)Setup WordPress database config.  

Seems like we got a challenge here!

I tried to enumerate the database name, username, password but I couldn’t succeed. I even searched for password dumps, did GitHub recon, used a common password but none of them were on the track.

Wait !!! why do I need to guess their database credentials? After all, it’s about installing WordPress. So I planned to try connecting the cloud database and completing the WordPress installation. I googled for a better Cloud database solution and ended up creating a MySQL remote database in Azure. 

![](https://smaranchand.com.np/wp-content/uploads/2020/04/azure.png)MySQL Database service in Azure.

I choose a cost-effective and healthy configuration and deployed it. My MySQL database server was ready within 100 seconds, that’s really cool.

![](https://smaranchand.com.np/wp-content/uploads/2020/04/deploy.png)Cloud Database Configuration

It’s doomsday now! I moved towards the setup page, fed the database configuration, password and hostname and clicked submit. 

![](https://smaranchand.com.np/wp-content/uploads/2020/04/Setup_Cloud_Database.png)Setup WordPress with a remote MySQL database.

But again it didn’t go as expected.

![](https://smaranchand.com.np/wp-content/uploads/2020/04/error.png)Error Connecting Database.

I tried troubleshooting the issue and found that Azure does have a connection security feature maybe I need to whitelist the IP address of the server (Where WordPress is Hosted). I also tried connecting the database with SQL client and got to know that I haven’t created any database. My bad!!!

So i used a SQL client tool called Sequel Pro connected the database server and created the database. 😀

![](https://smaranchand.com.np/wp-content/uploads/2020/04/setupdbdone-700x189.png)Create Database

Now !, Yes Now! 

Doomsday II started with the same thing, tried the setup with the same configuration and here we go.

![](https://smaranchand.com.np/wp-content/uploads/2020/04/databaseset.png)Database connected.

So finally I connected the remote SQL database with the victim’s website/CMS. Now let’s begin the setup. It all went smoothly, successfully setup the WordPress.

![](https://smaranchand.com.np/wp-content/uploads/2020/04/Screen-Shot-2020-04-22-at-3.08.27-PM.png)Installing WordPress

And I got to know that I just takeover their CMS in a noobs way.

![](https://smaranchand.com.np/wp-content/uploads/2020/04/pwned-700x377.png)Website Pwned

Booyah !!! Finally, I pwned their website/subdomain through a different technique which I never knew. I know it feels like a subdomain takeover but this isn’t actually a subdomain takeover. As of now, the webserver is the same as before but the database is mine. :-8.

## **IT DOES NOT END HERE !!!**

I logged into the WordPress admin panel and started thinking about chaining the attack. I have access to the CMS but don’t have access to the server. 

Bro, how about pwning the webserver now ???

Wait No! I shouldn’t be doing it in a noobs way. Ahh, I don’t want to repeat the old technique. 

The old habit of shelling websites is never leaving us, Aye! old days, gold days! (I borrowed this line partially from somewhere.)

Ethically trying to get a Remote Code Execution (RCE) now. I laughed very much here.

![](https://smaranchand.com.np/wp-content/uploads/2020/04/dashboard-700x505.png)WordPress Dashboard.

I tried to upload a PHP web shell via media upload and other functionalities but couldn’t succeed. How can I forget the old ninja technique? 

![](https://smaranchand.com.np/wp-content/uploads/2020/04/upload_webshell.png)Uploading webshell through themes.

I downloaded a random WordPress theme from the web unzipped it and added my webshell inside it. 

![](https://smaranchand.com.np/wp-content/uploads/2020/04/shell.png)PHP Webshell 

After WordPress theme is installed successfully I moved towards the location of wp themes which is generally /wp-content/themes/themename/ and added my webshell file name.

And here we go Remote Code Execution. !!! 

![](https://smaranchand.com.np/wp-content/uploads/2020/04/rce.png)Remote Code Execution in Windows Server

Here is the attack narrative/attack flow.

![](https://smaranchand.com.np/wp-content/uploads/2020/04/narrative.png)Attack Flow

**Summary**

Database: Belongs to the attacker 

WordPress website (CMS): Compromised by Attacker

Webserver: Compromised by Attacker

Well, that’s the end of the story, and it’s possible to take over any WordPress website having the same misconfiguration.

If you really liked my writeup do share it with others so that I will continue publishing more interesting findings for sure.

[Bug Bounty](https://smaranchand.com.np/writeups/bug-bounty/), [Research](https://smaranchand.com.np/writeups/researchs/)
