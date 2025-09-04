import polars as pl
import polars_deunicode_string as deunicode


def test_decode_string():
    df = pl.DataFrame(
        {
            "name": ["Jhon", "María", "José", "Eva-lin"],
            "city": ["Bogotá", "Tunja", "Medellín", "Nariño"],
        }
    )
    result = df.select([deunicode.decode_string(pl.col(pl.String))])

    expected_df = pl.DataFrame(
        {
            "name": ["Jhon", "Maria", "Jose", "Eva-lin"],
            "city": ["Bogota", "Tunja", "Medellin", "Narino"],
        }
    )

    assert result.equals(expected_df)
