SELECT
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_programa_trabalho), r'\.0$', '') AS STRING) AS id_programa_trabalho,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_unidade_administrativa), r'\.0$', '') AS STRING) AS id_unidade_administrativa,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_unidade_armazenadora), r'\.0$', '') AS STRING) AS id_unidade_armazenadora,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cnes), r'\.0$', '') AS STRING) AS id_cnes,
    SAFE_CAST(TRIM(ds_unidade_administrativa) AS STRING) AS descricao_unidade_administrativa,
    SAFE_CAST(TRIM(ds_unidade_armazenadora) AS STRING) AS descricao_unidade_armazenadora,
    PARSE_DATE("%Y%m%d",REGEXP_REPLACE(TRIM(dt_responsavel), r'\.0$', '')) as data_inicio_responsavel,
    PARSE_DATE("%Y%m%d",REGEXP_REPLACE(TRIM(dt_substituto1), r'\.0$', '')) as data_inicio_substituto_1,
    PARSE_DATE("%Y%m%d",REGEXP_REPLACE(TRIM(dt_substituto2), r'\.0$', '')) as data_inicio_substituto_2,
    SAFE_CAST(TRIM(matricula_responsavel) AS STRING) AS matricula_responsavel,
    SAFE_CAST(TRIM(matricula_substituto1) AS STRING) AS matricula_substituto_1,
    SAFE_CAST(TRIM(matricula_substituto2) AS STRING) AS matricula_substituto_2,
    SAFE_CAST(TRIM(nm_responsavel) AS STRING) AS nome_responsavel,
    SAFE_CAST(TRIM(nm_substituto1) AS STRING) AS nome_substituto_1,
    SAFE_CAST(TRIM(nm_substituto2) AS STRING) AS nome_substituto_2,
    SAFE_CAST(TRIM(st_expr_monetaria_oito_casas) AS STRING) AS expressao_monetaria,
    SAFE_CAST(TRIM(st_status) AS STRING) AS status_unidade_administrativa,
    SAFE_CAST(TRIM(tp_almoxarifado) AS STRING) AS tipo_almoxarifado,
    SAFE_CAST(TRIM(tp_unidade_armazenadora) AS STRING) AS tipo_unidade_armazenadora,
FROM `rj-smfp.compras_materiais_servicos_sigma_staging.unidade_armazenadora` AS t