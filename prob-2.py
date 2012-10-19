#!/usr/bin/env python

import Infeasible



solution = Infeasible.Solution()


@solution.must_satisfy
def no_loops_constraint( params, candidate ):
	return len( candidate ) == len( set( candidate ) )


@solution.is_valid
def valid_solution( params, candidate ):
	if len( candidate ) > 0:
		if candidate[-1] == params['target']:
			return True
	return False


@solution.first_candidates
def get_root( params, domain ):
	yield [params['start']]

@solution.next_candidates
def travel_graph( params, domain, current ):
	links = domain[current[-1]]
	return (current + [l] for l in links )




graph = {}

def add( g, a, b ):
	if a not in g:
		g[a] = []
	if b not in g:
		g[b] = []
	g[a].append( b )


add( graph, 'A', 'B' )
add( graph, 'A', 'C' )
add( graph, 'D', 'B' )
add( graph, 'B', 'E' )
add( graph, 'C', 'E' )
add( graph, 'E', 'F' )
add( graph, 'E', 'G' )
add( graph, 'E', 'A' )


print "Paths A -> G:", solution.get( params = {'start': 'A', 'target': 'G'}, domain = graph )
print ""
print "Paths D -> G:", solution.get( params = {'start': 'D', 'target': 'G'}, domain = graph )

