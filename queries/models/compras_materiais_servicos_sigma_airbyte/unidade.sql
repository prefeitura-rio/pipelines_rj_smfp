SELECT
    SAFE_CAST(ds_unidade AS STRING) AS descricao_unidade,
    SAFE_CAST(unidade AS STRING) AS id_unidade
FROM `rj-smfp.compras_materiais_servicos_sigma_staging.VW_UNIDADE` AS t