from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from model.objects.Base import Base

Base = Base().base


# noinspection PyClassHasNoInit
class Repository(Base):
    __tablename__ = 'repository'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    url = Column(String(200))
    issueTracking = relationship("IssueTracking", uselist=False, back_populates="repository")
    commits = relationship("Commit")
    files = relationship("File")
