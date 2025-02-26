SELECT
    SAFE_CAST(cd_grupo AS STRING) AS id_grupo,
    SAFE_CAST(ds_grupo AS STRING) AS descricao_grupo,
    SAFE_CAST(st_status AS STRING) AS id_status
FROM `rj-smfp.compras_materiais_servicos_sigma_staging.VW_GRUPO` AS t