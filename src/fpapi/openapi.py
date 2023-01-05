from fastapi.openapi.utils import get_openapi


class OpenApiSchema:
    def __init__(self, app_routes):
        self.cache = None
        self.app_routes = app_routes

    def get_openapi(self):
        if self.cache is not None:
            return self.cache

        openapi_schema = get_openapi(
            title="APIs for Financial Planning💰 [WIP]",
            version="0.1.0",
            description="Easy pension estimations, income predictions, etc.",
            servers=[{"description": "This Server", "url": "/"}],
            routes=self.app_routes
        )

        self.cache = openapi_schema

        return self.cache
