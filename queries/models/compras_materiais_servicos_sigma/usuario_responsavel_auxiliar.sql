SELECT
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_orgao), r'\.0$', '') AS STRING) AS id_orgao,
    SAFE_CAST(TRIM(ds_orgao) AS STRING) AS descricao_orgao,
    SAFE_CAST(DATE(dt_excepcionalidade) AS DATE) AS data_excepecionalidade,
    SAFE_CAST(DATE(dt_inicio) AS DATE) AS data_inicio,
    SAFE_CAST(DATE(dt_publicacao_designacao) AS DATE) AS data_publicacao_designação,
    SAFE_CAST(DATE(dt_termino) AS DATE) AS data_termino,
    SAFE_CAST(DATE(dt_termo_responsabilidade) AS DATE) AS data_termo_responsabilidade,
    SAFE_CAST(TRIM(escolaridade) AS STRING) AS escolaridade,
    SAFE_CAST(TRIM(matricula) AS STRING) AS matricula_funcionario,
    SAFE_CAST(TRIM(nm_funcionario) AS STRING) AS nome_funcionario,
    SAFE_CAST(TRIM(st_curso_gestao_material) AS STRING) AS curso_gestao_material,
    SAFE_CAST(TRIM(tp_funcionario) AS STRING) AS tipo_responsabilidade,
FROM `rj-smfp.compras_materiais_servicos_sigma_staging.usuario_responsavel_auxiliar` AS t