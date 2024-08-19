from pydantic import Field

from datetime import datetime
from typing import Optional, List, Any

from common.schema.base_schemas import BaseModel, BaseFilterSchema
from service.lesson.schemas.lesson_schemas import LessonSchemaForTable


class TrainingCheck(BaseModel):
    """ Схема оценки выполнения упражнения """
    training_id: int
    repetitions: int = Field(ge=1)
    assessment: Optional[int] = Field(default=None, le=10, ge=1)


class CreateCheckSchema(BaseModel):
    """ Схема создания моделей занятий """
    # id: int
    students_id: list[int]
    lesson_id: int
    training_check: list[TrainingCheck]
    date_add: datetime = Field(default_factory=datetime.now, hidden=True)
    date_update: datetime = Field(default_factory=datetime.now, hidden=True)


class EditCheckSchema(BaseModel):
    """Схема редактирования моделей занятий"""
    id: int
    student_id: int
    lesson_id: int
    training_check: list[TrainingCheck]
    date_update: datetime = Field(default_factory=datetime.now, hidden=True)


#
# class DeleteCheckSchema(BaseModel):
#     """Схема удаление моделей занятий"""
#     check_id: int
#
#
# class CheckIdSchema(DeleteCheckSchema):
#     """ Схема получения моделей занятий """
#     pass


class CheckFilterSchema(BaseFilterSchema):
    """ Схема фильтров для чек-листа """
    date_add: Optional[datetime] = Field(default=None)
    trainer: Optional[int] = Field(default=None)
    student: Optional[int] = Field(default=None)


class TrainingCheckShortSchema(BaseModel):
    training_id: int
    repetitions: int
    assessment: int


class LessonShortSchema(BaseModel):
    trainer_id: int
    space_id: int
    trainer_comments: str
    start: datetime
    date_add: datetime
    date_update: datetime


class CheckSchemaForTable(BaseModel):
    """ Схема деталей чек-листа """
    id: int
    student_id: int
    # lesson: LessonSchemaForTable
    lesson: LessonShortSchema
    date_add: datetime
    date_update: datetime
    # training_data: TrainingCheckShortSchema


class CheckViewSchemaByFilters(BaseModel):
    """ Постраничный вывод чек-листов по фильтрам """
    page: int
    max_page_count: int
    count_records: int
    records: List[CheckSchemaForTable]

# class EditLessonSchema(BaseModel):
#     """ Схема изменения моделей занятий """
#     id: int
#     space_id: int
#     trainer_id: int
#     trainer_comments: Optional[str]
#     start: datetime
#
#
# class TrainerShortSchema(BaseModel):
#     id: int
#     firstname: Optional[str] = None
#     lastname: Optional[str] = None
#     surname: Optional[str] = None
#
#
# class LessonSchemaForTable(BaseModel):
#     """ Схема деталей занятия """
#     id: int
#     space: SpaceSchemaForTable
#     trainer: TrainerShortSchema
#     trainer_comments: Optional[str]
#     start: datetime
#
#
# class LessonViewSchemaForPage(BaseModel):
#     """ Помтраничный вывод деталей моделей тренировок """
#     page: int
#     max_page_count: int
#     count_records: int
#     records: List[LessonSchemaForTable]
#
#
# class LessonFilterSchema(BaseFilterSchema):
#     """ Фильтрация и пагинация """
#     date_begin: datetime | None = Query(default=None, description="Дата начала занятия")
#     trainer: int | None = Query(default=None, description="Тренер")
