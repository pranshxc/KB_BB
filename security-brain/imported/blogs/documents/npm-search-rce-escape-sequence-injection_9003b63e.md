---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-14_npm-search-rce-escape-sequence-injection.md
original_filename: 2023-12-14_npm-search-rce-escape-sequence-injection.md
title: npm search RCE? - Escape Sequence Injection
category: documents
detected_topics:
- supply-chain
- command-injection
- automation-abuse
- api-security
- cloud-security
tags:
- imported
- documents
- supply-chain
- command-injection
- automation-abuse
- api-security
- cloud-security
language: en
raw_sha256: 9003b63e7635bd9fe0c162965ecf6e3580b2747386716d2265ccd3aa2c091439
text_sha256: 6f138c431ebfd5ec247948b4afe3ed0d48493b294f7b40c81fd64bd53454df20
ingested_at: '2026-06-28T07:32:28Z'
sensitivity: unknown
redactions_applied: false
---

# npm search RCE? - Escape Sequence Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-14_npm-search-rce-escape-sequence-injection.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, automation-abuse, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:28Z
- Redactions Applied: False
- Raw SHA256: `9003b63e7635bd9fe0c162965ecf6e3580b2747386716d2265ccd3aa2c091439`
- Text SHA256: `6f138c431ebfd5ec247948b4afe3ed0d48493b294f7b40c81fd64bd53454df20`


## Content

---
title: "npm search RCE? - Escape Sequence Injection"
page_title: "npm search RCE? - Escape Sequence Injection | solid-snail blog"
url: "https://blog.solidsnail.com/posts/npm-esc-seq"
final_url: "https://blog.solidsnail.com/posts/npm-esc-seq"
authors: ["solid-snail"]
programs: ["Radare2", "GitHub", "NPM CLI"]
bugs: ["RCE", "Escape sequence injection"]
publication_date: "2023-12-14"
added_date: "2024-07-15"
source: "pentester.land/writeups.json"
original_index: 625
---

# npm search RCE? - Escape Sequence Injection

Dec 14, 2023 

How many programmers does it take to filter out 36 characters? You may think this is an opening to a joke, but it’s not.

> **update** (2024-02-05): a patch was released for npm in v10.3.0, addressing and fixing the vulnerability.

![snail-terminal](/assets/img/snail-terminal.png)

> **Note:** ‘code points’ would be a more accurate term than ‘characters’, but I’ll probably keep using ‘character’ for the rest of this post.

In [a previous post](/posts/2023-08-28-iterm2-rce) I went over a vulnerability I discovered in iTerm2 that allowed code execution in the shell by leveraging the output of a command. Today, We’ll focus on the other side of that interaction, the application running underneath the terminal.

I’ll touch on reports I’ve personally made on this issue (Radare2, Github CLI, npm cli),  
how to exploit it with or without a vulnerability in the terminal itself,  
what challenges drove developers to fumble this seemingly trivial task,  
and my recommendations regarding mitigation.

