# -*- coding: utf-8 -*-
"""
Materialize Active SMS Employees from Ergon
"""

from copy import deepcopy

from prefect.run_configs import KubernetesRun
from prefect.storage import GCS
from prefeitura_rio.pipelines_templates.run_dbt_model.flows import (
    templates__run_dbt_model__flow,
)
from prefeitura_rio.pipelines_utils.prefect import set_default_parameters
from prefeitura_rio.pipelines_utils.state_handlers import (
    handler_initialize_sentry,
    handler_inject_bd_credentials,
)

from pipelines.constants import constants
from pipelines.ergon.materializa_funcionarios_saude.schedules import (
    smfp_funcionarios_saude_daily_update_schedule,
)

run_dbt_smfp_funcionarios_saude = deepcopy(templates__run_dbt_model__flow)
run_dbt_smfp_funcionarios_saude.name = "SMFP: brutos_ergon - Materializar tabelas"
run_dbt_smfp_funcionarios_saude.state_handlers = [
    handler_inject_bd_credentials,
    handler_initialize_sentry,
]
run_dbt_smfp_funcionarios_saude.storage = GCS(constants.GCS_FLOWS_BUCKET.value)
run_dbt_smfp_funcionarios_saude.run_config = KubernetesRun(
    image=constants.DOCKER_IMAGE.value, labels=[constants.RJ_SMFP_AGENT_LABEL.value]
)

smfp_funcionarios_saude_default_parameters = {
    "dataset_id": "brutos_ergon",
    "table_id": "cargo",
}
run_dbt_smfp_funcionarios_saude = set_default_parameters(
    run_dbt_smfp_funcionarios_saude,
    default_parameters=smfp_funcionarios_saude_default_parameters,
)

run_dbt_smfp_funcionarios_saude.schedule = smfp_funcionarios_saude_daily_update_schedule
