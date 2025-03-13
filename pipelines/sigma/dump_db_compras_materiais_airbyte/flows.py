# -*- coding: utf-8 -*-
"""
DBT flows for SMFP SIGMA COMPRAS MATERIAIS.
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
from pipelines.sigma.dump_db_compras_materiais_airbyte.schedules import (
    compras_sigma_daily_update_schedule,
)

rj_smfp_dump_db_sigma_medicamentos_flow = deepcopy(templates__run_dbt_model__flow)
rj_smfp_dump_db_sigma_medicamentos_flow.name = (
    "SMFP: SIGMA - Compras Materiais Serviços - Materializar tabelas"
)
rj_smfp_dump_db_sigma_medicamentos_flow.state_handlers = [
    handler_inject_bd_credentials,
    handler_initialize_sentry,
]
rj_smfp_dump_db_sigma_medicamentos_flow.storage = GCS(constants.GCS_FLOWS_BUCKET.value)
rj_smfp_dump_db_sigma_medicamentos_flow.run_config = KubernetesRun(
    image=constants.DOCKER_IMAGE.value,
    labels=[
        constants.RJ_SMFP_AGENT_LABEL.value,
    ],
)

rj_smfp_dump_db_sigma_medicamentos_default_parameters = {
    "dataset_id": "compras_materiais_servicos_sigma_airbyte",
    "upstream": True,
    "materialize_to_datario": False,
}
rj_smfp_dump_db_sigma_medicamentos_flow = set_default_parameters(
    rj_smfp_dump_db_sigma_medicamentos_flow,
    default_parameters=rj_smfp_dump_db_sigma_medicamentos_default_parameters,
)
rj_smfp_dump_db_sigma_medicamentos_flow.schedule = compras_sigma_daily_update_schedule

# comment to trigger build.
