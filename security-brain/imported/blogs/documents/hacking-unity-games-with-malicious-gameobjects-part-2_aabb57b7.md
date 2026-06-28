---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-13_hacking-unity-games-with-malicious-gameobjects-part-2.md
original_filename: 2022-09-13_hacking-unity-games-with-malicious-gameobjects-part-2.md
title: Hacking Unity Games with Malicious GameObjects, Part 2
category: documents
detected_topics:
- supply-chain
- ssrf
- command-injection
- api-security
tags:
- imported
- documents
- supply-chain
- ssrf
- command-injection
- api-security
language: en
raw_sha256: aabb57b7a3f1012ecc02ae5223445f585f78a5ed91d5f2f4d392d5373582ee25
text_sha256: 7c6201bc32f7ec6151409440a187e36aefd4a7e742f41b73452bab0edf5ca7af
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Hacking Unity Games with Malicious GameObjects, Part 2

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-13_hacking-unity-games-with-malicious-gameobjects-part-2.md
- Source Type: markdown
- Detected Topics: supply-chain, ssrf, command-injection, api-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `aabb57b7a3f1012ecc02ae5223445f585f78a5ed91d5f2f4d392d5373582ee25`
- Text SHA256: `7c6201bc32f7ec6151409440a187e36aefd4a7e742f41b73452bab0edf5ca7af`


## Content

---
title: "Hacking Unity Games with Malicious GameObjects, Part 2"
page_title: "Hacking Unity Games with Malicious GameObjects, Part 2 - Include Security Research Blog"
url: "https://blog.includesecurity.com/2022/09/hacking-unity-games-with-malicious-gameobjects-part-2/"
final_url: "https://blog.includesecurity.com/2022/09/hacking-unity-games-with-malicious-gameobjects-part-2/"
authors: ["Jason Kielpinski (@f2jason)"]
programs: ["Unity"]
bugs: ["Arbitrary code execution", "RCE"]
publication_date: "2022-09-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2174
---

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2022/09/gamehacking3-generated_by_OpenAI_DALLE2-1.png?fit=305%2C300&ssl=1)

# Hacking Unity Games with Malicious GameObjects, Part 2

September 13, 2022 — Jason Kielpinski

Hello again!

