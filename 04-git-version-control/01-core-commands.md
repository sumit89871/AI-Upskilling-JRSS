# Git Core Commands

## 1. What Git Is

Git is a version control system.

That means Git tracks changes in project files and lets you save meaningful snapshots over time.

Git helps you:

- track what changed
- save checkpoints
- compare versions
- recover older working code
- work safely on branches
- collaborate with others

Git works locally before GitHub is involved.

## 2. The Most Important Beginner Idea

Git is not GitHub.

- Git = tool on your machine.
- GitHub = online hosting/sharing platform.

When you run:

```powershell
git commit -m "Add health endpoint"
```

you save a checkpoint locally.

Command breakdown:

- `git` uses the Git tool.
- `commit` saves staged changes into local history.
- `-m` means message.
- `"Add health endpoint"` is the message describing the change.

Expected output:

```text
[main a1b2c3d] Add health endpoint
 1 file changed, 5 insertions(+)
```

That does not upload anything to GitHub yet.

Upload happens later with:

```powershell
git push
```

Command breakdown:

- `git` uses the Git tool.
- `push` uploads local commits to the configured remote repository.

Expected output:

```text
Writing objects: 100%
To https://github.com/example/repo.git
```

If no remote is configured, Git may show an error instead.

## 3. Git Mental Model

```text
Working folder -> Staging area -> Commit history -> Remote repository
```

### Working Folder

The folder you are editing now.

Example:

```text
my-fastapi-app/
  main.py
  README.md
```

### Staging Area

The preparation area for the next commit.

You choose files for the next snapshot using `git add`.

### Commit History

Saved snapshots of staged changes.

Each commit has:

- hash
- author
- date
- message
- file changes

### Remote Repository

Online copy such as GitHub, GitLab, or Azure DevOps.

## 4. What Is A Repository?

A repository is a project folder tracked by Git.

Local repository:

```text
Your computer folder + hidden .git folder
```

Remote repository:

```text
Online hosted Git repository
```

You create a local repository with `git init`.

You copy a remote repository with `git clone`.

## 5. What Is `.git`?

`.git` is a hidden folder Git creates inside a repository.

It stores:

- commit history
- branch information
- Git configuration
- staging data
- internal references

You normally do not edit `.git` manually.

If `.git` is deleted, your visible project files may remain, but Git history and branch data are removed.

## 6. Command 1: `git init`

Command:

```powershell
git init
```

Plain English meaning:

```text
Start tracking this folder as a Git repository.
```

Where to run it:

Run it from the root folder of a new project.

Example:

```powershell
cd C:\Users\Sumit\Desktop\my-ai-project
git init
```

Command parts:

- `cd C:\Users\Sumit\Desktop\my-ai-project` moves the terminal into the project folder.
- `git` means use the Git tool.
- `init` means initialize.
- together, `git init` creates Git tracking in the current folder.

What it creates:

```text
.git/
```

Expected output:

```text
Initialized empty Git repository in C:/Users/Sumit/Desktop/my-ai-project/.git/
```

How to verify:

```powershell
git status
```

Common mistake:

Running `git init` inside the wrong folder.

Example wrong location:

```text
my-ai-project/backend/temporary-test/
```

That would make only the temporary folder a repository, not your full project.

What happens if skipped:

Git commands like `git status` may show:

```text
fatal: not a git repository
```

## 7. Command 2: `git status`

Command:

```powershell
git status
```

Plain English meaning:

```text
Show what Git sees right now.
```

Use it often. It is the safest Git command.

It tells you:

- current branch
- untracked files
- modified files
- staged files
- whether there is anything to commit

### Before Creating Any File

Possible output:

```text
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

Meaning:

- `On branch main` means you are currently on the main branch.
- `No commits yet` means no snapshot exists.
- `nothing to commit` means Git sees no file changes.

### After Creating `README.md`

Possible output:

```text
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present
```

Meaning:

- `Untracked files` means Git sees the file but is not tracking it yet.
- `README.md` is visible to Git but not staged.
- `nothing added to commit` means staging area is empty.

### After Running `git add .`

Possible output:

```text
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md
```

Meaning:

- `Changes to be committed` means the file is staged.
- `new file` means Git will include this file in the next commit.

### After Commit

Possible output:

```text
On branch main
nothing to commit, working tree clean
```

Meaning:

- Git has no unsaved changes.
- Your working folder matches the latest commit.

### Tracked vs Untracked

Tracked file:

```text
Git already knows this file.
```

Untracked file:

```text
Git sees this file but it has not been added to tracking.
```

### Staged vs Unstaged

Staged:

```text
Selected for next commit.
```

Unstaged:

```text
Changed in working folder but not selected for next commit.
```

## 8. Command 3: `git add .`

Command:

```powershell
git add .
```

Plain English meaning:

```text
Stage all changes under the current folder for the next commit.
```

Command parts:

- `git` means use Git.
- `add` means stage file changes.
- `.` means current folder.

The dot is important.

```text
. = current directory
```

If you are in the project root, `git add .` stages changes in the whole project.

If you are inside a subfolder, it stages changes under that subfolder.

### What Is Staging?

Staging is choosing what goes into the next snapshot.

Imagine you changed three files:

```text
main.py
README.md
.env
```

You may want to commit `main.py` and `README.md`, but not `.env`.

That is why staging exists.

### `git add .` vs `git add README.md`

```powershell
git add .
```

Stages all changes under current folder.

```powershell
git add README.md
```

Stages only `README.md`.

Be careful:

`git add .` can accidentally stage `.env`, generated files, or files you did not intend to commit. Use `.gitignore` and check `git status`.

Expected output:

Usually no output if successful.

How to verify:

```powershell
git status
```

Look for:

```text
Changes to be committed
```

What happens if skipped:

If you run commit without staging, Git may say:

```text
no changes added to commit
```

## 9. Command 4: `git commit -m "message"`

Command:

```powershell
git commit -m "Add README file"
```

Plain English meaning:

```text
Save staged changes as a checkpoint with a message.
```

Command parts:

- `git` means use Git.
- `commit` means save staged changes into Git history.
- `-m` means message.
- `"Add README file"` is the commit message.

### What Is A Commit?

A commit is a snapshot of staged changes.

It does not save every file on your computer. It saves the changes you staged.

### Why Commit Message Matters

Good commit message:

```text
Add FastAPI health endpoint
```

Bad commit message:

```text
update
```

Good messages help future you and reviewers understand what changed.

Expected output:

```text
[main (root-commit) a1b2c3d] Add README file
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
```

Meaning:

- `main` is the branch.
- `root-commit` means first commit in this repository.
- `a1b2c3d` is a short commit hash.
- `1 file changed` summarizes file changes.
- `create mode` means a new file was added.

What happens if nothing is staged:

```text
nothing to commit, working tree clean
```

or:

```text
no changes added to commit
```

How to verify:

```powershell
git log --oneline
```

## 10. Command 5: `git log`

Command:

```powershell
git log
```

Plain English meaning:

```text
Show commit history.
```

Expected output:

```text
commit a1b2c3d4e5f6...
Author: Sumit <sumit@example.com>
Date:   Fri May 8 15:20:00 2026 +0530

    Add README file
