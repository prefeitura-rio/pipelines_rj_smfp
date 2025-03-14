SELECT
    SAFE_CAST(cd_ramo AS STRING) AS codigo_ramo,
    SAFE_CAST(ds_ramo AS STRING) AS descricao_ramo,
    SAFE_CAST(st_ramo AS STRING) AS situacao_ramo,
FROM `rj-smfp.compras_materiais_servicos_sigma_staging.VW_RAMO_ATIVIDADE` AS t