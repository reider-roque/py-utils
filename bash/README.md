Description
-----------

Each file in this directory is a library with one or more bash funcitons

1. `colorio.sh` - a set of functions for colorized printing in bash shell.
4. `whatshell.sh` - a function used to differenciate between login and interactive shells.
5. `activate_virtualenv.sh` - a funciton that brings convenience of using `activate project` command instead of `source project/bin/activate` with Python's *virtualenv* package. To use it with interactive login shell place the script to */etc/profile.d/* directory (no need to make it executable). To use it with interactive non-login shell either append the contents of the file to the *~/.bashrc* file or do the following:

```bash
mkdir ~/.bashrc.d
mv activate_virtualenv.sh ~/.bashrc.d/
vim ~/.bashrc
    # Append the following lines at the end of ~/.bashrc
    if [ -d ~/.bashrc.d ]; then
        for i in ~/.bashrc.d/*.sh; do
            if [ -r $i ]; then
                . $i
            fi
        done
        unset i
    fi
# Reopen your interfactive non-login shell

# The above setup will have ~/.bashrc.d/ directory behave for the non-login interactive
# shells the same way /etc/profile.d/ directory behaves for login interactive shell.
```
