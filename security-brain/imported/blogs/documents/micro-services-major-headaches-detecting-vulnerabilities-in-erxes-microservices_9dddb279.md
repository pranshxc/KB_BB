---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-03-21_micro-services-major-headaches-detecting-vulnerabilities-in-erxes-microservices.md
original_filename: 2024-03-21_micro-services-major-headaches-detecting-vulnerabilities-in-erxes-microservices.md
title: 'Micro Services, Major Headaches: Detecting Vulnerabilities in Erxes'' Microservices'
category: documents
detected_topics:
- jwt
- ssrf
- command-injection
- file-upload
- path-traversal
- otp
tags:
- imported
- documents
- jwt
- ssrf
- command-injection
- file-upload
- path-traversal
- otp
language: en
raw_sha256: 9dddb279febeb6f6386f2f57c8691e456c7c09657398b193ef20a9ac48246b7c
text_sha256: d9b8de9fbf83f171f555089f0c39e920f65ad8d6bc8c2bae3c8cd1064efd9c19
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: true
---

# Micro Services, Major Headaches: Detecting Vulnerabilities in Erxes' Microservices

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-03-21_micro-services-major-headaches-detecting-vulnerabilities-in-erxes-microservices.md
- Source Type: markdown
- Detected Topics: jwt, ssrf, command-injection, file-upload, path-traversal, otp
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: True
- Raw SHA256: `9dddb279febeb6f6386f2f57c8691e456c7c09657398b193ef20a9ac48246b7c`
- Text SHA256: `d9b8de9fbf83f171f555089f0c39e920f65ad8d6bc8c2bae3c8cd1064efd9c19`


## Content

---
title: "Micro Services, Major Headaches: Detecting Vulnerabilities in Erxes' Microservices"
page_title: "Micro Services, Major Headaches: Detecting Vulnerabilities in Erxes' Microservices | Sonar"
url: "https://www.sonarsource.com/blog/micro-services-major-headaches-detecting-vulnerabilities-in-erxes-microservices/"
final_url: "https://www.sonarsource.com/blog/micro-services-major-headaches-detecting-vulnerabilities-in-erxes-microservices/"
authors: ["Paul Gerste"]
programs: ["Erxes"]
bugs: ["RCE", "Path traversal", "Authentication bypass", "Arbitrary file overwrite", "GraphQL", "SSRF", "Security code review"]
publication_date: "2024-03-21"
added_date: "2024-05-11"
source: "pentester.land/writeups.json"
original_index: 368
---

## TL;DR overview

  * Sonar's research uncovered critical vulnerabilities in Erxes—an open source microservices platform—including an authentication bypass and a path traversal flaw that together allow unauthenticated attackers to take full control of an instance.
  * The authentication bypass exploits trust between Erxes microservices: a user header passed between containers was never validated, allowing any service to impersonate any user.
  * Chaining the path traversal with Redis SSRF enables attackers to read environment variables containing authentication secrets, escalating the initial low-impact finding to full compromise.
  * Both vulnerabilities were fixed in Erxes 1.6.3; teams using similar inter-service header trust patterns should add HMAC signing to prevent authentication bypasses even when SSRF is present.

As a developer, it can be hard to triage a reported vulnerability. How relevant is the issue? What could an attacker do? Is this actually a valid finding? In this article, we'll show you how to answer these questions based on a real-world example.

To benchmark and improve our security engine, we regularly scan open-source software and triage the findings. One of these scanned projects is [Erxes](https://erxes.io/), an open-source experience management solution. It's quite a complex piece of software with multiple microservices that can talk to each other.

After scanning the project's code on [SonarQube Cloud](https://sonarcloud.io/), we noticed two interesting vulnerabilities among the findings. If you want to follow along with this blog post, you can [view the issues on SonarQube Cloud here](https://sonarcloud.io/project/issues?impactSoftwareQualities=SECURITY&resolved=false&sonarsourceSecurity=path-traversal-injection&types=VULNERABILITY&id=SonarSourceResearch_erxes-blogpost); no account required! Let's dive in:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/016dac94-a4c1-484e-8f44-d8b236e444f1/erxes-sonarcloud-findings.png)

We can see that they are labeled as _intentionality_ issues that impact the _security_ of the software. This means that SonarQube Cloud detected a code pattern that does more than the developer intended and that it can lead to security problems. Let's take a closer look at the second finding:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/897a11f0-232f-400c-ad2d-ba8f049fe545/erxes-sonarcloud-finding-1-sink-zoomed.png)

The annotation shows that this code constructs a filesystem path using user-controlled data. This is dangerous if the user input is not correctly sanitized or escaped because attackers could use the relative path traversal sequence `../` to point the path to an arbitrary location on the file system.

