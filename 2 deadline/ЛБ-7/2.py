def build_user_profile(user_id: int, **kwargs) -> dict:
    """
    Создает профиль пользователя на основе user_id и дополнительной информации.
    
    Parameters:
    user_id (int): уникальный идентификатор пользователя
    **kwargs: произвольные именованные аргументы с дополнительной информацией
    
    Returns:
    dict: словарь с профилем пользователя
    """
    profile = {'user_id': user_id}
    profile.update(kwargs)
    return profile

profile = build_user_profile(101, name="Анна", status="online", email="anna@example.com")
print(profile)