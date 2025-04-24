# -*- coding: utf-8 -*-
"""
Schedules for the database dump pipeline
"""

from datetime import datetime, timedelta

import pytz
from prefect.schedules import Schedule
from prefect.schedules.clocks import IntervalClock
from prefeitura_rio.pipelines_utils.io import untuple_clocks as untuple

from pipelines.constants import constants

tables = [
    {"table_id": "cargo"},
    {"table_id": "empresa"},
    {"table_id": "funcionario"},
    {"table_id": "provimento"},
    {"table_id": "setor"},
    {"table_id": "vinculo"},
]


smfp_funcionarios_saude_clocks = [
    IntervalClock(
        interval=timedelta(days=1),
        start_date=datetime(2021, 11, 5, 0, 0, tzinfo=pytz.timezone("America/Sao_Paulo"))
        + timedelta(minutes=5 * count),
        labels=[
            constants.RJ_SMFP_AGENT_LABEL.value,
        ],
        parameter_defaults={
            "dataset_id": "brutos_ergon",
            "table_id": parameter["table_id"],
        },
    )
    for count, parameter in enumerate(tables)
]
smfp_funcionarios_saude_daily_update_schedule = Schedule(
    clocks=untuple(smfp_funcionarios_saude_clocks)
)
