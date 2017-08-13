#!/bin/bash

echo "Replicating to Dropbox folder"
cp -r ../VortexDynamics /home/christian/Dropbox/Dissertation/python/
cd /home/christian/Dropbox/Dissertation/python/VortexDynamics
echo "Removing repository and deployment script"
rm -rf .git
rm .gitignore
rm deploy.sh
echo "Done."

