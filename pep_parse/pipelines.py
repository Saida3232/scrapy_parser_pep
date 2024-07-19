from pathlib import Path

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from pep_parse.utils import add_count, status_pep, file_output

Base = declarative_base()
BASE_DIR = Path(__file__).parent.parent


class Pep(Base):
    __tablename__ = 'pep'
    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    name = Column(String(400))
    status = Column(String(2))


class PepParsePipeline:
    def open_spider(self, spider):
        engine = create_engine('sqlite:///sqlite_pep.db')
        Base.metadata.create_all(engine)
        self.session = Session(engine)
        self.results = []

    def process_item(self, item, spider):
        pep = Pep(
            number=item['number'],
            name=item['name'],
            status=item['status']
        )
        short_status = status_pep(item['status'])
        self.results.append(short_status)
        try:
            existing_pep = self.session.query(
                Pep).filter_by(name=item['name']).one()
            if existing_pep.status != pep.status:
                existing_pep.status = pep.status
        except NoResultFound:
            self.session.add(pep)

        self.session.commit()
        return item

    def close_spider(self, spider):
        pep_results = add_count(self.results)
        file_output(pep_results, BASE_DIR)
        self.session.close()
