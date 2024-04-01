-- TODO: did not materialize
SELECT
    SAFE_CAST(TRIM(complemento) AS STRING) AS complemento_endereco,
    SAFE_CAST(TRIM(cpf_cnpj) AS STRING) AS cpf_cnpj,
    SAFE_CAST(TRIM(nome) AS STRING) AS nome_razao_social,
    SAFE_CAST(REGEXP_REPLACE(TRIM(numero_porta), r'\.0$', '') AS INT64) AS numero_porta,
    SAFE_CAST(TRIM(tipo_cpf_cnpj) AS STRING) AS tipo_cpf_cnpj,
FROM `rj-smfp.compras_materiais_servicos_sigma_staging.fornecedor_sem_vinculo` AS t