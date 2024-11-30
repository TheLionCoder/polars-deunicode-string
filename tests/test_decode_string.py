import polars as pl
from polars_deunicode_string import decode_string


def test_decode_string():
    df = pl.DataFrame(
        {
            "spanish": ["Bogotá", "1ra de Mayo", None, "Nariño", "Güiza"],
        }
    )
    result = df.with_columns(normalized=decode_string("spanish"))

    expected_df = pl.DataFrame(
        {
            "spanish": ["Bogotá", "1ra de Mayo", None, "Nariño", "Güiza"],
            "normalized": ["Bogota", "1ra de Mayo", None, "Narino", "Guiza"],
        }
    )

    assert result.equals(expected_df)
