# encoding: UTF-8
from tdx.engine import Engine
from cn_zipline.bundles.tdx_bundle import *
import os
from zipline.data.bundles import register
from zipline.data import bundles as bundles_module
from functools import partial
from cn_zipline.utils.register import register_tdx


def target_ingest(assets,ingest_minute=False):
    import cn_stock_holidays.zipline.default_calendar

    if assets:
        if not os.path.exists(assets):
            raise FileNotFoundError
        df = pd.read_csv(assets, names=['symbol', 'name'], dtype=str,encoding='utf8')
        register_tdx(df[:1],ingest_minute)
    else:
        df = pd.DataFrame({
            'symbol':['000001'],
            'name':['平安银行']
        })
        register_tdx(df,ingest_minute)

    bundles_module.ingest('tdx',
                          os.environ,
                          pd.Timestamp.utcnow(),
                          show_progress=True,
                          )


def test_target_ingest():
    yield target_ingest,'tests/ETF.csv',True
    yield target_ingest,None,False
