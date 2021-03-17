"""
Task 1 (Optional): Execute an available CSV to RDF converter over the world cities
dataset and analyze the the obtained RDF triples.

Help: https://stackoverflow.com/questions/43524943/creating-rdf-file-using-csv-file-as-input
"""
import rdflib
import csv
import pandas

filename='worldcities-free-100.csv'
df = pd.read_csv(filename, sep=",")


# for row in df.itertuples(index=True, name="Pandas"):
#     print(row)



g = Graph()
ppl = Namespace('http://example.org/people/')
loc = Namespace('http://mylocations.org/addresses/')
schema = Namespace('http://schema.org/')


city,city_ascii,lat,lng,country,iso2,iso3,admin_name,capital,population




# df # uncomment to check for contents


# import pandas as pd #for handling csv and csv contents
# from rdflib import Graph, Literal, RDF, URIRef, Namespace #basic RDF handling
# from rdflib.namespace import FOAF , XSD #most common namespaces
# import urllib.parse #for parsing strings to URI's

# with open(file) as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",", quotechar='"', escapechar="\\")
#     for row in csv_reader:
#         print(row)
