from .settings import Settings
from .workspace import WorkSpace
from .framework import App


def create_tool(settings=Settings, workspace=WorkSpace):
    app = App(name='msph')
    app.register_settings(settings)
    app.register_workspace(workspace)
    
    from .commands.router import root_router
    app.register_root_router(root_router)

    return app