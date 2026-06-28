---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-31_reversing-uk-mobile-rail-tickets.md
original_filename: 2023-01-31_reversing-uk-mobile-rail-tickets.md
title: Reversing UK mobile rail tickets
category: documents
detected_topics:
- mobile-security
- sso
- jwt
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- mobile-security
- sso
- jwt
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: f4d2fc5b9d74a4324225ed72ee02c60bf1bf0caeb354aeed2538fc2cce2efc2f
text_sha256: 6f5b30bb7050c021019b3f0437ad54e57338e01cc6bb3930191ef88cc9d2c5d5
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: true
---

# Reversing UK mobile rail tickets

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-31_reversing-uk-mobile-rail-tickets.md
- Source Type: markdown
- Detected Topics: mobile-security, sso, jwt, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: True
- Raw SHA256: `f4d2fc5b9d74a4324225ed72ee02c60bf1bf0caeb354aeed2538fc2cce2efc2f`
- Text SHA256: `6f5b30bb7050c021019b3f0437ad54e57338e01cc6bb3930191ef88cc9d2c5d5`


## Content

---
title: "Reversing UK mobile rail tickets"
url: "https://eta.st/2023/01/31/rail-tickets.html"
final_url: "https://eta.st/2023/01/31/rail-tickets.html"
authors: ["Zeeshan Mustafa (@by6153)"]
bugs: ["Reverse engineering", "Android"]
publication_date: "2023-01-31"
added_date: "2023-02-16"
source: "pentester.land/writeups.json"
original_index: 1600
---

# Reversing UK mobile rail tickets

