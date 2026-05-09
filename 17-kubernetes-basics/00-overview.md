# Kubernetes Overview

## 1. What Kubernetes Is

Kubernetes is a platform for managing containerized applications.

Simple meaning:

```text
Kubernetes runs containers, keeps them alive, scales them, and exposes them through services.
```

Core mental model:

```text
YAML file -> Kubernetes object -> pod runs container -> service exposes it
```

## 2. Why Kubernetes Exists After Docker

Docker packages and runs containers.

Kubernetes manages containers when you need a system around them.

Example:

```text
Docker can run one FastAPI container locally.
Kubernetes can keep FastAPI pods running, recreate them if they fail, scale them, and expose them through a Service.
```

Kubernetes does not replace Docker knowledge. It builds on the container image idea.

## 3. Cluster

A cluster is the full Kubernetes environment.

Simple meaning:

```text
Cluster = the place where Kubernetes runs your applications
```

A cluster contains nodes. In local learning, minikube creates a small cluster on your machine. In enterprise, a cluster may run across many machines in cloud or data centers.

## 4. Node

A node is a machine inside the cluster.

Simple meaning:

```text
Node = worker machine where pods can run
```

In minikube, there may be one node. In a real cluster, there may be many nodes.

## 5. Pod

A pod is the smallest runnable unit in Kubernetes.

Simple meaning:

```text
Pod = Kubernetes wrapper around one or more containers
```

Most beginner examples use one container per pod.

Important:

You usually do not manually create individual pods for long-running apps. You create a Deployment, and the Deployment manages pods for you.

## 6. Deployment

A Deployment tells Kubernetes how to run and maintain pods.

Simple meaning:

```text
Deployment = desired state for app pods
```

It can define:

- image name
- number of replicas
- pod labels
- container port
- rollout behavior

Example:

```yaml
kind: Deployment
spec:
  replicas: 1
```

Meaning:

```text
Keep one copy of this app running.
```

## 7. Service

A Service gives stable network access to pods.

Pods can be deleted and recreated. Their IP addresses can change. A Service provides a stable way to reach matching pods.

Simple meaning:

```text
Deployment runs pods.
Service exposes pods.
```

In this module, the sample uses `NodePort` for local/minikube-style access.

## 8. Namespace

A namespace is a grouping boundary inside a Kubernetes cluster.

Simple meaning:

```text
Namespace = named area inside a cluster
```

Teams use namespaces to separate environments or applications, such as:

- `dev`
- `qa`
- `poc`
- `default`

Beginner note:

If you do not specify a namespace, many commands use the `default` namespace.

## 9. ConfigMap

A ConfigMap stores non-sensitive configuration.

Examples:

- `APP_ENV=local`
- `LOG_LEVEL=debug`
- `MODEL_NAME=mock-llm`

Simple meaning:

```text
ConfigMap = normal config outside the container image
```

Use ConfigMap when the value is not secret.

## 10. Secret

A Secret stores sensitive configuration.

Examples:

- API keys
- passwords
- tokens

Simple meaning:

```text
Secret = sensitive config object
```

Important beginner caution:

Kubernetes Secrets are better than plain ConfigMaps for sensitive values, but they still require proper access control. Do not commit real secrets to Git.

## 11. minikube

minikube is a local Kubernetes environment for learning and testing.

Simple meaning:

```text
minikube = local small Kubernetes cluster on your machine
```

Use it when you want to practice Kubernetes without a cloud cluster.

Command:

```powershell
minikube start
```

Where to run:

Run from any folder after minikube is installed.

What each part means:

- `minikube` runs the minikube CLI
- `start` creates or starts the local Kubernetes cluster

Expected output:

```text
Done! kubectl is now configured to use "minikube" cluster
```

How to verify:

```powershell
kubectl get nodes
```

Common beginner mistake:

Running `kubectl` commands before minikube or another cluster is running.

## 12. kubectl

`kubectl` is the Kubernetes command-line tool.

Simple meaning:

```text
kubectl = tool you use to talk to the cluster
```

It can:

- apply YAML
- list pods
- show logs
- describe resources
- scale deployments
- delete resources

