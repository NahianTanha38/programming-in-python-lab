resources = [
[101, "Laptop", "Electronics", 8],
[102, "Projector", "Electronics", 0],
[103, "Whiteboard", "Classroom", 5],
[104, "Microphone", "Audio", 3],
[105, "Camera", "Electronics", 2]
 ]

# Display all resources 
def display_resources(resources):
        for resource in resources:
           print(resource)
           
display_resources(resources)

#Search resources by category

def search_by_category(resources, category):
    for resource in resources:
        if resource[2] == category:
            print(resource)

search_by_category(resources, "Electronics")

# Identify resources whose available quantity is 0

def find_unavailable(resources):
    for resource in resources:
        if resource[3] == 0:
            print(resource)

find_unavailable(resources)







