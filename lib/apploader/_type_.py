
def partition(iterable, seps):
	"""generic: partitions an iterable into multiple iterables, separated by the sep[arator]"""
	r = []
	start = 0
	for limit, item in enumerate(iterable):
		if item in seps:
			a = iterable[start:limit]
			b = iterable[limit:limit + 1]  # b can't be set to sep because then it wont be wrapped in the source iterable type
			r.extend((a, b)) if a else r.append(b)
			start = limit + 1
	r.append(iterable[start:])
	return r


def remove(iterable, items):
	return (v for v in iterable if v not in items)


class FilePath:
	# works best being immutable

	def partition(self, txt):
		return remove(partition(txt, self.seps), self.seps)

	@classmethod
	def from_file(cls, __file__):
		from os.path import realpath
		return cls.from_str(realpath(__file__))

	@classmethod
	def from_str(cls, txt, seps=('/', '\\')):
		return cls(tuple(remove(partition(txt, seps), {'/', '\\'})), seps)

	def __init__(self, values=(), seps=('/', ), prefix='/'):
		"""immutable"""
		self.values = tuple(values)
		self.seps = seps  # preferred separator goes at index 0
		self.prefix = prefix

	def __repr__(self):
		return "".join((self.__class__.__name__, '(', self.values.__repr__(), ')'))

	def __str__(self):
		return self.prefix + self.seps[0].join(self.values)

	def __len__(self):
		return self.values.__len__()

	def __iter__(self):
		return self.values.__iter__()

	def __reversed__(self):
		return self.values.__reversed__()

	def __getitem__(self, item):
		if isinstance(item, slice):
			return type(self)(self.values[item], self.seps)
		return self.values[item]

	def join(self, *names):
		from copy import deepcopy
		new_self = deepcopy(self)
		for name in names:
			new_self.values += tuple(new_self.partition(name))
		return new_self


class FilePathWin(FilePath):
	def __init__(self, values=(), seps=('\\', '/', ), prefix=''):
		super().__init__(values, seps, prefix)
