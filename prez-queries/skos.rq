# Materialise the labels for vocabs

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
    ?iri rdfs:label ?label 
  }
}
WHERE {
  GRAPH ?graph {
    VALUES ?class_type {
      skos:ConceptScheme
      skos:Collection
      skos:Concept
    }

    ?iri a ?class_type ;
         skos:prefLabel ?label .
    
    FILTER NOT EXISTS {
      ?iri rdfs:label ?label
    }
  }
}
