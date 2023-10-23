from sqlalchemy import ForeignKey, JSON, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ARRAY
from typing import List, Optional
import time


class Base(DeclarativeBase):
    pass


class Entity(Base):
    """
    Object representing organization or owner of TOR operation.
    Entity can own many Domains.
    """
    __tablename__ = 'entities'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False, index=True, unique=True)
    name: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    description: Mapped[Optional[str]]
    extra_data: Mapped[Optional[str]] = mapped_column(JSON)
    contact_info: Mapped[Optional[str]]
    domains: Mapped[Optional[List['Domain']]] = relationship(back_populates='entity')

    def __repr__(self):
        return self.name


class Domain(Base):
    """
    Object representing a single unique TOR Domain.
    """
    __tablename__ = 'domains'

    entity_id: Mapped[Optional[int]] = mapped_column(ForeignKey('entities.id'), nullable=True)
    entity: Mapped[Optional['Entity']] = relationship(back_populates='domains')

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False, index=True, unique=True)
    name: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    created: Mapped[int] = mapped_column(default=int(time.time()))
    last_crawl_date: Mapped[Optional[int]]
    average_crawl_time: Mapped[Optional[int]]
    server: Mapped[Optional[str]]
    description: Mapped[Optional[str]]
    extra_data: Mapped[Optional[str]] = mapped_column(JSON)
    number_of_finished_crawls: Mapped[int] = mapped_column(default=0)
    number_of_webpages: Mapped[int] = mapped_column(default=0)
    site_structure: Mapped[Optional[str]] = mapped_column(JSON)

    def __repr__(self):
        return self.name


class Webpage(Base):
    """
    Object representing a single webpage(url) found while crawling TOR Domain.
    """
    __tablename__ = 'webpages'

    domain_id: Mapped[int] = mapped_column(ForeignKey('domains.id'), nullable=False)
    domain: Mapped['Domain'] = relationship(back_populates='webpages')

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False, index=True, unique=True)
    url: Mapped[str] = mapped_column(unique=True, index=True)
    url_after_request: Mapped[Optional[str]]
    last_http_status: Mapped[Optional[str]]
    average_response_time: Mapped[Optional[float]]
    html: Mapped[Optional[str]]
    page_title: Mapped[Optional[str]]
    meta_title: Mapped[Optional[str]]
    meta_description: Mapped[Optional[str]]
    on_page_urls = mapped_column(ARRAY(String), nullable=True)
    on_page_processed_urls = mapped_column(ARRAY(String), nullable=True)
    extra_data: Mapped[Optional[str]] = mapped_column(JSON)
    number_of_successful_requests: Mapped[int] = mapped_column(default=0)
    number_of_unsuccessful_requests: Mapped[int] = mapped_column(default=0)
    is_active: Mapped[bool] = mapped_column(default=False)
    created: Mapped[int] = mapped_column(default=int(time.time()))
    last_visit: Mapped[Optional[int]]

    def __repr__(self):
        return self.url
