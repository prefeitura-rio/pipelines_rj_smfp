# -*- coding: utf-8 -*-
"""
Database dumping flows for smfp ergon comlurb....
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
from pipelines.ergon_comlurb.dump_db_ergon_comlurb.schedules import (
    ergon_comlurb_daily_update_schedule,
)

dump_ergon_flow = deepcopy(dump_sql_flow)
dump_ergon_flow.name = "SMFP: ergon comlurb - Ingerir tabelas de banco SQL"
dump_ergon_flow.state_handlers = [handler_inject_bd_credentials, handler_initialize_sentry]
dump_ergon_flow.storage = GCS(constants.GCS_FLOWS_BUCKET.value)
dump_ergon_flow.run_config = KubernetesRun(
    image=constants.DOCKER_IMAGE.value,
    labels=[
        constants.RJ_SMFP_AGENT_LABEL.value,
    ],
)

ergon_default_parameters = {
    "db_database": "P25",
    "db_host": "10.70.6.26",
    "db_port": "1521",
    "db_type": "oracle",
    "infisical_secret_path": "/db-ergon-comlurb",
    "dataset_id": "recursos_humanos_ergon_comlurb",
}
dump_ergon_flow = set_default_parameters(
    dump_ergon_flow, default_parameters=ergon_default_parameters
)

dump_ergon_flow.schedule = ergon_comlurb_daily_update_schedule
