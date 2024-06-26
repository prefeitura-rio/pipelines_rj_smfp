SELECT
    SAFE_CAST(TRIM(ativo_inativo_bloqueado) AS STRING) AS status_fornecedor,
    SAFE_CAST(TRIM(bairro) AS STRING) AS bairro,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_natureza_juridica), r'\.0$', '') AS STRING) AS id_natureza_juridica,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_porte_empresa), r'\.0$', '') AS STRING) AS id_porte_fornecedor,
    SAFE_CAST(TRIM(cep) AS STRING) AS cep,
    SAFE_CAST(TRIM(complemento) AS STRING) AS complemento_endereco,
    SAFE_CAST(TRIM(cpf_cnpj) AS STRING) AS cpf_cnpj,
    SAFE.PARSE_DATE("%Y%m%d",REGEXP_REPLACE(TRIM(data_ultima_atualizacao), r'\.0$', '')) as data_ultima_atualizacao,
    SAFE_CAST(TRIM(ddd) AS STRING) AS ddd,
    SAFE_CAST(TRIM(ddi) AS STRING) AS ddi,
    SAFE_CAST(TRIM(ds_natureza_juridica) AS STRING) AS descricao_natureza_juridica,
    SAFE_CAST(TRIM(email) AS STRING) AS email,
    SAFE_CAST(TRIM(email_contato) AS STRING) AS email_contato,
    SAFE_CAST(TRIM(fax) AS STRING) AS fax_fornecedor,
    SAFE_CAST(TRIM(fornecedor_eventual) AS BOOL) AS fornecedor_eventual,
    SAFE_CAST(REGEXP_REPLACE(TRIM(inscricao_estadual), r'\.0$', '') AS STRING) AS id_inscricao_estadual,
    SAFE_CAST(TRIM(inscricao_municipal) AS STRING) AS inscricao_municipal,
    SAFE_CAST(TRIM(logradouro) AS STRING) AS logradouro,
    SAFE_CAST(TRIM(municipio) AS STRING) AS municipio,
    SAFE_CAST(TRIM(nome_contato) AS STRING) AS nome_contato,
    SAFE_CAST(TRIM(nome_fantasia) AS STRING) AS nome_fantasia,
    SAFE_CAST(REGEXP_REPLACE(TRIM(numero_porta), r'\.0$', '') AS INT64) AS numero_porta,
    SAFE_CAST(TRIM(ramal) AS STRING) AS ramal,
    SAFE_CAST(TRIM(ramo_atividade) AS STRING) AS ramo_atividade,
    SAFE_CAST(TRIM(razao_social) AS STRING) AS razao_social,
    SAFE_CAST(TRIM(telefone) AS STRING) AS telefone,
    SAFE_CAST(TRIM(tipo_cpf_cnpj) AS STRING) AS tipo_fornecedor,
    SAFE_CAST(TRIM(uf) AS STRING) AS uf,
FROM `rj-smfp.compras_materiais_servicos_sigma_staging.fornecedor` AS t