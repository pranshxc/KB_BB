---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-30_an-offensive-look-at-docker-desktop-extensions.md
original_filename: 2023-05-30_an-offensive-look-at-docker-desktop-extensions.md
title: an offensive look at docker desktop extensions
category: documents
detected_topics:
- supply-chain
- command-injection
- api-security
- ssrf
- mfa
- automation-abuse
tags:
- imported
- documents
- supply-chain
- command-injection
- api-security
- ssrf
- mfa
- automation-abuse
language: en
raw_sha256: ae2eb88095c72d2e5352cc31f8287dd536936fc0a27bafaf1ebae84716ff2381
text_sha256: 9f71a536523decadbf2d9c00669b929e336806bf70f6f494c881bc20a0e72c04
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# an offensive look at docker desktop extensions

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-30_an-offensive-look-at-docker-desktop-extensions.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, api-security, ssrf, mfa, automation-abuse
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `ae2eb88095c72d2e5352cc31f8287dd536936fc0a27bafaf1ebae84716ff2381`
- Text SHA256: `9f71a536523decadbf2d9c00669b929e336806bf70f6f494c881bc20a0e72c04`


## Content

---
title: "an offensive look at docker desktop extensions"
page_title: "SensePost | an offensive look at docker desktop extensions"
url: "https://sensepost.com/blog/2023/an-offensive-look-at-docker-desktop-extensions/"
final_url: "https://sensepost.com/blog/2023/an-offensive-look-at-docker-desktop-extensions/"
authors: ["Leon Jacobs (@leonjza)"]
programs: ["Docker"]
bugs: ["OS command injection", "Container security"]
publication_date: "2023-05-30"
added_date: "2023-06-12"
source: "pentester.land/writeups.json"
original_index: 1102
---

For our annual internal hacker conference dubbed SenseCon in 2023, I decided to take a quick look at [Docker Desktop Extensions](https://docs.docker.com/desktop/extensions/). Almost exactly a year after being [announced](https://www.docker.com/press-release/docker-announces-docker-extensions-and-docker-desktop-for-linux-at-dockercon-2022/), I wondered what the risks of a malicious docker extension could be. This is a writeup of what I learned, a few tricks I used to get some answers and how I found a “non-issue” command injection in the extensions SDK. Everything in this post was tested on macOS and Docker Desktop 4.19.0 (106363).

tl;dr – Be extra careful with Docker Desktop Extensions given that it is significantly easier for a malicious extension to run commands, access files and more when compared to a traditional container.

A summary of interesting things I discovered include:

  * Extensions can execute arbitrary operating system commands, even if there isn’t a specific binary shipped with the extension. This is a confirmed bug and will be fixed later.
  * Running extension service “VM’s” (aka: service containers) don’t show up in `docker ps`. You have to run `docker extension ls` to see those. This could be a fun persistence technique where malicious code could hide in the extensions service VM, away from endpoint security products’ prying eyes.
  * Service “VM’s” being the long running components of an extension which run as a container can have more privileges than you would be comfortable to give by adding extra port/volume/privilege labels to the extensions `docker-compose.yml` file. Bonus points for the fact that most enterprise endpoint security solutions probably wont be able to inspect the docker virtual machine either… ;)
  * Unless an extension author makes their extension open source, the only way to see what it is really doing is to manually inspect / reverse engineer the extension itself. There is no UI to give you an idea of what could be happening, which binaries were included in the extension or otherwise give you an overview of what the extension could do. The most interesting warning is the docs, and a warning when you install extensions via the CLI.
  * Extensions don’t have to live on the extension Marketplace to be installable. Any well-formed container can be installed as an extension with the `docker extension install` command.

As this is a large post, here is a table of contents to help navigate it.

  * introduction
  * extension architecture
  * extension -> backend communication
  * extension security contexts
  * on service “VM’s”
  * the extension-api-client sdk
  * (host|vm).cli.exec
  * debugging docker desktop extensions
  * running host binaries
  * arbitrary command execution in docker.cli.exec()
  * getting the extension-api-client sdk source code
  * analysing the sdk and finding the “bug”
  * command execution risks in context
  * docker extensions for persistence
  * docker desktop extensions and the extension market place
  * investigating docker desktop extensions
  * investigating extensions before installing
  * investigating extensions after installing
  * conclusion

## introduction

Like most things, I need to do a bit of an introduction on Docker Desktop Extensions to set the groundwork for the rest of the post. There is a surprising amount of moving parts to extensions. I am going to assume you have a basic familiarity with container runtimes like docker and have an idea how Docker Desktop works with the Virtual Machine driving the container runtime and the Electron-based GUI itself.

