SELECT
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_almoxarifado_destino), r'\.0$', '') AS STRING) AS id_almoxarifado_destino,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_almoxarifado_origem), r'\.0$', '') AS STRING) AS id_almoxarifado_origem,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_material), r'\.0$', '') AS STRING) AS id_material,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_movimentacao), r'\.0$', '') AS STRING) AS id_movimentcao,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_os), r'\.0$', '') AS STRING) AS id_organizacao_social,
    SAFE_CAST(REGEXP_REPLACE(TRIM(cd_secretaria), r'\.0$', '') AS STRING) AS id_secretaria,
    SAFE_CAST(TRIM(cnpj_fabricante) AS STRING) AS cnpj_fabricante,
    SAFE_CAST(TRIM(cnpj_fornecedor) AS STRING) AS cnpj_fornecedor,
    SAFE.PARSE_DATE("%Y%m%d",REGEXP_REPLACE(TRIM(data_nota_fiscal), r'\.0$', '')) as data_nota_fiscal,
    SAFE.PARSE_DATE("%Y%m%d",REGEXP_REPLACE(TRIM(data_ultima_atualizacao), r'\.0$', '')) as data_ultima_atualizacao,
    SAFE_CAST(TRIM(ds_almoxarifado_destino) AS STRING) AS descricao_almoxarifado_destino,
    SAFE_CAST(TRIM(ds_almoxarifado_origem) AS STRING) AS descricao_almoxarifado_origem,
    SAFE_CAST(TRIM(ds_movimentacao) AS STRING) AS tipo_movimentcao,
    SAFE_CAST(TRIM(ds_secretaria) AS STRING) AS descricao_secretaria,
    SAFE_CAST(DATE(dt_fim_contrato_os) AS DATE) AS data_fim_contrato,
    SAFE_CAST(DATE(dt_ini_contrato_os) AS DATE) AS data_inicio_contrato,
    SAFE_CAST(TRIM(nota_fiscal) AS STRING) AS nota_fiscal,
    SAFE_CAST(REGEXP_REPLACE(TRIM(nr_empenho), r'\.0$', '') AS STRING) AS id_empenho,
    SAFE_CAST(REGEXP_REPLACE(preco_item, r',', '.') AS FLOAT64) AS preco_item,
    SAFE_CAST(REGEXP_REPLACE(TRIM(quantidade_item), r'\.0$', '') AS INT64) AS quantidade_item,
    SAFE_CAST(TRIM(serie) AS STRING) AS serie_nota_fiscal,
    SAFE_CAST(REGEXP_REPLACE(TRIM(total_item), r'\.0$', '') AS INT64) AS total_item,
    SAFE_CAST(TRIM(tp_almoxarifado) AS STRING) AS tipo_almoxarifado,
FROM `rj-smfp.compras_materiais_servicos_sigma_staging.VW_MOVIMENTACAO` AS t