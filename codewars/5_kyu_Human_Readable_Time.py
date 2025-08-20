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

# f-string oneliner

def make_readable(seconds):
    return f"""{str(seconds // 3600).zfill(2)}:{str((seconds % 3600 - seconds
        % 60) // 60).zfill(2)}:{str(seconds % 60).zfill(2)}"""


# Better f-string oneliner with digit formatting {nuber:dd}

def make_readable(seconds):
    return f"{seconds // 3600:02}:{seconds % 3600 // 60:02}:{seconds % 60:02}"
