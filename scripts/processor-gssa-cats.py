from rdflib import Graph, URIRef, Literal
from rdflib.namespace import DCTERMS, RDF, RDFS, SKOS, XSD

g = Graph(bind_namespaces="rdflib").parse("../source/mer-cats-2.ttl")

concepts = {}
for c in g.subjects(RDF.type, SKOS.Concept):
    id = str(c).split("/")[-1]
    g.add((c, DCTERMS.identifier, Literal(id, datatype=XSD.token)))

    g.add((c, SKOS.definition, g.value(c, SKOS.prefLabel)))

    if "mer-categories" in str(c):
        g.add((c, RDFS.isDefinedBy, URIRef("https://linked.data.gov.au/def/mer-categories")))
        g.add((c, DCTERMS.provenance, Literal("Created by MER for this vocabulary")))
    else:
        g.add((c, RDFS.isDefinedBy, URIRef("https://linked.data.gov.au/def/anzsrc-for/2020")))
        g.add((c, DCTERMS.source, Literal("https://linked.data.gov.au/def/anzsrc-for/2020", datatype=XSD.anyURI)))


g.parse(
    data='''
        PREFIX cs: <https://linked.data.gov.au/def/mer-categories>
        PREFIX dcterms: <http://purl.org/dc/terms/>
        PREFIX for: <https://linked.data.gov.au/def/anzsrc-for/2020/>
        PREFIX mercat: <https://linked.data.gov.au/def/mer-categories/>
        PREFIX agldwgstatus: <https://linked.data.gov.au/def/reg-statuses/>        
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX reg: <http://purl.org/linked-data/registry#>
        PREFIX sdo: <https://schema.org/>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    
        cs:
            a skos:ConceptScheme ;
            dcterms:identifier "gssa-categories"^^xsd:token ;
            skos:prefLabel "South Australian Minerals and Energy Resources Categories"@en ;
            dcterms:created "2021-09-14"^^xsd:date ;
            dcterms:creator <https://linked.data.gov.au/org/gssa> ;
            dcterms:identifier "gssa-categories"^^xsd:token ;
            dcterms:license <https://purl.org/NET/rdflicense/cc-by4.0> ;
            dcterms:modified "2022-11-22"^^xsd:date ;
            dcterms:published "2022-11-01"^^xsd:date ;
            dcterms:publisher <https://linked.data.gov.au/org/gssa> ;
            dcterms:rights "© Department for Energy and Mining, 2022" ;
            dcterms:source "https://linked.data.gov.au/def/anzsrc-for"^^xsd:anyURI ;
            reg:status agldwgstatus:experimental ;
            skos:definition """Categories of data used by South Australian Minerals and Energy Resources.
        
        These categories are mostly the Australian/New Zealand Fields of Research (ANZSRC FoR) 2020 codes but with fine-grained additions in MER's areas of interest and excluding many codes in unrelated areas."""@en ;
        skos:hasTopConcept
            for:31 ,
            for:33 ,
            for:37 ,
            for:40 ,
            for:41 ,
            for:4407 ,
            gssacat:cultural-understanding ,
            gssacat:energy ,
            for:43 ,
            for:46 ,
            gssacat:mineral-resources-exc-energy-resources ;          
        .
        
        <https://linked.data.gov.au/org/gssa>
            a sdo:Organization ;
            sdo:name "SA Minerals & Energy Resources" ;
            sdo:url "https://www.energymining.sa.gov.au/industry/geological-survey"^^xsd:anyURI ;
        .
        ''',
    format="turtle"
)

g.serialize(destination="../vocabularies/gssa-categories.ttl", format="longturtle")
