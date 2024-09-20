WITH funcionarios AS (
	SELECT
		f.id_vinculo AS id_funcionario,
		LPAD(f.id_cpf, 11, '0') AS cpf,  -- Adiciona zero à esquerda caso o CPF tenha menos de 11 dígitos
		f.nome
	FROM `rj-smfp.recursos_humanos_ergon.funcionario` f
	-- WHERE LPAD(f.id_cpf, 11, '0') = ''
),

provimento AS (
	SELECT
		p.id_funcionario,
		p.id_vinculo,
		p.data_inicio AS provimento_inicio,
		p.data_fim AS provimento_fim,
		p.id_setor,
		p.id_cargo,
		p.empresa_vinculo AS id_empresa
	FROM `rj-smfp.recursos_humanos_ergon.provimento` p
	-- QUALIFY ROW_NUMBER() OVER (PARTITION BY id_funcionario ORDER BY id_vinculo DESC, data_inicio DESC) = 1
),

setor AS (
  SELECT
    id_setor,
    data_inicio AS setor_inicio,
    data_fim AS setor_fim,
    id_setor_pai,
    nome AS setor_nome,
    sigla AS setor_sigla,
    id_secretaria -- SAUDE 1800 (consultar SICI)
  FROM `rj-smfp.recursos_humanos_ergon.setor`
  -- WHERE data_fim IS NULL
  QUALIFY ROW_NUMBER() OVER (PARTITION BY id_setor ORDER BY data_inicio DESC) = 1
),

cargo AS (
  SELECT
    id_cargo,
    nome AS cargo_nome,
    categoria AS cargo_categoria,
    subcategoria AS cargo_subcategoria
  FROM `rj-smfp.recursos_humanos_ergon.cargo`
  -- WHERE data_fim IS NULL
),

vacancia_vinculo AS (
  SELECT
    id_funcionario,
    id_vinculo,
    data_vacancia
  FROM `rj-smfp.recursos_humanos_ergon.vinculo`
  QUALIFY ROW_NUMBER() OVER (PARTITION BY id_funcionario ORDER BY id_vinculo DESC) = 1
),

empresa AS (
  SELECT
    id_empresa,
    nome_empresa AS empresa_nome,
    sigla AS empresa_sigla
  FROM `rj-smfp.recursos_humanos_ergon.empresas`
),

funcionarios_saude AS (
  SELECT
    f.cpf,
    f.nome,
    CASE
      WHEN (p.provimento_fim IS NULL) AND (vv.data_vacancia IS NULL) THEN TRUE
      ELSE FALSE
    END AS status_ativo,
    p.provimento_inicio,
    p.provimento_fim,
    vv.data_vacancia,
    s.id_secretaria,
    p.id_empresa,
    s.setor_nome,
    s.setor_sigla,
    s.setor_inicio,
    s.setor_fim,
    c.cargo_nome,
    c.cargo_categoria,
    c.cargo_subcategoria,
    emp.empresa_nome,
    emp.empresa_sigla
  FROM funcionarios f
  LEFT JOIN provimento p
    ON f.id_funcionario = p.id_funcionario
  LEFT JOIN setor s
    ON p.id_setor = s.id_setor
  LEFT JOIN cargo c
    ON p.id_cargo = c.id_cargo
  LEFT JOIN vacancia_vinculo vv
    ON  f.id_funcionario = vv.id_funcionario
    AND p.id_vinculo = vv.id_vinculo
  LEFT JOIN empresa emp
    ON p.id_empresa = emp.id_empresa
  WHERE
  -- (p.provimento_fim IS NULL)
  -- AND (vv.data_vacancia IS NULL) AND
  (
    s.id_secretaria = '1800'
  OR p.id_empresa IN ('32','80','81','82','83','84','85','86','87','88','89','90','92','95','97')
  )
)


SELECT * FROM funcionarios_saude
WHERE status_ativo