As one does, I skipped reading all of the documentation and dove straight into the [quick start guide](https://docs.docker.com/desktop/extensions-sdk/quickstart/). My first shock came when I ran the `docker extension init` command as suggested.

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/7ceb5ac76652ccf29a363ddb3548c782.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/ce601dcac24ff6b6fd62427bc1d470a0.png)

Yeah, you are reading that right. A Go “backend” and a React UI resulting in 165MB worth of $stuff…
  
  
  $ du -sh
  165M	.

I pushed on through the guide in disbelief to see what the result would look like by building the extension and installing it as per the document. The result? A new entry in the “Extensions” section creatively called “My Extension” that when clicked, showed a user interface with a button and a text box for output.

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/741e483f6d482fada1baeabedb502098.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/785c4ba02ffc49ac0372fb30efad408a.png)

This button-pushing-inspecting-the-output flow was the general workflow I used throughout the testing of the Docker Desktop Extensions feature. For development there is a hot reload capability to reduce the time of the feedback loop using the `docker extension dev ui-source docker-test-extension http://localhost:3000/` command which sets an extensions frontend to point to a local web server (which will make more sense in the next section). Using this you don’t have to go through the long `docker build` part before you can see an incremental change you made, but rather, they reflect almost immediately. 

## extension architecture

Based on what just happened when running the init command, I figured I needed help to know what could possibly warrant so much complexity. So on to the next document we go. More specifically, the [architecture document](https://docs.docker.com/desktop/extensions-sdk/architecture/) that has an image with the high level extension architecture. 

While the documentation is definitely useful (who knew), after diving under the hood a little I came up with an expanded image that I think paints a clearer picture on all of the moving parts as well as how they interact with each other (according to my understanding anyways).

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/c58884f07b92b3afb2cb0bcba96a5509.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/dfe056bdc3786f410523e7d4c3506791.png)

