# Kubernetes Cheatsheet

## Mental Model

Syntax:

```text
YAML file -> Kubernetes object -> pod runs container -> service exposes it
```

Meaning:

YAML describes desired state. Kubernetes creates objects. Deployment creates pods. Service exposes matching pods.

When to use:

Use this when reading or debugging Kubernetes manifests.

Example:

```text
deployment.yaml -> Deployment -> Pod -> FastAPI container
service.yaml -> Service -> routes to pod
```

Be careful:

Kubernetes usually runs images you already built. It does not automatically build your Dockerfile.

## Start minikube

Command:

```powershell
minikube start
```

Meaning:

Starts a local Kubernetes cluster.

When to use:

Use before practicing Kubernetes locally.

Example:

```text
Done! kubectl is now configured to use "minikube" cluster
```

Be careful:

If minikube is not installed, this command will not work.

## List Nodes

Command:

```powershell
kubectl get nodes
```

Meaning:

Shows machines in the cluster.

When to use:

Use to verify cluster connectivity.

Example:

```text
NAME       STATUS   ROLES
minikube   Ready    control-plane
```

Be careful:

If this fails, fix cluster connection before applying YAML.

## Apply YAML

Command:

```powershell
kubectl apply -f deployment.yaml
```

Meaning:

Creates or updates resources from a YAML file.

When to use:

Use after writing or changing Kubernetes YAML.

Example:

```powershell
kubectl apply -f deployment.yaml
```

Be careful:

Run from the folder containing the file or provide the correct path.

## List Pods

Command:

```powershell
kubectl get pods
```

Meaning:

Shows pods in the current namespace.

When to use:

Use to check whether containers are running.

Example:

```text
NAME                 READY   STATUS    RESTARTS   AGE
fastapi-app-...      1/1     Running   0          1m
```

Be careful:

`Running` does not always mean the app works. Check logs and service if needed.

## List Deployments

Command:

```powershell
kubectl get deployments
```

Meaning:

Shows Deployment resources.

When to use:

Use to check desired and available replicas.

Example:

```text
NAME          READY   UP-TO-DATE   AVAILABLE
fastapi-app   1/1     1            1
```

Be careful:

Deployment is not the pod itself. It manages pods.

## List Services

Command:

```powershell
kubectl get services
```

Meaning:

Shows Services that expose pods.

When to use:

Use to check Service type, cluster IP, and ports.

Example:

```text
fastapi-service   NodePort   ...   8000:30080/TCP
```

Be careful:

Service must have selectors matching pod labels.

## Describe Pod

Command:

```powershell
kubectl describe pod <pod_name>
```

Meaning:

Shows detailed pod state and events.

When to use:

Use when pod is stuck, crashing, or cannot pull image.

Example:

```powershell
kubectl describe pod fastapi-app-abc123
```

Be careful:

Read the `Events` section.

## Logs

Command:

```powershell
kubectl logs <pod_name>
```

Meaning:

Shows application logs from a pod.

When to use:

Use to debug container startup or runtime errors.

Example:

```powershell
kubectl logs fastapi-app-abc123
```

Be careful:

Replace `<pod_name>` with the actual pod name.

## Scale Deployment

Command:

```powershell
kubectl scale deployment fastapi-app --replicas=2
```

Meaning:

Changes desired pod count for a Deployment.

When to use:

Use to practice scaling.

Example:

```text
deployment.apps/fastapi-app scaled
```

Be careful:

Scaling creates more pods, not more Services.

## Delete YAML Resources

Command:

```powershell
kubectl delete -f deployment.yaml
```

Meaning:

Deletes resources defined in the YAML file.

When to use:

Use to clean up after practice.

Example:

```text
deployment.apps "fastapi-app" deleted
```

Be careful:

Deleting a Deployment removes pods it manages.

## YAML Fields

Syntax:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fastapi-app
spec:
  replicas: 1
```

Meaning:

- `apiVersion`: Kubernetes API version.
- `kind`: object type.
- `metadata`: name and labels.
- `spec`: desired behavior.

When to use:

Use in Kubernetes manifest files.

Example:

Deployment uses `apps/v1`; Service commonly uses `v1`.

Be careful:

Indentation changes meaning. Use spaces, not tabs.

## Core Terms

- Cluster: Kubernetes environment.
- Node: machine in the cluster.
- Pod: smallest runnable unit.
- Deployment: manages pods and replicas.
- Service: exposes matching pods.
- Namespace: grouping boundary.
- ConfigMap: non-secret config.
- Secret: sensitive config.
- minikube: local Kubernetes.
- kubectl: Kubernetes command-line tool.
- Label: tag attached to object.
- Selector: rule for finding matching labels.
