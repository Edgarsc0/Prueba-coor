# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

setup(
    name="Nombre ejecutable",
    version="1.0",
    description="Breve descripcion",
    author="autor",
    author_email="email del autor",
    url="url del proyecto",
    license="tipo de licencia",
    scripts=["pandas_sql_matplotlib.py"],
    console=["pandas_sql_matplotlib.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)