> Also, someone brought to my attention that there’s a pretty good [Defcon video](https://www.youtube.com/watch?v=Y4A7KMQEmfo) (and [write-up](https://dgl.cx/2023/09/ansi-terminal-security)) on similar vulnerabilities. Would recommend.

## Brief on Escape Sequences

_Feel free to skip this section if you’re already familiar._

[Escape sequences](https://notes.burke.libbey.me/ansi-escape-codes/), sometimes also called control sequences, are the way terminal emulators and the application running beneath them communicate with each other. That is how colored output, loading bars, and mouse control are implemented. The important thing to remember is that they are embedded in the standard output and input.

I’ll give some examples:
  
  
  printf '\x1b[32mThis text will be green'
  printf 'This will create a scroll region: \x1b[3;5r - try pressing Enter a bunch of times'
  printf 'This will type for you: \x1b]4;0;?\x1b\\'
  

`\x1b` is the Escape character. And yes, it does refer to the Esc key on your keyboard. In a terminal, try pressing Esc, releasing it, and then pressing P. It will behave the same as Alt+p.

There are other characters that can initiate a sequence called C1 controls. I won’t get too much into it, but for example U+009B (`\u009b`) can replace `\x1b[`.

The last example demonstrates what happens when a response is left in stdin. It is picked up by the shell as input. In my [iTerm2 post](/posts/2023-08-28-iterm2-rce) I used a response that includes a newline to automatically execute a command. The interesting thing about it is that nothing in the standards dictates that terminal emulators should not do that. It can be argued that it is up to the application to not send unauthorized queries, but most terminals avoid it regardless because it is bound to be abused.

## Radare2

[CVE-2023-0302](https://nvd.nist.gov/vuln/detail/CVE-2023-0302)

Lets forget for a moment about vulnerabilities in the terminal itself. What can we do with the _“normal”_ stuff?

  * Change color of text and background.
  * Set text as bold, italic, underlined…
  * Make the cursor invisible.
  * Set the location of the cursor.
  * Set a scroll region.
  * Manipulating window properties - setting window title, icon, size and location (not all terminals implement all of these features).
  * Disable line overflow.

All of the above and more allow you to manipulate elements of the UI.

Additionally, all terminals push responses to queries to stdin. So even if an attacker couldn’t execute a command automatically, they could do something like manipulating the UI to show something like a disclaimer, asking the user to press Enter for confirmation. Unbeknownst to the user, a shell command printed outside the boundaries of the screen would be executed.

The vulnerability in [Radare2](https://github.com/radareorg/radare2) linked above, allowed escape sequences embedded in the debug info (DWARF section) of an ELF to be printed to the terminal.

The most straight forward use case for an attacker would be obfuscation during malware analysis. Manipulating the data displayed by Radare2.

The [original patch](https://github.com/radareorg/radare2/commit/961f0e723903011d4f54c2396e44efa91fcc74ce) used the following to sanitize inputs:
  
  
  static size_t __str_ansi_length(char const *str) {
  size_t i = 1;
  if (str[0] == 0x1b) {
  if (str[1] == '[') {
  i++;
  while (str[i] && str[i] != 'J' && str[i] != 'm' && str[i] != 'H' && str[i] != 'K') {
  i++;
  }
  } else if (str[1] == '#') {
  while (str[i] && str[i] != 'q') {
  i++;
  }
  }
  if (str[i]) {
  i++;
  }
  }
  return i;
  }
  
  R_API size_t r_str_ansi_strip(char *str) {
  size_t i = 0;
  while (str[i]) {
  size_t chlen = __str_ansi_length (str + i);
  if (chlen > 1) {
  r_str_cpy (str + i, str + i + chlen);
  } else {
  i++;
  }
  }
  return i;
  }
  

There are some issues there.

As far as I can tell, the function `__str_ansi_length` was originally utilized elsewhere for calculating the length of the string in its printed form, not sanitization. It therefore misses some cases that could be abused. It also fails to sanitize an ESC character in the last byte, allowing an attacker to bypass it by splitting the rest of the sequence to a consecutive print.

To be fair, I approved it before it was released…

After noticing those flaws while writing this, I submitted [a PR to address them](https://github.com/radareorg/radare2/pull/22385):
  
  
  static size_t __str_ansi_sanitize_length(char const *str) {
  size_t i = 0;
  if (str[0] == 0x1b || str[0] == 0x07 || str[0] == 0x05 || str[0] == 0x7f) { // ESC, BEL, ENQ, DEL
  i++;
  } else if (str[0] == -0x3e && str[1] >= -0x80 && str[1] <= -0x61) { // C1 control codes U+0080 - U+009F
  i += 2;
  }
  return i;
  }
  
  R_API size_t r_str_ansi_strip(char *str) {
  size_t i = 0;
  while (str[i]) {
  size_t chlen = __str_ansi_length (str + i);
  size_t sanitize_len = __str_ansi_sanitize_length (str + i);
  if (chlen > 1) {
  r_str_cpy (str + i, str + i + chlen);
  } else if (sanitize_len > 0) {
  r_str_cpy (str + i, str + i + sanitize_len);
  } else {
  i++;
  }
  }
  return i;
  }
  

It was quickly approved and merged.

BTW, [Radare2](https://github.com/radareorg/radare2)’s maintainer is doing a tremendous job. If you see value in the project I’d urge you to contribute either [time](https://github.com/radareorg/radare2/blob/master/CONTRIBUTING.md) or [money](https://opencollective.com/radareorg).

## Github CLI

The case of gh cli is quite interesting. It was the first time I managed to demonstrate RCE using this injection method, and the way the devs chose to fix it was a bit… ehm, peculiar.

To achieve RCE I utilized a specific feature of a terminal named iTerm2 that responded to a query with a newline. That response is pushed to stdin by the terminal. Since gh cli doesn’t pull data from stdin normally, it was left there for the shell. The shell interpreted the newline as the user pressing Enter. That allowed me to run an executable in a specific path. You can read more about it in my [previous post](/posts/2023-08-28-iterm2-rce).

There are plenty of ways to get gh cli to print user generated content. Issues, PR requests and more. At the time none of it was sanitized. The executable would theoretically be in a repo that the user cloned themselves.

It was one of the first times I reported to a bug bounty program. After overcoming the challenge of my own clumsy reporting and Github’s team managing to reproduce the bug (sneaky `$PAGER` trying to undermine my PoC!), it was accepted and they started working on a fix.

And the fix is…  
_Drumroll_  
Sanitizing serialized JSON (pre-parsed) of HTTP responses!  
Uhm  
.  
.  
.  
Wha-?

<https://github.com/cli/cli/releases/tag/v2.23.0>

The good is that they did try to address C1 controls to avoid a bypass.

The bad is that they failed to handle non-HTTP responses, and forgot the JSON specification doesn’t require control characters above the ASCII range to be escaped. For example U+009B doesn’t have to appear as `\u009b` in the raw JSON, even if it isn’t visible by itself.

The ugly is that they didn’t properly handle preceding backslashes, resulting in a DoS bug, and then mishandled preceding backslash _again_ , resulting in another bypass.

So why such a weird solution?

My best guess is that they wanted to hook into a bottleneck in the process. The point of printing wouldn’t work since that would include legitimate escape sequences, so they went with the opposite end of the of the process.

If I were to go with that approach, I’d try to hook into a point after the JSON is parsed. Perhaps wrap/override the default `Decoder` or `Unmarshaler`, and sanitize the relevant characters from the resulting string fields. _But_ , I didn’t explore that option in-depth, so they might have had a good reason not to.

To achieve RCE, you would have needed to utilize one of the two exploits I presented in my [iTerm2 post](/posts/2023-08-28-iterm2-rce). Particularly the one related to the `RequestUpload` feature, since you’ll be able to deliver an executable through a cloned repo.

![sassy branch name](/assets/img/gh-cli-sassy-branch-name.png)

Don’t get sassy with me [@samcoe](https://github.com/samcoe). It ends when it ends.

## NPM CLI

For the npm cli report I managed to come up with an exploit that didn’t require an executable. It involved a command named `m4`. Again, you can read about it in my [previous post](/posts/2023-08-28-iterm2-rce).

So, npm devs [released a fix](https://github.com/npm/cli/releases/tag/v9.7.0).  
They used an already existing regex pattern `ansiTrim`.
  
  
  function ansiTrim (str) {
  var r = new RegExp('\x1b(?:\\[(?:\\d+[ABCDEFGJKSTm]|\\d+;\\d+[Hfm]|' +
  '\\d+;\\d+;\\d+m|6n|s|u|\\?25[lh])|\\w)', 'g')
  return str.replace(r, '')
  }
  

From doing a bit of research into the code and git logs, it seems like its original purpose was to evaluate the length of a string in its printed form. Rings a bell?

It was completely bypass-able, since it wasn’t designed for that purpose.

After reporting a bypass they eventually released [another fix](https://github.com/npm/cli/releases/tag/v10.2.0). This time they used a package named [strip-ansi](https://www.npmjs.com/package/strip-ansi). It was still bypass-able. The package basically took the same approach of removing whole sequences using a pattern. There were some other issues like ignoring most C1 controls, or applying it only to `npm search` and not other commands, amongst other issues I already pointed out in the report.

I-It’s not like I want Github to fix their vulnerabilities, so DON’T GET THE WRONG IDEA! I just wanted the Hackerone badges, that’s all. Who would even want comprehension of their work by fellow professionals?  
_Baka!_

As it stands today, it is still mostly bypass-able.

This is the exploit I submitted to [Github’s BBP](https://hackerone.com/github?type=team):
  
  
  mkdir somepkg
  cd somepkg
  echo -E '{ "publishConfig": { "registry": "http://localhost:4873" }, "description": "somepkg1$ qrefresh-client", "keywords": ["syscmd(open -a Calculator)\u001b[5n\u001bP$q$|\u001b\\\u001b[#|\u001b[14H\u001b[6n\u001bP1000p%session-changed $9 s\n"] }' > package.json
  npm init -y
  npm publish
  
  # this should trigger the PoC, doesn't require to be run from this specific directory
  npm search somepkg
  

For an explanation on how it works, see my [post about it](/posts/2023-08-28-iterm2-rce).

Keep in mind that the current version of iTerm2 is patched against this. So for testing it the relevant version of iTerm2 is needed, or a different exploitation technique. I also used verdaccio as npm’s backend, but it _shouldn’t_ make a difference.

## Mitigation

You take your data at some point before constructing the output, and filter out the following characters:
  
  
  \u0007
  \u001b
  \u0080 - \u009f
  

And for good measure these as well:
  
  
  \u0005
  \u007f
  

It will leave behind artifacts from the now ineffective sequence. If you believe it’s a good idea to parse out those sequences, keep in mind that it isn’t as trivial as you might think, and that even terminals aren’t consistent about parsing in some cases. You will probably end up with a parser differential _somewhere_.

That’s it.  
It is as simple as that.  
Why most devs avoid it, is beyond me.

The npm devs’ choice to continue the [left-pad](https://left-pad.io/) legacy by using an external package, without fully understanding what it does, is especially disappointing.

If you ignore the common denominator to all these events, me being the reporter (as you should!), then you can safely conclude that there is an over-arching issue with the way we develop software.

[](/posts/npm-esc-seq)
