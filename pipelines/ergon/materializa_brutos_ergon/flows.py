# -*- coding: utf-8 -*-
# """
# Materialize Active SMS Employees from Ergon..
# """

# from copy import deepcopy

# from prefect.run_configs import KubernetesRun
# from prefect.storage import GCS
# from prefeitura_rio.pipelines_templates.run_dbt_model.flows import (
#     templates__run_dbt_model__flow,
# )
# from prefeitura_rio.pipelines_utils.prefect import set_default_parameters
# from prefeitura_rio.pipelines_utils.state_handlers import (
#     handler_initialize_sentry,
#     handler_inject_bd_credentials,
# )

# from pipelines.constants import constants
# from pipelines.ergon.materializa_brutos_ergon.schedules import (
#     smfp_brutos_ergon_daily_update_schedule,
# )

# run_dbt_brutos_ergon = deepcopy(templates__run_dbt_model__flow)
# run_dbt_brutos_ergon.name = "SMFP: brutos_ergon - Materializar tabelas"
# run_dbt_brutos_ergon.state_handlers = [
#     handler_inject_bd_credentials,
#     handler_initialize_sentry,
# ]
# run_dbt_brutos_ergon.storage = GCS(constants.GCS_FLOWS_BUCKET.value)
# run_dbt_brutos_ergon.run_config = KubernetesRun(
#     image=constants.DOCKER_IMAGE.value, labels=[constants.RJ_SMFP_AGENT_LABEL.value]
# )

# smfp_brutos_ergon_default_parameters = {
#     "dataset_id": "brutos_ergon",
#     "table_id": "cargo",
# }
# run_dbt_brutos_ergon = set_default_parameters(
#     run_dbt_brutos_ergon,
#     default_parameters=smfp_brutos_ergon_default_parameters,
# )

# run_dbt_brutos_ergon.schedule = smfp_brutos_ergon_daily_update_schedule
