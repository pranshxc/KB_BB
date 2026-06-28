---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-15_static-taint-analysis-using-binary-ninja-a-case-study-of-mysql-cluster-vulnerabi.md
original_filename: 2022-02-15_static-taint-analysis-using-binary-ninja-a-case-study-of-mysql-cluster-vulnerabi.md
title: 'Static Taint Analysis Using Binary Ninja: A Case Study Of MySQL Cluster Vulnerabilities'
category: documents
detected_topics:
- supply-chain
- sso
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- supply-chain
- sso
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: abd0e3d22f293b036287bd25781f0b14b4fc5cfe17bd69b5a513b94204971984
text_sha256: 3e22e215a0887ba40b533b6533d11465bcf0a15c2ab67d258db4376ad839fd12
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Static Taint Analysis Using Binary Ninja: A Case Study Of MySQL Cluster Vulnerabilities

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-15_static-taint-analysis-using-binary-ninja-a-case-study-of-mysql-cluster-vulnerabi.md
- Source Type: markdown
- Detected Topics: supply-chain, sso, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `abd0e3d22f293b036287bd25781f0b14b4fc5cfe17bd69b5a513b94204971984`
- Text SHA256: `3e22e215a0887ba40b533b6533d11465bcf0a15c2ab67d258db4376ad839fd12`


## Content

---
title: "Static Taint Analysis Using Binary Ninja: A Case Study Of MySQL Cluster Vulnerabilities"
page_title: "Zero Day Initiative — Static Taint Analysis using Binary Ninja: A Case Study of MySQL Cluster Vulnerabilities"
url: "https://www.zerodayinitiative.com/blog/2022/2/14/static-taint-analysis-using-binary-ninja-a-case-study-of-mysql-cluster-vulnerabilities"
final_url: "https://www.zerodayinitiative.com/blog/2022/2/14/static-taint-analysis-using-binary-ninja-a-case-study-of-mysql-cluster-vulnerabilities"
authors: ["Reno Robert (@renorobertr)"]
programs: ["Oracle (MySQL)"]
bugs: ["Memory corruption"]
publication_date: "2022-02-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2905
---

# Blog

#  Static Taint Analysis using Binary Ninja: A Case Study of MySQL Cluster Vulnerabilities 

__ February 15, 2022

__ Reno Robert

