# 17 Kubernetes Basics

## 1. What This Module Is

This module teaches Kubernetes basics for AI Engineer reskilling and POC discussion.

Kubernetes manages containerized applications. Docker helps package and run containers. Kubernetes helps run containers in a controlled cluster with restart, scaling, service exposure, configuration, and deployment management.

Core mental model:

```text
YAML file -> Kubernetes object -> pod runs container -> service exposes it
```

## 2. Why Kubernetes Exists After Docker

Docker is excellent for packaging and running containers.

But when applications grow, teams need more than one local container:

- keep containers running if they crash
- run multiple copies of the same app
- expose apps through stable network names
- roll out new versions
- store configuration separately from images
- manage secrets
- schedule workloads across machines
- inspect logs and status consistently

Kubernetes exists to manage those containerized apps at cluster level.

Beginner comparison:

```text
Docker = build and run containers
Kubernetes = manage containers across a cluster
```

## 3. What You Should Finish Knowing

After this module, you should understand:

- why Kubernetes exists after Docker
- cluster
- node
- pod
- deployment
- service
- namespace
- ConfigMap
- Secret
- minikube
- kubectl
- YAML basics
- `apiVersion`
- `kind`
- `metadata`
- `spec`
- labels
- selectors
- logs
- scaling
- troubleshooting

## 4. Study Order

1. `00-overview.md`
2. `01-yaml-deployment-service.md`
3. `implementation/README.md`
4. `exercises.md`
5. `cheatsheet.md`
6. `interview-questions.md`

## 5. File List

- `README.md`: module guide.
- `00-overview.md`: Kubernetes concepts, mental model, minikube, kubectl, objects, commands, logs, scaling, and troubleshooting.
- `01-yaml-deployment-service.md`: YAML syntax, Deployment, Service, labels, selectors, ports, ConfigMap, Secret, and field decoding.
- `implementation/README.md`: apply/check/logs/scale/delete instructions for the sample manifests.
- `implementation/deployment.yaml`: FastAPI deployment example.
- `implementation/service.yaml`: service exposing the deployment.
- `exercises.md`: Kubernetes practice tasks with commands and checks.
- `cheatsheet.md`: practical command and YAML reference.
- `interview-questions.md`: Kubernetes interview Q&A.

## 6. Practical Scope

This module focuses on reading and applying basic Kubernetes YAML for a local/minikube FastAPI deployment.

It does not cover Helm, service mesh, ingress controllers, operators, autoscaling internals, or production cluster governance.

## 7. What Not To Over-Focus On

Do not memorize every Kubernetes object first.

First understand:

- pod
- deployment
- service
- labels and selectors
- YAML structure
- `kubectl apply`
- `kubectl get`
- `kubectl logs`
- `kubectl describe`

## 8. How This Helps In JRSS, Mettl, POC, And Interviews

- JRSS labs: you can read basic Kubernetes deployment files.
- Mettl: Kubernetes questions often test pod/deployment/service and YAML basics.
- POC: you can show how a Dockerized FastAPI app could be deployed locally with minikube.
- Interview: you can explain how a container image becomes a running pod and how a service exposes it.
