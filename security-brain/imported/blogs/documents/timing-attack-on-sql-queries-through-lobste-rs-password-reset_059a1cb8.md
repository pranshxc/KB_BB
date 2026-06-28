---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-20_timing-attack-on-sql-queries-through-lobsters-password-reset.md
original_filename: 2021-08-20_timing-attack-on-sql-queries-through-lobsters-password-reset.md
title: Timing Attack on SQL Queries Through Lobste.rs Password Reset
category: documents
detected_topics:
- password-reset
- rate-limit
- sqli
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- password-reset
- rate-limit
- sqli
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 059a1cb8954409a85b79ec25e55b5c74f9eb845b17fa0484315bb610619752db
text_sha256: 20b146c914d2ddc8c51a7447653dfda79a3dfbf78936e052398bd756caedc845
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Timing Attack on SQL Queries Through Lobste.rs Password Reset

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-20_timing-attack-on-sql-queries-through-lobsters-password-reset.md
- Source Type: markdown
- Detected Topics: password-reset, rate-limit, sqli, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `059a1cb8954409a85b79ec25e55b5c74f9eb845b17fa0484315bb610619752db`
- Text SHA256: `20b146c914d2ddc8c51a7447653dfda79a3dfbf78936e052398bd756caedc845`


## Content

---
title: "Timing Attack on SQL Queries Through Lobste.rs Password Reset"
page_title: "Timing Attack on SQL Queries Through Lobste.rs Password Reset - Dhole Moments"
url: "https://soatok.blog/2021/08/20/lobste-rs-password-reset-vulnerability/"
final_url: "https://soatok.blog/2021/08/20/lobste-rs-password-reset-vulnerability/"
authors: ["Soatok (@SoatokDhole)"]
programs: ["Lobste.rs"]
bugs: ["Timing attack", "Password reset"]
publication_date: "2021-08-20"
added_date: "2023-08-21"
source: "pentester.land/writeups.json"
original_index: 3404
---

Categories 

