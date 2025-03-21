# Prez < v4 requires dcterms:identifier. This is used as the unique identifier for the resource in this system and is shown in the URL as the slug.

PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX dcat: <http://www.w3.org/ns/dcat#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX reg: <http://purl.org/linked-data/registry#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

INSERT {
  GRAPH <https://prez.dev/systemGraph> {
    ?iri dcterms:identifier ?identifier 
  }
}
WHERE {
  {
    GRAPH ?graph {
      ?iri a skos:ConceptScheme .
      BIND(
        REPLACE(STR(?iri),
          "https://linked.data.gov.au/def/",
          "")
        AS ?_identifier
      )
      BIND(STRDT(?_identifier, xsd:token) AS ?identifier)
    }
  }
  UNION {
    GRAPH ?graph {
      ?iri a skos:Collection ;
         skos:inScheme ?scheme .
      BIND(
        REPLACE(STR(?iri),
          CONCAT(STR(?scheme), "/"),
          "")
        AS ?_identifier
      )
      BIND(STRDT(?_identifier, xsd:token) AS ?identifier)
    }
  }
  UNION {
    GRAPH ?graph {
      ?iri a skos:Concept ;
         skos:prefLabel ?_label .
      
      BIND(
        STR(
          REPLACE(
            REPLACE(
              LCASE(?_label), " " , "-"
            ),
            "/",
            "-"
          )
        ) AS ?_identifier
      )
      BIND(STRDT(?_identifier, xsd:token) AS ?identifier)
    }
  }
}
