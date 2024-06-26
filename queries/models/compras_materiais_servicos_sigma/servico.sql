SELECT
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_atividade_economica), r'\.0$', '') AS STRING) AS id_atividade_economica,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_comprasnet), r'\.0$', '') AS STRING) AS id_compras_net,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_atividade_cae), r'\.0$', '') AS STRING) AS id_atividade_cae,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_grupo_cae), r'\.0$', '') AS STRING) AS id_grupo_cae,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_seq), r'\.0$', '') AS STRING) AS id_sequencia,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_servico), r'\.0$', '') AS STRING) AS id_servico,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_serv), r'\.0$', '') AS STRING) AS id_serv,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_subgrupo_cae), r'\.0$', '') AS STRING) AS id_subgrupo_cae,
    SAFE_CAST(TRIM(ds_atividade_economica) AS STRING) AS descricao_atividade_economica,
    SAFE_CAST(TRIM(ds_servico) AS STRING) AS descricao_servico,
    SAFE_CAST(TRIM(ds_subgrupo_cae) AS STRING) AS descricao_subgrupo_cae,
    SAFE_CAST(TRIM(dv) AS STRING) AS digito_verificador,
    SAFE_CAST(TRIM(nm_padronizado) AS STRING) AS nome_padronizado,
    SAFE_CAST(TRIM(st_cadastro_fornecedor) AS STRING) AS situacao_cadastro_fornecedor,
    SAFE_CAST(TRIM(st_responsavel_tecnico) AS STRING) AS responsavel_tecnico,
    SAFE_CAST(TRIM(st_sistema_registro_preco) AS STRING) AS registro_preco,
    SAFE_CAST(TRIM(st_status) AS STRING) AS status_servico,
    SAFE_CAST(TRIM(st_tabelado) AS STRING) AS situacao_tabelado,
    SAFE_CAST(TRIM(unidade_servico) AS STRING) AS unidade_servico,
FROM `rj-smfp.compras_materiais_servicos_sigma_staging.servico` AS t