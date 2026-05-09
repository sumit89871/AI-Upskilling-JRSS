# Kubernetes FastAPI Example

## 1. Project Goal

This folder contains Kubernetes YAML for running a Dockerized FastAPI app.

Core mental model:

```text
YAML file -> Kubernetes object -> pod runs container -> service exposes it
```

## 2. Files In This Folder

Folder:

```text
17-kubernetes-basics/implementation/
```

Files:

- `deployment.yaml`: creates a Deployment named `fastapi-app`.
- `service.yaml`: creates a Service named `fastapi-service`.
- `README.md`: explains how to apply, check, log, scale, and delete.

## 3. Important Assumption

The Docker image exists in the Kubernetes environment:

```text
fastapi-docker-example:latest
```

In local minikube practice, image availability can be a common issue. If the pod shows `ImagePullBackOff`, Kubernetes may not be able to find the image.

## 4. Read `deployment.yaml`

What it creates:

```text
Deployment -> ReplicaSet -> Pod -> Container
```

Important fields:

- `apiVersion: apps/v1`: API version for Deployment.
- `kind: Deployment`: object type.
- `metadata.name: fastapi-app`: Deployment name.
- `replicas: 1`: keep one pod running.
- `selector.matchLabels.app: fastapi-app`: choose pods to manage.
- `template.metadata.labels.app: fastapi-app`: label pods.
- `image: fastapi-docker-example:latest`: container image.
- `containerPort: 8000`: app port inside container.

## 5. Read `service.yaml`

What it creates:

```text
Service -> routes traffic to matching pods
```

Important fields:

- `apiVersion: v1`: API version for Service.
- `kind: Service`: object type.
- `metadata.name: fastapi-service`: Service name.
- `type: NodePort`: expose through a node port.
- `selector.app: fastapi-app`: find matching pods.
- `port: 8000`: Service port.
- `targetPort: 8000`: pod/container port.
- `nodePort: 30080`: node-level port.

## 6. Start Local Kubernetes

Command:

```powershell
minikube start
```

Where to run:

Run from any folder if minikube is installed.

What each part means:

- `minikube` runs the local Kubernetes tool
- `start` starts the local cluster

Expected output:

```text
Done! kubectl is now configured to use "minikube" cluster
```

How to verify:

```powershell
kubectl get nodes
```

Expected result:

You should see at least one node.

Common mistake:

Running `kubectl apply` before a cluster is available.

## 7. Apply Deployment

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

- `kubectl` talks to Kubernetes
- `apply` creates or updates resources
- `-f` reads a file
- `deployment.yaml` is the Deployment manifest

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

Expected result:

Deployment appears and a pod is created.

Common mistake:

Using the wrong folder and getting a file-not-found error.

## 8. Apply Service

Command:

```powershell
kubectl apply -f service.yaml
```

Where to run:

Run from:

```text
17-kubernetes-basics/implementation/
```

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

Expected result:

`fastapi-service` appears with type `NodePort`.

Common mistake:

Service selector does not match pod labels.

## 9. Check Pods

Command:

```powershell
kubectl get pods
```

Where to run:

Run from any folder.

What each part means:

- `kubectl` talks to cluster
- `get` lists resources
- `pods` lists pod resources

Expected output:

```text
NAME                          READY   STATUS    RESTARTS   AGE
fastapi-app-...               1/1     Running   0          1m
```

How to verify:

`STATUS` should be `Running`.

Common mistake:

Assuming `ContainerCreating` is always an error. It can be temporary. If it stays stuck, describe the pod.

## 10. Check Logs

Command:

```powershell
kubectl logs <pod_name>
```

Where to run:

Run from any folder after copying the pod name from `kubectl get pods`.

What each part means:

- `logs` shows container output
- `<pod_name>` must be replaced with a real pod name

Expected output:

FastAPI/Uvicorn logs if the app started.

How to verify:

Logs should show whether the app started successfully.

Common mistake:

Typing `<pod_name>` literally instead of replacing it.

## 11. Describe For Troubleshooting

Command:

```powershell
kubectl describe pod <pod_name>
```

Where to run:

Run from any folder.

What each part means:

- `describe` prints detailed information and events
- `pod` is the resource type
- `<pod_name>` is the real pod name

Expected output:

Detailed pod state, container state, and event messages.

How to verify:

Look for events such as image pull errors or crash restart details.

Common mistake:

Ignoring the `Events` section.

## 12. Scale Deployment

Command:

```powershell
kubectl scale deployment fastapi-app --replicas=2
```

Where to run:

Run from any folder after the Deployment exists.

What each part means:

- `scale` changes desired replica count
- `deployment fastapi-app` selects the Deployment
- `--replicas=2` asks Kubernetes for two pods

Expected output:

```text
deployment.apps/fastapi-app scaled
```

How to verify:

```powershell
kubectl get pods
```

Expected result:

You should eventually see two FastAPI pods.

Common mistake:

Forgetting that scaling creates more pods, not more Services.

## 13. Delete Resources

Command:

```powershell
kubectl delete -f service.yaml
```

Where to run:

Run from the implementation folder.

What each part means:

- `delete` removes resources from the cluster
- `-f service.yaml` deletes the Service defined in the file

Expected output:

```text
service "fastapi-service" deleted
```

How to verify:

```powershell
kubectl get services
```

Common mistake:

Thinking this deletes pods. The Service exposes pods; it does not own them.

Command:

```powershell
kubectl delete -f deployment.yaml
```

Where to run:

Run from the implementation folder.

What each part means:

- deletes the Deployment defined in `deployment.yaml`

Expected output:

```text
deployment.apps "fastapi-app" deleted
```

How to verify:

```powershell
kubectl get pods
```

Expected result:

Pods created by the Deployment should disappear.

Common mistake:

Deleting only the Service and wondering why pods are still running.
