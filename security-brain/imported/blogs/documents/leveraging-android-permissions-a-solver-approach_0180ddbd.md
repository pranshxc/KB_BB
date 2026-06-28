---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-20_leveraging-android-permissions-a-solver-approach.md
original_filename: 2023-06-20_leveraging-android-permissions-a-solver-approach.md
title: 'Leveraging Android Permissions: A Solver Approach'
category: documents
detected_topics:
- access-control
- command-injection
- api-security
- mobile-security
- supply-chain
tags:
- imported
- documents
- access-control
- command-injection
- api-security
- mobile-security
- supply-chain
language: en
raw_sha256: 0180ddbd944417c924f84933ab139006a89dd34bb4d824a1444644ae3bb1720e
text_sha256: 8c00437df1f64b96b1c79f5956ff318b0b1f1ab6f3ba4a2104bf9a62da8d0715
ingested_at: '2026-06-28T07:32:22Z'
sensitivity: unknown
redactions_applied: false
---

# Leveraging Android Permissions: A Solver Approach

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-20_leveraging-android-permissions-a-solver-approach.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, api-security, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:22Z
- Redactions Applied: False
- Raw SHA256: `0180ddbd944417c924f84933ab139006a89dd34bb4d824a1444644ae3bb1720e`
- Text SHA256: `8c00437df1f64b96b1c79f5956ff318b0b1f1ab6f3ba4a2104bf9a62da8d0715`


## Content

---
title: "Leveraging Android Permissions: A Solver Approach"
url: "https://blog.thalium.re/posts/leveraging-android-permissions/"
final_url: "https://blog.thalium.re/posts/leveraging-android-permissions/"
authors: ["Jérémy Breton"]
programs: ["Google (Android)"]
bugs: ["Android", "Local Privilege Escalation"]
publication_date: "2023-06-20"
added_date: "2023-06-21"
source: "pentester.land/writeups.json"
original_index: 1029
---

# Leveraging Android Permissions: A Solver Approach

The work presented in this post was part of an **internship** carried out in 2022 within Thalium.

## Table of Contents

  * Introduction
  * Case study: CVE-2021-0307
  * Exploitation overview
  * Root cause
  * Fix
  * Solver Approach
  * Modelling
  * Vulnerability Research
  * Proof of Concept
  * Conclusion

# Introduction

