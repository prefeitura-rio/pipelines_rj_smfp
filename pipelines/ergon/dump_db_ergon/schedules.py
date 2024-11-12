# -*- coding: utf-8 -*-
# flake8: noqa: E501
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
# Ergon Schedules
#
#####################################

ergon_queries = {
    "cargo": {
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
    "categoria": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                SIGLA, NOME, PONTLEI, PONTPUBL
            FROM C_ERGON.VW_DLK_ERG_CATEGORIAS_
        """,
    },
    "empresa": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                EMPRESA, NOME, FANTASIA,
                RAZAO, CGC, NUMENDER, COMPLEMENTO,
                CEP, DDD, FONE, EMAIL, WEB, FAX, RAMAL,
                CAIXA_POSTAL, ATIV_ECON, CNAE, NAT_JUR, RESPONSAVEL,
                CPF_RESP, CGC_DECLARANTE, MUNICIPIO_CODIGO, UF_SIGLA,
                MBAIRRO_CODIGO, LOG_CODIGO, BANCO, AGENCIA, CONTA, FLEX_CAMPO_03,
                FLEX_CAMPO_04, FLEX_CAMPO_05, FLEX_CAMPO_06, FLEX_CAMPO_07, FLEX_CAMPO_08,
                PONTPUBL, ID_DOCUMENTO, TIPOLOGRADOURO, NOMELOGRADOURO, MUNICIPIO, PONTPROC,
                ID_REG
            FROM C_ERGON.VW_DLK_ERG_EMPRESAS
        """,
    },
    "matricula": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                NUMFUNC, MATRIC
            FROM C_ERGON.VW_DLK_ERG_ERG_MATRICULAS
        """,
    },
    "fita_banco": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "partition_columns": "MES_ANO",
        "dump_mode": "append",
        "break_query_frequency": "month",
        "break_query_start": "current_month",
        "break_query_end": "current_month",
        "execute_query": """
            SELECT
                LANCAMENTO, NUMFUNC, NUMVINC, MES_ANO, NUMERO, RUBRICA, SETOR,
                VALORVAN, VALORDES, NUMPENS, NUMDEPEN, AGENCIA, BANCO, CONTA, VALORLIQ, TIPOPAG,
                CARGO, REFERENCIA, CENTRO_CUSTO, FUNCAO, NOME, SINDICATO, LOTE, EMP_CODIGO, FICHA,
                REGIMEJUR, TIPOVINC, DTEXERC, DTAPOSENT, DTVAC, CATEGORIA, SUBEMP_CODIGO, DATA_CREDITO,
                NUMREP, EMP_CODIGO_VINC, JORNADA, SUBCATEGORIA, CPF, SUBEMP_CODIGO_GFIP, FLEX_CAMPO_01,
                FLEX_CAMPO_02, FLEX_CAMPO_05, NUMJUR, ID_PESSOA, TIPO_PESSOA, SUB_CC, NOME_REP, CPF_REP,
                TIPOPAG_REP, BANCO_REP, AGENCIA_REP, CONTA_REP
            FROM C_ERGON.VW_DLK_ERG_FITA_BANCO
        """,
    },
    "folha_empresa": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "partition_columns": "MES_ANO",
        "dump_mode": "append",
        "break_query_frequency": "month",
        "break_query_start": "current_month",
        "break_query_end": "current_month",
        "execute_query": """
            SELECT
                MES_ANO, NUMERO, EMP_CODIGO, TIPO_FOLHA, NOME, DATA_ABER,
                MES_PRINCIPAL, MESES_RETRO, MESES_RETRO_FULL, MESES_ADIANT,
                MESES_PRE_ERGON, DATA_PROC, DATA_CONSOL, RESPONSAVEL, TIPO_CALCULO,
                DATA_CREDITO, DESTINO, EXPIRACAO, FLEX_CAMPO_01, FLEX_CAMPO_02, NUMERO_SEC,
                GRUPO_EMPRESAS, CLASSE_CALCULO, CLASSE_ESTORNO, DATA_LIMITES, ID_GRUPO_FOL_SEG,
                DATA_GERAELEITOS, DATA_GERAELEITOS_ANT, NUMERO_TERC, ID_REG
            FROM C_ERGON.VW_DLK_ERG_FOLHAS_EMP
        """,
    },
    "forma_provimento": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                SIGLA, NOME, INATIVO, OCUPA_QUADRO, TIPO_PERIODO, INICIAL, PRORROGACAO,
                MAX_INTERRUP, DURACAO, PRIMEIRO_PROV, ATIVO, PONTLEI, TIPO_RELAC,
                PERMITE_REGRESSAO
            FROM C_ERGON.VW_DLK_ERG_FORMAS_PROV_
        """,
    },
    "funcionario": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                NUMERO, NOME, SEXO, DTNASC, CIDNASC, UFNASC, G_SANGUINEO, PAI,
                MAE, ESTCIVIL, ESCOLARIDADE, NACIONALIDADE, CHEGBRASIL, UFEMPANT,
                ANOPRIMEMP, NUMRG, TIPORG, ORGAORG, UFRG, CPF, NUMCARTPRO, SERCARTPRO,
                UFCARTPRO, NUMTITEL, ZONATITEL, SECTITEL, UFTITEL, NUMDOCMILI, SERDOCMILI,
                CNH, CATCNH, VALIDCNH, UFCNH, PISPASEP, DATAPIS, BANCOPIS, INFORMARBB, IDENTPROF,
                TIPOIDPROF, TIPOLOGENDER, NOMELOGENDER, NUMENDER, COMPLENDER, BAIRROENDER,
                CIDADEENDER, UFENDER, CEPENDER, TELEFONE, BANCO, AGENCIA, CONTA, TIPOPAG,
                FOTO, PONTPUBL, NUM_CERT, LIVRO_A_CERT, FOLHA_CERT, CARTORIO_CERT, RAMAL,
                TRATAMENTO, DT_RECADAST, E_MAIL, NUMTEL_CELULAR, FLEX_CAMPO_01, FLEX_CAMPO_02,
                FLEX_CAMPO_03, FLEX_CAMPO_04, FLEX_CAMPO_05, FLEX_CAMPO_06, FLEX_CAMPO_07, FLEX_CAMPO_08,
                FLEX_CAMPO_09, FLEX_CAMPO_10, FLEX_CAMPO_11, FLEX_CAMPO_12, FLEX_CAMPO_13, FLEX_CAMPO_14,
                FLEX_CAMPO_15, FLEX_CAMPO_16, FLEX_CAMPO_17, FLEX_CAMPO_18, FLEX_CAMPO_19, FLEX_CAMPO_20, FLEX_CAMPO_21,
                FLEX_CAMPO_22, FLEX_CAMPO_23, FLEX_CAMPO_24, FLEX_CAMPO_25, FLEX_CAMPO_26, FLEX_CAMPO_27, FLEX_CAMPO_28,
                FLEX_CAMPO_29, FLEX_CAMPO_30, FLEX_CAMPO_31, FLEX_CAMPO_32, FLEX_CAMPO_33, FLEX_CAMPO_34, FLEX_CAMPO_35,
                FLEX_CAMPO_36, FLEX_CAMPO_37, FLEX_CAMPO_38, FLEX_CAMPO_39, FLEX_CAMPO_40, RACA, DEFICIENTE, FLAG_WEB,
                UF_CART, MUNICIPIO_CART, TIPODOC_CERT, UF_IDENTPROF, TIPODOC_CERT_FIM, DT_CERT_FIM, NUM_CERT_FIM,
                LIVRO_CERT_FIM, FOLHA_CERT_FIM, CARTORIO_CERT_FIM, UF_CART_FIM, MUNICIPIO_CART_FIM, EXPEDRG, ORGAOMILI,
                UFDOCMILI, TIPODEFIC, FLEX_CAMPO_41, FLEX_CAMPO_42, FLEX_CAMPO_43, FLEX_CAMPO_44, FLEX_CAMPO_45, GERA_PASEP,
                FLEX_CAMPO_46, FLEX_CAMPO_47, FLEX_CAMPO_48, FLEX_CAMPO_49, FLEX_CAMPO_50, ID_REG, US, MATRICULA_CERT, MATRICULA_CERT_FIM,
                FLEX_CAMPO_51, FLEX_CAMPO_52, FLEX_CAMPO_53, FLEX_CAMPO_54, FLEX_CAMPO_55, FLEX_CAMPO_56, FLEX_CAMPO_57, FLEX_CAMPO_58,
                FLEX_CAMPO_59, FLEX_CAMPO_60, FLEX_CAMPO_61, FLEX_CAMPO_62, FLEX_CAMPO_63, FLEX_CAMPO_64, FLEX_CAMPO_65, FLEX_CAMPO_66,
                FLEX_CAMPO_67, FLEX_CAMPO_68, FLEX_CAMPO_69, FLEX_CAMPO_70, FLEX_CAMPO_71, FLEX_CAMPO_72, FLEX_CAMPO_73, FLEX_CAMPO_74,
                FLEX_CAMPO_75, FLEX_CAMPO_76, FLEX_CAMPO_77, FLEX_CAMPO_78, FLEX_CAMPO_79, FLEX_CAMPO_80, FLEX_CAMPO_81, FLEX_CAMPO_82,
                FLEX_CAMPO_83, FLEX_CAMPO_84, FLEX_CAMPO_85, FLEX_CAMPO_86, FLEX_CAMPO_87, FLEX_CAMPO_88, FLEX_CAMPO_89, FLEX_CAMPO_90,
                FLEX_CAMPO_91, FLEX_CAMPO_92, FLEX_CAMPO_93, FLEX_CAMPO_94, FLEX_CAMPO_95, ID_PESSOA, FLEX_CAMPO_96, FLEX_CAMPO_97,
                FLEX_CAMPO_98, FLEX_CAMPO_99, FLEX_CAMPO_100, CATMILI, MUNICIPIO_CART_COD, MUNICIPIO_CART_FIM_COD, CIDADEENDER_COD, CIDNASC_COD
            FROM C_ERGON.VW_DLK_ERG_FUNCIONARIOS
        """,
    },
    "horario_trabalho": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                CODIGO, DESCRICAO, FLEX_CAMPO_01, FLEX_CAMPO_02,
                PONTLEI, CARGA_HR_MES, CARGA_HR_SEMANA, CARGA_HR_DIA, ID_REG
            FROM C_ERGON.VW_DLK_ERG_HORARIO_TRAB_
        """,
    },
    "setor": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                DATAINI, SETOR, NOMESETOR, PAISETOR, TIPOSETOR,
                DATAFIM, TIPOLOG, NOMELOG, NUMEROLOG, COMPLEMENTO,
                BAIRRO, CIDADE, UF, FONE, FAX, CENTRO_CUSTO,
                TIPOACESSO, TIPOLOGIA, OBS, MBAIRRO_MUNICIPIO_CODIGO,
                MBAIRRO_CODIGO, CGC, HLOCAL, PAISETOR1, PAISETOR2, PAISETOR3,
                PAISETOR4, EMP_CODIGO, SUBEMP_CODIGO, FLEX_CAMPO_01, FLEX_CAMPO_02,
                FLEX_CAMPO_05, EXTINTO, FLEX_CAMPO_14, FLEX_CAMPO_15, PONTPUBL,
                REPLACE(REPLACE(NOMESETORLONGO, CHR(13), ''), CHR(10), '') AS NOMESETORLONGO,
                CIDADE_COD, CEP
            FROM C_ERGON.VW_DLK_ERG_HSETOR_
        """,
    },
    "jornada": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                SIGLA, NOME, HORASSEM, HORASMEN, PONTLEI
            FROM C_ERGON.VW_DLK_ERG_JORNADAS_
        """,
    },
    "orgaos_externos": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                ORGAO, DESCR, TIPOLOG, NOMELOG, NUMEROLOG, COMPLEMENTO,
                BAIRRO, CEP, CIDADE, UF, FAX, FONE, CGC, TIPO_ORGAO,
                PONTLEI, ID_PESSOA_PJ, DDDFONE, DDDFAX, CIDADE_COD
            FROM C_ERGON.VW_DLK_ERG_ORGAOS_EXTERNOS
        """,
    },
    "orgaos_regime_juridico": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                SIGLA, NOME, PONTLEI
            FROM C_ERGON.VW_DLK_ERG_ORGAOS_REGIMES_JUR_
        """,
    },
    "provimento": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                NUMFUNC, NUMVINC, DTINI, DTFIM, SETOR, CARGO,
                REFERENCIA, JORNADA, FORMAPROV, HORARIOTRAB, PONTPUBL,
                NUMERO_VAGA, OBS, PONTLEI, FLEX_CAMPO_03, FLEX_CAMPO_04,
                FLEX_CAMPO_05, EMP_CODIGO, FLEX_CAMPO_20
            FROM C_ERGON.VW_DLK_ERG_PROVIMENTOS_EV
        """,
    },
    "regime_juridico": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                SIGLA, NOME, PONTLEI
            FROM C_ERGON.VW_DLK_ERG_REGIMES_JUR_
        """,
    },
    "tipo_folha": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                TIPO, NOME, E_NORMAL, E_FERIAS, E_SUPLEMENTAR, E_DECTER, E_ADIANT,
                E_ADIANT13, E_RESCISAO, PROC_CONSIG, PROC_MOV, E_AVULSA, E_COMPLEMENTAR,
                E_ADIANTFER, E_MULTIPLA, PROC_RETRO, DESABILITA_ALT, VISIVEL_PARA_DIF,
                E_ESTORNO, PAGAVEL, MES_PRINCIPAL, MESES_RETRO, MESES_RETRO_FULL, MESES_ADIANT,
                PROC_ATIVOS, PROC_INATIVOS, PROC_DESLIGADOS, EXPIRACAO, MES_INICIAL, CALCULAVEL,
                MESES_PRE_ERGON, E_VACFALEC, PER_LIQ_NEG, VISIBILIDADE_DIRF, VISIBILIDADE_RAIS,
                FINALIDADE_CALCULO, UTILIZA_HIST_PAGTO, GRUPO_TIPO_FOLHA, PROC_PARCEL, INDICADOR_01,
                INDICADOR_02, INDICADOR_03, INDICADOR_04, INDICADOR_05, INDICADOR_06, INDICADOR_07,
                INDICADOR_08, INDICADOR_09, INDICADOR_10, GRP_NULO_FOLPARCIAL, PREVALENCIA,
                TER_SECUNDARIA, TER_TERCIARIA
            FROM C_ERGON.VW_DLK_ERG_TIPO_FOLHA
        """,
    },
    "tipo_orgao": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                TIPO, DESCR, PONTLEI
            FROM C_ERGON.VW_DLK_ERG_TIPO_ORGAO
        """,
    },
    "tipo_vinculo": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                SIGLA, NOME, E_COMIS, E_ESPECIAL, E_MANDATO,
                E_REQUIS, IDADE_MINIMA, PONTLEI, TIPO_EVENTO_BASE
            FROM C_ERGON.VW_DLK_ERG_TIPO_VINC_
        """,
    },
    "vinculo": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                NUMFUNC, NUMERO, DTNOM, DTPOSSE, DTEXERC, REGIMEJUR, TIPOVINC,
                CATEGORIA, DESCONTA_IR, CORREIO, MOTIVO, CLASSIFCONC, DTCONC, DTOPFGTS,
                DTRETRFGTS, DTINICONTR, DTFIMCONTR, DTPRORROGCONTR, DTAPOSENT, TIPOAPOS,
                DTVAC, FORMAVAC, NUMVINCANT, NUMVINCPOS, TIPOORG_REQ, ORGAO_REQ, FUNCAO_REQ,
                FONE_REQ, PROJETO_ATIVIDADE, BANCOFGTS, AGENCIAFGTS, CONTAFGTS, MATRICULA,
                MATRICULA1, MOTIVOVAC, PONTPUBL, MATRIC, ORGAO_EXT_REQ, TIPO_ONUS_REQ,
                TIPO_RESSARC_REQ, TIPO_REQ, DT_PGTO_ATE, DT_SALDO_FGTS, VALOR_DEP_FGTS,
                FLEX_CAMPO_01, FLEX_CAMPO_02, FLEX_CAMPO_03, FLEX_CAMPO_04, FLEX_CAMPO_05,
                FLEX_CAMPO_06, FLEX_CAMPO_07, FLEX_CAMPO_08, FLEX_CAMPO_09, FLEX_CAMPO_10,
                FLEX_CAMPO_11, FLEX_CAMPO_12, FLEX_CAMPO_13, FLEX_CAMPO_14, FLEX_CAMPO_15,
                FLEX_CAMPO_16, FLEX_CAMPO_17, FLEX_CAMPO_18, FLEX_CAMPO_19, FLEX_CAMPO_20,
                PONTLEI, EMP_CODIGO, DT_HOMOLOG, FATOR_PROPORC_APOSENT, BANCO, AGENCIA, CONTA,
                TIPOPAG, ID_REG, DTINI_CESSAO, DTFIM_CESSAO, NUMFUNC_PERMUT_1, NUMERO_PERMUT_1,
                NUMFUNC_PERMUT_2, NUMERO_PERMUT_2, DTADM_RAIS, DTINICLASSE, DTFIMCLASSE, DTINIEXERC,
                DTFIMEXERC, ID_INGRESSO, MATRICULA3, MATRICULA2, PONTPROC
            FROM C_ERGON.VW_DLK_ERG_VINCULOS
        """,
    },
    "licenca_afastamento": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "partition_columns": "DTINI",
        "dump_mode": "append",
        "break_query_frequency": "month",
        "break_query_start": "current_month",
        "break_query_end": "current_month",
        "execute_query": """
        SELECT
            NUMFUNC,NUMVINC,DTINI,DTFIM,TIPOFREQ,CODFREQ,MOTIVO,DTPREVFIM,FLEX_CAMPO_01,
            FLEX_CAMPO_02,EMP_CODIGO,FLEX_CAMPO_07
        FROM ERGON.LIC_AFAST
        """,
    },
    "frequencia": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "partition_columns": "DTINI",
        "dump_mode": "append",
        "break_query_frequency": "month",
        "break_query_start": "current_month",
        "break_query_end": "current_month",
        "execute_query": """
            SELECT
                NUMFUNC,NUMVINC,DTINI,DTFIM,TIPOFREQ,CODFREQ,OBS,EMP_CODIGO
            FROM ERGON.FREQUENCIAS
        """,
    },
    "vantagens": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "partition_columns": "DTINI",
        "dump_mode": "append",
        "break_query_frequency": "month",
        "break_query_start": "current_month",
        "break_query_end": "current_month",
        "execute_query": """
        SELECT
            NUMFUNC,NUMVINC,VANTAGEM,DTINI,DTFIM,VALOR,INFO,TIPO_INCORPORACAO,PERC_INC_FUNCAO,
            INC_TABELAVENC,INC_REFERENCIA,OBS,VALOR2,INFO2,VALOR3,INFO3,VALOR4,INFO4,VALOR5,INFO5,
            VALOR6,INFO6,FLEX_CAMPO_05,EMP_CODIGO,CHAVEVANT
        FROM ERGON.VANTAGENS
        """,
    },
    "total_contagem": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
        SELECT CHAVE,
            NUMFUNC,NUMVINC,FINALIDADE,DIASTOT,DIASFPUB,DIASFPUBESP,TOTAL_PERIODOS,
            TOTAL_ANOS,DATA_PROXIMO,NOME_PROXIMO,EMP_CODIGO
        FROM ERGON.TOTAL_CONTA
        """,
        "interval": timedelta(days=15),
    },
    "pre_contagem": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                FINALIDADE,NUMFUNC,NUMVINC,PERIODOS,OFFSET,DTINI,EMP_CODIGO,FLEX_CAMPO_01
            FROM ERGON.PRE_CONTA
        """,
    },
    "averbacoes": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                NUMFUNC,NUMVINC,CHAVE,DTINI,DTFIM,INSTITUICAO,TIPOTEMPO,DATA_A_CONTAR,TOTAL_DIAS,
                MOTIVO,SOBREPOE,EMP_CODIGO,OBS,REGPREV
            FROM ERGON.AVERBACOES_CONTA
        """,
    },
    "averbacoes_contagem": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                NUMFUNC,NUMVINC,CHAVEAVERB,FINALIDADE,DIAS,EMP_CODIGO
            FROM ERGON.AVERB_OQUE_CONTA
        """,
    },
    "frequencia_antigo": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                M9, SF_OCORRENCIA, SF_DT_OC_Y2
            FROM C_ERGON.VW_SIMPA_SIRHU_FREQUENCIA_GBP
        """,
    },
    "afastamento_antigo": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                M10, SA_DT_AFAS_Y2, SA_DT_PRER_Y2, SA_DT_RETR_Y2
            FROM C_ERGON.VW_SIMPA_SIRHU_AFASTAMENTO_GBP
        """,
    },
    "afastamento_antigo_nomes": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                EMP_CODIGO, AFAST_COD, AFAST_DESCR
            FROM SIMPA.SIRHU_DBTABELAS_AFASTAMENTO
        """,
    },
    "tipo_tempo": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                SIGLA, NOME, APOSENTADORIA, FERIAS, DIAS_FER, ADICTSERV, LICESP, DIAS_LICESP,
                ADICTCHEFIA, PROGRESSAO
            FROM ERGON.TIPO_TEMPO
        """,
    },
    "ficha_financeira": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "append",
        "break_query_frequency": "month",
        "break_query_start": "current_month",
        "break_query_end": "current_month",
        "partition_columns": "MES_ANO_FOLHA",
        "execute_query": """
            SELECT
                MES_ANO_FOLHA,NUM_FOLHA,LANCAMENTO,NUMFUNC,NUMVINC,NUMPENS,MES_ANO_DIREITO,
                RUBRICA,TIPO_RUBRICA,DESC_VANT,COMPLEMENTO,VALOR,CORRECAO,EXECUCAO,EMP_CODIGO
            FROM ERGON.FICHAS_FINANCEIRAS
        """,
    },
    "ficha_financeira_contabil": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "append",
        "break_query_frequency": "month",
        "break_query_start": "current_month",
        "break_query_end": "current_month",
        "partition_columns": "MES_ANO_FOLHA",
        "execute_query": """
        SELECT
            MES_ANO_FOLHA,NUM_FOLHA,NUMFUNC,NUMVINC,NUMPENS,SETOR,SECRETARIA,TIPO_FUNC,
            ATI_INAT_PENS,DETALHA,RUBRICA,TIPO_RUBRICA,MES_ANO_DIREITO,DESC_VANT,VALOR,COMPLEMENTO,
            TIPO_CLASSIF,CLASSIFICACAO,TIPO_CLASSIF_FR,CLASSIF_FR,ELEMDESP,TIPORUB,EMP_CODIGO
        FROM ERGON.IPL_PT_FICHAS
        """,
    },
    "rubrica": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                RUBRICA, NOME, MNEMONICO, NOME_ABREV,
                TIPORUBR, FAT_VANT, FAT_IR, FAT_PREV,
                FAT_IRFER, FAT_PREVFER, FAT_RAIS, E_CONS,
                E_PA, E_SALFAM, E_IR, E_PREV, COMISSAO,
                FLEX_CAMPO_01, FLEX_CAMPO_02, FLEX_CAMPO_03,
                FLEX_CAMPO_04, FLEX_CAMPO_05, RUB, USA_COMPLEMENTO,
                FORMULA_PADRAO_02, FORMULA_PADRAO_12, PONTLEI, SQL_LOVCOMPL,
                VALIDA_COMPL_BD, FORMATO_COMPLEMENTO, FORMULA_PADRAO_02PER,
                FORMULA_PADRAO_12PER, MODALIDADE_CALCULO, FLEX_CAMPO_06,
                FLEX_CAMPO_07, FLEX_CAMPO_08, FLEX_CAMPO_09, FLEX_CAMPO_10,
                PONTPUBL, FAT_VANT_REPASSE, E_REPASSE, FLEX_CAMPO_11, FLEX_CAMPO_12,
                FLEX_CAMPO_13, FLEX_CAMPO_14, FLEX_CAMPO_15, FLEX_CAMPO_16, FLEX_CAMPO_17,
                FLEX_CAMPO_18, FLEX_CAMPO_19, FLEX_CAMPO_20, ID_REG
            FROM ERGON.RUBRICAS
        """,
    },
    "inscritos": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                CHAVE, CHAVE_VAGA, IDENTIFICACAO, NOME,
                NUMVINC, NUMFUNC, CONVOCACAO, NOMEACAO, POSSE,
                DESISTENCIA, CLASSIFICACAO, DEFICIENTE, SEXO, DATA_NASCIMENTO,
                ESTADO_CIVIL, TIPORG, ORGAORG, NUMRG, UFRG, CPF, TIPOLOGENDER, NOMELOGENDER,
                NUMENDER, COMPLENDER, BAIRROENDER, CIDADEENDER, UFENDER, CEPENDER,
                PONTOS_TITULO, EMP_CODIGO, FLEX_CAMPO_01, FLEX_CAMPO_02, FLEX_CAMPO_03,
                FLEX_CAMPO_04, FLEX_CAMPO_05, NACIONALIDADE, ORDEM_CHAMADA, SETOR, PONTPUBL,
                DT_EMISSAO_RG, FLEX_CAMPO_06, FLEX_CAMPO_07, FLEX_CAMPO_08, FLEX_CAMPO_09,
                FLEX_CAMPO_10, FLEX_CAMPO_11, FLEX_CAMPO_12, FLEX_CAMPO_13, FLEX_CAMPO_14,
                FLEX_CAMPO_15, TELEFONE, ID_PESSOA, ID_COTAS_CONCURSOS, FLEX_CAMPO_16,
                FLEX_CAMPO_17, FLEX_CAMPO_18, FLEX_CAMPO_19, FLEX_CAMPO_20, FLEX_CAMPO_21,
                FLEX_CAMPO_22, FLEX_CAMPO_23, FLEX_CAMPO_24, FLEX_CAMPO_25, FLEX_CAMPO_26,
                FLEX_CAMPO_27, FLEX_CAMPO_28, FLEX_CAMPO_29, FLEX_CAMPO_30
            FROM ERGON.INSCRITOS
        """,
    },
    "vagas_concurso": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                CHAVE, CHAVE_CONCURSO, CARGO, ESPECIALIDADE, HLOCAL, QTD_VAGAS,
                QTD_VAGAS_DEF, FLEX_CAMPO_01, FLEX_CAMPO_02, FLEX_CAMPO_03,
                FLEX_CAMPO_04, FLEX_CAMPO_05, EMP_CODIGO, SEXO, PERCENTUAL_VAGAS_DEF,
                DIAS_PRAZO_POSSE, DIAS_PRAZO_PRORROG_POSSE, DIAS_PRAZO_EXERC,
                DIAS_PRAZO_PRORROG_EXERC, GRUPO_VAGAS, FLEX_CAMPO_06, FLEX_CAMPO_07,
                FLEX_CAMPO_08, FLEX_CAMPO_09, FLEX_CAMPO_10
            FROM ERGON.VAGAS_CONCURSO
        """,
    },
    "concursos": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                CHAVE, SIGLA, REGIMEJUR, DTINI, VALIDADE, PUBLIC_EDITAL, RESULTADO,
                OBJETIVO, FLEX_CAMPO_01, FLEX_CAMPO_02, FLEX_CAMPO_03, FLEX_CAMPO_04,
                FLEX_CAMPO_05, EMP_CODIGO, PRORROGACAO, CANCELAMENTO, ABRANGENCIA,
                PONTPUBL, DTINI_INSCRICAO, DTFIM_INSCRICAO, SETOR, TIPO_CONCURSO,
                TIPOVINC, INSTITUICAO, DIAS_PRAZO_POSSE, DIAS_PRAZO_PRORROG_POSSE,
                DIAS_PRAZO_EXERC, DIAS_PRAZO_PRORROG_EXERC, FLEX_CAMPO_06, FLEX_CAMPO_07,
                FLEX_CAMPO_08, FLEX_CAMPO_09, FLEX_CAMPO_10
            FROM ERGON.CONCURSOS
        """,
    },
    "formas_vac": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                SIGLA, NOME, FLEX_CAMPO_01, FLEX_CAMPO_02, FLEX_CAMPO_03,
                FLEX_CAMPO_04, FLEX_CAMPO_05, PONTLEI, FLEX_CAMPO_06, FLEX_CAMPO_07,
                FLEX_CAMPO_08, FLEX_CAMPO_09, FLEX_CAMPO_10, FLEX_CAMPO_11,
                FLEX_CAMPO_12, FLEX_CAMPO_13, FLEX_CAMPO_14, FLEX_CAMPO_15,
                FLEX_CAMPO_16, FLEX_CAMPO_17, FLEX_CAMPO_18, FLEX_CAMPO_19,
                FLEX_CAMPO_20, CODIGO_CAGED
            FROM ERGON.FORMAS_VAC_
        """,
    },
}

ergon_clocks = generate_dump_db_schedules(
    interval=timedelta(days=1),
    start_date=datetime(2022, 11, 9, 22, 30, tzinfo=pytz.timezone("America/Sao_Paulo")),
    labels=[
        constants.RJ_LOCAL_IPLAN_AGENT_LABEL.value,
    ],
    db_database="P01.PCRJ",
    db_host="10.70.6.21",
    db_port="1526",
    db_type="oracle",
    dataset_id="recursos_humanos_ergon",
    infisical_secret_path="/db-ergon-prod",
    table_parameters=ergon_queries,
    agent_label=[constants.RJ_SMFP_AGENT_LABEL.value],
)

ergon_monthly_update_schedule = Schedule(clocks=untuple(ergon_clocks))
