import json

# Function to check control code
def check_control_code(control_code):
    lines = control_code.split('\n')
    for line in lines:
        if line:
            parts = line.split(':')
            if len(parts) != 2 or parts[0] not in ['S', 'B', 'E'] or not parts[1].isdigit():
                return False
    return True

# Function to check abc notation
def check_abc_notation(abc_notation):
    lines = abc_notation.split('\n')
    found_pipe = "|" in abc_notation

    if found_pipe:
        found_pipe_in_line = False
        found_no_pipe_after_pipe = False
        for line in lines:
            if '|' in line:
                if found_no_pipe_after_pipe:
                    return False
                found_pipe_in_line = True
            else:
                if found_pipe_in_line:
                    found_no_pipe_after_pipe = True
    else:
        return lines[0][1] == ':' and lines[0][0].isalpha()

    return True

# Check the control code and abc notation in the output.jsonl file
with open('output.jsonl', 'r') as file:
    for line in file:
        json_obj = json.loads(line)
        if not check_control_code(json_obj['control code']):
            print(f'Invalid control code in object: {json_obj}')
        if not check_abc_notation(json_obj['abc notation']):
            print(f'Invalid abc notation in object: {json_obj}')