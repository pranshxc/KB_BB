---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '881891'
original_report_id: '881891'
title: File System Monitoring Queue Overflow
weakness: Business Logic Errors
team_handle: owncloud
created_at: '2020-05-24T18:37:13.000Z'
disclosed_at: '2021-12-03T14:01:05.136Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
asset_identifier: Desktop Client
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- business-logic-errors
---

# File System Monitoring Queue Overflow

## Metadata

- HackerOne Report ID: 881891
- Weakness: Business Logic Errors
- Program: owncloud
- Disclosed At: 2021-12-03T14:01:05.136Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

in the source code "owncloud/client" in the file "src/gui/folderwatcher_linux.cpp" in the function "void FolderWatcherPrivate :: inotifyRegisterPath (const QString & path)" by calling "inotify_add_watch" the file paths are set for monitoring

```cpp
 int wd = inotify_add_watch(_fd, path.toUtf8().constData(),
        IN_CLOSE_WRITE | IN_ATTRIB | IN_MOVE | IN_CREATE | IN_DELETE | IN_DELETE_SELF | IN_MOVE_SELF | IN_UNMOUNT | IN_ONLYDIR);
```
But in the specified call, the flag "IN_Q_OVERFLOW" is omitted, which allows an attacker to influence the operation of the software.
The essence of the impact is to form a large number of events overflowing the monitoring queue.
In my opinion, the most effective and not noticeable will be creating a hidden file, writing data to it, closing and deleting.

It is worth noting that the function code "void FolderWatcherPrivate :: slotReceivedNotification (int fd)"

```cpp
  do {
        len = read(fd, buffer.data(), buffer.size());
        error = errno;
        /**
          * From inotify documentation:
          *
          * The behavior when the buffer given to read(2) is too
          * small to return information about the next event
          * depends on the kernel version: in kernels  before 2.6.21,
          * read(2) returns 0; since kernel 2.6.21, read(2) fails with
          * the error EINVAL.
          */
        if (len < 0 && error == EINVAL) {
            // double the buffer size
            buffer.resize(buffer.size() * 2);
            /* and try again ... */
            continue;
        }
    } while (false);
``` 

As my tests showed, it does not provide an increase in the buffer, which could offset the impact.
The function reads part of the data from the queue, since the minimum buffer necessary for reading is much less than 2048.

```
Specifying a buffer of size
sizeof(struct inotify_event) + NAME_MAX + 1
will be sufficient to read at least one event.
```

## Impact

Thus, the essence of the impact will consist in overflowing the monitoring queue.
What will force the system to discard incoming events and the program will skip them.
Skipping program monitoring events will lead to incorrect display of files and directories in the program, and will also affect the synchronization with the server.

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
