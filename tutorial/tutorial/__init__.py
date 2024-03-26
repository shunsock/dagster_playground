from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    EnvVar,
    define_asset_job,
    load_assets_from_modules,
)

from .assets import hacker_news
# from . import assets as hacker_news
from .resources import DataGeneratorResource

all_assets = load_assets_from_modules([hacker_news])

# Define a job that will materialize the assets
hackernews_job = define_asset_job("hackernews_job", selection=AssetSelection.all())

# Addition: a ScheduleDefinition the job it should run and a cron schedule of how frequently to run it
hackernews_schedule = ScheduleDefinition(
    job=hackernews_job,
    cron_schedule="0 * * * *",  # every hour
)

datagen = DataGeneratorResource(
    num_days=EnvVar.int("HACKERNEWS_NUM_DAYS_WINDOW"),
)

defs = Definitions(
    assets=all_assets,
    schedules=[hackernews_schedule],
    resources={
        "hackernews_api": datagen
    },
)

