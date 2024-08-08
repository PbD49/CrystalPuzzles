from typing import Optional

from sqlalchemy import insert

from common.repository.base_repository import BaseRepository, TModel
from service.lesson.models import Check, Lesson
from service.lesson.schemas.check_schema import CheckFilterSchema
from sqlalchemy import select
from sqlalchemy.orm import joinedload


class CheckRepository(BaseRepository):
    model = Check

    async def add(self, data: dict):
        stmt = insert(self.model).values(**data).returning(self.model.id)
        result = (await self.session.execute(stmt)).scalar_one_or_none()
        return result

    async def get_all_check_by_filter(self, filters: CheckFilterSchema) -> dict:
        stmt = (
            select(self.model)
            .options(joinedload(self.model.training_data))
            .options(joinedload(self.model.lesson))
            .filter(self.model.deleted.__eq__(False))
        )
        if filters.date_add:
            stmt = stmt.filter(self.model.date_add == filters.date_add.date())
        if filters.trainer:
            stmt = stmt.filter(self.model.lesson.has(Lesson.trainer_id == filters.trainer))
        if filters.student:
            stmt = await self._add_filters(stmt, student_id=filters.student)

        count_records = await self._get_count_records(stmt)
        records = await self._get_records(count_records, stmt, filters)
        response = await self._convert_response(count_records, records, filters)
        return response

    async def get(self, check_id: int) -> Optional[TModel]:
        stmt = (
            select(self.model)
            .filter(
                self.model.id == check_id,
                self.model.deleted.__eq__(False))
            .options(
                joinedload(self.model.lesson)
            )
        )
        result = (await self.session.execute(stmt)).scalar_one_or_none()
        return result
