from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import DCTERMS, RDF, RDFS, SKOS, XSD

REG = Namespace("http://purl.org/linked-data/registry#")

g = Graph(bind_namespaces="rdflib").parse("../background-resources/for2020.ttl")

for s in g.subjects(RDF.type, SKOS.Concept):
    g.add((s, REG.status, URIRef("http://def.isotc211.org/iso19135/-1/2015/CoreModel/code/RE_ItemStatus/original")))

g.bind("reg", REG)
g.bind("isostatus", Namespace("http://def.isotc211.org/iso19135/-1/2015/CoreModel/code/RE_ItemStatus/"))
g.serialize(destination="../background-resources/for2020.x.ttl", format="longturtle")
