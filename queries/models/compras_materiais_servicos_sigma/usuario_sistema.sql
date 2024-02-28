SELECT
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_orgao_designacao), r'\.0$', '') AS STRING) AS id_orgao_designacao,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_perfil), r'\.0$', '') AS STRING) AS id_perfil,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_terminal), r'\.0$', '') AS STRING) AS id_terminal,
    SAFE_CAST(TRIM(cpf) AS STRING) AS cpf_colaborador,
    SAFE_CAST(TRIM(ds_orgao_designacao) AS STRING) AS descricao_orgao_designacao,
    SAFE_CAST(TRIM(ds_perfil) AS STRING) AS descricao_perfil,
    SAFE_CAST(DATE(dt_inclusao) AS DATE) AS data_inclusao,
    SAFE_CAST(DATE(dt_ultima_sessao) AS DATE) AS data_ultima_sessao,
    SAFE_CAST(TRIM(email_alternativo) AS STRING) AS email_alternativo,
    SAFE_CAST(TRIM(email_institucional) AS STRING) AS email_institucional,
    SAFE_CAST(TRIM(hora_acesso_fim) AS STRING) AS hora_acesso_fim,
    SAFE_CAST(TRIM(hora_acesso_ini) AS STRING) AS hora_acesso_inicio,
    SAFE_CAST(TRIM(hora_ultima_sessao) AS STRING) AS hora_ultima_sessao,
    SAFE_CAST(TRIM(matricula) AS STRING) AS matricula,
    SAFE_CAST(TRIM(minuto_acesso_fim) AS STRING) AS minuto_acesso_fim,
    SAFE_CAST(TRIM(minuto_acesso_ini) AS STRING) AS minuto_acesso_inicio,
    SAFE_CAST(TRIM(nm_funcionario) AS STRING) AS nome_servidor,
    SAFE_CAST(TRIM(nm_prestador_servico) AS STRING) AS empresa_contratante,
    SAFE_CAST(TRIM(privilegio_almoxarifado) AS STRING) AS privilegio_almoxarifado,
    SAFE_CAST(TRIM(st_situacao) AS STRING) AS status_situacao,
    SAFE_CAST(TRIM(st_status) AS STRING) AS status,
    SAFE_CAST(TRIM(tel_alternativo1) AS STRING) AS telefone_alternativo_1,
    SAFE_CAST(TRIM(tel_alternativo2) AS STRING) AS telefone_alternativo_2,
    SAFE_CAST(TRIM(tel_corporativo1) AS STRING) AS telefone_corporativo_1,
    SAFE_CAST(TRIM(tel_corporativo2) AS STRING) AS telefone_corporativo_2,
FROM `rj-smfp.compras_materiais_servicos_sigma_staging.usuario_sistema` AS t