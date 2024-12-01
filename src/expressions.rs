#![allow(clippy::unused_unit)]

use deunicode::deunicode;
use polars::prelude::*;
use pyo3_polars::derive::polars_expr;

#[polars_expr(output_type=String)]
/// Take a string and decore it to ascii in the NFKD form.
fn decode_string(inputs: &[Series]) -> PolarsResult<Series> {
    let string: &StringChunked = inputs[0].str()?;
    let out: StringChunked =
        string.apply_into_string_amortized(|value: &str, output: &mut String| {
            let decoded: String = deunicode(value);
            output.push_str(&decoded)
        });
    Ok(out.into_series())
}