Frontends are written using your typical web technologies (HTML, JavaScript and CSS). Docker generates a React UI skeleton as a suggestion when you init a new extension. Logically, frontends can reach optional extension specific backends which are really just containers (can be multiple container services too) and do this via the [@docker/extension-api-client](https://www.npmjs.com/package/@docker/extension-api-client) SDK (embedded within Docker Desktop; more on this later). `docker init` also generates a Golang backend skeleton as an example (more on this later too).

Extension frontends don’t persist anything by design; this is what backends can be used for. In fact, extension UI’s die/reload when you navigate away from them in the UI and forcefully cleanup / kill any long running tasks when needed. Extension backends (also confusingly called “VM’s”) on the other hand live for as long as the extension is installed. Backends are typically web services that can be easily invoked from the frontend via a socket-like interface that the SDK exposes.

## extension -> backend communication

It’s probably obvious by now, but frontends need to talk to backends. This capability is exposed via the frontend SDK that the extension must use. Under the hood things are a little more complicated though. 

As you may know, Docker Desktop interacts with the Docker Desktop Virtual Machine via a local docker socket. The logic that handles this connection to the docker socket is part of Docker Desktop and is implemented in JavaScript as you’d expect from an Electron application. Extensions also communicate via sockets to backends, however they don’t use the docker socket. Instead, extension backends need to explicitly expose their own socket such that the frontend (via the SDK) can communicate with it. Technically you could expose a TCP socket, but the documentation suggests a unix socket / named pipe to prevent port clashes with the host operating system. Regardless of the target, Docker Desktop handles all socket communications using the same underlying library and will connect as appropriate depending on where it needs to go. For extensions, a socket hint is needed as part of the extension metadata so that it knows which backend a specific extension connects to.

Visually, communication flows could be represented as follows (where a container service lives within the Docker Desktop VM and an extension UI lives within the Docker Desktop Dashboard:

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/9d8c7e61e89b7ee3fa787eb87d4d5a08.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/5e1b984beba78660243158165c0f8165.png)

## extension security contexts

The [documentation](https://docs.docker.com/desktop/extensions-sdk/architecture/security/) is fairly clear on the security context of each component of Docker Desktop Extensions. Extensions effectively run as the same user running Docker Desktop, and have the same permissions. More specifically, while the UI runs as the same user as Docker Desktop is running as, the backend runs as a container (which could technically be seen as having less permissions itself but can be configured very permissively as you’d see later).

Extension User Interfaces can leverage the SDK to interact with docker itself, or execute any scripts and or binaries shipped as part of the extension (aka: defined in the extensions metadata). You also have the ability to run new containers which implies that an extension can run any container to execute code, mount any filesystem path and make (and listen for) network connections (via the service container) to local networks.

In summary, for as long as its possible to run arbitrary containers from the UI component, docker desktop extensions will effectively be arbitrary processes running on your host with no real sandboxing / privilege separation.

## on service “VM’s”

An extension can have one or many supporting services (confusingly called “VM’s”). These are simply docker containers that are orchestrated using a docker-compose.yaml file part of your extension’s source. The default service from the init command is fairly simple.
  
  
  services:
  docker-test-extension:
  image: ${DESKTOP_PLUGIN_IMAGE}

That in itself is not very interesting, but nothing stops a service from having some extra fun labels like:
  
  
  services:
  docker-test-extension:
  image: ${DESKTOP_PLUGIN_IMAGE}
  privileged: true
  volumes:
  - /:/host_root
  - /var/run/docker.sock:/host-docker.sock
  ports:
  - "8280:8280"

Something that really surprised me was that a service VM, even though it’s a container, does now show up when you run `docker ps`.
  
  
  $ docker ps  -a
  CONTAINER ID  IMAGE  COMMAND  CREATED  STATUS  PORTS  NAMES

Instead, you need to run `docker extension ls` to see extensions, and then infer that containers are running from the `VM` section in the output table.
  
  
  $ docker extension ls
  ID  PROVIDER  VERSION  UI  VM  HOST
  grafana/docker-desktop-extension  Grafana Labs  0.0.2  1 tab(Grafana)  Running(2)  -

It was also not immediately obvious to me how one would know which legitimate sockets an extension was listening on, or, because the `docker-compose.yml` can have so many other properties, which ports might be open and or volumes are mounted. Not great.

## the extension-api-client sdk

When a new UI component is scaffolded using the `docker extension init` command, one of the libraries imported is the extension-api-client library.
  
  
  import { createDockerDesktopClient } from '@docker/extension-api-client';

This is the primary library used to glue the extension to Docker Desktop and an optional backend service. A function called `createDockerDesktopClient()` is invoked to get a new `DockerDesktopClient` instance from where [various API calls](https://docs.docker.com/desktop/extensions-sdk/dev/api/reference/README/) can be made.

I couldn’t find the actual source code online for the library, but rather [a shim](https://www.npmjs.com/package/@docker/extension-api-client?activeTab=code) that would throw an error if the `.ddClient` property was not available on the `window` object.
  
  
  export function createDockerDesktopClient() {
  const ddClientFromWindowObject = window
  ?.ddClient;
  if (!ddClientFromWindowObject) {
  throw new Error('This version of @docker/extension-api-client is not supported by your version of Docker Desktop. Please upgrade to the latest version.');
  }
  return ddClientFromWindowObject;
  }

This is not a problem (as you will see later), and so I just decided to play with the API the `DockerDesktopClient` object provided for now. A simple way to do that is to just use the code completion VSCode is smart enough to setup for you to learn about it.

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/f3398af702ae4b11c1832f43a2a081e4.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/f8bde56adefe4b3febc5963bc16037e2.png)

The API is not very large, but three interesting functions immediately stood out for me:

  * ddClient.docker.cli.exec()
  * ddClient.extension.host.cli.exec()
  * ddClient.extension.vm.cli.exec()

I’ll be honest, the first time I saw these I had no idea what they really meant and I assumed a lot. My gut feel wasn’t too far off, and neither is yours if this is the first time you see them.

I took the boilerplate code and started messing with the function calls used on the created `DockerDesktopClient` instance to instead of calling the backend service, just invoke these exec() functions and populate the output in the UI (with the hot reloading feature I mentioned earlier configured). Effectively that meant that I only had to fiddle with the already provided `fetchAndDisplayResponse` function, save my changes, tab back to Docker Desktop and click the “Call backend” button to see the effect. For example:
  
  
  const fetchAndDisplayResponse = async () => {
  const result = await ddClient.docker.cli.exec("ps", []);
  setResponse(JSON.stringify(result));
  };

This function would update the extensions’ UI to show the output of the `exec()` function I called which supposedly (spoiler: it did) called `docker ps` under the hood like this:

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/22a6e170bb9f774a5338f4bd27cbbbc9.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/1afcb093d920681701da9a3b681c59e5.png)

Up until this point, everything behaved pretty much as I expected and matched what I read in the docs.

## (host|vm).cli.exec

The `ddClient.extension.host` and `ddClient.extension.vm` properties, as the names imply, refer to the service VM (aka: the backend) and the host operating system. Both of them have the `cli.exec()` function with the same signature, but behave slightly differently.

Let’s start with the service specific exec function, `vm.cli.exec`. Given the following line of code to run the `ls /` command:
  
  
  const result = await ddClient.extension.vm?.cli.exec("ls", ["/"]);

The resulting output in Docker Desktop would look as follows:

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/4ffa7f4877e2cc1755084d6fd4cce971.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/3a7b9c28ee4d87ed051df5a6c6c7f950.png)

That is the output as expected. A (hard to read) list of files and folders inside of the docker container which is also the container where the backend service that the boilerplate `docker init` generator provided is running. Easy enough.

To run a command on the host, I simply ran the host variant of the same code as follows:
  
  
  const result = await ddClient.extension.host?.cli.exec("ls", ["/"]);

The difference in output though was… that there was no output. I reloaded the extension numerous times, double checked for syntax errors and more, but no dice. I had to go deeper!

## debugging docker desktop extensions

Given that Docker Desktop is an electron application, it’s not strange to imagine that you can open the Chrome console/debugger attached to it. The question though is, how?

`up, up, down, down, left, right, left, right, p, d, t`

That is how. [I’m not even kidding](https://docs.docker.com/desktop/extensions-sdk/dev/test-debug/#open-chrome-devtools). While a variation of the [Konami Code](https://en.wikipedia.org/wiki/Konami_Code) funny the first time, it’s incredibly frustrating to deal with given how often the console window closes, forcing you to repeatedly type this sequence; every, freaking, time.

## running host binaries

With the developer console open, I could finally see some debugging output when I tried to run `ls` on the host.

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/7cb85e635c585aa92c8fd94b14e08a56.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/37fd57c728106b0db0f3cbba1eec6d49.png)

Turns out there were two problems. One, exceptions weren’t propagated to the UI which is why I needed the console (meh). Two, apparently my extension tried to run `ls` relative to the current directory. This wasn’t a problem when running `ls` in the container though. Okay, so let’s try running `/bin/ls` instead then.
  
  
  const result = await ddClient.extension.host?.cli.exec("/bin/ls", ["/"]);

The result?

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/901a4f7ff686f8e4d209d648482a641d.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/2558fd38e9ec8b3f4009318618b1c510.png)