```

Meaning:

- `commit` line shows the commit hash.
- commit hash is a unique ID for the commit.
- `Author` shows who made the commit.
- `Date` shows when it was made.
- message explains what changed.

Short version:

```powershell
git log --oneline
```

Expected output:

```text
a1b2c3d Add README file
```

If `git log` opens a scroll screen, press:

```text
q
```

`q` exits the log viewer.

## 11. Full Beginner Flow

Run these commands in a safe practice location, not inside an important repo:

```powershell
mkdir git-demo
cd git-demo
git init
echo "# Git Demo" > README.md
git status
git add .
git status
git commit -m "Add README file"
git status
git log --oneline
```

What this full command block does:

It creates a new practice folder, initializes Git, creates a README file, stages it, commits it, and then checks history.

Expected output summary:

- `mkdir git-demo` usually prints no output if the folder is created.
- `cd git-demo` usually prints no output; your prompt location changes.
- `git init` prints `Initialized empty Git repository...`.
- `echo "# Git Demo" > README.md` usually prints no output; it creates the file.
- first `git status` shows `README.md` as untracked.
- `git add .` usually prints no output.
- second `git status` shows `README.md` under `Changes to be committed`.
- `git commit -m "Add README file"` prints a commit hash and file-change summary.
- final `git status` shows `nothing to commit, working tree clean`.
- `git log --oneline` shows the commit hash and message.

### `mkdir git-demo`

Creates a folder named `git-demo`.

### `cd git-demo`

Moves your terminal into that folder.

### `git init`

Creates `.git` and makes this folder a Git repository.

### `echo "# Git Demo" > README.md`

Creates a file named `README.md` with one line of text.

Command parts:

- `echo "# Git Demo"` prints text.
- `>` writes that text into a file.
- `README.md` is the file name.

### `git status`

Shows `README.md` as untracked.

### `git add .`

Stages `README.md`.

### Second `git status`

Shows `README.md` under `Changes to be committed`.

### `git commit -m "Add README file"`

Creates a commit.

### Final `git status`

Shows working tree clean.

### `git log --oneline`

Shows the commit history in one-line format.

## 12. Common Mistakes

### Running `git init` In The Wrong Folder

Always check:

```powershell
Get-Location
```

before `git init`.

Command purpose:

Show the current terminal folder.

Expected output:

```text
Path
----
C:\Users\Sumit\Desktop\my-ai-project
```

Use this to confirm you are in the correct project root before creating `.git`.

### Forgetting `git add`

Commit only saves staged changes.

If you forget `git add`, your commit may contain nothing.

### Vague Commit Messages

Avoid:

```text
changes
final
update
```

Prefer:

```text
Add mock RAG retriever
Fix FastAPI validation error
Document Docker run steps
```

### Committing `.venv`

`.venv` can contain thousands of dependency files. Do not commit it.

Add to `.gitignore`:

```text
.venv/
```

### Committing `.env`

`.env` may contain API keys. Do not commit it.

Add to `.gitignore`:

```text
.env
```

### Deleting `.git`

Do not delete `.git` unless you intentionally want to remove repository history.

### Thinking Commit Means Upload

Commit is local.

Push uploads to remote.

### Thinking Push And Commit Are Same

They are different:

- `commit`: save local snapshot
- `push`: upload commits to remote

## 13. Similar Concepts Beginners Confuse

### `git add` vs `git commit`

`git add` stages changes. `git commit` saves staged changes into history.

### Tracked vs Untracked

Tracked files are known to Git. Untracked files are new files Git sees but does not track yet.

### Staged vs Unstaged

Staged changes are ready for commit. Unstaged changes are edited but not selected for commit.

### Commit vs Push

Commit saves locally. Push uploads to remote.

### Local Repo vs Remote Repo

Local repo is on your machine. Remote repo is hosted online.

## 14. Where Used In AI Engineer Work

You will use these commands when:

- saving FastAPI project changes
- versioning RAG chunking experiments
- tracking prompt template improvements
- saving Dockerfile edits
- committing Kubernetes YAML
- collaborating on the final POC
- rolling back after breaking code
- explaining your project timeline in an interview
