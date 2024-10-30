# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD
MATERIALIZA MODELOS DO DBT..............
=======
MATERIALIZA MODELOS DO DBT...
>>>>>>> 9248dea3c889cc0dd0466f8c2e75465ca1dbf796
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

templates__run_dbt_model_smas__flow = deepcopy(templates__run_dbt_model__flow)
templates__run_dbt_model_smas__flow.state_handlers = [handler_inject_bd_credentials]

templates__run_dbt_model_smas__flow.storage = GCS(constants.GCS_FLOWS_BUCKET.value)
templates__run_dbt_model_smas__flow.run_config = KubernetesRun(
    image=constants.DOCKER_IMAGE.value,
    labels=[
        constants.RJ_SMFP_AGENT_LABEL.value,
    ],
)

templates_run_dbt_model_smas_default_parameters = {
    "dataset_id": "dataset_id",
    "table_id": "table_id",
}
templates__run_dbt_model_smas__flow = set_default_parameters(
    templates__run_dbt_model_smas__flow,
    default_parameters=templates_run_dbt_model_smas_default_parameters,
)

# add comment to trigger build
