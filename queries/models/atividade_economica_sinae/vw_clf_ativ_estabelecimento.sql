SELECT
    SAFE_CAST(INSCMUNIC AS INT64) AS INSCMUNIC,
    SAFE_CAST(CODATIVIDADE AS INT64) AS CODATIVIDADE,
    SAFE_CAST(SEQ AS INT64) AS SEQ

FROM `rj-smfp.atividade_economica_sinae_staging.vw_clf_ativ_estabelecimento`