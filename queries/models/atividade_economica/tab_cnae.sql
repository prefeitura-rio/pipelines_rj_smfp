SELECT
    SAFE_CAST(ID_CNAE AS STRING) AS ID_CNAE,
    SAFE_CAST(DSC_CNAE AS STRING) AS DSC_CNAE

FROM `rj-smfp.atividade_economica_staging.tab_cnae`