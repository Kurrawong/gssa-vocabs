## How to update Fuseki

The vocabularies in this repository are uploaded to a Jena Fuseki instance (a triplestore database), which the Prez 
application uses to display the vocabularies on the web.

To update the vocabularies in Fuseki, you need to:
1. Clone or download this repo
2. Login to the Fuseki instance. During development this is at: https://gssa-fuseki-linux-web-app-dev.azurewebsites.net
3. You should see the "gssa" dataset. Click on the "Upload data" button.
4. Under "Dataset graph name" you must enter a valid graph name, i.e. a valid URI, for example "https://data-updates". It does not matter what the value is so long as it is valid. This step is required as Fuseki is configured to query the union of named graphs.
5. Click "Select files" and select all files within the "vocabularies" (except the json file), and 
"background-resources" directories of this repo. It is suggested but not required to upload these sets of files to two 
different named graphs (step 4), i.e. upload the first set of files, change the "Dataset graph name", then upload the 
second set.

## Automating updates

Updates to Fuseki can be automated through the use of Github Actions, Bitbucket Pipelines etc. This will not currently 
work from Github as the Fuseki instance is not publicly accessible.

Once the repo has been moved to its final location, automation could be reconsidered.

Using these kinds of automation for data updates is only advised for vocabularies as the volumes of data involved are 
relatively small.
