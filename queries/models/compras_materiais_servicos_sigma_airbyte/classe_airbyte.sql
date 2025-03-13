SELECT
    SAFE_CAST(cd_classe AS STRING) AS id_classe,
    SAFE_CAST(cd_grupo AS STRING) AS id_grupo,
    SAFE_CAST(ds_classe AS STRING) AS descricao_classe,
    SAFE_CAST(st_status AS STRING) AS id_status,

FROM `rj-smfp.compras_materiais_servicos_sigma_staging.VW_CLASSE` AS t