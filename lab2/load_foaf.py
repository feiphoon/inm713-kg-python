"""
Task 2.3. Load your (or my) FOAF with RDFLib or Jena API.
• Print the triples.
• Convert the RDF/XML file into RDF/Turtle.
FOAF was an interesting project, but there are currently more recent efforts. For example,
Wikidata (https://www.wikidata.org/) is a community driven knowledge
graph including both manually and automatically created entries. Check my entry:
https://www.wikidata.org/wiki/Q56614973.

"""

import rdflib
from rdflib.namespace import FOAF, XSD


g = rdflib.Graph()
# g.load('http://dbpedia.org/resource/Semantic_Web')


g.add((
    rdflib.URIRef("https://sws.ifi.uio.no/vocab/ernesto_foaf.rdf"),
    FOAF.givenName,
    rdflib.Literal("Prof", datatype=XSD.string)
))

for s, p, o in g:
    print(s, p, o)

g.bind("foaf", FOAF)
g.bind("xsd", XSD)
# https://sws.ifi.uio.no/vocab/ernesto_foaf.rdf http://xmlns.com/foaf/0.1/givenName Prof

print(g.serialize(format="turtle"))
# b'@prefix foaf: <http://xmlns.com/foaf/0.1/> .\n@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n\n<https://sws.ifi.uio.no/vocab/ernesto_foaf.rdf> foaf:givenName "Prof"^^xsd:string .\n\n'