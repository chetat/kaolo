def get_user_by_id(user_id: str):
    return {"message": f"Hello {user_id}"}


def add_user():
    return {"message": "User created"}


def logout_user():
    return {"message": "Logged Out"}


def authenticate_user(user_id: str):
    return {"message": f"Hello {user_id}"}


def update_user_info(user_id: str):
    return {"message": f"Hello {user_id}"}


def get_user_addresses(user_id: str):
    return {"message": f"Hello fetch address {user_id}"}


def update_user_address(user_id: str):
    return {"message": f"Hello update address {user_id}"}


def create_user_address(user_id: str, address_id: str):
    return {"message": f"Hello create address{user_id} {address_id}"}


def change_password(user_id: str, old_password: str, new_password: str):
    return {"message": f"Hello change password {user_id}"}


def reset_password(user_id: str, new_password: str):
    return {"message": f"Hello reset password {user_id}"}
