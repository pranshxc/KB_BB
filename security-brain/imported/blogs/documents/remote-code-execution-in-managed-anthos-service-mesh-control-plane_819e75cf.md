---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-15_remote-code-execution-in-managed-anthos-service-mesh-control-plane.md
original_filename: 2021-10-15_remote-code-execution-in-managed-anthos-service-mesh-control-plane.md
title: Remote code execution in Managed Anthos Service Mesh control plane
category: documents
detected_topics:
- oauth
- cloud-security
- command-injection
- otp
tags:
- imported
- documents
- oauth
- cloud-security
- command-injection
- otp
language: en
raw_sha256: 819e75cf4afbf905b8da9454d85fa10c543fc271e446487bffcb025a518b6aa3
text_sha256: 203d401b7f760c9ebfd644b634afd512772109a2096ab39a0821eadae0c43b2d
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Remote code execution in Managed Anthos Service Mesh control plane

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-15_remote-code-execution-in-managed-anthos-service-mesh-control-plane.md
- Source Type: markdown
- Detected Topics: oauth, cloud-security, command-injection, otp
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `819e75cf4afbf905b8da9454d85fa10c543fc271e446487bffcb025a518b6aa3`
- Text SHA256: `203d401b7f760c9ebfd644b634afd512772109a2096ab39a0821eadae0c43b2d`


## Content

---
title: "Remote code execution in Managed Anthos Service Mesh control plane"
page_title: "Remote code execution in Managed Anthos Service Mesh control plane | Anthony Weems"
url: "https://lf.lc/vrp/203177829/"
final_url: "https://amlw.dev/vrp/203177829/"
authors: ["Anthony Weems"]
programs: ["Google"]
bugs: ["RCE"]
bounty: "6,000"
publication_date: "2021-10-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3238
---

#  Remote code execution in Managed Anthos Service Mesh control plane 

October 15, 2021

### Vulnerability Details#

The following writeup describes a vulnerability that allows remote code execution on the Istio control plane. However, this vulnerability requires high privilege access to the Kubernetes cluster in which Istio is deployed. This would normally be a low / informational risk vulnerability, but in a managed Istio context, it becomes higher risk. To demonstrate, I focused on the Google-managed Anthos Service Mesh (ASM), which runs the Istio control plane in a Google-managed project using a per-product per-project service account (P4SA) that authenticates to the user’s GKE cluster. The end result of this vulnerability grants remote code execution in the managed ASM control plane.

