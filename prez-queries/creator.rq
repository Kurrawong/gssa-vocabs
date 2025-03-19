# The current version of Prez < v4 only recognises dcterms:creator.

PREFIX schema: <https://schema.org/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX dcat: <http://www.w3.org/ns/dcat#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX reg: <http://purl.org/linked-data/registry#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

INSERT {
  GRAPH ?graph {
    ?iri dcterms:creator ?creator 
  }
}
WHERE {
  GRAPH ?graph {
    VALUES ?class_type {
      skos:ConceptScheme
      skos:Collection
    }

    ?iri a ?class_type ;
         schema:creator ?creator .
    
    FILTER NOT EXISTS {
      ?iri dcterms:creator ?_creator
    }
  }
}