I double checked my own sanity, and confirmed that `/bin/ls` really is where I thought it would be, but instead, the response when trying to execute it is a sentence specifically saying that the extension binary is not found. Does this mean extensions can’t execute arbitrary commands on the host operating system?

I checked out [the documentation](https://docs.docker.com/desktop/extensions-sdk/guides/invoke-host-binaries/) once more to see what the intended flow was here, and learnt about the fact that an extension itself needs to also ship any scripts/binaries it wants to run. These binaries/scripts must be declared in the `metadata.json` file for each supported operating system / architecture and will be copied to the service VM (aka: backend) when building the extension. When installing the extension these will be copied to the host operating system. That means, if I wanted to have a script available to run from the frontend UI, I needed to declare a new block in my `metadata.json` file like this (next to the `ui` and `vm` keys) with the path where it will be in the service container:
  
  
  "host": {
  "binaries": [
  {
  "darwin": [{ "path": "/poo.sh" }]
  }
  ]
  }

The `Dockerfile` for the extension would simply copy the executable script from a local path into the container on build with this line:
  
  
  COPY poo.sh /poo.sh

After building the extension and finally installing it with the `docker extension install` command, a few lines showing that binaries are installed on the host (well really just copied out of the container into an extension specific directory on the host which was `~/Library/Containers/com.docker.docker/Data/extensions/extension-name/host/` for me) should show up:
  
  
  ...
  
  Installing Desktop extension binary "poo.sh" on host...
  Desktop extension binary "poo.sh" installed
  
  ...

With that all set up, running the `host.cli.exec` call with my new script should now look like this.
  
  
  const result = await ddClient.extension.host?.cli.exec("poo.sh", []);

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/ed3513b5e14f334d2d73acab15f4ba7d.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/69326c4963401765f4a0af78fcee8797.png)

To double check that the file on my host operating system really was the one the extension UI would run, I updated it from the host to print the current working directory as well, and reran it via the Docker Desktop Extension UI.

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/a13b38a9d2cfaaaf79c2ec21b26b31da.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/a13b38a9d2cfaaaf79c2ec21b26b31da.png)

As expected, the output updated to include the result of the `pwd` command that I had added.

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/d78adca9e426fca27b34e75aa7569527.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/d0acdeb3edb976fea92e874f32349a24.png)

