from msph.framework.cli import CliApp

from .workspace import WorkSpace

workspace = WorkSpace(hidden=True)

def create_app():
    app = CliApp(name='msph')

    app.register_plugin(workspace)
    
    from .commands.router import root_router
    app.register_root_router(root_router)

    return app
