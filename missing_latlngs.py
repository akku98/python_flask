# from geopy.distance import geodesic



# --------------------------geodesic (will give straight line path) --------------------

# def generate_points(start_point, end_point, num_points):
#     """
#     Generate latitude and longitude points between two given points using linear interpolation.

#     Parameters:
#     - start_point: Tuple (latitude, longitude) for the starting point.
#     - end_point: Tuple (latitude, longitude) for the ending point.
#     - num_points: Number of points to generate between the start and end points.

#     Returns:
#     - List of tuples representing generated latitude and longitude points.
#     """
#     lats = [start_point[0] + (end_point[0] - start_point[0]) * i / (num_points - 1) for i in range(num_points)]
#     lons = [start_point[1] + (end_point[1] - start_point[1]) * i / (num_points - 1) for i in range(num_points)]

#     return list(zip(lats, lons))

# # Example usage
# start_point = (37.7749, -122.4194)  # San Francisco, CA
# end_point = (34.0522, -118.2437)    # Los Angeles, CA
# num_points = 15

# generated_points = generate_points(start_point, end_point, num_points)

# # Display the generated points
# for point in generated_points:
#     print(point)


def generate_points(start_point, end_point, num_points):
    """
    Generate latitude and longitude points between two given points using linear interpolation.

    Parameters:
    - start_point: Tuple (latitude, longitude) for the starting point.
    - end_point: Tuple (latitude, longitude) for the ending point.
    - num_points: Number of points to generate between the start and end points.

    Returns:
    - List of tuples representing generated latitude and longitude points.
    """
    lats = [start_point[0] + (end_point[0] - start_point[0]) * i / (num_points - 1) for i in range(num_points)]
    lons = [start_point[1] + (end_point[1] - start_point[1]) * i / (num_points - 1) for i in range(num_points)]

    return list(zip(lats, lons))

# Example usage
start_point = (14.436801,75.89327)  # San Francisco, CA
end_point = (14.434147, 75.895256)    # Los Angeles, CA
num_points = 5

generated_points = generate_points(start_point, end_point, num_points)

# Display the generated points
for point in generated_points:
    print(point)



