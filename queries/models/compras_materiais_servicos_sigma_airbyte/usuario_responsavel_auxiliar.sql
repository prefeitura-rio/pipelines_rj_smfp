SELECT
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_orgao), r'\.0$', '') AS STRING) AS id_orgao,
    SAFE_CAST(TRIM(ds_orgao) AS STRING) AS descricao_orgao,
    SAFE.PARSE_DATE("%Y%m%d",REGEXP_REPLACE(TRIM(dt_excepcionalidade), r'\.0$', '')) as data_excepecionalidade,
    SAFE.PARSE_DATE("%Y%m%d",REGEXP_REPLACE(TRIM(dt_inicio), r'\.0$', '')) as data_inicio,
    SAFE.PARSE_DATE("%Y%m%d",REGEXP_REPLACE(TRIM(dt_publicacao_designacao), r'\.0$', '')) as data_publicacao_designacao,
    SAFE.PARSE_DATE("%Y%m%d",REGEXP_REPLACE(TRIM(dt_termino), r'\.0$', '')) as data_termino,
    SAFE.PARSE_DATE("%Y%m%d",REGEXP_REPLACE(TRIM(dt_termo_responsabilidade), r'\.0$', '')) as data_termo_responsabilidade,
    SAFE_CAST(TRIM(escolaridade) AS STRING) AS escolaridade,
    SAFE_CAST(TRIM(matricula) AS STRING) AS matricula_funcionario,
    SAFE_CAST(TRIM(nm_funcionario) AS STRING) AS nome_funcionario,
    SAFE_CAST(TRIM(st_curso_gestao_material) AS STRING) AS curso_gestao_material,
    SAFE_CAST(TRIM(tp_funcionario) AS STRING) AS tipo_responsabilidade,
FROM `rj-smfp.compras_materiais_servicos_sigma_staging.VW_USUARIO_RESPONSAVEL_AUXILIAR` AS t