Great. So it seems like there is something preventing one from running arbitrary operating system commands using just the SDK. The question though is, what and how does that work?

## arbitrary command execution in docker.cli.exec()

At this point I figured I knew enough about the SDK and how it was intended to be used that I started playing around a bit more. To recap, the host and VM versions of `cli.exec` had the same function signatures, but behaved differently in that the VM version did not sanitise paths whereas the host version did.

I tried a few things to try and get `host.cli.exec` to execute a command without it being in the `metadata.json` file first, but none of my cheap shots were successful. This included messing with some `ENV` variables you can set in the `exec` call via an optional `ExecOptions` argument. In most of the cases the console session attached to the extension UI told me the binary can’t be found, or threw some exception.

For a moment I turned back to the `ddClient.docker.cli.exec` call though and notices the `ps` argument passed to it; just like you’d use on the command line. I tried a classic command injection in the first argument there using something like `ps; pwd`. That meant my code looked something like this:
  
  
  const result = await ddClient.docker.cli.exec("ps; pwd", []);

The result?

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/25ecb0c263a05ab8f0b30d94864b4eaa.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/adfc632008eda0eb53f390e8993e93d8.png)

Arbitrary command execution using the SDK via the docker.cli.exec function!

At this stage I really wasn’t sure what this meant, if anything at all. Even though the host/VM exec versions clearly behave differently and it seemed like some effort was made to prevent extensions from running arbitrary operating system commands using the SDK, all of that was bypassed via the `docker.cli.exec` implementation. I was also mostly confused about why this injection worked in the first place, so, I started hunting for the SDK source code to learn more.

## getting the extension-api-client sdk source code

As I’ve mentioned previously, the `@docker/extension-api-client` source code wasn’t particularly interesting as it only contained a shim to check if the `ddClient` object was available on the `window` object. With Docker Desktop being an Electron application, one can easily supply extra JavaScript libraries as part of the application’s bundle, and it seemed like Docker decided that the source code for the SDK is not something you can get on Github (at least, not where I could find it). Not to worry though, Electron applications typically have their source code bundled into an [ASAR archive](https://www.electronjs.org/docs/latest/tutorial/asar-archives). There is even a handy [asar utility](https://github.com/electron/asar) to work with these archives provided by Electron which includes the ability to extract them.

On macOS, the Docker Desktop ASAR archive could be found in `/Applications/Docker.app/Contents/MacOS/Docker Desktop.app/Contents/Resources`. I copied the `app.asar` file together with the `app.asar.unpacked` folder to a temporary directory and extracted it there using the `asar extract` command. This left me with the following files and folder structure:
  
  
  ? ll
  Permissions Size User  Date Modified Name
  drwxr-xr-x  - leonjza 23 May 22:47  node_modules
  .rw-r--r--  945 leonjza 23 May 22:47  package.json
  drwxr-xr-x  - leonjza 23 May 22:30  src_transpiled
  drwxr-xr-x  - leonjza 23 May 22:30  web

I did a quick check to see if what I was looking for was in any of these files with a quick grep. 

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/944fe078a86ba2f58452074a4ca9c3d2.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/94c975e897ce54fc2ea0c98f0914eb82.png)

Yeah, this was it for sure. More specifically, the search revealed a directory called `extension-api-client-ipc` which was named closely to the one I was after. That was where I started to check for hints on how this all worked.

## analysing the sdk and finding the “bug”

I am not going to bore you with all of the details of the SDK, but I’ll highlight a few key things to learn from the codebase. Bonus points for the fact that it looked like the TypeScript source code was available, unminified. That made for very easy reading and analysis! Heck, for the most part VSCode intellisense even worked!

The SDK’s `src/createExtensionNode.ts` file had a function called `createExtensionNode` which returned a object that matched the SDK API. Notice the `TODO` there. I think someone knew what was coming here. :D 

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/f04f0ab504e8844c09be0bb8de4f8da4.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/6e5632ae2b1760c2bef9829d8ee7583b.png)

The SDK made heavy use of the Electron [ipcRenderer](https://www.electronjs.org/docs/latest/api/ipc-renderer), to communicate between the extension and the main Electron thread asynchronously. For example, the `host.cli.exec` function would call something like `ipcRenderer.postMessage('extension-spawn-cmd', ...);` (a reduced example) to effectively invoke whatever is registered to listen for `extension-spawn-cmd` to do some work.

In another location (not specifically the SDK now), in `src_transpiled/extensions/registerDashboardPageIpcHandlers.js`, many Electron IPC handlers were registered such as `extension-spawn-cmd`. These were implemented for example as `electron_1.ipcMain.on('extension-spawn-cmd', ...)`. From here we could finally see the real functions invoked to execute commands coming in from an SDK function invoked by an extension.

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/53a3029207e40f753bf0be38b0490999.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/f2540af799821a1af560e3dd1d0470df.png)

