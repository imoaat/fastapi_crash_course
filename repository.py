# Продвинутый паттерн "репозиторий", который позволяет работать с БД как с коллекцией объектов
from sqlalchemy import select

from database import new_session, TaskOrm
from schemas import STaskAdd, STask


class TaskRepository():
    @classmethod
    async def add_task(cls, task: STaskAdd):
        async with new_session() as session:
            task_dict = task.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id


    @classmethod
    async def get_tasks(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STask.model_validate(task_model) for task_model in task_models]
            return task_schemas
