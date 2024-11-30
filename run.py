import polars as pl
from polars_deunicode_string import decode_string


df: pl.DataFrame = pl.DataFrame(
    {"text": ["Nariño", "Jose Fernando Ramírez Güiza", "Córdoba", "Hello World!", None]}
)

result_df: pl.DataFrame = (
    df.lazy().with_columns([decode_string("text").name.prefix("decode_")]).collect()
)

print(result_df)
