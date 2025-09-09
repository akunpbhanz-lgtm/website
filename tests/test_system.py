import pathlib
import pytest
from agent.rag import ingest, query
from agent.tools.shell_tool import run_shell


def test_rag_ingest_query(tmp_path):
    p = tmp_path / "doc.md"
    p.write_text("hello world")
    ingest.ingest_docs(str(tmp_path))
    result = query.query_docs("hello")
    assert "hello world" in result


def test_shell_tool_allowed():
    assert run_shell("echo hi") == "hi"


def test_shell_tool_denied():
    with pytest.raises(ValueError):
        run_shell("rm -rf /")


def test_browser_denied_domain():
    from agent.tools import browser
    with pytest.raises(ValueError):
        browser.browse("https://example.com")
