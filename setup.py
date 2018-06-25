from setuptools import setup, find_packages

setup(name='python-package',
      version='6.g564',
      description='Example setup.py',
      url='https://github.com/example/python-package',
      author='double-beep',
      scripts=[],
      packages=find_packages(),
      setup_requires=[
          'numpy==1.14.5',
          'pytest-runner',
      ],
      install_requires=[
          'boto3==1.7.45',
          'flake8 >2.5.4,<4.0.0',
          'gocardless_pro',
          'pandas==0.23.1',
          'pep8==1.7.1',
          'psycopg2==2.7.5',
          'raven ==6.9.0',
          'requests>=2.12,<2.20',
          'scipy==1.1.0',
          'scikit-learn==0.19.1',
      ],
      tests_require=[
          'pytest==3.6.2',
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

          'responses==0.9.0',
      ],
      extras_require=dict(
          API=[
          ],
      ),
)
