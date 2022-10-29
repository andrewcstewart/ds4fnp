# import os

# from typing import Any, Dict, Iterable, Optional
# import os
# from kedro.config import ConfigLoader
# from kedro.config import TemplatedConfigLoader
# from kedro.framework.hooks import hook_impl
# from kedro.io import DataCatalog
# # # from kedro.versioning import Journal

# class ProjectHooks:
#     @hook_impl
#     # def register_config_loader(self, conf_paths: Iterable[str]) -> TemplatedConfigLoader:
#     def register_config_loader(self, conf_paths: Iterable[str]) -> ConfigLoader:
#         print( {
#                 k.lower(): v for k, v in os.environ.items() if k.startswith("KEDRO_")
#             })
#         return TemplatedConfigLoader(
#             conf_paths,
#             globals_dict={
#                 k.lower(): v for k, v in os.environ.items() if k.startswith("KEDRO_")
#             },
#             # globals_dict={
#             #     "DB_USERNAME": os.environ.get("KEDRO_DB_USERNAME"),
#             #     "DB_PASSWORD": os.environ.get("KEDRO_DB_PASSWORD"),
#             #     "DB_NAME": os.environ.get("KEDRO_DB_NAME"),
#             # },
#         )


#     # @hook_impl
#     # def register_catalog(
#     #     self,
#     #     catalog: Optional[Dict[str, Dict[str, Any]]],
#     #     credentials: Dict[str, Dict[str, Any]],
#     #     load_versions: Dict[str, str],
#     #     save_version: str,
#     #     # journal: Journal,
#     # ) -> DataCatalog:
#     #     return DataCatalog.from_config(
#     #         catalog, credentials, load_versions, save_version #, journal
#     #     )        