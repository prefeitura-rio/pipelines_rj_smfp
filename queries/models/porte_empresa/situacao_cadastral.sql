{{
    config(
        materialized='table',
        partition_by={
            "field": "data_particao",
            "data_type": "date",
            "granularity": "month",
        }
    )
}}
SELECT
    SAFE_CAST(cnpj_basico AS STRING) AS cnpj_basico,
    SAFE_CAST(cnpj_ordem AS STRING) AS cnpj_ordem,
    SAFE_CAST(cnpj_dv AS STRING) AS cnpj_dv,
    SAFE_CAST(razaosocial AS STRING) AS razao_social,
    SAFE_CAST(REGEXP_REPLACE(cd_porteempresa, r'\.0$', '') AS STRING) AS id_porte_empresa,
    SAFE_CAST(REGEXP_REPLACE(cd_situacaocadastral, r'\.0$', '') AS STRING) AS id_situacao_cadastral,
    SAFE_CAST(dt_situacaocadastral AS DATE) AS data_situacao_cadastral
    SAFE_CAST(data_particao AS DATE) data_particao
FROM `rj-smfp.porte_empresa_staging.situacao_cadastral`