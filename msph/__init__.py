from .app import CliApp
from .settings import Settings
from .config import Config
from .workspace import WorkSpace

settings = Settings()
wsp = WorkSpace()

def create_app(config = Config):
    app = CliApp(__name__)

    app.register_config(config)
    app.register_settings(settings)
    app.register_plugin(wsp)

    from .commands.root import msph
    parser = msph.assemble_parser(app=app)
    app.register_parser(parser)

    return app