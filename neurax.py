#!/usr/bin/env python3
"""Backwards-compatible entry point — the real package lives in neurax/.

Keep this module import-light: build tools may resolve the name
``neurax`` against THIS file before the neurax/ package.
"""
if __name__ == "__main__":
    from neurax.cli import main

    raise SystemExit(main())
