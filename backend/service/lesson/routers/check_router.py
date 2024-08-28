from http import HTTPStatus

from fastapi import APIRouter
from starlette.responses import JSONResponse

from common.dependensies import TrainerSupervisorAdminDep
from common.schema.base_schemas import Message
from service.lesson.dependensies import CheckUOWDep, CheckServiceDep, CheckFilterDep, TrainingCheckUOWDep
from service.lesson.schemas.check_schema import CreateCheckSchema, PatchCheckSchema, CheckViewSchemaByFilters, CheckSchemaForTable

check_router = APIRouter(
    prefix="/api/v1/check",
    tags=["Check"]
)


@check_router.post(
    "/",
    summary="Создание Чек-листа",
    response_model=int,
    responses={
        200: {"description": "Успешная обработка данных"},
        401: {"description": "Не авторизованный пользователь"},
        400: {"model": Message, "description": "Некорректные данные"},
        500: {"model": Message, "description": "Серверная ошибка"}},
)
async def create_check(
        model: CreateCheckSchema,
        uow: CheckUOWDep,
        check_service: CheckServiceDep,
        current_user: TrainerSupervisorAdminDep
):
    """admin, supervisor, trainer"""
    result = await check_service.add(uow, model)
    if result:
        return result
    return JSONResponse(status_code=HTTPStatus.CONFLICT.value, content="Check existing")


@check_router.patch("/{check_id}",
                  summary="Редактирование Чек-листа",
                  response_model=int,
                  responses={
                      200: {"description": "Успешная обработка данных"},
                      401: {"description": "Не авторизованный пользователь"},
                      400: {"model": Message, "description": "Некорректные данные"},
                      500: {"model": Message, "description": "Серверная ошибка"}},
                  )
async def edit_check(
        check_id: int,
        model: PatchCheckSchema,
        uow: TrainingCheckUOWDep,
        check_service: CheckServiceDep,
        current_user: TrainerSupervisorAdminDep,

):
    """admin, supervisor, trainer"""
    result = await check_service.patch_check(uow, model, check_id)
    if result:
        return result
    return JSONResponse(status_code=HTTPStatus.CONFLICT.value, content="Check not found")


@check_router.delete("/remove/",
                     summary="Удаление Чек-листа",
                     response_model=int,
                     responses={
                         200: {"description": "Успешная обработка данных"},
                         401: {"description": "Не авторизованный пользователь"},
                         400: {"model": Message, "description": "Некорректные данные"},
                         500: {"model": Message, "description": "Серверная ошибка"}},
                     )
async def delete_check(
        check_id: int,
        uow: CheckUOWDep,
        check_service: CheckServiceDep,
        current_user: TrainerSupervisorAdminDep
):
    """admin, supervisor, trainer"""
    result = await check_service.delete(uow, check_id)
    if result:
        return result
    return JSONResponse(status_code=HTTPStatus.CONFLICT.value, content="Check not found")


@check_router.get("/{check_id}",
                  summary="Вывод Чек-листа по ID",
                  response_model=CheckSchemaForTable,
                  responses={
                      200: {"description": "Успешная обработка данных"},
                      401: {"description": "Не авторизованный пользователь"},
                      400: {"model": Message, "description": "Некорректные данные"},
                      500: {"model": Message, "description": "Серверная ошибка"}},
                  )
async def list_check(
        check_id: int,
        uow: CheckUOWDep,
        check_service: CheckServiceDep,
        current_user: TrainerSupervisorAdminDep
):
    """admin, supervisor, trainer"""
    result = await check_service.get(uow, check_id)
    if result:
        return result
    return JSONResponse(status_code=HTTPStatus.CONFLICT.value, content="Check not found")


@check_router.get("/all_checks/",
                  summary="Вывод всех Чек-листов",
                  response_model=CheckViewSchemaByFilters,
                  responses={
                      200: {"description": "Успешная обработка данных"},
                      401: {"description": "Не авторизованный пользователь"},
                      400: {"model": Message, "description": "Некорректные данные"},
                      500: {"model": Message, "description": "Серверная ошибка"}},
                  )
async def list_check(
        uow: CheckUOWDep,
        check_service: CheckServiceDep,
        current_user: TrainerSupervisorAdminDep,
        filters: CheckFilterDep
):
    """admin, supervisor, trainer"""
    result = await check_service.get_all_by_filters(uow, filters)
    if result:
        return result
    return JSONResponse(status_code=HTTPStatus.CONFLICT.value, content="Check not found")
