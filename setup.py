from setuptools import setup, find_packages

setup(
    name='hypeapi',
    version='0.0.2.3',
    license='.-.',
    author='Neruxov',
    author_email='k.neruxov@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Neruxov/HypeAPI',
    keywords='hypixel hypixel_api hypixel_api_python',
    install_requires=[
          'requests'
    ],
    python_requires='>=3.7',
)