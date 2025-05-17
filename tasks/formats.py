"""Format tasks for pyinvoke."""

# %% IMPORTS

from invoke.context import Context
from invoke.tasks import task

# %% TASKS


@task
def imports(ctx: Context) -> None:
    """Format python imports with isort."""
    ctx.run("uv run isort src/ tasks/ tests/")


@task
def sources(ctx: Context) -> None:
    """Format python sources with black."""
    ctx.run("uv run black src/ tasks/ tests/")


@task(pre=[imports, sources], default=True)
def all(_: Context) -> None:
    """Run all format tasks."""
