SELECT
    SAFE_CAST(ID_TipoSolicitacao AS STRING) AS ID_TipoSolicitacao,
    SAFE_CAST(DSC_TipoSolicitacao AS STRING) AS DSC_TipoSolicitacao

FROM `rj-smfp.atividade_economica_staging.tab_tiposolicitacao`