---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-03_malicious-kubernetes-helm-charts-can-be-used-to-steal-sensitive-information-from.md
original_filename: 2022-02-03_malicious-kubernetes-helm-charts-can-be-used-to-steal-sensitive-information-from.md
title: Malicious Kubernetes Helm Charts can be used to steal sensitive information
  from Argo CD deployments
category: documents
detected_topics:
- supply-chain
- sso
- access-control
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- supply-chain
- sso
- access-control
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: e1bea6379ca2bc0ea7dc84ec16585e7671917acdddfd61c7ca52002f06fe111e
text_sha256: 9ca5adff75df1f2fc1b5bf250693d0f5fe81ab184b1447f7bfa0e4c44d6fd5d2
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Malicious Kubernetes Helm Charts can be used to steal sensitive information from Argo CD deployments

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-03_malicious-kubernetes-helm-charts-can-be-used-to-steal-sensitive-information-from.md
- Source Type: markdown
- Detected Topics: supply-chain, sso, access-control, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `e1bea6379ca2bc0ea7dc84ec16585e7671917acdddfd61c7ca52002f06fe111e`
- Text SHA256: `9ca5adff75df1f2fc1b5bf250693d0f5fe81ab184b1447f7bfa0e4c44d6fd5d2`


## Content

---
title: "Malicious Kubernetes Helm Charts can be used to steal sensitive information from Argo CD deployments"
page_title: "Sensitive Info Can Be Stolen from Argo CD Deployments | Apiiro"
url: "https://apiiro.com/blog/malicious-kubernetes-helm-charts-can-be-used-to-steal-sensitive-information-from-argo-cd-deployments/"
final_url: "https://apiiro.com/blog/malicious-kubernetes-helm-charts-can-be-used-to-steal-sensitive-information-from-argo-cd-deployments/"
authors: ["Apiiro’s Security Research"]
programs: ["Argo CD"]
bugs: ["Supply chain attack", "CI/CD"]
publication_date: "2022-02-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2943
---

