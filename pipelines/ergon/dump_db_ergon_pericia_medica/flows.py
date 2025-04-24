# -*- coding: utf-8 -*-
"""
Database dumping flows for segovi project
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
from pipelines.ergon.dump_db_ergon_pericia_medica.schedules import (
    ergon_pericia_medica_monthly_update_schedule,
)

dump_db_ergon_pericia_medica_flow = deepcopy(dump_sql_flow)
dump_db_ergon_pericia_medica_flow.state_handlers = [
    handler_inject_bd_credentials,
    handler_initialize_sentry,
]
dump_db_ergon_pericia_medica_flow.name = "SMFP: ergon pericia medica - Ingerir tabelas de banco SQL"
dump_db_ergon_pericia_medica_flow.storage = GCS(constants.GCS_FLOWS_BUCKET.value)
dump_db_ergon_pericia_medica_flow.run_config = KubernetesRun(
    image=constants.DOCKER_IMAGE.value,
    labels=[
        constants.RJ_SMFP_AGENT_LABEL.value,
    ],
)

ergon_pericia_medica_default_parameters = {
    "db_database": "P01.PCRJ",
    "db_host": "10.70.6.21",
    "db_port": "1526",
    "db_type": "oracle",
    "infisical_secret_path": "/db-ergon-prod",
    "dataset_id": "recursos_humanos_ergon_pericia_medica",
}
dump_db_ergon_pericia_medica_flow = set_default_parameters(
    dump_db_ergon_pericia_medica_flow, default_parameters=ergon_pericia_medica_default_parameters
)

dump_db_ergon_pericia_medica_flow.schedule = ergon_pericia_medica_monthly_update_schedule
