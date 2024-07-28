from http import HTTPStatus

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response
from starlette.responses import JSONResponse

from common.dependensies import TrainerSupervisorAdminDep
from common.schema.base_schemas import Message
from core.logger import logger
from service.lesson.dependensies import CheckUOWDep, CheckServiceDep
from service.users.models import User
from service.users.repository import UserRepository

from service.identity.security import get_current_user
from service.lesson.repositories.lesson_repository import LessonRepository
from service.lesson.schemas.check_schema import CreateCheckSchema, EditCheckSchema, DeleteCheckSchema, ListCheckSchema

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


@check_router.put("/",
            summary="Редактирование Чек-листа",
            response_model=int,
            responses={
                      200: {"description": "Успешная обработка данных"},
                      401: {"description": "Не авторизованный пользователь"},
                      400: {"model": Message, "description": "Некорректные данные"},
                      500: {"model": Message, "description": "Серверная ошибка"}},
)
async def edit_check(
        model: EditCheckSchema,
        uow: CheckUOWDep,
        check_service: CheckServiceDep,
        current_user: TrainerSupervisorAdminDep
):
    """admin, supervisor, trainer"""
    result = await check_service.edit(uow, model)
    if result:
        return result
    return JSONResponse(status_code=HTTPStatus.CONFLICT.value, content="Check existing")


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
        model: DeleteCheckSchema,
        uow: CheckUOWDep,
        check_service: CheckServiceDep,
        current_user: TrainerSupervisorAdminDep
):
    """admin, supervisor, trainer"""
    result = await check_service.delete_db(uow, model)
    if result:
        return result
    return JSONResponse(status_code=HTTPStatus.CONFLICT.value, content="Check existing")


@check_router.get("/{check_id}",
            summary="Удаление Чек-листа",
            response_model=int,
            responses={
                      200: {"description": "Успешная обработка данных"},
                      401: {"description": "Не авторизованный пользователь"},
                      400: {"model": Message, "description": "Некорректные данные"},
                      500: {"model": Message, "description": "Серверная ошибка"}},
)
async def list_check(
        model: ListCheckSchema,
        uow: CheckUOWDep,
        check_service: CheckServiceDep,
        current_user: TrainerSupervisorAdminDep
):
    """admin, supervisor, trainer"""
    result = await check_service.get(uow, model)
    if result:
        return result
    return JSONResponse(status_code=HTTPStatus.CONFLICT.value, content="Check existing")


