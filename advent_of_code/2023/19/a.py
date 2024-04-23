import itertools
import re


def create_condition(condition_str):
    if ':' in condition_str:
        (condition, result) = condition_str.split(':')

        lt = '<' in condition
        gt = '>' in condition
        var = condition[0]
        val = int(condition[2:])

        def c(x):
            if (lt and x[var] < val) or (gt and x[var] > val):
                return result
            else:
                return None

        return c

    else:
        return lambda x: condition_str


WORKFLOW_RE = r'([a-z]+)\{(.*)\}'


class Workflow:
    def __init__(self, workflow_line):
        matches = re.findall(WORKFLOW_RE, workflow_line)

        self.label = matches[0][0]

        self.conditions = []
        condition_strs = matches[0][1].split(',')
        for condition_str in condition_strs:
            self.conditions.append(create_condition(condition_str))

    def execute(self, part):
        # NOTE: returns either the next label, true, or false
        for condition in self.conditions:
            result = condition(part)
            if result is not None:
                return result

        print("No condition met for", self.label, part)
        return 'R'


def parse_part(part_line):
    ret = {}
    eqs = part_line.strip()[1:-1]
    for eq in eqs.split(','):
        (var, val) = eq.split('=')
        ret[var] = int(val)
    return ret


with open("input.txt") as file:
    lines = file.readlines()

(workflow_lines, part_lines) = [list(g) for k, g in itertools.groupby(
    lines, lambda x: x == '\n') if not k]

# construct workflow machine
label_to_workflow = {}
for line in workflow_lines:
    workflow = Workflow(line)
    label_to_workflow[workflow.label] = workflow

# generate parts
parts = [parse_part(part_line) for part_line in part_lines]

# run machine
total = 0
for part in parts:
    label = 'in'
    while label != 'R' and label != 'A':
        workflow = label_to_workflow[label]
        result = workflow.execute(part)
        if result == 'A':
            total += sum(part.values())
            break
        elif result == 'R':
            break
        else:
            label = result
            continue


print(total)