[Cryptography](https://soatok.blog/category/cryptography/) [Vulnerability](https://soatok.blog/category/technology/software-security/vulnerability/)

# Timing Attack on SQL Queries Through Lobste.rs Password Reset

  * Post author  By [Soatok](https://soatok.blog/author/soatok/)
  * Post date  [August 20, 2021](https://soatok.blog/2021/08/20/lobste-rs-password-reset-vulnerability/)
  * [3 Comments on Timing Attack on SQL Queries Through Lobste.rs Password Reset](https://soatok.blog/2021/08/20/lobste-rs-password-reset-vulnerability/#comments)

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/07/blogheader-lobsters.png?fit=1200%2C675&ssl=1)

Just to assuage any panic, let me state this up front.

If you’re reading this blog post wondering if your [Lobste.rs](https://lobste.rs/) account is at risk, good news: I didn’t publish it until after the vulnerability was mitigated, so you’re safe. You don’t need to change your passwords or anything.

This write-up is purely for education and entertainment purposes.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/03/soatoktelegramswave3-01.png?resize=512%2C512&ssl=1)(Art: [[CMYKat](https://cmykatgraphics.carrd.co/)](https://twitter.com/lynxvsjackalope))

However, there are a few [“Sister Sites”](https://github.com/lobsters/lobsters/wiki#sister-sites) using the Lobste.rs codebase, and I didn’t bother to check if they were affected, or that they patched if they were. If you run a similar site based on the Lobste.rs codebase, make sure you implement [a similar mitigation](https://github.com/lobsters/lobsters/commit/eaaa25b1afd385fb3b24762e9270412dff8d986a).

## Background

Lobste.rs is a news website created [nine years ago](https://lobste.rs/s/idj3tm/lobsters_is_nine_today) in response to Hacker News’s lack of moderation transparency and decline in submission/comment quality. One of the cool things Lobste.rs did was make the entire platform invite-only, with [a public tree of who invited who](https://lobste.rs/u).

In practice, I’ve found the Lobste.rs sysops to be friendly and reasonable, and the community is a bit more [tolerant of my furry antics](https://soatok.blog/2020/07/09/a-word-on-anti-furry-sentiments-in-the-tech-community/) than Hacker News or [most subreddits](https://soatok.blog/2021/03/04/no-gates-no-keepers/#r-netsec).

![Soatok hugs a giant heart](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/04/heart2.png?resize=224%2C224&ssl=1)(Art by [Swizz](https://twitter.com/SwizzlestixUK))

With that in mind, whenever I log onto content aggregation websites that have some concept of a reputation or karma score, I occasionally notice it increase–even during periods of inactivity. This usually piques my curiosity to look at the threads I’ve recently participated in, in hopes of discovering a new direction in the conversation that I hadn’t already seen.

This recently led me to discover a new link above one of my comments that I hadn’t seen before.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/07/disown-comment-link.png?resize=768%2C86&ssl=1)Oooo, what does _this_ button do? ([Link](https://lobste.rs/s/iuurqm/openpgp_js_openpgp_javascript#c_uhhgit))

I couldn’t find anything explaining this feature on the About page, so I decided to look at [the Lobste.rs source code on GitHub](https://github.com/lobsters/lobsters). After a few minutes, I got bored and then curious. I wondered about how passwords are stored (which is the only plausible reason for Lobste.rs to use any cryptography–which is my area of focus within infosec), and started delving into the user authentication code.

As a result of my curiosity, I discovered a vulnerability in Lobste.rs’s handling of forgotten passwords that could lead to a targeted account takeover.

## How Lobste.rs Handles Forgotten Passwords

Most web applications that allow users to authenticate with a username and password will inevitably implement a fail-safe for forgotten passwords.

**Lobste.rs is no exception.** If you forget your password, Lobste.rs will email you a link that you can use to change the password for your account to one you’ll hopefully remember next time.

[This is how tokens are generated](https://github.com/lobsters/lobsters/blob/cc19708575a1432ea9466bc9fe8b58788d910339/app/models/user.rb#L438-L440) in Lobste.rs:
  
  
  def initiate_password_reset_for_ip(ip)
  self.password_reset_token = "#{Time.current.to_i}-#{Utils.random_str(30)}"
  self.save!
  

The `Utils.random_str` definition, in turn, [looks like this](https://github.com/lobsters/lobsters/blob/f25fc62d7603c1bf7089925ad5517948b5008d42/extras/utils.rb#L2-L15):
  
  
  def self.random_str(len)
  str = ""
  while str.length < len
  chr = OpenSSL::Random.random_bytes(1)
  ord = chr.unpack1('C')
  
  #  0  9  A  Z  a  z
  if (ord >= 48 && ord <= 57) || (ord >= 65 && ord <= 90) || (ord >= 97 && ord <= 122)
  str += chr
  end
  end
  
  return str
  end
  
  

Good, they’re using a secure random number generator.

Now, there _is_ an edge case with OpenSSL’s random number generator in apps that use `fork()` (n.b. it [caused collisions in a popular UUID library](https://github.com/ramsey/uuid/issues/80#issuecomment-197539114) in PHP before), but I don’t know if that’s relevant to Ruby on Rails apps at all. That’s certainly not the vulnerability we’re discussing today. (If someone else wants to chase that down, be my guest.)

Look instead at [how the password reset tokens are _used_](https://github.com/lobsters/lobsters/blob/f25fc62d7603c1bf7089925ad5517948b5008d42/app/controllers/login_controller.rb#L136-L141):
  
  
  if (m = params[:token].to_s.match(/^(\d+)-/)) &&
  (Time.current - Time.zone.at(m[1].to_i)) < 24.hours
  @reset_user = User.where(:password_reset_token => params[:token].to_s).first
  end
  

Let me translate this code into English:

If the password begins with an integer followed by a hyphen, and the integer represents a valid UNIX Timestamp that’s also less than 24 hours old, then query the database for the first user that possesses this exact password reset token string in the appropriate field.

If this query returns a row, then you get to set the password for that user.

![Evil Laugh](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/04/soatok_stickerpack-evil-laughter.png?resize=512%2C512&ssl=1)(Art: [[CMYKat](https://cmykatgraphics.carrd.co/)](https://twitter.com/lynxvsjackalope))

## The Vulnerability

When performing a `SELECT` query against a relational database, most application security specialists are only concerned with SQL injection–which is fair, because a lot of applications are still vulnerable to that.

However, if you’re providing a cryptographic secret into your `WHERE` clause, you’re going to leak that secret via timing information, since databases use [a timing-leaky comparison function](https://github.com/MariaDB/server/blob/76f4a78ba2639b5abd01a88b24a3c509c11530ce/plugin/handler_socket/libhsclient/string_ref.hpp#L43-L46) like `memcmp()` when searching for strings. (Counter-examples _may_ exist, but I’m unaware of any.)

If you look at how Lobste.rs handled password resets, it should be clear that their password reset token is vulnerable to a **timing attack**.
  
  
  # ActiveRecord turns this into something like...
  # "SELECT * FROM user WHERE password_reset_token = $1"
  @reset_user = User.where(:password_reset_token => params[:token].to_s).first
  

### Is a Timing Attack Really Practical Here?

**Maybe.** That depends what you mean by “practical”.

Security experts have known since 2009 that it’s possible to reliably determine the correct signal for a timing difference of 15 nanoseconds [with about 49,000 samples over the Internet](http://www.cs.rice.edu/~dwallach/pub/crosby-timing2009.pdf).

Since you have a total window of about 86,400 seconds from the creation of a password reset token until it’s no longer usable, without any deeper analysis, you’d only need to be able to reliably perform about 17 guesses per second (49,000 samples based on the linked paper, times 30 characters of uncertainty, divided by 86,400 seconds) to guess the correct password reset token for a targeted Lobste.rs account. That’s not infeasible, but still a lot.

If one person attempted this attack, it might create increased server load, but shouldn’t otherwise cause any unintended side-effects.

If dozens or hundreds of attacks were attempted at once, it might cause an outage (or potentially trigger an Anti-DDoS mitigation).

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/04/soatoktelegramswave3-10.png?resize=512%2C512&ssl=1)(Art: [[Lynx vs Jackalope](https://twitter.com/lynxvsjackalope)](https://twitter.com/lynxvsjackalope))

I would consider 17 request per second (approximately one request per 57 milliseconds) within the realm of possibility for a hypothetical attacker to pull off, so from that sense, it _is_ practical.

**However, it’s very slow.**

This attack still involves a lot of traffic over a long period of time, and a lot of automated statistical analysis to determine which input is taking longer to fail. You need to maintain the request per second rate for an entire 24 hour period to break one token, which means hammering the server for an entire day.

I wouldn’t expect a timing attack to be any attacker’s first choice to get into a system. There’s usually a less expensive and less detectable attack to be found.

Consequently, I anticipate some commentators will dismiss my finding outright, because, “Nobody breaks into computers with cryptographic attacks like this.”

This is a bit silly when contrasted with the usual information security wisdom; n.b. “**Defenders have to be right 100% of the time, attackers only have to be right once**.”

But then again, who am I to judge people’s weird hills?

### Quick Aside About Timing Attack Exploitation

Most descriptions of a remote timing attack exploit you’ll find on the Internet are **actually wrong**.

It’s true that, in a challenge-response authentication protocol like this, you can use a timing attack to slowly guess the correct value based on which inputs take longer to fail.

What they get wrong is that you usually can’t attack functions like `memcmp()` one byte at a time. The actual resolution window is usually larger (e.g. [32 bits](https://github.com/lattera/glibc/blob/895ef79e04a953cac1493863bcae29ad85657ee1/string/memcmp.c#L49) in glibc).

This implementation detail matters a lot, and if you get it wrong, you’ll be chasing false positives instead of producing a working exploit demo.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/04/soatok-telegrams-wave-3-commission-13.png?resize=512%2C512&ssl=1)Ask me how I know!  
(Art: [CMYKat](https://cmykatgraphics.carrd.co/))

### What Would an Exploit Actually Look Like?

Remember that there are two pieces of information with the password reset token: The UNIX timestamp at the time of its creation, and a secret 30 character random string that is emailed to the user.

You almost always know the current time for the server you’re talking to on the Internet, but if you need to reliably leak _that_ , you can just issue a password reset request for your own user account and calculate the clock skew between your machine and the Lobste.rs server’s.

Next, the exploit would need to initiate a password reset token for the target user, taking note of the exact time the issue was requested. At this point, the target user will be notified by email (but if their email address is some small, DDoS-able server rather than a large enterprise like Gmail, that’s easily avoided too).

At the beginning, you know the UNIX timestamp and the hyphen.

`1625584524-??????????????????????????????`

From here, you’ll need to enumerate all possible values for a single character of the password keyspace `A-Za-z0-9` (62 combinations), for each byte that’s occupied by a `memcmp` call.

If the uncertainty of the window is one byte, that’s 62 combinations per `memcmp`. If the uncertainty of the window is two bytes, that’s 3,844 combinations. The size of the window (in bytes) is an exponent here, so breaking a four byte window involves selecting the slowest of a set of **_14,776,336_** combinations. The larger the window, the more painful remote timing attacks are (and the closer it gets to “brute force” territory).

For the purposes of this explanation, I’m going to assume a 32-bit (4 byte) window, since [that’s what glibc uses](https://github.com/lattera/glibc/blob/895ef79e04a953cac1493863bcae29ad85657ee1/string/memcmp.c#L49), which means the `memcmp()` chunks will look like this:

`1625|5845|24-?|????|????|????|????|????|????|????|?`

For the first chunk, the uncertainty is only one byte. Try all 62 possible values and collect samples until a measurable timing difference is clear. This may take many samples depending on network jitter.

`1625584524-a?????????????????????????????`

Then, move on with a four-byte window of uncertainty (14,776,336 possible values) for most of the remaining chunks, and perform the same analysis. Keep iterating until you get to the last character of uncertainty. This will take 7 iterations, and the success of each iteration depends on the previous iteration.

`1625584524-abcdefghijklmnopqrstuvwxyz012?`

Now, you only have to guess the correct final byte (only 62 possible values) in a browser window. From there, you can successfully change the password of, and subsequently take over, the account you targeted.

![Evil Laugh](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/04/soatok_stickerpack-evil-laughter.png?resize=512%2C512&ssl=1)(Art: [CMYKat](https://cmykatgraphics.carrd.co/))

Note: I’m not going to implement this attack publicly, because I don’t want to arm script kiddies with another exploit tool that they don’t deserve and will only use to cause harm to the Internet. (Or, more likely, DoS servers while failing to actually leak anything.)

### What Would the Runtime For This Attack Look Like?

After some back-of-the-envelope math above, I arrived at the requirement of about 17 requests per second in order to use this exploit (given the 24 hour expiration window).

This was meant more as a [Fermi estimate](https://brilliant.org/wiki/fermi-estimate/) than the real cost of an attack. Now let’s get technical.

Let’s assume you’ve parked your exploit code in the same data center as Lobste.rs and have less network jitter to contend with. This is what a real attacker would do. Let’s also assume, as a result, it only takes about 20 samples per guess to zero in on the actual timing resolution of the targeted `memcmp`.

The first byte will require a mere **1,240** guesses. The next 28 bytes will take the majority of the time.

Each of the seven remaining chunks will require 295,526,720 samples (assuming the sample-per-window remains at 20), for a total of 2,068,687,040 requests.

If you’re trying to fit this attack in a 24 hour window, the math comes out to about 24,000 requests per second before you know enough of the password reset token to easily solve the rest with 62 browser tabs.

If you’re in a hurry, you can probably do it faster. Nginx can handle [400K to 500K requests per second](https://github.com/denji/nginx-tuning). Ruby on Rails seems to score at about [80K per second](https://twitter.com/Sirupsen/status/885664106677710850) with performance tuning.

If you can afford 50,000 requests per second without crashing the target server and alerting the admin, you can complete the attack in a little under twelve hours.

Conversely, if the window wasn’t 24 hours but instead 30 days, then you could confidently leak the password reset token before it expires at a brisk 800 requests per second.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/04/glitch-ecb.png?resize=224%2C224&ssl=1)(Art by [Swizz](https://twitter.com/SwizzlestixUK))

### That Sounds Slow; Why Not Just Try a Brute Force Attack?

A probability space of 30 characters, where each character can be one of 62 different values, comes out to [about 178 bits of security](https://www.google.com/search?q=30+*+log\(62\)%2Flog\(2\)).

You aren’t brute forcing 178 bits of security.

As with the window size above, security margins are an exponent (this time, it’s base 2).

In 2013 (when the Snowden leaks happened) [80 bits of security](https://www.schneier.com/blog/archives/2013/09/the_nsas_crypto_1.html) was generally considered within the reach of intelligence agencies to crack within a month. As of 2021, Bitcoin miners have collectively been able to exceed [93 bits of hash guesses per year](https://crypto.stackexchange.com/a/13305).

However, there are [physical limits to brute force attacks](https://pthree.org/2016/06/19/the-physics-of-brute-force/). The growth in Bitcoin’s hash-rate isn’t indefinitely sustainable.

It would take over 100 times the current Bitcoin mining capacity to break the 100 bits of security threshold in a year. Further, generalizing that to a centralized effort to brute force a large random secret is nontrivial.

I’m not confident we’ll see the 100 bits per day threshold crossed in my lifetime. We would need a revolution in our understanding of physics to succeed.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/07/not-gonna-happen.jpg?resize=666%2C375&ssl=1)Excerpt from a conversation with [Filippo Valsorda](https://twitter.com/FiloSottile/) about the failure rate of lattice-based key encapsulation algorithms.

Reaching 128 bits of brute force capability is even _less_ likely (and would totally destroy e-commerce, since that’s the security level of most encryption used today), and that’s still one quintillionth the cost to brute force a 178-bit random number.

So, as slow as the timing attack might _seem_ , it’s nowhere near as prohibitively expensive as a brute force attack would be. In fact, the total cost of the timing attack (based on the above example) is on the order of a remote brute force attack against a 32-bit number.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/10/soatok_stickerpackedit-math.png?resize=512%2C512&ssl=1)(Art: [CMYKat](https://cmykatgraphics.carrd.co/))

## Short-Term Mitigation

To mitigate this attack while working on a complete fix, simply rate-limit password reset attempts.

If you limit the number of password reset attempts to, for example, less than 5 per _minute_ per IP address (which means you block after more than 4), you’ll force attackers to parallelize their attack by [an enormous factor](https://www.google.com/search?q=\(1/15s\)%20*%20\(50000/s\)).

(Keep in mind, horizontal scaling a timing attack also makes coordinating the actual statistical analysis harder due to subtle differences in the networking environments across multiple clients.)

This is [precisely what the Lobste.rs admin did](https://github.com/lobsters/lobsters/commit/eaaa25b1afd385fb3b24762e9270412dff8d986a) immediately after he read my email disclosing the vulnerability, as a stopgap measure until the complete fix could be written, tested, and deployed.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/04/soatoktelegramswave3-08.png?resize=512%2C512&ssl=1)(Art: [[CMYKat](https://cmykatgraphics.carrd.co/)](https://twitter.com/lynxvsjackalope))

## The Complete Fix

The first step in fixing any software vulnerability is to first fully understand the actual problem that led to insecurity. Often, the root cause of the insecurity is an assumption that doesn’t hold true. At other times, it’s an _unknown unknown_ entirely. Timing attacks are more of the latter; they exist where developers never thought to ask, “Does how long it takes for a comparison against an incorrect string to return false matter for security?”

In any case, the ideal patch is one that directly addresses the fundamental defect. Sometimes, the ideal patch is not possible (e.g. if you’re building atop cryptographic primitives with unsound security proofs). In those cases, don’t let perfect be the enemy of good; just do what you can.

Fortunately, an ideal patch for this vulnerability _**is possible**_.

The core problem is that the entire secret is being provided in the `WHERE` clause of a SQL query, and the string comparison used by relational databases isn’t meant for comparing cryptographic secrets.

If you want to prevent this attack, the simple thing to do is to use **[Split Tokens](https://paragonie.com/blog/2017/02/split-tokens-token-based-authentication-protocols-without-side-channels)**.

An implementation of Split Tokens in the existing Lobste.rs source code might look like this:

  1. Add a second field to the users table to store a SHA256 hash.
  2. When a password reset is initiated, generate `timestamp-random-additionalrandom`, but only store **the first two parts** in the database column. The `additionalrandom` is new (and sent to the user) but never directly touches the database.
  3. Calculate the SHA256 hash of the _entire_ string from step 2 and store this hash in the new column.
  4. Send the entire string from step 2 to the user via email.

When verifying password reset token, use the first two parts in a SELECT query (as currently implemented), but also re-calculate the SHA256 hash of the entire user-provided string and compare it (using [a constant-time compare function](https://soatok.blog/2020/08/27/soatoks-guide-to-side-channel-attacks/#string-comparison)) against the value stored in the database.

If it doesn’t match, first invalidate the stored token then redirect the user to the login page. This disincentivizes attacks, because you only get one bite at the apple: As soon as you get the correct prefix from a timing leak, unless you guessed `additionalrandom` correctly, you have to start your attack all over again.

### Analysis of the Remediation Strategy

By adopting Split Tokens, only two thirds of the token provided to the user are used in the database query. Since only part of the secret is used in the query, a timing attack cannot leak the entire secret.

The hash of the whole shebang is then checked against a stored hash in another column (which is, critically, NOT used in the WHERE clause of a SELECT query).

As long as this hash comparison is constant-time, we’ve successfully eliminated the timing leak, which removes the vulnerability.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/09/soatoktelegrams2020-08.png?resize=512%2C512&ssl=1)(Art: [[CMYKat](https://cmykatgraphics.carrd.co/)](https://twitter.com/lynxvsjackalope))

## Takeaways

There are a lot of ways you can frame any discussion over a security vulnerability discovery and subsequent disclosure. The worst takes are the, “An issue was found? That means they’re insecure!” variety. [CVEs aren’t scarlet letters](https://news.ycombinator.com/item?id=27764809).

What should matter to everyone is, instead, that Lobste.rs is more secure than they were previously, and the Loste.rs developers are now slightly more knowledgeable about application security. Hopefully, by reading this write-up, that increase in knowledge is now shared by the entire community.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2021/04/soatoktelegramswave3-06.png?resize=512%2C512&ssl=1)(Art: [[CMYKat](https://cmykatgraphics.carrd.co/)](https://twitter.com/lynxvsjackalope))

Let’s talk about application security for a moment. This certainly isn’t the kind of vulnerability that most application security engineers would identify from a casual review of the Lobste.rs source code. This discovery required very specialized knowledge about cryptographic side-channels and how they can crop up in non-cryptographic contexts.

How would you rate the severity of this finding? The answer to that inquiry is usually more opinion than science.

It’s certainly true that the impact is **high** (account takeover), but the exploitation is both highly complex and prohibitively expensive for most attackers to even bother. The only people I know that might be motivated enough to try are the dregs of 4chan (but they’ll also [stab you over what you name your fork of an open source project](https://github.com/tenacityteam/tenacity/issues/99), so they aren’t exactly representative of most computer criminals).

So, personally, I consider it a **sev:low** overall. But it’s still an interesting enough sev:low to write about, and hopefully my blog’s readers agree.

More broadly, this sort of timing attack is relevant to any challenge-response authentication based on a single value (i.e. long-lived access keys for custom APIs), but I find it most frequently in account recovery features.

If you find yourself affected by a similar attack but need to maintain backwards compatibility, just split the existing token in half and implement the same sort of lookup, hash, verify workflow as discussed in [the Split Tokens article](https://paragonie.com/blog/2017/02/split-tokens-token-based-authentication-protocols-without-side-channels).

That’s why they’re called Split Tokens. You split them on the backend.

![](https://i0.wp.com/soatok.blog/wp-content/uploads/2020/09/soatoktelegrams2020-07.png?resize=512%2C512&ssl=1)(Art: [[CMYKat](https://cmykatgraphics.carrd.co/)](https://twitter.com/lynxvsjackalope))

Authentication protocols with a username and password, or some sort of ID and secret (e.g. AWS credentials), are naturally resistant to this class of vulnerability by virtue of never performing a search operation on a secret value.

Finally, if you work for a software company and have the budget for it, try to get multiple security reviews from experts with different specializations. 

My knowledge and experience with computer security is finite, and I’m not perfect. Other experts might find things I miss, and I might find things they miss. In this article, I discussed using a well-known cryptanalysis technique to bypass a security control in a web application that talks to a relational database. Most application security professionals that don’t specialize cryptography wouldn’t think to look for that.

Diversity is a great learning opportunity for us all, and the software we study will be all the safer for it.

## Disclosure Timeline

I have one request for anyone discussing this on the Internet: Please don’t thank me for practicing [“responsible” disclosure](https://adamcaudill.com/2015/11/19/responsible-disclosure-is-wrong/). The term “coordinated disclosure” is preferable.

  * **2021-07-04 ~ 8:15 PM:** Vulnerability discovered and reported via email with analysis and recommendations. It being a holiday in the USA, I don’t expect an immediate response.
  * **2021-07-05** **~ 9:30 AM:** Lobste.rs is patched to also apply rate-limiting [applied to password resets](https://github.com/lobsters/lobsters/commit/eaaa25b1afd385fb3b24762e9270412dff8d986a), instead of only login attempt. [Peter Harkins](https://twitter.com/pushcx) responds to my email saying he’ll try to have it fixed this week (pending family stuff due to the holiday and whatnot).
  * **2021-07-06:** I emailed Peter an example patch while acknowledging I am not a Ruby expert and therefore it’s probably terrible.
  * **2021-07-07:** I start drafting this blog post.
  * **2021-08-19:** Sent a follow-up email to Peter.
  * **2021-08-20:** Given no response to any email since 2021-07-06, this post is made public.

## TL;DR

Lobste.rs mitigated a timing attack I reported against their password reset mechanism that only the most motivated and spiteful attackers would have been able to use successfully. 

Then I wrote a lot of words to teach the community about timing attacks in practice. There are probably a lot of interesting websites that are susceptible to a similar issue, and some won’t even enforce a 24 hour window, thus making attacks even more practical.

  * Tags  [authentication](https://soatok.blog/tag/authentication/), [computer security](https://soatok.blog/tag/computer-security/), [cryptography](https://soatok.blog/tag/cryptography/), [Cybersecurity](https://soatok.blog/tag/cybersecurity/), [databases](https://soatok.blog/tag/databases/), [Lobste.rs](https://soatok.blog/tag/lobste-rs/), [password reset](https://soatok.blog/tag/password-reset/), [Ruby on Rails](https://soatok.blog/tag/ruby-on-rails/), [security](https://soatok.blog/tag/security/), [side-channels](https://soatok.blog/tag/side-channels/), [timing attacks](https://soatok.blog/tag/timing-attacks/), [vuln](https://soatok.blog/tag/vulnerability/)

![](https://secure.gravatar.com/avatar/62964206396b67fb3a8985b19dc274f74b1a9232374e189577c0f1388fdc73f2?s=160&d=identicon&r=g)

##  By Soatok 

Security engineer with a fursona. Ask me about dholes or Diffie-Hellman!

[ View Archive → ](https://soatok.blog/author/soatok/)

* * *

[ ← Safer Illinois, Isn’t ](https://soatok.blog/2021/08/17/safer-illinois-isnt/) [ → Programmers Don’t Understand Hash Functions ](https://soatok.blog/2021/08/24/programmers-dont-understand-hash-functions/)

* * *

##  3 replies on “Timing Attack on SQL Queries Through Lobste.rs Password Reset” 

![](https://secure.gravatar.com/avatar/2e1ae2892b07d7ecd6b608ffc3aee6d25274c74c00ab33cb39d31dad822304bb?s=120&d=identicon&r=g)Farthingiesays:

[August 20, 2021 at 4:33 pm](https://soatok.blog/2021/08/20/lobste-rs-password-reset-vulnerability/#comment-2381)

Great article, didn’t know things are that leaky even through SQL. As a quick patch, how horrible an idea would it be to add a random amount of microsleep on internet facing services like this? I gather the granularity of one µs may not be enough, and no one likes the idea of CPUs just sitting at idle, or worse, running at 100% while “asleep”…

[For Your Infurmation - Dhole Momentssays:](https://soatok.blog/2021/12/29/for-your-infurmation/)

[December 29, 2021 at 3:25 pm](https://soatok.blog/2021/08/20/lobste-rs-password-reset-vulnerability/#comment-3077)

[…] An interesting timing attack on SQL queries in Lobste.rs’ password reset feature […]

![](https://secure.gravatar.com/avatar/c8126fcd1fa5d487a382ec72a2a43396b06715c27820c0d26513241841314193?s=120&d=identicon&r=g)SisterMandersonsays:

[September 16, 2022 at 8:19 pm](https://soatok.blog/2021/08/20/lobste-rs-password-reset-vulnerability/#comment-3370)

Wow, thats heavy^~^ great post. Came here from google where i searched for information impact on weak cipher suits, stayed here cause of furry fandom and interesting stuff. UwU

* * *

Comments are closed.
