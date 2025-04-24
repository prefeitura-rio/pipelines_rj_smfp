SELECT
    SAFE_CAST(CODIGO AS STRING) AS CODIGO,
    SAFE_CAST(DESCRICAO AS STRING) AS DESCRICAO,
    SAFE_CAST(STATUS AS STRING) AS STATUS



FROM `rj-smfp.atividade_economica_sinae_staging.vw_clf_status_contribuinte_iss`