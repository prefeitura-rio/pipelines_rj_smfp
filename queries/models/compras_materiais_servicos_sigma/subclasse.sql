SELECT
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_classe), r'\.0$', '') AS STRING) AS id_classe,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_grupo), r'\.0$', '') AS STRING) AS id_grupo,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_subclasse), r'\.0$', '') AS STRING) AS id_subclasse,
    SAFE_CAST(TRIM(ds_subclasse) AS STRING) AS descricao_subclasse,
    SAFE_CAST(REGEXP_REPLACE(TRIM(st_status), r'\.0$', '') AS STRING) AS id_status,
FROM `rj-smfp.compras_materiais_servicos_sigma_staging.subclasse` AS t