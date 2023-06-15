# -*- coding: utf-8 -*-

from acore_conf import api


def test():
    _ = api


if __name__ == "__main__":
    from acore_conf.tests import run_cov_test

    run_cov_test(__file__, "acore_conf.api", preview=False)
