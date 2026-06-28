---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-07-11_a-race-to-the-bottom-database-transactions-undermining-your-appsec.md
original_filename: 2024-07-11_a-race-to-the-bottom-database-transactions-undermining-your-appsec.md
title: A Race to the Bottom - Database Transactions Undermining Your AppSec
category: documents
detected_topics:
- race-condition
- sqli
- supply-chain
- oauth
- sso
- access-control
tags:
- imported
- documents
- race-condition
- sqli
- supply-chain
- oauth
- sso
- access-control
language: en
raw_sha256: 686f9b89eb7cf71c9cf6182aea40ddd8a8ea00d185ba9c71a7de8f22d284c9bc
text_sha256: a82616304c99e8aa91713e5dee0e84ea142d99f1bb9a4c3233c551cba6e1f579
ingested_at: '2026-06-28T07:32:35Z'
sensitivity: unknown
redactions_applied: false
---

# A Race to the Bottom - Database Transactions Undermining Your AppSec

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-07-11_a-race-to-the-bottom-database-transactions-undermining-your-appsec.md
- Source Type: markdown
- Detected Topics: race-condition, sqli, supply-chain, oauth, sso, access-control
- Ingested At: 2026-06-28T07:32:35Z
- Redactions Applied: False
- Raw SHA256: `686f9b89eb7cf71c9cf6182aea40ddd8a8ea00d185ba9c71a7de8f22d284c9bc`
- Text SHA256: `a82616304c99e8aa91713e5dee0e84ea142d99f1bb9a4c3233c551cba6e1f579`


## Content

---
title: "A Race to the Bottom - Database Transactions Undermining Your AppSec"
page_title: "A Race to the Bottom - Database Transactions Undermining Your AppSec · Doyensec's Blog"
url: "https://blog.doyensec.com/2024/07/11/database-race-conditions.html"
final_url: "https://blog.doyensec.com/2024/07/11/database-race-conditions.html"
authors: ["Viktor Chuchurski (@viktorot)"]
bugs: ["Race condition"]
publication_date: "2024-07-11"
added_date: "2024-07-15"
source: "pentester.land/writeups.json"
original_index: 172
---

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.  
  
