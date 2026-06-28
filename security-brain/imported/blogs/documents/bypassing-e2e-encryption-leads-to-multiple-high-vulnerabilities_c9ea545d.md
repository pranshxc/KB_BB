---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-20_bypassing-e2e-encryption-leads-to-multiple-high-vulnerabilities.md
original_filename: 2023-01-20_bypassing-e2e-encryption-leads-to-multiple-high-vulnerabilities.md
title: Bypassing E2E encryption leads to multiple high vulnerabilities.
category: documents
detected_topics:
- idor
- ssrf
- command-injection
- cors
- api-security
- mobile-security
tags:
- imported
- documents
- idor
- ssrf
- command-injection
- cors
- api-security
- mobile-security
language: en
raw_sha256: c9ea545d3e184bafd29b473991db3a0dd4c20313ec2cdf068d548b7a9f2ca58f
text_sha256: ba2b34802bf83b5c81c7fd8a0bd2366809959bb2224ffe8c46946fc8db83b6fa
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Bypassing E2E encryption leads to multiple high vulnerabilities.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-20_bypassing-e2e-encryption-leads-to-multiple-high-vulnerabilities.md
- Source Type: markdown
- Detected Topics: idor, ssrf, command-injection, cors, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `c9ea545d3e184bafd29b473991db3a0dd4c20313ec2cdf068d548b7a9f2ca58f`
- Text SHA256: `ba2b34802bf83b5c81c7fd8a0bd2366809959bb2224ffe8c46946fc8db83b6fa`


## Content

---
title: "Bypassing E2E encryption leads to multiple high vulnerabilities."
url: "https://melotover.medium.com/bypassing-e2e-encryption-leads-to-multiple-high-vulnerabilities-65b708e5ad84"
authors: ["Asem Eleraky (@melotover)"]
bugs: ["IDOR", "SSRF"]
publication_date: "2023-01-20"
added_date: "2023-01-23"
source: "pentester.land/writeups.json"
original_index: 1644
scraped_via: "browseros"
---

# Bypassing E2E encryption leads to multiple high vulnerabilities.

1

·

Asem Eleraky
 highlighted

Bypassing E2E encryption leads to multiple high vulnerabilities.
Asem Eleraky
Follow
9 min read
·
Jan 21, 2023

811

10

In today’s blog, I’m going to show you how I was able to bypass the E2E encryption of an application by analyzing an obfuscated javascript file that was imported to that application, and how this helped me to better understand the internals of this application and get to find other multiple high vulnerabilities.

Exploration:

I started from the login panel, sending requests here and there to explore the application, I found that almost all requests were sent to an API, and their body was formed with some type of encryption as shown below:

Press enter or click to view image in full size

As you can see, I can’t find the real body that was sent to the API, can’t find any parameters, all were encrypted!

That is a type of E2E (End-2-End) encryption, where the communication between the client and the server is encrypted, this is an extra security layer to protect against any type of middle attacks.

All requests are initiated from our browser, right? so any kind of encryption or encoding that is performed on the request body would be done on the client side, so javascript files will be our target.

Javascript Files Analysis— First Round:

There was only one large js file imported to the whole application, it was obfuscated, minimized, and very messy.

Press enter or click to view image in full size
messy javascript file

To find something here is similar to digging for the needle in the haystack, but let’s give it a try!

If we look at what we have, we only have the JSON body that has these key/pairs v, iv, keys, and cipher. All these keys are changeable for every request except the v key, its value is still the same for every request, which is “pef2”.

Press enter or click to view image in full size

As this value is fixed (didn’t change in every request), so for sure it would be defined somewhere in the js file, if I found it, maybe it would lead us to the function that performs this encryption.

Press enter or click to view image in full size
searching in javascript to guide us to the function that encrypts the request body

As expected, it was mentioned just once, but I spent some time searching and debugging, following the initiators (it was more than 55 called functions), I figured out how a couple of functions work but it wasn't helpful to my goal (finding where the encryption/decryption is done).

I needed any word or function name to search for in this js file to speed up the reversing process, so I tried to find the old version of this file in the internet archive maybe it wasn’t obfuscated, but no luck.

Who else is using the same API?

The android application! I thought that I can decompile their android application and get its resources, and try to find if they are using the same encryption/decryption implementation or if this file is obfuscated or not! let’s try

Press enter or click to view image in full size
decompiling the APK

I decompiled the APK with apktool and then started to search for the same word -“pef2”- inside the whole application files.

Press enter or click to view image in full size

I found a new js file called “index.android.bundle” containing this word, after opening this file with a js-beautifier tool, and thankfully it was not obfuscated!

Press enter or click to view image in full size

As you can see, “pef2” is mentioned in line 106568, and this string is mentioned in a function called “encrypt”.

We can use some words mentioned in this function and search for them in the JS file on the web application, just to focus more on our main target which is the web application.

I searched for new words like getBytesSync, RSA-OAEP , and of course encrypt .

Back to the main goal — Second Round:

I opened the Sources window in dev tools and searched for getBytesSync and found some results, but because the file was minimized, I used the pretty print feature in the browser to make it more readable.

Press enter or click to view image in full size
making the code more readable

I ended up with a function called “encrypt” in line 137777, and as you can see above, this function takes 2 arguments, let’s add a breakpoint to pause the JS execution and inspect this function and check what is going on.

