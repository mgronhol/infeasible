#!/usr/bin/env python

import collections


class CandidateStore( object ):
	def __init__( self ):
		self.iters = collections.deque()
	
	def add( self, iter ):
		self.iters.append( iter )
	
	def empty( self ):
		return (not self.current) and ( len(self.iters) == 0 )

	def next( self ):
		while len( self.iters ) > 0:
			iter = self.iters.popleft()
			for entry in iter:
				yield entry
	def __iter__( self ):
		return (x for x in self.next() )


class Solution( object ):
	def __init__( self, params = {}, domain = [] ):
		self.domain = domain
		self.params = {}

		self._constraints = []
		self._is_valid  = None
		self._first = lambda p, d: ([v] for v in d)
		self._next = lambda p,d,c: (c + [v] for v in d)
		self.out = []
	
	def must_satisfy( self, rule ):
		self._constraints.append( rule )
		return rule
	
	def is_valid( self, rule ):
		self._is_valid = rule
		return rule

	def first_candidates( self, first ):
		self._first = first
		return first
	
	def next_candidates( self, next ):
		self._next = next
		return next
	
	def add_constraint( self, rule ):
		self._constraints.append( rule )
	
	def accept( self, c ):
		return self._is_valid( self.params, c )
	
	def reject( self, c ):
		return any( not F( self.params, c ) for F in self._constraints )
	
	def first( self ):
		return self._first( self.params, self.domain )
	
	def next( self, c ):
		return self._next( self.params, self.domain, c )
	
	def bt( self, c ):
		if self.reject( c ):
			return False
		if self.accept( c ):
			self.out.append( c )
			return True
		
		for s in self.next( c ):
			self.bt( s )
	
	def bt2( self, start ):
		#Q = collections.deque()
		#Q.append( start )
		Q = CandidateStore()
		Q.add( [start] )
		#while len( Q ) > 0:
		#	c = Q.popleft()
		#	if self.reject( c ):
		#		continue
		#	if self.accept( c ):
		#		self.out.append( c )
		#		continue
		#	for s in self.next( c ):
		#		Q.append( s )
		for c in Q:
			if self.reject( c ):
				continue
			if self.accept( c ):
				self.out.append( c )
				continue
			Q.add( self.next( c ) )

	def get( self, domain = None, params = None ):
		if domain:
			self.domain = domain
		if params:
			self.params = params

		self.out = []
		for c in self.first():
			self.bt2( c )
		return self.out

