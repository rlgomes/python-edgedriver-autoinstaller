
def test_get_edge_version():
    from chromedriver_autoinstaller.utils import get_edge_version
    version = get_edge_version()
    assert version is None or version.count('.') == 3