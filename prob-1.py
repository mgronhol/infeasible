#!/usr/bin/env python

import Infeasible



solution = Infeasible.Solution()


@solution.must_satisfy
def sum_constraint( params, candidate ):
	S = sum( candidate )
	if S > 10:
		return False
	return True

@solution.must_satisfy
def begin_constraint( params, candidate ):
	if len( candidate ) > 2:
		if candidate[:2] != [1,2]:
			return False
	return True


@solution.is_valid
def valid_solution( params, candidate ):
	S = sum( candidate )
	return S == 10


import pprint


pprint.pprint( solution.get( domain = [1,2,3,4,5,10,11] ) )


