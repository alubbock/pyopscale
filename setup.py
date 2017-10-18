from distutils.core import setup

setup(name='pyopscale',
      version='1.0',
      description='Optimal scaling in Python',
      author='Alex Lubbock, William G. Jacoby',
      author_email='code@alexlubbock.com',
      url='https://github.com/alubbock/pyopscale',
      packages=['pyopscale'],
      install_requires=['rpy2', 'jinja2'],
      package_data={'pyopscale': ['pyopscale/opscale.R']}
     )
