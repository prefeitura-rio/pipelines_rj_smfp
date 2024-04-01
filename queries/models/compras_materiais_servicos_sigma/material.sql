SELECT
    SAFE_CAST(TRIM(acondicionamento) AS STRING) AS acondicionamento ,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_classe), r'\.0$', '') AS STRING) AS id_classe,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_comprasnet), r'\.0$', '') AS STRING) AS id_compras_net,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_grupo), r'\.0$', '') AS STRING) AS id_grupo,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_material), r'\.0$', '') AS STRING) AS id_material,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_material_substituto), r'\.0$', '') AS STRING) AS id_material_substituto,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_subclasse), r'\.0$', '') AS STRING) AS id_subclasse,
    SAFE_CAST(TRIM(ds_detalhe_material) AS STRING) AS descricao_detalhada ,
    SAFE.PARSE_DATE("%Y%m%d",REGEXP_REPLACE(TRIM(dt_desativacao), r'\.0$', '')) as data_desativacao,
    SAFE_CAST(TRIM(dv1) AS STRING) AS digito_verificador_1,
    SAFE_CAST(TRIM(dv2) AS STRING) AS digito_verificador_2,
    SAFE_CAST(TRIM(nm_complementar_material) AS STRING) AS nome_complementar_material,
    SAFE_CAST(TRIM(nm_fantasia) AS STRING) AS nome_fantasia,
    SAFE_CAST(TRIM(nm_padronizado) AS STRING) AS nome_padronizado_material,
    SAFE_CAST(TRIM(observacao) AS STRING) AS observacao,
    SAFE_CAST(TRIM(remume) AS STRING) AS tabela_remume,
    SAFE_CAST(REGEXP_REPLACE(TRIM(sequencial), r'\.0$', '') AS STRING) AS id_sequencial,
    SAFE_CAST(TRIM(st_continuado) AS STRING) AS medicamento_continuado,
    SAFE_CAST(TRIM(st_controlado) AS STRING) AS medicamento_controlado,
    SAFE_CAST(TRIM(st_item_sustentavel) AS STRING) AS item_sustentavel,
    SAFE_CAST(TRIM(st_padronizado) AS STRING) AS medicamento_padronizado,
    SAFE_CAST(TRIM(st_referencia) AS STRING) AS referencia,
    SAFE_CAST(TRIM(st_sistema_registro_preco) AS STRING) AS registro_preco,
    SAFE_CAST(TRIM(st_status) AS STRING) AS status_material,
    SAFE_CAST(TRIM(st_tabelado) AS STRING) AS medicamento_tabelado,
    SAFE_CAST(TRIM(st_uso_geral) AS STRING) AS medicamento_uso_geral,
    SAFE_CAST(TRIM(termolabel) AS STRING) AS medicamento_refrigerado ,
    SAFE_CAST(TRIM(tp_genero) AS STRING) AS genero_alimenticio,
    SAFE_CAST(TRIM(tp_material) AS STRING) AS tipo_material,
    SAFE_CAST(TRIM(unidade) AS STRING) AS unidade_consumo,
FROM `rj-smfp.compras_materiais_servicos_sigma_staging.material` AS t