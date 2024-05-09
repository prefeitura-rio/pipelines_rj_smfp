# -*- coding: utf-8 -*-
"""
Database dumping flows for segovi project.
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
from pipelines.ergon.dump_db_ergon_folha_pagamento.schedules import (
    ergon_folha_pagamento_monthly_update_schedule,
)

dump_db_ergon_folha_pagamento_flow = deepcopy(dump_sql_flow)
dump_db_ergon_folha_pagamento_flow.state_handlers = [
    handler_inject_bd_credentials,
    handler_initialize_sentry,
]
dump_db_ergon_folha_pagamento_flow.name = (
    "SMFP: ergon folha pagamento - Ingerir tabelas de banco SQL"
)
dump_db_ergon_folha_pagamento_flow.storage = GCS(constants.GCS_FLOWS_BUCKET.value)
dump_db_ergon_folha_pagamento_flow.run_config = KubernetesRun(
    image=constants.DOCKER_IMAGE.value,
    labels=[
        constants.RJ_SMFP_AGENT_LABEL.value,
    ],
)

ergon_folha_pagamento_default_parameters = {
    "db_database": "P01.PCRJ",
    "db_host": "10.70.6.21",
    "db_port": "1526",
    "db_type": "oracle",
    "infisical_secret_path": "/db-ergon-prod",
    "dataset_id": "recursos_humanos_ergon_folha_pagamento",
}
dump_db_ergon_folha_pagamento_flow = set_default_parameters(
    dump_db_ergon_folha_pagamento_flow, default_parameters=ergon_folha_pagamento_default_parameters
)

dump_db_ergon_folha_pagamento_flow.schedule = ergon_folha_pagamento_monthly_update_schedule
