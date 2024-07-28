from common.service.base_service import BaseService
from service.lesson.schemas.check_schema import CreateCheckSchema, EditCheckSchema
from service.lesson.unit_of_work.check_uow import CheckUOW


class CheckService(BaseService):
    async def create_check(self, uow: CheckUOW, model: CreateCheckSchema):
        data = model.model_dump()
        result = await super().add(uow, data)
        return result

    async def edit_check(self, uow: CheckUOW, model: EditCheckSchema):
        data = model.model_dump()
        result = await  super().edit(uow, data)
        return result
