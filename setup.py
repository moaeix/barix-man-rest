# -*- coding: utf-8 -*-
import setuptools


def read(path):
    """Read a file from `path`."""
    with open(path) as f:
        return f.read()

version = '0.1.dev0'
long_description = '\n\n'.join([
    read('README.rst'),
    read('CHANGES.rst'),
])

setuptools.setup(
    name='barix-mon-rest',
    version=version,
    description="REST API for the management of Barix devices",
    long_description=long_description,
    keywords='barix REST monitor API',
    author='Michael Howitz',
    author_email='icemac@gmx.net',
    url='https://github.com/moaeix/barix-man-rest',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Topic :: Communications',
        'Topic :: Database',
        'Topic :: System :: Logging',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Networking :: Monitoring',
        'Topic :: System :: Systems Administration',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'PyMySQL',
    ],
    extras_require=dict(
        test=[
            'gocept.testdb',
            'pytest >= 3.0',
        ]),
    entry_points="""
      """,
)
