---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-30_wormable-remote-code-execution-in-alien-swarm.md
original_filename: 2020-10-30_wormable-remote-code-execution-in-alien-swarm.md
title: Wormable remote code execution in Alien Swarm
category: documents
detected_topics:
- command-injection
- file-upload
- automation-abuse
- supply-chain
tags:
- imported
- documents
- command-injection
- file-upload
- automation-abuse
- supply-chain
language: en
raw_sha256: c05c0e26077608f24d04c641e3b970d78cce00e2e178c8407da9faaf47d0e004
text_sha256: 36002b76c937986e9d3c81e921c4aac50a85d9e54754dbe6f29eb6787455c4fb
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Wormable remote code execution in Alien Swarm

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-30_wormable-remote-code-execution-in-alien-swarm.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload, automation-abuse, supply-chain
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `c05c0e26077608f24d04c641e3b970d78cce00e2e178c8407da9faaf47d0e004`
- Text SHA256: `36002b76c937986e9d3c81e921c4aac50a85d9e54754dbe6f29eb6787455c4fb`


## Content

---
title: "Wormable remote code execution in Alien Swarm"
page_title: "Wormable remote code execution in Alien Swarm | secret club"
url: "https://secret.club/2020/10/30/alien-swarm-rce.html"
final_url: "https://secret.club/2020/10/30/alien-swarm-rce.html"
authors: ["mev"]
programs: ["Valve"]
bugs: ["RCE"]
publication_date: "2020-10-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4170
---

# Wormable remote code execution in Alien Swarm

![main authors image](/assets/author_img/mev.jpg) [mev](/author/mev)

Oct 30, 2020 

* * *

Alien Swarm was originally a free game released circa July 2010. It differs from most Source Engine games in that it is a top-down shooter, though with gameplay elements not dissimilar from Left 4 Dead. Fallen to the wayside, a small but dedicated community has expanded the game with Alien Swarm: Reactive Drop. The game averages about 800 users per day at peak, and is still actively updated.

Over a decade ago, multiple logic bugs in Source and GoldSrc titles allowed execution of arbitrary code from client to server, and vice-versa, allowing plugins to be stolen or arbitrary data to be written from client to server, or the reverse. We’ll be exploring a modern-day example of this, in Alien Swarm: Reactive Drop.

#  Client <-> Server file upload

Any Alien Swarm client can upload files to the game server (and vice versa) using the `CNetChan->SendFile` API, although with some questionable constraints: a client-side check in the game prevents the server from uploading files of certain extensions such as `.dll`, `.cfg`:
  
  
  if ( (!(*(unsigned __int8 (__thiscall **)(int, char *, _DWORD))(*(_DWORD *)(dword_104153C8 + 4) + 40))(
  dword_104153C8 + 4,
  filename,
  0)
  || should_redownload_file((int)filename))
  && !strstr(filename, "//")
  && !strstr(filename, "\\\\")
  && !strstr(filename, ":")
  && !strstr(filename, "lua/")
  && !strstr(filename, "gamemodes/")
  && !strstr(filename, "addons/")
  && !strstr(filename, "..")
  && CNetChan::IsValidFileForTransfer(filename) ) // fails if filename ends with ".dll" and more
  { /* accept file */ }
  
  
  
  bool CNetChan::IsValidFileForTransfer( const char *input_path )
  {
  char fixed_slashes[260];
  
  if (!input_path || !input_path[0])
  return false;
  
  int l = strlen(input_path);
  if (l >= sizeof(fixed_slashes))
  return false;
  
  strncpy(fixed_slashes, input_path, sizeof(fixed_slashes));
  FixSlashes(fixed_slashes, '/');
  if (fixed_slashes[l-1] == '/')
  return false;
  
  if (
  stristr(input_path, "lua/")
  || stristr(input_path, "gamemodes/")
  || stristr(input_path, "scripts/")
  || stristr(input_path, "addons/")
  || stristr(input_path, "cfg/")
  || stristr(input_path, "~/")
  || stristr(input_path, "gamemodes.txt")
  )
  return false;
  
  const char *ext = strrchr(input_path, '.');
  if (!ext)
  return false;
  
  int ext_len = strlen(ext);
  if (ext_len > 4 || ext_len < 3)
  return false;
  
  const char *check = ext;
  while (*check)
  {
  if (isspace(*check))
  return false;
  
  ++check;
  }
  
  if (!stricmp(ext, ".cfg") ||
  !stricmp(ext, ".lst") ||
  !stricmp(ext, ".lmp") ||
  !stricmp(ext, ".exe") ||
  !stricmp(ext, ".vbs") ||
  !stricmp(ext, ".com") ||
  !stricmp(ext, ".bat") ||
  !stricmp(ext, ".dll") ||
  !stricmp(ext, ".ini") ||
  !stricmp(ext, ".log") ||
  !stricmp(ext, ".lua") ||
  !stricmp(ext, ".nut") ||
  !stricmp(ext, ".vdf") ||
  !stricmp(ext, ".smx") ||
  !stricmp(ext, ".gcf") ||
  !stricmp(ext, ".sys"))
  return false;
  
  return true;
  }
  

