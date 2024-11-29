# polars-deunicode-string

This is a simple polars-plugin that de-unicodes and makes a string lowercase.

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

```

_Let´s de-unicode and make lowercase the column "text":_

```

```python
result*df: pl.DataFrame = (
df.lazy().with_columns([dunicode("text").name.prefix("decode*")]).collect()
)
print(result_df)

shape: (4, 2)
shape: (5, 2)
┌─────────────────────────────┬─────────────────────────────┐
│ text                        ┆ decode_text                 │
│ ---                         ┆ ---                         │
│ str                         ┆ str                         │
╞═════════════════════════════╪═════════════════════════════╡
│ Nariño                      ┆ narino                      │
│ Jose Fernando Ramírez Güiza ┆ jose fernando ramirez guiza │
│ Córdoba                     ┆ cordoba                     │
│ Hello World!                ┆ hello world!                │
│ null                        ┆ null                        │
└─────────────────────────────┴─────────────────────────────┘
```
