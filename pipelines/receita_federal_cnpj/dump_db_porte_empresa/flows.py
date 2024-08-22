# -*- coding: utf-8 -*-
"""
Database dumping flows
"""

from copy import deepcopy

from prefect.run_configs import KubernetesRun
from prefect.storage import GCS
from prefeitura_rio.pipelines_templates.dump_db.flows import flow as dump_sql_flow
from prefeitura_rio.pipelines_utils.prefect import set_default_parameters
from prefeitura_rio.pipelines_utils.state_handlers import (
    handler_initialize_sentry,
    handler_inject_bd_credentials,
)

from pipelines.constants import constants

from pipelines.receita_federal_cnpj.dump_db_porte_empresa.schedules import (
    porte_empresa_schedule,
)

porte_empresa_flow = deepcopy(dump_sql_flow)
porte_empresa_flow.name = "SMFP: CNPJ porte_empresa - Ingerir tabelas de banco SQL"
porte_empresa_flow.state_handlers = [handler_inject_bd_credentials, handler_initialize_sentry]
porte_empresa_flow.storage = GCS(constants.GCS_FLOWS_BUCKET.value)
porte_empresa_flow.run_config = KubernetesRun(
    image=constants.DOCKER_IMAGE.value,
    labels=[
        constants.RJ_SMFP_AGENT_LABEL.value,
    ],
)
porte_empresa_default_parameters = {
    "db_database": "CLUSTERSQL2",
    "db_host": "10.70.1.34",
    "db_port": "1433",
    "db_type": "sql_server",
    "dataset_id": "porte_empresa",
    "infisical_secret_path": "/db-porte-empresa",
}
porte_empresa_flow = set_default_parameters(
    porte_empresa_flow, default_parameters=porte_empresa_default_parameters
)

porte_empresa_flow.schedule = porte_empresa_schedule
