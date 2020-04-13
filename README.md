#Block-Chain

#####Install The Environment: <br/>

conda env create -f environment.yml

#####Create Node: <br/>

To create node you must see the constant.py file to make sure about the port. After that run ./sync_node.sh 8001 bash file and then a folder will create called block-chain8001 <br/>
If you want to define a new port and address, then declare it in constant.py <br/>

#####Syncing up the nodes :

> 1. Run node.py file form block-chain8001 folder and view the http://localhost:8001/blockchain endpoint to see that It doesn’t have any blocks for now.
> 2. Run the node.py from Parent node's (block-chain) folder 
> 3. Stop the block-chain8001's node.py file an run it again 
> 4. hit this url http://localhost:8001/blockchain and see the result