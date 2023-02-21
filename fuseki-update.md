## How to update Fuseki

The vocabularies in this repository are uploaded to a Jena Fuseki instance (a triplestore database), which the Prez 
application uses to display the vocabularies on the web.

To update the vocabularies in Fuseki, you need to:
1. Clone or download this repo
2. Login to the Fuseki instance. During development this is at: https://gssa-fuseki-linux-web-app-dev.azurewebsites.net
3. Click on the "info" button under "actions" for the gssa dataset
4. Click "count triples in all graphs"
5. Make a note of any graph names that you are going to update. A map of graph to file names is in this repo under 'vocabularies/index.json'
6. Drop the graphs that you are going to update:
   1. Click on 'query'
   2. Under 'SPARQL Endpoint', change '/gssa/query' to '/gssa/update'
   3. Enter update queries of the form:
   `DROP GRAPH <my-graph-name>`
   You should get an "Update succeeded" message for each graph that you drop.
7. Go to the 'add data' tab
8. For each file/graph that has been updated:
   1. Enter the graph name in 'Dataset graph name'
   2. Click 'Select files'
   3. Select the relevant file (mappings from graph to filenames are in `vocabularies/index.json`)
   4. Click 'upload now' or 'upload all'.
   There should only be one vocabulary file per graph.
9. Repeat steps 6-8 for the background resources (in the 'background-resources' directory of this repo). You can add all of the background resources 

## Automating updates

Updates to Fuseki can be automated through the use of Github Actions, Bitbucket Pipelines etc. This will not currently 
work from Github as the Fuseki instance is not publicly accessible.

Once the repo has been moved to its final location, automation could be reconsidered.

Using these kinds of automation for data updates is only advised for vocabularies as the volumes of data involved are 
relatively small.
