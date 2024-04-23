import itertools
import re

from collections import defaultdict, deque

# (bfs) trace all paths from 'A' back to 'in'
# for each path, keep track of all conditions (i.e. ranges for vars)
# take the sum of products of possibilities for each set of constraints at the end


WORKFLOW_RE = r'([a-z]+)\{(.*)\}'

CS_MAX = 4000
CS_MIN = 1


class Constraint:
    def __init__(self, var, op, val):
        self.var = var
        self.op = op
        self.val = val

    def from_str(constraint_str):
        return Constraint(constraint_str[0], constraint_str[1], int(constraint_str[2:]))

    def invert(self):
        match self.op:
            case '>':
                new_op = '<='
            case '<':
                new_op = '>='
            case '>=':
                new_op = '<'
            case '<=':
                new_op = '>'

            case _:
                print("Invalid op", self.op)
                exit(1)

        return Constraint(self.var, new_op, self.val)

    def to_range(self):
        match self.op:
            case '>':
                return (self.val + 1, CS_MAX + 1)
            case '<':
                return (CS_MIN, self.val)
            case '>=':
                return (self.val, CS_MAX + 1)
            case '<=':
                return (CS_MIN, self.val + 1)

            case _:
                print("Invalid op", self.op)
                exit(1)

    def __repr__(self):
        return f"{self.var}{self.op}{self.val}"


class RangeConstraintSet:

    def __init__(self, val_to_range):
        self.val_to_range = val_to_range

    def from_constraints(constraints):
        var_to_range = {}
        for constraint in constraints:
            if constraint.var in var_to_range:
                print("duplicate range for var on single edge!")
                exit(1)

            var_to_range[constraint.var] = constraint.to_range()

        return RangeConstraintSet(var_to_range)

    def consolidate(rcs1, rcs2):
        var_to_range = {}

        all_vars = set(rcs1.val_to_range.keys()) | set(
            rcs2.val_to_range.keys())

        for var in all_vars:
            if var in rcs1.val_to_range and var in rcs2.val_to_range:
                range1 = rcs1.val_to_range[var]
                range2 = rcs2.val_to_range[var]

                # check consistency of range, return none if inconsistent
                new_min = max(range1[0], range2[0])
                new_max = min(range1[1], range2[1])
                if new_min > new_max:
                    return None

                var_to_range[var] = (new_min, new_max)

            elif var in rcs1.val_to_range:
                var_to_range[var] = rcs1.val_to_range[var]

            else:
                var_to_range[var] = rcs2.val_to_range[var]

        return RangeConstraintSet(var_to_range)

    def __str__(self):
        return str(self.val_to_range)


def get_edges(workflow_line):
    matches = re.findall(WORKFLOW_RE, workflow_line)

    src = matches[0][0]
    condition_strs = matches[0][1].split(',')

    edges = []
    prev_constraints = []
    for condition_str in condition_strs:
        if ':' in condition_str:
            (cons, dst) = condition_str.split(':')
            constraint = Constraint.from_str(cons)

            edge_constraint_set = RangeConstraintSet.from_constraints(
                prev_constraints + [constraint])
            edges.append((dst, edge_constraint_set))

            prev_constraints.append(constraint.invert())

        else:
            edge_constraint_set = RangeConstraintSet.from_constraints(
                prev_constraints)
            edges.append((condition_str, edge_constraint_set))

    return (src, edges)


# 1. construct graph
with open("testinput.txt") as file:
    lines = file.readlines()

(workflow_lines, _) = [list(g) for k, g in itertools.groupby(
    lines, lambda x: x == '\n') if not k]

label_to_edges = defaultdict(list)  # label -> [(label, constraints)]
for line in workflow_lines:
    (src, to_add) = get_edges(line)
    label_to_edges[src].extend(to_add)

# 2. run bfs on graph to get all lists of constraints

constraint_sets = []

# [(label, constraints)]
to_visit = deque([('in', RangeConstraintSet.from_constraints([]), set())])
while to_visit:
    (label, constraints, visited) = to_visit.popleft()

    # NOTE: if no loops, we can ignore this
    if label in visited:
        print("found loop!", label)
        break
    visited.add(label)

    # if label == 'A', add constraints to list and continue
    if label == 'A':
        constraint_sets.append(constraints)
        continue
    elif label == 'R':
        continue

    edges = label_to_edges[label]
    for (dst, new_constraints) in edges:
        consolidated = RangeConstraintSet.consolidate(
            constraints, new_constraints)

        if consolidated is not None:
            to_visit.append((dst, consolidated, visited | {label}))


# 3. take sum of possibilities
def get_possibilities(rcs):
    if rcs.val_to_range == {}:
        print("empty rcs!", rcs)
        return 0

    total = 1
    for (min_val, max_val) in rcs.val_to_range.values():
        total *= max_val - min_val

    return total


print(sum([get_possibilities(cs) for cs in constraint_sets]))
