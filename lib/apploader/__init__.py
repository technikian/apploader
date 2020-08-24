# import importlib.machinery
# import sys
#
# # For illustrative purposes only.
# SpamMetaPathFinder = importlib.machinery.PathFinder
# SpamPathEntryFinder = importlib.machinery.FileFinder
# loader_details = (importlib.machinery.SourceFileLoader,
#                   importlib.machinery.SOURCE_SUFFIXES)
#
# # Setting up a meta path finder.
# # Make sure to put the finder in the proper location in the list in terms of
# # priority.
# sys.meta_path.append(SpamMetaPathFinder)
#
# # Setting up a path entry finder.
# # Make sure to put the path hook in the proper location in the list in terms
# # of priority.
# sys.path_hooks.append(SpamPathEntryFinder.path_hook(loader_details))
from ._type_ import FilePath as FilePath, FilePathWin


def module_load(name, __file__):
	from importlib.util import spec_from_file_location, module_from_spec
	spec = spec_from_file_location(name, __file__)
	module = module_from_spec(spec)
	spec.loader.exec_module(module)
	return module


def dir_includes(path: FilePath, names: set):
	from os import listdir
	from os.path import isfile
	path = str(path)
	if isfile(path):
		return False
	files_and_dirs = set(listdir(path))
	if len(files_and_dirs.intersection(names)) != len(names):
		return False
	return True


def dir_excludes(path: FilePath, names: set):
	from os import listdir
	from os.path import isfile
	path = str(path)
	if isfile(path):
		return False
	files_and_dirs = set(listdir(path))
	if len(files_and_dirs.intersection(names)) != 0:
		return False
	return True


def dir_conforms(path: FilePath, includes: set, excludes: set):
	from os import listdir
	from os.path import isfile
	path = str(path)
	if isfile(path):
		return False
	files_and_dirs = set(listdir(path))
	if len(files_and_dirs.intersection(includes)) != len(includes):
		return False
	if len(files_and_dirs.intersection(excludes)) != 0:
		return False
	return True


def dir_supers(path: FilePath, names: set):
	empty_set = set()
	found = {}
	if not isinstance(names, set):
		names = set(names)
	while len(names) and len(path):
		for name in names:
			if dir_conforms(path, {name}, empty_set):
				found[name] = path.join(name)
		names.difference_update(found)
		path = path[:-1]
	return found


def sys_args():
	from sys import argv
	return argv[1:]


def sys_path():
	from sys import path
	return path


def sys_path_add(*paths: FilePath):
	from sys import path as sys_path_
	new_paths = set(str(p) for p in paths).difference(sys_path_)
	sys_path_.extend(new_paths)
	return


def sys_path_sub():
	raise NotImplementedError
