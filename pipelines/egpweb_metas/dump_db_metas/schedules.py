# -*- coding: utf-8 -*-
"""
Schedules for the database dump pipeline.
"""

from datetime import datetime, timedelta

import pytz
from prefect.schedules import Schedule
from prefeitura_rio.pipelines_utils.io import untuple_clocks as untuple
from prefeitura_rio.pipelines_utils.prefect import generate_dump_db_schedules

from pipelines.constants import constants

#####################################
#
# EGPWeb Schedules
#
#####################################

egp_web_queries = {
    "chance": {
        "dump_mode": "overwrite",
        "execute_query": "SELECT * FROM EGPWEB_PRD.dbo.VW_CHANCE;",
        "materialize_after_dump": True,
    },
    "comentario": {
        "dump_mode": "overwrite",
        "execute_query": "SELECT * FROM EGPWEB_PRD.dbo.VW_Comentario;",
        "materialize_after_dump": True,
    },
    "indicador": {
        "dump_mode": "overwrite",
        "execute_query": "SELECT * FROM EGPWEB_PRD.dbo.VW_Indicador;",
        "materialize_after_dump": True,
    },
    "meta": {
        "dump_mode": "overwrite",
        "execute_query": "SELECT * FROM EGPWEB_PRD.dbo.VW_Metas;",
        "materialize_after_dump": True,
        "materialize_to_datario": False,
    },
    "nota_meta": {
        "dump_mode": "overwrite",
        "execute_query": "SELECT * FROM EGPWEB_PRD.dbo.VW_NotaMeta;",
        "materialize_after_dump": True,
    },
    "regra": {
        "dump_mode": "overwrite",
        "execute_query": "SELECT * FROM EGPWEB_PRD.dbo.VW_RegraMeta;",
        "materialize_after_dump": True,
    },
}

egp_web_clocks = generate_dump_db_schedules(
    interval=timedelta(days=1),
    start_date=datetime(2021, 11, 23, 13, 0, tzinfo=pytz.timezone("America/Sao_Paulo")),
    labels=[
        constants.RJ_SMFP_AGENT_LABEL.value,
    ],
    db_database="EGPWEB_PRD",
    db_host="10.2.221.101",
    db_port="1433",
    db_type="sql_server",
    dataset_id="planejamento_gestao_acordo_resultados",
    infisical_secret_path="/db-egpweb-prod",
    table_parameters=egp_web_queries,
)

egp_web_weekly_update_schedule = Schedule(clocks=untuple(egp_web_clocks))
