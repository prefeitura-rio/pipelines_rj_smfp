# -*- coding: utf-8 -*-
"""
Database dumping flows for SMFP FINCON
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
from pipelines.fincon.dump_db_fincon.schedules import fincon_infra_clocks

rj_smfp_dump_db_fincon_flow = deepcopy(dump_sql_flow)
rj_smfp_dump_db_fincon_flow.state_handlers = [
    handler_inject_bd_credentials,
    handler_initialize_sentry,
]
rj_smfp_dump_db_fincon_flow.name = (
    "SMFP: FINCON - administracao_instrumentos_firmados - Ingerir tabelas de banco SQL"
)
rj_smfp_dump_db_fincon_flow.storage = GCS(constants.GCS_FLOWS_BUCKET.value)

rj_smfp_dump_db_fincon_flow.run_config = KubernetesRun(
    image=constants.DOCKER_IMAGE.value,
    labels=[
        constants.RJ_SMFP_AGENT_LABEL.value,
    ],
)

rj_smfp_dump_db_fincon_default_parameters = {
    "db_database": "DW_IGAA",
    "db_host": "10.2.221.17",
    "db_port": "1433",
    "db_type": "sql_server",
    "dataset_id": "adm_instrumentos_firmados",
    "infisical_secret_path": "/db-fincon",
}

rj_smfp_dump_db_fincon_flow = set_default_parameters(
    rj_smfp_dump_db_fincon_flow,
    default_parameters=rj_smfp_dump_db_fincon_default_parameters,
)

rj_smfp_dump_db_fincon_flow.schedule = fincon_infra_clocks
