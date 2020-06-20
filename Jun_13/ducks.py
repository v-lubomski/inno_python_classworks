from sqlalchemy import Column, Integer, String,\
    create_engine, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///ducks.db')
Base = declarative_base()


class Players(Base):
    __tablename__ = 'players'

    identifier = Column(Integer, primary_key=True, nullable=False,
                        comment='Уникальный идентификатор игрока')
    nickname = Column(String(25), nullable=False,
                      unique=True, comment="Никнейм игрока")
    character_class = Column(String, nullable=False, comment="класс персонажа")
    character_passive_ability = Column(String, nullable=False,
                                       comment="пассивная абилка персонажа")


class Items(Base):
    __tablename__ = 'items'

    identifier = Column(Integer, primary_key=True, nullable=False,
                        comment='Уникальный идентификатор предмета')
    item_name = Column(String(25), nullable=False, unique=True)
    item_type = Column(String(25), nullable=False)


class BackPack(Base):
    __tablename__ = 'backpack'

    identifier = Column(Integer, primary_key=True, nullable=False)
    player_id = Column(Integer, ForeignKey("players.identifier"),
                       nullable=False)
    item_id = Column(Integer, ForeignKey("items.identifier"), nullable=False)
    amount = Column(Integer, nullable=False)
    equipped = Column(Boolean, nullable=False, default=False)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_player = Players(nickname="YourDuckky",
                     character_class="Giant Yellow Duck",
                     character_passive_ability="swimming")

new_item = Items(item_name='Мозговой имплант',
                 item_type='Киберпанк')

backpack_connection = BackPack(player_id=1, item_id=1, amount=2, equipped=True)

session.add_all((new_item, new_player, backpack_connection))
session.commit()