Visit us  
[doyensec.com](https://doyensec.com)  
  
Follow us  
[@doyensec](https://twitter.com/doyensec)  
  
Engage us  
[info@doyensec.com](mailto:info@doyensec.com)  
  

#### Blog Archive

  * 2026

  * 2025

  * 2024

  * 2023

  * 2022

  * 2021

  * 2020

  * 2019

  * 2018

  * 2017

© 2026 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# A Race to the Bottom - Database Transactions Undermining Your AppSec

11 Jul 2024 - Posted by Viktor Chuchurski

## Introduction

Databases are a crucial part of any modern application. Like any external dependency, they introduce additional complexity for the developers building an application. In the real world, however, they are usually considered and used as a black box which provides storage functionality.

This post aims shed light on a particular aspect of the complexity databases introduce which is often overlooked by developers, namely **concurrency control**. The best way to do that is to start off by looking at a fairly common code pattern we at Doyensec see in our day-to-day work:
  
  
  func (db *Db) Transfer(source int, destination int, amount int) error {
  ctx := context.Background()
  
  conn, err := pgx.Connect(ctx, db.databaseUrl)
  defer conn.Close(ctx)
  
  // (1)
  tx, err := conn.BeginTx(ctx)
  
  var user User
  // (2)
  err = conn.
  QueryRow(ctx, "SELECT id, name, balance FROM users WHERE id = $1", source).
  Scan(&user.Id, &user.Name, &user.Balance)
  
  // (3)
  if amount <= 0 || amount > user.Balance {
  tx.Rollback(ctx)
  return fmt.Errorf("invalid transfer")
  }
  
  // (4)
  _, err = conn.Exec(ctx, "UPDATE users SET balance = balance - $2 WHERE id = $1", source, amount)
  _, err = conn.Exec(ctx, "UPDATE users SET balance = balance + $2 WHERE id = $1", destination, amount)
  
  // (5)
  err = tx.Commit(ctx)
  return nil
  }
  

_Note: All error checking has been removed for clarity._

For the readers not familiar with Go, here’s a short summary of what the code is doing. We can assume that the application will initially perform authentication and authorization on the incoming HTTP request. When all required checks have passed, the `db.Transfer` function handling the database logic will be called. At this point the application will:

  1. 1\. Establish a new database transactions

  2. 2\. Read the source account’s balance

  3. 3\. Verify that the transfer amount is valid with regard to the source account’s balance and the application’s business rules

  4. 4\. Update the source and destination accounts’ balances appropriately

  5. 5\. Commit the database transaction

A transfer can be made by making a request to the `/transfer` endpoint, like so:
  
  
  POST /transfer HTTP/1.1
  Host: localhost:9009
  Content-Type: application/json
  Content-Length: 31
  
  {
  "source":1,
  "destination":2,
  "amount":50
  }
  

We specify the source and destination account IDs, and the amount to be transferred between them. The full source code, and other sample apps developed for this research can be found in our [playground](https://github.com/doyensec/db-race-conditions-playground) repo.

Before continuing reading, take a minute and review the code to see if you can spot any issues.

Notice anything? At first look, the implementation seems correct. Sufficient input validation, bounds and balance checks are performed, no possibility of SQL injection, etc. We can also verify this by running the application and making a few requests. We’ll see that transfers are being accepted until the source account’s balance reaches zero, at which point the application will start returning errors for all subsequent requests.

Fair enough. Now, let’s try some more dynamic testing. Using the following Go script, let us try and make 10 concurrent requests to the `/transfer` endpoint. We’d expect that two request will be accepted (two transfers of 50 with an initial balance of 100) and the rest will be rejected.
  
  
  func transfer() {
  client := &http.Client{}
  
  body := transferReq{
  From:  1,
  To:  2,
  Amount: 50,
  }
  bodyBuffer := new(bytes.Buffer)
  json.NewEncoder(bodyBuffer).Encode(body)
  
  req, err := http.NewRequest("POST", "http://localhost:9009/transfer", bodyBuffer)
  if err != nil {
  panic(err)
  }
  req.Header.Add("Content-Type", `application/json`)
  resp, err := client.Do(req)
  if err != nil {
  panic(err)
  } else if _, err := io.Copy(os.Stdout, resp.Body); err != nil {
  panic(err)
  }
  fmt.Printf(" / status code => %v\n", resp.StatusCode)
  }
  
  func main() {
  for i := 0; i < 10; i++ {
  // run transfer as a goroutine
  go transfer()
  }
  time.Sleep(time.Second * 2)
  fmt.Printf("done.\n")
  }
  

However, running the script we see something different. We see that almost all, if not all, of the request were accepted and successfully processed by the application server. Viewing the balance of both accounts with the `/dump` endpoint will show that the source account has a negative balance.

We have managed to overdraw our account, effectively making money out of thin air! At this point, any person would be asking “why?” and “how?”. To answer them, we first need to take a detour and talk about databases.

## Database Transactions and Isolation Levels

Transactions are a way to define a logical unit of work within a database context. Transactions consist of multiple database operations which need to be successfully executed, for the unit to be considered complete. Any failure would result in the transaction being reverted, at which point the developer needs to decide whether to accept the failure or retry the operation. Transactions are a way to ensure [ACID](https://en.wikipedia.org/wiki/ACID) properties for database operations. While all properties are important to ensure data correctness and safety, for this post we’re only interested in the “I” or Isolation.

In short, Isolation defines the level to which concurrent transactions will be isolated from each other. This ensures they always operate on correct data and don’t leave the database in an inconsistent state. Isolation is a property which is directly controllable by developers. The [ANSI SQL-92](https://www.contrib.andrew.cmu.edu/~shadow/sql/sql1992.txt) standard defines four isolation levels, which we will take a look at in more detail later onm, but first we need to understand why we need them.

### Why Do We Need Isolation?

The isolation levels are introduced to eliminate read phenomena or unexpected behaviors, which can be observed when concurrent transactions are being performed on the set of data. The best way to understand them is with a short example, graciously borrowed from [Wikipedia](https://en.wikipedia.org/wiki/Isolation_\(database_systems\)#Read_phenomena).

#### Dirty Reads

Dirty reads allow transactions to read uncommitted changes made by concurrent transactions.
  
  
  -- tx1
  BEGIN;
  SELECT age FROM users WHERE id = 1; -- age = 20 
  -- tx2
  BEGIN;
  UPDATE users SET age = 21 WHERE id = 1;
  -- tx1
  SELECT age FROM users WHERE id = 1; -- age = 21 
  -- tx2
  ROLLBACK; -- the second read by tx1 is reverted
  

#### Non-Repeatable Reads

Non-repeatable reads allow sequential `SELECT` operations to return different results as a result of concurrent transactions modifying the same table entry.
  
  
  -- tx1
  BEGIN;
  SELECT age FROM users WHERE id = 1; -- age = 20 
  -- tx2
  UPDATE users SET age = 21 WHERE id = 1;
  COMMIT;
  -- tx2
  SELECT age FROM users WHERE id = 1; -- age = 21
  

#### Phantom Reads

Phantom reads allow sequential `SELECT` operations on a set of entries to return different results due to modifications done by concurrent transactions.
  
  
  -- tx1
  BEGIN;
  SELECT name FROM users WHERE age > 17; -- returns [Alice, Bob]
  -- tx2
  BEGIN;
  INSERT INTO users VALUES (3, 'Eve', 26);
  COMMIT;
  -- tx1
  SELECT name FROM users WHERE age > 17; -- returns [Alice, Bob, Eve]
  

In addition the phenomena defined in the standard, behaviors such as “Read Skews”, “Write Skews” and “Lost Updates” can be observed in the real world.

#### Lost Updates

Lost updates occur when concurrent transactions perform an update on the same entry.
  
  
  -- tx1
  BEGIN;
  SELECT * FROM users WHERE id = 1;
  -- tx2
  BEGIN;
  SELECT * FROM users WHERE id = 1;
  UPDATE users SET name = 'alice' WHERE id = 1;
  COMMIT; -- name set to 'alice'
  -- tx1
  UPDATE users SET name = 'bob' WHERE id = 1;
  COMMIT; -- name set to 'bob'
  

This execution flow results in the change performed by `tx2` to be overwritten by `tx1`.

Read and write skews usually arise when the operations are performed on two or more entries that have a foreign-key relationship. The examples below assume that the database contains two tables: a `users` table which stores information about a particular user, and a `change_log` table which stores information about the user who performed the latest change of the target user’s `name` column:
  
  
  CREATE TABLE users(
  id INT PRIMARY KEY NOT NULL, 
  name TEXT NOT NULL
  );
  
  CREATE TABLE change_log(
  id INT PRIMARY KEY NOT NULL, 
  updated_by VARCHAR NOT NULL, 
  user_id INT NOT NULL,
  CONSTRAINT user_fk FOREIGN KEY (user_id) REFERENCES users(id)
  );
  

#### Read Skews

If we assume that we have the following sequence of execution:
  
  
  -- tx1
  BEGIN;
  SELECT * FROM users WHERE id = 1; -- returns 'old_name'
  -- tx2
  BEGIN;
  UPDATE users SET name = 'new_name' WHERE id = 1;
  UPDATE change_logs SET updated_by = 'Bob' WHERE user_id = 1;
  COMMIT;
  -- tx1
  SELECT * FROM change_logs WHERE user_id = 1; -- return Bob
  

the view of `tx1` transaction is that the user `Bob` performed tha last change on the user with ID: `1`, setting their name to `old_name`.

#### Write Skews

In the sequence of operations shown below, `tx1` will perform its update under the assumption that the user’s name is `Alice` and there were no prior changes on the name.
  
  
  -- tx1
  BEGIN;
  SELECT * FROM users WHERE id = 1; -- returns Alice
  SELECT * FROM change_logs WHERE user_id = 1; -- returns an empty set
  -- tx2
  BEGIN;
  SELECT * FROM users WHERE id = 1; 
  UPDATE users SET name = 'Bob' WHERE id = 1; -- new name set
  COMMIT;
  -- tx1
  UPDATE users SET name = 'Eve' WHERE id = 1; -- new name set
  COMMIT;
  

However, `tx2` performed its changes before `tx1` was able to complete. This results in `tx1` performing an update based on state which was changed during its execution.

* * *

Isolation levels are designed to guard against zero or more of these read phenomena. Let’s look at the them is more detail.

### Read Uncommitted

`Read Uncommitted` (`RU`) is the lowest isolation level provided. At this level, all phenomena discussed above can be observed, including reading uncommitted data, as the name suggests. While transactions using this isolation level can result in higher throughput in highly concurrent environments, it does mean that concurrent transactions will likely operate with inconsistent data. From a security standpoint, this is not a desirable property of any business-critical operation.

Thankfully, this it not a default in any database engine, and needs to be explicitly set by developers when a creating a new transaction.

### Read Committed

`Read Committed` (`RC`) builds on top of the previous level’s guarantee and completely prevents `dirty` reads. However, it does allow other transactions to modify, insert, or delete data between individual operations of the running transaction, which can result in `non-repeatable` and `phantom` reads.

`Read Committed` is the default isolation level in most database engines. [MySQL](https://dev.mysql.com/doc/refman/8.0/en/set-transaction.html#:~:text=The%20default%20isolation%20level%20is,isolation%20levels%2C%20see%20Section%2015.7.) is an outlier here.

### Repeatable Read

In similar fashion, `Repeatable Read` (`RR`) improves the previous isolation level, while adding a guarantee that `non-repeatable` reads will also be prevented. The transaction will view only data which was committed at the start of the transactions. `Phantom` reads can still be observed at this level.

### Serializable

Finally, we have the `Serializable` (`S`) isolation level. The highest level is designed to prevent all read phenomena. The result of concurrently executing multiple transactions with `Serializable` isolation will be equivalent to them being executed in serial order.

## Data Races and Race Conditions

Now that we have that covered, let’s circle back to the original example. If we assume that the example was using Postgres and we’re not explicitly setting the isolation level, we’ll be using the Postgres default: `Read Committed`. This setting will protect us from `dirty` reads, and `phantom` or `non-repeatable` reads are not a concern, since we’re not performing multiple reads within the transaction.

The main reason why our example is vulnerable boils down to concurrent transaction execution and insufficient concurrency control. We can enable database logging to easily see what is being executed on the database level when our example application is being exploited.

Pulling the logs for our example, we can see something similar to:
  
  
  1. [TX1] LOG:  BEGIN ISOLATION LEVEL READ COMMITTED
  2. [TX2] LOG:  BEGIN ISOLATION LEVEL READ COMMITTED
  3. [TX1] LOG:  SELECT id, name, balance FROM users WHERE id = 2
  4. [TX2] LOG:  SELECT id, name, balance FROM users WHERE id = 2
  5. [TX1] LOG:  UPDATE users SET balance = balance - 50 WHERE id = 2
  6. [TX2] LOG:  UPDATE users SET balance = balance - 50 WHERE id = 2
  7. [TX1] LOG:  UPDATE users SET balance = balance + 50 WHERE id = 1
  8. [TX1] LOG:  COMMIT
  9. [TX2] LOG:  UPDATE users SET balance = balance + 50 WHERE id = 1
  10. [TX2] LOG:  COMMIT
  

What we initially notice is that the individual operations of a single transaction are not executed as a single unit. Their individual operations are interweaved, contradicting how the initial transaction definition described them (i.e., a single unit of execution). This interweaving occurs as a result of transactions being executed concurrently.

### Concurrent Transaction Execution

Databases are designed to execute their incoming workload concurrently. This results in an increased throughput and ultimately a more performant system. While implementation details can vary between different database vendors, at a high level concurrent execution is implemented using “workers”. Databases define a set of workers whose job is to execute all transactions assigned to them by a component usually named “scheduler”. The workers are independent of each other and can be conceptually thought of as application threads. Like application threads, they are subject to context switching, meaning that they can be interrupted mid-execution, allowing other workers to perform their work. As a result we can end up having partial transaction execution, resulting in the interweaved operations we saw in the log output above. As with multithreaded application code, without proper concurrency control, we run the risk of encountering data races and race conditions.

Going back to the database logs, we can also see that both transactions are trying to perform an update on the same entry, one after the other (lines `#5` and `#6`). Such concurrent modification will be prevented by the database by setting a lock on the modified entry, protecting the change until the transaction that made the change completes or fails. Databases vendors are free to implement any number of different [lock types](https://www.postgresql.org/docs/current/explicit-locking.html), but most of them can be simplified to two types: shared and exclusive locks.

**Shared** (or read) locks are acquired on table entries read from the database. They are not mutually exclusive, meaning multiple transactions can hold a shared lock on the same entry.

**Exclusive** (or write) locks, as the name suggests are exclusive. Acquired when a write/update operation is performed, only one lock of this type can be active per table entry. This helps prevent concurrent changes on the same entry.

Database vendors provide a simple way to query active locks at any time of the transactions execution, given you can pause it or are executing it manually. In Postgres for example, the following query will show the active locks:
  
  
  SELECT locktype, relation::regclass, mode, transactionid AS tid, virtualtransaction AS vtid, pid, granted, waitstart FROM pg_catalog.pg_locks l LEFT JOIN pg_catalog.pg_database db ON db.oid = l.database WHERE (db.datname = '<db_name>' OR db.datname IS NULL) AND NOT pid = pg_backend_pid() ORDER BY pid;
  

A similar query can be used for MySQL:
  
  
  SELECT thread_id, lock_data, lock_type, lock_mode, lock_status FROM performance_schema.data_locks WHERE object_name = '<db_name>';
  

For other database vendors refer to the appropriate documentation.

### Root Cause

The isolation level used in our example (`Read Committed`) will not place any locks when data is being read from the database. This means that only the write operations will be placing locks on the modified entries. If we visualize this, our issue becomes clear:

![Transaction's Critical Section](/public/images/db-race-critical-section.svg)

The lack of locking on the `SELECT` operation allows for concurrent access to a shared resource. This introduces a TOCTOU (time-of-check, time-of-use) issue, leading to an exploitable race condition. Even though the issue is not visible in the application code itself, it becomes obvious in the database logs.

### Applying Theory in Practice

Different code patterns can allow for different exploit scenarios. For our particular example, the main difference will be how the new application state is calculated, or more specifically, which values are used in the calculation.

#### Pattern #1 - Calculations Using Current Database State

In the original example, we can see that the new balance calculations will happen on the database server. This is due to how the `UPDATE` operation is structured. It containins a simple addition/subtraction operation, which will be calculated by the database using the current value of the `balance` column at time of execution. Putting it all together, we end up with an execution flow shown on the graph below.

![Vulnerable Pattern #1](/public/images/db-race-pattern-1.svg)

Using the database’s default isolation level, the `SELECT` operation will be executed before any locks are created and the same entry will be returned to the application code. The transaction which gets its first `UPDATE` to execute, will enter the critical section and will be allowed to execute its remaining operations and commit. During that time, all other transactions will hang and wait for the lock to be released. By committing its changes, the first transaction will change the state of the database, effectively breaking the assumption under which the waiting transaction was initiated on. When the second transaction executes its `UPDATE`s, the calculations will be performed on the updated values, leaving the application in an incorrect state.

#### Pattern #2 - Calculations Using Stale Values

Working with stale values happens when the application code reads the current state of the database entry, performs the required calculations at the application layer and uses the newly calculated value in an `UPDATE` operation. We can perform a simple refactoring to our initial example and move the “new value” calculation to the application layer.
  
  
  func (db *Db) Transfer(source int, destination int, amount int) error {
  ctx := context.Background()
  conn, err := pgx.Connect(ctx, db.databaseUrl)
  defer conn.Close(ctx)
  
  tx, err := conn.BeginTx(ctx)
  
  var userSrc User
  err = conn.
  QueryRow(ctx, "SELECT id, name, balance FROM users WHERE id = $1", source).
  Scan(&userSrc.Id, &userSrc.Name, &userSrc.Balance)
  
  var userDest User
  err = conn.
  QueryRow(ctx, "SELECT id, name, balance FROM users WHERE id = $1", destination).
  Scan(&userDest.Id, &userDest.Name, &userDest.Balance)
  
  if amount <= 0 || amount > userSrc.Balance {
  tx.Rollback(ctx)
  return fmt.Errorf("invalid transfer")
  }
  
  // note: balance calculations moved to the application layer
  newSrcBalance := userSrc.Balance - amount
  newDestBalance := userDest.Balance + amount
  
  _, err = conn.Exec(ctx, "UPDATE users SET balance = $2 WHERE id = $1", source, newSrcBalance)
  _, err = conn.Exec(ctx, "UPDATE users SET balance = $2 WHERE id = $1", destination, newDestBalance)
  
  err = tx.Commit(ctx)
  return nil
  }
  

If two or more concurrent requests call the `db.Transfer` function at the same time, there is a high probability that the initial `SELECT` will be executed before any locks are created. All function calls will read the same value from the database. The amount verification will pass successfully and the new balances will be calculated. Let’s see how does this scenario affect out database state if we run the previous test case:

![Vulnerable Pattern #2](/public/images/db-race-pattern-2.svg)

At first glance, the database state doesn’t show any inconsistencies. That is because both transactions preformed their amount calculation based on the same state and both executed `UPDATE` operations with the same amounts. Even though the database state was not corrupted, it’s worth bearing in mind that we were able to execute the transaction more times that what the business logic should allow. For example, an application built using a microservice architecture might implement business logic such as:

![Vulnerable Pattern #2 - Microservice Application](/public/images/db-race-microservice.svg)

If `Service T` assumes that all incoming requests from the main application are valid, and does not perform any additional validation itself, it will happily process any incoming requests. The race condition described before allows us to exploit such behavior and call the downstream `Service T` multiple times, effectively performing more transfers that the business requirements would allow.

This pattern can also be (ab)used to corrupt the database state. Namely, we can perform multiple transfers from the source account to different destination accounts.

![Vulnerable Pattern #2.1](/public/images/db-race-pattern-2-1.svg)

With this exploit, both concurrent transactions will initially see a source balance of 100, which will pass the amount verification.

## Exploitation in the Real World

If you run the sample application locally, with a database running on the same machine, you will likely see that most, if not all, of the requests made to the `/transfer` endpoint will be accepted by the application server. The low latency between client, application server and database server allow all requests to hit the race window and successfully commit. However, real-world application deployments are much more complex, running in cloud environments, deployed using Kubernetes clusters, placed behind reverse proxies and protected by firewalls.

We were curious to see how difficult is to hit the race window in a real-world context. To test that we set up a simple application, deployed in an AWS Fargate container, alongside another container running the selected database.

Testing was focused on three databases: [Postgres](https://www.postgresql.org/), [MySQL](https://www.mysql.com/) and [MariaDB](https://mariadb.org/).

The application logic was implemented using two programming languages: [Go](https://go.dev/) and [Node](https://nodejs.org/en). These languages were chosen to allow us to see how their different concurrency models (Go’s goroutines vs. Node’s event loop) impact exploitability.

Finally, we specified three techniques of attacking the application:

  1. 1\. simple multi-threaded loop

  2. 2\. last-byte sync for HTTP/1.1

  3. 3\. [single packet attacks](https://portswigger.net/research/the-single-packet-attack-making-remote-race-conditions-local) for HTTP/2.0

All of these were performed using [BurpSuite’s](https://portswigger.net/burp) extensions: “Intruder” for (1) and “Turbo Intruder” for (2) and (3).

Using this setup, we attacked the application by performing 20 requests using 10 threads/connections, transferring an amount of 50 from Bob (account ID `2` with a starting balance of 200) to Alice. Once the attack was done, we noted the number of accepted requests. Given a non-vulnerable application, there shouldn’t be more than 4 accepted requests.

This was performed 10 times, for each combination of application/database/attack method. The number of successfully processed requests was noted. From those numbers we conclude if a specific isolation level is exploitable or not. Those results can be found here.

## Results and Observations

Our testing showed that if this pattern is present in an application, it is very likely that it can be exploited. In all cases, except for the `Serializable` level, we were able to exceed the expected number of accepted requests, overdrawing the account. The number of accepted requests varies between different technologies, but the fact that we were able to exceed it (and in some cases, to a significant degree) is sufficient to demonstrate the exploitability of the issue.

If an attacker is able to get a large number of request to the server in the same instant, effectively creating conditions of a local access, the number of accepted requests jumps up by a significant amount. So, to maximize the possibility of hitting the race window, testers should prefer methods such as last-byte sync or the single packet attack.

One outlier is Postgres’ `Repeatable Read` level. The reason it’s not vulnerable is that it implements an isolation level called [`Snapshot Isolation`](https://en.wikipedia.org/wiki/Snapshot_isolation). The guarantees provided by this isolation level sit between `Repeatable Read` and `Serializable`, ultimately providing sufficient protection and mitigating the race conditions for our example.

The languages concurrency modes did not have any notable impact on the exploitability of the race condition.

## Mitigation

On a conceptual level, the fix only requires the start of the critical section to be moved to the beginning of the transaction. This will ensure that the transaction which first reads the entry gets exclusive access to it and is the only one allowed to commit. All others will wait for its completion.

Mitigation can be implemented in a number of ways. Some of them require manual work, while others come out of the box, provided by the database of choice. Let’s start by looking at the simplest and generally preferred way: setting the transaction isolation level to `Serializable`.

As mentioned before, the isolation level is a user/developer controlled property of a database transaction. It can be set by simply specifying it when creating a transaction:
  
  
  BEGIN TRANSACTION SET TRANSACTION ISOLATION LEVEL SERIALIZABLE
  

This may slightly vary from database to database, so it’s always best to consult the appropriate documentation. Usually ORMs or database drivers provide an application level interface for setting the desired isolation level. Postgres’ Go driver [pgx](https://github.com/jackc/pgx) allows users to do the following:
  
  
  tx, err := conn.BeginTx(ctx, pgx.TxOptions{IsoLevel: pgx.Serializable})
  

It is worth noting that `Serizalizable`, being the highest isolation level, may have an impact of the performance of your application. However, its use can be limited to only the business-critical transaction. All other transactions can remain unchanged and be executed with the database’s default isolation level or any appropriate level for that particular operation.

One alternative to this method is implementing pessimistic locking via manual locking. The idea behind this method is that the business-critical transaction will obtain all required locks at the beginning and only release them when the transaction completes or fails. This ensures that no other concurrently executing transaction will be able to interfere. Manual locking can be performed by specifying the `FOR SHARE` or `FOR UPDATE` options your `SELECT` operations:
  
  
  SELECT id, name, balance FROM users WHERE id = 1 FOR UPDATE
  

This will instruct the database to place a shared or exclusive lock, respectively, to all entries returned by the read operation, effectively disallowing any modification to it until the lock is released. This method can, however, be error prone. There is always a possibility that other operations may get overlooked or new ones will be added without the `FOR SHARE / FOR UPDATE` option, potentially re-introducing the data race. Additionally, scenarios such as the one shown below, may be possible at lower isolation levels.

![Lost Update](/public/images/db-race-lost-update.svg)

The graph shows a scenario where ‘tx2’ performs validation on a value which becomes stale after `tx1` commits, and ends up overwriting the update performed by `tx1`, leading to a `Lost Update`.

Finally, mitigation can also be implemented using optimistic locking. The conceptual opposite of pessimistic locking, optimistic locking expects that nothing will go wrong and only performs conflict detection at the end of the transaction. If a conflict is detected (i.e., underlining data was modified by a concurrent transaction), the transaction will fail and will need to be retried. This method is usually implemented using a logic clock, or a table column, whose value must not change during the execution of the transaction.

The simplest way to implement this is by introducing a `version` column in your table:
  
  
  CREATE TABLE users(
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, 
  name TEXT NOT NULL, 
  balance INT NOT NULL,
  version INT NOT NULL AUTO_INCREMENT
  );
  

The value of the `version` column must then be always verified when performing any write/update operations to the database. If the value changed, the operation will fail, failing the entire transaction.
  
  
  UPDATE users SET balance = 100 WHERE id = 1 AND version = <last_seen_version>
  

## Detection

If the application uses an ORM, setting the isolation level would usually entails calling a setter function, or supplying it as a function parameter. On the other hand, if the application constructs database transactions using raw SQL statements, the isolation level will be supplied as part of the transaction’s `BEGIN` statement.

Both those methods represent a pattern which can be search for using tools such as [Semgrep](https://semgrep.dev/). So, if we assume that our application is build using Go and uses the [pgx](https://github.com/jackc/pgx) to access to data stored in a Postgres database, we can use the following Semgrep rules to detect instances of unspecified isolation levels.

### 1\. Raw SQL Transaction
  
  
  rules:
  - id: pgx-sql-tx-missing-isolation-level
  message: "SQL transaction without isolation level"
  languages:
  - go
  severity: WARNING
  patterns:
  - pattern: $CONN.Exec($CTX, $BEGIN)
  - metavariable-regex:
  metavariable: $BEGIN
  regex: ("begin transaction"|"BEGIN TRANSACTION")
  

### 2\. Missing pgx Transaction Creation Options
  
  
  rules:
  - id: pgx-tx-missing-options
  message: "Postgres transaction options not set"
  languages:
  - go
  severity: WARNING
  patterns:
  - pattern: $CONN.BeginTx($CTX)
  

### 3\. Missing Isolation Level in pgq Transaction Creation Options
  
  
  rules:
  - id: pgx-tx-missing-options-isolation
  message: "Postgres transaction isolation level not set"
  languages:
  - go
  severity: WARNING
  patterns:
  - pattern: $CONN.BeginTx($CTX, $OPTS)
  - metavariable-pattern:
  metavariable: $OPTS
  patterns:
  - pattern-not: >
  $PGX.TxOptions{..., IsoLevel:$LVL, ...}
  

All these patterns can be easily modified to suit you tech-stack and database of choice.

It’s important to note that rules like these are not a complete solution. Integrating them blindly into an existing pipeline will result in a lot of noise. We would rather recommend using them to build an inventory of all transactions the application performs, and use that information as a starting point to review the application and apply hardening if it is required.

## Closing Thoughts

To finish up, we should emphasize that this is not a bug in database engines. This is part of how isolation levels were designed and implemented and it is clearly described in both the SQL specification and dedicated documentation for each database. Transactions and isolation levels were designed to protect concurrent operations from interfering with each other. Mitigations against data races and race conditions, however, are not their primary use case. Unfortunately, we found that this is a common misconception.

While usage of transactions will help guard the application from data corruptions under normal circumstances, it is not sufficient to mitigate data races. When this insecure pattern is introduced in business-critical code (account management functionality, financial transactions, discount code application, etc.), the likelihood of it being exploitable is high. For that reason, review your application’s business-critical operations and verify that they are doing proper data locking.

## Resources

This research was presented by Viktor Chuchurski ([@viktorot](https://x.com/viktorot)) at the 2024 OWASP Global AppSec conference in Lisbon. The recording of that presentation can be found [here](https://www.youtube.com/watch?v=CdWQGpV2LI0) and the presentation slides can be downloaded [here](https://www.doyensec.com/resources/Global_AppSec_Lisbon_A_Race_To_The_Bottom.pdf).

Playground code can be found on Doyensec’s [GitHub](https://github.com/doyensec/db-race-conditions-playground).

## More information

If you would like to learn more about our other research, check out our blog, follow us on X ([@doyensec](https://x.com/doyensec)) or feel free to contact us at [info@doyensec.com](mailto:info@doyensec.com) for more information on how we can help your organization “Build with Security”.

## Appendix - Testing Results

The table below shows which isolation level allowed race condition to happen for the databases we tested as part of our research.

| RU | RC | RR | S  
---|---|---|---|---  
MySQL | Y | Y | Y | N  
Postgres | Y | Y | N | N  
MariaDB | Y | Y | Y | N  
  
### Other relevant posts:

  * ###  [ Introducing Session Switcher. Swap Burp Sessions with One Click! 17 Jun 2026 ](/2026/06/17/session-switcher.html)

  * ###  [ Trivial C# Random Exploitation 19 Aug 2025 ](/2025/08/19/trivial-exploit-on-C-random.html)

  * ###  [ Common OAuth Vulnerabilities 30 Jan 2025 ](/2025/01/30/oauth-common-vulnerabilities.html)

  * ###  [ Applying Security Engineering to Make Phishing Harder - A Case Study 19 Sep 2024 ](/2024/09/19/phishing-case-study.html)

  * ###  [ SSRF Cross Protocol Redirect Bypass 16 Mar 2023 ](/2023/03/16/ssrf-remediation-bypass.html)

  * ###  [ A New Vector For “Dirty” Arbitrary File Write to RCE 28 Feb 2023 ](/2023/02/28/new-vector-for-dirty-arbitrary-file-write-2-rce.html)

  * ###  [ Introducing Proxy Enriched Sequence Diagrams (PESD) 14 Feb 2023 ](/2023/02/14/pesd-extension-public-release.html)

  * ###  [ safeurl for Go 13 Dec 2022 ](/2022/12/13/safeurl.html)

  * ###  [ The Danger of Falling to System Role in AWS SDK Client 18 Oct 2022 ](/2022/10/18/cloudsectidbit-dataimport.html)

  * ###  [ Dependency Confusion 21 Jul 2022 ](/2022/07/21/dependency-confusion.html)

  * ###  [ Apache Pinot SQLi and RCE Cheat Sheet 09 Jun 2022 ](/2022/06/09/apache-pinot-sqli-rce.html)

  * ###  [ Lessons in auditing cryptocurrency wallets, systems, and infrastructures 01 Aug 2019 ](/2019/08/01/common-crypto-bugs.html)

  * ###  [ Jackson gadgets - Anatomy of a vulnerability 22 Jul 2019 ](/2019/07/22/jackson-gadgets.html)

  * ###  [ On insecure zip handling, Rubyzip and Metasploit RCE (CVE-2019-5624) 24 Apr 2019 ](/2019/04/24/rubyzip-bug.html)

  * ###  [ Introducing burp-rest-api v2 05 Nov 2018 ](/2018/11/05/burp-rest-api-v2.html)

  * ###  [ Developing Burp Suite Extensions training 02 Mar 2017 ](/2017/03/02/training-burp.html)
