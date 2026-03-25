#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup Chinese localization for Orange3.

This script deploys Chinese translation files to the correct locations
and patches the localization module to support Chinese as default language.

Usage:
    python -m Orange.i18n.setup_chinese
"""
import os
import sys
import shutil
import importlib


def get_package_i18n_dir(package_name):
    """Get the i18n directory for an installed package."""
    try:
        mod = importlib.import_module(package_name)
        return os.path.join(os.path.dirname(mod.__file__), "i18n")
    except ImportError:
        return None


def deploy_translations():
    """Deploy Chinese.json files to all Orange packages."""
    script_dir = os.path.dirname(os.path.abspath(__file__))

    deployments = [
        ("Chinese.json", "Orange"),
        ("orangecanvas_Chinese.json", "orangecanvas"),
        ("orangewidget_Chinese.json", "orangewidget"),
    ]

    for src_name, package in deployments:
        src = os.path.join(script_dir, src_name)
        if not os.path.exists(src):
            print(f"  Warning: {src_name} not found, skipping {package}")
            continue

        i18n_dir = get_package_i18n_dir(package)
        if i18n_dir is None:
            print(f"  Warning: {package} not installed, skipping")
            continue

        dst = os.path.join(i18n_dir, "Chinese.json")
        shutil.copy2(src, dst)
        print(f"  {package}: deployed Chinese.json")


def patch_localization():
    """Patch orangecanvas localization to use utf-8 and support ORANGE_LANG."""
    try:
        loc_file = os.path.join(
            os.path.dirname(importlib.import_module("orangecanvas").__file__),
            "localization", "__init__.py"
        )
    except ImportError:
        print("  orangecanvas not installed, skipping patch")
        return

    with open(loc_file, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False

    # Fix: ensure utf-8 encoding when loading JSON
    if 'encoding="utf-8"' not in content:
        content = content.replace(
            "with open(path) as handle:",
            'with open(path, encoding="utf-8") as handle:'
        )
        modified = True

    # Enable ORANGE_LANG environment variable
    if "ORANGE_LANG" not in content:
        content = content.replace(
            '    DEFAULT_LANGUAGE = "English"',
            '    DEFAULT_LANGUAGE = os.environ.get("ORANGE_LANG", "English")',
            1  # only replace the last fallback
        )
        modified = True

    if modified:
        with open(loc_file, "w", encoding="utf-8") as f:
            f.write(content)
        print("  Patched orangecanvas localization")
    else:
        print("  orangecanvas localization already patched")


def set_language_preference():
    """Set Chinese as the default language in QSettings."""
    try:
        from AnyQt.QtWidgets import QApplication
        from AnyQt.QtCore import QSettings
        # Need QApplication for QSettings to work
        app = QApplication.instance()
        if app is None:
            app = QApplication([])
            created = True
        else:
            created = False

        s = QSettings(QSettings.IniFormat, QSettings.UserScope,
                      "biolab.si", "Orange")
        s.setValue("application/language", "中文")
        s.sync()
        print(f"  Set language to Chinese in {s.fileName()}")

        if created:
            app.quit()
    except Exception as e:
        print(f"  Could not set QSettings: {e}")


def main():
    print("Orange3 Chinese Localization Setup")
    print("=" * 40)

    print("\n1. Deploying translation files...")
    deploy_translations()

    print("\n2. Patching localization module...")
    patch_localization()

    print("\n3. Setting language preference...")
    set_language_preference()

    print("\n4. Clearing caches...")
    # Clear __pycache__
    for pkg_name in ["Orange", "orangecanvas", "orangewidget"]:
        try:
            mod = importlib.import_module(pkg_name)
            pkg_dir = os.path.dirname(mod.__file__)
            for root, dirs, files in os.walk(pkg_dir):
                for d in dirs:
                    if d == "__pycache__":
                        shutil.rmtree(os.path.join(root, d))
        except ImportError:
            pass

    # Clear widget registry cache
    cache_dir = os.path.join(os.path.expanduser("~"),
                             "AppData", "Local", "Orange", "cache")
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)
        print("  Cleared widget registry cache")

    print("\nDone! Run 'python -m Orange.canvas' to start Orange3 in Chinese.")


if __name__ == "__main__":
    main()
