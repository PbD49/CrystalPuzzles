from typing import Union
from uuid import UUID

from common.repository.base_repository import BaseRepository, EditData
from service.lesson.models import TrainingCheck
from sqlalchemy import update


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

