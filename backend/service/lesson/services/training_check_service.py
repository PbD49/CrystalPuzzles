# from core.service import BaseService
from common.service.base_service import BaseService
from service.group.schemas import CreateGroupSchema, EditGroupSchema, GroupFilterSchema
from service.lesson.repositories.training_check_repository import TrainingCheckRepository
from service.lesson.schemas.check_schema import ExerciseTrainingCheckSchema
from service.lesson.unit_of_work.training_check_uow import TrainingCheckUow


class TrainingCheckService(BaseService):
    @staticmethod
    async def create_exercise(uow: TrainingCheckUow, model: ExerciseTrainingCheckSchema):
        data = model.model_dump()
        async with uow:
            result = await uow.repo.add_exercise(data)
            return result

    @staticmethod
    async def delete_exercise(uow: TrainingCheckUow, check_id: int, training_id: int):
        async with uow:
            result = await uow.repo.delete_exercise(check_id, training_id)
            return result
