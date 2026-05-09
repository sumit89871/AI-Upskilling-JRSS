# Git Cheatsheet

## git status

Meaning: Show current working tree state.

Use when: Before and after staging or committing.

Example: `git status`

Be careful: Read untracked, modified, staged, and branch messages.

## git add .

Meaning: Stage all changes under current folder.

Use when: Preparing changes for next commit.

Example: `git add .`

Be careful: It may stage files you did not intend. Check `git status`.

## git commit -m "message"

Meaning: Save staged changes as a commit with a message.

Use when: You have a meaningful checkpoint.

Example: `git commit -m "Add health endpoint"`

Be careful: Commit is local until pushed.

## git push

Meaning: Upload local commits to remote repository.

Use when: Sharing work.

Example: `git push origin main`

Be careful: Commit before push.
