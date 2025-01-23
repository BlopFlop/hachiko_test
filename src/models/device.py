from sqlalchemy import BigInteger, Boolean, CheckConstraint, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from core.db import Base

from datetime import date


class Device(Base):
    """Device model."""
    deviceName: Mapped[str]
    imei: Mapped[str]
    estPurchaseDate: Mapped[date]
    simLock: Mapped[bool]
    warrantyStatus: Mapped[str]
    repairCoverage: Mapped[bool]
    technicalSupport: Mapped[bool]
    modelDesc: Mapped[str]
    demoUnit: Mapped[bool]
    refurbished: Mapped[bool]
    purchaseCountry: Mapped[str]
    region: Mapped[str]
    fmiOn: Mapped[bool]
    lostMode: Mapped[bool]
    usaBlockStatus: Mapped[str]
    network: Mapped[str]

    device_name: Mapped[str] = mapped_column()
    model_description: Mapped[str] = mapped_column()
    purchase_date: Mapped[date] = mapped_column()
    country: Mapped[str] = mapped_column()
    usa_block_status: Mapped[str]
    network: Mapped[str]
    imei_number: Mapped[int] = mapped_column()
    serial_number: Mapped[int] = mapped_column()
    meid_number: Mapped[int] = mapped_column()
    replacement: Mapped[bool] = mapped_column()
    demo_unit: Mapped[bool] = mapped_column()
    refurbished: Mapped[bool] = mapped_column()
    sim_lock: Mapped[bool] = mapped_column()
    fmi_enabled: Mapped[bool] = mapped_column()
    replaced: Mapped[bool] = mapped_column()
    warranty_status: Mapped[bool] = mapped_column()
    repair_coverage: Mapped[bool]
    technical_support: Mapped[bool] 
    model_name: Mapped[str]
    loaner: Mapped[bool]
    lost: Mapped[bool]

    name: Mapped[str] = mapped_column(
        String(250),
        CheckConstraint("LENGTH(name) <= 250", name="check_len_name"),
        unique=True,
        nullable=False,
        comment=(
            "Уникальное название товара, обязательное строковое поле;"
            " допустимая длина строки — от 1 до 250 символов включительно;"
        ),
    )
    article: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        nullable=False,
        comment="Артикул товара в магазине, целочисленное уникальное значение.",
    )
    price: Mapped[float] = mapped_column(
        Float,
        CheckConstraint("price > 0", name="check_price_positive"),
        unique=False,
        nullable=False,
        comment="Цена товара, положительное число с плавающей запятой.",
    )
    rating: Mapped[Float] = mapped_column(
        Float,
        CheckConstraint("0 <= rating <= 5", name="check_rating"),
        unique=False,
        nullable=False,
        comment=(
            "Рейтинг товара, число с плавающей запятой от 0 до 5 включительно."
        ),
    )
    total: Mapped[int] = mapped_column(
        BigInteger,
        unique=False,
        nullable=False,
        comment="Количесво товара на всех складах.",
    )
    perform_update: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=True,
        comment="Обновлять ли товар при запуске, или по времени.",
    )

    def __repr__(self) -> str:
        return f"Product: Articul {self.article} Total {self.total}"
