from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.infrastructure.database.base import Base


class AddressModel(Base):
    __tablename__ = "addresses"

    id_address = Column(Integer, primary_key=True, autoincrement=True)
    id_company = Column(
        Integer,
        ForeignKey(
            "companies.id_company",
            name="fk_addresses_companies",
            ondelete="CASCADE",
        ),
        nullable=False,
        unique=True,
    )
    country = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    address = Column(String(255), nullable=False)

    company = relationship("CompanyModel", back_populates="address")
