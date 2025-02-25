SELECT
    SAFE_CAST(cd_orgao AS STRING) AS id_orgao,
    SAFE_CAST(ds_orgao AS STRING) AS descricao_orgao,
    SAFE_CAST(dt_excepcionalidade AS STRING) AS data_excepecionalidade,
    SAFE_CAST(dt_inicio AS STRING) AS data_inicio,
    SAFE_CAST(dt_publicacao_designacao AS STRING) AS data_publicacao_designacao,
    SAFE_CAST(dt_termino AS STRING) AS data_termino,
    SAFE_CAST(dt_termo_responsabilidade AS STRING) AS data_termo_responsabilidade,
    SAFE_CAST(escolaridade AS STRING) AS escolaridade,
    SAFE_CAST(matricula AS STRING) AS matricula_funcionario,
    SAFE_CAST(nm_funcionario AS STRING) AS nome_funcionario,
    SAFE_CAST(st_curso_gestao_material AS STRING) AS curso_gestao_material,
    SAFE_CAST(tp_funcionario AS STRING) AS tipo_responsabilidade,
FROM `rj-smfp.compras_materiais_servicos_sigma_staging.VW_USUARIO_RESPONSAVEL_AUXILIAR` AS t