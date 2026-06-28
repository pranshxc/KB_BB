---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-20_from-mlops-to-mloops-exposing-the-attack-surface-of-machine-learning-platforms.md
original_filename: 2024-08-20_from-mlops-to-mloops-exposing-the-attack-surface-of-machine-learning-platforms.md
title: 'From MLOps to MLOops: Exposing the Attack Surface of Machine Learning Platforms'
category: documents
detected_topics:
- supply-chain
- access-control
- command-injection
- sso
- xss
- automation-abuse
tags:
- imported
- documents
- supply-chain
- access-control
- command-injection
- sso
- xss
- automation-abuse
language: en
raw_sha256: 4d6f3e58a1827a3ad6ecb1ae0f43651f9fbc2006a66151dd62ec9c3e8cdd1009
text_sha256: e0ed3033888b676eba4d1b5f3cb7e1073eeca4b6d03447820e705efe763aa6b0
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# From MLOps to MLOops: Exposing the Attack Surface of Machine Learning Platforms

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-20_from-mlops-to-mloops-exposing-the-attack-surface-of-machine-learning-platforms.md
- Source Type: markdown
- Detected Topics: supply-chain, access-control, command-injection, sso, xss, automation-abuse
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `4d6f3e58a1827a3ad6ecb1ae0f43651f9fbc2006a66151dd62ec9c3e8cdd1009`
- Text SHA256: `e0ed3033888b676eba4d1b5f3cb7e1073eeca4b6d03447820e705efe763aa6b0`


## Content

---
title: "From MLOps to MLOops: Exposing the Attack Surface of Machine Learning Platforms"
page_title: "MLOps Platforms: The New High-Value Target & From MLOps to MLOops: Exposing the Attack Surface of Machine Learning Platforms"
url: "https://jfrog.com/blog/from-mlops-to-mloops-exposing-the-attack-surface-of-machine-learning-platforms/"
final_url: "https://jfrog.com/blog/from-mlops-to-mloops-exposing-the-attack-surface-of-machine-learning-platforms/"
authors: ["Ori Hollander", "Shachar Menashe", "Natan Nehorai", "Uriya Yavnieli"]
programs: ["Jupyter", "Hugging Face", "MLflow", "KServe", "Seldon"]
bugs: ["AI", "RCE", "XSS", "Missing authentication", "Container escape", "Malicious AI model", "Malicious datasets"]
publication_date: "2024-08-20"
added_date: "2024-08-26"
source: "pentester.land/writeups.json"
original_index: 57
---

# From MLOps to MLOops: Exposing the Attack Surface of Machine Learning Platforms

