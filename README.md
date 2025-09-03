# POLARS-DEUNICODE-STRING

[![Crates.io](https://img.shields.io/crates/v/deunicode.svg)](https://crates.io/crates/deunicode)

[![PIPY](https://img.shields.io/pypi/v/polars-deunicode-string.svg)](https://pypi.org/project/polars-deunicode-string/)
[![Docs.rs](https://docs.rs/deunicode/badge.svg)](https://docs.rs/deunicode)
[![PyPI - License](https://img.shields.io/pypi/l/polars-deunicode-string)](https://pypi.org/project/polars-deunicode-string/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/polars-deunicode-string)](https://pypi.org/project/polars-deunicode-string/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/polars-deunicode-string)](https://pypi.org/project/polars-deunicode-string/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/polars-deunicode-string)](https://pypi.org/project/polars-deunicode-string/)
[![PyPI - Format](https://img.shields.io/pypi/format/polars-deunicode-string)](https://pypi.org/project/polars-deunicode-string/)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/polars-deunicode-string)](https://pypi.org/project/polars-deunicode-string/)

This is a simple polars-plugin that de-unicodes a string using the deunicode crate.

---

## Installation

```bash
pip install polars-deunicode-string
```

---

## Basic Example

```python

import polars as pl
import polars_deunicode_string as deunicode


df = pl.DataFrame(
    {
        "name": ["Jhon", "María", "José", "Eva-lin"],
        "city": ["Bogotá", "Tunja", "Medellín", "Nariño"],
    }
)
normalized_df = df.select([
    deunicode.decode_string(pl.col(pl.String))
])
print(df)
>>> Data:

shape: (4, 2)
┌─────────┬──────────┐
│ name    ┆ city     │
│ ---     ┆ ---      │
│ str     ┆ str      │
╞═════════╪══════════╡
│ Jhon    ┆ Bogotá   │
│ María   ┆ Tunja    │
│ José    ┆ Medellín │
│ Eva-lin ┆ Nariño   │
└─────────┴──────────┘

print(normalized_df)
>>> Normalized Data:

shape: (4, 2)
┌─────────┬──────────┐
│ name    ┆ city     │
│ ---     ┆ ---      │
│ str     ┆ str      │
╞═════════╪══════════╡
│ Jhon    ┆ Bogota   │
│ Maria   ┆ Tunja    │
│ Jose    ┆ Medellin │
│ Eva-lin ┆ Narino   │
└─────────┴──────────┘
```
