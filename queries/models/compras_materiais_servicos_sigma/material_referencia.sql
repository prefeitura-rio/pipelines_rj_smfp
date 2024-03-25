SELECT
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_classe), r'\.0$', '') AS STRING) AS id_classe,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_grupo), r'\.0$', '') AS STRING) AS id_grupo,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_material), r'\.0$', '') AS STRING) AS id_material,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_referencia), r'\.0$', '') AS STRING) AS id_referencia,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_subclasse), r'\.0$', '') AS STRING) AS id_subclasse,
    SAFE_CAST(TRIM(ds_referencia) AS STRING) AS descricao_referencia,
    SAFE_CAST(TRIM(dv1) AS STRING) AS digito_verificador_1,
    SAFE_CAST(TRIM(dv2) AS STRING) AS digito_verificador_2,
    SAFE_CAST(TRIM(sequencial) AS STRING) AS sequencial_material,
    SAFE_CAST(TRIM(st_status) AS STRING) AS status,
FROM `rj-smfp.compras_materiais_servicos_sigma_staging.material_referencia` AS t