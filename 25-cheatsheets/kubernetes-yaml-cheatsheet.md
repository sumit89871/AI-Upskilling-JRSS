# Kubernetes YAML Cheatsheet

## apiVersion

Meaning: Kubernetes API version for the resource.

Use when: Writing any manifest.

Example: `apiVersion: apps/v1`

Be careful: Deployment and Service use different API groups.

## kind

Meaning: Resource type.

Use when: Telling Kubernetes what to create.

Example: `kind: Deployment`

Be careful: `Deployment`, `Service`, `ConfigMap`, and `Secret` behave differently.

## metadata

Meaning: Name, labels, and resource metadata.

Use when: Identifying resources.

Example: `name: qa-api`

Be careful: Labels must match selectors.

## spec

Meaning: Desired configuration.

Use when: Defining replicas, containers, ports, or service mapping.

Example: `replicas: 2`

Be careful: YAML indentation matters.

## Service

Meaning: Stable network access to pods.

Use when: Exposing a deployment.

Example: `type: NodePort` for minikube demo.

Be careful: Service is not the same as Deployment.