Press enter or click to view image in full size
Adding breakpoints

After initiating a random request to invoke the breakpoint, I found the following

Press enter or click to view image in full size
checking the DOM after invoking the breakpoint

One of the arguments of encrypt function is _0x3fc2ff, and its value as you can see in the Scope section is a JSON object, so let’s move to the console to fully understand its components.

As the breakpoint is on, we can print and perform actions while the application paused.

Analyzing the data passed to the “encrypt” function:
Press enter or click to view image in full size
original request body

A JSON object contains multiple keys/values that the API uses to handle the requests, so this is the original request body before any type of encryption.

The request is sent to /v1/user API endpoint with two parameters domain and user , and returns all information about this user as you can see below

Press enter or click to view image in full size
returned data from the request

As you may guess, we can test for IDOR in the user parameter, let’s change it to another username and check the response!

Press enter or click to view image in full size

and the result was promising!

Press enter or click to view image in full size
IDOR confirmed

Great! a valid IDOR vulnerability was confirmed, after digging more, I found multiple other IDORs that lead me to edit any user information like email and phone number, etc.

Get Asem Eleraky’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

What about the url parameter?

What came to my mind is to test for SSRF in the url parameter, so I changed its value to my burp collaborator to check if we can get an internal interaction.

{"url":"/v1/user","method":"get","headers":{"common":{"Accept":"application/json, text/plain, */*"},"delete":{},"get":{},"head":{},"post":{"Content-Type":"application/x-www-form-urlencoded"},"put":........}

Changed to:

{"url":"http://mycollab.burpcollaborator.net","method":"get","headers":{"common":{"Accept":"application/json, text/plain, */*"},"delete":{},"get":{},"head":{},"post":{"Content-Type":"application/x-www-form-urlencoded"},"put":........}
Press enter or click to view image in full size
SSRF confirmed

As you can see, I forward the request, then got an interaction!

What should I do if I couldn’t reach to the original JS file?

I used the above method to speed up the process of bypassing the encryption just by searching inside the js file with words that are already used in the original file, this method will not help you if you didn’t reach the original js file or any piece of code that can lead you the function that encrypts the request body.

Now let’s assume that there is no android application at all and no original js files, and we need to bypass it!

We can make use of the Event Listener Breakpoints tap in the browser’s dev tools which helps us to add breakpoints to pause the application when event listeners are hit/fired, we can select specific events, such as load, and error, etc.

The event that will be useful for us is click, so when we click on any button that initiates an API request the execution pauses, and the source panel displays the highlighted line of the JavaScript code that is next to be executed, along with the surrounding code for context. In addition, we have buttons to step over that line of code or resume execution.

Press enter or click to view image in full size
Setting up Event Listener Breakpoints

I selected click event and then I clicked a button that initiates an API request, the execution paused, and then I used the step-over buttons till I reach a function that takes the full request body!

Press enter or click to view image in full size

But as expected, it takes a bit of time to reach it.
Now again, I can edit the request before being encrypted.

This application is large, and editing every request with this method is a waste of time!

The application has many functions, and many API calls, which means I should intercept every request in the same way! it wastes the time, right?

So we need to find a method to be able to intercept the requests easily, (e.g. with burp suite), and to do so, we have two options:

Understand how the application encrypts the request body and finds a way to decrypt it.
Edit the javascript file and run our own file.

The first option will take a long time especially since the file is obfuscated, so let’s stick to the second option.

We can use the override feature to do that, with override, we can take a resource from the current webpage and store it locally. When you refresh the webpage, the browser doesn’t load the resource from the server. Instead, the browser replaces the server resource with your local copy of the resource.

Press enter or click to view image in full size
Press enter or click to view image in full size

We are now ready to edit this file, so the next step is to add some kind of a middle layer (e.g. proxy) into this function to make it encrypt our edited input, not the value that the application passes to the function.

We can do this in more than one way, but let’s keep it simple.
I launched my localhost, and created a simple PHP file that maps the request body to the response, just like below:

<?php

# to allow cross origin requests.
header("Access-Control-Allow-Origin: https://█████████████");
header("Access-Control-Allow-Credentials: true");
header("Content-Type: application/json; charset=UTF-8");
header("Access-Control-Allow-Methods: POST");

# get the request body as it is
$data = file_get_contents("php://input");

# return it back
echo $data; 

?>

So the idea is:

When the application calls the “encrypt” function, it passes two arguments, one of which is the original body.
We send a request to our PHP file with the original body, so we can edit it via burp. (Note that we should allow cross-origin requests)
The PHP file will return our edited body.
We pass the response to the next step in the encrypt function.

I created the following asynchronous function that sends the request to our proxy and returns the edited response:

async function editBeforeSend(originalBody) {
 const req = await fetch("http://proxy.melotover.local/editBeforeSend.php",
  {
  method: "POST",
  body: originalBody,
  credentials: 'include'
  });
 let editedBody = await req.text();
 return editedBody;
}

I added it to the javascript file, then called it inside encrypt function

Press enter or click to view image in full size

That's it! I saved the file, refreshed the page, and invoked any request to the API

Press enter or click to view image in full size
Press enter or click to view image in full size

Now I control any request body sent to the application just by editing it via burp.

That’s all for this blog, I hope you enjoyed reading and I will be pleased if you have any feedback!
