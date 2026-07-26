import pandas as pd


def get_selection_reason(row: pd.Series) -> str:
    """
    Determine the selection outcome for an asset based on the
    predefined eligibility criteria.

    Parameters
    ----------
    row : pd.Series
        Row from the data quality table.

    Returns
    -------
    str
        Explanation of the selection decision.
    """

    if row["passes_coverage"] and row["passes_missing"]:
        return "Eligible"

    if not row["passes_coverage"] and row["passes_missing"]:
        return "Insufficient historical coverage"

    if row["passes_coverage"] and not row["passes_missing"]:
        return "Excessive missing values"

    return "Insufficient historical coverage and excessive missing values"
