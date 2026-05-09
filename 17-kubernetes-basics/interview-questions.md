# Kubernetes Interview Questions

## 1. What is Kubernetes?

Short answer:

Kubernetes is a platform for managing containerized applications.

Expanded answer:

Kubernetes runs containers in pods, keeps desired replicas running, restarts failed pods, exposes apps through Services, and manages configuration and secrets.

Project example:

A Dockerized FastAPI AI backend can be deployed to minikube using a Deployment and Service YAML.

Common wrong answer:

Kubernetes is the same as Docker. Docker packages/runs containers; Kubernetes manages containers in a cluster.

## 2. Why Kubernetes after Docker?

Short answer:

Docker runs containers; Kubernetes manages them at cluster level.

Expanded answer:

When apps need restart behavior, scaling, service discovery, configuration, secrets, and multi-node management, Kubernetes provides orchestration around containers.

Project example:

The FastAPI image built in Docker can be run as pods managed by a Kubernetes Deployment.

Common wrong answer:

Kubernetes replaces the need to understand Docker images.

## 3. What is a cluster?

Short answer:

A cluster is the Kubernetes environment where workloads run.

Expanded answer:

A cluster contains nodes and Kubernetes control components. In local practice, minikube creates a small cluster on one machine.

Project example:

`minikube start` creates a local cluster for testing the FastAPI deployment YAML.

Common wrong answer:

A cluster is a single pod.

## 4. What is a node?

Short answer:

A node is a machine in a Kubernetes cluster.

Expanded answer:

Pods run on nodes. In minikube, the cluster may have one node. In enterprise, a cluster usually has multiple nodes.

Project example:

`kubectl get nodes` shows the minikube node.

Common wrong answer:

A node is the same as a container.

## 5. What is a pod?

Short answer:

A pod is the smallest runnable unit in Kubernetes.

Expanded answer:

A pod wraps one or more containers and gives them shared networking and lifecycle. Most beginner web apps use one container per pod.

Project example:

The FastAPI container runs inside a pod created by the Deployment.

Common wrong answer:

A pod is always the same thing as a Docker container. A pod is a Kubernetes wrapper around container(s).

## 6. What is a Deployment?

Short answer:

A Deployment manages pod replicas.

Expanded answer:

It describes desired state: image, replica count, pod template, labels, and selectors. Kubernetes tries to keep actual running pods matching that desired state.

Project example:

`deployment.yaml` asks Kubernetes to keep one `fastapi-app` pod running.

Common wrong answer:

A Deployment exposes the app to users. A Service exposes pods.

## 7. What is a Service?

Short answer:

A Service gives stable network access to pods.

Expanded answer:

Pods can be recreated and get new IPs. A Service uses selectors to route traffic to the current matching pods.

Project example:

`service.yaml` exposes pods labeled `app: fastapi-app` using NodePort `30080`.

Common wrong answer:

A Service creates pods. A Deployment creates/manages pods.

## 8. Deployment vs Service?

Short answer:

Deployment runs and manages pods. Service exposes pods.

Expanded answer:

A web app commonly needs both. Deployment ensures the app container is running. Service gives a stable network entry point to the pods.

Project example:

`deployment.yaml` runs FastAPI pods. `service.yaml` exposes those pods.

Common wrong answer:

Deployment and Service are interchangeable.

## 9. What is a namespace?

Short answer:

A namespace is a grouping boundary inside a cluster.

Expanded answer:

Namespaces help separate resources by team, environment, or application. If no namespace is specified, many commands use `default`.

Project example:

A POC might run in the `default` namespace locally, while real environments may use `dev`, `qa`, or `prod`.

Common wrong answer:

Namespace is the same as a node.

## 10. ConfigMap vs Secret?

Short answer:

ConfigMap stores non-sensitive config. Secret stores sensitive config.

Expanded answer:

Use ConfigMap for values such as environment name or log level. Use Secret for API keys, passwords, and tokens, with proper access control.

Project example:

`APP_ENV=local` can be a ConfigMap value. An LLM API key should be a Secret, not committed as plain YAML.

Common wrong answer:

ConfigMap is fine for passwords.

## 11. What is minikube?

Short answer:

minikube is a local Kubernetes cluster for learning and testing.

Expanded answer:

It lets you practice Kubernetes commands and YAML on your machine without needing a cloud cluster.

Project example:

Use minikube to test the FastAPI Deployment and Service from this module.

Common wrong answer:

minikube is the same as a production enterprise cluster.

## 12. What is kubectl?

Short answer:

`kubectl` is the Kubernetes command-line tool.

Expanded answer:

It sends commands to the cluster, such as apply YAML, list pods, read logs, describe resources, scale deployments, and delete objects.

Project example:

```powershell
kubectl apply -f deployment.yaml
kubectl get pods
kubectl logs <pod_name>
```

Common wrong answer:

`kubectl` is a YAML file. It is a CLI tool.

## 13. What do `apiVersion`, `kind`, `metadata`, and `spec` mean?

Short answer:

They define which API to use, what object to create, object identity, and desired behavior.

Expanded answer:

`apiVersion` selects the Kubernetes API version. `kind` says the resource type. `metadata` stores name and labels. `spec` describes what Kubernetes should create or maintain.

Project example:

`kind: Deployment` creates a Deployment; `spec.replicas: 1` asks for one pod.

Common wrong answer:

These fields are optional decoration. They are core Kubernetes object fields.

## 14. What are labels and selectors?

Short answer:

Labels tag resources. Selectors find matching labels.

Expanded answer:

Services and Deployments use selectors to connect to the correct pods. If labels and selectors do not match, traffic or management may not work.

Project example:

Service selector `app: fastapi-app` routes to pods labeled `app: fastapi-app`.

Common wrong answer:

Labels are only comments. They affect how Kubernetes objects find each other.

## 15. How do you view logs?

Short answer:

Use `kubectl logs <pod_name>`.

Expanded answer:

First list pods with `kubectl get pods`, then pass the real pod name to `kubectl logs`. Logs help debug app startup and runtime errors.

Project example:

If the FastAPI pod crashes, use logs to see Uvicorn or import errors.

Common wrong answer:

Only check `kubectl get pods`. Status alone is often not enough.

## 16. How do you scale a Deployment?

Short answer:

Use `kubectl scale deployment <name> --replicas=<count>`.

Expanded answer:

Scaling changes desired pod count. Kubernetes creates or removes pods to match the requested replica count.

Project example:

```powershell
kubectl scale deployment fastapi-app --replicas=2
```

Common wrong answer:

Scaling creates more Services. It creates more pods managed by the Deployment.

## 17. Scenario: Service exists but app is unreachable. What do you check?

Short answer:

Check pod status, service selector, pod labels, ports, and logs.

Expanded answer:

The Service may not match pods, `targetPort` may be wrong, the pod may not be running, or the app may be listening on a different port.

Project example:

Check:

```powershell
kubectl get pods
kubectl describe pod <pod_name>
kubectl logs <pod_name>
kubectl get services
```

Common wrong answer:

Assume the YAML applied successfully, so the app must be reachable.
