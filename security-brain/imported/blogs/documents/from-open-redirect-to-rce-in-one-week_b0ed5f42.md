---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-31_from-open-redirect-to-rce-in-one-week.md
original_filename: 2022-05-31_from-open-redirect-to-rce-in-one-week.md
title: From open redirect to RCE in one week
category: documents
detected_topics:
- command-injection
- path-traversal
- supply-chain
- idor
- ssrf
- xss
tags:
- imported
- documents
- command-injection
- path-traversal
- supply-chain
- idor
- ssrf
- xss
language: en
raw_sha256: b0ed5f42e97726355a88c1bc54ab310fa0e39fc973c3a0993e3d0ea8cc3ebdb2
text_sha256: 070a600849c0447804b6fada49cc5c7c4bf40de38be326d17a72c9d47dcab256
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# From open redirect to RCE in one week

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-31_from-open-redirect-to-rce-in-one-week.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, supply-chain, idor, ssrf, xss
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `b0ed5f42e97726355a88c1bc54ab310fa0e39fc973c3a0993e3d0ea8cc3ebdb2`
- Text SHA256: `070a600849c0447804b6fada49cc5c7c4bf40de38be326d17a72c9d47dcab256`


## Content

---
title: "From open redirect to RCE in one week"
url: "https://medium.com/@byq/from-open-redirect-to-rce-in-one-week-66a7f73fd082"
authors: ["byq (@ByQwert)"]
programs: ["Mail.ru"]
bugs: ["Open redirect", "SSRF", "Insecure deserialization", "LFI", "RCE"]
publication_date: "2022-05-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2593
scraped_via: "browseros"
---

# From open redirect to RCE in one week

Top highlight

From open redirect to RCE in one week
byq
Follow
20 min read
·
May 31, 2022

1.2K

8

In this article, I will tell you a story of how I chained multiple security issues to achieve RCE on several hosts of the Mail.Ru Group (or VK now). For me, as a regular reader of bug bounty write-ups, it is always interesting to learn the train of hunter’s thoughts during uncommon vulnerability exploitation, so I tried to describe my process as detailed as possible. I hope, you will enjoy it.

Intro

I am a huge fan of the Mail.Ru Group bug bounty program on HackerOne. VK, which is a new name of Mail.Ru group, sometimes buys new companies, and the VK BBP is replenished with new assets, which gives a nice chance for the hackers to loot low-hanging fruits.

Based on my experience I can say that it can be very profitable to access something, which no one before you tried to hack. I subscribed to VK BBP to receive updates about new assets to be among the first who will get access to them.

During 2021 I was not very active at BB and didn’t closely follow updates in my favorite BBP and that is the reason why I missed the notification that Seedr, which is a platform for video advertising, however now deprecated, was added to the assets.

My first meeting with Seedr happened in October 2021. Almost after a few minutes, I found several simple XSS, which I decided not to report because the chance of Duplicate was too high.

Presently you can observe several disclosed reports by other hunters and check how atypical bugs for modern applications were found there:

RCE в .api/nr/report/{id}/download
SSRF + RCE через fastCGI в POST /api/nr/video
XSS Stored on https://seedr.ru
OS command injection on seedr.ru

I thought that my train was gone, so I didn’t spend a lot of time on Seedr and continued my BB procrastination.

Functionality that caught my attention

I returned to Seedr during my December vacation in another country, where I was just with a backpack and laptop. After some time in such conditions BB hunger wakes up and there is a desire to find something interesting. To boost my confidence I usually take a fresh look at already familiar assets.

This time I spent more time on the recon: subdomain enumeration, port scanning, directory brute forcing, and so on. Luckily I found juicier things: GitLab, Grafana, several API hosts, cron files in the web directory, stack traces, and more. The more entry points you find — the higher chance to find something spicy. Unfortunately for me, none were worth reporting to BBP, but one functionality caught my attention.