In the [last post](https://blog.includesecurity.com/2021/06/hacking-unity-games-malicious-unity-game-objects/) I talked about a way I found to execute arbitrary code in Unity using no custom scripts, only built-in components. This allowed potential attacks against Unity games that load AssetBundles from untrusted sources since, although AssetBundles can’t include custom scripts, they _can_ include GameObjects with these built-in components attached. The attack I outlined in that blog used UnityEvents, which are primarily exposed via Unity’s built-in UI elements, but the attack required user interaction to trigger. 

In this post I am going to discuss a zero-click method of triggering UnityEvents, along with some additional things I’ve learned on this topic. I will also introduce a new exploit that does not use UnityEvents and removes one of the limitations of the UnityEvent-based attack (while adding limitations of its own). Finally, I will give some updated remediation thoughts.

## Zero-Click Exploit

I’ve been seeing more and more games using AssetBundles for modding functionality and user-generated content. In some cases these games did not use standard mouse input, or did not use standard ways of rendering UI elements, so getting a user to click a button or a collider was not feasible. I needed another way to prove that this was even a concern for those games. What I came up with is very simple:

  1. Add a Unity UI Toggle, along with an EventSystem
  2. Create an autoplaying animation that toggles the UI Toggle
  3. Unity will fire the onValueChanged UnityEvent when the animation changes the Toggle state

Here is an example of this in action:

![](https://i0.wp.com/blog.includesecurity.com/wp-content/uploads/2022/02/zeroclick.gif?resize=640%2C440&ssl=1)

## Additional Attack

While experimenting with animations for the zero-click exploit, I came across a Unity feature I was previously unaware of: [AnimationEvents](https://docs.unity3d.com/Manual/script-AnimationWindowEvent.html). AnimationEvents let you invoke a function on any components attached to the object running the animation when a certain keyframe in the animation has been reached. The function must have the following signature: `/*(any return type)*/ MethodName( (float|string|int|object|AnimationEvent) param )`.

What’s interesting about this is that, unlike with UnityEvents, you can call a method with _any_ return type. This could open up some possibilities for calling non-void functions that perform useful actions for the attacker. However, the UnityEvent attack discussed in the last post mainly relies on calling static methods, and it did not seem possible to call static methods with an AnimationEvent. Are there any actual attacks, then, that we can pull off using this?

As I briefly mentioned in my last post, GameObjects in AssetBundles can use not only built-in components, but also any components that exist in the project that loads the bundle. Most likely, modders will not have access to the full source code of the game (including meta files containing the script GUIDs), so they won’t be able to use any custom components written by the game developers. However, they _will_ be able to access any components in the game that come from Asset Store assets, as they can simply download these components for themselves. Similarly, they could access any components that come from other public sources (GitHub, etc).

What we need then is for one of these components to have a function of the correct signature that does something interesting. If it could run shell commands or something that would be awesome but it could also be vulnerable in other ways — perhaps making arbitrary HTTP requests from the user’s computer, deleting files, what have you. Trying to come up with an exploit here involves pouring over all of the publicly-available MonoBehaviours in the project for methods with the correct signature. Once you find one that does something interesting, you attach it to the GameObject with the animation and hook it up to the AnimationEvent. This exploitation would be very game specific, depending on what external packages are imported into the project, so there is no generic technique that applies to all games.

You can get creative here, but some things to look for in potentially vulnerable methods might be:

  * `System.Diagnostics.Process` — code execution
  * `Application.OpenURL()` — code execution (described in the last post)
  * `System.Xml.XmlTextReader` — Unity uses .NET 2.0, and all versions of this library prior to 4.5.2 are vulnerable to [XML External Entity (XXE)](https://portswigger.net/web-security/xxe) attacks, so if you can get user input into one of these you can get XXE. In my limited testing, XXE only seemed to work in builds of the game using the IL2CPP scripting backend, not in the Unity editor itself
  * `WWW`, `UnityWebRequest`, etc — HTTP requests
  * `UnityEngine.Windows.File`, `System.IO.File` — deleting/creating/modifying local files

## Vulnerable Versions

I recently discovered that UnityEvents could only call static methods starting with Unity 2020.x — before that, they were limited to methods on concrete MonoBehaviours attached to GameObjects. When testing games based on Unity 2019.x or below, a similar approach would have to be taken for UnityEvents as AnimationEvents — looking through the codebase for publicly-available functions of the correct signature on MonoBehaviours. In this case, AnimationEvents are far more flexible, since they don’t require a void return type, so you might as well just look for methods suitable for an AnimationEvent-based exploit (e.g. methods on a MonoBehaviour-derived class with the correct signature).

## Remediation

In my last post I gave a potential remediation that involved traversing a prefab GameObject and removing any vulnerable components before instantiating. Some people have rightly pointed out that a better approach would be to reject any GameObjects that have denylisted components instead of attempting to sanitize — I totally agree with this. Even better would be to reject any objects containing non-allowlisted components, if feasible. These approaches might look something like this:
  
  
  private static bool ValidateAllowlist(GameObject prefab)
  {
  var allowlist = new System.Type[] {
  typeof(UnityEngine.Transform),
  typeof(UnityEngine.Collider),
  typeof(UnityEngine.MeshFilter),
  typeof(UnityEngine.Renderer)
  };
  foreach (var component in prefab.GetComponentsInChildren(typeof(Component))) {
  bool inAllowlist = false;
  foreach (var type in allowlist) {
  if (type.IsAssignableFrom(component.GetType())) {
  inAllowlist = true;
  break;
  }
  }
  if (!inAllowlist) {
  Debug.LogWarning("Prefab contained non-allowlisted component " + component.GetType().ToString());
  return false;
  }
  }
  return true;
  }
  
  private static bool ValidateDenylist(GameObject prefab)
  {
  var denylist = new System.Type[] {
  typeof(UnityEngine.EventSystems.EventTrigger),
  typeof(UnityEngine.EventSystems.UIBehaviour),
  typeof(UnityEngine.Animation),
  //include these too if you use Bolt:
  //typeof(Bolt.FlowMachine),
  //typeof(Bolt.StateMachine),
  };
  foreach (var componentType in denylist) {
  if (prefab.GetComponentsInChildren(componentType, true).Length != 0) {
  Debug.LogWarning("Prefab contained denylisted component " + componentType.ToString());
  return false;
  }
  }
  return true;
  }
  
  public static Object SafeInstantiate(GameObject prefab)
  {
  if (!ValidateAllowlist(prefab)) {
  return null;
  }
  return Instantiate(prefab);
  }
  
  public void Load()
  {
  string evilpath = Application.dataPath + "/AssetBundles/evil";
  AssetBundle evilab = AssetBundle.LoadFromFile(evilpath);
  GameObject evilGO = evilab.LoadAsset<GameObject>("Exploit");
  SafeInstantiate(evilGO);
  evilab.Unload(false);
  }

I was wondering what kind of performance overhead this might add. To get a rough idea, I created a fairly complex prefab, about 1000 GameObjects with three components each, nested 15 levels deep. Running this a bunch of times and comparing, I found that `SafeInstantiate()` added about 12% overhead compared to plain `Instantiate()`. Prefab sizes are obviously game dependent (e.g. a game that lets you import user-created levels might have prefabs much bigger than that, a game that lets you import user-created avatars much smaller), so mileage may vary on this figure.

As part of vendor coordination we discussed this post with the Unity team, the Unity Security Team has updated their [article ](https://blog.unity.com/news/upm-dependency-confusion-assetbundle-security-in-the-editor)with suggested mitigations and we recommend Unity developers read the [article](https://blog.unity.com/news/upm-dependency-confusion-assetbundle-security-in-the-editor) for further guidance.

### Share this:

  * [ Share on X (Opens in new window) X ](https://blog.includesecurity.com/2022/09/hacking-unity-games-with-malicious-gameobjects-part-2/?share=twitter)
  * [ Share on Facebook (Opens in new window) Facebook ](https://blog.includesecurity.com/2022/09/hacking-unity-games-with-malicious-gameobjects-part-2/?share=facebook)
  * 

### Like this:

Like Loading…

Categories [appsec](https://blog.includesecurity.com/category/appsec/), [gamedev](https://blog.includesecurity.com/category/gamedev/), [games](https://blog.includesecurity.com/category/games/), [hacking](https://blog.includesecurity.com/category/hacking/), [unity](https://blog.includesecurity.com/category/unity/), [unity3d](https://blog.includesecurity.com/category/unity3d/), [vulnerabilities](https://blog.includesecurity.com/category/vulnerabilities/) Tags [games](https://blog.includesecurity.com/tag/games/), [security research](https://blog.includesecurity.com/tag/security-research/), [unity](https://blog.includesecurity.com/tag/unity/), [vulnerabilities](https://blog.includesecurity.com/tag/vulnerabilities/) Post navigation

[Reverse Engineering Windows Printer Drivers (Part 2)](https://blog.includesecurity.com/2022/08/reverse-engineering-windows-printer-drivers-part-2/)

[Mitigating SSRF in 2023](https://blog.includesecurity.com/2023/03/mitigating-ssrf-in-2023/)
