from collections import deque

jobs = [int(i) for i in input().split(", ")]
interesting_job_index = int(input())
total_cycles = 0
interesting_job = jobs[interesting_job_index]
ordered_jobs = deque(sorted(jobs))

counter = 0
for job_index in range(interesting_job_index + 1):
    if jobs[job_index] == interesting_job:
        counter += 1

while counter:
    if not ordered_jobs[0] == interesting_job:
        total_cycles += int(ordered_jobs.popleft())
    else:
        total_cycles += int(ordered_jobs.popleft())
        counter -= 1

print(total_cycles)
