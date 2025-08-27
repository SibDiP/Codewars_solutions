"""Human Readable Time | f-string oneliner | digit formatting {num:dd}

Instructions:
Write a function, which takes a non-negative integer (seconds) as
input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

DATE TIME MATHEMATICS ALGORITHMS
"""

# 1. f-string oneliner

def make_readable(seconds):
    return f"""{str(seconds // 3600).zfill(2)}:{str((seconds % 3600 - seconds
        % 60) // 60).zfill(2)}:{str(seconds % 60).zfill(2)}"""


# 2. Better f-string oneliner with digit formatting {nuber:dd}

def make_readable(seconds):
    return f"{seconds // 3600:02}:{seconds % 3600 // 60:02}:{seconds % 60:02}"

# 3. dict, direct calculations, f-string
def make_readable(seconds):
    time_dict = {'H': '00', 'M': '00', 'S': '00'}
    time = seconds

    hours = time // 3600
    min = (time - hours*3600) // 60
    sec = (time - hours*3600 - min*60)

    return(f"{hours:02}:{min:02}:{sec:02}")

# 4. divmod(), constant, list, for-loop, ":".join()
def make_readable(seconds: int) -> str:
    HMS = (('hour', 3600),
           ('minutes', 60),
           ('seconds', 1))
    parts = []
    reminder = seconds

    for _, measure_value in HMS:
        result, reminder = divmod(reminder, measure_value)
        parts.append(f'{result:02}')

    return ":".join(parts)
