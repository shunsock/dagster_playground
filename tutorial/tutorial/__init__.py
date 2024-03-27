from dagster import (
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
)

from .assets import run_rust

run_rust_assets = load_assets_from_modules([run_rust])

run_rust_job = define_asset_job(
        name="run_rust_job",
        selection=["run_rust"],
)

run_rust_schedule = ScheduleDefinition(
    job=run_rust_job,
    cron_schedule="0 * * * *",  # every hour
)

defs = Definitions(
    assets=run_rust_assets,
    schedules=[run_rust_schedule],
)

