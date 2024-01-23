from datetime import datetime, date
from typing import Optional

import sqlalchemy as sa
import sqlalchemy.orm as so

from app import db


class Day(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    date: so.Mapped[date] = so.mapped_column(
        sa.Date(), index=True, default=date.today()
    )

    def __repr__(self):
        return "<Day {}>".format(self.date)


class Category(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    label: so.Mapped[str] = so.mapped_column(sa.String(128))

    def __repr__(self):
        return "<Category {}>".format(self.label)


class Status(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    status: so.Mapped[str] = so.mapped_column(sa.String(128))

    def __repr__(self):
        return "<Status {}>".format(self.status)


class Block(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    date: so.Mapped[date] = so.mapped_column(sa.ForeignKey(Day.date), index=True)
    start_time: so.Mapped[datetime] = so.mapped_column(sa.DateTime)
    end_time: so.Mapped[datetime] = so.mapped_column(sa.DateTime)
    task: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    category_id: so.Mapped[Optional[int]] = so.mapped_column(
        sa.ForeignKey(Category.id), index=True
    )
    status_id: so.Mapped[Optional[int]] = so.mapped_column(
        sa.ForeignKey(Status.id), index=True
    )

    def __repr__(self):
        return "<Block {} start {} end {}>".format(
            self.date,
            self.start_time.strftime("%H:%M"),
            self.end_time.strftime("%H:%M"),
        )