[Apiiro Blog ](https://apiiro.com/blog) ﹥ Malicious Kubernetes Helm charts can be… 

Technical 

# Malicious Kubernetes Helm charts can be used to steal sensitive information from Argo CD deployments

Published February 3 2022 ·  4 min. read 

Apiiro’s Security Research team has uncovered a major software supply chain 0-day vulnerability ([CVE-2022-24348](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24348)) in Argo CD, the popular open source Continuous Delivery platform, which enables attackers to access sensitive information such as secrets, passwords, and API keys.

Argo CD manages and orchestrates the execution and monitoring of application deployment post-integration.

## TL;DR

  * Argo CD is a popular, open-source, Continuous Delivery (CD) platform that is used by thousands of organizations globally.
  * A 0-day vulnerability, discovered by Apiiro’s Security Research team, allows malicious actors to load a Kubernetes Helm Chart YAML file to the vulnerability and “hop” from their application ecosystem to other applications’ data outside of the user’s scope.
  * The actors can read and exfiltrate secrets, tokens, and other sensitive information residing on other applications.
  * The impact of the attack includes privilege escalation, sensitive information disclosure, lateral movement attacks, and more.
  * Although Argo CD contributors were aware of this weak point in 2019 and implemented an anti-path-traversal mechanism, a bug in the control allows for exploitation of this vulnerability. 

![](https://apiiro.com/wp-content/uploads/2022/02/CVE-image.png)

## Vulnerability Details & Attack Breakdown 

In order to build a new deployment pipeline, a user can define either a Git repository or a Kubernetes Helm Chart file that includes:

  * The metadata and information needed to deploy the appropriate Kubernetes configuration, and
  * The ability to dynamically update the cloud configuration as the manifest is being modified.

A Helm Chart is a YAML file that embeds different fields to form a declaration of resources and configurations needed in order for deploying an application.

The application in question can contain values of many sorts, one of those types can contain file names and relative paths to self-contained application parts in other files.

In fact, Argo CD’s contributors [envisioned this kind of exploitation in 2019](https://github.com/argoproj/argo-cd/issues/2715) to be possible and built a dedicated mechanism to thwart any such attempt.

Repositories are saved on a dedicated server or pod named _argocd-reposerver_. There is no strong segmentation apart from file hierarchy, so the anti-path-traversal mechanism is a critical linchpin of file security.The inner workings of the mechanism are mainly present in a single file in the source code at _util/security/path_traversal.go,_ which defines the procedural cleanup of source path input.

123456789101112131415161718192021222324252627282930313233 | // Ensure that `requestedPath` is on the same directory or any subdirectory of `currentRoot`. Both `currentRoot` and// `requestedPath` must be absolute paths. They may contain any number of `./` or `/../` dir changes.func EnforceToCurrentRoot(currentRoot, requestedPath string) (string, error) { currentRoot = filepath.Clean(currentRoot) requestedDir, requestedFile := parsePath(requestedPath) if !isRequestedDirUnderCurrentRoot(currentRoot, requestedDir) { return "", fmt.Errorf("requested path %s should be on or under current directory %s", requestedPath, currentRoot) } return requestedDir + string(filepath.Separator) + requestedFile, nil} func isRequestedDirUnderCurrentRoot(currentRoot, requestedPath string) bool { if currentRoot == string(filepath.Separator) { return true } else if currentRoot == requestedPath { return true } if requestedPath[len(requestedPath)-1] != '/' { requestedPath = requestedPath + "/" } if currentRoot[len(currentRoot)-1] != '/' { currentRoot = currentRoot + "/" } return strings.HasPrefix(requestedPath, currentRoot)} func parsePath(path string) (string, string) { directory := filepath.Dir(path) if directory == path { return directory, "" } return directory, filepath.Base(path)}  
---|---  
  
The functions in the code snippet above are in charge of cleanup (consisting mainly of [Go’s package filepath and its Clean()](https://pkg.go.dev/path/filepath#Clean) function) and check that the resulting cleaned-up version of the path matches the subdirectory of the current operating directory.

The function is used in Helm Chart processing under reposerver/repository/repository.go:

12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364 | func helmTemplate(appPath string, repoRoot string, env *v1alpha1.Env, q *apiclient.ManifestRequest, isLocal bool) ([]*unstructured.Unstructured, error) { concurrencyAllowed := isConcurrencyAllowed(appPath) if !concurrencyAllowed { manifestGenerateLock.Lock(appPath) defer manifestGenerateLock.Unlock(appPath) } templateOpts := &amp;helm.TemplateOpts{ Name: q.AppName, Namespace: q.Namespace, KubeVersion: text.SemVer(q.KubeVersion), APIVersions: q.ApiVersions, Set: map[string]string{}, SetString: map[string]string{}, SetFile: map[string]string{}, } appHelm := q.ApplicationSource.Helm var version string var passCredentials bool if appHelm != nil { if appHelm.Version != "" { version = appHelm.Version } if appHelm.ReleaseName != "" { templateOpts.Name = appHelm.ReleaseName } for _, val := range appHelm.ValueFiles { // If val is not a URL, run it against the directory enforcer. If it is a URL, use it without checking // If val does not exist, warn. If IgnoreMissingValueFiles, do not append, else let Helm handle it. if _, err := url.ParseRequestURI(val); err != nil { // Ensure that the repo root provided is absolute absRepoPath, err := filepath.Abs(repoRoot) if err != nil { return nil, err } // If the path to the file is relative, join it with the current working directory (appPath) path := val if !filepath.IsAbs(path) { absWorkDir, err := filepath.Abs(appPath) if err != nil { return nil, err } path = filepath.Join(absWorkDir, path) } _, err = security.EnforceToCurrentRoot(absRepoPath, path) if err != nil { return nil, err } _, err = os.Stat(path) if os.IsNotExist(err) { if appHelm.IgnoreMissingValueFiles { log.Debugf(" %s values file does not exist", path) continue } } } templateOpts.Values = append(templateOpts.Values, val) }  
---|---  
  
This function further inspects and relies on the returned values from the path_traversal’s cleanup and current-directory matching for listed elements under the Chart’s _valueFiles_ field. The field is supposed to contain a reference to the files within the **local** accompanying value files to be subsequently read and parsed into ingested values.

Here is a sample Argo CD manifest file with the valueFiles field present:

12345678910111213141516 | apiVersion: argoproj.io/v1alpha1kind: Applicationmetadata: name: testApplication namespace: argocdspec: destination: namespace: default server: https://kubernetes.default.svc project: default source: helm: valueFiles: - values.yaml path: src repoURL: https://github.com/[path_to_repo].git  
---|---  
  
## So far so good, but…

While investigating the control flow and potential angles to attack the system, the Apiiro Security Research team paid special attention to the way the _valueFiles_ values are evaluated and parsed by the application.

A crucial point of interaction is the preliminary check for input value content – [the code searches for patterned string that will fit into the mold of a URI](https://github.com/argoproj/argo-cd/blob/96f95ca1c1048c37f935f6f72ff54be641d92b60/reposerver/repository/repository.go#L588) by utilizing a function called _ParseRequestURI._

Looking deeper into this decisive point – here is what the [official documentation](https://pkg.go.dev/net/url#ParseRequestURI) says about the function’s behavior:

_ParseRequestURI parses a raw url into a URL structure. It assumes that url was received in an HTTP request, so the url is interpreted only as an absolute URI or an absolute path. The string url is assumed not to have a #fragment suffix. (Web browsers strip #fragment before sending the URL to a web server.)_

So can we make the parser accept a local file-path and confuse it to be a URI, and use that confusion to skip the whole cleanup and anti-path-traversal mechanism check?

The answer is yes – with a simple trick.

## If it walks like a URI

Deconstructing the sentence “It assumes that url was received in an HTTP request, so the url is interpreted only as an absolute URI or an absolute path” reveals the Achilles’ heel of the mechanism. Simply put: if the valueFiles listed are going to look like a URI, it will be treated as one, skipping all other checks and treating it as a legitimate URL.

Because the default behavior of the function is to take for granted that it receives an HTTP request,- it can be an absolute path of a URL like _/directory/values.yaml_ (take special notice of the prefixed backslash on the path).When looking at it as a URL, it passes the sanity test but is an absolute file-path.

Because the reposerver uses a monolithic and deterministic file-structure, all the other out-of-bound applications have a definite and predictable format and path. An attacker can ssemble a concatenated, direct call to a specified values.yaml file, which is used by many applications as a vassal for secret and sensitive values.

## Impact

The impact of the vulnerability is two-fold:

First, there are the direct implications of contents read from other files present on the reposerver, which can contain sensitive information. This by itself can impact an organization.

Second, because application files usually contain an assortment of transitive values of secrets, tokens, and environmental sensitive settings – this can effectively be used by the attacker to further expand their campaign by moving laterally through different services and escalating their privileges to gain more ground on the system and target organization’s resources.

## Technical designations

CVSS: 3.0/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N – Score 7.7 (High)

CVE-ID: CVE-2022-24348

## Acknowledgements

Apiiro’s Research Team would like to extend our gratitude to Argo CD’s swift incident response and professional handling of the case, for treating their large user-base with respect, and for understanding of the implications of the attack scenarios.

## Timeline

30-Jan-2022 : Vulnerability reported to vendor

30-Jan-2022 : Vendor verified and acknowledged the bug

31-Jan-2022 : Mutual continued triage to understand and discuss vulnerability’s extent and impact

01-Feb-2022 : Vendor reported on progressive work on patch and fix and release schedule

03-Feb-2022 : Synchronous release of advisories, patch, and blog
