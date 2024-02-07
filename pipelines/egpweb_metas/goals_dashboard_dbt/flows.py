# -*- coding: utf-8 -*-
"""
DBT-related flows.
"""

from copy import deepcopy

from prefect.run_configs import KubernetesRun
from prefect.storage import GCS
from prefeitura_rio.pipelines_templates.run_dbt_model.flows import (
    templates__run_dbt_model__flow,
)
from prefeitura_rio.pipelines_utils.prefect import set_default_parameters
from prefeitura_rio.pipelines_utils.state_handlers import handler_inject_bd_credentials

from pipelines.constants import constants
from pipelines.egpweb_metas.goals_dashboard_dbt.schedules import (
    smfp_dashboard_metas_daily_update_schedule,
)

run_dbt_smfp_dashboard_metas_flow = deepcopy(templates__run_dbt_model__flow)
run_dbt_smfp_dashboard_metas_flow.name = "SMFP: Dashboard de Metas - Materializar tabelas"
run_dbt_smfp_dashboard_metas_flow.state_handlers = [handler_inject_bd_credentials]
run_dbt_smfp_dashboard_metas_flow.storage = GCS(constants.GCS_FLOWS_BUCKET.value)
run_dbt_smfp_dashboard_metas_flow.run_config = KubernetesRun(image=constants.DOCKER_IMAGE.value)

smfp_dashboard_metas_default_parameters = {
    "dataset_id": "planejamento_gestao_dashboard_metas",
    "upstream": True,
    "materialize_to_datario": False,
}
run_dbt_smfp_dashboard_metas_flow = set_default_parameters(
    run_dbt_smfp_dashboard_metas_flow,
    default_parameters=smfp_dashboard_metas_default_parameters,
)

run_dbt_smfp_dashboard_metas_flow.schedule = smfp_dashboard_metas_daily_update_schedule
