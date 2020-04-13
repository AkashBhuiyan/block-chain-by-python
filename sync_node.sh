#!/bin/bash

port=$1

if [ -z "$port" ] #if port isn't assigned
then
  echo Need to specify port number
  exit 1
fi

FILES=(block.py block_chain.py constant.py node.py sync.py transaction.py utils.py)

mkdir block-chain$port
for file in "${FILES[@]}"
do
  echo Syncing $file
  ln block-chain/$file block-chain$port/$file
done

echo Synced new block-chain folder for port $port

exit 1
