from setuptools import setup, find_packages

setup(name='python-package',
      version='0.0',
      description='Example setup.py',
      url='httos://github.com/example/python-package',
      author='Dependabot',
      scripts=[],
      packages=find_packages(),
      setup_requires=[
          'numpy==1.14.5',
          'pytest-runner',
      ],
      install_requires=[
          'boto3==1.3.1',
          'flake8 >2.5.4,<4.0.0',
          'gocardless_pro',
          'pandas==0.23.1',
          'pep8==1.7.0',
          'psycopg2==2.7.5',
          'raven == 5.32.0',
          'requests==2.12.*',
          'scipy==0.18.1',
          'scikit-learn==0.19.1',
      ],
      tests_require=[
          'pytest==2.9.1',
          'responses==0.9.0',
      ],
      extras_require=dict(
          API=[
              'flask==0.12.2',
          ],
      ),
)
