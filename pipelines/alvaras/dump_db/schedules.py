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
# Alvaras Schedules
#
#####################################

_alvaras_infra_query = {
    "fact_fatoalvaras": {
        "biglake_table": True,
        "materialize_after_dump": True,
        "materialization_mode": "prod",
        "materialize_to_datario": False,
        "dump_to_gcs": False,
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                ID_Alvara,
                Quantidade,
                ID_AtvProcesso,
                ID_CAE, ID_CNAE,
                ID_DiaDeferimento,
                ID_DiaSolicitacao,
                ID_DiaTaxaPagamen,
                ID_Direcionamento,
                ID_TipoContribuint,
                ID_TipoSolicitacao
            FROM DW_BI_ALVARAS.dbo.FACT_FatoAlvaras;
        """,
    },
    "fact_fatocp": {
        "biglake_table": True,
        "materialize_after_dump": True,
        "materialization_mode": "prod",
        "materialize_to_datario": False,
        "dump_to_gcs": False,
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                ID_AtvProcesso,
                Quantidade_cp,
                ID_CAE,
                ID_CNAE,
                ID_Consulta,
                ID_DiaInicial,
                ID_Direcionamento,
                ID_TipoContribuint,
                ID_TipoSolicitacao
            FROM DW_BI_ALVARAS.dbo.FACT_FatoCP;
        """,
    },
    "fact_fatodatacarga": {
        "biglake_table": True,
        "materialize_after_dump": True,
        "materialization_mode": "prod",
        "materialize_to_datario": False,
        "dump_to_gcs": False,
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                DataCarga
            FROM DW_BI_ALVARAS.dbo.FACT_FatoDataCarga;
        """,
    },
    "tab_alvara": {
        "biglake_table": True,
        "materialize_after_dump": True,
        "materialization_mode": "prod",
        "materialize_to_datario": False,
        "dump_to_gcs": False,
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                ID_Alvara,
                DSC_Alvara,
                DSC_Endereco,
                DSC_Bairro,
                DSC_Zoneamento,
                DSC_IRLF,
                DSC_TipoAnalise,
                DSC_TempoRespDia,
                DSC_StatusIntermediario,
                DSC_StatusCPL,
                DSC_TempoRespMinuto,
                DSC_TipoAlvara,
                DSC_TaxaOriginal,
                DSC_TaxaMulta,
                DSC_TaxaMora,
                DSC_TaxaTotal,
                DSC_IsentoTaxa,
                DSC_Numero,
                DSC_AlvaraLiberado
            FROM DW_BI_ALVARAS.dbo.TAB_ALVARA;
        """,
    },
    "tab_atvprocesso": {
        "biglake_table": True,
        "materialize_after_dump": True,
        "materialization_mode": "prod",
        "materialize_to_datario": False,
        "dump_to_gcs": False,
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                ID_AtvProcesso,
                DSC_AtvProcesso,
                DSC_RespAtividade,
                DSC_RefAtividade
            FROM DW_BI_ALVARAS.dbo.TAB_AtvProcesso;
        """,
    },
    "tab_cae": {
        "biglake_table": True,
        "materialize_after_dump": True,
        "materialization_mode": "prod",
        "materialize_to_datario": False,
        "dump_to_gcs": False,
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                ID_CAE,
                DSC_CAE,
                ID_TipoAtividade,
                DSC_TipoAtividade
            FROM DW_BI_ALVARAS.dbo.TAB_CAE;
        """,
    },
    "tab_cnae": {
        "biglake_table": True,
        "materialize_after_dump": True,
        "materialization_mode": "prod",
        "materialize_to_datario": False,
        "dump_to_gcs": False,
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                ID_CNAE,
                DSC_CNAE
            FROM DW_BI_ALVARAS.dbo.TAB_CNAE;
        """,
    },
    "tab_cnae_tmp": {
        "biglake_table": True,
        "materialize_after_dump": True,
        "materialization_mode": "prod",
        "materialize_to_datario": False,
        "dump_to_gcs": False,
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                ID_CNAE,
                DSC_CNAE
            FROM DW_BI_ALVARAS.dbo.TAB_CNAE_TMP;
        """,
    },
    "tab_consulta": {
        "biglake_table": True,
        "materialize_after_dump": True,
        "materialization_mode": "prod",
        "materialize_to_datario": False,
        "dump_to_gcs": False,
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                ID_Consulta,
                DSC_Consulta,
                DSC_Endereco_cp,
                DSC_Bairro_cp,
                DSC_Zoneamento_cp,
                DSC_CodeConsulta,
                DSC_IRLF_cp,
                DSC_StatusCPL_cp,
                DSC_TipoAnalise_cp,
                DSC_Status_cp
            FROM DW_BI_ALVARAS.dbo.TAB_Consulta;
        """,
    },
    "tab_direcionamento": {
        "biglake_table": True,
        "materialize_after_dump": True,
        "materialization_mode": "prod",
        "materialize_to_datario": False,
        "dump_to_gcs": False,
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                ID_Direcionamento,
                DSC_Direcionamento
            FROM DW_BI_ALVARAS.dbo.TAB_Direcionamento;
        """,
    },
    "tab_tipocontribuinte_tipocontribuint": {
        "biglake_table": True,
        "materialize_after_dump": True,
        "materialization_mode": "prod",
        "materialize_to_datario": False,
        "dump_to_gcs": False,
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                ID_TipoContribuint,
                DSC_TipoContribuint
            FROM DW_BI_ALVARAS.dbo.TAB_TipoContribuinte_TipoContribuint;
        """,
    },
    "tab_tiposolicitacao": {
        "biglake_table": True,
        "materialize_after_dump": True,
        "materialization_mode": "prod",
        "materialize_to_datario": False,
        "dump_to_gcs": False,
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                ID_TipoSolicitacao,
                DSC_TipoSolicitacao
            FROM DW_BI_ALVARAS.dbo.TAB_TipoSolicitacao;
        """,
    },
}

alvaras_infra_clocks = generate_dump_db_schedules(
    interval=timedelta(days=1),
    start_date=datetime(2022, 3, 21, 2, 0, tzinfo=pytz.timezone("America/Sao_Paulo")),
    labels=[
        constants.RJ_IPLANRIO_AGENT_LABEL.value,
    ],
    db_database="DW_BI_ALVARAS",
    db_host="10.70.15.11",
    db_port="1433",
    db_type="sql_server",
    dataset_id="alvaras",
    infisical_secret_path="/db-alvaras",
    table_parameters=_alvaras_infra_query,
)

alvaras_infra_daily_update_schedule = Schedule(clocks=untuple(alvaras_infra_clocks))
