# Branching, Conflicts, And Team Workflow

## 1. What Branching Is

A branch is a separate line of work in Git.

Simple meaning:

```text
Branch = safe workspace for a specific change
```

If `main` has stable code, you can create a new branch to try a feature:

```text
main
  feature-rag
```

Your feature branch can change files without immediately changing `main`.

## 2. The Most Important Beginner Idea

A branch is not a copy-pasted project folder.

Git manages branches inside the same repository.

You do not need:

```text
project-main/
project-feature/
project-final/
```

You keep one repository and switch branches.

## 3. Why Branches Matter

Branches help you:

- build a FastAPI endpoint safely
- try a new RAG retrieval strategy
- update Docker files without breaking main code
- collaborate with team members
- isolate risky experiments

## 4. Beginner Mental Model

```text
main branch -> create feature branch -> commit changes -> merge back to main
```

Example:

```text
main
  |
  +-- feature-fastapi-health
```

When the feature works, merge it back.

## 5. Command: `git branch`

Command:

```powershell
git branch
```

Meaning:

Show local branches.

Possible output:

```text
* main
```

Meaning:

- `main` is the branch name.
- `*` means this is the branch you are currently on.

Create a branch:

```powershell
git branch feature-api
```

Command parts:

- `git branch` works with branches.
- `feature-api` is the new branch name.

This creates the branch but does not switch to it.

Expected output:

Usually no output if the branch is created successfully.

How to verify:

```powershell
git branch
```

Expected verification output:

```text
  feature-api
* main
```

The `*` marks the branch you are currently using.

## 6. Command: `git switch`

Command:

```powershell
git switch feature-api
```

Meaning:

Move your working folder to the `feature-api` branch.

Expected output:

```text
Switched to branch 'feature-api'
```

Create and switch in one command:

```powershell
git switch -c feature-api
```

Command parts:

- `switch` changes branch.
- `-c` means create.
- `feature-api` is the branch name.

Expected output:

```text
Switched to a new branch 'feature-api'
```

How to verify:

```powershell
git branch
```

Expected verification output:

```text
* feature-api
  main
```

Older command:

```powershell
git checkout feature-api
```

`checkout` can switch branches, but `switch` is clearer for beginners.

Expected output:

```text
Switched to branch 'feature-api'
```

## 7. Command: `git merge`

Command:

```powershell
git switch main
git merge feature-api
```

Meaning:

Bring changes from `feature-api` into `main`.

Mental model:

```text
Take the completed feature work and combine it into the stable branch.
```

Common mistake:

Merging before the feature is committed.

Check first:

```powershell
git status
```

Expected `git status` output before a clean merge:

```text
nothing to commit, working tree clean
```

Expected merge output may look like:

```text
Updating a1b2c3d..d4e5f6g
Fast-forward
 file.md | 1 +
```

Meaning:

- `Fast-forward` means Git could move `main` forward without conflict.
- `file.md | 1 +` means one line was added in that file.

## 8. What Is A Merge Conflict?

A merge conflict happens when Git cannot safely combine changes automatically.

Example:

Two people edit the same line in `README.md`.

Git may show conflict markers:

```text
<<<<<<< HEAD
Local version
=======
Incoming version
>>>>>>> feature-api
```

How to read it:

- `<<<<<<< HEAD` starts your current branch version.
- `=======` separates the two versions.
- `>>>>>>> feature-api` ends the incoming branch version.

To fix:

1. Open the file.
2. Decide the correct final text.
3. Delete conflict markers.
4. Save the file.
5. Run `git add`.
6. Run `git commit`.

## 9. Clone, Pull, And Push

### `git clone`

Command:

```powershell
git clone https://github.com/example/repo.git
```

Meaning:

Copy a remote repository to your machine.

Use when:

You do not have the project locally yet.

Expected output:

```text
Cloning into 'repo'...
Receiving objects: 100%
```

How to verify:

```powershell
cd repo
git status
```

Expected verification:

```text
On branch main
Your branch is up to date with 'origin/main'.
```

### `git pull`

Command:

```powershell
git pull
```

Meaning:

Download remote changes and integrate them into your local branch.

Use when:

You already have the repository and want latest remote changes.

Expected output when already updated:

```text
Already up to date.
```

Expected output when changes are downloaded:

```text
Updating a1b2c3d..d4e5f6g
Fast-forward
```

Common error:

```text
Please commit your changes or stash them before you merge.
```

Meaning:

You have local uncommitted changes that may conflict with remote changes.

### `git push`

Command:

```powershell
git push
```

Meaning:

Upload your local commits to the remote repository.

Use when:

You have committed local changes and want to share them.

Expected output:

```text
Enumerating objects: 5, done.
Writing objects: 100%
To https://github.com/example/repo.git
```

Common error:

```text
fatal: The current branch feature-api has no upstream branch.
```

Beginner meaning:

Git does not yet know which remote branch this local branch should push to.

## 10. Similar Concepts Beginners Confuse

### Clone vs Pull

Clone is first-time copy. Pull updates an existing local repository.

### Commit vs Push

Commit saves locally. Push uploads to remote.

### Branch vs Folder Copy

Branch is Git-managed line of work. Folder copy is manual duplication.

### Merge vs Pull

Merge combines one branch into another. Pull downloads remote changes and integrates them.

## 11. Feature Branch Workflow

Typical safe workflow:

```powershell
git status
git switch main
git pull
git switch -c feature-rag-retriever
```

Make changes, then:

```powershell
git status
git add .
git commit -m "Add mock RAG retriever"
git push
```

Command explanation:

- `git status` checks current state.
- `git switch main` moves to stable branch.
- `git pull` gets latest remote work.
- `git switch -c feature-rag-retriever` creates and switches to feature branch.
- `git add .` stages changes.
- `git commit -m "..."` saves local checkpoint.
- `git push` uploads the branch/commits to remote.

Expected output summary:

- `git status` should tell you whether the working tree is clean or has changes.
- `git switch main` should say `Switched to branch 'main'`.
- `git pull` may say `Already up to date.` or show downloaded changes.
- `git switch -c feature-rag-retriever` should say it switched to a new branch.
- `git add .` usually prints no output.
- `git commit -m "Add mock RAG retriever"` should show a commit hash and changed file count.
- `git push` should show upload progress, or ask you to set upstream for a new branch.

How to verify:

```powershell
git log --oneline
git branch
```

Expected verification:

- `git log --oneline` shows your commit message.
- `git branch` shows the current branch with `*`.

## 12. Common Mistakes

- Pulling while local changes are uncommitted.
- Creating branches with unclear names like `test1`.
- Fixing conflict markers but forgetting to remove all marker lines.
- Pushing secrets in `.env`.
- Merging without running tests.
- Thinking `git pull` is the same as `git clone`.

## 13. Where Used In AI Engineer Work

Use branches for:

- adding FastAPI endpoints
- changing Pydantic schemas
- testing RAG chunking strategies
- adding Docker support
- updating Kubernetes YAML
- preparing final POC features

In interviews, you can say:

```text
I used feature branches to isolate changes, committed small checkpoints, and kept secrets out of Git using .gitignore.
```
