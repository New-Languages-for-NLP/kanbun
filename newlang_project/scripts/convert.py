"""Load inception conll-2002 data and convert to spaCy binary format (DocBin)"""

from multiprocessing.sharedctypes import Value
import subprocess
from pathlib import Path

import typer
from spacy.util import get_lang_class
from spacy.tokens import DocBin


def convert(export_path: Path, raw_path: Path, n_sents: int):
    assert export_path.exists()
    assert raw_path.exists()

    converted_path = Path.cwd() / "corpus" / "converted"
    assert converted_path.exists()

    # convert conll to .spacy
    for file in export_path.glob("*.conll"):
        try:
            subprocess.run(
                [
                    "python",
                    "-m",
                    "spacy",
                    "convert",
                    f"{str(file)}",
                    str(converted_path),
                    f"-n {n_sents}",
                ],
                check=True
            )
        except subprocess.CalledProcessError as e:
            typer.secho(f"Error converting {file}: {e}", err=True, fg="red")

    # convert raw text to .spacy for pretraining
    lang = get_lang_class("lzh")
    nlp = lang()
    db = DocBin()
    for file in raw_path.glob("*.txt"):
        doc = nlp(file.read_text())
        db.add(doc)
    db.to_disk(converted_path / "raw_text.spacy")


if __name__ == "__main__":
    typer.run(convert)

convert.__doc__ = __doc__
