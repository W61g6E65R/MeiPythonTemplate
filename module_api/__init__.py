import importlib
import pkgutil
from fastapi import APIRouter

def include_all_routers(app, package_name:str, package_path):
    for _, module_name, _ in pkgutil.iter_modules(package_path):
        module = importlib.import_module(f"{package_name}.routes.{module_name}")
        if hasattr(module, "router") and isinstance(module.router, APIRouter):
            app.include_router(module.router)