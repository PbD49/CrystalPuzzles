from typing import Union
from uuid import UUID

from sqlalchemy.dialects.mysql import insert

from common.repository.base_repository import BaseRepository, EditData
from service.lesson.models import TrainingCheck
from sqlalchemy import update, insert, select


class TrainingCheckRepository(BaseRepository):
    model = TrainingCheck

    async def edit(self, data: EditData) -> bool:
        """Изменить данные в БД."""
        data_id: Union[int, UUID] = data.pop("id")
        training_check_data = data.pop("training_check")[0]
        stmt = (update(self.model)
                .filter(
            self.model.check_id == data_id)
                .values(**training_check_data)
                .returning(self.model.check_id))
        res = (await self.session.execute(stmt)).scalar_one_or_none()
        await self.session.commit()
        return bool(res)



    async def add_exercise(self, data):
        check_id = data["check_id"]
        training_id = data["training_id"]
        print(data)
        stmt = select(self.model.check_id).filter(self.model.check_id == check_id,
                                                   self.model.training_id == training_id)
        exercise_check_id = (await self.session.execute(stmt)).scalar_one_or_none()
        if exercise_check_id:
            return
        stmt = (insert(self.model).values(**data)
                .returning(self.model.check_id))
        res = (await self.session.execute(stmt)).scalar_one_or_none()
        await self.session.commit()
        return bool(res)
