# YAML, Deployment, And Service

## 1. What This Topic Covers

Kubernetes resources are usually described using YAML files.

This topic explains the beginner flow:

```text
YAML file -> Kubernetes object -> pod runs container -> service exposes it
```

For this module:

- `deployment.yaml` tells Kubernetes how to run FastAPI pods
- `service.yaml` tells Kubernetes how to expose those pods

## 2. YAML Basics

YAML is a structured text format.

Kubernetes uses YAML to describe desired state:

```text
I want a Deployment named fastapi-app with 1 replica.
I want a Service named fastapi-service that routes to that app.
```

Basic YAML example:

```yaml
metadata:
  name: fastapi-app
```

Meaning:

- `metadata` is a key
- `name` is nested under `metadata`
- indentation shows nesting
- spaces matter

List example:

```yaml
ports:
  - containerPort: 8000
```

Meaning:

- `ports` is a key
- `-` starts a list item
- `containerPort: 8000` is a key-value pair in that list item

Common YAML mistake:

Using tabs or wrong indentation.

## 3. Common Kubernetes YAML Fields

Most Kubernetes YAML files include:

```yaml
apiVersion:
kind:
metadata:
spec:
```

### `apiVersion`

```yaml
apiVersion: apps/v1
```

Meaning:

Which Kubernetes API version should handle this object.

### `kind`

```yaml
kind: Deployment
```

Meaning:

What type of Kubernetes object this file creates.

### `metadata`

```yaml
metadata:
  name: fastapi-app
```

Meaning:

Information that identifies the object, such as its name and labels.

### `spec`

```yaml
spec:
  replicas: 1
```

Meaning:

The desired behavior for the object.

Beginner memory:

```text
apiVersion = which Kubernetes API
kind = what object
metadata = identity
spec = desired behavior
```

## 4. Deployment YAML

File name:

```text
deployment.yaml
```

Folder path:

```text
17-kubernetes-basics/implementation/deployment.yaml
```

What this file is for:

It tells Kubernetes to run and maintain FastAPI app pods.

Full code:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fastapi-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: fastapi-app
  template:
    metadata:
      labels:
        app: fastapi-app
    spec:
      containers:
        - name: fastapi-app
          image: fastapi-docker-example:latest
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 8000
```

## 5. Deployment Line-By-Line

```yaml
apiVersion: apps/v1
```

Use the Kubernetes apps API version for Deployment.

```yaml
kind: Deployment
```

Create a Deployment object.

```yaml
metadata:
  name: fastapi-app
```

Name the Deployment `fastapi-app`.

```yaml
spec:
  replicas: 1
```

Ask Kubernetes to keep one pod replica running.

```yaml
selector:
  matchLabels:
    app: fastapi-app
```

Tell the Deployment which pods it manages by matching labels.

```yaml
template:
```

Define the pod template. Kubernetes uses this template when creating pods.

```yaml
metadata:
  labels:
    app: fastapi-app
```

Attach label `app: fastapi-app` to pods created from this template.

```yaml
containers:
  - name: fastapi-app
```

Start the container list and name the container.

```yaml
image: fastapi-docker-example:latest
```

Use the Docker image named `fastapi-docker-example:latest`.

```yaml
imagePullPolicy: IfNotPresent
```

Use a local image if it exists. This is useful in local/minikube practice.

```yaml
ports:
  - containerPort: 8000
```

Document that the container listens on port `8000`.

## 6. Labels And Selectors

Labels are tags on objects.

Pod label:

```yaml
labels:
  app: fastapi-app
```

Selectors find objects with matching labels.

Deployment selector:

```yaml
selector:
  matchLabels:
    app: fastapi-app
```

Service selector:

```yaml
selector:
  app: fastapi-app
```

Meaning:

```text
Find pods labeled app=fastapi-app.
```

Common mistake:

If the Service selector says `app: api` but pods have `app: fastapi-app`, the Service has no matching pods.

## 7. Service YAML

File name:

```text
service.yaml
```

Folder path:

```text
17-kubernetes-basics/implementation/service.yaml
```

What this file is for:

It exposes the FastAPI pods through a stable Service.

Full code:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: fastapi-service
spec:
  type: NodePort
  selector:
    app: fastapi-app
  ports:
    - port: 8000
      targetPort: 8000
      nodePort: 30080
```

## 8. Service Line-By-Line

```yaml
apiVersion: v1
```

Use the core Kubernetes API version.

