"""Load inception conll-2002 data and convert to spaCy binary format (DocBin)"""

import typer
from pathlib import Path
import subprocess


def convert(export_path: Path, n_sents: int):
    export_path = Path(export_path)
    assert export_path.exists()

    converted_path = Path.cwd() / "corpus" / "converted"
    assert converted_path.exists()

    # convert conll to .spacy
    for file in export_path.glob("*.conll"):
        subprocess.run(
            [
                "python",
                "-m",
                "spacy",
                "convert",
                f"{str(file)}",
                str(converted_path),
                f"-n {n_sents}",
            ]
        )


if __name__ == "__main__":
    typer.run(convert)

convert.__doc__ = __doc__
