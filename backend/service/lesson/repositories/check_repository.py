from sqlalchemy import insert

from common.repository.base_repository import BaseRepository
from service.lesson.models import Check
from service.lesson.schemas.check_schema import CheckFilterSchema
from sqlalchemy import select, or_
from sqlalchemy.orm import joinedload


class CheckRepository(BaseRepository):
    model = Check

    async def add(self, data: dict):
        stmt = insert(self.model).values(**data).returning(self.model.id)
        result = (await self.session.execute(stmt)).scalar_one_or_none()
        return result

    async def get_all_check_by_filter(self, filters: CheckFilterSchema):
        stmt = (
            select(self.model)
            .options(joinedload(self.model.lesson))
            .options(joinedload(self.model.training_data))
            .filter(self.model.deleted.__eq__(False))
        )
        if filters.date_add:
            stmt = stmt.filter(self.model.date_add == filters.date_add.date())
        if filters.trainer:
            stmt = await self._add_filters(stmt, lesson=filters.trainer)
        if filters.student:
            stmt = await self._add_filters(stmt, student_id=filters.student)

        count_records = await self._get_count_records(stmt)
        records = await self._get_records(count_records, stmt, filters)
        response = await self._convert_response(count_records, records, filters)
        return response