Istio supports several deployment modes, including [multicluster deployments](https://istio.io/latest/docs/ops/deployment/deployment-models/#multiple-clusters). In a two cluster installation, cluster administrators provision the Istio control plane in each cluster with access to the other cluster by creating a Kubernetes secret in the `istio-system` namespace with credentials in the form of a kubeconfig.

A kubeconfig contains information like the server address, certificate authority, and authentication material to access a cluster. To support client-side authentication protocols (e.g. OAuth2), `k8s.io/client-go` provides a credential plugin mechanism described [here](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#client-go-credential-plugins). This mechanism allows the user to configure a command that, when executed, returns bearer token credentials.

By combining these features, it is possible to execute arbitrary commands in the Istio control plane using the following steps:

  1. Create a kubeconfig with an exec credential plugin with a malicious command and arguments
  2. Deploying a secret to the `istio-system` namespace with the `istio/multiCluster=true` label with this kubeconfig inside
  3. Wait for the Istio control plane to attempt to authenticate to your remote cluster, executing the malicious command

Even though managed ASM runs outside the cluster, it still monitors the cluster for these secrets and executes the credential plugin if present.

A sample kubeconfig with the exec plugin is shown below:
  
  
  apiVersion: v1
  kind: Config
  current-context: default
  clusters:
  - name: default
  cluster:
  server: https://127.0.0.1
  contexts:
  - name: default
  context:
  cluster: default
  user: default
  users:
  - name: default
  user:
  exec:
  apiVersion: client.authentication.k8s.io/v1beta1
  command: /bin/sh
  args: ['-c', 'touch /tmp/flag']
  

The public Istiod container image on Docker Hub has many helpful utilities to assist an attacker. For example, `docker.io/istio/pilot:1.11.3` includes `/bin/bash` and `/usr/bin/nc` which can be easily used to construct a reverse shell to an attacker-controlled system.

However, the managed ASM container image is much lighter. The only executable binaries available in this container image are:
  
  
  /usr/local/bin/pilot-discovery
  /usr/bin/openssl
  

With just `openssl` to work with, it’s quite difficult, but not impossible to gain full control of the container. I spent nearly a full day working on this problem, and I’d be curious to hear about other solutions. The path I took uses `openssl`’s support for dynamic code execution with the `-engine` flag. The engine loader will load a shared object from disk using `dlopen`, so we simply need a method to write an arbitrary file to disk.

Unfortunately, I could not find an `openssl` subcommand equivalent of `curl` to support downloading data from a remote server. `s_client` is very promising of course, but doesn’t provide a means to write to disk. After reviewing each of the supported subcommands, I settled on using the `req` subcommand to write a DER encoded certificate to disk. Within this certificate, there are several fields controlled by command-line arguments, although most have limitations on length or character sets. However, the `-set_serial` accepts an integer of arbitrary size and includes this within the certificate. The layout of the DER encoded certificate is almost perfect, with our big endian-encoded integer appearing in the output file after 16-ish bytes of DER headers. Since ELF files can contain trailing bytes, the remainder of the certificate is irrelevant.

This would be perfect except for the first few bytes, which are not a valid ELF header. To deal with these bytes, I decided to treat the header and encoded integer as ciphertext, and choose an IV and integer such that the resulting plaintext would be my desired shared object. Then I used the `enc` subcommand to “decrypt” the certificate and write the result to a file.

In CBC mode, the IV is xor’d with the decryption of the first ciphertext block to produce the first plaintext block. The DER prefix is mostly static, so we can decrypt it under a known key, and xor the result with the first 16 bytes of our ELF file to determine the IV. Then we simply decrypt the remaining ELF using the first 16 bytes of ciphertext as the IV to learn the “plaintext” that we need to set as the serial number.

I’ve automated all of the above steps into a script that produces three Kubernetes YAML files for the following general commands:
  
  
  /usr/bin/openssl req -x509 -sha1 -nodes -days 1 -newkey rsa:512 -subj / \
  -keyout /dev/null -out /tmp/engine.enc -outform der -set_serial 271222847...
  /usr/bin/openssl enc -d -aes-128-cbc -K 00000000000000000000000000000000 \
  -iv b529bd0cf491dcf2c81d569cc07accef -in /tmp/engine.enc -out /tmp/engine.so
  /usr/bin/openssl req -engine /tmp/engine.so exploit
  

My `openssl` engine, the exploit script, and output YAML files can be found [here](/assets/vrp/203177829-exploit.tgz).

To replicate, create a GKE cluster and deploy managed ASM using `asmcli`:
  
  
  curl https://storage.googleapis.com/csm-artifacts/asm/asmcli_1.11 > asmcli
  chmod +x asmcli
  ./asmcli install -p <project> -l <zone> -n <cluster> --managed \
  --verbose --output_dir asm --enable-all
  

To customize the shared object, edit `exploit.c` and change the callback server. Then rebuild with `./build.sh` and regenerate the YAML files with `python3 cipher.py`. This will produce YAML files for the kubeconfig and secrets needed to execute the attack. If you’d like, you can examine the kubeconfigs to understand the commands that will be executed. You can then deploy the secrets using the following:
  
  
  kubectl apply -f stage-0-secret.yaml && sleep 3
  kubectl apply -f stage-1-secret.yaml && sleep 3
  kubectl apply -f stage-2-secret.yaml && sleep 3
  kubectl -n istio-system delete kubeconfig # cleanup
  

**Exploit generation script:** ![Exploit generation script.](/assets/vrp/203177829-generation.png)

**Callback after successful exploitation:** ![Callback after successful exploitation.](/assets/vrp/203177829-callback.png)

As shown above, I accessed the metadata service for the serverless workload running my ASM control plane in the `e7d5c125aa20b6d64-tp` project. I also obtained a token for the `service-278129962911@gcp-sa-meshcontrolplane.iam.gserviceaccount.com` P4SA.

### Attack Scenario#

To exploit this issue, an attacker must create a GKE cluster and deploy managed ASM in their project. After deploying three Kubernetes secrets to their cluster, they gain remote code execution in the managed ASM control plane instance for their project. This instance appears to be running in Cloud Run in a Google-managed project, with the P4SA `service-<project-number>@gcp-sa-meshcontrolplane.iam.gserviceaccount.com`.

I stopped research once I realized that the control plane ran in a Google-managed project with a P4SA.

### Remediation#

On November 30th, [John Howard](https://github.com/howardjohn) opened Istio PR [#36307](https://github.com/istio/istio/pull/36307). According to the release notes, this PR “[removes] support for a number of nonstandard kubeconfig authentication methods when using multicluster secret”. The PR add supports for the `PILOT_INSECURE_MULTICLUSTER_KUBECONFIG_OPTIONS` environment variable, which can be set to a comma separated list of kubeconfig authentication providers to allow. This configuration option was released in [Istio version 1.12.1](https://istio.io/latest/news/releases/1.12.x/announcing-1.12.1/). In 1.12.1, the default value for this environment variable is:
  
  
  gcp,azure,exec,openstack,clientkey,clientCertificate,tokenFile
  

However, users can set the environment variable to an empty string to block all authentication providers except OIDC.

### Timeline#

  * 2021-10-15: Initial report to Google VRP
  * 2021-10-15: Issue triaged
  * 2021-10-15: Internal bug report filed
  * 2021-10-26: VRP issued reward ($5000 + $1000 bonus for “a really cool exploit”)
