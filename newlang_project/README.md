<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Named Entity Recognition in the Dai Nihon Shi

This project trains a named entity recognizer on annotated text from the [_Dai Nihon Shi_](https://en.wikipedia.org/wiki/Dai_Nihonshi), a major scholarly work of Edo-period Japan.

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `install` | Install the new language object from Cadet |
| `check-conll` | Look for errors in CoNLL-2002 files |
| `convert` | Convert the data to spaCy's format |
| `split` | Split the data into train, validation, and test |
| `debug` | Assess data for training using spaCy's debug data |
| `pretrain` | Pretrain kanbun |
| `train` | Train kanbun |
| `evaluate` | Evaluate on the test data and save the metrics |
| `package` | Package the trained model so it can be installed |
| `document` | Generate project documentation |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `install` &rarr; `check-conll` &rarr; `convert` &rarr; `split` &rarr; `debug` &rarr; `pretrain` &rarr; `train` &rarr; `evaluate` &rarr; `package` &rarr; `document` |
| `tune` | `train` &rarr; `evaluate` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `assets/kanbun` | Git |  |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
