from . import abstract

import importlib


native = abstract
runtime_platform = None


def set_runtime_platform(platform, *args, **kwargs):
    global native
    global runtime_platform
    try:
        native = importlib.import_module(f".{platform.lower()}", "native_ui.impl")
        runtime_platform = platform.lower()
        native.requirements(*args, **kwargs)
    except ImportError:
        raise ValueError(f"{platform} not implemented")

