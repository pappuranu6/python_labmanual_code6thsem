import pkg_resources
for p in pkg_resources.working_set:
    print(p.project_name)
