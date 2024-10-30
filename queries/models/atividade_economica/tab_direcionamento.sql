SELECT
    SAFE_CAST(ID_Direcionamento AS STRING) AS ID_Direcionamento,
    SAFE_CAST(DSC_Direcionamento AS STRING) AS DSC_Direcionamento

FROM `rj-smfp.atividade_economica_staging.tab_direcionamento`