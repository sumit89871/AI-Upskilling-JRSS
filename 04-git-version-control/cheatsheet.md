# Git Cheatsheet

## `git init`

Meaning:

Start tracking the current folder as a Git repository.

Use when:

You are starting a new local project.

Example:

```powershell
git init
```

Expected output:

```text
Initialized empty Git repository in C:/path/project/.git/
```

Verify with:

```powershell
git status
```

Be careful:

Run it from the project root, not a random subfolder.

## `git status`

Meaning:

Show current Git state.

Use when:

Before and after every Git action.

Example:

```powershell
git status
```

Expected output examples:

```text
Untracked files:
  README.md
```

or:

```text
nothing to commit, working tree clean
```

Be careful:

Read whether files are untracked, unstaged, or staged.

## `git add .`

Meaning:

Stage all changes under the current folder.

Use when:

You want all current changes included in the next commit.

Example:

```powershell
git add .
```

Expected output:

```text
Usually no output when successful.
```

Verify with:

```powershell
git status
```

Look for:

```text
Changes to be committed
```

Be careful:

It may stage files you did not intend to commit. Check `git status`.

## `git add README.md`

Meaning:

Stage one specific file.

Use when:

You want controlled staging.

Example:

```powershell
git add README.md
```

Expected output:

```text
Usually no output when successful.
```

Verify with `git status`.

Be careful:

Only that file is staged.

## `git commit -m "message"`

Meaning:

Save staged changes as a local snapshot.

Use when:

You have staged meaningful changes.

Example:

```powershell
git commit -m "Add FastAPI health endpoint"
```

Expected output:

```text
[main a1b2c3d] Add FastAPI health endpoint
 1 file changed, 5 insertions(+)
```

Be careful:

Commit does not upload to GitHub.

## `git log --oneline`

Meaning:

Show compact commit history.

Use when:

You want to inspect previous commits.

Example:

```powershell
git log --oneline
```

Expected output:

```text
a1b2c3d Add FastAPI health endpoint
```

Be careful:

In full `git log`, press `q` to exit the viewer.

## `.gitignore`

Meaning:

Tells Git which files/folders to ignore.

Use when:

You want to avoid tracking secrets, environments, and generated files.

Example:

```text
.env
.venv/
__pycache__/
```

Be careful:

If a file was already committed, adding it to `.gitignore` later does not automatically remove it from history.

## `git branch`

Meaning:

List branches or create a branch.

Example:

```powershell
git branch
git branch feature-api
```

Expected output:

- `git branch` lists branches and marks the current branch with `*`.
- `git branch feature-api` usually prints no output if successful.

Verify with:

```powershell
git branch
```

Be careful:

Creating a branch does not switch to it.

## `git switch`

Meaning:

Move to another branch.

Example:

```powershell
git switch feature-api
git switch -c feature-rag
```

Expected output:

```text
Switched to branch 'feature-api'
```

or:

```text
Switched to a new branch 'feature-rag'
```

Be careful:

Commit or handle local changes before switching if Git warns you.

## `git clone`

Meaning:

Copy a remote repository to your machine.

Example:

```powershell
git clone https://github.com/example/repo.git
```

Expected output:

```text
Cloning into 'repo'...
Receiving objects: 100%
```

Use when:

You do not have the project locally yet.

## `git pull`

Meaning:

Download and integrate remote changes.

Use when:

You already have the repo and need latest updates.

Example:

```powershell
git pull
```

Expected output:

```text
Already up to date.
```

or a downloaded changes summary.

## `git push`

Meaning:

Upload local commits to remote.

Use when:

You committed changes locally and want to share them.

Example:

```powershell
git push
```

Expected output:

```text
Writing objects: 100%
To https://github.com/example/repo.git
```
