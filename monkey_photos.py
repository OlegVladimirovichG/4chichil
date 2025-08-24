# Коллекция фото обезьян, показывающих фак
MONKEY_PHOTOS = [
    "https://www.meme-arsenal.com/memes/cd5fe9d8a01d0398f7712266a604ba90.jpg",  # Горилла с факом (единственное фото)
]

# Локальные пути к фото (если будем хранить локально)
LOCAL_PHOTOS = [
    "photos/monkey1.jpg",
]

def get_random_monkey_photo():
    """Возвращает случайное фото обезьяны"""
    import random
    return random.choice(MONKEY_PHOTOS)
