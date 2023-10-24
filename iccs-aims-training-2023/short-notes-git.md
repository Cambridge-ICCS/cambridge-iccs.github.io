# Cheat-sheet on 'Using Git and GitHub effectively' by Tom Meltzer (notes by Dominic Orchard)

## Using git on the command line and some interesting advanced features

- `git log` - Gives you the log of your commits.
    - Pressing `Shift+G` then takes you to the earliest commit (last in the log and hence oldest commit)
    - `git log --oneline` gives you a more concise view with shorter hashes.

- The `.gitconfig` file in your home directory provides a way to make
command line aliases if you want to make shorter commands for git (see
[here](https://www.atlassian.com/git/tutorials/git-alias) for more info).

- Commits give you a snapshot in time with a 'hash' (a large hexadecimal
number).

- `git checkout <hash>` where `<hash>` comes from the log (e.g.
`9e3e42171cdd47f136e3f55d7c4c3957c6b4d970`, or they can be shorter `5691c3e8132`).

- `git checkout main` goes to the main branch

- `git bisect` let's you do a binary search through the commit
history to find when a change introduced a problem (e.g., making
a test fail) (Therefore you can find the problem in `log_2 n` where `n` is the number of commits, rather than going through sequentially) Really useful if you get a bug and not sure when it was introduced.

  - To start: `git bisect start`
  - Then give snapshot where it fails `git bisect bad` (marks current commit as failing), or `git bisect bad <hash>` for a particular commit.
  - `git bisect good <hash>` which one is good.
  - `git bisect run ./test.sh` then tells git bisect which script to run to determine whether the code is 'good' or 'bad'. `test.sh` needs to provide a 0 error code for success and something non-0 for fail (Lookup how to produce error codes in your language).
  - This will show you the first commit where `test.sh` fails and leaves you at the commit which was bad.

- `git diff` let's you see what has changed. You can give it a hash
to compare the current commit against another that was good (e.g.,
the preceding one) e.g., `git diff <good-commit>`

## GitHub intro

- Continuous integration: automated way to test code. On GitHub make a folder
`.github/workflows` (https://docs.github.com/en/actions/using-workflows).

- Tom showed us a setup that when a commit is made to GitHub, it
automatically sets up an environment for the code, installs it, and
runs the tests.

- Issue trackers on open projects allows us to collaborate with us. We saw
an example of a collaborative interaction with developers of another project.

## Interactive, exercise time

- https://github.com/TomMelt/git-bisect-demo

- Showed how to connect an existing repository locally with the remote one on github.
GitHub gives you the instructions:

- `git remote add origin git@github.com:TomMelt/git/bisect-demo.git`
- `git branch -M main`
- `git push -u origin main` Sends it to the remote server, after you've done this once you can do `git push`

- Software Carpentry provide free online learning resources. For their git course please head to https://swcarpentry.github.io/git-novice
