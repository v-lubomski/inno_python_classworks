# Задание 1 Создать класс для приложения по трекингу времени.
# Класс содержит продолжительность времязатраты, текстовый комметарий
# и набор текстовых тегов.
# Теги обязательно состоят из маленьких латинских букв
# без иных символов и длиной не более 20.

from datetime import datetime
from typing import Any
from string import ascii_lowercase


class TrackYourTime:
    time = None
    tag = None
    comment = None

    def __init__(self: Any, time: datetime, tag: str, comment: str) -> None:
        def check_tag(word):
            for ch in word:
                if ch not in ascii_lowercase:
                    raise Exception('Тег должен состоять'
                                    'из маленьких латинских букв')
                else:
                    if len(word) > 20:
                        raise Exception('Длинна тега должна быть'
                                        'не более 20 символов')
                    return word

        self.time = time
        self.tag = check_tag(tag)
        self.comment = comment


tracked_time = TrackYourTime(datetime.now(), 'develop', 'First exercise')
tracked_time2 = TrackYourTime(datetime.now(), 'evelop', 'First exercise')


