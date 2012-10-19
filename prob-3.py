#!/usr/bin/env python

import Infeasible

import re

def rewriter( rules, path ):
	for ( rule, endpoint ) in rules:
		if rule.match( path ):
			return endpoint
	return None



solution = Infeasible.Solution()


@solution.must_satisfy
def no_duplicate_rules_constraint( params, candidate ):
	return len( candidate ) <= params['N_rules']

@solution.must_satisfy
def correct_endpoint_constraint( params, candidate ):
	for ( path, endpoint) in params['paths']:
		ep = rewriter( candidate, path )
		if ep:
			if ep != endpoint:
				return False
	return True



@solution.is_valid
def valid_solution( params, candidate ):
	for (path, endpoint) in params['paths']:
		ep = rewriter( candidate, path )
		if ep != endpoint:
			return False
	return True

import pprint

params = {}
routes = [
				(re.compile( '/service/(.*)' ), "service"),
				(re.compile( '/service/(.*)/debug'), "debug")
				]

params['N_rules'] = len( routes )


params['paths'] = [
		('/service/1', 'service'),
		('/service/1/debug', 'debug'),
		('/service/elephants', 'service'),
		('/service/elephants/3', 'service'),
		('/service/1/debug', 'debug'),
		('/service/walruses/3/debug', 'debug')
		]


solutions = solution.get( params = params, domain = routes )

for solution in solutions:
		for (route, endpoint) in solution:
				print route.pattern
		print ""
