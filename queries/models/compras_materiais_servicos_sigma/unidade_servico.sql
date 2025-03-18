SELECT
  SAFE_CAST(NR_UNIDADE AS INT64) AS id_unidade_servico,
  SAFE_CAST(Ds_Unidade_Servico AS STRING) AS descricao_unidade_servico

from {{ source('compras_materiais_servicos_sigma_staging', 'VW_UNIDADE_SERVICO')}}