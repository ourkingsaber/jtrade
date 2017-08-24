import datetime
from sqlalchemy import Column, String, Float, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base

import Data.Fetch.Query

Base = declarative_base()


class EquityQuote(Base):
    __tablename__ = 'EquityQuote'

    symbol = Column(String(collation='utf8'), primary_key=True)
    time = Column(DateTime(), primary_key=True)
    price = Column(Float())
    change = Column(Float())
    pct_change = Column(Float())
    volume = Column(Float())
    avg_volume = Column(Float())
    name = Column(String(collation='utf8'))
    exchange = Column(String(collation='utf8'))
    market_cap = Column(Float())
    day_high = Column(Float())
    day_low = Column(Float())
    year_high = Column(Float())
    year_low = Column(Float())

    def __init__(self, symbol, time, price, change, pct_change, volume, avg_volume, name, exchange, market_cap,
                 day_high, day_low, year_high, year_low):
        try:
            self.symbol = symbol
            self.time = time
            self.price = price
            self.change = change
            self.pct_change = pct_change
            self.volume = volume
            self.avg_volume = avg_volume
            self.name = name
            self.exchange = exchange
            self.market_cap = market_cap
            self.day_high = day_high
            self.day_low = day_low
            self.year_high = year_high
            self.year_low = year_low
        except Exception as e:
            raise e.with_traceback(e.__traceback__)


class EquityHP1d(Base):
    __tablename__ = 'EquityHP1d'

    symbol = Column(String(collation='utf8'), primary_key=True)
    date = Column(Date(), primary_key=True)
    opn = Column(Float())
    high = Column(Float())
    low = Column(Float())
    close = Column(Float())
    volume = Column(Float())

    def __init__(self, symbol, date : datetime.date, opn, high, low, close, volume,
                 unadj_opn, unadj_high, unadj_low, unadj_close):
        try:
            self.symbol = symbol
            self.date = date
            self.opn = opn
            self.high = high
            self.low = low
            self.close = close
            self.volume = volume
        except Exception as e:
            raise e.with_traceback(e.__traceback__)


class Position(Base):
    __tablename__ = 'Position'

    symbol = Column(String(collation='utf8'), primary_key=True)
    date = Column(Date(), primary_key=True)
    share = Column(Float())
    price = Column(Float())
    value = Column(Float())
    cost = Column(Float())
    pct_ret = Column(Float())
    abs_ret = Column(Float())

    def __init__(self, symbol, date : datetime.date, share, price, value, cost, pct_ret, abs_ret):
        try:
            self.symbol = symbol
            self.date = date
            self.share = share
            self.value = value
            self.price = price
            self.cost = cost
            self.pct_ret = pct_ret
            self.abs_ret = abs_ret
        except Exception as e:
            raise e.with_traceback(e.__traceback__)


class Trade(Base):
    __tablename__ = 'Trade'

    symbol = Column(String(collation='utf8'), primary_key=True)
    date = Column(Date(), primary_key=True)
    share = Column(Float())
    price = Column(Float())

    def __init__(self, symbol, date : datetime.date, share, price):
        try:
            self.symbol = symbol
            self.date = date
            self.share = share
            self.price = price
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

def orm_to_nparr(obj : Base):
    try:
        d = {}
        for column in obj.__table__.columns:
            d[column.name] = getattr(obj, column.name)
        return d
    except Exception as e:
        raise e.with_traceback(e.__traceback__)

if __name__ == '__main__':
    import Data.DB.DBManager

    dm = Data.DB.DBManager.DBManager()
    pos = dm.query(Position, {('symbol','='):'USDCASH'}, True)
    print(pos)
    print(orm_to_nparr(pos))