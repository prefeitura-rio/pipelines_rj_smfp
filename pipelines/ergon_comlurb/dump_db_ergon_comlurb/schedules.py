# -*- coding: utf-8 -*-
# pylint: disable=C0302
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
    "cargo": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "dbt_alias": True,
        "execute_query": """
            SELECT
                CARGO,
                NOME,
                CATEGORIA,
                SUBCATEGORIA,
                DT_EXTINCAO,
                CONTROLE_VAGA,
                POR_REFER,
                E_AGLUTINADOR,
                CARGO_AGLUT,
                TIPO_CARGO,
                CARGO_FUNCAO,
                ESCOLARIDADE,
                FLEX_CAMPO_01,
                FLEX_CAMPO_02,
                FLEX_CAMPO_03,
                FLEX_CAMPO_04,
                FLEX_CAMPO_05,
                FLEX_CAMPO_06,
                FLEX_CAMPO_07,
                FLEX_CAMPO_08,
                FLEX_CAMPO_09,
                FLEX_CAMPO_10,
                FLEX_CAMPO_11,
                FLEX_CAMPO_12,
                FLEX_CAMPO_13,
                FLEX_CAMPO_14,
                FLEX_CAMPO_15,
                FLEX_CAMPO_16,
                FLEX_CAMPO_17,
                FLEX_CAMPO_18,
                FLEX_CAMPO_19,
                FLEX_CAMPO_20,
                FLEX_CAMPO_21,
                FLEX_CAMPO_22,
                FLEX_CAMPO_23,
                FLEX_CAMPO_24,
                FLEX_CAMPO_25,
                FLEX_CAMPO_26,
                FLEX_CAMPO_27,
                FLEX_CAMPO_28,
                FLEX_CAMPO_29,
                FLEX_CAMPO_30,
                FLEX_CAMPO_31,
                FLEX_CAMPO_32,
                FLEX_CAMPO_33,
                FLEX_CAMPO_34,
                FLEX_CAMPO_35,
                FLEX_CAMPO_36,
                FLEX_CAMPO_37,
                FLEX_CAMPO_38,
                FLEX_CAMPO_39,
                FLEX_CAMPO_40,
                FLEX_CAMPO_41,
                FLEX_CAMPO_42,
                FLEX_CAMPO_43,
                FLEX_CAMPO_44,
                FLEX_CAMPO_45,
                FLEX_CAMPO_46,
                FLEX_CAMPO_47,
                FLEX_CAMPO_48,
                FLEX_CAMPO_49,
                FLEX_CAMPO_50,
                PONTPUBL,
                FLEX_CAMPO_51,
                FLEX_CAMPO_52,
                FLEX_CAMPO_53,
                FLEX_CAMPO_54,
                FLEX_CAMPO_55,
                DT_CONTROLE_ACUM,
                PONTLEI,
                DT_INICIO_CONTR_VAGA,
                ID_REG
            FROM ERGON.CARGOS_
        """,
    },
    "dependente": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "dbt_alias": True,
        "execute_query": """
            SELECT
                NUMFUNC,
                NUMERO,
                NOME,
                SEXO,
                DTNASC,
                PARENTESCO,
                CPF,
                TIPOLOGENDER,
                NOMELOGENDER,
                NUMENDER,
                COMPLENDER,
                BAIRROENDER,
                CIDADEENDER,
                UFENDER,
                CEPENDER,
                TELEFONE,
                BANCO,
                AGENCIA,
                CONTA,
                TIPOPAG,
                FOTO,
                NUMFUNCDEP,
                PONTPUBL,
                NUM_CERT,
                LIVRO_A_CERT,
                FOLHA_CERT,
                CARTORIO_CERT,
                FLEX_CAMPO_01,
                FLEX_CAMPO_02,
                FLEX_CAMPO_03,
                FLEX_CAMPO_04,
                FLEX_CAMPO_05,
                FLEX_CAMPO_06,
                FLEX_CAMPO_07,
                FLEX_CAMPO_08,
                FLEX_CAMPO_09,
                FLEX_CAMPO_10,
                REPRESENTANTE_LEGAL,
                NUM_REPR_LEGAL,
                FLEX_CAMPO_11,
                FLEX_CAMPO_12,
                FLEX_CAMPO_13,
                FLEX_CAMPO_14,
                FLEX_CAMPO_15,
                FLEX_CAMPO_16,
                FLEX_CAMPO_17,
                FLEX_CAMPO_18,
                FLEX_CAMPO_19,
                FLEX_CAMPO_20,
                UF_CART,
                MUNICIPIO_CART,
                TIPODOC_CERT,
                NUMRG,
                TIPORG,
                ORGAORG,
                UFRG,
                TIPODOC_CERT_FIM,
                DT_CERT_FIM,
                NUM_CERT_FIM,
                LIVRO_CERT_FIM,
                FOLHA_CERT_FIM,
                CARTORIO_CERT_FIM,
                UF_CART_FIM,
                MUNICIPIO_CART_FIM,
                EXPEDRG,
                FLEX_CAMPO_21,
                FLEX_CAMPO_22,
                FLEX_CAMPO_23,
                FLEX_CAMPO_24,
                FLEX_CAMPO_25,
                FLEX_CAMPO_26,
                FLEX_CAMPO_27,
                FLEX_CAMPO_28,
                FLEX_CAMPO_29,
                FLEX_CAMPO_30,
                FLEX_CAMPO_31,
                FLEX_CAMPO_32,
                FLEX_CAMPO_33,
                FLEX_CAMPO_34,
                FLEX_CAMPO_35,
                FLEX_CAMPO_36,
                FLEX_CAMPO_37,
                FLEX_CAMPO_38,
                FLEX_CAMPO_39,
                FLEX_CAMPO_40,
                MATRICULA_CERT,
                MATRICULA_CERT_FIM,
                ID_PESSOA,
                CIDADEENDER_COD,
                MUNICIPIO_CART_COD,
                MUNICIPIO_CART_FIM_COD,
                NUMVINC,
                NUMPENS,
                TIPODEPEN,
                FLEX_CAMPO_41,
                FLEX_CAMPO_42,
                FLEX_CAMPO_43,
                FLEX_CAMPO_44,
                FLEX_CAMPO_45,
                ID_REG,
                PONTARQS
            FROM ERGON.DEPENDENTES
        """,
    },
    "funcionario_evento": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "dbt_alias": True,
        "execute_query": """
            SELECT
                NUMEV,
                NUMFUNC,
                NUMVINC,
                TIPOEVENTO,
                FORMAPROV,
                DTINI,
                DTFIM,
                DTINIREM,
                DTFIMREM,
                CARGO,
                SETOR,
                REFERENCIA,
                JORNADA,
                HORARIOTRAB,
                NUMEV_TIT,
                NUMFUNC_TIT,
                NUMVINC_TIT,
                NUMERO_VAGA,
                PONTPUBL,
                OBS,
                PONTLEI,
                TIPO_SUBST,
                FLEX_CAMPO_01,
                FLEX_CAMPO_02,
                FLEX_CAMPO_03,
                FLEX_CAMPO_04,
                FLEX_CAMPO_05,
                FLEX_CAMPO_06,
                FLEX_CAMPO_07,
                FLEX_CAMPO_08,
                FLEX_CAMPO_09,
                FLEX_CAMPO_10,
                EMP_CODIGO,
                PARAM_ID,
                ID_REG,
                FLEX_CAMPO_11,
                FLEX_CAMPO_12,
                FLEX_CAMPO_13,
                FLEX_CAMPO_14,
                FLEX_CAMPO_15,
                FLEX_CAMPO_16,
                FLEX_CAMPO_17,
                FLEX_CAMPO_18,
                FLEX_CAMPO_19,
                FLEX_CAMPO_20,
                FLEX_CAMPO_21,
                FLEX_CAMPO_22,
                FLEX_CAMPO_23,
                FLEX_CAMPO_24,
                FLEX_CAMPO_25,
                FLEX_CAMPO_26,
                FLEX_CAMPO_27,
                FLEX_CAMPO_28,
                FLEX_CAMPO_29,
                FLEX_CAMPO_30,
                FLEX_CAMPO_31,
                FLEX_CAMPO_32,
                FLEX_CAMPO_33,
                FLEX_CAMPO_34,
                FLEX_CAMPO_35,
                FLEX_CAMPO_36,
                FLEX_CAMPO_37,
                FLEX_CAMPO_38,
                FLEX_CAMPO_39,
                FLEX_CAMPO_40,
                FLEX_CAMPO_41,
                FLEX_CAMPO_42,
                FLEX_CAMPO_43,
                FLEX_CAMPO_44,
                FLEX_CAMPO_45,
                FLEX_CAMPO_46,
                FLEX_CAMPO_47,
                FLEX_CAMPO_48,
                FLEX_CAMPO_49,
                FLEX_CAMPO_50,
                FLEX_CAMPO_51,
                FLEX_CAMPO_52,
                FLEX_CAMPO_53,
                FLEX_CAMPO_54,
                FLEX_CAMPO_55,
                FLEX_CAMPO_56,
                FLEX_CAMPO_57,
                FLEX_CAMPO_58,
                FLEX_CAMPO_59,
                FLEX_CAMPO_60,
                FLEX_CAMPO_61,
                FLEX_CAMPO_62,
                FLEX_CAMPO_63,
                FLEX_CAMPO_64,
                FLEX_CAMPO_65,
                FLEX_CAMPO_66,
                FLEX_CAMPO_67,
                FLEX_CAMPO_68,
                FLEX_CAMPO_69,
                FLEX_CAMPO_70,
                FLEX_CAMPO_71,
                FLEX_CAMPO_72,
                FLEX_CAMPO_73,
                FLEX_CAMPO_74,
                FLEX_CAMPO_75,
                FLEX_CAMPO_76,
                FLEX_CAMPO_77,
                FLEX_CAMPO_78,
                FLEX_CAMPO_79,
                FLEX_CAMPO_80,
                ID_INGRESSO,
                PONTPROC
            FROM ERGON.EVENTO_FUNC
        """,
    },
    "ficha_financeira": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "dbt_alias": True,
        "execute_query": """
            SELECT
                MES_ANO_FOLHA,
                NUM_FOLHA,
                LANCAMENTO,
                NUMFUNC,
                NUMVINC,
                LINHA,
                NUMPENS,
                MES_ANO_DIREITO,
                RUBRICA,
                TIPO_RUBRICA,
                DESC_VANT,
                COMPLEMENTO,
                VALOR,
                CORRECAO,
                EXECUCAO,
                EMP_CODIGO
            FROM ERGON.FICHAS_FINANCEIRAS
        """,
    },
    "fita_banco": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "append",
        "lower_bound_date": "current_month",
        "partition_columns": "MES_ANO",
        "dbt_alias": True,
        "execute_query": """
            SELECT
                LANCAMENTO,
                NUMFUNC,
                NUMVINC,
                MES_ANO,
                NUMERO,
                RUBRICA,
                SETOR,
                VALORVAN,
                VALORDES,
                NUMPENS,
                NUMDEPEN,
                AGENCIA,
                BANCO,
                CONTA,
                VALORLIQ,
                TIPOPAG,
                CARGO,
                REFERENCIA,
                CENTRO_CUSTO,
                FUNCAO,
                NOME,
                SINDICATO,
                LOTE,
                EMP_CODIGO,
                FICHA,
                REGIMEJUR,
                TIPOVINC,
                DTEXERC,
                DTAPOSENT,
                DTVAC,
                CATEGORIA,
                SUBEMP_CODIGO,
                DATA_CREDITO,
                NUMREP,
                EMP_CODIGO_VINC,
                JORNADA,
                SUBCATEGORIA,
                CPF,
                SUBEMP_CODIGO_GFIP,
                FLEX_CAMPO_01,
                FLEX_CAMPO_02,
                FLEX_CAMPO_03,
                FLEX_CAMPO_04,
                FLEX_CAMPO_05,
                FLEX_CAMPO_06,
                FLEX_CAMPO_07,
                FLEX_CAMPO_08,
                FLEX_CAMPO_09,
                FLEX_CAMPO_10,
                FLEX_CAMPO_11,
                FLEX_CAMPO_12,
                FLEX_CAMPO_13,
                FLEX_CAMPO_14,
                FLEX_CAMPO_15,
                FLEX_CAMPO_16,
                FLEX_CAMPO_17,
                FLEX_CAMPO_18,
                FLEX_CAMPO_19,
                FLEX_CAMPO_20,
                FLEX_CAMPO_21,
                FLEX_CAMPO_22,
                FLEX_CAMPO_23,
                FLEX_CAMPO_24,
                FLEX_CAMPO_25,
                FLEX_CAMPO_26,
                FLEX_CAMPO_27,
                FLEX_CAMPO_28,
                FLEX_CAMPO_29,
                FLEX_CAMPO_30,
                NUMJUR,
                ID_PESSOA,
                TIPO_PESSOA,
                SUB_CC,
                NOME_REP,
                CPF_REP,
                TIPOPAG_REP,
                BANCO_REP,
                AGENCIA_REP,
                CONTA_REP
            FROM ERGON.FITABANCO
        """,
    },
    "frequencia": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "dbt_alias": True,
        "execute_query": """
            SELECT
                NUMFUNC,
                NUMVINC,
                DTINI,
                DTFIM,
                TIPOFREQ,
                CODFREQ,
                QUANTIDADE,
                PONTPUBL,
                OBS,
                FLEX_CAMPO_01,
                FLEX_CAMPO_02,
                FLEX_CAMPO_03,
                FLEX_CAMPO_04,
                FLEX_CAMPO_05,
                PONTLEI,
                EMP_CODIGO,
                HORA_ENTRADA,
                HORA_SAIDA,
                ID_REG,
                FLEX_CAMPO_06,
                FLEX_CAMPO_07,
                FLEX_CAMPO_08,
                FLEX_CAMPO_09,
                FLEX_CAMPO_10,
                FLEX_CAMPO_11,
                FLEX_CAMPO_12,
                FLEX_CAMPO_13,
                FLEX_CAMPO_14,
                FLEX_CAMPO_15,
                FLEX_CAMPO_16,
                FLEX_CAMPO_17,
                FLEX_CAMPO_18,
                FLEX_CAMPO_19,
                FLEX_CAMPO_20,
                FLEX_CAMPO_21,
                FLEX_CAMPO_22,
                FLEX_CAMPO_23,
                FLEX_CAMPO_24,
                FLEX_CAMPO_25,
                FLEX_CAMPO_26,
                FLEX_CAMPO_27,
                FLEX_CAMPO_28,
                FLEX_CAMPO_29,
                FLEX_CAMPO_30,
                FLEX_CAMPO_31,
                FLEX_CAMPO_32,
                FLEX_CAMPO_33,
                FLEX_CAMPO_34,
                FLEX_CAMPO_35,
                FLEX_CAMPO_36,
                FLEX_CAMPO_37,
                FLEX_CAMPO_38,
                FLEX_CAMPO_39,
                FLEX_CAMPO_40,
                FLEX_CAMPO_41,
                FLEX_CAMPO_42,
                FLEX_CAMPO_43,
                FLEX_CAMPO_44,
                FLEX_CAMPO_45,
                FLEX_CAMPO_46,
                FLEX_CAMPO_47,
                FLEX_CAMPO_48,
                FLEX_CAMPO_49,
                FLEX_CAMPO_50,
                PONTPROC
            FROM ERGON.FREQUENCIAS
        """,
    },
    "funcionario": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "dbt_alias": True,
        "execute_query": """
            SELECT
                NUMERO,
                NOME,
                SEXO,
                DTNASC,
                CIDNASC,
                UFNASC,
                G_SANGUINEO,
                PAI,
                MAE,
                ESTCIVIL,
                ESCOLARIDADE,
                NACIONALIDADE,
                CHEGBRASIL,
                UFEMPANT,
                ANOPRIMEMP,
                NUMRG,
                TIPORG,
                ORGAORG,
                UFRG,
                CPF,
                NUMCARTPRO,
                SERCARTPRO,
                UFCARTPRO,
                NUMTITEL,
                ZONATITEL,
                SECTITEL,
                UFTITEL,
                NUMDOCMILI,
                SERDOCMILI,
                CNH,
                CATCNH,
                VALIDCNH,
                UFCNH,
                PISPASEP,
                DATAPIS,
                BANCOPIS,
                INFORMARBB,
                IDENTPROF,
                TIPOIDPROF,
                TIPOLOGENDER,
                NOMELOGENDER,
                NUMENDER,
                COMPLENDER,
                BAIRROENDER,
                CIDADEENDER,
                UFENDER,
                CEPENDER,
                TELEFONE,
                BANCO,
                AGENCIA,
                CONTA,
                TIPOPAG,
                FOTO,
                PONTPUBL,
                NUM_CERT,
                LIVRO_A_CERT,
                FOLHA_CERT,
                CARTORIO_CERT,
                RAMAL,
                TRATAMENTO,
                DT_RECADAST,
                E_MAIL,
                NUMTEL_CELULAR,
                FLEX_CAMPO_01,
                FLEX_CAMPO_02,
                FLEX_CAMPO_03,
                FLEX_CAMPO_04,
                FLEX_CAMPO_05,
                FLEX_CAMPO_06,
                FLEX_CAMPO_07,
                FLEX_CAMPO_08,
                FLEX_CAMPO_09,
                FLEX_CAMPO_10,
                FLEX_CAMPO_11,
                FLEX_CAMPO_12,
                FLEX_CAMPO_13,
                FLEX_CAMPO_14,
                FLEX_CAMPO_15,
                FLEX_CAMPO_16,
                FLEX_CAMPO_17,
                FLEX_CAMPO_18,
                FLEX_CAMPO_19,
                FLEX_CAMPO_20,
                FLEX_CAMPO_21,
                FLEX_CAMPO_22,
                FLEX_CAMPO_23,
                FLEX_CAMPO_24,
                FLEX_CAMPO_25,
                FLEX_CAMPO_26,
                FLEX_CAMPO_27,
                FLEX_CAMPO_28,
                FLEX_CAMPO_29,
                FLEX_CAMPO_30,
                FLEX_CAMPO_31,
                FLEX_CAMPO_32,
                FLEX_CAMPO_33,
                FLEX_CAMPO_34,
                FLEX_CAMPO_35,
                FLEX_CAMPO_36,
                FLEX_CAMPO_37,
                FLEX_CAMPO_38,
                FLEX_CAMPO_39,
                FLEX_CAMPO_40,
                RACA,
                DEFICIENTE,
                FLAG_WEB,
                UF_CART,
                MUNICIPIO_CART,
                TIPODOC_CERT,
                UF_IDENTPROF,
                TIPODOC_CERT_FIM,
                DT_CERT_FIM,
                NUM_CERT_FIM,
                LIVRO_CERT_FIM,
                FOLHA_CERT_FIM,
                CARTORIO_CERT_FIM,
                UF_CART_FIM,
                MUNICIPIO_CART_FIM,
                EXPEDRG,
                ORGAOMILI,
                UFDOCMILI,
                TIPODEFIC,
                FLEX_CAMPO_41,
                FLEX_CAMPO_42,
                FLEX_CAMPO_43,
                FLEX_CAMPO_44,
                FLEX_CAMPO_45,
                GERA_PASEP,
                FLEX_CAMPO_46,
                FLEX_CAMPO_47,
                FLEX_CAMPO_48,
                FLEX_CAMPO_49,
                FLEX_CAMPO_50,
                ID_REG,
                US,
                MATRICULA_CERT,
                MATRICULA_CERT_FIM,
                FLEX_CAMPO_51,
                FLEX_CAMPO_52,
                FLEX_CAMPO_53,
                FLEX_CAMPO_54,
                FLEX_CAMPO_55,
                FLEX_CAMPO_56,
                FLEX_CAMPO_57,
                FLEX_CAMPO_58,
                FLEX_CAMPO_59,
                FLEX_CAMPO_60,
                FLEX_CAMPO_61,
                FLEX_CAMPO_62,
                FLEX_CAMPO_63,
                FLEX_CAMPO_64,
                FLEX_CAMPO_65,
                FLEX_CAMPO_66,
                FLEX_CAMPO_67,
                FLEX_CAMPO_68,
                FLEX_CAMPO_69,
                FLEX_CAMPO_70,
                FLEX_CAMPO_71,
                FLEX_CAMPO_72,
                FLEX_CAMPO_73,
                FLEX_CAMPO_74,
                FLEX_CAMPO_75,
                FLEX_CAMPO_76,
                FLEX_CAMPO_77,
                FLEX_CAMPO_78,
                FLEX_CAMPO_79,
                FLEX_CAMPO_80,
                FLEX_CAMPO_81,
                FLEX_CAMPO_82,
                FLEX_CAMPO_83,
                FLEX_CAMPO_84,
                FLEX_CAMPO_85,
                FLEX_CAMPO_86,
                FLEX_CAMPO_87,
                FLEX_CAMPO_88,
                FLEX_CAMPO_89,
                FLEX_CAMPO_90,
                FLEX_CAMPO_91,
                FLEX_CAMPO_92,
                FLEX_CAMPO_93,
                FLEX_CAMPO_94,
                FLEX_CAMPO_95,
                ID_PESSOA,
                FLEX_CAMPO_96,
                FLEX_CAMPO_97,
                FLEX_CAMPO_98,
                FLEX_CAMPO_99,
                FLEX_CAMPO_100,
                CATMILI,
                MUNICIPIO_CART_COD,
                MUNICIPIO_CART_FIM_COD,
                CIDADEENDER_COD,
                CIDNASC_COD,
                NOME_BUSCA,
                PONTARQS
            FROM ERGON.FUNCIONARIOS
        """,
    },
    "setor_h": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "dbt_alias": True,
        "execute_query": """
            SELECT *
            FROM ERGON.HSETOR_
        """,
    },
    "licenca_afastamento": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "dbt_alias": True,
        "execute_query": """
            SELECT
                NUMFUNC,
                NUMVINC,
                DTINI,
                DTFIM,
                TIPOFREQ,
                CODFREQ,
                MOTIVO,
                PONTPUBL,
                DTPREVFIM,
                FLEX_CAMPO_01,
                FLEX_CAMPO_02,
                FLEX_CAMPO_03,
                FLEX_CAMPO_04,
                FLEX_CAMPO_05,
                PONTLEI,
                EMP_CODIGO,
                FLEX_CAMPO_06,
                FLEX_CAMPO_07,
                FLEX_CAMPO_08,
                FLEX_CAMPO_09,
                FLEX_CAMPO_10,
                ID_REG,
                REQLICAFAST,
                RESULTPRONT,
                FLEX_CAMPO_11,
                FLEX_CAMPO_12,
                FLEX_CAMPO_13,
                FLEX_CAMPO_14,
                FLEX_CAMPO_15,
                FLEX_CAMPO_16,
                FLEX_CAMPO_17,
                FLEX_CAMPO_18,
                FLEX_CAMPO_19,
                FLEX_CAMPO_20,
                FLEX_CAMPO_21,
                FLEX_CAMPO_22,
                FLEX_CAMPO_23,
                FLEX_CAMPO_24,
                FLEX_CAMPO_25,
                FLEX_CAMPO_26,
                FLEX_CAMPO_27,
                FLEX_CAMPO_28,
                FLEX_CAMPO_29,
                FLEX_CAMPO_30,
                FLEX_CAMPO_31,
                FLEX_CAMPO_32,
                FLEX_CAMPO_33,
                FLEX_CAMPO_34,
                FLEX_CAMPO_35,
                FLEX_CAMPO_36,
                FLEX_CAMPO_37,
                FLEX_CAMPO_38,
                FLEX_CAMPO_39,
                FLEX_CAMPO_40,
                FLEX_CAMPO_41,
                FLEX_CAMPO_42,
                FLEX_CAMPO_43,
                FLEX_CAMPO_44,
                FLEX_CAMPO_45,
                PONTPROC,
                FLEX_CAMPO_46,
                FLEX_CAMPO_47,
                FLEX_CAMPO_48,
                FLEX_CAMPO_49,
                FLEX_CAMPO_50,
                FLEX_CAMPO_51,
                FLEX_CAMPO_52,
                FLEX_CAMPO_53,
                FLEX_CAMPO_54,
                FLEX_CAMPO_55,
                FLEX_CAMPO_56,
                FLEX_CAMPO_57,
                FLEX_CAMPO_58,
                FLEX_CAMPO_59,
                FLEX_CAMPO_60,
                FLEX_CAMPO_61,
                FLEX_CAMPO_62,
                FLEX_CAMPO_63,
                FLEX_CAMPO_64,
                FLEX_CAMPO_65
            FROM ERGON.LIC_AFAST
        """,
    },
    "setor": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "dbt_alias": True,
        "execute_query": """
            SELECT
                SETOR,
                DTINI,
                DTFIM,
                CENTRO_CUSTO,
                PERC_INSAL,
                PERC_PERIC,
                TIPOSETOR,
                TIPOACESSO,
                CEP,
                CODLOG,
                SINDICATO,
                TIPO_CLASSIF_FOLHA,
                CLASSIF_FOLHA,
                CARGO,
                FUNCAO,
                FLEX_CAMPO_01,
                FLEX_CAMPO_02,
                FLEX_CAMPO_03,
                FLEX_CAMPO_04,
                FLEX_CAMPO_05,
                EMP_CODIGO,
                FLEX_CAMPO_06,
                FLEX_CAMPO_07,
                FLEX_CAMPO_08,
                FLEX_CAMPO_09,
                FLEX_CAMPO_10,
                FLEX_CAMPO_11,
                FLEX_CAMPO_12,
                FLEX_CAMPO_13,
                FLEX_CAMPO_14,
                FLEX_CAMPO_15,
                PONTPUBL,
                FLEX_CAMPO_16,
                FLEX_CAMPO_17,
                FLEX_CAMPO_18,
                FLEX_CAMPO_19,
                FLEX_CAMPO_20,
                FLEX_CAMPO_21,
                FLEX_CAMPO_22,
                FLEX_CAMPO_23,
                FLEX_CAMPO_24,
                FLEX_CAMPO_25,
                PONTPROC
            FROM ERGON.SETORES_ERGON
        """,
    },
    "vantagens": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "dbt_alias": True,
        "execute_query": """
            SELECT
                NUMFUNC,
                NUMVINC,
                VANTAGEM,
                DTINI,
                DTFIM,
                VALOR,
                INFO,
                TIPO_INCORPORACAO,
                PERC_INC_FUNCAO,
                INC_TABELAVENC,
                INC_REFERENCIA,
                PERC_INC_GRAT_FUNCAO,
                INC_GRAT_TABVENC,
                INC_GRAT_REFERENCIA,
                INCORP_EXTRA_TIPOFREQ_1,
                QUANT_EXTRA_1,
                INCORP_EXTRA_TIPOFREQ_2,
                QUANT_EXTRA_2,
                OBS,
                PONTPUBL,
                VALOR2,
                INFO2,
                VALOR3,
                INFO3,
                VALOR4,
                INFO4,
                VALOR5,
                INFO5,
                VALOR6,
                INFO6,
                PONTLEI,
                FLEX_CAMPO_01,
                FLEX_CAMPO_02,
                FLEX_CAMPO_03,
                FLEX_CAMPO_04,
                FLEX_CAMPO_05,
                FLEX_CAMPO_06,
                FLEX_CAMPO_07,
                FLEX_CAMPO_08,
                FLEX_CAMPO_09,
                FLEX_CAMPO_10,
                EMP_CODIGO,
                CHAVEVANT,
                ID_REG,
                FLEX_CAMPO_11,
                FLEX_CAMPO_12,
                FLEX_CAMPO_13,
                FLEX_CAMPO_14,
                FLEX_CAMPO_15,
                FLEX_CAMPO_16,
                FLEX_CAMPO_17,
                FLEX_CAMPO_18,
                FLEX_CAMPO_19,
                FLEX_CAMPO_20,
                ID_PROC_PES,
                FLEX_CAMPO_21,
                FLEX_CAMPO_22,
                FLEX_CAMPO_23,
                FLEX_CAMPO_24,
                FLEX_CAMPO_25,
                FLEX_CAMPO_26,
                FLEX_CAMPO_27,
                FLEX_CAMPO_28,
                FLEX_CAMPO_29,
                FLEX_CAMPO_30,
                PONTPROC
            FROM ERGON.VANTAGENS
        """,
    },
    "vinculo": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "dbt_alias": True,
        "execute_query": """
            SELECT
                NUMFUNC,
                NUMERO,
                DTNOM,
                DTPOSSE,
                DTEXERC,
                REGIMEJUR,
                TIPOVINC,
                CATEGORIA,
                DESCONTA_IR,
                CORREIO,
                MOTIVO,
                CLASSIFCONC,
                DTCONC,
                DTOPFGTS,
                DTRETRFGTS,
                DTINICONTR,
                DTFIMCONTR,
                DTPRORROGCONTR,
                DTAPOSENT,
                TIPOAPOS,
                DTVAC,
                FORMAVAC,
                NUMVINCANT,
                NUMVINCPOS,
                TIPOORG_REQ,
                ORGAO_REQ,
                FUNCAO_REQ,
                FONE_REQ,
                PROJETO_ATIVIDADE,
                BANCOFGTS,
                AGENCIAFGTS,
                CONTAFGTS,
                MATRICULA,
                MATRICULA1,
                MOTIVOVAC,
                PONTPUBL,
                MATRIC,
                DT_PGTO_ATE,
                ORGAO_EXT_REQ,
                TIPO_ONUS_REQ,
                TIPO_RESSARC_REQ,
                TIPO_REQ,
                DT_SALDO_FGTS,
                VALOR_DEP_FGTS,
                FLEX_CAMPO_01,
                FLEX_CAMPO_02,
                FLEX_CAMPO_03,
                FLEX_CAMPO_04,
                FLEX_CAMPO_05,
                FLEX_CAMPO_06,
                FLEX_CAMPO_07,
                FLEX_CAMPO_08,
                FLEX_CAMPO_09,
                FLEX_CAMPO_10,
                FLEX_CAMPO_11,
                FLEX_CAMPO_12,
                FLEX_CAMPO_13,
                FLEX_CAMPO_14,
                FLEX_CAMPO_15,
                FLEX_CAMPO_16,
                FLEX_CAMPO_17,
                FLEX_CAMPO_18,
                FLEX_CAMPO_19,
                FLEX_CAMPO_20,
                PONTLEI,
                EMP_CODIGO,
                DT_HOMOLOG,
                FATOR_PROPORC_APOSENT,
                BANCO,
                AGENCIA,
                CONTA,
                FLEX_CAMPO_21,
                FLEX_CAMPO_22,
                FLEX_CAMPO_23,
                FLEX_CAMPO_24,
                FLEX_CAMPO_25,
                FLEX_CAMPO_26,
                FLEX_CAMPO_27,
                FLEX_CAMPO_28,
                FLEX_CAMPO_29,
                FLEX_CAMPO_30,
                FLEX_CAMPO_31,
                FLEX_CAMPO_32,
                FLEX_CAMPO_33,
                FLEX_CAMPO_34,
                FLEX_CAMPO_35,
                FLEX_CAMPO_36,
                FLEX_CAMPO_37,
                FLEX_CAMPO_38,
                FLEX_CAMPO_39,
                FLEX_CAMPO_40,
                FLEX_CAMPO_41,
                FLEX_CAMPO_42,
                FLEX_CAMPO_43,
                FLEX_CAMPO_44,
                FLEX_CAMPO_45,
                FLEX_CAMPO_46,
                FLEX_CAMPO_47,
                FLEX_CAMPO_48,
                FLEX_CAMPO_49,
                FLEX_CAMPO_50,
                TIPOPAG,
                ID_REG,
                DTINI_CESSAO,
                DTFIM_CESSAO,
                NUMFUNC_PERMUT_1,
                NUMERO_PERMUT_1,
                NUMFUNC_PERMUT_2,
                NUMERO_PERMUT_2,
                DTADM_RAIS,
                FLEX_CAMPO_51,
                FLEX_CAMPO_52,
                FLEX_CAMPO_53,
                FLEX_CAMPO_54,
                FLEX_CAMPO_55,
                FLEX_CAMPO_56,
                FLEX_CAMPO_57,
                FLEX_CAMPO_58,
                FLEX_CAMPO_59,
                FLEX_CAMPO_60,
                FLEX_CAMPO_61,
                FLEX_CAMPO_62,
                FLEX_CAMPO_63,
                FLEX_CAMPO_64,
                FLEX_CAMPO_65,
                FLEX_CAMPO_66,
                FLEX_CAMPO_67,
                FLEX_CAMPO_68,
                FLEX_CAMPO_69,
                FLEX_CAMPO_70,
                FLEX_CAMPO_71,
                FLEX_CAMPO_72,
                FLEX_CAMPO_73,
                FLEX_CAMPO_74,
                FLEX_CAMPO_75,
                FLEX_CAMPO_76,
                FLEX_CAMPO_77,
                FLEX_CAMPO_78,
                FLEX_CAMPO_79,
                FLEX_CAMPO_80,
                DTINICLASSE,
                DTFIMCLASSE,
                DTINIEXERC,
                DTFIMEXERC,
                ID_INGRESSO,
                MATRICULA3,
                MATRICULA2,
                PONTPROC,
                PONTARQS
            FROM ERGON.VINCULOS
        """,
    },
}


ergon_clocks = generate_dump_db_schedules(
    interval=timedelta(days=1),
    start_date=datetime(2022, 10, 25, 23, 30, tzinfo=pytz.timezone("America/Sao_Paulo")),
    labels=[
        constants.RJ_SMFP_AGENT_LABEL.value,
    ],
    db_database="P25",
    db_host="10.70.6.26",
    db_port="1521",
    db_type="oracle",
    dataset_id="recursos_humanos_ergon_comlurb",
    infisical_secret_path="/db-ergon-comlurb",
    table_parameters=ergon_queries,
)

ergon_comlurb_daily_update_schedule = Schedule(clocks=untuple(ergon_clocks))
