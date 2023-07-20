def user_info(*names, **details: dict):  # *args **kwargs
    user_info = {}
    for name in names:
        user_info[name] = details
    return user_info


print(user_info("Alice", "Nino", "Kim", "Leon", "Guy", "Jules", "Benoit",          fav_color="Marine blue",
                work="Developers Institute",
                hobbie="Football",
                city="Ramat Gan"))
