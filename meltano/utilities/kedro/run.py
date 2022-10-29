from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project
from pathlib import Path
import os

class set_directory(object):
    """Sets the cwd within the context

    Args:
        path (Path): The path to the cwd
    """
    def __init__(self, path: Path):
        self.path = path
        self.origin = Path().absolute()
    def __enter__(self):
        os.chdir(self.path)
    def __exit__(self, exc_type, exc_value, exc_traceback):
        os.chdir(self.origin)

def main():
    env_var = "KEDRO_PROJECT_ROOT"
    project_root = Path(os.environ.get(env_var, Path.cwd())).absolute()

    with set_directory(project_root):
        print(Path.cwd())
        metadata = bootstrap_project(Path.cwd())
        with KedroSession.create(metadata.package_name) as session:
            session.run()

if __name__ == "__main__":
    main()
