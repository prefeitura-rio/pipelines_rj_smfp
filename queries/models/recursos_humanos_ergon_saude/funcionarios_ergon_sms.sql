WITH all_cpf AS (
  SELECT
    DISTINCT
      cpf
  FROM (
    SELECT
        cpf,
        'sms' AS origin
    FROM `rj-sms.saude_dados_mestres.profissional_saude`
    WHERE cpf IS NOT NULL
    UNION ALL
    SELECT
        cpf,
        'ergon' AS origin
    FROM `rj-smfp.recursos_humanos_ergon_saude.funcionarios_ativos`
    WHERE cpf IS NOT NULL
  )
),

funcionarios AS (
  SELECT
    cpf.cpf,
    ps.cpf AS cpf_sms,
    ps.nome AS nome_sms,
    fa.cpf AS cpf_ergon,
    fa.nome AS nome_ergon
  FROM all_cpf cpf
  LEFT JOIN `rj-sms.saude_dados_mestres.profissional_saude` ps
    ON cpf.cpf = ps.cpf
  LEFT JOIN `rj-smfp.recursos_humanos_ergon_saude.funcionarios_ativos` fa
    ON cpf.cpf = fa.cpf
),

funcionarios_check AS (
  SELECT
    cpf,
    cpf_sms,
    cpf_ergon,
    nome_sms,
    nome_ergon,
    CASE
      WHEN cpf_sms IS NOT NULL AND cpf_ergon IS NOT NULL THEN 'both'
      WHEN cpf_sms IS NOT NULL THEN 'sms'
      WHEN cpf_ergon IS NOT NULL THEN 'ergon'
      ELSE 'none'
    END AS check
  FROM funcionarios
)


-- SELECT *
-- FROM funcionarios_check

SELECT
  check,
  COUNT(*) AS count
FROM funcionarios_check
GROUP BY 1
ORDER BY 2