# Materialise the derivation mode for vocabs
# Prior to Prez v4, it requires the use of dcat:hadRole instead of prov:hadRole

PREFIX schema: <https://schema.org/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX dcat: <http://www.w3.org/ns/dcat#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX reg: <http://purl.org/linked-data/registry#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

INSERT {
  GRAPH <https://prez.dev/systemGraph> {
    ?qd dcat:hadRole ?role .
  }
}
WHERE {
  GRAPH ?graph {
    VALUES ?class_type {
      skos:ConceptScheme
    }

    ?iri a ?class_type ;
         prov:qualifiedDerivation ?qd .
    
    ?qd prov:hadRole ?role .
  }

  FILTER NOT EXISTS {
    ?iri prov:qualifiedDerivation ?qd ;
         dcat:hadRole ?role .
  }
}
