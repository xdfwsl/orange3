# This module is a mixture of imports and code, so we allow import anywhere
# pylint: disable=wrong-import-position,wrong-import-order

# Orange3 Chinese Edition: set Chinese as default language
import os as _os
_os.environ.setdefault("ORANGE_LANG", "Chinese")

# Auto-deploy Chinese translation files to orangecanvas/orangewidget on first use
def _deploy_chinese_translations():
    import importlib, shutil
    _i18n_dir = _os.path.join(_os.path.dirname(__file__), "i18n")
    for src_name, pkg in [("orangecanvas_Chinese.json", "orangecanvas"),
                          ("orangewidget_Chinese.json", "orangewidget")]:
        src = _os.path.join(_i18n_dir, src_name)
        if not _os.path.exists(src):
            continue
        try:
            mod = importlib.import_module(pkg)
            dst = _os.path.join(_os.path.dirname(mod.__file__), "i18n", "Chinese.json")
            if not _os.path.exists(dst):
                shutil.copy2(src, dst)
        except ImportError:
            pass
    # Patch orangecanvas to use utf-8 for JSON loading
    try:
        mod = importlib.import_module("orangecanvas.localization")
        loc_file = mod.__file__
        with open(loc_file, "r", encoding="utf-8") as f:
            content = f.read()
        if 'encoding="utf-8"' not in content:
            content = content.replace(
                "with open(path) as handle:",
                'with open(path, encoding="utf-8") as handle:')
            with open(loc_file, "w", encoding="utf-8") as f:
                f.write(content)
    except Exception:
        pass

try:
    _deploy_chinese_translations()
except Exception:
    pass

from Orange import data

from .misc.lazy_module import _LazyModule
from .misc.datasets import _DatasetInfo
from .version import \
    short_version as __version__, git_revision as __git_version__

ADDONS_ENTRY_POINT = 'orange.addons'

for mod_name in ['classification', 'clustering', 'distance', 'ensembles',
                 'evaluation', 'misc', 'modelling', 'preprocess', 'projection',
                 'regression', 'statistics', 'version', 'widgets']:
    globals()[mod_name] = _LazyModule(mod_name)

datasets = _DatasetInfo()

del mod_name

# A hack that prevents segmentation fault with Nvidia drives on Linux if Qt's browser window
# is shown (seen in https://github.com/spyder-ide/spyder/pull/7029/files)
try:
    import ctypes
    ctypes.CDLL("libGL.so.1", mode=ctypes.RTLD_GLOBAL)
except:  # pylint: disable=bare-except
    pass
finally:
    del ctypes
