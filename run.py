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

print("Data:\n")
print(df)

print("Normalized Data:\n")
print(normalized_df)
