from pathlib import Path
from pyshacl import validate

ALLOW_WARNINGS = True  # Allows warnings to flag as invalid when true
SHOW_WARNINGS = True


REPO_ROOT_DIR = Path(__file__).parent.parent
VOCABS_DIR = REPO_ROOT_DIR / "vocabularies"
VALIDATOR_FILE = REPO_ROOT_DIR / "validation" / "vocpub-4.10.ttl"


def main():
    print(f"Validating all vocabs in {VOCABS_DIR}")
    warning_vocabs = {}  # format {vocab_filename: warning_msg}
    invalid_vocabs = {}  # format {vocab_filename: error_msg}

    for f in VOCABS_DIR.glob("*.ttl"):
        # ...validate each file
        print(f"Validating {f}")
        try:
            v = validate(str(f), shacl_graph=str(VALIDATOR_FILE), shacl_graph_format="ttl", allow_warnings=ALLOW_WARNINGS)
            if not v[0]:
                if "Severity: sh:Violation" in v[2]:
                    invalid_vocabs[f.name] = v[2]
                elif "Severity: sh:Warning" in v[2]:
                    warning_vocabs[f.name] = v[2]

        # syntax errors crash the validate() function
        except Exception as e:
            invalid_vocabs[f.name] = e

    # check to see if we have any invalid vocabs
    if len(warning_vocabs.keys()) > 0 and SHOW_WARNINGS:
        print("Warning Vocabs:\n")
        for vocab, warning in warning_vocabs.items():
            print(f"- {vocab}:")
            print(warning)
            print("-----")

    # check to see if we have any invalid vocabs
    if len(invalid_vocabs.keys()) > 0:
        print("Invalid Vocabs:\n")
        for vocab, error in invalid_vocabs.items():
            print(f"- {vocab}:")
            print(error)
            print("-----")

    assert len(invalid_vocabs.keys()) == 0, "Invalid vocabs: {}".format(", ".join([str(x) for x in invalid_vocabs.keys()]))


if __name__ == "__main__":
    main()
