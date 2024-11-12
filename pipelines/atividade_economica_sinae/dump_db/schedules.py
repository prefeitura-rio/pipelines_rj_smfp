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

_alvaras_sinae_infra_query = {
    "vw_clf_arrecad": {
        "biglake_table": True,
        "materialize_after_dump": True,
        "materialization_mode": "prod",
        "materialize_to_datario": False,
        "dump_to_gcs": False,
        "dump_mode": "overwrite",
        "execute_query": """
           SELECT INSCMUNIC,
                    NUMGUIA,
                    COMPETENCIA,
                    CODRECEITA,
                    DTVENC,
                    DTPGTO,
                    TRIBUTO,
                    VLPAGO,
                    MORA,
                    MULTA,
                    BANCO,
                    PROCESSO
            FROM DW_BI_ALVARAS_SINAE.dbo.VW_CLF_ARRECAD;
        """,
    },
    "vw_clf_ativ_econ": {
        "biglake_table": True,
        "materialize_after_dump": True,
        "materialization_mode": "prod",
        "materialize_to_datario": False,
        "dump_to_gcs": False,
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT COD_GRUPO,
                    DESC_GRUPO,
                    COD_SUB_GRUPO,
                    DESC_SUB_GRUPO,
                    COD_ATIVIDADE,
                    DESC_ATIVIDADE,
                    STATUS,
                    DIVISAO
            FROM DW_BI_ALVARAS_SINAE.dbo.VW_CLF_ATIV_ECON;
        """,
    },
    "vw_clf_ativ_estabelecimento": {
        "biglake_table": True,
        "materialize_after_dump": True,
        "materialization_mode": "prod",
        "materialize_to_datario": False,
        "dump_to_gcs": False,
        "dump_mode": "overwrite",
        "execute_query": """
           SELECT   INSCMUNIC,
                    CODATIVIDADE,
                    SEQ
            FROM DW_BI_ALVARAS_SINAE.dbo.VW_CLF_ATIV_ESTABELECIMENTO;
        """,
    },
    "vw_clf_estabelecimento": {
        "biglake_table": True,
        "materialize_after_dump": True,
        "materialization_mode": "prod",
        "materialize_to_datario": False,
        "dump_to_gcs": False,
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT  INSCMUNIC,
                    CPF_CNPJ,
                    TIPO_CPF_CNPJ,
                    NOME,
                    FANTASIA,
                    TIPO_ESTAB,
                    DESC_TIPO_ESTAB,
                    STATUS,
                    CEP,
                    CL,
                    LOGRADOURO,
                    NUMERO,
                    COMPLEMENTO,
                    CB,
                    NM_BAIRRO,
                    AP,
                    ATIVPRINC,
                    DATA_ALVARA,
                    IRLF,
                    ZONEAMENTO,
                    PROC_CONCESSAO,
                    DATA_DEFERIMENTO,
                    PROC_DEFERIMENTO
            FROM DW_BI_ALVARAS_SINAE.dbo.VW_CLF_ESTABELECIMENTO;
        """,
    },
    "vw_clf_restricao_ativ_econ": {
        "biglake_table": True,
        "materialize_after_dump": True,
        "materialization_mode": "prod",
        "materialize_to_datario": False,
        "dump_to_gcs": False,
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT  INSCMUNIC,
                    CODIGO,
                    DESCRICAO
            FROM DW_BI_ALVARAS_SINAE.dbo.VW_CLF_RESTRICAO_ATIV_ECON;
        """,
    },
    "vw_clf_socio": {
        "biglake_table": True,
        "materialize_after_dump": True,
        "materialization_mode": "prod",
        "materialize_to_datario": False,
        "dump_to_gcs": False,
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT  INSCMUNIC,
                    CPF_CNPJ,
                    NOME,
                    QUALIFICACAO,
                    DESC_QUALIFICACAO,
                    IDENTIDADE,
                    UF_IDENTIDADE,
                    ORGAO_EMISSOR_IDENTIDADE,
                    PATICIPACAO,
                    CL,
                    NUM_PORTA,
                    COMPLEMENTO,
                    LOGRADOURO,
                    BAIRRO,
                    CEP,
                    MUNICIPIO,
                    UF,
                    PAIS
            FROM DW_BI_ALVARAS_SINAE.dbo.VW_CLF_SOCIO;
        """,
    },
    "vw_clf_status_contribuinte_iss": {
        "biglake_table": True,
        "materialize_after_dump": True,
        "materialization_mode": "prod",
        "materialize_to_datario": False,
        "dump_to_gcs": False,
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT  CODIGO,
                    DESCRICAO,
                    STATUS
            FROM DW_BI_ALVARAS_SINAE.dbo.VW_CLF_STATUS_CONTRIBUINTE_ISS;
        """,
    },
    "vw_codigo_receita_smf": {
        "biglake_table": True,
        "materialize_after_dump": True,
        "materialization_mode": "prod",
        "materialize_to_datario": False,
        "dump_to_gcs": False,
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT  CODIGO,
                    DESCRICAO
            FROM DW_BI_ALVARAS_SINAE.dbo.VW_CODIGO_RECEITA_SMF;
        """,
    },
}

alvaras_sinae_infra_clocks = generate_dump_db_schedules(
    interval=timedelta(days=1),
    start_date=datetime(2022, 3, 21, 2, 0, tzinfo=pytz.timezone("America/Sao_Paulo")),
    labels=[
        constants.RJ_SMFP_AGENT_LABEL.value,
    ],
    db_database="DW_BI_ALVARAS_SINAE",
    db_host="10.70.15.11",
    db_port="1433",
    db_type="sql_server",
    dataset_id="atividade_economica_sinae",
    infisical_secret_path="/db-alvaras",
    table_parameters=_alvaras_sinae_infra_query,
)

alvaras_sinae_infra_daily_update_schedule = Schedule(clocks=untuple(alvaras_sinae_infra_clocks))
