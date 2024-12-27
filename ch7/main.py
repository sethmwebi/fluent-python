# def factorial(n):
#     """returns n!"""
#     return 1 if n < 2 else n * factorial(n - 1)
#
#
# # print(factorial.__doc__)
# # print(help(factorial))
# print(dir(factorial))
# import bobo
#
#
# @bobo.query("/")
# def hello(person):
#     return f"Hello {person}!"
# f = open("data.txt", "r")
# for i, line in enumerate(f):
#     if line.strip() == "":
#         print("Blank line at line #%i" % i)
# import itertools
#
# # Define the city list
# city_list = [
#     ("Decatur", "AL"),
#     ("Huntersville", "AL"),
#     ("Selma", "AL"),
#     ("Anchorage", "AK"),
#     ("Nome", "AK"),
#     ("Flagstaff", "AZ"),
#     ("Phoenix", "AZ"),
#     ("Tucson", "AZ"),
# ]
#
#
# def get_state(city_state):
#     return city_state[1]
#
#
# # Sort the city list by state to ensure groupby works correctly
# city_list.sort(key=get_state)
#
# # use itertools.groupby to group cities by state
# grouped = itertools.groupby(city_list, get_state)
#
# # Convert to list of tuples for display
# grouped_list = [(state, list(group)) for state, group in grouped]
#
# for state, cities in grouped_list:
#     print(f"({state}, {cities})")
import functools


def log(message, subsytem):
    """Write the contents of 'message' to the specified subsytem."""
    print(f"{subsytem}: {message}")


# Create a logger for the 'server' subsytem using functools.partial
server_log = functools.partial(log, subsytem="server")
server_log("Unable to open socket")
db_log = functools.partial(log, subsytem="database")
db_log("Connection failed")
