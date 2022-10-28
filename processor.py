from rdflib import Graph, Literal
from rdflib.namespace import RDF, SKOS


g = Graph().parse("source/commodity-codes.ttl")
for s, o in g.subject_objects(SKOS.altLabel):
    if isinstance(o, Literal):
        if o.language != "en":
            g.remove((s, SKOS.altLabel, o))

for s, o in g.subject_objects(SKOS.prefLabel):
    if isinstance(o, Literal):
        if o.language != "en":
            g.remove((s, SKOS.prefLabel, o))


g.serialize(destination="vocabularies/commodity-code.sa.ttl", format="longturtle")
