---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-04_securing-developer-tools-a-new-supply-chain-attack-on-php.md
original_filename: 2022-10-04_securing-developer-tools-a-new-supply-chain-attack-on-php.md
title: 'Securing Developer Tools: A New Supply Chain Attack on PHP'
category: documents
detected_topics:
- supply-chain
- command-injection
- sso
- access-control
- sqli
- mfa
tags:
- imported
- documents
- supply-chain
- command-injection
- sso
- access-control
- sqli
- mfa
language: en
raw_sha256: d02616baf07f1d1505c4a577ba9b01ec58feb1fcb34ee4497ac4489967494620
text_sha256: 17035f7da15ad8ed93085c487951b9d89c7feb79f68e99bdc873e7f6fd09a6da
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Securing Developer Tools: A New Supply Chain Attack on PHP

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-04_securing-developer-tools-a-new-supply-chain-attack-on-php.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, sso, access-control, sqli, mfa
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `d02616baf07f1d1505c4a577ba9b01ec58feb1fcb34ee4497ac4489967494620`
- Text SHA256: `17035f7da15ad8ed93085c487951b9d89c7feb79f68e99bdc873e7f6fd09a6da`


## Content

---
title: "Securing Developer Tools: A New Supply Chain Attack on PHP"
page_title: "Securing Developer Tools: A New Supply Chain Attack on PHP | Sonar"
url: "https://blog.sonarsource.com/securing-developer-tools-a-new-supply-chain-attack-on-php/"
final_url: "https://www.sonarsource.com/blog/securing-developer-tools-a-new-supply-chain-attack-on-php/"
authors: ["Thomas Chauchefoin (@swapgs)"]
programs: ["Packagist"]
bugs: ["Argument injection", "RCE", "Supply chain attack", "Security code review"]
publication_date: "2022-10-04"
added_date: "2022-10-06"
source: "pentester.land/writeups.json"
original_index: 2087
---

## TL;DR overview

  * Sonar's research on a supply chain attack targeting PHP developer tooling documents how attackers compromised the PHP source code repository to inject a backdoor directly into the language runtime, affecting every PHP developer who updated during the compromise window.
  * The attack targeted the php-src Git repository infrastructure rather than a third-party package, demonstrating that even official language distribution channels can be compromised and must be treated as untrusted until verified.
  * The appropriate response included migrating the PHP source repository to GitHub with stronger access controls and multi-factor authentication, reducing the risk of future infrastructure-level compromises.
  * This incident established a template for how supply chain attacks on developer tooling should be detected, disclosed, and remediated—a reference case for any team managing critical open source infrastructure.

## Introduction

Supply chain attacks are a hot topic for development organizations today. Last year, in the largest ever software supply chain attack, a backdoor infected 18,000 SolarWinds customers. Earlier this year, a security researcher was able to breach Apple, Microsoft, Paypal, and other tech giants using a new supply chain attack technique. 

The underlying design exploited by these attacks is that all modern software is built on top of other third-party software components, often without clear visibility of all the downloaded packages. And while reusing many components allows to speed up the development process, infecting the supply chain is a very effective and subtle attack vector to compromise many organizations at once.

While supply chains can take different forms, one of them is significantly more impactful: by gaining access to the servers distributing these third-party software components, threat actors can alter them to obtain a foothold in the systems of their users. 

