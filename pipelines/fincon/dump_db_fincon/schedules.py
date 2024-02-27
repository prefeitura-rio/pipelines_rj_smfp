# -*- coding: utf-8 -*-
"""
Schedules for the SMS SIGMA dump_db pipeline.
"""

from datetime import datetime, timedelta

import pytz
from prefect.schedules import Schedule
from prefeitura_rio.pipelines_utils.io import untuple_clocks as untuple
from prefeitura_rio.pipelines_utils.prefect import generate_dump_db_schedules

from pipelines.constants import constants

#####################################
#
# SMFP FINCON Schedules
#
#####################################

_fincon_queries = {
    "instrumento_firmado": {
        "biglake_table": True,
        "materialize_after_dump": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                Exercicio,
                Numero,
                Orgao_Executor,
                Descricao_Orgao_Executor,
                Objeto,
                Especie,
                Situacao,
                Cnpj,
                Favorecido,
                Processo,
                Data_Inicio_Prev,
                Data_Fim_Prev,
                Valor_Atualizado,
                Valor_Pago,
                Pt,
                Natureza,
                Fonte,
                Modalidade_Licitacao,
                Embasamento_Legal,
                Saldo_Exec,
                Valor_Empenhado,
                Valor_Liquidado,
                Data_Assinatura,
                Tipo_Favorecido
            FROM DW_IGAA.dbo.VINSTRUMENTOS_JURIDICOS_ESCRITORIO_GBP
        """,  # noqa
    },
}

fincon_infra_clocks = generate_dump_db_schedules(
    interval=timedelta(days=1),
    start_date=datetime(2022, 3, 21, 1, 0, tzinfo=pytz.timezone("America/Sao_Paulo")),
    labels=[
        constants.RJ_SMFP_AGENT_LABEL.value,
    ],
    db_database="DW_IGAA",
    db_host="10.2.221.17",
    db_port="1433",
    db_type="sql_server",
    dataset_id="adm_instrumentos_firmados",
    infisical_secret_path="/db-fincon",
    table_parameters=_fincon_queries,
)

compras_fincon_daily_update_schedule = Schedule(clocks=untuple(fincon_infra_clocks))