The `spawnHostCmd` was probably the most important function to find.

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/24b9bc1dd855c36e04fb139a3837d333.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/e289f1641996f9369b39657940568157.png)

This function does a path check on the `cmd` argument received, and if it does not exist, return the error we saw earlier when trying to run binaries with `host.cli.exec`. If everything checks out, execution passes to `spawnCommand` that simply does a [child_process.spawn](https://nodejs.org/api/child_process.html#child_processspawncommand-args-options) while gluing all of the relevant event listeners and cleanup routines together. In summary, `spawnCommand` takes a raw command and runs it.

In the same file though, there is a function called `spawnDockerCmd`.

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/8c1090042fbae505530451c1725faca0.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/f8c64a13fc170b3525ba9bc610033e42.png)

Notice how this function is simply a wrapper to `spawnCommand` and not `spawnHostCommand`? I double checked the flow from the `docker.cli.exec` definition for the SDK to here and it checked out. This is why a command injection in `docker.cli.exec` works; it’s literally just a wrapper to `child_process.spawn`. It makes sense too; the `docker` binary is not shipped with the extension but rather is available on the host so the path check in `spawnHostCommand` would cause it to fail.

## command execution risks in context

To be upfront, I am not sure about the risks of the command injection I found, especially in the context of what is possible with a Docker Desktop Extension by default. It could totally be a non-issue given how many different ways you could achieve the same thing with extensions.

The documentation as well as the `docker extension install` command warns you multiple times about the risks involved. However, most of the confusion for me in terms of risk is driven by the fact that some effort is made to limit what an extension can execute on the host running Docker Desktop from the UI. If you consider that backend service VM’s can mount any directory (via the `docker-compose.yml` file) and have any code they would want to run shipped as part of a container (including scripts that contain arbitrary commands), maybe the command injection really isn’t that interesting (or not even a bug to begin with)?

There is also the fact that you can run any arbitrary docker containers using the UI SDK which would effectively boil down to the same risk. For example:
  
  
  const result = await ddClient.docker.cli
  .exec("run", ["--rm", "-v", "/:/host_root", "alpine", "cat", "/etc/passwd"]);

When considering extension reviews (or otherwise investigating what an extension does which I touch on later in this post), it’s nice to have an overview of what an extension may be up to given the `metadata.json` file and SDK API usage (assuming no bugs) which is what I think Docker went for here. As extensions don’t have to be open source and can easily minify/obfuscate their source code, spotting malicious use of the `docker.cli.exec` function might be hard.

Then there is the other problem. It’s not immediately obvious to me how a user is supposed to verify (or get an overview of) how a particular extension works other than the description on the Marketplace to determine if they trust it. The only option really is to manually investigate it (which I dive into a bit later).

I reported this issue to the docker security team, and their response in short was that this is a non-issue, though they will try and fix the injection in a later release.

## docker extensions for persistence

Because backend service VM’s are long running containers, and the fact that they don’t show up when running `docker ps`, I figured it would be interesting to consider how extensions could be used for persistence. More so because they effectively run with the same privileges as the user running Docker Desktop.

Because the UI tears down completely when navigating away from it in the Docker Desktop application, I figured it wasn’t that interesting a place to have some code running that could be useful later. Especially if you wanted to make it not so obvious. Backend service VM’s however are significantly more interesting.

But, wouldn’t it be cool if we could have a service VM running without it being visible in Docker Desktop? We’ll, turns out if you just omit the value defined in the `metadata.json` file for the `ui.dashboard-tab.title` key, or completely omit the parent `ui` key, the extension will run the service VM without a tab showing up in Docker Desktop Extensions list. It will however show up in the extensions’ “Manage” tab.

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/151262be1ba6d7c31c8096c56c2d6182.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/5c444cc046a92ffecc93e8e3b394510d.png)

In contrast, when an extension with a UI is installed, it typically shows up in the Extensions list making it a little more obvious that an extension is running.

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/30ca80339c049097e6950727a41d98d5.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/1b08e992a00c2bb4ff39982de7725b6f.png)

