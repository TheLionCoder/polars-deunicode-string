# polars-deunicode-string

[![Crates.io](https://img.shields.io/crates/v/deunicode.svg)](https://crates.io/crates/deunicode)

[![PIPY](https://img.shields.io/pypi/v/polars-deunicode-string.svg)](https://pypi.org/project/polars-deunicode-string/)
[![Docs.rs](https://docs.rs/deunicode/badge.svg)](https://docs.rs/deunicode)
[![PyPI - License](https://img.shields.io/pypi/l/polars-deunicode-string)](https://pypi.org/project/polars-deunicode-string/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/polars-deunicode-string)](https://pypi.org/project/polars-deunicode-string/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/polars-deunicode-string)](https://pypi.org/project/polars-deunicode-string/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/polars-deunicode-string)](https://pypi.org/project/polars-deunicode-string/)
[![PyPI - Format](https://img.shields.io/pypi/format/polars-deunicode-string)](https://pypi.org/project/polars-deunicode-string/)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/polars-deunicode-string)](https://pypi.org/project/polars-deunicode-string/)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/polars-deunicode-string)](https://pypi.org/project/polars-deunicode-string/)
[![PyPI - Status](https://img.shields.io/pypi/status/polars-deunicode-string)](https://pypi.org/project/polars-deunicode-string/)

This is a simple polars-plugin that de-unicodes a string using the deunicode crate.

## Installation

```bash
pip install polars-deunicode-string
```

## Basic Example

```python
import polars-deunicode-string as dunicode


df: pl.DataFrame = pl.DataFrame(
    {
        "text": ["Nariño", "Jose Fernando Ramírez Güiza",
                 "Córdoba", "Hello World!", None],
    }
)

```

_Let´s de-unicode and make lowercase the column "text":_

```python
result*df: pl.DataFrame = (
df.lazy().with_columns([dunicode("text").name.prefix("decode")]).collect()
)
print(result_df)

shape: (5, 2)
┌─────────────────────────────┬─────────────────────────────┐
│ text                        ┆ decode_text                 │
│ ---                         ┆ ---                         │
│ str                         ┆ str                         │
╞═════════════════════════════╪═════════════════════════════╡
│ Nariño                      ┆ Narino                      │
│ Jose Fernando Ramírez Güiza ┆ Jose Fernando Ramirez Guiza │
│ Córdoba                     ┆ Cordoba                     │
│ Hello World!                ┆ Hello World!                │
│ null                        ┆ null                        │
└─────────────────────────────┴─────────────────────────────┘
```
