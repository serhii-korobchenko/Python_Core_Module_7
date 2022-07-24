from setuptools import setup, find_namespace_packages

setup(
    name='cleanfolderkorobchenko',
    version='0.0.1',
    description='Arrange your folder',
    url='https://github.com/serhii-korobchenko/Python_Core_Module_7/tree/main/Home_Works/clean_folder',
    author='Serhii Korobchenko and GoIT',
    author_email='flyingcircus@example.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder=clean_folder.clean:start']}
)
# Packaging Python Projects