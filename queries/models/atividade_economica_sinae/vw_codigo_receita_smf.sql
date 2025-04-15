SELECT
    SAFE_CAST(CODIGO AS STRING) AS CODIGO,
    SAFE_CAST(DESCRICAO AS STRING) AS DESCRICAO


FROM `rj-smfp.atividade_economica_sinae_staging.vw_codigo_receita_smf`