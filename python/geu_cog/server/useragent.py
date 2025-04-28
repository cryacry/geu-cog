from importlib.metadata import version


def _get_version() -> str:
    try:
        return version("geu_cog")
    except Exception:  # pylint: disable=broad-exception-caught
        return "unknown"


def get_user_agent() -> str:
    return f"geu_cog-worker/{_get_version()}"