2023-01-31 · [permalink](https://eta.st/2023/01/31/rail-tickets.html)

The UK has used small credit-card sized tickets to pay for train travel for years and years, since long before I was born — originally the [APTIS ticket](https://en.wikipedia.org/wiki/APTIS_ticket_features)1, which later got replaced by a [slightly easier to read version](https://en.wikipedia.org/wiki/2014_National_Rail_ticket_features) printed onto the same stock.

![a National Rail paper ticket](/assets/img/rsp6/ticket.jpg)

Nowadays, the industry would very much like you to ditch your paper ticket in favour of a fancy mobile barcode one (or an [ITSO](https://en.wikipedia.org/wiki/ITSO_Ltd) smartcard2); not only do they not have to spend money on printing tickets but they also gain the ability to more precisely track the ticket’s usage across the network and minimise fraud.

![promotional material about the benefits of mobile ticketing](/assets/img/rsp6/why-mobile.png)

There are obvious benefits for the user too — I’m willing to bet most people use the mobile tickets anyway, since they’re just easier if you’re booking your train travel in an app like [Trainline](https://www.thetrainline.com/).

But what data is inside the barcode of a mobile ticket, and how do they work? Could people who aren’t ticket inspectors get the data out of them? It turns out that the answer is a bit more interesting than I initially expected!

## Initial explorations

A mobile ticket is just an [Aztec barcode](https://en.wikipedia.org/wiki/Aztec_Code), either displayed inside an app or on a PDF you can print out:

![image of a Trainline ticket barcode, from Cathays \(CYS\) to Cardiff Queen St \(CDQ\), UTN TTDNQMCQF6S](/assets/img/rsp6/initial-ticket.png)

Googling around for prior work people had done decoding mobile tickets, I found [a bunch of discussion](https://de.wikipedia.org/w/index.php?title=Diskussion:Online-Ticket&oldid=198973306#Barcode) (German-language link) about UIC 918.3, a specification used by the German railway company Deutsche Bahn for their e-tickets. These also use the Aztec barcode format and looked superficially similar — and some people had already written code to read them. Maybe this could work?

(Why would I expect this to work? Well, the UIC is the international standards body for railways — in Europe at least — so it’s reasonable to assume they might’ve used a standard format here.)

However, the formats are sadly nothing alike — decoding our UK barcode using [zxing](https://github.com/zxing/zxing), we get:
  
  
  06DNQL4XHVK00TTRCGPUQWNTHPGHWBPOUTKRWXAJKGHFBAPBCTOGUZQVTZTKKDEBQXPGRWZJRJBXJZPOHNJGIPDJWEGYWJXLVPGEEZBCUUELIJMOINPRZMSDQCZJGLIZLUTQHXMTPKWCMJISUXQLORAOVYXSOLGXXGMVUDXTMHAYMBLUTKPUPFCRNNTDBBDLN***REDACTED-SUSPECT-TOKEN***…which looks nothing like you might expect a UIC barcode to look, given the latter are supposed to start with “#UT” (according to the discussion in German earlier).

In fact, this is a custom standard that is only used inside the UK, as the “06” at the start of the data hints at; this is an “RSP-6” ticket (as in RSP for [Rail Settlement Plan](https://en.wikipedia.org/wiki/Rail_Settlement_Plan)), which Google doesn’t seem to know much about. It is possible to find a [Freedom of Information Act request](https://www.whatdotheyknow.com/request/rsp_6_specification_for_barcodes_2) someone made asking for the spec that never got a response — sadly the Rail Delivery Group (RDG), technically a private company, doesn’t actually have to respond to such requests, so I’d have to figure this out myself.

## A friendly wolf comes to help

At this point, I basically had no idea how to continue. Comparing multiple tickets, the data seemed to be mostly random apart from some fixed headers, suggesting that it was probably encrypted in some way — I couldn’t just get lots of tickets and hope to find similarities between them.

![photo of 'binwalk -W cdq-cys.bin pad-aml.bin', showing no shared data apart from a few random bytes and some headers](/assets/img/rsp6/binwalk.png)

_image: output of`binwalk -W cdq-cys.bin pad-aml.bin`, which highlights similarities and differences between two tickets3_

My friend Harley (“[unlobito](https://lobi.to/)”) had noticed me complaining about tickets in a shared group chat and had a clue for me: the word “masabi”, which turned out to be the name of [a ticketing company](https://www.masabi.com/).

Masabi’s website has [this lovely page](https://www.masabi.com/justride-uk-rail/) where they explain all about how they invented mobile ticketing in the UK in 2007 and how the RSP6 national standard was actually written by them! They also boast about how their “JustRide Inspect” suite of apps can be used to decode these tickets.

![Masabi promotional copy about their Inspect app](/assets/img/rsp6/justride-web.png)

We sadly can’t just get this app off the Play Store. However, after some googling around you can totally get it from one of those less than official APK rehosting websites.

With the APK in hand there are a number of things we can do. We can just install it on an Android device and see whether it’ll give up anything interesting that way; we can also try to “decompile” it, to get a better idea of how the app (and the ticket parser) works.

## Running the app

Since I didn’t have any spare throwaway Android phones and that the APK might be malware, my first step was to just run it inside an [Android Virtual Device](https://developer.android.com/studio/run/managing-avds) (using the emulator in Android Studio). I reckoned this would be a bit safer than just installing it on my main Android phone.4

After a bit of fiddling about, I had it doing something:

![Inspect app showing "Scan config barcode" screen](/assets/img/rsp6/app-screen1.png)

Unfortunately, this wasn’t very useful — it wouldn’t scan standard ticket barcodes in this form. The “Login manually” button lets you choose a Train Operating Company (TOC) to sign in as (some of the companies mentioned don’t even exist any more!), which was pretty interesting but not useful for our goals:

![Inspect app showing list of TOCs](/assets/img/rsp6/app-screen2.png)

I don’t work for a train operating company, so clearly it wasn’t going to be possible for me to proceed5. Maybe examining the app another way could get us somewhere?

## Decompiling the app

You can point Android Studio at an APK and have it analyse what’s inside. Sort of.

If you try this (via the 3-dot menu in the project chooser → “Profile or Debug APK”), you get something that’s not entirely useful: a bunch of weird looking “smali” files.

![Android Studio showing debug view of the APK](/assets/img/rsp6/smalis.png)

This is because the APK only contains compiled bytecode, rather than any useful source code; as the yellow warning banner notes, this is stored inside the APK in [.dex format](https://source.android.com/docs/core/runtime/dex-format) (“Dalvik Executable”, where Dalvik is the name of the Android VM), and [smali](https://github.com/JesusFreke/smali) is just a human-readable representation someone invented for this format (like Assembly).

What we ideally need is something that can turn the bytecode all the way back into Java. Such a tool exists in the form of [jadx](https://github.com/skylot/jadx), a very handy tool that not only does just that, but can also do a bunch of other cool stuff like outputting a project Android Studio can load (and theoretically compile)!
  
  
  $ jadx --deobf -e -d out ~/Downloads/justride-inspect.apk
  INFO  - loading ...
  INFO  - processing ...
  INFO  - done  
  $ ls out/
  app  build.gradle  settings.gradle
  

## Making sense of the decompiled output

When I looked in jadx’s output directory I found a perfect copy of the original source code that Masabi had written, and my job was then very easy. Wait, no, that’s a lie.

Before shipping an APK to the end user, Android app developers usually run it through a number of steps to make it smaller including “obfuscation” — turning long class and member names like “mContext” into the smallest string they can get away with, like “a”. This means that the code jadx generated is rather hard to make sense of:
  
  
  public class TicketInspectActivity extends BaseActivity implements InterfaceC2526a {
  
  /* renamed from: c */
  private ViewPager f4615c;
  
  /* JADX INFO: Access modifiers changed from: private */
  /* renamed from: h */
  public C2496p m1419h() {
  return (C2496p) this.f4615c.getAdapter();
  }
  
  @Override // com.masabi.app.android.ticketcheck.activities.BaseActivity
  /* renamed from: a */
  public final void mo1410a() {
  super.mo1410a();
  if (isFinishing()) {
  return;
  }
  m1419h().m1467a(this.f4615c.getCurrentItem());
  }
  /* ... */
  }

Mmm yes, I knew exactly what they meant when they named their class `C2496p`. Of course! We just need to trace the execution of `void mo1410a()` and then we’ll figure it all out!6

Despite this looking daunting at first it’s actually quite okay with the tools Android Studio gives us. Not everything is completely obfuscated: some class names need to be left deobfuscated, such as activities (like this `TicketInspectActivity`). That lets us get some idea of where to start. The code also occasionally contains error messages that give away what the classes and methods are supposed to be:
  
  
  /* renamed from: com.masabi.c.a */
  /* loaded from: classes.dex */
  public final class C2666a {
  /* renamed from: a */
  public static final int m552a(Calendar calendar) {
  if (calendar == null) {
  System.err.println("DateTimeUtils.packDate() ERROR - Attempt to pack a null date!");
  }
  return (C2668c.m542a(calendar) << 16) | (C2667b.m548a(calendar) & 65535);
  }
  /* ... */
  }

In this case, the log line lets us instantly rename `C2666a` → `DateTimeUtils`, and `m552a` → `packDate`.

Android Studio also has excellent support for doing renames across an entire codebase at once, so after a long afternoon picking things apart it quickly started to take shape and our obfuscated code began to look something like the original source code might have looked7.

![the Refactor → Rename menu in Android Studio](/assets/img/rsp6/refactor-this.png)

## Interesting uses of RSA

My investigations into the app confirmed my suspicions that the data was indeed encrypted — well, not quite. Technically, the ticket data is actually _signed_ with RSA and [PKCS#1](https://en.wikipedia.org/wiki/PKCS_1) (I think). Ticket issuers generate a payload containing the ticket data, pad it a bit, and then use their RSA private key to create a signed message they put into the barcode. A ticket scanner has a set of the issuers’ public keys on hand to verify the signature and read the original payload.

As a more concrete example, some vague Rust code to do the verification and reading steps looks a bit like this:
  
  
  // BigUint is an arbitrary size unsigned integer.
  // The ticket is base26 encoded, so we need to undo that first:
  let ticket: BigUint = base26_decode(&ticket_str[15..]);
  // this is doing “S^e mod N”;
  // i.e. part of RSA signature verification
  let message = ticket.modpow(&key.public_exponent, &key.modulus);
  // convert big integer into raw bytes (big-endian)
  let message: Vec<u8> = message.to_bytes_be();
  // attempt to strip PKCS#1 padding; if it fails, the key is wrong
  if let Some(unpadded) = strip_padding(&message) {
  eprintln!("[+] decrypt done: {:?}", unpadded);
  }

I’m not a cryptographer, so this was all somewhat new to me! I was used to signatures being a [hash](https://en.wikipedia.org/wiki/Hash_function) of the original message (i.e. you’d send the plaintext, and then `sign(hash(plaintext))` along with it), which is usually done so that you can [sign messages longer than the size of your keys](https://crypto.stackexchange.com/questions/9896/how-does-rsa-signature-verification-work). In this case, they’ve put the _whole_ message inside the signature to save space on the barcode, meaning you need the public keys to read the message at all.

You also can’t make your own fraudulent tickets using this scheme; you’d need the RSA private key of one of the ticket issuers to do that, or to have a custom public key added to the network of gate readers and ticket inspectors’ apps, neither of which seem easy to do.

Some further details on the cryptography (click to expand)

How can you tell that the ticket payload was unwrapped correctly? The payload is padded in a way that I think corresponds to some of the algorithms in PKCS#1 (see [RFC 8017](https://www.rfc-editor.org/rfc/rfc8017)); it'll either be

Scheme 1: `padded = [0x00, 0x01, padding-string, 0x00, message]`  
(where `padding-string` is a length of `0xFF` octets) 

or 

Scheme 2: `padded = [0x00, 0x02, padding-string, 0x00, message]`  
(where `padding-string` is a length of random non zero octets) 

If the payload doesn't look like either of these, the RSA operation failed, so you probably have the wrong key and should try another one.

So the public keys are required knowledge for actually being able to decode these tickets. Where do we get those from?

## Obtaining the elusive public keys

The public keys aren’t really published anywhere obvious, and reversing the Masabi app seems to indicate that it downloads the keys from a configuration server once you scan the config barcode mentioned earlier.
  
  
  Global.logger.log(getClass().getSimpleName(), "loadAllKeys() - Fetched " + barcodeKeysList.length + " barcode keys from metadata");
  for (int i = 0; i < barcodeKeysList.length; i++) {
  AbstractJSONObject key = (barcodeKeysList[i2];
  if (ExtendedGlobal2.clock.getCurrentTime() < Global.f4949d.mo915a(key.getString("expiryDate")) * 1000 &&
  (decoder = makeDecoder(key.getString("issuerId"), key.getString("ticketType"), key.getString("modulus"), key.getString("exponent"), key.getLong("mQ"))) != null) {
  decoders.addElement(decoder);
  }
  }

You’d think this would be a dead end, since we don’t have any login credentials — but they also just left some keys inside the APK as well. As far as I can tell no part of the app actually reads these; maybe it did in the past, or maybe they used them for testing and forgot to take them out of the production version of the app.
  
  
  $ find . | grep 'keys' | grep rsp6
  ./app/src/main/assets/keys/rsp6_rsa_ao.dat
  ./app/src/main/assets/keys/rsp6_rsa_ua.dat
  ./app/src/main/assets/keys/rsp6_rsa_tt-qa.dat
  ./app/src/main/assets/keys/rsp6_rsa_tt.dat
  ./app/src/main/assets/keys/rsp6_rsa_t3.dat
  ./app/src/main/assets/keys/rsp6_rsa_t2.dat
  

The keys are split up by ticket issuer, a 2-character code that forms the first part of the ticket ID. This ticket from earlier was issued by Trainline, who have issuer code **TT** …

![barcode of the earlier ticket](/assets/img/rsp6/initial-barcode.png)

…and the keys to decode this ticket are in `rsp6_rsa_**tt**.dat`. Nice!8

This is only a subset of all the keys that are being used today though, as I quickly discovered when [unlobito](https://lobi.to/) gave me an [Avanti West Coast](https://www.avantiwestcoast.co.uk/) ticket to decode. The copy of the app I have is only from 2016 and a bunch more TOCs have started issuing mobile tickets since then!

## ttkMobile

Around when I was figuring all of this out [puck](https://twitter.com/puckipedia) pointed me towards the website for [The Ticket Keeper](http://info.theticketkeeper.com/), another firm who makes ticket validation and issuance tooling. They have an iOS app for ticket inspectors called **ttkMobile** , which you can just [download straight off the App Store](https://apps.apple.com/gb/app/ttkmobile/id921166994) and use to start validating tickets at home!9

![screenshot of ttkMobile](/assets/img/rsp6/ttkmobile.jpg)

Important note if you actually intend to use this app (click to expand)

Be warned!

If you install this app, you can’t ever uninstall it and expect it to work after a reinstall. On first load it registers your device UUID with some server and generates a random password that it stores in local storage. Uninstalling the app removes the password, but your device UUID doesn’t change, so next time you reinstall, it won’t be able to authenticate and it’ll be useless (since it needs to grab keys and stuff to work).

(“But wait,” I hear you cry, “isn’t getting a persistent device ID exactly what Apple don’t want you to do?” And you’d be right! Technically, I believe the device UUID actually _does_ change between installs, but they store a copy in the device keychain, which doesn’t get wiped when you remove the app. This is stupid, and almost certainly a contravention of App Store policy.)

I don’t have an iPhone, but some of my friends do. unlobito and another friend, Eva (“[thejsa](https://muffinti.me/)”), had a poke around and managed to get me a DRM-free10 [`.ipa`](https://en.wikipedia.org/wiki/.ipa) containing the app, which I could unwrap and decompile with the help of [Ghidra](https://ghidra-sre.org/). This let me figure out some of the pieces of the ticket that the Masabi app didn’t look at.

[thejsa](https://muffinti.me/) also spent some time running the app through a proxy in order to find out how it communicates with the server11, and it turns out there’s just an endpoint where you can get all of the public keys:
  
  
  $ curl 'https://device.theticketkeeper.com/download_keys?device_name=abc' | jq .
  {
  "return_code": "ok",
  "message": null,
  "keys": {
  "AA": [
  {
  "valid_from": "20000101000000",
  "valid_until": "29991231000000",
  "public_exponent_hex": "10001",
  "modulus_hex": "9140AA61F7D9A2E943C0510BACA5FA9CA7D12D78E301A36D640F2D28D8C0AA4D6A7102555CECF138E467730B797509EC1AB5BBA77CA6384BC8F483F609B121E75AE42660EDFE15EF91ADD4DA68C355F830FAAC6FFB25FBCFE1E61C7AF37C4AE8C85E264C151BD9C9AA4DE41D2756A9E260C0CC89AE2ADDD19E452A675E88DA47",
  "public_key_x509": null,
  "test_only": "N",
  "updated": "20200313175331"
  },
  [etc]
  

As I mentioned earlier, this is crucial information to be able to decode tickets at all, so thanks go to The Ticket Keeper developers for making it available so easily!

### Brief aside on freedom of information

I don’t know whether people in the industry (e.g. the Rail Delivery Group) will be upset with me publishing this information or not. I hope they won’t be: I really think the public keys should be made available to the public, along with the official specifications for decoding. The tickets are signed, so it’s not as if there’s any practical danger — people can’t use this to start forging tickets en masse, for example — and there are lots of potential innovative uses for this data. Imagine for example a journey logger that used ticket scans to track where you’d been automatically, or an expenses system that used the price information encoded in the ticket to automatically log expense requests!

The railways might be run by a consortium of private companies, but they are in effect a public service owned and controlled by the Government12 (as of Jan 2023), so they really should be subject to the same Freedom of Information Act provisions as other public bodies.

Some people in the industry already have the right idea; in conversation with one of the Ticket Keeper developers over email, I was made aware that the ttkMobile app being public along with some of this data is actually an intentional choice, which is really nice to see!

### Bonus: eTVD logs

The website also tells you how they have an electronic Ticket Validation Database ([eTVD](http://info.theticketkeeper.com/services/etvd/)) that has a copy of all ticket scans at gatelines and by people using their app. This is the anti-fraud thing I mentioned at the very start; this sort of data is presumably very useful to revenue protection staff trying to figure out systematic fare evasion, like short-faring13.

What it doesn’t tell you, though, is that the app will also give you this information unauthenticated, with nothing more than a ticket’s ID (!).

This was reported to the developers as a possible security issue / data leak on 2023-01-19. They confirmed it was intended behaviour, but agreed that it would probably be a good idea to restrict it; I'm told this will happen soon. 

This information can be quite disturbingly detailed, even pinpointing the exact username of the inspector who scanned you, where you were scanned, on what exact train service you were scanned, whether it succeeded, and a bunch more stuff. Helpfully it’ll also sometimes give you the entire barcode data, and what the ticket server thinks it decodes as, too!
  
  
  # getting scan history information for ticket CBCZSCDPVFF
  # (this is massively cut down; there are more fields in reality)
  $ curl 'https://device.theticketkeeper.com/get_ticket_details?device_name=abc&utn=CBCZSCDPVFF' | jq '.["ticket_detail"]["scans"]'
  [
  {
  "event_time_iso": "2022-06-10T18:30:47",
  "created": "2022-06-10T18:30:48",
  "device_type": "ttkMobile",
  "device_id": 1001,
  "device_name": "f95396f5-da22-47f9-8e85-dff4b2294a5d",
  "device_alias": "2021-TK10212",
  "username": "JLazlo01",
  "action_name": "Accepted",
  "rsp_action_code": 4001,
  "event_trigger": "scan",
  "scan_mode": "clip",
  "scan_nlc": "2728",
  "validation_result": "warning",
  "message_displayed": "16-25 Railcard",
  "gate_id": "OPN-3002i[021502]",
  "latitude": 51.7824963,
  "longitude": -0.2141781,
  "device_scan_id": 74402,
  "train_uid": "L77572",
  "departure_date": "2022-06-10",
  "barcode": "06CZSCDPVFF00…",
  "train_info": "Fr1803 KGX-SKI 1D26/GR2600",
  # etc
  },
  # etc
  ]
  

So yeah, your ticket barcode — or its ID, which is often written below the code in plain text — might let someone access a surprising amount of detailed tracking information as to where you are and what trains you’re taking! (Rather like [the booking reference they send you when you book a flight](https://mango.pdf.zone/finding-former-australian-prime-minister-tony-abbotts-passport-number-on-instagram).)

## Trying this out for yourself

With the decompiled Masabi app and the ttkMobile app together, it wasn’t too hard to work out a vague idea of what the ticket format was like. I’ve put together [a small repository](https://git.eta.st/eta/rsp6-decoder) with a Rust tool to decode a ticket, as well as a small spec with my best guess on what all the fields mean.

There’s also a [funky web tool](https://eta.st/tickets/) I threw together in an evening or so that’ll let you point your phone at a barcode (or upload a screenshot of one) and give you a relatively nice readout of what data’s inside. [Give it a try!](https://eta.st/tickets/) (If you need a barcode, feel free to scroll up and use the one from this post!)

Sorry, your browser doesn't support embedded videos. 

Do feel free to [get in touch](/#contact) if you find anything interesting or need help understanding something about the format!

## Acknowledgements

Thanks to [unlobito](https://lobi.to/), [puck](https://twitter.com/puckipedia), and [thejsa](https://muffinti.me/) (and assorted others in various chatrooms) for their help with all of this; go check those people out, too!

* * *

### Footnotes

  1. I still have fond memories of getting these as a child for local journeys to London Waterloo! ↩

  2. [This talk](https://lobi.to/talks/papertickets/) is a decent overview of the mess that is ITSO, if you’re interested. ↩

  3. I did try with more than just two tickets, but that’d make for an unwieldy image. ↩

  4. A VM provides a _decent_ level of protection against running untrusted code, but it’s not the end-all and be-all; I’d imagine the Android emulator isn’t exactly hardened against people trying to break out, so this probably isn’t a bulletproof strategy for running shady apps in the general case. ↩

  5. It turns out that the app actually downloads a lot of the keys and data necessary to decode tickets using this login, so even if I could somehow glitch it into starting the main ticket scanner, it wouldn’t have worked. ↩

  6. jadx has made things slightly easier for us by renaming some identifiers (“deobfuscation”): adding some numbers and adding prefixes like “C” for “class” that help us distinguish amongst the multitude of things called “a” or “b”. ↩

  7. It’s impossible to know without the real source what all the classes were actually called, but I can give them names that make sense to _me_ , and that’s all that matters really. puck actually did manage to find an app that used some classes from the Masabi SDK that was not obfuscated later on, which let me compare and see how accurate my invented names were against the real ones! ↩

  8. The format of these .dat files is a bit weird and nonstandard, and you have to reverse the RSA decryption code to figure out what it is. Or, you can be lazy like me, and just paste the decompiled code into a new Java project and treat it as a black box. ↩

  9. It does expect to report back completed ticket scans by default, so you have to futz around and listen to it complain a bit before it’ll work. Also, the “Ticket Issuing” button doesn’t work, if you were wondering; you need a login for that. ↩

  10. As I understand it, you usually need a jailbroken phone to do this. Otherwise, you could just copy paid apps between phones and share them with people who hadn’t paid for them. ↩

  11. This is also how she discovered the reason why the app doesn’t work after being uninstalled. She even went so far as writing a jailbreak tweak to change the device ID to make it work again, which is pretty cool! ↩

  12. Yes, our railway looks privatised on the surface, but COVID actually resulted in so-called [Emergency Recovery Measures Agreements](https://www.gov.uk/government/speeches/rail-update-emergency-recovery-measures-agreements) that forced the TOCs into effective state ownership and control (they’re now in effect contractors who run the service, rather than taking revenue risk). This means that the Government are actually responsible for things like the current union dispute over jobs and working conditions, despite what some ministers would have you think! ↩

  13. This refers to the practice of buying a ticket that doesn’t actually cover your whole journey (e.g. skipping some stops at the start or end), and gambling that you’ll only get inspected between the stations where it’s actually valid. ↩
