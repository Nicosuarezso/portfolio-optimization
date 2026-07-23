"""
Functions for downloading and loading financial market data.
"""

import yfinance as yf
import pandas as pd
import pyarrow as pa

def download_market_data(
    tickers: list[str],
    start_date: str,
    end_date: str,
) -> pd.DataFrame:
    """
    Download historical market data from Yahoo Finance.

    Parameters
    ----------
    tickers : list[str]
        List of ticker symbols.
    start_date : str
        Start date in YYYY-MM-DD format.
    end_date : str
        End date in YYYY-MM-DD format.

    Returns
    -------
    pd.DataFrame
        Historical adjusted price data.
    """

    prices = yf.download(
        tickers=tickers,
        start=start_date,
        end=end_date,
        auto_adjust=True,
        progress=False,
    )

    return prices

"""
Functions for saving and loading datasets.
"""

from pathlib import Path

def save_dataset(
    data: pd.DataFrame,
    output_path: str,
) -> None:
    """
    Save a DataFrame as a Parquet file.
    """

    Path(output_path).parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    data.to_parquet(output_path)