# encoding: UTF-8
"""

"""
import platform
from distutils.core import setup, Extension
from os.path import join

headers = ['MdApi.h', 'TdApi.h']
sources = ['MdApi.cpp', 'TdApi.cpp']

sources = [join('.', file_path) for file_path in sources]
depends = [join('.', file_path) for file_path in headers]

optional = {}
if platform.system() == 'Linux':
    optional['extra_compile_args'] = ['-std=c++11']
    optional['runtime_library_dirs'] = ['./']
    optional['include_dirs'] = ['./api/linux64']
    optional['library_dirs'] = ['./api/linux64', '/usr/lib/x86_64-linux-gnu']
if platform.system() == 'Windows':
    optional['include_dirs'] = ['./api/win32']
    optional['library_dirs'] = ['./api/win32']
    if '64 bit' in platform.python_compiler():
        optional['include_dirs'] = ['./api/win64']
        optional['library_dirs'] = ['./api/win64']
argments = dict(name='heron_api',
                sources=sources,
                language='c++',
                libraries=['thostmduserapi', 'thosttraderapi'],
                depends=depends)
argments.update(optional)

setup(name='heron_api',
      version='0.0.1',
      description='CTP for Python',
      long_description='CTP v6.3.6_20160606 for Python',
      author='MeiQuant',
      author_email='xiuguozhao@gmail.com',
      url='https://github.com/MeiQuant/heron-api',
      keywords=['ctp','futures','stock'],
      license='LGPL-3.0',
      platforms=['linux-x86_64','win32','win-amd64'],
      ext_modules=[Extension(**argments)]
      )