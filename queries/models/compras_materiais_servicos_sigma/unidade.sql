SELECT
    SAFE_CAST(TRIM(ds_unidade) AS STRING) AS descricao_unidade,
    SAFE_CAST(REGEXP_REPLACE(TRIM(unidade), r'\.0$', '') AS STRING) AS id_unidade,
FROM `rj-smfp.compras_materiais_servicos_sigma_staging.unidade` AS t