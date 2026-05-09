# Git Exercises

## Exercise 1: Create A Local Repository

### Task

Create a safe practice repository and initialize Git.

### Commands

```powershell
mkdir git-demo
cd git-demo
git init
git status
```

### Command Explanation

- `mkdir git-demo` creates a new folder named `git-demo`.
- `cd git-demo` moves the terminal into that folder.
- `git init` creates the hidden `.git` folder and starts Git tracking.
- `git status` shows what Git currently sees.

### Expected Result

`git init` should create a hidden `.git` folder.

`git status` should show something like:

```text
On branch main
No commits yet
nothing to commit
```

### Common Mistake

Running `git init` inside the wrong folder.

### Self-Check Question

What folder stores Git history?

## Exercise 2: Track Your First File

### Task

Create `README.md`, check status, stage it, and check status again.

### Commands

```powershell
echo "# Git Demo" > README.md
git status
git add .
git status
```

### Command Explanation

- `echo "# Git Demo" > README.md` writes text into a new file named `README.md`.
- first `git status` should show `README.md` as untracked.
- `git add .` stages all changes under the current folder.
- second `git status` confirms the file is staged.

### Expected Result

Before `git add`, `README.md` should appear under `Untracked files`.

After `git add`, it should appear under `Changes to be committed`.

### Common Mistake

Thinking file save and Git staging are the same thing.

### Self-Check Question

What does `git add .` do?

## Exercise 3: Create Your First Commit

### Task

Commit the staged README file.

### Commands

```powershell
git commit -m "Add README file"
git status
git log --oneline
```

### Command Explanation

- `git commit -m "Add README file"` saves staged changes with the message `Add README file`.
- `git status` checks whether anything is left uncommitted.
- `git log --oneline` shows compact commit history.

### Expected Result

`git status` should show:

```text
nothing to commit, working tree clean
```

`git log --oneline` should show one commit with your message.

### Common Mistake

Running `git commit` before `git add`.

### Self-Check Question

What does `-m` mean in `git commit -m`?

## Exercise 4: Modify A Tracked File

### Task

Edit `README.md`, then observe unstaged and staged status.

### Commands

```powershell
echo "This repo is for Git practice." >> README.md
git status
git add README.md
git status
git commit -m "Update README description"
```

### Command Explanation

- `>>` appends text to the existing `README.md` file.
- first `git status` shows the file as modified.
- `git add README.md` stages only that file.
- second `git status` confirms it is ready to commit.
- `git commit -m "Update README description"` saves the staged update.

### Expected Result

Before staging, Git should show `modified: README.md`.

After staging, Git should show it under `Changes to be committed`.

### Common Mistake

Using `git add .` without checking whether unrelated files are also staged.

### Self-Check Question

What is the difference between unstaged and staged?

## Exercise 5: Create A `.gitignore`

### Task

Prevent environment and generated files from being committed.

### File

Create `.gitignore` in the repository root:

```text
.venv/
.env
__pycache__/
*.pyc
```

### Commands

```powershell
git add .gitignore
git commit -m "Add Git ignore rules"
```

### Command Explanation

- `git add .gitignore` stages only the `.gitignore` file.
- `git commit -m "Add Git ignore rules"` saves the ignore rules into Git history.

### Expected Output

Commit output should mention one file changed.

### Expected Result

Git should track `.gitignore`, but ignore matching files.

### Common Mistake

Adding `.env` before creating `.gitignore`.

### Self-Check Question

Why should `.env` not be committed?

## Exercise 6: Branch Practice

### Task

Create a feature branch and commit a change on it.

### Commands

```powershell
git switch -c feature-notes
echo "Feature branch note" > feature.md
git add .
git commit -m "Add feature notes"
git branch
```

### Command Explanation

- `git switch -c feature-notes` creates and switches to a new branch.
- `echo "Feature branch note" > feature.md` creates a file.
- `git add .` stages the new file.
- `git commit -m "Add feature notes"` commits the file on the current branch.
- `git branch` lists branches so you can confirm where you are.

### Expected Result

`git branch` should show `feature-notes` with `*` next to it.

### Common Mistake

Creating a branch but forgetting to switch to it.

### Self-Check Question

What does the `*` mean in `git branch` output?

## Exercise 7: Explain The Full Flow

### Task

Write a short explanation of this flow:

```text
working folder -> staging area -> commit history -> remote repository
```

### Expected Result

You should be able to explain it without using the word "magic".

### Common Mistake

Saying `git add` saves history. It does not. It only stages changes.
