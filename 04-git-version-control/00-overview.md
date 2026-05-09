# Git Overview

## 1. What Git Is

Git is a version control system.

Simple meaning:

```text
Git tracks changes in your project files over time.
```

Git helps you answer questions like:

- What changed since yesterday?
- Who changed this file?
- Which version was working before I broke it?
- Can I try a new feature without damaging the main code?
- Can I safely share my code with another developer?

Git works locally on your machine. You can use Git even if you never create a GitHub account.

## 2. The Most Important Beginner Idea

Git is not GitHub.

Keep this difference clear:

- **Git** is the tool installed on your computer.
- **GitHub** is a website/cloud platform where Git repositories can be stored and shared.

Simple comparison:

```text
Git = tracking tool
GitHub = online place to host/share Git repositories
```

Example:

You can run this locally:

```powershell
git init
git add .
git commit -m "Add first files"
```

Command purpose:

These commands create local Git history on your machine.

Where to run:

Run them from the root folder of a project.

Command breakdown:

- `git init` starts Git tracking in the current folder and creates a hidden `.git` folder.
- `git add .` stages all current changes under the current folder.
- `git commit -m "Add first files"` saves the staged changes into local Git history.
- `-m` means message.
- `"Add first files"` is the commit message.

Expected output:

For `git init`:

```text
Initialized empty Git repository in C:/path/project/.git/
```

For `git add .`:

```text
Usually no output when successful.
```

For `git commit -m "Add first files"`:

```text
[main (root-commit) a1b2c3d] Add first files
 1 file changed, 1 insertion(+)
```

How to verify:

```powershell
git status
git log --oneline
```

Expected verification:

- `git status` should show whether the working tree is clean.
- `git log --oneline` should show your commit message.

This saves history on your machine. Nothing has gone to GitHub yet.

To send commits to GitHub, you later use a remote and `git push`.

## 3. Why Git Matters

Without Git, beginners often manage files like this:

```text
project-final/
project-final-new/
project-final-latest/
project-final-working-copy/
```

This becomes confusing quickly.

With Git, you keep one project folder and Git stores history:

```text
project/
  README.md
  main.py
  Dockerfile
  .git/        <- Git history lives here
```

## 4. Git Mental Model

The most useful beginner mental model is:

```text
Working folder -> Staging area -> Commit history -> Remote repository
```

### Working Folder

This is the normal project folder you edit.

Example:

```text
ai-engineer-poc-qa-assistant/
  backend/main.py
  frontend/app.py
  README.md
```

When you edit `backend/main.py`, the change first exists only in your working folder.

### Staging Area

The staging area is a preparation area for the next commit.

Think of it like:

```text
Files I want included in the next saved checkpoint
```

You put files into the staging area with `git add`.

### Commit History

A commit is a saved checkpoint.

It records:

- file changes
- commit message
- author
- date/time
- unique commit hash

### Remote Repository

A remote repository is the shared online copy, such as GitHub.

Remote is optional at first. You can learn local Git before GitHub.

## 5. What Is A Repository?

A repository is a project folder tracked by Git.

There are two common types:

- **local repository**: on your computer
- **remote repository**: hosted online

Example local repository:

```text
C:\Users\Sumit\Desktop\AI_Test_Engineer_JRSS\ai-engineer-jrss-reskilling-course
```

Example remote repository:

```text
https://github.com/your-name/ai-engineer-jrss-reskilling-course
```

## 6. What Is `.git`?

When you run:

```powershell
git init
```

Git creates a hidden folder named `.git`.

Command purpose:

Start Git tracking in the current folder.

Expected output:

```text
Initialized empty Git repository in C:/path/project/.git/
```

How to verify:

```powershell
git status
```

Expected verification output may include:

```text
On branch main
No commits yet
```

That folder stores Git's internal information:

- commit history
- branch information
- configuration
- staging information
- references to current branch and commits

Why hidden?

Because normal developers should not edit it manually. It is Git's internal storage.

Important:

Do not delete `.git` unless you intentionally want to remove Git history from the project.

If you delete `.git`, your files may still remain, but the Git history is gone.

## 7. Similar Concepts Beginners Confuse

### Git vs GitHub

Git tracks changes locally. GitHub hosts repositories online.

### Commit vs Push

Commit saves changes in local Git history. Push uploads commits to remote.

### Working Folder vs Repository

The working folder is where your files are. It becomes a Git repository when it contains `.git`.

### Save File vs Commit

Saving a file writes changes to disk. Committing saves a Git snapshot in history.

## 8. Quick Practice

Answer these before moving on:

1. Can Git work without GitHub?
2. What does `.git` store?
3. What is the difference between a saved file and a committed file?
4. Why is the staging area useful?
5. What does remote repository mean?

## 9. Common Mistakes

- Thinking GitHub and Git are the same thing.
- Thinking commit uploads code to GitHub.
- Deleting `.git` because it looks unnecessary.
- Running `git init` inside a random subfolder.
- Committing secrets such as `.env`.

## 10. Where Used In AI Engineer Work

Git appears when you:

- save FastAPI endpoint changes
- version prompt templates
- compare RAG retrieval experiments
- track Dockerfile updates
- collaborate on a final POC
- recover after breaking code
- show project progress in an interview
