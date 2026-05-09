# Kubernetes Exercises

Use this mental model:

```text
YAML file -> Kubernetes object -> pod runs container -> service exposes it
```

## Exercise 1: Explain The Core Objects

### Task

Explain cluster, node, pod, deployment, and service in beginner language.

### Expected Answer

```text
Cluster = Kubernetes environment.
Node = machine inside the cluster.
Pod = smallest runnable unit, usually wrapping one app container.
Deployment = object that manages pod replicas.
Service = object that exposes matching pods through stable networking.
```

### Expected Commands

No command is required.

### Expected Output

You should be able to explain:

```text
Cluster -> Node -> Pod -> Container
Deployment manages pods.
Service exposes pods.
```

### Hints

- Pod is not the same as Deployment.
- Service is not the same as Deployment.

### Self-Check

Which object usually keeps pods alive?

Expected answer:

Deployment.

### Solution Outline

1. Define cluster.
2. Define node.
3. Define pod.
4. Define deployment.
5. Define service.

### Common Mistake

Saying a Service runs the app. A Service exposes pods; it does not run containers.

## Exercise 2: Decode YAML Fields

### Task

Explain these Kubernetes YAML fields:

```text
apiVersion
kind
metadata
spec
labels
selector
```

### Expected Commands

No command is required, but you can view the deployment file:

```powershell
Get-Content implementation\deployment.yaml
```

Where to run:

Run from:

```text
17-kubernetes-basics/
```

What each part means:

- `Get-Content` prints a file
- `implementation\deployment.yaml` is the file path

Expected output:

The YAML content prints in the terminal.

How to verify:

Check that you can explain every top-level field.

Common mistake:

Ignoring indentation. YAML nesting changes meaning.

### Hints

- `kind` tells Kubernetes what object to create.
- `spec` describes desired behavior.
- labels and selectors must match.

### Self-Check

What happens if a Service selector does not match pod labels?

Expected answer:

The Service will not route traffic to those pods.

### Solution Outline

1. Read `deployment.yaml`.
2. Identify `apiVersion`, `kind`, `metadata`, and `spec`.
3. Find pod labels.
4. Compare labels with selectors.

### Common Mistake

Thinking `metadata.name` and label values are the same thing. They can be different.

## Exercise 3: Apply Deployment And Service

### Task

Apply the sample Kubernetes YAML files.

### Expected Commands

Command:

```powershell
cd 17-kubernetes-basics\implementation
```

Where to run:

Run from the course root.

What each part means:

- `cd` changes folder
- the path moves into the folder with Kubernetes YAML files

Expected output:

PowerShell changes folder. Usually no success message appears.

How to verify:

```powershell
Get-ChildItem
```

You should see `deployment.yaml` and `service.yaml`.

Common mistake:

Running `kubectl apply -f deployment.yaml` from the wrong folder.

Command:

```powershell
kubectl apply -f deployment.yaml
```

Where to run:

Run from `17-kubernetes-basics/implementation/`.

What each part means:

- `kubectl` talks to Kubernetes
- `apply` creates or updates objects
- `-f` reads a file
- `deployment.yaml` defines the Deployment

Expected output:

```text
deployment.apps/fastapi-app created
```

How to verify:

```powershell
kubectl get deployments
```

Common mistake:

Applying before a Kubernetes cluster is running.

Command:

```powershell
kubectl apply -f service.yaml
```

Where to run:

Run from the same implementation folder.

What each part means:

- `service.yaml` defines the Service

Expected output:

```text
service/fastapi-service created
```

How to verify:

```powershell
kubectl get services
```

Common mistake:

Applying Service YAML with selector values that do not match pod labels.

### Hints

- minikube or another Kubernetes cluster must be running.
- The Docker image must be available to the cluster.

### Self-Check

Which file creates pods indirectly?

Expected answer:

`deployment.yaml`.

### Solution Outline

1. Start cluster if needed.
2. Move into implementation folder.
3. Apply deployment.
4. Apply service.
5. Check deployments, pods, and services.

## Exercise 4: Check Pod Status And Logs

### Task

List pods and inspect logs.

### Expected Commands

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
NAME                          READY   STATUS    RESTARTS   AGE
fastapi-app-...               1/1     Running   0          1m
```

How to verify:

Check that `STATUS` becomes `Running`.

Common mistake:

Assuming a pod is ready just because it exists. Check `READY` and `STATUS`.

Command:

```powershell
kubectl logs <pod_name>
```

Where to run:

Run from any folder after copying the real pod name.

What each part means:

- `logs` prints app output
- `<pod_name>` must be replaced with the actual pod name

Expected output:

FastAPI/Uvicorn logs if the container started.

How to verify:

Logs should not show startup crashes.

Common mistake:

Typing `<pod_name>` literally.

### Hints

- Use `kubectl get pods` first.
- Copy the exact pod name.

### Self-Check

What should you check if pod status is `CrashLoopBackOff`?

Expected answer:

Run `kubectl logs <pod_name>` and `kubectl describe pod <pod_name>`.

### Solution Outline

1. List pods.
2. Copy pod name.
3. Run logs.
4. If status is not running, describe the pod.

## Exercise 5: Scale The Deployment

### Task

Scale `fastapi-app` to two replicas.

### Expected Command

```powershell
kubectl scale deployment fastapi-app --replicas=2
```

Where to run:

Run from any folder after the Deployment exists.

What each part means:

- `kubectl` talks to the cluster
- `scale` changes replica count
- `deployment fastapi-app` selects the Deployment
- `--replicas=2` asks for two pods

Expected output:

```text
deployment.apps/fastapi-app scaled
```

How to verify:

```powershell
kubectl get pods
```

Expected output:

You should eventually see two pods for `fastapi-app`.

### Hints

- Kubernetes may take a few seconds to create the second pod.
- Service still points to matching pods through labels.

### Self-Check

Does scaling create another Service?

Expected answer:

No. It creates more pods managed by the Deployment.

### Solution Outline

1. Scale deployment.
2. List pods.
3. Confirm two replicas.
4. Optionally scale back to one.

### Common Mistake

Expecting the Service count to increase when scaling pods.

## Exercise 6: Clean Up

### Task

Delete the Service and Deployment from the cluster.

### Expected Commands

Command:

```powershell
kubectl delete -f service.yaml
```

Where to run:

Run from `17-kubernetes-basics/implementation/`.

What each part means:

- `delete` removes resources
- `-f service.yaml` reads the Service manifest

Expected output:

```text
service "fastapi-service" deleted
```

How to verify:

```powershell
kubectl get services
```

Common mistake:

Thinking this deletes pods. It deletes only the Service.

Command:

```powershell
kubectl delete -f deployment.yaml
```

Where to run:

Run from the implementation folder.

What each part means:

- deletes the Deployment from the manifest

Expected output:

```text
deployment.apps "fastapi-app" deleted
```

How to verify:

```powershell
kubectl get pods
```

Pods from the Deployment should disappear.

### Hints

- Delete Service and Deployment both.
- The Deployment owns the pods.

### Self-Check

Why do pods disappear after deleting the Deployment?

Expected answer:

Because the Deployment owns and manages those pods.

### Solution Outline

1. Delete Service.
2. Delete Deployment.
3. Check services.
4. Check pods.

### Common Mistake

Deleting only the Service and leaving the Deployment running.
