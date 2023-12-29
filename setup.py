import re
import ast
from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('pytestifyx/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pytestifyx',
    version=version,
    url='https://github.com/jaylu2018/PyTestifyx',
    license='Apache License 2.0',
    author='luyh',
    author_email='jaylu1995@outlook.com',
    description='pytestifyx is a pytest-based automation testing framework for api, ui, app testing',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    package_data={
        'pytestifyx': ['/*.pytestifyx'],
    },
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pytest>=7.2.1',
        'playwright>=1.30.0',
        'pytest-playwright>=0.3.0',
        'pytest_cases>=3.6.13',
        'loguru>=0.6.0',
        'prettytable>=3.6.0',
        'deepdiff>=6.3.0',
        'requests==2.29.0',
        'requests_toolbelt==1.0.0',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': [
            'pytestifyx = pytestifyx.cli:main',
        ],
        "pytest11": [
            'pytestifyx = pytestifyx',
            'pytest_chinese_fix = pytestifyx.chinese_fix',
        ],
    },
    extras_require={
    },
)
