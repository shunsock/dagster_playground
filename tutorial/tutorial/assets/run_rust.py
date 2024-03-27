from dagster import (
    AssetExecutionContext,
    MaterializeResult,
    MetadataValue,
    asset,
)

import json
import os
import pandas as pd
import subprocess


@asset
def run_rust(context: AssetExecutionContext) -> MaterializeResult:

    result = subprocess.run(["./bin/write_csv"], shell=True, check=True)
    df= pd.read_csv("data/from_rust.csv")

    return MaterializeResult(
        metadata={
            "num_records": len(df),
            "preview": MetadataValue.md(df.head().to_markdown()),
        }
    )

