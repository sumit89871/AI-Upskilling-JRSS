# Git Interview Questions

## 1. What is Git?

Short answer:

Git is a version control system that tracks file changes over time.

Expanded explanation:

Git lets developers save checkpoints called commits. It helps compare changes, recover older versions, and work safely on branches.

Project example:

In the final AI QA Assistant POC, Git can track changes to `backend/main.py`, `Dockerfile`, RAG logic, and Streamlit UI files.

Common wrong answer:

"Git is GitHub."

Why wrong:

Git is the tool. GitHub is a hosting platform.

## 2. What is the difference between Git and GitHub?

Short answer:

Git is local version control. GitHub is an online platform for hosting Git repositories.

Expanded explanation:

You can commit locally with Git without using GitHub. GitHub becomes involved when you push commits to a remote repository.

Project example:

You can run `git commit -m "Add RAG helper"` locally. To share it online, you later run `git push`.

## 3. What is a repository?

Short answer:

A repository is a project folder tracked by Git.

Expanded explanation:

A local repository contains your files plus a hidden `.git` folder that stores history and branch information.

Project example:

`ai-engineer-jrss-reskilling-course` can be a Git repository.

## 4. What is `.git`?

Short answer:

`.git` is Git's hidden internal folder.

Expanded explanation:

It stores commit history, branches, configuration, and staging information. Do not edit or delete it manually.

Project example:

After `git init`, your POC folder gets a `.git` folder.

## 5. What is the difference between `git add` and `git commit`?

Short answer:

`git add` stages changes. `git commit` saves staged changes as a snapshot.

Expanded explanation:

`git add` does not permanently save history. It only prepares selected changes for the next commit. `git commit` records whatever is staged.

Project example:

If you modify `main.py`, run:

```powershell
git add main.py
git commit -m "Add health endpoint"
```

Command explanation:

- `git add main.py` stages only `main.py`.
- `git commit -m "Add health endpoint"` saves the staged change with a clear message.

Expected output:

```text
[main a1b2c3d] Add health endpoint
 1 file changed, 5 insertions(+)
```

Common wrong answer:

"git add saves the file."

Why incomplete:

Saving happens in the editor. `git add` stages changes for commit.

## 6. What does the dot mean in `git add .`?

Short answer:

The dot means current folder.

Expanded explanation:

`git add .` stages all changed files under the current folder. If you are in the project root, it stages project-wide changes.

Project example:

From the POC root, `git add .` can stage backend, frontend, Docker, and README changes.

Be careful:

It may also stage files you did not intend to commit.

## 7. What is staging?

Short answer:

Staging is selecting changes for the next commit.

Expanded explanation:

It lets you choose exactly what goes into the next snapshot instead of committing every edited file automatically.

Project example:

You can stage `backend/main.py` but leave experimental notes unstaged.

## 8. Tracked vs untracked file?

Short answer:

Tracked files are known to Git. Untracked files are new files Git has not started tracking.

Expanded explanation:

After creating `README.md`, Git sees it as untracked until you run `git add README.md` or `git add .`.

Project example:

A new `Dockerfile` appears as untracked until staged.

## 9. Staged vs unstaged changes?

Short answer:

Staged changes are selected for commit. Unstaged changes are edited but not selected yet.

Expanded explanation:

`git status` shows this difference clearly.

Project example:

If `main.py` is modified but not added, it is unstaged.

## 10. What is a commit?

Short answer:

A commit is a saved snapshot of staged changes.

Expanded explanation:

Each commit has a hash, author, date, message, and file changes.

Project example:

`Add mock RAG retriever` can be one commit.

## 11. What is a commit hash?

Short answer:

A commit hash is a unique ID for a commit.

Expanded explanation:

Git uses it to identify a specific point in history.

Project example:

`a1b2c3d Add README file` in `git log --oneline` shows a short hash and message.

## 12. What is `.gitignore`?

Short answer:

`.gitignore` tells Git which files or folders not to track.

Expanded explanation:

It protects generated files and secrets from being committed.

Project example:

```text
.env
.venv/
__pycache__/
```

## 13. What is a branch?

Short answer:

A branch is a separate line of work.

Expanded explanation:

Branches let you build features or experiments without changing stable code immediately.

Project example:

Create `feature-fastapi-endpoints` to add new API routes.

## 14. What is merge?

Short answer:

Merge combines changes from one branch into another.

Expanded explanation:

You usually merge a completed feature branch back into `main`.

Project example:

Merge `feature-rag-retriever` into `main` after testing.

## 15. What is a merge conflict?

Short answer:

A merge conflict happens when Git cannot automatically combine changes.

Expanded explanation:

It often happens when two branches edit the same line differently. You must manually choose the correct final content.

Project example:

Two developers edit the same README setup section.

## 16. Clone vs pull?

Short answer:

Clone copies a remote repository for the first time. Pull updates an existing local repository.

Expanded explanation:

Use `git clone` when you do not have the repo. Use `git pull` when you already have it.

## 17. Commit vs push?

Short answer:

Commit saves locally. Push uploads commits to remote.

Expanded explanation:

A commit can exist only on your machine until pushed.

Project example:

You commit the Dockerfile locally, then push so the team can see it.

## 18. Scenario: You changed `main.py`, but `git commit` says nothing to commit. Why?

Short answer:

The file may not be staged.

Expanded explanation:

Run `git status`. If the file is unstaged, run `git add main.py`, then commit.

## 19. Scenario: You accidentally see `.env` in `git status`. What should you do?

Short answer:

Do not commit it. Add `.env` to `.gitignore`.

Expanded explanation:

`.env` may contain secrets such as API keys. It should stay local.

## 20. How does Git help in an AI Engineer POC?

Short answer:

It tracks project changes and helps recover, collaborate, and explain progress.

Expanded explanation:

AI POCs change across prompts, APIs, RAG logic, Docker setup, and UI. Git keeps each meaningful step traceable.
