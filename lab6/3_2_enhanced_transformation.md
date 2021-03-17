# Steps to make all this work

## Creating the ontology in Protege

1. Under Classes > owl:Thing, create:
    - Country
    - City
        - CapitalCity
        - AdminCapitalCity
            - FirstLevelAdminCapitalCity
            - LowerLevelAdminCapitalCity
2. Under Object properties > owl:topObjectProperty, create:
    - hasCity
        - hasAdminCapitalCity
        - hasCapitalCity
    - isLocatedIn
        - isLocatedInCountry
    <!-- - hasCityPopulation -->
    <!-- - hasISO2
    - hasISO3
    - hasLongitude
    - hasLatitude -->
3. Under Object properties:
    - isLocatedIn
        - isLocatedInCountry
            - Domains: City
            - Ranges: Country
    - hasCity
        - Domains: Country
        - Ranges: City
3. Under Individuals, create:
    - Japan
        - Description > Types > Country
        - Object property assertions > hasCity: Tokyo
    - Tokyo
        - Description > Types > CapitalCity
    To test City <-> Country relationship
4. Under
4. Under Data properties, create:
    - hasCityPopulation
        - Functional > (tick)
        - Description >
            - Domains: City
            - Ranges: xsd:integer
5. Under Individuals, set:
    - Tokyo
        - Data property assertions > hasCityPopulation
            - Type: xsd:integer
            - Value: 37977000