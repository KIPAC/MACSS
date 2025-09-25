import pytest

from macss import utility_functions

@pytest.fixture(name="setup_data", scope="session")
def setup_data(request: pytest.FixtureRequest) -> int:
    ret_val = utility_functions.setup_data()

    request.addfinalizer(utility_functions.teardown_datq)

    return ret_val
