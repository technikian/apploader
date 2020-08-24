import apploader
# from .test_program_dep import test

if __name__ == '__main__':
	#print(test())
	test_program_dep = apploader.module_load("asdf", __file__[:-3] + "_dep.py")
	print(test_program_dep.test())
	apploader.sys_path_add(apploader.FilePathWin(("asdf", "asdf")))
	print(apploader.sys_path())