Bypassing `"//" and ".."` can be done with `"/\\"` because there is a call to FixSlashes that makes proper slashes _after_ the sanity check, and for the `".."` the `"/\\"` will set the path to the root of the drive, so we can write to anywhere on the system if we know the path. Bypassing `"lua/", "gamemodes/" and "addons/"` can be done by using capital letters e.g. `"ADDONS/"` since file paths are not case sensitive on Windows.

Bypassing the file extension check is a bit more tricky, so let’s look at the structure sent by `SendFile` called `dataFragments_t`:
  
  
  typedef struct dataFragments_s
  {
  FileHandle_t  file;  // open file handle
  char  filename[260];  // filename
  char*  buffer;  // if NULL it's a file
  unsigned int  bytes;  // size in bytes
  unsigned int  bits;  // size in bits
  unsigned int  transferID;  // only for files
  bool  isCompressed;  // true if data is bzip compressed
  unsigned int  nUncompressedSize;  // full size in bytes
  bool  isReplayDemo;  // if it's a file, is it a replay .dem file?
  int  numFragments;  // number of total fragments
  int  ackedFragments;  // number of fragments send & acknowledged
  int  pendingFragments;  // number of fragments send, but not acknowledged yet
  } dataFragments_t;
  

The 260 bytes name buffer in `dataFragments_t` is used for the file name checks and filters, but is later copied and then truncated to 256 bytes after all the sanity checks thus removing our fake extension and activating the malicious extension:
  
  
  Q_strncpy( rc->gamePath, gamePath, BufferSize /* BufferSize = 256 */ );
  

Using a file name such as `./././(...)/file.dll.txt` (pad to max length with `./`) would get truncated to `./././(...)/file.dll` on the receiving end after checking if the file extension is valid. This also has the side effect that we can overwrite files as the _file exists_ check is done before the file extension truncation.

#  Remote code execution

Using the aforementioned remote file inclusion, we can upload Source Engine config files which have the potential to execute arbitrary code. Using Procmon, I discovered that the game engine searches for the config file in both `platform/cfg` and `swarm/cfg` respectively:

![procmon](/assets/alien_swarm/procmon.png)

We can simply upload a malicious plugin and config file to `platform/cfg` and hijack the server. This is due to the fact that the Source Engine server config has the capability to load plugins with the `plugin_load` command:
  
  
  plugin_load addons/alien_swarm_exploit.dll
  

This will load our dynamic library into the game server application, granting arbitrary code execution. The only constraint is that the `newmapsettings.cfg` config file is only reloaded on map change, so you will have to wait till the end of a game.

#  Wormable demonstration

Since both of these exploits apply to both the server and the client, we can infect a server, which can infect all players, which can carry on the virus when playing other servers. This makes this exploit chain completely wormable and nothing but a complete shutdown of the game servers can fix it.

#  Timeline

  * [2020-05-12] Reported to Valve on HackerOne
  * [2020-05-13] Triaged by Valve: “Looking into it!”
  * [2020-08-03] Patched in beta branch
  * [2020-08-18] Patched in release

Tagged[ binary-exploitation](/tags#binary-exploitation),[ pwn](/tags#pwn) [PREVIOUSAbusing MacOS Entitlements for code execution ](/2020/08/14/macos-entitlements.html) [NEXTNew year, new anti-debug: Don't Thread On Me ](/2021/01/04/thread-stuff.html)
