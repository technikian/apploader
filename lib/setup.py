from distutils.core import setup

setup(
	name='apploader',
	packages=['apploader'],
	version='0.1',
	license='MIT',
	description='a lightweight module to make importing modules with "no known parent package" less bulky',
	author='the technician',  # Type in your name
	author_email='your.email@domain.com',
	url='https://github.com/technikian/apploader',
	download_url='https://github.com/technikian/apploader/archive/v_01.tar.gz',
	keywords=['app', 'loader', 'import', 'system'],
	install_requires=[],
	classifiers=[
		'Development Status :: 3 - Alpha',
		# Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
		'Intended Audience :: Developers',  # Define that your audience are developers
		'Topic :: Software Development :: Build Tools',
		'License :: OSI Approved :: MIT License',  # Again, pick a license
		'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
	],
)
