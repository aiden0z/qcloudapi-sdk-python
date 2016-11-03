# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

version = '2.0'

setup(
    name='qcloudapi-sdk-python',
    version=version,
    description='Python sdk for Qcloud',
    url='https://github.com/QcloudApi/qcloudapi-sdk-python',
    # packages=['qcloudapi.modules', 'qcloudapi.common'],
    packages=find_packages(),
    install_requires=['requests >= 2.5.2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License',
    ],
)
