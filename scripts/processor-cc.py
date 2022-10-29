from rdflib import Graph, Literal, Namespace
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

g.bind("", Namespace("http://resource.geosciml.org/classifier/cgi/commodity-code/"))
g.bind("cs", Namespace("http://resource.geosciml.org/classifierscheme/cgi/2016.01/commodity-code"))
g.bind("eucc", Namespace("http://inspire.ec.europa.eu/codelist/CommodityCodeValue/"))

g.serialize(destination="vocabularies/commodity-code.sa.ttl", format="longturtle")