In the HTML source code of the https://api-stage.seedr.ru/player page, I noticed the following comment:

Press enter or click to view image in full size
https://player.seedr.ru/video?vid=cpapXGq50UY&post_id=57b6ceef64225d5b0f8b456c&config=https%3A%2F%2Fseedr.com%2Fconfig%2F57975d1b64225d607e8b456e.json&hosting=youtube

I bet that you already want to modify the config GET parameter with your host to receive incoming HTTP connection, which I did. After several attempts, I didn’t receive any connections and continued to play with other parameters.

When I opened https://player.seedr.ru/video?vid=cpapXGq50UY&post_id=57b6ceef64225d5b0f8b456c&config=https%3A%2F%2Fseedr.com%2Fconfig%2F57975d1b64225d607e8b456e.json&hosting=youtube in browser and observed response I noticed that Open Graph meta tags filled with some information about video like title, description, image, etc.:

Press enter or click to view image in full size

After some tests, I understood that post_id and config GET parameters have no significant effect on the response, so let’s simplify the URL to https://player.seedr.ru/video?vid=cpapXGq50UY&hosting=youtube.

I assumed that it’s unlikely that the player only supports YouTube and changed hosting GET parameter to coub and vimeo:

Press enter or click to view image in full size
Press enter or click to view image in full size

So, it seems like depending on the value of hosting GET parameter server performs an HTTP request with file_get_contents() to YouTube, Vimeo, or Coub API, downloads metadata about the video (vid GET parameter), parses it, and returns the player HTML page with this video and filled Open Graph meta tags.

