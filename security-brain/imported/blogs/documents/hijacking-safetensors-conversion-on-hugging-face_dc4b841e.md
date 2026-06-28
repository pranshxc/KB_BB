---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-21_hijacking-safetensors-conversion-on-hugging-face.md
original_filename: 2024-02-21_hijacking-safetensors-conversion-on-hugging-face.md
title: Hijacking Safetensors Conversion On Hugging Face
category: documents
detected_topics:
- supply-chain
- sso
- command-injection
- otp
- automation-abuse
- webhooks
tags:
- imported
- documents
- supply-chain
- sso
- command-injection
- otp
- automation-abuse
- webhooks
language: en
raw_sha256: dc4b841ed9a395877ab62db9ce39eda5e8bfdf0dcf2810c273c2bace597765a5
text_sha256: db9a4bc54fe461a5a6ce0d86bb5ff496d3eee7d2d546a3bf130fb961e60cea2e
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: false
---

# Hijacking Safetensors Conversion On Hugging Face

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-21_hijacking-safetensors-conversion-on-hugging-face.md
- Source Type: markdown
- Detected Topics: supply-chain, sso, command-injection, otp, automation-abuse, webhooks
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: False
- Raw SHA256: `dc4b841ed9a395877ab62db9ce39eda5e8bfdf0dcf2810c273c2bace597765a5`
- Text SHA256: `db9a4bc54fe461a5a6ce0d86bb5ff496d3eee7d2d546a3bf130fb961e60cea2e`


## Content

---
title: "Hijacking Safetensors Conversion On Hugging Face"
page_title: "Silent Sabotage: Hijacking Safetensors Conversion on Hugging Face"
url: "https://hiddenlayer.com/research/silent-sabotage/"
final_url: "https://www.hiddenlayer.com/research/silent-sabotage"
authors: ["Eoin Wickens (@enwckns)", "Kasimir Schulz (@Abraxus7331)"]
programs: ["Hugging Face"]
bugs: ["Malicious AI model", "Supply chain attack"]
publication_date: "2024-02-21"
added_date: "2024-08-14"
source: "pentester.land/writeups.json"
original_index: 415
---

research

# Hijacking Safetensors Conversion on Hugging Face

February 21, 2024

‍

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf5e/6979193da9127fb6d3100065_HuggingFace_FeaturedImage-scaled.webp)

### Table of Contents

H2 Link

