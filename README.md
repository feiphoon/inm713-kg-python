## Example codes in Python for the 'Semantic Web Technologies and Knowledge Graphs' module

- **Laboratory 1**: Set up.
- **Laboratory 2**: Creating simple RDF-based Knowledge Graphs.
- **Laboratory 3**: Querying RDF-based Knowledge Graphs via SPARQL 1.0.
- **Laboratory 4**: Reasoning with RDFS Semantics. Updated with solutions.
- **Laboratory 5**: Modelling Ontologies with OWL 2 and Protégé.
- **Laboratory 6**: Exposing Tabular Data as an RDF-based Knowledge Graph.

### Dependencies
- [Python 3](https://www.python.org/)
- [Owlready2](https://pypi.org/project/Owlready2/)
- [SPARQLWrapper](https://pypi.org/project/SPARQLWrapper/)
- [RDFlib](https://pypi.org/project/rdflib/)
- [OWL-RL](https://pypi.org/project/owlrl/5.2.1/)
- [requests](https://pypi.org/project/requests/)
- [logging](https://pypi.org/project/logging/)
- [pandas](https://pypi.org/project/pandas/)
- [python-Levenshtein](https://pypi.org/project/python-Levenshtein/)

## Setup instructions from fork:

- Fork (don't clone) via the button on the source repo's page at https://github.com/city-knowledge-graphs/python
- On your local, clone your forked repo:
    ```
    git clone git@github.com:your-name/your-renamed-repo.git
    cd your-renamed-repo
    ```
- You want to be able to update your branch from the source repo, and push changes to your own forked repo.
    View your current settings on your local repo by:
    ```
    git remote -v
    ```
    You'll see this:
    ```
    origin  git@github.com:your-name/your-renamed-repo.git (fetch)
    origin  git@github.com:your-name/your-renamed-repo.git (push)
    ```
- Set the upstream to the source repo:
    ```
    git remote add upstream git@github.com:city-knowledge-graphs/python.git
    ```
    Now:
    ```
    git remote -v
    ```
    You'll see this:
    ```
    origin  git@github.com:your-name/your-renamed-repo.git (fetch)
    origin  git@github.com:your-name/your-renamed-repo.git (push)
    upstream  git@github.com:city-knowledge-graphs/python.git (fetch)
    upstream  git@github.com:city-knowledge-graphs/python.git (push)
    ```
- Now, when you want to **pull new changes from the source repo**:
    ```
    git fetch upstream
    ```
    You'll see that a new main(not your own remote), called `upstream/main` has been identified.
    ```
    remote: Enumerating objects: 5, done.
    remote: Counting objects: 100% (5/5), done.
    remote: Compressing objects: 100% (4/4), done.
    remote: Total 4 (delta 1), reused 3 (delta 0), pack-reused 0
    Unpacking objects: 100% (4/4), 585 bytes | 117.00 KiB/s, done.
    From github.com:city-knowledge-graphs/python
    * [new branch]      main       -> upstream/main
    ```
    Merge these updates into your own repo:
    ```
    git merge upstream/main
    ```
    You'll see:
    ```
    [main 1f9e47c] Merge remote-tracking branch 'upstream/main' into main
    ```
- When you want to **push these updates to your own remote repo**:
    ```
    git push
    ```
    (`git push origin` is implied)