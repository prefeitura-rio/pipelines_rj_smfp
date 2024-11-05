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

tables = [{"table_id": "funcionarios_ativos"}, {"table_id": "funcionarios"}]


smfp_funcionarios_saude_clocks = [
    IntervalClock(
        interval=timedelta(days=1),
        start_date=datetime(2021, 11, 23, 1, 0, tzinfo=pytz.timezone("America/Sao_Paulo"))
        + timedelta(minutes=5 * count),
        labels=[
            constants.RJ_SMFP_AGENT_LABEL.value,
        ],
        parameter_defaults={
            "dataset_id": "recursos_humanos_ergon_saude",
            "table_id": parameter["table_id"],
        },
    )
    for count, parameter in enumerate(tables)
]
smfp_funcionarios_saude_daily_update_schedule = Schedule(
    clocks=untuple(smfp_funcionarios_saude_clocks)
)
