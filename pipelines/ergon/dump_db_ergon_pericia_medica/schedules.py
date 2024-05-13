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
    "cid": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                TIPO, CODIGO, DESCRICAO, COD_PAI, FLEX_CAMPO_01,
                FLEX_CAMPO_02, FLEX_CAMPO_03, FLEX_CAMPO_04, FLEX_CAMPO_05,
                FLEX_CAMPO_06, FLEX_CAMPO_07, FLEX_CAMPO_08, FLEX_CAMPO_09,
                FLEX_CAMPO_10, FLEX_CAMPO_11, FLEX_CAMPO_12, FLEX_CAMPO_13,
                FLEX_CAMPO_14, FLEX_CAMPO_15, CAPITULO, GUID_GRUPO,
                DESCRICAO_ABREV, CLASSIF, REFER, RESTR_SEXO, CAUSA_OBITO,
                EXCLUIDOS, NIVEL
            FROM ERGON.CID
        """,
    },
    "designacoes_ev": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                NUMFUNC, NUMVINC, DTINI, DTFIM, FUNCAO, SETOR, OBS,
                NUMFUNCSUBS1, NUMVINCSUBS1, NUMFUNCSUBS2, NUMVINCSUBS2,
                PONTPUBL, NUMERO_VAGA, PONTLEI, FLEX_CAMPO_01, FLEX_CAMPO_02,
                FLEX_CAMPO_03, FLEX_CAMPO_04, FLEX_CAMPO_05, EMP_CODIGO, ID_REG
            FROM ERGON.DESIGNACOES_EV
        """,
    },
    "erg_pm_cid10_capitulo": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                CAPITULO, DESCRICAO, FLEX_CAMPO_01,
                FLEX_CAMPO_02, FLEX_CAMPO_03, FLEX_CAMPO_04, FLEX_CAMPO_05
            FROM ERGON.ERG_PM_CID10_CAPITULO
        """,
    },
    "erg_pm_decisao": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                DECISAO, SIGLAEXAME, SIGLA, DESCRICAO, GERA_LICAFAST,
                GERA_READAPTACAO, ALTA_AT, NEGADO, QUANT_PERITOS, TEXTO_LAUDO,
                NUM_MESES, RETIFICA, INTERVALO_DIAS, FLEX_CAMPO_01,
                FLEX_CAMPO_02, FLEX_CAMPO_03, FLEX_CAMPO_04, FLEX_CAMPO_05,
                FLEX_CAMPO_06, FLEX_CAMPO_07, FLEX_CAMPO_08, FLEX_CAMPO_09,
                FLEX_CAMPO_10, CONCLUI_INGRESSO, FLEX_CAMPO_11, FLEX_CAMPO_12,
                FLEX_CAMPO_13, FLEX_CAMPO_14, FLEX_CAMPO_15, FLEX_CAMPO_16, FLEX_CAMPO_17,
                FLEX_CAMPO_18, FLEX_CAMPO_19, FLEX_CAMPO_20, EXAME_ENCAM, RETIF_POR_EXCLUSAO,
                TITULO_LAUDO, TITULO_01, TITULO_02, TITULO_03
            FROM ERGON.ERG_PM_DECISAO
        """,
    },
    "erg_pm_grupoexame": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                GRUPOEXAME, NOME, FLEX_CAMPO_01, FLEX_CAMPO_02,
                FLEX_CAMPO_03, FLEX_CAMPO_04, FLEX_CAMPO_05
            FROM ERGON.ERG_PM_GRUPOEXAME
        """,
    },
    "erg_pm_pront_med": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                PROFISPRONT, CHAVEPRONT, CRM, PROFISSIONAL, SENHA,
                OK, NOK, JUSTIFICATIVA, "DATA", ORDEM_HOMOL, FLEX_CAMPO_01,
                FLEX_CAMPO_02, FLEX_CAMPO_03, FLEX_CAMPO_04, FLEX_CAMPO_05,
                FLEX_CAMPO_06, FLEX_CAMPO_07, FLEX_CAMPO_08, FLEX_CAMPO_09, FLEX_CAMPO_10
            FROM ERGON.ERG_PM_PRONT_MED
        """,
    },
    "erg_pm_resultpront": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                RESULTPRONT, CHAVEPRONT, DECISAO, NUMVINC, DTINI,
                DTFIM, NUMDIAS, TIPOFREQ, CODFREQ, PONTPUBL, DTCONCL,
                ERROCONCL, RESULTRETIF, FLEX_CAMPO_01, FLEX_CAMPO_02,
                FLEX_CAMPO_03, FLEX_CAMPO_04, FLEX_CAMPO_05, FLEX_CAMPO_06,
                FLEX_CAMPO_07, FLEX_CAMPO_08, FLEX_CAMPO_09, FLEX_CAMPO_10,
                JUSTIFICATIVA, PRAZO, NEXO, JURIDICO, MOTIVOPUBL, VERSAOPUBL,
                FLEX_CAMPO_11
            FROM ERGON.ERG_PM_RESULTPRONT
        """,
    },
    "exames": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                SIGLA, NOME, FLEX_CAMPO_01, FLEX_CAMPO_02, FLEX_CAMPO_03,
                FLEX_CAMPO_04, FLEX_CAMPO_05, CONSULTAS_AFAST, PRORROG_LIC,
                OBRIG_ESPEC, OBRIG_ULTATEND, PRAZO_RECONSIDERACAO, QUANTMED,
                GRUPOEXAME, OBRIG_DEPEN, OBRIG_CAT, OBRIG_PROCESSO, OBRIG_PENS,
                DISPONIVEL_UNID, TIPOEQUIPE, EXAMERECURSO, MAX_DIAS_RETROAC,
                VAGASAGENDA, IMPRIME_CONVOCACAO, SETOR_CONVOCACAO, INSTRUCOES,
                FLEX_CAMPO_06, FLEX_CAMPO_07, FLEX_CAMPO_08, FLEX_CAMPO_09,
                FLEX_CAMPO_10, FICHA_VACINA, EXAME_LABORATORIO, EXAME_COMPLEMENTAR,
                TIPO_PERICIA, INGRESSO, PUBLICA_AGENDAMENTO, DATA_AGENDAMENTO,
                FLEX_CAMPO_11, FLEX_CAMPO_12, FLEX_CAMPO_13, FLEX_CAMPO_14, FLEX_CAMPO_15,
                FLEX_CAMPO_16, FLEX_CAMPO_17, FLEX_CAMPO_18, FLEX_CAMPO_19, FLEX_CAMPO_20,
                PERICIA_EXTERNA, GRUPO2EXAME, TITULO_01, TITULO_02, TITULO_03, LEMBRETE
            FROM ERGON.EXAMES
        """,
    },
    "funcoes_ev": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                FUNCAO, NOME, CONTROLE_VAGA, FLEX_CAMPO_01, FLEX_CAMPO_02,
                FLEX_CAMPO_03, FLEX_CAMPO_04, FLEX_CAMPO_05, PONTPUBL,
                FLEX_CAMPO_06, FLEX_CAMPO_07, FLEX_CAMPO_08, FLEX_CAMPO_09,
                FLEX_CAMPO_10, FLEX_CAMPO_11, FLEX_CAMPO_12, FLEX_CAMPO_13, FLEX_CAMPO_14,
                FLEX_CAMPO_15, FLEX_CAMPO_16, FLEX_CAMPO_17, FLEX_CAMPO_18, FLEX_CAMPO_19,
                FLEX_CAMPO_20, FLEX_CAMPO_21, FLEX_CAMPO_22, FLEX_CAMPO_23, FLEX_CAMPO_24,
                FLEX_CAMPO_25, FLEX_CAMPO_26, FLEX_CAMPO_27, FLEX_CAMPO_28, FLEX_CAMPO_29,
                FLEX_CAMPO_30, DT_INICIO_CONTR_VAGA, ID_REG
            FROM ERGON.FUNCOES_EV_
        """,
    },
    "medicos": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                CRM, NOME, NUMFUNC, FLEX_CAMPO_01, FLEX_CAMPO_02, FLEX_CAMPO_03,
                FLEX_CAMPO_04, FLEX_CAMPO_05, DATAINATIV, ID_PESSOA, FLEX_CAMPO_06,
                FLEX_CAMPO_07, FLEX_CAMPO_08, FLEX_CAMPO_09, FLEX_CAMPO_10, FLEX_CAMPO_11,
                FLEX_CAMPO_12, FLEX_CAMPO_13, FLEX_CAMPO_14, FLEX_CAMPO_15
            FROM ERGON.MEDICOS
        """,
    },
    "prontuario": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                NUMFUNC, SIGLA, DT_HOMOL, CRM_HOMOL, CRM_ATEST,
                COD_CID1, TP_CID1, COD_CID2, TP_CID2, COD_CID3,
                TP_CID3, ATEST_PUBL, DTINI, DTFIM, APTO, TEXTO_AUT,
                TEXTO_MEDICO, TIPO_LIC, EXAM_TEXT, COD_ACIDENTE,
                FLEX_CAMPO_01, FLEX_CAMPO_02, FLEX_CAMPO_03, FLEX_CAMPO_04,
                FLEX_CAMPO_05, FLEX_CAMPO_06, FLEX_CAMPO_07, FLEX_CAMPO_08,
                FLEX_CAMPO_09, FLEX_CAMPO_10, CHAVE, PONTPUBL, CHAVEATEND,
                DTATEND, HORAATEND, FLEX_CAMPO_11, FLEX_CAMPO_12, FLEX_CAMPO_13,
                FLEX_CAMPO_14, FLEX_CAMPO_15, FLEX_CAMPO_16, FLEX_CAMPO_17,
                FLEX_CAMPO_18, FLEX_CAMPO_19, FLEX_CAMPO_20, FLEX_CAMPO_21,
                FLEX_CAMPO_22, FLEX_CAMPO_23, FLEX_CAMPO_24, FLEX_CAMPO_25,
                FLEX_CAMPO_26, FLEX_CAMPO_27, FLEX_CAMPO_28, FLEX_CAMPO_29,
                FLEX_CAMPO_30, ANAMNESE, EXAMEADIC, DTCONCLUSAO, REQPERICIA,
                CHAVEANT, CAT, NOMEPARENTE, GRAU_PARENTESCO, NUMPENS, NUMVINC_PENS,
                NUMPROC, US, ID_REG, INSCRITO, JUSTIFICATIVA, NUMDEP, FLEX_CAMPO_31,
                FLEX_CAMPO_32, FLEX_CAMPO_33, FLEX_CAMPO_34, FLEX_CAMPO_35
            FROM ERGON.PRONTUARIO
        """,
    },
    "tpmrj_pm_juntas": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                ID_JUNTA, NUMFUNC, SIGLA, DTINI,
                JUSTIFICATIVA, DTCONCLUSAO, NUMPROC
            FROM C_ERGON.TPMRJ_PM_JUNTAS
        """,
    },
    "tpmrj_pm_periciasjunta": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                ID_PERICIA_JUNTA, ID_JUNTA, CHAVEPRONT
            FROM C_ERGON.TPMRJ_PM_PERICIASJUNTA
        """,
    },
    "tpmrj_pm_resultjunta": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                ID_RESULTJUNTA, ID_JUNTA, DECISAO, NUMVINC,
                DTINI, DTFIM, NUMDIAS, ID_RESULTJUNTARETIF,
                PONTPUBL, JUSTIF_RETIF, RETIFICADO, TIPOFREQ,
                CODFREQ, CRM, PROFISSIONAL, COMPL_DECISAO_PUBL,
                ERROCONCL, LOTE_PUBL
            FROM C_ERGON.TPMRJ_PM_RESULTJUNTA
        """,
    },
    "tpmrj_pm_vwbim ": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                ROWID_REG, ID_BIM, ID_SOLIC_BIM, NUMFUNC,
                NUMVINC, MATRIC, NOME, TIPOVINC, CARGO,
                DESC_CARGO, SETOR, NOMESETOR, READAPTADO,
                TIPO_PESSOA, NUMDEP, DT_SOLICITACAO, REQUERIMENTO,
                EH_REASSUNCAO, EMAIL, TELEFONE, NOME_DEPENDENTE,
                MOTIVO_INSPECAO, SITUACAO, SITUACAO_DESC, FALTANDO_SERVICO,
                FALTANDO_SERVICO_DESDE, SITUACAO_FUNCIONAL_REGULAR,
                HORARIO_TRABALHO_INI, HORARIO_TRABALHO_FIM, OBSERVACAO_RH,
                MOTIVO_REJEICAO, ARTIGO, DIAS_DIF_AGENDAMENTO
            FROM C_ERGON.TPMRJ_PM_VWBIM
        """,
    },
    "tpmrj_pm_vwtpconclper ": {
        "materialize_after_dump": True,
        "biglake_table": True,
        "materialization_mode": "prod",
        "dump_mode": "overwrite",
        "execute_query": """
            SELECT
                ROWID_REG, ID_SOLIC_BIM, NUMFUNC,
                NUMVINC, MATRICULA, NOME, DT_SOLICITACAO,
                REQUERIMENTO, REQUERIMENTO_DESC, EH_REASSUNCAO,
                EMAIL, EMAIL_FUNCIONARIO, TELEFONE,
                TELEFONE_FUNCIONARIO, EMAIL_CHEFE, TELEFONE_CHEFE,
                TIPO_PESSOA, MOTIVO_INSPECAO, EXAME_PESSOA_DE, NUMDEP,
                NOME_DEPENDENTE, GRAU_PARENTESCO, COD_SETOR, SETOR,
                SITUACAO, DESC_SITUACAO, ORIGEM_SOLIC, E_MAIL_ALTERNATIVO,
                EH_EMAIL_INSTITUCIONAL, EH_EMAIL_INSTITUCIONAL_BIM
            FROM C_ERGON.TPMRJ_PM_VWSOLICBIM
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


# for table_id in ergon_queries:
#     query = f"""SELECT
#                     *
#                 FROM `rj-smfp.recursos_humanos_ergon_pericia_medica_staging.{table_id}`
#     """
#     # save the query in a table_id.sql
#     with open(f"queries/models/recursos_humanos_ergon_pericia_medica/{table_id}.sql", "w") as f:
#         f.write(query.replace("                ", ""))
