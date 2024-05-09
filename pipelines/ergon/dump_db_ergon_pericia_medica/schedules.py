# -*- coding: utf-8 -*-
# flake8: noqa: E501
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
# Ergon Schedules
#
#####################################

ergon_queries = {
    "folha_pagamento": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                CARGO, NOME, CATEGORIA, SUBCATEGORIA, DT_EXTINCAO,
                CONTROLE_VAGA, POR_REFER, E_AGLUTINADOR, CARGO_AGLUT,
                TIPO_CARGO, CARGO_FUNCAO, ESCOLARIDADE, FLEX_CAMPO_09,
                PONTPUBL, DT_CONTROLE_ACUM, PONTLEI, DT_INICIO_CONTR_VAGA,
                ID_REG
            FROM C_ERGON.VW_DLK_ERG_CARGOS_
        """,
    },
}

ergon_clocks = generate_dump_db_schedules(
    interval=timedelta(days=1),
    start_date=datetime(2022, 11, 9, 22, 30, tzinfo=pytz.timezone("America/Sao_Paulo")),
    labels=[
        constants.RJ_SMFP_AGENT_LABEL.value,
    ],
    db_database="P01.PCRJ",
    db_host="10.70.6.21",
    db_port="1526",
    db_type="oracle",
    dataset_id="recursos_humanos_ergon_pericia_medica",
    infisical_secret_path="/db-ergon-prod",
    table_parameters=ergon_queries,
)

ergon_pericia_medica_monthly_update_schedule = Schedule(clocks=untuple(ergon_clocks))
