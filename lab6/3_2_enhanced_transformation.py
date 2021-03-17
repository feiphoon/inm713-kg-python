"""
Task 3: Convert the CSV file intro triples (i.e., into 4 * data) using the vocabulary of the
defined ontology (e.g., ex:City). Create fresh entity URIs for the cities and countries
(e.g., http://example.org/New_York).
"""
from owlready2 import *
from onto_access import OntologyAccess
import pandas as pd

from rdflib import Graph
from rdflib import URIRef, BNode, Literal
from rdflib import Namespace
from rdflib.namespace import OWL, RDF, RDFS, XSD
# from rdflib.util import guess_format

# from stringcmp import isub
# from lookup import DBpediaLookup

# import owlrl



def load_csv(file):
    data_frame = pd.read_csv(file, sep=',', quotechar='"',escapechar="\\", nrows=1)
    # for row in data_frame.itertuples(index=True, name="Pandas"):
    #     print(row)
    return data_frame


def load_classes(uri_onto):
    onto_access = OntologyAccess(uri_onto)
    onto_access.loadOntology(True)

    results = onto_access.getClasses()

    for r in results:
        print(r)

def load_object_properties(uri_onto):
    onto_access = OntologyAccess(uri_onto)
    onto_access.loadOntology(True)

    results = onto_access.getObjectProperties()

    for r in results:
        print(r)


def load_data_properties(uri_onto):
    onto_access = OntologyAccess(uri_onto)
    onto_access.loadOntology(True)

    results = onto_access.getDataProperties()

    for r in results:
        print(r)


def load_individuals(uri_onto):
    onto_access = OntologyAccess(uri_onto)
    onto_access.loadOntology(True)

    results = onto_access.getIndividuals()

    for r in results:
        print(r)


world_cities_df = load_csv("data/worldcities-free-100.csv")

# Load ontology
# urionto = "world-cities-fei-ontology.owl"
# load_classes(urionto)
# load_object_properties(urionto)
# load_data_properties(urionto)
# load_individuals(urionto)

g = Graph()
fp = Namespace("http://www.example.org/fp#")
g.bind("fp", fp)

def create_main_classes(subject_col_src, namespaced_class):
    prefixed_subject = fp + subject_col_src.replace(" ", "_").lower()
    g.add((URIRef(prefixed_subject), RDF.type, namespaced_class))

for row in world_cities_df.itertuples(index=True, name="Pandas"):
    # Pandas(Index=0, city='Tokyo', city_ascii='Tokyo', lat=35.6897, lng=139.6922, country='Japan', iso2='JP', iso3='JPN', admin_name='Tōkyō', capital='primary', population=37977000)
    create_main_classes(row.city_ascii, fp.City)
    create_main_classes(row.country, fp.Country)


    # def mappingToCreateTypeTriple(self, subject_column, class_type, useExternalURI):
        
    #     for subject in self.data_frame[subject_column]:
                
    #         #We use the ascii name to create the fresh URI for a city in the dataset
    #         if subject.lower() in self.stringToURI:
    #             entity_uri=self.stringToURI[subject.lower()]
    #         else:
    #             entity_uri=self.createURIForEntity(subject.lower(), useExternalURI)
            
    #         #TYPE TRIPLE
    #         #For the individuals we use URIRef to create an object "URI" out of the string URIs
    #         #For the concepts we use the ones in the ontology and we are using the NameSpace class
    #         #Alternatively one could use URIRef(self.labe6_ns_str+"City") for example 
    #         self.g.add((URIRef(entity_uri), RDF.type, class_type))
        

                        

print(g.serialize(format="turtle").decode("utf-8"))
g.serialize(destination="fei.ttl", format="ttl")


# def mappingToCreateTypeTriple(self, subject_column, class_type, useExternalURI):


#     for subject in self.data_frame[subject_column]:
            
#         #We use the ascii name to create the fresh URI for a city in the dataset
#         if subject.lower() in self.stringToURI:
#             entity_uri=self.stringToURI[subject.lower()]
#         else:
#             entity_uri=self.createURIForEntity(subject.lower(), useExternalURI)
        
#         #TYPE TRIPLE
#         #For the individuals we use URIRef to create an object "URI" out of the string URIs
#         #For the concepts we use the ones in the ontology and we are using the NameSpace class
#         #Alternatively one could use URIRef(self.labe6_ns_str+"City") for example 
#         self.g.add((URIRef(entity_uri), RDF.type, class_type))


                    

# bnode = BNode()  # a GUID is generated

# g.add((city.inm713, RDF.type, city.Module))
# g.add((city.ernesto, city.teaches, city.inm713))

# g.add((bnode, RDF.type, RDF.Statement))
# g.add((bnode, RDF.subject, city.ernesto))
# g.add((bnode, RDF.predicate, city.teaches))
# g.add((bnode, RDF.object, city.inm713))
# g.add((bnode, dbpo.year, year))

# print(g.serialize(format="turtle").decode("utf-8"))
# g.serialize(destination="mylab.ttl", format="ttl")
