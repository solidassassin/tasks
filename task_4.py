from pathlib import Path
from tempfile import NamedTemporaryFile

from pytest import fixture
from click.testing import CliRunner
from pytest_click_app.upper_case_file import upper_case_file


def items():
    p = Path("pytest_click_app/data")
    inputs = sorted(p.glob("*.input.txt"))
    outputs = sorted(p.glob("*.output.txt"))
    return zip(inputs, outputs)


@fixture(scope="module")
def runner():
    return CliRunner()


@fixture(scope="session", params=items())
def pair(request):
    return request.param


def test_output(runner, pair):
    inp, out = pair
    temp = NamedTemporaryFile(mode='w+')
    result = runner.invoke(
        upper_case_file,
        ("--input-file", inp, "--output-file", temp.name)
    )
    assert result.exit_code == 0
    with open(out) as f:
        assert f.read() == temp.read()