The next thing you may notice is how little information is shown in the manage tab of the Docker Desktop UI for my test extension. Part of the extensions requirements for service VM’s is that you need to declare various labels in your Dockerfile for the service VM. Only the `com.docker.desktop.extension.api.version` label was required when I built it locally, so leaving everything else blank has your extension tell a little less about itself to Docker Desktop. This may be a good or bad thing, depending on how you plan on hiding in plain sight ;). Keep in mind though that this will fail with the `docker extension validate` if you plan on publishing your extension on the market place.

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/2d46d19c5d9ae138d30faef46f4ed0dc.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/5a088bf7db3781dbe70220058ab496f8.png)

The `docker-compose.yml` file is probably the most important part to have your service VM able to do anything interesting beyond maybe just being a tunnel into the target network where a malicious extension is installed (which is already powerful). Access to the host operating systems filesystem can be achieved with a mount point defined that makes the compose file look something like this:
  
  
  services:
  docker-test-extension:
  image: ${DESKTOP_PLUGIN_IMAGE}
  volumes:
  - /:/host_root

This will have a Docker Desktop Extension service VM have access to the host operating systems file system. Inside of the service VM there could be code running that makes a connection out to a command and control server, ready to execute commands, setup proxies to an internal network and or read files of the host (to name a few); all without you really knowing that this is obviously happening. Lastly, given that Docker Desktop depends on a backend Virtual Machine to run, I’m not sure of many endpoint security products having the ability to peek inside of VM’s to spot something nefarious happening there.

As for a PoC, I’ll leave this as an exercise for the reader to explore a little further ;)

## docker desktop extensions and the extension market place

The next part you might be wondering is how the Docker Desktop Extension marketplace helps with any of this. Docker has a guideline for how extension marketplace submissions work, along with the verification workflow [here](https://www.docker.com/products/extensions/submissions/). In summary, the extension needs to meet some requirements and the review process is manual. In exchange, your extension gets a cool “Reviewed” label.

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/40203c37ed46d1db0eb773e5ebc4a56f.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/4ae04db092701e638255785c4506cbe9.png)

Looking at the publishing documentation [here](https://docs.docker.com/desktop/extensions-sdk/extensions/publish/) though, you can also find a link to “Self-publish” your extension which appears to be driven by a Github Action workflow that automates extension publishing to the marketplace without human intervention. For example, [this submission issue](https://github.com/docker/extensions-submissions/issues/70) shows that in action. Doing it this way has your extension show up in the market place with a “Not reviewed label”.

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/be87ecbf5a7954b403f887731dc24216.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/ddfd510cba1bec62dc7b4a469f95e315.png)

I did not try and publish a malicious extension myself, though I imagine the automated submission process of a seemingly benign extension would have at least some shelf-life. More so abusing the command injection I found.

That said, your extension does not have to be in the Marketplace to be installable. You can simply publish your extension container to a registry and install it with `docker extension install`. For example:

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/ef6b62bb34d595aa87cea03edda56be5.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/ec4edf1456157cb7b7bf5212ec5e36ee.png)

## investigating docker desktop extensions

So I just spoke a lot about all of the bad things an extension could potentially get up to. The more important question though should be: “How can I investigate extensions myself?”.

You are generally interested in two things. The frontend UI and the backend service(s). Diving into each, below is a handy guide with some tips to dig under the covers and see whats really happening depending on if you have installed the extension already, or not.

The basic components you should be interested in is the `docker-compose.yml`, the `metadata.json` file, the service containers themselves and finally the UI sources.

The `metadata.json` file could give you an idea of where:

  * The `docker-compose.yml` lives together with any unix sockets/named pipes it will expect to connect the UI.
  * The UI source code lives.
  * Any host binaries are that will be copied to the OS.

The `docker-compose.yml` file should be checked as it could enable services to:

  * Mount host directories into the container.
  * Grant the container extra privileges.
  * Mount in the docker socket to do all of the above.
  * Open arbitrary ports.

The UI source directory could be checked to see if there is:

  * Suspicious usage of the Docker Desktop Extensions SDK. i.e. Is the UI spawning arbitrary containers?
  * Host binary invocation and what that is? Maybe even command injections ;)

One issue you may run into with the UI components is that extension authors could easily minify and or otherwise obfuscate the JavaScript sources, making it difficult to analyse. In fact, of the few extensions I looked at nearly all of them at least minified their JavaScript sources. Annoying.