Taint analysis is an effective technique for finding vulnerabilities, even in large codebases. My colleague, Lucas Leong, recently [demonstrated](https://www.zerodayinitiative.com/blog/2022/2/10/mindshare-when-mysql-cluster-encounters-taint-analysis) how Clang Static Analyzer and CodeQL can be used to model and find vulnerabilities in MySQL NDB Cluster using taint analysis. Largely inspired by his work, I wanted to try something similar but using Binary Ninja since it can also work with closed-source programs.

These are a few things I had in mind while working:

• Identify vulnerabilities due to uses of untrusted values without bounds checking  
• Taint propagation and filtering should be control-flow sensitive  
• Support inter-procedure analysis

I approached this as a graph reachability problem, for which [Tainted Flow Analysis on e-SSA-form Programs](https://homepages.dcc.ufmg.br/~fernando/publications/papers/CC11rimsa.pdf) served as an excellent reference. All the analysis in this article is based on MySQL Cluster 8.0.25 and Binary Ninja 2.4.2846.

**Defining Taint Sources**

To get taint analysis working, it is essential to define the taint sources clearly. MySQL Cluster has a message passing architecture, and interesting taint sources are the messages themselves. This section provides details on message handling and how the message handlers can be identified for analysis.

**_MySQL NDB Cluster Signals_**

MySQL NDB Cluster defines functionalities as “blocks” and messages passing between them as “signals”. The NDB blocks are implemented as C++ classes, and each block registers multiple signal handlers during initialization, which are also methods of the class. Most of the vulnerabilities reported were in these message handlers, also known as signal handlers.

All the blocks inherit the `SimulatedBlock` class to register their signals using `addRecSignal()`, which invokes the `SimulatedBlock::addRecSignalImpl()` method. The registered signal handlers are of type `ExecSignalLocal`, which takes a single argument. Interested readers can refer to blog posts on [Ndb software architecture](http://messagepassing.blogspot.com/2009/09/ndb-software-architecture.html) by Frazer Clement and [Code Reading Notes – MySQL Cluster](https://web.archive.org/web/20201001043806/https:/steinwaywu.ghost.io/code-reading-notes-mysql-cluster/) by Steinway Wu for further details. The scope of this article is limited to entry points to signal handlers. Below is an example of the code of the NDBCNTR block registering a signal handler:

The “Signal” object that each handler receives contains untrusted data. The signal handlers can access the data as `signal->getDataPtr()` or with a few other methods. The handlers can also further pass the “Signal” object to other functions. There are a couple of ways to proceed here. You can either analyze any function that takes Signal as an argument or analyze only the actual signal handlers by cross-referencing calls to `SimulatedBlock::addRecSignalImpl()` and then let inter-procedure analysis take care of the rest. I chose to start with the former since the inter-procedure analysis was implemented at a later stage.

The Signal object is 0x8030 bytes in size and not all bytes should be considered tainted. We should only define a small region of memory of the object as tainted so that only memory reads from the tainted region are propagated. Marking the entire structure as tainted will lead to a lot of false positives. In this case, the signal’s tainted data starts at offset 0x28 and any memory loads from this offset are marked tainted. Both `Signal::getDataPtr()` and `Signal::getDataPtrSend()` return a pointer to this memory.

**_Porting type information from IDA Pro to Binary Ninja_**

The executable under analysis is “ndbd”, which is the [NDB Cluster Data Node Daemon](https://dev.mysql.com/doc/refman/8.0/en/mysql-cluster-programs-ndbd.html) built with DWARF debug information. In order to find functions that take a pointer to a Signal object as an argument, check the type information of all functions as follows:

However, at the moment, Binary Ninja does not handle DWARF information as robustly as IDA Pro does. Another issue with Binary Ninja is its [failure to detect the “this” argument](https://github.com/Vector35/binaryninja-api/issues/604) when analyzing C++ executables. As a result, argument detection will not be accurate, breaking our taint source analysis. An easy fix is to import type information from IDA Pro into Binary Ninja. For example, the `Dblqh::prepareContinueAfterBlockedLab()` method has the following type information as per IDA Pro:

The same function looks different in Binary Ninja. In this case, the “this” pointer is missing, and Signal becomes the first argument. Marking “arg1” as a taint source makes the entire analysis wrong.

Since we are only interested in the right argument position and type information of the Signal argument, we fix it using the scripts provided in ida2bn directory:

Once the type information is fixed, we are good to identify functions and mark taint sources using the Signal argument. More details on working with types in Binary Ninja are documented here [Working with Types, Structures, and Symbols](https://docs.binary.ninja/guide/type.html).

**Taint Propagation and Filtering**

The goals of taint propagation are simple: when a variable is assigned a value from the Signal data, mark it as tainted. If any other variable is derived from the tainted variable, also mark it tainted, and so on. The challenge comes when there are sanitizers. Say a variable is tainted, and in some code path there is a validation for that variable. In this case, the variable is no longer tainted in that code path. Taint propagation should be control-flow sensitive to avoid over tainting and false positives. This section details how I approached the problem using Binary Ninja’s IL and SSA form. For a thorough reading on the topic, please refer to blog posts [Breaking Down Binary Ninja’s Low-Level IL](https://blog.trailofbits.com/2017/01/31/breaking-down-binary-ninjas-low-level-il/) and [Vulnerability Modeling with Binary Ninja](https://blog.trailofbits.com/2018/04/04/vulnerability-modeling-with-binary-ninja/).

**_Binary Ninja ILs and SSA form_**

Binary Ninja supports a variety of Intermediate Languages (IL) like Low-Level IL (LLIL), Medium Level IL (MLIL), and High-Level IL (HLIL). Since MLIL abstracts away stack memory access with variables and has parameters associated with call sites, I found it more suitable to perform inter-procedure taint analysis. Moreover, it is better documented than HLIL.

Another powerful feature supported is the [Single Static Assignment (SSA) form](https://en.wikipedia.org/wiki/Static_single_assignment_form) of the available ILs. In SSA form, each variable is defined only once. When the variable is reassigned to another value, a new version of the variable is created. Therefore, it is easy to track a tainted variable at any point in a function. Consider this minimalistic example: when variable x is reassigned a new value, a new version of the variable is created in the SSA form:

**_SSA variable def-use chain_**

Binary Ninja provides `get_ssa_var_definition()` and `get_ssa_var_uses()` APIs to get a variable’s definition site and their uses respectively. Consider the MLIL SSA code snippet of `Thrman::execOVERLOAD_STATUS_REP()` method below:

Here, `arg2` is a pointer to a Signal object. At the address 0x00784165, the SSA variable “rax#1” is loaded with a tainted value from `[arg2#0 + 0x28]`. The MLIL instructions that use the tainted SSA variable `rax#1` can be fetched as below:

These APIs form the building blocks of our taint analysis going further.

**_Taint propagation with SSA def-use chain_**

Binary Ninja’s ILs are structured as an expression tree such that operands of an operation can be composed of other operations. Consider the graph generated for the below MLIL SSA instruction by the [BNIL Instruction Graph plugin](https://github.com/withzombies/bnil-graph):

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/c18308d2-f241-4fc0-a8d1-1f48074dcad3/Fig1.png)

The `MLIL_SET_VAR_SSA` operation marks the definition of a new SSA variable, which sets the `dest` variable to the result of the `src` expression. The `src` expression could be composed of many other operations. In this case, `MLIL_ADD` adds an offset 0x28 to the base address of Signal and then `MLIL_LOAD_SSA` reads the value from the address computed using `MLIL_ADD`. Effective taint propagation requires visiting all the `MLIL SSA` operations for every instruction expression. Josh Watson’s [emILator](https://github.com/joshwatson/emilator) and [IL instruction counting](https://gist.github.com/psifertex/6fbc7532f536775194edd26290892ef7#file-count_il-py) by Jordan are good examples for visiting and processing MLIL SSA instruction expressions. What does the taint propagation algorithm look like?

• Visit all `MLIL SSA` instructions in the function linearly  
• For any `MLIL_SET_VAR_SSA` operation, resolve the `src` expression to check if it is tainted data  
• If the `src` operand returns tainted data, get the uses of the `dest` SSA variable with `get_ssa_var_uses()`  
• Visit the instructions that use the tainted SSA variable and propagate taint when `MLIL_SET_VAR_SSA` is encountered  
• Once an instruction taints a variable, mark it as visited and never visit again

**_Constraints on SSA variables_**

Once we have the taint propagation algorithm in place, how do we handle sanitizers on the tainted variables? We are only interested in code paths without any validations. With this in mind, let’s revisit our taint propagation algorithm, which relies on the def-use chain. Def-use chains are sequential statements of code; therefore, taint propagation is not control-flow sensitive. Here is an example to demonstrate the issue:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/e35131e8-5851-4a3d-a588-10b5bef5e210/Fig2.png)

The “`value`” variable passed to the function is tainted and gets used in two different code paths. Along the code path executing the basic block at 0x1184, the variable is validated and considered clean. The `get_ssa_var_uses()` for the variable returns 3 instructions:

Processing these 3 instructions linearly would lead to the incorrect conclusion that the validation precedes both usages of the tainted value. In reality, only one instruction is protected. The other two are vulnerable. This problem can be solved by taking control flow into account.

**_Control-flow sensitive propagation using constraint graph_**

The `MediumLevelILInstruction` class has an `il_basic_block` property to get the basic block information of the MLIL instruction.

Using this property, we can fetch the basic blocks of SSA variable definition and SSA variable uses, which also includes the basic blocks where the validations are done. The basic blocks are also referred to as the “constraint” blocks. Some properties of these basic blocks are as follows:

• The definition block always dominates all uses of the SSA variable.  
• The basic block that has the definition can contain constraints. The same applies to any basic blocks of the def-use chain.  
• A definition block is always reachable and hence all the instructions in it are reachable too.

Considering this as a graph reachability problem, the question is, can we reach all the instructions in the def-use chain of the SSA variable in the presence of a constraint block? To answer this, we build a constraint graph from the CFG of the function and use a pathfinding algorithm on it:

• Remove the outgoing edges of constraint blocks from the CFG. This is our constraint graph.  
• Find if a path exists between the definition basic block and other basic blocks of the def-use chain in the constraint graph.  
• If any def-use basic blocks are not reachable, then those instructions are not used for taint propagation.

Since each assignment is unique in SSA representation, we maintain a per-variable dictionary of the necessary information including the constraint graph for later analysis. Here is a sample pseudocode to find reachable blocks in the presence of constraint blocks:

To find if an SSA variable is tainted at a given instruction, all we need to do is check its reachable def-use chain:

**_Arithmetic operations as filters_**

Other than explicit filters, there are also arithmetic operations that can also be taint filters. For example, AND or Logical Shift Right (LSR) operations may place constraints on a value. In such circumstances, a heuristic can be used to filter out undesired results. Consider the example below:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/0cf29020-fbaf-46b0-8606-408c39025cb9/Fig3.png)

Here, the tainted value is not explicitly compared against anything, but operations such as LSR and AND limit the input range. This is where I found the `possible_values` property very useful. Binary Ninja’s data flow analysis can provide possible values for an expression:

**Handling Transitively Tainted Variables**

The first stage of analysis propagates taint data and generates information such as a list of tainted variables, constraints placed on each SSA variable, and their respective constraint subgraphs.

During the second stage of analysis, we explore the relationships between the tainted SSA variables. Why is this important? We are only looking for unbounded SSA variables. While any direct constraints placed on an SSA variable are already handled in the first stage, the constraints placed on SSA variables that are propagated transitively are not yet handled. Consider the example below:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/24afd514-1dc9-4daf-8c00-b018388656ab/Fig4.png)

The `index#0` variable could be tainted and not constrained. However, the derived variable `constrained_var#1` is validated, indirectly placing constraints on the `index` variables. Therefore `index#3` is not tainted during the memory access at 0x11f2. Here is another example:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/4fb7d84c-6236-4f2e-a7ea-0144d3ca07bd/Fig5.png)

Here, `index#1`, `index#2`, `rax#1`, and `constrained_var#1` are copies or direct assignments of the variable `index#0`. When variable `constrained_var#1` is validated, the other variables are also validated. Not analyzing the effect of constraints on derived variables or copies of variables leads to false-positives. This section details ideas on handling constraints on related variables.

**_Constraints on transitively related SSA variables_**

After the taint propagation phase is over, we iterate through all the tainted variables that have constraints on them. For every variable with constraints, we find its child variables and parent variables.

• Variables that are derived from a given variable are called child variables.  
• Variables from which a given variable is derived are called parent variables.

To check if the constraints on the variable under consideration have any effect on its parent or child variables, we perform the below checks:

• Pick the constraint subgraph for the SSA variable under consideration.  
• Check if the definitions of child variables are reachable from the definition of the current variable.  
· If not, the constraint is placed before defining the child variable in the CFG, and therefore none of the basic blocks in the def-use chain are tainted.  
· If yes, the constraint is placed after defining the child variable in the CFG. In this case, also check if all basic blocks of the def-use chain of the child variable are reachable from the definition of child. Mark the non-reachable blocks as clean.

• For each parent variable, get its list of child variables. While all the child variables of the current variable are also child variables of the parent, parent variables might have other child variables too. The child variables already visited in the previous step can be skipped. Now check if the definitions of child variables are reachable from the definition of parent variable. For a yes or no, repeat the same as mentioned in the previous step to mark the non-reachable blocks as clean.

This way the non-reachable basic blocks are removed from tainted entries of variables related to a constrained variable. We can also choose to perform analysis on variables that are derived or just direct assignments using tags associated with a variable.

While propagating taint, two different tags were used – a direct memory load using `MLIL_LOAD_SSA` from tainted memory returns an offset, size pair as tag and it gets associated with the destination variable. Whereas for any derived variable, the destination variable is associated with a marker but not the offset, size pair. Consider the code:

The variable `rcx_1#2` is tainted with a tag `[0x2c, 0x4]`, which is the offset size pair. This is the same as the case with `rbx#1`, which is a direct assignment. However, `rbx_1#2` derived from the expression `rbx#1 u>> 5` is tainted with a tag `[0xdeadbeef, 0xdeadbeef]`. Using different tag type information, it is possible to identify the nature of taint propagation.

**_Constraints on SSA variables from multiple taint sources_**

While propagating taint, we mark a destination variable as tainted if any of the source variables are tainted, including the [PHI function](https://en.wikipedia.org/wiki/Static_single_assignment_form#Converting_to_SSA). During filtering in the second stage, if a variable is constrained, we apply the constraints to all is related variables. But, when the derived variable (child) is coming from more than one independent taint sources (parents) and only one of the parent variables is validated, the child variable is also considered validated. But this is not desirable. Consider the example below:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/79aefdb7-9c8e-47de-be1a-0955d8704017/Fig6.png)

Let’s say `x` and `y` are coming from two independent taint sources and `index` is a sum of both, hence a derived variable. When `x` gets validated, `index` can still be tainted since `y` is not validated. The previous algorithm does not take this into account.

To solve this problem, I considered associating each derived tainted variable with the actual source variables referred to as root variables and maintain copies of def-use chain per root variable. For example, variable `index#3` has two roots – `x#0` and `y#0`. For each root, maintain a copy of reachable blocks in taint information associated with `index#3`. When `x#1` is validated, only the `x#0` copy of `index#3` is marked not reachable and the `y#0` copy is still considered tainted. A dependency graph of variables is built to establish these relationships.

**_Establishing SSA variable relationship using a dependency graph_**

In a variable dependency graph, any tainted variable in the function is represented as a node. When a variable is derived from another variable, it forms a directed edge from the parent variable (node) to the child variable (node).

In order to establish a relationship between variables, the definition site of all the tainted variables is visited using `get_ssa_var_definition()`. When any of the source variables in the MLIL expression are tainted, create an edge connection in the graph. A variable tainted during `MLIL_LOAD_SSA` operation does not have a parent node or incoming edges and therefore becomes the root node.

Such a dependency graph will have many [weakly connected components](https://networkx.guide/algorithms/components/weakly-connected-components/) because each memory load from the tainted memory region will be assigned to a new variable and therefore a new node in the graph. Put simply, each memory load creates a subgraph along with its derived variables. A subgraph might connect with another when a variable is derived out of more than one root node. Here is a sample dependency graph from the function `Dbtux::execTUX_ADD_ATTRREQ()`:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/605ac207-43be-4f80-9265-7d0b914d2e70/Fig7.png)

Another property to note is that dependency graphs are not necessarily Directed Acyclic Graphs (DAG). This is because loops can be introduced by a circular dependency of variables in PHI functions. Consider the below SSA representation of a loop operation:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/3167af65-de8c-45fe-b787-fb379f8ae766/Fig8.png)

Here, the value of `counter#2` depends on `counter#1` or `counter#4`, which is a PHI function. The predecessor block decides the outcome of the function. Further down in the loop, `counter#4` depends on `counter#2`. This relationship will be represented as a cycle in a dependency graph.

Once the dependency graph is generated, it is easy to get the root variables associated with any tainted variables. Moreover, child and parent variables for any given variable can be fetched for handling transitive relationships. The only missing part now is the forward propagation of tainted information to other functions.

**Static Function Hooks and Inter-procedure Taint Propagation**

All the `MLIL_CALL_SSA` and `MLIL_TAILCALL_SSA` instructions with tainted arguments are processed once the analysis of the current function is finished. For any CALL instructions with a known destination (e.g., `MLIL_CONST_PTR`), the symbol is fetched to check for static hooks. Here is the code snippet:

Static hooks are handlers to functions that we intend to handle differently compared to other functions. Consider a call to the `libc` `memcpy` function, where taint propagation is not necessary but only interested in checking for tainted size, source, or destination arguments. In order to provide this information to the analyzer and make it configurable, a JSON config with function names and arguments is used as below:

The arguments to check are indexed from 0. In the case of `memcpy`, all 3 parameters are marked for analysis. The argument index provided in the JSON config is checked against the tainted SSA variables. For example, `arg2` in the config maps to an SSA argument variable associated with memcpy’s size argument.

Static hooks can also be used to mark an output variable or return value of a function to be tainted and further propagated. However, this is not currently implemented since function-specific details are not considered. When necessary, the visitor handler for the `MLIL_SET_VAR_SSA` operation can be reused for implementing backward taint propagation during CALL operations. For any other function without hooks, taint information is propagated by marking the target function’s variable as tainted.

**Tracing Vulnerabilities from Reachable Blocks**

Once the taint propagation and filtering phases are over, the last phase of analysis involves iterating through all tainted variables and checking the reachable blocks for potential sinks. Based on the bugs already reported, I chose to look for vulnerabilities involving Out-Of-Bounds (OOB) memory access, buffer overflows during function calls to APIs such as `memcpy`, untrusted inputs casted to a pointer, and tainted loop counters. The rest of this section details additional detection strategies.

**_OOB reads and writes_**

The majority of vulnerabilities in MySQL Cluster were OOB read and write memory access bugs due to the missing validation of untrusted array indexes. To detect these bugs, we can specifically consider any `MLIL_LOAD_SSA` or `MLIL_STORE_SSA` instructions as sinks. Here is an example code from `Dbdih::execGET_LATEST_GCI_REQ()`:

Here, `rax#1` is tainted, hence the read operation using `MLIL_LOAD_SSA` can be considered an OOB read condition. Similarly, consider another case from `Thrman::execOVERLOAD_STATUS_REP()`:

Here again, `rax#1` is tainted, hence write operation using `MLIL_STORE_SSA` can be considered an OOB write condition.

**_API buffer overflows_**

Static function hooks are used to detect buffer overflows caused by a lack of validation of arguments passed to functions like `memcpy`, `memmove`, etc. Details regarding this are already detailed in the section “Static Function Hooks and Inter-procedure taint propagation” above. Essentially, if any of the interesting parameters of a hooked function are tainted, we log it as a potential vulnerability.

**_Untrusted pointer dereferences_**

In some cases, I noticed that MySQL Cluster converts untrusted input to a pointer then dereferences it. To identify this, I relied on Binary Ninja’s type information. The MLIL variable object has a `Type` property that returns the `Type` object associated with a variable. A `Type` object’s type can be accessed using the `type_class` property. Here the pattern is that the source points to a tainted memory region within a `Signal` structure, and the destination variable is of type `PointerTypeClass`. The `Type` object also has a `confidence` property, as seen below:

The maximum `confidence` value for a variable type is 255. To reduce false positives, the analyzer only considers type information having the maximum confidence.

**_Tainted control flow operations in a loop_**

Loop termination conditions depending on tainted variables can lead to interesting bugs. Binary Ninja’s MLIL does not provide information on loops, therefore the alternative was to rely on HLIL to detect tainted loop conditions. The HLIL of a loop in `Cmvmi::execEVENT_SUBSCRIBE_REQ()` looks like the example below:

The trouble here is that we have implemented the entire taint propagation using MLIL, and Binary Ninja does not provide a mapping between MLIL and HLIL. Therefore, even if loops can be detected, the challenge is to know if a tainted MLIL variable maps to a HLIL variable used in a loop condition.

As a workaround, the HLIL instruction has a condition property that fetches the condition statement associated with a loop. The address of this condition statement can be mapped to a `MLIL_IF` instruction.

Therefore, if any of the `MLIL_IF` instructions are tainted and are a part of a HLIL loop condition, then the analyzer logs it as a potential bug.

**Experiments with Dominance Relationships**

A [dominance relationship](https://en.wikipedia.org/wiki/Dominator_\(graph_theory\)) provides information on the order of execution of some basic blocks. A basic block X is said to dominate another basic block Y if all paths to Y should go through X. Let’s take the example from Wikipedia:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/c4f9de03-9cf6-4581-90b3-42ce9b91771d/Fig9.png)

In the provided graph, node B dominates the nodes C, D, E and F because all paths to these nodes must go through node B. By definition, every node dominates itself. So, the full set of nodes that are dominated by node B is B, C, D, E and F. There is also a related concept called the strict dominator, which does not consider the node in question. Therefore, the set of all nodes that are strictly dominated by node B is C, D, E and F.

Binary Ninja’s `BasicBlock` object has `dominators` and `strict_dominators` properties which provides information regarding dominance relation in a function.

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/0e33f361-d091-4520-bc30-78f12371be8e/Fig10.png)

What about using the already available `dominance` properties in Binary Ninja for handling taint constraints instead of relying on graph reachability algorithms from `networkx` package?

**_Mapping constraints to dominator blocks_**

In order to check if any basic blocks in a def-use chain of an SSA variable are reachable, we can follow the steps below:

• Find all constraint blocks associated with a variable.  
• Get all the basic blocks that reference the variable using the def-use chain.  
• For each basic block, check if it is strictly dominated by a constraint block. If yes, the variable is considered validated for that basic block and considered not reachable.

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/4ec60823-4de5-48a8-85cf-0201ddbf9e75/Fig11.png)

Going back to the same example, the `index` gets validated in `<mlil block: x86_64@0-2>` which dominates the `<mlil block: x86_64@4-9>`. Therefore, by checking a constraint block against dominators it is possible to establish reachability.

**_False positives with dominators_**

While the dominance relationship was promising and gives good results, it does give rise to certain false positives. Consider the following CFG, where validation is done in two different program paths:

View fullsize

![](https://images.squarespace-cdn.com/content/v1/5894c269e4fcb5e65a1ed623/37b272f4-9cf9-4c3d-af9e-298c763e3498/Fig12.png)

Here, the `index` is validated in two different program paths before hitting a potential sink block `<mlil block: x86_64@11-16>`. However, none of the constraint blocks that perform validation `<mlil block: x86_64@3-4>` and `<mlil block: x86_64@4-5>` are dominators. In such cases, since constraint blocks cannot be mapped to any dominators, the potential sink block `<mlil block: x86_64@11-16>` will be considered vulnerable on read access at address 0x11ba. This is a false-positive result.

The same is the case with the [branch_dependence](https://blog.trailofbits.com/2018/04/04/vulnerability-modeling-with-binary-ninja/) property, which returns a dictionary of branch instruction index and the branching decision taken to reach the instruction. When both the True and False branches dominate the instruction basic block, we do not get information regarding reachability.

A general observation from the scan result is that most constraints are part of dominator blocks. Very few are validated across multiple code paths, producing false positives. Since path-finding algorithms relying on the definition and usage of variables eliminate these false-positive results, I preferred it over dominators. However, the code is still in the repository for experimental purposes.

**Notes on Analysis**

The target `ndbd` executable is loaded in Binary Ninja to generate the BNDB analysis database. Then the analyzer is executed against `ndbd.bndb` for faster analysis: 

`python3 mysql_bugs.py --function_hooks functions_to_hook.json ndbd.bndb`

Though not optimized for speed, the analyzer runs for about 4-5 minutes and returns 195 results. Some of the results are duplicates because a single vulnerability in a helper function might get used by multiple handlers. The analyzer was able to find most of the issues already known as well as a few that were not previously known: ZDI-CAN-15120, ZDI-CAN-15121 and ZDI-CAN-15122. However, there is a high triage cost associated with static analysis results, especially when the target is less familiar. Luckily, my colleague Lucas had already spent a fair amount of time on the codebase making it easier to triage the results. 

Source code for the project can be found [here](https://github.com/thezdi/binaryninja/tree/master/mysqlcluster).

**Acknowledgments and References**

• Thanks to Lucas Leong for all the discussions and triage. His blog post [MindShaRE: When MySQL Cluster Encounters Taint Analysis](https://www.zerodayinitiative.com/blog/2022/2/10/mindshare-when-mysql-cluster-encounters-taint-analysis) is an excellent reference for performing static taint analysis on MySQL Cluster.  
• [Tainted Flow Analysis on e-SSA-form Programs](https://homepages.dcc.ufmg.br/~fernando/publications/papers/CC11rimsa.pdf) which served as an excellent reference for taint analysis as a graph reachability problem.  
• Various blog posts from [Trail of Bits](https://blog.trailofbits.com/category/binary-ninja/) on Binary Ninja.  
• Josh Watson for various projects using Binary Ninja. The visitor class implementation is based on [emILator](https://github.com/joshwatson/emilator).  
• Jordan for all the [code snippets](https://gist.github.com/psifertex/6fbc7532f536775194edd26290892ef7) and the Binary Ninja slack community for answering various questions.

**Conclusion**

I hope you have enjoyed this look at using Binary Ninja to find vulnerabilities through taint analysis. In a few days, I’ll be back to discuss using Clang Static Analyzer (CSA) for detecting untrusted pointer dereferences and tainted loop conditions. Until then, you can find me on Twitter [@RenoRobertr](https://twitter.com/renorobertr), and follow the [team](https://www.twitter.com/thezdi) for the latest in exploit techniques and security patches.

  * [Binary Ninja](/blog/tag/Binary+Ninja)
  * [Taint Analysis](/blog/tag/Taint+Analysis)
  * [MySQL](/blog/tag/MySQL)
