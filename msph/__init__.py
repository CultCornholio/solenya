from msph.framework.cli import App

from .workspace import WorkSpace

workspace = WorkSpace(hidden=True)

def create_tool():
    app = App(name='msph')

    app.register_plugin(workspace)
    
    from .commands.router import root_router
    app.register_root_router(root_router)

    return app