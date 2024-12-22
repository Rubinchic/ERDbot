# Словник для збереження даних користувачів
user_data = {}

def set_user_step(user_id, step):
    if user_id not in user_data:
        user_data[user_id] = {}
    user_data[user_id]['step'] = step

def get_user_step(user_id):
    return user_data.get(user_id, {}).get('step')

def clear_user_data(user_id):
    if user_id in user_data:
        del user_data[user_id]