Share:

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf57/696e337906885201580ac74b_FacebookLogo.svg)![](https://cdn.prod.website-files.com/694066252c49b2800c70cf57/696e33794aab57f9903a8b57_XLogo.svg)![](https://cdn.prod.website-files.com/694066252c49b2800c70cf57/696e33796a759478dd5e3614_LinkedinLogo.svg)![](https://cdn.prod.website-files.com/694066252c49b2800c70cf57/696e33794d6bd97674dd23a2_EnvelopeSimple.svg)

## Summary

In this blog, we show how an attacker could compromise the [Hugging Face Safetensors conversion space](https://huggingface.co/spaces/safetensors/convert) and its [associated service bot](https://huggingface.co/SFconvertbot). These comprise a popular service on the site dedicated to converting insecure machine learning models within their ecosystem into safer versions. We then demonstrate how it’s possible to send malicious pull requests with attacker-controlled data from the Hugging Face service to any repository on the platform, as well as hijack any models that are submitted through the conversion service. We achieve this using nothing but a hijacked model that the bot was designed to convert, allowing an attacker to request changes to any repository on the platform by impersonating the Hugging Face conversion bot. We also show how it is possible to persist malicious code inside the service so that models are hijacked automatically as they are converted with [ai data poisoning](/insight/understanding-ai-data-poisoning).

While the code for the conversion service is run on Hugging Face servers, the system is containerized in Hugging Face Spaces - a place where any user of the platform can run code. As a result, most of the risk isn’t to Hugging Face themselves but rather to the repositories hosted on the site and their users. Our team felt obligated to release the research to the public so that any compromised models may be found before any damage could occur. On top of our public reporting of the vulnerability, we also contacted Hugging Face prior to release to give them time to shut down the conversion service or implement safeguards.

## Introduction;

At the heart of any Artificial Intelligence system lies a machine learning model - the result of; vast computation across a given dataset, which has been trained, tweaked, and tuned to perform a specific task or put to a more general application. Before a model can be deployed in a product or used as part of a service, it must be serialized (saved) to disk in what is referred to as a serialization format. By effectively boiling a model down into a binary representation, we can deploy the model outside the system it was trained on or share it with whomever we desire. In the industry, these models are commonly referred to as ‘pre-trained models’ - and they’ve taken the world by storm.

Pre-trained, open-source models are one of the main driving factors behind the widespread adoption of AI, enabling data science teams to share, download, and repurpose existing models to suit their bespoke applications without needing the vast resources required to create them from scratch. In fact, the sharing of models has become so ubiquitous that companies such as [Hugging Face](https://huggingface.co/) have been created around this premise. Hugging Face boasts a strong community that has uploaded over 500,000 pre-trained models to the platform to date.

But, there’s a catch.

## Models are code

If you’ve been following our research, you’ll know that [models are code](/research/models-are-code), and several of the most widely used serialization formats allow for arbitrary code execution in some way, shape, or form and are being [actively exploited in the wild](/research/pickle-strike).;  
  
The biggest perpetrator for this is [Pickle](https://docs.python.org/3/library/pickle.html), which, despite being one of the most vulnerable serialization formats, is the most widely used. Pickle underpins the [PyTorch](https://pytorch.org/) library and is the most prevalent serialization format on Hugging Face [as of last year](https://www.splunk.com/en_us/blog/security/paws-in-the-pickle-jar-risk-vulnerability-in-the-model-sharing-ecosystem.html). However, to mitigate the supply chain risk posed by vulnerable serialization formats, the Hugging Face team set to work on developing a new serialization format, one that would be built from the ground up with security in mind so that it could not be used to execute malicious code - which they called [Safetensors](https://github.com/huggingface/safetensors).

## Understanding the conversion service

Safetensors does what it says on the tin, and, to the best of our knowledge, allows for safe deserialization of machine learning models largely due to it storing only model weights/biases and no executable code or computational primitives. To help pivot the Hugging Face userbase to this safer alternative, the company created a [conversion service](https://huggingface.co/spaces/safetensors/convert) to convert any PyTorch model contained within a repository into a Safetensors alternative via a pull request. The [code (convert.py)](https://github.com/huggingface/safetensors/blob/main/bindings/python/convert.py) for the conversion service is sourced directly from the Safetensors projects and runs via [Hugging Face Spaces](https://huggingface.co/spaces), a cloud compute offering for running Python code in the browser.  
  
In this Space, a [Gradio application](https://huggingface.co/spaces/safetensors/convert/blob/main/app.py) is bundled alongside convert.py, providing a web interface where the end user can specify a repository for conversion. The application only permits PyTorch binaries to be targeted for conversion and requires a filename of _pytorch_model.bin_ to be present within the repository __ to initiate the process, as shown below:

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf5e/6979193ca9127fb6d30fffee_1SilentSabotage.webp)

_Figure 1 - A Hugging Face repository to be converted._

‍

Users can navigate to the converter application web interface and enter the repository ID in the following format:

_< Username>/<repository-name>_

For our testing, we created the following repository with our specially crafted PyTorch model:

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf5e/6979193ca9127fb6d30fffc9_2SilentSabotage.png)

_Figure 2 - The conversion service web UI._

‍

Providing the user has specified a valid repository with a parseable PyTorch model in the required format, the conversion service will convert the model and create a pull request within the originating repository via the [_‘SFconvertbot’_](https://huggingface.co/SFconvertbot) __ user. Despite the first step of the process shown in _Figure 2_ , we do not need to enter a user token from the owner of the target repository, meaning that we can submit a conversion request to any project, even those that don’t belong to us.

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf5e/6979193ca9127fb6d30fffeb_3SilentSabotage.webp)

_Figure 3 - The SafeTensors conversion bot “SFconvertbot” issuing a pull request to a repo._

‍

## Identifying the attack vector

We became curious as to how the conversion bot was loading up the PyTorch files, as all it takes is a simple _torch.load()_ to compromise the host machine. In convert.py, there is a safety warning that has to be manually bypassed with the ‘-y’ flag when run directly via the command line (as opposed to the bundled Gradio application _app.py_):

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf5e/6979193ca9127fb6d30fffdb_4SilentSabotage.webp)

_Figure 4 - convert.py safety warning._

‍

Lo and behold, the tensors are being loaded using the _torch.load()_ function, which can lead to arbitrary code execution if malicious code is stored within data.pkl in the PyTorch model. But what is different with the conversion bot in Hugging Face spaces? As it turns out, nothing - they’re the same thing!

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf5e/6979193ca9127fb6d30ffffb_5SilentSabotage.webp)

_Figure 5 - torch.load() used in the convert.py conversion script._

‍

At this point, it dawned on us. Could someone hijack the hosted conversion service using the very thing that it was designed to convert?

## Crafting the exploit

We set to work putting our thoughts into practice by crafting a malicious PyTorch binary using the pre-trained AlexNet model from torchvision and injected our first payload - _eval(“print(‘hi’)”)_ \- a simple _eval_ call that would print out ‘hi’.

Rather than testing on the live service, we deployed a local version of the converter service to evaluate our code execution capabilities and see if a pull request would be created.

We were able to confirm that our model had been loaded as we could see ‘hi’ in the output but with one peculiar error. It seemed that by adding in our exploit code, we had modified the file size of the model past a point of 1% difference, which had ultimately prevented the model from being converted or the bot from creating a pull request:

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf5e/6979193ca9127fb6d30fffd2_6SilentSabotage.webp)

_Figure 6 - Terminal output from a local run of convert.py._

‍

Faced with this error, we considered two possible approaches to circumvent the problem. Either use a much larger file or use our exploit to bypass the size check. As we wanted our exploit to work on any type of PyTorch model, we decided to proceed with the latter and investigate the logic for the file size check.

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf5e/6979193ca9127fb6d30fffcc_7SilentSabotage.webp)

