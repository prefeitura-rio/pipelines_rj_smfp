SELECT
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_ramo), r'\.0$', '') AS STRING) AS id_ramo,
    SAFE_CAST(TRIM(ds_ramo) AS STRING) AS descricao_ramo,
    SAFE_CAST(TRIM(st_ramo) AS STRING) AS situacao_ramo,
FROM `rj-smfp.compras_materiais_servicos_sigma_staging.ramo_atividade` AS t