'''
Created on 02 Feb 2021

@author: ejimenez-ruiz
'''
from rdflib import Graph

def queryLocalGraph():

    #Example from  https://www.stardog.com/tutorials/data-model/

    g = Graph()
    g.parse("playground.ttl", format="ttl")


    print("Loaded '" + str(len(g)) + "' triples.")

    #for s, p, o in g:
    #    print((s.n3(), p.n3(), o.n3()))

    print("Females:")

    qres = g.query(
    """SELECT ?thing ?name where {
      ?thing tto:sex "female" .
      ?thing dbp:name ?name .
    }""")

    for row in qres:
      #Row is a list of matched RDF terms: URIs, literals or blank nodes
      print("%s is female with name '%s'" % (str(row.thing),str(row.name)))


    # Query 1
    # Query to return Eve’s grandfather.
    qres_grandfather1 = g.query(
      """select ?name ?grandfather where {
        ttr:Eve dbo:parent / dbo:parent ?grandfather  .
        ?grandfather dbp:name ?name .
      }
      """
    )

    for row in qres_grandfather1:
      print(f"{row.grandfather}: {row.name}")

    qres_grandfather2 = g.query(
      """select ?name ?grandfather where {
        ttr:Eve dbo:parent [dbo:parent ?grandfather]  .
        ?grandfather dbp:name ?name .
      }
      """
    )

    for row in qres_grandfather2:
      print(f"{row.grandfather}: {row.name}")

    # Query 2
    # Things that are dogs with color and sex.
    qres_dog = g.query(
      """
      select ?name ?sex ?color ?thing where {
      ?thing tto:sex ?sex .
      ?thing a tto:Dog .
      ?thing tto:color ?color .
      ?thing dbp:name ?name .
      }
      """
    )

    for row in qres_dog:
      print(f"{row.thing}: {row.name}, {row.sex}, {row.color}")

    # Query 3
    # This query shows pets with their owners
      qres_pets_owners = g.query(
      """
      select ?pet_name ?owner_name ?pet ?owner where {
        ?pet a / rdfs:subClassOf+ tto:Animal .
        {?owner tto:pet ?pet} .
        ?pet dbp:name ?pet_name .
        ?owner dbp:name ?owner_name .
      }
      """
    )

    for row in qres_pets_owners:
      print(f"{row.pet_name}: {row.owner_name}")

    # Query 4
    # Select people with their gender and birth date ordered by gender and birth date (oldest first).

    qres_people_gender_dob = g.query(
      """
      select ?gender ?birthdate ?name where {
        ?person tto:sex ?gender .
        ?person dbp:birthDate ?birthdate .
        ?person dbp:name ?name .
      } order by ?gender ?birthdate
      """
    )

    for row in qres_people_gender_dob:
      print(f"{row.name}: {row.gender}, {row.birthdate}")

queryLocalGraph()