vid GET parameter is an injection point, it’s possible to control the last part of the path in file_get_contents(). I could use path traversal (/../) and useful symbols (?, #, @) as well.

What is more interesting, in the case of Vimeo server makes a request to http://vimeo.com/api/v2/video/VID.php, you could notice it on the previous screenshot and it turned out that, when you use .php extension in the path, Vimeo returns not a JSON string, but serialized string!

I assumed that after file_get_contents() the server uses unserialize() on the response from Vimeo:

Press enter or click to view image in full size

Wow, do I have unsafe deserialization here? It’s safe, as long as the response is under Vimeo’s control.

Possible scenarios

At that point I already saw three possible scenarios:

Fuzzing of file_get_contents() to escape vimeo.com host, achieve blind SSRF and probably unsafe deserialization;
Find controlled response on vimeo.com -> probably unsafe deserialization;
Find open redirect on vimeo.com -> blind SSRF -> probably unsafe deserialization.

After hours of different modifications of the vid GET parameter and the fuzzing of file_get_contents() locally, I didn’t find anything useful and decided to share all information about this finding with several trusted mates.

Ok, the first scenario didn’t work, let’s move to the next one with a controlled response on vimeo.com.

Endpoint with the controlled response should meet the following requirements:

200 OK HTTP status code;
Available for an unauthenticated user;
Controlled string should be at the beginning of the response body (PHP will successfully parse something like this {VALID_SER_STRING}TRASH);
Controlled string should support { }, " symbols required for storing serialized objects.

Here are some of my attempts to find desired behavior on vimeo.com:

injection is not a valid method.
Cons: 404 Not Found HTTP status code, doesn’t support {}, " symbols.
Press enter or click to view image in full size

2. injection is not a valid format.
Cons: 404 Not Found HTTP status code, doesn’t support {}, " symbols.

Press enter or click to view image in full size

3. JS callback.
Cons: /**/ at the beginning, doesn’t support {}, " symbols.

Press enter or click to view image in full size

4. Export of chat of live broadcast:
Cons: Date and name at the beginning, require authentication.

Press enter or click to view image in full size

Unfortunately, the second scenario also didn’t work, so my last hope was to find an open redirect on vimeo.com. Previously I already saw a disclosed report on HackerOne from 2015 with an open redirect on vimeo.com: https://hackerone.com/reports/44157, so I assumed that there was some chance to find one more. Actually, I already looked for an open redirect during the discovery of controlled response but didn’t find anything useful.

Open redirect

All that time when I tried to exploit this vulnerability I kept in mind the article from Harsh Jaiswal (@rootxharsh) about SSRF on vimeo.com. I distinctly remember that he chained several open redirects on vimeo.com to achieve the goal. This finding was in 2019, almost 3 years ago, so of course, at first, I thought that these open redirects were fixed. But it was probably my last chance, so I started digging in that way.

Thanks to low censoring of the screenshots it was possible to fingerprint the endpoint by GET parameters. Combining this, some googling, and reading Vimeo API docs I was able to guess what endpoint was used by Harsh in his chain. Anyway, it was still unclear what values I should provide.

Press enter or click to view image in full size
Screenshot from Harsh’s article

I very rarely ask someone for help while exploiting something, not counting several mates, but because I was at an impasse, Harsh was my last key.

After I contacted him and provided him with information that I had on that step, he shared with me a working open redirect link which was the same as I assumed but with proper values of GET parameters. From that link, I understood that it’s not a security issue on vimeo.com, but just a feature (really, it’s not a joke).

Press enter or click to view image in full size

Ok, now I have a working open redirect on vimeo.com, let’s try it at work:

Press enter or click to view image in full size
Press enter or click to view image in full size

Yes, I finally got an HTTP hit on my host. Before jumping to deserialization I decided to play a little with SSRF:

https://127.0.0.1
Press enter or click to view image in full size
https://127.0.0.1:22
Press enter or click to view image in full size
http://127.0.0.1:25
Press enter or click to view image in full size

Because the response from file_get_contents() goes directly to unserialize() I couldn’t achieve full SSRF, but at least I already had semi-blind SSRF with ability to perform the port scan:

After understanding that I used almost the whole potential of this SSRF I switched to the exploitation of unserialize().

Deserialization

Briefly, what is needed for successful exploitation of unsafe deserialization in PHP?

̶C̶o̶n̶t̶r̶o̶l̶l̶e̶d̶ ̶i̶n̶p̶u̶t̶;̶
Class with magical method (__wakeup(), __destroy(), __toString(), etc.);
Useful for attacker functionality in magical method which can be abused for file manipulation, RCE, SQLi, etc.;
Class is loaded.

As you can see, at that point I had only 1 of 4 requirements. I didn’t know anything about backend code on the host, so the only way to exploit deserialization is to blindly try all known gadget chains. For that purpose, I used the awesome tool PHPGGC which is a library of PHP unserialize() payloads along with a tool to generate them. At the moment of exploitation, it has almost 90 available payloads. A big part of them is for different CMS and frameworks like WordPress, ThinkPHP, Typo3, Magento, Laravr, etc., which would be useless in my case. So I betted on commonly used libraries like Doctrine, Guzzle, Monolog and Swift Mailer.

I pre-generated all available payloads with PHPGGC, hosted them on a controlled server, and started brute-forcing. And… in all of the cases, I got the same error:

Press enter or click to view image in full size

The error occurs because inside serialized string there is a reference to a class that hasn’t been included yet — so the PHP autoloading mechanism is triggered to load that class, and this fails for some reason. © Sven

At that point I have come to terms with the fact that this PHP script is very primitive and doesn’t include any additional classes, which I can use. Sad, but at least I tried. It often happens when you chain cool vulnerability, but face something that completely blocks you.

After summarizing all the findings I went to HackerOne and submitted a report with the name [player.seedr.ru] Semi-blind SSRF and for sure invited Harsh Jaiswal as a collaborator for his open redirect on vimeo.com.

Basically, this is where the story could have ended. But there was a feeling inside that kept me up at night telling me that it was not over yet and I should try something else. I guess you know how it feels.

Kohana

I don’t remember where exactly but a few days later by chance, my eye caught on something about use-after-free vulnerability in PHP unserialize(). As it happened the version of PHP on player.seedr.ru was outdated and of course, I started “researching” this area. During that “research” I got acquainted with the reports of Taoguang Chen who reported to PHP may be dozens of issues with unserialize(). Actually, vulnerabilities related to memory are still a dark area for me, but honestly, I tried to build some payloads. After some poking on the local environment, I returned to player.seedr.ru, hosted the payload on a controlled server, sent a request, and …

Press enter or click to view image in full size

“What? No space left on the device? Really, I just started? But, wait, this doesn’t look like a default error about space on the device.”

By the way, this error occurred probably because I sent too many requests with scanners for hidden directories and files on previous days.

ErrorException [ 2 ]: file_put_contents(/var/www/seedr.backend.v2/application/logs/2021/12/20.php): failed to open stream: No space left on device ~ SYSPATH/classes/kohana/log/file.php [ 81 ]

“Custom class for logging? Seems like this “primitive” PHP script nevertheless loads logging class, interesting. Kohana? I already saw this word during security testing of Seedr. But where?”

Thanks to Burp Suite Professional I quickly found the first mention of Kohana in Proxy history, opened that page, and observed a detailed error page.

Vanilla Burp Suite Community can’t do this
Press enter or click to view image in full size
Paradise for security tester

Here I will make a small digression to give you some information about Seedr and where v2.nativeroll.tv came from. I should note that I may be wrong but here are my thoughts I had at that moment.

Seedr and Nativeroll are both platforms for Video advertising. Seedr had an old fashioned design, so I guess that it was created long before Nativeroll. Both platforms were bought by Mail.Ru Group, probably somehow merged and listed on HackerOne at the same scope. So, v2.nativeroll.tv/api/, api.seedr.ru, api-stage.seedr.ru, player.seedr.ru shared the same code base. Hope now it’s more clear.

Ok, let’s return to the beautiful error page. Environment, Included files, Loaded extensions — looks juicy. Here is what I observed after clicked on Included files link:

Press enter or click to view image in full size

There were almost 90 included files, which in fact were different classes loaded with something like autoload.php. Is Kohana some sort of CMS or framework? Yes, it is. After some googling I found GitHub repository https://github.com/koseven/kohana/ which looks deprecated:

Press enter or click to view image in full size

Because v2.nativeroll.ru and api.seed.ru share the same code base, I successfully triggered Error exception on api.seedr.ru with the same payload (https://api.seedr.ru/<svg>) and got the same result.

For triggering Error exception exactly on api.seedr.ru/video (endpoint which I attacked), I took the result from http://vimeo.com/api/v2/video/123459.php and modified value of description attribute from string to array.

a:1:{i:0;a:23:{s:2:”id”;i:123456;s:5:”title”;s:30:”London Tornado — The aftermath”;s:11:”description”;a:1:{i:0;i:1337;}s:3:”url”;s:24:”https://vimeo.com/123456";s:11:"upload_date";s:19:"2006-12-14 06:53:32";s:15:”thumbnail_small”;s:111:”https://i.vimeocdn.com/video/46783763-254c2bbf4211bd6657c59e96a682169c8e74fc56e96ebb4e0a2882b103cab878-d_100x75";s:16:"thumbnail_medium";s:112:"https://i.vimeocdn.com/video/46783763-254c2bbf4211bd6657c59e96a682169c8e74fc56e96ebb4e0a2882b103cab878-d_200x150";s:15:"thumbnail_large";s:108:"https://i.vimeocdn.com/video/46783763-254c2bbf4211bd6657c59e96a682169c8e74fc56e96ebb4e0a2882b103cab878-d_640";s:7:"user_id";i:146861;s:9:"user_name";s:11:"wordtracker";s:8:"user_url";s:29:"https://vimeo.com/wordtracker";s:19:"user_portrait_small";s:51:"https://i.vimeocdn.com/portrait/defaults-blue_30x30";s:20:"user_portrait_medium";s:51:"https://i.vimeocdn.com/portrait/defaults-blue_75x75";s:19:"user_portrait_large";s:53:"https://i.vimeocdn.com/portrait/defaults-blue_100x100";s:18:"user_portrait_huge";s:53:"https://i.vimeocdn.com/portrait/defaults-blue_300x300";s:21:"stats_number_of_likes";i:11;s:21:"stats_number_of_plays";i:122560;s:24:"stats_number_of_comments";i:12;s:8:"duration";i:32;s:5:"width";i:320;s:6:"height";i:240;s:4:"tags";s:0:"";s:13:"embed_privacy";s:8:"anywhere";}}

During script execution the htmlspecialchars() function expected a string, but got an array, which caused an Error exception with partly disclosed template and stack trace:

Press enter or click to view image in full size
Press enter or click to view image in full size

There was a composer autoload script, as I thought. Among these included files I highlighted several, which can be useful during deserialization:

Guzzle (/var/www/sentry/vendor/guzzlehttp/…)
Swift Mailer (MODPATH/email/vendor/swiftmailer/…)
Symfony (/var/www/sentry/vendor/symfony/…)
Mustache (MODPATH/kostache/vendor/mustache/…)
Sentry (/var/www/sentry/vendor/sentry/…)

I knew that PHPGGC has some gadget chains for Guzzle, Swift Mailer and Symfony. After I built and tested the payloads on api-stage.seedr.ru I got new error. For example, an attempt with Guzzle payload returned the following error: FnStream should never be unserialized. Which indicated that the script used an already patched version:

Press enter or click to view image in full size

Swift Mailer and Symfony didn’t work at all and analysis of Mustache and Sentry code on Github also didn’t bear any fruit, so third-party libraries wouldn’t help me. It was time to dive into Kohana.

Get byq’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Search for magical methods, like __wakeup(), __destruct(), __toString(), in Kohana repository was empty:

Press enter or click to view image in full size

But this Kohana repository has a system directory which in fact is a dedicated repository Kohana Core:

Press enter or click to view image in full size
Press enter or click to view image in full size

Let’s try to search for magical methods in this repository. There were almost no results for __destruct(), __wakeup(), but results for __toString() were reassuring:

Press enter or click to view image in full size

I briefly overlooked the findings, but classes/Kohana/View.php and its render() function immediately caught my attention.

I should say I have some experience with backend development in the past, especially with PHP. I developed a few projects with Laravel and already knew about its MVC (Model-View-Controller) pattern. For rendering of Views Laravel uses an engine called Blade. Because such rendering engines usually load some templates (files) for rendering, I guessed that maybe somehow I can pass to function my own file or my own content.

Let’s take a look at the render() function closely. Function render() accepts 1 argument called $file and then calls function capture():

public function render($file = NULL)
{
  if ($file !== NULL)
  {
  $this->set_filename($file);
  }
  if (empty($this->_file))
  {
  throw new View_Exception('You must set the file to use within your view before rendering');
  }
  // Combine local and global data and capture the output
  return View::capture($this->_file, $this->_data);
}

In my case function render() calls without argument and let me bypass set_filename() function which also checks existence of the $file in the views directory:

public function set_filename($file)
{
  if (($path = Kohana::find_file(‘views’, $file)) === FALSE)
  {
  throw new View_Exception(‘The requested view :file could not be found’, array(‘:file’ => $file,));
 }
  // Store the file path locally
  $this->_file = $path;
  return $this;
}

Thus I call capture() function with $this->_file variable:

public function render($file = NULL)
{
  ...
  // Combine local and global data and capture the output
  return View::capture($this->_file, $this->_data);
}

As it says in the comment capture() function combines local and global data and captures the output. For example, you can render a template file for email and use username as a variable there.

protected static function capture($kohana_view_filename, array $kohana_view_data)
{
  // Import the view variables to local namespace
  extract($kohana_view_data, EXTR_SKIP);
  if (View::$_global_data)
  {
  // Import the global view variables to local namespace
  extract(View::$_global_data, EXTR_SKIP | EXTR_REFS);
  }
  // Capture the view output
  ob_start();
  try
  {
  // Load the view within the current scope
  include $kohana_view_filename;
  }
  catch (Exception $e)
  {
  // Delete the output buffer
  ob_end_clean();
  // Re-throw the exception
  throw $e;
  }
  // Get the captured output and close the buffer
  return ob_get_clean();
}

capture() function accepts 2 arguments: $kohana_view_filename and $kohana_view_data. Some of you probably already spotted the function that potentially can be abused during deserialization:

...
try
{
  // Load the view within the current scope
  include $kohana_view_filename;
}
...

include()! It already smells like LFI and RCE. But do I have control over $kohana_view_filename?

Yes, I do! Because $kohana_view_filename is $this->_file in my context and _file is an attribute of View class.

class Kohana_View {
  // Array of global variables protected static 
  $_global_data = array();
  ...
  // View filename 
  protected $_file;  
  // Array of local variables 
  protected $_data = array();
  ...
}

At that moment I had all the elements for successful unsafe deserialization:

I controlled the input;
I had a magical method __toString() of View class with a useful function include().
The class View was loaded.

Bingo!

Chaining all together

After some time I created gadget and chain for PHPGGC locally, which later were committed and added to main repository:

<?php
namespace GadgetChain\Kohana;
class FR1 extends \PHPGGC\GadgetChain\FileRead
{
  public static $version = ‘3.*’;
  public static $vector = ‘__toString’;
  public static $author = ‘byq’;
  public static $information = ‘include()’;
  public function generate(array $parameters)
  {
  return new \View($parameters[‘remote_path’]);
  }
}
<?php
class View 
{
  protected $_file;
  public function __construct($_file) {
  $this->_file = $_file;
  }
}

Then I just ran PHPGGC and got following serialized object:

Hosted payload on a controlled server, sent a request and …

Press enter or click to view image in full size

Oookey, at least it was something new. But what I was hoping for? I used not __wakeup() or __destruct() methods which trigger at the moment of Object creation and destruction respectively, I used __toString(). As per PHP docs:

The __toString() method allows a class to decide how it will react when it is treated like a string. For example, what echo $obj; will print.

So I somehow should output my View object. Actually it wasn’t difficult to understand that I should provide my View object as a value of title or description attribute, the trick which I made before with an array to trigger an Error exception. Here is what my payload looked like:

a:1:{i:0;a:23:{s:2:”id”;i:123456;s:5:”title”;s:30:”London Tornado — The aftermath”;s:11:”description”;O:4:”View”:1:{s:8:”*_file”;s:11:”/etc/passwd”;}s:3:”url”;s:24:”https://vimeo.com/123456";s:11:"upload_date";s:19:"2006-12-14 06:53:32";s:15:”thumbnail_small”;s:111:”https://i.vimeocdn.com/video/46783763-254c2bbf4211bd6657c59e96a682169c8e74fc56e96ebb4e0a2882b103cab878-d_100x75";s:16:"thumbnail_medium";s:112:"https://i.vimeocdn.com/video/46783763-254c2bbf4211bd6657c59e96a682169c8e74fc56e96ebb4e0a2882b103cab878-d_200x150";s:15:"thumbnail_large";s:108:"https://i.vimeocdn.com/video/46783763-254c2bbf4211bd6657c59e96a682169c8e74fc56e96ebb4e0a2882b103cab878-d_640";s:7:"user_id";i:146861;s:9:"user_name";s:11:"wordtracker";s:8:"user_url";s:29:"https://vimeo.com/wordtracker";s:19:"user_portrait_small";s:51:"https://i.vimeocdn.com/portrait/defaults-blue_30x30";s:20:"user_portrait_medium";s:51:"https://i.vimeocdn.com/portrait/defaults-blue_75x75";s:19:"user_portrait_large";s:53:"https://i.vimeocdn.com/portrait/defaults-blue_100x100";s:18:"user_portrait_huge";s:53:"https://i.vimeocdn.com/portrait/defaults-blue_300x300";s:21:"stats_number_of_likes";i:11;s:21:"stats_number_of_plays";i:122560;s:24:"stats_number_of_comments";i:12;s:8:"duration";i:32;s:5:"width";i:320;s:6:"height";i:240;s:4:"tags";s:0:"";s:13:"embed_privacy";s:8:"anywhere";}}

Once again I updated payload on controlled server, sent request and finally:

Press enter or click to view image in full size

I got the content of /etc/passwd inside og:description meta tag. Awesome, local file read is better than semi-blind SSRF, but it’s still not a RCE.

Logs

Local file inclusion is such a rare gem in modern web applications that I had to remember where I can store my RCE payload to include() it later. The most common techniques are:

file upload (in my case application didn’t have such functionality);
logs (apache, nginx, mail, ssh, …);
Press enter or click to view image in full size
Press enter or click to view image in full size
/proc/*/fd, …;
Press enter or click to view image in full size
session file;
Press enter or click to view image in full size

As you can understand I tried almost everything and nothing worked.

It’s time to take a few steps back, namely to the error related to “no space left on device”:

Press enter or click to view image in full size

From that error, I could extract a path to some log file: /application/logs/2021/12/20.php. After I tried to open https://api.seedr.ru/application/logs/2021/12/20.php in the browser I got the following error: No direct script access. Actually, almost every PHP file in Kohana framework has such a string in the beginning:

Press enter or click to view image in full size

Seems like I can’t access log files with the .php extension directly from the browser. I gave a try at the staging host: http://api-stage.seedr.ru/application/logs/2021/12/20.php and to my surprise, I received a 404 HTTP status code. I don’t know what pushed me to do that, but I changed the .php extension to .log, and …

Press enter or click to view image in full size

Yes, I got the huge log file which even froze my Burp Suite a little. I should note that such a trick didn’t work on the production host api.seedr.ru. I can only guess that Seedr developers changed something on the staging environment to make accessing log files easier. But as usual, it led to a security issue.

One more time I opened a new door and started exploring it. Do you still remember how I triggered the Error exception the first time? Here is a record about it in the log file:

Press enter or click to view image in full size

After short analysis of log file I poisoned it with such a record:

Press enter or click to view image in full size

With PHPGGC I created a new serialized View object with _file attribute /var/www/t1.seedr.backend/application/logs/2021/12/20.log, hosted it on the controlled server, sent request and got following error:

Press enter or click to view image in full size

Seems like because the log file was too huge (>200000 lines), some function failed on one of the ? symbols, threw an exception and stopped the execution of the script. From PHP docs I learned that:

Press enter or click to view image in full size

Because the log file for December 20 was ruined with my unsuccessful payload, all other tests on that host were useless so I moved to the local environment. Hours of debugging and tests with include() and log file did not lead to the desired result.

During the morning shower, I remembered one more awesome article from Charlese Fol Laravel <= v8.4.2 debug mode: Remote code execution (CVE-2021–3129). It uses the technique with multiple base64 decoding feature which ignore not base64. Firstly, I read about it from Orange Tsai blog. My idea was to poison a log with multiple base64 encoded PHP payload, then decode it with multiple convert.base64-decode filters inside the include() function to bypass that exception with the ? symbol. But because it was a sleepless night my brain didn’t work well and I completely forgot that in the Laravel case it abused file_get_contents() and file_put_contents() functions chain with the same arguments inside it which allowed Charlese to rewrite log. I also forgot about this limitation:

Press enter or click to view image in full size
Screenshot from Charlese’s article

Because of the predictable log file path (/application/logs/2021/12/20.log) I downloaded a few log files for previous days and planned to poison the log for December 21 at the beginning of the day until it wasn’t too huge.

I posted all collected information to the H1 report and had a full day before December 21. Without wasting time I tried to exploit my finding on the production environment api.seedr.ru, because all my last tests were on api-stage.seedr.ru. One more time with the help of PHPGGC I created a View object with _file attribute /etc/passwd, hosted it on the controlled server and … I didn’t observe the content of the /etc/passwd file in the response. I repeated the same steps on api-stage.seedr.ru and all worked fine. “Oops, does it only work on a staging environment?”

Null bytes

Here I must confess that when I generated serialized object with PHPGGC I modified it a little:

Does the *_file string has really 8 symbols? No, it has only 6. That is what I modified every time and it worked flawlessly on api-stage.seedr.ru. Later in the stack trace, I noticed the following:

Value of protected _file attribute is NULL, but for some reason View object has public *_file attribute with my payload. Probably PHP experts already understood the reason for such behavior, but I had to spend some time dealing with this problem.

As you could notice from screenshots for storing payloads I used https://webhook.site/, it’s a fast and easy solution for receiving incoming HTTP connections and hosting the payloads. Unfortunately that time it played a bad joke on me. The thing is to store protected value in serialized string PHP use null characters (\0) around “*” symbol, that is why *_file has 8 symbols:

Because I just copy-pasted payload to webhook.site, it didn’t store these null characters and delivered to unserialize() public attribute *_file. To resolve such a problem I just hosted a serialized string with null bytes on my server. Now vimeo.com redirects requests to my server where I just echo() payload with null characters. After I was able to observe the content of /etc/passwd on api.seedr.ru I one more time returned to analyze downloaded log files.

Last poison

Log files had a lot of record types, but only a few could be used to store payload and most of them required authentication. Even during the first analysis of log files, I noticed the following record type:

Press enter or click to view image in full size

What was good about this record type, was that it stored payload only once per record and didn’t repeat it several times like my previous attempt. I also noted a possible injection point: user-agent. But the problem was that I didn’t know how to generate such a record in a log and what endpoint should I access. I “grepped” logs with my IP and discovered that today’s log file already has such a record with my IP, which meant that I definitely touched the required endpoint. By that time my Burp Proxy history had already more than 40000 records, so it was kind of difficult to find a proper endpoint. Comparing the time of the record with my IP and the activity that I performed at that time I understood that the record was probably generated during my scan with dirsearch. I rerun it and after some time the endpoint which generated such a record was found: api-stage.seedr.ru/inc.

On the local environment, I hid the new payload in a test log file, include() it, and got the output of the bash command. All that was left was to wait until December 21 and fresh log file, because on December 20 log files for api.seedr.ru and api-stage.seedr.ru were poisoned with my unsuccessful payloads.

The next day I poisoned the log with the following request:

Press enter or click to view image in full size

Generated the payload, hosted on the server, sent request …

Press enter or click to view image in full size

Yeap, I forgot to change $argv[1] to $_GET[1] after local tests… Looking forward to waiting one more day I remembered that for today I have one more attempt at api-stage.seedr.ru:

Press enter or click to view image in full size
This is how victory looks
TL;DR
Press enter or click to view image in full size
https://i.imgur.com/DrNEGRH.png without compression
Thanks to:
@rootxharsh for sharing open redirect;
@act1on3 and my personal PHP expert for being my rubber ducks.
References:

https://infosecwriteups.com/vimeo-ssrf-with-code-execution-potential-68c774ba7c1e

https://github.com/ambionics/phpggc

https://hackerone.com/ryat

https://www.ambionics.io/blog/laravel-debug-rce

http://blog.orange.tw/2018/10/