```yaml
kind: Service
```

Create a Service object.

```yaml
metadata:
  name: fastapi-service
```

Name the Service `fastapi-service`.

```yaml
spec:
  type: NodePort
```

Expose the Service on a port on the Kubernetes node. This is simple for local/minikube practice.

```yaml
selector:
  app: fastapi-app
```

Route traffic to pods with label `app: fastapi-app`.

```yaml
ports:
  - port: 8000
    targetPort: 8000
    nodePort: 30080
```

Port meanings:

- `port: 8000` is the Service port inside the cluster
- `targetPort: 8000` is the pod/container port to forward to
- `nodePort: 30080` is the port exposed on the node

## 9. Deployment vs Service

Deployment and Service are different.

```text
Deployment = runs and manages pods
Service = exposes matching pods
```

You usually need both for a web app:

```text
Deployment creates FastAPI pods.
Service gives a stable way to reach those pods.
```

## 10. ConfigMap And Secret Basics

This implementation does not include ConfigMap or Secret files, but you should understand them.

ConfigMap:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_ENV: local
```

Meaning:

Store non-sensitive config.

Secret:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: app-secret
type: Opaque
stringData:
  API_KEY: replace-with-safe-placeholder
```

Meaning:

Store sensitive config separately from normal app YAML.

Common mistake:

Putting real API keys in plain committed YAML files.

## 11. Apply Deployment And Service

Command:

```powershell
kubectl apply -f deployment.yaml
```

Where to run:

Run from:

```text
17-kubernetes-basics/implementation/
```

What each part means:

- `kubectl` talks to the cluster
- `apply` creates or updates resources
- `-f` reads from a file
- `deployment.yaml` is the file

Expected output:

```text
deployment.apps/fastapi-app created
```

How to verify:

```powershell
kubectl get deployments
kubectl get pods
```

Common mistake:

Applying the Service but forgetting the Deployment. A Service without matching pods cannot serve traffic.

Command:

```powershell
kubectl apply -f service.yaml
```

Where to run:

Run from the same implementation folder.

What each part means:

- `service.yaml` defines the Service object

Expected output:

```text
service/fastapi-service created
```

How to verify:

```powershell
kubectl get services
```

Common mistake:

Selector does not match pod label.

## 12. Check Status

Command:

```powershell
kubectl get pods
```

Where to run:

Run from any folder.

What each part means:

- `kubectl` talks to the cluster
- `get` lists resources
- `pods` is the resource type

Expected output:

```text
NAME                           READY   STATUS    RESTARTS   AGE
fastapi-app-...                1/1     Running   0          1m
```

How to verify:

`STATUS` should become `Running`.

Common mistake:

Seeing `ImagePullBackOff` and not checking whether the image exists in the cluster environment.

## 13. Logs And Troubleshooting

Command:

```powershell
kubectl describe pod <pod_name>
```

Where to run:

Run from any folder after getting the pod name.

What each part means:

- `describe` prints detailed resource information
- `pod` is the resource type
- `<pod_name>` is the exact pod name

Expected output:

Detailed pod information and events.

How to verify:

Look at the `Events` section for image, scheduling, or crash errors.

Common mistake:

Only using `kubectl get pods` and not reading events.

Command:

```powershell
kubectl logs <pod_name>
```

Where to run:

Run from any folder.

What each part means:

- `logs` prints application output from the pod

Expected output:

FastAPI/Uvicorn logs if the app started.

How to verify:

Logs should show whether the app started or crashed.

Common mistake:

Using a placeholder literally. Replace `<pod_name>` with the real pod name.

## 14. Delete Resources

Command:

```powershell
kubectl delete -f service.yaml
kubectl delete -f deployment.yaml
```

Where to run:

Run from:

```text
17-kubernetes-basics/implementation/
```

What each part means:

- `delete` removes resources
- `-f` reads the file to know what to delete

Expected output:

```text
service "fastapi-service" deleted
deployment.apps "fastapi-app" deleted
```

How to verify:

```powershell
kubectl get pods
kubectl get services
```

Common mistake:

Deleting the Deployment first and wondering why pods disappear. That is expected because the Deployment owns the pods.

## 15. Where This Appears In AI Engineer Work

Kubernetes YAML appears in:

- deploying a FastAPI AI backend
- exposing RAG services
- scaling API replicas
- configuring model-serving apps
- separating non-secret config from images
- interview answers about production readiness
