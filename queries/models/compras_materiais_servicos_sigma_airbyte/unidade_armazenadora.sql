SELECT
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_programa_trabalho), r'\.0$', '') AS STRING) AS id_programa_trabalho,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_unidade_administrativa), r'\.0$', '') AS STRING) AS id_unidade_administrativa,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_unidade_armazenadora), r'\.0$', '') AS STRING) AS id_unidade_armazenadora,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cnes), r'\.0$', '') AS STRING) AS id_cnes,
    SAFE_CAST(TRIM(ds_unidade_administrativa) AS STRING) AS descricao_unidade_administrativa,
    SAFE_CAST(TRIM(ds_unidade_armazenadora) AS STRING) AS descricao_unidade_armazenadora,
    SAFE_CAST(TRIM(st_expr_monetaria_oito_casas) AS STRING) AS expressao_monetaria,
    SAFE_CAST(TRIM(st_status) AS STRING) AS status_unidade_administrativa,
    SAFE_CAST(TRIM(tp_almoxarifado) AS STRING) AS tipo_almoxarifado,
    SAFE_CAST(TRIM(tp_unidade_armazenadora) AS STRING) AS tipo_unidade_armazenadora,
FROM `rj-smfp.compras_materiais_servicos_sigma_staging.VW_UNIDADE_ARMAZENADORA` AS t