#!/usr/bin/env python




class Room(object):
	"""docstring for Room: The class creates room objects for
	fellows and staff of Andela at The Dojo"""
	def __init__(self,purpose, name):
		self.name = name
		self.purpose = purpose
		self.occupants = []
	def __repr__(self):
		return 'Room {}'.format(self.name)

if '__name__' == '__main__':
    unittest.main()


