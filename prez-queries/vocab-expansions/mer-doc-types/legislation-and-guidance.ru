PREFIX : <https://linked.data.gov.au/def/mer-doc-types/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

INSERT {
    GRAPH ?graph {
        :legislation-and-guidance skos:member ?member
    }
}
WHERE {
    GRAPH ?graph {
        :legislation-and-policy ^skos:broader+ ?member
    }
}
