from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)

    job_types = set()

    for job in jobs:
        kind = job["job_type"]
        job_types.add(kind)

    return job_types


def filter_by_job_type(jobs, job_type):
    filter_job = list()

    for x in jobs:
        if x["job_type"] == job_type:
            filter_job.append(x)

    return filter_job


def get_unique_industries(path):
    jobs = read(path)

    industries = set()

    for industry in jobs:
        if industry["industry"] != "":
            industries.add(industry["industry"])

    return industries


def filter_by_industry(jobs, industry):
    filter_industry = list()

    for x in jobs:
        if x["industry"] == industry:
            filter_industry.append(x)

    return filter_industry


def get_max_salary(path):
    jobs = read(path)

    salary = []
    for item in jobs:
        if item["max_salary"].isnumeric():
            salary.append(int(item["max_salary"]))
  
    return max(salary)


def get_min_salary(path):
    jobs = read(path)

    salary = []
    for item in jobs:
        if item["min_salary"].isnumeric():
            salary.append(int(item["min_salary"]))
  
    return min(salary)


def matches_salary_range(job, salary):
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError
    elif (
        type(salary) != int
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
    ):
        raise ValueError
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError
    elif job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    list_of_salary_ranges = list()

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_of_salary_ranges.append(job)
        except ValueError:
            pass
    return list_of_salary_ranges