_Figure 7 - The check_file_size function._

‍

The function _check_file_size_ took two string arguments representing the filenames, then used _os.stat_ to check their respective file size, and if they differed too greatly (>1%), it would throw an error.

At first, we wanted to find a viable method to modify the file sizes to skip the conditional logic. However, when the PyTorch model was being loaded, the Safetensors file did not yet exist, causing the error. As our malicious model had loaded before this file size check, we knew we could use it to make changes to the convert.py script at runtime and decided to overwrite the function pointer so that a different function would get called instead of _check_file_size_.  
  
As _check_file_size_ did not return anything, we just needed a function that took in two strings and didn’t throw an exception. Our potential replacement function _os.path.join_ fit this criteria perfectly. However, when we attempted to overwrite the _check_file_size_ function, we discovered a problem. PyTorch does not permit the equals symbol _‘=’_ inside any strings, preventing us from assigning a value to a function pointer in that manner. To counter this, we created the following payload, using _setattr_ to overwrite the function pointer manually:

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf5e/6979193ca9127fb6d30fffd5_8SilentSabotage.webp)

_Figure 8 - Python code to overwrite the check_file_size function pointer._

‍

After modifying our PyTorch model with the above payload, we were then able to convert our model successfully using our local converter. Additionally, when we ran the model through Hugging Face’s converter, we were able to successfully create a pull request, now with the ability to compromise the system that the conversion bot was hosted on:

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf5e/6979193ca9127fb6d30ffff4_9SilentSabotage.webp)

_Figure 9 - Successfully converting a malicious PyTorch model and issuing a pull request using the Hugging Face service._

‍

## Imitation is the greatest form of flattery

While the ability to arbitrarily execute code is powerful even when operating in a sandbox, we noticed the potential for a far greater threat. All pull requests from the conversion service are generated via the [SFconvertbot](https://huggingface.co/SFconvertbot), an official bot belonging to Hugging Face specifically for this purpose. If an unwitting user sees a pull request from the bot stating that they have a security update for their models, they will likely accept the changes. This could allow us to upload different models in place of the one they wish to be converted, implant neural backdoors, degrade performance, or change the model entirely - posing a huge supply chain risk.

Since we knew that the bot was creating pull requests from within the same sandbox that the convert code runs in, we also knew that the credentials for the bot would more than likely be inside the sandbox, too.;  
  
Looking through the code, we saw that they were set as environmental variables and could be accessed using _os.environ.get("HF_TOKEN")_. While we now had access to the token, we still needed a method to exfiltrate it. Since the container had to download the files and create the pull requests, we knew it would have some form of network access, so we put it to the test. To ascertain if we could hit a domain outside the Hugging Face domain space, we created a remote webhook and sent a get request to the hook via the malicious model:

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf5e/6979193ca9127fb6d30fffe8_10SilentSabotage.webp)

_Figure 10 - Receiving a web request from the system running the Hugging Face conversion service._

‍

Success! We now have a way to exfiltrate the Hugging Face SFConvertbot token, send a malicious pull request to any repository on the site impersonating a legitimate, official service.

Though we weren’t done quite yet.

## You can’t beat the real thing

Unhappy with just impersonating the bot, we decided to check if the service restarted each time a user tried to convert a model, so as to evaluate an opportunity for persistence. To achieve this, we created our own Hugging Face Space built on the Gradio SDK, to make our Space as close to the conversion service as possible.

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf5e/6979193ca9127fb6d30fffe1_11SilentSabotage.webp)

