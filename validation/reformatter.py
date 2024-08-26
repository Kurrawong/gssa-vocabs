from pathlib import Path
from rdflib import Graph

REPO_ROOT_DIR = Path(__file__).parent.parent
VOCABS_DIR = REPO_ROOT_DIR / "vocabularies"

for f in VOCABS_DIR.glob("*.ttl"):
    g = Graph().parse(str(f))
    g.serialize(destination=f.with_suffix(".2.tt"), format="longturtle")
