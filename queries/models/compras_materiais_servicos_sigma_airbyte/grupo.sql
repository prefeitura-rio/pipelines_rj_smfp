SELECT
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_grupo), r'\.0$', '') AS STRING) AS id_grupo,
    SAFE_CAST(TRIM(ds_grupo) AS STRING) AS descricao_grupo,
    SAFE_CAST(REGEXP_REPLACE(TRIM(st_status), r'\.0$', '') AS STRING) AS id_status,
FROM `rj-smfp.compras_materiais_servicos_sigma_staging.VW_GRUPO` AS t