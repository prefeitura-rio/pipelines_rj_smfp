SELECT
    SAFE_CAST(INSCMUNIC AS INT64) AS INSCMUNIC,
    SAFE_CAST(CPF_CNPJ AS STRING) AS CPF_CNPJ,
    SAFE_CAST(NOME AS STRING) AS NOME,
    SAFE_CAST(QUALIFICACAO AS INT64) AS QUALIFICACAO,
    SAFE_CAST(DESC_QUALIFICACAO AS STRING) AS DESC_QUALIFICACAO,
    SAFE_CAST(IDENTIDADE AS STRING) AS IDENTIDADE,
    SAFE_CAST(UF_IDENTIDADE AS STRING) AS UF_IDENTIDADE,
    SAFE_CAST(ORGAO_EMISSOR_IDENTIDADE AS STRING) AS ORGAO_EMISSOR_IDENTIDADE,
    SAFE_CAST(PATICIPACAO AS INT64) AS PATICIPACAO,
    SAFE_CAST(CL AS INT64) AS CL,
    SAFE_CAST(NUM_PORTA AS INT64) AS NUM_PORTA,
    SAFE_CAST(COMPLEMENTO AS STRING) AS COMPLEMENTO,
    SAFE_CAST(LOGRADOURO AS STRING) AS LOGRADOURO,
    SAFE_CAST(BAIRRO AS STRING) AS BAIRRO,
    SAFE_CAST(CEP AS STRING) AS CEP,
    SAFE_CAST(MUNICIPIO AS STRING) AS MUNICIPIO,
    SAFE_CAST(UF AS STRING) AS UF,
    SAFE_CAST(PAIS AS STRING) AS PAIS


FROM `rj-smfp.atividade_economica_sinae_staging.vw_clf_socio`