Since its inception, Android has identified applications as a security threat. As a consequence, applications run in a sandboxed environment, leveraging various Linux mechanisms, as well as access control mechanisms known as [permissions](https://developer.android.com/guide/topics/permissions/overview).

Whenever an application needs access to resources owned by the system or other applications, it usually must be granted the permissions to do so. Those permissions must be declared in the application’s manifest, and depending on their protection level, they sometimes require user consent.

Starting from Android Marshmallow (API level 23), runtime permissions protect privacy sensitive assets such as access to the camera or phone calls related data. These permissions are system-defined, contrary to application-defined ones, which are called **custom permissions**.

Granting runtime permissions requires user consent. To smoothen user experience, runtime permissions are grouped, and if a permission of a group has been granted, then every requested permission from this group would be **mechanically** granted.

To add an extra layer of security, Android 11 (API level 30) implements a feature called [**one-time permission**](https://developer.android.com/training/permissions/requesting#one-time). A few runtime permissions — microphone, location and camera — may be granted once to an application. The permission is automatically revoked when the application is stopped, or after a short while.

This new feature does not seem to have been the subject of specific research and thus has caught our attention. To sum up, permissions:

  * are either _defined by an application_ (**custom**), or _by the system_ (**system**).
  * have a _protection level_ such as **normal** , **dangerous** , **signature** or **special**.
  * can be _part of a group_.

The logic of the rules behind this system are mostly implemented in two framework services: _PermissionManagerService_ and _PackageManagerService_.

Recently, those components have suffered from several vulnerabilities [that were found through fuzzing](https://ieeexplore.ieee.org/document/9519385). They led to critical privilege escalation without user consent.

In this blog post, we first present a case study of a permission management vulnerability. Then, we describe the solver approach we followed to help in the vulnerability research. Eventually, we explain a new vulnerability that was discovered thanks to the solver, and which was reported to Google.

# Case study: CVE-2021-0307

A malevolent application could leverage CVE-2021-0307 to silently obtain any system permission part of a group. Android 10 and 11 were affected by this vulnerability.

## Exploitation overview

Three applications are needed: _app-exp_ , _app-eop_ and _app-exp-update_. The permissions defined or used in the respective manifests are the following:

  * App-exp:

  
  
  <!-- Defines custom permission as normal -->
  <permission android:name="com.example.cve0307.perm" />
  

  * App-eop:

  
  
  <!-- Use custom permission and system permission PHONE -->
  <uses-permission android:name="com.example.cve0307.perm" />
  <uses-permission android:name="android.permission.CALL_PHONE" />
  

  * App-exp-update:

  
  
  <!-- Re-defines custom permission as dangerous and grouped with PHONE -->
  <permission android:name="com.example.cve0307.perm"
  android:protectionLevel="dangerous"
  android:permissionGroup="android.permission-group.PHONE">
  </permission>
  

The actions to perform are:

  1. Install _app-exp_
  2. Install _app-eop_
  3. Uninstall _app-exp_
  4. Install _app-exp-update_

The _PHONE_ group is then granted to _app-eop_ without the user having authorized it.

## Root cause

The _PackageManagerService_ refreshes the registration and the granting status of all permissions, when an application is updated or uninstalled; if a dangerous custom permission definition is removed during this process, its grants will also be revoked from applications. Therefore, if a normal or signature custom permission definition is removed, the applications will keep the granted status.

If an application defines a normal or signature custom permission, and the application defining it is uninstalled, the applications requesting it will keep the granted status as normal or signature. Therefore, if the user installs an application which redefines the custom permission, the applications that have the granted status will be allowed to use the permission without the user’s consent, even if the redefined permission is now dangerous.

In the proof of concept, _app-exp_ defines a normal custom permission, which is requested by _app-eop_. Then _app-exp_ is uninstalled, consequently _app-eop_ will keep the granted status of _com.example.cve0307.perm_ as normal, even if the permission is not defined. Later, if an update of _app-exp_ (_app-exp-update_) is installed, and redefines the custom permission as dangerous and belongs to the permission group _PHONE_ ; _app-eop_ requests the dangerous _CALL_PHONE_ permission and will be allowed to use it without the user’s consent.

## Fix

Google fixed the issue by making sure the install permissions status are revoked when the application that defined them is uninstalled.

# Solver Approach

To model the Android permission system, our choice is to use [Clingo](https://potassco.org/), an open-source answer set programming (ASP) system. Answer set programming is a declarative programming paradigm used for solving logic problems.

Clingo allows users to specify a problem in a high-level language, and then automatically translates that specification into a set of logical rules that can be used to reason about the problem. By setting rules and facts, Clingo will find all possible “answer sets” that satisfy them.

Here is an example:
  
  
  innocent(Suspect) :- motive(Suspect), not guilty(Suspect).
  motive(harry).
  motive(sally).
  guilty(harry).
  

A solution to the above rule and the three facts is the answer set containing all three facts as well as the proposition _innocent(sally)_.
  
  
  > clingo example.lp
  clingo version 5.4.1
  Reading from example.lp
  Solving...
  Answer: 1
  motive(harry) motive(sally) guilty(harry) innocent(sally)
  SATISFIABLE
  
  Models  : 1
  Calls  : 1
  Time  : 0.004s (Solving: 0.00s 1st Model: 0.00s Unsat: 0.00s)
  CPU Time  : 0.001s
  

## Modelling

The goal of modelling the Android permission system is to find new design vulnerabilities, but first we need to model this system.

As clingo generates answer sets, we give the parameters which will be used as bounds in the model, such as the number of applications and permissions that we want to generate, and how many actions are possible.

Next, through facts and rules, we define applications, permissions, manifests and the number of actions. The possible actions are: `install`, `uninstall`, `run`, `stop`, `grant`, `grantAuto`, `grantOneTime`, `update`, `reboot`.

The important part is the definition of the system’s behavior. The easiest way to be in line is to perform tests by developing simple applications and transcribing them in the model. Later, to refine the model, the Android Open Source Project (AOSP) can be used.

For example, the model must be in line either when a permission is updated or after a system reboot, which is typically an action that cannot be easily performed using an application.

The following model’s snippet defines that: _“If at step S the install action of an application A with a manifest M is performed, then the application with its manifest is installed at S+1. And if an application is not installed, then the run action can not be performed.”_
  
  
  installed(A,M,S+1) :- install(A,M,S).
  :- run(A,S), not installed(A,_,S).
  

Many rules must be defined in the system. The more accurate the model is, the more likely the discovery of a vulnerability. To that end, the CVEs can be of precious help, either to try to find them, or to improve our modelling.

This leads to the question _“how to find a vulnerability”_ with the model.

## Vulnerability Research

To find a vulnerability, constraints must be defined. Here, a vulnerability would be to have a permission granted while the _grant_ action has not been performed.
  
  
  # grant action can not be performed
  :- grant(_,_,_).
  
  # system permission is granted to app user at the end
  :- not granted(A, P, S), A=userApp, P=systPerm, S=step+1.
  

So, if Clingo finds a solution where a system permission is granted after `S` actions, there is an issue. Armed with this method, we can try to rediscover CVEs, and then try to find new bugs. Since Clingo’s output can be messy, we made a [helper tool](https://github.com/Ghizmoo/DroidSolver) to simplify it.

With a model in line with the latest AOSP, many solutions are found but they can be grouped under one. One of these solutions is the following:
  
  
  Solving...
  Answer: 1
  install(2,3,1) run(2,2) grantOneTime(2,1,3) grantAuto(2,2,4) stop(2,5) run(2,6) grantAuto(2,1,7)
  SATISFIABLE
  
  Models : 1+
  

The output is simplified for better understanding, but it tells us the steps to perform:

  1. Install user app (2) which defines dangerous custom perm (2) which is grouped with a system perm (1), and use these two perms.
  2. Run the app (2).
  3. Do a one-time grant of the system perm (1) to the app (2).
  4. The custom perm (2) is mechanically granted to the app (2) while requesting it.
  5. Stop the app (2).
  6. Run the app (2).
  7. The dangerous perm (1) is mechanically granted to the app (2) while requesting it.

This is potentially a vulnerability because a dangerous permission is granted after some actions, while the `grant` action has not been performed by the user.

# Proof of Concept

For the sake of testing, let’s define a custom permission belonging to the same group as _android.permission.CAMERA_ :
  
  
  <permission android:name="com.example.cp"
  android:protectionLevel="dangerous"
  android:permissionGroup="android.permission-group.CAMERA" />
  
  <uses-permission android:name="com.example.cp"/>
  <uses-permission android:name="android.permission.CAMERA" />
  

Once installed, the application may turn the _android.permission.CAMERA_ one-time grant into a permanent grant.

[![PoC CVE-2023-20947](/posts/img/leveraging-android-permissions/poc.png)](/posts/img/leveraging-android-permissions/poc.png)

  1. The malicious application requests for _android.permission.CAMERA_.
  2. Android checks if there is any granted permission which is in the same group, but there is none: it asks the user to give or deny consent.
  3. The user gives a one-time consent: the granted permission will be revoked after a period of time. Exactly when it is revoked depends on a few conditions listed in the Android documentation.
  4. The malicious application requests for _com.example.cp_ , which is a custom permission defined by itself, and member of the same group as _android.permission.CAMERA_ ; the permission is mechanically granted, without the user knowing.
  5. After force killing the application, _android.permission.CAMERA_ is automatically revoked by Android. As detailed before there are a few other configurations that lead to this behavior.
  6. The malicious application requests _android.permission.CAMERA_ again. The previous grant has been revoked, but this time the application already has a permission in the same group, the custom permission _com.example.cp_ it purposely defined and had granted previously. **The user is not asked for their consent, and the runtime permission is silently granted**.

To sum up, there is an issue where an app can get a permission A granted permanently while the user granted it _one-time_. If the user has granted a _one-time_ permission A, which is in the same group as permission B, then the permission B is granted permanently without user interaction. The app can then further use that permanent grant on permission B to get the permission A granted permanently.

Android 11, 12 and 13 have been tested, and they exhibit the same behavior. The issue was reported and assigned **CVE-2023-20947**.

# Conclusion

A solver approach led to the discovery of a vulnerability in the Android permission system. However, the model is not perfect: it does not necessarily represent the system perfectly, and still has room for improvement. The more accurate the model, the better our chances at finding a vulnerability.

The Android permission system is one of the applications where the solver approach is interesting, but that can be applied to many systems, and a variety of other interesting tools could be explored, such as [Prolog](https://www.swi-prolog.org).

[#Android](/tags/android)

[#Permissions](/tags/permissions)

[#CVE](/tags/cve)

[#Vulnerability Research](/tags/vulnerability-research)

2023-06-20 by Jérémy Breton
