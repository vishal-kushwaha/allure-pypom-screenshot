''' setup for allure_pypom_screenshot plugin '''
from setuptools import setup

setup(name='PyPOM-screenshot',
      description='plugin for PyPOM that takes a lot of screenshots and attach to allure reports',
      long_description=open('README.rst').read(),
      author='Vishal Kushwaha',
      author_email='vishal.02jan@gmail.com',
      url='https://github.com/vishal-kushwaha/allure-pypom-screenshot.git',
      packages=['allure_pypom_screenshot'],
      install_requires=['PyPOM', 'allure-pytest'],
      entry_points={'pypom.plugin': ['screenshot = allure_pypom_screenshot.plugin']},
      license='Mozilla Public License 2.0 (MPL 2.0)',
      keywords='pypom page object model selenium screenshots allure attachment',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
          'Operating System :: POSIX',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: MacOS :: MacOS X',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Software Development :: Testing',
          'Topic :: Utilities',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.7'])
