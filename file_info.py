def file_info (root_folder, file_path):
    file_path = str(file_path)
    relative = file_path[file_path.index(root_folder) + len(root_folder) + 1:]
    # for windows os
    relative = relative.replace("\\", "/")
    relative_parts = relative.split("/")
    country = relative_parts[0]
    website = relative_parts[1]
    vamid = relative_parts[2]
    return country,website, vamid