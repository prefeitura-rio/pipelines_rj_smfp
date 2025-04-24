SELECT
    SAFE_CAST(INSCMUNIC AS INT64) AS INSCMUNIC,
    SAFE_CAST(CODIGO AS STRING) AS CODIGO,
    SAFE_CAST(DESCRICAO AS STRING) AS DESCRICAO

FROM `rj-smfp.atividade_economica_sinae_staging.vw_clf_restricao_ativ_econ`