from typing import Optional

from fastapi import Depends
from sqlalchemy.orm import Session

from spells.models import Spell
from spells.views import get_db


def get_spells(name_filter: Optional[str] = None,
                    sources: Optional[list[str]] = None,
                    description_filter: Optional[str] = None,
                    casting_time_filter: Optional[str] = None,
                    spell_resistance_filter: Optional[str] = None,
                    casting_range_filter: Optional[str] = None,
                    target_filter: Optional[str] = None,
                    saving_throw_filter: Optional[str] = None,
                    material_components: Optional[list[str]] = None,
                    duration_filter: Optional[str] = None,
                    class_levels: Optional[list[str]] = None, db_session: Session = Depends(get_db)) -> list[Spell]:
    list_of_spells = None
    return list_of_spells