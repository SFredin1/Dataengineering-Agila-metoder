import pkg_resources
import platform

# Get the Python version
python_version = platform.python_version()
print(f"Python version: {python_version}\n")

# Get the list of installed packages
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])

print("Installed packages:")
for package in installed_packages_list:
    print(package)
