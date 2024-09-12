# -*- coding: utf-8 -*-
"""
Schedules for the database dump pipeline...........
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
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "partition_columns": "dt_SituacaoCadastral",
        "partition_date_format": "%Y-%m-%d",
        "dump_mode": "append",
        "break_query_frequency": "month",
        "break_query_start": "current_month",
        "break_query_end": "current_month",
        "execute_query": """
            SELECT
                CNPJ_basico, CNPJ_ordem, CNPJ_dv, RazaoSocial,
                cd_PorteEmpresa, cd_SituacaoCadastral, dt_SituacaoCadastral
            FROM SDI.ReceitaFederal.Vw_PorteEmpresa_Sigma
        """,
    }
}

porte_empresa_clocks = generate_dump_db_schedules(
    interval=timedelta(days=7),
    start_date=datetime(2022, 10, 30, 23, 0, tzinfo=pytz.timezone("America/Sao_Paulo")),
    labels=[
        constants.RJ_SMFP_AGENT_LABEL.value,
    ],
    db_database="SDI",
    db_host="10.70.1.34",
    db_port="1433",
    db_type="sql_server",
    dataset_id="porte_empresa",
    infisical_secret_path="/db-porte-empresa",
    table_parameters=porte_empresa_queries,
)

porte_empresa_schedule = Schedule(clocks=untuple(porte_empresa_clocks))
