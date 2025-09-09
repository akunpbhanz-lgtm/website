import typer
from . import config
from .rag import ingest as rag_ingest
from .rag import query as rag_query
from .tools.shell_tool import run_shell

app = typer.Typer(help="Codex Mini (FREE) CLI")


@app.command()
def ingest(docs: str):
    """Ingest documentation into the local knowledge base."""
    rag_ingest.ingest_docs(docs)


@app.command()
def plan(task: str):
    """Plan a task using the ingested documents."""
    result = rag_query.query_docs(task)
    typer.echo(result)


@app.command()
def run(task: str = "", mode: str | None = None):
    """Run a shell command respecting guardrails."""
    if mode:
        config.set_mode(mode)
    current = config.load_config()["mode"]
    typer.echo(f"Running in {current} mode")
    if task:
        output = run_shell(task)
        typer.echo(output)


@app.command()
def dryrun(task: str):
    """Preview a shell command without executing."""
    typer.echo(f"Dryrun: {task}")


@app.command("set-mode")
def set_mode_cli(mode: str):
    """Persist execution mode."""
    config.set_mode(mode)
    typer.echo(f"Mode set to {mode}")


if __name__ == "__main__":
    app()
