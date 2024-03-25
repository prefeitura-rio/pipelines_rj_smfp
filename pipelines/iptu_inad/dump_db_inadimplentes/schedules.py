# -*- coding: utf-8 -*-
"""
Schedules for the database dump pipeline
"""

from datetime import datetime, timedelta

import pytz
from prefect.schedules import Schedule
from prefeitura_rio.pipelines_utils.io import untuple_clocks as untuple
from prefeitura_rio.pipelines_utils.prefect import generate_dump_db_schedules

from pipelines.constants import constants

#####################################
#
# Inadimplente Schedules
#
#####################################

inadimplente_queries = {
    "perfil_inadimplente_v2": {
        "dump_mode": "overwrite",
        "execute_query": "SELECT * FROM DBINAD.IPTU.IPTU;",
        "materialize_after_dump": True,
        "materialization_mode": "prod",
    }
}

inadimplente_clocks = generate_dump_db_schedules(
    interval=timedelta(days=7),
    start_date=datetime(2022, 10, 30, 23, 0, tzinfo=pytz.timezone("America/Sao_Paulo")),
    labels=[
        constants.RJ_SMFP_AGENT_LABEL.value,
    ],
    db_database="DBINAD",
    db_host="10.3.23.158",
    db_port="1433",
    db_type="sql_server",
    dataset_id="iptu_inadimplentes",
    infisical_secret_path="/db-iptu-inadimplentes",
    table_parameters=inadimplente_queries,
)

inadimplente_weekly_update_schedule = Schedule(clocks=untuple(inadimplente_clocks))
