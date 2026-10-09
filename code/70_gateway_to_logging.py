"""Very basic intro to logging"""
import logging
import pandas as pd
import numpy as np

# ---------------------------
# CONFIGURE THE LOGGER (ONCE)
# ---------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | f: %(funcName)-17s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


# ------------------
# PIPELINE FUNCTIONS
# ------------------
def read_data() -> pd.DataFrame:
    """Read data from a source."""
    logging.info("")
    df = pd.DataFrame.from_dict(
        {
            "text": ["abc-01", "cDe 02", "Efg_03", np.nan],
            "Number1": [1, 6, 10, 5],
            "Number2": [59.99, 14.99, 9.99, 23.99],
        }
    )
    logging.info(f"{df.shape[0], df.shape[1]} data loaded.")
    return df


def clean_data(data: pd.DataFrame = None) -> pd.DataFrame:
    """Remove nans."""
    logging.info("Remove NANs")
    df_dropped = data.dropna().reset_index(drop=True)
    logging.info(f"{len(data)-len(df_dropped)} rows dropped.")
    return df_dropped


def calculate_metrics(data: pd.DataFrame = None) -> pd.DataFrame:
    """Add new KPI columns to the data."""
    logging.info("Total sales calculated.")
    data["product"] = data.iloc[:, 1] * data.iloc[:, 2]
    logging.info(f"Max sale: {data["product"].max()}")
    return data


def main():
    """Run main pipeline"""
    logging.info("Start the logging")

    df = read_data()
    df = clean_data(df)
    df = calculate_metrics(df)


if __name__ == "__main__":
    main()