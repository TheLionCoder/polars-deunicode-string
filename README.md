# polars-deunicode-string

[![Crates.io](https://img.shields.io/crates/v/deunicode.svg)](https://crates.io/crates/deunicode)

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

shape: (4, 2)
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
