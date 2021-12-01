#!/bin/bash
# Simple Bash script to deploy the current developer branch to the lacebook
# container.
#
# This script is used by developers to push locally made changes to an already
# running Lacebook container.
#
# This script needs to be run in the root folder, eg:
# sh jupyter/devtools/deploy_to_container.sh
#
# Then inside the container select "reset runtime" and the new changes
# should be applied.

if [ ! -d "jupyter" ];
then
    echo "Unable to run, this needs to run in the root folder.";
    exit 1;
fi


if [ ! -f "jupyter/devtools/deploy_to_container.sh" ];
then
    echo "Unable to run, this needs to run in the root folder.";
    exit 1;
fi

echo "Deleting old remnants of developer updates."
docker exec  -u root lacebook bash -c "rm -rf /home/lacework/jup*"
echo "Adding the current code to the container"
docker cp jupyter lacebook:/home/lacework/jup

echo "Updating the source"
docker exec  lacebook bash -c "cd /home/lacework && source lacenv/bin/activate && tar cfvz jup.tgz jup && pip install --upgrade jup.tgz"

echo "If there wasn't any error, you can now restart the runtime inside the container."
