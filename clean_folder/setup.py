from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='1.0',
      description='folder clean, folder goooood.',
      url='url',
      author='Dawid',
      author_email='dziekan.dawid@wp.pl',
      license='license',
      packages= find_namespace_packages(),
      entry_points={'console_scripts': ['clean_folder = clean_folder.clean:main']},
    )