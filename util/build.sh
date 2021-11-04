#!/bin/bash

# Remove the current build artefacts.
rm -r dist

# Get the version from Git and format as "{tag}.{commits}g{hash}", where {tag} 
# is the current tag, and will be a 'major.minor' version number in its own
# right, {commits} is the number of commits we are ahead of {tag}, and {hash} is
# the current commit's hash. Note that when run on a tagged commit, we just get
# "{tag}".
ver=`git describe --always --tags \
    | sed 's/\(.*\)\.\(.*\)-\(.*\)-\(.*\)/\1.\2.\3+\4/'`

# Make the version file.
echo "VERSION = \"${ver}\"" > brace_expand/version.py

# Build the source archive and distro.
python -m build

# Remove the .egg-info that was produced during the build to test it.
rm -r brace_expand.egg-info
