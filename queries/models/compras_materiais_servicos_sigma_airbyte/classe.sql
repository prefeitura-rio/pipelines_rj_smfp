SELECT
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_classe), r'\.0$', '') AS STRING) AS id_classe,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_grupo), r'\.0$', '') AS STRING) AS id_grupo,
    SAFE_CAST(TRIM(ds_classe) AS STRING) AS descricao_classe,
    SAFE_CAST(REGEXP_REPLACE(TRIM(st_status), r'\.0$', '') AS STRING) AS id_status,
FROM `rj-smfp.compras_materiais_servicos_sigma_staging.VW_CLASSE` AS t