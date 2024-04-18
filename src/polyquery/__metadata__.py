"""Project metadata."""
import importlib.metadata

__all__ = ("__version__", "__name__",)



# __version__ = importlib.metadata.version("polyquery")
__version__ = "0.1.0"
"""Version of the project."""
__project__ = importlib.metadata.metadata("polyquery")["Name"]
"""Name of the project."""
