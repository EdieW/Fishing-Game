from model.user import User, UserInventory, UserProgress

import configparser


# 获取配置文件信息
config = configparser.ConfigParser()
config.read('./config/config.ini')
expiry_time = config.getint('CacheSettings', 'ExpiryTime', fallback=3600)

async def get_user_information(user_id):

    basic = {'user_name': 'mock_user', 'rod_type': 'mock_rod'}
    finance = {'coins': 1000, 'diamonds': 50}
    level = {'level': 5, 'current_experience': 150, 'experience_for_next_level': 500}
    inventory = {'fish_inventory': ['fish1', 'fish2', 'fish3']}

    # 创建User对象，模拟真实函数返回
    user = User(user_id, basic.get('user_name'), finance.get('coins'), finance.get('diamonds'),
                inventory.get('fish_inventory'), basic.get('rod_type'), level.get('level'),
                level.get('current_experience'), level.get('experience_for_next_level'))
    return user
