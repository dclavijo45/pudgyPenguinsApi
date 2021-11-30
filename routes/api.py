from controllers.apiPudgyPenguinsController import ApiPudgyPenguinsController
from controllers.paginatorPubgyPenguinsController import PaginatorPudgyPenguinsController

api_v1 = {
    "api": "/api/v1/",
    "api_controller": ApiPudgyPenguinsController.as_view("api"),
    # ----------------------------------------------------------------

    "api_by_id": "/api/v1/<id>/",
    "api_controller_by_id": ApiPudgyPenguinsController.as_view("api_by_id"),
    # ----------------------------------------------------------------

    "api_paginator": "/api/v1/page/<page>/",
    "api_controller_paginator": PaginatorPudgyPenguinsController.as_view("api_paginator"),
    # ----------------------------------------------------------------
    
}