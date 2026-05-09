# Git, Docker, and Kubernetes MCQs

## MCQ 1: Git vs GitHub

Question:

What is the difference between Git and GitHub?

Options:

A. Git is version control; GitHub is a cloud platform for hosting Git repositories  
B. GitHub is a Python package; Git is a web browser  
C. They are exactly the same  
D. Git is only for Docker

Correct answer:

A. Git is version control; GitHub is a cloud platform for hosting Git repositories

Explanation:

Git runs locally and tracks file history. GitHub hosts repositories online for sharing and collaboration.

Common trap:

Thinking `git commit` uploads code to GitHub. It saves locally. `git push` uploads.

## MCQ 2: `git add .`

Question:

What does `git add .` do?

Options:

A. Stages changed files in the current folder and subfolders  
B. Creates a remote repository  
C. Deletes untracked files  
D. Commits changes permanently

Correct answer:

A. Stages changed files in the current folder and subfolders

Explanation:

`git add .` moves changes into the staging area for the next commit.

Common trap:

Thinking `git add` creates a commit. It only stages changes.

## MCQ 3: `git commit -m`

Question:

What does `-m` mean in `git commit -m "Add API"`?

Options:

A. Message  
B. Merge  
C. Move  
D. Model

Correct answer:

A. Message

Explanation:

`-m` provides the commit message directly in the command.

Common trap:

Using vague messages like `"changes"`. Good messages explain what changed.

## MCQ 4: Docker image

Question:

What is a Docker image?

Options:

A. A packaged template used to create containers  
B. A running process only  
C. A Kubernetes node  
D. A Git branch

Correct answer:

A. A packaged template used to create containers

Explanation:

An image contains app files, dependencies, and runtime setup. Containers are running instances of images.

Common trap:

Confusing image and container.

## MCQ 5: Docker container

Question:

What is a Docker container?

Options:

A. A running instance of an image  
B. A text file only  
C. A Git commit  
D. A Kubernetes YAML key

Correct answer:

A. A running instance of an image

Explanation:

You build an image, then run a container from that image.

Common trap:

Saying "container is the Dockerfile." Dockerfile is the recipe.

## MCQ 6: Dockerfile

Question:

What is a Dockerfile?

Options:

A. A recipe for building a Docker image  
B. A running container  
C. A Python virtual environment  
D. A Kubernetes cluster

Correct answer:

A. A recipe for building a Docker image

Explanation:

Docker reads Dockerfile instructions such as `FROM`, `COPY`, `RUN`, and `CMD` to build an image.

Common trap:

Thinking Dockerfile itself is the image. It is the build recipe.

## MCQ 7: Port mapping

Question:

What does `8000:8000` usually mean in Docker run port mapping?

Options:

A. Host port 8000 maps to container port 8000  
B. Delete port 8000  
C. Create two containers  
D. Install FastAPI

Correct answer:

A. Host port 8000 maps to container port 8000

Explanation:

The left side is the host machine port. The right side is the container port.

Common trap:

Forgetting which side is host and which side is container.

## MCQ 8: Kubernetes pod

Question:

What is a Kubernetes pod?

Options:

A. The smallest deployable unit in Kubernetes, usually running one or more containers  
B. A Docker image registry  
C. A Git repository  
D. A Python class

Correct answer:

A. The smallest deployable unit in Kubernetes, usually running one or more containers

Explanation:

Kubernetes schedules pods. Containers run inside pods.

Common trap:

Confusing pod with deployment. A deployment manages pods.

## MCQ 9: Deployment

Question:

What does a Kubernetes Deployment manage?

Options:

A. Desired number and rollout of pods  
B. Python package installation  
C. Git staging area  
D. Local virtual environment

Correct answer:

A. Desired number and rollout of pods

Explanation:

A Deployment tells Kubernetes how many pod replicas should exist and how to update them.

Common trap:

Thinking deployment and pod are identical.

## MCQ 10: Service

Question:

What is a Kubernetes Service used for?

Options:

A. Stable network access to pods  
B. Writing Python functions  
C. Building Docker images only  
D. Creating Git branches

Correct answer:

A. Stable network access to pods

Explanation:

Pods can be replaced and get new IPs. A Service gives a stable way to reach them.

Common trap:

Thinking users should directly call pod IPs.

## MCQ 11: ConfigMap vs Secret

Question:

Which Kubernetes object should store non-sensitive configuration?

Options:

A. ConfigMap  
B. Secret  
C. Pod only  
D. Namespace only

Correct answer:

A. ConfigMap

Explanation:

ConfigMap stores non-sensitive configuration. Secret is for sensitive values such as tokens or passwords.

Common trap:

Putting API keys in ConfigMap. Use Secret for sensitive values.

## MCQ 12: `kubectl logs`

Question:

What is `kubectl logs` used for?

Options:

A. Viewing logs from a pod/container  
B. Building Docker image  
C. Creating Git commit  
D. Running Python tests

Correct answer:

A. Viewing logs from a pod/container

Explanation:

Logs help debug what happened inside running workloads.

Common trap:

Checking only YAML when the real error is visible in pod logs.
