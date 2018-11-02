## Motivating exercise

we want to publish our Python analysis module and we want
to keep history of changes so we can roll back to any previous version to
reproduce previous results, i.e. when we submitted a paper.

## Git setup

    git init
    git config --global user.name "Firstname Lastname"
    git config --global user.email "yourworkemail@youruniversity.edu"
    git config --global core.editor "notepad.exe" # for windows
    git config --global core.editor "nano" # for MAC and Linux

## Basic git commands

* `git init`: create a new repository in the current folder (initially no file is under version control)
* `git add FILENAME`: either add an untracked file to version control or put changes on a tracked file "in the shopping cart", ready to be written to history on the next commit
* `git status`: check what is modified, what is ready to be committed
* `git diff`: shows difference between the last version committed to the history and the current status of the files
* `git diff --staged`: shows the difference between the last version committed to the history just of the files that were added to the staging area (the "shopping cart")
* `git commit`: "buy" (opens editor to type commit message), writes a record in the history of the repository
* `git commit -m "Commit message"`: buy with short commit message written on the command line
* `git log`: show history

## Exploring history

go back and forth in history, `git checkout HEAD~1` goes back 1 commit, `git checkout HEAD~3` 3 commits, otherwise look for a specific commit hash in `git log` and use the first 5-6 characters like: `git checkout wer234` to go bac k to that specific version.

Consider that you should not make changes to the files in this state, it is only for exploration purposes, when you are done you should go back to the tip of the history with `git checkout master`.

## Github

open github account with same email used in git configuration
create a remote following the instructions on github

    git push origin master
    
will save all the new commits to Github.

make a change from the web interface, that changes nothing locally!
`git pull origin master` to syncronize.

Try another commit locally, push to github

Show different parts of the github GUI, show how research group in the area of the students use github for code or papers.

Create a new local copy of the repository with `git clone` by pasting the repository address from the right column of the repository homepage under "**HTTPS** clone URL".

## Conflicts

Make a commit on your original copy of the repository and push it to Github.
Now if in the other local copy you make a commit and try to push to Github `git` fails:

    To https://github.com/xxxxxxxxxxxxxxxxxxxxxxxxx
     ! [rejected]        master -> master (non-fast-forward)
    error: failed to push some refs to 'https://github.com/xxxxxxxxxxx.git'
    hint: Updates were rejected because the tip of your current branch is behind
    hint: its remote counterpart. Merge the remote changes (e.g. 'git pull')
    hint: before pushing again.
    hint: See the 'Note about fast-forwards' in 'git push --help' for details.

`git` prevents you to loose or overwrite history.

You first need to get the other changes from Github to your local copy with:

    git pull origin master
    
If changes are on different files or on different section of the same file `git`
generally is able to automatically merge them and then we can just push
our new changes with:

    git push origin master
    
Instead if we edited the very same lines `git` fails, we need then to open manually
the conflicting files, look for the lines with `======` characters, fix them, then:

    git add CONFLICTINGFILE
    git commit -m "Fixed conflict in CONFLICTINGFILE"
    git push origin master
