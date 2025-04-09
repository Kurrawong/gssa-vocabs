PREFIX : <https://linked.data.gov.au/def/mer-doc-types/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

INSERT {
    :legislation-and-guidance skos:member ?member
}
WHERE {
    :legislation-and-policy ^skos:broader+ ?member
}
