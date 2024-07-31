from common.service.base_service import BaseService
from service.lesson.schemas.check_schema import CreateCheckSchema, EditCheckSchema, CheckFilterSchema
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

    @staticmethod
    async def get_all_by_filters(uow: CheckUOW, filters: CheckFilterSchema):
        async with uow:
            result = await uow.repo.get_all_check_by_filter(filters)
            return result
