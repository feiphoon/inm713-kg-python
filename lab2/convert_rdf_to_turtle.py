"""
Task 2.3. Load your (or my) FOAF with RDFLib or Jena API.
• Print the triples.
• Convert the RDF/XML file into RDF/Turtle.
FOAF was an interesting project, but there are currently more recent efforts. For example,
Wikidata (https://www.wikidata.org/) is a community driven knowledge
graph including both manually and automatically created entries. Check my entry:
https://www.wikidata.org/wiki/Q56614973.


https://stackoverflow.com/questions/23520266/how-to-export-graph-in-rdf-file-using-rdflib
"""
import rdflib

g = rdflib.Graph()
g.parse("beatles.rdf", format="xml")

g.serialize(destination="beatles_new.ttl", format="turtle")
