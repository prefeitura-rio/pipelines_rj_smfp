# -*- coding: utf-8 -*-
"""
Database dumping flows...
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

# from pipelines.iptu_inad.dump_db_inadimplentes.schedules import (
#     inadimplente_weekly_update_schedule,
# )

smfp_inadimplente_flow = deepcopy(dump_sql_flow)
smfp_inadimplente_flow.name = "SMFP: Inadimplentes - Ingerir tabelas de banco SQL"
smfp_inadimplente_flow.state_handlers = [handler_inject_bd_credentials, handler_initialize_sentry]
smfp_inadimplente_flow.storage = GCS(constants.GCS_FLOWS_BUCKET.value)
smfp_inadimplente_flow.run_config = KubernetesRun(
    image=constants.DOCKER_IMAGE.value,
    labels=[
        constants.RJ_SMFP_AGENT_LABEL.value,
    ],
)

inadimplente_default_parameters = {
    "db_database": "DBINAD",
    "db_host": "10.3.23.158",
    "db_port": "1433",
    "db_type": "sql_server",
    "dataset_id": "iptu_inadimplentes",
    "infisical_secret_path": "db-iptu-inadimplentes",
}
smfp_inadimplente_flow = set_default_parameters(
    smfp_inadimplente_flow, default_parameters=inadimplente_default_parameters
)

# smfp_inadimplente_flow.schedule = inadimplente_weekly_update_schedule