![Ori Hollander](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

![Shachar Menashe](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

![Natan Nehorai](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

![Uriya Yavnieli](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

By  [Ori Hollander,  JFrog Security Researcher](https://jfrog.com/blog-author/ori-hollander/) [Shachar Menashe,  JFrog VP Security Research](https://jfrog.com/blog-author/shachar-menashe/) [Natan Nehorai,  JFrog Application Security Researcher](https://jfrog.com/blog-author/natan-nehorai/) [Uriya Yavnieli,  JFrog Security Researcher](https://jfrog.com/blog-author/uriya-yavnieli/) August 20, 2024

__ 26 min read

SHARE:

[ __](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fjfrog.com%2Fblog%2Ffrom-mlops-to-mloops-exposing-the-attack-surface-of-machine-learning-platforms%2F)

[ __](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fjfrog.com%2Fblog%2Ffrom-mlops-to-mloops-exposing-the-attack-surface-of-machine-learning-platforms%2F&title=From+MLOps+to+MLOops%3A+Exposing+the+Attack+Surface+of+Machine+Learning+Platforms)

[ ](https://twitter.com/intent/tweet?text=From+MLOps+to+MLOops%3A+Exposing+the+Attack+Surface+of+Machine+Learning+Platforms%0ahttps%3A%2F%2Fjfrog.com%2Fblog%2Ffrom-mlops-to-mloops-exposing-the-attack-surface-of-machine-learning-platforms%2F&via=jfrog)

![From MLOps to MLOops: Exposing the Attack Surface of Machine Learning Platforms](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20863%20300'%3E%3C/svg%3E)

**NOTE** : This research was recently presented at Black Hat USA 2024, under the title [“ _From MLOps to MLOops – Exposing the Attack Surface of Machine Learning Platforms_ ”](https://www.blackhat.com/us-24/briefings/schedule/index.html#from-mlops-to-mloops---exposing-the-attack-surface-of-machine-learning-platforms-39309).

The JFrog Security Research team recently dedicated its efforts to exploring the various attacks that could be mounted on **open source machine learning (MLOps) platforms used inside organizational networks**.

Our research culminated in more than 20 disclosed CVEs to various ML vendors, and a deeper understanding of how real-world attacks can be launched against deployed MLOps platforms.

In this blog post, we will tackle –

  * Core features of MLOps platforms
  * How each MLOps feature can be attacked
  * Best practices for deploying MLOps platforms

  
**What’s included in this post:**

  * What can MLOps do for you
  * Inherent vs. Implementation Vulnerabilities
  * Inherent Vulnerabilities in MLOps Platforms
  * Malicious ML Models
  * Malicious Datasets
  * Jupyter Sandbox Escape
  * Implementation Vulnerabilities in MLOps Platforms
  * Lack of Authentication
  * Container Escape
  * Immaturity of MLOps platforms
  * How would an attacker chain these vulnerabilities together?
  * Mapping MLOps features to possible attacks
  * Mitigating some of the attack surface
  * Takeaways for deploying MLOps platforms in your organization

## What can MLOps do for you

Before we list the various MLOps platform attacks, let’s familiarize ourselves with some basic MLOps concepts.

![Figure 1. The ML Software Supply Chain](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20863%20300'%3E%3C/svg%3E)_Figure 1. The ML Software Supply Chain_

The common lifecycle of building and deploying a machine learning model involves –

  1. Choosing a machine learning algorithm (ex. SVM or Decision Tree)
  2. Feeding a dataset to the algorithm (“Training” the model) 
  * This produces a “pretrained” model which can be queried
  3. Optionally – Deploying the pretrained model to a model registry
  4. Deploying the pretrained model to production, either by – 
  * Embedding it in an application
  * Deploying it to an Inference server (“Model Serving” or “Model as a Service”)

Let’s take a deeper look into each of these steps.

### MLOps Pipeline

![Figure 2. Steps of a common MLOps Pipeline](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20863%20300'%3E%3C/svg%3E)_Figure 2. Steps of a common MLOps Pipeline_

As mentioned, MLOps platforms provide the ability to construct and run an ML model pipeline. The idea is to automate the various stages of model development and deployment.

An MLOps pipeline is similar to a traditional DevOps pipeline.

For example, in a DevOps pipeline we might perform a nightly build based on source code changes, but in an MLOps pipeline we might perform a nightly model training based on dataset changes.

ML Pipelines are usually defined through Python code, the pipeline code monitors for changes in either the dataset or model parameters, and then trains a new model, evaluates it and if it passes the evaluation – deploys it to production.

For example – we can see abbreviated Python code from the popular [Kubeflow](https://www.kubeflow.org/) platform that defines an MLOps pipeline which analyzes, transforms, trains and evaluates a machine learning model, based on datasets stored in (Google) cloud storage that can be constantly updated

![Figure 3. Abbreviated ML Pipeline code \(Kubeflow framework\)](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20645%20428'%3E%3C/svg%3E)_Figure 3. Abbreviated ML Pipeline code (Kubeflow platform)_

![Figure 4. Graph representation of an MLOps Pipeline \(Kubeflow framework\)](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20690%20937'%3E%3C/svg%3E)_Figure 4. Graph representation of an MLOps Pipeline (Kubeflow platform)_

### Model Registry

After training a model, either manually or by running an ML pipeline, the most robust way for tracking the pre-trained models is by using a **Model Registry**.

![Figure 5. Uploading and downloading models from a Model Registry](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20863%20448'%3E%3C/svg%3E)_Figure 5. Uploading and downloading models from a Model Registry_

The Model registry acts as a version control mechanism for ML models. It is the single source of truth for an organization’s ML models and allows for easy fetching of specific model versions, aliasing, tagging and more.

Data scientists use training data to create the models, and then collaborate and iterate on different models and different versions of the models.

ML engineers can then promote some of these models to production machines where the models will be served to clients that will be able to query them.

A good example of an ML Model registry is [MLFlow](https://mlflow.org/), one of the most popular MLOps platforms today –

![Figure 6. The MLFlow model registry](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201117%20445'%3E%3C/svg%3E)_Figure 6. The MLFlow model registry_

### Model Serving

When we want to promote a model to be used in production, we have two choices, either we embed the model in an application or we allow users to query the model through an API, the latter is called “Model Serving” or “Model as a Service” –

![Figure 7. Production ML Model Embedding vs. Serving](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20863%20448'%3E%3C/svg%3E)_Figure 7. Production ML Model Embedding vs. Serving_

Several MLOps platforms support model serving for various ML model formats.

This saves us the need of wrapping the model in some web application (ex. A Python Flask app) as it is difficult to manage, not very scalable, not agile (we usually can’t switch our model type without re-engineering our backend) and requires us to invent custom APIs for this purpose.

Instead of writing a custom web application to serve our model, the more robust solution is to use an MLOps platform that supports “Model Serving”. For example, [Seldon Core](https://github.com/SeldonIO/seldon-core), implements Model Serving by converting the model into a Docker image and then deploying it through Kubernetes and wrapping it with a standard API layer –

![Figure 8. Seldon Core model serving architecture](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20863%20448'%3E%3C/svg%3E)_Figure 8. Seldon Core model serving architecture_

It’s extremely easy to serve multiple model types, without writing custom code, and consuming the models is also easy using the same API everywhere regardless of the underlying ML model type that is served. The only thing an ML engineer needs to do is apply a relevant Kubernetes configuration and the model is served instantly –

![Figure 9. Kubernetes configuration for serving a model with Seldon Core](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20353'%3E%3C/svg%3E)_Figure 9. Kubernetes configuration for serving a model with Seldon Core_

## Inherent vs. Implementation Vulnerabilities

_Back to top >_

Now that we understand the basic functionalities of an MLOps platform, let’s see how attackers can abuse these functionalities to infiltrate and spread inside an organization.

In our research, we chose to analyze six of the most popular open source MLOps platforms, and see which attacks can be implemented against them when deployed in an organization.

![Figure 10. Our research targets - six of the most popular open-source MLOps platforms](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20863%20448'%3E%3C/svg%3E)_Figure 10. Our research targets – six of the most popular open-source MLOps platforms_

In our research, we ended up distinguishing between two types of vulnerabilities in MLOps platforms, **inherent vulnerabilities and implementation vulnerabilities**.

Inherent vulnerabilities are vulnerabilities that are caused by the underlying formats and processes used in the target technology (in our case – MLOps platforms).

To draw an analogy – Let’s see an inherent vulnerability in Python.

Let’s imagine a PyPI package provides the following **unjson_and_unpickle** function –
  
  
  def unjson_and_unpickle(json_data: str):
  pickle_bytes = json.loads(json_data)["pickle_data"]
  return pickle.loads(pickle_bytes)

As you might know, passing untrusted data to **pickle.loads** can result in **arbitrary code execution**. Therefore, would the existence of this function merit a vulnerability report (CVE) on our PyPI library? The general consensus to this answer is No, since –

  * The [pickle module](https://docs.python.org/3/library/pickle.html) is well-known and documented to be insecure when passing untrusted data.  
![Figure 11. Python docs about the unsafe nature of Unpickling](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20669%20196'%3E%3C/svg%3E)  
_Figure 11. Python docs about the unsafe nature of Unpickling_
  * Our potentially vulnerable function has a descriptive name (“unpickle” as part of the function name) and hopefully our library also documents this function as unsafe with untrusted inputs.
  * In most cases, there is no way to “fix” this function without hurting the library’s functionality

Therefore, the users of this library must be aware of the dangers of using the Pickle format, there is no “vulnerability” that should be fixed in this library.

This is all fine and well since developers already have a lot of experience with Python and Pickle, but the problem is that machine learning is a new field.

Since ML is a new field, this raises the question – **which of these “inherent” vulnerabilities are out there which we might not know about?** Which ML actions should not be used with untrusted data?

Inherent vulnerabilities are scarier since there are no patches or CVEs against them, **either you know about them or you don’t**.

## Inherent Vulnerabilities in MLOps Platforms

_Back to top> _

Now that we know about inherent vulnerabilities, let’s enumerate the inherent vulnerabilities in MLOps platforms that we were able to exploit in our research.

### Malicious ML Models

**Models are code!** This is probably the most well-known inherent vulnerability in machine learning, but it’s also the most dangerous one. It can lead to code execution even when ML users are aware of the dangers of loading untrusted ML models.

Unfortunately, most ML model formats that are in use today support automatic code execution on load, **this means that just by loading an untrusted model, arbitrary code runs on your machine**. Contrary to popular belief, this feature is not limited only to Pickle-based models.

![Figure 12. Model formats that support code-execution-on-load \(top row\) and some that don’t \(bottom row\)](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20863%20305'%3E%3C/svg%3E)_Figure 12. Model formats that support code-execution-on-load (top row) and some that don’t (bottom row)_

Exact details on how the code is executed depend on the model format, but in general, the code is just embedded into the model binary, and rigged to execute when the model is loaded.

This can be illustrated by examining a Keras H5 model which we rigged to open a Calculator.

![Figure 13. Examining a Keras H5 model with an embedded Python code object](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201001%20662'%3E%3C/svg%3E)_Figure 13. Examining a Keras H5 model with an embedded Python code object_

![Figure 14. Decompilation of the “Decoded bytes” Python code object](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20363%20155'%3E%3C/svg%3E)_Figure 14. Decompilation of the “Decoded bytes” Python code object_

The problem is that the user just wanted to load a model, and got arbitrary code execution instead.

![Figure 15. Simply loading the model leads to code execution](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20613%20189'%3E%3C/svg%3E)_Figure 15. Simply loading the model leads to code execution_

To further illustrate how accessible and dangerous this inherent vulnerability is, JFrog’s research team has already seen [data scientists targeted by these malicious models on the popular Hugging Face ML Model repository](https://jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face-ml-models-with-silent-backdoor/).

### Malicious Datasets

Similar to models having auto-executed code embedded in them, some datasets formats and libraries also allow for automatic code execution. Luckily, these possibly-vulnerable dataset libraries are very rare compared to their model counterparts.

One prominent example of code execution when loading untrusted datasets is when using the [Hugging Face Datasets](https://github.com/huggingface/datasets) library.

Using this library, it is extremely easy to download and load a dataset, directly from the Hugging Face repository. For example, with just two lines we can load the [hails/mmlu_no_train](https://huggingface.co/datasets/hails/mmlu_no_train/tree/main) dataset (to clarify – this specific dataset is NOT malicious).

![Figure 16. Python code that downloads and loads a dataset from Hugging Face](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20463%2066'%3E%3C/svg%3E)_Figure 16. Python code that downloads and loads a dataset from Hugging Face_

However, when browsing this dataset we can see that except for the actual data (_data.tar file_) the repository also contains a Python script called _mmlu_no_train.py_.

It is not a coincidence that this Python file has the exact same name as the repository.

When calling [load_dataset](https://huggingface.co/docs/datasets/v2.19.0/en/package_reference/loading_methods#datasets.load_dataset) **by default** , the library will run a Python script from the remote repository.

![Figure 17. Prototype for “load_dataset”](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20468%20316'%3E%3C/svg%3E)_Figure 17. Prototype for “load_dataset”_

![Figure 18. “trust_remote_code” default argument](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20146'%3E%3C/svg%3E)_Figure 18. “trust_remote_code” default argument_

An ML or data engineer can easily not know about this functionality, and get hit with arbitrary code execution when loading an untrusted dataset.

This is one example of a platform/library that allows for arbitrary code execution when loading untrusted datasets. Although in our research we did not encounter any other library that allowed the same functionality, it is easy to imagine that some ML libraries may support dataset serialization formats (ex. Pickle) that will lead to arbitrary code execution when loaded. Therefore – it is imperative to read the documentation before using functions that perform dataset loading.

### Jupyter Sandbox Escape

One of the most popular tools in use by data scientists today is [JupyterLab](https://jupyter.org/) (or its older interface – Jupyter Notebook). JupyterLab is a web application that allows writing individual code blocks with documentation blocks, and then running each block separately and seeing their output.

![Figure 19. The JupyterLab interface, mixing code, output and documentation blocks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201291%20838'%3E%3C/svg%3E)_Figure 19. The JupyterLab interface, mixing code, output and documentation blocks_

This interface is amazing for model testing and visualization in a highly interactive environment.

An inherent issue that many do not know about, is the handling of HTML output when running code blocks in Jupyter. Namely – **The output of your Python code may emit HTML and JS which will be happily rendered by your browser**. This at first may not seem like a big deal since arbitrary JS code running in the browser by itself has a very limited security impact. However – the real issue here is that in Jupyter –

  1. The emitted JavaScript **is not sandboxed** in any way from the Jupyter “parent” web application
  2. The Jupyter parent web application can run **arbitrary Python code “as a feature”**

For example, here is a JavaScript payload that when run in Jupyter will –

  * Add a new “Code” cell
  * Fill the cell with Python code
  * Run the cell

![Figure 20. JS sandbox-escape payload - before execution](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201326%20843'%3E%3C/svg%3E)_Figure 20. JS sandbox-escape payload – before execution_

![Figure 21. JS sandbox-escape payload - after execution \(note the new code cell\)](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201062%20782'%3E%3C/svg%3E)_Figure 21. JS sandbox-escape payload – after execution (note the new code cell)_

This, at first, does not seem like a big issue. We should not execute untrusted JS code in Jupyter anyways, so it doesn’t matter if JS code leads to full remote code execution.

But is it possible that a browser will run JavaScript code unexpectedly? When performing seemingly safe operations? This is of course true **when exploiting an XSS vulnerability**.

For example, as part of our research we discovered and disclosed [CVE-2024-27132](https://research.jfrog.com/vulnerabilities/mlflow-untrusted-recipe-xss-jfsa-2024-000631930/) in the MLFlow client library. This CVE leads to XSS when executing an MLFlow recipe –

![Figure 22. CVE-2024-27132 XSS vulnerability](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20650%20127'%3E%3C/svg%3E)_Figure 22. CVE-2024-27132 XSS vulnerability_

An MLFlow recipe is just a YAML file, this is inherently a safe format and should not lead to any vulnerabilities even when loading an untrusted recipe.

However, we discovered that due to lack of output filtration, running an untrusted recipe will lead to arbitrary HTTP being emitted, including JS.

Many attack vectors are possible, for example when fetching a recipe from an untrusted source, or even fetching a trusted recipe but through an insecure network (man-in-the-middle attack in the local network)

![Figure 23. Attackers serving a malicious MLFlow recipe with XSS payload](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20520%20397'%3E%3C/svg%3E)_Figure 23. Attackers serving a malicious MLFlow recipe with XSS payload_

Exploitation of the CVE in Jupyter looks like this – just by running the recipe, we get arbitrary JS code execution –

![Figure 24. XSS when loading a malicious MLFlow recipe](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20510%20230'%3E%3C/svg%3E)_Figure 24. XSS when loading a malicious MLFlow recipe_

As we’ve seen, XSS in Jupyter is equivalent to full code execution on whichever machine hosts the Jupyter server.

Therefore, one of our main takeaways from this research is that **we need to treat all XSS vulnerabilities in ML libraries as potential arbitrary code execution** , since data scientists may use these ML libraries with Jupyter Notebook.

## Implementation Vulnerabilities in MLOps Platforms

_Back to top >_

While inherent vulnerabilities are the scariest due to their more hidden nature, in our research we also found and disclosed multiple implementation issues in various MLOps platforms. These are “classic” vulnerabilities that are more likely to plague MLOps platforms or cause a heightened severity on MLOps platforms. Also, unlike inherent vulnerabilities, the implementation issues should get a CVE and patch when discovered. These are the categories of implementation issues we’ve encountered.

### Lack of Authentication

As we’ve seen, a lot of MLOps platforms support the “ML Pipeline” feature, which means a user with enough privileges can just run arbitrary code on the MLOps platform, by creating a new pipeline. Some of these platforms require that the pipelines run inside a container, but some do not. With **“Remote Code Execution” as a feature** , we were hoping the MLOps platforms would have strong authentication and roles built-in.

Unfortunately, our research highlights that many platforms that support pipelines either don’t support authentication at all or require the user to deploy an external resource for authentication, which leaves simple deployments completely exposed.

For example, our research shows that in the cases of Seldon Core, MLRun and Metaflow, any user with network access to the platform can just run arbitrary code on the platform by abusing the ML Pipeline feature, in the platform’s default configuration!

Users are expected to either –

  * Run the MLOps platform in a completely trusted network
  * Add custom authentication/authorization mechanisms (ex. reverse proxy with authentication) which aren’t built-in to the MLOps platforms

These two requests are not very likely to happen, since many users simply deploy an MLOps platform to their local network, and expect the platform to have built-in authentication or access control.

![Figure 25. MLOps platforms that support ML Pipelines without an auth mechanism](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20863%20426'%3E%3C/svg%3E)_Figure 25. MLOps platforms that support ML Pipelines without an auth mechanism_

Some of these issues get a CVE due to lack of authentication, but most of them don’t.

An example that DID get a CVE is the Ray platform, which also allowed to submit arbitrary pipeline jobs but didn’t include an auth mechanism

_![Figure 26. RCE CVE for the Ray server by abusing ML Pipelines](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20714%20252'%3E%3C/svg%3E)Figure 26. RCE CVE for the Ray server by abusing ML Pipelines_

The above CVE in the Ray platform is highly exploitable, but was disputed by the Ray maintainers since the Ray documentation states **“Ray, …, is not intended for use outside of a strictly controlled network environment”**. This is an unreasonable requirement for a daemon, that only a very small number of deployers can actually enforce.

This point is not theoretical, since a [great research by Oligo’s security team](https://www.oligo.security/blog/shadowray-attack-ai-workloads-actively-exploited-in-the-wild) revealed that this vulnerability was already **exploited in the wild on thousands of servers**! This is not surprising since these servers were –

  * Exposed to WAN
  * Without any authentication mechanism
  * Supported RCE as a feature (ML Pipelines)

### Container Escape

Another vulnerability type that has increased effectiveness against MLOps platforms is a container escape.

The more robust MLOps platforms use Docker containers for security and convenience in two scenarios –

  1. **ML Pipelines** – The pipeline code is run inside a container. In this scenario attacker code execution is obvious so editing pipeline code should require high privileges (although we just saw that authentication in several platforms is severely lacking)
  2. **Model serving** – The served model is loaded inside a container. Here, attacker code execution is a side-effect, since some model types just support automatic code execution on load. Regular users are more likely to have permissions to upload an arbitrary model to be served.

![Figure 27. MLOps platforms using Docker containers in Model Training and Model Serving](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20863%20418'%3E%3C/svg%3E)_Figure 27. MLOps platforms using Docker containers in Model Training and Model Serving_

In both of these scenarios, attackers can already execute code.

**Breaking the container will allow the attacker to move laterally and expose the attacker to more MLOps resources** (other user models, datasets etc.).

Let’s see how an attacker can perform a container escape in the Model serving scenario, since in general this endpoint will be more exposed to attackers.

#### KServe

In our research, we’ve looked at two platforms that performed Model serving, KServe and Seldon-core.

In both of them, it’s easy to get code execution inside the Docker container that serves the model, by uploading a malicious model that executes code on load.

In KServe, we observed that the environment that loads the model is very well isolated from the rest of the platform.

For example, the uploaded malicious model in Pod 1 doesn’t have access to a different model that runs in Pod 2.

With just code execution, we couldn’t achieve lateral movement or get access to sensitive resources such as other models or datasets.

![Figure 28. KServe model serving architecture \(well-isolated\)](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20863%20430'%3E%3C/svg%3E)_Figure 28. KServe model serving architecture (well-isolated)_

However – we should remember that many container escape 1-days exist (for example, every Linux kernel local privilege escalation is also a container escape)

By utilizing such a privilege escalation (for example [CVE-2022-0185](https://nvd.nist.gov/vuln/detail/CVE-2022-0185)) as part of the malicious model payload, the attacker can achieve lateral movement in the organization.

#### Seldon Core

In Seldon-core the situation was a bit different. We observed that the model’s execution environment is also containerized, but unfortunately all the models are inside the SAME container.

This enables the following attack scenarios –

  * The attacker uploads a malicious model to the Seldon inference server.
  * The malicious model triggers code execution inside the Docker container and hijacks it.
  * Since the poisoned model and other models all live in the same container, multiple attacks are possible – 
  * **Poisoning** – The hijacked container poisons some of the models stored in the server. This will cause the inference server to return attacker-controlled data to any user that queries the server. **For example – a user that queries the poisoned inference server** for “What’s the best PyPI package for computer vision” could get back a malicious result such as “ _Try MyRemoteAccessTool v99.9_ ”.
  * **IP Leakage** – The hijacked container uploads sensitive models to an attacker’s server on the cloud, leading to intellectual property loss.

![Figure 29. Poisoning adjacent ML models](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20863%20375'%3E%3C/svg%3E)_Figure 29. Poisoning adjacent ML models_

![Figure 30. Exfiltrating adjacent ML models](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20863%20375'%3E%3C/svg%3E)_Figure 30. Exfiltrating adjacent ML models_

### Immaturity of MLOps platforms

The last point regarding implementation vulnerabilities that we observed in our research is **that we can expect a high number of security issues in MLOps platforms in the upcoming years**.

This is due to two reasons –

  1. Open source MLOps platforms are all quite new (the oldest ones are about 5 years old)
  2. AI experts are usually NOT security experts

This hypothesis can be easily verified by looking at recent CVE data –

![Figure 31. Number for CVEs from the past two years, MLFlow vs Jenkins](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20863%20393'%3E%3C/svg%3E)_Figure 31. Number for CVEs from the past two years, MLFlow vs Jenkins_

If we look at MLFlow for example, it has a staggering amount of CVEs reported –

38 Critical and high CVEs is a huge amount for 2 years, and the criticals are especially concerning since they involve things like [unauthenticated remote code execution](https://nvd.nist.gov/vuln/detail/CVE-2023-1177).

If we compare this to a mature project in a similar category, like the Jenkins DevOps server, it has a much lower number of vulnerabilities.

## How would an attacker chain these vulnerabilities together?

_Back to top >_

Now that we have all the pieces of the puzzle, let’s see how attackers might take advantage of these vulnerabilities in the real world

### Client-side malicious models

In this first attack chain let’s see how an attacker can use client-side malicious models to infiltrate and spread inside an organization.

This scenario is relevant to model registries such as MLFlow, W&B and ZenML.

![Figure 32. Using malicious client-side models to infiltrate and move within an organization](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20863%20447'%3E%3C/svg%3E)_Figure 32. Using malicious client-side models to infiltrate and move within an organization_

  1. First, the attacker wants to infiltrate the organization, this can be facilitated by uploading a malicious model to a public repository such as Hugging Face.  
Similar to attacks on npm and PyPI, anyone can upload a malicious model, the model just needs to look enticing enough for people to download it.
  2. Once an organizational user, for example a data scientist, consumes the malicious model – the attacker has code execution inside the organization.  
Downloading and loading a model from Hugging Face is just 3 lines of code. Convenient but dangerous!  
![Figure 33. Code for downloading & loading a remote model from Hugging Face](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20100'%3E%3C/svg%3E)  
_Figure 33. Code for downloading & loading a remote model from Hugging Face_
  3. The attacker uses the foothold to hijack the organization’s model registry, as we saw this can be done via – 
  * Lack of authentication.
  * Stored credentials, for example it makes sense that a data scientist will have credentials to the model registry.  
![Credentials to the model registry](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20528%2079'%3E%3C/svg%3E)
  * Exploiting a CVE/0-day software vulnerability.
  4. After the model registry is hijacked, the attacker infects all existing models with backdoor code. This means that if anyone loads these models, they will get infected as well.
  5. As part of the regular organization workflow, both servers and users request the latest model version from the model registry.  
For example in the MLFlow registry, this can be done with 4 lines of code.  
![Figure 34. Code for downloading & loading a remote model from MLFlow](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20773%20117'%3E%3C/svg%3E)  
_Figure 34. Code for downloading & loading a remote model from MLFlow_
  6. At this point, all the relevant services and users are infected as well, and this worm can keep propagating throughout the organization.

### Server-side malicious models

Alternatively, malicious models can be used to infect **servers** and not just clients.

This scenario is relevant to MLOps platforms that provide Model Serving or Model as a service, such as Seldon and KServe –

![Figure 35. Using malicious server-side models to infiltrate and move within an organization](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20863%20481'%3E%3C/svg%3E)_Figure 35. Using malicious server-side models to infiltrate and move within an organization_

  1. The attacker is already inside the organization, or even on the cloud.
  2. The attacker uploads a new model to the inference server. This almost always requires less privileges than editing existing models.
  3. The model runs a malicious payload once loaded inside the serving container and hijacks the container.
  4. The payload then utilizes a container escape. 
  1. Either exploiting a well-known CVE,
  2. Or an escape technique tailored to the specific MLOps platform (like the one shown above on Seldon core).
  5. The attacker has control of the entire inference server. From here, the attacker can continue spreading through the organization using other techniques.

## Mapping MLOps features to possible attacks

_Back to top >_

![Figure 36. Map of MLOps features to pre- and post-exploitation techniques](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20863%20481'%3E%3C/svg%3E)_Figure 36. Map of MLOps features to pre- and post-exploitation techniques_

Summarizing all the above, we can see which MLOps features are vulnerable to which attacks, and the platforms that we currently identify as vulnerable.

For example, if you’re deploying a platform that allows for Model Serving, you should now know that anybody that can serve a new model can also actually run arbitrary code on that server. Make sure that the environment that runs the model is completely isolated and hardened against a container escape.

## Mitigating some of the attack surface

_Back to top >_

### Mitigate XSS attacks on JupyterLab with XSSGuard

The JFrog Security Research team released an open source extension for JupyterLab called “[XSSGuard](https://github.com/jfrog/jupyterlab-xssguard)” that mitigates XSS attacks, by sandboxing Jupyter’s output elements that are susceptible to XSS.

For example, this plugin can mitigate the impact of the vulnerabilities we previously disclosed in MLflow (CVE-2024-27132 & CVE-2024-27133) –

![Figure 37. XSSGuard denying DOM access from malicious JS code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20920%20388'%3E%3C/svg%3E)_Figure 37. XSSGuard denying DOM access from malicious JS code_

Install it from the JupyterLab Extension Manager by searching “XSSGuard” –

![Figure 38. Installing XSSGuard with JupyterLab’s Extension Manager](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20918%20788'%3E%3C/svg%3E)_Figure 38. Installing XSSGuard with JupyterLab’s Extension Manager_

### Upgrade your Hugging Face Datasets library

Since starting our MLOps research, the Hugging Face maintainers realized that automatic code execution on dataset loading is a major issue, and released a new version of their datasets library about two months ago.

In this new library version, an explicit flag is required to allow code execution when loading a dataset!

![Figure 39. HF datasets 2.20.0 disables automatic code execution by default](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20816%20261'%3E%3C/svg%3E)_Figure 39. HF datasets 2.20.0 disables automatic code execution by default_

We recommend all Hugging Face dataset users to upgrade to this latest version of the datasets library ([2.20.0](https://github.com/huggingface/datasets/releases/tag/2.20.0)).

## Takeaways for deploying MLOps platforms in your organization

_Back to top >_

Summarizing our recent research on MLOps platforms, these are our main takeaways –

  1. Check if your MLOps platform supports **ML Pipelines, Model serving or a Model registry**. If you don’t need these features, disable them completely. 
  1. If you do need them, make sure they run inside separate Docker containers.
  2. Make sure authentication is available and enabled!
  2. Models are code! 
  1. Anyone that can upload a model to an inference server is basically running code on that server.
  2. Set an organizational policy to work only with models that don’t support code execution on load (for example [Safetensors](https://huggingface.co/docs/safetensors/en/index)).
  3. Brief anybody that loads ML models about the dangers of untrusted models and datasets.
  4. If working with unsafe models, scan all the models in your organization either periodically or even before allowing them in your organization, for example using [picklescan](https://github.com/mmaitre314/picklescan).
  3. Using Jupyter? Install our open-source [XSSGuard extension](https://github.com/jfrog/jupyterlab-xssguard).

## Keep your ML Models safe with JFrog

_Back to top >_

Ensure integrity and security of ML Models using the JFrog Platform, by leveraging important controls including RBAC, versioning, licensing and security scanning. This brings together ML developers, operations and security by producing secure releases including scanning of ML Models for malicious code. JFrog’s scalability allows for managing very large models and datasets that can be handled by other solutions.

![Figure 40. Detecting malicious ML models with JFrog Xray](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201829%20865'%3E%3C/svg%3E)_Figure 40. Detecting malicious ML models with JFrog Xray_

The platform serves as a single source of truth for each AI/ML release that includes a list of all associated artifacts, third party licensing information and proof of compliance for industry standards and emerging government regulations. From a user perspective, the solution is transparent to developers, while allowing DevOps to manage and secure ML Models alongside other binaries and seamlessly bundle them and distribute them as part of any software release.

Check out the benefits of JFrog for MLOps by [scheduling a demo](https://jfrog.com/artifactory/schedule-a-demo/) at your convenience.

## Stay up-to-date with JFrog Security Research

The security research team’s findings and research play an important role in improving the JFrog Software Supply Chain Platform’s application software security capabilities.

Follow the latest discoveries and technical updates from the JFrog Security Research team on our [research website](https://research.jfrog.com/), and on X [@JFrogSecurity](https://twitter.com/JFrogSecurity).

Tags: [ MLOps ](/blog/tag/mlops/) [ machine learning ](/blog/tag/machine-learning/) [ security-research ](/blog/tag/security-research/)

[ Start a Trial ](https://jfrog.com/start-free/)

SHARE:

[ __](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fjfrog.com%2Fblog%2Ffrom-mlops-to-mloops-exposing-the-attack-surface-of-machine-learning-platforms%2F)

[ __](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fjfrog.com%2Fblog%2Ffrom-mlops-to-mloops-exposing-the-attack-surface-of-machine-learning-platforms%2F&title=From+MLOps+to+MLOops%3A+Exposing+the+Attack+Surface+of+Machine+Learning+Platforms)

[ ](https://twitter.com/intent/tweet?text=From+MLOps+to+MLOops%3A+Exposing+the+Attack+Surface+of+Machine+Learning+Platforms%0ahttps%3A%2F%2Fjfrog.com%2Fblog%2Ffrom-mlops-to-mloops-exposing-the-attack-surface-of-machine-learning-platforms%2F&via=jfrog)