_Figure 11 - Selecting the Gradio SDK option when creating our own Space for testing_

‍

Now that we had the space set up, we needed a way to imitate the conversion process. We created a Gradio application that took in user input, executed it using the inbuilt Python function _‘exec’._ Then, we included with it a dummy function ‘greet_world’ which, regardless of user input, would output ‘Hello world!’.  
  
In effect, this incredibly strenuous work allowed us to closely simulate the environment of the conversion function by allowing us to execute code similarly to the torch.load() call, and gave us a target function to attempt to overwrite at runtime. Our real target being the [_save_file_](https://huggingface.co/spaces/safetensors/convert/blob/main/convert.py#L202) function in convert.py which saves the converted SafeTensors file to disk.

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf5e/6979193ca9127fb6d30fffe5_12SilentSabotage.webp)

_Figure 12 - Our testing code from Hugging Face Spaces_

‍

Once we had everything up and running, we issued a simple test to see if the application would return “Hello World” after being given some code to execute:

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf5e/6979193ca9127fb6d30fffd8_13SilentSabotage.webp)

_Figure 13 - The testing Gradio application in our own Space_

In a similar vein to how we approached bypassing the _get_file_size_ function, we attempted to overwrite _greet_world_ using _setattr_. In our exploit script, we limited ourselves to what we would be allowed to use in the context of the _torch.load_. We decided to go with the approach of creating a local file, writing the code we wanted into it, retrieving a pointer to _greet_world_ , and replacing it with our own malicious function.

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf5e/6979193ca9127fb6d30fffcf_14SilentSabotage.webp)

_Figure 14 - Successfully overwriting the greet_world function_

‍

As seen in Figure 14, the response changed from “Hello World!” to “pwned”, which was our success case. Now the real test began. We had to see if the changes made to the Space would persist once we had refreshed it in the browser. By doing so, we could see if the instance would restart and, by virtue, if our changes would persist. Once again, we input our initial benign prompt, except this time “pwned” was the result on our newly refreshed page.;

**We had persistence.**

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf5e/6979193ca9127fb6d30fffde_15SilentSabotage.webp)

_Figure 15 - Testing our initial benign prompt against the compromised Space_

‍

We had now proved that an attacker could run any arbitrary code any time someone attempted to convert their model. Without any indication to the user themselves, their models could be hijacked upon conversion. What’s more, if a user wished to convert their own private repository, we could in effect steal their Hugging Face token, compromise their repository, and view all private repositories, datasets, and models which that user has access to.

**_Nota bene:_**_  
While conducting this research, we did not leak the SFConvertbot token or pursue malicious actions on the Hugging Face systems in question. At HiddenLayer, we believe in finding vulnerabilities so that they can be fixed, and we ceased our investigation once we had confirmed our findings._

## What does this mean for you?

Users of Hugging Face range from individual researchers to major organizations, uploading models for the community to use freely. Many of the 500,000+ machine-learning models uploaded to the platform are vulnerable to malicious code injection through insecure file formats. In an effort to stem this, Hugging Face introduced the Safetensors conversion bot, where any user can convert their models into a safer alternative, free from malware. However, we show how this process can be hijacked and openly question if this service could have been previously compromised, potentially leading to a considerable supply chain risk where major organizations have accepted changes to their models suggested by this bot.;

We have identified organizations such as Microsoft and Google, who, between them, have 905 models hosted on Hugging Face, as having accepted changes to some of their Hugging Face repositories from this bot and who may potentially be at risk of a targeted supply chain attack.;

Any changes created as part of a pull request from this service are widely accepted without dispute as they arise from the trusted Hugging Face associated bot. While a user can ask for their own repository to be converted, it does not have to originate from that user - any user can submit a conversion request for a public repository, which in turn will create a pull request from the bot in the repository in question.;

If an attacker wished, they could use the outlined methodology to create their own version of the original model with a backdoor to trigger malicious behavior, for example, bypassing a facial recognition system or generating disinformation. Comparing changes between machine learning models requires careful scrutiny as the models themselves are stored in a non-human readable format, meaning that the only way of comparing them is programmatic, and standard visual comparisons will not work. As a result, it is not immediately apparent that a model has been hijacked or altered when accepting a pull request on Hugging Face. Therefore, we recommend that you thoroughly investigate any repositories under your control to determine if there has been any form of illicit tampering to your model weights and biases as a result of this insecure conversion process.

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf5e/6979193ca9127fb6d30ffff1_16SilentSabotage.webp)

