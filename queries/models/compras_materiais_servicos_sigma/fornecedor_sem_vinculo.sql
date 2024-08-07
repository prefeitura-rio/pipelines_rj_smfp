SELECT
    SAFE_CAST(TRIM(cpf_cnpj) AS STRING) AS cpf_cnpj,
    SAFE_CAST(TRIM(nome) AS STRING) AS nome_razao_social,
    SAFE_CAST(TRIM(tipo_cpf_cnpj) AS STRING) AS tipo_cpf_cnpj,
    SAFE_CAST(REGEXP_REPLACE(TRIM(numero_porta), r'\.0$', '') AS INT64) AS numero_porta,
    SAFE_CAST(TRIM(email) AS STRING) AS email,
    SAFE_CAST(TRIM(fax) AS STRING) AS fax,
    SAFE_CAST(TRIM(ddd) AS STRING) AS ddd,
    SAFE_CAST(TRIM(ddi) AS STRING) AS ddi,
    SAFE_CAST(TRIM(ramal) AS STRING) AS ramal,
    SAFE_CAST(TRIM(telefone) AS STRING) AS telefone,
    SAFE_CAST(TRIM(logradouro) AS STRING) AS logradouro,
    SAFE_CAST(TRIM(complemento) AS STRING) AS complemento_logradouro,
    SAFE_CAST(TRIM(bairro) AS STRING) AS bairro,
    SAFE_CAST(TRIM(municipio) AS STRING) AS municipio,
    SAFE_CAST(TRIM(uf) AS STRING) AS uf,
    SAFE_CAST(TRIM(cep) AS STRING) AS cep,
    SAFE_CAST(TRIM(ativo_inativo_bloqueado) AS STRING) AS ativo_inativo_bloqueado,
    SAFE_CAST(TRIM(cd_natureza_juridica) AS STRING) AS id_natureza_juridica,
    SAFE_CAST(TRIM(ds_natureza_juridica) AS STRING) AS descricao_natureza_juridica,
    SAFE_CAST(TRIM(ramo_atividade) AS STRING) AS ramo_atividade,
    SAFE_CAST(TRIM(cd_porte_empresa) AS STRING) AS id_porte_empresa,
    SAFE_CAST(PARSE_DATE('%Y%m%d', TRIM(data_ultima_atualizacao)) AS DATE) AS data_ultima_atualizacao
FROM `rj-smfp.compras_materiais_servicos_sigma_staging.fornecedor_sem_vinculo` AS t