One year after our first publication about a critical vulnerability in the PHP supply chain (read more in [PHP Supply Chain Attack on Composer](https://blog.sonarsource.com/php-supply-chain-attack-on-composer/)), the Sonar R&D team uncovered a new critical vulnerability in similar components. **It allowed taking control of the server distributing information about existing PHP software packages, and ultimately compromising every organization that uses them.**

In this publication, we present our findings in the biggest PHP package manager, Composer, and its official package repository Packagist. We explain how the discovered code vulnerability works in theory, how it affected Packagist, and how we could demonstrate it on both a test instance and the real one. We will also look at how these code vulnerabilities can be prevented and how the maintainers patched this particular one. 

## Impact

The attack we demonstrate in this publication allowed us to execute arbitrary commands on the server running the official instance of [Packagist](https://packagist.org). Composer uses this service to fetch the metadata associated with a given package and its dependencies. Every month, [around 2 billion software dependencies](https://packagist.org/statistics) are downloaded with Composer from Packagist, among which at least 100 million of these installs require fetching metadata from Packagist. 

The security of these backend services is critical: they perform the association between the name of a package and where the package manager should download it from, so compromising them would allow attackers to force users to download backdoored software dependencies the next time they do a fresh install or an update of a Composer package based on data from 2021. Since Composer is the standard package manager for PHP, most open-source and commercial PHP projects would have been impacted.

**You are already safe if you are using the default, official Packagist instance or Private Packagist.** We responsibly disclosed our findings, and maintainers patched it on the public production instances within hours.

If you integrate Composer as a library and operate on untrusted repositories, upgrade at least to Composer 1.10.26, 2.2.12, or 2.3.5 to benefit from the security patches for CVE-2022-24828. 

## Previous work

Now, let's dive into the technical details of this new finding to see what we can learn. As you'll see, there is a direct link between what we documented in [PHP Supply Chain Attack on Composer](https://blog.sonarsource.com/php-supply-chain-attack-on-composer/): we will first summarize what we did a year ago, show how one of our approaches leads to a dead end, and finally see how we could reuse the same exploitation technique that we introduced last year.

### Discovery of CVE-2021-29472

Our previous work on CVE-2021-29472 provided us with insights on interesting attack surfaces. Even though we reviewed the patches fixing CVE-2021-29472, we could have missed something, and getting back on them is relevant. 

The vulnerability we identified occurred in the implementation of `VcsDriver` sub-classes: one driver exists for every supported Version Control System (hence the name) like Git, Mercurial, Subversion, etc. Their role is to interact with code repositories created by these tools without re-implementing the related necessary code; instead, Composer invokes them as external commands. 

Code that calls system commands is commonly prone to two major classes of vulnerabilities:

  * Command Injection: attackers can inject command substitution sequences later interpreted by the shell to force the execution of additional, arbitrary commands (also see Sonar rule S2076).
  * Argument Injection: attackers can add extra arguments to the invoked command in the hope of influencing its behavior in a dangerous way (also see Sonar rule S5883).

### Command Injection? Argument Injection?

To better understand these concepts, let's go through a few slides from the talk we presented at [BARBHACK](https://www.barbhack.fr/2022/en/) at the end of August.

In the case of a command injection bug, where the attacker-controlled value is not escaped at all, the command within `$()` is first executed by the shell, and its output is used in the second command:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/b6af25e9-a0e3-4fd4-83f0-70143a8704fa/body-6d8f21f0-f4ca-4be6-ae79-8f578f50805b_Securing%2BDeveloper%2BTools_%2BA%2BNew%2BSupply%2BChain%2BAttack%2Bon%2BPHP.png)

Suppose the attacker-controlled value is correctly enclosed by single quotes by an escaping function. In that case, the command substitution will be ignored by the shell and treated as regular characters in a string literal:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/0688f4c9-1bdf-4f7e-ad97-63d6751f84f0/body-9a091e0b-5cdb-456c-a743-17cb66504576_Securing%2BDeveloper%2BTools_%2BA%2BNew%2BSupply%2BChain%2BAttack%2Bon%2BPHP%2B%25281%2529.png)

However, the invoked command's argument parser is going to interpret this value as operands and as arguments when prefixed by one or more dashes (-h, --help):

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/547de5b8-0e3c-4a15-96a2-e2ceb39d8967/body-19a1c44e-93a0-4211-9dd8-b3576ba56d9a_Securing%2BDeveloper%2BTools_%2BA%2BNew%2BSupply%2BChain%2BAttack%2Bon%2BPHP%2B%25282%2529.png)

In this example, a harmless help message will be displayed, but we discovered a specific option of the `hg` client that enables the execution of arbitrary commands in all cases. Again, you can find more details about the exploitation [in our previous publication](https://blog.sonarsource.com/php-supply-chain-attack-on-composer/).

As you can see, it is impossible to protect against argument injection vulnerabilities using escaping functions. It can be surprising as we are used to neutralizing special characters by escaping or encoding them to prevent so-called injection vulnerabilities (e.g., SQL injections). 

Here, developers have to use a special option called the end-of-options: as part of the POSIX specification, it is used to tell the program that parses its arguments to separate options from operands. In simpler terms, anything located at the right of the end-of-options sequence will be treated as an operand: running `hg identify -- --help` won't display the help message.

## Uncovering a new vulnerability

The Packagist interface displays information about packages, for instance, here for the famous Symfony framework: <https://packagist.org/packages/symfony/symfony>:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/3fdde7af-9359-4567-9af2-a7e2a11b9b68/body-9c7a3853-890c-41c6-b6fd-be6509f37067_Securing%2BDeveloper%2BTools%2BPackagist%2BSymfony.png)

When a new package is imported or updated, asynchronous workers are notified. They will then pull the entire repository associated with it. One of the steps of this process is to update the main documentation page of this package.

This content originates from a file named `README.md` by default. This filename could conflict with other services, so the maintainers added an option to specify this file name directly in the package's manifest, as documented in <https://getcomposer.org/doc/04-schema.md#readme>. 

To fetch the contents of this file, the name of the branch is obtained at [1], the file name at [2], and finally, `getFileContents()` is invoked at [3]:

**packagist/src/Package/Updater.php**

Copy to clipboard
  
  
  private function updateReadme(IOInterface $io, Package $package, VcsDriverInterface $driver): void
  {
  // [...]
  try {
  // [1]
  $composerInfo = $driver->getComposerInformation($driver->getRootIdentifier()); 
  if (isset($composerInfo['readme']) && is_string($composerInfo['readme'])) {
  // [2]
  $readmeFile = $composerInfo['readme'];
  } else {
  $readmeFile = 'README.md';
  }
  // [...]
  switch ($ext) {
  case '.txt':
  // [3]
  $source = $driver->getFileContent($readmeFile, $driver->getRootIdentifier());
  if (!empty($source)) {
  $package->setReadme('<pre>' . htmlspecialchars($source) . '</pre>');
  }
  break;
  // [...]

The goal of `getFileContent()` is to allow reading files from a repository at a given branch, tag, or commit. This is the fastest way to proceed and probably safer, too: there is no risk of mistakenly following symbolic links pointing to unintended destinations or introducing command injection vulnerabilities when performing multiple shell commands. 

Each `VcsDriver` implements its version of this method. Let's focus on `GitDriver` (for Git) and `HgDriver` (for Mercurial):

**composer/src/Composer/Repository/Vcs/GitDriver.php**

Copy to clipboard
  
  
  public function getFileContent(string $file, string $identifier): ?string
  {
  $resource = sprintf('%s:%s', ProcessExecutor::escape($identifier), ProcessExecutor::escape($file));
  $this->process->execute(sprintf('git show %s', $resource), $content, $this->repoDir);
  // [...]
  }

**composer/src/Composer/Repository/Vcs/HgDriver.php**

Copy to clipboard
  
  
  public function getFileContent(string $file, string $identifier): ?string
  {
  $resource = sprintf('hg cat -r %s %s', ProcessExecutor::escape($identifier), ProcessExecutor::escape($file));
  $this->process->execute($resource, $content, $this->repoDir);
  // [...]
  }

This is a similar situation to what was done for our previous finding, where we can inject additional arguments. **Both are ideal for exploitation, as the name of the branch and the file are fully controlled through the manifest file.**

### Investigating GitDriver

As a reminder, this command will be invoked as `git show '<branch>':'<file>'`. We can't use the file's name to inject a new argument, so we have to figure out a way to create a Git branch with all the characters we need for our payload and take care of that mandatory suffix `(:'<file>')`.

Among all the options supported by `git show`, only `--output` seems promising as it would allow writing the contents of all the files of the current Git repository into an arbitrary destination. In [Securing Developer Tools: Git Integrations](https://blog.sonarsource.com/securing-developer-tools-git-integrations/), we've already demonstrated that the security of a Git repository is very fragile when the attacker can control or modify internal files such as `.git/config`; this file would be a target of choice here. 

The first step is to create a branch with our injected options in its name. What should be simple appears to be blocked:

Copy to clipboard
  
  
  $ git checkout -b --help
  fatal: '--help' is not a valid branch name

We could still figure out a way to force it on the local repository, and this branch would be accepted by the Git remote: 

Copy to clipboard
  
  
  $ echo "ref: refs/heads/--help" > .git/HEAD
  $ mv .git/refs/heads/main .git/refs/heads/--help
  $ git push origin -- --help

However, the mandatory suffix becomes a significant constraint. The only way to get around it would be to create a symbolic link between, for instance, `foo:README.md` and `.git/config`. 

We quickly figured out that this path is a dead end: repositories are cloned as bare (notice the option `--mirror` in the code snippet below), which means that the directory won't expose files from the malicious package in the repository.

**composer/src/Composer/Util/Git.php**

Copy to clipboard
  
  
  public function syncMirror(string $url, string $dir): bool
  {
  // [...]
  $commandCallable = static function ($url) use ($dir): string {
  return sprintf('git clone --mirror -- %s %s', ProcessExecutor::escape($url), ProcessExecutor::escape($dir));
  };
  $this->runCommand($commandCallable, $url, $dir, true);

### Back on HgDriver

Now, let's have a look at the other vulnerable `VcsDriver`. This time, the command is invoked as `hg cat -r '<branch>' '<file>'`; this is a more ideal context than in `GitDriver`.

As described in the section _Previous Work_ , we can use Mercurial's `--config` option to override the behavior of a built-in command, e.g., `cat`, and make it execute an arbitrary shell script instead. 

We can craft the following payload based on the information above in a very similar fashion to what we did for CVE-2021-29472:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/05056348-5020-4225-86fe-9ac0ed1f7f38/body-421d0009-0b9f-40ca-ba2f-8d4f32f00702_Securing%2BDeveloper%2BTools_%2BA%2BNew%2BSupply%2BChain%2BAttack%2Bon%2BPHP%2B%25283%2529.png)

The payload may be slightly more complex than what you could have expected; let's break it down:

  * _Injected configuration override_ : this is the extra argument that declares a shell command something overriding Mercurial's `cat`;
  * _Payload_ : the repository is cloned as bare, so we can't access files. Using an unmodified call to `hg cat`, we can read the repository's file named `payload.sh` and pipe it to a shell;
  * _Mandatory suffix_ : Packagist only processes files ending with `.txt` or `.md`; other ones are discarded.

An attacker would have to follow these steps to attempt exploiting this vulnerability against Packagist:

  * Create a project in a remote Mercurial repository;
  * Put the manifest in `composer.json` and add a malicious readme entry;
  * When using a payload like the one depicted above, create a file named `payload.sh` to perform the desired actions;  
undefined
  * Import the package on Packagist, and request an update of the package.  

We performed these steps on a test instance we set up and could demonstrate the execution of arbitrary commands on the server: 

The next step would be to modify the definition of a package to point to an unintended destination and compromise the application in which they are used; this is something that we've already demonstrated in [our Insomni'hack talk](https://www.youtube.com/watch?v=RLcK0kRGpjw) and won't be presented again in this article. 

The exploitability of this vulnerability on the production instance, packagist.org, was also demonstrated with a non-destructive command. We immediately reached out to the maintainers with all the technical details of our attempt, IP address, etc. It should be noted that maintainers did not identify any prior exploitation of this vulnerability.

## Patch

**CVE-2022-24828**

As you may remember from the previous sections, it is not possible to patch the injection in GitDriver with the POSIX end-of-options switch. Git introduced a non-standard flag, --end-of-options, but it's only supported starting from Git 2.24, which may break Composer for some users.

As a result, the maintainers merged [2c40c53](https://github.com/composer/composer/commit/2c40c53637c5c7e43fff7c09d3d324d632734709), containing a patch for both vulnerable VcsDriver classes. First, GitDriver is patched by forbidding any branch whose name starts with a dash:

Copy to clipboard
  
  
  public function getFileContent($file, $identifier)
  {
  +  if (isset($identifier[0]) && $identifier[0] === '-') {
  +  throw new \RuntimeException('Invalid git identifier detected. Identifier must not start with a -, given: ' . $identifier);
  +  }
  +
  $resource = sprintf('%s:%s', ProcessExecutor::escape($identifier), ProcessExecutor::escape($file));
  $this->process->execute(sprintf('git show %s', $resource), $content, $this->repoDir);

In a similar fashion, HgDriver now forbids leading slashes in the branch name and introduced the end-of-options switch to protect against argument injections with filename:

Copy to clipboard
  
  
  public function getFileContent($file, $identifier)  {
  -  $resource = sprintf('hg cat -r %s %s', ProcessExecutor::escape($identifier), ProcessExecutor::escape($file));
  +  if (isset($identifier[0]) && $identifier[0] === '-') {
  +  throw new \RuntimeException('Invalid hg identifier detected. Identifier must not start with a -, given: ' . $identifier);
  +  }
  +
  +  $resource = sprintf('hg cat -r %s -- %s', ProcessExecutor::escape($identifier), ProcessExecutor::escape($file));  
  $this->process->execute($resource, $content, $this->repoDir);

**Further hardening**

Composer is slightly different than other package managers because it uses Packagist only to fetch metadata about a given package and download the dependency later from another source. They are not hosting the packages, so it becomes slightly harder to integrate and enforce tools like [sigstore](https://www.sigstore.dev/). 

## Timeline

**Date**| **Action**  
---|---  
2022-04-07| We report the vulnerability to the Packagist maintainers.  
2022-04-07| Vendor acknowledges the issues and starts working on a patch.  
2022-04-08| The public instance at packagist.org is hot-patched.  
2022-04-13| CVE assigned, official communication by Packagist on their blog and new Composer releases. No indicator of previous exploitation of CVE-2022-24828 has been detected.  
  
## Summary

We demonstrated how we discovered an argument injection in the backend services of the PHP package manager Composer and could successfully exploit it to compromise any PHP software dependency. 

This is a perfect example of a retrospectively simple bug missed by the maintainers and vulnerability researchers, even if both likely spent a few hours on this code before merging the security patch for CVE-2021-29472! Coming back on old bugs with a clear mind is a powerful tool that shouldn't be underestimated. 

We want to thank the Packagist maintainers that handled our report, namely @glaubinix, @seldaek, and @naderman; their disclosure process is again one of the smoothest that we have ever experienced. You can read their advisory on the official Packagist blog: [CVE-2022-24828: Composer Command Injection Vulnerability](https://blog.packagist.com/cve-2022-24828-composer-command-injection-vulnerability/).

If you loved what you've just read, and want to help us bring our static analysis technology to the next level, don't hesitate to look at our open security engineering positions: [AppSec Researcher](https://jobs.lever.co/sonarsource/4f9dbd7e-a5ee-4858-b526-56b2c671f9c4), [Vulnerability Researcher](https://jobs.lever.co/sonarsource/06ddcdf2-c99f-4672-aa86-4fc0b58625ae), [Static Analysis Scientist](https://jobs.lever.co/sonarsource/869c6386-4f66-479b-932f-db5019f8c14a)… Many more are to be found on [our careers page](https://jobs.lever.co/sonarsource)!

## Related Blog Posts

  * [PHP Supply Chain Attack on Composer](https://blog.sonarsource.com/php-supply-chain-attack-on-composer/)
  * [PHP Supply Chain Attack on PEAR](https://blog.sonarsource.com/php-supply-chain-attack-on-pear/)
  * [Securing Developer Tools: Git Integrations](https://blog.sonarsource.com/securing-developer-tools-git-integrations/)
  * [Securing Developer Tools: Argument Injection in Visual Studio Code](https://blog.sonarsource.com/securing-developer-tools-argument-injection-in-vscode/)
