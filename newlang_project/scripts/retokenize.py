"""
Script for re-merging tokens that were split in INCEpTION
"""

import re
import pathlib

MERGED_TOKEN = re.compile(
    r"""
    ^
    (?P<token>\w{2,})\W
    (?P<position>[B|I|O])-?
    (?P<tag>\w+)?
    $
""",
    re.VERBOSE | re.MULTILINE,
)


def split_tokens(match: re.Match) -> str:
    token, position, tag = match.groups()

    if position == "O":
        lines = [f"{tok_part} {position}" for tok_part in token]
        return "\n".join(lines)
    elif position == "I":
        lines = [f"{tok_part} {position}-{tag}" for tok_part in token]
        return "\n".join(lines)
    elif position == "B":
        lines = [f"{tok_part} I-{tag}" for tok_part in token[1:]]
        lines = [f"{token[0]} B-{tag}"] + lines
        return "\n".join(lines)
    else:
        raise ValueError(f"Invalid tag {tag}")


if __name__ == "__main__":
    for file in pathlib.Path("3_inception_export").glob("*.conll"):
        contents = open(file).read()
        contents = MERGED_TOKEN.sub(split_tokens, contents)
        file.write_text(contents)
