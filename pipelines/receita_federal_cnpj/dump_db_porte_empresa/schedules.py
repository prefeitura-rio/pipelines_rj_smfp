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

porte_empresa_queries = {
    "situacao_cadastral": {
        "dump_mode": "overwrite",
        "execute_query": "SELECT * FROM SDI.ReceitaFederal.Vw_PorteEmpresa_Sigma",
        "materialize_after_dump": False,
        "materialization_mode": "prod",
    }
}

porte_empresa_clocks = generate_dump_db_schedules(
    interval=timedelta(days=7),
    start_date=datetime(2022, 10, 30, 23, 0, tzinfo=pytz.timezone("America/Sao_Paulo")),
    labels=[
        constants.RJ_SMFP_AGENT_LABEL.value,
    ],
    db_database="CLUSTERSQL2",
    db_host="10.70.1.3",
    db_port="1433",
    db_type="sql_server",
    dataset_id="porte_empresa",
    infisical_secret_path="/db-porte-empresa",
    table_parameters=porte_empresa_queries,
)

porte_empresa_schedule = Schedule(clocks=untuple(porte_empresa_clocks))
