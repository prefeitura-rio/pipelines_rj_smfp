# -*- coding: utf-8 -*-
"""
Database dumping flows for EGPWeb project..
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
from pipelines.egpweb_metas.dump_db_metas.schedules import (
    egp_web_weekly_update_schedule,
)

smfp_egpweb_flow = deepcopy(dump_sql_flow)
smfp_egpweb_flow.name = "SMFP: EGPWeb - Ingerir tabelas de banco SQL"
smfp_egpweb_flow.state_handlers = [handler_inject_bd_credentials, handler_initialize_sentry]
smfp_egpweb_flow.storage = GCS(constants.GCS_FLOWS_BUCKET.value)
smfp_egpweb_flow.run_config = KubernetesRun(
    image=constants.DOCKER_IMAGE.value,
    labels=[
        constants.RJ_SMFP_AGENT_LABEL.value,
    ],
)

egpweb_default_parameters = {
    "db_database": "EGPWEB_PRD",
    "db_host": "10.2.221.101",
    "db_port": "1433",
    "db_type": "sql_server",
    "infisical_secret_path": "/db-egpweb-prod",
    "materialization_mode": "prod",
    "dataset_id": "planejamento_gestao_acordo_resultados",
    "materialize_to_datario": False,
}
smfp_egpweb_flow = set_default_parameters(
    smfp_egpweb_flow, default_parameters=egpweb_default_parameters
)

smfp_egpweb_flow.schedule = egp_web_weekly_update_schedule
