from setuptools import setup, find_packages

setup(
    name='hypeapi',
    version='0.1.0',
    license='MIT',
    author='Neruxov',
    author_email='k.neruxov@gmail.com',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Neruxov/HypeAPI',
    keywords='hypixel hypixel_api hypixel_api_python',
    install_requires=[
          'requests'
    ],
    python_requires='>=3.7',
)