_Figure 16 - A Google repository with the only accepted pull request from the Hugging Face SFconvertbot - the only accepted pull request on the repo._

‍

As can be seen in Figure 16, Google’s _vit-base-patch26-224-in21k_ model accepted a pull request from the SFConvertbot and rejected another pull request trying to change the README. In Figure 17 below, we can see that the model has been downloaded 3,836,972 times in the last month alone. While we haven’t detected any sign of compromise in this model, this attests to the implicit trust placed in the conversion service by even the largest of organizations.

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf5e/6979193ca9127fb6d30ffff7_17SilentSabotage.webp)

_Figure 17 - The same Google repository with 3,836,972 downloads in the last month alone._

‍

## Conclusions

Through a malicious PyTorch binary, we demonstrated how it was possible to compromise the Hugging Face Safetensors conversion service. We showed how we could have stolen the token for the official Safetensors conversion bot to submit pull requests on its behalf to any repository on the site. We also demonstrated how an attacker could take over the service to automatically hijack any model submitted to the service.

The potential consequences for such an attack are huge, as an adversary could implant their own model in its stead, push out malicious models to repositories en-masse, or access private repositories and datasets. In cases where a repository has already been converted, we would still be able to submit a new pull request, or in cases where a new iteration of a PyTorch binary is uploaded and then converted using a compromised conversion service, repositories with hundreds of thousands of downloads could be affected.

Despite the best intentions to secure machine learning models in the Hugging Face ecosystem, the conversion service has proven to be vulnerable and has had the potential to cause a widespread supply chain attack via the Hugging Face official service. Furthermore, we also showed how an attacker could gain a foothold into the container running the service and compromise any model converted by the service.

Sandboxing is a great first step in locking down an application if you’re concerned about the potential for code execution on the machine. However, even when sandboxed, arbitrary code should not be allowed to run in the same application that performs an important community service. At HiddenLayer we understand that dealing with a known method of code execution, such as the Pickle/PyTorch file format, can be tricky, which is why we are such strong advocates for scanning machine learning models for malicious content before you interact with it in any way.

Out of the top 10 most downloaded models from both Google and Microsoft combined, the models that had accepted the merge from the bot had a staggering 16,342,855 downloads in the last month. While 20 models are only a small subset of the 500,000+ models hosted on Hugging Face, they reach an incredible number of users, leaving us to wonder, considering the bot has made 42,657 contributions, how many users have downloaded a potentially compromised model?

## Related Research

All Researchs

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf57/6941993a7d7b9513251ef4e7_Frame%202147223616.svg)

[](/research)

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf5e/6a3211a079992339d7c8f18f_APE%20Taxonomy%202026_FeaturedImage.jpg)

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf57/694066252c49b2800c70cf88_image.svg)

Research

min read

Updating HiddenLayer’s APE Taxonomy: A New Objective Model for AI Attacks

HiddenLayer's APE Taxonomy update introduces a new objective model for AI attacks, expanded techniques, and improved threat modeling for generative AI systems.

[](/research/updating-hiddenlayers-ape-taxonomy-a-new-objective-model-for-ai-attacks)

Read time

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf5e/6a2ac2672fdfd59d406fe218_Skills%20Blog_FeaturedImage.jpg)

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf57/694066252c49b2800c70cf88_image.svg)

Research

min read

The Next AI Supply Chain Risk: Malicious Skills in Agentic AI

Agentic AI is rapidly transforming how individuals and enterprises work, with skills emerging as a key mechanism for extending agent capabilities. However, the same flexibility that makes skills powerful also creates a new supply chain attack surface.

[](/research/the-next-ai-supply-chain-risk-malicious-skills-in-agentic-ai)

Read time

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf5e/6a15be9622cce6bbf6d1ac90_Tokenizer2_FeaturedImage.jpg)

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf57/694066252c49b2800c70cf88_image.svg)

Research

min read

Inside the Prompt: How LLMs Learn Roles, Follow Instructions, and Get Exploited

Learn how LLMs use control tokens, instruction hierarchy, and prompt templates to power agentic AI systemsand how attackers exploit these same mechanisms through prompt injection and control token spoofing. 

[](/research/inside-the-prompt-how-llms-learn-roles-follow-instructions-and-get-exploited)

Read time

![](https://cdn.prod.website-files.com/694066252c49b2800c70cf57/695f983050b266fad6c09179_1b38f9474edda1c2caf54995d03db737_cta-3-bg.svg)

## Stay Ahead of AI Security Risks

Get research-driven insights, emerging threat analysis, and practical guidance on securing AI systems—delivered to your inbox.