## 13. YAML Basics

Kubernetes objects are usually written in YAML.

Basic structure:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fastapi-app
spec:
  replicas: 1
```

YAML rules:

- indentation matters
- use spaces, not tabs
- `key: value` stores a value
- nested fields are indented
- `-` starts a list item

## 14. `apiVersion`, `kind`, `metadata`, `spec`

These fields appear in almost every Kubernetes YAML file.

`apiVersion`:

```yaml
apiVersion: apps/v1
```

Tells Kubernetes which API version to use for this object.

`kind`:

```yaml
kind: Deployment
```

Tells Kubernetes what type of object to create.

`metadata`:

```yaml
metadata:
  name: fastapi-app
```

Stores identity information such as name and labels.

`spec`:

```yaml
spec:
  replicas: 1
```

Describes the desired behavior.

Beginner memory:

```text
apiVersion = which API
kind = what object
metadata = who it is
spec = what you want it to do
```

## 15. Labels And Selectors

Labels are key-value tags attached to Kubernetes objects.

Example:

```yaml
labels:
  app: fastapi-app
```

Selectors find objects with matching labels.

Example:

```yaml
selector:
  app: fastapi-app
```

Why this matters:

A Service uses a selector to find the pods it should route traffic to.

Common mistake:

If pod label is `app: fastapi-app` but service selector is `app: api`, the Service will not route to those pods.

## 16. Apply YAML

Command:

```powershell
kubectl apply -f deployment.yaml
```

Where to run:

Run from the folder containing `deployment.yaml`, or provide a full path.

What each part means:

- `kubectl` talks to the Kubernetes cluster
- `apply` creates or updates resources
- `-f` means read from file
- `deployment.yaml` is the YAML file

Expected output:

```text
deployment.apps/fastapi-app created
```

or:

```text
deployment.apps/fastapi-app configured
```

How to verify:

```powershell
kubectl get deployments
kubectl get pods
```

Common beginner mistake:

Running apply from the wrong folder and getting a file-not-found error.

## 17. Logs

Command:

```powershell
kubectl logs <pod_name>
```

Where to run:

Run from any folder after the pod exists.

What each part means:

- `kubectl` talks to the cluster
- `logs` prints container logs from a pod
- `<pod_name>` is the pod name from `kubectl get pods`

Expected output:

For FastAPI, logs may include Uvicorn startup output.

How to verify:

First run:

```powershell
kubectl get pods
```

Then copy the pod name into `kubectl logs`.

Common beginner mistake:

Using the deployment name where a pod name is expected. Some commands support deployment logs, but beginners should first learn pod logs.

## 18. Scaling

Scaling means changing how many pod replicas should run.

Command:

```powershell
kubectl scale deployment fastapi-app --replicas=2
```

Where to run:

Run from any folder after the deployment exists.

What each part means:

- `kubectl` talks to the cluster
- `scale` changes replica count
- `deployment fastapi-app` selects the deployment
- `--replicas=2` asks for two pods

Expected output:

```text
deployment.apps/fastapi-app scaled
```

How to verify:

```powershell
kubectl get pods
```

Expected result:

You should eventually see two pods for the deployment.

Common beginner mistake:

Scaling a deployment before it exists.

## 19. Troubleshooting Basics

Useful commands:

```powershell
kubectl get pods
kubectl describe pod <pod_name>
kubectl logs <pod_name>
kubectl get services
```

Common issues:

- cluster is not running
- image name is wrong
- image is not available to minikube
- pod is stuck in `ImagePullBackOff`
- container app crashes
- YAML indentation is wrong
- Service selector does not match pod labels
- service `targetPort` does not match container port

Debugging order:

```text
Check pod status -> describe pod -> read logs -> check service selector/ports
```

## 20. Where Kubernetes Appears In AI Engineer Work

Kubernetes appears in:

- deploying Dockerized FastAPI AI services
- scaling backend APIs
- exposing model-serving endpoints
- managing configuration and secrets
- running RAG components in enterprise platforms
- final POC deployment discussion
- interview questions about productionization
