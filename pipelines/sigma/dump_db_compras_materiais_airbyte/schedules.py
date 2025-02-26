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

#####################################
#
# SMFP SIGMA COMPRAS MATERIAIS SCHEDULES
#
#####################################


smfp_compras_materiais_servicos_tables = {
    "sancao_fornecedor": "sancao_fornecedor_airbyte",
    "movimentacao": "movimentacao_airbyte",
    "classe": "classe_airbyte",
    "fornecedor": "fornecedor_airbyte",
    "grupo": "grupo_airbyte",
    "material": "material_airbyte",
    "ramo_atividade": "ramo_atividade_airbyte",
    "servoco": "servoco_airbyte",
    "subclasse": "subclasse_airbyte",
    "unidade": "unidade_airbyte",
    "material_referencia": "material_referencia_airbyte",
    "usuario_sistema": "usuario_sistema_airbyte",
    "orgao": "orgao_airbyte",
    "usuario_responsavel_auxiliar": "usuario_responsavel_auxiliar_airbyte",
    "unidade_armazenadora": "unidade_armazenadora_airbyte",
    "responsavel_unidade_armazenadora": "responsavel_unidade_armazenadora_airbyte",
    "movimento_estoque": "movimento_estoque_airbyte",
    "devolucao_material": "devolucao_material_airbyte",
    "saldo_mensal_estoque": "saldo_mensal_estoque_airbyte",
    "fechamento_mensal_estoque": "fechamento_mensal_estoque_airbyte",
    "posicao_fechada_estoque": "posicao_fechada_estoque_airbyte",
    "material_em_transito": "material_em_transito_airbyte",
    "unidade_servico": "unidade_servico_airbyte"
}

compras_sigma_clocks = [
    IntervalClock(
        interval=timedelta(days=1),
        start_date=datetime(2021, 11, 23, 14, 0, tzinfo=pytz.timezone("America/Sao_Paulo"))
        + timedelta(minutes=3 * count),
        labels=[
            constants.RJ_SMFP_AGENT_LABEL.value,
        ],
        parameter_defaults={
            "dataset_id": "compras_materiais_servicos_sigma_airbyte",
            "table_id": table_id,
            "mode": "prod",
        },
    )
    for count, (_, table_id) in enumerate(smfp_compras_materiais_servicos_tables.items())
]
compras_sigma_daily_update_schedule = Schedule(clocks=untuple(compras_sigma_clocks))
