from setuptools import setup

extras_require = {
    'tests': ["pytest"]
}

extras_require['all'] = []
for reqs in extras_require.values():
    extras_require['all'].extend(reqs)


setup(
    name='testapp',
    packages=['testapp'],
    include_package_data=True,
    extras_require=extras_require,
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'marshmallow',
        'click',
        'psycopg2',
        'ipdb'
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
