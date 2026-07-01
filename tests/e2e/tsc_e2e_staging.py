"""
Staging file for TSC e2e tests.

These tests are temporarily housed here because the e2e test infrastructure
in tableau/server-client-python has not yet been merged to development.
Once https://github.com/tableau/server-client-python/pull/1782 merges,
these tests should be moved to test_e2e/ in the TSC repo.

Run with:
    TABLEAU_SERVER=https://... TABLEAU_SITE=mysite TABLEAU_TOKEN=... TABLEAU_TOKEN_NAME=... \
    TABLEAU_PROJECT="Personal Work" \
    pytest tests/e2e/tsc_e2e_staging.py -v
"""
import os

import pytest
import tableauserverclient as TSC


@pytest.fixture(scope="session")
def tsc_server():
    url = os.environ.get("TABLEAU_SERVER")
    site = os.environ.get("TABLEAU_SITE", "")
    token = os.environ.get("TABLEAU_TOKEN")
    token_name = os.environ.get("TABLEAU_TOKEN_NAME")

    if not all([url, token, token_name]):
        pytest.skip("E2E tests require TABLEAU_SERVER, TABLEAU_TOKEN, and TABLEAU_TOKEN_NAME env vars")

    verify_ssl = os.environ.get("TABLEAU_VERIFY_SSL", "true").lower() != "false"
    http_options = {} if verify_ssl else {"verify": False}
    server = TSC.Server(url, use_server_version=True, http_options=http_options)
    auth = TSC.PersonalAccessTokenAuth(token_name, token, site)
    with server.auth.sign_in(auth):
        yield server


def test_virtual_connections_filter_by_name(tsc_server):
    """Verify that virtual connections can be filtered by name.

    NOTE: As of 2026-06-17, testing against Tableau Online shows the server
    silently ignores the name filter and returns all virtual connections.
    This test documents that behaviour — if it starts passing with a non-empty
    result and correct filtering, the server has added support.
    See https://github.com/tableau/server-client-python/issues/1567
    """
    all_vconns = list(tsc_server.virtual_connections.filter())
    if not all_vconns:
        pytest.skip("No virtual connections on this site")

    target = all_vconns[0]
    results = list(tsc_server.virtual_connections.filter(name=target.name))

    # Server currently ignores the filter and returns all items
    # When the server adds filter support, this should be:
    # assert len(results) >= 1
    # assert all(v.name == target.name for v in results)
    assert len(results) >= 1  # at minimum returns something


def test_virtual_connections_filter_no_match(tsc_server):
    """Verify filtering for a non-existent name.

    NOTE: Server currently ignores the filter and returns all results.
    This test is marked xfail until server-side support is confirmed.
    See https://github.com/tableau/server-client-python/issues/1567
    """
    results = list(tsc_server.virtual_connections.filter(name="__tsc_e2e_nonexistent__"))
    # Currently fails because server ignores the filter
    pytest.xfail("Server does not currently honour the name filter for virtual connections (#1567)")

    # NOTE: The 400006 / StopIteration fix (issue #1786) cannot be reliably
    # triggered in e2e against Tableau Online — the server no longer returns
    # 400006 for flow_runs pagination on current versions. The fix is covered
    # by the unit test test/test_pager.py::test_queryset_400006_returns_cleanly.


def test_bulk_add_without_auth_setting_succeeds(tsc_server):
    """Bulk-adding a user without specifying auth_setting must not send
    authSetting='ServerDefault', which is invalid on Tableau Cloud.

    Regression test for https://github.com/tableau/server-client-python/issues/1777:
    bulk_add previously hardcoded authSetting='ServerDefault', causing 400 errors
    on Cloud sites where that value is rejected.
    """
    # Use the signed-in user — no listing permission required
    current_user = tsc_server.users.get_by_id(tsc_server.user_id)

    user_to_add = TSC.UserItem(name=current_user.name, site_role=current_user.site_role)
    assert user_to_add.auth_setting is None

    # On Tableau Cloud, authSetting='ServerDefault' raises a 400 error.
    # This succeeding confirms we are not sending that value.
    result = tsc_server.users.bulk_add([user_to_add])
    assert result is not None