In this case, the path is used to read a file and return its contents. It is pretty clear that the code is not intended to allow users to read every file on the file system. The developers likely wanted to give users access to files in the upload folder only, so SonarQube Cloud's finding is, in fact, a vulnerability!

But where does the user input come from? We can see the flow of user-controlled data next to the code:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/633595a7-74dd-4b81-9b26-2c9d65455a82/erxes-sonarcloud-finding-1-flow.png)

If we click on the first entry, marked with the source label, we get to see where the user-controlled data originates from:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/04d4654e-191b-4b1d-b22f-f88e6846d82f/erxes-sonarcloud-finding-1-source.png)

As we can see, the request handler for the `/read-file` endpoint takes several query parameters. One of them, named `key`, is then passed into the `readFileRequest()` function without prior validation. The missing validation allows attackers to send a request such as `GET /read-file?key=../../../../some/secret/file` to leak secrets of the application. This vulnerability is now tracked as CVE-2024-57186.

Now that we have confirmed the vulnerability and know how attackers would exploit it, we have to determine the impact. The immediate impact is clear; attackers can read arbitrary files. But what does that mean in the context of the application? What information does the file system contain, and can leaking this information lead to a higher impact?

These questions led to a more thorough manual investigation from our vulnerability researchers. We discovered that attackers could take full control of an Erxes instance if it is set up using the official deployment guide.

## Technical details

To understand the full impact, we first have to understand how Erxes works on a high level. Their docs provide [a good starting point](https://docs.erxes.io/intro), including an architecture diagram. We simplified it to highlight the relevant parts:

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/605a981b-f6ef-41c1-b638-b1d5d8ebad02/erxes-architecture.png)

As we can see, Erxes consists of a central gateway and several microservices. There are also databases such as Redis that every service and the gateway can talk to, and services can speak to each other. Each part (gateway, services, databases) runs inside its own Docker container in production deployment.

We can now better gauge the overall impact of the vulnerability discovered by SonarQube Cloud. Since the issue is inside the core service and most interesting data is stored in other containers, there's not much an attacker could leak.

