"""
loadOntology code created on 19 Jan 2021
@author: ejimenez-ruiz

Modified a little.
"""

from owlready2 import *
from onto_access import OntologyAccess

# def getClasses(onto):        
#     return onto.classes()
    
# def getDataProperties(self):        
#     return onto.data_properties()
    
# def getObjectProperties(self):        
#     return onto.object_properties()
    
# def getIndividuals(self):        
#     return onto.individuals()



def loadOntology(urionto, debug=False):

    # Method from owlready
    onto = get_ontology(urionto).load()

    if debug:
        print("Classes in Ontology: " + str(len(list(getClasses(onto)))))
        for cls in getClasses(onto):                
            print("\t"+cls.iri)


#Load ontology
urionto="pizza_restaurant_ontology3.owl"
loadOntology(urionto, debug=True)


    uri_onto = "http://www.cs.ox.ac.uk/isg/ontologies/dbpedia.owl"
    # uri_onto="http://www.cs.ox.ac.uk/isg/ontologies/schema.org.owl"

    # onto_access = DBpediaOntology()
    # onto_access = SchemaOrgOntology()
    onto_access = OntologyAccess(uri_onto)
    onto_access.loadOntology(True)  # Classify True

    query = """SELECT ?s ?p ?o WHERE { ?s ?p ?o . }"""

    results = onto_access.queryGraph(query)

    for r in results:
        print(r)