Finally, the service VM containers themselves are obviously interesting. These containers could really be running anything, so I would suggest investigating them separately, inspecting their layers with tools such as [dive](https://github.com/wagoodman/dive) and getting an idea of what is run inside.

Regardless, now that you know which components of extensions are interesting, lets look at how you can get hold of these files depending on if an extension has been installed or not.

### investigating extensions before installing

This is the one method of investigation that does not involve you actually installing the extension with Docker Desktop. When browsing the marketplace, you will see references to the DockerHub repo where the extension is hosted. For example, looking at the PGAdmin GUI, we can see the repo is `mochoa/pgadmin4-docker-extension`:

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/b314d3ab8b1dbe188de2792caf32f055.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/67308624f1bb2198b45a3ca4346871d0.png)

This means the extensions repo is: <https://hub.docker.com/r/mochoa/pgadmin4-docker-extension>. Looking at the DockerHub page, we can see we can pull the container with `docker pull mochoa/pgadmin4-docker-extension:7.1.0` (specifying the version number for the container as it does not seem to have a `latest` tag). We can run the extension container as is with the `docker run --rm -it mochoa/pgadmin4-docker-extension:7.1.0 sh` command, specifying that we want an `sh` shell in the container. We’re mostly banking on the fact that we’re not exposing ports and or mounting any folders into the container as a form of safety for us to explore the internals.

Once you have a shell in the container, there is a lot of information about the extension available to check, which includes the extensions’ `metadata.json`, the `docker-compose.yml` and the `ui` folder. These are all included as a result of the build phase of an extension.

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/92b263e4389f9653b1de1aa5d1f5b83e.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/f611e447ba2cc50811b97f97e5715eb9.png)

If the extension ships binaries, the `metadata.json` file will reveal their locations which you would be able to access here as well.

### investigating extensions after installing

If an extension is already installed, well, you will have most of the artefacts you need on-disk already. To know which extensions are installed, run the `docker extension ls` command. This command will also give you an overview of the components the extension consists of, which include a UI, service VM and host binaries.
  
  
  $ docker extension ls
  ID  PROVIDER  VERSION  UI  VM  HOST
  docker-test-extension  -  Running(1)  1 binarie(s)
  tailscale/docker-extension  Tailscale Inc.  1.0.0  1 tab(Tailscale)  Running(1)  1 binarie(s)

On the host operating system, depending on the OS itself, installed extension artefacts will be available in:

  * macOS: `~/Library/Containers/com.docker.docker/Data/extensions/`
  * Windows: `%userprofile%/AppData/Local/Docker/`
  * Linux: `~/.docker/desktop/`

Each extension will be contained in its own folder, but apart from the service VM itself, everything you need to get an idea of what an extension may be doing will be available in these directories. For example, taking a look at the [Tailscale](https://hub.docker.com/r/tailscale/docker-extension) extension on a macOS host:

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/482bf51c2fbe4698080ea4a2dfeef9a2.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/f6e050068bfb6522dc1b6948da9ad8ca.png)

Having an idea of the file artefacts on the host (metadata, docker-compose, ui etc.) is interesting, but you may also want to have a look at the service VM itself too. This is a little more tricky. Remember that the service VM’s (aka: containers) don’t show up in `docker ps`? Well, you need to get a shell in the Docker Desktop VM first, then enter the namespace for the extension service to get access to that “container”. Imagining you have the Tailscale extension installed, you would do something like this.

[![](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/a37c31da7d18d8359a4d33e3327e6085.png)](/img/pages/blog/2023/an-offensive-look-at-docker-desktop-extensions/fefee47086501a0a269ba12aaa21cf49.png)

Spawn a container with `--pid=host` such that you enter the docker-desktop VM’s host namespace with the container. I’m using a simple debian container here, running `bash`.
  
  
  docker run -it --privileged --pid=host debian bash

Next, list the namespaces that are running / available on the host with `lsns`. I’m filtering the output columns here as well as filtering the type to be `pid` only so that I can only see command running in a pid namespace.
  
  
  lsns -t pid -o ns,pid,command

Knowing the PID of a target program, we can `nsenter` into the namespace where that program is running.
  
  
  nsenter -t 2474 -a

This should drop you into a shell environment in the context of the Docker Desktop Extension. I realise you wont always obviously know what software is running in the container, so you may need to know a better to find the target namespace, or trial and error a bit :)

## conclusion

In summary, while extensions provide an easy way to add powerful capability to Docker Desktop, they have a surprisingly complex architecture and by extension are excellent candidates for persistence and arbitrary code execution. I think a lot of work still needs to be done to help people understand what extensions are capable of, along with better ways to make it obvious in the Marketplace what extensions are going to try and do. A bit like the permissions overview you see in mobile app stores so that you can choose if you want this or not. As for the command injection, I am undecided on the risks given the overall architecture of extensions. I guess only time will tell where this will go.