However, one promising file for attackers is `/proc/self/environ`. This special [procfs](https://man7.org/linux/man-pages/man5/proc.5.html) file contains all environment variables of the current process. More and more applications, especially those built for the cloud, are configurable using environment variables. In the case of Erxes, an attacker can find authentication secrets such as database credentials in there.

This is definitely a bad thing and needs to be fixed, but it does not allow attackers to increase the impact yet because they can't communicate with the databases from the outside. They first have to get access to one of the services, and for that, they need to get through the gateway. Can they do it?

### You can be whoever you want to be

The gateway not only dispatches requests to their respective services but also handles user authentication. It does so by reading a JSON Web Token (JWT) from the `auth-token` cookie or the `erxes-app-token` HTTP header, verifying its signature, and finally checking if that token exists in the Redis database:

Copy to clipboard
  
  
  export default async function userMiddleware(/* ... */) {
    // ...
    const token = req.cookies['auth-token'];
    // ...
    try {
      // verify user token and retrieve stored user information
      const { user } = jwt.verify(token, process.env.JWT_TOKEN_SECRET || '');
      const userDoc = await models.Users.findOne({ _id: user._id });
      if (!userDoc) {
        return next();
      }
      const validatedToken = await redis.get(`user_token_${user._id}_${token}`);
      // invalid token access.
      if (!validatedToken) {
        return next();
      }
      // ...
  }

The authenticated user is stored as `req.user` upon successfully validating the token. When forwarding the request to a service, the user object is taken from `req.user`, serialized to a Base64-encoded JSON string, and set as the `user` HTTP header on the request being forwarded:

Copy to clipboard
  
  
  export default async function userMiddleware(/* ... */) {
    // ...
    try {
      // ...
      // invalid token access.
      if (!validatedToken) {
        return next();
      }
      req.user = user;
      // ...
    }
    // ...
    generateBase64(req);
    return next();
  }
  
  const generateBase64 = req => {
    if (req.user) {
      const userJson = JSON.stringify(req.user);
      const userJsonBase64 = Buffer.from(userJson, 'utf8').toString('base64');
      req.headers.user = userJsonBase64;
    }
  };

When a service receives a request, it will trust the value stored in the `user` header and use it for further permission checks. The following code is present in all services and the service template:

Copy to clipboard
  
  
  if (req.headers.user) 
    if (Array.isArray(req.headers.user)) {
      throw new Error(`Multiple user headers`);
    }
    const userJson = Buffer.from(req.headers.user, 'base64').toString('utf-8');
    user = JSON.parse(userJson);
  }

The gateway only sets the header after successful authentication, so what is wrong here?

When an incoming request is not authenticated, it will neither have an `erxes-app-token` header nor an `auth-token` cookie. In this case, the gateway does not set the `user` header, but since it forwards the whole incoming request to the respective service, it will also forward an existing `user` header! This allows attackers to set the header to any user they want to impersonate, including admins.

This vulnerability, tracked as CVE-2024-57190, has a critical impact because it allows any user to become an admin on an Erxes instance just by sending a special header! An attacker could access all data stored in the application and even create their own admin account for persistent access.

But could an attacker go even further and execute arbitrary code on the underlying system? This would be much harder to detect later, and cleaning a compromised system would be much harder than just removing suspicious admin users.

### The weakest link

One particular file is mounted into every Erxes service: `/data/enabled-services.js`. It exports a list of enabled services:

Copy to clipboard
  
  
  module.exports = [
      'workers','logs','notifications','products','forms','tags'
  ]

Every service executes this file during startup when they use `require()` to load the enabled services:

Copy to clipboard
  
  
  function refreshEnabledServices() {
    // ...
    enabledServicesCache = require(ENABLED_SERVICES_PATH) || [];
    // ...
  }

This makes the file a juicy target for attackers. If they can overwrite it, they can cause a service to execute malicious code! Since the file is mounted from the host system into the service containers, it is not clear if the services have the right filesystem permissions to write to the file. However, we noticed that when setting up Erxes using the official Docker deployment guide, this file is writable by each service because both the user used on the host system and the user that a service is running under have the same UID (1000).

But how can an attacker write to that file?

### Yet another path traversal

While investigating the `workers` service, we noticed a code pattern that was very similar to that of the first vulnerability:

Copy to clipboard
  
  
  const importBulkStream = ({ fileName, /* ... */ }) => {
    // ...
    if (uploadType === 'AWS') {
        const { AWS_BUCKET } = await getFileUploadConfigs();
        const s3 = await createAWS();
        const params = { Bucket: AWS_BUCKET, Key: fileName };
        const file = (await s3.getObject(params).promise()) as any;
        await fs.promises.writeFile(
          `${uploadsFolderPath}/${fileName}`,
          file.Body
        );
        // ...
    }
    // ...
  }

This is the implementation of the `​​importHistoriesCreate` GraphQL mutation. It takes, among other things, a file name as input and then imports that file based on the currently configured upload type. If configured accordingly, Erxes uses S3 to store and retrieve files.

When calling the `​​importHistoriesCreate` GraphQL mutation while 'AWS' is configured, the `workers` service will first download the file to import from S3 to the local file system before processing it.__ As with the first vulnerability, the path is unsafely created using user-controlled data.

To exploit this vulnerability, tracked as CVE-2024-57189, an attacker would need to control the downloaded file's content. They could do this by uploading a malicious payload to the S3 service. Alternatively, they could change the configuration to point to an S3 server under their control.

As a result, calling the `importHistoriesCreate` GraphQL mutation with a path traversal payload causes the malicious file to be downloaded from S3 to the attacker-specified location.

As discussed earlier, the most promising target file for an attacker is `/data/enabled-services.js`. However, there's one final element of uncertainty: after overwriting the file, the attacker must wait for a service to restart for the compromised file to be executed. To circumvent this, attackers can use a final trick to ensure immediate execution, forcing the compromised file to be loaded without waiting for a service restart.

### Triggering a file reload

Each service uses Redis Pub/Sub to listen for messages in several channels. If a message arrives in the `refresh_enabled_services` channel, the service immediately reloads the enabled services file:

Copy to clipboard
  
  
  const REDIS_CHANNEL_REFRESH_ENABLED_SERVICES = 'refresh_enabled_services';
  
  (async () => {
    // ...
    const redisSubscriber = new Redis({
      host: REDIS_HOST,
      port: parseInt(REDIS_PORT || '6379', 10),
      password=***REDACTED***
    });
    await redisSubscriber.subscribe(REDIS_CHANNEL_REFRESH_ENABLED_SERVICES);
    await redisSubscriber.on('message', refreshEnabledServices);
  })();

So, to trigger the execution of the overwritten file, the attacker needs to publish a message to that specific channel.

As noted earlier, attackers cannot directly communicate with Redis. And even if they could, Redis would still require password authentication. The attacker can pass the authentication by using the initial file read vulnerability to extract the Redis password from the configuration file, but how can the attacker communicate directly with the database?

### Uploading commands to Redis

The attacker can misuse the previously mentioned S3 file storage functionality to establish communication with Redis. By setting the Erxes S3 configuration to point to the Redis host and port, the attacker can forge server-side requests (SSRF). With such a configuration in place, triggering an upload will send an HTTP request directly to Redis.

Redis does not speak HTTP, but its protocol (RESP) is also text-based. Redis will read the incoming HTTP request line-by-line, ignore lines that don't start with a valid Redis command, and execute lines that are valid commands.

It is important to note that Redis added protection against cross-protocol attacks and now closes the connection when it sees HTTP-related lines, such as a host header. However, because Redis runs in authenticated mode, protection was not enabled in the version used. Since version 7, Redis has also enabled protection in authenticated mode.

When triggering an Erxes file upload with the SSRF configuration in place, the file's content is sent as the HTTP request body. Therefore, an attacker can place arbitrary Redis commands in a file that will then be executed by the database when the file is uploaded.

To trigger the execution of the overwritten `enabled-services.js` file, the attacker crafts and uploads a file containing the following Redis commands:

  * `AUTH <password>` to authenticate the connection. The password is obtained earlier using the file read vulnerability.
  * `PUBLISH refresh_enabled_services foo` to trigger the reload.
  * `QUIT` to close the connection.

This sequence triggers a message to the designated Pub/Sub channel. Since all services subscribe to this channel, they receive the message, prompting a reload of the previously compromised `enabled-services.js` file.

### Putting it all together

We started with a simple file read vulnerability and ended with a remote code execution impact. To summarize, an attacker would have to take the following steps, also visualized in the graphic below:

  1. Leak the Redis password from `/proc/self/environ` using the file read vulnerability.
  2. Use the authentication bypass vulnerability to configure S3 file storage with an attacker-controlled host.
  3. Overwrite `/data/enabled-services.js` with a malicious payload using the file write vulnerability.
  4. Configure the S3 file storage to point to the Redis host and port using the authentication bypass vulnerability.
  5. Trigger the Redis SSRF by uploading a crafted file containing Redis commands, causing execution of the previously written payload.

![](https://assets-eu-01.kc-usercontent.com:443/ef593040-b591-0198-9506-ed88b30bc023/c1a2dd8a-5087-4332-8b1c-04242451329c/erxes-chain.png)

## Patches

To prevent the Authentication Bypass, Erxes now deletes the `user` header from all incoming HTTP requests, which is a valid fix. If you use a similar mechanism to pass important data between microservices, we recommend hardening your application by using an HMAC to sign that data. This would prevent authentication bypasses even in the presence of Server-Side Request Forgery (SSRF) vulnerabilities.

Erxes tackled the Path Traversal vulnerabilities by removing unwanted characters from user-controlled filenames. In this case, this correctly prevents the issue, but such a block-list approach comes with the risk of missing certain characters. A safer approach would be to use the user-controlled data to build the final path for the file operation, normalize the path, and then test if it is inside the allowed directory.

If you are using Erxes, make sure to update your instance to the latest version (1.6.3) to benefit from the security patches. 

## Timeline

**Date**| **Action**  
---|---  
2023-10-06| We report all issues to Erxes, including our 90-day disclosure deadline  
2023-10-27| We ping Erxes about an update  
2023-10-28| Erxes confirms the issues  
2024-01-26| We remind Erxes that the disclosure deadline has elapsed  
2024-02-22| Erxes releases version 1.6.1, fixing the Authentication Bypass vulnerability  
2024-03-04| We inform Erxes about the upcoming blog post  
2024-03-04| Erxes informs us that the reported issues have been addressed  
2024-03-04| We ask Erxes which versions contain the fixes  
2024-03-06| Erxes releases version 1.6.2, fixing the Path Traversal vulnerabilities  
2024-03-20| Erxes releases version 1.6.3, fixing the last vulnerability reported by us  
2024-03-21| This blog post is released  
  
## Summary

In this article, we saw firsthand how SonarQube Cloud empowers developers to catch real-world vulnerabilities. Integrating SonarQube Cloud into your CI/CD workflow creates a safety net, preventing these issues from ever reaching production environments and keeping your code clean.

We also learned about the pitfalls of microservices architectures, especially around authentication between services. If you're using the pattern yourself, make sure to secure communication between services to avoid microservice security vulnerabilities.

Finally, we would like to thank the Erxes team for addressing the vulnerabilities we reported.

## Related Blog Posts

  * [Excessive Expansion: Uncovering Critical Security Vulnerabilities in Jenkins](https://www.sonarsource.com/blog/excessive-expansion-uncovering-critical-security-vulnerabilities-in-jenkins/ "Excessive Expansion: Uncovering Critical Security Vulnerabilities in Jenkins")
  * [Security Vulnerabilities in CasaOS](https://www.sonarsource.com/blog/security-vulnerabilities-in-casaos/ "Security Vulnerabilities in CasaOS")
  * [Source Code at Risk: Critical Code Vulnerability in CI/CD Platform TeamCity](https://www.sonarsource.com/blog/teamcity-vulnerability/ "Source Code at Risk: Critical Code Vulnerability in CI/CD Platform TeamCity")
