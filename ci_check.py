import time
import sys

is_success = open("ci_result.txt").readline() == "success"
sleep_time_seconds = int(open("ci_sleep.txt").readline())

time.sleep(sleep_time_seconds)

if not is_success:
    sys.exit(1)
