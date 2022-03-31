from setuptools import setup, find_packages

print(find_packages('src'))

setup(
    name='hypeapi',
    version='0.0.2.1',
    license='.-.',
    author='Neruxov',
    author_email='k.neruxov@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Neruxov/HypeAPI',
    keywords='example project',
    install_requires=[
          'requests'
    ],
)